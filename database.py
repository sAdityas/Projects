import mysql.connector #Importing the MYSQL library

#Creating Connection the DataBase
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Panda@2611',
    database = 'emp'
)
#Creating a cursor that will help to execute all the commands
cursor = connection.cursor()

#Checking if the table already exists if not then Creating a new table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS employees ( 
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               first_name VARCHAR(20) NOT NULL,
               last_name VARCHAR(20) NOT NULL,
               email VARCHAR(100) NOT NULL,
               department VARCHAR(20) NOT NULL,
               salary INT DEFAULT "20000"
               ) """)
connection.commit()

#To get the last Employee ID
def get_last_employee():
    cursor.execute("SELECT MAX(id) AS max_id FROM employees")
    result = cursor.fetchone()

    #following checks if the result is None or the result instance is a tuple and if it is then is results first index None
    if result is None or (isinstance(result, tuple) and result[0] is None):
        return 0  # Return 0 if no employees exist
    
    # Check if result is a tuple and return the id 
    if isinstance(result, tuple):  # If result is a tuple then it is accessed by index
        last_id = result[0]
    elif isinstance(result, dict):  # If result is a dictionary it is then accessed by key
        last_id = result.get('MAX(id)', 0)  # Using key from the query alias created 
    else:
        last_id = 0
    
    # Ensure last_id is a number (int), defaulting to 0 if invalid
    if isinstance(last_id, (int, float)):
        return int(last_id)  # Return last_id as integer
    return 0  # Default return if last_id is not valid

#Function to Insert Employees in the Table
def insert_employee():
    try:
        last_id = get_last_employee()
        new_id = last_id + 1 #Adds 1 to the last employee id works as Auto-Increment Function in MYSQL

        print(f"The last employee was :",{last_id},"The new employee ID will be :",{new_id})

        #Getting manual Input from the user to enter data in the table
        first_name = input("Enter Employee's First Name : ")
        last_name = input("Enter Employee's Last Name : ")
        email = input("Enter Employee's E-mail ID : ")
        department = input("Enter Employee's Department : ")
        salary = int(input("Enter Employee's Salary : "))

        #Using the %s as it is a universal placeholder and also to treat the entry as a data rather than a executable code to prevent SQL Injection Attacks
        cursor.execute("""INSERT INTO employees(id, first_name, last_name, email, department, salary)
                   VALUES(%s,%s,%s,%s,%s,%s)""", (new_id,first_name,last_name,email,department,salary))
        #commiting the changes
        connection.commit()

        print("Employee Added Successfully!!")
    except Exception as e:
        print(e)

#running a while loop for the Menu Options
while True:
    insert_employee()
    option = input("Do you want to add another Employee? (Yes/No) : ").upper()
    if option != "YES":
        break

#Executing Select all command to fetchall the data from database and print it
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("\n All Employees : ")

for row in rows:
    print(row)

#closing the cursor and connection is important
cursor.close()
connection.close()