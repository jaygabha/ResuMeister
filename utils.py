import pymongo
import os
from dotenv import load_dotenv

load_dotenv("secrets.env")
client = pymongo.MongoClient(os.getenv('connection_string'))
db = client['ResuMeister_DB']