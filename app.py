from flask import Flask
from extensions import db, bcrypt
from config import Config
from routes.user_routes import user_routes


app = Flask(__name__)

# Configurations
app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
bcrypt.init_app(app)

# Register Blueprints
app.register_blueprint(user_routes, url_prefix='/users')

# Create database tables and run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
