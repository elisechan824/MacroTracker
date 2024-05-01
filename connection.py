from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os, json

app = Flask(__name__)
app.secret_key = os.getenv('MYSQL_PASSWORD')

config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': 'macrotracker'
}

user_data = {}

@app.route('/')
def foodItem():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM foodItem")
    food_items = cursor.fetchall()  # Fetch all rows from the result
    cursor.close()
    conn.close()
    return render_template('foodItem.html', food_items=food_items)

##### USER PROFILE FUNCTIONALITY #####
@app.route('/profile')
def profile():
    return render_template('user.html', user_data=user_data)

##### LOGIN/SIGNUP FUNCTIONALITY
@app.route('/login')
def login():
    error_message = request.args.get('error_message')
    return render_template('login.html', error_message=error_message)

@app.route('/signup')
def signup():
    error_message = request.args.get('error_message')
    return render_template('signup.html', error_message=error_message)

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
    cursor.execute("SELECT * FROM user WHERE userID = %s", (userID, ))
    results = cursor.fetchone()

    if results != None:
        return redirect(url_for('signup') + '?error_message=userID+already+taken')
    else :
        cursor.execute("INSERT INTO user (userID, user_name, gender, dob, age, weight, height, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (userID, fullname, gender, dob, age, weight, height, password))
        user_data = {
            'userID': userID,
            'user_name': fullname,
            'gender': gender,
            'dob': dob.format(),
            'age': age,
            'weight': weight,
            'height': height,
            'password': password
        }
        print(user_data)
        conn.commit()
        cursor.close()
        conn.close()
        session['current_user'] = user_data
        return redirect(url_for('foodItem'))

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
    user_data = {
        'userID': user[0],
        'user_name': user[1],
        'gender': user[2],
        'dob': user[3].isoformat(),
        'age': user[4],
        'weight': user[5],
        'height': user[6],
        'password': user[7]
    }
    session['current_user'] = user_data
    print(user_data)
    return redirect(url_for('foodItem'))

##### FOODITEM FUNCTIONALITY #####
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
    return redirect(url_for('foodItem'))

@app.route('/deleteFoodItem', methods=['POST'])
def deleteFoodItem():
    foodID = request.form['foodID']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM foodItem WHERE foodID=%s", (foodID, ))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('foodItem'))

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
    return redirect(url_for('foodItem'))

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
#     return redirect(url_for('foodItem'))
