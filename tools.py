import yaml, urllib2, re, requests


def read_config(level0, level1, level2):
    with open("config.yaml", 'r') as stream:
        try:
            content = yaml.load(stream)
            link = content[level0][level1][level2]
        except yaml.YAMLError as exc:
            print(exc)
    stream.close()
    return link


def get_page_source(url):
    response = urllib2.urlopen(url)
    page_source = response.read()
    page_source = re.split('\\\n', page_source)
    page_source = [line for line in page_source if len(line)>0]
    return page_source


def access_page_search(url, keywords):
    search_results = requests.get(url + keywords).text
    results_parsed = re.split('\\\n', search_results)
    results_parsed = [line for line in results_parsed if len(line)>0]
    return results_parsed


def find_tag_in_source(source_line, tag_type_list, AND=True):
    html_tags = {"hyperlink": "a href","title":"title"}
    if AND:
        for tag_type in tag_type_list:
            tag_regex = r'\b'+html_tags[tag_type]+r'\b'
            if re.search(tag_regex, source_line) is None:
                return False
        return True
    else:
        for tag_type in tag_type_list:
            tag_regex = r'\b'+html_tags[tag_type]+r'\b'
            if re.search(tag_regex, source_line) is not None:
                return True
            else:
                return False