def userInput():
    subject = dict.fromkeys(['physics', 'chemistry', 'biology', 'mathematics', 'computer'])

    for i in subject.keys():
        subject[i] = int(input("Enter the marks for {0} subject: ".format(i.title())))
    
    print(subject)
    return subject

def calculatePercentageAndGrade(marks):
    total_marks = 0
    grade = None
    for v in marks.values():
        total_marks += v
    
    percentage = (total_marks / 5)
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'
    
    print(f"Percentage: {percentage}% and Grade: {grade}.")


marks = userInput()

calculatePercentageAndGrade(marks)