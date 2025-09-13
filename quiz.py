#Dictionary for questions and their respective answers
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
#Function to ask the questions and check users answers against the correct ones 
def quiz_run(questions_answers):
    print("🍁 Welcome to my quiz game! 🍁")
    print("Please answer the following questions! ")

    score = 0 #Score tracker
    wrong_questions = [] # Tracks what numbers were wrong
    total_questions = len(questions_answers) 

    current_question = 1
    #For loop that loops through the dictionary 
    for questions, answers in questions_answers():
        print(f"Question {current_question}/{total_questions}")
        user_input = input("Question: "+questions)
        #This checks if the current answer is an integer, in which case it converts users string input to an integer
        if isinstance(answers,int):
            if user_input.isdigit():
                user_input = int(user_input)
        