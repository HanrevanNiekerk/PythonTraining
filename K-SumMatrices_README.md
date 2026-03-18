AnchorSum: Submatrix Counter
A highly efficient Python solution for counting submatrices that originate from the top-left corner (0, 0) and
maintain a total sum less than or equal to a threshold k.

📌 Overview
This project implements a 2D prefix sum algorithm to solve the "Count Submatrices with Top-Left Element" problem. 
Instead of re-calculating the sum for every possible submatrix—which would be computationally expensive—this solution uses 
In-place Dynamic Programming to achieve optimal performance.

🚀 The Logic
The algorithm follows these core steps:
Prefix Sum Construction: 
It transforms the input grid so that each cell grid[i][j] stores the total sum of the rectangle from (0,0) to (i,j).

Inclusion-Exclusion Principle: To avoid double-counting overlapping areas, it uses the formula:
Sum(i, j) = \text{val} + Sum(i-1, j) + Sum(i, j-1) - Sum(i-1, j-1) 
Threshold Validation: During the single pass, it checks if the current prefix sum is $\le k$ and increments the counter.

🛠️ Usage
from solution import Solution

# Initialize the grid and threshold
grid = [[7, 6, 3], [6, 4, 1]]
k = 18

sol = Solution()
result = sol.countSubmatrices(grid, k)

print(f"Number of valid submatrices: {result}")

📊 Complexity Analysis
Time Complexity: O(M \times N), where M is the number of rows and $N$ is the number of columns. 
We traverse the grid exactly once.
Space Complexity: O(1) (excluding the input storage), as the prefix sums are calculated in-place, 
modifying the original grid to save memory.
