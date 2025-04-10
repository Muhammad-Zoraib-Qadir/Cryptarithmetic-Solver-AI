# 🧩 Cryptarithmetic Puzzle Solver  
*AI assignment implementing BFS/DFS with heuristics to solve word math puzzles like SEND+MORE=MONEY*  

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  
[![Report PDF](https://img.shields.io/badge/Report-PDF-red)](Report.pdf)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  

## 📖 Project Overview  
This repository contains:  
- **BFS/DFS implementations** with domain-specific heuristics  
- **Constraint validation** (no leading zeros, unique digit mapping)  
- **Search space pruning** strategies  
- Detailed technical report (`Report.pdf`)  
- Example solutions for classic puzzles  

## 🔑 Key Features  
| Component         | Implementation Details              |  
|-------------------|-------------------------------------|  
| **State Space**   | Letter-digit mappings               |  
| **BFS Heuristic** | Prioritizes most-constrained letters|  
| **DFS Heuristic** | Letter frequency-based exploration  |  
| **Validation**    | `validate_solution()` & `validate_partial_solution()` |  

## 📂 Repository Structure  
Cryptarithmetic-Solver-AI/    
│   ├── solver.py   # Beadth_First Depth-First Search implementation     
├── Report.pdf           # Detailed analysis document  
└── Readme.md
## 📊 Report Highlights  
- **Search Tree Analysis**: Comparison of BFS vs DFS performance  
- **Heuristic Design**: Frequency-based vs constraint-based approaches  
- **Pruning Strategies**: Early termination of invalid branches  
- **Output Samples**:  
  ![Solution Output](output_example.png) *Sample BFS solution mapping*  

## 🧠 Algorithms Overview  

### BFS Approach  
- **Level-order exploration**: Uses a queue to traverse states layer by layer.  
- **Early pruning**: Discards invalid branches immediately using `validate_partial_solution()`.  
- **Optimality**: Guaranteed to find the shortest path to a solution.  

### DFS Approach  
- **Depth-first assignment**: Prioritizes full branch exploration before backtracking.  
- **Frequency heuristic**: Assigns digits to most frequent letters first.  
- **Speed advantage**: Faster for puzzles with constrained search spaces.  
