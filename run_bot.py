from clothing import aritzia
from skincare import faceshop

sale_sweaters = aritzia.get_sale_items('sweater')
for item, url in sale_sweaters.iteritems():
    print item, url


faceshop_promotions = faceshop.get_promotions('home')
for item, url in faceshop_promotions.iteritems():
    print item, url