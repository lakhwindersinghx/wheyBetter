def calculate_score(high_quality, fillers, artificial,unknown,neutral):
    base_score=10
    base_score += len(high_quality) * 2
    base_score -= len(fillers) * 2  # Deduct points for fillers
    base_score -= len(artificial) * 3  # Deduct more for artificial ingredients
    base_score -= len(unknown) * 1  # Slight penalty for unknown ingredients
    base_score -= len(neutral) * 0.5  # Minor penalty for neutral ingredients
    return max(base_score, 0)  # Ensure score is not negative