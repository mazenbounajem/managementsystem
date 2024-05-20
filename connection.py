import pyodbc

class connection():
            

            def contogetrows(sql= '',data=[]):
            
                    try:
                        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                        "Server=DESKTOP-Q7U1STD;"
                                        "Database=Retail;"
                                        "Trusted_Connection=yes;")


                        cursor = cnxn.cursor()
                        cursor.execute(sql)
                    except:
                        print("cant open connection") 
                    else:         

                        for row in cursor:
                            data.append(row)
                        cursor.commit()
                        cursor.close()  
            
            def contogetheaders(sqlh=''):
                   try:
                        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                        "Server=DESKTOP-Q7U1STD;"
                                        "Database=Retail;"
                                        "Trusted_Connection=yes;")


                        cursor = cnxn.cursor()
                        cursor.execute(sqlh)
                   except:
                        print("cant open connection") 
                   else:
                        
                        headers = [i[0] for i in cursor.description]
                        return headers
                        cursor.commit()
                        cursor.close()  
                  

      
                         
testting= connection.contogetrows
variable=[]
query=testting('SELECT * FROM dbo.customer',variable) 
print (variable)
testting2=connection.contogetheaders
variable2=[]
query2=testting2('SELECT * FROM dbo.customer')
print(query2)
             