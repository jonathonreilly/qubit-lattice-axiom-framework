#!/usr/bin/env python3
"""Cubic ice on L = 16: the small-wavevector covariance keeps the transverse angular form.

Uniform ice and the Gaussian comparison are supplied mathematical models, as
in landed PR 8881; every number here is a finite diagnostic of the stated
sampling. Landed PR 8968 found that the smallest wavevectors of the unit-arrow
covariance on the L = 16 torus imply a Gaussian stiffness 0.29% above half
the continuous calibration K_cont = (2N+1)/(3N), and landed PR 8984 found the
same offset on L = 12 and L = 24. Its reading as one stiffness assumes the
covariance keeps the transverse form S_zz = P_zz / K at small wavevectors,
with P_zz = 1 - s_z^2 / Q. This runner tests that angular form directly.

Wavevectors whose folded components are the same multiset {a, b, c} have the
same Q = sum 2(1 - cos k_i) exactly, but different P_zz according to which
component lies along z. Under the transverse form the batch ratio
r = K_cont sum S_zz / sum P_zz is the same for every assignment. With four
fresh seeds of 10^6 loops each (160 batches), the runner compares the
assignment with the largest P_zz against the one with the smallest, over the
five multisets with |k|^2 at most 9 units that have two usable assignments.
Binned errors are descriptive; no mixing bound or thermodynamic
extrapolation is asserted.

Checks:

A. The exact L = 2 torus: 9600 configurations, 880 at zero flux, 125
   winding sectors, <W^2> = 76/25; the loop sampler reproduces <W^2> within
   4 standard errors (as in landed PR 8968).
B. Every batch obeys the unit-arrow identity, and the 24 smallest
   wavevectors imply a stiffness 0.1% to 0.5% above K_cont / 2 by more than
   5 binned standard errors: landed PR 8968's offset, with independent seeds.
C. Permuted wavevector sets share Q exactly (to 1e-12), and every multiset
   has at least two assignments with P_zz > 0.05.
D. For each of the five multisets the ratio difference between the smallest
   and largest P_zz lies within 3 binned standard errors of zero, and their
   mean lies within 3 standard errors of zero and below 0.1% in magnitude.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""

AUDIT_TIMEOUT_SEC = 3600
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
def worm(E, L):
    # E[i, x, y, z] = +1 when the link from r to r + e_i points forward
    x0 = np.random.randint(L)
    y0 = np.random.randint(L)
    z0 = np.random.randint(L)
    x, y, z = x0, y0, z0
    li, lx, ly, lz = -1, -1, -1, -1
    ci = np.empty(6, np.int64)
    cx = np.empty(6, np.int64)
    cy = np.empty(6, np.int64)
    cz = np.empty(6, np.int64)
    cd = np.empty(6, np.int64)
    n = 0
    while True:
        m = 0
        for i in range(3):
            if E[i, x, y, z] == 1 and not (li == i and lx == x and ly == y and lz == z):
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
            if E[i, bx, by, bz] == -1 and not (li == i and lx == bx and ly == by and lz == bz):
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


@njit(cache=False)
def divergence_defects(E, L):
    bad = 0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                d = (E[0, x, y, z] - E[0, (x - 1) % L, y, z] + E[1, x, y, z] - E[1, x, (y - 1) % L, z]
                     + E[2, x, y, z] - E[2, x, y, (z - 1) % L])
                if d != 0:
                    bad += 1
    return bad


def initial(L):
    # zero-winding ice: E_x alternates along y, E_y along z, E_z along x
    E = np.empty((3, L, L, L), np.int8)
    alt = (-1) ** np.arange(L)
    E[0] = np.broadcast_to(alt[None, :, None], (L, L, L))
    E[1] = np.broadcast_to(alt[None, None, :], (L, L, L))
    E[2] = np.broadcast_to(alt[:, None, None], (L, L, L))
    return E


def windings(E):
    return np.array([E[0, 0].sum(), E[1, :, 0].sum(), E[2, :, :, 0].sum()], dtype=np.int64)


def projector(L):
    k = 2 * np.pi * np.arange(L) / L
    s2 = 2 - 2 * np.cos(k)
    tot = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
    P = np.zeros((L, L, L))
    nz = tot > 0
    P[nz] = 1 - (np.broadcast_to(s2[None, None, :], tot.shape)[nz] / tot[nz])
    return P


def K_from_W2(w2, L):
    Ws = np.arange(-L * L, L * L + 1, 2, dtype=float)
    lo, hi = 1e-3, 20.0
    for _ in range(200):
        K = 0.5 * (lo + hi)
        wts = np.exp(-K * Ws ** 2 / (2 * L) + (K * Ws ** 2 / (2 * L)).min())
        if (Ws ** 2 * wts).sum() / wts.sum() > w2:
            lo = K
        else:
            hi = K
    return 0.5 * (lo + hi)


def sample(L, nloops, nbins, s, every=1):
    seed(s)
    E = initial(L)
    for _ in range(max(nloops // 20, 50)):
        worm(E, L)
    per = nloops // nbins
    W2b = np.zeros(nbins)
    Z0b = np.zeros(nbins)
    Sb = np.zeros((nbins, L, L, L))
    sectors = set()
    N = L ** 3
    for b in range(nbins):
        ns = 0
        for t in range(per):
            worm(E, L)
            W = windings(E)
            W2b[b] += (W ** 2).mean()
            Z0b[b] += float((W == 0).all())
            if L == 2:
                sectors.add(tuple(W))
            if every and t % every == 0:
                F = np.fft.fftn(E[2].astype(float))
                Sb[b] += np.abs(F) ** 2 / N
                ns += 1
        W2b[b] /= per
        Z0b[b] /= per
        Sb[b] /= max(ns, 1)
    return E, W2b, Z0b, Sb, sectors


# ---------------------------------------------------------------- A. exact L = 2
print("== A. The exact L = 2 torus ==")
L2 = 2


def lid(i, x, y, z):
    return i * 8 + ((x % 2) * 4 + (y % 2) * 2 + (z % 2))


outs = [[lid(0, x, y, z), lid(1, x, y, z), lid(2, x, y, z)] for x in range(2) for y in range(2) for z in range(2)]
ins = [[lid(0, x - 1, y, z), lid(1, x, y - 1, z), lid(2, x, y, z - 1)] for x in range(2) for y in range(2) for z in range(2)]
wl = [[lid(0, 0, y, z) for y in range(2) for z in range(2)], [lid(1, x, 0, z) for x in range(2) for z in range(2)],
      [lid(2, x, y, 0) for x in range(2) for y in range(2)]]
count = zero = 0
w2sum = 0
sec = {}
for c in range(16):
    idx = np.arange(c << 20, (c + 1) << 20, dtype=np.int64)
    bits = (((idx[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int8)
    ok = np.ones(len(idx), bool)
    for o, b in zip(outs, ins):
        ok &= bits[:, o].sum(1) == bits[:, b].sum(1)
    g = bits[ok]
    Ws = np.stack([g[:, w].sum(1) for w in wl], axis=1).astype(np.int64)
    count += len(g)
    zero += int((Ws == 0).all(1).sum())
    w2sum += int((Ws ** 2).sum())
    for w in map(tuple, Ws):
        sec[w] = sec.get(w, 0) + 1
W2_exact = Fraction(w2sum, 3 * count)
check("all 2^24 arrow patterns give 9600 ice configurations, 880 at zero flux, in 125 winding sectors, <W^2> = 76/25",
      count == 9600 and zero == 880 and len(sec) == 125 and W2_exact == Fraction(76, 25),
      f"{count}, {zero}, {len(sec)}, {W2_exact}")
_, W2b, Z0b, _, visited = sample(2, 200000, 20, 20260923)
m, e = W2b.mean(), W2b.std(ddof=1) / np.sqrt(len(W2b))
mz, ez = Z0b.mean(), Z0b.std(ddof=1) / np.sqrt(len(Z0b))
check("the worm reproduces <W^2> and the zero-flux fraction within 4 standard errors and visits all 125 sectors",
      abs(m - 3.04) < 4 * e and abs(mz - 880 / 9600) < 4 * ez and len(visited) == 125,
      f"<W^2> {m:.4f} +- {e:.4f} vs 3.04; zero flux {mz:.5f} +- {ez:.5f} vs {880 / 9600:.5f}; sectors {len(visited)}")
print()

# ---------------------------------------------------------------- B-D. L = 16, four seeds
L, nl, nb = 16, 1000000, 40
SEEDS = (4001, 4002, 4003, 4004)
Sb = np.concatenate([sample(L, nl, nb, s, 1)[3] for s in SEEDS])
NB = len(Sb)
N = L ** 3
P = projector(L)
KL = (2 * N + 1) / (3 * N)
k = 2 * np.pi * np.arange(L) / L
s2 = 2 - 2 * np.cos(k)
Q = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
fold = np.minimum(np.arange(L), L - np.arange(L))
FX, FY, FZ = np.meshgrid(fold, fold, fold, indexing="ij")
F2 = FX ** 2 + FY ** 2 + FZ ** 2


def ratio(mask):
    rb = KL * Sb[:, mask].sum(1) / P[mask].sum()
    return rb


print("== B. The identity and the offset, four fresh seeds ==")
dev = np.abs(Sb.reshape(NB, -1).sum(1) - N).max()
check("every batch obeys the unit-arrow identity: the covariance sums to N over the zone",
      dev < 1e-8, f"{NB} batches of {nl // nb} loops from seeds {SEEDS}; largest deviation {dev:.1e}")
rS = ratio((F2 <= 3) & (P > 0.05))
r, re = rS.mean(), rS.std(ddof=1) / np.sqrt(NB)
c, ce, cL = KL / (2 * r), KL / (2 * r) * re / r, KL / 2
check("the smallest wavevectors imply a stiffness 0.1% to 0.5% above K_cont/2, by more than 5 standard errors",
      0.001 < c / cL - 1 < 0.005 and (c - cL) > 5 * ce,
      f"c = {c:.5f} +- {ce:.5f}, {(c / cL - 1) * 100:+.3f}%, {(c - cL) / ce:.1f} standard errors")
print()

print("== C. Permuted wavevector sets ==")
MS = [ms for ms in sorted({tuple(sorted((a, b, cc))) for a in range(4) for b in range(4) for cc in range(4)})
      if 0 < sum(x * x for x in ms) <= 9]
PAIRS, qdev = [], 0.0
for ms in MS:
    groups = {}
    for z in set(ms):
        rest = list(ms)
        rest.remove(z)
        m = (FZ == z) & (np.minimum(FX, FY) == min(rest)) & (np.maximum(FX, FY) == max(rest)) & (P > 0.05)
        if m.sum():
            groups[z] = (P[m].mean(), m)
    if len(groups) >= 2:
        allm = np.zeros_like(FZ, dtype=bool)
        for z, (pm, m) in groups.items():
            allm |= m
        qdev = max(qdev, float(Q[allm].max() - Q[allm].min()))
        hi = max(groups, key=lambda z: groups[z][0])
        lo = min(groups, key=lambda z: groups[z][0])
        PAIRS.append((ms, groups[hi][0], groups[lo][0], ratio(groups[lo][1]) - ratio(groups[hi][1])))
check("permuted wavevector sets share Q exactly, and five multisets have two usable assignments",
      qdev < 1e-12 and len(PAIRS) == 5,
      f"{len(PAIRS)} multisets: " + ", ".join(f"{p[0]} (P {p[1]:.3f} vs {p[2]:.3f})" for p in PAIRS) + f"; largest Q spread {qdev:.1e}")
print()

print("== D. The angular form ==")
diffs = [(p[3].mean(), p[3].std(ddof=1) / np.sqrt(NB)) for p in PAIRS]
Dm = np.mean([p[3] for p in PAIRS], axis=0)
dm, de = Dm.mean(), Dm.std(ddof=1) / np.sqrt(NB)
check("each multiset's ratio difference lies within 3 standard errors of zero; their mean within 3 and below 0.1%",
      all(abs(m) < 3 * e for m, e in diffs) and abs(dm) < 3 * de and abs(dm) < 0.001,
      "; ".join(f"{p[0]}: {m:+.4f} +- {e:.4f}" for p, (m, e) in zip(PAIRS, diffs)) + f"; mean {dm:+.5f} +- {de:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
