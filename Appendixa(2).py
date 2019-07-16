#Editor:-Nilay Trivedi
#Date:-16/07/2019
#Code is for the half part of appendixa
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from openpyxl import workbook
import math
df=pd.read_excel("appendexa.xlsx", names=['Serialno','Name','D.O.B','Serialno','Name','D.O.B'])
df.drop([0,1,2,3], axis=0, inplace= True)#To drop first 4 rows of title
df.to_excel("dbappendexa2.xlsx", index=False,columns=['Serialno.1','Name.1','D.O.B.1',] )
df=pd.read_excel("dbappendexa2.xlsx")
#Changing datatype into strings of all the elements present in dataframe
df['Name'] = df['Name'].fillna('').apply(lambda x: str(x).strip())
df['Serialno'] = df['Serialno'].fillna('').apply(lambda x: str(x).strip())
df['D.O.B'] = df['D.O.B'].fillna('').apply(lambda x: str(x).strip())
#Making separate column for Allotment year.
df['Allotment Year']=""
df['Allotment_year_check']=df['Name'].apply(lambda x : x.startswith('Allot'))
df.loc[(df['Allotment_year_check']==1),'Allotment Year']=df['Name']
df['Allotment Year'].replace("",None,inplace=True)
df['Allotment Year'].replace('Allotment Year : 1993','1993',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1994','1994',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1995','1995',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1996','1996',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1997','1997',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1998','1998',inplace=True)
df['Allotment Year'].replace('Allotment Year : 1999','1999',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2000','2000',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2001','2001',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2002','2002',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2003','2003',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2004','2004',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2005','2005',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2006','2006',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2007','2007',inplace=True)
df['Allotment Year'].replace('Allotment Year : 2008','2008',inplace=True)
df.ffill(axis=1)
b=df.to_dict()
a=[]#list for storing location of key
c=[]#list for storing state name
#Maaking separate column for Cadre by checking the ending letters in the name of IAS officers.
#By iteriting in the dataframe using for loop.
for key,value in b.iteritems():
    if key=='Name':
        for key2,value2 in value.iteritems():
            if value2.endswith('(MP)')==True:
               a.append(key2)
               c.append('Madhya Pradesh')
            if value2.endswith('(AP)')==True:
               a.append(key2)
               c.append('Andhra Pradesh')
            if value2.endswith('(MH)')==True:
               a.append(key2)
               c.append('Maharashtra')
            if value2.endswith('(KL)')==True:
               a.append(key2)
               c.append('Kerala')
            if value2.endswith('(TN)')==True:
               a.append(key2)
               c.append('Tamil Nadu')
            if value2.endswith('(NL)') == True:
                a.append(key2)
                c.append('Nagaland')
            if value2.endswith('(UT)') == True:
                a.append(key2)
                c.append('Union Territory')
            if value2.endswith('(TR)') == True:
                a.append(key2)
                c.append('Tripura')
            if value2.endswith('(PB)') == True:
                a.append(key2)
                c.append('Punjab')
            if value2.endswith('(HY)') == True:
                a.append(key2)
                c.append('HY')
            if value2.endswith('(AM)') == True:
                a.append(key2)
                c.append('AM')
            if value2.endswith('(GJ)') == True:
                a.append(key2)
                c.append('Gujrat')
            if value2.endswith('(UT)') == True:
                a.append(key2)
                c.append('Uttarakhand')
            if value2.endswith('(RJ)') == True:
                a.append(key2)
                c.append('Rajasthan')
            if value2.endswith('(SK)') == True:
                a.append(key2)
                c.append('Sikkhim')
            if value2.endswith('(WB)') == True:
                a.append(key2)
                c.append('West Bengal')
            if value2.endswith('(CG)') == True:
                a.append(key2)
                c.append('Chhattisgarh')
            if value2.endswith('(TG)') == True:
                a.append(key2)
                c.append('Telangana')
        # To form the dictionary and update into dataframe so that new column can be performed of Cadre
        s=dict(zip(a,c))
        f={'Cadre':s}
b.update(f)
print b
df = pd.DataFrame(b)
#With the help of excel write forming an excel file of name (final)appendixa.xlsx by passing the dataframe formed above
writer = ExcelWriter('(final)appendixa2.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()


