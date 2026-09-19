#!/usr/bin/env python3
"""J:note falsifier for REALIZATION_ROW_SIGMA_RECONCILIATION_BOUNDED_THEOREM_NOTE_2026-06-11 (on main).

Falsifier implemented (the note's first, inherited from block05's census surface): "a licensed dispersive equivariant cell outside
the six-orbit family whose symmetric-point gradient vector lies outside the computed discrete set"; plus the proof step the note's
reconciliation rests on (its Part A global factorization, from which the sigma law, the translation identity and the drift follow),
verified literally at exact rational points.

Disjoint machinery (the runners build orbits by breadth-first sign propagation, verify Part A by one symbolic expansion, and census
by least squares on sampled momenta with ~90 starts):
  1. the eta-twisted S3 action W = V P (block05's V12, V23 and the corner/axis permutations) closed into its group; the equivariant
     licensed basis by GROUP AVERAGING of every hop label and on-site label (Laurent matrices in z1, z2, z3 with integer entries);
  2. the six-orbit subfamilies found intrinsically: all 6-subsets of hop orbits that are unitary for ALL phases (pairwise
     B_o^dag B_o' = 0 and sum B_o^dag B_o = 3 I as Laurent identities);
  3. Part A's identity e3^2 det(mu - sqrt3 U) = 9 Q_A(X) Q_B(X), X = mu^2/3, checked EXACTLY over the Gaussian rationals at 60 random
     rational points of the torus and of the phase torus for every such subfamily (the pairing of phases into alpha, beta, gamma is
     identified first by a numerical scan of all 90 assignments);
  4. the census, beyond block05's size: the full 16-orbit equivariant licensed family (4 on-site + 12 hop orbits, 32 real
     parameters), unitarity imposed EXACTLY as the vanishing of every Laurent coefficient of U^dag U - I, Levenberg-Marquardt with
     the analytic Jacobian from 600 seeded starts; every unitary found is classified (dispersive?, inside a six-orbit subfamily?),
     and for dispersive cells outside, the symmetric-point band slopes along the three axes and the diagonal are computed.
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp
from scipy.optimize import least_squares
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

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


def build_basis():
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
    V12 = np.diag([1, 1, 1, 1, 1, 1, -1, -1])
    V23 = np.diag([1, 1, 1, -1, 1, 1, 1, -1])

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

    H, Dg = orbit_sums(labels), orbit_sums(onsite)
    equiv = all(key(act(g, B)) == key(B) for g in group for B in H + Dg)
    return group, H, Dg, equiv


def to_numeric(A, z):
    M = np.zeros((8, 8), complex)
    for m, v in A.items():
        M += v * np.prod([zz ** e for zz, e in zip(z, m)])
    return M


def pyth_points(n, rng):
    trip = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53)]
    out = []
    for _ in range(n):
        a, b, c = trip[rng.integers(len(trip))]
        if rng.integers(2):
            a, b = b, a
        out.append(sp.Rational(int(a) * (1 - 2 * int(rng.integers(2))), c) + sp.I * sp.Rational(int(b) * (1 - 2 * int(rng.integers(2))), c))
    return out


def main():
    group, H, Dg, equiv = build_basis()
    print(f"1. eta-twisted action closes to a group of order {len(group)}; group-averaged licensed basis: {len(Dg)} on-site + {len(H)} hop "
          f"orbits, all equivariant {equiv}")
    orth = np.array([[a != b and not mul(dag(H[a]), H[b]) for b in range(len(H))] for a in range(len(H))])
    fams = []
    for S in itertools.combinations(range(len(H)), 6):
        if all(orth[a, b] for a, b in itertools.combinations(S, 2)):
            tot = {}
            for a in S:
                tot = lm_add(tot, mul(dag(H[a]), H[a]))
            if set(tot) == {(0, 0, 0)} and np.array_equal(tot[(0, 0, 0)], 3 * np.eye(8, dtype=int)):
                fams.append(S)
    print(f"2. six-orbit subsets unitary for all phases (amplitude 1/sqrt3): {fams}")

    rng = np.random.default_rng(11)
    PAIRINGS = [((0, 1), (2, 3), (4, 5)), ((0, 1), (2, 4), (3, 5)), ((0, 1), (2, 5), (3, 4)), ((0, 2), (1, 3), (4, 5)),
                ((0, 2), (1, 4), (3, 5)), ((0, 2), (1, 5), (3, 4)), ((0, 3), (1, 2), (4, 5)), ((0, 3), (1, 4), (2, 5)),
                ((0, 3), (1, 5), (2, 4)), ((0, 4), (1, 2), (3, 5)), ((0, 4), (1, 3), (2, 5)), ((0, 4), (1, 5), (2, 3)),
                ((0, 5), (1, 2), (3, 4)), ((0, 5), (1, 3), (2, 4)), ((0, 5), (1, 4), (2, 3))]

    def U_num(S, u, z):
        return sum(u[i] * to_numeric(H[S[i]], z) for i in range(6)) / np.sqrt(3)

    def is_dispersive(S):
        u = np.exp(2j * np.pi * rng.random(6))
        cps = [np.poly(np.linalg.eigvals(U_num(S, u, np.exp(2j * np.pi * rng.random(3))))) for _ in range(4)]
        return any(np.max(np.abs(cp - cps[0])) > 1e-8 for cp in cps[1:])

    disp_fams = [S for S in fams if is_dispersive(S)]
    flat_fams = [S for S in fams if S not in disp_fams]
    print(f"   dispersive among them: {disp_fams}; flat (characteristic polynomial independent of z): {flat_fams}")

    def e123(z):
        return z[0] + z[1] + z[2], z[0] * z[1] + z[0] * z[2] + z[1] * z[2], z[0] * z[1] * z[2]

    ident = {}
    for S in disp_fams:
        best = None
        for orient in (1, -1):   # -1: the identity read at k -> -k (z -> 1/z), the mirror orientation
            for pairing in PAIRINGS:
                for roles in itertools.permutations(range(3)):
                    err = 0.0
                    for _ in range(3):
                        u = np.exp(2j * np.pi * rng.random(6))
                        z = np.exp(2j * np.pi * rng.random(3))
                        prs = [u[pairing[j][0]] * u[pairing[j][1]] for j in range(3)]
                        al, be, ga = prs[roles[0]], prs[roles[1]], prs[roles[2]]
                        e1, e2, e3 = e123(z ** orient)
                        QA = np.poly1d([3 * e3, -(al * e2 + be * e3 * e1), 3 * al * be * e3])
                        QB = np.poly1d([3 * e3, -(ga * e2 + be * e3 * e1), 3 * be * ga * e3])
                        cpX = np.poly(np.linalg.eigvals(U_num(S, u, z)))[::2]
                        err = max(err, np.abs((np.poly1d(cpX * 9 * e3 * e3) - QA * QB).coeffs).max())
                    if best is None or err < best[0]:
                        best = (err, orient, pairing, roles)
        ident[S] = best
    print("   numerical identification (orientation, pairing, roles) of Part A per dispersive subset: "
          + "; ".join(f"{S}: orientation {'k' if b[1] == 1 else '-k'}, pairing {b[2]}, roles {b[3]}, err {b[0]:.1e}" for S, b in ident.items()))

    exact = {}
    Xs = sp.Symbol("X")
    for S in disp_fams:
        err, orient, pairing, roles = ident[S]
        ok_all = True
        for t in range(60):
            zs = pyth_points(3, rng)
            us = pyth_points(6, rng)
            Vm = sp.zeros(8, 8)
            for i in range(6):
                for m, v in H[S[i]].items():
                    mono = sp.Integer(1)
                    for zz, e in zip(zs, m):
                        mono *= zz ** e if e >= 0 else sp.conjugate(zz) ** (-e)   # |z| = 1: z^-1 = conj(z), exact
                    Vm += us[i] * mono * sp.Matrix(v.tolist())
            dM = DomainMatrix.from_Matrix(Vm.applyfunc(sp.expand)).convert_to(QQ_I)
            cp = [QQ_I.to_sympy(c) for c in dM.charpoly()]  # det(mu - V), V = sqrt3 U, degree 8
            odd_zero = all(sp.expand(cp[k]) == 0 for k in range(1, 9, 2))
            prs = [us[pairing[j][0]] * us[pairing[j][1]] for j in range(3)]
            al, be, ga = prs[roles[0]], prs[roles[1]], prs[roles[2]]
            zo = zs if orient == 1 else [sp.conjugate(zz) for zz in zs]
            e1, e2, e3 = e123(zo)
            QA = 3 * Xs ** 2 * e3 - Xs * (al * e2 + be * e3 * e1) + 3 * al * be * e3
            QB = 3 * Xs ** 2 * e3 - Xs * (ga * e2 + be * e3 * e1) + 3 * be * ga * e3
            cpX = sum(cp[8 - 2 * j] * (3 * Xs) ** j for j in range(5))  # mu^(2j) = (3X)^j
            ok_all &= odd_zero and sp.expand(e3 ** 2 * cpX - 9 * QA * QB) == 0
        exact[S] = (ok_all, "k" if orient == 1 else "-k")
    print(f"3. Part A identity e3^2 det(mu - sqrt3 U) = 9 Q_A Q_B (X = mu^2/3), exact over QQ_I at 60 random rational points per "
          f"dispersive subset: {exact}")

    def slopes(S, u, k0, dq=1e-6):
        ev0 = np.linalg.eigvals(U_num(S, u, np.exp(1j * k0)))
        cands = np.linspace(0, 2 * np.pi, 97)[:-1]
        rot = np.exp(1j * max(cands, key=lambda t: np.min(np.abs(ev0 * np.exp(1j * t) + 1))))
        cols = []
        for d in np.eye(3):
            up = np.sort(np.angle(rot * np.linalg.eigvals(U_num(S, u, np.exp(1j * (k0 + dq * d))))))
            dn = np.sort(np.angle(rot * np.linalg.eigvals(U_num(S, u, np.exp(1j * (k0 - dq * d))))))
            cols.append((up - dn) / (2 * dq))
        return sorted({tuple(np.round(r, 4)) for r in np.array(cols).T})

    grads = {}
    for S in disp_fams:
        u = np.exp(2j * np.pi * rng.random(6))
        grads[S] = slopes(S, u, np.zeros(3))
    print(f"   symmetric-point (k = 0) band gradient vectors at generic phases: {grads}")

    # census
    basis = Dg + H
    nb = len(basis)
    exps = sorted({m for a in range(nb) for b in range(nb) for m in mul(dag(basis[a]), basis[b])})
    M = np.zeros((len(exps), nb, nb, 8, 8), complex)
    for a in range(nb):
        for b in range(nb):
            for m, v in mul(dag(basis[a]), basis[b]).items():
                M[exps.index(m), a, b] = v
    delta = np.zeros((len(exps), 8, 8), complex)
    delta[exps.index((0, 0, 0))] = np.eye(8)

    def split(x):
        return x[:nb] + 1j * x[nb:]

    def resid(x):
        c = split(x)
        r = np.einsum("o,p,mopij->mij", c.conj(), c, M) - delta
        return np.concatenate([r.real.ravel(), r.imag.ravel()])

    def jac(x):
        c = split(x)
        A = np.einsum("o,mopij->mpij", c.conj(), M)
        Bt = np.einsum("p,mopij->moij", c, M)
        dx = A + Bt
        dy = 1j * (A - Bt)
        J = np.concatenate([dx, dy], axis=1)  # (m, 2nb, 8, 8)
        J = np.moveaxis(J, 1, -1).reshape(-1, 2 * nb)
        return np.concatenate([J.real, J.imag], axis=0)

    rngc = np.random.default_rng(2026)
    starts = [rngc.normal(size=2 * nb) * s for s in (0.3, 0.5, 0.8) for _ in range(160)]
    for S in fams:
        base = np.zeros(2 * nb)
        ph = np.exp(2j * np.pi * rngc.random(6)) / np.sqrt(3)
        for i, o in enumerate(S):
            base[len(Dg) + o] = ph[i].real
            base[nb + len(Dg) + o] = ph[i].imag
        starts += [base + a * rngc.normal(size=2 * nb) for a in (0.05, 0.2, 0.4) for _ in range(10)]
    zs_test = [np.exp(2j * np.pi * rngc.random(3)) for _ in range(4)]
    found = []
    for x0 in starts:
        sol = least_squares(resid, x0, jac=jac, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        if np.max(np.abs(resid(sol.x))) < 1e-10:
            found.append(split(sol.x))
    n_unit = len(found)
    disp, in_fam, outside, by_subset = 0, 0, [], {}
    for c in found:
        U = lambda z: sum(c[o] * to_numeric(basis[o], z) for o in range(nb))
        cps = [np.poly(np.linalg.eigvals(U(z))) for z in [np.ones(3)] + zs_test]
        dsp = any(np.max(np.abs(cp - cps[0])) > 1e-7 for cp in cps[1:])   # flat iff the characteristic polynomial is z-independent
        if not dsp:
            continue
        disp += 1
        member = [S for S in fams if all(abs(c[o]) < 1e-7 for o in range(nb) if o not in [len(Dg) + s for s in S]) and
                  all(abs(abs(c[len(Dg) + s]) - 1 / np.sqrt(3)) < 1e-7 for s in S)]
        if member:
            in_fam += 1
            by_subset[member[0]] = by_subset.get(member[0], 0) + 1
        else:
            support = tuple(o for o in range(nb) if abs(c[o]) > 1e-7)
            slopes = []
            dq = 1e-5
            ev0 = np.linalg.eigvals(U(np.ones(3)))
            cands = np.linspace(0, 2 * np.pi, 97)[:-1]
            rot = np.exp(1j * max(cands, key=lambda t: np.min(np.abs(ev0 * np.exp(1j * t) + 1))))   # keep phases off the branch cut
            for dirn in (np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]), np.ones(3) / np.sqrt(3)):
                up = np.sort(np.angle(rot * np.linalg.eigvals(U(np.exp(1j * dq * dirn)))))
                dn = np.sort(np.angle(rot * np.linalg.eigvals(U(np.exp(-1j * dq * dirn)))))
                slopes.append(sorted({round(abs(v), 4) for v in (up - dn) / (2 * dq)}))
            outside.append((support, [round(abs(c[o]), 4) for o in support], slopes))
    print(f"4. census of the full 16-orbit equivariant licensed family ({2 * nb} real parameters, {len(exps)} Laurent coefficients of "
          f"U^dag U - I imposed exactly, {len(starts)} Levenberg-Marquardt starts): unitary {n_unit}, dispersive {disp}, inside a "
          f"six-orbit subset {in_fam} (by subset {by_subset}), dispersive outside {len(outside)}")
    for o in outside[:12]:
        print(f"   outside: support {o[0]} moduli {o[1]}; |slopes| at k = 0 along x, y, z, diagonal: {o[2]}")
    allowed = {0.1667, 0.2887}
    new_grad = [o for o in outside if not all(set(s) <= allowed for s in o[2])]
    family_grads_ok = all(all(abs(abs(x) - 1 / 6) < 1e-3 for row in g for x in row) and all(len(set(np.sign(row))) == 1 for row in g)
                          for g in grads.values())
    bad_A = [S for S, (ok, _) in exact.items() if not ok]
    if bad_A or not disp_fams or not equiv:
        print(f"HIT: Part A's global factorization fails in both orientations for dispersive six-orbit subset(s) {bad_A}")
    if new_grad:
        print(f"HIT: {len(new_grad)} dispersive equivariant unitary cells outside the six-orbit subsets have symmetric-point slopes "
              f"outside {{1/6, 1/(2 sqrt3)}}: first {new_grad[0]}")
    print(f"SUMMARY: the group-averaged construction reproduces block05's 4 on-site + 12 hop orbits; {len(fams)} six-orbit subsets are "
          f"unitary for all phases, {len(flat_fams)} of them flat and {len(disp_fams)} dispersive; Part A's factorization holds exactly at 60 "
          f"rational points for each dispersive subset ({', '.join(f'{S}: {o}' for S, (ok, o) in exact.items() if ok)}; the '-k' one is "
          f"the mirror copy), both with k = 0 gradient vectors +-(1,1,1)/6 ({family_grads_ok}); the exact-coefficient census "
          f"({len(starts)} starts, beyond block05's ~90) found {n_unit} unitaries, {disp} dispersive, all {in_fam} inside those subsets "
          f"({by_subset}) and {len(outside)} outside, so falsifier 1 does not fire")


if __name__ == "__main__":
    main()
