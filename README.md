# Unlisted Zone Shares Data Extraction
Parse and extract database for stock analysis of companies based on the [Unlisted Zone Shares](https://unlistedzone.com/shares/) website.

<br/>

![alt text](https://github.com/shahriar-rahman/Scraping-Unlisted-Zone-Shares/blob/main/files/analytics.jpg)
['Studying the Business Analytics' by Tima Miroshnichenko](https://www.pexels.com/photo/a-business-person-studying-the-business-analytics-7567234/)  |  [Pexels Licensed](https://www.pexels.com/)

<br/>

## ◘ Introduction
**Unlisted Shares** is one of the leading startup to facilitate in India where transactions of purchase and selling a myriad of Unlisted, ESOP, or Pre-IPO Shares. This study aims to utilize crawleing tools to acquire the database that can be found on the aforementioned website. 

<br/>

## ◘ Repository Organization
---------------------------------------------------------

    ├── LICENSE
    │ 
    ├── README.md	#The top-level README for developers using this project.
    │ 
    ├── datasets
    │   ├── excel	#XLSX format for better visualization.
    │
    │   ├── csv	#CSV format.
    │
    │   └── json	#Json format for effective utilization.
    │
    ├── files	#Contains various files related to this repository.
    │   
    │
    ├── requirements.txt	#Allows reproducing the analysis environment, generated using `pip freeze > requirements.txt` command.    
    │                         			
    ├── unlisted_zone	#Source codes for this project.
    │   ├── __init__.py	#Treats the source a Python module.
    │   
    │   ├── scrapy.cfg	#Configuration setings for the scrapy module
    |
    │   ├── spiders	#Crawlers initiating instructions for the scraping procedure.
    │		└── items.py
    │   
    │		└── middlewares.py
    │		└── pipelines.py
    │		└── settings.py
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
