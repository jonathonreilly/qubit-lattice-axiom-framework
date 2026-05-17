# Block 22 Report: observable-principle-from-axiom

**Date:** 2026-05-17
**Worktree:** `/private/tmp/physics-loop-2026-05-17/block22-observable-principle-from-axiom`
**Branch:** `physics-loop/observable-principle-from-axiom-block22-2026-05-17`
**Lane:** observable_principle (TOTALLY FRESH — no prior block under
this campaign on this row).
**Target row:** `observable_principle_from_axiom_note`
**Audit state of target:** `audited_conditional` (bounded_theorem),
713 descendants, lbs=26.70, criticality `critical`.

## Audit-named open chain step

The parent note's load-bearing chain has four admitted bridge
premises P1-P4. As of the 2026-05-09 update three of those (P2/P3/P4)
were retired to runner-local algebraic consequences plus zero-source
baseline convention. The remaining admitted premise is **P1 (scalar
additivity on independent subsystems)**.

`notes_for_re_audit_if_any` repair target:

> Re-audit if scalar additivity and CPT-even phase-blindness are
> accepted as retained-grade upstream theorems, **or if the source is
> narrowed to a conditional exact-algebra statement**.

The parent already implements branch (b). Branch (a) (close P1) has
been heavily attacked in 5 prior sibling notes (Routes A/B/C/D/E,
PRs #1368, #1373, #1402, #1406, plus Route D consolidated sharpened
no-go). All five routes converge on the same structural obstruction
(the counterexample family `F_p[J] = r(J)^p`); a sixth P1 route
would be churn per `feedback_physics_loop_corollary_churn.md`.

## V1-V5 outcome

- **V1** (6th P1-derivation route, e.g. model-theoretic categorical
  semantics, ergodic theory, Galois conjugation): SKIP — Route D
  consolidated no-go explicitly enumerates the structural obstruction
  (Pattern L circularity + Pattern D inapplicability). Sixth negative
  is churn.
- **V2** (strengthen X2 admissibility-class uniqueness on a different
  class): SKIP — any P1-containing admissibility class reduces to the
  same Cauchy log functional-equation closure the parent already does.
  No new load-bearing step.
- **V3** (Klein-four orbit structure on APBC phases for ALL even
  `L_t` — closed-form proof of parent's Theorem 4): **THIS IS THE
  BUILT ANGLE.**
- **V4** (`A(L_t)` numerator structure for the `(7/8)^(1/4)` selector
  base): SKIP — too close to parent's out-of-scope numerical `v`
  readout.
- **V5** (cyclotomic-Galois supporting algebraic observation):
  included as Observation 4.1 + 4.2 in the source note, runner T10
  verifies. Not load-bearing on its own.

V1-V5 reasoning is detailed in `V1_V5_SCRATCH.md`.

## What was built (positive narrow theorem)

A closed-form algebraic / number-theoretic narrow theorem on the
Klein-four group action on the APBC temporal phase set
`Φ(L_t) := { e^{i (2n+1) π / L_t} : n = 0, …, L_t-1 }` for every
even `L_t`:

- **Theorem 2 (closed-form orbit count).** For every even
  `L_t = 2m`, `m ≥ 1`,
  `| Φ(L_t) / K_4 | = ceil(m/2) = ceil(L_t/4)`.
  Equivalently, the number of distinct values of
  `sin²((2n+1) π / L_t)` for `n = 0, …, L_t-1` equals `ceil(L_t/4)`.
- **Corollary 2.1.1 (single-orbit characterization).** Single-orbit
  iff `L_t ∈ {2, 4}`.
- **Corollary 2.1.2 (orbit-size dichotomy at `L_t ∈ {2, 4}`).** At
  `L_t = 2`, orbit size 2 with `sin² = 1`. At `L_t = 4`, orbit size 4
  with `sin² = 1/2` uniform.
- **Corollary 2.1.3 (unique minimal resolved orbit).** `L_t = 4` is
  the unique even `L_t` for which `Φ(L_t)` is a single `K_4`-orbit of
  size > 2.

The proof in §3 uses only elementary trigonometric identities
(`sin²(θ + π) = sin²(θ)`, `sin²(π - θ) = sin²(θ)`, the
`cos(2α) = cos(2β) ⇔ α ≡ ±β (mod π)` reduction) and elementary
integer arithmetic. No P1 input. No P2/P3/P4 input. No Grassmann /
Dirac-operator input. No framework primitive input beyond the APBC
phase set `Φ(L_t)` already used by the parent's runner.

A supporting algebraic observation (Observation 4.1) records the
cyclotomic-Galois identification of `Φ(4)` with the roots of
`Φ_8(x) = x^4 + 1` (Galois group `(Z/8Z)^× ≅ K_4`); this is
cross-discipline cross-reference, not load-bearing for Theorem 2.

## Relation to parent and sibling notes

| Note | What it closes | Relation to this block |
|---|---|---|
| `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` | parent (audited_conditional, P1-P4 conditional algebra closure) | this block proves Theorem 4 (selector content) in closed form for all even `L_t` |
| `HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md` | sibling (qualitative `L_t = 4` selector claim) | this block proves the selector claim in closed form |
| `OBSERVABLE_PRINCIPLE_P1_BRIDGE_ROUTE_{A,B,C,D,E}_*.md` | attempts to close P1 (all bounded_theorem / no_go on derivation obstruction) | orthogonal — this block closes a different load-bearing step (Theorem 4 selector), does NOT consume or close P1 |
| `OBSERVABLE_PRINCIPLE_REAL_D_BLOCK_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md` | block-local uniqueness of `W` on real-D blocks (audited_failed) | orthogonal — this block does not consume X2 admissibility class |
| `OBSERVABLE_PRINCIPLE_SCALE_INVARIANT_SOURCE_RESPONSE_NARROW_THEOREM_NOTE_2026-05-16.md` | residual scale `c` cancels in normalized ratios (P4 side) | orthogonal — this block closes the orbit-structure side |

This block's narrow theorem closes the **Theorem 4 selector content**
of the parent at the strongest possible scope (closed-form for all
even `L_t`), strengthening the parent's runner-scope finite scan
(`L_t ∈ {2, 4, 6, 8, 10, 12}`) and the
`HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE`'s qualitative claim.

## Deliverables

- **Source note:**
  `docs/OBSERVABLE_PRINCIPLE_KLEIN_FOUR_APBC_ORBIT_PARTITION_CLOSED_FORM_NARROW_THEOREM_NOTE_2026-05-17.md`
- **Runner:**
  `scripts/audit_companion_observable_principle_klein_four_apbc_orbit_partition_closed_form_exact_2026_05_17.py`
- **Runner cache:**
  `logs/runner-cache/audit_companion_observable_principle_klein_four_apbc_orbit_partition_closed_form_exact_2026_05_17.txt`
- **Block artifacts:**
  `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block22/V1_V5_SCRATCH.md`
  + this report.

**Runner result:** `THEOREM PASS=21 FAIL=0` (eleven part-groups
T1-T11, 21 sub-checks, all exact SymPy / `Fraction`).

## What this does NOT close

- The P1 (scalar additivity on independent subsystems) admitted
  premise — remains admitted on the parent. Routes A/B/C/D/E document
  the structural obstruction to deriving P1 from current retained
  primitives + standard mathematical scaffolds. This block is
  orthogonal to that load-bearing step.
- P2 (CPT-even phase blindness), P3 (continuity), P4 (normalization)
  — runner-local algebraic consequences in the parent; not touched.
- The Grassmann factorization / Dirac-determinant derivation chain
  of the parent's Theorems 1-3.
- The hierarchy baseline `M_Pl * α_LM^16`.
- The `v = 246.28 GeV` numerical readout.
- The measurement comparator `v_meas = 246.22 GeV`.
- The parent's `audited_conditional` audit verdict.
- Any sibling note's audit status.
- Any audit verdict whatsoever — this block is a source-note
  proposal; the independent audit lane sets all verdicts.

## Hard rules check

- **A_min only:** consumes only the APBC phase set definition
  `Φ(L_t)` (already in parent's `apbc_phases(lt)` /
  `temporal_modes(lt)`) and the standard Klein-four group `K_4 = Z_2
  × Z_2` on `S^1`. Elementary trigonometric identities and integer
  arithmetic. No new framework primitives, no new repo vocabulary,
  no new axioms, no P1 input, no Grassmann / Dirac input.
- **Source-only PR:** added only `docs/` (source note + block
  artifacts), `scripts/` (runner), and `logs/runner-cache/` (runner
  output). No `CANONICAL_HARNESS_INDEX`, `DERIVATION_ATLAS`,
  `DERIVATION_VALIDATION_MAP`, `audit-data`, `README`, or
  lane-registry touches.
- **Status authority:** independent audit lane only; note labels
  itself `bounded_theorem` with claim scope explicit, no audit-status
  promotion or prediction.
- **No main push, no merge.**

## Honest status

The narrow note proves the Klein-four APBC orbit partition closed
form `|Φ(L_t)/K_4| = ceil(L_t/4)` for every even `L_t`, with the
single-orbit characterization `L_t ∈ {2, 4}` and the unique minimal
resolved-orbit characterization `L_t = 4` (size 4, weight `sin² = 1/2`
uniform). This closes the parent note's Theorem 4 selector content
at closed-form scope, strengthening the parent's runner-scope finite
scan and the `HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE`'s qualitative
claim. The P1 admitted premise of the parent is **not** addressed by
this block (the load-bearing step is orthogonal); the parent's
`audited_conditional` audit verdict is unchanged.
