# flask-app
Secure complex web application in Python using the Flask framework. 

The web application serves as a tool for browsing employee records. The records include basic information about the employees such as their address, email, role, and contact details. The database contains two tables. One table is used to store information about the employees who have a contract of employment with the company and the second table contains information about the employees who are non-contract workers or are temporary workers. 

Two types of users exist: regular and admin. Regular users need to register before login. The regular user can browse the records, read, add records and edit employee information. The admin user is able to perform all CRUD operations.
The admin user credentials:
email: "admin@cisco.com"
password: "Cisco123!"

Flask has been used as the framework for developing the web application in the python language. SQLAlchemy is the SQL toolkit used to gain easy access to and interact with the SQLite database. 

To run the app, run the following commands:
$pip install -r requirements.txt       
$make run

