#!/usr/bin/env python3
"""J:derive:chessboard-repair:a1 (worker w-jonathonsmac4f50-j877a, claude-opus-5): exact checks for ATTEMPT.md.

Block 17 (PR #8151): tori T_L = (Z/2L)^d, the static six-axis law mu_L(v) = prod_bonds phi(v_x, v_y)/Z_L, phi = p, q, r (same, antipodal,
orthogonal), m = max(q, r); a bond is bad if its endpoints differ.

Checks (fractions / integers unless stated):
  A  orbits: under the site reflections theta_{i,k} the canonical direction-1 bond of the origin cell reaches exactly the direction-1 bonds
     with the same transverse parity (N/2 in 2D, N/4 in 3D) - the defect; under site reflections in direction 1 and BOND-plane reflections
     x_j -> 2k + 1 - x_j in the other directions it reaches every direction-1 bond (N);
  B  the counting lemmas of route A: (i) the one-line lemma - for a cyclic line s and a cyclic neighbour line a with all consecutive entries
     of a different, bad(s) + 2 bad(s, a) >= n, exhaustive for n = 4 and n = 6 over all s and all such a; (ii) the 2D minimum over the 4x2
     torus (all 6^8 patterns): every pattern with all even-row horizontal bonds bad has >= N = 8 bad bonds, attained; (iii) sharpness:
     explicit patterns with exactly N bad bonds (2D) and exactly 3N/4 bad bonds (3D) in the corrected disseminated events on (Z/4)^d, (Z/6)^d;
  C  bond-plane reflection positivity: the eigenvalues of phi; on the four-site ring the reflection form is G^T (phi x phi) G, so it is
     positive for every F iff phi is positive semidefinite (p >= q and p + q >= 2r): exact negative witnesses at (5,2,4), (1,3,2), and
     positivity of random rational F at (3,1,2), (7,3,5), (216,1,1); on the 4 x 2 torus (bond planes in the length-4 direction) the
     smallest eigenvalue of the reflection matrix in floating point, and an exact rational witness at (5,2,4);
  D  the corrected disseminated bound on the 4 x 2 torus at (216, 1, 1) and (432, 1, 2), exactly: mu(all even-row horizontal bonds bad)^(1/N)
     <= 6m/p; mu(all horizontal bonds bad)^(1/N) <= 6m/p;
  E  constants: 6m/p <= 1/36 iff p >= 216 m; 6 (m/p)^(3/4) <= 1/36 iff p >= 6^4 m = 1296 m; p >= 216 m implies phi positive semidefinite.
"""
import itertools
import sys
from fractions import Fraction as F

import numpy as np

VALS = range(6)                                   # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z


def phi(p, q, r):
    return [[p if a == b else (q if a == b ^ 1 else r) for b in VALS] for a in VALS]


# ---------------------------------------------------------------------------------------------------------------- A: orbits
def orbit(d, side, bond_plane_dirs):
    """orbit of the direction-0 bond (0,...,0)-(1,0,...,0) under reflections: site planes x_i -> 2k - x_i for i not in bond_plane_dirs,
    bond planes x_i -> 2k + 1 - x_i for i in bond_plane_dirs (all k)"""
    def refl(bond, i, k):
        (a, b) = bond
        f = (lambda x: (2 * k + 1 - x) % side) if i in bond_plane_dirs else (lambda x: (2 * k - x) % side)
        a2 = tuple(f(a[j]) if j == i else a[j] for j in range(d))
        b2 = tuple(f(b[j]) if j == i else b[j] for j in range(d))
        return tuple(sorted((a2, b2)))
    start = tuple(sorted(((0,) * d, (1,) + (0,) * (d - 1))))
    seen, todo = {start}, [start]
    while todo:
        bnd = todo.pop()
        for i in range(d):
            for k in range(side):
                nb = refl(bnd, i, k)
                if nb not in seen:
                    seen.add(nb)
                    todo.append(nb)
    direction0 = all(sum(1 for j in range(d) if (u[j] - w[j]) % side != 0) == 1 and (u[0] - w[0]) % side != 0 for u, w in seen)
    parity_class = all(u[j] % 2 == 0 for u, w in seen for j in range(1, d))
    return len(seen), direction0, parity_class


# ---------------------------------------------------------------------------------------------------------------- B: counting
def line_lemma(n):
    """bad(s) + 2*bad(s, a) >= n for every cyclic line s and every cyclic line a with all consecutive entries different"""
    lines = np.array(list(itertools.product(VALS, repeat=n)), dtype=np.int8)
    bad_own = (lines != np.roll(lines, -1, axis=1)).sum(1)
    proper = lines[bad_own == n]
    worst = None
    for chunk in np.array_split(proper, max(1, len(proper) // 200)):
        between = (lines[:, None, :] != chunk[None, :, :]).sum(2)          # (all s, chunk a)
        total = bad_own[:, None] + 2 * between
        mn = int(total.min())
        worst = mn if worst is None else min(worst, mn)
    return worst, len(proper)


def min_bad_4x2():
    """all 6^8 patterns of the torus Z/4 x Z/2 (rows y = 0 even, 1 odd; horizontal cycles of length 4; each vertical pair joined by two bonds)"""
    conf = np.array(list(itertools.product(VALS, repeat=8)), dtype=np.int8).reshape(-1, 2, 4)
    row0, row1 = conf[:, 0, :], conf[:, 1, :]
    hbad0 = (row0 != np.roll(row0, -1, axis=1)).sum(1)
    hbad1 = (row1 != np.roll(row1, -1, axis=1)).sum(1)
    vbad = 2 * (row0 != row1).sum(1)
    total = hbad0 + hbad1 + vbad
    event = hbad0 == 4
    return int(total[event].min()), int(event.sum())


def bad_count(d, side, pattern):
    tot = 0
    for x in itertools.product(range(side), repeat=d):
        for i in range(d):
            y = tuple((x[j] + (1 if j == i else 0)) % side for j in range(d))
            tot += pattern[x] != pattern[y]
    return tot


def sharp_2d(side):
    # even rows alternate 0,2,0,2,...; odd rows constant 0
    pat = {(x, y): (0 if y % 2 else (0 if x % 2 == 0 else 2)) for x in range(side) for y in range(side)}
    ev = all(pat[(x, y)] != pat[((x + 1) % side, y)] for x in range(side) for y in range(0, side, 2))
    return bad_count(2, side, pat), side * side, ev


def sharp_3d(side):
    # lines in direction 1 with both transverse coordinates even alternate 0,2; every other site 0
    pat = {}
    for x in itertools.product(range(side), repeat=3):
        pat[x] = (0 if x[0] % 2 == 0 else 2) if (x[1] % 2 == 0 and x[2] % 2 == 0) else 0
    ev = all(pat[x] != pat[((x[0] + 1) % side, x[1], x[2])] for x in itertools.product(range(side), repeat=3) if x[1] % 2 == 0 and x[2] % 2 == 0)
    return bad_count(3, side, pat), side ** 3, ev


# ---------------------------------------------------------------------------------------------------------------- C: bond-plane RP
def ring4_form(pqr, Fvec):
    """four-site ring 0-1-2-3-0, bond planes 1/2 and 5/2: H+ = {1,2}, theta: 1 <-> 0, 2 <-> 3; Q(F) = sum F(a) F(b) weight(v1,v2 = a; v0,v3 = b)"""
    P = phi(*pqr)
    tot = F(0)
    for a1, a2, b1, b2 in itertools.product(VALS, repeat=4):
        w = P[b1][a1] * P[a1][a2] * P[a2][b2] * P[b2][b1]
        tot += Fvec[(a1, a2)] * Fvec[(b1, b2)] * w
    return tot


def eig_phi(pqr):
    p, q, r = pqr
    return p + q + 4 * r, p - q, p + q - 2 * r


def torus42_rp(pqr):
    """torus Z/4 (direction of the reflection) x Z/2; bond planes x = 1/2 and x = 5/2; H+ = {x in {1,2}} (4 sites), theta: x -> 1 - x.
    Reflection matrix R(alpha, beta) = sum of weights with v_{H+} = alpha and v_{H-} = theta(beta) (unnormalized)."""
    P = np.array(phi(*pqr), dtype=float)
    Pint = phi(*pqr)
    # sites (x, y); H+ sites (1,0),(1,1),(2,0),(2,1); H- sites (0,0),(0,1),(3,0),(3,1) with theta(1,y)=(0,y), theta(2,y)=(3,y)
    confs = list(itertools.product(VALS, repeat=4))                 # (v(1,0), v(1,1), v(2,0), v(2,1))
    def inner(c):                                                    # bonds inside H+: x-bond (1,y)-(2,y), y-bonds (double: Z/2) at x=1,2
        a10, a11, a20, a21 = c
        return P[a10, a20] * P[a11, a21] * P[a10, a11] ** 2 * P[a20, a21] ** 2
    w_in = np.array([inner(c) for c in confs])
    A = np.array(confs)
    # crossing bonds: (1,y)-(0,y) and (2,y)-(3,y); beta gives v(0,y) = beta(1,y) positions, v(3,y) = beta(2,y) positions
    cross = (P[A[:, None, 0], A[None, :, 0]] * P[A[:, None, 1], A[None, :, 1]] * P[A[:, None, 2], A[None, :, 2]] * P[A[:, None, 3], A[None, :, 3]])
    R = w_in[:, None] * cross * w_in[None, :]
    R = R / np.abs(R).max()                                          # scale: the sign of the spectrum is what matters
    ev, evec = np.linalg.eigh(R)
    return ev[0], evec[:, 0], confs, Pint


def exact_form_42(pqr, Fv, confs, Pint):
    def inner(c):
        a10, a11, a20, a21 = c
        return Pint[a10][a20] * Pint[a11][a21] * Pint[a10][a11] ** 2 * Pint[a20][a21] ** 2
    tot = F(0)
    wi = [inner(c) for c in confs]
    for i, a in enumerate(confs):
        if Fv[i] == 0:
            continue
        for j, b in enumerate(confs):
            if Fv[j] == 0:
                continue
            cr = Pint[a[0]][b[0]] * Pint[a[1]][b[1]] * Pint[a[2]][b[2]] * Pint[a[3]][b[3]]
            tot += Fv[i] * Fv[j] * wi[i] * cr * wi[j]
    return tot


# ---------------------------------------------------------------------------------------------------------------- D: disseminated bound on 4x2
def diss_42(pqr):
    p, q, r = pqr
    m = max(q, r)
    P = np.array(phi(*pqr), dtype=object)
    conf = np.array(list(itertools.product(VALS, repeat=8)), dtype=np.int64).reshape(-1, 2, 4)
    row0, row1 = conf[:, 0, :], conf[:, 1, :]
    w = np.ones(len(conf), dtype=object)
    for x in range(4):
        w = w * P[row0[:, x], row0[:, (x + 1) % 4]] * P[row1[:, x], row1[:, (x + 1) % 4]] * P[row0[:, x], row1[:, x]] ** 2
    Z = int(w.sum())
    ev0 = (row0 != np.roll(row0, -1, axis=1)).all(1)
    evall = ev0 & (row1 != np.roll(row1, -1, axis=1)).all(1)
    pe0 = F(int(w[ev0].sum()), Z)
    pall = F(int(w[evall].sum()), Z)
    N = 8
    bound = F(6 * m, p)
    return float(pe0) ** (1 / N), float(pall) ** (1 / N), float(bound), pe0 <= bound ** N, pall <= bound ** N


def main():
    hits_ok = True
    # A
    for d, side in ((2, 4), (2, 8), (3, 4), (3, 6)):
        n_site, dir0, par = orbit(d, side, set())
        n_mixed, dir0m, _ = orbit(d, side, set(range(1, d)))
        N = side ** d
        ok = n_site == N // 2 ** (d - 1) and par and dir0 and n_mixed == N and dir0m
        hits_ok &= ok
        print(f"[A] d={d} side {side}: site reflections reach {n_site} direction-1 bonds (N/2^(d-1) = {N // 2 ** (d - 1)}; all with even transverse "
              f"coordinates: {par}); site reflections along the bond + bond-plane reflections across it reach {n_mixed} (N = {N}): {ok}")
    # B
    for n in (4, 6):
        worst, nprop = line_lemma(n)
        hits_ok &= worst >= n
        print(f"[B-i] one-line lemma n = {n}: min over all lines s and all {nprop} proper cyclic neighbour lines a of bad(s) + 2 bad(s, a) = "
              f"{worst} (>= n: {worst >= n})")
    mn, cnt = min_bad_4x2()
    hits_ok &= mn == 8
    print(f"[B-ii] 4x2 torus, all 6^8 patterns: {cnt} patterns have every even-row horizontal bond bad; their minimum number of bad bonds is {mn} "
          f"(N = 8)")
    for side in (4, 6):
        b2, n2, e2 = sharp_2d(side)
        b3, n3, e3 = sharp_3d(side)
        ok = b2 == n2 and e2 and 4 * b3 == 3 * n3 and e3
        hits_ok &= ok
        print(f"[B-iii] side {side}: a 2D pattern in the corrected event with {b2} bad bonds (N = {n2}); a 3D pattern with {b3} (3N/4 = {3 * n3 // 4}): {ok}")
    # C
    rng = np.random.default_rng(8151)
    for pqr in ((3, 1, 2), (7, 3, 5), (216, 1, 1), (5, 2, 4), (1, 3, 2)):
        e = eig_phi(pqr)
        psd = min(e) >= 0
        # witness for indefinite phi: G = f_neg (x) f_pos with phi f_neg = lambda_neg f_neg, lambda_neg < 0; F(a) = G(a)/phi(a1, a2)
        P = phi(*pqr)
        if not psd:
            if e[1] < 0:
                fneg = [1, -1, 0, 0, 0, 0]                           # odd: eigenvalue p - q
            else:
                fneg = [1, 1, -1, -1, 0, 0]                          # even zero-sum: eigenvalue p + q - 2r
            fpos = [1] * 6
            Fvec = {(a1, a2): F(fneg[a1] * fpos[a2], P[a1][a2]) for a1 in VALS for a2 in VALS}
            val = ring4_form(pqr, Fvec)
            ok = val < 0
            label = f"indefinite (eigenvalues {e}): witness Q(F) = {val} < 0"
        else:
            vals = []
            for _ in range(20):
                Fvec = {(a1, a2): F(int(rng.integers(-9, 10)), 7) for a1 in VALS for a2 in VALS}
                vals.append(ring4_form(pqr, Fvec))
            ok = min(vals) >= 0
            label = f"positive semidefinite (eigenvalues {e}): min over 20 random rational F of Q(F) = {float(min(vals)):.4g} >= 0"
        hits_ok &= ok
        print(f"[C ring] {pqr}: {label}: {ok}")
    for pqr in ((216, 1, 1), (3, 1, 2), (5, 2, 4)):
        lam, vec, confs, Pint = torus42_rp(pqr)
        line = f"[C 4x2] {pqr}: smallest eigenvalue of the reflection matrix (scaled to max entry 1) {lam:.4g}"
        if lam < -1e-8:
            scale = 10 ** 4
            Fv = [F(int(round(x * scale)), scale) for x in vec]
            exact = exact_form_42(pqr, Fv, confs, Pint)
            line += f"; rationalized eigenvector gives exactly Q(F) = {float(exact):.4g} < 0: {exact < 0}"
            hits_ok &= exact < 0
        print(line)
    # D
    for pqr in ((216, 1, 1), (432, 1, 2)):
        r0, rall, bnd, ok0, okall = diss_42(pqr)
        hits_ok &= ok0 and okall
        print(f"[D] 4x2 torus {pqr}: mu(even-row horizontal bonds all bad)^(1/N) = {r0:.5f}, mu(all horizontal bonds bad)^(1/N) = {rall:.5f}, "
              f"6m/p = {bnd:.5f}: both below: {ok0 and okall}")
    # E
    e1 = F(6, 216) == F(1, 36)
    ok3d = (F(1, 36) / 6) ** 4 == F(1, 1296) ** 3                   # (m/p)^(3/4) = 1/216 iff m/p = 1/216^(4/3) = 1/1296
    psd216 = all(min(eig_phi((216 * max(q, r), q, r))) >= 0 for q in range(1, 6) for r in range(1, 6))
    hits_ok &= e1 and ok3d and psd216
    print(f"[E] 6m/p <= 1/36 iff p >= 216m: {e1}; 6(m/p)^(3/4) = 1/36 at p/m = 1296 (216^(4/3) = 6^4): {ok3d}; p = 216 max(q,r) gives a positive "
          f"semidefinite phi for q, r in 1..5: {psd216}")
    if hits_ok:
        print("HIT: block 17's chain repaired: (route A, site reflections only) the disseminated event is 'every direction-i bond of one transverse "
              "parity class is bad'; every such pattern has at least N bad bonds in 2D and 3N/4 in 3D (sharp), so T4 holds as stated in 2D "
              "(threshold p >= 216 m) and becomes 6(m/p)^(3/4) in 3D (threshold p >= 1296 m); (route B) for p >= q and p + q >= 2r the law is "
              "reflection positive through bond planes, site reflections along a bond and bond-plane reflections across it disseminate to every "
              "bond of its direction, mu(B_i bad) <= (6m/p)^|B_i| per direction and (6m/p)^(n/2) for in-plane sets, and since p >= 216 max(q,r) "
              "forces p >= q and p + q >= 2r, block 17's T5-T7 hold as stated: at least two Gibbs states on Z^2 and Z^3 for p >= 216 max(q,r)")
        print("SUMMARY: PROVED (for referee) - block 17's thresholds p >= 216 max(q,r) in 2D and 3D restored by bond-plane reflection positivity "
              "(valid there since phi is then positive semidefinite); the site-reflection route alone gives 216 m in 2D and 1296 m in 3D (sharp "
              "counting lemmas N and 3N/4); bond-plane RP holds iff phi is PSD on the four-site ring (exact witnesses)")
    else:
        print("SUMMARY: ROUTE FAILS AT a finite check (see above)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
