"""
LeetCode 39: Combination Sum
Difficulty: Medium
Topics: Array, Backtracking

Problem: Find all unique combinations in candidates where the candidate numbers sum to target.
Link: https://leetcode.com/problems/combination-sum/
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Approach: Backtracking with reusable elements
        Time Complexity: O(n^(target/min)) - Branching factor depends on target and smallest candidate
        Space Complexity: O(target/min) - Maximum recursion depth
        """
        result = []
        current = []
        
        def backtrack(start, remaining):
            # Base cases
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
            
            # Try each candidate starting from start
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # Can reuse same element, so pass i (not i+1)
                backtrack(i, remaining - candidates[i])
                current.pop()  # Backtrack
        
        backtrack(0, target)
        return result
