import yaml, urllib2, re


def get_link(level0, level1, level2):
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