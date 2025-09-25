from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://kdkr0357:ybiC5Nhakp4ifWx5@lung-cancer-prediction.rlhawlj.mongodb.net/"
)

# MongoDB client
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["pdf_app"]   # database
files_collection = db["files"] # collection
users_collection = db["users"]
otp_collection = db["otp_verifications"]
