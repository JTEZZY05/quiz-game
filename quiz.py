questions_answers = {"What is 4 + 4? ":8,
                     "What is 2 x 2?":4,
                     "What is 4 ÷ 2?":2,
                     "What is 10 - 5?":5,
                     "What is the capital of France?":"Paris",
                     "What is the color of grass?":"green",
                     "Is water wet?":"yes",
                     "Is bread a food?":"yes",
                     "Who was the first man to throw a pie?":"Harold Lloyd",
                     "Who is the coolest programmer(Hint:It's JTEZZY05:)":"JTEZZY05"}

def quiz_run(questions_answers):
    print("🍁 Welcome to my quiz game! 🍁")
    print("Please answer the following questions! ")

    score = 0
    wrong_questions = []
    total_questions = len(questions_answers)

    current_question = 1
    