# Exercise 1b

## Output

| metric | value |
|---|---:|
| avg winners | 4.1/20 |
| min winners | 1 |
| max winners | 8 |
| winner means within eps | 40/50 trials |

## Explanation

Using `eps = 0.35 * sd` gives `top()` a practical-difference threshold, so small differences between treatments are ignored even if a statistical split is possible. In these 50 trials, the number of winners was usually small but not always just one, which means several Weibull treatments were often statistically tied with the best. A larger `eps` produces more winners because the algorithm becomes less willing to separate treatments unless their means differ by more than that threshold. The winner means were within `eps` in most trials, which shows that the selected treatments were usually close in central tendency, though not perfectly so every time.
