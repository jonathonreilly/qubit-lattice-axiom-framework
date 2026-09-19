#!/usr/bin/env python3
"""Probe: UT_PLACEMENT_TABLE_AND_SPECIES_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-11.

The note's table rests on three cone constants (H-kernel 1 site/tau; family
cone 1/sqrt(3) site/tick, "RE-DERIVED from the 8x8 walk matrix" by one-sided
numeric phase tracking along 5 random directions at phases zero) and on
Part E (the family's symmetric point is an odd drift, so the E3 cones are
the only comparison loci; third falsifier: "a family comparison locus other
than the E3 cones evading Part E's odd-vs-even obstruction").  Machinery
disjoint from the runner (which uses a sympy limit, numeric eigenphase
tracking, and the cosine-law FORMULA for Part E):

 H  exact Laurent-polynomial arithmetic (Fraction coefficients in
    z_mu = e^{i k_mu}): the staggered Bloch kernel D = iR satisfies
    R^dagger = -R and D^2 = sum_mu (2 - z_mu - 1/z_mu)/4 I identically; the
    exact Hessian of D^2 at k = 0 gives the slope in every direction.
 F1 the family matrix W = sqrt3 U rebuilt from its orbit definition: exact
    Laurent identities W W^dagger = 3 I and W^2 + (W^dagger)^2 =
    sum_mu (z_mu + 1/z_mu) I (the sigma law, for EVERY eigenvalue, whole BZ).
 F2 exact arithmetic in the cyclotomic field Q(zeta_24) (x^8 - x^4 + 1):
    spectral projectors at both touching points k = 0 and k = (pi,pi,pi);
    first-order operators B_mu = P(-i lambda^-1 dU/dk_mu)P; the isotropic
    cone is B_mu^2 = P/12 and B_mu B_nu + B_nu B_mu = 0 (mu != nu) exactly.
 E1 Q(zeta_24) exact at k0 = psi(1,1,1), psi in {pi/3, pi/2, 2pi/3} (phases
    zero; the runner used the formula at psi = 0.7 and 1): projectors onto
    the four eigenvalues +-e^{+-i psi/2}; P B_mu P = s/6 P for every mu —
    a pure drift, odd, first order.
 E2 beyond the runner's phases-zero object: the FULL six-phase family
    (unitary for every phase, checked): at k = 0 for 300 random moduli the
    first-order form on every eigenspace; an off-diagonal degeneracy search
    over the Brillouin zone for 40 random moduli (400 local minimizations
    of the smallest gap outside a tube of radius 0.2 around the diagonal
    nodal line); the extra degeneracies on the diagonal located for 12
    random moduli and their first-order forms classified (cone rate).
 F3 numeric rate on 2000 random directions at both touching points.
 C  1/sqrt3 irrational; tick/tau = 1/sqrt3 needed; the per-axis row 1 = 1.

Prints SUMMARY: lines; HIT: only when a stated constant or Part E fails, or a
comparison locus with a non-drift first-order form is found off the E3 cones.
"""
import itertools
import sys
import time
from collections import deque
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import minimize

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


comps = list(itertools.product((0, 1), repeat=3))
idx = {p: i for i, p in enumerate(comps)}


def eta_val(mu, p):
    return 1 if mu == 0 else ((-1) ** p[0] if mu == 1 else (-1) ** (p[0] + p[1]))


# ---------------------------------------------------------------- Laurent polys
def lp_add(a, b, s=1):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) + s * c
        if out[e] == 0:
            del out[e]
    return out


def lp_mul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = (e1[0] + e2[0], e1[1] + e2[1], e1[2] + e2[2])
            out[e] = out.get(e, 0) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def lm_mul(A, B):
    n = len(A)
    C = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if not A[i][k]:
                continue
            for j in range(n):
                if B[k][j]:
                    C[i][j] = lp_add(C[i][j], lp_mul(A[i][k], B[k][j]))
    return C


def lm_dagger(A):
    """conjugate transpose on the unit torus for REAL coefficients: z -> 1/z, transpose."""
    n = len(A)
    return [[{(-e[0], -e[1], -e[2]): c for e, c in A[j][i].items()} for j in range(n)] for i in range(n)]


def lm_eq(A, B):
    return all(lp_add(A[i][j], B[i][j], -1) == {} for i in range(len(A)) for j in range(len(A)))


def lm_scalar(p, n=8):
    return [[dict(p) if i == j else {} for j in range(n)] for i in range(n)]


def hessian_at_zero(p):
    """f(k) = sum_e c_e e^{i e.k}: d^2 f / dk_mu dk_nu at 0 = -sum c_e e_mu e_nu."""
    return [[-sum(c * e[m] * e[n] for e, c in p.items()) for n in range(3)] for m in range(3)]


def unit(mu, s):
    e = [0, 0, 0]
    e[mu] = s
    return tuple(e)


# ---------------------------------------------------------------------------- H
def run_H():
    print("=" * 78)
    print("H  staggered Bloch kernel, exact Laurent arithmetic")
    R = [[{} for _ in range(8)] for _ in range(8)]
    for p in comps:
        for mu in range(3):
            q = list(p)
            q[mu] ^= 1
            q = tuple(q)
            php = {unit(mu, 1): Fr(1)} if p[mu] == 1 else {(0, 0, 0): Fr(1)}
            phm = {unit(mu, -1): Fr(1)} if p[mu] == 0 else {(0, 0, 0): Fr(1)}
            term = {e: Fr(eta_val(mu, p), 2) * c for e, c in lp_add(php, phm, -1).items()}
            R[idx[p]][idx[q]] = lp_add(R[idx[p]][idx[q]], term)
    # D = i R ; D^dagger = -i R^dagger ; D Hermitian <=> R^dagger = -R
    Rd = lm_dagger(R)
    herm = lm_eq(Rd, [[{e: -c for e, c in R[i][j].items()} for j in range(8)] for i in range(8)])
    D2 = [[{e: -c for e, c in x.items()} for x in row] for row in lm_mul(R, R)]      # D^2 = -R^2
    target = {}
    for mu in range(3):
        target = lp_add(target, {(0, 0, 0): Fr(1, 2), unit(mu, 1): Fr(-1, 4), unit(mu, -1): Fr(-1, 4)})
    ok = lm_eq(D2, lm_scalar(target))
    Hs = hessian_at_zero(target)
    iso = all(Hs[m][n] == (Fr(1, 2) if m == n else 0) for m in range(3) for n in range(3))
    # E^2 = k^T (Hs/2) k + O(k^4) = |k|^2/4 = |kappa|^2 (kappa = k/2): slope 1/2 per cell momentum, 1 per site momentum
    slope_cell = Fr(1, 2) if iso else None
    v_H = 2 * slope_cell if iso else None
    print(f"  R^dagger = -R (D Hermitian): {herm}; D^2 = sum_mu (2 - z_mu - 1/z_mu)/4 I identically: {ok}; "
          f"Hessian of E^2 at 0 = {[[str(x) for x in r] for r in Hs]} -> E = |k|/2 + O(k^3) in every direction; v_H = {v_H} site/tau")
    if not (herm and ok and iso and v_H == 1):
        hit("the H-kernel's cone is not the isotropic 1 site/tau")
    return herm, ok, v_H


# ---------------------------------------------------------------------------- family
def build_family():
    g12, g23 = (1, 0, 2), (0, 2, 1)
    v12 = [1, 1, 1, 1, 1, 1, -1, -1]
    v23 = [1, 1, 1, -1, 1, 1, 1, -1]
    pairs = []
    for p in comps:
        for q in comps:
            if sum(abs(p[i] - q[i]) for i in range(3)) == 1:
                ax = [i for i in range(3) if p[i] != q[i]][0]
                pairs.append((p, q, ax, +1 if p[ax] == 1 else -1))
    pair_at = {(p, q): i for i, (p, q, ax, s) in enumerate(pairs)}

    def act(g, vv, kind, i):
        p, q, ax, s = pairs[i]
        return (kind, pair_at[(tuple(p[g[j]] for j in range(3)), tuple(q[g[j]] for j in range(3)))], vv[idx[p]] * vv[idx[q]])
    seen = set()
    orbs = []
    for lab in [("c", i) for i in range(24)] + [("d", i) for i in range(24)]:
        if lab in seen:
            continue
        orb = {lab: 1}
        dq = deque([lab])
        cons = True
        while dq:
            cur = dq.popleft()
            for g, vv in ((g12, v12), (g23, v23)):
                kind, j, sign = act(g, vv, cur[0], cur[1])
                val = orb[cur] * sign
                if (kind, j) in orb:
                    cons &= orb[(kind, j)] == val
                else:
                    orb[(kind, j)] = val
                    dq.append((kind, j))
        seen |= set(orb)
        if cons:
            orbs.append(orb)
    active = (1, 2, 5, 6, 9, 10)
    # per active orbit: integer pieces (constant, e^{+ik_mu}, e^{-ik_mu})
    per = []
    for j in active:
        C0 = np.zeros((8, 8), int)
        Ap = np.zeros((3, 8, 8), int)
        Am = np.zeros((3, 8, 8), int)
        for (kind, i2), sign in orbs[j].items():
            p, q, ax, sgn = pairs[i2]
            if kind == "d":
                (Ap if sgn > 0 else Am)[ax][idx[p], idx[q]] += sign
            else:
                C0[idx[p], idx[q]] += sign
        per.append((C0, Ap, Am))
    return per, len(orbs)


def family_pieces(per, phis):
    C = sum(np.exp(1j * phis[t]) * per[t][0] for t in range(6)) / np.sqrt(3)
    Ap = sum(np.exp(1j * phis[t]) * per[t][1] for t in range(6)) / np.sqrt(3)
    Am = sum(np.exp(1j * phis[t]) * per[t][2] for t in range(6)) / np.sqrt(3)
    return C, Ap, Am


def U_batch(K, P):
    C, Ap, Am = P
    e = np.exp(1j * K)
    U = np.broadcast_to(C, (K.shape[0], 8, 8)).astype(complex)
    for mu in range(3):
        U += e[:, mu, None, None] * Ap[mu] + (1 / e[:, mu])[:, None, None] * Am[mu]
    return U


def U_one(kv, P):
    return U_batch(np.array(kv, float)[None, :], P)[0]


def dU_one(kv, P, mu):
    C, Ap, Am = P
    return 1j * Ap[mu] * np.exp(1j * kv[mu]) - 1j * Am[mu] * np.exp(-1j * kv[mu])


def run_F1(per):
    print("=" * 78)
    print("F1 family at phases zero: exact Laurent identities (unitarity, the sigma law)")
    C0 = sum(pp[0] for pp in per)
    Ap = sum(pp[1] for pp in per)
    Am = sum(pp[2] for pp in per)
    W = [[{} for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            d = {}
            if C0[i, j]:
                d[(0, 0, 0)] = int(C0[i, j])
            for mu in range(3):
                if Ap[mu][i, j]:
                    d = lp_add(d, {unit(mu, 1): int(Ap[mu][i, j])})
                if Am[mu][i, j]:
                    d = lp_add(d, {unit(mu, -1): int(Am[mu][i, j])})
            W[i][j] = d
    Wd = lm_dagger(W)
    uni = lm_eq(lm_mul(W, Wd), lm_scalar({(0, 0, 0): 3}))
    sig = {}
    for mu in range(3):
        sig = lp_add(sig, {unit(mu, 1): 1, unit(mu, -1): 1})
    W2 = lm_mul(W, W)
    Wd2 = lm_mul(Wd, Wd)
    law = lm_eq([[lp_add(W2[i][j], Wd2[i][j]) for j in range(8)] for i in range(8)], lm_scalar(sig))
    # 3(U^2 + U^-2) = sum(z + 1/z): with U^2 = e^{2i theta}: 6 cos(2 theta) = 2 sum cos k_mu ->
    # Hessian: -24 theta^2 ... expand: 6(1 - 2 theta^2) = 6 - |k|^2  =>  theta^2 = |k|^2/12
    Hs = hessian_at_zero(sig)                   # = -I (sum cos k_mu ~ 3 - |k|^2/2, times 2)
    theta2_coeff = [[-Fr(Hs[m][n], 2) / 12 for n in range(3)] for m in range(3)]
    iso = all(theta2_coeff[m][n] == (Fr(1, 12) if m == n else 0) for m in range(3) for n in range(3))
    print(f"  W W^dagger = 3 I identically: {uni}; W^2 + (W^dagger)^2 = sum_mu (z_mu + 1/z_mu) I identically: {law}")
    print(f"  so every eigenvalue lambda = e^{{i theta}} obeys 6 cos(2 theta) = 2 sum_mu cos k_mu on the whole zone; "
          f"theta^2 = k^T A k + O(k^4) with A = {[[str(x) for x in r] for r in theta2_coeff]}: theta = +-|k|/(2 sqrt3) at k = 0 for ALL 8 bands")
    if not (uni and law and iso):
        hit("the family matrix fails unitarity or the isotropic |k|/(2 sqrt3) cone at phases zero")
    return uni, law, iso, (C0, Ap, Am)


# ------------------------------------------------------------- Q(zeta_24) arithmetic
N_Z = 8          # phi(24); zeta^8 = zeta^4 - 1


def z_red(c):
    c = list(c)
    for d in range(len(c) - 1, 7, -1):
        if c[d]:
            c[d - 4] += c[d]
            c[d - 8] -= c[d]
            c[d] = 0
    return tuple(c[:8]) + (0,) * (8 - len(c[:8]))


def z_pow(m):
    m %= 24
    c = [0] * 24
    c[m] = 1
    # zeta^12 = -1 first
    for d in range(23, 11, -1):
        if c[d]:
            c[d - 12] -= c[d]
            c[d] = 0
    return z_red(c[:12])


ZERO = (0,) * 8
ONE = z_pow(0)


def z_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def z_neg(a):
    return tuple(-x for x in a)


def z_scale(a, r):
    return tuple(x * r for x in a)


def z_mul(a, b):
    c = [0] * 15
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[i + j] += x * y
    return z_red(c)


SQRT3 = z_add(z_pow(2), z_pow(22))            # 2 cos(pi/6)
I_ = z_pow(6)
assert z_mul(SQRT3, SQRT3) == z_scale(ONE, 3) and z_mul(I_, I_) == z_neg(ONE)


def zm_mul(A, B):
    n = len(A)
    C = [[ZERO] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a == ZERO:
                continue
            for j in range(n):
                b = B[k][j]
                if b != ZERO:
                    C[i][j] = z_add(C[i][j], z_mul(a, b))
    return C


def zm_add(A, B, s=1):
    return [[z_add(A[i][j], z_scale(B[i][j], s)) for j in range(len(A))] for i in range(len(A))]


def zm_scal(A, a):
    return [[z_mul(A[i][j], a) for j in range(len(A))] for i in range(len(A))]


def zm_eye(n=8, a=ONE):
    return [[a if i == j else ZERO for j in range(n)] for i in range(n)]


def zm_is_zero(A):
    return all(x == ZERO for row in A for x in row)


def zm_trace(A):
    t = ZERO
    for i in range(len(A)):
        t = z_add(t, A[i][i])
    return t


def zm_from_int(M):
    return [[z_scale(ONE, Fr(int(M[i, j]))) for j in range(8)] for i in range(8)]


def family_exact(pieces, zexp):
    """sqrt3 U and sqrt3 dU/dk_mu at k_mu = 2 pi zexp_mu / 24 (phases zero), exact in Q(zeta_24)."""
    C0, Ap, Am = pieces
    W = zm_from_int(C0)
    dW = []
    for mu in range(3):
        zp, zm = z_pow(zexp[mu]), z_pow(-zexp[mu])
        W = zm_add(W, zm_add(zm_scal(zm_from_int(Ap[mu]), zp), zm_scal(zm_from_int(Am[mu]), zm)))
        dW.append(zm_scal(zm_add(zm_scal(zm_from_int(Ap[mu]), zp), zm_scal(zm_from_int(Am[mu]), zm), -1), I_))
    inv3 = Fr(1, 3)
    U = zm_scal(W, z_scale(SQRT3, inv3))                      # W / sqrt3 = W sqrt3 / 3
    dU = [zm_scal(d, z_scale(SQRT3, inv3)) for d in dW]
    return U, dU


def run_F2(pieces):
    print("=" * 78)
    print("F2 exact first-order operators at the two touching points (Q(zeta_24) arithmetic)")
    res = []
    all_ok = True
    for name, ze, lams in (("k=0", (0, 0, 0), (0, 12)), ("k=(pi,pi,pi)", (12, 12, 12), (6, 18))):
        U, dU = family_exact(pieces, ze)
        U2 = zm_mul(U, U)
        lam0 = z_pow(lams[0])
        minpoly = zm_is_zero(zm_add(U2, zm_eye(8, z_mul(lam0, lam0)), -1))     # U^2 = lambda^2 I
        for le in lams:
            lam, lamb = z_pow(le), z_pow(-le)
            P = zm_scal(zm_add(zm_eye(), zm_scal(U, lamb)), z_scale(ONE, Fr(1, 2)))     # (I + lambda^-1 U)/2
            idem = zm_mul(P, P) == P
            rank = zm_trace(P)
            A = [zm_scal(d, z_mul(z_neg(I_), lamb)) for d in dU]                    # -i lambda^-1 dU
            B = [zm_mul(zm_mul(P, a), P) for a in A]
            sq = all(zm_mul(B[m], B[m]) == zm_scal(P, z_scale(ONE, Fr(1, 12))) for m in range(3))
            anti = all(zm_is_zero(zm_add(zm_mul(B[m], B[n]), zm_mul(B[n], B[m]))) for m in range(3) for n in range(m + 1, 3))
            herm = all(B[m] == [[tuple(Fr(x) for x in conj(B[m][j][i])) for j in range(8)] for i in range(8)] for m in range(3))
            ok = minpoly and idem and rank == z_scale(ONE, 4) and sq and anti and herm
            all_ok &= ok
            res.append((name, le, ok))
            print(f"  {name}: U^2 = lambda^2 I {minpoly}; eigenvalue zeta^{le}: projector idempotent {idem}, trace {rank[0]}; "
                  f"B_mu Hermitian {herm}; B_mu^2 = P/12 {sq}; B_mu B_nu + B_nu B_mu = 0 {anti}")
    print("  => on each rank-4 eigenspace M(n) = sum n_mu B_mu has M(n)^2 = |n|^2/12: phase rate +-|n|/(2 sqrt3) exactly, every direction")
    if not all_ok:
        hit("the exact first-order operators at a touching point are not the isotropic 1/(2 sqrt3) cone")
    return all_ok


def conj(a):
    """complex conjugation in Q(zeta_24): zeta -> zeta^-1."""
    out = ZERO
    for i, x in enumerate(a):
        if x:
            out = z_add(out, z_scale(z_pow(-i), x))
    return out


def run_E1(pieces):
    print("=" * 78)
    print("E1 exact first-order forms at the symmetric-point translates k0 = psi(1,1,1), phases zero")
    res = []
    all_ok = True
    for psi_e, psi_name in ((4, "pi/3"), (6, "pi/2"), (8, "2pi/3")):
        U, dU = family_exact(pieces, (psi_e, psi_e, psi_e))
        # eigenvalues +- e^{+- i psi/2}: exponents in zeta_24 units
        h = psi_e // 2
        lam_e = [h, -h, h + 12, -h + 12]
        prod = zm_eye()
        for le in lam_e:
            prod = zm_mul(prod, zm_add(U, zm_eye(8, z_pow(le)), -1))
        minpoly = zm_is_zero(prod)
        drifts = []
        for le in lam_e:
            Q = zm_eye()
            c = ONE
            for lo in lam_e:
                if lo != le:
                    Q = zm_mul(Q, zm_add(U, zm_eye(8, z_pow(lo)), -1))
                    c = z_mul(c, z_add(z_pow(le), z_neg(z_pow(lo))))
            idem = zm_mul(Q, Q) == zm_scal(Q, c)                         # Q = c P
            tr_ok = zm_trace(Q) == z_scale(c, 2)                          # rank 2
            A = [zm_scal(d, z_mul(z_neg(I_), z_pow(-le))) for d in dU]
            s_found = None
            for s in (1, -1):
                if all(zm_mul(zm_mul(Q, a), Q) == zm_scal(Q, z_scale(c, Fr(s, 6))) for a in A):
                    s_found = s
            ok = idem and tr_ok and s_found is not None
            all_ok &= ok and minpoly
            drifts.append(s_found)
        res.append((psi_name, minpoly, drifts))
        print(f"  psi = {psi_name}: prod (U - lambda) = 0 {minpoly}; for eigenvalues e^{{i pi m/12}}, m = {lam_e}: rank 2 and "
              f"P B_mu P = s/6 P with s = {drifts} (a pure drift s(1,1,1)/6, odd)")
    if not all_ok:
        hit("the family's first-order form at the symmetric-point translate is not a pure drift")
    return res, all_ok


def clusters(kv, P, tol):
    U = U_one(kv, P)
    w, V = np.linalg.eig(U)
    used = [False] * 8
    out = []
    for i in range(8):
        if used[i]:
            continue
        c = [j for j in range(8) if not used[j] and abs(w[j] - w[i]) < tol]
        for j in c:
            used[j] = True
        lam = w[c].mean()
        Qm, _ = np.linalg.qr(V[:, c])
        Ms = [Qm.conj().T @ (-1j / lam * dU_one(np.array(kv, float), P, mu)) @ Qm for mu in range(3)]
        out.append((len(c), lam, Ms))
    return out


def mingap(Us):
    w = np.linalg.eigvals(Us)
    d = np.abs(w[:, :, None] - w[:, None, :]) + 10 * np.eye(8)[None]
    return d.reshape(len(w), -1).min(1)


def dperp(K):
    u = (K[:, 0] - K[:, 1] + np.pi) % (2 * np.pi) - np.pi
    v = (K[:, 1] - K[:, 2] + np.pi) % (2 * np.pi) - np.pi
    w = (K[:, 2] - K[:, 0] + np.pi) % (2 * np.pi) - np.pi
    return np.sqrt((u * u + v * v + w * w) / 3)


def run_E2(per):
    print("=" * 78)
    print("E2 the full six-phase family (beyond the runner's phases-zero object)")
    rng = np.random.default_rng(20260611)
    # unitarity for arbitrary phases
    uni = 0.0
    for _ in range(50):
        P = family_pieces(per, rng.uniform(0, 2 * np.pi, 6))
        U = U_one(rng.uniform(-np.pi, np.pi, 3), P)
        uni = max(uni, np.abs(U @ U.conj().T - np.eye(8)).max())
    # (a) symmetric point k = 0, 300 random moduli
    worst_scal, worst_grad, sizes = 0.0, 0.0, set()
    for _ in range(300):
        P = family_pieces(per, rng.uniform(0, 2 * np.pi, 6))
        for sz, lam, Ms in clusters((0, 0, 0), P, 1e-7):
            sizes.add(sz)
            for M in Ms:
                worst_scal = max(worst_scal, np.abs(M - np.trace(M) / sz * np.eye(sz)).max())
                worst_grad = max(worst_grad, abs(abs(np.trace(M).real / sz) - 1 / 6))
    print(f"  unitarity for 50 random (phases, k): {uni:.1e}; k = 0 at 300 random moduli: eigenspace sizes {sorted(sizes)}; "
          f"max deviation of every first-order operator from a scalar {worst_scal:.1e}; max ||grad_mu| - 1/6| {worst_grad:.1e}")
    if worst_scal > 1e-8 or worst_grad > 1e-8:
        hit("the full family's symmetric-point first-order form is not a pure odd drift at some moduli")
    # (b) off-diagonal degeneracy search: multi-start local minimization of the smallest eigenvalue gap in the
    # region d >= 0.2 (d = distance to the diagonal line); a barrier keeps the search out of the tube.  An off-diagonal
    # degeneracy shows up as an INTERIOR local minimum with gap -> 0; minima that end on the barrier are the gap
    # decreasing toward the (known) diagonal nodal line.
    D0 = 0.2
    n_starts, n_interior, n_barrier, n_interior_zero = 0, 0, 0, 0
    min_interior, min_barrier = np.inf, np.inf
    cone_off = False
    for _ in range(40):
        P = family_pieces(per, rng.uniform(0, 2 * np.pi, 6))

        def f(k):
            d = dperp(k[None, :])[0]
            return mingap(U_batch(k[None, :], P))[0] + (100 * (D0 - d) if d < D0 else 0.0)
        for _s in range(10):
            k0 = rng.uniform(-np.pi, np.pi, 3)
            while dperp(k0[None, :])[0] < 0.3:
                k0 = rng.uniform(-np.pi, np.pi, 3)
            r = minimize(f, k0, method="Nelder-Mead", options=dict(xatol=1e-11, fatol=1e-14, maxiter=4000))
            n_starts += 1
            d = dperp(r.x[None, :])[0]
            gap = mingap(U_batch(r.x[None, :], P))[0]
            if d > D0 + 1e-3:
                n_interior += 1
                min_interior = min(min_interior, gap)
                if gap < 1e-7:
                    n_interior_zero += 1
                    for sz, lam, Ms in clusters(r.x, P, 1e-6):
                        if sz > 1 and max(np.abs(Ms[a] @ Ms[b] - Ms[b] @ Ms[a]).max() for a in range(3) for b in range(3)) > 1e-6:
                            cone_off = True
            else:
                n_barrier += 1
                min_barrier = min(min_barrier, gap)
    print(f"  off-diagonal search (40 random moduli x 10 starts, Nelder-Mead on the smallest gap in d >= {D0}): {n_interior} interior "
          f"local minima (smallest gap {("%.2e" % min_interior) if n_interior else "none"}; {n_interior_zero} below 1e-7), {n_barrier} ended on the barrier d = {D0} "
          f"(gap decreasing toward the diagonal; smallest there {min_barrier:.1e})")
    if cone_off:
        hit("a degeneracy off the diagonal with a non-drift first-order form (a comparison locus other than the E3 cones)")
    best_R, gx, dx, best_gap_far = min_interior, n_interior_zero, n_interior, min_barrier
    # (c) extra degeneracies on the diagonal and their first-order forms
    ts = np.linspace(-np.pi, np.pi, 3001)
    n_pts, n_cone_clusters, worst_cone, worst_iso, other = 0, 0, 0.0, 0.0, 0
    dirs = rng.normal(size=(200, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    for _ in range(12):
        P = family_pieces(per, rng.uniform(0, 2 * np.pi, 6))

        def ndistinct_gap(t, tol=1e-6):
            th = np.sort(np.angle(np.linalg.eigvals(U_one((t, t, t), P))))
            reps = [th[0]]
            for x in th[1:]:
                if abs(x - reps[-1]) > tol:
                    reps.append(x)
            if len(reps) > 1 and abs(reps[0] + 2 * np.pi - reps[-1]) < tol:
                reps = reps[:-1]
            r = np.array(reps)
            return np.diff(np.concatenate([r, [r[0] + 2 * np.pi]])).min()
        gv = np.array([ndistinct_gap(t) for t in ts])
        mins = [i for i in range(1, len(ts) - 1) if gv[i] <= gv[i - 1] and gv[i] <= gv[i + 1] and gv[i] < 1e-2]
        for i in mins:
            # the colliding pair: minimize the smallest gap among eigenvalues not in a persistent double
            def f(t):
                th = np.sort(np.angle(np.linalg.eigvals(U_one((t, t, t), P))))
                d = np.abs(th[:, None] - th[None, :])
                d = np.minimum(d, 2 * np.pi - d) + 10 * np.eye(8)
                s = np.sort(d[np.triu_indices(8, 1)])
                return s[2]                              # two persistent doubles at 0; the third-smallest gap closes
            a, b = ts[i - 1], ts[i + 1]
            for _ in range(120):
                m1, m2 = a + (b - a) * 0.382, a + (b - a) * 0.618
                if f(m1) < f(m2):
                    b = m2
                else:
                    a = m1
            t = (a + b) / 2
            n_pts += 1
            for sz, lam, Ms in clusters((t, t, t), P, 1e-5):
                if sz < 2:
                    continue
                comm = max(np.abs(Ms[x] @ Ms[y] - Ms[y] @ Ms[x]).max() for x in range(3) for y in range(3))
                if comm < 1e-6:
                    continue
                n_cone_clusters += 1
                evs = np.array([np.sort(np.linalg.eigvalsh(sum(n[m] * Ms[m] for m in range(3)))) for n in dirs])
                drift = dirs.sum(1) / 6
                for j in range(sz):
                    dd = min(np.abs(evs[:, j] - drift).max(), np.abs(evs[:, j] + drift).max())
                    cc = np.abs(np.abs(evs[:, j]) - 1 / (2 * np.sqrt(3))).max()
                    if dd < 1e-4:
                        continue
                    worst_cone = max(worst_cone, cc)
                    if cc > 1e-4:
                        other += 1
                # isotropy: the non-drift eigenvalues equal +-|n|/(2 sqrt3) for every n (unit n)
                worst_iso = max(worst_iso, np.abs(np.abs(evs[:, 0]) - 1 / (2 * np.sqrt(3))).max())
    print(f"  diagonal (12 random moduli, 3001-point scan + golden refinement): {n_pts} extra-degeneracy points, "
          f"{n_cone_clusters} non-commuting (cone-type) eigenspaces; their non-drift first-order eigenvalues equal "
          f"+-|n|/(2 sqrt3) on 200 directions within {worst_cone:.1e} ({other} other eigenvalues)")
    if other:
        hit("a cone-type first-order eigenvalue at the family's diagonal degeneracies is not +-|n|/(2 sqrt3) (moduli rigidity)")
    return uni, worst_scal, worst_grad, sorted(sizes), best_R, gx, dx, best_gap_far, n_pts, n_cone_clusters, worst_cone, other


def run_F3(pieces):
    print("=" * 78)
    print("F3 numeric phase rate on 2000 random directions at both touching points (runner: 5 at k = 0)")
    C0, Ap, Am = pieces
    P = (C0 / np.sqrt(3), Ap / np.sqrt(3), Am / np.sqrt(3))
    rng = np.random.default_rng(2026)
    worst = {}
    for name, k0 in (("k=0", np.zeros(3)), ("k=(pi,pi,pi)", np.pi * np.ones(3))):
        lam0 = np.linalg.eigvals(U_one(k0, P))
        w = 0.0
        for _ in range(2000):
            d = rng.normal(size=3)
            d /= np.linalg.norm(d)
            t = 1e-6
            lam = np.linalg.eigvals(U_one(k0 + t * d, P))
            # match each eigenvalue to the nearest unperturbed one; rate = phase difference / t
            rates = [abs(np.angle(l / lam0[np.argmin(np.abs(lam0 - l))])) / t for l in lam]
            w = max(w, max(abs(r - 1 / (2 * np.sqrt(3))) for r in rates))
        worst[name] = w
    print(f"  max |rate - 1/(2 sqrt3)| over all 8 bands: " + "; ".join(f"{k}: {v:.1e}" for k, v in worst.items()))
    if max(worst.values()) > 1e-5:
        hit("numeric phase rate differs from 1/(2 sqrt3)")
    return worst


def run_C():
    print("=" * 78)
    print("C  the table's arithmetic")
    # 1/sqrt3 = p/q  <=>  q^2 = 3 p^2: the 3-adic valuation of q^2 is even, of 3p^2 odd — never equal
    val3 = lambda n: 0 if n % 3 else 1 + val3(n // 3)
    parity = all(val3(q * q) % 2 == 0 and val3(3 * p * p) % 2 == 1 for p in range(1, 300) for q in range(1, 300))
    near = min(abs(Fr(p, q) ** 2 - Fr(1, 3)) for q in range(1, 300) for p in range(1, q))
    print(f"  1/sqrt3 rational would need q^2 = 3 p^2: 3-adic parities differ for all p, q < 300: {parity} "
          f"(min |(p/q)^2 - 1/3| over q < 300: {float(near):.2e} > 0); the family row matches only at tick/tau = 1/sqrt3; "
          f"the per-axis row at tick = tau (1 = 1)")
    if not parity or near == 0:
        hit("the family-to-H ratio is rational")
    return parity, near


def main():
    t0 = time.time()
    herm, ok, v_H = run_H()
    summary(f"H exact Laurent arithmetic: D Hermitian {herm}, D^2 = sum_mu (2 - z_mu - 1/z_mu)/4 I identically {ok}, "
            f"Hessian isotropic -> v_H = {v_H} site/tau in every direction")
    per, norbs = build_family()
    uni, law, iso, pieces = run_F1(per)
    summary(f"F1 family (phases zero; {norbs} consistent orbits, active 1,2,5,6,9,10): W W^dagger = 3I {uni}; the sigma law "
            f"W^2 + W^dagger^2 = sum(z + 1/z) I identically {law}; every band theta = +-|k|/(2 sqrt3) + O(k^3): {iso}")
    f2 = run_F2(pieces)
    summary(f"F2 exact Q(zeta_24) projectors at k = 0 and (pi,pi,pi): rank-4 eigenspaces with B_mu^2 = P/12 and anticommuting "
            f"B_mu: {f2} -> isotropic cone rate 1/(2 sqrt3) per cell momentum = 1/sqrt3 site/tick (cell = 2 sites)")
    worst = run_F3(pieces)
    summary(f"F3 numeric rate, 2000 directions, all 8 bands: max deviation {max(worst.values()):.1e}")
    e1, e1ok = run_E1(pieces)
    summary(f"E1 exact symmetric-point translates psi(1,1,1), psi = pi/3, pi/2, 2pi/3: every rank-2 eigenspace carries "
            f"P B_mu P = s/6 P (s = " + "; ".join(f"{r[0]}: {r[2]}" for r in e1) + f"), a pure odd drift: {e1ok}")
    (uni6, wsc, wgr, sizes, bR, gx, dx, gfar, npts, ncone, wcone, other) = run_E2(per)
    summary(f"E2 full six-phase family (unitary to {uni6:.0e}): at k = 0 over 300 moduli every eigenspace (sizes {sizes}) is a pure "
            f"drift with |grad_mu| = 1/6 (scalar deviation {wsc:.0e}, gradient deviation {wgr:.0e}); off the diagonal "
            f"(d >= 0.2, 400 local minimizations) {dx} interior local minima (smallest gap {("%.2e" % bR) if dx else "none"}; {gx} below 1e-7), "
            f"the rest ending on the barrier (smallest gap there {gfar:.1e}); "
            f"on the diagonal {npts} extra degeneracies at 12 moduli, {ncone} cone-type eigenspaces, cone eigenvalues "
            f"+-|n|/(2 sqrt3) within {wcone:.0e} ({other} exceptions)")
    parity, near = run_C()
    summary(f"C 1/sqrt3 irrational (3-adic parity for p, q < 300: {parity}; nearest square {float(near):.1e} from 1/3); "
            f"the natural row 1 = 1")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
