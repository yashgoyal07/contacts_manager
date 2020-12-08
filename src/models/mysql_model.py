import mysql.connector
from helpers.utils import get_environment
from configs.mysql_config import MysqlConfig


# model class for communication with mysql or any database.
class ModelMysql(object):
    def __init__(self):
        self.infra_env = get_environment()  # function from utils file of helpers package

        # initialization below is basically give particular mysql config from INSTANCE_CONFIG
        # from configs package according to environment(local, QA or prod)
        self.instance_config = MysqlConfig.INSTANCE_CONFIG.get(self.infra_env, {})

    # This method return an connection from mysql database using mysql.connector
    def get_connection(self):
        connection = mysql.connector.connect(host=self.instance_config.get("host"),
                                             port=self.instance_config.get("port"),
                                             user=self.instance_config.get("username"),
                                             password=self.instance_config.get("password"),
                                             )
        return connection

    # method for executing queries which are not return any result such as insert, delete etc.
    def insert_query(self, query, query_params):
        connection = self.get_connection()
        cur = connection.cursor()
        cur.execute(query, query_params)
        connection.commit()
        cur.close()

    # method for executing queries which are return results such as select etc.
    def extract_query(self, query, query_params):
        connection = self.get_connection()
        cur = connection.cursor()
        cur.execute(query, query_params)
        result = cur.fetchall()  # here, fetchall returns list of tuples
        connection.commit()
        cur.close()
        return result  # returns result
