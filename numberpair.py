class Solution:
    def numSetBits(self, a):
        result = 0
        while a:
            a &= a - 1
            result += 1
        return result
        # write your method here