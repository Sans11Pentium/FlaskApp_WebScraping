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
query = {'name': 'Charlie'}
result = collection.delete_one(query)

# Print the number of documents deleted
print(f"Deleted {result.deleted_count} document.")

#Deleting Multiple Document
# Criteria to find documents to delete
query = {'city': 'New Chicago'}

# Delete the documents
result = collection.delete_many(query)

# Print the number of documents deleted
print(f"Deleted {result.deleted_count} documents.")

# Criteria to find documents to update
query = {'city': 'Chicago'}

# New values to update
new_values = {'$set': {'city': 'New Chicago'}}

# Update the documents
result = collection.update_many(query, new_values)

new_values = {'$set': {'age': 26}}

# Update the document
result = collection.update_one(query, new_values)