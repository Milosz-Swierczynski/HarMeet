import json

user_choice = -1
tasks = []

def load_tasks_from_file():
    try:
        with open('tasks.json', 'r') as file:
            global tasks
            tasks = json.load(file)
        print("Zbiórki zostały wczytane z pliku JSON...")
    except FileNotFoundError:
        print("Nie znaleziono pliku ze zbiórkami. Rozpoczynam z pustą listą.")
    except json.JSONDecodeError:
        print("Plik ze zbiórkami jest uszkodzony. Rozpoczynam z pustą listą.")

def show_tasks():
    print()
    if tasks:
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")
    else:
        print("Brak zbiórek do wyświetlenia.")

def add_task():
    print()
    task = input("Wpisz tytuł i opis zbiórki (wpisz tytuł, myślnik, opis): ")
    tasks.append(task)
    print("Zbiórka została dodana...")

def remove_task():
    try:
        print()
        task_index = int(input("Wybierz zbiórkę do usunięcia: "))
        tasks.pop(task_index)
        print("Zbiórka usunięta pomyślnie...")
    except IndexError:
        print("Nie ma takiej zbiórki. Usuwanie nie powiodło się.")
    except ValueError:
        print("Błędny indeks. Nie udało się usunąć zbiórki.")

def save_tasks_to_file():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    print("Zbiórki zostały zapisane do pliku JSON...")

# Wczytywanie zadań z pliku na początku programu
load_tasks_from_file()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        remove_task()

    if user_choice == 4:
        save_tasks_to_file()

    print()
    print("1 - zobacz zbiórki.")
    print("2 - utwórz zbiórkę.")
    print("3 - usuń zbiórkę.")
    print("4 - zapisz zmiany.")
    print("5 - wyjdź")

    try:
        user_choice = int(input("Wybierz opcję: "))
    except ValueError:
        print("Proszę wybrać poprawną opcję.")
