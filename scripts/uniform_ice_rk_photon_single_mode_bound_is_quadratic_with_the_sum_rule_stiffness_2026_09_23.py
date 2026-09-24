#!/usr/bin/env python3
'Finite computations supporting: An exact conditional flip-graph energy identity and finite numerical Rayleigh quotients; a positive-excitation bound additionally requires removal of all ground-space components. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_WITH_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/UNIFORM_ICE_STATIC_PHOTON_HAS_TWO_DEGENERATE_TRANSVERSE_POLARIZATIONS_WITH_ONE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md')

import sys
import time
from fractions import Fraction

import numpy as np
from numba import njit

PASS = FAIL = 0
T0 = time.time()
print("Evidence boundary: finite computations and bin diagnostics; no certified spectral enclosure, confidence coverage, particle claim or limit theorem.")


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
        assert m == 3
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
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      len(codes) == 9600 and nf2 == Fraction(13, 60) and fsum_ok, f"{len(codes)} configurations, {len(edges)} flips, n_f = {nf2}")
# A nonzero momentum does not remove all constant-on-component zero modes.
parent=list(range(len(codes)))
def component(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]; i=parent[i]
    return i
for u_,v_ in edges:
    parent[component(u_)]=component(v_)
groups={}
for i_ in range(len(codes)):groups.setdefault(component(i_),[]).append(i_)
phase=np.array([(-1)**v[0] for v in V2])
obs=(arrows[:,Ez]*phase).sum(1)
ground= sum((Fraction(int(obs[g].sum())**2,len(g)) for g in groups.values()),Fraction(0))/(8*len(codes))
check("Exact nonzero-momentum ground-space counterexample",len(groups)==937 and ground==Fraction(14,75),f"components {len(groups)}, projected norm {ground}")
nfb2, _ = sample(2, 200000, 20, 20260923, fft=False)
m2, e2 = nfb2.mean(), nfb2.std(ddof=1) / np.sqrt(len(nfb2))
check('Finite diagnostic 2; scope and exceptions are in the companion note',
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
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      o8["Rmin"] > 0.985 and o8["Rmax"] < 1.015,
      f"R in [{o8['Rmin']:.4f}, {o8['Rmax']:.4f}], n_f = {o8['nf']:.5f} +- {o8['nfe']:.5f}, 2 n_f K_L = {2 * o8['nf'] * o8['KL']:.4f}")
print()

print("== D. The bound is soft ==")
o16 = out[16]
coef = o16["w1"] / o16["s1"]
slope8, slope16 = o8["w1"] / o8["k1"], o16["w1"] / o16["k1"]
quad = (o16["s1"] / o16["k1"]) / (o8["s1"] / o8["k1"])
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      abs(coef / (2 * o16["nf"] * o16["KL"]) - 1) < 0.02 and abs(slope16 / slope8 / quad - 1) < 0.01,
      f"omega_SMA = {o16['w1']:.4f} at |k| = {o16['k1']:.4f}; ratio to 2 n_f K_L |s|^2 {coef / (2 * o16['nf'] * o16['KL']):.4f}; "
      f"omega/|k| {slope8:.4f} (L=8) -> {slope16:.4f} (L=16), factor {slope16 / slope8:.4f} vs |s|^2/|k| factor {quad:.4f} (a linear branch gives 1)")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
