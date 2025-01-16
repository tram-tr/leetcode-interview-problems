# https://leetcode.com/problems/cutting-ribbons/
'''
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.


For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your task is to determine the maximum length of ribbon, x, that allows you to cut at least k ribbons, each of length x. You can discard any leftover ribbon from the cuts. If it is impossible to cut k ribbons of the same length, return 0.




Example 1:




Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.


Example 2:
Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.


Example 3:
Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
'''
# 1          max(ribbons)
# TTTTTTFFFFFF


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
       
        n = len(ribbons)
        def can_cut(size):
            s = 0
            for i in range(n):
                s += ribbons[i]//size
               
            return s >= k
           
        left = 0
        right = max(ribbons)
        while left < right:
            mid = right - (right - left) // 2
            if can_cut(mid):
                left = mid
            else:
                right = mid - 1


        return right


s = Solution()
print(s.maxLength(ribbons = [9,7,5], k = 3)) # 5
print(s.maxLength(ribbons = [7,5,9], k = 4)) # 4
print(s.maxLength(ribbons = [5,7,9], k = 22)) # 0
