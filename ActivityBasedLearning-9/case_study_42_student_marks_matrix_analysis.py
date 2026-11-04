# Priority #9 - Case Study 42: Student Marks Matrix Analysis
# Objective: Process a 2D matrix of student marks to compute totals, averages, and class rank.

def analyze_marks_matrix(matrix, student_names, subject_names):
    num_students = len(matrix)
    num_subjects = len(matrix[0])
    
    student_totals = [sum(row) for row in matrix]
    student_averages = [tot / num_subjects for tot in student_totals]
    
    subject_averages = [
        sum(matrix[i][j] for i in range(num_students)) / num_students
        for j in range(num_subjects)
    ]
    
    return student_totals, student_averages, subject_averages

def main():
    students = ["Alice", "Bob", "Charlie"]
    subjects = ["Math", "Physics", "Chemistry"]
    
    # Rows: Students, Columns: Subjects
    marks = [
        [85, 90, 88],  # Alice
        [78, 82, 80],  # Bob
        [92, 95, 94]   # Charlie
    ]
    
    totals, st_avgs, sub_avgs = analyze_marks_matrix(marks, students, subjects)
    
    print(f"{'Student':<10} | {'Total':<6} | {'Average':<8}")
    print("-" * 30)
    for i in range(len(students)):
        print(f"{students[i]:<10} | {totals[i]:<6} | {st_avgs[i]:<8.2f}")
        
    print("
Subject Averages:")
    for j in range(len(subjects)):
        print(f" - {subjects[j]}: {sub_avgs[j]:.2f}")

if __name__ == "__main__":
    main()
