import pymysql
from db_connect import *

def rollback_Person():

    try:

        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM Person"
        cursor.execute(query) 
        connection.commit()

    except pymysql.Error as e:
        print "import_Person error:" + e.strerror
