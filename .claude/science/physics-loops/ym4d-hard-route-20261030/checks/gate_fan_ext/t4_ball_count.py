#!/usr/bin/env python3
"""T4, consumer note only: how many bricks of (3.1) can a ball or cube of radius b/8, b/16 meet in d = 4?
Lemma J of quiet-boundary-rarity.md reads at most d + 1 = 5 in a ball of radius t_0/8.
Lower bounds by random search; a value above 5 is a counterexample, a value of 5 proves nothing."""
import math, random


def brick(x, b=1.0):
    """indices m of the brick of (3.1) containing x."""
    m4 = math.floor(x[3] / b)
    m3 = math.floor(x[2] / b - m4 / 2)
    m2 = math.floor(x[1] / b - m3 / 2 - m4 / 4)
    m1 = math.floor(x[0] / b - m2 / 2 - m3 / 4 - m4 / 8)
    return (m1, m2, m3, m4)


def count(c, r, ball, n=4000):
    s = set()
    for _ in range(n):
        v = [random.uniform(-r, r) for _ in range(4)]
        if ball:
            nv = math.sqrt(sum(t * t for t in v))
            if nv >= r:
                f = (r * 0.999) / nv
                v = [t * f for t in v]
        s.add(brick([a + t for a, t in zip(c, v)]))
    return len(s)


random.seed(11)
for r, name in ((1 / 8, "b/8"), (1 / 16, "b/16"), (1 / 20, "b/20"), (1 / 64, "b/64")):
    for ball in (True, False):
        best = 0
        for _ in range(4000):
            c = [random.randrange(0, 64) / 16 + random.uniform(-r / 4, r / 4) for _ in range(4)]
            best = max(best, count(c, r, ball, 600))
        print("radius", name, "ball" if ball else "cube", "max bricks found", best, flush=True)
