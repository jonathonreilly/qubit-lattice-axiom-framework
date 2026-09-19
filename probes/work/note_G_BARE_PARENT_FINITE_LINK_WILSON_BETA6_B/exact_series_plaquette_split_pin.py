#!/usr/bin/env python3
"""Probe: G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.

Machinery disjoint from the runner (numerical matrix exponentials, principal
logarithm, Richardson extrapolation in a): EXACT formal power series in a with
matrix coefficients over Q(i) (sympy Rational/I), for SU(N_c) with
N_c = 2, 3, 4 (the note's statements are written for general N_c; the runner
works at N_c = 3).

Lattice data: C_mu(x) = A, C_nu(x) = B, C_nu(x + a mu) = B + a D1,
C_mu(x + a nu) = A + a D2 with A, B, D1, D2 traceless Hermitian over Q(i)
(so Delta_mu C_nu = D1, Delta_nu C_mu = D2 exactly).

 T1  U_P = e^{iaA} e^{ia(B + aD1)} e^{-ia(A + aD2)} e^{-iaB} as an exact series
     to a^5; log U_P exact to a^5: the a^1 coefficient vanishes, the a^2
     coefficient equals i(D1 - D2 + i[A, B]) = i F[C; 1] (unit weights), and
     F is traceless Hermitian (in the canonical generator span); the a^3
     coefficient is reported.
 T3  1 - Re Tr U_P / N_c exactly to a^5: a^0..a^3 vanish and the a^4
     coefficient equals Tr(F^2)/(2 N_c) = F^a F^a/(4 N_c) with Tr(T_a T_b) =
     delta_ab/2; hence beta gamma^2/(4 N_c) = 1/2 gives gamma*^2 = 2 N_c/beta.
 T2  split (gamma, C/gamma) for 6 exact gamma per instance (negative, fractional): links
     equal as exact series, gamma F[C/gamma; gamma] = F[C; 1] exactly.
 P   pin: on beta = k/10, k = 1..400, the positive root gamma*(beta) equals
     s = 1 exactly at beta = 2 N_c only (N_c = 2..6); the beta = 24 exhibit.

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import random
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

HITS = []
I = sp.I


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


K = 5   # series order in a


def rand_herm_traceless(n, rng, den=4):
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            z = sp.Rational(rng.randint(-4, 4), den) + I * sp.Rational(rng.randint(-4, 4), den)
            M[i, j] = z
            M[j, i] = sp.conjugate(z)
    d = [sp.Rational(rng.randint(-4, 4), den) for _ in range(n - 1)]
    for i in range(n - 1):
        M[i, i] = d[i]
    M[n - 1, n - 1] = -sum(d)
    return M


def s_mul(X, Y, n):
    out = [sp.zeros(n, n) for _ in range(K + 1)]
    for i, Xi in enumerate(X):
        if Xi.is_zero_matrix:
            continue
        for j, Yj in enumerate(Y):
            if i + j > K or Yj.is_zero_matrix:
                continue
            out[i + j] += Xi * Yj
    return [sp.expand(m) for m in out]


def s_exp(X, n):
    """exp of a series with zero constant term"""
    out = [sp.eye(n)] + [sp.zeros(n, n) for _ in range(K)]
    P = [sp.eye(n)] + [sp.zeros(n, n) for _ in range(K)]
    for k in range(1, K + 1):
        P = s_mul(P, X, n)
        out = [o + p / sp.factorial(k) for o, p in zip(out, P)]
    return [sp.expand(m) for m in out]


def s_log(U, n):
    E = [sp.zeros(n, n)] + U[1:]           # U = 1 + E
    out = [sp.zeros(n, n) for _ in range(K + 1)]
    P = [sp.eye(n)] + [sp.zeros(n, n) for _ in range(K)]
    for k in range(1, K + 1):
        P = s_mul(P, E, n)
        out = [o + sp.Rational((-1) ** (k + 1), k) * p for o, p in zip(out, P)]
    return [sp.expand(m) for m in out]


def series_arg(n, lin, quad=None, sign=1):
    """sign * i * (a lin + a^2 quad)"""
    X = [sp.zeros(n, n) for _ in range(K + 1)]
    X[1] = sign * I * lin
    if quad is not None:
        X[2] = sign * I * quad
    return X


def plaquette(A, B, D1, D2, n):
    f1 = s_exp(series_arg(n, A), n)
    f2 = s_exp(series_arg(n, B, D1), n)
    f3 = s_exp(series_arg(n, A, D2, sign=-1), n)
    f4 = s_exp(series_arg(n, B, sign=-1), n)
    return s_mul(s_mul(s_mul(f1, f2, n), f3, n), f4, n)


def F_of(A, B, D1, D2, g=1):
    return sp.expand(D1 - D2 + I * g * (A * B - B * A))


def run(n_inst=3, seed=20260919):
    rng = random.Random(seed)
    res = {}
    for N in (2, 3, 4):
        bad1 = bad_span = bad3 = bad2 = 0
        a3norms = []
        for inst in range(n_inst):
            A, B, D1, D2 = (rand_herm_traceless(N, rng) for _ in range(4))
            U = plaquette(A, B, D1, D2, N)
            Lg = s_log(U, N)
            F = F_of(A, B, D1, D2)
            if not Lg[0].is_zero_matrix or not Lg[1].is_zero_matrix:
                bad1 += 1
            if not sp.expand(Lg[2] - I * F).is_zero_matrix:
                bad1 += 1
            if not (sp.expand(F - F.H).is_zero_matrix and sp.expand(F.trace()) == 0):
                bad_span += 1
            a3norms.append(max(abs(complex(v)) for v in Lg[3]))
            # Wilson density 1 - Re Tr U / N
            tr = [sp.expand(m.trace()) for m in U]
            dens = [sp.expand((N if k == 0 else 0) - sp.re(tr[k])) / N for k in range(K + 1)]
            dens = [sp.expand(d) for d in dens]
            want4 = sp.expand((F * F).trace() / (2 * N))
            # F^a F^a with Tr(T_a T_b) = delta_ab / 2 equals 2 Tr(F^2)
            if any(sp.simplify(dens[k]) != 0 for k in range(4)) or sp.simplify(dens[4] - want4) != 0:
                bad3 += 1
            # T2 split: gamma F[C/gamma; gamma] = F[C; 1], links equal as exact series
            for g in (sp.Rational(1, 3), sp.Rational(-2, 5), 2, -7, sp.Rational(11, 13), sp.Rational(-1, 9)):
                Fs = F_of(A / g, B / g, D1 / g, D2 / g, g)
                if not sp.expand(g * Fs - F).is_zero_matrix:
                    bad2 += 1
                link1 = s_exp(series_arg(N, g * (A / g)), N)
                link0 = s_exp(series_arg(N, A), N)
                if any(not sp.expand(x - y).is_zero_matrix for x, y in zip(link1, link0)):
                    bad2 += 1
        res[N] = (bad1, bad_span, bad3, bad2, max(a3norms))
        print(f"  N_c={N}: {n_inst} exact instances; log U_P a^1 = 0 and a^2 = i F[C;1] failures {bad1}; F traceless "
              f"Hermitian failures {bad_span}; Wilson density a^0..a^3 = 0 and a^4 = Tr F^2/(2N_c) = F^aF^a/(4N_c) failures "
              f"{bad3}; split identities (6 gamma x link and field strength) failures {bad2}; max |a^3 coefficient of log U_P| = {res[N][4]:.4f}")
        if bad1 or bad_span:
            hit(f"N_c={N}: plaquette exponent is not a^2 F[C;1] + O(a^3) in the canonical generator span")
        if bad3:
            hit(f"N_c={N}: Wilson density a^4 coefficient differs from F^aF^a/(4N_c)")
        if bad2:
            hit(f"N_c={N}: a split changed a link or gamma F[C/gamma;gamma] != F[C;1]")
    return res


def run_pin():
    print("=" * 78)
    print("P  pin equivalence and the beta = 24 exhibit")
    bad = 0
    eq_points = {}
    for N in range(2, 7):
        eq = []
        for k in range(1, 401):
            beta = Fr(k, 10)
            g2 = Fr(2 * N) / beta                      # gamma*^2 = 2 N_c / beta
            # the positive root equals s = 1 iff g2 == 1 (both positive)
            if g2 == 1:
                eq.append(beta)
            # W-PHYS relation beta gamma^2 / (4 N_c) = 1/2
            if beta * g2 / (4 * N) != Fr(1, 2):
                bad += 1
        eq_points[N] = eq
        if eq != [Fr(2 * N)]:
            bad += 1
    g2_24 = Fr(6, 24)
    ok24 = g2_24 == Fr(1, 4) and sp.sqrt(sp.Rational(1, 4)) == sp.Rational(1, 2) and 24 * Fr(1, 4) == 6
    print(f"  beta = k/10, k = 1..400: equality points {dict((N, [str(b) for b in v]) for N, v in eq_points.items())}; "
          f"W-PHYS relation failures {bad}; beta = 24: gamma*^2 = {g2_24}, gamma* = 1/2, 24 * 1/4 = 6: {ok24}")
    if bad or not ok24:
        hit("pin equivalence or the beta = 24 exhibit fails")
    return eq_points, ok24


def main():
    t0 = time.time()
    print("=" * 78)
    print("T1/T2/T3  exact series in a for SU(N_c), N_c = 2, 3, 4")
    res = run()
    summary("T1-T3 exact series: " + "; ".join(
        f"N_c={N}: exponent a^1=0, a^2=iF[C;1] failures {r[0]}, span failures {r[1]}, Wilson a^4 = F^aF^a/(4N_c) failures "
        f"{r[2]}, split failures {r[3]}, max |a^3 exponent coefficient| {r[4]:.3f}" for N, r in res.items()))
    eq, ok24 = run_pin()
    summary(f"P pin: gamma*(beta) = 1 on the grid only at beta = 2N_c ({', '.join(f'N_c={N}: {[str(b) for b in v]}' for N, v in eq.items())}); "
            f"beta = 24 exhibit gamma*^2 = 1/4, gamma* = 1/2: {ok24}")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
