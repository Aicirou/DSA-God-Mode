# Personal Notes: LC79 Word Search

## First Attempt
- **Date:** 2024-01-19
- **Time Taken:** 45 minutes
- **Result:** Solved after debugging ✓

## Challenges Faced
1. Forgot to restore board state
   - Bug: Modified board permanently
   - Fix: Save temp value and restore after recursion

2. Checked match after marking visited
   - Bug: Marked wrong cells as visited
   - Fix: Check match before marking

## Aha Moments 💡
- In-place marking saves space
- Must try from every cell, not just first match
- The OR in 4 directions means we succeed on first found path

## Pattern: Grid Backtracking
This pattern applies to many grid problems:
1. Mark cell as visited
2. Explore neighbors
3. Unmark cell (backtrack)

## Review Schedule
- [x] Day 1: Solved
- [ ] Day 3: Review
- [ ] Week 1: Solve LC212
