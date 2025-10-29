from pymongo import MongoClient
from dotenv import load_dotenv
import easygui, csv
from urllib.parse import quote_plus
import os

csv_path = easygui.fileopenbox(title="Select CSV file", default="*.csv")

load_dotenv()

username = os.getenv('DB_USERNAME')
password = quote_plus(os.getenv('DB_PASSWORD'))


mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.gi579ft.mongodb.net/?appName=Cluster0"

def readfromcsv(csv_path):
    data = []
    with open(csv_path, mode ='r')as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            data.append(lines)
    return data
    
def insertintodb(document):
    client = MongoClient(mongo_uri)
    db = client['TestDB']  # Database name
    collection = db['CP']  # Collection name
    inserted_documents = collection.insert_many(document)  
    print(f"Inserted document ids: {inserted_documents.inserted_ids}")
    client.close()

def main():
    data = readfromcsv(csv_path)
    insertintodb(data)

if __name__ == "__main__":
    main()