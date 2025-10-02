# Personal Notes: LC46 Permutations

## First Attempt
- **Date:** 2024-01-16
- **Time Taken:** 25 minutes
- **Result:** Solved ✓

## Challenges Faced
1. Initially confused with subsets pattern
   - Used start index → Generated combinations instead
   - Fix: Use used array instead of start index

2. Forgot to unmark used elements during backtracking
   - Bug: Some permutations were skipped
   - Fix: Add `used[i] = False` after recursion

## Aha Moments 💡
- Permutations need ALL elements in different orders
- Unlike subsets, we need to track which elements are used
- The used array is the key difference from subset pattern

## Alternative Approaches
1. **Swap Method (In-place)**
   - More space efficient (no used array)
   - Swaps elements to generate permutations
   - Slightly harder to understand

2. **Iterative (Next Permutation)**
   - Start with sorted array
   - Generate next permutation repeatedly
   - Good for specific permutation finding

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review
- [ ] Week 1: Solve LC47 (with duplicates)
- [ ] Month 1: Revisit without notes

## Pattern Comparison
| Feature | Subsets | Permutations |
|---------|---------|--------------|
| Use all elements? | No | Yes |
| Order matters? | No | Yes |
| Tracking | Start index | Used array |
| Count | 2^n | n! |
| Base case | Implicit | len == n |

## Connection to Other Problems
- Foundation for LC47 (Permutations II) - add duplicate skipping
- Different from LC78 (Subsets) - must use all elements
- Related to LC31 (Next Permutation) - iterative generation
