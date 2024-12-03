import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};''Server=DESKTOP-BMRL1VM;''Database=master;''trusted_connection=yes;')
connection.commit()
connection.autocommit = True

cursor1 = connection.cursor()


# create_db = 'create database Class15_F7'
# cursor1.execute(create_db)


active_db = 'use Class15_F7'
cursor1.execute(active_db)

# create_table = 'create table employee (id int, name varchar(50), phone varchar (50))'
# cursor1.execute(create_table)

insert_employee = "insert into employee values ({}, '{}', '{}' )"
cursor1.execute(insert_employee.format(5,'Saida','91 425 00 12'))
cursor1.execute(insert_employee.format(6,'Yusuf','91 988 00 88'))
cursor1.execute(insert_employee.format(7,'Atabay','90 399 06 12'))

select_query = 'select * from employee'
cursor1.execute(select_query)
print('OK')