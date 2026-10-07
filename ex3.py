#print sum of first 10 even numbers using for loop
sum_even = 0
for i in range(2, 21, 2):
    sum_even += i
print("The sum of the first 10 even numbers is:", sum_even)
#accept two values S and N . print square of N numbers starting from  S


S = int(input("Enter the starting value (S): "))
N = int(input("Enter the number of values (N): "))
for i in range(S, S + N):
    print(f"The square of {i} is {i**2}")
