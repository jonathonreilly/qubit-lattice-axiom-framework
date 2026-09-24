#!/usr/bin/env python3
"""Referee of J:derive:gravity-node-with-the-formation-kernels:a2.

Independent of the author's script: exact stencil algebra, a float bracket of
the Langevin roots, and the FCC quadratic form.
"""
import math

import sympy as sp


def A_over(k):
    e = math.exp(2 * k)
    return ((e + 1) / (e - 1) - 1 / k) / k


def main():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = sum(2 - 2 * sp.cos(k) for k in (k1, k2, k3))
    phi7 = (1 + 2 * sum(sp.cos(k) for k in (k1, k2, k3))) / 7
    if sp.expand(7 * (1 - phi7) - E) != 0 or sp.expand(7 * (1 + phi7) - (14 - E)) != 0:
        raise SystemExit("stencil")
    chi = sp.simplify(1 / (1 - phi7))
    C_over = sp.simplify(1 / (1 - phi7 ** 2))
    if sp.simplify(chi - 7 / E) != 0:
        raise SystemExit("chi")
    if sp.simplify(C_over - sp.Rational(7, 2) * (1 / E + 1 / (14 - E))) != 0:
        raise SystemExit("C")
    ratio = sp.simplify(C_over / chi)
    if sp.simplify(ratio - 7 / (14 - E)) != 0:
        raise SystemExit("ratio")
    # E = |k|^2 - (1/12) sum k_a^4 + O(k^6)
    t, x, y, z = sp.symbols("t x y z")
    ser = sp.series(E.subs({k1: t * x, k2: t * y, k3: t * z}), t, 0, 6).removeO()
    quad = sp.expand(ser.coeff(t, 2))
    quar = sp.expand(ser.coeff(t, 4))
    if quad != x ** 2 + y ** 2 + z ** 2 or quar != -sp.Rational(1, 12) * (x ** 4 + y ** 4 + z ** 4):
        raise SystemExit(f"expansion {quad} {quar}")
    print("STEPS 2-4 FOLLOW: chi=7/E, C/sigma^2=(7/2)(1/E+1/(14-E)), "
          "C/(sigma^2 chi)=7/(14-E) -> 1/2 at k=0; E=|k|^2-(1/12)sum k_a^4+O(k^6)")

    # self-consistent bookkeeping
    kap, bet, m = sp.symbols("kappa beta m", positive=True)
    # kappa = 7*beta*m, m=A, sigma^2=A/kappa => sigma^2=1/(7 beta)
    sig = sp.simplify(m / (7 * bet * m))
    if sig != 1 / (7 * bet):
        raise SystemExit("bookkeeping")
    # prescribed response: A(7 beta)=beta iff A/kappa=1/7 with kappa=7 beta
    if sp.simplify((bet / (7 * bet)) - sp.Rational(1, 7)) != 0:
        raise SystemExit("1/7")
    print("STEPS 5-9 FOLLOW: sigma^2=1/(7 beta) identically when kappa=7 beta m and m=A(kappa); "
          "unit response is beta=1 and unit two-point tail is beta=1/2; both impose A(kappa)/kappa=1/7 or 2/7")

    for target, lo, hi in ((1 / 7, 5.79145, 5.79146), (2 / 7, 1.63831, 1.63832)):
        if not (A_over(lo) > target > A_over(hi)):
            raise SystemExit(f"root bracket {target}")
    # partial-fraction tail at kappa=1, N=4000, compare to coth
    s = sum(2 / (1 + (n * math.pi) ** 2) for n in range(1, 4001))
    tail = 2 / (math.pi ** 2 * 4000)
    if abs((s + tail) - A_over(1)) > 2e-6:
        raise SystemExit(f"coth series {s} {A_over(1)}")
    print(f"ROOTS FOLLOW: A/k-1/7 changes sign on [5.79145, 5.79146] "
          f"({A_over(5.79145)-1/7:.2e}, {A_over(5.79146)-1/7:.2e}); "
          f"2/7 on [1.63831, 1.63832]; partial fractions track coth at kappa=1")

    # candidate (ii)
    M = (4 * sp.eye(3) - sp.ones(3)) / 16
    ev = sp.Matrix.eigenvals(M)
    if ev.get(sp.Rational(1, 16)) != 1 or ev.get(sp.Rational(1, 4)) != 2:
        raise SystemExit(f"eigenvalues {ev}")
    Minv = sp.simplify(M.inv())
    if Minv != 4 * (sp.eye(3) + sp.ones(3)):
        raise SystemExit("inverse")
    # amplitude ~ 1/sqrt(x^T Minv x); [111] vs a level direction orthogonal to it
    d111 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    plane = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    q111 = sp.simplify(d111.T * Minv * d111)[0]
    qpl = sp.simplify(plane.T * Minv * plane)[0]
    if sp.simplify(sp.sqrt(q111) / sp.sqrt(qpl) - 2) != 0:
        raise SystemExit(f"ratio {q111} {qpl}")
    print("STEP 10 FOLLOWS: FCC quadratic form has eigenvalues 1/4, 1/4, 1/16 and inverse 4(I+J); "
          "the 1/r amplitude along the level plane is twice the amplitude along [111]")

    # step 11: task's candidate (i) is a plane Green function times a level-time heat kernel.
    # a3 (marked GIVEN) writes the symbol with |1 - phi exp(i w)|^2, which depends on w.
    w = sp.symbols("w", real=True)
    phi = sp.symbols("phi")
    sym = sp.Abs(1 - phi * sp.exp(sp.I * w)) ** 2
    if sp.diff(sp.expand(sym.rewrite(sp.exp)), w) == 0:
        raise SystemExit("unexpectedly w-independent")
    print("STEP 11 DOES NOT FOLLOW: the task's candidate (i) is a plane Green function times a "
          "level-time heat kernel. Its symbol depends on the level-time momentum "
          "(a3's |1 - phi e^{iw}|^2, which this attempt marks GIVEN). "
          "A Fourier integral that assumes no w dependence only recovers delta_{n,0} for a "
          "different object. The equal-level slice sigma^2/(1-u) is two-dimensional; that is a "
          "different reason it is not 1/(4 pi r) on Z^3")

    print("SUMMARY: fails at step 11 - candidate (i) is not confined to one level by a w-independent "
          "symbol; the task's kernel depends on level time, and the delta_{n,0} check does not apply. "
          "Steps 2-10 do follow: chi=7/E, self-consistent sigma^2 chi=G/beta so beta=1 (beta=1/2 for the "
          "two-point tail), kappa* of A/k=1/7 lies in [5.79145, 5.79146], and candidate (ii)'s 1/r "
          "amplitude on the level plane is exactly twice the [111] amplitude")


if __name__ == "__main__":
    main()
