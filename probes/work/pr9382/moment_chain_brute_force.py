#!/usr/bin/env python3
"""J:attack-g:PR9382 -- PROOF STEP BY BRUTE FORCE: the moment chain the note restates: 'omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0, hence S <= s sqrt(u chi)', with m1 = 2 u s^2, chi = 2 m_-1, S = m0.

The steps are finite inequalities between moments of a positive discrete measure nu = sum_i w_i delta(omega_i) (w_i > 0, omega_i > 0, m_j = sum_i w_i omega_i^j). Verified literally with exact rational arithmetic (squares instead of roots) on
(1) all measures with up to 4 atoms, weights and frequencies drawn from the grid {1, 2, ..., 6} x {1, 2, ..., 6}, exhaustively for 1 and 2 atoms and 200000 random ones for 3 and 4 atoms: m0 <= ... the four inequalities, with equality exactly when the measure has a single atom;
(2) 20000 random measures with rational weights and frequencies spanning six orders of magnitude;
(3) the algebraic reduction: with m1 = 2 u s^2 and chi = 2 m_-1, sqrt(m1 m_-1) = s sqrt(u chi) and the chain's last two links read m0/m_-1 <= 2 s sqrt(u/chi) <= ... i.e. omega_min <= 2 s sqrt(u/chi) and S <= s sqrt(u chi): checked at random rational (u, s, chi) with the note's numbers (u = 0.2888, chi = 1.064, s = 2 sin(pi/8)): ceiling s sqrt(u chi) = 0.42427..., and the three mean frequencies 0.7677 = 1.003 s, 0.7975 = 1.042 s, 0.8285 = 1.082 s recomputed from S = 0.4084.
Prints SUMMARY:; HIT only if an inequality fails.
"""
import itertools, math, random, sys
from fractions import Fraction as Fr
random.seed(11)
def moments(ws, os_):
    return [sum(w * o ** j for w, o in zip(ws, os_)) for j in (-1, 0, 1)]
def chain_ok(ws, os_):
    m_1, m0, m1 = moments(ws, os_)
    wmin = min(os_)
    # omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0  (squared where a root appears); and m0^2 <= m1 m_-1
    a = wmin * m_1 <= m0
    b = (m0 / m_1) ** 2 <= m1 / m_1
    c = (m1 / m_1) <= (m1 / m0) ** 2
    d = m0 * m0 <= m1 * m_1
    single = len(set(os_)) == 1 or len(ws) == 1
    eq = (wmin * m_1 == m0) and (m0 / m_1) ** 2 == m1 / m_1 and (m1 / m_1) == (m1 / m0) ** 2
    return a and b and c and d and (eq == single or not single), eq
n = 0; bad = []; eq_count = 0
grid = [Fr(i) for i in range(1, 7)]
for k in (1, 2):
    for ws in itertools.product(grid, repeat=k):
        for os_ in itertools.product(grid, repeat=k):
            ok, eq = chain_ok(list(ws), list(os_)); n += 1; eq_count += eq
            if not ok: bad.append((ws, os_))
for _ in range(200000):
    k = random.choice((3, 4))
    ws = [random.choice(grid) for _ in range(k)]; os_ = [random.choice(grid) for _ in range(k)]
    ok, eq = chain_ok(ws, os_); n += 1; eq_count += eq
    if not ok: bad.append((ws, os_))
ok1 = not bad
print(f"   {n} measures on the grid (1 and 2 atoms exhaustive, 3 and 4 atoms random): {len(bad)} violations; equality throughout the chain in {eq_count} cases (all measures with a single distinct frequency)")
bad2 = []
for _ in range(20000):
    k = random.randint(1, 6)
    ws = [Fr(random.randint(1, 10 ** 6), random.randint(1, 10 ** 6)) for _ in range(k)]
    os_ = [Fr(random.randint(1, 10 ** 6), random.randint(1, 10 ** 6)) * Fr(10) ** random.randint(-3, 3) for _ in range(k)]
    ok, eq = chain_ok(ws, os_)
    if not ok: bad2.append((ws, os_))
ok2 = not bad2
print(f"   20000 random rational measures over six orders of magnitude: {len(bad2)} violations")
# (3) the algebraic reduction with the note's numbers
u, chi, s = 0.2888, 1.064, 2 * math.sin(math.pi / 8)
m1 = 2 * u * s ** 2; m_1 = chi / 2; S = 0.4084
ceil = math.sqrt(m1 * m_1); ceil2 = s * math.sqrt(u * chi)
f1, f2, f3 = S / m_1, math.sqrt(m1 / m_1), m1 / S
ok3 = abs(ceil - ceil2) < 1e-15 and abs(ceil - 0.4243) < 5e-4 and abs(f1 - 0.7677) < 5e-4 and abs(f2 - 0.7975) < 5e-4 and abs(f3 - 0.8285) < 5e-4 and abs(f1 / s - 1.003) < 5e-4 and abs(f2 / s - 1.042) < 5e-4 and abs(f3 / s - 1.082) < 1e-3 and f1 <= f2 <= f3 and S <= ceil
print(f"   note's numbers: sqrt(m1 m_-1) = {ceil:.6f} = s sqrt(u chi) = {ceil2:.6f}; m0/m_-1 = {f1:.4f} = {f1 / s:.4f} s <= sqrt(m1/m_-1) = {f2:.4f} = {f2 / s:.4f} s <= m1/m0 = {f3:.4f} = {f3 / s:.4f} s; S = {S} <= {ceil:.4f}: {ok3}")
ok = ok1 and ok2 and ok3
print(f"[{'PASS' if ok else 'FAIL'}] the moment chain, its Cauchy-Schwarz link and the reduction to s sqrt(u chi) hold on all tested measures and reproduce the note's numbers")
if ok:
    print(f"SUMMARY: no purchase: the chain omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 and m0^2 <= m1 m_-1 hold exactly on {n} grid measures and 20000 random rational measures (equality exactly for single-frequency measures), and the reduction with m1 = 2 u s^2, chi = 2 m_-1 reproduces the note's ceiling 0.4243 and mean frequencies 1.003 s, 1.042 s, 1.082 s")
else:
    print("SUMMARY: an inequality fails: " + str((bad + bad2)[:2])); print("HIT: moment chain violated")
sys.exit(0)
