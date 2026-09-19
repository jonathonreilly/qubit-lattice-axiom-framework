#!/usr/bin/env python3
"""J:note falsifiers for STACK_SPECTRAL_TRANSCRIPTION_WEAK_REGISTRATION_FAITHFUL_LIMIT_BOUNDED_THEOREM_NOTE_2026-06-11 (on main).

Falsifiers implemented: (1) the displacement and dephasing forms; (2) "a simulated stack covariance deviating from M(eps)^n
structure"; (3) "a nonzero eps^2 coefficient in g(eps)"; (4) "an oscillatory transcription inside the window or an overdamped one
well outside it (would refute the window law)".

The runner simulates 12-layer stacks in floating point, recovers (r, omega_eps) by Prony, and tests the window only at omega = omega_c/2
and 3 omega_c. Here, disjoint and exact:
  - the stack is simulated in exact Gaussian-rational arithmetic (QQ_I amplitudes) at parameter points where cos(omega/2),
    sin(omega/2), cos(eps), sin(eps) are rational (Pythagorean), 7 layers, both branches of the maximally mixed system state; the
    connected record-record covariance k[d] is computed exactly and the M(eps) structure is tested as the exact two-term recurrence
    k[d+2] = tr(M) k[d+1] - det(M) k[d] with tr M = cos(omega)(1 + cos 2eps), det M = cos 2eps;
  - the character of the transcription is read off exactly from the discriminant tr(M)^2 - 4 det(M): negative = complex roots
    (oscillatory), positive = real roots (overdamped); the full condition for oscillation is |cos omega| g(eps) < 1, so besides the
    infrared window omega < omega_c(eps) there is a zone-edge window omega > pi - omega_c(eps) of the same width, where the roots are
    real and NEGATIVE (the covariance alternates in sign with two decay rates; the frequency locks to pi);
  - the displacement identity and the sigma_x-dephasing channel symbolically; the series of g(eps).
"""
from __future__ import annotations

from fractions import Fraction as Fr
from math import acos, pi, sqrt

import sympy as sp
from sympy.polys.domains import QQ_I

ZERO, ONE = QQ_I(0, 0), QQ_I(1, 0)


def conj(z):
    return QQ_I(z.x, -z.y)


def apply(psi, n, op, sites):
    """apply a 2^k x 2^k operator (list of lists of QQ_I) on the given qubit sites (site 0 = most significant)."""
    k = len(sites)
    out = [ZERO] * len(psi)
    shifts = [n - 1 - s for s in sites]
    for idx, amp in enumerate(psi):
        if amp == ZERO:
            continue
        col = 0
        for sh in shifts:
            col = (col << 1) | ((idx >> sh) & 1)
        base = idx
        for sh in shifts:
            base &= ~(1 << sh)
        for row in range(2 ** k):
            c = op[row][col]
            if c == ZERO:
                continue
            tgt = base
            for j, sh in enumerate(shifts):
                if (row >> (k - 1 - j)) & 1:
                    tgt |= 1 << sh
            out[tgt] = out[tgt] + c * amp
    return out


def inner(a, b):
    tot = ZERO
    for x, y in zip(a, b):
        if x != ZERO and y != ZERO:
            tot = tot + conj(x) * y
    return tot


X = [[ZERO, ONE], [ONE, ZERO]]


def stack_cov(cw2, sw2, ce, se, N):
    n = N + 1
    u = [[QQ_I(cw2, -sw2), ZERO], [ZERO, QQ_I(cw2, sw2)]]      # exp(-i omega sigma_z / 2)
    # V = cos(eps) I - i sin(eps) sigma_x (x) sigma_y is real: sigma_x (x) sigma_y has entries -i, i, -i, i at (0,3), (1,2), (2,1), (3,0)
    c, s = QQ_I(ce, 0), QQ_I(se, 0)
    V = [[c, ZERO, ZERO, -s], [ZERO, c, s, ZERO], [ZERO, -s, c, ZERO], [s, ZERO, ZERO, c]]
    branches = []
    for s0 in (0, 1):
        psi = [ZERO] * (2 ** n)
        psi[s0 << N] = ONE
        for t in range(N):
            psi = apply(psi, n, u, [0])
            psi = apply(psi, n, V, [0, t + 1])
        branches.append(psi)

    def avg(ops):
        tot = Fr(0)
        for psi in branches:
            phi = psi
            for site in ops:
                phi = apply(phi, n, X, [site])
            re = sp.re(QQ_I.to_sympy(inner(psi, phi)))
            tot += Fr(int(re.p), int(re.q))
        return tot / 2

    m = [avg([j]) for j in range(1, N + 1)]
    return [avg([1, d + 1]) - m[0] * m[d] if d > 0 else avg([1, 1]) - m[0] * m[0] for d in range(N)]


def main():
    e, w = sp.symbols("epsilon omega", real=True)
    SX, SY, SZ = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    G = sp.kronecker_product(SX, SY)
    Vs = sp.cos(e) * sp.eye(4) - sp.I * sp.sin(e) * G
    Xa = sp.kronecker_product(sp.eye(2), SX)
    disp = sp.simplify(Vs.H * Xa * Vs - (sp.cos(2 * e) * Xa + sp.sin(2 * e) * sp.kronecker_product(SX, SZ))) == sp.zeros(4, 4)
    ket0 = sp.Matrix([1, 0])
    chan = {}
    for name, P in (("sx", SX), ("sy", SY), ("sz", SZ)):
        out = Vs * sp.kronecker_product(P, ket0 * ket0.T) * Vs.H
        red = sp.Matrix(2, 2, lambda i, j: out[2 * i, 2 * j] + out[2 * i + 1, 2 * j + 1])
        chan[name] = sp.simplify(red)
    deph = (sp.simplify(chan["sx"] - SX) == sp.zeros(2, 2) and sp.simplify(chan["sy"] - sp.cos(2 * e) * SY) == sp.zeros(2, 2)
            and sp.simplify(chan["sz"] - sp.cos(2 * e) * SZ) == sp.zeros(2, 2))
    g = (1 + sp.cos(2 * e)) / (2 * sp.sqrt(sp.cos(2 * e)))
    ser = sp.series(g, e, 0, 7).removeO()
    print(f"1. symbolic: V^dag X^a V = cos2e X^a + sin2e sx (x) Z^a: {disp}; induced channel = sigma_x dephasing (1, cos2e, cos2e): "
          f"{deph}; g(eps) = {sp.expand(ser)} (eps^2 coefficient {ser.coeff(e, 2)})")
    cases = [("weak eps, omega near pi", Fr(96, 2305), Fr(2303, 2305), Fr(24, 25), Fr(7, 25)),
             ("weak eps, omega mid-band", Fr(3, 5), Fr(4, 5), Fr(24, 25), Fr(7, 25)),
             ("weak eps, omega in the infrared window", Fr(2303, 2305), Fr(96, 2305), Fr(24, 25), Fr(7, 25)),
             ("strong eps, omega = 2.57", Fr(7, 25), Fr(24, 25), Fr(4, 5), Fr(3, 5))]
    N = 7
    results = []
    for name, cw2, sw2, ce, se in cases:
        k = stack_cov(cw2, sw2, ce, se, N)
        c2 = ce * ce - se * se
        cw = cw2 * cw2 - sw2 * sw2
        tr, det = cw * (1 + c2), c2
        rec = all(k[d + 2] == tr * k[d + 1] - det * k[d] for d in range(1, N - 2))
        disc = tr * tr - 4 * det
        omega = 2 * acos(float(cw2))
        eps = acos(float(ce))
        gnum = (1 + float(c2)) / (2 * sqrt(float(c2)))
        om_c = acos(min(1.0, 1 / gnum))
        roots = sp.Poly(sp.Symbol("x") ** 2 - sp.Rational(tr.numerator, tr.denominator) * sp.Symbol("x") + sp.Rational(det.numerator, det.denominator)).nroots(n=12)
        results.append((name, omega, eps, om_c, rec, disc, roots, [float(v) for v in k[1:5]]))
        print(f"2. {name}: omega = {omega:.6f}, eps = {eps:.6f}, infrared window edge omega_c = {om_c:.6f} (zone-edge window starts at "
              f"pi - omega_c = {pi - om_c:.6f}); exact covariance obeys the M(eps) recurrence: {rec}; discriminant tr^2 - 4 det = "
              f"{float(disc):.6e} ({'real roots: overdamped' if disc > 0 else 'complex roots: oscillatory'}); roots {roots}; "
              f"k[1..4] = {[round(v, 8) for v in results[-1][7]]}")
    ok_struct = disp and deph and ser.coeff(e, 2) == 0 and all(r[4] for r in results)
    edge = results[0]
    fires = edge[5] > 0 and edge[1] > 10 * edge[3]
    if not ok_struct:
        print("HIT: a structural falsifier fires (displacement, dephasing, eps^2 coefficient or M recurrence)")
    if fires:
        print(f"HIT: falsifier 4 fires: at weak registration eps = {edge[2]:.4f} the transcription of omega = {edge[1]:.4f} is overdamped "
              f"(exact discriminant {float(edge[5]):.3e} > 0, real negative transfer roots {edge[6]}), although omega is {edge[1] / edge[3]:.0f} "
              f"times the infrared window edge omega_c = {edge[3]:.4f}; the exact oscillation condition is |cos omega| g(eps) < 1, so the "
              f"note's window law 'oscillatory only for cos(omega) g(eps) < 1 / overdamped window omega < omega_c' misses a zone-edge window "
              f"omega > pi - omega_c(eps) of the same width (both close as eps -> 0)")
    print(f"SUMMARY: the displacement and dephasing forms hold symbolically, g(eps) = 1 + eps^4/2 + ... has no eps^2 term, and the exact "
          f"Gaussian-rational stack covariance obeys the M(eps) recurrence at all four parameter points ({ok_struct}); the window test "
          f"finds real transfer roots both inside the infrared window and at the zone edge: at eps = {edge[2]:.4f}, omega = {edge[1]:.4f} "
          f"(pi - omega = {pi - edge[1]:.4f} < omega_c = {edge[3]:.4f}) the transcription is overdamped, mid-band it is oscillatory")


if __name__ == "__main__":
    main()
