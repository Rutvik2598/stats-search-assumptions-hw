# Exercise 3

## Output Tables

### Reservoir (non-parametric)

| algo | wins |
|---|---:|
| ls | 127 |
| lsRminus | 17 |
| sa | 111 |
| saRplus | 127 |

### Welford (Gaussian)

| algo | wins |
|---|---:|
| ls | 127 |
| lsRminus | 25 |
| sa | 123 |
| saRplus | 127 |

## Comparison

The parametric assumption changes the counts somewhat, but it does not change the overall ranking at the top. In both versions, `ls` and `saRplus` still win on all 127 datasets, so the strongest conclusion stays the same. Under Welford, plain `sa` improves from 111 to 123 wins and `lsRminus` improves from 17 to 25, which suggests the Gaussian assumption changes distances enough to help some weaker settings more often. So the assumption matters somewhat quantitatively, but not enough to overturn the main result about which algorithms are most reliable.
