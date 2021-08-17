from question_model import Question 
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
quiz_active = True 
while quiz_active: #if quiz still has questions remaining 
    quiz.next_question()
    quiz_active = quiz.still_has_questions()

quiz.quiz_complete()