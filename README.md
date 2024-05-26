# FlaskApp_WebScraping
This project scapes data from multiple websites, stores it into database and displays it on website through a flask app.

# When you insert scraped data into MongoDB and you need to handle dynamic data changes on a website, you have a few options:

# Periodic Scraping: 
Set up a periodic scraping job using a scheduler like Celery or cron. This job would scrape the website at regular intervals (e.g., every hour, every day) to update your MongoDB database with any changes.

# Real-Time Scraping: 
Implement real-time scraping using tools like Selenium or Scrapy with real-time monitoring of changes on the website. When a change is detected, update your MongoDB database accordingly.

# Webhooks or APIs: 
Some websites offer webhooks or APIs that notify you of data changes. You can integrate with these services to receive notifications when data changes occur and update your MongoDB database accordingly.

# Delta Updates: 
Keep track of the last time you scraped the website and only scrape the parts of the website that have changed since then. This can reduce the amount of data you need to process and update in MongoDB.

# Manual Triggering: 
Provide an interface for users or administrators to manually trigger a scraping job when they suspect data has changed on the website.

Choose the approach that best fits your requirements, taking into account factors like the frequency of data changes, the volume of data to be scraped, and the resources available for scraping and updating your MongoDB database.
