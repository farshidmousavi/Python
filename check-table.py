import mysql-connection #the file with connection to mysql database function

databaseName="YOUR-DATABASE-NAME"
#check YOUR-DATABASE-NAME for tables, if table exist, return true, else return false
def checkTableExists(tablename):#tablename is the table name you want to check exist or not
    dbcon= mysql-connection.connection()
    dbcur = dbcon.cursor()
    dbcur.execute("""
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = '{1}' 
    AND table_name = '{0}'
    LIMIT 1
        """.format(tablename.replace('\'', '\'\''),databaseName))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    dbcur.close()
    return False
  
#Test 
if checkTableExists('users'):
  print('users table exist')
else:
  print('there is no users table')
