"""
Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0
        for c in s:
            if c == '(':
                open_c += 1
            elif c == ')' and open_c > 0:
                open_c -= 1
            else:
                close_c += 1
        return open_c + close_c