#!/usr/bin/python3
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Print newline after each row
    row += 1
