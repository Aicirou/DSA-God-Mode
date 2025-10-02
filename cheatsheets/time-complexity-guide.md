# Time Complexity Guide

## 📊 Common Time Complexities

### Visual Comparison
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!)

For n = 10:
O(1)      = 1
O(log n)  = ~3
O(n)      = 10
O(n log n)= ~30
O(n²)     = 100
O(2^n)    = 1,024
O(n!)     = 3,628,800
```

---

## 🎯 Backtracking Complexities

### Subsets
- **Time:** O(n × 2^n)
- **Why:** Generate 2^n subsets, O(n) to copy each
- **Problems:** LC78, LC90

### Permutations
- **Time:** O(n! × n) or O(n × n!)
- **Why:** Generate n! permutations, O(n) to copy each
- **Problems:** LC46, LC47

### Combinations (size k)
- **Time:** O(k × C(n,k)) where C(n,k) = n!/(k!(n-k)!)
- **Why:** Generate C(n,k) combinations, O(k) to copy each
- **Problems:** LC77

### Combination Sum
- **Time:** O(n^(target/min))
- **Why:** At each level, n choices; depth is target/smallest_candidate
- **Problems:** LC39, LC40

### Word Search
- **Time:** O(m × n × 4^L)
- **Why:** Try from m×n cells, explore 4 directions for L characters
- **Problems:** LC79

### Palindrome Partitioning
- **Time:** O(n × 2^n)
- **Why:** 2^n possible partitions, O(n) for palindrome check
- **Problems:** LC131

---

## 📈 Analysis Techniques

### 1. Count the Recursive Calls

**Example: Fibonacci**
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
- Tree has 2^n nodes → O(2^n)

### 2. Analyze Branch Factor & Depth

**Formula:** O(b^d)
- b = branching factor (choices per level)
- d = depth of recursion tree

**Example: Subsets**
- Each element: 2 choices (include/exclude)
- Depth: n levels
- Time: O(2^n)

### 3. Consider Work Per Node

**Formula:** O(nodes × work_per_node)

**Example: Permutations**
- Nodes: n! permutations
- Work: O(n) to copy each
- Total: O(n! × n)

---

## 🔄 Common Patterns

### Array/String Iteration
```python
for i in range(n):
    # O(1) work
```
**Time:** O(n)

### Nested Loops
```python
for i in range(n):
    for j in range(n):
        # O(1) work
```
**Time:** O(n²)

### Divide and Conquer
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)  # O(n)
```
**Time:** O(n log n)
- Divides into 2 halves: log n levels
- Merges: O(n) per level

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```
**Time:** O(log n)
- Halves search space each iteration

---

## 🎲 Space Complexity

### Recursion Stack
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```
**Space:** O(n) - recursion depth

### Additional Data Structures
```python
def subsets(nums):
    result = []  # O(2^n × n) space for all subsets
    current = []  # O(n) space for current path
    # backtracking...
```
**Space:** O(2^n × n) for result, O(n) for recursion

### In-place Algorithms
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```
**Space:** O(1) - constant extra space

---

## 📝 Quick Reference Table

| Algorithm | Time | Space | Example |
|-----------|------|-------|---------|
| Linear Search | O(n) | O(1) | Find in array |
| Binary Search | O(log n) | O(1) | Find in sorted array |
| Bubble Sort | O(n²) | O(1) | Simple sorting |
| Merge Sort | O(n log n) | O(n) | Efficient sorting |
| Quick Sort | O(n log n) avg | O(log n) | Efficient sorting |
| DFS/BFS | O(V + E) | O(V) | Graph traversal |
| Subsets | O(n × 2^n) | O(n) | Backtracking |
| Permutations | O(n! × n) | O(n) | Backtracking |
| Dynamic Programming | O(n²) typical | O(n) or O(n²) | Optimization |

---

## 🎯 Optimization Strategies

### 1. Pruning (Backtracking)
Skip branches that can't lead to valid solutions
```python
if remaining < 0:
    return  # Prune early
```

### 2. Memoization
Cache results to avoid recomputation
```python
memo = {}
if key in memo:
    return memo[key]
# ... compute result ...
memo[key] = result
```

### 3. Early Termination
Stop when answer is found
```python
if found:
    return True  # Don't explore further
```

### 4. Sorting
Can enable better pruning
```python
nums.sort()
if nums[i] > remaining:
    break  # Rest will be larger too
```

---

## 💡 Analysis Tips

1. **Count loops:** Each nested loop multiplies complexity
2. **Identify recursion pattern:** Draw recursion tree
3. **Consider input size:** What happens as n grows?
4. **Count operations:** How many times is each line executed?
5. **Worst case vs average:** Usually analyze worst case

---

## 🚨 When to Worry

- **O(n!) or O(2^n):** Only works for small n (< 15-20)
- **O(n³) or higher:** May be too slow for n > 1000
- **O(n²):** Be careful with n > 10,000
- **O(n log n):** Usually fine up to n = 10^6
- **O(n) or better:** Can handle large inputs

---

## 🔍 Practice Problems by Complexity

**O(n):**
- Two Sum (with hash map)
- Maximum Subarray

**O(n log n):**
- Merge Sort
- Binary Search variations

**O(n²):**
- Bubble Sort
- Many DP problems

**O(2^n):**
- Subsets (LC78)
- Combination Sum (LC39)

**O(n!):**
- Permutations (LC46)
- N-Queens (LC51)

---

## 📚 Resources

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Master Theorem](https://en.wikipedia.org/wiki/Master_theorem)
- [Time Complexity Analysis](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
