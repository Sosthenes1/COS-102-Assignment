def calculate_grade(score):
    """
    Calculates the letter grade based on the given score.
    """
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif score < 40:
        return "F"
    else:
        return "Invalid Score"  # Should ideally not be reached with proper input validation

def main():
    """
    Main function to run the grading system.
    """
    print("Welcome to the Simple Grading System!")

    while True:
        user_input = input("Enter the student's score: ").strip().lower()

        if user_input == 'exit':
            break

        try:
            score = int(user_input)
            if 0 <= score <= 100:
                grade = calculate_grade(score)
                print(f"The grade for score {score} is: {grade}")
            else:
                print("Invalid score. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit'.")

    print("Thank you for using the grading system.")

if __name__ == "__main__":
    main()