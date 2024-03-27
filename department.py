class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees_List = []

    def add_Employee(self, employee):
            self.employees_List.append(employee)

    def remove_Employee(self, employee_Id):
        for emp in self.employees_List:
            if emp.employee_Id == employee_Id:
                self.employees_List.remove(emp)
                return True
            else:
                return False
            
    def list_Employees(self):
        for emp in self.employees_List:
            print(f"Name: {emp.name}, ID: {emp.employee_Id}, Title: {emp.title} Department: {emp.department}")

    def __str__(self):
        return f"Department Name: {self.department_name}"