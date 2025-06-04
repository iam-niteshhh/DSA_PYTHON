class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
                continue
            i+=1
        return len(nums[:length]), nums[:length]


a = Solution()
a.removeElement([3,2,2,3], 3)
