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
    for questions, answers in questions_answers.items():
        print(f"Question {current_question}/{total_questions}")
        user_input = input("Question: "+questions)
        #This checks if the current answer is an integer, in which case it converts users string input to an integer
        if isinstance(answers,int):
            if user_input.isdigit():
                user_input = int(user_input)
        if user_input == answers and total_questions < 9: # Loops up untill 8, this is because 9 and 10 have special responses
            print("✨WOWZERS YOU ARE CORRECT✨")
            score+=1
        elif user_input != answers:
            print("❌YOU ARE WRONG❌")
            wrong_questions.append(current_question) #Updates the wrong question tracker for each question missed
        elif user_input == answers and total_questions == 9:
            print("✨🔥🚀HOW DO YOU EVEN KNOW THAT?✨🔥🚀") #I am gonna be impressed if someone just knows this
            score+=1
        elif user_input == answers and total_questions ==10:
            print("😎💯AND YOU'RE GOSH DARN RIGHT😎💯") #Well then, that settles things
            score+=1
        current_question+=1
        #Final summary
        print("You finished the quiz 🎉")
        print(f"Your final score is {score}/{total_questions}")
        
        if score == total_questions:
            print("🎉✨PERFECT SCORE🎉✨")
        elif score == 0:
            print("0_0 HOWWWWWWWWWWWWWWWWWWWW")
            print("You got.....EVERYTHING WRONG OMLLLL")
        else:
            print("You missed these questions:",wrong_questions)
quiz_run(questions_answers)


