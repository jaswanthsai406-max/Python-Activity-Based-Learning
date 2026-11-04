# Priority #3 - Case Study 16: Multi-Day Water Tank Simulation
# Objective: Simulate multi-day water tank inflow/outflow and monitor capacity status.

def simulate_water_tank(capacity, initial_level, daily_logs):
    current_level = initial_level
    print(f"Initial Tank Level: {current_level} L / {capacity} L")
    print("-" * 50)
    
    for day, (inflow, outflow) in enumerate(daily_logs, 1):
        current_level += inflow
        overflow = 0
        if current_level > capacity:
            overflow = current_level - capacity
            current_level = capacity
            
        current_level -= outflow
        underflow = False
        if current_level < 0:
            underflow = True
            current_level = 0
            
        print(f"Day {day}: Inflow={inflow}L, Outflow={outflow}L -> Current Level={current_level}L "
              f"| Overflow={overflow}L | Deficit/Empty={underflow}")

def main():
    capacity = 1000  # Liters
    initial_level = 300
    logs = [
        (500, 200),  # Day 1: +500, -200
        (400, 300),  # Day 2: +400, -300
        (100, 700),  # Day 3: +100, -700
        (600, 200)   # Day 4: +600, -200
    ]
    simulate_water_tank(capacity, initial_level, logs)

if __name__ == "__main__":
    main()
