import os
from urllib.parse import unquote

import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["ebooks.az"]
    start_urls = ["https://www.ebooks.az/category_economy.html"]

    def parse(self, response):
        book_links = response.css('a[href^="book_"]::attr(href)').extract()
        self.logger.info(f'Found {len(book_links)} book links on {response.url}')

        for book_link in book_links:
            book_url = response.urljoin(book_link)
            self.logger.info(f'Processing book link: {book_url}')
            yield scrapy.Request(book_url, callback=self.parse_book_page)

    def parse_book_page(self, response):
        book_name = response.css('section h2::text').get()
        self.logger.info(f'Book Name: {book_name}')

        token_link = response.css('div[align="right"] a.button.green.large::attr(href)').get()

        if token_link:
            # Check if the token_link is a relative URL
            if not token_link.startswith('http'):
                # Construct the complete URL by joining with the base URL
                base_url = "https://www.ebooks.az"  # Replace with the actual base URL
                token_link = response.urljoin(base_url + token_link)

            # Pass the book_name to the download_pdf method
            yield scrapy.Request(token_link, callback=self.download_pdf, meta={'book_name': book_name})
        else:
            self.logger.warning('PDF token link not found on this page.')

    def download_pdf(self, response):
        content_type = response.headers.get('Content-Type')
        self.logger.info(f'Content-Type: {content_type}')

        # Check if the Content-Type indicates a PDF
        if content_type == b'application/pdf':
            # Use the book_name as the file name
            file_name = response.meta['book_name']

            # Clean the file name to remove invalid characters
            clean_file_name = self.clean_file_name(file_name)

            self.logger.info(f'Downloading PDF: {clean_file_name}')

            file_path = os.path.join(self.settings["FILES_STORE"], clean_file_name)

            with open(file_path, 'wb') as f:
                f.write(response.body)
        else:
            self.logger.warning('Not a PDF file.')

    def clean_file_name(self, file_name):
        # Decode URL-encoded characters and remove invalid characters
        cleaned_name = unquote(file_name)
        cleaned_name = "".join(c for c in cleaned_name if c.isalnum() or c in ('.', '_', '-'))
        return cleaned_name
