import requests
from scrapy import Selector

url = 'https://ui.adsabs.harvard.edu/abs/2020ApJ...898...38B/abstract'

html = requests.get(url).content

sel = Selector(text=html)
css_expr = 'div#article-publication ::text'
title = sel.css(css_expr).extract()
#' '.join(title)
#title = title[0].strip()
print(title)