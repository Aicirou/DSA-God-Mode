# Backtracking Cheat Code: Subsets Pattern

## Template
```python
def backtrack_subsets(nums):
    result = []
    current = []
    
    def backtrack(start):
        result.append(current[:])  # Add current state
        
        for i in range(start, len(nums)):
            current.append(nums[i])   # Choose
            backtrack(i + 1)          # Explore
            current.pop()             # Unchoose
    
    backtrack(0)
    return result
```

## Key Pattern Points
✅ **When to use:** Generate all combinations/subsets
✅ **Decision:** Include or exclude current element
✅ **Base case:** No explicit base case (implicit when start >= len)
✅ **Backtrack:** Remove last element after recursion

## Variations
- **Subsets:** Start index, no constraints
- **Subsets II:** Start index + skip duplicates
- **Combinations:** Start index + size constraint
- **Permutations:** Used array + no start index

## Common Mistakes
❌ Forgetting to copy current array: `result.append(current[:])`
❌ Not incrementing start: `backtrack(i + 1)` not `backtrack(i)`
❌ Modifying after recursion without backtracking

## Related Problems
- LC90: Subsets II (with duplicates)
- LC77: Combinations (fixed size)
- LC39: Combination Sum (reusable elements)
