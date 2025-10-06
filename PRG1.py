def evaluate_grade(mark):
    
    if mark is None or mark < 0 or mark > 100:
        return "Invalid Mark"
    elif mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "Fail"

if __name__ == "__main__":
    print("--- Student Grade Evaluation Program (Initial) ---")
    try:
        # Prompt the user for the mark
        mark_input = input("Enter the student's overall mark (0-100): ")
        mark = float(mark_input)

        grade = evaluate_grade(mark)

        print(f"\nStudent's Mark: {mark}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Error: Please enter a valid numerical mark.")

