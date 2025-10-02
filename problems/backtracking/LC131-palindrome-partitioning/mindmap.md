# Mind Map: Palindrome Partitioning

```mermaid
graph TD
    A[Palindrome Partitioning] --> B[Pattern Type]
    B --> C[Backtracking on String]
    
    C --> D[Key Components]
    D --> D1[Result List]
    D --> D2[Current Partition]
    D --> D3[Start Index]
    D --> D4[Palindrome Check]
    
    C --> E[Algorithm Steps]
    E --> E1[Base: start = len s]
    E --> E2[Try all substrings from start]
    E --> E3[Check if palindrome]
    E --> E4[Add to current]
    E --> E5[Recurse with end index]
    E --> E6[Remove from current]
    
    C --> F[Optimizations]
    F --> F1[DP for Palindrome Check]
    F --> F2[Memoization]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style E fill:#ffe66d
```

## Palindrome Check Methods

**1. Simple Reverse:**
```python
s == s[::-1]
```

**2. Two Pointers:**
```python
left, right = 0, len(s)-1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
return True
```

**3. DP Precomputation (Best for multiple checks):**
```python
# Build palindrome table once
dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
```
