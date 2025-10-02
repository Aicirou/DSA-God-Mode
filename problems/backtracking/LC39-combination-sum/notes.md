# Personal Notes: LC39 Combination Sum

## First Attempt
- **Date:** 2024-01-17
- **Time Taken:** 30 minutes
- **Result:** Solved ✓

## Challenges Faced
1. Initially passed i+1 instead of i
   - Bug: Couldn't reuse elements
   - Fix: Pass i to allow reusing same element

2. Didn't add pruning condition
   - Performance: Explored unnecessary branches
   - Fix: Return early when remaining < 0

## Aha Moments 💡
- The key difference is passing `i` not `i+1`
- Pruning is important for performance
- Start index still prevents duplicates

## Pattern Variations
| Problem | Reuse? | Pass to recursion |
|---------|--------|-------------------|
| Combination Sum | Yes | i |
| Combination Sum II | No | i+1 |
| Subsets | N/A | i+1 |

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review
- [ ] Week 1: Solve LC40
- [ ] Month 1: Revisit
