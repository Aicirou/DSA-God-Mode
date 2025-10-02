"""
LeetCode 78: Subsets
Difficulty: Medium
Topics: Array, Backtracking, Bit Manipulation

Problem: Given an integer array nums of unique elements, return all possible subsets.
Link: https://leetcode.com/problems/subsets/
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(n * 2^n) - Generate all subsets and copy them
        Space Complexity: O(n) - Recursion stack depth
        """
        result = []
        current = []
        
        def backtrack(start):
            # Add current subset to result
            result.append(current[:])
            
            # Try adding each remaining number
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()  # Backtrack
        
        backtrack(0)
        return result
