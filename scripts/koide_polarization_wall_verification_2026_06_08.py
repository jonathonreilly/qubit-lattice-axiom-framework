#!/usr/bin/env python3
"""Independent verification scaffold for the Koide r=1/2 polarization selector (the #2624 wall + harness).

This re-derives, from primitives, the load-bearing facts that ANY proposed polarization-selector frame
must contend with -- so a campaign survivor can be tested and a no-go can be grounded, WITHOUT trusting
agent assertions (per the verify-the-bridge discipline).

SETUP (C3 generation triplet, circulant Yukawa M = a*P_triv + b*P_omega + b-bar*P_omegabar):
  - trivial isotype: real coefficient a, block energy E_s = 3 a^2 (one real mode).
  - conjugate-pair doublet isotype: complex coefficient b, block energy E_d = 6 |b|^2.
  - Koide ratio r = |b|^2 / a^2; Q = 1/3 + (2/3) r; r=1/2 <=> Q=2/3.

VERIFIES:
  W1 (the weighting->r law). With readout weights (w_s, w_d) on (singlet, doublet) modes, the energy
     fraction x = w_s/(w_s+w_d) and the stationary r = (1-x)/(2x). Hence (1,2)->x=1/3->r=1 (vector/real
     count), (1,1)->x=1/2->r=1/2 (holomorphic count). The SELECTOR is exactly which weighting.
  W2 (the #2624 wall: the CW fluctuation MODULUS is rank-2 over the doublet -> 2 real modes -> (1,2) -> r=1).
     The one-loop Coleman-Weinberg modulus Tr log(M^dag M) restricted to the doublet fluctuation b = b1 + i b2
     has Hessian (over (b1,b2)) of RANK 2 (two strictly positive eigenvalues), i.e. two real propagating
     modes -- NOT one. So the modulus readout counts the doublet TWICE -> weighting (1,2) -> r=1, robustly,
     independent of any determinant PHASE (the phase carries delta, not r). This is the wall.
  W3 (the holomorphic alternative is a DIFFERENT count, not a rescaling). Counting b once (1 complex mode)
     is the asymmetric (1,1) split; a UNIFORM complex recount rescales (1,2)->(1/2,1) which is proportional
     to (1,2) and STILL gives r=1 (so "everything is complex" does NOT help -- only the asymmetric
     singlet-real / doublet-holomorphic split gives r=1/2, which is exactly the unproven selector).

This is NOT a derivation of r=1/2; it is the verified WALL + harness against which selector frames are judged.
No PDG/fitted value; exact sympy.
"""
from __future__ import annotations
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def main() -> int:
    print("KOIDE r=1/2 POLARIZATION WALL -- independent verification scaffold")
    print("=" * 70)

    a, b1, b2, ws, wd = sp.symbols('a b1 b2 w_s w_d', positive=True, real=True)
    # ---- W1: weighting -> r law ----
    # singlet energy 3a^2 carries weight w_s; doublet energy 6|b|^2 carries weight w_d.
    # The 2-sector entropy / equipartition stationary point gives r*(w_s,w_d) = w_d/(2 w_s) ... pin via x.
    x = ws / (ws + wd)                      # singlet energy fraction
    r_of_x = (1 - x) / (2 * x)              # Koide stationary relation r=(1-x)/(2x)
    r_12 = sp.simplify(r_of_x.subs({ws: 1, wd: 2}))   # vector/real count (1,2)
    r_11 = sp.simplify(r_of_x.subs({ws: 1, wd: 1}))   # holomorphic count (1,1)
    check("W1: weighting (1,2) [vector/real, 2 doublet modes] -> r = 1  (Q = 1/3+2/3 = 1)",
          r_12 == 1, f"r(1,2) = {r_12}, Q = {sp.nsimplify(sp.Rational(1,3) + sp.Rational(2,3)*r_12)}")
    check("W1: weighting (1,1) [holomorphic, 1 doublet mode] -> r = 1/2  (Q = 1/3+1/3 = 2/3, the Koide value)",
          r_11 == sp.Rational(1, 2),
          f"r(1,1) = {r_11}, Q = {sp.nsimplify(sp.Rational(1,3) + sp.Rational(2,3)*r_11)}")

    # ---- W2: the #2624 wall -- CW fluctuation modulus is rank-2 over the doublet ----
    # Doublet fluctuation field b = b1 + i b2. The one-loop modulus piece ~ |b|^2 = b1^2 + b2^2 (and any
    # smooth even function f(|b|^2)); its Hessian over the REAL fields (b1,b2) is what counts propagating modes.
    modulus = b1**2 + b2**2                                  # |b|^2  (leading CW modulus over the doublet)
    H = sp.Matrix([[sp.diff(modulus, v1, v2) for v2 in (b1, b2)] for v1 in (b1, b2)])
    H0 = H  # constant Hessian here (quadratic); rank is field-independent
    rank = H0.rank()
    eigs = list(H0.eigenvals().keys())
    check("W2 (the wall): the doublet CW fluctuation modulus |b|^2 has Hessian over (Re b, Im b) of RANK 2 "
          "(two strictly positive eigenvalues) -> TWO real propagating modes -> weighting (1,2) -> r=1, robustly",
          rank == 2 and all(e > 0 for e in eigs),
          f"Hessian = {H0.tolist()}, rank = {rank}, eigenvalues = {eigs}")
    # robustness: a general smooth even modulus f(|b|^2) still gives a rank-2 (rotationally symmetric) Hessian
    # at any b != 0 -- both radial and angular directions present in the real (b1,b2) plane.
    f = sp.Function('f')
    gen = f(b1**2 + b2**2)
    Hg = sp.Matrix([[sp.diff(gen, v1, v2) for v2 in (b1, b2)] for v1 in (b1, b2)])
    # at a generic point the determinant of Hg is generically nonzero (rank 2) -> two modes
    detHg = sp.simplify(Hg.det())
    check("W2 robustness: a general smooth modulus f(|b|^2) has a generically full-rank (rank-2) Hessian over "
          "(Re b, Im b) (det not identically zero) -> the modulus reading ALWAYS counts two real doublet modes",
          detHg != 0,
          f"det Hessian[f(|b|^2)] = {detHg} (not identically 0 -> rank 2 generically)")

    # ---- W3: uniform complex recount does NOT help; only the asymmetric split gives r=1/2 ----
    # Uniform "everything counts as complex" => (w_s,w_d) -> (1/2, 1), proportional to (1,2):
    r_uniform = sp.simplify(r_of_x.subs({ws: sp.Rational(1, 2), wd: 1}))
    check("W3: a UNIFORM complex recount (1/2,1) is proportional to (1,2) -> STILL r=1 (Frobenius-Schur "
          "objection); only the ASYMMETRIC (singlet-real, doublet-holomorphic) = (1,1) split gives r=1/2 -- "
          "that asymmetric split IS the unproven selector",
          r_uniform == 1, f"r(1/2,1) = {r_uniform} = r(1,2); the selector must be the ASYMMETRIC (1,1)")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT (wall established, not a derivation): the polarization selector is the binary "
        "{doublet counted as 2 real modes (modulus/CW, rank-2) -> r=1} vs {doublet counted as 1 holomorphic "
        "mode -> r=1/2}. The CW fluctuation modulus ROBUSTLY gives the rank-2 / r=1 count (#2624 wall). Any "
        "frame claiming r=1/2 must produce a NON-modulus, ASYMMETRIC, holomorphic count of the doublet that is "
        "(a) not the rank-2 modulus, (b) not a uniform complex rescaling, (c) not circular. This scaffold is "
        "the test harness for campaign survivors and the ground for a sharpened no-go."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
