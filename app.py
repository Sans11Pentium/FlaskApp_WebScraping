#pip install virtualenv 
#python -m venv env

# to run the virtual env, run this on terminal:-
#.\env\Scripts\Activate.ps1


#import needed python modules
import requests
from bs4 import BeautifulSoup as bsp
from flask import Flask, render_template
from flask import Flask
from flask_pymongo import PyMongo
import json

#import functions for scraping
from scrape_data import oscar_data, hockey_data, get_adv_urls, failed_req_spoofing_headers, spoof_headers

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db

@app.route('/')
def home():
    # a = db.inventory.find({})
    # print(a,type(a))
    # for item in a:
    #     print(item['b'])
    # db.inventory.insert_one({'b':2})
    return render_template('index.html')


# Function to insert data into MongoDB collection
def insert_data(collection_name, data):
    collection = db[collection_name]
    collection.insert_many(data)

@app.route('/oscar')
def oscar():
    # Call the oscar_data function to scrape data
    full_info, best_pictures = oscar_data()
    
    # Insert full_info into the 'full_info_collection' if it doesn't exist, else create it
    if not db.full_info_collection.count_documents({}):
        insert_data('full_info_collection', full_info)
    
    # Insert best_pictures into the 'best_pictures_collection' if it doesn't exist, else create it
    if not db.best_pictures_collection.count_documents({}):
        insert_data('best_pictures_collection', best_pictures)
    
    # Render the oscar.html template and pass the data to it
    return render_template('oscar.html', full_info=full_info, best_pictures=best_pictures)



# @app.route('/oscar')
# def product():
#     return render_template('oscar.html')

@app.route('/hockey')
def hockey():
    return render_template('hockey.html')

@app.route('/spoof')
def spoof():
    return render_template('spoof.html')

if __name__=="__main__":
    app.run(debug=True)