#!/usr/bin/env python3
"""Cubic ice on the L = 16 torus: the smallest wavevectors sit above the continuous sum-rule calibration.

Uniform ice and the Gaussian comparison are supplied mathematical models, as
in landed PR 8881; every number here is a finite diagnostic of the stated
sampling. K_L below is the continuous zero-mode calibration K_cont =
(2N+1)/(3N) of landed PR 8881, and c_W is its discrete winding fit.

Because E_z^2 = 1 on every link, the covariance S_zz(q) = (1/N)|E_z(q)|^2
sums to N over the zone in every configuration; with P_zz the transverse
projector this makes the P_zz-weighted mean of r = K_L S_zz / P_zz, with the
zero mode at weight 1, equal to 1 exactly. Every estimate is the batch ratio
K_L sum S_zz / sum P_zz over a set of wavevectors, formed within each of 40
batches, with a binned standard error from their spread. A Gaussian of
stiffness K gives r = K_L / K, so c = K_L / (2r) is the stiffness a set
implies. Binned errors are descriptive; no mixing bound or thermodynamic
extrapolation is asserted.

Checks:

A. The exact L = 2 torus: 9600 configurations, 880 at zero flux, 125
   winding sectors, <W^2> = 76/25; the loop sampler reproduces <W^2>
   within 4 standard errors.
B. On L = 16 with 10^6 loops every batch obeys the identity, and the 24
   smallest wavevectors (|k|^2 at most 3 units, P_zz > 0.05) imply a
   stiffness c = K_L / (2r) 0.1% to 0.5% above K_L / 2, by more than 5
   binned standard errors.
C. The discrete winding fit also lies above K_L / 2, by more than 2
   standard errors and within 1%. Its batch-by-batch difference to the
   smallest wavevectors is printed and not claimed.
D. In nine shells of Q = sum 2(1 - cos k) the ratio rises from the innermost
   shell to the outermost by more than 10 standard errors; the inner half
   of the zone (Q < 6) lies below 1 and the outer half above 1, each by
   more than 20 standard errors.

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

# ---------------------------------------------------------------- B-D. L = 16
L, nl, nb = 16, 1000000, 40
E, W2b, _, Sb, _ = sample(L, nl, nb, 1616 + L, 1)
N = L ** 3
P = projector(L)
KL = (2 * N + 1) / (3 * N)
k = 2 * np.pi * np.arange(L) / L
Q = sum(np.meshgrid(*(3 * [2 - 2 * np.cos(k)]), indexing="ij"))
fold = np.minimum(np.arange(L), L - np.arange(L))
F2 = sum(np.meshgrid(*(3 * [fold ** 2]), indexing="ij"))


def ratio(mask):
    rb = KL * Sb[:, mask].sum(1) / P[mask].sum()
    return rb, rb.mean(), rb.std(ddof=1) / np.sqrt(nb)


print("== B. The long-wavelength stiffness on L = 16 ==")
dev = np.abs(Sb.reshape(nb, -1).sum(1) - N).max()
check("every batch obeys the unit-field sum rule: the structure factor sums to N over the zone",
      dev < 1e-8, f"{nb} batches of {nl // nb} worms; largest deviation {dev:.1e}")
small = (F2 <= 3) & (P > 0.05)
rSb, rS, rSe = ratio(small)
cS, cSe = KL / (2 * rS), KL / (2 * rS) * rSe / rS
cL = KL / 2
check("the smallest wavevectors give a stiffness 0.1% to 0.5% above the torus sum-rule value K_L/2, by more than 5 standard errors",
      (cS - cL) > 5 * cSe and 0.001 < cS / cL - 1 < 0.005,
      f"{small.sum()} wavevectors, K_L S_zz / P_zz = {rS:.5f} +- {rSe:.5f}; c = {cS:.5f} +- {cSe:.5f} against K_L/2 = {cL:.6f}: "
      f"{(cS / cL - 1) * 100:+.2f}%, {(cS - cL) / cSe:.1f} standard errors ({(3 * cS - 1) * 100:+.2f}% from 1/3)")
print()

print("== C. The winding ==")
cWb = np.array([K_from_W2(w, L) / 2 for w in W2b])
cW, cWe = K_from_W2(W2b.mean(), L) / 2, cWb.std(ddof=1) / np.sqrt(nb)
dd = cWb - KL / (2 * rSb)
dm, de = dd.mean(), dd.std(ddof=1) / np.sqrt(nb)
check("the winding stiffness also lies above the torus sum-rule value, by more than 2 standard errors and within 1%",
      (cW - cL) > 2 * cWe and cW / cL - 1 < 0.01,
      f"c_W = {cW:.5f} +- {cWe:.5f}, {(cW / cL - 1) * 100:+.2f}%; batch difference to the smallest wavevectors "
      f"c_W - c = {dm:+.5f} +- {de:.5f} (printed, not claimed)")
print()

print("== D. The zone profile ==")
edges = [0, 0.8, 1.6, 3, 4.5, 6, 7.5, 9, 10.5, 12.5]
shells = [ratio((Q > 0) & (Q >= a) & (Q < b)) for a, b in zip(edges[:-1], edges[1:])]
_, rin, rine = ratio((Q > 0) & (Q < 6))
_, rout, route = ratio(Q >= 6)
rise = shells[-1][1] - shells[0][1]
check("the ratio rises from the innermost shell to the outermost by more than 10 standard errors, "
      "the inner half of the zone lies below 1 and the outer half above 1, each by more than 20 standard errors",
      rise > 10 * np.hypot(shells[-1][2], shells[0][2]) and (1 - rin) > 20 * rine and (rout - 1) > 20 * route,
      "shells " + ", ".join(f"{s[1]:.4f} +- {s[2]:.4f}" for s in shells) + f"; inner {rin:.5f} +- {rine:.5f}, outer {rout:.5f} +- {route:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
