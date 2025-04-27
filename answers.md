# CMPS 2200 Recitation 5
## Answers

**Name:** Roberto Junqueira
**Name:** Mauricio Uribe


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

n | qsort-fixed-pivot | qsort-random-pivot | tim-sort
100 | 0.104 | 0.105 | 0.012
200 | 0.148 | 0.201 | 0.022
500 | 0.434 | 0.591 | 0.060
1000 | 0.977 | 1.214 | 0.134
2000 | 22.148 | 2.760 | 0.299
5000 | 5.911 | 7.011 | 0.916
10000 | 15.485 | 19.107 | 2.177
20000 | 48.543 | 33.717 | 4.523
50000 | 91.633 | 101.616 | 13.030
100000 | 201.413 | 286.680 | 32.229

The average-case complexity for quicksort is O(n log n), while the worst-case complexity is O(n^2). Selection sort, however, has a consistent complexity of O(n^2) for both average and worst-case scenarios.

- **1c.**

The built-in sorting method (Timsort) consistently performed better than both of the quicksort variations in this recitation. The results clearly show how Timsort was faster across all input sizes that were tested, performing significantly better than both fixed pivot and random pivot quicksort. This was especially true as the input lists began to grow larger.
