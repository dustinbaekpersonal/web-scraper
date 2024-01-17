<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a project to create web scraper using python.

Inspiration comes from front office data engineering pipeline.

You might be asking: “Isn’t data gathering what APIs are for?”. Well, APIs can be fantastic, if you find one that suits your purposes. They are designed to provide a convenient stream of well-formatted data from one computer program to another. You can find an API for many types of data you might want to use, such as Twitter posts or Wikipedia pages. In general, it is preferable to use an API (if one exists), rather than build a bot to get the same data. However, an API might not exist or be useful for your purposes, for several reasons:

* You are gathering relatively small, finite sets of data across a large collection of websites without a cohesive API.
* The data you want is fairly small or uncommon, and the creator did not think it warranted an API.
* The source does not have the infrastructure or technical ability to create an API.
* The data is valuable and/or protected and not intended to be spread widely.

Even when an API does exist, the request volume and rate limits, the types of data, or the format of data that it provides might be insufficient for your purposes.”

Excerpt From
Web Scraping with Python, 2nd Edition
Ryan Mitchell
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0
This material may be protected by copyright.


Here's how:
* Scrape data from website quickly, once it's uploaded or updated e.g. https://ec.europa.eu/eurostat/web/main/data/database
* Dump it into S3 or GCS bucket
* ETL
* Write it into on-premise


### Built With

* https://realpython.com/beautiful-soup-web-scraper-python/




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

### Installation

1. Clone the repo
    ```bash
    git clone git@github.com:dustinbaekpersonal/web-scraper.git
    ```

2. Create virtual environment and activate
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

3. Install dependencies
    ```bash
    make pip-tools-dev
    ```

    _**Optional**_
4. To run pre-commit,
    ```bash
    pre-commit install
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create README.md template
- [ ] Write basic web scraper
- [ ]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dustin-baek-715729179/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
