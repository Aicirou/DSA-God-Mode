# LC90: Subsets II

## Problem Statement
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Link:** [LeetCode 90](https://leetcode.com/problems/subsets-ii/)

## Examples

### Example 1:
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Approach

### Backtracking with Duplicate Handling
1. **Sort** the array first to group duplicates
2. Use standard subsets backtracking
3. **Skip duplicates** at the same recursion level
4. Use condition: `if i > start and nums[i] == nums[i-1]: continue`

### Why Sorting + Skip Works
- Sorting groups duplicate values together
- Skip condition prevents choosing same value twice at same level
- Different levels can still use duplicate values

Example: `[1, 2, 2]`
- Can have `[1, 2, 2]` (uses both 2s from different levels)
- Cannot have `[2]` twice (would be same level)

## Complexity Analysis
- **Time:** O(n × 2^n) - Generate subsets and copy them
- **Space:** O(n) - Recursion depth

## Key Insights
- Same duplicate handling as Combination Sum II
- Sort first, then skip at same level
- Pattern reusable across many backtracking problems
