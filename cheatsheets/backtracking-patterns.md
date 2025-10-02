# Backtracking Patterns Cheat Sheet

## 📚 Core Patterns

### 1. Subsets Pattern
**Use Case:** Generate all possible combinations (power set)

```python
def backtrack_subsets(nums):
    result = []
    current = []
    
    def backtrack(start):
        result.append(current[:])  # Add at every node
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)  # Move to next
            current.pop()
    
    backtrack(0)
    return result
```

**Key Points:**
- No explicit base case (implicit when start >= len)
- Add to result at every recursion level
- Use `i + 1` to avoid using same element

**Problems:** LC78, LC90

---

### 2. Permutations Pattern
**Use Case:** Generate all possible arrangements

```python
def backtrack_permutations(nums):
    result = []
    current = []
    used = [False] * len(nums)
    
    def backtrack():
        if len(current) == len(nums):  # Explicit base case
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                current.append(nums[i])
                used[i] = True
                backtrack()
                current.pop()
                used[i] = False
    
    backtrack()
    return result
```

**Key Points:**
- Need explicit base case (length check)
- Track used elements (boolean array or set)
- No start index (can pick any unused element)

**Problems:** LC46, LC47

---

### 3. Combination Sum Pattern
**Use Case:** Find combinations with target sum

```python
def backtrack_combination_sum(candidates, target):
    result = []
    current = []
    
    def backtrack(start, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            # Use i for reusable, i+1 for non-reusable
            backtrack(i, remaining - candidates[i])
            current.pop()
    
    backtrack(0, target)
    return result
```

**Key Points:**
- Track remaining target
- Prune when remaining < 0
- Pass `i` for reusable elements, `i+1` for non-reusable

**Problems:** LC39 (reusable), LC40 (non-reusable)

---

### 4. Grid Search Pattern
**Use Case:** Search in 2D grids

```python
def backtrack_grid(board, target):
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(target):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] != target[index]):
            return False
        
        # Mark visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Try 4 directions
        found = (backtrack(row+1, col, index+1) or
                backtrack(row-1, col, index+1) or
                backtrack(row, col+1, index+1) or
                backtrack(row, col-1, index+1))
        
        # Restore
        board[row][col] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False
```

**Key Points:**
- In-place marking (use special character)
- Explore 4 directions (up, down, left, right)
- Must restore state after backtracking
- Try from every cell as starting point

**Problems:** LC79, LC212

---

### 5. String Partitioning Pattern
**Use Case:** Partition string with constraints

```python
def backtrack_partition(s, is_valid):
    result = []
    current = []
    
    def backtrack(start):
        if start == len(s):
            result.append(current[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_valid(substring):
                current.append(substring)
                backtrack(end)
                current.pop()
    
    backtrack(0)
    return result
```

**Key Points:**
- Try all possible end positions
- Validate substring before recursing
- Base case when start reaches string end

**Problems:** LC131, LC139

---

## 🎯 Duplicate Handling Pattern

When input has duplicates, use this universal pattern:

```python
def backtrack_with_duplicates(nums):
    result = []
    current = []
    nums.sort()  # MUST sort first
    
    def backtrack(start):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            # Skip duplicates at same level
            if i > start and nums[i] == nums[i-1]:
                continue
            
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()
    
    backtrack(0)
    return result
```

**Key Points:**
- **MUST** sort array first
- Skip condition: `i > start and nums[i] == nums[i-1]`
- Works for subsets, combinations (not permutations)

**Problems:** LC40, LC90

---

## 📊 Pattern Comparison

| Pattern | Start Index | Used Tracking | Base Case | When to Add |
|---------|------------|---------------|-----------|-------------|
| Subsets | ✅ | ❌ | Implicit | Every level |
| Permutations | ❌ | ✅ | len == n | At leaf |
| Combinations | ✅ | ❌ | len == k | At leaf |
| Comb Sum | ✅ | ❌ (track sum) | sum == target | At target |
| Grid Search | ❌ (use row/col) | ✅ (mark cell) | index == len | At match |

---

## 🔍 Decision Guide

**Need all subsets?** → Use Subsets Pattern

**Need all arrangements?** → Use Permutations Pattern

**Have target sum/count?** → Use Combination Sum Pattern

**Working with grid/matrix?** → Use Grid Search Pattern

**Partition string?** → Use String Partitioning Pattern

**Have duplicates?** → Add duplicate handling (sort + skip)

---

## ⚠️ Common Mistakes

1. ❌ **Forgetting to copy current array**
   ```python
   result.append(current)  # Wrong! Reference issue
   result.append(current[:])  # Correct! Creates copy
   ```

2. ❌ **Wrong skip condition for duplicates**
   ```python
   if i > 0 and nums[i] == nums[i-1]:  # Wrong!
   if i > start and nums[i] == nums[i-1]:  # Correct!
   ```

3. ❌ **Not restoring state**
   ```python
   used[i] = True
   backtrack()
   # Missing: used[i] = False
   ```

4. ❌ **Using start index in permutations**
   ```python
   # Permutations don't use start index
   # They use used array instead
   ```

---

## 🎓 Practice Progression

**Beginner:**
1. LC78: Subsets
2. LC46: Permutations

**Intermediate:**
3. LC39: Combination Sum
4. LC90: Subsets II (with duplicates)
5. LC40: Combination Sum II

**Advanced:**
6. LC79: Word Search
7. LC131: Palindrome Partitioning
8. LC51: N-Queens

---

## 💡 Pro Tips

1. **Always copy the current array** before adding to result
2. **Sort first** when dealing with duplicates
3. **Use in-place marking** for grid problems (saves space)
4. **Add pruning conditions** to improve performance
5. **Draw the decision tree** to understand the problem
6. **Test with small inputs** to verify logic

---

## 🔗 Related Resources

- [Backtracking Template Guide](https://leetcode.com/problems/subsets/solutions/)
- [Visual Algorithm Explanation](https://visualgo.net/en/recursion)
