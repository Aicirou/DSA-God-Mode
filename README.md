# 🧠 DSA-God-Mode

A comprehensive repository for mastering Data Structures and Algorithms through LeetCode problems. Each problem includes detailed solutions, test cases, visual mind maps, cheat codes, and personal learning notes.

## 🎯 Repository Goals

- **Master algorithm patterns** through deliberate practice
- **Build visual understanding** with mind maps and diagrams
- **Create quick reference** cheat sheets for interview prep
- **Track learning progress** and insights over time
- **Learn by doing** with comprehensive test coverage

## 📊 Progress Tracker

| Category | Problems Solved | Status |
|----------|----------------|--------|
| Backtracking | 7 | ✅ In Progress |
| Dynamic Programming | 0 | 📝 Coming Soon |
| Graphs | 0 | 📝 Coming Soon |
| Trees | 0 | 📝 Coming Soon |
| Arrays | 0 | 📝 Coming Soon |

## 🗂️ Problems by Pattern

### Backtracking (7 Problems)

| # | Problem | Difficulty | Topics | Solution |
|---|---------|-----------|---------|----------|
| 78 | [Subsets](problems/backtracking/LC78-subsets/) | 🟡 Medium | Array, Backtracking | [✓](problems/backtracking/LC78-subsets/solution.py) |
| 46 | [Permutations](problems/backtracking/LC46-permutations/) | 🟡 Medium | Array, Backtracking | [✓](problems/backtracking/LC46-permutations/solution.py) |
| 39 | [Combination Sum](problems/backtracking/LC39-combination-sum/) | 🟡 Medium | Array, Backtracking | [✓](problems/backtracking/LC39-combination-sum/solution.py) |
| 40 | [Combination Sum II](problems/backtracking/LC40-combination-sum-ii/) | 🟡 Medium | Array, Backtracking | [✓](problems/backtracking/LC40-combination-sum-ii/solution.py) |
| 79 | [Word Search](problems/backtracking/LC79-word-search/) | 🟡 Medium | Array, Backtracking, Matrix | [✓](problems/backtracking/LC79-word-search/solution.py) |
| 90 | [Subsets II](problems/backtracking/LC90-subsets-ii/) | 🟡 Medium | Array, Backtracking | [✓](problems/backtracking/LC90-subsets-ii/solution.py) |
| 131 | [Palindrome Partitioning](problems/backtracking/LC131-palindrome-partitioning/) | 🟡 Medium | String, Backtracking | [✓](problems/backtracking/LC131-palindrome-partitioning/solution.py) |

## 📁 Repository Structure

```
DSA-God-Mode/
├── problems/                          # All problem solutions
│   ├── backtracking/
│   │   ├── LC78-subsets/
│   │   │   ├── solution.py           # Solution with detailed comments
│   │   │   ├── test_cases.py         # Comprehensive test cases
│   │   │   ├── README.md             # Problem statement & approach
│   │   │   ├── mindmap.md            # Visual problem-solving map
│   │   │   ├── cheatcode.md          # Quick reference template
│   │   │   └── notes.md              # Personal learning notes
│   │   └── ... (other problems)
│   │
│   ├── dynamic-programming/          # Coming soon
│   ├── graphs/                        # Coming soon
│   └── ...
│
├── templates/
│   └── problem-template/              # Template for new problems
│       ├── solution.py
│       ├── test_cases.py
│       ├── README.md
│       ├── mindmap.md
│       ├── cheatcode.md
│       └── notes.md
│
├── cheatsheets/
│   ├── backtracking-patterns.md       # All backtracking patterns
│   ├── time-complexity-guide.md       # Big-O analysis guide
│   └── common-pitfalls.md             # Mistakes to avoid
│
├── tools/
│   └── test_runner.py                 # Auto-run all tests
│
└── README.md                          # This file
```

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.7 or higher
python --version

# Install pytest for running tests
pip install pytest
```

### Running Tests

**Run all tests:**
```bash
python tools/test_runner.py
```

**Run tests for a specific problem:**
```bash
python tools/test_runner.py --problem LC78
python tools/test_runner.py -p subsets
```

**Run tests for a single problem directly:**
```bash
cd problems/backtracking/LC78-subsets
python test_cases.py
```

### Adding a New Problem

1. **Copy the template:**
```bash
cp -r templates/problem-template problems/[category]/LC[number]-[name]
```

2. **Fill in the files:**
   - `solution.py` - Your solution code
   - `test_cases.py` - Test cases
   - `README.md` - Problem explanation
   - `mindmap.md` - Visual approach
   - `cheatcode.md` - Pattern template
   - `notes.md` - Personal insights

3. **Run tests to verify:**
```bash
python tools/test_runner.py --problem LC[number]
```

## 📚 Learning Resources

### Pattern Guides
- [Backtracking Patterns](cheatsheets/backtracking-patterns.md) - Complete guide to backtracking
- [Time Complexity Guide](cheatsheets/time-complexity-guide.md) - Big-O analysis
- [Common Pitfalls](cheatsheets/common-pitfalls.md) - Mistakes to avoid

### Problem Organization

Each problem folder contains:
- **solution.py** - Clean, well-documented solution
- **test_cases.py** - Edge cases and validation
- **README.md** - Problem statement, examples, complexity analysis
- **mindmap.md** - Visual learning with Mermaid diagrams
- **cheatcode.md** - Reusable template/pattern
- **notes.md** - Personal learning journey

## 🎓 Study Plan

### Backtracking Pattern
**Recommended Order:**

1. **Start Here** (Foundational)
   - LC78: Subsets
   - LC46: Permutations

2. **Build Skills** (Core Patterns)
   - LC39: Combination Sum
   - LC90: Subsets II

3. **Advanced** (Variations)
   - LC40: Combination Sum II
   - LC79: Word Search
   - LC131: Palindrome Partitioning

## 💡 Tips for Success

1. **Understand the pattern** before memorizing code
2. **Draw the decision tree** for backtracking problems
3. **Test with small inputs** first
4. **Review the mind maps** to visualize the approach
5. **Keep track of insights** in notes.md
6. **Use cheat codes** as templates for similar problems
7. **Run tests frequently** to catch mistakes early

## 🔍 Key Patterns Covered

### Backtracking
- ✅ Subsets generation
- ✅ Permutations generation
- ✅ Combination with target sum
- ✅ Duplicate handling (sort + skip)
- ✅ Grid/matrix search
- ✅ String partitioning

### Coming Soon
- 🔜 Dynamic Programming
- 🔜 Graph algorithms (DFS, BFS)
- 🔜 Tree traversals
- 🔜 Two pointers
- 🔜 Sliding window
- 🔜 Binary search variations

## 🤝 Contributing

This is a personal learning repository, but suggestions for improvements are welcome! Feel free to:
- Report issues with solutions
- Suggest additional test cases
- Share insights or alternative approaches
- Recommend problems to add

## 📖 Additional Resources

- [LeetCode](https://leetcode.com/) - Problem source
- [NeetCode](https://neetcode.io/) - Curated problem lists
- [Visualgo](https://visualgo.net/) - Algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - Complexity reference

## 📝 Notes

This repository is created for **non-profit educational purposes** to enhance understanding of algorithms and problem-solving techniques. All problems are from LeetCode, and credit goes to the original problem authors.

## 📈 Stats

- **Total Problems:** 7
- **Languages:** Python 3
- **Test Coverage:** 100%
- **Last Updated:** 2024

---

**Happy Coding!** 🚀 Remember: *"The expert in anything was once a beginner."*