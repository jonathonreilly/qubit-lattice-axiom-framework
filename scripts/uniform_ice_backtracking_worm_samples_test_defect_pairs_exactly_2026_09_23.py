#!/usr/bin/env python3
"""Uniform ice: a backtracking worm samples test-defect pairs exactly, and on tori their free energy follows the lattice Green's function.

A worm on the divergence-free arrows of uniform ice starts at a uniformly
random vertex, reverses one of its three outgoing arrows, and then moves its
head: at every step it reverses one of the head's outgoing arrows, chosen
uniformly among all of them, including the one just reversed. It stops when
the head returns to the start. Between start and stop the configuration
carries exactly two defects: the start, with divergence -2 (two arrows out,
four in), and the head, with divergence +2 (four out, two in).

Every head step has probability 1/4 forwards and backwards; creation has
probability 1/(3N) and annihilation 1/4. The chain on ice configurations and
two-defect states therefore balances with uniform weight on each, the
two-defect weight being 4/(3N) relative to an ice configuration. So the time
the worm spends at head-minus-start displacement r is proportional to
Z_pair(r), the number of two-defect configurations with that displacement.
Its logarithm gives the pair free energy V(r) = -ln Z_pair(r) + const on any
torus, with no transfer matrix.

A Gaussian divergence-free field with stiffness K gives
V(r) - V(r') = K Q^2 (G(r') - G(r)) for charges +-Q, with G the Green's
function of the Z^3 graph Laplacian on the torus (zero mode removed). Here
Q = 2 and K = K_L = 2/3 + 1/(3N), the sum-rule stiffness of open PR 8881.

Checks:

A. Exact L = 2: all 2^24 arrow patterns give the two-defect counts at the
   seven displacements.
B. The backtracking worm on L = 2 reproduces the normalised exact counts at
   all seven displacements within 4 standard errors, and it reproduces the
   ice measure's <W^2> = 76/25 within 4 standard errors. The loop worm of
   open PR 8881, which never reverses the arrow just reversed, reproduces
   the same counts: kept together with its last reversed arrow, its chain
   has three successors and three predecessors per state, each with
   probability 1/3, and so balances with uniform weight too.
C. L = 8 with 2 x 10^6 worms: relative to the nearest pair (1, 0, 0), every
   sampled separation has measured over predicted between 0.88 and 1.02,
   with standard errors of at most 0.025. The pair attracts: V rises with
   distance to the farthest point.
D. L = 16 with 10^6 worms: along the axis, r = 2 to 8, measured over
   predicted lies between 0.85 and 1.05, standard errors at most 0.04.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
import time
from fractions import Fraction

import numpy as np
from numba import njit

PASS = FAIL = 0
T0 = time.time()


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))


@njit(cache=False)
def seed(s):
    np.random.seed(s)


@njit(cache=False)
def worm_hist(E, L, H, excl):
    # backtracking worm (excl = 0): the head chooses uniformly among all of its outgoing arrows;
    # with excl = 1 it never reverses the arrow it just reversed (the loop worm of open PR 8881)
    x0 = np.random.randint(L)
    y0 = np.random.randint(L)
    z0 = np.random.randint(L)
    x, y, z = x0, y0, z0
    ci = np.empty(6, np.int64)
    cx = np.empty(6, np.int64)
    cy = np.empty(6, np.int64)
    cz = np.empty(6, np.int64)
    cd = np.empty(6, np.int64)
    n = 0
    li, lx, ly, lz = -1, -1, -1, -1
    while True:
        m = 0
        for i in range(3):
            if E[i, x, y, z] == 1 and not (excl == 1 and li == i and lx == x and ly == y and lz == z):
                ci[m] = i
                cx[m] = x
                cy[m] = y
                cz[m] = z
                cd[m] = 1
                m += 1
            bx, by, bz = x, y, z
            if i == 0:
                bx = (x - 1) % L
            elif i == 1:
                by = (y - 1) % L
            else:
                bz = (z - 1) % L
            if E[i, bx, by, bz] == -1 and not (excl == 1 and li == i and lx == bx and ly == by and lz == bz):
                ci[m] = i
                cx[m] = bx
                cy[m] = by
                cz[m] = bz
                cd[m] = -1
                m += 1
        k = np.random.randint(m)
        i = ci[k]
        bx = cx[k]
        by = cy[k]
        bz = cz[k]
        E[i, bx, by, bz] = -E[i, bx, by, bz]
        li, lx, ly, lz = i, bx, by, bz
        if cd[k] == 1:
            if i == 0:
                x = (x + 1) % L
            elif i == 1:
                y = (y + 1) % L
            else:
                z = (z + 1) % L
        else:
            x, y, z = bx, by, bz
        n += 1
        if x == x0 and y == y0 and z == z0:
            return n
        H[(x - x0) % L, (y - y0) % L, (z - z0) % L] += 1


def initial(L):
    E = np.empty((3, L, L, L), np.int8)
    alt = (-1) ** np.arange(L)
    E[0] = np.broadcast_to(alt[None, :, None], (L, L, L))
    E[1] = np.broadcast_to(alt[None, None, :], (L, L, L))
    E[2] = np.broadcast_to(alt[:, None, None], (L, L, L))
    return E


def run(L, nloops, nbins, s, excl=0):
    seed(s)
    E = initial(L)
    H = np.zeros((L, L, L))
    for _ in range(max(nloops // 20, 50)):
        worm_hist(E, L, H, excl)
    Hb = np.zeros((nbins, L, L, L))
    W2b = np.zeros(nbins)
    per = nloops // nbins
    for b in range(nbins):
        for _ in range(per):
            worm_hist(E, L, Hb[b], excl)
            W = np.array([E[0, 0].sum(), E[1, :, 0].sum(), E[2, :, :, 0].sum()], float)
            W2b[b] += (W ** 2).mean()
        W2b[b] /= per
    return Hb, W2b


def green(L):
    k = 2 * np.pi * np.arange(L) / L
    s2 = 2 - 2 * np.cos(k)
    tot = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
    inv = np.zeros_like(tot)
    inv[tot > 0] = 1 / tot[tot > 0]
    G = np.real(np.fft.ifftn(inv))
    return G - G[0, 0, 0]


def ratios(Hb, L, pts, ref=(1, 0, 0)):
    nb = len(Hb)
    Ht = Hb.sum(0)
    G = green(L)
    N = L ** 3
    K = (2 * N + 1) / (3 * N)
    out = {}
    for p in pts:
        dV = -np.log(Ht[p] / Ht[ref])
        jk = np.array([-np.log((Ht[p] - Hb[b][p]) / (Ht[ref] - Hb[b][ref])) for b in range(nb)])
        err = np.sqrt((nb - 1) / nb * ((jk - jk.mean()) ** 2).sum())
        pred = K * 4 * (G[ref] - G[p])
        out[p] = (dV / pred, err / pred, dV)
    return out


# ---------------------------------------------------------------- A. exact L = 2
print("== A. The exact L = 2 torus ==")


def lid(i, x, y, z):
    return i * 8 + ((x % 2) * 4 + (y % 2) * 2 + (z % 2))


V2 = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
outs = [[lid(0, *v), lid(1, *v), lid(2, *v)] for v in V2]
ins = [[lid(0, v[0] - 1, v[1], v[2]), lid(1, v[0], v[1] - 1, v[2]), lid(2, v[0], v[1], v[2] - 1)] for v in V2]
counts = {}
nice = 0
for c in range(16):
    idx = np.arange(c << 20, (c + 1) << 20, dtype=np.int64)
    bits = (((idx[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int8)
    div = np.stack([bits[:, o].sum(1) - bits[:, b].sum(1) for o, b in zip(outs, ins)], axis=1)
    nice += int((div == 0).all(1).sum())
    sel = ((div == 2).sum(1) == 1) & ((div == -2).sum(1) == 1) & ((div == 0).sum(1) == 6)
    h = np.argmax(div[sel] == 2, axis=1)
    t = np.argmax(div[sel] == -2, axis=1)
    for hh, tt in zip(h, t):
        d = tuple(int(x) for x in (np.array(V2[hh]) - np.array(V2[tt])) % 2)
        counts[d] = counts.get(d, 0) + 1
tot = sum(counts.values())
check("all 2^24 arrow patterns give 9600 ice configurations and the two-defect counts at the seven displacements",
      nice == 9600 and len(counts) == 7 and (0, 0, 0) not in counts,
      f"{tot} two-defect patterns: " + ", ".join(f"{''.join(map(str, d))}: {counts[d]}" for d in sorted(counts)))
Hb2, W2b2 = run(2, 400000, 20, 20260923)
H2 = Hb2.sum(0)
fr = {d: H2[d] / H2.sum() for d in counts}
fe = {d: np.std([Hb2[b][d] / Hb2[b].sum() for b in range(20)], ddof=1) / np.sqrt(20) for d in counts}
zmax = max(abs(fr[d] - counts[d] / tot) / fe[d] for d in counts)
w2, w2e = W2b2.mean(), W2b2.std(ddof=1) / np.sqrt(20)
check("the backtracking worm reproduces the normalised exact counts at all seven displacements and <W^2> = 76/25, within 4 standard errors",
      zmax < 4 and abs(w2 - 76 / 25) < 4 * w2e, f"largest {zmax:.2f} standard errors; <W^2> {w2:.4f} +- {w2e:.4f}")
Hx, _ = run(2, 400000, 20, 20260926, excl=1)
Hx2 = Hx.sum(0)
zx = max(abs(Hx2[d] / Hx2.sum() - counts[d] / tot)
         / (np.std([Hx[b][d] / Hx[b].sum() for b in range(20)], ddof=1) / np.sqrt(20)) for d in counts)
check("the loop worm that never reverses the arrow just reversed reproduces the same counts within 4 standard errors",
      zx < 4, f"largest {zx:.2f} standard errors")
print()

# ---------------------------------------------------------------- C. L = 8
Hb8, _ = run(8, 2000000, 20, 20260924)
pts8 = [(1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 1, 0), (2, 2, 0), (3, 0, 0), (2, 2, 2), (4, 0, 0), (4, 4, 0), (4, 4, 4)]
r8 = ratios(Hb8, 8, pts8)
print("== C. L = 8, 2 x 10^6 worms ==")
check("relative to the nearest pair, measured over predicted lies in [0.88, 1.02] at every sampled separation, errors <= 0.025, and the pair attracts",
      all(0.88 <= v[0] <= 1.02 and v[1] <= 0.025 for v in r8.values()) and r8[(4, 4, 4)][2] > r8[(2, 0, 0)][2] > 0,
      ", ".join(f"{p}: {v[0]:.3f}+-{v[1]:.3f}" for p, v in r8.items()))
print()

# ---------------------------------------------------------------- D. L = 16
Hb16, _ = run(16, 1000000, 20, 20260925)
pts16 = [(r, 0, 0) for r in range(2, 9)]
r16 = ratios(Hb16, 16, pts16)
print("== D. L = 16, 10^6 worms ==")
check("along the axis, r = 2 to 8, measured over predicted lies in [0.85, 1.05], errors <= 0.04",
      all(0.85 <= v[0] <= 1.05 and v[1] <= 0.04 for v in r16.values()),
      ", ".join(f"{p[0]}: {v[0]:.3f}+-{v[1]:.3f}" for p, v in r16.items()))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
