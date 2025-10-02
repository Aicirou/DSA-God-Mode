# LC46: Permutations

## Problem Statement
Given an array `nums` of **distinct** integers, return all the possible permutations. You can return the answer in **any order**.

**Link:** [LeetCode 46](https://leetcode.com/problems/permutations/)

## Examples

### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:
```
Input: nums = [1]
Output: [[1]]
```

## Constraints
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All integers are **unique**

## Approach

### Backtracking Strategy
1. Use a boolean array to track which elements are used
2. Build permutations one element at a time
3. When permutation is complete (length = n), add to result
4. Backtrack by unmarking the element and removing it

### Decision Tree Example (nums = [1,2,3])
```
                    []
          /         |         \
        [1]        [2]        [3]
       /  \       /   \       /  \
    [1,2][1,3] [2,1][2,3] [3,1][3,2]
     |     |     |     |     |     |
  [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

## Complexity Analysis
- **Time:** O(n! × n) - Generate n! permutations, each takes O(n) to copy
- **Space:** O(n) - Recursion depth and used array

## Key Insights
- Each position can be filled with any unused element
- Total permutations = n!
- Different from subsets: must use all elements
