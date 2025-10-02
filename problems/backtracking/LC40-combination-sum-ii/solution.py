"""
LeetCode 40: Combination Sum II
Difficulty: Medium
Topics: Array, Backtracking

Problem: Find all unique combinations where candidate numbers sum to target (each number used once).
Link: https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Approach: Backtracking with duplicate handling
        Time Complexity: O(2^n) - In worst case, explore all subsets
        Space Complexity: O(n) - Recursion depth
        """
        result = []
        current = []
        candidates.sort()  # Sort to handle duplicates
        
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at same level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                current.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i+1: no reuse
                current.pop()
        
        backtrack(0, target)
        return result
