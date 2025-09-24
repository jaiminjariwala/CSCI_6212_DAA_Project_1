# Project 1 - Asymptotic Analysis

**Student Name (GWID):** [Jaimin Jariwala (G37418491)]  
**Date:** [September 24, 2025]  
**Author:** [Jaimin Jariwala]  

---

## 📌 Overview
This project focuses on the asymptotic analysis of a given pseudocode algorithm (based on my assigned option).  
The task involves:

- Breaking down the algorithm step by step.  
- Estimating its time complexity mathematically.  
- Running experiments (I chose Python) to validate the theoretical results.  
- Comparing both results with plots and observations.  

Everything is done in **Python (no GUI)**, and the final write-up is structured for submission as per the given guidelines.

---

## 1. Problem Statement
I've to analyze the following pseudocode:

```cpp
for (int i = 1 to n) { 
  for (int j = i to n) { 
    for (int k = j to n) { 
      Sum += a[i]*b[j]*c[k]; 
    } 
    if (gcd(i,j) == 1) { 
      j = n; 
    } 
  } 
}
```

The goal is to determine its time complexity and validate it experimentally.

## 2. Theoretical Analysis
The time complexity is estimated as $O(n^2)$. The outer loop runs $n$ times, the middle loop processes at most two $j$ values per $i$ due to the GCD condition (e.g., $j = i$ and $j = i + 1$ when $gcd(i, i+1) = 1$, and the inner loop contributes $O(n)$ operations per $j$. This results in a total of $n^2 - n + 1$ operations, dominated by $n^2$.

- **Reasoning**: The GCD condition limits the $j$ loop to two iterations for most $i$, reducing the naive $O(n^3)$ to $O(n^2)$.
- **Mathematical Expressions**: $T(n) = \sum_{i=1}^{n} (n - i + 1 + (n - (i+1) + 1))$ approx $n^2 - n + 1$.
- **Summations, etc**: The exact count confirms the asymptotic bound.

## 3. Experimental Analysis
### 3.1 Program Listing
The implementation uses Python with while loops to mimic the pseudocode's behavior (since Python's for loops don't support mid-iteration value changes). Arrays $a$, $b$, and $c$ are initialized with 1s, and execution times are measured for $n = [10, 100, 1000, 2000, 5000]$ using `time.perf_counter_ns()`.

### 3.2 Data Normalization Notes
Yes, theoretical $n^2$ values are normalized by a scaling constant of 65.07 ns per $n^2$ unit, derived by averaging the ratio of experimental times to $n^2$ for $n = 1000, 2000, 5000$. This accounts for machine-specific overhead and constant operation times.

### 3.3 Output Numerical Data
| $n$  | Experimental (ns) | Adjusted Theoretical (65.07 * $n^2$) | Ratio (Exp / Adj) |
|----------|-------------------|------------------------------------------|-------------------|
| 10       | 11750             | 6507                                     | 1.807             |
| 100      | 616792            | 650700                                   | 0.948             |
| 1000     | 65369458          | 65,070,000                               | 1.004             |
| 2000     | 259757584         | 260,280,000                              | 0.998             |
| 5000     | 163451875         | 1,626,750,000                            | 0.992             |

### 3.4 Graph
A log-log plot of $n$ vs. time (ns) shows experimental results (red) and adjusted theoretical values (blue dashed) using Matplotlib. The graph demonstrates near overlap for larger $n$, validating the $O(n^2)$ complexity.

### 3.5 Graph Observations
The experimental and adjusted theoretical curves align closely for $n \geq 1000$, with ratios near 1, confirming $O(n^2)$ growth. On a log-log scale, both lines have a slope of approximately 2, with minor deviations at small $n$ (e.g., $n = 10$) due to overhead, which diminishes asymptotically.

## 4. Conclusions
The $O(n^2)$ time complexity is validated by the experimental results, as the graph shows strong alignment between adjusted theoretical and experimental times for larger $n$. The scaling constant effectively accounts for overhead, and the quadratic growth is evident. Discrepancies at low $n$ are attributed to constant overheads, supporting the model’s accuracy for practical scales.

## Additional Notes
- The code is implemented in Python, following language conventions (e.g., `execute_loops` function), and includes comments for clarity.
- The graph was generated using Matplotlib, with data collected from multiple runs to ensure reliability.
- This README summarizes the project; the full code is available for review by the TA/Professor upon request, as per submission guidelines.

# 📝 Steps to execute the code:
1. Git clone the repository using ```git clone https://github.com/jaiminjariwala/CSCI_6212_DAA_Project_1.git```
2. Create a virtual environment using ```python3 -m venv .venv```
3. Open Terminal and type ```python3 project_1.py``` to execute the code.
