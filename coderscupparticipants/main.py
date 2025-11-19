from pydoc import doc
from pymongo import MongoClient
from dotenv import load_dotenv
import easygui, csv
from urllib.parse import quote_plus
from html_content import get_confirmation_content
from send_email import sendConfirmation
from datetime import datetime
import os

# csv_path = "./Competitive Programming Registrations - (Nov 11 - 2 15 pm).csv"
csv_path = easygui.fileopenbox(title="Select CSV file with participant details", filetypes=["*.csv"])
# template_path = "./emailtemp.html"

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
            lines["Att Code"] = generateCode()
            # lines["Att Code"] = "cc-10000" #DUMMY CODE FOR TESTING
            lines["Attendance Marked"] = False
            data.append(lines)
            print(lines["Leader Email Address"])
    return data

def add_or_update():
    client = MongoClient(mongo_uri)
    db = client["CodersCup"]  # adjust DB name if different
    collection = db["CodersCupAttendance"]
    update_data = {"$set": {"Competition Name": "Competitive Programming"}}

    with open(csv_path, mode ='r')as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            try: 
                participant = collection.find_one({"Leader Email Address": lines["Leader Email Address"]})
                if not participant:
                    lines["Att Code"] = generateCode()
                    # lines["Att Code"] = "cc-10000" #DUMMY CODE FOR TESTING
                    lines["Attendance Marked"] = False
                    lines["Competition Name"] = "Competitive Programming"
                    collection.insert_one(lines)
                    print(f"Inserted: {lines['Leader Email Address']}")
                else:
                    print(f"Skipped (already exists): {lines['Leader Email Address']}")
                    filter_query = {"Leader Email Address": lines["Leader Email Address"]}
                    collection.update_one(filter_query, update_data)

            except Exception as e:
                print(f"[!] Database error for {lines['Leader Email Address']}: {e}")
                return None
    client.close()

def writetocsv(data):
    failedcsv = open("failed.csv", "w", newline="")
    fieldnames = data[0].keys()
    writer = csv.DictWriter(failedcsv, fieldnames=fieldnames)
    writer.writeheader()
    for team in data:
        writer.writerow(team)
    failedcsv.close()

def generateCode():
    with open("codegen.txt", "r") as f:
        last_code = f.read().strip()
    code = str(int(last_code) + 1).zfill(5)
    new_code = "CC-" + code
    with open("codegen.txt", "w") as f:
        f.write(str(code))
    return new_code

def insertintodb(document):
    client = MongoClient(mongo_uri)
    db = client["CodersCup"]  # adjust DB name if different
    collection = db["CodersCupAttendance"]
    inserted_documents = collection.insert_many(document)  
    # update_data = {"$set": {"Competition Name": "Competitive Programming"}}
    # for doc in document:
    #     try: 
    #         participant = collection.find_one({"Leader Email Address": doc["Leader Email Address"]})
    #         if not participant:
    #             # doc["Competition Name"] = "Competitive Programming"
    #             collection.insert_one(doc)
    #             print(f"Inserted: {doc['Leader Email Address']}")
    #         else:
    #             print(f"Skipped (already exists): {doc['Leader Email Address']}")
    #             filter_query = {"Leader Email Address": doc["Leader Email Address"]}
    #             collection.update_one(filter_query, update_data)

    #     except Exception as e:
    #         print(f"[!] Database error for {doc['Leader Email Address']}: {e}")
    #         return None
    print(f"Inserted document ids: {inserted_documents.inserted_ids}, Last Code: {document[-1]['Att Code']}")
    client.close()

# def email(data):
#     failed_records = []
#     logfile = open("processlogs.log", "a"); 
#     for team in data: 
#         try:
#             html = get_confirmation_content(template_path, team, "Competitive Programming")
#             rcvr = team["Leader Email Address"]
#             sbjct = "Registration Confirmation for Coders Cup 2025"
            
#             if not sendConfirmation(rcvr, sbjct, html): 
#                 failed_records.append(team)
#                 print(f"[!] Error sending email to {rcvr}")
#                 logfile.write(f"{datetime.now()} : Couldn't send email to {rcvr}\n")
#             else:
#                 print(f"[+] Email sent to {rcvr}")
#                 logfile.write(f"{datetime.now()} : Email sent to {rcvr}\n")
#         except Exception as e:
#             print(f"[!] Error processing email for {rcvr}: {e}")
#             logfile.write(f"{datetime.now()} : [!] Error processing email for {rcvr}: {e}\n")
#             failed_records.append(team)
#     logfile.close()
#     if failed_records:
#         writetocsv(failed_records)


def main():
    data = readfromcsv(csv_path)
    insertintodb(data)
    # email(data)
    # add_or_update()

if __name__ == "__main__":
    main()