# Priority #8 - Case Study 31: String-Based Examination Answer Evaluation
# Objective: Evaluate student test answers by string comparison and scoring against answer keys.

def evaluate_exam(student_answers, answer_key, marks_per_correct=4, penalty_per_wrong=1):
    score = 0
    correct_cnt = 0
    wrong_cnt = 0
    unanswered_cnt = 0
    
    for q_id, correct_ans in answer_key.items():
        student_ans = student_answers.get(q_id, "").strip().upper()
        if not student_ans:
            unanswered_cnt += 1
        elif student_ans == correct_ans.upper():
            score += marks_per_correct
            correct_cnt += 1
        else:
            score -= penalty_per_wrong
            wrong_cnt += 1
            
    return {
        "Total Score": score,
        "Correct": correct_cnt,
        "Wrong": wrong_cnt,
        "Unanswered": unanswered_cnt
    }

def main():
    key = {1: "A", 2: "C", 3: "B", 4: "D", 5: "A"}
    student = {1: "A", 2: "C", 3: "D", 4: "D"}  # Q5 unanswered, Q3 wrong
    
    result = evaluate_exam(student, key)
    print("Examination Scorecard:")
    for k, v in result.items():
        print(f" - {k}: {v}")

if __name__ == "__main__":
    main()
