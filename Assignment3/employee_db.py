import mysql.connector
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
class EmployeeManager:
    def __init__(self, host="localhost", user="root", password="password", database="company"):
        self.connection = mysql.connector.connect(host=host, user=user, password=password)
        self.cursor = self.connection.cursor(buffered=True)
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.cursor.execute(f"USE {database}")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), department VARCHAR(100), salary FLOAT)")
        self.connection.commit()
    def add(self, employee):
        self.cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", (employee.name, employee.department, employee.salary))
        self.connection.commit()
        print("employee added with id", self.cursor.lastrowid)
    def view(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        if not rows:
            print("no records")
            return
        for row in rows:
            print(f"id:{row[0]} name:{row[1]} dept:{row[2]} salary:{row[3]}")
    def update(self):
        self.cursor.execute("SELECT * FROM employees")
        if not self.cursor.fetchall():
            print("no records")
            return
        while True:
            emp_id_input = input("enter emp id to update: ").strip()
            if emp_id_input.isdigit():
                emp_id = int(emp_id_input)
                self.cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
                if self.cursor.fetchone():
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
        self.cursor.execute(f"UPDATE employees SET {field} = %s WHERE emp_id = %s", (value, emp_id))
        self.connection.commit()
        print("employee updated")
    def delete(self):
        self.cursor.execute("SELECT * FROM employees")
        if not self.cursor.fetchall():
            print("no records")
            return
        while True:
            emp_id_input = input("enter emp id to delete: ").strip()
            if emp_id_input.isdigit():
                emp_id = int(emp_id_input)
                self.cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
                if self.cursor.fetchone():
                    break
            print("employee not found")
        self.cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
        self.connection.commit()
        print("employee deleted")
    def close(self):
        self.cursor.close()
        self.connection.close()
def main():
    manager = EmployeeManager()
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
            manager.close()
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()