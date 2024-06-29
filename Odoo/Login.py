import pymongo
import hashlib
import datetime
from bson.objectid import ObjectId  # Correct import for ObjectId

# Database connection parameters
DB_NAME = "DietManagementSystem"
DB_HOST = "127.0.0.1"
DB_PORT = 27017

# Connect to MongoDB
client = pymongo.MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
users_collection = db["users"]
recipes_collection = db["recipes"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return ['Underweight', 600]
    elif 18.5 <= bmi < 24.9:
        return ['Normal weight', 0]
    elif 25 <= bmi < 29.9:
        return ['Overweight', 300]
    else:
        return ['Obese', 100]

def get_meal_plan(food_preference, bmi_category):
    if bmi_category[0] == "Underweight":
        query = {
            "food_preference": food_preference,
            "total_calories": {"$gt": bmi_category[1]}
        }
    elif bmi_category[0] == "Overweight" or bmi_category[0] == "Obese":
        query = {
            "food_preference": food_preference,
            "total_calories": {"$lt": bmi_category[1]}
        }
    else:
        print("You are Fit! You can continue your regular diet!!")
        query = {
            "food_preference": food_preference,
            "total_calories": bmi_category[1]
        }

    # Fetch recipes based on the initial query
    recipes = list(recipes_collection.find(query))

    # Fallback mechanism if the number of recipes is too few
    if len(recipes) < 5:
        print("Few recipes found, expanding search criteria...")
        if bmi_category[0] == "Underweight":
            query = {
                "food_preference": food_preference,
                "total_calories": {"$gte": bmi_category[1]}
            }
        elif bmi_category[0] == "Overweight" or bmi_category[0] == "Obese":
            query = {
                "food_preference": food_preference,
                "total_calories": {"$lte": bmi_category[1]}
            }
        else:
            query = {
                "food_preference": food_preference
            }
        recipes = list(recipes_collection.find(query))
    
    return recipes

def create_user_table():
    # MongoDB doesn't require explicit table creation
    pass

def register_user():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')
    password = input('Enter a password: ')
    hashed_password = hash_password(password)
    age = int(input('Enter your age: '))
    gender = input('Enter your gender: ')
    phone_number = input('Enter your phone number: ')
    height = float(input('Enter your height (in cm): '))
    weight = float(input('Enter your weight (in kg): '))
    allergies = input('Enter your allergies: ')
    food_preference = input('Enter your food preference (Vegetarian/Non-Vegetarian): ')
    health_goals = input('Enter your health goals: ')

    bmi = calculate_bmi(weight, height)
    bmi_category = categorize_bmi(bmi)

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": hashed_password,
        "age": age,
        "gender": gender,
        "phone_number": phone_number,
        "height": height,
        "weight": weight,
        "allergies": allergies,
        "food_preference": food_preference,
        "health_goals": health_goals,
        "created_at": datetime.datetime.now(),
        "bmi": bmi,
        "bmi_category": bmi_category
    }

    try:
        users_collection.insert_one(user)
        print('Registration successful!')
    except pymongo.errors.DuplicateKeyError:
        print('Email already exists!')

def login_user():
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    hashed_password = hash_password(password)

    user = users_collection.find_one({"email": email, "password": hashed_password})
    
    if user:
        print('Login successful!')
        return user
    else:
        print('Invalid email or password')
        return None

def update_profile(user):
    user_id = user["_id"]
    age = int(input('Enter your age: '))
    height = float(input('Enter your height (in cm): '))
    weight = float(input('Enter your weight (in kg): '))
    allergies = input('Enter your allergies: ')

    bmi = calculate_bmi(weight, height)
    bmi_category = categorize_bmi(bmi)

    update_data = {
        "age": age,
        "height": height,
        "weight": weight,
        "allergies": allergies,
        "bmi": bmi,
        "bmi_category": bmi_category
    }

    users_collection.update_one({"_id": user_id}, {"$set": update_data})
    print('Profile updated successfully!')

def admin_panel(user):
    if user.get('role') != 'admin':
        print('Unauthorized access!')
        return
    
    users = users_collection.find()
    for user in users:
        print(f"First Name: {user['first_name']}, Last Name: {user['last_name']}, Email: {user['email']}, Age: {user['age']}, Gender: {user['gender']}, Phone Number: {user['phone_number']}, Height: {user['height']}, Weight: {user['weight']}, Allergies: {user['allergies']}, Food Preference: {user['food_preference']}, Health Goals: {user['health_goals']}, BMI: {user['bmi']:.2f}, BMI Category: {user['bmi_category']}")

def get_meal_plan_for_user(user):
    food_preference = user['food_preference']
    bmi_category = user['bmi_category']
    recipes = get_meal_plan(food_preference, bmi_category)
    if recipes:
        print(f"Meal Plan for {user['first_name']} {user['last_name']}:")
        for recipe in recipes:
            print(f"- {recipe['recipe_name']} ({recipe['total_calories']} calories)")
            print("Instructions: ")
            instructions = recipe.get("instructions", "").split(". ")
            for rec in instructions:
                print(rec)
            print()
    else:
        print('No meal plans available for your preferences and BMI category.')

def view_user_details_by_id():
    user_id = input("Enter the user ID: ")
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            print(f"User Details for User ID {user_id}:")
            print(f"First Name: {user['first_name']}")
            print(f"Last Name: {user['last_name']}")
            print(f"Email: {user['email']}")
            print(f"Age: {user['age']}")
            print(f"Gender: {user['gender']}")
            print(f"Phone Number: {user['phone_number']}")
            print(f"Height: {user['height']} cm")
            print(f"Weight: {user['weight']} kg")
            print(f"Allergies: {user['allergies']}")
            print(f"Food Preference: {user['food_preference']}")
            print(f"Health Goals: {user['health_goals']}")
            print(f"BMI: {user['bmi']:.2f}")
            print(f"BMI Category: {user['bmi_category']}")
        else:
            print(f"No user found with ID {user_id}")
    except Exception as e:
        print(f"Invalid User ID format: {e}")

def main():
    create_user_table()
    
    while True:
        print('\nMenu:')
        print('1. Register')
        print('2. Login')
        print('3. Update Profile')
        print('4. Admin Panel')
        print('5. Get Meal Plan')
        print('6. View User Details by ID')
        print('7. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
        elif choice == '3':
            if 'user' not in locals() or not user:
                print('You need to login first!')
            else:
                update_profile(user)
        elif choice == '4':
            if 'user' not in locals() or not user:
                print('You need to login first!')
            else:
                admin_panel(user)
        elif choice == '5':
            if 'user' not in locals() or not user:
                print('You need to login first!')
            else:
                get_meal_plan_for_user(user)
        elif choice == '6':
            view_user_details_by_id()
        elif choice == '7':
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
    client.close()