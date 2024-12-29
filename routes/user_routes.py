from flask import Blueprint, request, jsonify, session
from models.user import User  
from extensions import db, bcrypt

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

# ** User Registration **
@user_routes.route('/register', methods=['POST'])
def register_user():
    user_name = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")

    if not user_name or not password or not email:
        return jsonify({"error": "All fields (username, password, email) are required."}), 400


    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email is already in use "}), 409

    #Hash pass
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(user_name=user_name, password=hashed_password, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created", "id": new_user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# User Sign In
@user_routes.route("/login", methods=["POST"])
def fetch_user():
    user_name = request.json.get("username")
    password = request.json.get("password")

    existing_user = User.query.filter_by(username=user_name).first()

    if not existing_user or not bcrypt.check_password_hash(existing_user.password, password):
        return jsonify({"error": "Invalid username or password"}), 401


    session['user_id'] = existing_user.id

    return jsonify({"message": "Login successful", "user_id": existing_user.id})



# User log out
@user_routes.route("/logout", methods=["POST"])
def logout_user():
    if 'user_id' not in session:
        return jsonify({"error": "No user is logged in."}), 400

    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully."}), 200