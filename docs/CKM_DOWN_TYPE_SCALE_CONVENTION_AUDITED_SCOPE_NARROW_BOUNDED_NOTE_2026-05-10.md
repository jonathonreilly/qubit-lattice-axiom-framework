# CKM Down-Type Scale-Convention Audited-Scope Narrowing Bounded Note

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Historical runner relationship:** the 2026-05-10 version shared its parent's
then-current runner. The 2026-07-12 parent repair replaces that runner's claim
and output surface; the current parent runner is not a reproduction surface for
this historical narrowing note.

**Downstream hygiene (2026-07-12):** the parent now proves a bounded
shared-transport covariance theorem and no longer treats the sub-percent
cross-surface match as derivation evidence. The sections below record the old
audit scope in the past tense. They do not pin current runner output or current
science status.

## Why this note exists

The 2026-05-05 audit pass on the parent
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
returned `audited_numerical_match` with the explicit verdict:

> The runner mostly verifies arithmetic over imported constants and
> external PDG-style inputs, and it hard-codes the decisive full-loop
> transport factor as 1.14747 after noting its own one-loop computation
> gives a different value. The note is candid that the 5/6 bridge and
> the threshold-local scale choice are not theorem-grade closures. The
> load-bearing support is therefore a numerical match at a selected
> comparator scale, not a first-principles derivation or clean
> algebraic closure from retained inputs.

with re-audit guidance:

> missing_bridge_theorem: provide a retained derivation of the 5/6
> bridge and a retained argument selecting the threshold-local mass
> comparator, then rerun without hard-coding the contested transport
> factor.

This note narrows the parent's audited scope into the explicitly
algebraic and arithmetic content that the runner does close, separated
from the open-bridge dependencies that the parent itself flags.

This is a bounded scope-narrowing companion of the parent's historically
audited pre-repair source version; the rewritten parent row is currently
`bounded_theorem`, `unaudited`. It does not add a new axiom, does not add a new
repo-wide theory class, does not propose a status promotion, and does not
modify the parent note's audit ledger row.

## Audited verdict (verbatim, for clarity)

- `audit_status: audited_numerical_match`
- `audit_date: 2026-05-05`
- `chain_closes: false`
- `claim_scope` (audited): "Audited the support-level numerical
  scale-convention identity relating threshold-local and common-scale
  down-type mass-ratio comparisons, conditional on the imported
  alpha_s(v), 5/6 bridge, PDG mass inputs, and QCD transport factor."

The parent note's `Status` line and `Scope qualifiers` section already
record the same boundary in source form. This narrowing companion
isolates the **within-scope algebraic content** that the audit
verdict accepts as a numerical match.

## Narrow within-scope content (what the audited row does close)

Inside the audited support-level scope, the historical runner verified the
following identities. This table describes the source version reviewed in
2026-05, not the current parent runner:

| Identity | Class | Status |
|---|---|---|
| `C_F - T_F = 5/6` from SU(3) Casimir arithmetic | exact rational | audited PASS (sympy) |
| `|V_cb|_atlas = alpha_s(v) / sqrt(6)` | supplied CKM-atlas comparator identification, conditional on `alpha_s(v)` | audited PASS (historical) |
| 1-loop mass-anomalous-dimension exponent `gamma_m / (2 beta_0) = 12/25` for `n_f = 4` | exact rational from SU(3) Casimir bookkeeping | audited PASS |
| `R_thresh = R_common * transport_1loop` | comparator bookkeeping; the 1-loop-truncated factor is not an exact all-orders QCD transport | audited PASS (10^-10) |
| `(R_pred / R_common) / (R_pred / R_thresh) = transport_1loop` | algebraic consequence of the previous identity | audited PASS (10^-10) |

The historical audit treated these identities and the reproduced numerical
match as comparator-relative support. The 2026-07-12 parent repair supersedes
that interpretation: it transports both theory and observation and proves that
the relative deviation stays on the common-scale value.

## What the narrow scope does **not** close

The audit verdict and the parent's own scope qualifiers section
already flag these explicitly. This companion note records them in
one place for re-audit traceability:

- the theorem-grade derivation of the `5/6` bridge itself (the parent
  cites [`CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md`](CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md)
  as bounded support);
- a retained theorem forcing the threshold-local comparator as the
  unique framework-natural mass-scale convention;
- elimination of the historical runner's hard-coded full-loop PDG transport
  factor `1.14747` in favour of a covariant theory/observation comparison;
- the down-type mass-ratio lane's bounded -> retained promotion;
- the canonical parent note
  [`QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md`](QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md)
  records the same scale-selection boundary as a separate bounded
  theorem.

## 2026-07-12 parent repair and remaining work

The parent repair now supplies an exact abstract rank-`1+5` determinant lemma
and proves that shared multiplicative transport cannot rescue the crossed
sub-percent comparison. It does not claim the full bridge. The remaining
positive target is:

1. a retained theorem deriving the `5/6` bridge `|V_cb| = (m_s/m_b)^{5/6}`
   from framework primitives at `g = 1` (non-perturbative
   exponentiation mechanism);
2. a retained typed map from that mass operator to the CKM amplitude through
   the normalized determinant;
3. a common or explicitly RG-covariant mass surface. A directly mixed surface
   must carry its scale prescription inside the mass/operator map.

The independent audit lane owns the repaired parent's later classification.

## Dependencies

- [`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
  for the parent bounded support note (historically audited pre-repair; the
  rewritten row is currently `bounded_theorem`, `unaudited`).
- [`CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md`](CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md)
  for the open 5/6 bridge dependency.
- [`QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md`](QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md)
  for the canonical scale-selection boundary statement.
- [`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md)
  for the `alpha_s(v)` comparator (currently `bounded_theorem`, `unaudited`;
  conditional on the reused plaquette `<P>=0.5934`).
- [`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](CKM_ATLAS_AXIOM_CLOSURE_NOTE.md)
  for the supplied `|V_cb|_atlas = alpha_s(v) / sqrt(6)` identification
  (currently `positive_theorem`, `unaudited`; a supplied identification, not a
  derivation).

These are imported comparator authorities for a bounded scope-narrowing
companion note.
The row remains unaudited until the independent audit lane reviews this
companion and its dependencies.

## Boundaries

This companion note does **not**:

- modify the parent note's audit-ledger row;
- promote the parent's `audit_status` from `audited_numerical_match`;
- re-derive the `5/6` bridge or the scale-selection theorem;
- reproduce or pin the current parent runner's output;
- extend the audited scope beyond what the parent already declares.

## Verification boundary

This historical narrowing note has no current paired runner. The parent runner
now verifies a different theorem surface and must not be used to reproduce the
old `PASSED: 14/14` transcript. The archived audit ledger preserves the old
runner classification and verdict provenance.

```yaml
claim_id: ckm_down_type_scale_convention_audited_scope_narrow_bounded_note_2026-05-10
note_path: docs/CKM_DOWN_TYPE_SCALE_CONVENTION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md
runner_path: null
proposed_claim_type: bounded_theorem
deps:
  - ckm_down_type_scale_convention_support_note_2026-04-22
  - ckm_five_sixths_bridge_support_note
  - quark_five_sixths_scale_selection_boundary_note_2026-04-28
  - alpha_s_derived_note
  - ckm_atlas_axiom_closure_note
audit_authority: independent audit lane only
```
