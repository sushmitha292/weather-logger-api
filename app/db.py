import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri=os.getenv("MONGO_URI")
client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
db=client.weather_db

