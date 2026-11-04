# Priority #2 - Case Study 12: Attendance Recovery Computation
# Objective: Calculate minimum classes required to achieve a target attendance percentage.

import math

def calculate_required_classes(total_conducted, total_attended, target_pct=75.0):
    current_pct = (total_attended / total_conducted) * 100
    print(f"Current Attendance: {current_pct:.2f}%")
    
    if current_pct >= target_pct:
        return 0, current_pct
    
    # Formula: (total_attended + x) / (total_conducted + x) >= target / 100
    # x >= (target * total_conducted - 100 * total_attended) / (100 - target)
    target_fraction = target_pct / 100.0
    required = math.ceil((target_fraction * total_conducted - total_attended) / (1.0 - target_fraction))
    return max(0, required), current_pct

def main():
    try:
        conducted = int(input("Enter total classes conducted: "))
        attended = int(input("Enter total classes attended: "))
        
        if conducted <= 0 or attended < 0 or attended > conducted:
            print("Invalid input: Attended classes cannot exceed conducted classes.")
            return
            
        needed, current = calculate_required_classes(conducted, attended)
        if needed == 0:
            print("Target attendance already achieved!")
        else:
            print(f"Additional consecutive classes needed for 75%: {needed}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
