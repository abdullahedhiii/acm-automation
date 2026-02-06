from pymongo import MongoClient
from dotenv import load_dotenv
import csv, easygui
from urllib.parse import quote_plus
from html_content import get_event_content
from send_email import sendConfirmation
from datetime import datetime
import os


# csv_path = "./Coders Cup Lab Allocation (Monday 10th) - Monday 10th Nov.csv"
# csv_path = "./Coders Cup Lab Allocation (Freshman Tuesday 11th) - Tuesday 11th.csv"
# csv_path = "./Coders Cup Lab Allocation (Seniors Tuesday 11th) - Tuesday senior 11th.csv"
csv_path = easygui.fileopenbox(title="Select the CSV file with event details", default="*.csv")
# csv_path = "./test.csv"
template_path = easygui.fileopenbox(title="Select the HTML template file", default="*.html")

load_dotenv()

mongo_uri = os.getenv("MONGO_URI_TEST")

def readfromcsv(csv_path):
    data = []
    with open(csv_path, mode='r') as file:
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


def get_attendance_code(email, comp):
    """Fetch attendance code from MongoDB for given leader email"""
    try:
        client = MongoClient(mongo_uri)
        db = client["CodersCup"]  # adjust DB name if different
        collection = db["CodersCupAttendance"]

        
        participant = collection.find_one({
            "Leader Email Address": email,
            "Competition Name": comp
        })
        if participant and "Att Code" in participant:
            return participant["Att Code"]
        else:
            return None
    except Exception as e:
        print(f"[!] Database error for {email}: {e}")
        return None
    finally:
        client.close()




def email(data, rules, attw):
    failed_records = []
    logfile = open("processlogs.log", "a")

    for team in data:
        try:
            # fetch att_code from DB and add to row
            email_addr = team.get("Leader Email Address", "").strip()
            mem1 = team.get("Member 1 Email Address", "").strip()
            mem2 = team.get("Member 2 Email Address", "").strip()
            # comp = team.get("Competition Name").strip()
            # house = team.get("House").strip()
            # att_code = get_attendance_code(email_addr, comp)
            # team["att_code"] = att_code if att_code else "N/A"
            # cc = [team.get("Member 1 Email Address", "").strip(), team.get("Member 2 Email Address", "").strip()]
            # html = get_event_content(template_path, team, comp, rules, attw)
            # if house == "Master Oogway":
            #     template_path = "./FINALROUND/masteroogway_template.html"
            # elif house == "Lord Shen":
            #     template_path = "./FINALROUND/lordshen_template.html"
            # elif house == "Tai Lung":
            #     template_path = "./FINALROUND/tailung_template.html"
            # else:
            #     template_path = "./FINALROUND/dragonwarrior_template.html"
            html = get_event_content(template_path, team,rules)
            rcvr = email_addr
            # sbjct = "Event Details for Coders Cup 2025"
            # sbjct = "Welcome to CODERS TANK – Final Round Qualification Confirmed"
            # sbjct = "Welcome to CHI PARADOX – Coders Cup 2025"
            # sbjct = f"Welcome to House {house} - Coders Cup 2025"
            sbjct = "Invitation – Coder’s Cup 2025 Closing Ceremony 🎉"
            # sbjct = f"Login Credentials for Chi Paradox - Coders Cup 2025"
            if not sendConfirmation(rcvr, mem1, mem2, sbjct, html):
                failed_records.append(team)
                print(f"[!] Error sending email to {rcvr}")
                logfile.write(f"{datetime.now()} : Couldn't send email to {rcvr}\n")
            else:
                print(f"[+] Email sent to {rcvr} (att_code=)")
                logfile.write(f"{datetime.now()} : Email sent to {rcvr}\n")

        except Exception as e:
            print(f"[!] Error processing email for {team.get('Leader Email Address')}: {e}")
            logfile.write(f"{datetime.now()} : [!] Error processing email for {team.get('Leader Email Address')}: {e}\n")
            failed_records.append(team)

    logfile.close()
    if failed_records:
        writetocsv(failed_records)


def main():
    # competition = "Competitive Programming"
    rules = "https://coderscup.acmnuceskhi.com/ruleBook/Competitive%20Programming.pdf"
    # rules = "https://coderscup.acmnuceskhi.com/ruleBook/Chi%20Paradox%20By%20PROCOM.pdf"
    # rules = "https://coderscup.acmnuceskhi.com/ruleBook/Code%20Fu%20Debugging%20trials.pdf" #debugging
    # rules = "https://coderscup.acmnuceskhi.com/ruleBook/Pitch%20Warriors.pdf" #pitch warriors
    # rules = "https://coderscup.acmnuceskhi.com/ruleBook/Data%20Dash.pdf"
    attendance_website = "https://attendance.acmnuceskhi.com/"
    data = readfromcsv(csv_path)
    email(data, rules, attendance_website)
    # print(get_attendance_code("k241028@nu.edu.pk", "Chi Paradox"))


if __name__ == "__main__":
    main()
