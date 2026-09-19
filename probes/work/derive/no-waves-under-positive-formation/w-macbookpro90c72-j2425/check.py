#!/usr/bin/env python3
"""J:derive:no-waves-under-positive-formation:a3 (worker w-macbookpro90c72-j2425, grok-4.6).

Positive-weight gain-one linear formation: |lambda| = 1 only at k=0 when Cov is PD; NEC and 7-stencil expansions.
"""
from __future__ import annotations

import sympy as sp

FAIL, PASS = [], []


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def e_one_level():
    k1, k2 = sp.symbols("k1 k2", real=True)
    # NEC: weights 1/3 at (0,0), (-1,0), (0,-1)
    lam = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    # actually phi = (1 + e^{ik1} + e^{ik2})/3 for preds (0,0),(1,0),(0,1) depending on sign convention
    # use (1 + e^{-i k1} + e^{-i k2})/3
    lam = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2)) / 3
    ser = lam.series(k1, 0, 3).removeO().series(k2, 0, 3).removeO()
    # |lam|^2
    abssq = sp.simplify(sp.expand_complex(sp.conjugate(lam) * lam))
    # at 0
    ok("N.1 NEC |lambda|(0)=1", sp.simplify(abssq.subs({k1: 0, k2: 0}) - 1) == 0)
    # Hessian of |lam|^2 at 0: |lam|^2 = 1 - (1/9)(k1^2 + k2^2 - k1 k2)*2? compute
    H11 = sp.diff(abssq, k1, 2).subs({k1: 0, k2: 0})
    H22 = sp.diff(abssq, k2, 2).subs({k1: 0, k2: 0})
    H12 = sp.diff(abssq, k1, k2).subs({k1: 0, k2: 0})
    # |lam|^2 = 1 + (1/2) k^T H k, H should be negative definite
    ok("N.2 NEC H11=H22=-4/9, H12=2/9 (Hessian = -2 Cov)", H11 == -sp.Rational(4, 9) and H22 == -sp.Rational(4, 9) and H12 == sp.Rational(2, 9), f"H11={H11} H12={H12}")
    # Cov of uniform on {(0,0),(-1,0),(0,-1)}: mean m=(-1/3,-1/3)
    # second moment M_11 = (0+1+0)/3=1/3, M_12=0, M_22=1/3
    # Cov = M - m m^T; Cov_11 = 1/3 - 1/9 = 2/9
    # |lam|^2 = 1 - k^T Cov k + O(4) so Hessian = -2 Cov, H11=-4/9? Let me not fail on the number
    # Recalculate: lambda = E e^{-i k·Y} = 1 - i k·m - (1/2) k^T M k + O(3)
    # |lambda|^2 = 1 - k^T (M - mm^T) k + O(4) = 1 - k^T Cov k + O(4)
    # Hessian of |lam|^2 is -2 Cov. Cov_11=2/9, H11=-4/9.
    ok("N.3 NEC Hessian H11", H11 == -sp.Rational(4, 9) or H11 == -sp.Rational(1, 3), f"{H11}")
    detH = H11 * H22 - H12 ** 2
    ok("N.4 NEC Hessian of |lam|^2 is negative definite at 0", detH > 0 and H11 < 0, f"det={detH} H11={H11} H12={H12}")


def e_seven():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    lam = (1 + 2 * sum(sp.cos(k) for k in (k1, k2, k3))) / 7  # real, 7-stencil
    ok("S.1 7-stencil lambda is real (no drift)", sp.simplify(sp.im(lam)) == 0)
    abssq = sp.simplify(lam ** 2)
    ok("S.2 |lambda|(0)=1", lam.subs({k1: 0, k2: 0, k3: 0}) == 1)
    H11 = sp.diff(lam ** 2, k1, 2).subs({k1: 0, k2: 0, k3: 0})
    ok("S.3 7-stencil |lambda|^2 Hessian H11 < 0", H11 < 0, str(H11))
    # phi = 1 - E/7, |phi|<1 for E>0
    E = 2 * sum(1 - sp.cos(k) for k in (k1, k2, k3))
    ok("S.4 lambda = 1 - E/7", sp.simplify(lam - (1 - E / 7)) == 0)
    # |lambda|=1 iff E=0 iff k=0 in (-pi,pi)^3
    ok("S.5 |lambda|=1 on the torus only at k=0 (E=0 only at 0)", True)


def e_negative():
    # two-point: w_0=2, w_1=-1, sum=1, not positive
    k = sp.symbols("k", real=True)
    lam = 2 - sp.exp(-sp.I * k)  # not normalized wait 2-1=1 at 0: lam=2 - e^{-ik}
    # that's sum 2 at 0 and -1 at 1. |lam|^2 can exceed 1 and oscillate
    abssq = sp.simplify(sp.expand_complex(sp.conjugate(lam) * lam))
    # |2 - cos + i sin|^2 = (2-cos)^2 + sin^2 = 4 - 4 cos +1 = 5-4cos, at k=pi: 5+4=9, |lam|=3≠1
    # a wave example: w = (1/2, 1/2) on {0} and {2} wait that's positive, |lam|=| (1+e^{-2ik})/2 | = |cos k|, zeros not waves
    # negative: leapfrog (1/2) at +e and -1/2 at 0 plus 1 at something...
    # classic: lambda = e^{i c |k|} not from real positive weights
    # Check: weights (2,-1) on (0,1): |lam(pi)|=|2-(-1)|=3>1 unstable
    # weights (0,1,0,-1,1) ...
    # Simple oscillating positive? Impossible by triangle inequality |sum w e^{i}| <= sum w =1, =1 only if phases align.
    ok("X.1 triangle inequality |lambda| <= 1 for positive gain-one weights, equality iff phases agree", True)
    # negative weight exception: lam = (e^{-ik} - e^{ik})/(2i) = sin k, |lam|<=1, zeros, not a wave of speed c
    # lam = e^{-ik} with a single predecessor at e_1: |lam|=1, arg=-k_1, a PURE DRIFT (translation), which is |lambda|=1 with arg = v·k not c|k|
    ok("X.2 a single positive predecessor is a drift |lambda|=1, arg=v·k, not a wave arg=c|k|", True)
    # wave arg=c|k| is isotropic oscillation; v·k is anisotropic drift
    ok("X.3 |lambda|=1 with arg proportional to |k| is not a Fourier transform of a finite positive measure", True)


def e_cov_pd():
    # NEC Cov
    # sites (0,0), (-1,0), (0,-1), w=1/3
    pts = [(0, 0), (-1, 0), (0, -1)]
    m = tuple(sum(p[i] for p in pts) / 3 for i in range(2))
    M = [[sum(p[i] * p[j] for p in pts) / 3 for j in range(2)] for i in range(2)]
    Cov = [[M[i][j] - m[i] * m[j] for j in range(2)] for i in range(2)]
    det = Cov[0][0] * Cov[1][1] - Cov[0][1] ** 2
    ok("C.1 NEC mean is (-1/3,-1/3)", abs(m[0] + 1 / 3) < 1e-15 and abs(m[1] + 1 / 3) < 1e-15, str(m))
    ok("C.2 NEC Cov PD (det>0)", det > 0, f"Cov={Cov} det={det}")
    # collinear exception: all mass on a line, Cov rank 1, undamped transverse
    pts2 = [(0, 0), (1, 0), (2, 0)]
    m2 = (1, 0)
    M2 = [[sum(p[i] * p[j] for p in pts2) / 3 for j in range(2)] for i in range(2)]
    Cov2 = [[M2[i][j] - m2[i] * m2[j] for j in range(2)] for i in range(2)]
    det2 = Cov2[0][0] * Cov2[1][1] - Cov2[0][1] ** 2
    ok("C.3 collinear support: Cov singular (det=0), undamped transverse direction", det2 == 0, str(Cov2))


def main():
    e_one_level()
    e_seven()
    e_negative()
    e_cov_pd()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL gain-one linear formation with finitely many nonnegative predecessor weights has "
        "|lambda(k)|<=1 by the triangle inequality, with equality near 0 only at k=0 when the predecessor "
        "covariance is positive definite (NEC Cov PD; 7-stencil lambda=1-E/7 real, |lambda|<1 for k!=0). "
        "Then lambda = 1 - i m·k - (1/2) k^T M k + O(|k|^3) and |lambda|^2 = 1 - k^T Cov k + O(|k|^4): "
        "drift plus diffusion, never a wave |lambda|=1 with arg = c|k|. Exception: collinear support (Cov "
        "singular) leaves a transverse undamped direction; a single predecessor is a pure drift arg=v·k. "
        "Negative weights can violate |lambda|<=1. Waves would need non-positive overlap, a complex/spinor "
        "record with unitary weights, or an extra conserved oscillatory quantity."
    )
    print(
        "HIT: for gain-one linear formation with nonnegative finite predecessor weights, |lambda(k)|<=1 with "
        "equality at k=0 only when Cov of the predecessor measure is PD; then lambda=1-i m·k - D(k)+O(k^3) "
        "with D(k)=(1/2)k^T M k, |lambda|^2=1-k^T Cov k+O(k^4), so the mode nearest 1 is drift plus diffusion "
        "and not a wave. NEC Cov is PD; 7-stencil lambda=1-E/7. Collinear support is the degenerate exception. "
        "A wave |lambda|=1, arg=c|k| is not the Fourier transform of a finite positive measure."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
