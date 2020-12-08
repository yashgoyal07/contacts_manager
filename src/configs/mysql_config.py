# here, your seems there's no need of making config class but i think in future,
# it will be useful.
class MysqlConfig(object):
    INSTANCE_CONFIG = {
        "local": {
            "host": "localhost",
            "port": 3306,
            "username": "root",
            "password": "#######"  # password of your database
        },
        # config for Quality Assurance environment
        "qa": {
            "host": "10.11.XX.XX",
            "port": 3306,
            "username": "root",
            "password": "#########"
        },
        # config for Production environment
        "prod": {
            "host": "10.11.XX.XX",
            "port": 3306,
            "username": "root",
            "password": "#########"}
    }

    # Database name
    USER_DATABASE = "users"

    # Table for storing contacts
    CONTACTS_TABLE = "contacts"

    # Table for storing customers
    CUSTOMERS_TABLE = "customers"
