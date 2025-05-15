import json
import random
import subprocess

# Load glossary
with open('glossary.json', 'r', encoding='utf-8') as f:
    glossary = json.load(f)

# Pick a random term
entry = random.choice(glossary)
term = entry['term']
definition = entry['definition']

# Prompt for the model
prompt = f"What is the meaning of '{term}' in a programming course?"

# Run the Ollama model using subprocess
print(f"\n🧠 Quiz Prompt:\n{prompt}\n")
print("📝 Model Response:\n")

process = subprocess.Popen(
    ['ollama', 'run', 'quiz-tutor'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Send the prompt to the model
stdout, stderr = process.communicate(prompt)

# Print model's response
print(stdout)

if stderr:
    print("\n⚠️ Error:\n", stderr)
