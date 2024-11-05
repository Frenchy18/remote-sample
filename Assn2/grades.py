# Name: Christopher Groves


def calculate_average(scores):
    """
    Calculate the average of a list of exam scores.

    Parameters:
    scores (list of int or float): List of exam scores.

    Returns:
    float: The average score.

    Raises:
    ValueError: If any score is less than 0 or greater than 100.
    ValueError: If the list of scores is empty.
    The ValueError must include a message clarifying the cause.
    """
    if not scores:
        raise ValueError("List is empty")
    
    total = 0

    for i in scores[:]:
        if 0<=i<=100:
            total += i
        else:
            raise ValueError(f"{i} is outside bounds (0 to 100)")

        
    return total/len(scores)


def determine_grade(score):
    """
    Determines the letter grade based on the average score:
        A >90%
        B 80-89
        C 70-79
        D 60-69
        F <60

    Parameters:
    score (float): The score.
    
    Returns:
    str: The letter grade (A, B, C, D, or F).
    """
    if score > 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    

def main(scores):
    try:
        average_score = calculate_average(scores)
        grade = determine_grade(average_score)
        
        print(f"Average Score: {average_score:.2f}")
        print(f"Average Grade: {grade}")
    
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    valid_scores = [85, 90, 78, 92, 88]  # Example list of scores
    main(valid_scores)
    
    invalid_scores = [85, 110, 78]  # Invalid score of 110
    main(invalid_scores)