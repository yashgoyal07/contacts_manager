from flask import session
import os


# function to pass environment on which mysql is deployed such as local, QA or production.
def get_environment():
    return os.environ.get("my_env", "local")


# function for checking that customer or user already logged in or not
# using cookies or we can say flask sessions.
def is_login():
    if 'email' and 'password' in session:
        return True
    else:
        return False
