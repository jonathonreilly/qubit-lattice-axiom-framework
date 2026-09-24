#!/usr/bin/env python3
"""Uniform ice carries the lattice Green function in its charged sector, while neutral scalar records are short-ranged.

The derivation campaign's design note (#8093) asks, at its record-dynamics
seam, whether a Laplacian or transverse kernel appears in the finished record
statistics of a formation law, and it names the gravity node's input: a scalar
record statistic whose two-point function equals the lattice Green function.
Open PRs 8881 and 8890 found the transverse kernel in uniform ice's arrow
correlations, and open PRs 8875 and 8913 found the Green function in the free
energy of test defects, which carry charge +-2. This runner asks what neutral
scalar records do.

Checks:

A. The six outward arrows at a vertex are permuted by the 48 signed axis
   permutations and by the 24 proper rotations. The group average on them
   has rank 1 and is spanned by their sum, which is the divergence and
   vanishes in ice: no neutral scalar is linear in the arrows at one
   vertex. As a sampler control, the straight-through count f defined below
   has <f> = 39/25 exactly on the L = 2 torus, and the worm reproduces it.
B. The lattice Green function, as reference. On a 128^3 torus with the
   zero mode removed, G(0) - G(e) = (1 - 1/N)/6 within 1e-12, and G(r)/G(1)
   along an axis is printed for r = 2 to 8; it stays above 0.1.
C. A neutral quadratic scalar is short-ranged. On L = 16 with 5 x 10^5
   worms, f(r) = sum_i E_i(r) E_i(r - e_i), the straight-through count at a
   vertex, has a resolved correlation at r = 1 and r = 2, with
   C(2)/C(1) below a third of G(2)/G(1). For r = 3 to 8 its correlation is
   zero within 4 standard errors, and its 3-standard-error upper bound on
   C(r)/C(1) stays below G(r)/G(1).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
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
check("the six outward arrows at a vertex have no invariant combination but their sum, the divergence: group average of rank 1 for 48 and 24 elements",
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
check("on the exact L = 2 torus <f> = 39/25, and the worm reproduces it within 4 standard errors",
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
check("G(0) - G(e) = (1 - 1/N)/6 within 1e-12 (zero mode removed), and G(r)/G(1) along an axis stays above 0.1 for r = 2 to 8",
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
Ce = np.sqrt(((Cb - Cb.mean(0)) ** 2).sum(0) / (nb * (nb - 1)))
print("== C. A neutral scalar record, L = 16, 5 x 10^5 worms ==")
resolved = C[1] > 5 * Ce[1] and C[2] > 5 * Ce[2] and C[2] / C[1] < gratio[2] / 3
far = all(abs(C[r]) < 4 * Ce[r] and (abs(C[r]) + 3 * Ce[r]) / C[1] < gratio[r] for r in range(3, 9))
check("f has resolved correlation at r = 1, 2 with C(2)/C(1) below a third of G(2)/G(1); for r = 3 to 8 it is zero within 4 errors and bounded below G(r)/G(1)",
      resolved and far,
      f"C(1)/C(0) = {C[1] / C[0]:.5f}, C(2)/C(1) = {C[2] / C[1]:.4f} (G: {gratio[2]:.3f}); "
      + "bounds on C(r)/C(1): " + ", ".join(f"{r}: {(abs(C[r]) + 3 * Ce[r]) / C[1]:.3f}" for r in range(3, 9)))
print()
print(f"time {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
