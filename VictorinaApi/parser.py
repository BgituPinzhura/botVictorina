import requests
from typing import Dict
from VictorinaApi.generator_url import GeneratorUrl


# Парсер ответа api, удаляет символ \u2063, который по какой-то причине неккоректно отображается
class Parser:
    def __init__(self, question_type: int):
        self.question_type = question_type
    
    def get_json(self) -> Dict:
        url = GeneratorUrl().get_url(question_type=self.question_type)
        response = requests.get(url).json()["data"][0]
        
        response["question"] = response["question"].replace("\u2063", "", 1000)
        for i in range(4):
            response["answers"][i] = response["answers"][i].replace("\u2063", "", 1000)
        
        return response
