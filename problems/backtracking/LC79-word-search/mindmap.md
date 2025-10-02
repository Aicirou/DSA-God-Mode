# Mind Map: Word Search Problem

```mermaid
graph TD
    A[Word Search] --> B[Pattern Type]
    B --> C[Backtracking + DFS on Grid]
    
    C --> D[Key Components]
    D --> D1[Board Grid]
    D --> D2[Word String]
    D --> D3[Current Index]
    D --> D4[Visited Marker]
    
    C --> E[Algorithm Steps]
    E --> E1[Try Each Cell as Start]
    E --> E2[Check Bounds & Match]
    E --> E3[Mark Cell Visited]
    E --> E4[Try 4 Directions]
    E --> E5[Unmark Cell Backtrack]
    
    C --> F[Optimizations]
    F --> F1[In-place Marking]
    F --> F2[Early Termination]
    F --> F3[Boundary Checks First]
    
    style A fill:#ff6b6b
    style C fill:#4ecdc4
    style E fill:#ffe66d
```

## 4 Direction Exploration
```
     (row-1, col)
          ↑
(row, col-1) ← (row, col) → (row, col+1)
          ↓
     (row+1, col)
```

## State Management
- **Mark visited:** `board[row][col] = '#'`
- **Restore:** `board[row][col] = temp`
- **Purpose:** Prevent using same cell twice
