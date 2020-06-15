import scrapy


class QuotesSpider(scrapy.Spider):
    name = "kitsunekko"

    def start_requests(self):
        url = "https://kitsunekko.net/dirlist.php?dir=subtitles%2F"
        yield scrapy.Request(url=url, callback=self.parse_index_page)

    def parse_index_page(self, response):
        urls = response.css('table#flisttable a::attr(href)').getall()
        for url in urls:
            self.logger.info(f'getting anime {response.urljoin(url)}')
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_anime_child)

    def parse_anime_child(self, response):
        urls = response.css('table#flisttable a::attr(href)').getall()
        for url in urls:
            self.logger.info(f'getting download link {response.urljoin(url)}')
            yield scrapy.Request(url=response.urljoin(url), callback=self.save_file)

    def save_file(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving file into %s', path)
        with open(f'files/{path}', 'wb') as f:
            f.write(response.body)
