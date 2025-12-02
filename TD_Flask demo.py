from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
import redis

# Initialize Flask app and Redis
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

# Route to get user details
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({'username': user.username, 'email': user.email})
    else:
        return jsonify({'message': 'User not found'}), 404

# Route to store session in Redis
@app.route('/set_session', methods=['POST'])
def set_session():
    user_id = request.json.get('user_id')
    redis_client.set(f'user_session_{user_id}', 'active')
    return jsonify({'message': f'Session for user {user_id} set successfully'}), 200

# Route to check session status from Redis
@app.route('/check_session/<int:user_id>', methods=['GET'])
def check_session(user_id):
    session_status = redis_client.get(f'user_session_{user_id}')
    if session_status:
        return jsonify({'message': f'Session for user {user_id} is active'})
    else:
        return jsonify({'message': f'No active session for user {user_id}'}), 404

if __name__ == '__main__':
    db.create_all()  # Create all tables
    app.run(debug=True)
