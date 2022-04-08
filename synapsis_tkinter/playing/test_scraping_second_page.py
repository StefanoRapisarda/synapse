import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from twisted.internet import reactor

class TestSpider(scrapy.Spider):
    
    name = 'test_spider'

    def __init__(self, *args, **kwargs):
	    super(TestSpider, self).__init__(*args, **kwargs)
	    self.start_urls = [kwargs.get('start_url')]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse_info)
            
    def parse_info(self,response):
        print('I am in parse_info')
        to_read = '//h2[@class="s-article-title"]/@text'
        #to_read = "h2.s-article-title ::text"

        info = response.css(to_read).extract()
       
info = 'niente'

url = 'https://ui.adsabs.harvard.edu/abs/2014PASP..126..838W/references'
process = CrawlerProcess()
process.crawl(TestSpider,start_url=url)
process.start()

print('info',info)