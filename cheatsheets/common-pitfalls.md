# Common Pitfalls in DSA

## 🐛 Backtracking Pitfalls

### 1. Reference vs Copy Issue
❌ **Wrong:**
```python
result.append(current)  # Stores reference, not copy!
```

✅ **Correct:**
```python
result.append(current[:])  # Creates a copy
# or
result.append(list(current))
result.append(current.copy())
```

**Why:** Python lists are mutable. Appending `current` stores a reference, so all results point to the same list that keeps changing.

---

### 2. Forgetting to Backtrack
❌ **Wrong:**
```python
current.append(nums[i])
used[i] = True
backtrack(i + 1)
# Missing: current.pop() and used[i] = False
```

✅ **Correct:**
```python
current.append(nums[i])
used[i] = True
backtrack(i + 1)
current.pop()  # Undo the choice
used[i] = False  # Mark as unused
```

**Why:** Backtracking means undoing choices to explore other paths.

---

### 3. Wrong Duplicate Skip Condition
❌ **Wrong:**
```python
if i > 0 and nums[i] == nums[i-1]:
    continue
```

✅ **Correct:**
```python
if i > start and nums[i] == nums[i-1]:
    continue
```

**Why:** `i > 0` skips valid choices. `i > start` only skips duplicates at the same recursion level.

**Example:** For `[1,1,2]`, we want `[1,1,2]` but not duplicate `[1,2]` results.

---

### 4. Grid Backtracking - Not Restoring State
❌ **Wrong:**
```python
board[row][col] = '#'  # Mark visited
found = backtrack(row+1, col)
# Missing: restore board[row][col]
return found
```

✅ **Correct:**
```python
temp = board[row][col]
board[row][col] = '#'  # Mark visited
found = backtrack(row+1, col)
board[row][col] = temp  # Restore!
return found
```

---

### 5. Using Start Index in Permutations
❌ **Wrong:**
```python
def permute(nums):
    def backtrack(start):  # Wrong for permutations!
        for i in range(start, len(nums)):
            # ...
```

✅ **Correct:**
```python
def permute(nums):
    used = [False] * len(nums)
    def backtrack():  # No start parameter
        for i in range(len(nums)):
            if not used[i]:
                # ...
```

**Why:** Permutations can use any unused element, not just remaining ones.

---

## 🔢 Array/List Pitfalls

### 6. Off-by-One Errors
❌ **Wrong:**
```python
for i in range(len(arr) - 1):  # Misses last element
    print(arr[i])

# String slicing
s[start:end-1]  # Often wrong!
```

✅ **Correct:**
```python
for i in range(len(arr)):  # Includes all elements
    print(arr[i])

# String slicing (end is exclusive)
s[start:end]  # Correct for substring from start to end-1
```

---

### 7. Modifying List While Iterating
❌ **Wrong:**
```python
for i in range(len(arr)):
    if arr[i] < 0:
        arr.pop(i)  # Changes indices during iteration!
```

✅ **Correct:**
```python
arr = [x for x in arr if x >= 0]  # List comprehension
# or
i = 0
while i < len(arr):
    if arr[i] < 0:
        arr.pop(i)
    else:
        i += 1
```

---

### 8. Integer Division in Python 3
❌ **Wrong:**
```python
mid = (left + right) / 2  # Returns float!
```

✅ **Correct:**
```python
mid = (left + right) // 2  # Integer division
# or
mid = left + (right - left) // 2  # Avoids overflow (in other languages)
```

---

## 🔍 Search & Sorting Pitfalls

### 9. Binary Search Boundary Errors
❌ **Wrong:**
```python
while left < right:  # May miss the answer
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid  # Infinite loop possible!
    else:
        right = mid - 1
```

✅ **Correct:**
```python
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1  # Move past mid
    else:
        right = mid - 1
return -1  # Not found
```

---

### 10. Unstable Sorting Assumptions
❌ **Wrong:**
```python
# Assuming sort preserves relative order without key
arr.sort()  # May not preserve order for equal elements in some contexts
```

✅ **Correct:**
```python
# Python's sort is stable, but be explicit if needed
arr.sort(key=lambda x: (x[0], x[1]))  # Explicit multi-key sort
```

---

## 🧮 Mathematical Pitfalls

### 11. Integer Overflow (Other Languages)
❌ **Wrong (in Java/C++):**
```java
int sum = a + b;  // May overflow
```

✅ **Correct:**
```java
long sum = (long)a + b;  // Use larger type
```

**Note:** Python handles big integers automatically, but be aware in other languages.

---

### 12. Division by Zero
❌ **Wrong:**
```python
average = sum / count  # Crashes if count is 0
```

✅ **Correct:**
```python
average = sum / count if count != 0 else 0
# or
if count == 0:
    average = 0
else:
    average = sum / count
```

---

## 🔤 String Pitfalls

### 13. String Immutability
❌ **Wrong:**
```python
s = "hello"
s[0] = 'H'  # Error! Strings are immutable
```

✅ **Correct:**
```python
s = "hello"
s = 'H' + s[1:]  # Create new string
# or use list for modifications
chars = list(s)
chars[0] = 'H'
s = ''.join(chars)
```

---

### 14. String Concatenation in Loop
❌ **Inefficient:**
```python
result = ""
for char in s:
    result += char  # O(n²) because strings are immutable
```

✅ **Efficient:**
```python
result = []
for char in s:
    result.append(char)  # O(n)
result = ''.join(result)
```

---

## 📊 Data Structure Pitfalls

### 15. Using List as Queue
❌ **Inefficient:**
```python
queue = []
queue.append(1)
queue.pop(0)  # O(n) operation!
```

✅ **Efficient:**
```python
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()  # O(1) operation
```

---

### 16. Set/Dict Ordering Assumptions
❌ **Wrong (Python < 3.7):**
```python
s = {3, 1, 2}
# Assuming specific order
```

✅ **Correct:**
```python
# Python 3.7+ dicts maintain insertion order
# But sets don't guarantee order
# Use list if order matters
ordered = [3, 1, 2]
```

---

## 🎯 Logic Pitfalls

### 17. Using `is` for Value Comparison
❌ **Wrong:**
```python
if a is 1000:  # Compares identity, not value
    print("Equal")
```

✅ **Correct:**
```python
if a == 1000:  # Compares value
    print("Equal")
```

**Note:** `is` checks if two variables point to the same object. Use `==` for value comparison.

---

### 18. Mutable Default Arguments
❌ **Wrong:**
```python
def append_to(element, arr=[]):  # Dangerous!
    arr.append(element)
    return arr

list1 = append_to(1)  # [1]
list2 = append_to(2)  # [1, 2] - Unexpected!
```

✅ **Correct:**
```python
def append_to(element, arr=None):
    if arr is None:
        arr = []
    arr.append(element)
    return arr
```

---

### 19. Shadowing Built-in Names
❌ **Wrong:**
```python
list = [1, 2, 3]  # Shadows built-in list!
# Later: new_list = list()  # Error!
```

✅ **Correct:**
```python
my_list = [1, 2, 3]  # Use descriptive name
```

Common built-ins to avoid: `list`, `dict`, `set`, `str`, `int`, `sum`, `all`, `any`, `min`, `max`

---

## 🔄 Recursion Pitfalls

### 20. Missing Base Case
❌ **Wrong:**
```python
def factorial(n):
    return n * factorial(n - 1)  # Infinite recursion!
```

✅ **Correct:**
```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)
```

---

### 21. Modifying Mutable Arguments
❌ **Wrong:**
```python
def backtrack(current):  # current is a list
    if len(current) == n:
        result.append(current)  # Wrong! Stores reference
```

✅ **Correct:**
```python
def backtrack(current):
    if len(current) == n:
        result.append(current[:])  # Copy the list
```

---

## 🎓 Testing Pitfalls

### 22. Not Testing Edge Cases
❌ **Wrong:**
```python
# Only test typical cases
assert solution([1,2,3]) == expected
```

✅ **Correct:**
```python
# Test edge cases
assert solution([]) == expected_empty
assert solution([1]) == expected_single
assert solution([1,1,1]) == expected_duplicates
assert solution([-1,-2,-3]) == expected_negative
```

---

### 23. Hardcoding Test Values
❌ **Wrong:**
```python
result = solution([1,2,3])
assert result == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Order might vary!
```

✅ **Correct:**
```python
result = solution([1,2,3])
expected = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
```

---

## 💡 Best Practices

1. ✅ **Always test edge cases:** empty input, single element, duplicates
2. ✅ **Use descriptive variable names:** `start_index` > `i`
3. ✅ **Add comments for tricky logic:** Future you will thank you
4. ✅ **Draw out examples:** Visualize before coding
5. ✅ **Use type hints:** Helps catch errors early
6. ✅ **Test incrementally:** Don't write everything then test
7. ✅ **Handle errors gracefully:** Check for None, empty, invalid input
8. ✅ **Read problem constraints:** They give hints about solution complexity

---

## 🔗 Resources

- [Python Gotchas](https://docs.python-guide.org/writing/gotchas/)
- [Common Algorithm Mistakes](https://www.geeksforgeeks.org/common-mistakes-to-be-avoided-in-competitive-programming/)
