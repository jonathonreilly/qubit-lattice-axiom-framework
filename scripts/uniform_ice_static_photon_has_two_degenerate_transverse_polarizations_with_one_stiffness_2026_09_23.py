#!/usr/bin/env python3
'Finite computations supporting: Longitudinal covariance nulls and exact L=2 tensor values, with seeded L=8 estimates of transverse covariance eigenvalues. Numerical diagnostics are not limit or particle theorems.'
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_STATIC_PHOTON_HAS_TWO_DEGENERATE_TRANSVERSE_POLARIZATIONS_WITH_ONE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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


def sample_tensor(L, nloops, nbins, s):
    seed(s)
    E = initial(L)
    for _ in range(max(nloops // 20, 50)):
        worm(E, L)
    N = L ** 3
    per = nloops // nbins
    Sb = np.zeros((nbins, 3, 3, L, L, L), complex)
    for b in range(nbins):
        for _ in range(per):
            worm(E, L)
            F = np.fft.fftn(E.astype(float), axes=(1, 2, 3))
            Sb[b] += F[:, None] * F[None, :].conj() / N
        Sb[b] /= per
    return Sb


def fold(m, L):
    return min(m, L - m)


def transverse(M, kk):
    # eigenvalues of the Hermitian tensor M at wavevector kk: longitudinal residual and the two transverse values
    s = 1 - np.exp(-1j * np.asarray(kk))
    u = s / np.linalg.norm(s)
    H = (M + M.conj().T) / 2
    ev = np.linalg.eigvalsh(H)
    return np.linalg.norm(H @ u.conj()), ev[1], ev[2]


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
    good.append(bits[ok])
G2 = np.concatenate(good).astype(np.int64)
KS = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
EX = {}
for kk in KS:
    ph = np.array([(-1) ** (kk[0] * x + kk[1] * y + kk[2] * z) for (x, y, z) in V2])
    F = np.stack([(G2[:, [lid(i, *v) for v in V2]] * ph).sum(1) for i in range(3)], axis=1)
    EX[kk] = [[Fraction(int((F[:, i] * F[:, j]).sum()), 8 * len(G2)) for j in range(3)] for i in range(3)]
null_exact = all(sum(EX[kk][i][j] * 2 * kk[j] for j in range(3)) == 0 for kk in KS for i in range(3))
sumrule = sum(EX[kk][2][2] for kk in KS) / 8
S111 = EX[(1, 1, 1)]
deg111 = S111[0][0] - S111[0][1] == Fraction(87, 75) and S111[0][1] == S111[0][2] == S111[1][2]
S110 = EX[(1, 1, 0)]
split110 = (S110[0][0] - S110[0][1], S110[2][2])
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      len(G2) == 9600 and null_exact and sumrule == 1 and deg111 and split110 == (Fraction(86, 75), Fraction(114, 75)),
      f"{len(G2)} configurations; sum rule {sumrule}; (pi,pi,0): {split110[0]}, {split110[1]}")
Sb2 = sample_tensor(2, 200000, 20, 20260923)
m2 = Sb2.mean(0)
e2 = Sb2.real.std(0, ddof=1) / np.sqrt(len(Sb2))
zs = [abs(m2[i, j][kk].real - float(EX[kk][i][j])) / max(e2[i, j][kk], 1e-12) for kk in KS for i in range(3) for j in range(3)
      if EX[kk][i][j] != 0 or e2[i, j][kk] > 0]
exact_zero_ok = all(abs(m2[i, j][kk]) < 1e-12 for kk in KS for i in range(3) for j in range(3) if EX[kk][i][j] == 0 and e2[i, j][kk] == 0)
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      max(zs) < 4 and exact_zero_ok, f"largest deviation {max(zs):.2f} standard errors over {len(zs)} fluctuating entries")
print()

# ---------------------------------------------------------------- C, D. L = 8
L = 8
Sb = sample_tensor(L, 2000000, 20, 20260924)
N = L ** 3
KL = (2 * N + 1) / (3 * N)
nb = len(Sb)
tot = Sb.sum(0)
kgrid = 2 * np.pi * np.arange(L) / L
keys = [(a, b, c) for a in range(L) for b in range(L) for c in range(L) if (a, b, c) != (0, 0, 0)]


def summarize(S):
    out = {}
    for (a, b, c) in keys:
        res, l1, l2 = transverse(S[:, :, a, b, c], (kgrid[a], kgrid[b], kgrid[c]))
        out[(a, b, c)] = (res, KL * l1, KL * l2)
    return out


full = summarize(tot / nb)
null = max(v[0] for v in full.values())
lo = min(v[1] for v in full.values())
hi = max(v[2] for v in full.values())
print("== C. L = 8, 2 x 10^6 worms ==")
check('Finite diagnostic 3; scope and exceptions are in the companion note', null < 1e-10, f"largest residual {null:.1e}")
check('Finite diagnostic 4; scope and exceptions are in the companion note', lo > 0.99 and hi < 1.01,
      f"K_L lambda in [{lo:.4f}, {hi:.4f}], K_L = {KL:.6f}")
print()


def cls(key):
    return tuple(sorted(fold(m, L) for m in key))


def kind(c):
    nz = [x for x in c if x]
    if len(nz) == 1:
        return "axial"
    if len(nz) == 3 and len(set(nz)) == 1:
        return "body"
    return "other"


def class_splits(summary):
    acc = {}
    for key, (_, l1, l2) in summary.items():
        acc.setdefault(cls(key), []).append(l2 - l1)
    return {c: float(np.mean(v)) for c, v in acc.items()}


base = class_splits(full)
jk = [class_splits(summarize((tot - Sb[b]) / (nb - 1))) for b in range(nb)]
err = {c: float(np.sqrt((nb - 1) / nb * sum((j[c] - np.mean([jj[c] for jj in jk])) ** 2 for j in jk))) for c in base}
worst = max(base, key=lambda c: base[c])
# unbiased degeneracy test: project S on a fixed real transverse basis where symmetry forces B = (tr B / 2) I
tests = []
for m in range(1, L):
    for ax in range(3):
        k = [0, 0, 0]
        k[ax] = m
        b1, b2 = [i for i in range(3) if i != ax]
        e = np.zeros((2, 3))
        e[0, b1] = 1
        e[1, b2] = 1
        tests.append((tuple(k), e))
    e = np.array([[1, -1, 0], [1, 1, -2]], float)
    e = e / np.linalg.norm(e, axis=1)[:, None]
    tests.append(((m, m, m), e))
zmax = 0.0
for k, e in tests:
    Bs = np.einsum("ai,nij,bj->nab", e, Sb[:, :, :, k[0], k[1], k[2]], e)
    q = np.stack([(Bs[:, 0, 0] - Bs[:, 1, 1]).real, Bs[:, 0, 1].real, Bs[:, 0, 1].imag], axis=1)
    mq = q.mean(0)
    eq = q.std(0, ddof=1) / np.sqrt(nb)
    for v, ev in zip(mq, eq):
        if ev > 0:
            zmax = max(zmax, abs(v) / ev)
print("== D. The splits ==")
check('Finite diagnostic 5; scope and exceptions are in the companion note',
      zmax < 4, f"{len(tests)} wavevectors, {3 * len(tests)} linear tests; largest {zmax:.2f} standard errors")
check('Finite diagnostic 6; scope and exceptions are in the companion note',
      base[worst] < 0.01 and base[(0, 4, 4)] < 0.01,
      f"largest {base[worst] * 100:.2f}% +- {err[worst] * 100:.2f}% at {worst} 2pi/8; (pi,pi,0): {base[(0, 4, 4)] * 100:.2f}% +- {err[(0, 4, 4)] * 100:.2f}%")
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
