from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os, json

app = Flask(__name__)
app.secret_key = os.getenv('MYSQL_PASSWORD', 'Jinrie2713')

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Jinrie2713',
    'database': 'macrotracker'
}

user_data = {}

@app.route('/foodItem')
def foodItem():
    if 'current_user' not in session:
        return redirect(url_for('login'))

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM foodItem")
    food_items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('foodItem.html', current_user=session.get('current_user'), food_items=food_items)

##### USER PROFILE FUNCTIONALITY #####
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'current_user' not in session:
        return redirect(url_for('login'))
    user_data = session['current_user']
    if request.method == 'POST':
        userID = request.form['userID']
        fullname = request.form['user_name']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        password = request.form['password']
        target_daily_cals = request.form['target_daily_cals']
        
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("""UPDATE user 
                       SET user_name=%s, gender=%s, dob=%s, age=%s, weight=%s, height=%s, password=%s, target_daily_cals=%s
                       WHERE userID = %s""",
                        (fullname, gender, dob, age, weight, height, password, target_daily_cals, userID))
        conn.commit()
        cursor.close()
        conn.close()

        user_data = {
            'userID': userID,
            'user_name': fullname,
            'gender': gender,
            'dob': dob.format(),
            'age': age,
            'weight': weight,
            'height': height,
            'password': password,
            'target_daily_cals': target_daily_cals
        }
        
        session['current_user'] = user_data
        return redirect(url_for('profile'))
    
    return render_template('user.html', current_user=user_data)

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

    cursor.execute("SELECT * FROM foodItem")
    food_items = cursor.fetchall()

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
        return render_template('foodItem.html', current_user=user_data, food_items=food_items)

@app.route('/loginUser', methods=['POST'])
def loginUser():
    userID = request.form['userID']
    password = request.form['password']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # get fooditems
    cursor.execute("SELECT * FROM foodItem")
    food_items = cursor.fetchall()
    
    # get user data
    cursor.execute("SELECT * FROM user WHERE userID = %s;",
                   (userID,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    # login verification logic
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
    return render_template('foodItem.html', current_user=user_data, food_items=food_items)

##### FOODITEM FUNCTIONALITY #####
@app.route('/insertFoodItem', methods=['POST'])
def insertFoodItem():
    # fetch form info from foodItem.html
    foodID = request.form['foodID']
    foodName = request.form['foodName']
    foodGroup = request.form['foodGroup']
    calories = request.form['calories']
    servingSize = request.form['servingSize']

    # post to database
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
