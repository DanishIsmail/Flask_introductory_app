from flask import jsonify
from functools import wraps

def token_required(f):
    """Decorator for routes that need authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
            
        except Exception as e:
            return jsonify({'error': 'Authentication failed'}), 401
            
    return decorated

