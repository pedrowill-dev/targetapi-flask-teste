from src.config import ConfigurationMongoDB
import urllib


instance_config = ConfigurationMongoDB

DEBUG = True
CORS_HEADERS = 'Content-Type'
SECRET_KEY = "ZmlyYTIwMjAyMDIxMjAyMnRlc3RlZmxhc2s="
SESSION_EXPIRATE_MINUTES = 30

MONGO_URI = f"mongodb://{instance_config.host}:{instance_config.port}/{instance_config.database}"
