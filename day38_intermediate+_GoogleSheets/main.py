import requests
from datetime import datetime
from env import APP_ID,API_KEY, BEARER


GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 163
AGE = 30

def exercise():
    api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    
    headers = {"x-app-id":APP_ID,
            "x-app-key": API_KEY}
    
    user_input = input("Tell me which exercise you did:")
    
    parameters = {"query": user_input,
                  "gender": GENDER,
                  "weight_kg": WEIGHT_KG,
                  "height_cm": HEIGHT_CM,
                  "age": AGE
                  }
    
    response = requests.post(url=api_endpoint, headers=headers, json=parameters)
    response.raise_for_status()
    
    result = []
    for item in response.json()["exercises"]:
        result.append({
            "exercise" : item["name"],
            "duration" : item["duration_min"],
            "calories" : item["nf_calories"]
            })
    return(result)
    
    
# exercise()

def add_row(exercise_data: dict):
    api_endpoint = "https://api.sheety.co/05718e36fb70ee70027b841f529b82c0/myWorkouts/workouts"
    
    header = {"Authorization": f"Bearer {BEARER}"}
    
    body = {
        "workout" : {
            "date" : datetime.now().strftime("%d/%m/%Y"),
            "time" : datetime.now().strftime("%H:%M:%S"),
            "exercise" : exercise_data["exercise"],
            "duration" : exercise_data["duration"],
            "calories" : exercise_data["calories"]
        }
    }
    
    response = requests.post(url=api_endpoint, headers=header, json=body)
    response.raise_for_status()
    result = response.text
    print(result)
    
# add_row()

for exercise_data in exercise():
    add_row(exercise_data)

