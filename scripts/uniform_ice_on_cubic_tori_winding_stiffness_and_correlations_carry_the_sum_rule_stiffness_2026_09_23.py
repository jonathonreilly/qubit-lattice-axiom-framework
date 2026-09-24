#!/usr/bin/env python3
"""Uniform ice on cubic tori: winding stiffness and correlations carry the sum-rule stiffness.

Uniform ice occupies three of the six links at every vertex of the cubic
lattice, so the staggered link field E = (-1)^(x+y+z) (2v - 1) = +-1 is
divergence-free. Open PR 8871 found on infinite prisms of small cross-section
that a Gaussian divergence-free field with one stiffness K fixed by the sum
rule <E^2> = 1 predicts both the flux cost and the correlations. The Gaussian
reading's large-section value is K = 2/3, c = 1/3. This runner tests that
value on L x L x L tori well beyond the reach of transfer matrices.

The sampler is a worm on the divergence-free arrows. It starts at a uniformly
random vertex, reverses one of the three outgoing arrows (never the one just
reversed) at every step, and stops when it returns to the start. Every step
has probability 1/3 forward and backward, so it samples the uniform measure
on all ice configurations of the torus, winding sectors included.

On the torus the Gaussian field gives the winding W_i (the flux through a
plane normal to i) the weight exp(-K W^2 / (2L)) on W in 2Z, and the
equal-time correlation S_zz(k) = P_zz(k) / K at k != 0, with
P_zz = 1 - s_z^2 / (s_x^2 + s_y^2 + s_z^2) and s_i^2 = 2 - 2 cos k_i. The sum
rule <E_z^2> = 1 fixes K_L = (1/N) (sum_{k != 0} P_zz(k) + 1), which tends to
2/3.

Checks:

A. The exact L = 2 torus: all 2^24 arrow patterns give 9600 ice
   configurations, 880 of them at zero flux, in 125 winding sectors, with
   <W^2> = 76/25 per direction. The worm reproduces <W^2> and the
   zero-flux fraction within 4 standard errors and visits every sector.
B. The winding stiffness. By cubic symmetry the projector's trace 2 is
   shared equally by the three directions, so the sum-rule stiffness is
   K_L = 2/3 + 1/(3N) exactly. On L = 8, 12, 16 and 24 the stiffness
   c_W = K_W / 2, inverted from <W^2> through the discrete Gaussian, agrees
   with the sum-rule value K_L / 2 within 1%. Combined over L = 12, 16 and
   24 it lies within 1% of 1/3 (0.3352 +- 0.0008, 0.56% above).
C. The correlations on L = 8 with 10^6 worms. Grouped into the 70 symmetry
   classes with P_zz > 0.05, K_L S_zz / P_zz agrees with 1 within 1% in
   every class. The deviations are systematic, not noise: the smallest
   wavevectors lie below 1 (r = 0.9966 +- 0.0004), and the stiffness they
   imply, K_L / (2r) = 0.3348, agrees with the winding value within 2
   standard errors.
D. The longitudinal null. S_zz vanishes at k = (0, 0, k_z != 0), and the
   divergence stays zero at every vertex after sampling.

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

# ---------------------------------------------------------------- B-D. large tori
defects = 0
wind = {}
for L, nl in ((8, 200000), (12, 200000), (16, 200000), (24, 60000)):
    E, W2b, _, _, _ = sample(L, nl, 20, 20260923 + L, 0)
    defects += divergence_defects(E, L)
    P = projector(L)
    KL = (P.sum() + 1) / L ** 3
    w2, w2e = W2b.mean(), W2b.std(ddof=1) / np.sqrt(len(W2b))
    KW = K_from_W2(w2, L)
    wind[L] = dict(cW=KW / 2, dc=abs(K_from_W2(w2 + w2e, L) - KW) / 2, cL=KL / 2, KL=KL)
big = [12, 16, 24]
wts = np.array([1 / wind[L]["dc"] ** 2 for L in big])
c_comb = float(sum(wind[L]["cW"] * w for L, w in zip(big, wts)) / wts.sum())
c_comb_e = float(1 / np.sqrt(wts.sum()))

print("== B. The winding stiffness ==")
check("the sum-rule stiffness is K_L = 2/3 + 1/(3N) exactly: the projector's trace 2 is shared equally by the three directions",
      all(abs(v["KL"] - float(Fraction(2 * L ** 3 + 1, 3 * L ** 3))) < 1e-12 for L, v in wind.items()),
      ", ".join(f"L={L}: {v['KL']:.6f}" for L, v in wind.items()))
check("c_W from <W^2> agrees with the sum-rule value K_L/2 within 1% on L = 8, 12, 16 and 24",
      all(abs(v["cW"] / v["cL"] - 1) < 0.01 for v in wind.values()),
      ", ".join(f"L={L}: {v['cW']:.4f} +- {v['dc']:.4f} (K_L/2 {v['cL']:.4f})" for L, v in wind.items()))
check("the combined value on L = 12, 16, 24 lies within 1% of 1/3",
      abs(c_comb * 3 - 1) < 0.01, f"c_W = {c_comb:.4f} +- {c_comb_e:.4f}, {(c_comb * 3 - 1) * 100:+.2f}% from 1/3")
print()

# ---------------------------------------------------------------- C. correlations on L = 8
L = 8
E, _, _, Sb, _ = sample(L, 1000000, 40, 777 + L, 1)
defects += divergence_defects(E, L)
P = projector(L)
KL = (P.sum() + 1) / L ** 3
S = Sb.mean(0)
Se = Sb.std(0, ddof=1) / np.sqrt(len(Sb))
nullmax = float(S[0, 0, 1:].max())
f = lambda m: min(m, L - m)
classes = {}
for a in range(L):
    for b in range(L):
        for c in range(L):
            if P[a, b, c] > 0.05:
                classes.setdefault((tuple(sorted((f(a), f(b)))), f(c)), []).append((a, b, c))
cl = {}
for key, pts in classes.items():
    r = np.array([KL * S[q] / P[q] for q in pts])
    re = np.array([KL * Se[q] / P[q] for q in pts])
    w = 1 / re ** 2
    cl[key] = ((r * w).sum() / w.sum(), 1 / np.sqrt(w.sum()))
worst = max(cl, key=lambda k: abs(cl[k][0] - 1))
small = [k for k in cl if k[0][0] ** 2 + k[0][1] ** 2 + k[1] ** 2 <= 3]
ws = np.array([1 / cl[k][1] ** 2 for k in small])
r_small = float(sum(cl[k][0] * w for k, w in zip(small, ws)) / ws.sum())
r_small_e = float(1 / np.sqrt(ws.sum()))
c_small = KL / (2 * r_small)
c_small_e = c_small * r_small_e / r_small

print("== C. The correlations on L = 8, 10^6 worms ==")
check("K_L S_zz / P_zz agrees with 1 within 1% in every symmetry class with P_zz > 0.05",
      abs(cl[worst][0] - 1) < 0.01,
      f"{len(cl)} classes; largest deviation {(cl[worst][0] - 1) * 100:+.2f}% +- {cl[worst][1] * 100:.2f}% at k = {worst[0] + (worst[1],)} 2pi/8")
check("the smallest wavevectors lie below 1, and their stiffness K_L / (2 r) agrees with the winding value within 2 standard errors",
      r_small < 1 and abs(c_small - c_comb) < 2 * np.hypot(c_small_e, c_comb_e),
      f"r = {r_small:.4f} +- {r_small_e:.4f} over {len(small)} classes; c = {c_small:.4f} +- {c_small_e:.4f} vs winding {c_comb:.4f}")
print()

print("== D. The longitudinal null and the divergence ==")
check("S_zz vanishes at k = (0, 0, k_z != 0) and no vertex carries divergence after sampling",
      nullmax < 1e-20 and defects == 0, f"largest {nullmax:.1e}, defects {defects}")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
