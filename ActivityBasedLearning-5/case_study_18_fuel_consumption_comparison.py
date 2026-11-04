# Priority #5 - Case Study 18: Fuel Consumption and Route Comparison
# Objective: Compare trip routes based on distance, traffic conditions, and fuel efficiency.

def calculate_route_cost(distance_km, avg_speed_kmh, fuel_efficiency_kml, fuel_price_per_l):
    fuel_needed = distance_km / fuel_efficiency_kml
    total_cost = fuel_needed * fuel_price_per_l
    travel_time_hrs = distance_km / avg_speed_kmh
    return round(fuel_needed, 2), round(total_cost, 2), round(travel_time_hrs, 2)

def main():
    fuel_price = 100.0  # Cost per liter
    routes = {
        "Route A (Highway)": {"distance": 120, "speed": 80, "efficiency": 15},
        "Route B (City/Short)": {"distance": 90, "speed": 40, "efficiency": 10},
        "Route C (Bypass)": {"distance": 105, "speed": 60, "efficiency": 12.5}
    }
    
    print(f"{'Route':<22} | {'Fuel (L)':<10} | {'Cost (₹)':<10} | {'Time (hrs)':<10}")
    print("-" * 60)
    for name, r in routes.items():
        fuel, cost, time_hrs = calculate_route_cost(r["distance"], r["speed"], r["efficiency"], fuel_price)
        print(f"{name:<22} | {fuel:<10} | {cost:<10} | {time_hrs:<10}")

if __name__ == "__main__":
    main()
