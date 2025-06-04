class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n -1
        k =  m + n - 1
        while i >= 0 and j >= 0:
            print(i,j,k)
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
            print(nums1, nums2)

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)

a = Solution()
# a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
a.merge([4,5,6,0,0,0], 3, [1,2,3], 3)