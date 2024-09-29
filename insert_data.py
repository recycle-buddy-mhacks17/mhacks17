from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import streamlit_authenticator_mongo as stauth


mongo_username = os.environ.get("MONGO_USER")
mongo_password = os.environ.get("MONGO_PASS")
uri = f"mongodb+srv://{mongo_username}:{mongo_password}@cluster0.lcktyax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(mongo_username)
print(mongo_password)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# # Function to create a new user
# def create_user(username, password, email, name, database: str, collect: str):
#     try:
#         # Choose the database and collection
#         db = client[database]
#         collection = db[collect]

#         # Hash the password
#         hashed_password = stauth.Hasher([password]).generate()[0]

#         # Create the user document
#         user_doc = {
#             'username': username,
#             'password': hashed_password,
#             'email': email,
#             'name': name
#         }

#         # Insert the document into the collection
#         result = collection.insert_one(user_doc)

#         print(f"User created with record ID: {result.inserted_id}")

#     except Exception as e:
#         print(f"An error occurred while creating user: {e}")

# # Example usage: Create a new user
# create_user("example_user", "securepassword", "example@example.com", "Example User", 'myFirstDatabase', 'myCollection')

# def add_to_mongo(key, value, database: str, collect: str):
#     try:
#         # Choose the database and collection
#         db = client[database]
#         collection = db[collect]

#         # Insert the document into the collection
#         result = collection.insert_one({key: value})

#         # Print the inserted document's ID
#         print(f"Data inserted with record ID: {result.inserted_id}")

#     except Exception as e:
#         print(f"An error occurred while inserting data: {e}")


# # Function to retrieve a document from MongoDB based on a key-value pair
# def retrieve_from_mongo(key, value, database: str, collect: str):
#     try:
#         # Choose the database and collection
#         db = client[database]
#         collection = db[collect]

#         # Query the collection for a document where the key matches the given value
#         document = collection.find_one({key: value})

#         if document:
#             return document
#         else:
#             return f"No document found with {key} = {value}"

#     except Exception as e:
#         return f"An error occurred while retrieving data: {e}"

# # Example usage: Adding a document
# add_to_mongo("hello", 1, 'myFirstDatabase', 'myCollection')

# # Example usage: Retrieving a document
# result = retrieve_from_mongo("hello", 1, 'myFirstDatabase', 'myCollection')
# print(result) 