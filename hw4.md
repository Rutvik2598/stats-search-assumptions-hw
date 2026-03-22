# Exercise 4

## Output Table

| treatment | wins |
|---|---:|
| ('ls', 25) | 127 |
| ('ls', 50) | 127 |
| ('ls', 100) | 127 |
| ('ls', 200) | 119 |
| ('sa', 0.7) | 114 |
| ('sa', 0.9) | 114 |
| ('sa', 0.1) | 112 |
| ('sa', 0.3) | 111 |
| ('sa', 0.5) | 111 |
| ('ls', 0) | 16 |

## Explanation

These results suggest that hyperparameters matter less than the overall search design. Several LS restart settings, especially `25`, `50`, and `100`, are all tied at the top, which means a wide range of restart counts works equally well in practice. SA is also fairly insensitive to `m`, since all five values are clustered closely together, while the big drop from `('ls', 0)` to the restarted LS settings shows that some restarts matter much more than fine tuning. So many settings are tied, which implies that spending a lot of time on precise knob tuning may not be worth the effort compared to choosing a solid algorithm structure.
