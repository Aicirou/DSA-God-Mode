# LC39: Combination Sum

## Problem Statement
Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Link:** [LeetCode 39](https://leetcode.com/problems/combination-sum/)

## Examples

### Example 1:
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
```

### Example 2:
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3:
```
Input: candidates = [2], target = 1
Output: []
```

## Constraints
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements are **distinct**
- `1 <= target <= 40`

## Approach

### Backtracking Strategy
1. Try each candidate starting from a certain index
2. Add candidate to current combination and subtract from target
3. Can reuse the same candidate (pass same index, not i+1)
4. Base case: remaining target = 0 (found valid combination)
5. Prune: remaining target < 0 (exceeded target)

## Complexity Analysis
- **Time:** O(n^(target/min)) - Worst case depends on target and smallest candidate
- **Space:** O(target/min) - Maximum recursion depth

## Key Insights
- Similar to subsets but with reusability (pass i instead of i+1)
- Need to track remaining target instead of using all elements
- Start index prevents duplicate combinations
