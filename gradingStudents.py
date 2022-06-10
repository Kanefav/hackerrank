def gradingStudents(grades):
    for grade in range(0, len(grades)):
        if grades[grade] >= 38:
            string = str(grades[grade])[-1]
            if 5 - int(string) <= 2 and  5 - int(string) >= 0:
                grades[grade] += 5 - int(string)
            elif 5 - int(string) <= -3:
                grades[grade] += 10 - int(string)
    return grades
    

print(gradingStudents([79]))