#!/usr/bin/env python3
"""Uniform ice at the RK point: the photon's single-mode bound is quadratic with the sum-rule stiffness.

The landed cubic-ice notes supply a ring Hamiltonian on the ice configurations,
H(V) = D - A + (V - 1) N_f: A flips a flippable plaquette (all four arrows
circulating), D counts the flippable plaquettes. At V = 1, the RK point,
H = D - A is a graph Laplacian and the uniform superposition of ice
configurations is a ground state with energy 0. Its equal-time law is the
uniform ice measure studied by open PRs 8881 and 8890. This runner adopts no
Hamiltonian; it asks what the supplied one implies at V = 1.

Take O = E_z(k) / sqrt(N), with E_z the arrow field on the z links. For a
diagonal O, [O^+, [H, O]] = sum_p |Delta_p O|^2 T_p, where T_p flips p. An
xz or yz plaquette changes E_z on its two z links by -+2, so
|Delta_p O|^2 = 4 s_x^2 / N or 4 s_y^2 / N with s_i^2 = 2 - 2 cos k_i, and
the f-sum is <0|O^+ H O|0> = 2 n_f (s_x^2 + s_y^2), n_f the density of
flippable plaquettes. The single-mode bound says the lowest excitation at
momentum k has energy at most

    omega_SMA(k) = 2 n_f (s_x^2 + s_y^2) / S_zz(k).

With the Gaussian S_zz = P_zz / K, where P_zz = (s_x^2 + s_y^2) / |s|^2, the
bound is 2 n_f K |s|^2: quadratic in k.

Checks:

A. Exact L = 2 (all 9600 configurations): n_f = 13/60, and the f-sum
   <0|O^+ H O|0> equals 2 n_f (s_x^2 + s_y^2) exactly at all 8 wavevectors,
   with H = D - A built from every plaquette flip.
B. The worm reproduces n_f = 13/60 on L = 2 within 4 standard errors.
C. L = 8 with 10^6 worms: R(k) = omega_SMA(k) / (2 n_f K_L |s|^2) lies
   within 1.5% of 1 at every k with P_zz > 0.05, with K_L = 2/3 + 1/(3N).
D. The bound is soft: on L = 16 at the smallest wavevector (2 pi/16, 0, 0),
   omega_SMA / |s|^2 agrees with 2 n_f K_L within 2%. From L = 8 to L = 16
   the bound's slope omega_SMA / |k| at the smallest wavevector falls by the
   factor of |s|^2 / |k| (0.520) within 1%, where a linear branch would keep
   it fixed.

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


def initial(L):
    E = np.empty((3, L, L, L), np.int8)
    alt = (-1) ** np.arange(L)
    E[0] = np.broadcast_to(alt[None, :, None], (L, L, L))
    E[1] = np.broadcast_to(alt[None, None, :], (L, L, L))
    E[2] = np.broadcast_to(alt[:, None, None], (L, L, L))
    return E


def flippable(E):
    # count plaquettes whose four arrows circulate, in the three planes
    tot = 0
    for i, j in ((0, 1), (0, 2), (1, 2)):
        a = E[i]
        b = np.roll(E[j], -1, axis=i)
        c = -np.roll(E[i], -1, axis=j)
        d = -E[j]
        tot += int(((a == b) & (b == c) & (c == d)).sum())
    return tot


def sample(L, nloops, nbins, s, fft=True):
    seed(s)
    E = initial(L)
    for _ in range(max(nloops // 20, 50)):
        worm(E, L)
    N = L ** 3
    per = nloops // nbins
    nfb = np.zeros(nbins)
    Sb = np.zeros((nbins, L, L, L))
    for b in range(nbins):
        for _ in range(per):
            worm(E, L)
            nfb[b] += flippable(E) / (3 * N)
            if fft:
                Sb[b] += np.abs(np.fft.fftn(E[2].astype(float))) ** 2 / N
        nfb[b] /= per
        Sb[b] /= per
    return nfb, Sb


# ---------------------------------------------------------------- A. exact L = 2
print("== A. The exact L = 2 torus ==")


def lid(i, x, y, z):
    return i * 8 + ((x % 2) * 4 + (y % 2) * 2 + (z % 2))


V2 = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
outs = [[lid(0, *v), lid(1, *v), lid(2, *v)] for v in V2]
ins = [[lid(0, v[0] - 1, v[1], v[2]), lid(1, v[0], v[1] - 1, v[2]), lid(2, v[0], v[1], v[2] - 1)] for v in V2]
good = []
for c in range(16):
    idx = np.arange(c << 20, (c + 1) << 20, dtype=np.int64)
    bits = (((idx[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int8)
    ok = np.ones(len(idx), bool)
    for o, b in zip(outs, ins):
        ok &= bits[:, o].sum(1) == bits[:, b].sum(1)
    good.append(idx[ok])
codes = np.concatenate(good)
where = {int(cd): n for n, cd in enumerate(codes)}
plaq = []
for (x, y, z) in V2:
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        r = [x, y, z]
        ri = list(r)
        ri[i] += 1
        rj = list(r)
        rj[j] += 1
        plaq.append(((lid(i, *r), 1), (lid(j, *ri), 1), (lid(i, *rj), -1), (lid(j, *r), -1)))
arrows = (((codes[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int64)
D = np.zeros(len(codes), np.int64)
edges = []
for n, cd in enumerate(codes):
    for p in plaq:
        circ = [arrows[n, l] * s for (l, s) in p]
        if len(set(circ)) == 1:
            D[n] += 1
            new = int(cd)
            for (l, _) in p:
                new ^= 1 << l
            edges.append((n, where[new]))
nf2 = Fraction(int(D.sum()), len(codes) * 24)
Ez = [lid(2, *v) for v in V2]
fsum_ok = True
for kk in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]:
    ph = np.array([(-1) ** (kk[0] * x + kk[1] * y + kk[2] * z) for (x, y, z) in V2])
    O = (arrows[:, Ez] * ph).sum(1)
    val = int((D * O * O).sum()) - int(sum(O[u] * O[v] for u, v in edges))
    lhs = Fraction(val, len(codes) * 8)
    rhs = 2 * nf2 * ((2 - 2 * (-1) ** kk[0]) + (2 - 2 * (-1) ** kk[1]))
    fsum_ok &= lhs == rhs
check("n_f = 13/60, and <0|O^+ (D - A) O|0> = 2 n_f (s_x^2 + s_y^2) exactly at all 8 wavevectors",
      len(codes) == 9600 and nf2 == Fraction(13, 60) and fsum_ok, f"{len(codes)} configurations, {len(edges)} flips, n_f = {nf2}")
nfb2, _ = sample(2, 200000, 20, 20260923, fft=False)
m2, e2 = nfb2.mean(), nfb2.std(ddof=1) / np.sqrt(len(nfb2))
check("the worm reproduces n_f = 13/60 on L = 2 within 4 standard errors",
      abs(m2 - 13 / 60) < 4 * e2, f"{m2:.5f} +- {e2:.5f} vs {13 / 60:.5f}")
print()

# ---------------------------------------------------------------- C, D.
out = {}
for L, nl in ((8, 1000000), (16, 200000)):
    nfb, Sb = sample(L, nl, 20, 20260924 + L)
    N = L ** 3
    KL = (2 * N + 1) / (3 * N)
    nf = nfb.mean()
    S = Sb.mean(0)
    k = 2 * np.pi * np.arange(L) / L
    s2 = 2 - 2 * np.cos(k)
    sxy = s2[:, None, None] + s2[None, :, None] + 0 * s2[None, None, :]
    tot = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
    P = np.zeros_like(tot)
    P[tot > 0] = sxy[tot > 0] / tot[tot > 0]
    mask = P > 0.05
    omega = 2 * nf * sxy[mask] / S[mask]
    R = omega / (2 * nf * KL * tot[mask])
    w1 = 2 * nf * s2[1] / S[1, 0, 0]
    out[L] = dict(nf=nf, nfe=nfb.std(ddof=1) / np.sqrt(len(nfb)), KL=KL, Rmin=float(R.min()), Rmax=float(R.max()),
                  w1=float(w1), s1=float(s2[1]), k1=float(k[1]))

print("== C. L = 8, 10^6 worms ==")
o8 = out[8]
check("omega_SMA / (2 n_f K_L |s|^2) lies within 1.5% of 1 at every k with P_zz > 0.05",
      o8["Rmin"] > 0.985 and o8["Rmax"] < 1.015,
      f"R in [{o8['Rmin']:.4f}, {o8['Rmax']:.4f}], n_f = {o8['nf']:.5f} +- {o8['nfe']:.5f}, 2 n_f K_L = {2 * o8['nf'] * o8['KL']:.4f}")
print()

print("== D. The bound is soft ==")
o16 = out[16]
coef = o16["w1"] / o16["s1"]
slope8, slope16 = o8["w1"] / o8["k1"], o16["w1"] / o16["k1"]
quad = (o16["s1"] / o16["k1"]) / (o8["s1"] / o8["k1"])
check("on L = 16 at (2 pi/16, 0, 0) omega_SMA / |s|^2 agrees with 2 n_f K_L within 2%; from L = 8 to 16 omega_SMA / |k| falls by the quadratic factor within 1%",
      abs(coef / (2 * o16["nf"] * o16["KL"]) - 1) < 0.02 and abs(slope16 / slope8 / quad - 1) < 0.01,
      f"omega_SMA = {o16['w1']:.4f} at |k| = {o16['k1']:.4f}; ratio to 2 n_f K_L |s|^2 {coef / (2 * o16['nf'] * o16['KL']):.4f}; "
      f"omega/|k| {slope8:.4f} (L=8) -> {slope16:.4f} (L=16), factor {slope16 / slope8:.4f} vs |s|^2/|k| factor {quad:.4f} (a linear branch gives 1)")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
