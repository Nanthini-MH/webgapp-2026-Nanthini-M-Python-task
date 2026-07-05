import psycopg2
from datetime import date


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nanthini",
    port="5432"
)
conn.autocommit= True

cursor =conn.cursor()

cursor.execute("CREATE DATABASE employee_management")

cursor.close()
conn.close()


class Database:

    def __init__(self):


        self.conn = psycopg2.connect(
            host="localhost",
            database="employee_management",
            user="postgres",
            password="nanthini"
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        employee_table = """
        CREATE TABLE IF NOT EXISTS employee(
            emp_id SERIAL PRIMARY KEY,
            emp_name VARCHAR(100) NOT NULL,
            department VARCHAR(100),
            designation VARCHAR(100),
            salary DECIMAL(10,2)
        )
        """

        attendance_table = """
        CREATE TABLE IF NOT EXISTS attendance(
            attendance_id SERIAL PRIMARY KEY,
            emp_id INTEGER REFERENCES employee(emp_id)
            ON DELETE CASCADE,
            attendance_date DATE NOT NULL,
            status VARCHAR(10)
            CHECK(status IN ('Present','Absent'))
        )
        """

        self.cursor.execute(employee_table)
        self.cursor.execute(attendance_table)

        self.conn.commit()



class Employee(Database):

    def add_employee(self):

        name = input("Enter Employee Name : ")
        dept = input("Enter Department : ")
        designation = input("Enter Designation : ")
        salary = float(input("Enter Salary : "))

        query = """
        INSERT INTO employee
        (emp_name,department,designation,salary)
        VALUES(%s,%s,%s,%s)
        """

        self.cursor.execute(
            query,
            (name, dept, designation, salary)
        )

        self.conn.commit()

        print("Employee Added Successfully")

    def view_employee(self):

        self.cursor.execute(
            "SELECT * FROM employee ORDER BY emp_id"
        )

        records = self.cursor.fetchall()

        if not records:
            print("No Employees Found")
            return

        print("\nEMPLOYEE DETAILS")
        print("-" * 80)

        for row in records:
            print(
                f"ID:{row[0]} | "
                f"Name:{row[1]} | "
                f"Dept:{row[2]} | "
                f"Designation:{row[3]} | "
                f"Salary:{row[4]}"
            )

    def search_employee(self):

        emp_id = int(input("Enter Employee ID : "))

        self.cursor.execute(
            "SELECT * FROM employee WHERE emp_id=%s",
            (emp_id,)
        )

        employee = self.cursor.fetchone()

        if employee:

            print("\nEmployee Found")
            print("-" * 40)

            print("Employee ID :", employee[0])
            print("Name :", employee[1])
            print("Department :", employee[2])
            print("Designation :", employee[3])
            print("Salary :", employee[4])

        else:
            print("Employee Not Found")



class Attendance(Employee):

    def mark_attendance(self):

        emp_id = int(input("Enter Employee ID : "))

        self.cursor.execute(
            "SELECT * FROM employee WHERE emp_id=%s",
            (emp_id,)
        )

        employee = self.cursor.fetchone()

        if not employee:
            print("Employee Not Found")
            return

        status = input(
            "Enter Status (Present/Absent) : "
        ).capitalize()

        if status not in ["Present", "Absent"]:
            print("Invalid Status")
            return

        query = """
        INSERT INTO attendance
        (emp_id,attendance_date,status)
        VALUES(%s,%s,%s)
        """

        self.cursor.execute(
            query,
            (emp_id, date.today(), status)
        )

        self.conn.commit()

        print("Attendance Marked Successfully")

    def view_attendance(self):

        query = """
        SELECT
            e.emp_id,
            e.emp_name,
            a.attendance_date,
            a.status
        FROM attendance a
        JOIN employee e
        ON a.emp_id = e.emp_id
        ORDER BY a.attendance_date
        """

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if not records:
            print("No Attendance Records")
            return

        print("\nATTENDANCE DETAILS")
        print("-" * 80)

        for row in records:

            print(
                f"ID:{row[0]} | "
                f"Name:{row[1]} | "
                f"Date:{row[2]} | "
                f"Status:{row[3]}"
            )

    def attendance_percentage(self):

        emp_id = int(input("Enter Employee ID : "))

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE emp_id=%s
            """,
            (emp_id,)
        )

        total_days = self.cursor.fetchone()[0]

        if total_days == 0:
            print("No Attendance Records")
            return

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE emp_id=%s
            AND status='Present'
            """,
            (emp_id,)
        )

        present_days = self.cursor.fetchone()[0]

        percentage = (present_days / total_days) * 100

        print("\nAttendance Percentage")
        print("-" * 40)
        print(f"{percentage:.2f}%")

    def salary_report(self):

        emp_id = int(input("Enter Employee ID : "))

        self.cursor.execute(
            """
            SELECT emp_name,salary
            FROM employee
            WHERE emp_id=%s
            """,
            (emp_id,)
        )

        employee = self.cursor.fetchone()

        if not employee:
            print("Employee Not Found")
            return

        emp_name = employee[0]
        salary = float(employee[1])

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE emp_id=%s
            """,
            (emp_id,)
        )

        total_days = self.cursor.fetchone()[0]

        if total_days == 0:
            print("No Attendance Records")
            return

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE emp_id=%s
            AND status='Present'
            """,
            (emp_id,)
        )

        present_days = self.cursor.fetchone()[0]

        attendance_percent = (
            present_days / total_days
        ) * 100

        payable_salary = (
            salary * attendance_percent
        ) / 100

        print("\nSALARY REPORT")
        print("-" * 50)

        print("Employee Name :", emp_name)
        print("Base Salary :", salary)
        print("Total Working Days :", total_days)
        print("Present Days :", present_days)
        print(
            f"Attendance Percentage : "
            f"{attendance_percent:.2f}%"
        )
        print(
            f"Payable Salary : "
            f"{payable_salary:.2f}"
        )

    def close_connection(self):

        self.cursor.close()
        self.conn.close()



obj = Attendance()

while True:

    print("\n")
    print("=" * 50)
    print("EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Mark Attendance")
    print("5. View Attendance")
    print("6. Attendance Percentage")
    print("7. Salary Report")
    print("8. Exit")

    try:
        choice = int(input("Enter Choice : "))

        if choice == 1:
            obj.add_employee()

        elif choice == 2:
            obj.view_employee()

        elif choice == 3:
            obj.search_employee()

        elif choice == 4:
            obj.mark_attendance()

        elif choice == 5:
            obj.view_attendance()

        elif choice == 6:
            obj.attendance_percentage()

        elif choice == 7:
            obj.salary_report()

        elif choice == 8:
            obj.close_connection()
            print("Thank You...")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please Enter Numeric Choice Only")