# load_questions.py

import json
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from authapp.models import QuizQuestion

# Clear existing questions (optional)
QuizQuestion.objects.all().delete()

with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for item in questions:
    question_text = item['question']
    options = item['options']
    correct = item['correct_answer']

    try:
        correct_index = options.index(correct) + 1  # 1-based index
    except ValueError:
        print(f"Skipping invalid question: {question_text}")
        continue

    QuizQuestion.objects.create(
        question_text=question_text,
        option1=options[0],
        option2=options[1],
        option3=options[2],
        option4=options[3],
        correct_option=correct_index
    )

print(f"Successfully loaded {len(questions)} questions.")
