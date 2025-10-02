# Mind Map: Permutations Problem

```mermaid
graph TD
    A[Permutations Problem] --> B[Pattern Type]
    B --> C[Backtracking]
    
    C --> D[Key Components]
    D --> D1[Result Array]
    D --> D2[Current Path]
    D --> D3[Used Array/Set]
    
    C --> E[Algorithm Steps]
    E --> E1[Base Case: len = n]
    E --> E2[Loop All Elements]
    E --> E3[Skip if Used]
    E --> E4[Mark Used & Add]
    E --> E5[Recurse]
    E --> E6[Mark Unused & Remove]
    
    C --> F[Time Complexity]
    F --> F1[O n! × n]
    F --> F2[n! permutations]
    F --> F3[n time to copy each]
    
    C --> G[Related Problems]
    G --> G1[LC47: Permutations II]
    G --> G2[LC78: Subsets]
    G --> G3[LC77: Combinations]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style E fill:#ffe66d
```

## Problem Solving Framework

**1. Understand**
- Generate all arrangements of elements
- Use each element exactly once
- Order matters (different from subsets)

**2. Pattern Recognition**
- Backtracking with state tracking
- Need to track used elements
- Complete path = full permutation

**3. Implementation Steps**
```
1. Initialize result, current, and used tracking
2. Define backtrack function
3. Base case: when current length equals input length
4. For each element:
   - Skip if already used
   - Mark as used and add to current
   - Recurse
   - Mark as unused and remove from current
```

**4. Optimization**
- Use set for used elements for O(1) lookup
- Alternative: swap elements in-place
