# Personal Notes: LC90 Subsets II

## First Attempt
- **Date:** 2024-01-20
- **Time Taken:** 20 minutes
- **Result:** Solved ✓ (easier after LC40)

## Challenges Faced
1. None - knew the pattern from LC40
   - Used same duplicate handling technique
   - Just applied to subsets instead of combination sum

## Aha Moments 💡
- Same pattern as LC40 Combination Sum II
- Only difference is no target sum constraint
- The skip condition is universally applicable

## Pattern Recognition
```python
# Universal duplicate handling in backtracking:
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i-1]:
        continue
    # ... rest of backtracking
```

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review
- [ ] Week 1: Compare with LC78 and LC40
