class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///zendatabase.db"
    SECRET_KEY = "zenSecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional: Disable tracking
