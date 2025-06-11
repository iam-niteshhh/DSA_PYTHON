from annotated_types.test_cases import cases


class Solution:
    def longestPalindrome(self, s):
        ls = ""
        lsl = 0

        #odd cases
        for i in range(len(s)):
            low, high = i, i
            while low>=0 and high<len(s) and s[low] == s[high]:
                if lsl < high - low + 1:
                    ls = s[low: high + 1]
                    lsl = len(ls)
                low -= 1
                high += 1

        # even case
        for i in range(len(s)):
            low, high = i, i+1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if lsl < high - low + 1:
                    ls = s[low: high + 1]
                    lsl = len(ls)
                low -= 1
                high += 1
        return ls


a = Solution()
print(a.longestPalindrome("babad"))
a.longestPalindrome("cbbd")
