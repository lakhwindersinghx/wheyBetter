from utils.scoring import calculate_score

def analyze_ingredients(ingredients):
    # Simulate database lookup
    ingredient_data = {
        "Whey Protein Isolate": "high_quality",
        "Maltodextrin": "filler",
        "Sucralose": "artificial"
    }

    response = {
        "high_quality": [],
        "fillers": [],
        "artificial": [],
        "neutral": []
    }

    for ingredient in ingredients:
        category = ingredient_data.get(ingredient, "neutral")
        if category in response:
            response[category].append(ingredient)
        else:
            response["neutral"].append(ingredient)

    # Add a score based on categories
    response["score"] = calculate_score(response["high_quality"], response["fillers"], response["artificial"])

    return response
