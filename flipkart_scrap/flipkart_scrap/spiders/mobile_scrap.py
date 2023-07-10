import scrapy


class MobileScrapSpider(scrapy.Spider):
    name = 'mobile_scrap'
    allowed_domains = ['www.flipkart.com']
    
    def start_requests(self):
        yield scrapy.Request(url ='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAPPLE&param=167811&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkFwcGxlIFNtYXJ0cGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=44.productCard.PMU_V2_25', callback= self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

    def parse(self, response):
        mobile = response.xpath('(//div[@class="_1YokD2 _3Mn1Gg"]/div[@class="_1AtVbE col-12-12"])')
        for mobiles in mobile:
            
            product_name = mobiles.xpath('.//div[@class="col col-7-12"]/div[@class="_4rR01T"]/text()').get()
            price = mobiles.xpath('.//div[@class="_25b18c"]/div[@class="_30jeq3 _1_WHN1"]/text()').get()
            rom = mobiles.xpath('.//div[@class="fMghEO"]/ul[@class="_1xgFaf"]/li/text()').get()
            display = mobiles.xpath('.//ul[@class="_1xgFaf"]/li[2]/text()').get()
            camera = mobiles.xpath('.//ul[@class="_1xgFaf"]/li[3]/text()').get()
            processor = mobiles.xpath('.//ul[@class="_1xgFaf"]/li[4]/text()').get()
            warranty = mobiles.xpath('.//ul[@class="_1xgFaf"]/li[5]/text()').get()
            ratting = mobiles.xpath('//div[@class="_3LWZlK"]/text()').get()
            
            yield {
                "Product_name":product_name,
                "Price":price,
                "Rom":rom,
                "Display":display,
                "Camera":camera,
                "Processor":processor,
                "Warranty":warranty,
                "Ratting":ratting,
               
            } 

        next_page = response.xpath('//a[@class="_1LKTO3"]/@href').get()

        if next_page:
            yield scrapy.Request(url='https://www.flipkart.com' + next_page, callback=self.parse, headers= {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            })






