# LC131: Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

**Link:** [LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)

## Examples

### Example 1:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2:
```
Input: s = "a"
Output: [["a"]]
```

## Constraints
- `1 <= s.length <= 16`
- `s` contains only lowercase English letters

## Approach

### Backtracking Strategy
1. Try all possible ways to partition the string
2. At each step, try all substrings starting from current position
3. Only continue if substring is a palindrome
4. When we reach end of string, we have a valid partition

### Decision Tree Example (s = "aab")
```
                    ""
           /         |         \
         "a"       "aa"       "aab"
        /   \        |
      "a"  "ab"     "b"
       |
      "b"
```

### Palindrome Check
Simple approach: Compare string with its reverse
```python
def is_palindrome(s):
    return s == s[::-1]
```

## Complexity Analysis
- **Time:** O(n × 2^n) - Generate all partitions, each palindrome check is O(n)
- **Space:** O(n) - Recursion depth

## Optimization
Can precompute palindrome status with DP:
```python
# dp[i][j] = True if s[i:j+1] is palindrome
# Saves repeated palindrome checks
```

## Key Insights
- Every single character is a palindrome
- Must try all possible partition points
- Only explore valid palindrome partitions
