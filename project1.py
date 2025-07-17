# Employee Management System (EMS)

# Step 1: Plan the Data Storage
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'John', 'age': 30, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Alice', 'age': 28, 'department': 'Finance', 'salary': 55000}
}

# Step 2: Define the Menu System
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 3: Add Employee Functionality
def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    if emp_id in employees:
        print("Employee ID already exists. Please enter a unique ID.")
        return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"Employee {name} added successfully.")

# Step 4: View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nEmployee Details:")
    print(f"{'ID':<10}{'Name':<20}{'Age':<5}{'Department':<15}{'Salary':<10}")
    print("-" * 60)

    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<5}{details['department']:<15}{details['salary']:<10}")

# Step 5: Search for an Employee by ID
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        details = employees[emp_id]
        print(f"Employee Found: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
    else:
        print("Employee not found.")

# Step 6: Exit the Program
if _name_ == "_main_":
    main_menu()