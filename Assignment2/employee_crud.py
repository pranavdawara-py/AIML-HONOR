import pandas as pd
import os
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        if os.path.exists(self.filename):
            return pd.read_csv(self.filename)
        return pd.DataFrame(columns=["emp_id", "name", "department", "salary"])
    def add(self, employee):
        df = self.read()
        emp_id = len(df) + 1
        df.loc[len(df)] = [emp_id, employee.name, employee.department, employee.salary]
        df.to_csv(self.filename, index=False)
        print("employee added with id", emp_id)
    def view(self):
        df = self.read()
        if df.empty:
            print("no records")
            return
        for _, row in df.iterrows():
            print(f"id:{int(row['emp_id'])} name:{row['name']} dept:{row['department']} salary:{row['salary']}")
    def update(self):
        df = self.read()
        if df.empty:
            print("no records")
            return
        while True:
            emp_id_input = input("enter emp id to update: ").strip()
            if emp_id_input.isdigit():
                emp_id = int(emp_id_input)
                match = df[df["emp_id"] == emp_id]
                if not match.empty:
                    break
            print("employee not found")
        while True:
            field = input("which field to update (name/department/salary): ").strip().lower()
            if field in ["name", "department", "salary"]:
                break
            print("invalid choice")
        while True:
            value = input(f"enter new {field}: ").strip()
            if field == "salary":
                try:
                    value = float(value)
                    if value > 0:
                        break
                    print("invalid choice")
                except ValueError:
                    print("invalid choice")
            else:
                break
        df.loc[df["emp_id"] == emp_id, field] = value
        df.to_csv(self.filename, index=False)
        print("employee updated")
    def delete(self):
        df = self.read()
        if df.empty:
            print("no records")
            return
        while True:
            emp_id_input = input("enter emp id to delete: ").strip()
            if emp_id_input.isdigit():
                emp_id = int(emp_id_input)
                match = df[df["emp_id"] == emp_id]
                if not match.empty:
                    break
            print("employee not found")
        df = df[df["emp_id"] != emp_id]
        df.to_csv(self.filename, index=False)
        print("employee deleted")
def main():
    manager = EmployeeManager("employees.csv")
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("enter choice: ").strip()
        if choice == "1":
            name = input("enter name: ").strip()
            department = input("enter department: ").strip()
            while True:
                salary_input = input("enter salary: ").strip()
                try:
                    salary = float(salary_input)
                    if salary > 0:
                        break
                    print("invalid choice")
                except ValueError:
                    print("invalid choice")
            manager.add(Employee(name, department, salary))
        elif choice == "2":
            manager.view()
        elif choice == "3":
            manager.update()
        elif choice == "4":
            manager.delete()
        elif choice == "5":
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()
