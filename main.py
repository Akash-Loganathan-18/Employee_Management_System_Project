from company import Company
from department import Department
from employee import Employee



def menu():
    print("\nEmployee Management System Menu: ")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Display Departments")
    print("4. Add Employee")
    print("5. Remove Employee")
    print("6. List Employees in Department")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")

def main():
    company = Company()
    intial_load(company)

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name to add: ")
            company.add_department(department_name)

        elif choice == '2':
            department_name = input("Enter department name to add: ")
            company.remove_department(department_name)

        elif choice == '3':
            company.diplay_departments()
        
        elif choice == '4':
            name = input("Enter employee name: ")
            employee_Id = input("Enter employee Id: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")
            if department in company.departments:
                employee = Employee(name, employee_Id, title, department)
                employee.display_Employee_Details()
                company.departments[department].add_Employee(employee)
                print("Employee added successfully.")
            else:
                print("Department does not exist.")

        elif choice == '5':
            department = input("Enter department name: ")
            if department in company.departments:
                employee_Id = input("Enter employee Id to remove: ")
                if company.departments[department].remove_Employee(employee_Id):
                    print("Employee removed successfully.")
                else:
                    print("Employrr not found.")
            else:
                print("Department does not exist.")

        elif choice == '6':
            department = input("Enter department name: ")
            if department in company.departments:
                print(f"Employees in {department}:")
                company.departments[department].list_Employees()
            else:
                print("Department does not exist.")

        elif choice == '7':
            fileName = input("Enter fileName to load data: ")
            company.save_data(fileName)
            print("Data saved successfully.")

        elif choice == '8':
            intial_load(company)

        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

def intial_load(company):
    fileName = input("Enter fileName to load data: ")
    company.load_data(fileName)
    print("data loaded successfully.")

if __name__ == "__main__":
    main()