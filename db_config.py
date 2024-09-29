import yaml
import streamlit as st
from pymongo import MongoClient
import streamlit_authenticator_mongo as stauth
from insert_data import client  # Import the MongoDB client

# Load YAML configuration
def load_config():
    with open('config.yaml') as file:
        return yaml.load(file, Loader=yaml.SafeLoader)


# Initialize the authenticator
def init_authenticator():
    config = load_config()
    db = client['myFirstDatabase']  # Replace with your database name
    collection = db['myCollection']  # Replace with your collection name
    authenticator = stauth.Authenticate(
        collection,
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator