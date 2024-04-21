import csv
import psycopg2

# Database connection parameters
dbname = "test"
user = "postgres"
password = "Aa1234"

def create_table():
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone VARCHAR(15) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully.")

def upload_data_from_csv(file_path):
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                row
            )
    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded from CSV successfully.")

def insert_data_from_console():
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Data entered from console successfully.")

def update_data(first_name, new_phone=None, new_first_name=None):
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    if new_phone:
        cursor.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, first_name))
    if new_first_name:
        cursor.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_first_name, first_name))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data updated successfully.")

def query_data(filter_condition):
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM phonebook WHERE {filter_condition}")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def delete_data(first_name=None, phone=None):
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cursor = conn.cursor()
    if first_name:
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (first_name,))
    if phone:
        cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data deleted successfully.")

# Example of using the functions
if __name__ == "__main__":
    create_table()
    # upload_data_from_csv('phonebook_data.csv')
    # insert_data_from_console()
    # print(query_data("first_name = 'John'"))
    # update_data('John', new_phone='1234567890')
    # delete_data(first_name='John')
