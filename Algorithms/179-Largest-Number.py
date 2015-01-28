class Solution:
    def largestNumber(self, num):
        num = map(str,num)
        num.sort(cmp = lambda s1,s2:1 if s1+s2 > s2+s1 else -1 if s1+s2 < s2+s1 else 0, reverse = True)
        return str(int(''.join(num)))
