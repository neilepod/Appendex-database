#Editor:-Nilay Trivedi
#Date:-16/07/2013
#This code is to separate the appendexc into two excel file and edit the first excel file.
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from openpyxl import workbook
import math
df=pd.read_excel("appendexc.xlsx", names=['Name','D.O.S','Pageno','Name','D.O.S','Pageno'])
df.drop([0,1,2,3], axis=0, inplace= True)
df.to_excel("dbappendexc.xlsx", index=False)
df.to_excel("dbappendexc2.xlsx", index=False,columns=['Serialno.1','Name.1','D.O.B.1',] )
df.to_excel("dbappendexc.xlsx", index=False)
df.drop(['Pageno','Serialno.1','Name.1','D.O.B.1'],axis=1,inplace=True)
df.to_excel("dbappendexc.xlsx", index=False)
df=pd.read_excel("dbappendexc.xlsx")
df['Name'] = df['Name'].fillna('').apply(lambda x: str(x).strip())
df['Serialno'] = df['Serialno'].fillna('').apply(lambda x: str(x).strip())
df['D.O.B'] = df['D.O.B'].fillna('').apply(lambda x: str(x).strip())
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
a=[]
c=[]
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

        s=dict(zip(a,c))
        f={'Cadre':s}
b.update(f)
print b
df = pd.DataFrame(b)
writer = ExcelWriter('(final)appendixc.xlsx', engine='xlsxwriter')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()


