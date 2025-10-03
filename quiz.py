
#Load flashcards from flashcards.json
#Randomly pick N questions (start with 5)
#For each question:
#Show the question
#Get user input
#Show correct answer + whether user was right
#Show results at the end


import json
import random


def load_flashcards(filename='flashcards.json'):
    with open(filename, 'r') as f:
        return json.load(f)
    
if __name__ == "__main__":
    
    
    while True:
        score = 0
        flashcards = random.sample(load_flashcards(), 5)
        for card in flashcards:
            print("\n"+"-"*40)
            print(f"Question: {card['question']}")
            answer = input("Your answer: ")
            if answer.lower().strip() == card['answer'].lower().strip():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {card['answer']}")
        print(f"You scored {score} out of {len(flashcards)}")
        again = input("Do you want to try again? (yes/no): ")
        if again.lower() != 'yes':
            print("Thanks for playing, Good Bye!")
            break
        score = 0
        flashcards = random.sample(load_flashcards(), 5)