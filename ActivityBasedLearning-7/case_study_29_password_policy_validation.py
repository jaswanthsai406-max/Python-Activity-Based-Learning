# Priority #7 - Case Study 29: Password Policy Validation Engine
# Objective: Validate input passwords against customizable security policies.

import re

def validate_password(password):
    rules = {
        "Minimum length of 8 characters": len(password) >= 8,
        "Contains at least one uppercase letter": bool(re.search(r'[A-Z]', password)),
        "Contains at least one lowercase letter": bool(re.search(r'[a-z]', password)),
        "Contains at least one digit": bool(re.search(r'\d', password)),
        "Contains at least one special character": bool(re.search(r'[@$!%*?&#]', password))
    }
    
    passed_all = all(rules.values())
    return passed_all, rules

def main():
    pwd = input("Enter password to evaluate: ")
    is_valid, report = validate_password(pwd)
    
    print("
Validation Results:")
    for rule, status in report.items():
        symbol = "[PASS]" if status else "[FAIL]"
        print(f" {symbol} {rule}")
        
    print(f"
Final Status: {'STRONG / VALID' if is_valid else 'WEAK / INVALID'}")

if __name__ == "__main__":
    main()
