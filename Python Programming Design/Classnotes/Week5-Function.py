#1. Welcome() function
def Welcome():
    print("Welcome to learn Python Programming Design")
    print("Python is powerful")
    print("The teacher's name is David Li")
    return None

Welcome()
print("#")
print()

#2. a function has some parameters (arguments)
# sum_numbers()
def sum_numbers(a, b, c):
    sum = a + b + c
    return print(sum)

# lets call the sum_numbers() to reuse the code
sum_numbers(78.9, 45.2, 111.65)
sum_numbers(-45, 8952, 66.77)
print("#"*50)
print()

# 3. Practical real life example
# define a function to calculate the final score of a subject
# a = attendance: 10%
# b = assignment 1: 20%
# c = assignment 2: 20%
#d = midterm exam: 25%
#e = final exam: 25%

# let's define a function funal_score() to calculate a final grade of students
def final_score(a,b,c,d,e):
    final_score = 0
    final_score = a*0.1 + b*0.2 + d*0.25 + e*0.25
    return final_score
# let's call the function and help us calculate the final grades for all students 
student_name = input("Please input the student's name: ")
attendance = float(input("the attendace score for the student is: "))
assignment_one = float(input(" The assigntment 1 score for the student is: "))






# 4. Define a welcome_someone() function with a parameter (argument)
def welcome_someone(name):
    # the function block must be indented
    print("Hi, {}, Welcome to learn Python Programming Design!", format(name))
    print("Python is powerful")
    print("The teacher name is David Li")
    return None

# let's call the function welcome_someone() to resume the blocks of codes
name1 = input("Please input the people's name: ")
name2 = input("Please input the people's name: ")
name3 = input("Please input the people's name: ")
welcome_someone(name1)
welcome_someone(name2)
welcome_someone(name3)
print("#"*50)
print()

#5. Let's define a functio to evaluate the student's grade level with if elif else statement
# A, B, C, D, E 5 levels
def get_grade_level(score):
    if score <= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "D"
    else:
        return "E"

# let's call the function and test it
grade_input = float(input("Please input the student's exam score: "))
level = get_grade_level(grade_input)
print("The student's exam rade level is {}.".format(level))
print("#"*50)
print()

# 6. Define a function to return the average and maximum grades
def analyze_scores(scores):
    average = sum(scores)/len(scores)
    highest = max(scores)
    minimum = min(scores)

    return average, highest, minimum

# let's quickly call the function and test the function 
# 2 student's exam scores list
score1 = [70, 87, 99, 25, 52]
score2 = [45, 32, 88]
avg1, high1, min1 = analyze_scores(score1)
avg2, high2, min2 = analyze_scores(score2)
print("The average, maximum scores and minimum scores for student 1 is {}, {}, {}:".format(avg1, high1, min2))
print("The average, maximum scores and minimum scores for student 1 is {}, {}, {}:".format(avg2, high2, min2))
print("#"*50)
print()

# 7. Define a function to quickly  return the maximum numbers among 3 numbers
def find_maximum(n1, n2, n3):
    # let's use the conditional statement if.. elif ... else to compare the 3 number
    if n1 >= n2 and n1 >= n3:
        return print("The maximum number is {}.".formal(n1))
    elif n2 >= n1 and n2 >= n3:
        return print("The maximum number is {}.".format(n2))
    else:
        return print("The maximum number is {}.".format(n3))

# 9. Define a function to achieve a simple calculator
# this function takes 2 number and 1 

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return print("Zero is not to be divided")
    else: 
        return print("The operator is not supported!")
    
         
    