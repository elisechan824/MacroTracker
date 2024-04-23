import mysql.connector, os

config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': 'macrotracker'
}

def setup():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM foodItem")
    # TODO: set up commands to insert into db
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    print(results)

if __name__ == '__main__':
    setup()