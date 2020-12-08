from models.mysql_model import ModelMysql
from helpers.sql_quries import create_contact, find_customer_id, show_contact, delete_contact, update_contact
import logging


# controller class for contact related operations (create, show, update, delete etc.)
class ContactsController(object):
    def __init__(self):
        self.mysql_model_obj = ModelMysql()

    def create_contact(self, name, mobile, description, customerid):
        query = create_contact
        error = ""
        try:
            # Here, if query execute successfully, error variable remains empty
            # otherwise an error will be raised
            self.mysql_model_obj.insert_query(query=query, query_params=(name, mobile, description, customerid))
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
        return error

    def show_contact(self, cus_email, cus_password):
        query_1 = find_customer_id  # Query for finding customer id
        query_2 = show_contact   # Query for extracting contacts of customer id same as above
        try:
            # if Queries execute successfully, this returns a list of tuples containing
            # contact information (Means one tuple contains one contact)
            temp = self.mysql_model_obj.extract_query(query=query_1, query_params=(cus_email, cus_password))
            result = self.mysql_model_obj.extract_query(query=query_2, query_params=(temp[0][0],))
            return result
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
            return error

    def delete_contact(self, contactid, customerid):
        query = delete_contact
        error = ""
        try:
            # acts same as create_contact method
            self.mysql_model_obj.insert_query(query=query, query_params=(contactid, customerid))
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
        return error

    def update_contact(self, contactname, contactnumber, contactdescription, contactid, customerid):
        query = update_contact
        error = ""
        try:
            # acts also same as create_contact method
            self.mysql_model_obj.insert_query(query=query, query_params=(contactname, contactnumber, contactdescription, contactid, customerid))
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
        return error