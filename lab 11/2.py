import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Aa1234"
)
cur = conn.cursor()

def queryData():
    cur.execute("SELECT * FROM get_records_by_pattern('John')")
    data = cur.fetchall()

    for row in data:
        print(row)


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone VARCHAR(15) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    print("Table created successfully.")

def upload_data_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                row
            )
    conn.commit()
    print("Data uploaded from CSV successfully.")

def insert_data_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "CALL insert_or_update_user(%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    print("Data entered from console successfully.")

def update_data(first_name, new_phone=None, new_first_name=None):
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, first_name))
    if new_first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_first_name, first_name))
    conn.commit()
    print("Data updated successfully.")

def query_data_by_pattern(pattern):
    cur.execute("SELECT * FROM get_records_by_pattern(%s)", (pattern,))
    results = cur.fetchall()
    return results

def delete_data(mode, identifier):
    cur.execute("CALL delete_data_by_username_or_phone(%s, %s)", (mode, identifier))
    conn.commit()
    print("Data deleted successfully.")

def paginated_query(limit, offset):
    cur.execute("SELECT * FROM paginating(%s, %s)", (limit, offset))
    results = cur.fetchall()
    return results

# Example of using the functions
if __name__ == "__main__":
    create_table()
    # upload_data_from_csv('phonebook_data.csv')
    # print(query_data_by_pattern("John"))
    # insert_data_from_console()
    # update_data('John', new_phone='1234567890')
    # print(paginated_query(10, 0))
    # delete_data('username', 'John')
