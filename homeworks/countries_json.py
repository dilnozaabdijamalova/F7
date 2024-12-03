import pyodbc
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.freetestapi.com/api/v1/countries'

respo = requests.get(url)

data = respo.json()

connection = connection = pyodbc.connect('DRIVER={SQL Server};''Server=DESKTOP-BMRL1VM;''Database=master;''trusted_connection=yes;')

connection.autocommit = True
cursor1 = connection.cursor()


create_DB = """ IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'Homework_15')
BEGIN
    CREATE DATABASE Homework_15;
END;
"""
# cursor1.execute(create_DB)

active_db = 'use Homework_15'
cursor1.execute(active_db)


for row in data:
    row.pop(list(row.keys())[-1]) 

for obj in data:
    obj.popitem()


create_tab = " create table countries_from_json ( "

for column in data[0].keys():
    create_tab = create_tab + column + ' ' + 'nvarchar(150), '

create_tab = create_tab[:-2] + ')'
cursor1.execute(create_tab)

inserting_data = 'insert into countries_from_json values ('

for obj in data:
    for val in map(str,obj.values()): 
        val = val.replace("'", "''")
        inserting_data = inserting_data  + f"'{val}'" + ','
    inserting_data = inserting_data[:-1] + ')' + ',('
inserting_data = inserting_data[:-2]

cursor1.execute(inserting_data)   


print('ok')