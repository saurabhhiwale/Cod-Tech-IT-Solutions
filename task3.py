import random

# Define the questions and answers for the quiz
quiz_questions = {
    "Math": [
        {"question": "What is 2 + 2?", "options": ["a) 3", "b) 4", "c) 5", "d) 6"], "answer": "b"},
        {"question": "What is 3 * 4?", "options": ["a) 9", "b) 10", "c) 11", "d) 12"], "answer": "d"}
    ],
    "Science": [
        {"question": "What is the chemical symbol for water?", "options": ["a) H2O", "b) CO2", "c) NaCl", "d) O2"], "answer": "a"},
        {"question": "What planet is known as the Red Planet?", "options": ["a) Jupiter", "b) Mars", "c) Saturn", "d) Venus"], "answer": "b"}
    ]
}

def run_quiz():
    score = 0

    print("Welcome to the Quiz Application!\n")

    # Shuffle the order of categories
    categories = list(quiz_questions.keys())
    random.shuffle(categories)

    # Iterate over categories
    for category in categories:
        print(f"\nCategory: {category}")
        questions = quiz_questions[category]

        # Shuffle the order of questions
        random.shuffle(questions)

        # Iterate over questions in the category
        for q in questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)
            
            # Get user's answer
            user_answer = input("\nEnter your answer (a/b/c/d): ").lower()

            # Check if the answer is correct
            if user_answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

    print("\nQuiz completed!")
    print("Your final score:", score)

if __name__ == "__main__":
    run_quiz()
