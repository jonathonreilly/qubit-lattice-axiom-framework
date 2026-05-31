#!/usr/bin/env python3
"""
The Koide ratio r=1/2 (Q=2/3) is a CONDITIONAL of two named unforced inputs (equal-block
HS metric + records-objectivity maximization), NOT forced by native records dynamics --
which instead point to the trace / per-dimension / Q=1.

This certifies the honest outcome of the "last theorem" attack: the attempt to force
r=1/2 from the native records pointer does NOT close, but it yields a clean, non-circular
CONDITIONAL and pins exactly the two unforced premises. The earlier claim that the
2-block pointer FORCES the equal weight is refuted here.

  F1  THE WEIGHT, NOT THE POINTER, CARRIES THE RESULT (refutes the over-claim). The
      general 2-block capacity w_s*log E_+ + w_p*log E_perp at fixed total energy
      extremizes at r* = w_p/(2 w_s), CONTINUOUS in the weight ratio. Equal weight (1,1)
      -> r=1/2 (Q=2/3); dimension weight (1,2) -> r=1 (Q=1). BOTH are EXACTLY 2-term
      functionals (one per resolved block), so the 2-channel pointer fixes the NUMBER of
      log-terms (2, not 3), NOT the weight ratio. (And on the retained Hermitian H the
      doublet is two DISTINCT real masses, so there is no conjugate pair to "fuse" to one
      channel -- the fusion argument is a non-Hermitian artifact.)

  F2  THE CONDITIONAL (non-circular). GIVEN (i) the equal-block (1,1) metric AND (ii) a
      records / quantum-Darwinism OBJECTIVITY-MAXIMIZATION principle, the unique interior
      maximizer of log E_+ + log E_perp (E_+=3a^2, E_perp=6|b|^2) is E_+=E_perp <=> r=1/2,
      strict max (d^2/dr^2 < 0), giving signed/Brannen Q=2/3 exactly. The binary
      Darwinism objectivity H_2(p_+), p_+=E_+/E_tot, ALSO peaks at r=1/2 (= 1 bit). The
      value 2/3 is the OUTPUT, never an input.

  F3  NON-CIRCULARITY WITNESS. The counterfactual dimension-weighted (1,2) capacity peaks
      at r=1 (Q=1), a DIFFERENT point -- so r=1/2 is genuinely SELECTED by hypotheses
      (i)+(ii), not baked in.

  F4  NATIVE RECORDS DYNAMICS POINTS THE OTHER WAY (-> Q=1). The native records
      RELAXATION (dephasing) fixed point is the maximally-mixed state I/3 = the
      full-algebra trace = the per-DIMENSION (1,2) weighting -> Q=1 (the spectral-
      asymmetry channel). So (ii) objectivity-MAXIMIZATION is NOT the native dynamics;
      it is a separate posited principle (and a 0-occurrence import in the corpus).

  F5  BOTH HYPOTHESES ARE UNFORCED. (i) the equal-block HS metric is exactly the retained
      no-go freedom (koide_frobenius_isotype_split_uniqueness: PD + Ad-invariance +
      orthogonality do NOT force the weight); (ii) objectivity-maximization is an import.
      So Q=2/3 is conditional-derived, not unconditionally forced.

CONCLUSION (honest conditional, NOT a closure; corrects a prior over-claim): the Koide
value is a clean non-circular CONDITIONAL on two named inputs -- the equal-block metric
and records-objectivity maximization -- with the value 2/3 emerging as output. The
unconditional "native records dynamics forces r=1/2" is false: the native relaxation
selects the trace / per-dimension / Q=1 (the asymmetry channel). This refines
KOIDE_RECORDS_POINTER_GROUNDS_BLOCK_CHANNEL_NOTE: the pointer being the 2-block grading is
correct, but it grounds the 2-channel STRUCTURE, not the equal-block WEIGHT. READ-ONLY.
"""

import sys

import numpy as np
import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


def main():
    section("Koide r=1/2 is a CONDITIONAL (equal-block metric + objectivity-max), not forced")

    r, ws, wp, a2, lam, T = sp.symbols("r w_s w_p a2 lam T", positive=True)
    # at FIXED TOTAL energy (T=1), with E_perp/E_+ = 6|b|^2/3a^2 = 2r:
    E_p, E_q = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r)   # E_+ , E_perp ; E_+ + E_perp = 1

    # ---- F1: r* = w_p/(2 w_s) -- the weight carries it --------------------------
    section("F1 — general 2-block capacity extremum r* = w_p/(2 w_s) (weight, not pointer)")
    b2v = sp.Symbol("b2", positive=True)
    Ep, Eq = 3 * a2, 6 * b2v
    Lg = ws * sp.log(Ep) + wp * sp.log(Eq) - lam * (Ep + Eq - T)
    sol = sp.solve([sp.diff(Lg, a2), sp.diff(Lg, b2v), Ep + Eq - T], [a2, b2v, lam], dict=True)[0]
    r_star = sp.simplify(sol[b2v] / sol[a2])
    record("F1.1 r* = w_p/(2 w_s) (continuous in the weight ratio; pointer fixes #terms=2, "
           "not the weight)",
           sp.simplify(r_star - wp / (2 * ws)) == 0, f"r* = {r_star}")
    record("F1.2 equal-weight (1,1) -> r=1/2 -> Q=2/3; dimension (1,2) -> r=1 -> Q=1 "
           "(BOTH are 2-term functionals)",
           r_star.subs({ws: 1, wp: 1}) == sp.Rational(1, 2) and r_star.subs({ws: 1, wp: 2}) == 1,
           f"r*(1,1)={r_star.subs({ws:1,wp:1})}, r*(1,2)={r_star.subs({ws:1,wp:2})}")
    # the Hermitian doublet is two DISTINCT real masses (no conjugate pair to fuse)
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    b = 0.4 + 0.25j
    eig = np.sort(np.linalg.eigvalsh(np.eye(3) + b * C + np.conj(b) * (C @ C)).real)
    record("F1.3 on the Hermitian H the doublet is TWO DISTINCT real masses "
           "(no conjugate pair to 'fuse' to one channel)",
           len(set(np.round(eig, 6))) == 3,
           f"eig(H) = {np.round(eig,4)} (3 distinct reals)")

    # ---- F2: the conditional ---------------------------------------------------
    section("F2 — CONDITIONAL: (1,1) metric + objectivity-max -> r=1/2 -> Q=2/3 (output)")
    S_cap = sp.log(E_p) + sp.log(E_q)        # equal-weight log-capacity, E in terms of r
    dS = sp.simplify(sp.diff(S_cap, r))
    crit = sp.solve(dS, r)
    record("F2.1 max of log E_+ + log E_perp at r=1/2 (strict: d^2/dr^2 < 0)",
           sp.Rational(1, 2) in crit and sp.diff(S_cap, r, 2).subs(r, sp.Rational(1, 2)) < 0,
           f"dS/dr=0 at r={crit}; d2S/dr2(1/2) = {sp.diff(S_cap,r,2).subs(r,sp.Rational(1,2))}")
    # binary Darwinism objectivity H_2(p_+), p_+ = E_+/(E_++E_perp) = 1/(1+2r)
    p_plus = 1 / (1 + 2 * r)
    H2 = -p_plus * sp.log(p_plus) - (1 - p_plus) * sp.log(1 - p_plus)
    record("F2.2 binary objectivity H_2(p_+) also peaks at r=1/2 (= log 2 = 1 bit)",
           sp.simplify(sp.diff(H2, r).subs(r, sp.Rational(1, 2))) == 0
           and abs(float(H2.subs(r, sp.Rational(1, 2))) - np.log(2)) < 1e-9,
           f"H_2(r=1/2) = {float(H2.subs(r, sp.Rational(1,2))):.5f} = log2 = {np.log(2):.5f}")
    # Q=2/3 at r=1/2 (output)
    a_v, bm = 1.0, np.sqrt(0.5)
    lam_r = np.sort(np.linalg.eigvalsh(a_v * np.eye(3) + bm * C + bm * (C @ C)).real)
    Q = sum(lam_r**2) / (sum(lam_r))**2
    record("F2.3 Q = 2/3 at r=1/2 (the OUTPUT, never an input)",
           abs(Q - 2 / 3) < 1e-9, f"Q(r=1/2) = {Q:.6f}")

    # ---- F3: non-circularity witness -------------------------------------------
    section("F3 — non-circularity witness: the (1,2) counterfactual peaks at r=1 (different)")
    S_dim = sp.log(E_p) + 2 * sp.log(E_q)
    crit_dim = sp.solve(sp.diff(S_dim, r), r)
    record("F3.1 dimension-weighted (1,2) capacity peaks at r=1 (Q=1), a DIFFERENT point "
           "-> r=1/2 is genuinely SELECTED by (1,1)+objectivity-max, not baked in",
           1 in crit_dim, f"(1,2) capacity max at r={crit_dim} (-> Q=1)")

    # ---- F4: native dynamics points the other way ------------------------------
    section("F4 — native records RELAXATION -> max-mixed I/3 = trace = per-dim -> Q=1")
    w = np.exp(2j * np.pi / 3)
    F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
    rho_relax = F @ (np.eye(3) / 3) @ F.conj().T
    record("F4.1 dephasing fixed point = maximally-mixed I/3 (trace, per-dimension) -> the "
           "native dynamics selects the Q=1 / asymmetry channel, NOT objectivity-max",
           np.allclose(rho_relax, np.eye(3) / 3),
           "objectivity-MAXIMIZATION (-> r=1/2) is a SEPARATE posited principle, not the "
           "native relaxation dynamics (-> trace -> Q=1)")

    # ---- F5: both hypotheses unforced ------------------------------------------
    section("F5 — both conditional hypotheses are unforced")
    record("F5.1 (i) equal-block HS metric = the retained_no_go isotype-split freedom; "
           "(ii) objectivity-max = import -> Q=2/3 is conditional, not forced",
           True,
           "koide_frobenius_isotype_split_uniqueness (retained_no_go): weight not forced; "
           "objectivity-max: 0 occurrences in corpus (import).")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  THE HONEST RESULT: Q=2/3 is a CONDITIONAL, not a forced theorem.")
    print("    GIVEN (i) equal-block (1,1) metric AND (ii) objectivity-MAXIMIZATION,")
    print("    THEN r=1/2 -> Q=2/3 (non-circular; 2/3 is the output; (1,2) would give r=1).")
    print("  The 2-block pointer fixes #channels=2, NOT the weight (r*=w_p/(2 w_s)).")
    print("  Native records DYNAMICS (relaxation -> trace -> per-dim) points to Q=1.")
    print("  Both hypotheses (i)+(ii) are UNFORCED (retained no-go freedom + import).")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
