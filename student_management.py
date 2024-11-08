import sqlite3

con = sqlite3.connect("student.db")
cursor = con.cursor()

institute_name = input("Enter Your Institute Name: ")

cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{institute_name}" (student_name TEXT, student_class INT, roll_no INT)''')
con.commit()

def add_student(student_name, student_class, roll_no):
    cursor.execute(f'''SELECT * FROM "{institute_name}" WHERE roll_no = ?''', (roll_no,))
    student = cursor.fetchone()
    if student:
        print(f"This Student Already Exists\nName: {student_name}\nClass: {student_class}\nRoll No: {roll_no}")
    else:
        cursor.execute(f'''INSERT INTO "{institute_name}" (student_name, student_class, roll_no) VALUES (?, ?, ?)''',
                    (student_name, student_class, roll_no))
        con.commit()
        print(f"Successfully Added Student\nStudent Name: {student_name}\nStudent Class: {student_class}\nRoll No: {roll_no}")

def config_all_students():
    cursor.execute(f'''SELECT * FROM "{institute_name}"''')
    all_students = cursor.fetchall() 
    
    if all_students:
        for student in all_students:
            student_dict = {
                "Student Name":student[0],
                "Student Class": student[1],
                "Roll No": student[2]
            }
            print(student_dict)
    else:
        print(f"No students found in {institute_name}")
def remove_student(roll_no):
    cursor.execute(f'''SELECT * FROM "{institute_name}" WHERE roll_no = ?''', (roll_no,))
    student = cursor.fetchone()
    if student:
        cursor.execute(f'''DELETE FROM "{institute_name}" WHERE roll_no = ?''', (roll_no,))
        con.commit()
        print(f"Successfully Removed Student with Roll No: {roll_no}")
    else:
        print(f"This Student Doesn't Exist In {institute_name}")

print(f'Welcome To {institute_name} Management System!')

choice = input("Enter Your Choice (add, remove, config): ").lower()

if choice == "config":
    config_all_students()  
else:
    student_name = input("Enter Student Name: ")
    student_class = input("Enter Student Class: ")
    roll_no = int(input("Enter Student Roll No: "))

    if choice == "add":
        add_student(student_name, student_class, roll_no)
    elif choice == "remove":
        remove_student(roll_no)

con.close()
