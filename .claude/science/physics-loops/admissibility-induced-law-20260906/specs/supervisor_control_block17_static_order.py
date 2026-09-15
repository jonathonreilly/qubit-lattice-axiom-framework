"""Control, block 17 (supervisor): the static six-axis law at strong coupling.
(1) eigenvalues of phi: Z1, p-q (x3), p+q-2r (x2); PSD region;
(2) reflection positivity for site reflections on a ring of 4 and a 4x2 torus (exact, random F);
(3) chessboard instance on the ring of 4: P(bonds (0,1) and (2,3) bad) <= P(all bad)^{2/4};
(4) disseminated ratio Z(all dir-1 bonds bad)/Z on small tori vs (6 m/p)^N, m = max(q,r);
(5) connected sets of dual plaquettes (bonds) of size n containing a fixed bond in the bond-adjacency graph, n <= 5, vs (e*11)^(n-1);
(6) the Peierls threshold p_0 from sum_{n>=6} 3n 30^n eps^{n/3} <= 1/2 with eps = 6m/p;
(7) LRO on 2x2xL tori by transfer matrix at p = 3 and p = p_0 (P(v_0 = v_{L/2}))."""
from fractions import Fraction as F
from itertools import product, permutations
from functools import reduce
import random, math, sys

import sympy as sp
M = 6
def orbit_type(s, u):
    return "p" if s == u else ("q" if s // 2 == u // 2 else "r")
def phi_matrix(p, q, r):
    W = {"p": p, "q": q, "r": r}
    return [[W[orbit_type(s, t)] for t in range(M)] for s in range(M)]
# (1)
P, Q, R = sp.symbols("p q r", positive=True)
Phi = sp.Matrix(6, 6, lambda i, j: {"p": P, "q": Q, "r": R}[orbit_type(i, j)])
print("eigenvalues of phi:", Phi.eigenvals())
# (2) RP: ring of 4 sites 0-1-2-3-0, reflection theta fixing 0 and 2, swapping 1 and 3
def ring_measure(phi, n):
    w = {}
    for v in product(range(M), repeat=n):
        x = 1
        for i in range(n):
            x *= phi[v[i]][v[(i + 1) % n]]
        w[v] = x
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}
phi = phi_matrix(3, 1, 2)
mu4 = ring_measure(phi, 4)
random.seed(1)
ok_rp = True
for _ in range(20):
    Ftab = {k: F(random.randint(-9, 9)) for k in product(range(M), repeat=3)}  # F depends on (v0, v1, v2)
    val = sum(mu4[v] * Ftab[(v[0], v[1], v[2])] * Ftab[(v[0], v[3], v[2])] for v in mu4)  # theta F depends on (v0, v3, v2)
    ok_rp = ok_rp and val >= 0
print("RP (site reflection) on the ring of 4 for 20 random F:", ok_rp)
# 4x2 torus: sites (i,j), i mod 4, j mod 2; reflection i -> -i mod 4 fixes i = 0, 2
def torus_measure_4x2(phi):
    sites = [(i, j) for i in range(4) for j in range(2)]
    idx = {s: k for k, s in enumerate(sites)}
    bonds = set()
    for (i, j) in sites:
        bonds.add(tuple(sorted((idx[(i, j)], idx[((i + 1) % 4, j)]))))
        bonds.add(tuple(sorted((idx[(i, j)], idx[(i, (j + 1) % 2)]))))
    bonds = sorted(bonds)
    w = {}
    for v in product(range(M), repeat=8):
        x = 1
        for (a, b) in bonds:
            x *= phi[v[a]][v[b]]
        w[v] = x
    Z = sum(w.values())
    return sites, idx, bonds, {v: F(x, Z) for v, x in w.items()}
sites, idx, bonds, mu8 = torus_measure_4x2(phi)
left = [idx[(i, j)] for i in (0, 1, 2) for j in range(2)]
refl = {idx[(i, j)]: idx[((-i) % 4, j)] for (i, j) in sites}
ok_rp2 = True
for _ in range(5):
    Ftab = {k: F(random.randint(-5, 5)) for k in product(range(M), repeat=len(left))}
    val = F(0)
    for v, pr in mu8.items():
        f = Ftab[tuple(v[s] for s in left)]
        tf = Ftab[tuple(v[refl[s]] for s in left)]
        val += pr * f * tf
    ok_rp2 = ok_rp2 and val >= 0
print("RP on the 4x2 torus for 5 random F:", ok_rp2)
# (3) chessboard on the ring: bad = different values
def bad(v, a, b):
    return v[a] != v[b]
p_both = sum(pr for v, pr in mu4.items() if bad(v, 0, 1) and bad(v, 2, 3))
p_all = sum(pr for v, pr in mu4.items() if all(bad(v, i, (i + 1) % 4) for i in range(4)))
print("chessboard on the ring: P(bonds 01,23 bad) =", p_both, "<= P(all bad)^{2/4}:", p_both ** 2 <= p_all)
# (4) disseminated ratio on the 4x2 torus: all horizontal (dir-1) bonds bad
Zratio = sum(pr for v, pr in mu8.items() if all(v[idx[(i, j)]] != v[idx[((i + 1) % 4, j)]] for i in range(4) for j in range(2)))
m = 2
print("4x2 torus: P(all dir-1 bonds bad) =", Zratio, "; (6m/p)^N with N = 8 =", F(6 * m, 3) ** 8, "; per-site ratio", float(Zratio) ** (1 / 8), "vs 6m/p =", 6 * m / 3)
# (5) connected sets of bonds (dual plaquettes) of size n containing the origin bond, adjacency = share a dual edge (bonds sharing a site or both ... use: two bonds are adjacent if their dual plaquettes share an edge = the bonds are within one unit cube and not parallel-opposite)
def bond_neighbors(b):
    (x, d) = b  # bond from x in direction d
    out = set()
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    # dual plaquette of bond (x,d): plaquettes sharing an edge with it: the 4 parallel-shifted... use all bonds within distance: sites x, x+e_d and their neighbours' bonds
    e = dirs[d]
    y = tuple(x[k] + e[k] for k in range(3))
    for z in (x, y):
        for dd in range(3):
            for sgn in (1, -1):
                w = tuple(z[k] + sgn * dirs[dd][k] for k in range(3))
                # bond between z and w in canonical form
                if sgn == 1:
                    cand = (z, dd)
                else:
                    cand = (w, dd)
                if cand != b:
                    out.add(cand)
    return out
counts = {}
frontier = {frozenset([((0, 0, 0), 0)])}
for n in range(1, 6):
    counts[n] = len(frontier)
    nxt = set()
    for s in frontier:
        nb = set()
        for b in s:
            nb |= bond_neighbors(b)
        for b in nb - s:
            nxt.add(frozenset(s | {b}))
    frontier = nxt
print("connected bond-sets containing the origin bond, size n = 1..5:", counts, "; bound (e*11)^(n-1):", [round((math.e * 11) ** (n - 1)) for n in range(1, 6)])
# (6) Peierls threshold: sum_{n>=6} 3n 30^n eps^(n/3) with x = 30 eps^(1/3): sum = 3 sum_{n>=6} n x^n = 3 x^6 (6 - 5x)/(1-x)^2 for x<1; require <= 1/2
x = sp.symbols("x", positive=True)
S6 = 3 * x ** 6 * (6 - 5 * x) / (1 - x) ** 2
sol = sp.nsolve(S6 - sp.Rational(1, 2), x, 0.6)
print("x* with 3 sum_{n>=6} n x^n = 1/2:", sol, "; eps = (x/30)^3 =", (sol / 30) ** 3, "; p_0 = 6m/eps =", 6 * m / (sol / 30) ** 3)
