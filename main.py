def calculate_grade(percentage):
    # Decide the grade based on the percentage
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def main():
    # Ask how many subjects the student has
    try:
        num_subjects = int(input("Enter number of subjects: "))

        if num_subjects <= 0:
            print("Number of subjects must be positive.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    subjects = []
    total_marks = 0
    passed_all = True

    # Get the name and marks for every subject
    for i in range(num_subjects):
        name = input(f"Enter subject {i + 1} name: ").strip()

        if not name:
            print("Subject name cannot be empty.")
            return

        try:
            marks = float(input(f"Enter marks for {name} (out of 100): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

        except ValueError:
            print("Please enter valid numeric marks.")
            return

        subjects.append((name, marks))
        total_marks += marks

        # A subject requires at least 40 marks to pass
        if marks < 40:
            passed_all = False

    # Calculate the average percentage
    percentage = total_marks / num_subjects
    grade = calculate_grade(percentage)

    # Display the report
    print("\n===== GRADE REPORT =====")

    for name, marks in subjects:
        print(f"{name}: {marks:g}/100")

    print(f"Total marks: {total_marks:g}/{num_subjects * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    if passed_all:
        print("Result: PASS")
    else:
        print("Result: FAIL")


if __name__ == "__main__":
    main()