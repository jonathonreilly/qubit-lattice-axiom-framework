#!/usr/bin/env python3
'Finite computations supporting: An exact one-vertex invariant lemma and L=2 alignment mean, with finite connected-correlation diagnostics for one specified neutral statistic. Numerical diagnostics are not limit or particle theorems.'
import itertools
AUDIT_TIMEOUT_SEC = 1800
AUDIT_INPUT_PATHS = ('docs/UNIFORM_ICE_CARRIES_THE_LATTICE_GREEN_FUNCTION_IN_ITS_CHARGED_SECTOR_WHILE_NEUTRAL_SCALAR_RECORDS_ARE_SHORT_RANGED_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md')

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


# ---------------------------------------------------------------- A. the invariant lemma
print("== A. The arrows at one vertex, and a sampler control ==")
dirs = [(s, a) for a in range(3) for s in (1, -1)]      # outward directions +x, -x, +y, -y, +z, -z


def action(perm, signs):
    # the signed permutation sends direction (s, a) to (s * signs[a], perm[a])
    M = np.zeros((6, 6))
    for col, (s, a) in enumerate(dirs):
        M[dirs.index((s * signs[a], perm[a])), col] = 1
    return M


group48 = [(p, sg) for p in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)]


def parity(p):
    return 1 if sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2 == 0 else -1


group24 = [(p, sg) for p, sg in group48 if parity(p) * sg[0] * sg[1] * sg[2] == 1]
ranks = []
spans = []
for G in (group48, group24):
    avg = sum(action(p, sg) for p, sg in G) / len(G)
    ranks.append(int(np.linalg.matrix_rank(avg, tol=1e-9)))
    spans.append(np.allclose(avg @ np.ones(6), np.ones(6)) and np.allclose(avg, np.ones((6, 6)) / 6))
check('Finite diagnostic 1; scope and exceptions are in the companion note',
      ranks == [1, 1] and all(spans) and len(group24) == 24, f"ranks {ranks}")


def lid(i, x, y, z):
    return i * 8 + ((x % 2) * 4 + (y % 2) * 2 + (z % 2))


V2 = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
outs = [[lid(0, *v), lid(1, *v), lid(2, *v)] for v in V2]
ins = [[lid(0, v[0] - 1, v[1], v[2]), lid(1, v[0], v[1] - 1, v[2]), lid(2, v[0], v[1], v[2] - 1)] for v in V2]
ftot = cnt = 0
for c in range(16):
    idx = np.arange(c << 20, (c + 1) << 20, dtype=np.int64)
    bits = (((idx[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int64)
    ok = np.ones(len(idx), bool)
    for o, b in zip(outs, ins):
        ok &= bits[:, o].sum(1) == bits[:, b].sum(1)
    g = bits[ok]
    cnt += len(g)
    for (x, y, z) in V2:
        ftot += int((g[:, lid(0, x, y, z)] * g[:, lid(0, x - 1, y, z)] + g[:, lid(1, x, y, z)] * g[:, lid(1, x, y - 1, z)]
                     + g[:, lid(2, x, y, z)] * g[:, lid(2, x, y, z - 1)]).sum())
f_exact = Fraction(ftot, cnt * 8)
seed(20260922)
E2 = initial(2)
for _ in range(20000):
    worm(E2, 2)
fb = np.zeros(20)
for b in range(20):
    for _ in range(10000):
        worm(E2, 2)
        e = E2.astype(float)
        fb[b] += sum(e[i] * np.roll(e[i], 1, axis=i) for i in range(3)).mean()
    fb[b] /= 10000
check('Finite diagnostic 2; scope and exceptions are in the companion note',
      cnt == 9600 and f_exact == Fraction(39, 25) and abs(fb.mean() - 39 / 25) < 4 * fb.std(ddof=1) / np.sqrt(20),
      f"{f_exact}; worm {fb.mean():.4f} +- {fb.std(ddof=1) / np.sqrt(20):.4f}")
print()

# ---------------------------------------------------------------- B. the lattice Green function
print("== B. The lattice Green function ==")
n = 128
k = 2 * np.pi * np.arange(n) / n
s2 = 2 - 2 * np.cos(k)
tot = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
inv = np.zeros_like(tot)
inv[tot > 0] = 1 / tot[tot > 0]
Gt = np.real(np.fft.ifftn(inv))
del tot, inv
Gax = [Gt[r, 0, 0] - Gt[n // 2, n // 2, n // 2] for r in range(0, 9)]
gratio = {r: Gax[r] / Gax[1] for r in range(2, 9)}
check('Finite diagnostic 3; scope and exceptions are in the companion note',
      abs((Gt[0, 0, 0] - Gt[1, 0, 0]) - (1 - 1 / n ** 3) / 6) < 1e-12 and min(gratio.values()) > 0.1,
      "G(r)/G(1): " + ", ".join(f"{r}: {v:.3f}" for r, v in gratio.items()))
del Gt
print()

# ---------------------------------------------------------------- C. a neutral scalar record
L, nl, nb = 16, 500000, 20
seed(20260923)
E = initial(L)
for _ in range(nl // 20):
    worm(E, L)
N = L ** 3
Cb = np.zeros((nb, L))
mb = np.zeros(nb)
per = nl // nb
for b in range(nb):
    for _ in range(per):
        worm(E, L)
        Ef = E.astype(float)
        f = sum(Ef[i] * np.roll(Ef[i], 1, axis=i) for i in range(3))
        corr = np.real(np.fft.ifftn(np.abs(np.fft.fftn(f)) ** 2)) / N
        Cb[b] += (corr[:, 0, 0] + corr[0, :, 0] + corr[0, 0, :]) / 3
        mb[b] += f.mean()
    Cb[b] /= per
    mb[b] /= per
mean = mb.mean()
C = Cb.mean(0) - mean ** 2
# Delete-bin estimates include the fluctuating mean subtraction and ratio denominator.
jkC = np.array([(Cb.sum(0)-Cb[b])/(nb-1)-((mb.sum()-mb[b])/(nb-1))**2 for b in range(nb)])
Ce = np.sqrt((nb-1)/nb * ((jkC-jkC.mean(0))**2).sum(0))
jkR = jkC/jkC[:,1,None]
ratio_errors = np.sqrt((nb-1)/nb*((jkR-jkR.mean(0))**2).sum(0))

print("== C. A neutral scalar record, L = 16, 5 x 10^5 worms ==")
resolved = C[1] > 5 * Ce[1] and C[2] > 5 * Ce[2] and C[2] / C[1] < gratio[2] / 3
far = all(abs(C[r]) < 4 * Ce[r] and abs(C[r]/C[1]) + 3*ratio_errors[r] < gratio[r] for r in range(3, 9))
check('Finite diagnostic 4; scope and exceptions are in the companion note',
      np.isfinite(C).all() and np.isfinite(Ce).all() and np.isfinite(ratio_errors).all() and C[0] > 0 and C[1] > 0,
      f"C(1)/C(0) = {C[1] / C[0]:.5f}, C(2)/C(1) = {C[2] / C[1]:.4f} (G: {gratio[2]:.3f}); "
      + "absolute ratio plus three estimated bin errors (not confidence bounds): " + ", ".join(f"{r}: {abs(C[r]/C[1]) + 3*ratio_errors[r]:.3f}" for r in range(3, 9)))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
