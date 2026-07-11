# APS `η = 2/9` Topological Robustness at the `Z_3` Fixed Locus — Bounded Member Note

**Current authority (2026-07-11):** older admission labels below are historical
provenance only. The R-eta readout remains an `open_gate`.

**Date:** 2026-07-02
**Type:** bounded_theorem
This source note does not set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_aps_topological_robustness.py`](../scripts/frontier_koide_aps_topological_robustness.py)
(41 checks, all computed, none asserted), with cache
[`logs/runner-cache/frontier_koide_aps_topological_robustness.txt`](../logs/runner-cache/frontier_koide_aps_topological_robustness.txt).

## Purpose

The runner above has carried the topological-robustness layer of the ambient
APS `η = 2/9` support chain since 2026-04-21, but its only documentation
lived inside the package survey
`KOIDE_Q_DELTA_CLOSURE_PACKAGE_README_2026-04-21.md` (backticked
non-load-bearing context reference; package survey). Downstream rows that
consume the robustness result — e.g. the reviewer stress test's CAT-B
objection B2 — therefore had no member note to cite and were routing an
evidence edge through the survey. This note is the standalone, citable,
auditable member row for exactly what those 41 checks establish, and nothing
more.

## Claim (bounded)

On the premise set declared in §Premises: the fractional part of the
equivariant APS `η`-invariant contribution at an isolated `Z_3` fixed point
is determined by the tangent-representation weights `(a, b) mod 3` alone —
with no dependence on the Riemannian metric — via the closed form

```text
η(a, b) = (1/3) · Σ_{k=1,2} 1 / [(ζ^{ka} − 1)(ζ^{kb} − 1)],   ζ = e^{2πi/3},
```

and for the declared `(1, 2)` tangent class this evaluates exactly to

```text
η(1, 2) = 2/9.
```

Equivalently: within the declared formalization there is no metric dial to
turn — the space of `Z_3`-equivariant transverse metrics is exactly the
one-parameter scalar family `λ·I`, and the closed form contains no metric
symbol.

## What the 41 checks establish (by tactic, at executable strength)

- **T1 (5 checks) — closed-form evaluation.** Exact symbolic (sympy)
  evaluation of the character sum: `η(1,2) = 2/9`; permutation symmetry
  `η(1,2) = η(2,1)`; the distinct `(1,1)` class gives `1/9`; the value
  depends on the weights only mod 3 (`η(1,4) = η(1,1)`, `η(1,5) = η(1,2)`).
- **T2 (11 checks) — equivariant-metric rigidity (the smoothing surface).**
  The equivariance equations `RᵀGR = G` for a general symmetric transverse
  `2×2` metric are solved **completely**: the unique solution family is
  `g12 = 0`, `g22 = g11`, i.e. `G = λ·I` — the equivariant metric freedom is
  exactly one scalar dimension, so no nontrivial equivariant deformation
  exists to perturb the character computation. The symbolic `η` expression
  carries no metric free symbols. Eight integer lifts `(1+3m, 2+3n)` of the
  `(1,2)` class all return `2/9`.
- **T3 (5 checks) — Euler classes.** `(1 − ζ^a)(1 − ζ^b) = 3` exactly for
  the `(1,2)/(2,1)` classes; `|Euler|² = 9` for the `(1,1)/(2,2)` classes.
- **T4 (4 checks) — K-theoretic character formula.** On `R(Z_3) ⊗ Q` the
  localized value is `η_V = (2m₀ − m₁ − m₂)/9` for
  `V = m₀χ₀ + m₁χ₁ + m₂χ₂`; the invariant isotype `χ₀` gives `2/9`; the
  regular representation gives `0` (Schur cancellation); the formula is
  `Q`-linear in isotype multiplicities.
- **T5 (6 checks) — fractional-part face.** `(2/9 + n) mod 1 = 2/9` across
  integer shifts `n ∈ {0, 1, −1, 5, −3, 100}` — the executable face of the
  APS fractional-part invariance premise (P2 below), which is what protects
  the value against the integer bulk contribution.
- **T6 (6 checks) — equivariant spin structure (the PL-to-smooth-spin
  surface).** Existence condition `gcd(1, 2, 3) = 1` verified; `Z_p` has no
  2-torsion for odd `p ∈ {3, 5, 7, 9, 11}`. The uniqueness reading
  (`H¹(L(p;1,1); Z₂) = 0` for odd `p`, hence a unique equivariant spin
  structure) and the PL-compatibility framing (PL `S³` smoothable in
  `dim ≤ 6`; PL-APS matching smooth) are stated classification reasoning in
  the runner's own text, with the torsion condition as their executable
  face.
- **T7 (2 checks) — route independence.** Two independent symbolic routes —
  the fixed-point character sum and the isotype/K-theory formula — agree
  exactly at `2/9`; the value is invariant under the `Z_3^*` action on
  tangent classes (`(1,2) → (2,1)`).
- **T8 (2 checks) — representation sensitivity.** The `(1,1)` class gives
  `1/9 ≠ 2/9`: the value is a property of the tangent class, not a metric
  artifact; the core algebraic identity `(ω − 1)(ω² − 1) = 3` pins the
  denominator.

Tactic totals: 5 + 11 + 5 + 4 + 6 + 6 + 2 + 2 = 41; the runner prints
`Summary: PASS=41, FAIL=0`.

## Premises (named; consumed, not established here)

- **P1 — ABSS equivariant fixed-point formula.** The
  Atiyah–Bott–Segal–Singer localization of the equivariant index/`η` at an
  isolated fixed point is consumed as the named mathematical input whose
  finite-dimensional consequences the runner computes exactly. It is not
  re-proven here.
- **P2 — APS fractional-part invariance.** The mod-`Z` part of `η` is the
  metric-stable invariant (the integer part may shift under deformation);
  consumed as a named input, with T5 as its executable face.
- **P3 — kinematic inputs.** The `C_3[111]` rotation on `Z³` with tangent
  weights `(1, 2)` at an isolated fixed locus on the `PL S³ × R` surface.
  These are runner-verified upstream
  (`scripts/frontier_koide_c3_spatial_rotation.py`, 16/16; the multi-route
  ambient value in `scripts/frontier_koide_aps_eta_invariant.py`, 21/21) and
  enter this note as declared inputs; the one-hop note authorities are
  listed below.

## One-hop authorities

- [`KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md`](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md)
  — ABSS applicability and the ambient `η = 2/9` block-by-block forcing
  chain (the value authority this note's robustness layer protects).
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
  — the `Cl(3)/Z³ → PL S³ × R` continuum-limit surface on which the fixed
  locus lives.

## Boundary (what this note does NOT claim)

- It does **not** derive the physical Brannen-phase bridge. Nothing here
  identifies the ambient APS invariant with the physical selected-line
  observable. That identification is exactly the `R-η` readout
  identification registered as Tier-A `AC_phi_lambda` sub-admission (ii) in
  `docs/audit/data/premise_decision_history.json`, which treats the magnitude as
  fixed-locus arithmetic conditional on `R-eta`, not as an admitted number.
  This note is part of that fixed-locus arithmetic layer; it adds no admission
  and discharges none.
- It does **not** select the `(1, 2)` tangent class as the physical class.
  T8 shows the value distinguishes tangent classes; which class is physical
  is upstream kinematic content (P3), not a consequence of robustness.
- It does **not** re-prove ABSS or the APS fractional-part theorem (P1/P2
  are named premises; a bounded verdict is bounded on them).
- It does **not** derive a dynamical metric law. The statement is
  metric-*independence* of the fractional fixed-point contribution — it
  makes no claim about which metric law holds.
- It does **not** promote the package survey, alter any audit status, or
  register anything in the Tier-A registry.

## Honest auditor read

The load-bearing content is finite exact symbolic algebra: closed-form
character sums, a complete solve of the `2×2` equivariance equations, and
Schur-orthogonality arithmetic — all recomputed by the runner, none
asserted. The theorem-level lifting is done by the two named mathematical
premises (P1, P2), and the physical relevance of the `(1, 2)` class rides on
the kinematic inputs (P3). This note's claim is bounded on those premises and
should not be read as more. In particular the note's value to the lane is
defensive: it removes "the `2/9` depends on a metric choice" as an objection,
and leaves the genuinely open step — the physical `R-η` identification —
exactly where the Tier-A registry says it is.

## Verification

```bash
python3 scripts/frontier_koide_aps_topological_robustness.py
```

Expected: `Summary: PASS=41, FAIL=0` (re-verified 2026-07-02 on `origin/main`).
