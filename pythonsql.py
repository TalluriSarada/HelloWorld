import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='Bonam@2009', host='127.0.0.1', database='mydatabase')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE STUDENTS (
    STUDENTID int  NOT NULL,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    PRIMARY KEY (STUDENTID)
);'''
cursor.execute(sql)

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO STUDENT(STUDENTID,LastName, FirstName, Address, City)"
   "VALUES (%s, %s, %s, %s, %s)"
)
data = (1,'Talluri', 'Sarada', 'Irving', 'Dalla')
try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()
