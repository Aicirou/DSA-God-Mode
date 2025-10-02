# LC40: Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Link:** [LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)

## Examples

### Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

### Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Constraints
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Approach

### Backtracking with Duplicate Handling
1. **Sort** the candidates array first
2. Use backtracking to explore combinations
3. **Skip duplicates** at the same recursion level
4. Pass `i+1` to prevent reusing same element

### Key Technique: Skip Duplicates
```python
if i > start and candidates[i] == candidates[i-1]:
    continue
```
This skips duplicate values at the same level while allowing duplicates across different levels.

## Complexity Analysis
- **Time:** O(2^n) - Worst case explores all subsets
- **Space:** O(n) - Recursion depth

## Key Insights
- Must sort first to handle duplicates
- Skip duplicates at same level, not across levels
- Different from LC39: each element used at most once
