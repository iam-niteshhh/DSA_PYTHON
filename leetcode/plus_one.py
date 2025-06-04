class Solution:
    def plusOne(self, digits):
        length = len(digits)
        j = length-1
        while j>=0:
            x = digits[j]
            x = x+1
            if x<=9:
                digits[j] = x
                break
            else:
                digits[j] = 0
                j -=1
                continue
        if j == -1:
            digits.append(0)
            digits[0] = 1
        return digits


a = Solution()
print(a.plusOne([8,9,9,9]))