# LC78: Subsets

## Problem Statement
Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Link:** [LeetCode 78](https://leetcode.com/problems/subsets/)

## Examples

### Example 1:
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All numbers are unique

## Approach

### Backtracking Strategy
1. Start with an empty subset
2. For each element, make a choice: include it or skip it
3. Recursively explore both branches
4. Backtrack by removing the last added element

### Decision Tree
```
                    []
           /                  \
        [1]                    []
       /    \                /    \
    [1,2]   [1]           [2]      []
    /  \    /  \         /  \     /  \
[1,2,3][1,2][1,3][1]  [2,3][2]  [3]  []
```

## Complexity Analysis
- **Time:** O(n × 2^n) - Generate 2^n subsets, each takes O(n) to copy
- **Space:** O(n) - Recursion depth

## Key Insights
- Each element has 2 choices: in or out
- Total subsets = 2^n (power set)
- Similar to: Combinations, Permutations
