import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='Bonam@2009', host='127.0.0.1', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO STUDENT(STUDENTID,LastName, FirstName, Address, City)"
   "VALUES ( (2,'Legedt', 'Karlye', 'Frisco', 'Dalls'), (1,'Talluri', 'Sarada', 'Irving', 'Dallas'))"
)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()