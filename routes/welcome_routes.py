from flask import Blueprint, jsonify

welcome_bp = Blueprint('welcome', __name__)

@welcome_bp.route('/', methods=['GET'])
def welcome():
    """Welcome endpoint that returns a greeting message.
    
    Returns:
        tuple: JSON response with welcome message and HTTP 200 status code
    """
    return jsonify({'message': 'Hello Neurostack User'}), 200