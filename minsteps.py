class Solution:
    def coverPoints(self, A, B):
        # write your method here
        totalStep = 0
        currentA = A[0]
        currentB = B[0]
        for i in range(1, len(A)) :
            totalStep += max(abs(currentA - A[i] ), abs(currentB - B[i]))
            currentA = A[i]
            currentB = B[i]
        return totalStep