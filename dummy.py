
import sqlite3
#creating database for class10
def database_db():
	class_con=sqlite3.connect("class9.db")
	#creating table and headers for the database class10
	class_con.execute(''' CREATE TABLE IF NOT EXISTS `CLASS_TABLE`(
		`ROLLNO` `INTEGER`,
		`NAME` `TEXT`,
		`MARKS` `INTEGER`,
		`PERCENTAGE` `BLOB`,
		`RESULT` `BLOB`
		);''')
	#assigning values for the database table class10 
	insertelements1=("insert into CLASS_TABLE values('13345','M.VISHNU VARDHAN REDDY','100','100','PASS')")
	insertelements2=("insert into CLASS_TABLE values('13346','M.saketh','100','100','fail')")
	insertelements3=("insert into CLASS_TABLE values('13347','M.sreedhar','100','100','fail')")
	insertelements4=("insert into CLASS_TABLE values('13348','M.vardhan','100','100','PASS')")
	insertelements5=("insert into CLASS_TABLE values('13349','M.REDDY','100','100','fail')")
	insertelements6=("insert into CLASS_TABLE values('13340','M.lovely','100','100','PASS')")
	class_con.execute(insertelements1)
	class_con.execute(insertelements2)
	class_con.execute(insertelements3)
	class_con.execute(insertelements4)
	class_con.execute(insertelements5)
	class_con.execute(insertelements6)
	class_con.commit()
	class_con.close()
database_db()
