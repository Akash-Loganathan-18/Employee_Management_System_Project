class Employee:
    def __init__(self, name, employee_Id, title, department):
        self.name = name
        self.employee_Id = employee_Id
        self.title = title
        self.department = department

    def display_Employee_Details(self):
        print(f"Name: {self.name}\nId: {self.employee_Id}\nTitle: {self.title}\nDepartment: {self.department}")

    def __str__(self):
        return f"{self.name} - Id: {self.employee_Id}"

        