from pymongo import MongoClient
from dotenv import load_dotenv
import csv, easygui
import os

csv_path = easygui.fileopenbox(title="Select the CSV file with event details", default="*.csv")
output_csv_path = "./attendance_codes.csv"

load_dotenv()
mongo_uri = os.getenv("MONGO_URI_TEST")


def readfromcsv(csv_path):
    """Read teams from original CSV"""
    with open(csv_path, mode="r") as file:
        csvFile = csv.DictReader(file)
        return list(csvFile)


def get_attendance_code(email):
    """Fetch attendance code from MongoDB for given leader email"""
    client = MongoClient(mongo_uri)
    db = client["CodersCup"]
    collection = db["CodersCupAttendance"]

    try:
        participant = collection.find_one({"Leader Email Address": email})
        if participant and "Att Code" in participant:
            return participant["Att Code"]
        return None
    except Exception as e:
        print(f"[!] Database error for {email}: {e}")
        return None
    finally:
        client.close()


def create_new_csv(input_data, output_path):
    """Create new CSV with Leader Email, Vjudgeusername, and Att Code"""
    with open(output_path, "w", newline="") as csvfile:
        fieldnames = ["Leader Email Address", "Vjudge username", "Att Code"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for team in input_data:
            email = team.get("Leader Email Address", "").strip()
            vjudge = team.get("Vjudge username", "").strip()
            att_code = get_attendance_code(email)
            writer.writerow({
                "Leader Email Address": email,
                "Vjudge username": vjudge,
                "Att Code": att_code or "N/A"
            })
            print(f"Processed: {email} -> {att_code or 'N/A'}")


def main():
    data = readfromcsv(csv_path)
    create_new_csv(data, output_csv_path)
    print(f"\n✅ New CSV saved as: {output_csv_path}")


if __name__ == "__main__":
    main()
