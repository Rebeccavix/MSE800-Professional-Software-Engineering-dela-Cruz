from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

def search_user_by_id(name, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE id = ? AND name LIKE ?",
        (user_id, '%' + name + '%')
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


# Function to create the course table
def create_course_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            unit INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a course into the course table
def insert_course(course_id, name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (id, name, unit) VALUES (?, ?, ?)", (course_id, name, unit))
        conn.commit()
        print("Course added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Course ID must be unique.")
    conn.close()

# Function to search for a course by course_id and user_name
def search_course(course_id, user_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.id, c.name, c.unit FROM course c
        JOIN enrollment e ON c.id = e.course_id
        JOIN users u ON u.id = e.user_id
        WHERE c.id = ? AND u.name LIKE ?
    """, (course_id, '%' + user_name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to create the enrollment table for user-course relationship
def create_enrollment_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollment (
            user_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (course_id) REFERENCES course(id)
        )
    ''')
    conn.commit()
    conn.close()

# Function to enroll a user in a course
def enroll_user_in_course(user_id, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Check if the user exists and if the course exists
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            print("Error: User not found.")
            return
        
        cursor.execute("SELECT id FROM course WHERE id = ?", (course_id,))
        if not cursor.fetchone():
            print("Error: Course not found.")
            return
        
        cursor.execute("INSERT INTO enrollment (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
        conn.commit()
        print("✅ User enrolled in course.")
    except sqlite3.IntegrityError:
        print("Error: Enrollment already exists.")
    conn.close()
