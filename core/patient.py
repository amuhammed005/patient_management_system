import datetime
from typing import Dict, Any

def register_patient(id: int) -> Dict[str, Any]:
    while True:
        first_name = input("First Name: ").strip().capitalize()
        if first_name.isalpha():
            break
        print("⚠️ Use only letters!")
    while True:
        last_name = input("Last Name: ").strip().capitalize()
        if last_name.isalpha():
            break
        print("⚠️ Use only letters!")

    name = f"{first_name} {last_name}"

    while True:
        try:
            birth_year = int(input("Enter DOB (DD-MM-YYYY)").strip().split("-")[-1])
            age = int(datetime.datetime.today().year) - birth_year
            if 0 < age < 130:
                break
            print("⚠️ Enter a reasonable age!")
        except ValueError:
            print("❌ Invalid date format. Please enter (e.g 01-06-2001)")

    while True:
        gender = input("Gender (e.g Enter Male('M') or Female('F')): ").upper()
        if gender in ("M", "F"):
            break
        print(f"❌ Invalid input. Please enter 'M' for Male or 'F' for Female.")

    return {
        "id": id,
        "name": name,
        "age": age,
        "gender": gender,
        "records": [],
    }