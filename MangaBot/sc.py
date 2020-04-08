import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
def addQuote(text,author):
  with open('output_quotes.csv', 'a',encoding='utf-8') as csvfile:
    f_writer = csv.writer(csvfile, delimiter='|',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    f_writer.writerow([text,author])


class MangaSpider(CrawlSpider):
  name = 'quoteSpider'
  start_urls = ['http://quotes.toscrape.com/page/1']
  allowed_domains = ['quotes.toscrape.com']

  rules = (
        Rule(LinkExtractor(allow=[r'page/[0-9]+/?$']),callback='parse_quote',follow=True),
    )

  custom_settings = {
      'LOG_ENABLED': True,
      'ROBOTSTXT_OBEY':True
  }

  def parse_quote(self,response):
    for quote in response.css('div.quote'):
      text = quote.css('span.text::text').extract_first()
      author = quote.css('span small::text').extract_first()
      addQuote(text,author)