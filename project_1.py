import math
import time
import matplotlib.pyplot as plt     # for plotting a graph

# Function to execute the nested loops as per the pseudo code
def execute_loops(n):
    a = [1] * (n + 1)   # create lists of size n+1 initialized to 1
    b = [1] * (n + 1)
    c = [1] * (n + 1)
    Sum = 0
    i = 1
    while i <= n:   # using while loops rather than for to match pseudo code
        j = i
        while j <= n:
            for k in range(j, n + 1):
                Sum += a[i] * b[j] * c[k]
            if math.gcd(i, j) == 1:
                j = n
            j += 1
        i += 1
    return Sum

# Measure execution time for different values of n
ns = [10, 100, 1000, 2000, 5000]
experimental_times = []
for n in ns:
    start = time.perf_counter_ns()  # time in int nanoseconds
    _ = execute_loops(n)
    end = time.perf_counter_ns()
    elapsed_ns = end - start
    experimental_times.append(elapsed_ns)
    print(f"n={n}, elapsed_ns={elapsed_ns}")

# Plotting the graph...
# Theoretical values (n^2) and adjusted theoretical values
theoretical_n2 = [n * n for n in ns]
scaling_constant = 65.07  # Derived from average ratio for n=1000, 2000, 5000
adjusted_theoretical = [scaling_constant * n * n for n in ns]

# Plotting the figure...
plt.figure(figsize=(10, 6))
plt.loglog(ns, experimental_times, 'r-', label='Experimental Results', linewidth=2) # red continouous line
plt.loglog(ns, adjusted_theoretical, 'b--', label='Adjusted Theoretical', linewidth=2)  # blue dashed line

# Adding labels and title
plt.xlabel('n (log scale)')
plt.ylabel('Time (ns) (log scale)')
plt.title('Experimental vs Adjusted Theoretical Time')
plt.legend()
plt.grid(True, which="both", ls="--")   # added grid for better readability

# Display the plot
plt.show()