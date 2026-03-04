class Solution:
    def checkPangram(self, s):

        s = s.lower()

        letters = set()

        for i in s:
            if i.isalpha():
                letters.add(i)

        return len(letters) == 26
