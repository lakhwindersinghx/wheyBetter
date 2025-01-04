from database import connect_to_database
from utils.scoring import calculate_score

def analyze_ingredients(ingredients):
    # Initialize response
    response = {
        "high_quality": [],
        "fillers": [],
        "artificial": [],
        "neutral": [],
        "unknown": []
    }

    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor(dictionary=True)

    for ingredient in ingredients:
        # Query the database
        cursor.execute("SELECT category, impact, notes FROM ingredients WHERE ingredient = %s", (ingredient,))
        result = cursor.fetchone()

        if result:
            # Categorize based on database result
            category = result["category"].lower()
            if category in response:
                response[category].append(ingredient)
            else:
                response["neutral"].append(ingredient)  # Fallback to neutral if the category is invalid
        else:
            # Mark as unknown if the ingredient is not in the database
            response["unknown"].append(ingredient)

    # Add a score based on categories
    response["score"] = calculate_score(response["high_quality"], response["fillers"], response["artificial"])

    # Close database connection
    cursor.close()
    conn.close()

    return response
