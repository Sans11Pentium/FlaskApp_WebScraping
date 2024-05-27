from pymongo import MongoClient
from scrape_data import oscar_data, hockey_data  # Make sure these are correctly imported

client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]

# INSERTING A SINGLE DOCUMENT

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Accessing a database
db = client['myDatabase']

# Accessing a collection
collection = db['myCollection']

# Data to be inserted
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Insert the document
result = collection.insert_one(data)

# Print the inserted document's ID
print(f"Inserted ID: {result.inserted_id}")


#INSERTING MULTIPLE DOCUMENTS

#Data to be inserted (list of dictionaries)
data_list = [
    {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Bob', 'age': 35, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 40, 'city': 'Houston'}
]

# Insert the documents
result = collection.insert_many(data_list)

# Print the inserted documents' IDs
print(f"Inserted IDs: {result.inserted_ids}")