employees = []
running = True

while running:
    print("\n===== Welcome to WorkTrack: Employee Record Management System =====\n")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit\n")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        emp = {}

        # Employee ID validation
        while True:
            emp_id = input("\nEnter Employee ID (numbers only): ").strip()
            if not emp_id.isdigit():
                print("Invalid ID. Please enter numbers only.")
                continue
            if any(e['Employee ID'] == emp_id for e in employees):
                print("Employee ID already exists. Please enter a unique ID.")
                continue
            emp['Employee ID'] = emp_id
            break

        # First Name
        while True:
            fname = input("Enter First Name: ").strip()
            if fname:
                emp['First Name'] = fname.capitalize()
                break
            print("First Name cannot be blank.")

        # Last Name
        while True:
            lname = input("Enter Last Name: ").strip()
            if lname:
                emp['Last Name'] = lname.capitalize()
                break
            print("Last Name cannot be blank.")

        # Gender
        while True:
            gender = input("Enter Gender (Male/Female): ").strip().capitalize()
            if gender in ['Male', 'Female']:
                emp['Gender'] = gender
                break
            print("Invalid gender. Please enter Male or Female.")

        # Position
        valid_positions = ['Full-time', 'Part-time', 'Seasonal', 'Intern']
        while True:
            position = input("Enter Position (Full-time, Part-time, Seasonal, Intern): ").strip().capitalize()
            if position in [p.capitalize() for p in valid_positions]:
                emp['Position'] = position
                break
            print("Invalid position. Please enter one of the listed options.")

        # Salary
        while True:
            salary_input = input("Enter Salary (numbers only, without ₱): ").replace(",", "").strip()
            if not salary_input.replace('.', '', 1).isdigit():
                print("Invalid salary. Please enter numbers only.")
                continue
            salary = float(salary_input)
            emp['Salary'] = f"₱{salary:,.2f}"
            break

        employees.append(emp)
        print("\nEmployee added successfully!")

    elif choice == '2':
        if not employees:
            print("\nNo employee records found.")
        else:
            for emp in employees:
                print("\n----------------------")
                for key in emp:
                    print(f"{key}: {emp[key]}")

    elif choice == '3':
        search = input("\nEnter Employee ID or keyword: ").lower()
        found = False
        for emp in employees:
            if search == emp['Employee ID'].lower() or any(search in str(value).lower() for value in emp.values()):
                print("\nEmployee Found:")
                for key in emp:
                    print(f"{key}: {emp[key]}")
                found = True
        if not found:
            print("\nNo matching employee found.")

    elif choice == '4':
        update_id = input("\nEnter Employee ID to update: ")
        for emp in employees:
            if emp['Employee ID'] == update_id:
                print("Leave blank to keep current value.")
                for key in ['First Name', 'Last Name', 'Gender', 'Position', 'Salary']:
                    new_value = input(f"New {key} [{emp[key]}]: ").strip()
                    if new_value:
                        if key == 'Gender':
                            if new_value.capitalize() in ['Male', 'Female']:
                                emp[key] = new_value.capitalize()
                            else:
                                print("Invalid gender. Skipped update.")
                        elif key == 'Position':
                            if new_value.capitalize() in ['Full-time', 'Part-time', 'Seasonal', 'Intern']:
                                emp[key] = new_value.capitalize()
                            else:
                                print("Invalid position. Skipped update.")
                        elif key == 'Salary':
                            salary_input = new_value.replace(",", "").replace("₱", "")
                            if salary_input.replace('.', '', 1).isdigit():
                                salary = float(salary_input)
                                emp[key] = f"₱{salary:,.2f}"
                            else:
                                print("Invalid salary. Skipped update.")
                        else:
                            emp[key] = new_value.capitalize()
                print("\nEmployee updated successfully!")
                break
        else:
            print("\nEmployee not found.")

    elif choice == '5':
        delete_id = input("\nEnter Employee ID to delete: ")
        for emp in employees:
            if emp['Employee ID'] == delete_id:
                employees.remove(emp)
                print("\nEmployee deleted successfully.")
                break
        else:
            print("\nEmployee not found.")

    elif choice == '6':
        print("\nThank you for using WorkTrack, Goodbye!\n")
        running = False

    else:
        print("\nInvalid choice. Please try again.")
