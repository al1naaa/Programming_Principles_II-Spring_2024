import psycopg2
import csv

# Соединение с базой данных
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="Aa1234"
)

# Создание курсора для выполнения запросов
cur = conn.cursor()

def InputData():
    name = input("Input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO telephone ("name", "phone_number") VALUES (%s, %s);', (name, number))

def Import():
    with open('data.csv', 'r') as file:
        read=csv.reader(file)
        for i in read:
            name, phone_number=i
            cur.execute(' INSERT INTO telephone("name", "phone_number") VALUES(%s, %s);', (name, phone_number))

def update_contact(name, phone_number):
    cur.execute('UPDATE telephone SET "phone_number"=%s WHERE "name"=%s', (name, phone_number))

def queryData():
    cur.execute(' SELECT * FROM telephone ')
    data = cur.fetchall()
    path = r"c:/Users/user/Desktop/PostgreSQL/query_data.txt"

    f = open(path, "w")
    for row in data:
        f.write("Name: " + str(row[0]) + "\n" + "Number: " + str(row[1]) + "\n")
    f.close()

def deleteData():
    print("Which name do ypu want to delete?\n")
    personName = input()
    cur.execute(f''' DELETE FROM telephone WHERE "name"='{personName}' ''')

def deleteAllData():
    cur.execute(' DELETE FROM telephone ')

while True:
    try:
        x = int(input())
        if x == 1:
            InputData()
            conn.commit()  # Подтверждаем изменения в базе данных после каждой вставки данных
        elif x==2:
            Import()
            conn.commit()
        elif x==3:
            name1=input("Input name:")
            phone_number1=input("Input number:")
            update_contact(name1, phone_number1)
            conn.commit()
        if x == 4:
            queryData()
            conn.commit()
        if x == 5:
            deleteData()
            conn.commit()
        if x == 6:
            deleteAllData()
            conn.commit()
        elif x==7:
            break  # Выходим из цикла
    except ValueError:
        print("Invalid input. Please enter a number.")

# Закрытие курсора и соединения
cur.close()
conn.close()