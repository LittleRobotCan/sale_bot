from retailers.aritzia import *

sale_sweaters = get_sale_items('sweater')
for item, url in sale_sweaters.iteritems():
    print item, url