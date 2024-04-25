# Завдання 1
# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.
# import json
# import time
#
# def save_timer(timee):
#     with open('timer.json', 'w') as file:
#         json.dump({'timee': timee}, file)
#
# def load_timer():
#     try:
#         with open('timer.json', 'r') as file:
#             data = json.load(file)
#             return data['timee']
#     except FileNotFoundError:
#         return 0
#
# def timer():
#     timee = load_timer()
#
#     while True:
#         hours = timee // 3600
#         minutes = (timee % 3600) // 60
#         seconds = timee % 60
#         print("Час: {:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
#         time.sleep(1)
#         timee += 1
#         save_timer(timee)
#
# timer()




# Завдання 2
# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.
import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_tasks(tasks):
    task = input('Введіть завдання:')
    tasks.append(task)
    save_tasks(tasks)
    print('Завдання додали.')

def delete_task(tasks):
    print('Список завдань:')
    for i, task in enumerate(tasks):
        print(f'{i+1}. {task}')

    while True:
        choice = input('Введіть номер завдань для видалення(0 - вийти):')
        if choice == '0':
            return
        try:
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                save_tasks(tasks)
                print('Завдання видалено')
                break
            else:
                print('Некоректний ввід.')
        except ValueError:
            print('Некоректний ввід.')

def display(tasks):
    if not tasks:
        print('Список завдань порожній.')
    else:
        print('Список завдань:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def main():
    tasks = load_tasks()

    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Відобразити список завдань")
        print("4. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            display(tasks)
        elif choice == "4":
            print("Програма завершена.")
            break
        else:
            print("Некоректний ввід. Спробуйте ще раз.")

main()

