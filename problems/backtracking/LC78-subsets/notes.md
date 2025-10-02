# Personal Notes: LC78 Subsets

## First Attempt
- **Date:** 2024-01-15
- **Time Taken:** 35 minutes
- **Result:** Solved ✓

## Challenges Faced
1. Initially forgot to make a copy of `current` array
   - Bug: All results pointed to same reference
   - Fix: Use `current[:]` or `current.copy()`

2. Confused about when to add to result
   - Tried adding only at leaf nodes → Wrong!
   - Should add at every node in decision tree

## Aha Moments 💡
- Every subset is valid at every stage
- The decision tree naturally generates all combinations
- Similar to DFS but we collect at every node, not just leaves

## Alternative Approaches
1. **Iterative (Cascading)**
   ```python
   result = [[]]
   for num in nums:
       result += [curr + [num] for curr in result]
   return result
   ```
   
2. **Bit Manipulation**
   - Use binary representation
   - Each bit = include/exclude element

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review
- [ ] Week 1: Solve variations
- [ ] Month 1: Revisit without notes

## Connection to Other Problems
- Same pattern as LC46 (Permutations) but with start index
- Foundation for LC90 (Subsets II) - just add duplicate handling
