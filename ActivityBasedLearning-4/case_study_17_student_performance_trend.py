# Priority #4 - Case Study 17: Student Performance Trend Analysis
# Objective: Analyze student assessment scores across subjects to detect trends.

def analyze_performance(scores):
    if not scores:
        return "No scores provided."
    
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # Trend evaluation
    is_improving = all(scores[i] <= scores[i+1] for i in range(len(scores)-1))
    is_declining = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
    
    if is_improving:
        trend = "Consistent Improvement"
    elif is_declining:
        trend = "Declining Trend"
    else:
        trend = "Fluctuating Performance"
        
    return {
        "Average": round(avg_score, 2),
        "Highest": max_score,
        "Lowest": min_score,
        "Trend": trend
    }

def main():
    test_scores = [65, 72, 78, 85, 90]
    metrics = analyze_performance(test_scores)
    print("Student Performance Summary:")
    for k, v in metrics.items():
        print(f" - {k}: {v}")

if __name__ == "__main__":
    main()
