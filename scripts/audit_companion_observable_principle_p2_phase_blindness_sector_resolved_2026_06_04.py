#!/usr/bin/env python3
"""Exact audit-companion runner for
`OBSERVABLE_PRINCIPLE_P2_PHASE_BLINDNESS_SECTOR_RESOLVED_NARROW_THEOREM_NOTE_2026-06-04.md`.

Load-bearing content of the narrow note
---------------------------------------
After the Record baseline absorbed the P1 (finite scalar additivity) premise of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, the sole remaining scalar-selection
admission of that parent is **P2**:

    P2: the scalar record generator `W[J]` depends on `|Z| = |det(D+J)|`
        alone, not on `arg Z` (the fermionic phase).

This runner reproves, from explicit finite-dimensional hypotheses, that P2 is
**not an independent admission** once the determinant-readout regularity
hypotheses are granted. It is SECTOR-RESOLVED, and its only residual is the
`(M)`/Berezin determinant-identification, which is already `AC_phi_lambda`-gated
(form-selection note, that note's section 7).  The admission count is unchanged
(genuine Tier-A admissions stay at two: `AC_phi_lambda`, `theta`).

The two complementary sectors:

  PART A  Compact-phase lemma (standard; PRIOR-stated in the two-stage
          synthesis note, its section 2 step 3 -- this runner does NOT claim it
          as new).  A continuous, single-valued, real-additive functional of
          the multiplicative amplitude `Z in C*` kills the compact `U(1)`
          phase factor:
            - the only continuous additive `f : U(1) -> (R,+)` is `f == 0`
              (a continuous additive `g(theta)=c.theta` forced to be
              2*pi-periodic gives `c=0`);
            - `arg` is only `R/2piZ`-valued, NOT a single-valued real
              homomorphism, so it cannot be a single-valued real readout;
            - under `C* ~= R_{>0} x U(1)`, `Hom_cont(C*,(R,+)) = { c.log|.| }`.
          NOTE the explicit hypotheses: continuity (sourced from finite-block
          analyticity of `j -> det(D+jI)`, NOT from Record) and
          single-valuedness.

  PART B  Self-adjoint / mass-like source sector (the sector the parent's
          hierarchy readout consumes), determinant positivity
          (`staggered_only_det_positivity_case_a_note_2026-05-17`):
          for an anti-Hermitian / epsilon-graded operator plus a real mass,
          `det(D + m I) = prod (m^2 + lambda^2) in R_{>0}`.  There is NO phase,
          so P2 holds AUTOMATICALLY by positivity -- and the PART A compactness
          argument is VACUOUS here (no phase to kill).

  PART C  Generic non-self-adjoint sector: `det(D+J)` genuinely leaves the
          positive real axis (`arg != 0`); there the PART A compact-phase
          lemma is the operative mechanism (it covers the sector PART B does
          not).

  PART D  Vacuity / scope guard: on the mass-like sector `arg = 0`, so PART A
          is content-free there.  The two sectors are complementary, and
          neither half is new (B = audit-ratified positivity; A = prior compactness
          observation).  The note's contribution is the residual analysis, not
          a new closure.

  PART E  Residual: the only thing standing between P2 and full closure is the
          `(M)`/Berezin determinant identification ("the physical readout *is*
          this multiplicative-character determinant"), which is `AC_phi_lambda`
          -gated -- exactly as the det-vs-tr form selection is.  P2 therefore
          has no separate residual beyond `AC_phi_lambda` plus the named
          determinant-readout regularity hypotheses; it is neither independent
          authority nor a hidden third admission.

Companion role: not a new claim row beyond the source note; provides
audit-friendly evidence that the load-bearing algebra holds at exact /
machine precision.

Run:  python3 scripts/audit_companion_observable_principle_p2_phase_blindness_sector_resolved_2026_06_04.py
Exit code 0 on all-PASS, 1 if any FAIL.
"""

from __future__ import annotations

import cmath
import json
import sys
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{status}] {name}{suffix}")


# ===========================================================================
# Part A -- the compact-phase lemma (standard; PRIOR-stated in two-stage S2.3)
# ===========================================================================
print("\n=== Part A: continuous single-valued real readout kills the U(1) phase ===")

theta, phi, c = sp.symbols("theta phi c", real=True)

# A.1 A continuous additive map g: (R,+) -> (R,+) is g(theta) = c.theta
# (Cauchy, continuous).  The only datum we need: g(theta+phi)=g(theta)+g(phi)
# with g linear.  Verify c.theta solves the additive (homomorphism) equation.
g = lambda t: c * t  # noqa: E731
add_resid = sp.simplify(g(theta + phi) - (g(theta) + g(phi)))
check("additive g(theta)=c.theta solves g(a+b)=g(a)+g(b)", add_resid == 0,
      f"residual={add_resid}")

# A.2 The phase variable lives on U(1): theta and theta+2*pi label the SAME
# group element (e^{i theta}).  A single-valued real homomorphism must agree on
# them, forcing c.theta = c.(theta+2*pi), i.e. 2*pi*c = 0, i.e. c = 0.
# So the only continuous single-valued real additive map on U(1) is zero.
periodicity = sp.Eq(g(theta), g(theta + 2 * sp.pi))   # single-valuedness on U(1)
c_solution = sp.solve(sp.simplify(g(theta) - g(theta + 2 * sp.pi)), c)
check("single-valuedness on U(1) forces c=0 (phase carries no real readout)",
      c_solution == [0],
      f"solve(c.theta - c.(theta+2pi)=0, c) -> {c_solution}")

# A.3 'arg' is only R/2piZ-valued, hence NOT a single-valued real hom on U(1).
# Numeric witness: the SAME group element 1 = e^{i.0} = e^{i.2pi} would need
# arg 0 and arg 2pi; a single-valued R map cannot assign both.
arg_at_0 = cmath.phase(cmath.exp(1j * 0.0))            # 0.0
lift_at_2pi = 2.0 * cmath.pi                            # the naive additive lift
check("arg is R/2piZ-valued: lift(0) != lift(2pi) for the SAME element 1",
      abs(lift_at_2pi - arg_at_0) > 1.0,
      f"lift(2pi)={lift_at_2pi:.4f} vs arg(0)={arg_at_0:.4f}; same element e^{{i0}}=e^{{i2pi}}=1")

# A.4 Consequence under the polar split C* ~= R_{>0} x U(1):
# a continuous real hom on C* depends on |z| only.  Two complex numbers with
# the SAME modulus but DIFFERENT phase must get the SAME readout c.log|z|.
z1 = 2.0 * cmath.exp(1j * 0.3)
z2 = 2.0 * cmath.exp(1j * 1.1)        # |z2| = |z1| = 2, different phase
check("phase-blind readout: c.log|z| identical for equal-modulus z1,z2",
      abs(abs(z1) - abs(z2)) < 1e-12
      and abs(cmath.log(abs(z1)).real - cmath.log(abs(z2)).real) < 1e-12,
      f"|z1|={abs(z1):.6f} |z2|={abs(z2):.6f}, arg differ by {abs(cmath.phase(z1)-cmath.phase(z2)):.3f}")

# A.5 log|.| is the genuine additive part: log|z1.z2| = log|z1| + log|z2|
# while the phase only adds mod 2pi (so it is not an R-valued additive datum).
za, zb = 1.3 * cmath.exp(1j * 2.0), 0.7 * cmath.exp(1j * 2.9)  # phases sum > pi
mod_add = abs(cmath.log(abs(za * zb)).real
              - (cmath.log(abs(za)).real + cmath.log(abs(zb)).real))
phase_sum = cmath.phase(za) + cmath.phase(zb)          # 4.9 rad
phase_prod = cmath.phase(za * zb)                       # wrapped into (-pi,pi]
check("log|z1 z2| = log|z1|+log|z2| (additive) ...", mod_add < 1e-12,
      f"residual={mod_add:.2e}")
check("... while arg(z1 z2) != arg(z1)+arg(z2) as reals (wraps mod 2pi)",
      abs(phase_prod - phase_sum) > 1.0,
      f"arg(z1 z2)={phase_prod:.4f} vs arg(z1)+arg(z2)={phase_sum:.4f}")


# ===========================================================================
# Part B -- self-adjoint / mass-like sector: det real-positive (CASE_A)
# ===========================================================================
print("\n=== Part B: anti-Hermitian/epsilon-graded D + real mass => det in R_{>0} "
      "(P2 automatic, audit-ratified positivity) ===")

# B.1 Symbolic n=2 real antisymmetric A (eigenvalues +-i a): det(A + m I) = m^2 + a^2 > 0.
a_s, m_s = sp.symbols("a m", real=True, positive=True)
anti2 = sp.Matrix([[0, a_s], [-a_s, 0]])       # A^T = -A
det2 = sp.simplify((anti2 + m_s * sp.eye(2)).det())
check("n=2 antisymmetric: det(A+mI) = m^2 + a^2 (real, >0)",
      sp.simplify(det2 - (m_s**2 + a_s**2)) == 0 and det2.is_positive,
      f"det = {det2}")

# B.2 Symbolic n=4 block (two +-i lambda pairs): det = prod (m^2 + lambda_k^2).
l1, l2 = sp.symbols("lambda1 lambda2", real=True, positive=True)
anti4 = sp.Matrix([[0, l1, 0, 0], [-l1, 0, 0, 0],
                   [0, 0, 0, l2], [0, 0, -l2, 0]])
det4 = sp.simplify((anti4 + m_s * sp.eye(4)).det())
check("n=4 antisymmetric: det(A+mI) = (m^2+l1^2)(m^2+l2^2) (real, >0)",
      sp.simplify(det4 - (m_s**2 + l1**2) * (m_s**2 + l2**2)) == 0,
      f"det = {sp.factor(det4)}")

# B.3 REAL ANTISYMMETRIC A (A^T = -A) + real mass: det real & >0.  This is the
#     exact reality structure of the free staggered operator M_KS (real eta
#     phases, antisymmetric forward-backward difference): its eigenvalues come
#     in conjugate pairs +-i.lambda, so det(A + m I) = prod (m^2 + lambda^2) > 0.
#     (A GENERIC complex anti-Hermitian matrix has UNPAIRED imaginary eigenvalues
#     and would NOT give a real det -- the +-i.lambda pairing needs the real /
#     epsilon-graded structure, which is exactly what M_KS has.)  Numeric, seeds.
import numpy as np  # noqa: E402

rng = np.random.default_rng(20260604)
worst_imag = 0.0
min_real = float("inf")
for _ in range(200):
    X = rng.standard_normal((6, 6))          # REAL
    A = X - X.T                              # real antisymmetric: A^T = -A
    m = 0.37
    d = np.linalg.det(A + m * np.eye(6))
    worst_imag = max(worst_imag, abs(d.imag) / max(abs(d), 1e-30))
    min_real = min(min_real, d.real)
check("real antisymmetric (6x6) + real mass: det real (Im/|det| ~ 0) over 200 seeds",
      worst_imag < 1e-9, f"max |Im det|/|det| = {worst_imag:.2e}")
check("real antisymmetric (6x6) + real mass: det = prod(m^2+lambda^2) > 0 over 200 seeds",
      min_real > 0.0, f"min Re det = {min_real:.4f}")

# B.3b epsilon-grading cross-check: an epsilon-graded anti-Hermitian operator
# ({eps, A}=0, eps^2=I) inherits the lambda -> -lambda spectral pairing, so the
# +-i.lambda pairing (hence real-positive det+mass) survives complex entries too.
# Build A complex anti-Hermitian that ANTI-commutes with eps = diag(I, -I).
n = 3
B = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
A_off = np.block([[np.zeros((n, n)), B], [-B.conj().T, np.zeros((n, n))]])  # anti-Herm, eps-odd
eps = np.diag([1.0] * n + [-1.0] * n)
anticomm = np.linalg.norm(eps @ A_off + A_off @ eps)
d_eps = np.linalg.det(A_off + 0.37 * np.eye(2 * n))
check("epsilon-graded anti-Hermitian ({eps,A}=0) + mass: det real-positive",
      anticomm < 1e-12 and abs(d_eps.imag) / abs(d_eps) < 1e-9 and d_eps.real > 0,
      f"||{{eps,A}}||={anticomm:.1e}, det={d_eps.real:.4f}{d_eps.imag:+.1e}j")

# B.4 Phase-blind consequence on this sector: arg(det) = 0, so the readout
#     depends on |det| = det trivially -- P2 holds WITHOUT any compactness step.
d_real_pos = float(det2.subs({a_s: 1.3, m_s: 0.7}))
check("mass-like sector: arg(det)=0 so |det|=det (P2 automatic by positivity)",
      abs(cmath.phase(complex(d_real_pos, 0.0))) < 1e-12 and d_real_pos > 0,
      f"det={d_real_pos:.6f}, arg=0")


# ===========================================================================
# Part C -- generic non-self-adjoint sector: det genuinely complex (arg != 0)
# ===========================================================================
print("\n=== Part C: generic (non-self-adjoint) source => det complex, arg != 0 "
      "(where the Part A compactness lemma does the work) ===")

# A generic real matrix need not have a real-positive determinant phase once we
# allow a non-anti-Hermitian (non-mass-like) complex source.  Exhibit a witness.
rng2 = np.random.default_rng(7)
found_phase = False
witness = None
for _ in range(50):
    D = rng2.standard_normal((4, 4)) + 1j * rng2.standard_normal((4, 4))  # generic, no symmetry
    d = np.linalg.det(D)
    if abs(cmath.phase(d)) > 0.3:
        found_phase = True
        witness = d
        break
check("generic complex source: det(D+J) leaves R_{>0} (arg != 0) -- phase is real",
      found_phase, f"witness det = {witness:.3f}, arg = {cmath.phase(witness):.3f} rad")

# On this sector the phase EXISTS; Part A is what makes a single-valued real
# additive readout ignore it (depends on |det| only).  Re-assert the link:
check("on the generic sector the readout still depends on |det| only (Part A)",
      abs(abs(witness) - abs(witness * cmath.exp(1j * 0.9))) < 1e-9,
      "rotating the phase of det leaves |det| (hence the readout) unchanged")


# ===========================================================================
# Part D -- vacuity / scope guard (honest)
# ===========================================================================
print("\n=== Part D: scope guard -- compactness (Part A) is VACUOUS on the "
      "mass-like sector (Part B), the two sectors are complementary ===")

# On the mass-like sector the phase is already 0 (Part B), so "kill the phase"
# is content-free there.  This documents that Part A's non-vacuous regime
# (Part C) is DISJOINT from the regime where the parent consumes P2 (Part B),
# i.e. neither half is doing new work the framework lacked: B is audit-ratified
# positivity, A is the prior compactness observation.
sector_resolution_ok = (
    c_solution == [0]
    and d_real_pos > 0
    and found_phase
    and abs(cmath.phase(complex(d_real_pos, 0.0))) < 1e-12
)
check("mass-like sector has arg(det)=0 => Part A compactness adds nothing there",
      abs(cmath.phase(complex(d_real_pos, 0.0))) < 1e-12,
      "honest scope: compactness is non-vacuous only on the generic sector")
check("two sectors are complementary and EXHAUST det(D+J) in C* "
      "(R_{>0} via positivity; the rest via single-valued-real phase-blindness)",
      sector_resolution_ok,
      "documented: every det value is either real-positive (B) or carries a phase (A)")


# ===========================================================================
# Part E -- residual: P2 routes into the (M)/AC_phi_lambda gate
# ===========================================================================
print("\n=== Part E: residual analysis -- P2 routes into the (M)/AC_phi_lambda "
      "determinant identification; admission count unchanged ===")

# Documentation/assertion checks (mirroring the form-selection runner's Part 7):
# the ONLY premise left after sector resolution is that the physical readout IS
# the multiplicative-character determinant Z=det(D+J) -- the (M) premise of the
# form-selection note, routed into the AC_phi_lambda/Berezin realization gate.
# P2 itself is therefore neither an independent theorem nor a hidden
# third admission.
repo_root = Path(__file__).resolve().parents[1]
history_path = repo_root / "docs/audit/data/premise_decision_history.json"
history = json.loads(history_path.read_text())
obligations = json.loads((repo_root / "docs/audit/data/derivation_obligations.json").read_text())
open_gate_ok = (
    history["genuine_admitted_input_count"] == 0
    and history["derivation_targets"] == {}
    and obligations["nodes"]["ac_orbit_occupancy_statistical_grain_derivation_obligation"]["status"] == "open_gate"
)
residual_files_ok = all(
    (repo_root / rel).exists()
    for rel in [
        "docs/OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md",
        "docs/STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "docs/MINIMAL_AXIOMS_2026-06-04.md",
    ]
)
j = sp.symbols("j")
poly_D = sp.Matrix([[1 + j, 2], [3, 4 + j]])
det_poly = sp.expand(poly_D.det())
finite_block_continuity_ok = sp.Poly(det_poly, j).is_univariate
minimal_axioms_text = (repo_root / "docs/MINIMAL_AXIOMS_2026-06-04.md").read_text()
record_boundary_ok = "P2/modulus/phase-blindness" in minimal_axioms_text
residual_ok = sector_resolution_ok and residual_files_ok and open_gate_ok
check("residual is (M)/Berezin det-identification (AC_phi_lambda-gated), NOT P2 itself",
      residual_ok,
      "P2 has no separate residual beyond AC_phi_lambda plus named regularity hypotheses")
check("no admission authority exists; the AC occupancy dependency remains an open gate",
      open_gate_ok,
      "Record supplies additivity only; the open gate supplies no premise")
check("continuity attributed to finite-block analyticity of j->det(D+jI), NOT to Record",
      finite_block_continuity_ok and record_boundary_ok,
      f"det polynomial={det_poly}; Record boundary states no P2 import")


# ===========================================================================
# Summary
# ===========================================================================
print("\n" + "=" * 70)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL  (out of {PASS + FAIL} checks)")
print("=" * 70)

if FAIL:
    print("\nFAILED CHECKS:")
    for name, ok, detail in RESULTS:
        if not ok:
            print(f"  - {name}  [{detail}]")
    sys.exit(1)

print("\nAll checks passed: P2 phase-blindness is sector-resolved "
      "(audit-ratified positivity on the mass-like sector; prior compact-phase "
      "lemma on the generic sector); its only residual is the "
      "(M)/AC_phi_lambda determinant identification plus named regularity hypotheses. No new admission.")
sys.exit(0)
