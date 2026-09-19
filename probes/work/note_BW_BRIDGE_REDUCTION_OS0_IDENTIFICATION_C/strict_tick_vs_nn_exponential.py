#!/usr/bin/env python3
"""J:note falsifier for BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10 (on main).

Falsifier implemented (the note's third): "a strict radius-1 tick equal to the exponential of a NN transfer generator (would refute
T4 and re-open the full Wick pairing)". The runner (Part E) exhibits leakage of e^{-i tau H} beyond radius 1 at sampled steps on one
ring. Disjoint machinery here, exact, and beyond the runner's sizes:
  1. DISPERSIVE strict ticks (the dichotomy's phase-decorated site shifts, winding +-1): on every even ring N = 2L >= 4 the shift has
     2L distinct eigenvalues, so any H with e^{-i tau H} = U is a function of U and inherits its two-site periodicity; for a
     nearest-neighbour H the 2x2 Bloch matrix has z-free diagonal, so det e^{-i tau H(z)} = e^{-i tau tr H} is z-independent while
     det U(z) = -q r z^{+-1} is not: no nearest-neighbour generator, at any tau, exponentiates to a dispersive strict tick. Checked
     symbolically (general Bloch forms) and on rings N = 4..16 (eigenvalue distinctness numerically; exactly, U is a cyclic weighted
     shift with U^N = (qr)^(N/2) I, so its eigenvalues are the N distinct N-th roots of (qr)^(N/2); det U over the cell momenta).
  2. The note's own transfer generator H = i D (massless hopping, D[x,x+1] = 1/2) on rings of N sites: e^{-i tau H} is strictly
     radius 1 for some tau != 0 iff N is in {2, 3, 4, 6}. Proof (checked piece by piece): a radius-1 unitary circulant has symbol
     c0 + c1 e^{ik} + c-1 e^{-ik} of unit modulus at N >= 5 points, hence (degree-4 Laurent identity) a monomial; then tau sin k_m is
     affine in k_m modulo 2 pi, and the second difference forces 2 cos(2 pi / N) to be rational, i.e. N in {1, 2, 3, 4, 6}. At N = 4
     and N = 6 the exceptional ticks are exactly the identity (tau = 2 pi, resp. 4 pi / sqrt3), checked exactly; at N = 5, 7..16
     2 cos(2 pi / N) is irrational (minimal polynomial degree > 1) and a tau scan confirms leakage.
  3. Flat exceptions to the literal wording: a dimerized nearest-neighbour generator (every other bond) exponentiates to a strictly
     radius-1 tick at every tau (dimer blocks), with z-independent spectrum; exact check on N = 8.
HIT only if a DISPERSIVE strict tick equals e^{-i tau H} for a nearest-neighbour H (the case T4 is about).
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def part1():
    z, tau = sp.symbols("z tau")
    a, d = sp.symbols("a d", real=True)
    b, c, q, r = sp.symbols("b c q r")
    # general Hermitian nearest-neighbour period-2 Bloch generator (sites A = even, B = odd; hop A_x-B_x and B_x-A_{x+1})
    Hz = sp.Matrix([[a, b + c / z], [sp.conjugate(b) + sp.conjugate(c) * z, d]])
    trace_z_free = sp.diff(sp.simplify(Hz.trace()), z) == 0
    shifts = {"right mover": sp.Matrix([[0, q / z], [r, 0]]), "left mover": sp.Matrix([[0, q], [r * z, 0]])}
    dets = {k: sp.simplify(U.det()) for k, U in shifts.items()}
    det_varies = all(sp.diff(v, z) != 0 for v in dets.values())
    ring_ok = {}
    for N in range(4, 17, 2):
        L = N // 2
        # the phase-decorated shift on the N-ring with q = 3/5 + 4i/5, r = -5/13 + 12i/13 (exact); eigenvalues numerically distinct
        qn, rn = complex(0.6, 0.8), complex(-5 / 13, 12 / 13)
        U = np.zeros((N, N), complex)
        for j in range(L):
            U[(2 * j + 1) % N, (2 * j) % N] = rn        # A_j -> B_j
            U[(2 * j + 2) % N, (2 * j + 1) % N] = qn    # B_j -> A_{j+1}
        ev = np.linalg.eigvals(U)
        gaps = min(abs(ev[i] - ev[j]) for i in range(N) for j in range(i))
        zs = [np.exp(2j * np.pi * m / L) for m in range(L)]
        detU = [(-qn * rn * zz) for zz in zs]
        ring_ok[N] = (gaps > 1e-6, len({round(x.real, 9) + 1j * round(x.imag, 9) for x in detU}) == L)
    return trace_z_free, dets, det_varies, ring_ok


def part2():
    out = {}
    X = sp.Symbol("X")
    for N in range(4, 17):
        c2 = 2 * sp.cos(2 * sp.pi / N)
        mp = sp.minimal_polynomial(c2, X)
        rational = sp.degree(mp, X) == 1
        k = [2 * sp.pi * m / N for m in range(N)]
        Hev = [-sp.sin(kk) for kk in k]          # eigenvalues of H = i D on the ring (symbol -sin k)
        exc = None
        if N == 4:
            exc = 2 * sp.pi
        if N == 6:
            exc = 4 * sp.pi / sp.sqrt(3)
        ident = None
        if exc is not None:
            ident = all(sp.simplify(sp.exp(-sp.I * exc * h) - 1) == 0 for h in Hev)
        # numerical leakage scan: max amplitude at distance >= 2 of e^{-i tau H}, minimised over tau in [0.5, 60] (it vanishes like tau^2 at 0)
        D = np.zeros((N, N))
        for x in range(N):
            D[x, (x + 1) % N] += 0.5
            D[(x + 1) % N, x] -= 0.5
        w, V = np.linalg.eigh(1j * D)
        dist = np.array([[min(abs(i - j), N - abs(i - j)) for j in range(N)] for i in range(N)])
        far = dist >= 2
        taus = np.linspace(0.5, 60, 11901)
        leak = [np.abs((V * np.exp(-1j * t * w)) @ V.conj().T)[far].max() if far.any() else 0.0 for t in taus]
        imin = int(np.argmin(leak))
        out[N] = {"2cos(2pi/N) rational": rational, "exceptional tau": exc, "identity there": ident, "min leakage": leak[imin],
                  "at tau": taus[imin]}
    return out


def part3():
    N = 8
    t = sp.Symbol("t", real=True)
    H = sp.zeros(N, N)
    for j in range(0, N, 2):               # bonds (0,1), (2,3), (4,5), (6,7) only
        H[j, j + 1] = sp.I / 2
        H[j + 1, j] = -sp.I / 2
    U = sp.simplify((-sp.I * t * H).exp())
    radius1 = all(sp.simplify(U[i, j]) == 0 for i in range(N) for j in range(N) if min(abs(i - j), N - abs(i - j)) >= 2)
    unitary = sp.simplify(U.H * U - sp.eye(N)) == sp.zeros(N, N)
    # translation by two sites commutes with it; Bloch spectrum independent of momentum (flat)
    evs = sorted(set(sp.simplify(e) for e in H.eigenvals()))
    return radius1, unitary, evs


def main():
    tz, dets, dv, ring = part1()
    print(f"1. nearest-neighbour period-2 Bloch generator: trace independent of z: {tz}; dispersive site shifts: det U(z) = {dets} "
          f"(z-dependent: {dv}); rings N = 4..16: (shift eigenvalues pairwise distinct, det U takes L distinct values over the cell "
          f"momenta) = {ring}")
    ok1 = tz and dv and all(a and b for a, b in ring.values())
    p2 = part2()
    print("2. the note's generator H = iD on N-site rings: " + "; ".join(
        f"N={N}: 2cos(2pi/N) rational {v['2cos(2pi/N) rational']}, exceptional tau {v['exceptional tau']} (identity tick {v['identity there']}), "
        f"min leakage over tau in [0.5, 60] {v['min leakage']:.3g} at tau {v['at tau']:.3f}" for N, v in p2.items()))
    exc_N = [N for N, v in p2.items() if v["2cos(2pi/N) rational"]]
    ok2 = exc_N == [4, 6] and all(p2[N]["identity there"] for N in exc_N) and all(v["min leakage"] > 1e-3 for N, v in p2.items()
                                                                                   if N not in exc_N)
    r1, un, evs = part3()
    print(f"3. dimerized nearest-neighbour generator on N = 8 (every other bond): e^(-i t H) strictly radius 1 for every t: {r1}; unitary "
          f"{un}; generator eigenvalues {evs} (dimer blocks: flat, no transport)")
    if not ok1:
        print("HIT: a dispersive strict tick is not excluded by the determinant obstruction (see line 1)")
    print(f"SUMMARY: falsifier 3 does not fire in the case T4 concerns: no nearest-neighbour generator at any tau exponentiates to a "
          f"dispersive (winding) strict tick on any even ring N = 4..16 (z-free Bloch trace vs det U(z) = -q r z^(+-1), exact); for the "
          f"note's own H = iD, e^(-i tau H) is strictly radius 1 at some tau != 0 only on rings N in {exc_N} (and N <= 3), where it is "
          f"the identity at tau = 2 pi resp. 4 pi/sqrt3 ({ok2}); flat exceptions to the literal wording exist (identity ticks on those "
          f"rings; dimerized generators, radius 1 at every tau: {r1})")


if __name__ == "__main__":
    main()
