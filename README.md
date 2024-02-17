# With-python

In Python, there are various ways to get input from the user, depending on the type of data you want to receive and how you want to process it. Here are several common methods:

**Single Integer Input:**

num = int(input("Enter an integer: "))


**Single String Input:**

name = input("Enter your name: ")


**Single Float Input:**

num = float(input("Enter a float: "))


**Multiline Input (Multiple strings until an empty line is entered):**

lines = []
while True:
    line = input("Enter a line (or leave empty to finish): ")
    if not line:
        break
    lines.append(line)

**    
Array of Inputs (Accepting multiple space-separated values as input and converting them into a list):**

arr = list(map(int, input("Enter space-separated integers: ").split()))


**List of Integers (Taking input as a list of integers):**

num_list = [int(x) for x in input("Enter space-separated integers: ").split()]


**List of Strings (Taking input as a list of strings):**

str_list = input("Enter space-separated strings: ").split()


**Using Command-Line Arguments (Input from command line arguments when executing the script):**

import sys
arg1 = sys.argv[1]  # First command-line argument
arg2 = sys.argv[2]  # Second command-line argument
    

    



  

