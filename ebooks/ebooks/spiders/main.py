from urllib.parse import urljoin

import scrapy
from unidecode import unidecode


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["ebooks.az"]
    start_urls = ["https://www.ebooks.az/category_economy.html"]
    download_timeout = 300

    def parse(self, response):
        # Scraping book links
        book_links = response.css('a[href^="book_"]::attr(href)').extract()
        for book_link in book_links:
            book_url = response.urljoin(book_link)
            yield scrapy.Request(book_url, callback=self.parse_book_page)

        # Check if there's a "Next Page" link and follow it
        next_page = response.css('a.button.white::attr(href)').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        # Extracting book information
        title = unidecode(response.css('section h2::text').get())
        pdf_url = response.css('div[align="right"] a::attr(href)').get()
        if title and pdf_url:
            if not pdf_url.startswith('http'):
                base_url = response.url
                pdf_url = urljoin(base_url, pdf_url)
            file_name = f"{title}.pdf"
            yield scrapy.Request(pdf_url, callback=self.save_pdf, meta={'file_name': file_name})

    def save_pdf(self, response):
        # Saving PDFs
        file_name = response.meta['file_name']
        if response.status == 200:
            with open(f'files/{file_name}', 'wb') as f:
                f.write(response.body)
        else:
            self.logger.error(f"Failed to download PDF: {file_name} - Status code: {response.status}")
