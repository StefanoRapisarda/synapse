import scrapy

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger

import time

class AdsSpider(scrapy.Spider):
    # Initializing log file
    logfile('openq_spider.log', maxBytes=1e6, backupCount=4)

    name = 'ads_spider'

    def __init__(self,*args,**kwargs):
        self.url = kwargs.get('start_url')
        self.info = kwargs.get('info_dict')
    
    def start_requests(self):
        dummy_url = 'https://ui.adsabs.harvard.edu/'
        yield scrapy.Request(url=dummy_url, callback=self.parse_paper_info)

    def parse_paper_info(self,response):

        # driver = webdriver.Chrome() # To open a new browser window

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

        driver.get(self.url)
        driver.implicitly_wait(5)

        # Getting paper information
        self.info['title'] = driver.find_element_by_class_name('s-abstract-title').text
        self.info['authors'] = driver.find_element_by_class_name('s-authors-and-aff').text
        self.info['abstract'] = driver.find_element_by_class_name('s-abstract-text').text
        self.info['publication'] = driver.find_element_by_id('article-publication').text
        self.info['date'] = driver.find_element_by_css_selector('dl.s-abstract-dl-horizontal > dd:nth-of-type(2)').text
        element = driver.find_element_by_css_selector('dl.s-abstract-dl-horizontal > dd:nth-of-type(4) > span > a')
        self.info['arxiv_link'] = element.get_attribute('href')
        self.info['keywords'] = driver.find_element_by_css_selector('dl.s-abstract-dl-horizontal > dd:nth-of-type(6)').text
        self.info['comments'] = driver.find_element_by_css_selector('dl.s-abstract-dl-horizontal > dd:nth-of-type(7)').text

        # Going to references
        element = driver.find_element_by_xpath("//a[@data-widget-id='ShowReferences']")
        #link = element.get_attribute('href')
        element.click()
        time.sleep(2)

        references = {}
        elements = driver.find_elements_by_class_name('abs-redirect-link')
        references['bib_code'] = [e.text for e in elements]
        elements = driver.find_elements_by_class_name('abs-redirect-link')
        references['ads_link'] = [e.get_attribute('href') for e in elements]
        elements = driver.find_elements_by_xpath('//div[@aria-label="date published"]')
        references['date'] = [e.text for e in elements]
        elements = driver.find_elements_by_class_name('s-results-title')
        references['title'] = [e.text for e in elements]
        elements = driver.find_elements_by_class_name('s-results-authors')
        references['authors'] = [e.text for e in elements]
        self.info['references'] = references

info = {}
url = 'https://ui.adsabs.harvard.edu/abs/2014PASP..126..838W/abstract'
process = CrawlerProcess(Settings())
process.crawl(AdsSpider,start_url=url, info_dict=info)
process.start()

for key,item in info.items():
    if isinstance(item,dict):
        print('{:>10} =============='.format(key))
        for i,j in item.items():
            if len(j) != 0:
                print('{:>10}: {} ({})'.format(i,j[0],type(j[0])))
            else:
                print('{:>10}: {}'.format(i,None))
    else:
        print('{:>10}: {} ({})'.format(key,item,type(item)))
