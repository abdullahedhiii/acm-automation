from pymongo import MongoClient
from dotenv import load_dotenv
import easygui, csv
from urllib.parse import quote_plus
from html_content import get_event_content
from send_email import sendConfirmation
from datetime import datetime
import os

csv_path = easygui.fileopenbox(title="Select CSV file with event details", filetypes=["*.csv"])
template_path = easygui.fileopenbox(title="Select HTML template file", filetypes=["*.html"])

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
            print(lines["LeaderEmailAddress"])
    return data

def writetocsv(data):
    failedcsv = open("failed.csv", "w", newline="")
    fieldnames = data[0].keys()
    writer = csv.DictWriter(failedcsv, fieldnames=fieldnames)
    writer.writeheader()
    for team in data:
        writer.writerow(team)
    failedcsv.close()

# def insertintodb(document):
#     client = MongoClient(mongo_uri)
#     db = client['TestDB']  # Database name
#     collection = db['CP']  # Collection name
#     inserted_documents = collection.insert_many(document)  
#     print(f"Inserted document ids: {inserted_documents.inserted_ids}")
#     client.close()

def email(data, competition, rules, attw):
    failed_records = []
    logfile = open("processlogs.log", "a"); 
    for team in data: 
        try:
            html = get_event_content(template_path, team, competition, rules, attw)
            rcvr = team["LeaderEmailAddress"]
            sbjct = "Event Details for Coders Cup 2025"
            
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
    competition = "Competitive Programming"
    rules = "https://coderscup.acmnuceskhi.com/ruleBook/Competitive%20Programming.pdf"
    attendance_website = "https://attendance.acmnuceskhi.com/"
    data = readfromcsv(csv_path)
    # insertintodb(data)
    email(data, competition, rules, attendance_website)

if __name__ == "__main__":
    main()