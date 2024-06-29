
import pymongo
import json

# Database connection parameters
DB_NAME = "DietManagementSystem"
DB_HOST = "127.0.0.1"
DB_PORT = 27017

# Connect to MongoDB
client = pymongo.MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]
recipes_collection = db["recipes"]

# Sample dataset of 20 recipes with instructions
recipes_data = [
    {
        "recipe_name": "Vegetarian Pasta",
        "ingredients": [
            {"name": "Pasta", "quantity": "200g", "calories": 300},
            {"name": "Tomato Sauce", "quantity": "100g", "calories": 50},
            {"name": "Cheese", "quantity": "50g", "calories": 200}
        ],
        "total_calories": 550,
        "food_preference": "Vegetarian",
        "instructions": "1. Boil pasta until al dente. 2. Heat tomato sauce in a pan. 3. Mix pasta with tomato sauce and top with cheese."
    },
    {
        "recipe_name": "Chicken Salad",
        "ingredients": [
            {"name": "Chicken Breast", "quantity": "200g", "calories": 220},
            {"name": "Lettuce", "quantity": "100g", "calories": 15},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Cucumber", "quantity": "100g", "calories": 16}
        ],
        "total_calories": 339,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Grill chicken breast until cooked. 2. Chop lettuce and cucumber. 3. Mix all ingredients with olive oil."
    },
    {
        "recipe_name": "Quinoa Salad",
        "ingredients": [
            {"name": "Quinoa", "quantity": "100g", "calories": 120},
            {"name": "Tomatoes", "quantity": "50g", "calories": 10},
            {"name": "Cucumber", "quantity": "50g", "calories": 8},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Lemon Juice", "quantity": "10g", "calories": 2}
        ],
        "total_calories": 228,
        "food_preference": "Vegetarian",
        "instructions": "1. Cook quinoa according to package instructions. 2. Chop tomatoes and cucumber. 3. Mix quinoa, vegetables, olive oil, and lemon juice."
    },
    {
        "recipe_name": "Grilled Chicken",
        "ingredients": [
            {"name": "Chicken Breast", "quantity": "200g", "calories": 220},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Garlic", "quantity": "5g", "calories": 8},
            {"name": "Lemon Juice", "quantity": "10g", "calories": 2}
        ],
        "total_calories": 318,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Marinate chicken with olive oil, garlic, and lemon juice. 2. Grill until fully cooked."
    },
    {
        "recipe_name": "Vegetable Stir Fry",
        "ingredients": [
            {"name": "Broccoli", "quantity": "100g", "calories": 34},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Bell Peppers", "quantity": "50g", "calories": 15},
            {"name": "Soy Sauce", "quantity": "10g", "calories": 10},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88}
        ],
        "total_calories": 167,
        "food_preference": "Vegetarian",
        "instructions": "1. Heat olive oil in a pan. 2. Stir fry all vegetables until tender. 3. Add soy sauce and mix well."
    },
    {
        "recipe_name": "Beef Stew",
        "ingredients": [
            {"name": "Beef", "quantity": "200g", "calories": 400},
            {"name": "Potatoes", "quantity": "100g", "calories": 77},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Onions", "quantity": "50g", "calories": 20}
        ],
        "total_calories": 517,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Brown beef in a pot. 2. Add vegetables and cover with water. 3. Simmer until beef is tender."
    },
    {
        "recipe_name": "Tofu Stir Fry",
        "ingredients": [
            {"name": "Tofu", "quantity": "200g", "calories": 144},
            {"name": "Broccoli", "quantity": "100g", "calories": 34},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Soy Sauce", "quantity": "10g", "calories": 10},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88}
        ],
        "total_calories": 296,
        "food_preference": "Vegetarian",
        "instructions": "1. Heat olive oil in a pan. 2. Stir fry tofu and vegetables until cooked. 3. Add soy sauce and mix well."
    },
    {
        "recipe_name": "Fish Tacos",
        "ingredients": [
            {"name": "Fish Fillets", "quantity": "200g", "calories": 206},
            {"name": "Tortillas", "quantity": "100g", "calories": 218},
            {"name": "Lettuce", "quantity": "50g", "calories": 7},
            {"name": "Sour Cream", "quantity": "20g", "calories": 48}
        ],
        "total_calories": 479,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Cook fish fillets. 2. Warm tortillas. 3. Assemble tacos with fish, lettuce, and sour cream."
    },
    {
        "recipe_name": "Eggplant Parmesan",
        "ingredients": [
            {"name": "Eggplant", "quantity": "200g", "calories": 48},
            {"name": "Tomato Sauce", "quantity": "100g", "calories": 50},
            {"name": "Cheese", "quantity": "50g", "calories": 200},
            {"name": "Bread Crumbs", "quantity": "20g", "calories": 70}
        ],
        "total_calories": 368,
        "food_preference": "Vegetarian",
        "instructions": "1. Bake eggplant slices. 2. Layer with tomato sauce and cheese. 3. Top with bread crumbs and bake."
    },
    {
        "recipe_name": "Shrimp Stir Fry",
        "ingredients": [
            {"name": "Shrimp", "quantity": "200g", "calories": 170},
            {"name": "Broccoli", "quantity": "100g", "calories": 34},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Soy Sauce", "quantity": "10g", "calories": 10},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88}
        ],
        "total_calories": 322,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Heat olive oil in a pan. 2. Stir fry shrimp and vegetables until cooked. 3. Add soy sauce and mix well."
    },
    {
        "recipe_name": "Vegan Chili",
        "ingredients": [
            {"name": "Black Beans", "quantity": "200g", "calories": 220},
            {"name": "Tomatoes", "quantity": "100g", "calories": 20},
            {"name": "Bell Peppers", "quantity": "50g", "calories": 15},
            {"name": "Onions", "quantity": "50g", "calories": 20},
            {"name": "Garlic", "quantity": "5g", "calories": 8}
        ],
        "total_calories": 283,
        "food_preference": "Vegan",
        "instructions": "1. Sauté onions and garlic. 2. Add all ingredients and simmer until cooked."
    },
    {
        "recipe_name": "Turkey Sandwich",
        "ingredients": [
            {"name": "Turkey Breast", "quantity": "100g", "calories": 150},
            {"name": "Whole Wheat Bread", "quantity": "50g", "calories": 120},
            {"name": "Lettuce", "quantity": "20g", "calories": 3},
            {"name": "Tomato", "quantity": "20g", "calories": 4},
            {"name": "Mayonnaise", "quantity": "10g", "calories": 68}
        ],
        "total_calories": 345,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Toast bread. 2. Assemble sandwich with turkey, lettuce, tomato, and mayonnaise."
    },
    {
        "recipe_name": "Veggie Burger",
        "ingredients": [
            {"name": "Veggie Patty", "quantity": "100g", "calories": 200},
            {"name": "Whole Wheat Bun", "quantity": "50g", "calories": 120},
            {"name": "Lettuce", "quantity": "20g", "calories": 3},
            {"name": "Tomato", "quantity": "20g", "calories": 4},
            {"name": "Ketchup", "quantity": "10g", "calories": 10}
        ],
        "total_calories": 337,
        "food_preference": "Vegetarian",
        "instructions": "1. Cook veggie patty. 2. Assemble burger with bun, patty, lettuce, tomato, and ketchup."
    },
    {
        "recipe_name": "Beef Tacos",
        "ingredients": [
            {"name": "Beef", "quantity": "200g", "calories": 400},
            {"name": "Tortillas", "quantity": "100g", "calories": 218},
            {"name": "Lettuce", "quantity": "50g", "calories": 7},
            {"name": "Cheese", "quantity": "20g", "calories": 80}
        ],
        "total_calories": 705,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Cook beef. 2. Warm tortillas. 3. Assemble tacos with beef, lettuce, and cheese."
    },
    {
        "recipe_name": "Lentil Soup",
        "ingredients": [
            {"name": "Lentils", "quantity": "200g", "calories": 230},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Onions", "quantity": "50g", "calories": 20},
            {"name": "Celery", "quantity": "50g", "calories": 10},
            {"name": "Garlic", "quantity": "5g", "calories": 8}
        ],
        "total_calories": 288,
        "food_preference": "Vegan",
        "instructions": "1. Sauté onions, garlic, and celery. 2. Add lentils and carrots. 3. Simmer until lentils are cooked."
    },
    {
        "recipe_name": "Grilled Salmon",
        "ingredients": [
            {"name": "Salmon", "quantity": "200g", "calories": 400},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Lemon Juice", "quantity": "10g", "calories": 2}
        ],
        "total_calories": 490,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Marinate salmon with olive oil and lemon juice. 2. Grill until fully cooked."
    },
    {
        "recipe_name": "Falafel Wrap",
        "ingredients": [
            {"name": "Falafel", "quantity": "100g", "calories": 300},
            {"name": "Tortilla", "quantity": "50g", "calories": 109},
            {"name": "Lettuce", "quantity": "20g", "calories": 3},
            {"name": "Tomato", "quantity": "20g", "calories": 4},
            {"name": "Tahini Sauce", "quantity": "10g", "calories": 89}
        ],
        "total_calories": 505,
        "food_preference": "Vegan",
        "instructions": "1. Cook falafel. 2. Warm tortilla. 3. Assemble wrap with falafel, lettuce, tomato, and tahini sauce."
    },
    {
        "recipe_name": "Vegetable Curry",
        "ingredients": [
            {"name": "Potatoes", "quantity": "100g", "calories": 77},
            {"name": "Carrots", "quantity": "50g", "calories": 20},
            {"name": "Peas", "quantity": "50g", "calories": 42},
            {"name": "Coconut Milk", "quantity": "100g", "calories": 230},
            {"name": "Onions", "quantity": "50g", "calories": 20}
        ],
        "total_calories": 389,
        "food_preference": "Vegan",
        "instructions": "1. Sauté onions and carrots. 2. Add potatoes, peas, and coconut milk. 3. Simmer until vegetables are tender."
    },
    {
        "recipe_name": "Chicken Curry",
        "ingredients": [
            {"name": "Chicken Breast", "quantity": "200g", "calories": 220},
            {"name": "Coconut Milk", "quantity": "100g", "calories": 230},
            {"name": "Onions", "quantity": "50g", "calories": 20},
            {"name": "Garlic", "quantity": "5g", "calories": 8},
            {"name": "Ginger", "quantity": "5g", "calories": 4}
        ],
        "total_calories": 482,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Sauté onions, garlic, and ginger. 2. Add chicken and cook until browned. 3. Add coconut milk and simmer until chicken is cooked."
    },
    {
        "recipe_name": "Mushroom Risotto",
        "ingredients": [
            {"name": "Rice", "quantity": "200g", "calories": 260},
            {"name": "Mushrooms", "quantity": "100g", "calories": 22},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Parmesan Cheese", "quantity": "20g", "calories": 80}
        ],
        "total_calories": 450,
        "food_preference": "Vegetarian",
        "instructions": "1. Cook rice. 2. Sauté mushrooms in olive oil. 3. Mix rice and mushrooms with Parmesan cheese."
    },
    {
        "recipe_name": "Baked Salmon",
        "ingredients": [
            {"name": "Salmon", "quantity": "200g", "calories": 400},
            {"name": "Lemon Juice", "quantity": "10g", "calories": 2},
            {"name": "Olive Oil", "quantity": "10g", "calories": 88},
            {"name": "Garlic", "quantity": "5g", "calories": 8}
        ],
        "total_calories": 498,
        "food_preference": "Non-Vegetarian",
        "instructions": "1. Marinate salmon with olive oil, lemon juice, and garlic. 2. Bake until fully cooked."
    }
]

# Insert recipes into MongoDB
recipes_collection.insert_many(recipes_data)
print('Recipes inserted successfully!')