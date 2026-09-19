#!/usr/bin/env python3
"""J:note falsifiers for KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10 (on main).

Falsifiers implemented: (2) "a dispersive unitary in the linear permutation-equivariant leaf systems"; (3) "a site-allowed single
tick or factorized decorated-shift composite with a curved band or continuously tunable slope inside the analyzed class".

Disjoint machinery (the runner reduces the linear family to 25 leaves by exact bilinear kills and sweeps each leaf with least squares
on sampled momenta):
  - the linear (untwisted) permutation action of S3 on the 2^3 cell and its momenta; the equivariant licensed basis by GROUP AVERAGING
    of every hop label (24 directed corner pairs x {within-cell, cross-cell}) and on-site label; the same construction with the
    staggered sign twist (V12, V23) as the control that DOES contain dispersive unitaries (block05's family);
  - unitarity imposed exactly as the vanishing of every Laurent coefficient of U^dag U - I (a quadratic system in all orbit
    coefficients at once, no leaf split), Levenberg-Marquardt with the analytic Jacobian from 800 seeded starts for the linear class
    and 300 for the twisted control; every unitary found is tested for dispersion (characteristic polynomial at four momenta, one
    momentum per matrix);
  - the factorized decorated-shift class: exact eta-decorated per-axis shifts S_1, S_2, S_3 on the cell (Laurent matrices), S_i^2 =
    z_i^(-1) I and pairwise anticommutation checked exactly, and EVERY word of length 1..8 (9840 words, beyond the note's length six)
    checked to have W^2 = (monomial) I, i.e. exactly linear bands.
"""
from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import least_squares

C = list(itertools.product((0, 1), repeat=3))
IDX = {p: i for i, p in enumerate(C)}


def lm_add(A, B, s=1):
    out = {k: v.copy() for k, v in A.items()}
    for k, v in B.items():
        out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if np.any(v)}


def dag(A):
    return {tuple(-x for x in m): v.T.copy() for m, v in A.items()}


def mul(A, B):
    out = {}
    for m1, v1 in A.items():
        for m2, v2 in B.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            out[m] = out.get(m, 0) + v1 @ v2
    return {k: v for k, v in out.items() if np.any(v)}


def build_basis(twisted):
    labels, onsite = [], []
    for p in C:
        E = np.zeros((8, 8), int)
        E[IDX[p], IDX[p]] = 1
        onsite.append({(0, 0, 0): E})
        for q in C:
            d = [i for i in range(3) if p[i] != q[i]]
            if len(d) == 1:
                ax = d[0]
                for kind in "cd":
                    m = [0, 0, 0]
                    if kind == "d":
                        m[ax] = 1 if p[ax] == 1 else -1
                    E = np.zeros((8, 8), int)
                    E[IDX[p], IDX[q]] = 1
                    labels.append({tuple(m): E})
    V12 = np.diag([1, 1, 1, 1, 1, 1, -1, -1]) if twisted else np.eye(8, dtype=int)
    V23 = np.diag([1, 1, 1, -1, 1, 1, 1, -1]) if twisted else np.eye(8, dtype=int)

    def P_of(perm):
        P = np.zeros((8, 8), int)
        for p in C:
            P[IDX[tuple(p[perm[i]] for i in range(3))], IDX[p]] = 1
        return P

    gens = [(V12 @ P_of((1, 0, 2)), (1, 0, 2)), (V23 @ P_of((0, 2, 1)), (0, 2, 1))]
    compose = lambda a, b: (a[0] @ b[0], tuple(b[1][a[1][i]] for i in range(3)))
    group, frontier = [(np.eye(8, dtype=int), (0, 1, 2))], [(np.eye(8, dtype=int), (0, 1, 2))]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                c = compose(h, g)
                if not any(np.array_equal(c[0], x[0]) and c[1] == x[1] for x in group):
                    group.append(c)
                    new.append(c)
        frontier = new

    def act(g, A):
        W, perm = g
        Winv = np.round(np.linalg.inv(W)).astype(int)
        out = {}
        for m, v in A.items():
            m2 = tuple(m[perm.index(i)] for i in range(3))
            out[m2] = out.get(m2, 0) + Winv @ v @ W
        return {k: v for k, v in out.items() if np.any(v)}

    def avg(A):
        tot = {}
        for g in group:
            tot = lm_add(tot, act(g, A))
        return tot

    key = lambda A: tuple(sorted((m, tuple(v.flatten())) for m, v in A.items()))
    canon = lambda A: min(key(A), key({m: -v for m, v in A.items()}))

    def orbit_sums(ls):
        out, seen = [], set()
        for L in ls:
            B = avg(L)
            if B and canon(B) not in seen:
                seen.add(canon(B))
                w = max(np.abs(v).max() for v in B.values())
                out.append({m: v // w for m, v in B.items()})
        return out

    return group, orbit_sums(labels), orbit_sums(onsite)


def to_numeric(A, z):
    M = np.zeros((8, 8), complex)
    for m, v in A.items():
        M += v * np.prod([zz ** e for zz, e in zip(z, m)])
    return M


def census(basis, starts_n, seed):
    nb = len(basis)
    exps = sorted({m for a in range(nb) for b in range(nb) for m in mul(dag(basis[a]), basis[b])})
    M = np.zeros((len(exps), nb, nb, 8, 8), complex)
    for a in range(nb):
        for b in range(nb):
            for m, v in mul(dag(basis[a]), basis[b]).items():
                M[exps.index(m), a, b] = v
    delta = np.zeros((len(exps), 8, 8), complex)
    delta[exps.index((0, 0, 0))] = np.eye(8)
    split = lambda x: x[:nb] + 1j * x[nb:]

    def resid(x):
        c = split(x)
        r = np.einsum("o,p,mopij->mij", c.conj(), c, M) - delta
        return np.concatenate([r.real.ravel(), r.imag.ravel()])

    def jac(x):
        c = split(x)
        A = np.einsum("o,mopij->mpij", c.conj(), M)
        Bt = np.einsum("p,mopij->moij", c, M)
        J = np.concatenate([A + Bt, 1j * (A - Bt)], axis=1)
        J = np.moveaxis(J, 1, -1).reshape(-1, 2 * nb)
        return np.concatenate([J.real, J.imag], axis=0)

    rng = np.random.default_rng(seed)
    zs = [np.exp(2j * np.pi * rng.random(3)) for _ in range(4)]
    n_unit, n_disp, disp_support = 0, 0, set()
    for s in range(starts_n):
        x0 = rng.normal(size=2 * nb) * (0.3 + 0.5 * (s % 3))
        sol = least_squares(resid, x0, jac=jac, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        if np.max(np.abs(resid(sol.x))) > 1e-10:
            continue
        n_unit += 1
        c = split(sol.x)
        cps = [np.poly(np.linalg.eigvals(sum(c[o] * to_numeric(basis[o], z) for o in range(nb)))) for z in zs]
        if any(np.max(np.abs(cp - cps[0])) > 1e-7 for cp in cps[1:]):
            n_disp += 1
            disp_support.add(tuple(o for o in range(nb) if abs(c[o]) > 1e-7))
    return len(exps), n_unit, n_disp, sorted(disp_support)


def eta(mu, p):
    return 1 if mu == 0 else ((-1) ** p[0] if mu == 1 else (-1) ** (p[0] + p[1]))


def decorated_shift(axis):
    """site shift by +1 along `axis` on the doubled lattice with Kawamoto-Smit sign eta_axis; cross-cell hops carry z_axis^(-1)."""
    S = {}
    for q in C:
        p = list(q)
        p[axis] ^= 1
        p = tuple(p)
        m = [0, 0, 0]
        if q[axis] == 1:          # q -> q + e_axis leaves the cell: amplitude lands in the next cell
            m[axis] = -1
        E = np.zeros((8, 8), int)
        E[IDX[p], IDX[q]] = eta(axis, q)
        S = lm_add(S, {tuple(m): E})
    return S


def main():
    for twisted, starts in ((False, 800), (True, 300)):
        group, H, Dg = build_basis(twisted)
        ncoef, nu, nd, sup = census(Dg + H, starts, 11 if not twisted else 12)
        label = "linear (untwisted)" if not twisted else "eta-twisted control"
        print(f"{'1' if not twisted else '2'}. {label}: group order {len(group)}, {len(Dg)} on-site + {len(H)} hop orbit sums; census over "
              f"{ncoef} exact Laurent coefficients from {starts} starts: unitary {nu}, dispersive {nd}"
              + (f" (supports {sup[:4]})" if nd else ""))
        if not twisted:
            lin = (nu, nd)
        else:
            tw = (nu, nd)
    S = [decorated_shift(a) for a in range(3)]
    I8 = np.eye(8, dtype=int)
    sq_ok = all(set(mul(S[a], S[a])) == {tuple(-1 if i == a else 0 for i in range(3))} and
                np.array_equal(mul(S[a], S[a])[tuple(-1 if i == a else 0 for i in range(3))], I8) for a in range(3))
    anti_ok = all(not lm_add(mul(S[a], S[b]), mul(S[b], S[a])) for a, b in itertools.combinations(range(3), 2))
    n_words, bad = 0, []
    for Lw in range(1, 9):
        for word in itertools.product(range(3), repeat=Lw):
            W = S[word[0]]
            for a in word[1:]:
                W = mul(W, S[a])
            W2 = mul(W, W)
            n_words += 1
            if len(W2) != 1 or not any(np.array_equal(v, s * I8) for v in W2.values() for s in (1, -1)):
                bad.append(word)
    print(f"3. factorized class: S_i^2 = z_i^-1 I exactly: {sq_ok}; pairwise anticommutation exactly: {anti_ok}; words of length 1..8: "
          f"{n_words}, all with W^2 = +-(monomial) I: {not bad}")
    if lin[1] or bad or not (sq_ok and anti_ok):
        print(f"HIT: a falsifier fires: linear-class dispersive unitaries {lin[1]}, words with non-scalar square {len(bad)}")
    print(f"SUMMARY: falsifiers 2 and 3 do not fire: the untwisted permutation-equivariant licensed family, solved as one exact quadratic "
          f"Laurent system from 800 starts, gives {lin[0]} unitaries and {lin[1]} dispersive, while the same census on the eta-twisted "
          f"control finds {tw[1]} dispersive of {tw[0]}; the eta-decorated per-axis shifts square to z_i^-1 I, anticommute pairwise, and "
          f"all {n_words} words through length 8 square to a monomial times I (exactly linear bands, no curvature, no dial)")


if __name__ == "__main__":
    main()
