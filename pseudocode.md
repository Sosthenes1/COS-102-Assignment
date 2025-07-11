START

  FUNCTION calculate_grade(score):
    IF score IS GREATER THAN OR EQUAL TO 70 AND score IS LESS THAN OR EQUAL TO 100 THEN
      RETURN "A"
    ELSE IF score IS GREATER THAN OR EQUAL TO 60 AND score IS LESS THAN OR EQUAL TO 69 THEN
      RETURN "B"
    ELSE IF score IS GREATER THAN OR EQUAL TO 50 AND score IS LESS THAN OR EQUAL TO 59 THEN
      RETURN "C"
    ELSE IF score IS GREATER THAN OR EQUAL TO 45 AND score IS LESS THAN OR EQUAL TO 49 THEN
      RETURN "D"
    ELSE IF score IS GREATER THAN OR EQUAL TO 40 AND score IS LESS THAN OR EQUAL TO 44 THEN
      RETURN "E"
    ELSE IF score IS LESS THAN 40 THEN
      RETURN "F"
    ELSE
      RETURN "Invalid Score"
    END IF
  END FUNCTION

  DISPLAY "Enter the student's score: "
  READ score

  IF score IS NOT A NUMBER THEN
    DISPLAY "Invalid input. Please enter a numerical score."
  ELSE IF score IS LESS THAN 0 OR score IS GREATER THAN 100 THEN
    DISPLAY "Score must be between 0 and 100."
  ELSE
    SET grade = calculate_grade(score)
    DISPLAY "The grade for a score of ", score, " is: ", grade
  END IF

END