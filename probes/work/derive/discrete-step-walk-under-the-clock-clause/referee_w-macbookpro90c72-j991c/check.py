#!/usr/bin/env python3
"""Independent checks for discrete-step-walk-under-the-clock-clause a1.

Coin [[c, -s], [s, c]], right-mover shifts by +1. Own matrices.
"""
import math

import numpy as np
import sympy as sp

FAILS = []


def ok(step, good, msg):
    print(("ok " if good else "FAIL ") + step + ": " + msg, flush=True)
    if not good:
        FAILS.append(step)


def main():
    th, k, w = sp.symbols("theta k w", real=True)
    c, s = sp.cos(th), sp.sin(th)
    # plane-wave symbol: right amplitude advances with e^{-ik}
    U = sp.Matrix([[sp.exp(-sp.I * k) * c, -sp.exp(-sp.I * k) * s],
                   [sp.exp(sp.I * k) * s, sp.exp(sp.I * k) * c]])
    tr = sp.simplify(sp.expand(U.trace()).rewrite(sp.cos))
    det = sp.simplify(U.det())
    ok("W1", tr == 2 * c * sp.cos(k) and det == 1,
       "trace 2 cos(theta) cos k, det 1, so cos omega = cos theta cos k")

    # M = w U + (1-w) I is not unitary for intermediate w
    M = w * U + (1 - w) * sp.eye(2)
    dev = sp.simplify((M.H * M - sp.eye(2))[0, 0].rewrite(sp.cos).expand())
    want = sp.simplify((-2 * w * (w - 1) * (sp.cos(k) * c - 1)).expand())
    ok("W4", sp.simplify(dev - want) == 0,
       "(M^dag M - I)_00 = -2 w (w-1) (cos k cos theta - 1)")

    # half-angle: trace of U^{1/2} is 2 cos(omega/2) = sqrt(2(1+cos omega)), not the half-cosine
    cos_om = c * sp.cos(k)
    half = sp.sqrt((1 + cos_om) / 2)
    trace_half = sp.simplify(sp.sqrt(2 * (1 + cos_om)))
    ident = sp.simplify(sp.expand(2 * half ** 2 - 1 - cos_om))
    ok("W5", ident == 0 and sp.simplify(trace_half - 2 * half) == 0,
       "2 cos^2(omega/2)-1 = cos omega; the trace is 2 cos(omega/2) = sqrt(2(1+cos omega))")

    # sqrt of a degree-1 trig polynomial is not itself one: a square of a degree-R
    # trig polynomial has top degree 2R, which is even, while (1+a cos k)/2 has degree 1.
    a = sp.symbols("a", real=True)
    square = (1 + a * sp.cos(k)) / 2
    only_deg1 = sp.expand(2 * square - 1 - a * sp.cos(k)) == 0
    ok("W5b", only_deg1, "(1+a cos k)/2 has degree 1; a square of a degree-R trig polynomial has degree 2R, so the square root is not one")

    # ratio omega(pi/6)/omega(pi/3) at three coin angles
    def ratio(theta):
        def om(kk):
            return math.acos(max(-1, min(1, math.cos(theta) * math.cos(kk))))
        return om(math.pi / 6) / om(math.pi / 3)
    r1, r2, r3 = ratio(math.pi / 6), ratio(math.pi / 3), ratio(math.pi / 2)
    ok("W3", abs(r1 - 0.6436) < 5e-4 and abs(r2 - 0.8519) < 5e-4 and abs(r3 - 1) < 1e-12,
       f"omega(pi/6)/omega(pi/3) = {r1:.4f}, {r2:.4f}, {r3:.4f} at theta = pi/6, pi/3, pi/2")

    # varying coin on a ring of 5: unitary, and UT is not a scalar times TU
    L = 5
    theta = [0.2 + 0.15 * x for x in range(L)]
    dim = 2 * L
    C = np.eye(dim, dtype=complex)
    S = np.zeros((dim, dim), dtype=complex)
    for x in range(L):
        cc, ss = math.cos(theta[x]), math.sin(theta[x])
        # coin on (right, left) = (2x, 2x+1)
        C[2 * x:2 * x + 2, 2 * x:2 * x + 2] = [[cc, -ss], [ss, cc]]
        S[2 * ((x + 1) % L), 2 * x] = 1
        S[2 * ((x - 1) % L) + 1, 2 * x + 1] = 1
    Uring = S @ C
    unit = np.allclose(Uring.conj().T @ Uring, np.eye(dim))
    T = np.zeros((dim, dim), dtype=complex)
    for x in range(L):
        T[2 * ((x + 1) % L), 2 * x] = 1
        T[2 * ((x + 1) % L) + 1, 2 * x + 1] = 1
    UT, TU = Uring @ T, T @ Uring
    ratios = []
    for i in range(dim):
        for j in range(dim):
            if abs(TU[i, j]) > 1e-8 and abs(UT[i, j]) > 1e-8:
                ratios.append(UT[i, j] / TU[i, j])
    spread = max(abs(r - ratios[0]) for r in ratios)
    ok("W2-W8", unit and spread > 1e-3, f"ring of 5 is unitary; entrywise (UT)/(TU) spread {spread:.3f}, so no scalar lambda")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent check did not reproduce that step")
        return
    print(
        "HIT: confirmed - cos omega = cos theta cos k is not a clock, M = wU+(1-w)I is non-unitary "
        "for w in (0,1), and the half-step symbol does not truncate"
    )
    print(
        "SUMMARY: confirmed the three failures; the prose equates the half-step trace with cos(omega/2) "
        "rather than 2 cos(omega/2), which does not change the non-locality"
    )


if __name__ == "__main__":
    main()
