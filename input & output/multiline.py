# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.

# Output Description:
# Print the taken input in the same format.

# Sample Input :
# 5 3
# 1 2 3 4 5
# Sample Output :
# 5 3
# 1 2 3 4 5


class get_input:

    def input1(self):
        s,k=map(int,input().split())
        arr=list(map(str,input().split()))
        # print(arr)
        print(s,k)
        print(" ".join(arr))

obj=get_input()
obj.input1()
