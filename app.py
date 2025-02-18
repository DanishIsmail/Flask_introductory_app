from flask import Flask
from flask_cors import CORS
# from app.routes.user_routes import user_routes

app = Flask(__name__)

# Enable CORS for all routes and allow any origin
CORS(app, resources={r"/*": {"origins": "*"}})

# register api routes
app.register_blueprint(user_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)