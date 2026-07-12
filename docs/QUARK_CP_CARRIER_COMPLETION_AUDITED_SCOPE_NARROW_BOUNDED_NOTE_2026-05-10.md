# Quark CP-Carrier Completion Audited-Scope Narrowing Bounded Note

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_quark_cp_carrier_completion.py`](../scripts/frontier_quark_cp_carrier_completion.py)
**Current claim scope:** historical numerical existence of a CKM/J comparator
match on the stated complex-coordinate ansatz, together with an explicit
firewall that the optimized diagonal labels are not the completed matrices'
physical singular-value mass ratios.

## Why this note exists

The 2026-05-05 audit pass on the historical revision of
`QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`
returned `audited_numerical_match` with the explicit verdict:

> The load-bearing step is an optimized numerical completion using
> explicit solved carrier coefficients and imported comparator targets.
> The runner is not a trivial printout: it builds Hermitian mass
> matrices, diagonalizes them, computes CKM observables, and checks
> the determinant phase. However, the parameters xi_u and xi_d are
> tuned degrees of freedom rather than derived from the stated axiom,
> and the success criteria are external observation/atlas matches, so
> this is class G rather than first-principles class C.

with re-audit guidance:

> A second auditor should re-check the upstream imported constants and
> solve_magnitude_surface implementation if the audit scope is
> expanded beyond this restricted packet.

This note now narrows the historical fit to the explicit CKM/J and diagonal-
label content that the runner actually computes, separated from both the
physical singular-spectrum mismatch and the absence of a retained derivation
of the carrier coefficients.

This is a bounded scope-narrowing companion of an existing audited
note. It does not add a new axiom, does not add a new repo-wide theory
class, does not propose a status promotion, and does not modify the
parent note's audit ledger row.

## Historical audit context (verbatim, not current authority)

- `audit_status: audited_numerical_match`
- `audit_date: 2026-05-05`
- `chain_closes: true`
- `claim_scope` (audited): "Audited the bounded numerical existence
  claim that sector-specific complex 1-3 carriers can fit m_u/m_c,
  m_c/m_t, |V_us|, |V_cb|, |V_ub|, and J while keeping
  arg det(M_u M_d) numerically zero."

The 2026-07-12 source correction to the parent found a load-bearing readout
error not tested in that historical audit: the optimizer compared its diagonal
input labels with mass-ratio targets but never compared the completed matrices'
singular-value ratios. Independent re-audit owns the consequence of that
correction. The table below states only the current source/runner boundary.

## Narrow current source/runner content

Inside the audited bounded-existence scope, the runner verifies the
following structural facts. Each is independent of any claim that the
solved carriers `xi_u`, `xi_d` are derived from framework primitives:

| Current source/runner content | Source-side boundary |
|---|---|
| The minimal Schur-NNI anchor under-produces the CKM CP area | historical numerical control |
| The optimizer places its two diagonal labels near the imported up-sector mass-ratio comparators | diagonal-parameter fit only; not a physical mass check |
| The completed up-sector singular-value ratios are about `5.36e-3` and `4.28e-3`, not the imported `1.70e-3` and `7.38e-3` comparators | current runner PASS; physical-spectrum firewall |
| The two complex coordinates admit a numerical match of `(\|V_us\|, \|V_cb\|, \|V_ub\|, J)` on the diagonal-label ansatz | bounded numerical match |
| `arg det(M_u M_d) = 0 mod 2pi` is maintained numerically by the Hermitian fit | matrix-arithmetic check, not a carrier-phase or strong-CP derivation |
| The fitted coordinates are non-perturbatively large relative to the Schur `1-3` base term | bounded caveat |

The within-scope conclusion is an existence statement only for the CKM/J
comparator match on a diagonal-label ansatz. It is not a simultaneous physical
quark-mass plus CKM completion and is not a derivation of the coordinates from
framework primitives.

## What the narrow scope does **not** close

The audit verdict and the parent's own scope-qualifier sections
already flag these explicitly. This companion note records them in
one place for re-audit traceability:

- a retained derivation of `xi_u`, `xi_d` from framework primitives
  (the parent flags these as numerical bounded carrier coefficients);
- a physical mass-ratio match using the completed matrices' singular values;
- a perturbatively small correction interpretation: the fitted
  carriers dominate the Schur 1-3 base term, especially in the up
  sector, so this is not a small retained correction;
- a minimal-surface theorem upgrade: the Schur-NNI no-go on the
  minimal carrier remains intact;
- promotion of the row from `bounded` to `retained`.

A complementary reduced-coordinate attempt is recorded in
`QUARK_PROJECTOR_RAY_PHASE_COMPLETION_NOTE_2026-04-18.md`. That name is
non-load-bearing context and is intentionally not a citation-graph dependency
of this narrowing companion.

## What would close the open dependency (Path A future work)

Promoting the parent row from `audited_numerical_match` to a retained
theorem-grade derivation would require, per the audit verdict's
repair target:

1. a corrected mass readout that evaluates the completed matrices' singular
   values rather than their diagonal input labels;
2. an independent retained theorem fixing `xi_u` and `xi_d` from
   framework primitives, including their carrier normalization,
   readout convention, and determinant-neutral constraint;
3. an updated runner that **tests** the derived carrier point
   (rejecting if it deviates from the derived value) rather than
   **fitting** to the comparator surface;
4. an explicit retained statement of why the determinant-neutral
   1-3 carrier is the minimal admissible CP-carrier slot beyond the
   Schur-NNI base.

Until these are supplied, this row is bounded numerical CKM/J fit context with
an explicit physical-spectrum failure, not a full-quark existence result.

## Non-dependency context

- `QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md` is the historically related
  row and now carries the exact route obstruction.
- `QUARK_PROJECTOR_RAY_PHASE_COMPLETION_NOTE_2026-04-18.md` is a separate
  reduced-coordinate attempt.

Neither name is a proof authority for this companion. The bounded numerical
content is exercised directly by the historical optimizer runner, and the row
remains unaudited until the independent audit lane reviews the changed source
and runner.

## Boundaries

This companion note does **not**:

- modify the parent note's audit-ledger row;
- promote the parent's `audit_status` from `audited_numerical_match`;
- derive `xi_u` or `xi_d` from framework primitives;
- claim that the optimized diagonal labels equal physical quark masses;
- claim a small-correction interpretation of the fit;
- change the Schur-NNI minimal-surface CP no-go;
- extend the audited scope beyond what the parent already declares.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_cp_carrier_completion.py
```

Expected after the physical-spectrum firewall correction:

```text
TOTAL: PASS=11, FAIL=0
```

The runner preserves the historical optimizer and public helper API used by
the small-correction companion, but its first two completion checks now verify
the singular-spectrum mismatch instead of mislabeling diagonal parameters as
physical mass ratios. The separate exact obstruction runner is cited by the
revised parent note.

```yaml
claim_id: quark_cp_carrier_completion_audited_scope_narrow_bounded_note_2026-05-10
note_path: docs/QUARK_CP_CARRIER_COMPLETION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md
runner_path: scripts/frontier_quark_cp_carrier_completion.py
proposed_claim_type: bounded_theorem
deps: []
audit_authority: independent audit lane only
```
