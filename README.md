# Contacts Manager

Web Application to store and manage contacts.

## Installation

Clone this directory in your system.

Install Python 3.8.5

Upgrade PIP

```bash
python3 -m pip install --user --upgrade pip
```
Install virtual environment

```bash
python -m pip install --user virtualenv
```
cd to directory 'contacts_manager' (change directory)

Create a virtual environment

```bash
python3 -m venv venv
```
Activate the virtual environment

```bash
source venv/bin/activate
```
Install Flask in this virtual environment

```bash
pip install Flask
```
Deactivate virtual environment

```bash
deactivate
```
cd into main directory using 'cd ~'

Install mysql according to this [documentation] (https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing)

After mysql installation, connecting to mysql server  

```bash
mysql -u root -p
```
Enter password which you make during installation.

Run commands in sequence given below in mysql> prompt:

```SQL
CREATE DATABASE users;

```SQL
USE users

```SQL
CREATE TABLE customers
	(
	  id              INT NOT NULL AUTO_INCREMENT, 		# Unique ID for the customer
	  name            VARCHAR(100) NULL,                # Name of the customer
	  email           VARCHAR(100) NULL,                # Email of the customer
	  mob             VARCHAR(20) NULL,                 # Mobile of the customer
	  pass            VARCHAR(50) NULL,					# Password of the customer
	  PRIMARY KEY     (id)                              # Make the id the primary key
	);

```SQL
CREATE TABLE contacts
	(
	  contactid              INT NOT NULL AUTO_INCREMENT, 		        # Unique ID for the contact
	  contactname            VARCHAR(100) NOT NULL,                     # Name of the contact
	  contactnumber          VARCHAR(20) NOT NULL,                      # Contact Number of the contact
	  contactdescription     VARCHAR(100) NULL,                         # Description of the contact
	  customerid			 INT NULL,									# Customer id 
	  PRIMARY KEY     		 (contactid),                               # Make the contactid the primary key
	  FOREIGN KEY 			 (customerid) REFERENCES customers(id)      # Make the customerid the foreign key
	);

```SQL
exit

Again cd to directory 'contacts_manager' (change directory)

Activate the virtual environment

```bash
source venv/bin/activate
```

Install mysql-connector-python using command given below

```bash
python -m pip install mysql-connector-python
```
After that runs command given below with path of src folder of contacts_manager directory

```bash
export PYTHONPATH=:/home/yash/documents/contacts_manager/src
```

Now open 'mysql_config.py' in config folder of src folder of 'contacts_manager' directory in text-editor.

Replace "######" password of local key of INSTACE_CONFIG dictionary with your mysql password which you make during installation of mysql.

Now open 'views.py' in views folder of src folder of 'contacts_manager' directory in text-editor.

Replace "################" password of app.secret.key from key obtained by steps goven below.

Step-1: Go to terminal, deactivate the virtual environment, then go to main directory by using 'cd ~'

Step-2: Run this command

```bash
python3 -c 'import os; print(os.urandom(16))'
```
Step-3: Copy whole output which is in the form like "b'############'" something.

Step-4: Paste into field of app.secret.key = "############" into above mentioned file.

Again cd to directory 'contacts_manager'

Activate the virtual environment

Run the following command:

```bash
python3 src/views/views.py
```
Open browser.

Go to 'http://127.0.0.1:5000/' and webapp starts working. !!!!