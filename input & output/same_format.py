# Write a code to get the input in the given format and print the output in the given format

# Input Description:
# First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.

# Output Description:
# Print the input in the same format.

# Sample Input :
# 2 4
# 2 4
# 2 4
# Sample Output :
# 2 4
# 2 4
# 2 4


# Sample Input :
# 2 5
# 2 5 6
# 2 4 5
# Sample Output :
# 2 5
# 2 5 6
# 2 4 5

class get_input:

    def input1(self):
        s=" ".join(list(map(str,input().split())))
        t=" ".join(list(map(str,input().split())))
        u=" ".join(list(map(str,input().split())))
        print(s)
        print(t)
        print(u)

obj=get_input()
obj.input1()