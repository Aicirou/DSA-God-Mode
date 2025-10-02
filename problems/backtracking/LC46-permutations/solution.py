"""
LeetCode 46: Permutations
Difficulty: Medium
Topics: Array, Backtracking

Problem: Given an array nums of distinct integers, return all possible permutations.
Link: https://leetcode.com/problems/permutations/
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(n! * n) - Generate n! permutations, each takes O(n) to copy
        Space Complexity: O(n) - Recursion stack depth
        """
        result = []
        current = []
        used = [False] * len(nums)
        
        def backtrack():
            # Base case: current permutation is complete
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            # Try adding each unused number
            for i in range(len(nums)):
                if not used[i]:
                    current.append(nums[i])
                    used[i] = True
                    backtrack()
                    current.pop()  # Backtrack
                    used[i] = False
        
        backtrack()
        return result
