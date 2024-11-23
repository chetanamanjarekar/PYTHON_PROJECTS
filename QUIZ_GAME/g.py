def quiz_game():
    print("------Welcome to the Quiz Game!------")
    print("Answer the following questions by typing A, B, C, or D.")

    # Questions and answersa
    questions = [
        {
            "question": "WHEN PYTHON IS DEVELOPED IN WHICH YEAR",
            "options": ["A. 1991", "B. 1998", "C. 1996", "D. 1994"],
            "answer": "A"
        },
        {
            "question": "WHO DEVELOPED PYTHON",
            "options": ["A. Guido van Rossum", "B. James Gosling", "C. Raymond Boyce", "D. Brendan Eich"],
            "answer": "A"
        },
        {
            "question": "WHICH IS A PROGRAMMING LANGUAGE'?",
            "options": ["A.HTML", "B. CSS", "C.PYTHON"],
            "answer": "B"
        },
        {
            "question": "DOES PYTHON IS HIGH LEVEL AND INTERPRETED PROGRAMMING LANGUAGE ?",
            "options": ["A. YES", "B. NO"],
            "answer": "D"
        }
    ]

    score = 0

    # Loop through each question
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer: ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    # Final Score
    print("\nQuiz Over!")
    print(f"Your final score is {score}/{len(questions)}.")
    print("---THANKYOU FOR PARTICIPATING---")

# Run the gamea
if __name__ == "__main__":
    quiz_game()
