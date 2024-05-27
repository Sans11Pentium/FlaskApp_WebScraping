from pymongo import MongoClient
from scrape_data import oscar_data, hockey_data  # Make sure these are correctly imported

client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]

def insertOscarData():
    full_info, best_pictures = oscar_data() 
    # full_info : [[{'' : ''},{},..],[{},{},..],..], best_pictures : [{'' : ''},{},...]
    
    oscar_collection = db["oscar_data"]
    best_film = db["best_oscar"]
    
    if oscar_collection.count_documents({}) > 0:
        print("Oscar data already present in the database. Skipping insertion.")
    else:
        for i in full_info:
            result = oscar_collection.insert_many(i)
            print(f"Inserted Oscar Data IDs: {result.inserted_ids}")
    
    if best_film.count_documents({}) > 0:
        print("Best picture data already present in the database. Skipping insertion.")
    else:
        result = best_film.insert_many(best_pictures)
        print(f"Inserted Best Picture Data IDs: {result.inserted_ids}")

def insertHockeyData():
    teams = hockey_data()
    
    hockey_collection = db["hockey_data"]
    
    if hockey_collection.count_documents({}) > 0:
        print("Hockey data already present in the database. Skipping insertion.")
    else:
        result = hockey_collection.insert_many(teams)
        print(f"Inserted Hockey Data IDs: {result.inserted_ids}")

def refreshDB():
    db.drop_collection("oscar_data")
    print('Successfully dropped the old records of oscar data')
    db.drop_collection("best_oscar")
    print('Successfully dropped the old records of best movies in oscar data')
    db.drop_collection("hockey_data")
    print('Successfully dropped the old records of hockey data')
    
    insertOscarData()
    insertHockeyData()

insertOscarData()
insertHockeyData()
# call to refresh the db to load new updated content
#refreshDB()