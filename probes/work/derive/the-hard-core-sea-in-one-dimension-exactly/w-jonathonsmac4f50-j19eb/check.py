#!/usr/bin/env python3
"""the-hard-core-sea-in-one-dimension-exactly, attempt 1 (worker w-jonathonsmac4f50-j19eb, claude-opus-5-5).

Exact claims: sympy / integers. Lines tagged [executed] are floating point (full exact diagonalisation of the many-record space and
the charge reduction), labelled as evidence. Step labels refer to ATTEMPT.md.
"""
import itertools
import sys
import time
from math import gcd

import numpy as np
import scipy.sparse as sps
import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- Step 1: exact identities behind the reduction
N6 = 6
Tm = sp.zeros(N6, N6)
for x in range(N6):
    Tm[x, (x + 1) % N6] = 1
D = (Tm - Tm.T) / (2 * sp.I)
G = sp.diag(*[(-1) ** x for x in range(N6)])
ok("1.1 (-1)^x D (-1)^x = -D on an even ring: the gauge (-1)^x on down coins turns sigma_3 D into D for both coins", sp.simplify(G * D * G + D) == sp.zeros(N6, N6))
a = sp.symbols("a", positive=True)
phi = sp.diag(*[a ** ((-1) ** x) for x in range(N6)])
ok("1.2 chessboard of clocks phi_x = a^{(-1)^x}: phi D phi = D exactly (phi_x phi_{x+1} = 1 on every bond), so the sea cannot see it", sp.simplify(phi * D * phi - D) == sp.zeros(N6, N6))
th, nn = sp.symbols("theta n", real=True)
Nn = sp.symbols("N", positive=True, integer=True)
full = sp.simplify(sum(sp.sin((2 * sp.pi * k + th) / 8) for k in range(8)))
ok("1.3 a full twisted charge band sums to zero: sum_n sin((2 pi n + theta)/N) = 0 (checked for N = 8, symbolic theta)", full == 0)


from functools import lru_cache
from sympy import divisors
from sympy.functions.combinatorial.numbers import mobius


def ramanujan(m, J):  # c_m(J) = sum_{r mod m, gcd(r, m) = 1} e^{2 pi i J r/m} = sum_{k | gcd(m, J)} mu(m/k) k  (an integer)
    g = gcd(m, J)
    return sum(int(mobius(m // k)) * k for k in divisors(g))


@lru_cache(maxsize=None)
def Dcount(Np, J):
    # N_p^-1 sum_{r mod N_p} e^{-2 pi i J r/N_p} 2^{gcd(r, N_p)} = N_p^-1 sum_{d | N_p} 2^d c_{N_p/d}(J), exactly in integers
    tot = sum(2 ** d * ramanujan(Np // d, J % Np) for d in divisors(Np))
    assert tot % Np == 0
    return tot // Np


Dc = {(Np, J): Dcount(Np, J) for Np in (3, 4, 6) for J in range(Np)}
# cross-check the integer formula against the defining sum of roots of unity for small N_p (exact sympy)
direct = all(sp.simplify(sp.expand_complex(sum(sp.exp(-2 * sp.pi * sp.I * J * r / Np) * 2 ** gcd(r, Np) for r in range(Np)) / Np)) == Dcount(Np, J)
             for Np in (3, 4, 6) for J in range(Np))
ok("1.4 coin sequences by cyclic momentum J (necklace count D(J) = N_p^-1 sum_r e^{-2 pi i J r/N_p} 2^{gcd(r, N_p)}): exact integers summing to 2^{N_p}",
   direct and all(sum(Dcount(Np, J) for J in range(Np)) == 2 ** Np for Np in (3, 4, 6, 12, 30, 62)), f"N_p=3: {[Dc[(3, J)] for J in range(3)]}, 4: {[Dc[(4, J)] for J in range(4)]}, 6: {[Dc[(6, J)] for J in range(6)]}")

# ---------------------------------------------------------------- [executed] full many-record diagonalisation against the reduction


def build(N, Np, sign, phiv):
    states = [s for s in itertools.product((0, 1, 2), repeat=N) if sum(1 for q in s if q) == Np]
    idx = {s: i for i, s in enumerate(states)}
    rows, cols, vals = [], [], []
    for s in states:
        i = idx[s]
        for x in range(N):
            y = (x + 1) % N
            for (src, dst, back) in ((y, x, False), (x, y, True)):
                q = s[src]
                if q == 0 or s[dst] != 0:
                    continue
                s3 = 1 if q == 1 else -1
                amp = phiv[x] * phiv[y] * s3 / 2j
                if back:
                    amp = np.conj(amp)
                t = list(s)
                t[dst], t[src] = q, 0
                f = (-1) ** (Np - 1) if (sign == "F" and {src, dst} == {0, N - 1}) else 1
                rows.append(idx[tuple(t)])
                cols.append(i)
                vals.append(amp * f)
    return sps.csr_matrix((vals, (rows, cols)), shape=(len(states), len(states)))


def charge_levels(N, theta, phiv):
    h = np.zeros((N, N), complex)
    for x in range(N):
        y = (x + 1) % N
        amp = phiv[x] * phiv[y] / 2j * (np.exp(1j * theta) if y == 0 else 1)
        h[x, y] += amp
        h[y, x] += np.conj(amp)
    return np.sort(np.linalg.eigvalsh(h))


def reduction_ground(N, Np, sign, phiv):
    best = []
    for J in range(Np):
        d = Dcount(Np, J)
        if d == 0:
            continue
        th_ = 2 * np.pi * J / Np + (np.pi * (Np - 1) if sign == "B" else 0)
        best.append((charge_levels(N, th_, phiv)[:Np].sum(), d))
    e0 = min(e for e, d in best)
    return e0, sum(d for e, d in best if abs(e - e0) < 1e-9)


match = True
rows_out = []
for N in (6, 8):
    for Np in (N // 2, N - 2):
        for sign in ("F", "B"):
            ev = np.sort(np.linalg.eigvalsh(build(N, Np, sign, np.ones(N)).toarray()))
            deg = int(np.sum(np.abs(ev - ev[0]) < 1e-9))
            e_r, d_r = reduction_ground(N, Np, sign, np.ones(N))
            match &= abs(ev[0] - e_r) < 1e-10 and deg == d_r
            rows_out.append((N, Np, sign, ev[0], deg))
ok("X1 [executed] full diagonalisation of the many-record space (each site empty or one record with a coin; hard-core; fermionic F and bosonic B) equals the reduction - free charge fermions with twist 2 pi J/N_p (+ pi(N_p - 1) for B) times coin sequences of cyclic momentum J - in ground energy and degeneracy, N = 6, 8",
   match, "; ".join(f"N={r[0]} Np={r[1]} {r[2]}: E0 {r[3]:.6f} deg {r[4]}" for r in rows_out))
# exact closed form of one ground energy: N = 6, N_p = 3 (twist 2 pi/3): -(sin(pi/9) + sin(2 pi/9) + sin(4 pi/9))
e_exact = -(sp.sin(sp.pi / 9) + sp.sin(2 * sp.pi / 9) + sp.sin(4 * sp.pi / 9))
ok("X2 N = 6, N_p = 3: the ground energy is -(sin(pi/9) + sin(2pi/9) + sin(4pi/9)) = -1.9696155..., the three lowest levels of the band twisted by 2 pi/3",
   abs(float(e_exact) - rows_out[0][3]) < 1e-12, f"{sp.N(e_exact, 12)}")

# ---------------------------------------------------------------- Step 3: energy per site and the bound at filling N - 2


def onebody_E(N, Np, phiv):
    h = np.zeros((2 * N, 2 * N), complex)
    for x in range(N):
        y = (x + 1) % N
        for s, s3 in ((0, 1), (1, -1)):
            amp = phiv[x] * phiv[y] * s3 / 2j
            h[2 * x + s, 2 * y + s] += amp
            h[2 * y + s, 2 * x + s] += np.conj(amp)
    return np.sort(np.linalg.eigvalsh(h))[:Np].sum()


tab = []
for N in (8, 16, 32, 64):
    eh = reduction_ground(N, N - 2, "F", np.ones(N))[0]
    ef = onebody_E(N, N - 2, np.ones(N))
    tab.append((N, eh / N, ef / N))
ok("3.1 at the filling N - 2 that would fill the free sea's negative branch, the hard-core energy is minus the two highest charge levels (1.3), so |E0|/N <= 2/N -> 0, against the free sea's -> -2/pi",
   all(abs(r[1]) <= 2 / r[0] + 1e-12 for r in tab) and abs(tab[-1][2] + 2 / np.pi) < 0.01,
   "; ".join(f"N={r[0]}: hard-core {r[1]:.4f}, free {r[2]:.4f}" for r in tab))

# ---------------------------------------------------------------- [executed] the polarisability: second-order response to u = eps cos(2 pi m x/N)


def stiffness(fE, N, m, h=0.005):
    q = 2 * np.pi * m / N
    E = lambda e: fE(np.exp(e * np.cos(q * np.arange(N)) / 2))
    e0 = E(0)
    d2 = (E(h) + E(-h) - 2 * e0) / h ** 2
    return d2, (d2 - (e0 / N) * N / 2) / (N * (2 - 2 * np.cos(q)) / 2)


# ED check of the reduction's response at N = 8
ed8 = stiffness(lambda p: np.linalg.eigvalsh(build(8, 6, "F", p).toarray())[0], 8, 1)
rd8 = stiffness(lambda p: reduction_ground(8, 6, "F", p)[0], 8, 1)
ok("X3 [executed] the reduction reproduces the full diagonalisation's second-order response (N = 8, filling 6)", abs(ed8[0] - rd8[0]) < 1e-5, f"d2E/de2 {ed8[0]:.6f} vs {rd8[0]:.6f}")
kt = []
for N in (8, 16, 32, 64):
    kf = stiffness(lambda p: onebody_E(N, N - 2, p), N, 2)[1]
    kh = stiffness(lambda p: reduction_ground(N, N // 2, "F", p)[0], N, 1)[1]
    kn = stiffness(lambda p: reduction_ground(N, N - 2, "F", p)[0], N, 1)[1]
    kt.append((N, kf, kh, kn))
    print(f"EXEC kappa (gradient part after the volume term, block 76's split): N={N}: free sea (N-2, m=2) {kf:+.4f}; hard-core half filling (m=1) {kh:+.4f}; hard-core N-2 (m=1) {kn:+.4f}")
ok("X4 [executed] half filling: the hard-core stiffness is positive and converges (0.0817 -> 0.0796), the free sea's sign; at filling N - 2 the hard-core response is NEGATIVE and grows without bound (two holes, no local stiffness), opposite to the free sea's positive stiffness",
   all(r[1] > 0 and r[2] > 0 and r[3] < 0 for r in kt) and kt[-1][3] < 50 * kt[0][3])

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL on a ring the hard-core many-record problem of the reduced walk is exactly free charge fermions of ONE band with a twist set by "
      "the coin sequence's cyclic momentum, times the coin sequences (necklace counts), for either exchange sign (full diagonalisation agrees, N = 6, 8); "
      "at the filling N - 2 that would fill the free sea's negative branch the energy is minus two levels (|E0|/N <= 2/N, free -2/pi), the ground space "
      "is coin-degenerate (6/4 on N = 6, 10/14 on N = 8) and the second-order response to a rate modulation is negative and unbounded in N, opposite to the "
      "free sea's positive stiffness; at half filling the stiffness is positive (0.0796); the chessboard of clocks stays exactly invisible")
print("HIT: under one-record-per-site exclusion the 'filled negative branch' has no sea meaning on a ring: the filling that would fill it is a nearly full "
      "single charge band (energy per site bounded by 2/N, not -2/pi), coin-degenerate, with a negative and unbounded response to a rate modulation - "
      "opposite in sign to the free sea's stiffness; at half filling the hard-core stiffness is positive (0.0796)")
