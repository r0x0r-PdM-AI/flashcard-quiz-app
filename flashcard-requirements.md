# 🧠 Flashcard Quiz App (Rak Edition)

A CLI-based flashcard quiz tool to help users review knowledge by topic. Stores cards in JSON and quizzes users from the terminal.

---

## ✅ Core Features (MVP)

1. Load flashcards from a local JSON file
2. Display a random question
3. Wait for user answer (input)
4. Show correct answer and whether user was right
5. Track and show score (correct/total)
6. Run a fixed number of questions per session (e.g., 5 or 10)
7. Exit gracefully

---

## 📚 Flashcard Data Structure

Each flashcard contains:
- `id`: Unique number
- `question`: String
- `answer`: String
- `topic`: Optional (string)
- `difficulty`: Optional (easy/medium/hard)

```json
{
  "id": 1,
  "question": "What is the capital of France?",
  "answer": "Paris",
  "topic": "Geography",
  "difficulty": "easy"
}
```

## 🔄 Usage Flow

1. User runs the app with python quiz.py
2. App loads flashcards from flashcards.json
3. App selects N questions at random
4. For each question:
    - Show prompt
    - Accept user answer
    - Show feedback + correct answer
5. After all questions, show final score (e.g., 7/10 correct)

## 🎯 Stretch Goals (Future Enhancements)

1. Add CLI flags for quiz settings (topic, number of questions)
2. Add ability to add new flashcards via CLI
3. Track history or wrong answers
4. Support CSV import/export
5. Prep for a web UI or API

## 🔖 MVP Acceptance Criteria

1. At least 5 flashcards in the JSON file
2. Functional CLI quiz loop
3. Score tracked and shown
4. Clean exit and friendly messages