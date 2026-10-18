#!/usr/bin/env python3
"""Scope test for 'closure with structure functions is vacuous': ruler model in d = 2.
du_x = xi_x (1 + (Delta_1 u)_x) on an L1 x L2 torus, Delta_1 = central difference along e_1.
(a) e_1 sector xi = xi(x_1): L1 generators on an L1*L2-dim space -> test involutivity (Frobenius).
(b) full set xi(x): L1*L2 generators = a frame -> closes trivially.  Exact rationals.  New code."""
import random, itertools, sympy as sp
L1, L2 = 3, 3
sites = [(i, j) for i in range(L1) for j in range(L2)]
idx = {s: k for k, s in enumerate(sites)}
u = sp.symbols(f"u0:{len(sites)}")
def D1u(s):
    i, j = s
    return sp.Rational(1, 2) * (u[idx[((i + 1) % L1, j)]] - u[idx[((i - 1) % L1, j)]])
g = [1 + D1u(s) for s in sites]
def br(V, W):
    return [sp.expand(sum(V[a] * sp.diff(W[b], u[a]) - W[a] * sp.diff(V[b], u[a]) for a in range(len(u)))) for b in range(len(u))]
rnd = random.Random(11)
pt = {v: sp.Rational(rnd.randint(-6, 6), rnd.randint(5, 11)) for v in u}
# (a) column generators
Vcol = [[g[idx[s]] if s[0] == c else 0 for s in sites] for c in range(L1)]
rows = [[sp.sympify(x).subs(pt) for x in V] for V in Vcol]
base_rank = sp.Matrix(rows).rank()
for a, b in itertools.combinations(range(L1), 2):
    rows.append([x.subs(pt) for x in br(Vcol[a], Vcol[b])])
full_rank = sp.Matrix(rows).rank()
ok_a = base_rank == L1 and full_rank > L1
print(f"[{'PASS' if ok_a else 'FAIL'}] d2_e1_sector_not_involutive  rank span(V_col) = {base_rank}, with brackets = {full_rank}: "
      f"the e_1 sector does NOT close even with structure functions in d = 2")
# (b) full site set is a frame at the point
Vsite = [[g[idx[s]] if s == t else 0 for s in sites] for t in sites]
fr = sp.Matrix([[sp.sympify(x).subs(pt) for x in V] for V in Vsite]).rank()
ok_b = fr == len(sites)
print(f"[{'PASS' if ok_b else 'FAIL'}] d2_full_set_frame  rank = {fr} = dim: the full xi(x) set is a frame, so it closes trivially with structure functions")
print(f"\nTOTAL: PASS={int(ok_a)+int(ok_b)} FAIL={2-int(ok_a)-int(ok_b)}")
