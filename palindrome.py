class Solution:
    def isPalindrome(self, A):
        b=str(A)
        c=b[::-1]
        if(b==c):
            return(True)
        else:
            return(False)
        # write your method here