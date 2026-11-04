# Priority #10 - Case Study 53: Food Waste Monitoring System
# Objective: Track daily food waste metrics across dining facilities and generate alert reports.

def analyze_food_waste(daily_waste_kg, warning_threshold=50.0):
    total_waste = sum(daily_waste_kg)
    avg_waste = total_waste / len(daily_waste_kg)
    max_waste = max(daily_waste_kg)
    exceeded_days = [day + 1 for day, waste in enumerate(daily_waste_kg) if waste > warning_threshold]
    
    return {
        "Total Waste (kg)": round(total_waste, 2),
        "Average Daily Waste (kg)": round(avg_waste, 2),
        "Peak Daily Waste (kg)": max_waste,
        "High Waste Days": exceeded_days
    }

def main():
    # Waste logged in kg for 7 days
    waste_logs = [42.5, 58.0, 39.0, 65.2, 48.0, 70.1, 35.4]
    metrics = analyze_food_waste(waste_logs, warning_threshold=50.0)
    
    print("Food Waste Analysis Summary:")
    for k, v in metrics.items():
        print(f" - {k}: {v}")

if __name__ == "__main__":
    main()
