import mysql.connector
def connect_to_mysql():
  try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fapi"
    )
  except mysql.connector.Error as err:   
    return None  

  return connection
