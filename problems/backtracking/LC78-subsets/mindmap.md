# Mind Map: Subsets Problem

```mermaid
graph TD
    A[Subsets Problem] --> B[Identify Pattern]
    B --> C[Backtracking]
    
    C --> D[Key Components]
    D --> D1[Result Array]
    D --> D2[Current Path]
    D --> D3[Start Index]
    
    C --> E[Algorithm Steps]
    E --> E1[Add Current to Result]
    E --> E2[Loop Through Remaining]
    E --> E3[Make Choice: Add Element]
    E --> E4[Recurse with Next Index]
    E --> E5[Undo Choice: Remove Element]
    
    C --> F[Time Complexity]
    F --> F1[O n × 2^n]
    F --> F2[2^n subsets]
    F --> F3[n time to copy each]
    
    C --> G[Related Problems]
    G --> G1[LC90: Subsets II]
    G --> G2[LC46: Permutations]
    G --> G3[LC77: Combinations]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style E fill:#ffe66d
```

## Problem Solving Framework

**1. Understand**
- Generate all possible subsets
- No duplicates allowed
- Order doesn't matter

**2. Pattern Recognition**
- Backtracking problem
- Decision tree: include or exclude
- Power set generation

**3. Implementation Steps**
```
1. Initialize result and current arrays
2. Define backtrack function
3. Base case: add current to result
4. For each remaining element:
   - Include it
   - Recurse
   - Exclude it (backtrack)
```

**4. Optimization**
- Can't optimize beyond O(2^n) - must generate all subsets
- Use iterative bit manipulation for alternative approach
