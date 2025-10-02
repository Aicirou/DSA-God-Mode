"""
LeetCode 90: Subsets II
Difficulty: Medium
Topics: Array, Backtracking

Problem: Given an integer array with possible duplicates, return all possible unique subsets.
Link: https://leetcode.com/problems/subsets-ii/
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Approach: Backtracking with duplicate handling
        Time Complexity: O(n * 2^n) - Generate all subsets and copy them
        Space Complexity: O(n) - Recursion stack depth
        """
        result = []
        current = []
        nums.sort()  # Sort to handle duplicates
        
        def backtrack(start):
            # Add current subset to result
            result.append(current[:])
            
            # Try adding each remaining number
            for i in range(start, len(nums)):
                # Skip duplicates at same level
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()  # Backtrack
        
        backtrack(0)
        return result
