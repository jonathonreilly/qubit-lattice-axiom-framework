# BZ Volume `(2π)³` on `Z³`: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing substrate-internal identification
`vol_Lebesgue([-π, π]³) = (2π)³` and
`mu_Haar(dk) = d³k / (2π)³` of the parent note
[`BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md`](BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md)
is invariant under the 2026-06-04 Record-axiom adoption. It is not a new
theorem claim, not a status promotion, and not an attempt to perform
re-audit work. If the audit pipeline seeds this file, it is a meta
companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that authority.
**Companion target:** `bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26`
(parent note `docs/BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md`).
**Primary companion runner:**
[`scripts/audit_companion_bz_volume_two_pi_cubed_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_bz_volume_two_pi_cubed_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_bz_volume_two_pi_cubed_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_bz_volume_two_pi_cubed_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent narrow theorem
`bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26`
was previously audit-loop-resolved on 2026-05-28 as `audited_clean`
(`bounded_theorem`, criticality leaf) by a single auditor verdict on the
narrowed scope:

> From the accepted `Z^3` spatial substrate plus standard
> Pontryagin-duality and Haar-normalization facts, the Brillouin-zone
> dual is `T^3` and its Haar probability measure in `[-π, π]^3`
> coordinates is `d^3k / (2π)^3`. The continuum `R^3` Fourier
> denominator is certified only as a downstream numerical comparison,
> not a load-bearing import.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per `docs/audit/AXIOM_MINIMALITY_POLICY.md`
section 6) changed the stable `minimal_axioms` premise-node note-hash
from `1d36a556` to `b8848fc8`. The audit pipeline correctly invalidated
the prior `audited_clean` snapshot via
`invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`,
returning the row to unaudited effective status.

This companion records, for the audit lane, that the parent's
load-bearing chain is **independent of the Record axiom**: it uses only
the Lattice axiom content (`Z^3` site set) plus standard textbook
abelian-harmonic-analysis identities (Pontryagin duality on locally
compact abelian groups; Haar uniqueness on a compact abelian group).
Adopting the Record axiom adds a strictly additive scalar
record-readout statement, which is neither used nor invoked anywhere in
the BZ volume / Haar normalization calculation. The numeric constant
`(2π)³ = 248.0502...`, the Haar density `1/(2π)³`, and the dual-group
identification `(Z^3)^* ≅ T^3 = [-π, π]^3` are unchanged.

This companion is therefore audit-friendly evidence that the prior
clean verdict's substantive content survives the axiom-set change. It
is not a re-audit and does not promote status; it documents the
load-bearing-step dependency surface in machine-checkable form so the
audit lane can decide whether to honor or re-test the prior verdict on
the new premise hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the BZ volume identification.** The
parent's load-bearing chain (Theorem statements T1-T5 and proof-walk
steps B1-B6 of
`BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md`)
depends only on:

1. the `Z^3` site set (Lattice axiom content);
2. Pontryagin duality for discrete cyclic `Z` and for finite products
   (standard locally-compact abelian harmonic analysis; textbook);
3. the Lebesgue product measure on `R^3` (standard real analysis);
4. Haar uniqueness on a compact abelian group (textbook).

None of items 1-4 use the Record axiom's additive scalar record-readout
content. The Quantum axiom (one-qubit local algebra on each site) does
not enter the BZ-volume identification either — the parent's chain is
purely dual-group geometry on the Lattice substrate. The continuum
comparison step B7 is explicitly recorded as non-load-bearing in the
parent.

**(C1) is the only auditable companion observation.** The bridge from
the BZ volume `(2π)^3` factor to downstream Plancherel integrand rows
(e.g. the Maradudin cubic Green's function row) and to any hierarchy
formula primitive remains explicitly out of scope, exactly as in the
parent note ("Honest assessment" and "Boundaries" sections).

This companion does **not**:

- introduce a new minimal-axiom statement (the explicit-owner-approved
  axiom set is fixed at `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs;
- assert anything about Record-axiom content or its scope;
- re-audit
  `bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26`
  or any other ledger row;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to re-honor
the previous verdict or whether a fresh per-site audit is warranted on
the new premise hash.

---

## The Record axiom is not used by the load-bearing chain

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` §"Record") says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The parent's load-bearing chain defines no record surface, asks no
question about scalar record additivity, and writes no record
functional `I(.)`. It records four substrate-internal facts:

- (T1) The Pontryagin dual of `Z^3` is `T^3 := (R/2πZ)^3`.
- (T2) `vol_Lebesgue([-π, π]^3) = (2π)^3` (Lebesgue product measure).
- (T3) `mu_Haar(dk) = d^3k / (2π)^3` (Haar probability normalization on `T^3`).
- (T4) The same numerical constant `(2π)^3` appears in the continuum
  `R^3` Fourier convention `d^3k / (2π)^3`.
- (T5) No continuum import is consumed in (T1)-(T3); the (T4)
  comparison is a downstream observation.

All five statements are fixed by:

- the `Z^3` site set (Lattice axiom content);
- Pontryagin duality (textbook abelian harmonic analysis);
- Lebesgue product measure on `[-π, π]^3` (standard real analysis);
- Haar uniqueness on a compact abelian group (textbook).

The Record axiom adds an additive scalar record functional. It does
not modify (and is not modified by) the dual-group identification of
`Z^3`, the Lebesgue volume of `[-π, π]^3`, or the Haar measure
uniqueness on a compact abelian group. The numeric constant
`(2π)^3 ≈ 248.0502...` and the Haar density `1/(2π)^3 ≈ 0.004031...`
are invariant under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic check passes using only Lattice axiom
content plus standard real-analytic / abelian-harmonic-analysis
identities, and a "Record-axiom counterfactual" block confirms the
constants are unchanged whether or not a Record-axiom statement is
appended.

---

## Companion runner block plan

`scripts/audit_companion_bz_volume_two_pi_cubed_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the BZ-volume / Haar
normalization load-bearing chain. Each block runs as an independent
numeric/algebraic check; nothing is hard-coded against an expected
target value beyond standard real analysis and abelian harmonic
analysis. The runner reports `PASS` / `FAIL` per check; the cached
output records the run.

Block 1 — 1D fundamental domain volume. Verifies
`vol_Lebesgue([-π, π]) = 2π` exactly (sympy) and numerically.

Block 2 — 2D fundamental domain volume. Verifies
`vol_Lebesgue([-π, π]^2) = (2π)^2` exactly and numerically.

Block 3 — 3D fundamental domain volume (the load-bearing BZ volume).
Verifies `vol_Lebesgue([-π, π]^3) = (2π)^3` exactly and numerically.
This is the parent's step B4-3D and the substrate-internal `(2π)^3`.

Block 4 — Haar density and probability normalization. Verifies
`∫_{[-π, π]^3} 1/(2π)^3 dk = 1` via discrete Riemann-sum integration
with multiple grid resolutions; confirms `1/(2π)^3 ≈ 0.004031441...`.

Block 5 — Continuum-comparison numerical match. Verifies that the
substrate-internal `(2π)^3` from Block 3 matches the same numerical
constant used in the continuum `R^3` Fourier convention
`d^3k / (2π)^3` (parent's step B7, explicitly non-load-bearing).

Block 6 — Pontryagin-dual functoriality on finite products.
Verifies the dual-group fact `(Z^3)^* ≅ (Z^*)^3 = (T^1)^3 = T^3` by
explicit construction of characters `χ_k(n) = e^{i k · n}` for
`k ∈ [-π, π]^3` and `n ∈ Z^3`, confirming periodicity in `k` with
period `2π` per coordinate and orthogonality of distinct characters.

Block 7 — Haar uniqueness on a compact abelian group. Verifies
translation-invariance of the Haar measure on `T^3` numerically: for
finitely many test shifts `τ` of a finitely-supported test function,
`∫ f(k - τ) mu_Haar(dk) = ∫ f(k) mu_Haar(dk)` within Riemann-sum
truncation error.

Block 8 — Static-source scan of parent note's load-bearing section:
zero Record-axiom usage tokens. Enumerates the phrase set
`{"I(R_1", "I(R)", "scalar record", "record functional",
"record-readout", "additive record", "additive scalar record",
"MINIMAL_AXIOMS_2026-06-04"}` over the parent's `## Theorem`,
`## Proof-walk`, `## Exact arithmetic check`, and `## Numerical
certificate` sections and confirms zero matches.

Block 9 — Static-source scan of parent note for Lattice axiom
content. Confirms the parent's load-bearing chain explicitly cites
`Z^3` and `T^3` (or `[-π, π]^3`) as the substrate and dual.

Block 10 — Record-axiom counterfactual: identical numeric output.
Re-runs Blocks 3-4 inside an explicit "Record axiom asserted" outer
scope and an explicit "Record axiom not asserted" outer scope;
verifies `(2π)^3 = 248.0502...` and Haar normalization
`∫ mu_Haar = 1` are identical in both runs. The counterfactual is a
tautology at the calculation level (no Record-axiom content enters
the Lebesgue / Pontryagin / Haar steps), which is precisely the
substantive content of (C1).

Block 11 — Quantum / Lattice content preservation across the
historical 2026-05-20 and current 2026-06-04 minimal-axioms memos.
Confirms the `Z^3` lattice content used by the parent is preserved
under the new wording.

Block 12 — Independent recomputation of `(2π)^3`. Computes
`(2π)^3` four ways (1-D × 1-D × 1-D Lebesgue product; cube of
`2π`; Haar denominator from probability normalization condition;
numerical Riemann sum) and verifies that all four agree to
machine precision.

Total: 12 blocks. The exact PASS/FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status`), no status field changes are implied by this PR.
The audit lane decides whether to re-honor the prior verdict on the new
premise hash; this companion only supplies machine-checkable evidence
on whether the new Record axiom disturbs the load-bearing chain.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
output (e.g. the Maradudin cubic Green's function row, the hierarchy
formula primitives, any 4D loop-measure analysis). Each downstream
claim must be examined independently against the new axiom-set premise
hash. The other rows recently axiom-invalidated under the same hash
change are out of scope of this companion; they are listed in the
audit queue's `axiom_premise_changed` cohort and should be examined
separately as the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`MINIMAL_AXIOMS_2026-05-20.md` citations to
`MINIMAL_AXIOMS_2026-06-04.md`. Both are valid framework axiom memos;
the 2026-06-04 memo cites the 2026-05-20 memo as the "local-algebra
authority and historical source for the prior two-axiom wording." A
separate citation-migration PR (if desired) can refresh the parent
note's load-bearing-dependencies column; this companion is independent
of that text update and is content-only.

This companion's load-bearing-chain invariance observation depends only
on the Lattice content being preserved across the two memos — verified
in Block 11 — and on the Record axiom adding a strictly additive
non-overlapping statement — confirmed by direct reading of
`MINIMAL_AXIOMS_2026-06-04.md` §"Record".

---

## References

- Parent note:
  [`BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md`](BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md)
- Parent runner:
  `scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py`
- Prior verdict snapshot:
  `docs/audit/data/audit_ledger.json` row
  `bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26`,
  `previous_audits[-1]` (`audited_clean`, `bounded_theorem`, leaf,
  single-auditor verdict, 2026-05-28, archived 2026-06-04 with
  `invalidation_reason=axiom_premise_changed:minimal_axioms:1d36a556->b8848fc8`)
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
