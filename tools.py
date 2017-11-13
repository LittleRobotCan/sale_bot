import yaml, urllib2, re


def get_link(category, retailer):
    with open("config.yaml", 'r') as stream:
        try:
            content = yaml.load(stream)
            link = content['clothing'][category][retailer]
        except yaml.YAMLError as exc:
            print(exc)
    stream.close()
    return link


def get_page_source(url):
    response = urllib2.urlopen("http://www.aritzia.com/en/clothing/sweaters?lastViewed=1000")
    page_source = response.read()
    page_source = re.split('\\\n', page_source)
    page_source = [line for line in page_source if len(line)>0]
    return page_source