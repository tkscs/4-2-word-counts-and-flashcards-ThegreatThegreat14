import random

# Update this dictionary with questions and answers:
flashcards = {
    "question": "answer"
}

# Get a list of keys (questions) from the dictionary

keys = list(flashcards.keys())

# Randomly sample one question

random_question_1 = random.choice(keys)

# Use the `input` function to ask the user the question and get their response

user_answer_1 = input(random_question_1)

# Use the question as a key to look up the answer in the dicitonary

answer_1 = flashcards[random_question_1]

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect

if user_answer_1 == answer_1:
    print("Correct!")
else:
    print("That's incorrect.")