#This is fast and easy mysql connection for python script
import mysql.connector as database

username="YOUR-DATABASE-USERNAME"
passowrd="YOUR-DATABASE-PASSWORD"
hostname="localhost"#prefered
databasename="YOUR-DATABASE-NAME"

try:
    def connection():
        connection = database.connect(
            user=username,
            password=passowrd,
            host=hostname,
            database=databasename
        )
        return connection #return connection to mysql
except:
    print("Can not connect to database")
