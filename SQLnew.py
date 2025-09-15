import psycopg2

conn = psycopg2.connect(
    dbname="mydb", 
    password="myuser", 
    user="myuser", 
    host="localhost", 
    port="5432"
)

cursor = conn.cursor()

# !!! Вивід значення з таблиці
# cursor.execute("SELECT * FROM employees")
# employees = cursor.fetchall()
# for emp in employees:
#     print(emp)

# !!! Додано нове значення
# a = 'Natan'
# b = 'Khlemenko'
# c = 'HR'
# d = 2000
# cursor.execute("INSERT INTO employees (first_name, last_name, department, salary) VALUES (%s, %s, %s, %s)", (a, b, c, d))
# conn.commit()

# !!! Оновнено старе значення
# cursor.execute("UPDATE employees SET salary = %s WHERE last_name = %s", (2500, "Khlemenko"))
# conn.commit()

# !!! Функція фільтру за показником
# def get_employees_by_department(department_name: str) -> list:
       
#     cursor.execute("SELECT * FROM employees WHERE department = %s", (department_name, ))
#     employees = cursor.fetchall()
#     if not employees:
#                 print("No one employees there")
#     else:
#         for emp in employees:
#             print(f"Employee: {emp[1]} {emp[2]} | Department: {department_name}")
    
# while True:
#     wanna_see = input("Wanna see employeers in Department \nY / N\n")
    
#     if wanna_see == 'Y':
#         department_name = input("Department name: ") 
#         get_employees_by_department(department_name)

#     else:
#         break

# !!!   
# def get_high_salary(min_salary: float) -> list:
       
#     cursor.execute("SELECT * FROM employees WHERE salary > %s", (min_salary, ))
#     employees = cursor.fetchall()
#     if not employees:
#                 print("No one employees there")
#     else:
#         for emp in employees:
#             print(f"Employee: {emp[1]} {emp[2]} | Department: {emp[3]} | Salary: {emp[4]}")
    
# while True:
#     wanna_see = input("Wanna see employeers with Salary \nY / N\n")
    
#     if wanna_see == 'Y':
#         min_salary = float(input("Min Salary: ")) 
#         get_high_salary(min_salary)

#     else:
#         break

# !!! Взаємодія данних
# def transfer_salary(sender_id: int, receiver_id: int, amount: float):

#     cursor.execute("SELECT * FROM employees WHERE id = %s", (sender_id, ))
#     sender_salary = cursor.fetchone()

#     if not sender_id:
#         print("Sender not found")
#         return
    
#     sender_salary = sender_salary[4]

#     if sender_salary >= amount:
#         cursor.execute("UPDATE employees SET salary = salary - %s WHERE id = %s", (amount, sender_id))
#         cursor.execute("UPDATE employees SET salary = salary + %s WHERE id = %s", (amount, receiver_id))
#         conn.commit()
#         print("Transfer successful")
    
#     else:
#         conn.rollback()
#         print("Not enough money")

# while True:
#     make_transfer = input("Wanna make transfer \nY / N \n")
#     if make_transfer == 'Y':
#         sender_id = int(input("Enter |Sender ID| "))
#         receiver_id = int(input("Enter |Receiver ID| "))
#         amount = float(input("Enter |Amount| "))
#         transfer_salary(sender_id, receiver_id, amount)
#     else:
#         break

# !!! Середня ЗП
# def get_average_salary(department_name: str):
#     cursor.execute("SELECT AVG(salary) FROM employees WHERE department = %s", (department_name, ))
#     average_salary = cursor.fetchall()
#     print(f"Department: {department_name} | Arerage salary: {average_salary}")

# def what_department(department_name: str) -> bool:
#         cursor.execute("SELECT 1 FROM employees WHERE department = %s LIMIT 1", (department_name, ))
#         return cursor.fetchone() is not None

# while True:
#     wanna_know = input("Wanna now average salary of Department \nY / N\n")

#     if wanna_know == 'Y':
#         department_name = input("What Department?\n")

#         department = what_department(department_name)      
        
#         if not department:
#             print("Unknown Department!")
#         else:
#             get_average_salary(department_name)
#     else:
#         break


def get_employee_count_by_department():
    cursor.execute("SELECT department, COUNT(*) FROM employees GROUP BY department")
    results = cursor.fetchall()
    for department, count in results:
        print(f"{department}: {count} employees")

while True:
    wanna_know = input("Wanna now how many employees on Department \nY / N\n")
    if wanna_know == 'Y':
        get_employee_count_by_department()
    else:
        break


# Найвища ЗП
# def get_top_employee():
#     cursor.execute("SELECT first_name, last_name, department, salary FROM employees ORDER BY salary DESC LIMIT 1")
#     top_employee = cursor.fetchone()
#     print(top_employee)
# while True:
#     wanna_get = input("Wanna get top employee? \nY / N\n")
#     if wanna_get == 'Y':
#         get_top_employee()
#     else:
#         break


        

cursor.close()
conn.close()