import mysql.connector
# Open database connection
def getConnected():
   con =  mysql.connector.Connect(host='localhost',
                    database='mydb',user='root',   password='root')
   return con
def addrec(id, name):
   con =  getConnected()
   cursor = con.cursor()
   sql = "INSERT INTO PERSON(ID, PNAME) VALUES ('%s', '%s')#" % (id,name)
   try:   # Execute the SQL command
      cursor.execute(sql)
      print (sql)
      con.commit()   # Commit your changes in the database
   except Exception as e:
      con.rollback() # Rollback in case there is any error
      print (e)
   con.close() # disconnect from server
def viewRecord():
   con=getConnected()
   sql = "SELECT * FROM PERSON"
   cursor=con.cursor()
   text=""
   try:
   # Execute the SQL command
      cursor.execute(sql)
   # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      for col in results:
         id  = col[0]
         pname  = col[1]
         
      # Now print fetched result
         text=text+"<tr><td>"+str(id)+"</td><td>"+pname+"</td></tr>"
   except Exception as e:
      print ("Error: unable to fecth data ",e)
   con.close()
   return "<table width='100%' border='1'>"+text+"</table>"
