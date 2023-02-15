import requests
import html

from question_model import Question

def get_question_data(amount:int=10, type:str="boolean"):
    response = requests.get(
        url="https://opentdb.com/api.php", 
        params={
            "amount": amount, 
            "type": type
            }
        )
    response.raise_for_status()
    question_data = [Question(html.unescape(data["question"]), data["correct_answer"]=="True") 
                     for data in response.json()['results']]
    return question_data