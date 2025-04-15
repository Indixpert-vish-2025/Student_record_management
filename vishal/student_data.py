import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, 'w') as file:
        json.dump(students, file, indent=4)
