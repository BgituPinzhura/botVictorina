import Database
from VictorinaApi import easy_question_parser, medium_question_parser, hard_question_parser, kid_question_parser
from typing import Union, List


class GameObj:
    def __init__(self, database: Database.Database, telegram_id: str):
        self.question_type = database.get_question_type(telegram_id)
        if self.question_type == 1:
            self.parser = kid_question_parser.get_json()
        elif self.question_type == 2:
            self.parser = easy_question_parser.get_json()
        elif self.question_type == 3:
            self.parser = medium_question_parser.get_json()
        elif self.question_type == 4:
            self.parser = hard_question_parser.get_json()
        self.right_answer = self.parser["answers"][0]
    
    def get_question(self) -> str:
        return self.parser["question"]
    
    def get_answers(self) -> List[List[Union[int, str]]]:
        answers = self.parser["answers"]
        for i in range(4):
            answers[i] = [i, answers[i]]
        return answers
    
    def if_win(self, answer: str) -> bool:
        return answer.lower() == self.right_answer.lower()
