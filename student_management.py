import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Ankita25",  
    database="student_db"
)

cursor = db.cursor()

# ADD STUDENT
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    db.commit()

    print("Student added")

# VIEW STUDENTS
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- Student List ---")
    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")

# SEARCH STUDENT
def search_student():
    id = int(input("Enter ID to search: "))
    query = "SELECT * FROM students WHERE id=%s"
    cursor.execute(query, (id,))
    result = cursor.fetchall()

    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")

# UPDATE STUDENT
def update_student():
    id = int(input("Enter ID to update: "))
    new_course = input("Enter new course: ")

    query = "UPDATE students SET course=%s WHERE id=%s"
    cursor.execute(query, (new_course, id))
    db.commit()

    print("✅ Updated")

# DELETE STUDENT
def delete_student():
    id = int(input("Enter ID to delete: "))

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    print("❌ Deleted")

# MENU
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        break
    else:
        print("Invalid choice")