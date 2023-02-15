from question_data import get_question_data

class QuizMaster:
    
    def __init__(self):
        self.question_bank = get_question_data()
        self.question_no = 1
        self.score = 0
        
    def get_question(self):
        return f"Q {self.question_no}. {self.question_bank[self.question_no-1].text}"
        
    def next_question(self):
        if self.question_no < len(self.question_bank):
            self.question_no += 1
            return 1
        else: return None
        
    def check_answer(self, answer:bool):
        if self.question_bank[self.question_no-1].answer == answer:
            self.score += 1
            return True
        else: 
            return False