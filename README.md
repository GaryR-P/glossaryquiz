#  Glossary Quiz Tool

This project randomly quizzes the user on glossary terms from our course using an LLM (Ollama).

## How it works
- Loads terms from `glossary.json`
- Picks a random term
- Asks an Ollama model ("quiz-tutor") to explain it
- Displays prompt + model response

## Requirements
- Requires Ollama
- Requires the quiz tutor model(ollama pull quiz-tutor)
  
## How to run
```bash
python quiz.py

