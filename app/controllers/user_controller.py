from flask import jsonify
from app.models.user_model import create_user


def create_user_logic(user_data):
    """
    Creates a new user and returns a response.
    """
    try:
        # Validate the user data using Marshmallow schema
       
        result, status_code = create_user(user_data)

        # If user creation is successful, create an access token (JWT)
        if status_code == 201:
            # access_token = create_access_token(identity=user_data['email'])
            return {
                "isError": False,
                "message": "User created successfully.",
                # "access_token": access_token
            }, 201
        else:
            return result, status_code

    except Exception as e:
        return {
            "isError": True,
            "message": f"An internal error occurred: {str(e)}"
        }, 500
