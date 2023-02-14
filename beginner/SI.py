# You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

# Print the output up to two decimal places (Round-off if necessary).

# (S.I. = P*T*R/100)

# Input Description:
# Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

# Output Description:
# Find the Simple interest and print it up to two decimal places. Round off if required.

# Sample Input :
# 1000 2 5
# Sample Output :
# 100.00

# P,R,T=map(int,input().split(" "))
# print(format((P*T*R)/100,".2f"))

P,R,T=map(float,input().split(" "))
si=(P*T*R)/100
print(round(si,2))