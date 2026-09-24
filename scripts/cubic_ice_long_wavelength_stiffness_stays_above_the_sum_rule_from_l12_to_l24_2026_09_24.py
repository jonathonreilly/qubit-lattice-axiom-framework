#!/usr/bin/env python3
"""Cubic ice on L = 12 and L = 24: the smallest wavevectors stay above the continuous calibration.

Uniform ice and the Gaussian comparison are supplied mathematical models, as
in landed PR 8881; every number here is a finite diagnostic of the stated
sampling. K_L below is the continuous zero-mode calibration K_cont =
(2N+1)/(3N) of landed PR 8881, and c_W is its discrete winding fit. Open PR
8968 found the smallest wavevectors on L = 16 0.29% above K_L / 2, at 6.0
binned standard errors. This runner measures L = 12 and L = 24 with the same
loop sampler and the same batch ratios K_L sum S_zz / sum P_zz, formed within
each of 40 batches, with binned standard errors from their spread. Binned
errors are descriptive; no mixing bound or thermodynamic extrapolation is
asserted.

Checks:

A. The exact L = 2 torus: 9600 configurations, 880 at zero flux, 125
   winding sectors, <W^2> = 76/25; the loop sampler reproduces <W^2>
   within 4 standard errors.
B. On L = 12 (10^6 loops) and L = 24 (5 x 10^5 loops) every batch obeys
   the unit-arrow identity, and the smallest wavevectors (|k|^2 at most 3
   units, P_zz > 0.05) imply a stiffness 0.1% to 0.5% above K_L / 2, by
   more than 3 binned standard errors on each torus.
C. The two offsets agree within 2 combined standard errors, and each
   discrete winding fit lies within 1% of K_L / 2. On which side it lies,
   and its batch-by-batch difference to the smallest wavevectors, are
   printed and not claimed.
D. On L = 24 the inner half of the zone (Q < 6) lies below 1 and the outer
   half above 1, each by more than 10 standard errors.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
import time
from fractions import Fraction

import numpy as np
from numba import njit

AUDIT_TIMEOUT_SEC = 1800

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

# ---------------------------------------------------------------- B-D. L = 12 and L = 24
nb = 40


def measure(L, nl, s):
    E, W2b, _, Sb, _ = sample(L, nl, nb, s, 1)
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

    small = (F2 <= 3) & (P > 0.05)
    rSb, rS, rSe = ratio(small)
    c, ce, cL = KL / (2 * rS), KL / (2 * rS) * rSe / rS, KL / 2
    cWb = np.array([K_from_W2(w, L) / 2 for w in W2b])
    dd = cWb - KL / (2 * rSb)
    return dict(dev=np.abs(Sb.reshape(nb, -1).sum(1) - N).max(), n=int(small.sum()), c=c, ce=ce, cL=cL,
                off=c / cL - 1, offe=ce / cL, cW=K_from_W2(W2b.mean(), L) / 2, cWe=cWb.std(ddof=1) / np.sqrt(nb),
                dm=dd.mean(), de=dd.std(ddof=1) / np.sqrt(nb),
                inner=ratio((Q > 0) & (Q < 6))[1:], outer=ratio(Q >= 6)[1:])


res = {12: measure(12, 1000000, 1212), 24: measure(24, 500000, 2424)}

print("== B. The long-wavelength stiffness on L = 12 and L = 24 ==")
check("every batch obeys the unit-field sum rule on both tori",
      all(v["dev"] < 1e-8 for v in res.values()),
      ", ".join(f"L={L}: largest deviation {v['dev']:.1e}" for L, v in res.items()))
check("the smallest wavevectors give a stiffness 0.1% to 0.5% above K_L/2, by more than 3 standard errors on each torus",
      all(0.001 < v["off"] < 0.005 and v["off"] > 3 * v["offe"] for v in res.values()),
      "; ".join(f"L={L}: {v['n']} wavevectors, c = {v['c']:.5f} +- {v['ce']:.5f} against K_L/2 = {v['cL']:.6f}, "
                f"{v['off'] * 100:+.2f}% +- {v['offe'] * 100:.2f}% ({v['off'] / v['offe']:.1f} standard errors)" for L, v in res.items()))
print()

print("== C. Size and winding ==")
o12, o24 = res[12], res[24]
check("the offsets on L = 12 and L = 24 agree within 2 combined standard errors",
      abs(o12["off"] - o24["off"]) < 2 * np.hypot(o12["offe"], o24["offe"]),
      f"difference {(o24['off'] - o12['off']) * 100:+.2f}% +- {np.hypot(o12['offe'], o24['offe']) * 100:.2f}%")
check("each discrete winding fit lies within 1% of K_L/2; its side and its difference to the smallest wavevectors are printed, not claimed",
      all(abs(v["cW"] / v["cL"] - 1) < 0.01 for v in res.values()),
      "; ".join(f"L={L}: c_W = {v['cW']:.5f} +- {v['cWe']:.5f}, {(v['cW'] / v['cL'] - 1) * 100:+.2f}%, "
                f"{(v['cW'] - v['cL']) / v['cWe']:.1f} standard errors; c_W - c = {v['dm']:+.5f} +- {v['de']:.5f}" for L, v in res.items()))
print()

print("== D. The zone profile on L = 24 ==")
(ri, rie), (ro, roe) = o24["inner"], o24["outer"]
check("the inner half of the zone lies below 1 and the outer half above 1, each by more than 10 standard errors",
      (1 - ri) > 10 * rie and (ro - 1) > 10 * roe,
      f"inner {ri:.5f} +- {rie:.5f}, outer {ro:.5f} +- {roe:.5f}; "
      f"on L = 12 inner {o12['inner'][0]:.5f} +- {o12['inner'][1]:.5f}, outer {o12['outer'][0]:.5f} +- {o12['outer'][1]:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
