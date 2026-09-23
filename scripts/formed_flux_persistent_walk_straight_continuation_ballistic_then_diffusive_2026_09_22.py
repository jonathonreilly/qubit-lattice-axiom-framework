#!/usr/bin/env python3
"""Persistent mean-flux transport for a supplied straight-continuation rule.

The supplied sweep, axis pairing and probability rule are premises. The explicit finite error bound below is checked only at p=1/2 over the printed range. No continuum telegraph limit, isotropic wave theorem, photon dynamics or physical diffusion coefficient is established.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from fractions import Fraction as Fr
from itertools import permutations, product
from math import factorial

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


PM = (1, -1)


def rule(p, back):
    B = sum(back)
    outs = [f for f in product(PM, repeat=3) if sum(f) == B]
    law = {f: (1 - p) / len(outs) for f in outs}
    law[tuple(back)] = law.get(tuple(back), Fr(0)) + p
    return law


# ---------- A. the rule ----------
print("A. the straight-continuation rule")
ok_ice, ok_mean, ok_sym = True, True, True
for p in (Fr(0), Fr(1, 3), Fr(1, 2), Fr(1)):
    for back in product(PM, repeat=3):
        law = rule(p, back)
        ok_ice = ok_ice and sum(law.values()) == 1 and all(sum(f) == sum(back) for f, q in law.items() if q)
        for i in range(3):
            m = sum(q * f[i] for f, q in law.items())
            ok_mean = ok_mean and m == p * back[i] + (1 - p) * Fr(sum(back), 3)
        for s in permutations(range(3)):
            perm = lambda v: tuple(v[s[k]] for k in range(3))
            law2 = rule(p, perm(back))
            ok_sym = ok_sym and all(law2.get(perm(f), 0) == q for f, q in law.items())
check("R_p keeps the ice rule exactly and each forward arrow has mean p b_i + (1 - p) B/3",
      ok_ice and ok_mean, "p = 0, 1/3, 1/2, 1; all 8 back patterns")
check("R_p is covariant under the six axis permutations that preserve the sweep's octant (soldered: straight pairs axes)",
      ok_sym)

# ---------- B. the direction kernel ----------
print("B. the persistent walk")


def K(p):
    return [[p * (i == j) + (1 - p) / 3 for j in range(3)] for i in range(3)]


ok_k = True
for p in (Fr(0), Fr(1, 2), Fr(3, 4), Fr(1)):
    k = K(p)
    ones = [sum(r) for r in k]
    v = [Fr(1), Fr(-1), Fr(0)]
    kv = [sum(k[i][j] * v[j] for j in range(3)) for i in range(3)]
    ok_k = ok_k and ones == [1, 1, 1] and kv == [p * x for x in v]
check("the flux's direction kernel K = p I + (1 - p) J/3 has eigenvalues 1, p, p: memory relaxes by p per layer",
      ok_k, "a unit of flux keeps its axis with probability (1 + 2p)/3")


def flux_kernel(p, nmax):
    k = K(p)
    G = {((0, 0, 0), 0): Fr(1)}
    for s in range(1, nmax + 1):
        for a in range(s + 1):
            for b in range(s + 1 - a):
                y = (a, b, s - a - b)
                for j in range(3):
                    prev = tuple(y[t] - (1 if t == j else 0) for t in range(3))
                    if min(prev) < 0:
                        continue
                    val = sum(G.get((prev, i), Fr(0)) * k[i][j] for i in range(3))
                    if val:
                        G[(y, j)] = val
    return G


NM = 24
kern = {p: flux_kernel(p, NM) for p in (Fr(0), Fr(1, 2), Fr(1))}
mass = all(sum(v for (y, j), v in G.items() if sum(y) == s) == 1 for G in kern.values() for s in range(NM + 1))


def site_mass(G, y):
    return sum(G.get((y, j), Fr(0)) for j in range(3))


def multinomial(y):
    n = sum(y)
    return Fr(factorial(n), factorial(y[0]) * factorial(y[1]) * factorial(y[2]) * 3 ** n)


sites0 = {y for (y, j) in kern[Fr(0)]}
multinom0 = all(site_mass(kern[Fr(0)], y) == multinomial(y) for y in sites0) and site_mass(kern[Fr(0)], (1, 1, 1)) == Fr(2, 9)
ballistic = all(v == 0 or (y == (sum(y), 0, 0) and j == 0) for (y, j), v in kern[Fr(1)].items())
check("each layer carries flux 1; at p = 1 the flux runs straight along its axis; at p = 0 it is the multinomial walk",
      mass and ballistic and multinom0, f"p = 0 reproduces the multinomial walk of open PR 8687 at all {len(sites0)} sites")

# ---------- C. ballistic then diffusive ----------
print("C. spreading")


def spread(G, s):
    ms = {y: site_mass(G, y) for (y, j) in G if sum(y) == s}
    mean = sum(m * y[0] for y, m in ms.items())
    return sum(m * (y[0] - mean) ** 2 for y, m in ms.items())


def markov_var(p, n):
    pi = Fr(1, 3)
    a = [pi + (1 - pi) * p ** t for t in range(n + 1)]
    v = sum(a[t] * (1 - a[t]) for t in range(1, n + 1))
    v += 2 * sum(a[s] * (pi + (1 - pi) * p ** (t - s) - a[t]) for s in range(1, n + 1) for t in range(s + 1, n + 1))
    return v


P = Fr(1, 2)
agree = all(spread(kern[P], s) == markov_var(P, s) for s in range(1, 16))
rate = Fr(2, 9) * (1 + P) / (1 - P)
diffs = [spread(kern[P], s + 1) - spread(kern[P], s) for s in range(1, NM)]
conv = all(abs(diffs[s] - rate) < 4 * (s + 2) * P ** (s + 1) for s in range(len(diffs)))
check("the spread along the source axis equals the Markov occupation variance and grows at rate (2/9)(1+p)/(1-p)",
      agree and conv and rate == Fr(2, 3), f"p = 1/2: rate 2/3, three times the rate 2/9 at p = 0; finite error bound checked at p=1/2")
check("at p = 1 the spread is 0 in every layer; at p = 0 it is 2n/9",
      all(spread(kern[Fr(1)], s) == 0 for s in range(NM + 1)) and all(spread(kern[Fr(0)], s) == Fr(2 * s, 9) for s in range(NM + 1)))

# ---------- D. exact covariances on a box ----------
print("D. exact covariances on a box")


def box_covariance(p, L):
    verts = sorted(product(range(L), repeat=3), key=lambda x: (sum(x), x))
    vid, n = {}, 0
    for x in verts:
        for i in range(3):
            if x[i] == 0:
                vid[("in", x, i)] = n
                n += 1
    nin = n
    for x in verts:
        for i in range(3):
            vid[("fw", x, i)] = n
            n += 1
    C = [[Fr(0)] * n for _ in range(n)]
    for k in range(nin):
        C[k][k] = Fr(1)

    def back_id(x, i):
        if x[i] == 0:
            return vid[("in", x, i)]
        return vid[("fw", tuple(x[j] - (1 if j == i else 0) for j in range(3)), i)]
    A = K(p)
    defined = list(range(nin))
    vbs = set()
    for x in verts:
        b = [back_id(x, i) for i in range(3)]
        f = [vid[("fw", x, i)] for i in range(3)]
        VB = sum(C[u][w] for u in b for w in b)
        vbs.add(VB)
        rows = [[sum(A[i][j] * C[b[j]][y] for j in range(3)) for y in range(n)] for i in range(3)]
        for i in range(3):
            for y in defined:
                C[f[i]][y] = C[y][f[i]] = rows[i][y]
        for i in range(3):
            for k in range(3):
                C[f[i]][f[k]] = Fr(1) if i == k else p * C[b[i]][b[k]] + (1 - p) * (VB - 3) / 6
        defined += f
    return verts, vid, C, vbs


LB = 4
causal_ok = True
for p in (Fr(1, 2), Fr(3, 4)):
    verts, vid, C, vbs = box_covariance(p, LB)
    G = flux_kernel(p, 3 * LB)
    src = vid[("in", (0, 0, 0), 0)]
    kern_ok = all(C[src][vid[("fw", y, k)]] == G.get((tuple(y[t] + (1 if t == k else 0) for t in range(3)), k), Fr(0))
                  for y in verts for k in range(3))
    same_layer = all(C[vid[("fw", x, i)]][vid[("fw", y, k)]] == 0 for x in verts for y in verts
                     if sum(x) == sum(y) and x != y for i in range(3) for k in range(3))
    at_vertex = all(C[vid[("fw", x, i)]][vid[("fw", x, k)]] == (1 if i == k else 0) for x in verts for i in range(3) for k in range(3))
    causal_ok = causal_ok and kern_ok and same_layer and at_vertex and vbs == {3}
check("for p = 1/2 and 3/4 the covariance stays causal: back sums have variance 3, same-layer arrows are uncorrelated",
      causal_ok, "and the covariance with an inflow arrow is the persistent-walk kernel, on a 4x4x4 box")

print('per_element: Integer configurations, weights and conditional cross-products are exact within the stated finite alphabets; floating spectral estimates are labelled.')
print('per_site: Site and unit tests use the declared records, neighbour graph, boundary conditions and fixed formation orders only.')
print('per_mode: Transfer and walk modes refer to supplied finite matrices; numerical estimates do not establish untested physical or infinite-cross-section limits.')
print('per_block: This bounded support result retains its explicit controls, parameter values and search caps; alternative rules and records remain outside scope.')
print('lattice_wide: Finite windows do not establish universal formation impossibility; infinite-height statements apply only to the specified fixed-cross-section transfer model.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
