class Solution:
    def searchInsert(self, nums, target) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                return mid
        return high+1


a=Solution()
print(a.searchInsert([1,2,3,4,5],2))
print(a.searchInsert([1,3,5,6],5))
print(a.searchInsert([1,3,5,6],2))
print(a.searchInsert([1,3,5,6],7))