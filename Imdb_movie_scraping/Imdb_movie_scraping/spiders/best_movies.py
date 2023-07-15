import scrapy
from pymongo import MongoClient
import scrapy_user_agents
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

client = MongoClient(
    'Db URI')
db = client['Imdb_movies_rating']
collection = db['Top_movies']


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?languages=hi&title_type=feature&num_votes=10000,&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="lister-item-header"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='(//a[@class="lister-page-next next-page"])[2]'))
    )

    def parse_item(self, response):
        item = {
            'Tittle': response.xpath('//h1/span[@class="sc-afe43def-1 fDTGTb"]/text()').get(),
            'Year': response.xpath('(//li/a[@class="ipc-link ipc-link--baseAlt ipc-link--inherit-color"])[4]/text()').get(),
            'Duration': response.xpath('((//li[@class="ipc-inline-list__item"])[5] | (//li[@class="ipc-inline-list__item"])[6])/text()').get(),
            'Rating': response.xpath('(//div/span[@class="sc-bde20123-1 iZlgcd"])[1]/text()').get(),
            'Storyline': response.xpath('//span[@class="sc-6a7933c5-2 dPFGVH"]/text()').get(),
            'Movies_url':response.url,
        }
        collection.insert_one(dict(item))


        
        
