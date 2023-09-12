# Unlisted Zone Shares Data Extraction
This project focuses on the crawling and scraping aspects of extracting data tables from UnlistedZone.com.

![alt text](https://github.com/shahriar-rahman/Scraping-Unlisted-Zone-Shares/blob/main/files/analytics.jpg)
[Studying the Business Analytics Photo by Tima Miroshnichenko](https://www.pexels.com/photo/a-business-person-studying-the-business-analytics-7567234/)  |  [Pexels Licensed](https://www.pexels.com/)

## Introduction
---------------------------------------------------------
UnlistedZone is India’s leading startup to facilitate the buying or selling process of your Unlisted, ESOP, or Pre-IPO Shares. 
This project aims to extract all the information by utilizing spider bots to index, then fetch and parse the page to obtain 
relevant information related to the Company such as their names, shares, last traded price, and cost per lot.


## Project Organization
---------------------------------------------------------

    ├── LICENSE
    ├── Makefile           <- Makefile with various commands
    ├── README.md     <- The top-level README for developers using this project.
    ├── scraping_data
    │   ├── excel          <- Data in xlsx format for better data analysis.
    │   ├── xml            <- Data in xml format.
    │   └── json           <- Data in Json format for better utilization.
    │
    │   ├── config         <- Contains the scrapy configuration file.
    │
    │
    ├── img                 <- Contains project image files.
    │   
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         			generated with `pip freeze > requirements.txt`
    │
    ├── setup.py         <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                 <- Source codes for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── spiders         <- Contains scripts that crawls and initiates instructions for data scraping.
    │   │   └── items.py
	│   │   └── middlewares.py
	│   │   └── pipelines.py
	│   │   └── settings.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
![alt text](https://github.com/shahriar-rahman/Unlisted-Zone-Shares-Data-Extraction/blob/main/img/unlisted_shares_page.PNG)

## Modules Required:
• Python 3.11

• Scrapy 2.8.0

• Applied separate Selectors (.css and xpath) to achieve data extraction

• Data Storage

• Pagination

• User Agents

• Temporary Containers

• DataFrame Manipulation using Pandas

• Data Storage using Excel, JSON and XML format
