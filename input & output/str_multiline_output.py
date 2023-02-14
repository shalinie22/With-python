# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by line.

# Sample Input :
# guvigeek
# Sample Output :
# g
# u
# v
# i
# g
# e
# e
# k


class get_string:
    def input(self):
        strg=input()
        for i in strg:
            print(i)

obj=get_string()
obj.input()