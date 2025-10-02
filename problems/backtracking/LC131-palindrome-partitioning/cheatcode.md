# Backtracking Cheat Code: String Partitioning Pattern

## Template
```python
def partition_palindrome(s):
    result = []
    current = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start):
        if start == len(s):
            result.append(current[:])
            return
        
        # Try all possible end positions
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end)
                current.pop()
    
    backtrack(0)
    return result
```

## Key Pattern Points
✅ **When to use:** Partition string with constraints
✅ **Base case:** start == len(s)
✅ **Inner loop:** Try all end positions from start
✅ **Validation:** Check constraint (palindrome, etc.)

## Optimization: DP Palindrome Check
```python
def build_palindrome_table(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Single characters
    for i in range(n):
        dp[i][i] = True
    
    # Two characters
    for i in range(n-1):
        dp[i][i+1] = (s[i] == s[i+1])
    
    # Longer substrings
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    
    return dp
```

## Related Problems
- LC132: Palindrome Partitioning II (min cuts)
- LC139: Word Break (similar partitioning)
