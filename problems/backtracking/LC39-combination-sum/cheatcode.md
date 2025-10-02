# Backtracking Cheat Code: Combination Sum Pattern

## Template
```python
def combination_sum(candidates, target):
    result = []
    current = []
    
    def backtrack(start, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, remaining - candidates[i])  # i, not i+1
            current.pop()
    
    backtrack(0, target)
    return result
```

## Key Pattern Points
✅ **When to use:** Find combinations with target sum
✅ **Reusability:** Pass `i` to allow reusing same element
✅ **Base case:** remaining == 0
✅ **Pruning:** remaining < 0 (stop early)

## Optimization Tips
- Sort candidates first for better pruning
- Break loop early if `candidates[i] > remaining`

## Related Problems
- LC40: Combination Sum II (no reuse)
- LC216: Combination Sum III (fixed size)
- LC377: Combination Sum IV (count only)
