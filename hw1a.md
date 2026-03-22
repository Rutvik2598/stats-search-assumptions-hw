# Exercise 1a Explanation

## Output Table

| ratio | acc | pd | pf | prec |
|---|---:|---:|---:|---:|
| 50/50 | 80 | 68 | 8 | 89 |
| 10/90 | 91 | 90 | 8 | 52 |
| 5/95 | 93 | 60 | 5 | 37 |
| 1/99 | 96 | 100 | 4 | 20 |
| 1/999 | 95 | 0 | 4 | 0 |

## Explanation

This table shows that accuracy stays high and even increases as the data becomes more imbalanced, even though the classifier itself is not actually improving. The false alarm rate (`pf`) stays close to 5%, which matches the design of the simulation, while `pd` is unstable in the most imbalanced cases because there are so few positive examples that one correct or incorrect guess changes the result drastically. Precision (`prec`) drops sharply as positives become rarer, showing that a predicted positive is less trustworthy when the minority class is very small. So accuracy is misleading here because it is inflated by the large number of negatives and hides weak performance on the rare class we care about.
