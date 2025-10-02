"""
LeetCode 79: Word Search
Difficulty: Medium
Topics: Array, Backtracking, Matrix

Problem: Given a 2D board and a word, find if the word exists in the grid.
Link: https://leetcode.com/problems/word-search/
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Approach: Backtracking with DFS
        Time Complexity: O(m * n * 4^L) - Try 4 directions for each character
        Space Complexity: O(L) - Recursion depth where L is word length
        """
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(row, col, index):
            # Base case: found entire word
            if index == len(word):
                return True
            
            # Check boundaries and character match
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                board[row][col] != word[index]):
                return False
            
            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore all 4 directions
            found = (backtrack(row+1, col, index+1) or
                    backtrack(row-1, col, index+1) or
                    backtrack(row, col+1, index+1) or
                    backtrack(row, col-1, index+1))
            
            # Backtrack: restore the cell
            board[row][col] = temp
            
            return found
        
        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
