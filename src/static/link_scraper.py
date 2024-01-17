"""Basic Web Scraper using python standard packages."""
import logging

import requests  # type: ignore
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


class WebScraper:
    """Basic web scraper to get data from single website."""

    def __init__(self, url: str):
        """Initializes Web Scraper class instance with url."""
        self.url = url

    def html_parser(self) -> BeautifulSoup:
        """Parses HTML with beautiful soup parser."""
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

        return soup

    def find_links(self) -> set:
        """Finds links embedded within the webpage.

        Returns:
            link_set (set): set of links inside a webpage
        """
        soup = self.html_parser()
        return {link["href"] for link in soup.find_all("a")}

    def dump_data(self):
        """Stores scraped raw data locally in parquet."""
        pass


if __name__ == "__main__":
    # we want to find, Detailed Dataset > Environment and Energy > Energy (nrg)
    #  > Energy statistics - quantities > monthly daat > supply transf ...
    #  > crude oil supply
    url = "https://ec.europa.eu/eurostat/web/main/data/database"

    scraper = WebScraper(url=url)
    links = scraper.find_links()
    logging.info(links)

    # # find element by class name
    # elements = results.find_all("div", class_="tree")
    # logging.info(elements)

    # trees = results.find_all("navigation-full-tree")
    # logging.info(trees)

    # tree = trees.find("div", class_="tree")
    # target_label = "For downloading the complete table
    # in TSV format: Crude oil supply - monthly data"
