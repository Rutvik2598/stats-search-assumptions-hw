# Exercise 2

## Output Table

| algo | wins |
|---|---:|
| ls | 127 |
| lsRminus | 17 |
| sa | 111 |
| saRplus | 127 |

## Explanation

The results suggest that restarts help both search styles. `ls` beat `lsRminus` by a very large margin, and `saRplus` matched the best result across all files, so adding restarts clearly improved robustness. Plain `sa` also performed strongly, but it did not match restarted SA or restarted LS across all datasets. So SA is competitive and often strong, but in this tournament it does not clearly beat LS, because `ls` and `saRplus` tied for the most wins.
