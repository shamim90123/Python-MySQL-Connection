import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='db_name'
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Execute SQL query to retrieve data from a table
cursor.execute("SELECT * FROM table_name")

# Fetch all the rows from the query result
result = cursor.fetchall()

# Iterate over the rows and print the data
for row in result:
    print(row)

# Close the cursor and the database connection
cursor.close()
mydb.close()