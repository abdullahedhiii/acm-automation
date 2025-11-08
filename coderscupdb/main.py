from pymongo import MongoClient
from dotenv import load_dotenv
import easygui, csv, random, string
from urllib.parse import quote_plus
import os

csv_path = "./Competitive Programming Registrations - (Nov 11 - 2 15 pm).csv"

load_dotenv()

username = os.getenv('DB_USERNAME')
password = quote_plus(os.getenv('DB_PASSWORD'))

mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.gi579ft.mongodb.net/?appName=Cluster0"

# Function to generate a unique random attendance code
def generate_unique_codes(count, length=8):
    chars = string.ascii_uppercase + string.digits + "#$@"
    codes = set()

    while len(codes) < count:
        code = ''.join(random.choices(chars, k=length))
        codes.add(code)

    return list(codes)

def readfromcsv(csv_path):
    data = []
    with open(csv_path, mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            data.append(lines)
    return data

def insertintodb(document):
    client = MongoClient(mongo_uri)
    db = client['CodersCup']  # Database name
    collection = db['CP-Participants']  # Collection name
    inserted_documents = collection.insert_many(document)
    print(f"Inserted document ids: {inserted_documents.inserted_ids}")
    client.close()

def main():
    data = readfromcsv(csv_path)
    codes = generate_unique_codes(len(data))

    # Add a unique code to each row
    for i, row in enumerate(data):
        row["attendance_code"] = codes[i]

    insertintodb(data)

if __name__ == "__main__":
    main()
