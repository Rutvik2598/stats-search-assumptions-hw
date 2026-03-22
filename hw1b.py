#!/usr/bin/env python3 -B
"""hw1b.py: top() with pragmatic eps"""
import random, math, statistics
from stats import top

random.seed(1)

def weibull(n=20):
  shape = random.uniform(0.5, 3)
  scale = random.uniform(1, 4)
  return [min(10,
    scale*(-math.log(random.random()))**(1/shape)*2.5)
    for _ in range(n)]

sizes = []
for trial in range(50):
  rxs = {i: weibull() for i in range(20)}

  # baseline = pool all observations
  pooled = [x for rx in rxs.values() for x in rx]  # TODO: flatten all rxs values
  sd     = statistics.stdev(pooled)   # TODO: statistics.stdev(pooled)

  winners = top(rxs, eps=0.35 * sd)
  sizes.append(len(winners))

  # TODO: check that all winner means are
  #       within eps of each other
  means = [sum(rxs[w])/len(rxs[w]) for w in winners]
  globals().setdefault("checks", []).append(
    (not means) or (max(means) - min(means) <= 0.35 * sd))

print(f"avg winners: {sum(sizes)/len(sizes):.1f}/20")
print(f"min winners: {min(sizes)}")
print(f"max winners: {max(sizes)}")
# TODO: does larger eps -> more or fewer winners? why?
print(f"winner means within eps: {sum(globals()['checks'])}/{len(globals()['checks'])} trials")
print("larger eps -> more winners, since bigger practical-difference thresholds make top() less willing to split treatments apart.")
