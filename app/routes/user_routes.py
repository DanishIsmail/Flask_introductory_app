from flask import Blueprint, request, jsonify
from app.controllers.user_controller import create_user_logic


user_routes = Blueprint('user_routes', __name__)

# Register a new user
@user_routes.route('/user/register', methods=['POST'])
def register():
    user_data = request.get_json()
    result, status_code = create_user_logic(user_data)
    return jsonify(result), status_code
