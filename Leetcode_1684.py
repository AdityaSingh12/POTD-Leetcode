"""
1684. Count the no of consistent string

You are given a string allowed consisting of distinct characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

def countString():
    allowed = input("Enter allowed string: ")
    words = input("Enter any list: ").split()
    total_count = 0
    for word in words:
        if all(char in allowed for char in word):
            total_count = total_count+1
    print(total_count)
countString()