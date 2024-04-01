class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question)

    def display_options(self, options):
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()

    def start_quiz(self):
        for question, options, correct_answer in self.questions:
            self.display_question(question)
            self.display_options(options)
            user_choice = input("Enter your answer (number): ")
            
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(options):
                if self.check_answer(options[int(user_choice) - 1], correct_answer):
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect.")
            else:
                print("Invalid choice. Skipping question.")

        print(f"Quiz ended. Your score is {self.score} out of {len(self.questions)}.")

# Example quiz questions
questions = [
    ("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus"], "Mars"),
    ("What is the largest mammal?", ["Elephant", "Blue whale", "Giraffe"], "Blue whale")
]

# Initialize and start the quiz
quiz = Quiz(questions)
quiz.start_quiz()
