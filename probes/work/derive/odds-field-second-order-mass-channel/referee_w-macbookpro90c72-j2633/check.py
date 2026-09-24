#!/usr/bin/env python3
"""Independent referee of J:derive:odds-field-second-order-mass-channel:a1.

Author w-jonathonsmac4f50-j728e (claude-opus-5-5). This file does not import that check.
Exact claims use fractions. The 5^3 field is reduced by the stabilizer of the origin.
The 11^3 body numbers are a separate sparse solve. Watson's G(0) is integrated, not copied.
"""
from fractions import Fraction as F
import itertools
import math

import numpy as np
from numpy.polynomial.legendre import leggauss

E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def poly_mul(poly, c):
    nxt = [F(0)] * (len(poly) + 1)
    for i, a in enumerate(poly):
        nxt[i] += a
        nxt[i + 1] += a * c
    return nxt


def normalizer_coeffs(leans, lam=1, n=5):
    """Z = (1/6) sum_s prod_y (1 + eps * 3 * lam * m_y.e(s)), coefficients of eps^0..eps^{n-1}."""
    acc = [F(0)] * n
    for e in E6:
        poly = [F(1)]
        for m in leans:
            poly = poly_mul(poly, 3 * lam * dot(m, e))
        for i in range(n):
            acc[i] += poly[i] if i < len(poly) else 0
    return [a / 6 for a in acc]


def esym(xs, k):
    s = F(0)
    for comb in itertools.combinations(xs, k):
        p = F(1)
        for t in comb:
            p *= t
        s += p
    return s


def step1():
    rng = np.random.default_rng(7)
    for _ in range(40):
        leans = [tuple(int(x) for x in rng.integers(-4, 5, size=3)) for _ in range(6)]
        c = normalizer_coeffs(leans)
        pair = sum(dot(leans[i], leans[j]) for i in range(6) for j in range(i + 1, 6))
        if c[0] != 1 or c[1] != 0 or c[2] != 3 * pair or c[3] != 0:
            raise SystemExit("step 1 algebra failed")
    unit = normalizer_coeffs([(1, 0, 0)] * 6)
    if unit[4] == 0:
        raise SystemExit("fourth order vanished on a case where it should not")
    bad = 0
    for axis in E6[:3]:
        for _ in range(12):
            us = [F(int(x)) for x in rng.integers(-3, 4, size=6)]
            xs = [3 * u for u in us]
            Z = F(0)
            for e in E6:
                p = F(1)
                for u in us:
                    p *= 1 + 3 * u * dot(axis, e)
                Z += p
            Z /= 6
            if Z != 1 + (esym(xs, 2) + esym(xs, 4) + esym(xs, 6)) / 3:
                bad += 1
    if bad:
        raise SystemExit("parallel closed form failed")
    print("STEP 1 FOLLOWS: on 40 integer leans, orders 1 and 3 of Z are 0 and order 2 is 3*sum_{y<y'} m.m'; "
          f"six parallel unit leans have fourth order {unit[4]} (so the remainder is O(m^4)); "
          "the parallel closed form holds for all three axes")


def step2():
    rng = np.random.default_rng(11)
    for _ in range(20):
        leans = [tuple(int(x) for x in rng.integers(-3, 4, size=3)) for _ in range(6)]
        # average of the six content-factors is Z, exactly, by the definition used in the attempt
        avg = [F(0)] * 4
        for e in E6:
            poly = [F(1)]
            for m in leans:
                poly = poly_mul(poly, 3 * dot(m, e))
            for i in range(4):
                avg[i] += poly[i]
        avg = [a / 6 for a in avg]
        Z = normalizer_coeffs(leans, n=4)
        if avg != Z:
            raise SystemExit("average factor is not Z")
        for e in E6:
            first = sum(3 * dot(m, e) for m in leans)
            poly = [F(1)]
            for m in leans:
                poly = poly_mul(poly, 3 * dot(m, e))
            if poly[1] != first:
                raise SystemExit("first-order coefficient is not 3 e.sum m")
    print("STEP 2 FOLLOWS inside the pure-vector hypothesis: each content's factor opens as "
          "1 + 3 e(b).sum m + ..., and the average over the six contents is Z, whose order 1 is 0")


def gauss(M):
    n = len(M)
    A = [row[:] for row in M]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pivv = A[col][col]
        for j in range(col, n + 1):
            A[col][j] /= pivv
        for r in range(n):
            if r == col or A[r][col] == 0:
                continue
            f = A[r][col]
            for j in range(col, n + 1):
                A[r][j] -= f * A[col][j]
    return [A[i][n] for i in range(n)]


def orbit_field(lam, L=5):
    sites = list(itertools.product(range(L), repeat=3))

    def canon(s):
        return tuple(sorted(min(c, L - c) for c in s))

    orbits = {}
    for s in sites:
        orbits.setdefault(canon(s), []).append(s)
    reps = {k: v[0] for k, v in orbits.items()}
    keys = [k for k in orbits if k != (0, 0, 0)]

    def neigh(s):
        out = []
        for a in range(3):
            for d in (1, -1):
                q = list(s)
                q[a] = (q[a] + d) % L
                out.append(tuple(q))
        return out

    idx = {k: i for i, k in enumerate(keys)}
    n = len(keys)
    M = [[F(0) for _ in range(n + 1)] for _ in range(n)]
    for k in keys:
        i = idx[k]
        M[i][i] = 1
        for q in neigh(reps[k]):
            ck = canon(q)
            if ck == (0, 0, 0):
                M[i][n] += lam
            else:
                M[i][idx[ck]] -= lam
    sol = gauss(M)
    u = {(0, 0, 0): F(1)}
    for k, val in zip(keys, sol):
        u[k] = val
    return u, neigh, canon


def far_constants(l1):
    """Coefficient of u^2 in 3 l1^2 sum_{y<y'} u_y u_y' for a pure decaying mode."""
    # along one axis: 2 cosh k + 4 = 1/l1
    c = (1 / l1 - 4) / 2
    c2 = 2 * c * c - 1
    axis = F(3, 2) * (1 - l1 * l1 * (2 * c2 + 4))
    # body diagonal: 6 cosh k = 1/l1
    cd = 1 / (6 * l1)
    cd2 = 2 * cd * cd - 1
    diag = F(3, 2) * (1 - l1 * l1 * 6 * cd2)
    return axis, diag


def step3():
    l1 = F(3, 23)
    u, neigh, canon = orbit_field(l1)
    l2 = F(5 + 2 - 8, 23)
    psi, _, _ = orbit_field(l2)
    stated = {
        (2, 0, 0): (1.1184e-3, 1.1182e-3),
        (1, 1, 0): (2.9438e-3, 2.9432e-3),
        (2, 2, 0): (8.572e-5, 8.572e-5),
    }
    for site, (z_claim, z2_claim) in stated.items():
        us = [u[canon(y)] for y in neigh(site)]
        ps = [psi[canon(y)] for y in neigh(site)]
        Z = F(1, 6) * (
            math.prod(1 + 3 * l1 * uy for uy in us)
            + math.prod(1 - 3 * l1 * uy for uy in us)
            + 4
        )
        pair = sum(us[i] * us[j] for i in range(6) for j in range(i + 1, 6))
        Z2 = 1 + 3 * l1 * l1 * pair
        pp = sum(ps[i] * ps[j] for i in range(6) for j in range(i + 1, 6))
        quad = 2 * l2 * l2 * pp  # w_a.w_a = 2/3, so 3 l2^2 * (2/3) sum psi psi
        if abs(float(Z - 1) - z_claim) > 5e-8 or abs(float(Z2 - 1) - z2_claim) > 5e-8:
            raise SystemExit(f"5^3 value disagrees at {site}: {float(Z-1)} {float(Z2-1)}")
        rel = abs(float((Z - Z2) / (Z2 - 1)))
        if rel > 5e-4:
            raise SystemExit("vector fourth order is not small")
        print(f"  site {site}: Z-1={float(Z-1):.6e} second={float(Z2-1):.6e} "
              f"rel4={rel:.3e} quad-second={float(quad):.3e} "
              f"45 l1^2 u^2={float(45*l1*l1*u[canon(site)]**2):.6e}")
    axis, diag = far_constants(l1)
    if axis != F(585, 529) or diag != F(610, 529):
        raise SystemExit(f"far constants {axis} {diag}")
    smooth = 45 * l1 * l1
    print(f"STEP 3 FOLLOWS as a pure-vector boundary-value computation (l1=3/23, l2={l2}). "
          f"The smooth coefficient 45 l1^2={smooth}={float(smooth):.4f} is not the linear-regime far constant: "
          f"axis {axis}={float(axis):.4f}, diagonal {diag}={float(diag):.4f}")


def watson_G0(n=48):
    """G(0) of -Delta on Z^3, via x=u^2 on the positive octant so the 1/k^2 peak is smooth."""
    nodes, wts = leggauss(n)
    span = math.sqrt(math.pi)
    xs = 0.5 * (nodes + 1) * span
    ws = 0.5 * wts * span
    U, V, W = np.meshgrid(xs, xs, xs, indexing="ij")
    WU, WV, WW = np.meshgrid(ws, ws, ws, indexing="ij")
    X, Y, Z = U * U, V * V, W * W
    den = 3 - np.cos(X) - np.cos(Y) - np.cos(Z)
    integ = np.sum((8 * U * V * W) / den * WU * WV * WW)
    return float(integ / (2 * math.pi ** 3))


def step4():
    # massless surface (3,1,2): l1=1/6, 45 l1^2 = 45/36 = 5/4
    l1 = F(1, 6)
    if 45 * l1 * l1 != F(5, 4):
        raise SystemExit("5/4 reduction failed")
    # leading harmonic correction: sum_{pairs} = 15 u^2 - |grad u|^2 + ... and 3*(1/6)^2 of that is 5/4 u^2
    # the gradient piece is O(1/r^4) once u ~ 1/r, so the leading potential is -(5/4) u^2
    G_int = watson_G0()
    G_quoted = 0.2527310098
    if abs(G_int - G_quoted) > 2e-6:
        raise SystemExit(f"Watson integral {G_int} is not the quoted constant")
    pref = (5 / 4) / (4 * math.pi * G_quoted) ** 2
    from_torus = F(5, 4) * (F(7, 25) ** 2)  # (5/4)*(0.28)^2
    if from_torus != F(49, 500):
        raise SystemExit(f"0.28 arithmetic failed: {from_torus}")
    amp = 1 / (4 * math.pi * G_quoted)
    print(f"STEP 4 DOES NOT FOLLOW: inputs G(0)={G_quoted} (integral {G_int:.7f}) and u~1/(4*pi*G(0)*r) "
          f"(amplitude {amp:.5f}) give V ~ -{pref:.5f}/r^2, not -0.098/r^2. "
          f"0.098 = (5/4)*(0.28)^2 = {float(from_torus):.3f}, the bottom of the task's 27^3 window r*v in 0.28..0.30, "
          "which is not Watson's amplitude. The attempt's own check formula prints this Watson prefactor and never tests 0.098; "
          "its only numeric assertion is 45/36=5/4 and that the prefactor is positive")
    return pref


def step5():
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import spsolve
    Lb = 11
    lam = 3 / 23
    sites = list(itertools.product(range(Lb), repeat=3))

    def neigh(s):
        for a in range(3):
            for d in (1, -1):
                q = list(s)
                q[a] = (q[a] + d) % Lb
                yield tuple(q)

    cache = {}

    def field(S):
        key = frozenset(S)
        if key in cache:
            return cache[key]
        free = [s for s in sites if s not in key]
        fi = {s: i for i, s in enumerate(free)}
        A = lil_matrix((len(free), len(free)))
        rhs = np.zeros(len(free))
        for s in free:
            A[fi[s], fi[s]] = 1.0
            for q in neigh(s):
                if q in fi:
                    A[fi[s], fi[q]] -= lam
                else:
                    rhs[fi[s]] += lam
        sol = spsolve(A.tocsr(), rhs)
        out = {s: (1.0 if s in key else float(sol[fi[s]])) for s in sites}
        cache[key] = out
        return out

    def body(c, n):
        return {tuple((c[i] + d[i]) % Lb for i in range(3)) for d in itertools.product(range(n), repeat=3)}

    def capacity(S, u):
        return sum(1 - lam * sum(u[q] for q in neigh(s)) for s in S)

    def coupling(A, B):
        uAB, uB = field(A | B), field(B)
        return 3 * lam * sum(uAB[y] - uB[y] for s in B for y in neigh(s) if y not in B)

    def blind(A, B):
        u = field(A)
        tot = 0.0
        for s in B:
            us = [u[y] for y in neigh(s)]
            pair = sum(us[i] * us[j] for i in range(6) for j in range(i + 1, 6))
            tot += 3 * lam * lam * pair
        return tot

    rows = {}
    for n in (1, 2):
        A, B = body((1, 1, 1), n), body((6, 1, 1), n)
        rows[n] = (capacity(A, field(A)), coupling(A, B), blind(A, B))
    ratio_c = rows[2][1] / rows[1][1]
    ratio_cap = (rows[2][0] / rows[1][0]) ** 2
    ratio_b = rows[2][2] / rows[1][2]
    if abs(ratio_c - 28.718) > 0.01 or abs(ratio_cap - 23.186) > 0.01:
        raise SystemExit(f"body arithmetic disagrees: {ratio_c} {ratio_cap}")
    print(f"STEP 5 ARITHMETIC FOLLOWS but it is not a redo of (a): first-order like-content coupling grows by "
          f"{ratio_c:.3f}, against (cap ratio)^2={ratio_cap:.3f} (caps {rows[1][0]:.4f}, {rows[2][0]:.4f}) and N^2=64. "
          f"The content-blind sum over B of 3 l1^2 pair-sums grows by {ratio_b:.1f}, near neither cap^2 nor N^2 nor cap^4="
          f"{ratio_cap**2:.1f}. Later than step 4")


def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                M[perm[i]][i] = signs[i]
            det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                   - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                   + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if det == 1:
                mats.append(M)
    avg = [[sum(M[i][j] for M in mats) for j in range(3)] for i in range(3)]
    if len(mats) != 24 or any(v != 0 for row in avg for v in row):
        raise SystemExit("vector average failed")
    # even axis weights, plane x+y+z=0, basis (1,-1,0), (1,1,-2)
    acc = [[0, 0], [0, 0]]
    for M in mats:
        perm = [int(np.argmax([abs(M[r][i]) for r in range(3)])) for i in range(3)]

        def apply(w):
            out = [0, 0, 0]
            for i in range(3):
                out[perm[i]] += w[i]
            return out

        cols = []
        for basis in ((1, -1, 0), (1, 1, -2)):
            img = apply(basis)
            # img = a(1,-1,0)+b(1,1,-2) => b = -img[2]/2, a = img[0]-b
            b = F(img[2], -2)
            a = img[0] - b
            if img[1] != -a + b:
                raise SystemExit("quadrupole image left the plane")
            cols.append((a, b))
        for i in range(2):
            for j in range(2):
                acc[i][j] += cols[j][i]
    if any(v != 0 for row in acc for v in row):
        raise SystemExit("quadrupole average failed")
    print("STEP 6 MATRIX SUM FOLLOWS: the 24 proper rotations average to 0 on vectors and on the "
          "even-axis (quadrupole) plane, so one site's six-outcome odds have no linear content-blind singlet. "
          "Not the first break")


def main():
    step1()
    step2()
    step3()
    step4()
    step5()
    rotations()
    print("SUMMARY: fails at step 4 - the massless claim V ~ -(5/4) u^2 ~ -0.098/r^2 does not follow from the step's own inputs: "
          "u = G/G(0) ~ 1/(4*pi*G(0)*r) with Watson G(0)=0.2527310098 gives the prefactor (5/4)/(4*pi*G(0))^2 = 0.12393/r^2; "
          "0.098 is exactly (5/4)*(0.28)^2, the task's 27^3 window, not that amplitude. "
          "Steps 1-3 do follow for purely vector leans (orders 1 and 3 vanish, order 2 is 3 l1^2 sum_{y<y'} m.m', "
          "parallel form 1+(e2+e4+e6)/3, and the 5^3 rationals at (5,2,4) match); the linear-regime far constant there is "
          "585/529 along an axis and 610/529 on the diagonal, not 45 l1^2 = 405/529")


if __name__ == "__main__":
    main()
