# Backtracking Cheat Code: Subsets with Duplicates Pattern

## Template
```python
def subsets_with_dup(nums):
    result = []
    current = []
    nums.sort()  # MUST sort first
    
    def backtrack(start):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            # Skip duplicates at same level
            if i > start and nums[i] == nums[i-1]:
                continue
            
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()
    
    backtrack(0)
    return result
```

## Key Pattern Points
✅ **Sort first:** Required for duplicate handling
✅ **Skip condition:** `i > start and nums[i] == nums[i-1]`
✅ **Same as LC78:** Just add the skip condition
✅ **Works for:** Subsets, combinations with duplicates

## Reusable Pattern
This exact skip pattern works for:
- LC90: Subsets II
- LC40: Combination Sum II
- LC47: Permutations II (slight variation)

## Related Problems
- LC78: Subsets (no duplicates)
- LC40: Combination Sum II (same pattern)
