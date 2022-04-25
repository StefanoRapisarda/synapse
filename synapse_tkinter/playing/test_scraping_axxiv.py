import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from twisted.internet import reactor
from scrapy_selenium import SeleniumRequest

class TestSpider(scrapy.Spider):
    
    name = 'test_spider'

    def __init__(self, *args, **kwargs):
	    super(TestSpider, self).__init__(*args, **kwargs)
	    self.start_urls = [kwargs.get('start_url')]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse_info)
            
    def parse_info(self,response):
        to_read = {'title':'h2.s-abstract-title ::text',
                   'authors':'div#authors-and-aff.s-authors-and-aff ::text',
                   'abstract':'div.s-abstract-text > p ::text',
                   'publication':'div#article-publication ::text',
                   'date':'dl.s-abstract-dl-horizontal > dd:nth-of-type(2) ::text',
                   'keywords':'dl.s-abstract-dl-horizontal > dd:nth-of-type(6) ::text',
                   'comments':'dl.s-abstract-dl-horizontal > dd:nth-of-type(7) ::text'}

        for key,item in to_read.items():
            text = response.css(item).extract()
            cleaned_text = [t.strip() for t in text if t.strip() != '' and t.strip() != ';']
            if isinstance(cleaned_text,list) and len(cleaned_text) == 1:
                cleaned_text = cleaned_text[0]
            if key == 'keywords':
                for i in range(len(cleaned_text)):
                    cleaned_text[i]=cleaned_text[i].replace(';','')    
            info[key] = cleaned_text

        xpath_references = '//a[@data-widget-id="ShowReferences"]/@href'
        link = response.xpath(xpath_references).get()
        if not link is None:
            link = response.urljoin(link)
            print(link)
            yield scrapy.Request(url=link,callback=self.parse_ref)
        else:
            print('Reference link is None!!!')

    def parse_ref(self,response):
        with open('test.html','wb') as outfile:
            outfile.write(response.body)
        css_line = 'h3.s-results-title:nth-of-type(1) ::text'
        test = response.css(css_line).get()
        info['test'] = test
       
info = {}

url = 'https://ui.adsabs.harvard.edu/abs/2014PASP..126..838W/abstract'
process = CrawlerProcess(Settings())
process.crawl(TestSpider,start_url=url)
process.start()

for key,item in info.items():
    print('{:>10}: {}'.format(key,item))

