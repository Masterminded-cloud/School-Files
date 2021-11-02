grades = [
    [71, 14, 41, 87, 49, 93],
    [66, 73, 54, 55, 94, 79],
    [20, 51, 77, 20, 86, 15],
    [79, 63, 72, 57, 63, 73],
    [30, 66, 78, 65, 41, 45],
    [11, 83, 51, 47, 68, 63],
    [99, 43, 85, 86, 24, 75],
    [67, 102, 11, 84, 64, 109],
    [16, 24, 101, 78, 55, 89],
    [100, 26, 37, 95, 106, 100],
    [55, 77, 30, 34, 28, 15],
    [87, 67, 13, 71, 67, 83],
    [95, 65, 94, 56, 15, 92],
    [102, 23, 36, 39, 60, 39],
    [90, 59, 96, 105, 83, 16],
    [101, 40, 17, 12, 44, 36],
    [39, 63, 96, 12, 65, 82],
    [95, 20, 105, 34, 69, 95],
    [95, 93, 75, 18, 105, 102],
    [35, 15, 82, 106, 73, 30],
    [80, 52, 67, 49, 11, 88],
    [86, 17, 44, 75, 78, 49],
    [22, 60, 74, 110, 92, 37],
    [13, 14, 15, 82, 75, 57],
    [71, 106, 15, 77, 30, 98],
    [43, 80, 76, 85, 102, 53],
    [26, 98, 60, 80, 104, 79],
    [12, 28, 40, 106, 88, 84],
    [82, 75, 101, 29, 51, 75],
    [20, 31, 84, 35, 19, 85],
    [84, 63, 56, 101, 83, 102],
    [25, 106, 36, 24, 61, 80],
    [86, 75, 89, 47, 28, 27],
    [38, 48, 22, 72, 53, 83],
    [70, 34, 46, 86, 32, 58],
    [83, 59, 38, 16, 94, 104],
    [62, 110, 13, 12, 13, 83],
    [90, 59, 55, 19, 69, 34],
    [73, 102, 60, 49, 67, 109],
    [94, 63, 100, 29, 64, 30],
    [105, 19, 12, 65, 65, 47],
    [10, 21, 72, 82, 104, 64],
    [39, 107, 107, 108, 63, 80],
    [52, 76, 77, 16, 49, 80],
    [35, 30, 58, 36, 52, 51],
    [102, 100, 22, 78, 57, 107],
    [63, 11, 69, 61, 71, 95],
    [76, 80, 83, 72, 79, 55],
    [104, 14, 14, 92, 17, 89],
    [46, 68, 108, 45, 23, 97]
    ]

def clean_grades(grades):
    """
    this function takes a list of lists; each sublist is assumed to be a list of
    integers of length at least 5 representing student grades.  The function modifies
    the grades by adding 2 to the 5th element for all sublists and replacing any values
    over 100 with 100.

    :param grades: A list of lists of integers.  Each inner list must have length at least 5.
    :return: None
    """
    for student in grades:
        student[4] = student[4] + 2
        for i in range(len(student)):
            if student[i] > 100:
                student[i] = 100


def student_averages(grades):
    """
    creates a list of integers representing student averages in the course.
    input is a list of lists, where each sublist contains 6 items: 4 assignment grades
    (worth 10% each), a midterm exam grade worth 20% and final exam worth 40%.
    Each student's final grade is rounded to the nearest integer.

    :param grades: list of lists of integers.  Each sublist must be size 6 and contain numbers
    in the range 0-100
    :return: a list of integers, each one in the range 0-100, representing student final grades
    """
    result = []
    for student in grades:
        total = 0.0
        for i in range(4):
            total += student[i]*0.1
        total += student[4]*0.2
        total += student[5]*0.4
        total = round(total)
        result.append(total)

    return result

def average(grades):
    """
    computes and returns the average of a list of integers
    :param grades: a list of integers
    :return: float representing the average of all numbers in the list
    """
    return sum(grades) / len(grades)

clean_grades(grades)
averages = student_averages(grades)
print("The final grades for the class are:")
print(averages)
print("The overall class average is:", average(averages))


