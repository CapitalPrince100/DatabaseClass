import pymysql

from rollback_Person import *
from rollback_Company import *
from rollback_Product import *
from rollback_Complaint import * 
from rollback_Company_Product import *

from import_Person import *
from import_Company import *
from import_Product import *
from import_Complaint import *
from import_Company_Product import *

is_success = rollback_Company_Product()
if is_success is True:
        print "rollback_Company_Product: successful"
else:
        print "rollback_Company_Product: failed"

is_success = rollback_Complaint()
if is_success is True:
        print "rollback_Complaint: successful"
else:
        print "rollback_Complaint: failed"


is_success = rollback_Person()
if is_success is True:
        print "rollback_Person: successful"
else:
        print "rollback_Person: failed"

is_success = rollback_Company()
if is_success is True:
        print "rollback_Company: successful"
else:
        print "rollback_Company: failed"


is_success = rollback_Product()
if is_success is True:
        print "rollback_Product: successful"
else:
        print "rollback_Product: failed"

print ""
'''
rollback_Company_Product() 
rollback_Complaint()
rollback_Person()
rollback_Company()
rollback_Product()
'''
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

# populate Complaint table
is_success = import_Complaint()

if is_success is True:
	print "import_Complaint: successful"
else:
	print "import_Complaint: failed"

# populate Company_Product table
is_success = import_Company_Product()

if is_success is True:
	print "import_Company_Product: successful"
else:
	print "import_Company_Product: failed"
	



