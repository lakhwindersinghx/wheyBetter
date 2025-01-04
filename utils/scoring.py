def calculate_score(high_quality, fillers, artificial):
    # Scoring logic
    score = 10
    score += len(high_quality) * 2
    score -= len(fillers) * 1
    score -= len(artificial) * 2
    return max(score, 0)  # Ensure score doesn't go below 0
