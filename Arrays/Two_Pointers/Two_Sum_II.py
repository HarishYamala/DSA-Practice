"""
Problem: Two Sum II - Input array is sorted
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium

Approach:
- Use two-pointer technique
- Move left/right based on comparison with target

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1