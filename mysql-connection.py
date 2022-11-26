#This is fast and easy mysql connection for python script
import mysql.connector as database

username="YOUR-DATABASE-USERNAME"
passowrd="YOUR-DATABASE-PASSWORD"
hostname="locolhost"#prefered
databasename="YOUR-DATABASE-NAME"

def connection():
    connection = database.connect(
        user=username,
        password=passowrd,
        host=hostname,
        database=databasename
    )
    return connection #return connection to mysql
