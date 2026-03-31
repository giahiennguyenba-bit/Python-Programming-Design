## Please create a program that takes in a list of numbers and calculates the sum of all even numbers in the list. You can use a for loop to iterate through each number in the list, and use the continue statement to skip over any odd numbers. (Hint: You can use the number % 2 == 0 to check the number is even, or the number % 2 !=0 to check the number is odd).#
list = [10, 13, 23, 14, 22, 88, 101, 112]
sum = 0
for i in list:
    if i % 2 == 0:
        sum += i
    if i % 2 != 0:
        continue
print("The sum of all even numbers in the list is:", sum)