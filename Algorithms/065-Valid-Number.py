class Solution:
    def isNumber(self, s):
        try:
            float(s)
        except ValueError:
            return False
        return True
