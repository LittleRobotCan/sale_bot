import urllib2, re

response = urllib2.urlopen("http://www.aritzia.com/en/clothing/sweaters?lastViewed=1000")
page_source = response.read()
page_source = re.split('\\\n', page_source)
page_source = [line for line in page_source if len(line)>0]

sale = []
for i in range(len(page_source)):
    line = page_source[i]
    if re.search('product-standard-price', line) is not None:
        neighbor = page_source[(i-15):i]
        for row in neighbor:
            if re.search('http://www.aritzia', row) is not None:
                sale.append(row)

sale = list(set(sale))

old_sale = sale
for i in sale:
    if i not in old_sale:
        print i


import yaml

with open("config.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
stream.close()
