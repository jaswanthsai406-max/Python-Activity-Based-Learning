# Priority #1 - Case Study 27: Advanced Numeric Pattern Generator
# Objective: Generate a dynamic numeric pattern based on matrix dimensions and rules.

def generate_pattern(n):
    """
    Generates an n x n numeric pattern where each cell (i, j) 
    contains min(i, j, n - 1 - i, n - 1 - j) + 1.
    """
    for i in range(n):
        row = []
        for j in range(n):
            val = min(i, j, n - 1 - i, n - 1 - j) + 1
            row.append(str(val))
        print(" ".join(row))

def main():
    try:
        size = int(input("Enter matrix size (N): "))
        if size <= 0:
            print("Size must be a positive integer.")
            return
        print(f"\nGenerated Numeric Pattern for N = {size}:\n")
        generate_pattern(size)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
