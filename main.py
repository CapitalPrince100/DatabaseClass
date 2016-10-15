import pymysql

from import_Person import *
from import_Company import *
from import_Product import *
from import_Complaint import * 

# populate Person table
is_success = import_Person()

if is_success is True:
	print "import_Person: successful"
else:
	print "import_Person: failed"


# populate Company table
is_success = import_Company()

if is_success is True:
	print "import_Company: successful"
else:
	print "import_Company: failed"


# populate Product table
is_success = import_Product()

if is_success is True:
	print "import_Product: successful"
else:
	print "import_Product: failed"

'''
# populate Company_Product table
is_success = import_Company_Product()

if is_success is True:
	print "import_Enrollment: successful"
else:
	print "import_Enrollment: failed"
'''
# populate Complaint table
is_success = import_Complaint()

if is_success is True:
	print "import_Complaint: successful"
else:
	print "import_Complaint: failed"



