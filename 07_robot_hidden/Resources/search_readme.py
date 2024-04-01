# import scrapy
from scrapy.spiders import Spider
from scrapy.crawler import CrawlerProcess

class ReadmeSpider(Spider):
    name = 'readme_spider'
    # Assuming 192.168.56.101 is the base URL where the .hidden directory exists
    start_urls = ['http://192.168.56.101/.hidden/']

    def parse(self, response):
        # Look for links to README.md files and yield a request to parse the README content
        for readme_link in response.css('a[href$="README"]::attr(href)').getall():
            yield response.follow(readme_link, self.parse_readme)

        # Recursively follow directory links
        for directory_link in response.css('a[href$="/"]::attr(href)').getall():
            if directory_link not in ('../', '/'):  # Avoid going up the directory tree
                yield response.follow(directory_link, self.parse)

    def parse_readme(self, response):
        print(f'Parsing README file: {response.text}')
        # Extract and store the README content
        content = response.text
        yield {
            'url': response.url,
            'content': content
        }


if __name__ == '__main__':
    
    process = CrawlerProcess()
    process.crawl(ReadmeSpider)
    process.start()