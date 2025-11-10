from pymongo import MongoClient
import os
mongo_uri = os.getenv("MONGO_URI_TEST")

client = MongoClient(mongo_uri)
db = client["CodersCup"]

db["CP-Participants"].rename("CodersCupAttendance")
print("Renamed successfully!")
