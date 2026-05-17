# `DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`](DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`
is a **bounded proof-walk** that establishes lattice-independence of the
`d_t = 1` forcing chain inside the cited
`ANOMALY_FORCES_TIME_THEOREM.md`. It exhibits, step-by-step, that the
load-bearing inputs at each step of the parent's argument are
algebraic/structural (multiplicities, Dynkin indices, Clifford parity,
single-clock codimension-1 evolution) and that none of them is a
lattice-action quantity (Wilson plaquette, staggered phases,
Brillouin-zone labels, link unitaries, `u_0`, MC measurement, fitted
observational value).

This downstream fix-record does **not** change that character. It only:

1. corrects a stale citation-routing target (F-C, inherited from the
   same routing bug fixed upstream in PR [#1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500));
2. corrects stale dependency-tier descriptors (F-A); and
3. makes the upstream-admission inheritance explicit and links to the
   parent's F-B framing-fix (PR [#1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502)).

## 2. Findings

### F-C — Stale citation routing for the chirality grading

**Symptom:** the proof-walk's Step 2 row and the Dependencies list cited

> [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) — for the Clifford-volume /
> sublattice-parity chirality grading `ε(x) = staggered γ_5` cited at
> Steps 2 and 3 of the source note.

**Reality:** `CPT_EXACT_NOTE.md` defines `ε(x) = (-1)^(x_1+x_2+x_3)`
only as the **charge conjugation operator `C`**. It contains zero `γ_5`
content and no anti-commutation derivation `{ε, D_staggered} = 0`. The
two roles of `ε(x)` (chirality grading vs charge conjugation) share
notation but are algebraically orthogonal.

**Correct routing target:**
`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`,
whose Step 4 derives `{ε, D_staggered} = 0` from site-chirality +
no-rooting irreducibility. This is the same routing fix applied
upstream in
[`ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md).

**Fix:** Step 2 of the proof-walk table now routes to the Kawamoto-Smit
forcing note; the Dependencies list replaces the `CPT_EXACT_NOTE` entry
with the correct entry; both edits include a one-sentence note about
the algebraic-orthogonality of the two `ε(x)` roles to help readers
disambiguate.

### F-A — Stale dependency tier descriptors

**Symptom:** two places in the note described the cited single-clock
codimension-1 evolution theorem and the chirality grading as

> "both proposed_retained (audit-pending)"

(in the Boundaries block) and

> "(proposed_retained, audit-pending)"

(in the Step 4 row of the proof-walk table).

**Reality (per 2026-05-17 ledger snapshot):**

| `claim_id` | `audit_status` | `effective_status` |
|---|---|---|
| `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | `unaudited` | `unaudited` |
| `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | `unaudited` | `unaudited` |

Both descriptors are stale (`proposed_retained, audit-pending` ≠
`unaudited`).

**Fix:** both descriptors corrected to `unaudited`, with an explicit
acknowledgment that any future audit-status change on those companions
propagates directly into this proof-walk's effective tier. No claim
about the proof-walk's own internal correctness changes.

### F-B — Upstream admission-inheritance acknowledgment

**Symptom:** the proof-walk's Step 3/Step 4 split already mirrors the
upstream parent's `d_t = 1` decomposition:

- Step 3 conclusion in the table: `d_t in {1, 3, 5, ...}` (derived from
  Clifford parity + `d_s = 3` axiom A2);
- Step 4 in the table: single-clock codimension-1 evolution excludes
  `d_t > 1` (collapsing to `d_t = 1`).

But the note did not link this split to the upstream parent's recent
**F-B framing-fix**
([`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md),
PR [#1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502)),
which identifies the same decomposition at the parent level as:

- **Derived (Step 3):** `d_t ∈ {1, 3, 5, ...}`
- **Inherited (admission (iv)):** `d_t > 1` excluded

A downstream reader could not see from this note alone that the Step 4
row is the **inherited (admission (iv))** branch of the parent's
framing-fix decomposition.

**Fix:** the Step 4 row now explicitly links to the upstream F-B
framing-fix and labels itself as the inherited branch. The proof-walk's
own claim is unchanged: it still asserts lattice-independence of the
entire `d_t = 1` chain (both branches) modulo the cited authorities.

## 3. What this fix does NOT do

- It does **not** change the bounded_theorem claim type.
- It does **not** change the proof-walk's verdict
  (lattice-independence).
- It does **not** change the list of load-bearing inputs at any step.
- It does **not** re-derive or promote the cited single-clock theorem
  or the chirality-grading theorem.
- It does **not** propose a status promotion for this proof-walk.
- It does **not** modify any pipeline code, any retained-tier claim, or
  any other source theorem note.
- It does **not** set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (bounded proof-walk retained; effective tier
inherits the weaker of the cited companions' tiers, which are both
currently `unaudited`).

The corrected note:

- routes the chirality-grading citation to the companion that actually
  derives it;
- gives honest tier descriptors for the cited companions;
- makes the upstream-admission inheritance from
  `ANOMALY_FORCES_TIME_THEOREM` explicit.

Once the cited companions audit through, the proof-walk's effective
tier rises accordingly without further surgical edits.

## 5. Verification

Paired runner:
`scripts/frontier_dt1_time_dimension_proof_walk_downstream_fix.py`

Programmatically verifies:

- **F-C:** Step 2 table row and Dependencies list now cite
  `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07`; the
  stale `CPT_EXACT_NOTE` routing is no longer the sole/primary
  chirality-grading citation; `CPT_EXACT_NOTE` contains 0 `γ_5`
  occurrences; the KS companion contains the `{ε, D_staggered} = 0`
  anticommutator derivation.
- **F-A:** stale `proposed_retained` / `audit-pending` descriptors
  retired for the two cited companions; `unaudited` descriptors
  appear; the 2026-05-17 corrective wording is present.
- **F-B:** Step 4 row of the proof-walk table now references the
  upstream `F-B` framing-fix note and labels itself as the
  inherited (admission (iv)) branch; the derived-branch label appears
  for Step 3.
- **Structural invariants:** `bounded_theorem` claim type unchanged;
  proof-walk table still names Steps 1-5 with the same step labels;
  the "load-bearing inputs" list is unchanged in scope; the verdict
  wording is preserved.

Cached output: `logs/runner-cache/frontier_dt1_time_dimension_proof_walk_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`](DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent
- [`ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md) — upstream `F-B` fix
- [`ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_ADMISSION_III_ROUTING_CORRECTION_NOTE_2026-05-17.md) — upstream `F-C` fix (same routing pattern)
- [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — corrected routing target
- [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) — formerly mis-routed authority
- [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) — Step 4 cited companion (tier descriptor corrected)
- [PR #1500](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1500) — upstream `F-C` PR
- [PR #1502](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1502) — upstream `F-B` PR
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream surgical-fix (`s3_anomaly_spacetime_lift_note`)
