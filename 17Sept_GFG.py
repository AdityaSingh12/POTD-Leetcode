"""
Minimize the Heights II

Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
"""

def getMinDiff():
    k=int(input("Enter the height you want to increase or decrease: "))
    arr=list(map(int, input("Enter the heights of tower: ").split()))
    n=len(arr)
    arr.sort()
    diff = arr[n-1] - arr[0]
    for i in range(1,n):
        if arr[i] - k < 0:
            continue
        if arr[0] + k < arr[i] - k:
            mini = arr[0] + k        
        else:
            mini = arr[i] - k
        if arr[i-1] + k > arr[n-1] - k:
            maxi = arr[i-1] + k
        else:
            maxi = arr[n-1] - k
        current_diff = maxi - mini
        if current_diff < diff:
            diff = current_diff
    print(diff)
getMinDiff()