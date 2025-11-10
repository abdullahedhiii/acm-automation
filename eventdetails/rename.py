from pymongo import MongoClient

client = MongoClient("mongodb+srv://abdullahedhi17:3fEs_-jzY%23V6VN%40@cluster0.gi579ft.mongodb.net/CodersCupDB?retryWrites=true&w=majority")
db = client["CodersCup"]

db["CP-Participants"].rename("CodersCupAttendance")
print("Renamed successfully!")
