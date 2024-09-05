"""
2028. Find Missing Observations
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. 
n of the observations went missing, and you only have the observations of m rolls. 
Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. 
You are also given the two integers mean and n.

Return an array of length n containing the missing observations 
such that the average value of the n + m rolls is exactly mean. 
If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
"""

def missingRolls():
    n = int(input("Enter the no of missing observations: "))
    mean = int(input("Enter any mean value: "))
    rolls = list(map(int, input("Enter any list: ").split()))
    l  = len(rolls)
    m=l+n
    
    count=0
    sum=mean*(m)
    for i in range(0,len(rolls)):
        count= count+rolls[i]

    result=sum-count
    
    min_value=1
    max_value=6
    min_sum = n * min_value
    max_sum = n * max_value

    if result < min_sum or result > max_sum:
        print([])  
        return
    
    parts = [min_value] * n
    remaining_sum = result - min_sum
    i = 0

    while remaining_sum > 0 and i < n:
        add_value = min(max_value - parts[i], remaining_sum)
        parts[i] += add_value
        remaining_sum -= add_value
        i += 1
    print(parts)
    

missingRolls()

