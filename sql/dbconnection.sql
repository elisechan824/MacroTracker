-- Create the User table
CREATE TABLE User (
     UserID VARCHAR(255) PRIMARY KEY, 
     user_name VARCHAR(255) NOT NULL, 
     gender VARCHAR(255), 
     dob DATE, 
     age INT,
     weight FLOAT(5, 2), 
     height INT,
     password VARCHAR(255)
);

-- Create the MealPlans table
CREATE TABLE MealPlans (
    mealPlanID VARCHAR(255),
    userID VARCHAR(255),
    nutritionalValue JSON,
    meals JSON,
    PRIMARY KEY (mealPlanID, userID),
    FOREIGN KEY (userID) REFERENCES User(UserID)
);

-- Create the FoodItem table
CREATE TABLE FoodItem (
     foodID VARCHAR(255) PRIMARY KEY,
     foodName VARCHAR(255) NOT NULL,
     foodGroup VARCHAR(255),
     calories INT,
     servingSize VARCHAR(255)
);

-- Create the Admin table
CREATE TABLE Admin (
    AdminID VARCHAR(255) PRIMARY KEY
);

-- Create the Goals table
CREATE TABLE Goals (
    goalName VARCHAR(255) PRIMARY KEY,
    UserID VARCHAR(255),
    target_daily_cals INT,
    deadline DATE,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);