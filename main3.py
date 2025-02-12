def main():
  print("Hello learners!")

if __name__=="__main__":
  main()


import random

# Function to fetch trivia about a given number
def trivia_fetch(num):
    trivia_dict = {
        1: "One is the first positive integer.",
        2: "Two is the only even prime number.",
        3: "Three is the first odd prime number.",
        4: "Four is the first composite number.",
        5: "Five is the number of human senses.",
        6: "Six is a perfect number (sum of its divisors equals the number itself).",
        7: "Seven is considered a lucky number in many cultures.",
        8: "Eight is the number of bits in a byte.",
        9: "Nine is a square number (3x3).",
        10: "Ten is the base of the decimal system."
    }
    return trivia_dict.get(num, "No trivia available for this number.")

# Main function to run the quiz
def main():
    print("Welcome to the Number Trivia Quiz!")
    score = 0

    questions = [
        {"question": "What is the first positive integer?", "answer": 1},
        {"question": "What is the only even prime number?", "answer": 2},
        {"question": "What is the number of human senses?", "answer": 5},
        {"question": "What is the number of bits in a byte?", "answer": 8},
    ]

    random.shuffle(questions)

    for q in questions:
        user_answer = int(input(q["question"] + " "))
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        
        trivia = trivia_fetch(q["answer"])
        print("Trivia: " + trivia)

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
