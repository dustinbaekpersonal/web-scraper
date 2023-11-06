"""Basic Web Scraper using python standard packages."""
import logging
from urllib.request import urlopen

from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


class WebScraper:
    """Basic web scraper to get data from single website."""

    def __init__(self, url: str):
        """Initializes Web Scraper class instance with url."""
        self.url = url

    def html_parser(self) -> BeautifulSoup:
        """Parses HTML with beautiful soup parser."""
        html = urlopen(self.url)
        bsobj = BeautifulSoup(html, features="html.parser")
        return bsobj

    def find_links(self) -> list:
        """Finds links embedded within the webpage.

        Returns:
            link_list (list): list of links inside a webpage
        """
        bsobj = self.html_parser()
        return [link["href"] for link in bsobj.find_all("a")]


if __name__ == "__main__":
    url = "https://ec.europa.eu/eurostat/web/main/home"
    web_scraper = WebScraper(url=url)
    logging.info(f"{web_scraper.find_links()}")
