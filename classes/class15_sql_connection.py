

import pyodbc


connection  = pyodbc.connect('DRIVER={SQL Server};''Server=DESKTOP-BMRL1VM;''Database=master;''trusted_connection=yes;')

print('Successful')

connection.autocommit = True

my_cursor = connection.cursor()



create_db = """IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'Class151_f7')
BEGIN
    CREATE DATABASE Class151_f7;
END;
"""

aktive_db = 'use Class151_f7'
create_tb = 'create table department (DeptID int, Deptname varchar(30))'

# my_cursor.execute(create_db)
my_cursor.execute(aktive_db)
# my_cursor.execute(create_tb)



#1
insert_query = "insert into Department values (1,'HR')"
#2
insert_query = "insert into Department values ({},'{}')"
#3
insert_query = "insert into Department values (?,?)"

##1
my_cursor.execute(insert_query)

##2   
# my_cursor.execute(insert_query.format(2,'sales'))

##3
my_cursor.execute(insert_query,3,'Production')






