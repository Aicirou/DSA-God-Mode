# Backtracking Cheat Code: Combination Sum II Pattern

## Template
```python
def combination_sum2(candidates, target):
    result = []
    current = []
    candidates.sort()  # MUST sort for duplicate handling
    
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
            backtrack(i + 1, remaining - candidates[i])  # i+1!
            current.pop()
    
    backtrack(0, target)
    return result
```

## Key Pattern Points
✅ **Sort first:** Required for duplicate handling
✅ **Skip condition:** `i > start and arr[i] == arr[i-1]`
✅ **No reuse:** Pass `i+1` not `i`
✅ **Base case:** remaining == 0

## Related Problems
- LC90: Subsets II (same duplicate handling)
- LC39: Combination Sum (allows reuse)
