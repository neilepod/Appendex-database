#Author:-Nilay Trivedi
#Date:-22/7/19
#Code to perform sql query and print on the web page
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import pandas as pd
from flask.ext.jsonpify import jsonify
import urllib
import webbrowser
db_connect = create_engine('sqlite:///appendex.db')
app = Flask(__name__)
api = Api(app)
#sql query to print all name
class All(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from employees;") #sql to be writtten in execute(
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        a=jsonify(result) #convert format into json format
#export to json file
        Export = a.to_json(r'C:\codes\result.json')
        return a
#to open html page on new tab of chrome for other browser change name in get()
        webrowser.get('mychrome').open_new_tab('result.htm')
class AllotmentYear(Resource):
    def get(self, AllotmentYear):
        conn = db_connect.connect()
        query = conn.execute("select * from Officer where Allotment Year =%d " % int(AllotmentYear))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        a=jsonify(result)
        Export=a.to_json(r'C:\codes\result.json')
        return a
        webbrowser.get('mychrome').open_new_tab('result.htm')
class Name(Resource):
    def get(self, Name):
        conn = db_connect.connect()
        query = conn.execute("select * from Officer where Name =%d " %Name)
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        a = jsonify(result)
        Export = a.to_json(r'C:\codes\result.json')
        return a
        webbrowser.get('mychrome').open_new_tab('result.htm')
class DOB(Resource):
    def get(self, DOB):
        conn = db_connect.connect()
        query = conn.execute("select * from Officer where D.O.B =%d " %DOB)
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        a = jsonify(result)
        Export = a.to_json(r'C:\codes\result.json')
        return a
        webbrowser.get('mychrome').open_new_tab('result.htm')
class Cadre(Resource):
    def get(self,Cadre):
        conn=db_connect.connect()
        query=conn.execute("select * from Officer where Cadre=%d"%Cadre)
        result={'data':[dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
        a = jsonify(result)
        Export = a.to_json(r'C:\codes\result.json')
        return a
        webbrowser.get('mychrome').open('result.htm')
class Orderby(Resource):
    def get(self,a):
        conn=db_connect.connect()
        query = conn.execute("SELECT * FROM Customers ORDER BY %d"%a)
        result={'data':[dict(zip(tuple(query.keys()),i)) for i in query.curaor]}
        a = jsonify(result)
        Export = a.to_json(r'C:\codes\result.json')
        return a
        webbrowser.get('mychrome').open_new_tab('result.htm')
class Between(Resource):
    def get(self,start,to):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM Employees WHERE AllotmentYear BETWEEN '%d' AND '%a'"%(start,to))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        a=jsonify(result)
        Export = a.to_json(r'C:\codes\result.json')
        webbrowser.get('mychrme').open_new_tab('result.htm')
api.add_resource(Appendex, '/Officer')  # Route_1
if __name__ == '__main__':
    app.run(port='3306')
    while True:
        print "press 1 to exit"
        print "press 2 to see whole table"
        print "press 3 to find officer with specific Allotment Year"
        print "press 4 to find officer with specific Name"
        print "press 5 to find officer with specific Cadre"
        print "press 6 to order the table with specific table"
        print "press 7 to find officers in between any field"
        a=input("Enter your command")
        if a==1:
            break
        elif a==2:
            All.get()
        elif a==3:
            b=raw_input("Enter Allotment Year")
            AllotmentYear.get(b)
        elif a==4:
            b=raw_input("Enter Name of the Officer")
            Name.get(b)
        elif a==5:
            b=raw_input("Enter Cadre")
            Cadre.get(b)
        elif a==6:
            b=raw_input("Enter Field")
        elif a==7:
            b=raw_input("Enter starting field")
            c=raw_input("Enter ending field")
            Between.get(b,c)
