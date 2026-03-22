# Final Submission

> Note: The code snippets below show only the parts I added to fill in the starter code `TODO`s, not the full starter files.

## Exercise 1a: When Accuracy Lies

### Code Snippet

```python
for n_pos, n_neg in RATIOS:
	cf = Confuse()
	for _ in range(n_pos):
		got = "pos" if random.random() < TP_RATE else "neg"
		confuse(cf, "pos", got)
	for _ in range(n_neg):
		got = "pos" if random.random() < FP_RATE else "neg"
		confuse(cf, "neg", got)
	summary = confused(cf, summary=True)
	pos = next(c for c in confused(cf) if c.label == "pos")
	print(f"{f'{n_pos}/{n_neg}':>10} {summary.acc:>5} {pos.pd:>5}"
				f" {pos.pf:>5} {pos.prec:>5}")
```

### Output Table

| ratio | acc | pd | pf | prec |
|---|---:|---:|---:|---:|
| 50/50 | 80 | 68 | 8 | 89 |
| 10/90 | 91 | 90 | 8 | 52 |
| 5/95 | 93 | 60 | 5 | 37 |
| 1/99 | 96 | 100 | 4 | 20 |
| 1/999 | 95 | 0 | 4 | 0 |

### Explanation

This table shows that accuracy stays high and even increases as the data becomes more imbalanced, even though the classifier itself is not actually improving. The false alarm rate (`pf`) stays close to 5%, which matches the design of the simulation, while `pd` is unstable in the most imbalanced cases because there are so few positive examples that one correct or incorrect guess changes the result drastically. Precision (`prec`) drops sharply as positives become rarer, showing that a predicted positive is less trustworthy when the minority class is very small. So accuracy is misleading here because it is inflated by the large number of negatives and hides weak performance on the rare class we care about.

---

## Exercise 1b: What "Top" Means

### Code Snippet

```python
for trial in range(50):
	rxs = {i: weibull() for i in range(20)}
	pooled = [x for rx in rxs.values() for x in rx]
	sd = statistics.stdev(pooled)

	winners = top(rxs, eps=0.35 * sd)
	sizes.append(len(winners))

	means = [sum(rxs[w])/len(rxs[w]) for w in winners]
	globals().setdefault("checks", []).append(
		(not means) or (max(means) - min(means) <= 0.35 * sd))
```

### Output Table

| metric | value |
|---|---:|
| avg winners | 4.1/20 |
| min winners | 1 |
| max winners | 8 |
| winner means within eps | 40/50 trials |

### Explanation

Using `eps = 0.35 * sd` gives `top()` a practical-difference threshold, so small differences between treatments are ignored even if a statistical split is possible. In these 50 trials, the number of winners was usually small but not always just one, which means several Weibull treatments were often statistically tied with the best. A larger `eps` produces more winners because the algorithm becomes less willing to separate treatments unless their means differ by more than that threshold. The winner means were within `eps` in most trials, which shows that the selected treatments were usually close in central tendency, though not perfectly so every time.

---

## Exercise 2: Tournament on MOOT Data Sets

### Code Snippet

```python
seen = {a.__name__: [] for a in ALGOS}
for _ in range(REPEATS):
	rows = shuffle(d0.rows[:])[:SAMPLE]
	d1   = Data([d0.cols.names] + rows)
	for algo in ALGOS:
		for h, e, row in algo(d1):
			pass
		seen[algo.__name__].append(int(100*e))

winners = top(seen, eps=0.35 * sd)
for w in winners:
	wins[w] += 1
```

### Output Table

| algo | wins |
|---|---:|
| ls | 127 |
| lsRminus | 17 |
| sa | 111 |
| saRplus | 127 |

### Explanation

The results suggest that restarts help both search styles. `ls` beat `lsRminus` by a very large margin, and `saRplus` matched the best result across all files, so adding restarts clearly improved robustness. Plain `sa` also performed strongly, but it did not match restarted SA or restarted LS across all datasets. So SA is competitive and often strong, but in this tournament it does not clearly beat LS, because `ls` and `saRplus` tied for the most wins.

---

## Exercise 3: Welford's Num — Does It Matter?

### Code Snippet

```python
class WelfordNum(Num):
	def add(self, v):
		if v == "?": return v
		self.seen += 1
		self.n += 1
		delta = v - self.mu
		self.mu += delta / self.n
		delta2 = v - self.mu
		self.m2 += delta * delta2
		return v

	def spread(self):
		return math.sqrt(self.m2/(self.n-1)) if self.n > 1 else 0

	def norm(self, v):
		if v == "?": return v
		lo, hi = self._lo(), self._hi()
		return 0 if lo == hi else max(0, min(1, (v - lo)/(hi - lo)))
```

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

### Explanation

The parametric assumption changes the counts somewhat, but it does not change the overall ranking at the top. In both versions, `ls` and `saRplus` still win on all 127 datasets, so the strongest conclusion stays the same. Under Welford, plain `sa` improves from 111 to 123 wins and `lsRminus` improves from 17 to 25, which suggests the Gaussian assumption changes distances enough to help some weaker settings more often. So the assumption matters somewhat quantitatively, but not enough to overturn the main result about which algorithms are most reliable.

---

## Exercise 4: Hyperparameter Sensitivity

### Code Snippet

```python
for _ in range(REPEATS):
	rows = shuffle(d0.rows[:])[:SAMPLE]
	d1   = Data([d0.cols.names] + rows)
	for name, param in treatments:
		if name == "sa":
			for h, e, row in sa(d1, m=param):
				pass
		if name == "ls":
			for h, e, row in ls(d1, restarts=param):
				pass
		seen[(name,param)].append(int(100*e))

winners = top(seen, eps=0.35 * sd)
for w in winners:
	wins[w] += 1
```

### Output Table

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

### Explanation

These results suggest that hyperparameters matter less than the overall search design. Several LS restart settings, especially `25`, `50`, and `100`, are all tied at the top, which means a wide range of restart counts works equally well in practice. SA is also fairly insensitive to `m`, since all five values are clustered closely together, while the big drop from `('ls', 0)` to the restarted LS settings shows that some restarts matter much more than fine tuning. So many settings are tied, which implies that spending a lot of time on precise knob tuning may not be worth the effort compared to choosing a solid algorithm structure.

---

## Exercise 5: Sample Size Sensitivity

### Code Snippet

```python
for _ in range(REPEATS):
	for name, n in treatments:
		rows = shuffle(d0.rows[:])[:n]
		d1   = Data([d0.cols.names] + rows)
		algo = algo_by_name[name]
		for h, e, row in algo(d1):
			pass
		seen[(name, n)].append(int(100*e))

winners = top(seen, eps=0.35 * sd)
best_n  = min(n for (_,n) in winners)
winners = {w for w in winners if w[1]==best_n}
for w in winners:
	wins[w] += 1
```

### Output Table

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

### Explanation

These results suggest that winners often stabilize surprisingly early, since the 30-row settings dominate after applying the tie-break that prefers smaller sample sizes. In other words, when 30 rows and 100 or 200 rows are statistically tied, the cheaper 30-row treatment gets the win, and that happens often here. Larger samples still win sometimes, so more data can help on some datasets, but less data clearly wins often enough to matter. This implies that for expensive-to-label software engineering tasks, collecting a modest amount of data may already be enough to reach the same conclusions as much larger samples.
