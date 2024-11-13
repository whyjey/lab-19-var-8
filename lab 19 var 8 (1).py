import pickle

# Задача 1: Обробка рядка слів
def process_words(input_string):
    words = input_string.split()
    words_dict = {word: i for i, word in enumerate(sorted(words))}
    with open('words.pkl', 'wb') as f:
        pickle.dump(words_dict, f)

# Задача 2: Обробка даних трикутника
def process_triangle(sides_data):
    with open('triangle.pkl', 'wb') as f:
        pickle.dump(sides_data, f)

# Приклад використання:
input_string = "яблуко банан груша апельсин"
process_words(input_string)

sides_data = {"a": 3, "b": 4, "c": 5}  # Дані про сторони трикутника
process_triangle(sides_data)
import pickle
import math

# Зчитування та виведення списку слів
def read_words():
    with open('words.pkl', 'rb') as f:
        words_dict = pickle.load(f)
    print("Словник слів:", words_dict)

# Зчитування даних про трикутник та обчислення площі і периметра
def calculate_triangle():
    with open('triangle.pkl', 'rb') as f:
        sides = pickle.load(f)
    
    a, b, c = sides['a'], sides['b'], sides['c']
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print(f"Периметр трикутника: {perimeter}")
    print(f"Площа трикутника: {area}")

# Приклад використання:
read_words()
calculate_triangle()
import shelve

# Задача 1: Обробка рядка слів
def process_words(input_string):
    words = input_string.split()
    words_dict = {word: i for i, word in enumerate(sorted(words))}
    with shelve.open('words_shelf') as db:
        db['words'] = words_dict

# Задача 2: Обробка даних трикутника
def process_triangle(sides_data):
    with shelve.open('triangle_shelf') as db:
        db['triangle'] = sides_data

# Приклад використання:
input_string = "яблуко банан груша апельсин"
process_words(input_string)

sides_data = {"a": 3, "b": 4, "c": 5}  # Дані про сторони трикутника
process_triangle(sides_data)
import shelve
import math

# Зчитування та виведення списку слів
def read_words():
    with shelve.open('words_shelf') as db:
        words_dict = db['words']
    print("Словник слів:", words_dict)

# Зчитування даних про трикутник та обчислення площі і периметра
def calculate_triangle():
    with shelve.open('triangle_shelf') as db:
        sides = db['triangle']
    
    a, b, c = sides['a'], sides['b'], sides['c']
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print(f"Периметр трикутника: {perimeter}")
    print(f"Площа трикутника: {area}")

# Приклад використання:
read_words()
calculate_triangle()
