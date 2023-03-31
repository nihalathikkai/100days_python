import requests
from datetime import datetime
from env import USERNAME, TOKEN

API_URL = "https://pixe.la"

def create_user():
    endpoint = "v1/users"
    json_body = {
        "token":TOKEN, 
        "username":USERNAME, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes", 
    }
    
    response = requests.post(
        url=f"{API_URL}/{endpoint}",
        json=json_body
    )
    
    response_json = response.json()
    if response_json["isSuccess"]: print("User has been created.")
    else: print("Error! Unable to create user.")
    print(response_json["message"])
    

def create_graph():
    endpoint = f"/v1/users/{USERNAME}/graphs"
    json_body = {
        "id":"test-graph1",
        "name":"graph-test-1",
        "unit":"hours",
        "type":"float",
        "color":"ajisai",
        "timezone":"Asia/Calcutta"
    }
    
    response = requests.post(
        url=f"{API_URL}/{endpoint}",
        headers={"X-USER-TOKEN":TOKEN},
        json=json_body
    )
    
    print(response.text)


def post_value(date, value):
    endpoint = f"/v1/users/{USERNAME}/graphs/test-graph1"
    
    response = requests.post(
        url=f"{API_URL}/{endpoint}",
        headers={"X-USER-TOKEN":TOKEN},
        json={"date":date, "quantity":str(value)}
    )
    
    print(response.text)


date = datetime.strftime(datetime.now(), "%Y%m%d")

post_value(date, 3)

# create_user()
# create_graph()