# Web Scraping Project
This project aims to scrape data from various pages of scrapethissite.com using Python. The scraped data will be stored in a MongoDB database. The project focuses on implementing robust error handling, optimizing performance, and providing clear documentation for ease of use.

Web scraping is the process of extracting data from websites. In this project, the requests library in Python is used to scrape data from dynamic content, such as AJAX and JavaScript-driven pages, provided by scrapethissite.com.

## Requirements
- Scraping Dynamic Content
- Use only the requests library to scrape content from the website.
- Extract every available data visible on the front-end of the specified website pages.
- Data Persistence
- Design an appropriate database schema to efficiently store scraped data.
- Save the scraped data to either MongoDB or PostgreSQL.
- Robust Error Handling
- Implement error handling to manage timeouts, network errors, or unexpected changes in the website's structure.
- Log any encountered errors to a log file for debugging purposes.
- Performance Optimization (Optional)
- Implement techniques such as parallel scraping or caching mechanisms to improve performance.
- Optimize the scraping process to minimize the load on the target website's servers.

## Setup
### Clone the repository:

```bash
git clone https://github.com/your_username/web-scraping-project.git
```

### Install dependencies:

``` bash
pip install -r requirements.txt
```

### Set up the database (MongoDB).
- Open mongoDB compass and connect 'mongodb://localhost:27017/'

### To run the scraping application:
- set up virtual environment
```bash
pip install virtualenv 
python -m venv env
```

### to run the virtual env, run this on terminal:-
```bash
.\env\Scripts\Activate.ps1
```
### to stop virtual env, run this on terminal:-
```bash
deactivate
```
### run the app
```bash
python app.py
```

### Error Handling
The application handles errors gracefully by logging them to a designated log file (error.log). This ensures that any encountered errors are captured for debugging purposes.

This project scapes data from multiple websites, stores it into database and displays it on website through a flask app.

## When you insert scraped data into MongoDB and you need to handle dynamic data changes on a website, you have a few options:

### Periodic Scraping: 
Set up a periodic scraping job using a scheduler like Celery or cron. This job would scrape the website at regular intervals (e.g., every hour, every day) to update your MongoDB database with any changes.

### Real-Time Scraping: 
Implement real-time scraping using tools like Selenium or Scrapy with real-time monitoring of changes on the website. When a change is detected, update your MongoDB database accordingly.

### Webhooks or APIs: 
Some websites offer webhooks or APIs that notify you of data changes. You can integrate with these services to receive notifications when data changes occur and update your MongoDB database accordingly.

### Delta Updates: 
Keep track of the last time you scraped the website and only scrape the parts of the website that have changed since then. This can reduce the amount of data you need to process and update in MongoDB.

### Manual Triggering: 
Provide an interface for users or administrators to manually trigger a scraping job when they suspect data has changed on the website.