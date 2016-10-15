import pymysql
import csv
from db_connect import *

def import_Product():

    is_success = True
    insert_stmt = "insert into Product (product_type, sub_product) values (%s, %s)"

    try:

        connection = create_connection()
        cursor = connection.cursor()

        csvfile = open("Consumer_Complaints.csv", "rb")
        reader = csv.reader(csvfile)

        for i, row in enumerate(reader):
            if i == 0: continue

            for j, val in enumerate(row):
                
                if j == 1:
                    product_type = val
                elif j == 2:
                    sub_product = val
                else:
                    continue
            insert_status = run_prepared_stmt(cursor, insert_stmt, (product_type, sub_product))
            if insert_status is False:
                is_success = False;
                return is_success


        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False
            return is_success

    except pymysql.Error as e:
        print "import_Company error: " + e.strerror

    return is_success
