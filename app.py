#pip install virtualenv 
#python -m venv env

# to run the virtual env, run this on terminal:-
# .\env\Scripts\Activate.ps1
# to stop virtual env, run this on terminal:-
# deactivate

# import needed python modules
import requests
from bs4 import BeautifulSoup as bsp
from flask import Flask, render_template
from flask import Flask
from flask_pymongo import PyMongo
import json

#import functions for scraping
from scrape_data import oscar_data, hockey_data, failed_req_spoofing_headers, spoof_headers

#start mongodb compass and operate on database called "myDatabase"
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
db = PyMongo(app).db

#home route
@app.route('/')
def home():
    # a = db.inventory.find({})
    # print(a,type(a))
    return render_template('index.html')

#route for oscar data
@app.route('/oscar')
def oscar():
    # Call the oscar_data function to scrape data
    full_info, best_pictures = oscar_data()
    
    # Render the oscar.html template and pass the data to it
    return render_template('oscar.html', full_info=full_info, best_pictures=best_pictures)

# route for hockey data
@app.route('/hockey')
def hockey():
    # Call the hockey_data function to retrieve hockey data
    teams = hockey_data()
    # Pass the data to the hockey.html template
    return render_template('hockey.html', teams=teams)

# spoofing headers
@app.route('/spoof')
def spoof():
    errorResponse=failed_req_spoofing_headers()
    noErrorResponse=spoof_headers()
    return render_template('spoof.html',errorResponse=errorResponse,noErrorResponse=noErrorResponse)

# run the app
if __name__=="__main__":
    app.run(debug=True)