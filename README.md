# Unlisted Zone Shares Data Extraction
Parse and extract database for stock analysis of companies based on [Unlisted Zone Shares](https://unlistedzone.com/shares/).

<br/>

![alt text](https://github.com/shahriar-rahman/Scraping-Unlisted-Zone-Shares/blob/main/files/analytics.jpg)
['Studying the Business Analytics' by Tima Miroshnichenko](https://www.pexels.com/photo/a-business-person-studying-the-business-analytics-7567234/)  |  [Pexels Licensed](https://www.pexels.com/)

<br/><br/>

## ◘ Navigation
- [Introduction](#-introduction)
    - [Background](#-background)
    - [Objectives](#-objectives)
- [Repository Organization](#-repository-organization)
- [Techncal Preliminaries](#-techncal-preliminaries)
- [Repository Organization](#-repository-organization)
- 

<br/><br/>

## ◘ Introduction

### • Background
**Unlisted Shares** is one of the leading startup to facilitate in India where transactions of purchase and selling a myriad of Unlisted, ESOP, or Pre-IPO Shares. This study aims to utilize crawleing tools to acquire the database that can be found on the aforementioned website. 

<br/>

### • Objectives
• Crawl the target site.

• Parse the page.

• Acquire relevant data.

• Store in memory.

<br/><br/>

## ◘ Technical Preliminaries

### • Repository Organization
---------------------------------------------------------
    │
    ├── LICENSE
    │ 
    ├── README.md	#The top-level README for developers using this project.
    │ 
    ├── datasets
    |
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
    |
    │    ├── __init__.py	
    │   
    │    ├── scrapy.cfg    #Configuration settings for Scrapy.
    |
    │    ├── py_utils    #Utilities folder.    
    |
    |            └── __init__.py	
    |
    |            └── common_utils.py	
    |
    │            └── scraping_utils.py
    │   
    │    ├── unlisted_zone    #Scrapy project folder.    
    |
    |            └── spiders	
    |
    |                    └── __init__.py
    |
    |                    └── crawler_bot.py
    |
    │            └── items.py
    │   
    │            └── middlewares.py
    │   
    │            └── pipelines.py
    │   
    │            └── settings.py
    │
    └── 
--------

<br/><br/>

## ◘ Requirements

### • Technologies Requirements:
1. Python 3.11
2. PyCharm IDE (2023.1)

<br/>

### • Package Requirements:
1. Python 3.11
2. Scrapy 2.8.0

<br/>

### • Technical Utilization:
1. XPATH Selectors
2. User Agents
3. Automated Pagination
4. Temporary Containers
5. Storage in Excel, JSON and CSV format

<br/>


