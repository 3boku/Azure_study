import sqlite3

def create_table():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS `students` 
                    (id INTEGER PRIMARY KEY, name TEXT, 
                    age INTEGER, major TEXT)''')
    
    connection.commit()
    connection.close()

create_table()

def insert_student(name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO students (name, age, major)
                        VALUES (?, ?, ?)''', (name, age, major))
    
    connection.commit()
    connection.close()

#insert_student("john", 21, "computer science")
#insert_student("lee", 25, "computer science")
#insert_student("john", 21, "computer science")
#insert_student("lee", 25, "computer science")

def query_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    connection.close()

    return rows


def update_student(student_id, name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute('''UPDATE students SET name = ?,
                        age = ?, major = ? WHERE id = ?''',
                        (name, age, major, student_id))
    
    connection.commit()
    connection.close()

update_student(1, "kim", 20, "robotics")
update_student(4, "lee", 25, "computer engineering")
    

def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    
    connection.commit()
    connection.close()

delete_student(2)
delete_student(3)
print(query_students())