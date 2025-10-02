# Mind Map: Combination Sum Problem

```mermaid
graph TD
    A[Combination Sum] --> B[Pattern Type]
    B --> C[Backtracking with Reusability]
    
    C --> D[Key Components]
    D --> D1[Result Array]
    D --> D2[Current Path]
    D --> D3[Start Index]
    D --> D4[Remaining Target]
    
    C --> E[Algorithm Steps]
    E --> E1[Base: remaining = 0]
    E --> E2[Prune: remaining < 0]
    E --> E3[Loop from start]
    E --> E4[Add to current]
    E --> E5[Recurse with same i]
    E --> E6[Remove from current]
    
    C --> F[Key Difference]
    F --> F1[Can reuse elements]
    F --> F2[Pass i not i+1]
    F --> F3[Track remaining sum]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style E fill:#ffe66d
```

## Problem Solving Framework

**1. Understand**
- Find combinations that sum to target
- Can reuse same element multiple times
- No duplicate combinations

**2. Pattern Recognition**
- Backtracking with sum constraint
- Similar to subsets but with reusability
- Need pruning for efficiency

**3. Key Differences from Similar Problems**
- **vs Subsets:** Has target sum constraint
- **vs Combinations:** Can reuse elements
- **vs Combination Sum II:** This allows reuse
