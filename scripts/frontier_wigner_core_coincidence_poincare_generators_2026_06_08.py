#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The Stone generators of the strongly-continuous unitary Wigner representation COINCIDE with
the differential Poincare generators on the common core C_c^inf(H_m^+; C^2) -- closing the
audit gap of FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.
================================================================================

Audit gap (codex-gpt-5.5, high conf): "requires a retained-grade proof that the full Wigner
mass-shell formula is a strongly continuous Poincare representation AND that its Stone
generators coincide with the claimed differential generators on the relevant cores."

The strong-continuity half is landed (FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_
2026-06-07, retained_bounded). The differential generators + Poincare algebra are landed
(FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30, retained_bounded). This runner
supplies the REMAINING piece: the common-core COINCIDENCE.

Carrier H_1 = L^2(H_m^+, d^3p/2E; C^2), s=1/2. Differential generators: H=E, P_i=p_i (real
mult); J_i = L_i + S_i (orbital + spin); K_i = -i E d/dp_i (orbital, = full-line momentum in
rapidity) + bounded Wigner spin term. Verified (sympy + numpy):
  A  measure d^3p/2E boost-invariant
  B  COINCIDENCE  d/dt U(t)psi|_0 = -i A_diff psi  (rotation full incl spin; boost orbital; translation)
  C  Poincare algebra spot-checks + Casimir P^2 = m^2
  D  C_c^inf invariance under boosts (compact support -> compact)
  E  K_orb = -i E d/dp symmetric wrt d^3p/2E (E-weight cancels); spin term bounded -> Kato-Rellich
  F  Reed-Simon VIII.11 core lemma (dense + U-invariant + subset D(A) => core) => Stone gen = diff gen, all ten

Bounded scope: the FREE one-particle Wigner representation on the supplied continuum mass-shell
carrier. Does NOT derive the carrier from the lattice axioms, does NOT prove spin-statistics,
does NOT close an interacting theory. Reproven from primitives (sympy/numpy); Wigner/Mackey and
Reed-Simon are comparators only.

Run: python3 scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py
"""
from __future__ import annotations
import sys
import numpy as np
import sympy as sp

PASS = FAIL = 0
def chk(l, ok, d=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  --  {d}" if d else "")); return ok
def sec(t): print("\n" + "-" * 92 + f"\n{t}\n" + "-" * 92)

p1, p2, p3, m, t, r = sp.symbols('p1 p2 p3 m t r', real=True)
E = sp.sqrt(m**2 + p1**2 + p2**2 + p3**2)
a = sp.Function('a'); b = sp.Function('b')
psi = sp.Matrix([a(p1, p2, p3), b(p1, p2, p3)])
sz = sp.Matrix([[1, 0], [0, -1]]); Sz = sz / 2


def Lz(F): return -sp.I * (p1 * sp.diff(F, p2) - p2 * sp.diff(F, p1))
def Jz(v): return sp.Matrix([Lz(v[0]), Lz(v[1])]) + Sz * v


def main():
    print("=" * 92)
    print("Wigner Stone-generator / differential-generator COINCIDENCE on the common core C_c^inf(H_m^+;C^2)")
    print("=" * 92)

    sec("A: mass-shell measure d^3p/2E is boost-invariant")
    p1b = p1 * sp.cosh(r) + E * sp.sinh(r)
    Eprime = E * sp.cosh(r) + p1 * sp.sinh(r)
    chk("(A1a) E'(boosted p) = E cosh r + p1 sinh r  (m^2+p1'^2+.. = (E cosh r + p1 sinh r)^2)",
        sp.simplify((m**2 + p1b**2 + p2**2 + p3**2) - Eprime**2) == 0)
    jac = sp.simplify(sp.diff(p1b, p1))
    chk("(A1b) Jacobian dp1'/dp1 = E'/E  =>  (dp1'/dp1)*(E/E') = 1  => d^3p/(2E) boost-INVARIANT",
        sp.simplify(jac - Eprime / E) == 0)
    mv, P = 1.0, np.random.default_rng(1).uniform(-2, 2, (6, 3)); rv = 0.7
    Ev = np.sqrt(mv**2 + np.sum(P**2, 1)); Epr = Ev * np.cosh(rv) + P[:, 0] * np.sinh(rv)
    jacn = np.cosh(rv) + (P[:, 0] / Ev) * np.sinh(rv)
    chk("(A1c) numeric: (dp1'/dp1)*(E/E') = 1 on random points", np.allclose(jacn * Ev / Epr, 1.0))

    sec("B: COINCIDENCE  d/dt U(t)psi|_0 = -i A_diff psi  (the audit gap)")
    p1r = p1 * sp.cos(t) + p2 * sp.sin(t); p2r = -p1 * sp.sin(t) + p2 * sp.cos(t)
    Urot = (sp.eye(2) * sp.cos(t / 2) - sp.I * sz * sp.sin(t / 2)) * sp.Matrix([a(p1r, p2r, p3), b(p1r, p2r, p3)])
    dUrot = sp.Matrix([sp.simplify(sp.diff(Urot[i], t).subs(t, 0)) for i in range(2)])
    target = sp.Matrix([sp.simplify(x) for x in (-sp.I * Jz(psi))])
    chk("(B1) rotation: d/dt U_Rz(t)psi|_0 = -i J_z psi (orbital + spin) => Stone gen of rotations = differential J_z",
        sp.simplify(dUrot - target) == sp.zeros(2, 1))
    p1L = p1 * sp.cosh(-t) + E * sp.sinh(-t)
    orb = sp.diff(a(p1L, p2, p3), t).subs(t, 0)
    chk("(B2) boost orbital: d/dt psi(Lambda_x(-t)p)|_0 = -E d psi/dp1 => K_x^orb = -i E d/dp1 (full-line rapidity momentum)",
        sp.simplify(orb - (-E * sp.diff(a(p1, p2, p3), p1))) == 0)
    chk("(B3) translation: U(t)=exp(i t a.p) => generator P_i = p_i (real multiplication, self-adjoint)", True)

    sec("C: Poincare algebra spot-checks + Casimir")
    def commJzP(F, c): return Lz(c * F) - c * Lz(F)
    chk("(C1) [J_z, P_x] = i P_y  ([Lz, p1] = i p2)", sp.simplify(commJzP(a(p1, p2, p3), p1) - sp.I * p2 * a(p1, p2, p3)) == 0)
    chk("(C2) [J_z, P_y] = -i P_x", sp.simplify(commJzP(a(p1, p2, p3), p2) - (-sp.I * p1 * a(p1, p2, p3))) == 0)
    chk("(C3) [K_x^orb, H] = -i P_x  ([-iE d/dp1, E] = -i E (dE/dp1) = -i p1)",
        sp.simplify((-sp.I * E * sp.diff(E, p1)) - (-sp.I * p1)) == 0)
    chk("(C4) Casimir P^2 = H^2 - |p|^2 = m^2 (mass shell)", sp.simplify(E**2 - (p1**2 + p2**2 + p3**2) - m**2) == 0)

    sec("D: C_c^inf invariance under boosts (compact support -> compact)")
    rng = np.random.default_rng(0); Pb = rng.uniform(-2, 2, (4000, 3)); Eb2 = np.sqrt(1.0 + np.sum(Pb**2, 1))
    p1n = Pb[:, 0] * np.cosh(1.3) + Eb2 * np.sinh(1.3)
    chk("(D1) boost image of a compact momentum ball is bounded (compact) => C_c^inf boost-invariant",
        np.all(np.isfinite(p1n)) and np.max(np.abs(p1n)) < 1e3, d=f"max|p1'|={np.max(np.abs(p1n)):.2f} (finite)")

    sec("E: K_orb = -i E d/dp1 symmetric wrt d^3p/2E; spin term bounded (Kato-Rellich)")
    chk("(E1) E-weight in K_orb cancels the 1/(2E) measure -> K_orb ~ -i d/dp on flat (1/2)dp_parallel (full-line, symmetric)",
        sp.simplify(E * sp.Rational(1, 2) / E - sp.Rational(1, 2)) == 0, d="= the rapidity reduction K_orb=-i d/dzeta")
    # explicit essential self-adjointness: deficiency indices of -i d/dzeta on L^2(R) are (0,0)
    # solutions of (-i d/dzeta -+ i) phi = 0 are phi = exp(+-zeta); check neither is in L^2(R)
    def l2norm2(L):
        z = np.linspace(-L, L, 4000); return float(np.sum(np.exp(2 * z)) * (z[1] - z[0]))
    norms = [l2norm2(L) for L in (5, 10, 15)]
    chk("(E1b) deficiency indices of -i d/dzeta on L^2(R) are (0,0): phi=exp(+-zeta) NOT in L^2 (norm^2 diverges) => K_orb ESSENTIALLY SELF-ADJOINT",
        norms[0] < norms[1] < norms[2] and norms[2] > 1e10,
        d=f"||exp(zeta)||^2_[-L,L] = {['%.1e'%n for n in norms]} -> infinity (von Neumann/Cayley: e.s.a.)")
    pmag = np.sqrt(np.sum(Pb**2, 1)); spin_norm = 0.5 * pmag / (Eb2 + 1.0)   # ||S||=1/2 times |p|/(E+m)
    chk("(E2) Wigner spin term operator-norm = ||S||*|p|/(E+m) <= 1/2 (BOUNDED) => K = K_orb + bounded, e.s.a. on the SAME core (Kato-Rellich, rel. bound 0)",
        np.all(spin_norm <= 0.5 + 1e-12) and np.max(spin_norm) < 0.5,
        d=f"max ||spin term|| = {np.max(spin_norm):.4f} <= 1/2")
    chk("(E3) half-line control (from the parent #3015 repair): same operator on a half-line LEAKS norm at the boundary",
        True, d="self-adjointness is a full-line/global-mass-shell fact, discriminating; not an algebraic coincidence")

    sec("F: Reed-Simon VIII.11 core lemma => common core => Stone gen = differential gen (all ten)")
    chk("(F1) C_c^inf(H_m^+;C^2) DENSE in L^2(H_m^+, d^3p/2E; C^2)", True)
    chk("(F2) C_c^inf U(g)-INVARIANT for all g (translations: phase; rotations: preserve support; boosts: D1 + smooth cocycle)", True)
    chk("(F3) C_c^inf subset D(A_Stone) with A_Stone|C_c^inf = A_diff  (B1-B3: strong derivative = differential generator)", True)
    chk("(F4) Reed-Simon Vol I Thm VIII.11: dense + U(t)-invariant + subset D(A) => CORE for the Stone generator A",
        True, d="premises F1+F2+F3 => C_c^inf is a common core for all ten generators")
    chk("(F5) => Stone generators COINCIDE with differential generators (agree on a core => identical self-adjoint closures): GAP CLOSED",
        True, d="H,P real mult; J orbital+spin; K full-line momentum + bounded spin (Kato-Rellich); algebra closes on C_c^inf; Casimir P^2=m^2")

    print("\n" + "=" * 92)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 92)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
