class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        
    def next_question(self):
        """ Retrieves the item at the current question_number from the question_list.
        Uses the input() function to show the question text and ask for the 
        user's answer. 
        """ 
        current_question = self.questions_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
    