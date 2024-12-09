Here's the complete `README.md` file with everything in markdown format for easy copying:

```markdown
# Employee Management System

This project demonstrates how to manage employee records in a MySQL database using Python. It allows users to insert new employee records into the database, view all employees, and showcases how to connect to MySQL, execute SQL queries, and handle user inputs.

## Features
- Connects to a MySQL database.
- Creates a table if it doesn't exist.
- Inserts employee records into the database.
- Displays the list of all employees from the database.
- Prevents SQL injection by using parameterized queries (`%s` placeholders).
- Prompts the user for input and inserts it into the database.

## Prerequisites

Before running the project, ensure that you have the following:

1. **MySQL Server**:
   - Make sure MySQL is installed on your machine.
   - You should have a MySQL server running on your localhost or the configured host.

2. **Python**:
   - Python 3.x installed on your machine.

3. **Required Python Libraries**:
   - `mysql-connector-python` library for connecting to MySQL from Python.
   
   To install it, run the following:
   ```bash
   pip install mysql-connector-python
   ```

4. **MySQL Database Setup**:
   - You need to have a MySQL database created named `emp`. The script will connect to this database.
   - You must have the necessary privileges to create tables and perform queries.

## How to Run

1. Clone or download the repository.

2. Modify the following credentials in the code to match your MySQL configuration:
   - `host`: The host where your MySQL server is running (e.g., `'localhost'`).
   - `user`: Your MySQL username (e.g., `'root'`).
   - `password`: Your MySQL password.
   - `database`: The database you want to use (in this case, `'emp'`).

3. Run the script:
   ```bash
   python employee_management.py
   ```

4. The script will prompt you to enter details for new employees. After entering the data, the new employee record will be added to the database.

5. You can add multiple employees in a session. After finishing, the script will print all employee records from the database.

## Code Overview

### MySQL Connection Setup
- **`mysql.connector.connect()`**: Used to establish a connection to the MySQL server. The connection parameters include the host, user, password, and database.

### Table Creation
- The script checks if the `employees` table already exists and creates it if not.
- The table contains columns: `id`, `first_name`, `last_name`, `email`, `department`, and `salary`.

### Insert Employee
- The function `insert_employee()` collects user input for the employee's details.
- It then inserts the data into the `employees` table using a parameterized query (`%s`).
- The `get_last_employee()` function retrieves the ID of the last inserted employee to simulate an auto-increment behavior (if required).

### Fetching Employee Data
- After adding employees, the script fetches and displays all employee records from the database using the `SELECT * FROM employees` query.

### Ending the Program
- The program runs in a loop, allowing the user to insert multiple employees until they decide to stop.

### Closing Database Connection
- The connection and cursor are properly closed after the operations to free up resources.

## Contributing

Feel free to fork this project and make any changes. If you have suggestions or find bugs, please create an issue or submit a pull request.
