# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle each row
while row < size:
    # Inner for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    print()  
    row += 1
