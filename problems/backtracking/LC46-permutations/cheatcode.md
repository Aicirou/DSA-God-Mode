# Backtracking Cheat Code: Permutations Pattern

## Template
```python
def backtrack_permutations(nums):
    result = []
    current = []
    used = [False] * len(nums)
    
    def backtrack():
        if len(current) == len(nums):
            result.append(current[:])  # Base case
            return
        
        for i in range(len(nums)):
            if not used[i]:
                current.append(nums[i])  # Choose
                used[i] = True
                backtrack()              # Explore
                current.pop()            # Unchoose
                used[i] = False
    
    backtrack()
    return result
```

## Key Pattern Points
✅ **When to use:** Generate all arrangements/orderings
✅ **Decision:** Which unused element to add next
✅ **Base case:** Current length equals target length
✅ **State tracking:** Boolean array or set for used elements

## Variations
- **Permutations:** Use all elements, track used
- **Permutations II:** Add duplicate handling, sort + skip
- **Subsets:** No used tracking, use start index
- **Combinations:** Start index + size limit

## Common Mistakes
❌ Forgetting to mark element as unused after backtracking
❌ Not copying the current array before adding to result
❌ Using start index (makes it combinations, not permutations)
❌ Not having proper base case check

## Alternative Approach: In-place Swapping
```python
def permute_swap(nums):
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Swap back
    
    backtrack(0)
    return result
```

## Related Problems
- LC47: Permutations II (with duplicates)
- LC60: Permutation Sequence
- LC31: Next Permutation
