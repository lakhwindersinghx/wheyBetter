from database import connect_to_database
from utils.scoring import calculate_score

def analyze_ingredients(ingredients):
    try:
        # Initialize response
        response = {
            "high_quality": [],
            "fillers": [],
            "artificial": [],
            "neutral": [],
            "unknown": []
        }

        print("Connecting to database...")
        # Connect to the database
        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)
        print("Database connection established.")

        for ingredient in ingredients:
            print(f"Processing ingredient: {ingredient}")
            # Query the database
            cursor.execute("SELECT category, impact, notes FROM ingredients WHERE ingredient = %s", (ingredient,))
            result = cursor.fetchone()

            if result:
                print(f"Found in database: {result}")
                # Categorize based on database result
                category = result["category"].lower()
                if category in response:
                    response[category].append(ingredient)
                else:
                    response["neutral"].append(ingredient)
            else:
                print(f"Not found in database: {ingredient}")
                # Mark as unknown if the ingredient is not in the database
                response["unknown"].append(ingredient)

        # Add a score based on categories
        print("Calculating score...")
        response["score"] = calculate_score(response["high_quality"], response["fillers"], response["artificial"])

        # Close database connection
        cursor.close()
        conn.close()
        print("Database connection closed.")

        return response
    except Exception as e:
        print(f"Error in analyze_ingredients: {e}")
        raise
