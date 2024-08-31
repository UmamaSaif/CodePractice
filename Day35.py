"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")

        for word in words:
            lower=word.lower()
            if set(lower).issubset(row1) or set(lower).issubset(row2) or set(lower).issubset(row3):
                result.append(word)
        return result
