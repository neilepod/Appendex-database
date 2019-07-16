#Code is for conversion of pdf file to excel file
import pdftables_api                        #importing module given by pdftables
import os
#Enter the path of the folder where all pdf file are stored
a=raw_input("Enter the path of the folder")
try:
    c = pdftables_api.Client('zmll391gneyq')
    file_path = a+"\\"
    for file in os.listdir(file_path):
#If statement to find all the file in the folder with .pdf format
        if file.endswith(".pdf"):
            c.xlsx(os.path.join(file_path,file), file+'.xlsx')
#Except handling just to prevent any error in try statement regarding intalling gitbash or apikey
except Exception:
    try:
        c = pdftables_api.Client('mu5pqlmbcxzh')
        file_path = a+"\\"
        for file in os.listdir(file_path):
            if file.endswith(".pdf"):
                c.xlsx(os.path.join(file_path, file), file + '.xlsx')
    except Exception:
        try:
            c = pdftables_api.Client('rk8wn6n8l98b')
            file_path = a+"\\"
            for file in os.listdir(file_path):
                if file.endswith(".pdf"):
                    c.xlsx(os.path.join(file_path, file), file + '.xlsx')
        except Exception:
            try:
                c = pdftables_api.Client('vchmq35pbbjy')
                file_path = a+"\\"
                for file in os.listdir(file_path):
                    if file.endswith(".pdf"):
                        c.xlsx(os.path.join(file_path, file), file + '.xlsx')
            except Exception:
                try:
                    c = pdftables_api.Client('346a98o500xx')
                    file_path = a+"\\"
                    for file in os.listdir(file_path):
                        if file.endswith(".pdf"):
                            c.xlsx(os.path.join(file_path, file), file + '.xlsx')
                except Exception:
                    try:
                        c = pdftables_api.Client('zt2yek0att23')
                        file_path = a+"\\"
                        for file in os.listdir(file_path):
                            if file.endswith(".pdf"):
                                c.xlsx(os.path.join(file_path, file), file + '.xlsx')
                    except Exception:
                        try:
                            c = pdftables_api.Client('zt2yek0att23')
                            file_path = a+"\\"
                            for file in os.listdir(file_path):
                                if file.endswith(".pdf"):
                                    c.xlsx(os.path.join(file_path, file), file + '.xlsx')
                        except Exception:
                            print "Finish"
