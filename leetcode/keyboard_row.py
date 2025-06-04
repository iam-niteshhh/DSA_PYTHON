class Solution:
    def findWords(self, words):
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"

        answer = []
        for word in words:
            w = word.lower()
            if len(set(w + l1)) == len(l1) or len(set(w + l2)) == len(l2) or len(set(w + l3))== len(l3):
                answer.append(word)
        return answer

a = Solution()
print(a.findWords(["Hello","Alaska","Dad","Peace"]))