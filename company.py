import json
from department import Department
from employee import Employee


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_Name):
        if department_Name not in self.departments:
            self.departments[department_Name] = Department(department_Name)
            print(f"Department {department_Name} added successfully")
        else:
            print (f"The Department already exists")

    def remove_department(self, department_Name):
        if department_Name in self.departments:
            self.departments.pop(department_Name)
            print(f"Department {department_Name} removed successfully.")
        else:
            print(f"The Department does not exist.")

    def diplay_departments(self):
        print("Departments:")
        for key, value in self.departments.items():
            print(f"Key: {key}")
            value.list_Employees()

    def save_data(self, fileName):
        with open(fileName, 'w') as file:
            json.dump(self.departments, file, default = lambda o: o.__dict__)

    def load_data(self, fileName):
        try:
            with open(fileName, 'r') as file:
                self.departments = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{fileName}' Not found.")
        except Exception as e:
            print(f"Error: Failed to load data from '{fileName}': {e}")
            