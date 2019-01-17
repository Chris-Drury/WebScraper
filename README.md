# WebScraper
A Python script built to scrape images and compile them into .pdfs

# Getting Started
There are 3 main steps to follow before the Webscraper can be run

## Getting a Webdriver
This project uses the Selenium web module. As a result, a webdriver will be needed.
I recommend a [Chrome webdriver](http://chromedriver.chromium.org/getting-started)

## Installing the Dependencies
The WebScraper uses 3 additional modules:
* [Selenium](https://selenium-python.readthedocs.io)
* [fpdf](https://pyfpdf.readthedocs.io/en/latest/)
* [PIL](https://pillow.readthedocs.io/en/stable/)
Each module will need to be installed before use. This can be done using [pip](https://pip.pypa.io/en/stable/installing/)

## The Config file
The WebScraper user supplied information from the config.txt file alongside the python script.
This file specifies configurations including the website to scrape from (and any login information if required), 
as well as the location of the installed webdriver and the number of images to scrape.

# Running the WebScraper
Once the above is completed, running the webscraper should be as simple as typing:
```
Python WebScraper.py
```

# License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
