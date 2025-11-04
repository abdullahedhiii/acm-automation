from pymongo import MongoClient
from dotenv import load_dotenv
import easygui, csv
from urllib.parse import quote_plus
from html_content import get_confirmation_content
from send_email import sendConfirmation
from datetime import datetime
import os

csv_path = easygui.fileopenbox(title="Select CSV file", default="*.csv")
template_path = easygui.fileopenbox(title="Select html template", default="*.html")

load_dotenv()

# username = os.getenv('DB_USERNAME')
# password = quote_plus(os.getenv('DB_PASSWORD'))


# mongo_uri = f"mongodb+srv://{username}:{password}@cluster0.gi579ft.mongodb.net/?appName=Cluster0"
mongo_uri = os.getenv('MONGO_URI_TEST')

def readfromcsv(csv_path):
    data = []
    with open(csv_path, mode ='r')as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            data.append(lines)
    return data

def writetocsv(data):
    failedcsv = open("failed.csv", "w", newline="")
    fieldnames = data[0].keys()
    writer = csv.DictWriter(failedcsv, fieldnames=fieldnames)
    writer.writeheader()
    for team in data:
        writer.writerow(team)
    failedcsv.close()

def insertintodb(document):
    client = MongoClient(mongo_uri)
    db = client['TestDB']  # Database name
    collection = db['CP']  # Collection name
    inserted_documents = collection.insert_many(document)  
    print(f"Inserted document ids: {inserted_documents.inserted_ids}")
    client.close()

def email(data):
    failed_records = []
    logfile = open("processlogs.log", "a"); 
    for team in data: 
        try:
            html = get_confirmation_content(template_path, team, "Competitive Programming")
            rcvr = team["LeaderEmailAddress"]
            sbjct = "Registration Confirmation for Coders Cup 2025"
            
            if not sendConfirmation(rcvr, sbjct, html): 
                failed_records.append(team)
                print(f"[!] Error sending email to {rcvr}")
                logfile.write(f"{datetime.now()} : Couldn't send email to {rcvr}\n")
            else:
                print(f"[+] Email sent to {rcvr}")
                logfile.write(f"{datetime.now()} : Email sent to {rcvr}\n")
        except Exception as e:
            print(f"[!] Error processing email for {rcvr}: {e}")
            logfile.write(f"{datetime.now()} : [!] Error processing email for {rcvr}: {e}\n")
            failed_records.append(team)
    logfile.close()
    if failed_records:
        writetocsv(failed_records)


def main():
    data = readfromcsv(csv_path)
    # insertintodb(data)
    email(data)

if __name__ == "__main__":
    main()