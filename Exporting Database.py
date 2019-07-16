#Editor:-Nilay Trivedi
#Date:-16/07/2019
#This code is to export excel file into mysl database
import pandas as pd
import pymysql
from sqlalchemy import create_engine
user = 'testuser' #user name
passw = 'root'#mysql password
host =  'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address
port = 3306 #Enter port number
database = 'Appendexa'# Enter database name
mydb = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
directory = r'C:\Users\Acer\Desktop\pyPDF\PyPDF2-1.26.0'  # path of csv file
csvFileName = '(final)appendexb.xlsx'

df = pd.read_csv(os.path.join(directory, csvFileName ))

df.to_sql(name=csvFileName[:-4], con=mydb, if_exists = 'replace', index=False)

"""
if_exists: {'fail', 'replace', 'append'}, default 'fail'
     fail: If table exists, do nothing.
     replace: If table exists, drop it, recreate it, and insert data.
     append: If table exists, insert data. Create if does not exist.
"""