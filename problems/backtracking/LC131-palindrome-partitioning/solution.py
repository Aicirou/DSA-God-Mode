"""
LeetCode 131: Palindrome Partitioning
Difficulty: Medium
Topics: String, Backtracking, Dynamic Programming

Problem: Partition string into all possible palindrome substrings.
Link: https://leetcode.com/problems/palindrome-partitioning/
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        Approach: Backtracking with palindrome check
        Time Complexity: O(n * 2^n) - Generate all partitions and check palindromes
        Space Complexity: O(n) - Recursion depth
        """
        result = []
        current = []
        
        def is_palindrome(sub):
            """Check if substring is palindrome"""
            return sub == sub[::-1]
        
        def backtrack(start):
            # Base case: reached end of string
            if start == len(s):
                result.append(current[:])
                return
            
            # Try all possible partitions from start
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end)
                    current.pop()  # Backtrack
        
        backtrack(0)
        return result
