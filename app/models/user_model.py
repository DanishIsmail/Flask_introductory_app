import os
from pymongo import MongoClient
from datetime import datetime
from marshmallow import ValidationError
from app.schemas.users_schema import users_schema
from app.config import Config
from app.helpers.roles import Roles

# MongoDB Client Setup
client = MongoClient(Config.MONGO_URL)
db = client[Config.MONGO_DB]
users_collection = db['users']

# Create a new user in the database
def create_user(user_data):
    try:
        # Validate user data using Marshmallow schema
        validated_data = users_schema.load(user_data)

        # Check if the user already exists by email
        existing_user = users_collection.find_one({"email": validated_data['email']})
        if existing_user:
            return {
                "isError": True,
                "message": "User with this email already exists"
            }, 409

        # Add timestamps for created_at and updated_at
        validated_data['created_at'] = datetime.now()
        validated_data['updated_at'] = datetime.now()

        # Insert the user into the MongoDB collection
        users_collection.insert_one(validated_data)

        return {"message": "User created successfully"}, 201

    except ValidationError as err:
        return {
            "isError": True,
            "message": "Validation Error", "errors": err.messages
        }, 400

    except Exception as e:
        print(f"An internal error occurred: {e}")
        return { 
            "isError": True,
            "message": f"An internal error occurred: {e}"
        }, 500

# Fetch a user by email
def find_user_by_email(email):
    return users_collection.find_one({"email": email})

# Fetch a user by ID
def find_user_by_id(user_id):
    return users_collection.find_one({"_id": user_id})
