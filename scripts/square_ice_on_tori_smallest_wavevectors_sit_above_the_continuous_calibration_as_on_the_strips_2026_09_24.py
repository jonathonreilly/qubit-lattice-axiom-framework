#!/usr/bin/env python3
"""Square ice on L x L tori: the smallest wavevectors sit above the continuous calibration, as on the strips.

Square ice (two of four links occupied at every vertex of the square lattice,
so that the staggered unit field E = +-1 is divergence-free) and every
Gaussian comparison below are supplied mathematical models; every number here
is a finite diagnostic of the stated sampling. Landed PR 8930 found the flux
cost of square ice on strips of width 4 to 20 between 4.1% and 4.7% above
the planar calibration, and landed PR 8954 gave the exact weighted identity
for its row correlations. Open PR 8968 set up the same identity and batch
ratios for cubic tori with a loop sampler. This runner samples square ice on
L x L tori with the planar loop sampler.

On the L x L torus, N = L^2. With s_i^2 = 2 - 2 cos q_i and Q = s_x^2 + s_y^2,
the transverse projector for E_y is P_yy = 1 - s_y^2 / Q; its sum over q != 0
is (N - 1)/2, so a Gaussian with a continuous zero mode has unit variance at
K_cont = (N + 1)/(2N). Because E_y^2 = 1 on every link, S_yy(q) =
(1/N)|E_y(q)|^2 sums to N over the zone in every configuration, and the
P_yy-weighted mean of r = K_cont S_yy / P_yy, with the zero mode at weight 1,
equals 1 exactly. Every estimate is the batch ratio K_cont sum S_yy / sum P_yy
over a set of wavevectors, formed within each of 40 batches, with a binned
standard error from their spread; c = K_cont / (2r) is the stiffness a set
implies. The discrete winding fit c_W = K_W / 2 reproduces <W^2> under weights
exp(-K W^2 / 2) on W = -L, -L + 2, ..., L. Binned errors are descriptive; no
mixing bound or thermodynamic extrapolation is asserted.

Checks:

A. The exact L = 2 torus: 18 configurations, 6 at zero flux, 9 winding
   sectors, <W^2> = 16/9; the loop sampler reproduces <W^2> within 4
   standard errors.
B. On L = 32, 64 and 128 (10^6 loops each; the spectrum after every loop,
   every second loop on L = 128) every batch obeys the identity,
   and the smallest wavevectors (|k|^2 at most 2 units, P_yy > 0.05) imply a
   stiffness 3% to 6% above K_cont / 2 on each torus, by more than 10 binned
   standard errors.
C. The discrete winding fit also lies 3% to 6% above K_cont / 2 on each
   torus; its batch-by-batch difference to the smallest wavevectors is
   printed and not claimed.
D. On L = 128 the ratio rises from the innermost of eight shells of Q to the
   outermost by more than 5%, and the outer half of the zone (Q >= 4) lies
   above 1 by more than 20 standard errors.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
import time
from fractions import Fraction

import numpy as np
from numba import njit

AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/SQUARE_ICE_ON_TORI_SMALLEST_WAVEVECTORS_SIT_ABOVE_THE_CONTINUOUS_CALIBRATION_AS_ON_THE_STRIPS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ICE_UNIT_FIELD_SUM_RULE_IS_TEN_TIMES_CLOSER_IN_THREE_DIMENSIONS_THAN_IN_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/SQUARE_ICE_IS_GAUSSIAN_AT_LONG_WAVELENGTH_AND_A_ZONE_BOUNDARY_EXCESS_MAKES_THE_SUM_RULE_MISS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/CUBIC_ICE_LONG_WAVELENGTH_STIFFNESS_LIES_MEASURABLY_ABOVE_THE_UNIT_FIELD_SUM_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/CUBIC_ICE_LONG_WAVELENGTH_STIFFNESS_STAYS_ABOVE_THE_SUM_RULE_FROM_L12_TO_L24_BOUNDED_THEOREM_NOTE_2026-09-24.md')

T0 = time.time()
PASS = FAIL = 0


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
    # E[i, x, y] = +1 when the link from r to r + e_i points forward
    x0 = np.random.randint(L)
    y0 = np.random.randint(L)
    x, y = x0, y0
    li, lx, ly = -1, -1, -1
    ci = np.empty(4, np.int64)
    cx = np.empty(4, np.int64)
    cy = np.empty(4, np.int64)
    cd = np.empty(4, np.int64)
    n = 0
    while True:
        m = 0
        for i in range(2):
            if E[i, x, y] == 1 and not (li == i and lx == x and ly == y):
                ci[m] = i
                cx[m] = x
                cy[m] = y
                cd[m] = 1
                m += 1
            bx, by = x, y
            if i == 0:
                bx = (x - 1) % L
            else:
                by = (y - 1) % L
            if E[i, bx, by] == -1 and not (li == i and lx == bx and ly == by):
                ci[m] = i
                cx[m] = bx
                cy[m] = by
                cd[m] = -1
                m += 1
        k = np.random.randint(m)
        i = ci[k]
        bx = cx[k]
        by = cy[k]
        E[i, bx, by] = -E[i, bx, by]
        li, lx, ly = i, bx, by
        if cd[k] == 1:
            if i == 0:
                x = (x + 1) % L
            else:
                y = (y + 1) % L
        else:
            x, y = bx, by
        n += 1
        if x == x0 and y == y0:
            return n


def divergence(E):
    return int(np.abs(E[0] - np.roll(E[0], 1, 0) + E[1] - np.roll(E[1], 1, 1)).sum())


def initial(L):
    # zero-winding ice: E_x alternates along y, E_y alternates along x
    E = np.empty((2, L, L), np.int8)
    alt = ((-1) ** np.arange(L)).astype(np.int8)
    E[0] = alt[None, :]
    E[1] = alt[:, None]
    return E


def windings(E):
    return np.array([E[0][0, :].sum(), E[1][:, 0].sum()], dtype=np.int64)


def projector(L):
    k = 2 * np.pi * np.arange(L) / L
    s2 = 2 - 2 * np.cos(k)
    Q = s2[:, None] + s2[None, :]
    P = np.zeros((L, L))
    nz = Q > 0
    P[nz] = 1 - np.broadcast_to(s2[None, :], Q.shape)[nz] / Q[nz]
    return P, Q


def K_from_W2(w2, L):
    Ws = np.arange(-L, L + 1, 2, dtype=float)
    lo, hi = 1e-3, 20.0
    for _ in range(200):
        K = 0.5 * (lo + hi)
        wts = np.exp(-K * Ws ** 2 / 2 + (K * Ws ** 2 / 2).min())
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
    Sb = np.zeros((nbins, L, L))
    sectors = set()
    N = L * L
    for b in range(nbins):
        for t in range(per):
            worm(E, L)
            W = windings(E)
            W2b[b] += (W ** 2).mean()
            if L == 2:
                sectors.add(tuple(W))
            if t % every == 0:
                Sb[b] += np.abs(np.fft.fft2(E[1].astype(float))) ** 2 / N
        W2b[b] /= per
        Sb[b] /= len(range(0, per, every))
    return E, W2b, Sb, sectors


# ---------------------------------------------------------------- A. exact L = 2
print("== A. The exact L = 2 torus ==")
cnt = z0 = 0
w2 = Fraction(0)
secs = set()
for idx in range(256):
    E2 = (np.array([(idx >> b) & 1 for b in range(8)], dtype=np.int8).reshape(2, 2, 2) * 2 - 1).astype(np.int8)
    if divergence(E2) == 0:
        cnt += 1
        W = windings(E2)
        secs.add(tuple(W))
        w2 += Fraction(int((W ** 2).sum()), 2)
        z0 += int((W == 0).all())
w2 /= cnt
check("all 2^8 arrow patterns give 18 ice configurations, 6 at zero flux, in 9 winding sectors, <W^2> = 16/9",
      (cnt, z0, len(secs), w2) == (18, 6, 9, Fraction(16, 9)), f"{cnt}, {z0}, {len(secs)}, {w2}")
E2s, W2s, _, sec2 = sample(2, 200000, 40, 22)
m2, e2 = W2s.mean(), W2s.std(ddof=1) / np.sqrt(len(W2s))
check("the loop sampler reproduces <W^2> within 4 standard errors and visits all 9 sectors",
      abs(m2 - 16 / 9) < 4 * e2 and len(sec2) == 9 and divergence(E2s) == 0,
      f"<W^2> {m2:.4f} +- {e2:.4f} vs {16 / 9:.4f}; sectors {len(sec2)}")
print()

# ---------------------------------------------------------------- B-D. L = 32, 64, 128
nb = 40


def measure(L, nl, s, every):
    E, W2b, Sb, _ = sample(L, nl, nb, s, every)
    N = L * L
    P, Q = projector(L)
    KL = (N + 1) / (2 * N)
    fold = np.minimum(np.arange(L), L - np.arange(L))
    F2 = fold[:, None] ** 2 + fold[None, :] ** 2

    def ratio(mask):
        rb = KL * Sb[:, mask].sum(1) / P[mask].sum()
        return rb, rb.mean(), rb.std(ddof=1) / np.sqrt(nb)

    rSb, rS, rSe = ratio((F2 <= 2) & (P > 0.05))
    c, ce, cL = KL / (2 * rS), KL / (2 * rS) * rSe / rS, KL / 2
    cWb = np.array([K_from_W2(w, L) / 2 for w in W2b])
    cW = K_from_W2(W2b.mean(), L) / 2
    dd = cWb - KL / (2 * rSb)
    edges = [0, 0.5, 1, 2, 3, 4, 5, 6, 8.01]
    shells = [ratio((Q > 0) & (Q >= a) & (Q < b))[1:] for a, b in zip(edges[:-1], edges[1:])]
    return dict(dev=np.abs(Sb.reshape(nb, -1).sum(1) - N).max(), div=divergence(E), c=c, ce=ce, cL=cL,
                off=c / cL - 1, offe=ce / cL, cW=cW, cWe=cWb.std(ddof=1) / np.sqrt(nb), offW=cW / cL - 1,
                dm=dd.mean(), de=dd.std(ddof=1) / np.sqrt(nb), shells=shells, outer=ratio(Q >= 4)[1:])


res = {L: measure(L, 1000000, 3000 + L, 1 if L < 128 else 2) for L in (32, 64, 128)}

print("== B. The smallest wavevectors ==")
check("every batch obeys the unit-arrow identity and no vertex carries divergence on the three tori",
      all(v["dev"] < 1e-8 and v["div"] == 0 for v in res.values()),
      ", ".join(f"L={L}: {v['dev']:.1e}" for L, v in res.items()))
check("the smallest wavevectors imply a stiffness 3% to 6% above K_cont/2 on each torus, by more than 10 standard errors",
      all(0.03 < v["off"] < 0.06 and v["off"] > 10 * v["offe"] for v in res.values()),
      "; ".join(f"L={L}: c = {v['c']:.5f} +- {v['ce']:.5f}, {v['off'] * 100:+.2f}% +- {v['offe'] * 100:.2f}%"
                for L, v in res.items()))
print()

print("== C. The discrete winding fit ==")
check("the winding fit also lies 3% to 6% above K_cont/2 on each torus",
      all(0.03 < v["offW"] < 0.06 for v in res.values()),
      "; ".join(f"L={L}: c_W = {v['cW']:.5f} +- {v['cWe']:.5f}, {v['offW'] * 100:+.2f}%, "
                f"c_W - c = {v['dm']:+.5f} +- {v['de']:.5f} (printed, not claimed)" for L, v in res.items()))
print()

print("== D. The zone profile on L = 128 ==")
sh = res[128]["shells"]
ro, roe = res[128]["outer"]
check("the ratio rises from the innermost shell to the outermost by more than 5%, and the outer half lies above 1 by more than 20 standard errors",
      sh[-1][0] - sh[0][0] > 0.05 and (ro - 1) > 20 * roe,
      "shells " + ", ".join(f"{m:.4f}" for m, e in sh) + f"; outer half {ro:.5f} +- {roe:.5f}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
