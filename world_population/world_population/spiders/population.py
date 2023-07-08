import scrapy


class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
            yield response.follow(url=link, callback=self.parse_country, meta={"country_name":name})

    def parse_country(self, response):
        name = response.request.meta["country_name"]
        all_row = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for details in all_row:
            year = details.xpath(".//td[1]/text()").get()
            population= details.xpath(".//td[2]/strong/text()").get()
            yearly_change = details.xpath(".//td[4]/text()").get()
            Urban_Population = details.xpath(".//td[10]/text()").get()
            
            yield {
                "Country":name,
                "Year": year,
                "Population": population,
                "Yearly_Change":yearly_change,
                "Urban_Population":Urban_Population,
            }
