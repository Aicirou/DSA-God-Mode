# Personal Notes: LC40 Combination Sum II

## First Attempt
- **Date:** 2024-01-18
- **Time Taken:** 40 minutes
- **Result:** Solved after debugging ✓

## Challenges Faced
1. Forgot to sort the array first
   - Bug: Duplicate handling didn't work
   - Fix: Must sort before backtracking

2. Wrong skip condition
   - Used `i > 0` instead of `i > start`
   - Bug: Skipped valid combinations
   - Fix: `i > start` ensures we only skip at same level

## Aha Moments 💡
- The condition `i > start` is crucial
- Allows [1,1,2] but prevents [1,2] and [1,2] duplicates
- Sorting enables the duplicate check

## Key Pattern: Duplicate Handling
```python
if i > start and arr[i] == arr[i-1]:
    continue
```
This pattern is reusable in:
- LC90: Subsets II
- LC47: Permutations II

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review duplicate handling
- [ ] Week 1: Apply to LC90
