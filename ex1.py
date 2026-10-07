#create a list of numbers of 10 numbers and display the sum of last 4 elements in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_last_four = sum(numbers[-4:])
print("The sum of the last 4 elements is:", sum_last_four)
#remove numbers from list located at 5 and 2 positions
del numbers[4]
del numbers[1]
print("The list after removing elements at positions 5 and 2 is:", numbers)
#print difference between the largest and smallest number in the list
largest = max(numbers)
smallest = min(numbers)
difference = largest - smallest
print("The difference between the largest and smallest number is:", difference)


