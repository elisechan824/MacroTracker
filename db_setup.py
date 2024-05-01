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
    cursor = conn.cursor(buffered=True)
    # cursor.execute("SELECT * FROM foodItem")
    # USER TABLE
    cursor.execute(""" CREATE Table User (
                    UserID VARCHAR(255) PRIMARY KEY, 
                    user_name varchar(255) NOT NULL, 
                    gender varchar(255), 
                    dob DATE, 
                    age INT,
                    weight FLOAT(5, 2), 
                    height INT,
                    password VARCHAR(255));
                    """)
    cursor.execute(""" INSERT INTO User (UserID, user_name, gender, dob, age, weight, height, password)
                    VALUES 
                    ('cparks288', 'Caden Parks', 'Male', '1999-12-21', 24, 184, 71, 'koalas3'),
                    ('strawberries229', 'Sally Brooks', 'Female', '2000-11-01', 23, 200, 68, 'rav42013'),
                    ('jackinthebox9', 'Jack Prescott', 'Male', '1974-04-17', 49, 197, 71, 'chickenwings'),
                    ('jdoeee', 'Jane Doe', 'Female', '2006-01-24', 18, 121, 63, 'redorangeyellow'),
                    ('h2rov', 'Henry Rover', 'Male', '1999-01-23', 25, 160, 57, '5ajkg8i2'),
                    ('hannah10', 'Hannah Smith', 'Female', '2004-07-06', 19, 108, 62, 'coolpenguin12'),
                    ('jackinthebox9', 'Jack Prescott', 'Male', '1974-04-17', 49, 197, 71, 'chickenwings'),
                    ('jdoeee', 'Jane Doe', 'Female', '2006-01-24', 18, 121, 63, 'redorangeyellow'),
                    ('jennnroddd1', 'Jennifer Rodriguez', 'Female', '1990-01-15', 32, 145, 62, 'sunr1s3'),
                    ('jessdavis12', 'Jessica Davis', 'Female', '1989-09-10', 33, 135, 65, 'applesauce4lyfe'),
                    ('jmartinez000', 'Jason Martinez', 'Male', '1998-04-12', 26, 170, 69, 'password123'),
                    ('js23', 'John Smith', 'Male', '1985-07-15', 39, 175, 68, 'ilovepuppies123'),
                    ('leechristopher1', 'Christopher Lee', 'Male', '2001-05-20', 21, 160, 70, 'c00k0ut'),
                    ('m58brown', 'Michael Brown', 'Male', '1978-11-02', 46, 190, 72, 'kl3j6sj3'),
                    ('mandy882', 'Amanda Taylor', 'Female', '1982-08-25', 39, 155, 64, 'saw45end13ban2'),
                    ('mattgarc0605', 'Matthew Garcia', 'Male', '1976-06-05', 48, 200, 74, 'forkknifespoon'),
                    ('michellew2', 'Michelle White', 'Female', '1987-10-30', 34, 160, 67, 'jessi346'),
                    ('nancyn', 'Nancy Newman', 'Female', '1967-09-07', 56, 145, 66, 'sk5o1js65fd'),
                    ('sarahmiller4926', 'Sarah Miller', 'Female', '1995-12-07', 27, 140, 66, 'nyctimessquare');
                    """)
    # MEALPLAN TABLE
    cursor.execute("""
                    CREATE TABLE MealPlans (
                    mealPlanID VARCHAR(255),
                    userID VARCHAR(255),
                    nutritionalValue JSON,
                    meals JSON,
                    PRIMARY KEY (mealPlanID, userID),
                    FOREIGN KEY (userID) REFERENCES User(userID)
                );
                   """)
    cursor.execute("""
                    INSERT INTO MealPlans (mealPlanID, userID, nutritionalValue, meals) VALUES
                    ('diet1', 'cparks288', '{"protein": "chicken", "carbs": "rice", "fat": "avocado"}', '{"breakfast": "scrambled eggs", "lunch": "grilled salmon", "dinner": "quinoa salad"}'),
                    ('no red meats', 'strawberries229', '{"protein": "salmon", "carbs": "potatoes", "fat": "olive oil"}', '{"breakfast": "smoothie (banana, spinach, almond milk)", "lunch": "chicken stir-fry", "snack": "Greek yogurt", "dinner": "baked sweet potatoes"}'),
                    ('cut', 'jackinthebox9', '{"protein": "tofu", "carbs": "quinoa", "fat": "nuts"}', '{"breakfast": "oatmeal with almond butter", "lunch": "tofu and vegetable stir-fry", "dinner": "quinoa salad"}'),
                    ('meal plan', 'jdoeee', '{"protein": "beef", "carbs": "pasta", "fat": "cheese"}', '{"breakfast": "avocado toast", "lunch": "beef and vegetable stir-fry", "snack": "apple with peanut butter", "dinner": "whole wheat pasta with marinara sauce"}'),
                    ('week of 4/2', 'h2rov', '{"protein": "turkey", "carbs": "sweet potatoes", "fat": "coconut oil"}', '{"breakfast": "Greek yogurt with berries", "lunch": "turkey and avocado wrap", "dinner": "grilled chicken with roasted sweet potatoes"}'),
                    ('eat more greens', 'nancyn', '{"protein": "eggs", "carbs": "oatmeal", "fat": "peanut butter"}', '{"breakfast": "scrambled eggs with spinach", "lunch": "salmon salad", "dinner": "chicken and vegetable stir-fry"}'),
                    ('diet2', 'cparks288', '{"protein": "shrimp", "carbs": "couscous", "fat": "avocado"}', '{"breakfast": "smoothie bowl (banana, mango, coconut milk)", "lunch": "shrimp and avocado salad", "snack": "almonds", "dinner": "grilled shrimp with couscous"}'),
                    ('vegetarian', 'strawberries229', '{"protein": "chickpeas", "carbs": "brown rice", "fat": "olive oil"}', '{"breakfast": "whole grain toast with avocado", "lunch": "chickpea curry", "dinner": "stuffed bell peppers"}'),
                    ('bulk', 'jackinthebox9', '{"protein": "chicken", "carbs": "quinoa", "fat": "almonds"}', '{"breakfast": "protein smoothie (spinach, banana, protein powder)", "lunch": "grilled chicken salad", "snack": "carrot sticks with hummus", "dinner": "quinoa bowl with grilled vegetables"}'),
                    ('balanced diet', 'jdoeee', '{"protein": "salmon", "carbs": "sweet potatoes", "fat": "avocado"}', '{"breakfast": "chia seed pudding", "lunch": "salmon and avocado wrap", "dinner": "sweet potato and black bean chili"}'),
                    ('liquid diet lol', 'h2rov', '{"protein": "tofu", "carbs": "brown rice", "fat": "sesame oil"}', '{"breakfast": "smoothie (kale, banana, almond milk)", "lunch": "tofu and vegetable stir-fry", "snack": "edamame", "dinner": "sushi bowl"}'),
                    ('dairy heavy', 'nancyn', '{"protein": "beef", "carbs": "pasta", "fat": "cheese"}', '{"breakfast": "Greek yogurt with granola", "lunch": "beef and vegetable stir-fry", "dinner": "spaghetti squash with marinara sauce"}'),
                    ('superfoods meal plan', 'cparks288', '{"protein": "chicken", "carbs": "quinoa", "fat": "almonds"}', '{"breakfast": "avocado toast", "lunch": "grilled chicken salad", "snack": "mixed berries", "dinner": "chicken and vegetable stir-fry"}'),
                    ('week of 4/15', 'strawberries229', '{"protein": "salmon", "carbs": "sweet potatoes", "fat": "coconut oil"}', '{"breakfast": "overnight oats with berries", "lunch": "salmon and avocado salad", "dinner": "grilled salmon with sweet potato fries"}'),
                    ('pescetarian diet', 'jackinthebox9', '{"protein": "tofu", "carbs": "brown rice", "fat": "sesame oil"}', '{"breakfast": "smoothie (spinach, pineapple, coconut water)", "lunch": "tofu and vegetable stir-fry", "snack": "almonds", "dinner": "sushi bowl"}'),
                    ('treat myself!', 'jdoeee', '{"protein": "beef", "carbs": "pasta", "fat": "cheese"}', '{"breakfast": "scrambled eggs with vegetables", "lunch": "beef and broccoli stir-fry", "snack": "apple slices with almond butter", "dinner": "spaghetti with meat sauce"}'),
                    ('meatless mondays', 'h2rov', '{"protein": "chickpeas", "carbs": "brown rice", "fat": "olive oil"}', '{"breakfast": "banana pancakes", "lunch": "chickpea and vegetable curry", "snack": "Greek yogurt with honey", "dinner": "stuffed bell peppers"}'),
                    ('on a budget cut', 'nancyn', '{"protein": "chicken", "carbs": "quinoa", "fat": "almonds"}', '{"breakfast": "smoothie (blueberries, kale, almond milk)", "lunch": "grilled chicken salad", "snack": "carrot sticks with hummus", "dinner": "chicken and vegetable stir-fry"}'),
                    ('aldi haul', 'cparks288', '{"protein": "salmon", "carbs": "sweet potatoes", "fat": "avocado"}', '{"breakfast": "avocado toast", "lunch": "salmon and quinoa salad", "snack": "mixed nuts", "dinner": "grilled salmon with roasted vegetables"}'),
                    ('bulking', 'strawberries229', '{"protein": "tofu", "carbs": "brown rice", "fat": "sesame oil"}', '{"breakfast": "smoothie (banana, spinach, almond milk)", "lunch": "tofu and vegetable stir-fry", "snack": "edamame", "dinner": "sushi bowl"}');
                   """)
    # FOODITEM TABLE
    cursor.execute(""" CREATE TABLE FoodItem (
                    foodID VARCHAR(255) PRIMARY KEY,
                    foodName VARCHAR(255) NOT NULL,
                    foodGroup VARCHAR(255),
                    calories INT,
                    servingSize VARCHAR(255)
                    );
                    """)
    cursor.execute(""" 
                    INSERT INTO FoodItem (foodID, foodName, foodGroup, calories, servingSize) VALUES
                    ('cheese_pizza', 'Cheese pizza', 'carbs', 285, '1 slice'),
                    ('chicken_salad', 'Chicken salad', 'protein', 215, '1 cup'),
                    ('apple', 'Apple', 'fruit', 95, '1 medium'),
                    ('spaghetti', 'Spaghetti', 'carbs', 221, '1 cup'),
                    ('grilled_salmon', 'Grilled salmon', 'protein', 233, '3 ounces'),
                    ('banana', 'Banana', 'fruit', 105, '1 medium'),
                    ('hamburger', 'Hamburger', 'protein', 354, '1 sandwich'),
                    ('steak', 'Steak', 'protein', 679, '8 ounces'),
                    ('brown_rice', 'Brown rice', 'carbs', 216, '1 cup cooked'),
                    ('spinach_salad', 'Spinach salad', 'vegetable', 23, '1 cup'),
                    ('fried_chicken', 'Fried chicken', 'protein', 320, '1 piece'),
                    ('orange', 'Orange', 'fruit', 62, '1 medium'),
                    ('cheeseburger', 'Cheeseburger', 'protein', 303, '1 sandwich'),
                    ('yogurt', 'Yogurt', 'dairy', 150, '1 cup'),
                    ('popcorn', 'Popcorn', 'snack', 31, '1 cup popped'),
                    ('chocolate_chip_cookie', 'Chocolate chip cookie', 'snack', 78, '1 cookie'),
                    ('grapes', 'Grapes', 'fruit', 62, '1 cup'),
                    ('bread', 'Bread', 'carbs', 79, '1 slice'),
                    ('ice_cream', 'Ice cream', 'dairy', 137, '1/2 cup'),
                    ('carrot_sticks', 'Carrot sticks', 'vegetable', 25, '1 cup');
                    """)
    # ADMIN TABLE
    cursor.execute("""
                    CREATE TABLE Admin (
                    AdminID VARCHAR(255) PRIMARY KEY);
                   """)
    cursor.execute("""
                    INSERT INTO Admin (AdminID) VALUES
                    ('dennis_the_admin'),
                    ('cheeseybagel'),
                    ('fitnessluvr845'),
                    ('adminguy'),
                    ('adamadmin2'),
                    ('lotus_28'),
                    ('finnjackson2'),
                    ('2maverick2'),
                    ('starry_nighttt'),
                    ('nina_kim2'),
                    ('toyota_camry2018'),
                    ('erin29'),
                    ('paul0h'),
                    ('2021glow'),
                    ('sonnyangelluvr'),
                    ('harryhans3n'),
                    ('hernandez_stacy'),
                    ('joshu4'),
                    ('mango_smoothie3'),
                    ('lucydrewer3');
                    """)
    # GOALS TABLE
    cursor.execute("""
                    CREATE TABLE Goals (
                    goalName VARCHAR(255) PRIMARY KEY,
                    UserID VARCHAR(255),
                    target_daily_cals INT,
                    deadline DATE,
                    FOREIGN KEY (userID) REFERENCES User(userID));
                    """)
    cursor.execute("""
                    INSERT INTO Goals (goalName, userID, target_daily_cals, deadline)
                    VALUES
                    ('Run 5 kilometers', 'cparks288', 1950, '2024-06-30'),
                    ('Consume 2000 calories daily', 'strawberries229', 2000, '2024-08-15'),
                    ('Eat 5 servings of vegetables daily', 'jackinthebox9', 2100, '2024-07-31'),
                    ('Achieve a body fat percentage of 15%', 'jdoeee', 1600, '2025-01-01'),
                    ('Complete a 30-day fitness challenge', 'h2rov', NULL, '2024-10-30'),
                    ('Reduce sugar intake to less than 50g per day', 'nancyn', 1900, '2025-03-01'),
                    ('Attend gym 3 times a week', 'cparks288', NULL, '2024-09-15'),
                    ('Achieve 10,000 steps daily', 'strawberries229', NULL, '2024-11-30'),
                    ('Meal prep for the week every Sunday', 'jackinthebox9', 2400, '2024-12-31'),
                    ('Increase protein intake to 100g daily', 'jdoeee', 1500, '2025-02-28'),
                    ('Complete a half marathon', 'h2rov', NULL, '2025-05-15'),
                    ('Limit processed food consumption to once a week', 'nancyn', 2050, '2024-08-01'),
                    ('Join a fitness class', 'cparks288', NULL, '2024-07-15'),
                    ('Reduce sodium intake to less than 2300mg per day', 'strawberries229', 2310, '2024-10-31'),
                    ('Achieve a BMI of 25', 'jackinthebox9', 1700, '2025-01-01'),
                    ('Increase daily water intake to 3 liters', 'jdoeee', NULL, '2024-09-30'),
                    ('Complete a 7-day detox', 'h2rov', 1400, '2025-03-01'),
                    ('Track food intake using a mobile app daily', 'nancyn', 2000, '2024-07-31'),
                    ('Attend yoga class twice a week', 'cparks288', NULL, '2024-08-31'),
                    ('Achieve a waist circumference of 32 inches', 'strawberries229', 1750, '2025-06-30');
                    """)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    setup()