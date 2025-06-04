class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            c_l = r - l
            c_h = min(height[l], height[r])
            area = c_h * c_l
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1

        return max_area

a = Solution()
a.maxArea([1,8,6,2,5,4,8,3,7])