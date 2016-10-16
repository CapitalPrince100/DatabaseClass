import pymysql 
from db_connect import *

def rollback_Company_Product():
	try:

		connection = create_connection()
		cursor = connection.cursor()

		query = "DELETE FROM Company_Product" 

		cursor.execute(query)
		connection.commit()
		
	except pymysql.Error as e:
		print "import_Person error:" + e.strerror		