```plaintext
# Ebook PDF Downloader

## Overview
This Scrapy spider is designed to download PDF books from a specific website. It follows links to individual book pages, extracts book information, and downloads the associated PDF files. This README provides an overview of the project, how to set it up, and how to run the spider.

## Prerequisites
To use this spider, you need to have the following installed:

- Python 3.x
- Scrapy
- unidecode
- Any additional dependencies mentioned in the spider's source code

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ebook-pdf-downloader.git
```

2. Change into the project directory:

```bash
cd ebook-pdf-downloader
```

3. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

4. Install the required Python packages:

```bash
pip install scrapy unidecode
```

## Usage

1. Edit the spider configuration: Open `ebooks_az/spiders/main_spider.py` and adjust the spider's settings if needed.

2. Run the spider with the following command:

```bash
scrapy crawl main
```

The spider will start scraping the target website and downloading PDFs. Downloaded PDF files will be saved in the `files` directory within the project folder.

## Important Notes

- Respect website policies: Ensure that your web scraping activities comply with the website's terms of service and respect their robots.txt file. Consider adding appropriate delays between requests to avoid overloading the server.

- File storage: The downloaded PDF files will be saved in the `files` directory within the project folder. Make sure this directory exists and has appropriate write permissions.

- Customization: Feel free to customize the spider to suit your specific scraping requirements, such as adapting the URL, improving error handling, or setting different user agents.

## License
This project is provided under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code for your purposes.

## Contact
If you have any questions or need further assistance, please feel free to [contact us](mailto:your@email.com) or open an issue in this repository.

Happy web scraping!
```

You can replace "yourusername" in the GitHub clone URL, "your@email.com" in the contact section, and adapt the README to include any additional information specific to your project. This README provides an overview, installation instructions, usage, and important notes for your PDF downloader spider.
