from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv("MYSQL_PASSWORD"),
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
