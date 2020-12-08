from models.mysql_model import ModelMysql
from helpers.sql_quries import create_customer, check_cred, find_customer
import logging


# controller class for customers(user) related operations
# such as create customer, find customer details (id, name)
# and check credentials of customer who wants login.
class CustomersController(object):
    def __init__(self):
        self.mysql_model_obj = ModelMysql()

    def create_customer(self, name, email, mobile, password):
        query_1 = find_customer
        query_2 = create_customer
        error = ""
        try:
            # this query find whether customer(user) has signed up already or not
            result = self.mysql_model_obj.extract_query(query=query_1, query_params=(email,))
            if result[0][1] == name:
                # if customer(user) is new, Query below will create new customer
                self.mysql_model_obj.insert_query(query=query_2, query_params=(name, email, mobile, password))
            else:
                raise ValueError
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
        return error

    def find_customer(self, email, password):
        query = check_cred
        try:
            # if Queries execute successfully, this returns a list of one tuple containing
            # customer information (such as id, name, mobile, email, password etc)
            result = self.mysql_model_obj.extract_query(query=query, query_params=(email, password))
            return result[0][0]  # returns only customer's id
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
            return error

    def check_cred(self, email, password):
        query = check_cred
        error = ""
        try:
            # this query check that the customer with these email & password is exist or not
            # if exist, then if condition checks that returned email & password is equal or not
            # to the given credentials
            result = self.mysql_model_obj.extract_query(query=query, query_params=(email, password))
            if result[0][2] == email and result[0][4] == password:
                pass
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
        return error

    def find_customer_name(self, email, password):
        query = check_cred
        try:
            # here, check_cred queries is used to prevent duplication, Because we want only
            # customer(user) name.
            result = self.mysql_model_obj.extract_query(query=query, query_params=(email, password))
            return result[0][1]  # returns only customer's name
        except Exception as err:
            logging.error(f"jaan gyi due to {err}")
            error = "something went wrong"
            return error