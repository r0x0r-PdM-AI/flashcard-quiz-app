#Load flashcards from flashcards.json
#Randomly pick N questions (start with 5)
#For each question:
#Show the question
#Get user input
#Show correct answer + whether user was right
#Show results at the end


import json
import random


def load_flashcards(filename='flashcards.json', topic=None):
    with open(filename, 'r') as f:
        data = json.load(f)  # read once into a Python object
    if topic is None:
        return data
    return [card for card in data if card['topic'] == topic]
    
if __name__ == "__main__":
    
    print("Welcome to the Flashcard Quiz App!")

    
    while True:
        score = 0

        topics = sorted(set(card.get('topic') for card in load_flashcards() if 'topic' in card))

        print("\nAvailable topics:")
        for i, t in enumerate(topics, 1):
            print(f"{i}. {t}")
        print("Press Enter to select a random topic.")

        topic_choice = input("Select a topic by number (or press Enter for random): ")
        if topic_choice:
            try:
                selected_topic = int(topic_choice)
                if 1 <= selected_topic <= len(topics):
                    topic = list(topics)[selected_topic - 1]
                else:
                    print("Invalid selection.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        cards = load_flashcards(topic=list(topics)[int(topic_choice)-1] if topic_choice else None)
        if not cards:
            print("No flashcards found.")
            continue
        n = min(5, len(cards))
        flashcards = random.sample(cards, n)

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
        print("\n"+"="*40)