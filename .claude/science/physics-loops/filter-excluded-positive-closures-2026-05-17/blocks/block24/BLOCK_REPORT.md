# Block 24 Report: lh-doublet-traceless-abelian (fresh EW lane)

**Block:** 24 (electroweak, fresh lane)
**Date:** 2026-05-17
**Target:** `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02`
**Branch:** `physics-loop/lh-doublet-traceless-abelian-block24-2026-05-17`
**Worktree:** `/private/tmp/physics-loop-2026-05-17/block24-lh-doublet-traceless-abelian`

## Outcome

**POSITIVE narrow closure landed** as a Pattern-A bounded class-A narrow
theorem on the *inverse* direction of the LH-doublet traceless abelian
eigenvalue algebra. The new narrow theorem completes the forward/inverse
pair on the LH-doublet `(6+2)` trace-surface state count: the existing
2026-05-02 narrow theorem closes "given the partition `(6, 2)`, the
ratio is `1 : (-3)`"; this block lands "given the state count `N = 8`
and target integer ratio `-3`, the partition `(6, 2)` is unique".

## Audit landscape ground (V1)

Pulled from `docs/audit/data/audit_ledger.json` at session start:

- `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02`
  — `audited_clean` (audit_status), `retained_bounded` (effective_status),
  `bounded_theorem` (claim_type), `transitive_descendants = 894`.
- The brief listed the target as "unaudited 704 desc"; the live ledger
  shows the target was already audited_clean at session start with
  894 descendants. The block therefore did not retry an audit on an
  already-audited row; instead it landed a positive narrow corollary
  on the orthogonal *inverse* direction.
- Cited authorities are both retained-bounded:
  - `graph_first_su3_integration_note` (`retained_bounded`)
  - `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02` (`retained_bounded`)
- Adjacent existing narrow theorems:
  - `lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10` —
    parametric strengthening in the *forward* direction (`audited_clean`)
  - `lh_doublet_eigenvalue_ratio_proof_walk_lattice_independence_bounded_note_2026-05-10` —
    proof-walk lattice-independence note (`audited_clean`)

No existing narrow theorem closes the inverse direction. This block
landed the orthogonal inverse-uniqueness narrow theorem.

## V1-V5 fresh-lane check

- **V1 existence:** no existing narrow theorem isolates the
  inverse-uniqueness claim ("given state count `N` and target integer
  ratio `-k`, the integer-multiplicity partition `(m, n)` of `N` with
  `m / n = k` is unique whenever it exists"). The forward direction is
  covered by the 2026-05-02 narrow theorem and parametrically
  strengthened by the 2026-05-10 narrow theorem; the inverse direction
  is new content.
- **V2 premise check:** premises are positive-integer hypotheses on
  `(N, k)` plus elementary divisibility. No new axioms; no graph-first
  selectors; no SM identification.
- **V3 orthogonality:** no load-bearing markdown-link dependencies. The
  proof goes through unchanged for any positive integer `N >= 2` and any
  positive integer `k >= 1`. The cross-references to the forward narrow
  ratio theorem and the graph-first SU(3) integration note are
  explicitly *non-load-bearing* sanity-readout references that supply
  the framework-instance values `N = 8, k = 3`, not the abstract
  theorem statement.
- **V4 downstream:** the existing forward narrow theorem and the parent
  `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` can cite this inverse narrow
  theorem to discharge the implicit assumption that the `(6, 2)`
  partition is the *only* integer-multiplicity partition of `8`
  consistent with the target integer ratio. The forward/inverse pair
  together establishes biuniqueness between the `(6, 2)` partition and
  the `-3` ratio on the LH-doublet 8-state surface; this is a
  load-bearing tightening of the parent chain's "the (6, 2) partition
  is forced" assertion.
- **V5 forbidden imports:** none consumed (no PDG, no fitted, no SM
  hypercharge identification, no convention `b = -1`, no staggered-Dirac
  realization input). The proof uses only positive-integer divisibility
  and exact Fraction/sympy arithmetic.

## Artifacts

- **Source note:**
  `docs/LH_DOUBLET_PARTITION_RATIO_INVERSE_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md`
  (`claim_type: bounded_theorem`; staggered-Dirac open-gate inheritance
  on the framework-instance side only, not on the abstract algebra).
- **Runner:**
  `scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py`
  (Pattern A exact: sympy symbolic + Fraction explicit; 58 checks).
- **Runner cache:**
  `logs/runner-cache/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.txt`
  (full runner stdout, 111 lines).
- **Block report:** this file.

## Runner result

```
Summary: PASS=58  FAIL=0
Verdict: PASS.
```

Items covered (all class-A exact algebra; sympy symbolic solve +
Fraction explicit + integer divisibility):

- `(R1)` parametric ratio identity `beta/alpha = -m/n` via sympy
  symbolic `solve()` plus a 6-triple explicit `Fraction` sweep.
- `(R2)` closed-form `(m, n) = (k*N/(k+1), N/(k+1))` checked across
  11 admissible `(N, k)` pairs.
- `(R3)` admissibility `(k+1) | N and N >= k+1` checked exhaustively
  over `N in {2..32}` and `k in {1..15}` (465 pairs).
- `(R4)` uniqueness inside `P(8)`: all 7 ordered partitions enumerated;
  each ratio appears in exactly one partition; integer-ratio partitions
  are exactly `{(4,4), (6,2), (7,1)}`; `(6, 2)` is the unique partition
  with ratio `-3`.
- Framework readout `(N, k) = (8, 3) -> (m, n) = (6, 2)`.
- Counterfactuals `(C4)-(C7)`: no integer partition of 8 yields ratio in
  `{-2, -4, -5, -6}` (divisibility fails for `(k+1) in {3, 5, 6, 7}`).
- Corollaries `(C2), (C3)`: `(8, 1) -> (4, 4)` and `(8, 7) -> (7, 1)`.
- Forward/inverse pair consistency: `forward(inverse(8, 3))` recovers
  ratio `-3`; `inverse(8, forward(6, 2))` recovers partition `(6, 2)`.
- Cross-referenced authorities are both `retained-grade` per the live
  audit ledger.

## Scope discipline

The narrow theorem explicitly excludes:

- derivation of `N = 8` (inherited from retained-bounded graph-first
  SU(3) integration note);
- derivation of `k = 3` (inherited from retained-bounded forward narrow
  ratio theorem);
- identification of the `(6, 2)` partition with SM quark/lepton
  multiplicities;
- derivation of the convention `b = -1` (scale-free narrow theorem);
- any SM hypercharge identification, charge formula, or anomaly
  cancellation claim.

The runner checks include a positive forbidden-imports scan asserting
that the source note does **not** contain SM-identification language
("Q = T_3 + Y/2 then matches" or "identifies … with the Standard
Model").

## Tier

Honest tier: **Pattern A narrow positive theorem (bounded_theorem
proposal; independent audit lane to ratify retained_bounded effective
status)**. The narrow theorem is class-A algebra on positive-integer
divisibility; the staggered-Dirac open-gate context input applies only
to the framework readout sub-section, not to the abstract algebra,
following the same `claim_type: bounded_theorem` discipline as the
sister forward narrow theorem.

## What this block does NOT close

- Does not promote the target row to `positive_theorem` (the
  staggered-Dirac open-gate inheritance keeps it `bounded_theorem`).
- Does not derive the framework-instance values `N = 8`, `k = 3` from
  inside the narrow theorem.
- Does not perform SM hypercharge identification.
- Does not close the parent `LEFT_HANDED_CHARGE_MATCHING_NOTE.md`'s
  full chain (which still depends on the convention `b = -1` for the
  absolute eigenvalue pattern).

## Audit-lane handoff

The audit-lane disposition (proposed) is:

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  For positive integers N >= 2 and k >= 1 with (k+1) | N and N >= k+1,
  the integer-multiplicity partition (m, n) of N with m + n = N and
  m / n = k is unique with m = k*N/(k+1), n = N/(k+1). Framework
  instance (N, k) = (8, 3) -> (m, n) = (6, 2). Inverse counterpart of
  the existing forward narrow ratio theorem. No SM identification, no
  convention b = -1, no staggered-Dirac realization input.
audit_status_authority: independent audit lane only
proposed_load_bearing_step_class: A (class-A integer divisibility + linear algebra)
audit_required_before_effective_retained: true
```

Both cited cross-references are already retained-bounded, so the
pipeline can derive a retained-bounded effective status upon
audit-lane ratification.

## A_min compliance

- A_min only (no new axioms).
- Source-only PR (1 note + 1 runner + 1 cache + 1 block report).
- No atlas / harness / audit-data / README / lane-registry touches.
- No main push, no merge.

## Hard-rule check (PR composition)

```
docs/LH_DOUBLET_PARTITION_RATIO_INVERSE_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md      [+]
scripts/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.py [+]
logs/runner-cache/audit_companion_lh_doublet_partition_ratio_inverse_uniqueness_exact_2026_05_17.txt [+]
.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block24/BLOCK_REPORT.md [+]
```

No other touches.
