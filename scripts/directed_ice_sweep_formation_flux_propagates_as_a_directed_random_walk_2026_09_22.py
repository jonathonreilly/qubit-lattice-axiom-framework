#!/usr/bin/env python3
"""Directed ice: formation along a sweep keeps the ice rule exactly, and a
flux fluctuation then propagates along the sweep diagonal as a directed
random walk; the uniform ice measure has no direction.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic; no floating point.

Declared objects
  * coarse vertices of Z^3 with arrow variables on links (sigma = +1 when the
    arrow points along +e_i); the ice rule in arrow form: at every vertex
    the forward arrows sum to the backward arrows (3 in, 3 out);
  * the sweep of open PRs 8667 and 8670: each vertex forms after its three
    back-links and chooses its forward arrows uniformly among those that
    keep the ice rule (the soldered uniform-consistent vertex rule);
  * the mean-response kernel: the change of expected arrows after a unit
    change of one back-link, propagated by the rule's conditional means;
  * a coarse box with independent uniform inflow arrows, and the uniform
    ice measure on the 2x2x2 torus of the landed notes (9600 states).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 120
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


# ---------- A. the sweep rule ----------
print("A. the sweep rule in arrow form")
PM = (1, -1)
ok_mean, ok_cov, ok_sum = True, True, True
for back in product(PM, repeat=3):
    B = sum(back)
    outs = [f for f in product(PM, repeat=3) if sum(f) == B]
    n = len(outs)
    mean = [Fr(sum(f[i] for f in outs), n) for i in range(3)]
    ok_mean = ok_mean and mean == [Fr(B, 3)] * 3
    for i in range(3):
        for j in range(3):
            cov = Fr(sum(f[i] * f[j] for f in outs), n) - mean[i] * mean[j]
            p0 = Fr(1 if i == j else 0) - Fr(1, 3)
            ok_cov = ok_cov and cov == Fr(3, 2) * (1 - Fr(B * B, 9)) * p0
    ok_sum = ok_sum and all(sum(f) == B for f in outs)
check("each forward arrow has conditional mean B/3, where B is the back-arrow sum",
      ok_mean, "the ice rule forces the forward sum to equal B")
check("the conditional covariance is (3/2)(1 - B^2/9) times the projector onto sum-zero patterns",
      ok_cov and ok_sum, "the fluctuations never change the flux a vertex passes on")

# ---------- B. the mean-response kernel ----------
print("B. flux propagation")
NMAX = 14
R = {(0, 0, 0): Fr(1)}
for s in range(1, NMAX + 1):
    for a in range(s + 1):
        for b in range(s + 1 - a):
            c = s - a - b
            R[(a, b, c)] = sum(R.get(t, Fr(0)) for t in ((a - 1, b, c), (a, b - 1, c), (a, b, c - 1))) / 3


def multinom(a, b, c):
    n = a + b + c
    return Fr(factorial(n), factorial(a) * factorial(b) * factorial(c) * 3 ** n)


check("the response obeys R(x) = (1/3) sum over back-neighbours, and equals the multinomial walk",
      all(R[x] == multinom(*x) for x in R), f"all points with a + b + c <= {NMAX}")
layers = [sum(v for x, v in R.items() if sum(x) == s) for s in range(NMAX + 1)]
spread = [sum(v * (x[0] - Fr(s, 3)) ** 2 for x, v in R.items() if sum(x) == s) for s in range(NMAX + 1)]
check("each diagonal layer carries total response 1 (conserved flux), with per-coordinate centered variance 2n/9",
      all(m == 1 for m in layers) and all(spread[s] == Fr(2 * s, 9) for s in range(NMAX + 1)),
      "the response lives in the forward cone and spreads like a random walk")
diag = [multinom(m, m, m) for m in range(1, 21)]
ratio = all(diag[m] / diag[m - 1] == Fr((3 * m + 1) * (3 * m + 2), 9 * (m + 1) ** 2) for m in range(1, 20))
mono = all((m + 2) * diag[m + 1] > (m + 1) * diag[m] for m in range(19)) and 20 * diag[19] < 1
check("on the diagonal R(m,m,m) = (3m)!/(m!^3 27^m): consecutive ratios (3m+1)(3m+2)/(9(m+1)^2), m R_m rising below 1",
      ratio and mono, f"R(1,1,1) = {diag[0]}, 20 R(20,20,20) = {float(20 * diag[19]):.4f}: decay like 1/m")

axis_decay = all(multinom(n, 0, 0) == Fr(1, 3 ** n) for n in range(0, 21))
edge = all(multinom(n, n, 0) * (n + 1) < 1 for n in range(1, 21)) and all(
    multinom(n + 1, n + 1, 0) / multinom(n, n, 0) == Fr((2 * n + 1) * (2 * n + 2), 9 * (n + 1) ** 2) for n in range(20))
check("along a lattice axis the response is 3^(-n); along a face diagonal it falls by (2n+1)(2n+2)/(9(n+1)^2) per step",
      axis_decay and edge, "exponential along axes, geometric 4/9 along face diagonals, power law only along the body diagonal")

# ---------- C. the symbol ----------
print("C. the Fourier symbol")


def series_exp_minus_i(order):
    # coefficients of e^{-ik} = sum (-i k)^n / n!, as (real, imag) pairs per power of k
    out = []
    for n in range(order + 1):
        c = Fr(1, factorial(n))
        re, im = [(c, 0), (0, -c), (-c, 0), (0, c)][n % 4]
        out.append((Fr(re), Fr(im)))
    return out


E = series_exp_minus_i(3)
D = {n: (-E[n][0] / 3, -E[n][1] / 3) for n in (1, 2, 3)}
check("D(k) = 1 - (1/3) sum_j e^(-i k_j) expands as (i/3) sum k_j + (1/6) sum k_j^2 - (i/18) sum k_j^3 + ...",
      1 - E[0][0] == 0 and D[1] == (0, Fr(1, 3)) and D[2] == (Fr(1, 6), 0) and D[3] == (0, Fr(-1, 18)),
      "first order along (1,1,1), second order across it: directed diffusion")
QUARTER = [(1, 0), (0, -1), (-1, 0), (0, 1)]
zeros = [k for k in product(range(4), repeat=3)
         if (3 - sum(QUARTER[m][0] for m in k), -sum(QUARTER[m][1] for m in k)) == (0, 0)]
check("D vanishes only at k = 0 modulo 2pi per coordinate (Re D = 1 - (1/3) sum cos k_j); on the quarter-period grid the only zero is k = 0",
      zeros == [(0, 0, 0)], "zero set of this declared scalar response symbol only")

# ---------- D. exact covariances on a box ----------
print("D. exact covariances on a box")
L = 4
verts = sorted(product(range(L), repeat=3), key=lambda x: (sum(x), x))
vid, N = {}, 0
for x in verts:
    for i in range(3):
        if x[i] == 0:
            vid[("in", x, i)] = N
            N += 1
NIN = N
for x in verts:
    for i in range(3):
        vid[("fw", x, i)] = N
        N += 1
C = [[Fr(0)] * N for _ in range(N)]
for k in range(NIN):
    C[k][k] = Fr(1)


def back_id(x, i):
    if x[i] == 0:
        return vid[("in", x, i)]
    return vid[("fw", tuple(x[j] - (1 if j == i else 0) for j in range(3)), i)]


defined = list(range(NIN))
for x in verts:
    b = [back_id(x, i) for i in range(3)]
    f = [vid[("fw", x, i)] for i in range(3)]
    VB = sum(C[p][q] for p in b for q in b)
    row = [(C[b[0]][y] + C[b[1]][y] + C[b[2]][y]) / 3 for y in range(N)]
    for fi in f:
        for y in defined:
            C[fi][y] = C[y][fi] = row[y]
    for i in range(3):
        for j in range(3):
            C[f[i]][f[j]] = Fr(1) if i == j else (VB - 3) / 6
    defined += f
unit = all(C[k][k] == 1 for k in range(N))
div = True
for x in verts:
    b = [back_id(x, i) for i in range(3)]
    f = [vid[("fw", x, i)] for i in range(3)]
    w = {k: 1 for k in f}
    for k in b:
        w[k] = w.get(k, 0) - 1
    div = div and sum(w[p] * w[q] * C[p][q] for p in w for q in w) == 0
check("every arrow has variance 1 and every vertex passes on exactly its incoming flux",
      unit and div, f"{N} arrows on a {L}x{L}x{L} box, second moments closed exactly")
o = vid[("in", (0, 0, 0), 0)]
kern = all(C[o][vid[("fw", x, i)]] == multinom(*x) / 3 for x in verts for i in range(3))
src = vid[("in", (0, 2, 2), 0)]
cone = all((C[src][vid[("fw", x, i)]] != 0) == (x[1] >= 2 and x[2] >= 2) for x in verts for i in range(3))
check("covariance with one inflow arrow is the kernel R/3, and vanishes outside that arrow's forward cone",
      kern and cone, "a flux fluctuation reaches only the sweep's future")
VBS = set()
for x in verts:
    b = [back_id(x, i) for i in range(3)]
    VBS.add(sum(C[p][q] for p in b for q in b))
causal = True
for x in verts:
    for i in range(3):
        head = tuple(x[j] + (1 if j == i else 0) for j in range(3))
        for y in verts:
            for k in range(3):
                got = C[vid[("fw", x, i)]][vid[("fw", y, k)]]
                if y == x:
                    want = Fr(1 if k == i else 0)
                elif all(y[j] >= head[j] for j in range(3)):
                    want = multinom(*(y[j] - head[j] for j in range(3))) / 3
                elif all(x[j] >= y[j] + (1 if j == k else 0) for j in range(3)):
                    want = multinom(*(x[j] - y[j] - (1 if j == k else 0) for j in range(3))) / 3
                else:
                    want = Fr(0)
                causal = causal and got == want
check("the whole covariance is causal: arrows correlate only inside each other's forward cone, as R/3",
      causal and VBS == {3}, f"{len(verts) * 3} forward arrows; back sums always have variance 3, so same-layer arrows are uncorrelated")

# ---------- E. the uniform measure has no direction ----------
print("E. the uniform ice measure (landed L = 2 torus)")
T = 4
SITES = [(x, y, z) for x in range(T) for y in range(T) for z in range(T)]
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def addm(s, d):
    return tuple((a + b) % T for a, b in zip(s, d))


VS = [s for s in SITES if all(a % 2 == 0 for a in s)]
LS = [s for s in SITES if sum(a % 2 for a in s) == 1]
LI = {l: i for i, l in enumerate(LS)}
ice = []


def rec(k, n):
    if k == len(VS):
        ice.append(tuple(n[l] for l in LS))
        return
    star = [addm(VS[k], d) for d in DIRS]
    free = [l for l in star if l not in n]
    need = 3 - sum(n[l] for l in star if l in n)
    if 0 <= need <= len(free):
        for occ in product((0, 1), repeat=len(free)):
            if sum(occ) == need:
                for l, v in zip(free, occ):
                    n[l] = v
                rec(k + 1, n)
                for l in free:
                    del n[l]


rec(0, {})


def axis(l):
    return next(a for a in range(3) if l[a] % 2)


def arrow(c, l):
    a = axis(l)
    lo = tuple((l[j] - (1 if j == a else 0)) % T for j in range(3))
    return 1 if (c[LI[l]] == 1) == (sum(v // 2 for v in lo) % 2 == 0) else -1


ARR = [[arrow(c, l) for l in LS] for c in ice]
M = len(ARR)
COV = [[Fr(sum(r[i] * r[j] for r in ARR), M) for j in range(len(LS))] for i in range(len(LS))]
SP = [tuple(tuple(s[i] if j == p[i] else 0 for j in range(3)) for i in range(3))
      for p in permutations(range(3)) for s in product((1, -1), repeat=3)]


def act(g, s):
    return tuple(sum(g[i][j] * s[j] for j in range(3)) % T for i in range(3))


def arrow_sign(g, l):
    a = axis(l)
    return next(g[i][a] for i in range(3) if g[i][a] != 0)


sym = all(COV[LI[act(g, l)]][LI[act(g, m)]] * arrow_sign(g, l) * arrow_sign(g, m) == COV[LI[l]][LI[m]]
          for g in SP for l in LS for m in LS)
check("the uniform measure's arrow covariance is invariant under all 48 cubic symmetries, including reversal",
      M == 9600 and sym, "the sweep's response lives in one diagonal cone, so it has no such symmetry")

print("N5 resolution certificate: exact finite algebra and declared enumeration domains only")
print("N5 sampling certificate: external fixed orders and fresh conditional draws where formation is used")
print("N5 dependency certificate: self-contained stdlib runner; no physical encoding supplied")
print("N5 scaling certificate: finite checks do not execute infinite-volume or spectral limits")
print("N5 scope certificate: source proofs carry universal implications; alternative models remain open")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
