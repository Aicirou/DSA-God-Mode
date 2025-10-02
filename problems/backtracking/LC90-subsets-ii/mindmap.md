# Mind Map: Subsets II Problem

```mermaid
graph TD
    A[Subsets II] --> B[Challenge]
    B --> B1[Has Duplicates]
    B --> B2[No Duplicate Subsets]
    
    A --> C[Solution]
    C --> C1[Sort First]
    C --> C2[Standard Backtracking]
    C --> C3[Skip Same-Level Dups]
    
    C2 --> D[Algorithm]
    D --> D1[Add Current to Result]
    D --> D2[Loop from start]
    D --> D3[Skip if i > start AND nums i = nums i-1]
    D --> D4[Add to current]
    D --> D5[Recurse with i+1]
    D --> D6[Remove from current]
    
    A --> E[Comparison]
    E --> E1[LC78: No duplicates in input]
    E --> E2[LC90: Has duplicates in input]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style D fill:#ffe66d
```

## Duplicate Handling Example
```
nums = [1, 2, 2]

Level 0: []
Level 1: [1], [2]  (skip second 2 at same level)
Level 2: [1,2], [2,2]  (both 2s from different levels)
Level 3: [1,2,2]
```
