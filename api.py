#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

#  https://pynative.com/python-mysql-insert-data-into-database-table/
connection = mysql.connector.connect(

    host="localhost",
    database="feinstaub",
    user="root",
    password=""
)

# print (mydb)


app = Flask(_name_)


@app.route('/values',methods=['POST'])
def create_record():
    record = json.loads(request.data)

    # print(record['sensordatavalues'][0]['value'])
    SDS_P1=""
    SDS_P2=""
    temperature=""
    humidity=""

    for value in record['sensordatavalues']:
        if value['value_type'] =="SDS_P1":
            SDS_P1 = value['value']
            print( value['value'])
        if value['value_type'] =="SDS_P2":
            SDS_P2 = value['value']
            print( value['value'])
        if value['value_type'] =="temperature":
            temperature = value['value']
        if value['value_type'] =="humidity":
            humidity = value['value']

    cursor = connection.cursor(prepared=True)
    mySql_insert_query = """INSERT INTO sensordaten (PM25, PM10, Temperature, Humidity) 
                           VALUES 
                           (%s, %s, %s, %s) """

    insert_value = (SDS_P2, SDS_P1, temperature, humidity)

    cursor.execute(mySql_insert_query, insert_value)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

    # with open('data.json', 'r') as f:
    #     data = f.read()
    # if not data:
    #     records = [record]
    # else:
    #     records = json.loads(data)
    #     records.append(record)
    # with open('data.json', 'w') as f:
    #     f.write(json.dumps(records, indent=2))
    
    
    return jsonify(record)


@app.route('/temperatur')
def index1():
    return jsonify({'name': 'heiss',
                       'email': 'heisse@outlook.com'})


app.run(host='0.0.0.0')
