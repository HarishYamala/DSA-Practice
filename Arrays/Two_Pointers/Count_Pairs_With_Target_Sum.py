"""
Problem: Count Pairs with Given Sum (Sorted Array)
Platform: GFG / DSA Practice
Difficulty: Medium

Problem Statement:
Given a sorted array arr[] and an integer target,
find the number of pairs in arr[] such that their sum equals target.
Pairs must use distinct indices.

Approach:
- Use two-pointer technique since array is sorted.
- If sum equals target:
    • If both elements are same → use nC2 formula.
    • Else count duplicates on both sides and multiply.
- If sum < target → move left pointer.
- If sum > target → move right pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countPairs(self, arr, target):
        left = 0
        right = len(arr) - 1
        count = 0
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum == target:
                
                # Case 1: All elements between left and right are same
                if arr[left] == arr[right]:
                    n = right - left + 1
                    count += (n * (n - 1)) // 2
                    break
                
                # Case 2: Duplicates on left or right
                left_count = 1
                right_count = 1
                
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left_count += 1
                    left += 1
                    
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right_count += 1
                    right -= 1
                
                count += left_count * right_count
                
                left += 1
                right -= 1
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return count