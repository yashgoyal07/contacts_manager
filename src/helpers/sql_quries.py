from configs.mysql_config import *

# Query for create new contact by customer(user)
create_contact = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.CONTACTS_TABLE} (contactname, contactnumber, contactdescription, customerid) values(
%s, %s, %s, %s)"""

# Query for create new customer or user (used for new sign up)
create_customer = f"""INSERT INTO {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} (name, email, mob, pass) values(
%s, %s, %s, %s)"""

# Query for check customer's(user's) credentials such as email & password (used for login)
check_cred = f"""SELECT * FROM  {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} WHERE email = %s and pass = %s"""

# Query for finding Customer's id (used for showing contacts of particular customer(user))
find_customer_id = f"""SELECT * FROM {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} WHERE email = %s and pass = %s"""

# Query for showing contacts of particular customer(user) using customer's id
show_contact = f"""SELECT * FROM {MysqlConfig.USER_DATABASE}.{MysqlConfig.CONTACTS_TABLE} WHERE customerid = %s ORDER BY contactname"""

# Query for deleting particular contact of particular customer(user) using customer's id and contact's id
delete_contact = f"""DELETE FROM {MysqlConfig.USER_DATABASE}.{MysqlConfig.CONTACTS_TABLE} WHERE contactid = %s and customerid = %s"""

# Query for updating particular contact of particular customer(user) using customer's id and contact's id
update_contact = f"""UPDATE {MysqlConfig.USER_DATABASE}.{MysqlConfig.CONTACTS_TABLE} SET contactname = %s, contactnumber = %s, contactdescription = %s WHERE contactid = %s and customerid = %s"""

# Query for finding customer's(user's) details to check that this customer already exist or not (used during signup)
find_customer = f"""SELECT * FROM {MysqlConfig.USER_DATABASE}.{MysqlConfig.CUSTOMERS_TABLE} WHERE email = %s"""
