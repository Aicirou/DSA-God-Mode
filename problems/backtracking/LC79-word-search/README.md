# LC79: Word Search

## Problem Statement
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Link:** [LeetCode 79](https://leetcode.com/problems/word-search/)

## Examples

### Example 1:
```
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:
```
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3:
```
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCB"
Output: false
```

## Constraints
- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters

## Approach

### Backtracking + DFS Strategy
1. Try starting from each cell in the board
2. Use DFS to explore in all 4 directions
3. Mark visited cells to avoid reuse
4. Backtrack by unmarking cells
5. Return true if word is found

### Visited Cell Handling
Instead of using a separate visited set, we modify the board in-place:
- Mark cell as '#' when visiting
- Restore original value when backtracking

## Complexity Analysis
- **Time:** O(m × n × 4^L) - Try from each cell, explore 4 directions for L characters
- **Space:** O(L) - Recursion depth equals word length

## Key Insights
- In-place marking is space efficient
- Must try from every cell as potential starting point
- Early termination when character doesn't match
