"""Basic Web Scraper using python standard packages."""

from urllib.request import urlopen

from bs4 import BeautifulSoup


class WebScrpaer:
    """Basic web scraper."""

    def __init__(self):
        """Initialising web scraper."""
        pass


html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features="html.parser")
print(bsObj.head.title.asdf.asdf)


if __name__ == "__main__":
    web_scraper = WebScrpaer()
