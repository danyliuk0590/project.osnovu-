class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task}' було надано працівнику {self.name}.")

    def update_position(self, new_position):
        self.position = new_position
        print(f"Посаду працівника {self.name} оновлено: {new_position}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Зарплату працівника {self.name} оновлено: {new_salary}")

class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name.lower() == employee_name.lower():
                self.employees.remove(employee)
                print(f"Працівника {employee_name} видалено зі списку.")
                break
        else:
            print("Працівника з таким ім'ям не знайдено.")

    def list_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}, Tasks: {employee.tasks}")

def print_menu():
    print("Головне меню:")
    print("1. Переглянути список працівників")
    print("2. Додати нового працівника")
    print("3. Надати завдання працівнику")
    print("4. Змінити посаду або зарплату працівника")
    print("5. Звільнити працівника")
    print("6. Вийти")

def view_employee_list():
    print("\nСписок працівників:")
    hr_system.list_employees()

def add_employee():
    name = input("Введіть ім'я працівника: ")
    position = input("Введіть посаду працівника: ")
    salary = float(input("Введіть зарплату працівника: "))
    new_employee = Employee(name, position, salary)
    hr_system.add_employee(new_employee)
    print("\nПрацівника успішно додано.")

def assign_task_to_employee():
    employee_name = input("Введіть ім'я працівника: ")
    task = input("Введіть завдання для працівника: ")
    for employee in hr_system.employees:
        if employee.name.lower() == employee_name.lower():
            employee.assign_task(task)
            return
    print("Працівника з таким ім'ям не знайдено.")

def update_employee_details():
    employee_name = input("Введіть ім'я працівника: ")
    for employee in hr_system.employees:
        if employee.name.lower() == employee_name.lower():
            update_type = input("Що бажаєте змінити (посаду/зарплату): ").lower()
            if update_type == 'посаду':
                new_position = input("Введіть нову посаду: ")
                employee.update_position(new_position)
            elif update_type == 'зарплату':
                new_salary = float(input("Введіть нову зарплату: "))
                employee.update_salary(new_salary)
            else:
                print("Некоректний ввід. Повинно бути 'посаду' або 'зарплату'.")
            return
    print("Працівника з таким ім'ям не знайдено.")

def remove_employee():
    employee_name = input("Введіть ім'я працівника: ")
    hr_system.remove_employee(employee_name)

# Приклад використання
hr_system = HRSystem()

while True:
    print_menu()
    option = input("Виберіть опцію: ")
    if option == '1':
        view_employee_list()
    elif option == '2':
        add_employee()
    elif option == '3':
        assign_task_to_employee()
    elif option == '4':
        update_employee_details()
    elif option == '5':
        remove_employee()
    elif option == '6':
        print("Дякую за використання нашої системи. До побачення!")
        break
    else:
        print("Некоректний ввід. Спробуйте ще раз.")


