# Створіть DataFrame з ім'ям "students", який містить такі стовпці:
# "Name" (ім'я студента)
# "Age" (вік студента)
# "Gender" (стать студента)
# "Score" (оцінка студента за певний предмет)
# Підготуйте дані для графіку (наприклад, кількість продаж за місяць або результати тестування студентів).
# Використовуючи бібліотеку Matplotlib, створіть графік для відображення цих даних.
# Виберіть відповідний тип графіку (лінійний, стовпчиковий, круговий тощо), підпишіть осі, додайте заголовок та легенду. +

# Виведіть перші 5 рядків з DataFrame "students". +

# Створіть графік для відображення залежності між двома змінними.
# Наприклад, це може бути діаграма розсіювання (scatter plot), де по одній вісі буде відображена одна змінна, а по іншій - інша змінна.
# Додайте легенду та підпишіть осі. +

# Створіть графік для відображення категоріальних даних, наприклад, розподілу кількості об'єктів за певною категорією.
# Використайте стовпчиковий графік або кругову діаграму для цього завдання.
# Підпишіть категорії, осі та додайте заголовок.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

students = {
        'Name': ['John', 'Stacy', 'Maks', 'Anna',],
        'Age': [17, 18, 17, 19,],
        'Gender': ['male', 'female', 'male', 'female',],
        'english_score': [93, 82, 78, 80,],
    }

def work_with_dict():
    df = pd.DataFrame(students)

def get_score():
    df = pd.DataFrame(students)
    name = df['Name']
    grade = df['english_score']

    plt.plot(name, grade)
    plt.xlabel("І'мя учня")
    plt.ylabel('Оцінка анг.')
    plt.title('Результат за 2 четверть')

    plt.legend()
    plt.show()

# get_score()

def students_inf():
    df = pd.DataFrame(students)
    print(df[:5])

# students_inf()

def scater():
    df = pd.DataFrame(students)
    name = df['Name']
    grade = df['english_score']

    colors = np.array(["red","green","blue","yellow",])
    plt.scatter(name, grade, c=colors, alpha=0.5, s=300) # додав s для збільшення розміру точок
    plt.xlabel("Ім'я учня")
    plt.ylabel('Оцінка')

    plt.title('Результати учнів з англійської')
    # plt.legend()
    plt.colorbar()
    plt.show()

# scater()

def categories():
    category = ['Категорія 1', 'Категорія 2', 'Категорія 3', 'Категорія 4']
    object = [5, 41, 60, 23]

    plt.pie(object ,labels=category)
    plt.title("Категорії по об'єктам")
    plt.legend()
    plt.show()

categories()

