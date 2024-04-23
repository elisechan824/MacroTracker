from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': 'macrotracker'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM foodItem")
    food_items = cursor.fetchall()  # Fetch all rows from the result
    cursor.close()
    conn.close()
    return render_template('index.html', food_items=food_items)

@app.route('/login')
def login():
    error_message = request.args.get('error_message')
    return render_template('login.html', error_message=error_message)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/addUser', methods=['POST'])
def addUser():
    userID = request.form['userID']
    fullname = request.form['fullname']
    gender = request.form['gender']
    dob = request.form['dob']
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    password = request.form['password']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (userID, user_name, gender, dob, age, weight, height, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (userID, fullname, gender, dob, age, weight, height, password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/loginUser', methods=['POST'])
def loginUser():
    userID = request.form['userID']
    password = request.form['password']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE userID = %s;",
                   (userID,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user is None:
        return redirect(url_for('login') + '?error_message=No+such+user')
    if password != user[7]:
        return redirect(url_for('login') + '?error_message=Incorrect+password')
    return redirect(url_for('index'))

@app.route('/insertFoodItem', methods=['POST'])
def insertFoodItem():
    foodID = request.form['foodID']
    foodName = request.form['foodName']
    foodGroup = request.form['foodGroup']
    calories = request.form['calories']
    servingSize = request.form['servingSize']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO foodItem (foodID, foodName, foodGroup, calories, servingSize) VALUES (%s, %s, %s, %s, %s)",
                   (foodID, foodName, foodGroup, calories, servingSize))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/deleteFoodItem', methods=['POST'])
def deleteFoodItem():
    foodID = request.form['foodID']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM foodItem WHERE foodID=%s", (foodID, ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/updateFoodItem', methods=['POST'])
def updateFoodItem():
    foodID = request.form['foodID']
    foodName = request.form['foodName']
    foodGroup = request.form['foodGroup']
    calories = request.form['calories']
    servingSize = request.form['servingSize']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE foodItem SET foodName=%s, foodGroup=%s, calories=%s, servingSize=%s WHERE foodID=%s",
                   (foodName, foodGroup, calories, servingSize, foodID))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





# @app.route('/add', methods=['POST'])
# def add():
#     data = request.form['data']
#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (Name) VALUES (%s)", (data,))
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return redirect(url_for('index'))
