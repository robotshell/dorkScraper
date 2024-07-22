<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/dorkScraper"><img src="https://i.ibb.co/1LwdRCw/dorkscraper.png" alt="cubeSpraying" style="width:100%"></a>
</h1>

## Description

Dork Scraper is an open-source tool designed to scrape URLs using Google dorks. It is a simple Python script that automates the process of searching for specific terms on Google and collecting the resulting URLs. This can be particularly useful for security researchers, penetration testers, and anyone interested in gathering information from search engines using advanced search queries (dorks).

This script is distributed under the terms of the GNU General Public License v3.0.

## Requirements

- Python 3.x
- `googlesearch-python` package

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/robotshell/dorkScraper
    cd dorkSraper
    ```

2. Install the required Python package:
    ```sh
    pip install googlesearch-python
    ```

## Usage

To run the Dork Scraper, you can use the following command syntax:

```sh
python dorkSraper.py "dork" number_of_websites [-s output.txt]
