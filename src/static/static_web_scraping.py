"""Web scraping static HTML website using python packages."""

import requests  # type: ignore
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://realpython.github.io/fake-jobs/"

    page = requests.get(url)
    # print(page.text)

    # pass page.content instead of page.text to avoid problems with character encoding.
    # The .content attribute holds raw bytes, which can be decoded better than
    # the text representation you printed earlier using the .text attribute.
    soup = BeautifulSoup(page.content, "html.parser")

    # find element by id
    results = soup.find(id="ResultsContainer")

    # print(results.prettify())

    # find element by class name
    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        # print(job_element, end="\n" * 2)
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip(), end="\n" * 2)
