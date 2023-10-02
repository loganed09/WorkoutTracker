import requests
from datetime import *
import os

WORKOUT_APP_ID = os.environ.get("WORKOUT_APP_ID")
WORKOUT_API_KEY = os.environ.get("WORKOUT_API_KEY")
TOKEN = os.environ.get("TOKEN")
GENDER = "male"
WEIGHT_KG = 81.65
HEIGHT_CM = 167.64
AGE = 32
now = datetime.now()
date_string = now.strftime("%m/%d/%Y")
time_string = now.strftime("%H:%M:%S")



workout_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

query = input("What workout did you do today? ")

workout_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY
}

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=workout_endpoint, json=params, headers=workout_headers)
exercises = exercise_response.json()

# response2 = requests.get(url=sheety_endpoint)

for exercise in exercises["exercises"]:
    data = {
        "sheet1": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=data, headers=sheety_headers)
    print(response.text)

