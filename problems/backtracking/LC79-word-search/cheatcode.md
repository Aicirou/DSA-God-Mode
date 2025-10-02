# Backtracking Cheat Code: Grid Search Pattern

## Template
```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        # Base case: found word
        if index == len(word):
            return True
        
        # Check boundaries and match
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False
        
        # Mark visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Try 4 directions
        found = (backtrack(row+1, col, index+1) or
                backtrack(row-1, col, index+1) or
                backtrack(row, col+1, index+1) or
                backtrack(row, col-1, index+1))
        
        # Backtrack
        board[row][col] = temp
        
        return found
    
    # Try from each cell
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False
```

## Key Pattern Points
✅ **In-place marking:** Use special character '#'
✅ **4 directions:** up, down, left, right
✅ **Restore state:** Critical for backtracking
✅ **Try all starts:** Check every cell as starting point

## Common Mistakes
❌ Forgetting to restore cell value
❌ Not checking boundaries before accessing
❌ Using separate visited set (less efficient)

## Related Problems
- LC212: Word Search II (multiple words, trie)
- LC200: Number of Islands (grid DFS)
