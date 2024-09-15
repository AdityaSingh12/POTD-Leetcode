"""
Find the longest substring contained vowels in even count

Given the string s, return the size of the longest substring 
containing each vowel an even number of times. 
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
"""

def findThelongestsubstring():
    s=input("Enter any string: ")
    vowels = {"a":0, "e":1, "i":2, "o":3, "u":4 }
    state_to_index = {0:-1}
    max_length = 0
    current_state = 0
    for i, char in enumerate(s):
        if char in vowels:
            current_state ^= (1<< vowels[char])
        if current_state in state_to_index:
            max_length = max(max_length, i - state_to_index[current_state])
        else:
            state_to_index[current_state] = i
    print(max_length)
findThelongestsubstring()