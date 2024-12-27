from VictorinaApi.url import url


# Класс для генерации подходящей ссылки от выбранного уровня сложности вопроса
class GeneratorUrl:
    def get_url(self, question_type: int) -> str:
        funcs = {1: self.get_easy_question_url(self),
                 2: self.get_medium_question_url(self),
                 3: self.get_hard_question_url(self),
                 4: self.get_kid_question_url(self)}
        return funcs[question_type]
    
    @staticmethod
    def get_easy_question_url(self) -> str:
        return url + "1&count=1"
    
    @staticmethod
    def get_medium_question_url(self) -> str:
        return url + "2&count=1"
    
    @staticmethod
    def get_hard_question_url(self) -> str:
        return url + "3&count=1"
    
    @staticmethod
    def get_kid_question_url(self) -> str:
        return url + "4&count=1"
