# Exercise 5

## Output Table

| treatment | wins |
|---|---:|
| ('ls', 30) | 52 |
| ('saRplus', 30) | 50 |
| ('sa', 30) | 48 |
| ('saRplus', 200) | 23 |
| ('ls', 200) | 21 |
| ('sa', 200) | 17 |
| ('saRplus', 100) | 17 |
| ('ls', 100) | 16 |
| ('sa', 100) | 14 |
| ('lsRminus', 30) | 12 |
| ('sa', 50) | 4 |
| ('ls', 50) | 3 |
| ('saRplus', 50) | 3 |
| ('lsRminus', 50) | 0 |
| ('lsRminus', 100) | 0 |
| ('lsRminus', 200) | 0 |

## Explanation

These results suggest that winners often stabilize surprisingly early, since the 30-row settings dominate after applying the tie-break that prefers smaller sample sizes. In other words, when 30 rows and 100 or 200 rows are statistically tied, the cheaper 30-row treatment gets the win, and that happens often here. Larger samples still win sometimes, so more data can help on some datasets, but less data clearly wins often enough to matter. This implies that for expensive-to-label software engineering tasks, collecting a modest amount of data may already be enough to reach the same conclusions as much larger samples.
