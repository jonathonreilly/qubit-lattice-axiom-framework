# SM One-Generation Anomaly Closure From Retained Anchors — Decoupled From `anomaly_forces_time` (Bounded Theorem)

**Date:** 2026-06-08
**Type:** bounded theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling. Status authority is
the independent audit lane only; this note asserts no audit verdict and claims
no "retained"/"promoted" standing. **Audit-readiness purpose:** its load-bearing
dependencies are all retained-grade, so the row is deps-all-retained ("ready")
and does not route through the unaudited `anomaly_forces_time_theorem`.
**Primary runner:**
[`scripts/audit_companion_sm_anomaly_closure_retained_anchors_2026_06_08.py`](../scripts/audit_companion_sm_anomaly_closure_retained_anchors_2026_06_08.py)
(SCORECARD PASS=11 FAIL=0, exact `fractions.Fraction` / integer parity).

## Why this note exists (audit-unblock)

The one-generation matter-content / anomaly-cancellation results
(`axiom_first_sm_anomaly_cancellation_complete`,
`sm_hypercharge_uniqueness_without_nu_r`,
`rh_sector_anomaly_cancellation_identities`) are correct but sit at
`awaiting_audit`: every one routes a dependency through
`anomaly_forces_time_theorem` (unaudited, with documented circular admissions),
so none becomes deps-all-retained and none reaches the auditor dispatch queue.
This note reproves the **load-bearing arithmetic** of that chain from
retained anchors plus **explicit admissions**, so the result is auditable on its
own. It is the same decoupling move that
`sm_hypercharge_uniqueness_without_nu_r` made against
`HYPERCHARGE_IDENTIFICATION` — completed: here the minimal right-handed
completion is stated as an explicit admitted premise rather than imported from
`anomaly_forces_time_theorem`.

## Premises

- **(R1, retained)** Native cubic `SU(2)` gauge structure and `N_c = 3` colour:
  [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md),
  [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md).
- **(R2, retained)** Left-handed content `Q_L : (2,3)_{+1/3}`, `L_L : (2,1)_{-1}`
  (doubled-Y), with the `+1/3 : -1` hypercharge ratio:
  [`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
  (retained_bounded).
- **(R3, retained)** Three generations `n_gen = 3`:
  [`THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md`](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md).
- **(Axiom)** The `{Lattice, Quantum, Record}` baseline:
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).
- **(P, admitted premise — stated, not imported)** the **minimal SU(2)-singlet
  right-handed completion** `u_R:(1,3)`, `d_R:(1,3)`, `e_R:(1,1)` (no `ν_R`).
  This is an admission (see Honest ledger C1); it is **not** derived here and
  **not** imported from `anomaly_forces_time_theorem`.
- **(External)** Standard ABJ anomaly cancellation (Adler 1969; Bell-Jackiw
  1969), Dynkin indices `T(3)=T(2)=1/2`, `SU(3)` cubic indices
  `A(3)=+1, A(3̄)=-1`, and Witten `π₄(SU(2))=ℤ₂` — admitted-context external
  mathematical facts (comparator role).

## Statement and result

**Theorem (bounded).** Under (R1)–(R3), the axiom baseline, and the admitted
minimal RH completion (P):

1. **RH hypercharges uniquely forced.** Anomaly cancellation
   (`Tr[SU(3)²Y]=0`, `Tr[Y]=0`, `Tr[Y³]=0`) on the no-`ν_R` sector forces
   `(Y(u_R), Y(d_R), Y(e_R)) = (+4/3, -2/3, -2)` (doubled-Y). The quadratic for
   `(y_1,y_2)` has discriminant `4` (a perfect square ⇒ rational, unique), and
   the `Q(u_R) > 0` convention fixes the `u_R ↔ d_R` swap.
2. **All six gauge-anomaly conditions cancel exactly** on the one-generation
   content `{Q_L, L_L, u_R, d_R, e_R, (ν_R)}`:
   `SU(3)³ = 0`, `SU(2)²U(1)_Y = 0`, `grav²U(1)_Y ≡ Tr[Y] = 0`,
   `U(1)_Y³ = 0`, `SU(2)` Witten `N_D = 12` (even), and `SU(2)³ = 0`
   (group-theoretic). Each is an exact `Fraction`/integer equality.

This reproduces the arithmetic of `axiom_first_sm_anomaly_cancellation_complete`
and `sm_hypercharge_uniqueness_without_nu_r`, **without** their dependency on
`anomaly_forces_time_theorem`.

## Honest forced / admitted / convention ledger

What is **forced** (given the content): the RH hypercharge **values** and the
**cancellation** of all six anomalies. What is **not** forced (verified in the
runner):

- **C1 (admission — the content).** The matter content is **not**
  anomaly-unique: the SM content **plus a vectorlike pair** `(Y, -Y)` also
  cancels `Tr[Y]` and `Tr[Y³]`. So the minimal RH completion (P) is an admitted
  ansatz, not an anomaly consequence. (Excluding vectorlike/mirror content is the
  separate chirality question, which reduces to the staggered-Dirac /
  spin-statistics import and the Koide chiral-vs-vector binary — not closed here.)
- **C2 (convention — the scale).** The **absolute** hypercharge scale is a
  vacuous rescaling convention: scaling all `Y` by any `λ` preserves every
  anomaly zero. Only the **ratios** are content; the scale is a gauge/
  normalization choice (the `Y₀` convention), not an admitted number.
- **C3 (admission — `ν_R`).** Adding `ν_R` with free `y₄` reopens a 1-parameter
  anomaly-free family; neutrality `y₄ = 0` is load-bearing only when `ν_R` is
  included. The runner checks the full family member
  `y_u = 4/3 + t`, `y_d = -2/3 - t`, `y_e = -2 - t`, `y_ν = t` at `t=1/2`,
  verifying `SU(3)^2Y = 0`, `Tr[Y] = 0`, and `Tr[Y^3] = 0`. The no-`ν_R`
  minimal sector closes without it.

## What this does and does not claim

- **Does:** given retained (R1)–(R3) and the admitted minimal RH completion,
  the RH hypercharges are uniquely `(+4/3,-2/3,-2)` and all six gauge anomalies
  cancel — reproven from primitives, decoupled from `anomaly_forces_time`.
- **Does not** derive the matter **content** (the chiral reps), nor exclude
  vectorlike/mirror completions, nor select the `ν_R` branch, nor fix the
  absolute `Y`-scale — these are admissions/conventions (C1–C3).
- **Does not** derive `N_c = 3`, `n_gen = 3`, the LH content, the ABJ formula,
  or Witten's homotopy fact — these are retained inputs (R1–R3) or
  admitted-context external facts.
- Introduces **no** new axiom and changes **no** numerical prediction.

## Reprove-and-cite

- The character/anomaly arithmetic (six conditions, RH uniqueness, the C1–C3
  caveats, including the full `ν_R` one-parameter family check) is reproven
  exactly in the runner, not asserted by name.
- Prior packaging of the same arithmetic (cited as context, **not** as
  load-bearing markdown deps, to keep this row deps-all-retained):
  `axiom_first_sm_anomaly_cancellation_complete_theorem_note_2026-05-03`,
  `sm_hypercharge_uniqueness_without_nu_r_input_theorem_note_2026-05-02`,
  `rh_sector_anomaly_cancellation_identities_note_2026-05-02`. This note
  **decouples** that result from `anomaly_forces_time_theorem`.
- Adler 1969; Bell-Jackiw 1969; Witten 1982 — external comparator authorities.

## Forbidden-imports check

No PDG values, fitted selectors, or literature numerical comparators are used as
derivation inputs. The ABJ trace formulae, Dynkin indices, `SU(3)` cubic
indices, and the Witten homotopy fact are named external mathematical content
(comparator role), reproven-in-runner where arithmetical. The absolute `Y`-scale
is treated as a convention, not consumed as a number.
