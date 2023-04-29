import scrapy


class ProductsParseSpider(scrapy.Spider):
    name = "products_parse"
    allowed_domains = ["nn.russcvet.ru"]
    start_urls = ["https://nn.russcvet.ru/"]


    def parse(self, response, category:str='enamels', n:int=16):
        self.n = n
        yield response.follow(f'catalog/{category}/?count={n}', callback=self.parse_products )

    def parse_products(self, response):
        for i in range(self.n):
            yield {
                'name': response.css('div.catalog div div.name a::text')[i].get().strip(),
                'price': float(response.xpath('//div[not(@class="offer hide")]/div[@class="catalog-item-price"]/span/text()')[i].get().strip().split()[0])
            }