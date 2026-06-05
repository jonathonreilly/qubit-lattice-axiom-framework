# Signed Gravity Tensor-Source Transport Retention: Dep-Resolution Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / dep-resolution hygiene evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
parent
[`SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md`](SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md)
does not load-bear on the specific *audit grade* of its dep
[`tensor_source_map_eta_note`](TENSOR_SOURCE_MAP_ETA_NOTE.md) — only on
that dep's *structural rank-two carrier* on the restricted classes,
which the parent's own runner
[`scripts/signed_gravity_tensor_source_transport_retention.py`](../scripts/signed_gravity_tensor_source_transport_retention.py)
already re-verifies block-for-block. This is not a new theorem claim,
not a status promotion, and not an attempt to perform re-audit work.
If the audit pipeline seeds this file, it is a meta companion row;
the audit lane still sets `audit_status`, and the pipeline-derived
`effective_status` remains downstream of that authority.
**Companion target:** `signed_gravity_tensor_source_transport_retention_note`
(parent note
[`docs/SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md`](SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md)).
**Primary companion runner:**
[`scripts/audit_companion_signed_gravity_tensor_source_transport_retention_dep_resolution_2026_06_04.py`](../scripts/audit_companion_signed_gravity_tensor_source_transport_retention_dep_resolution_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_signed_gravity_tensor_source_transport_retention_dep_resolution_2026_06_04.txt`](../logs/runner-cache/audit_companion_signed_gravity_tensor_source_transport_retention_dep_resolution_2026_06_04.txt)

This is an audit-friendly meta companion: the parent's load-bearing
finite/projective transport substance is independently re-verified by
the parent's own runner on the *same* restricted gravity classes, with
no citation to any external audit grade. The companion records that
substance-vs-grade separation as machine-checkable evidence for the
audit lane; it does not re-audit the parent and does not promote
status.

---

## 0. Why this companion exists

The parent's prior audit snapshot (archived 2026-05-04) was
`audited_clean` at `claim_type=bounded_theorem`, with verdict scope
"Finite linear/projective transport of the chi_eta tensor-source twist
over the retained bounded tensor carrier, with nonlinear and physical
signed-gravity claims excluded."

That snapshot was invalidated with reason

```text
dep_weakened:tensor_source_map_eta_note:retained_bounded->unaudited
```

The dep
[`tensor_source_map_eta_note`](TENSOR_SOURCE_MAP_ETA_NOTE.md) was
downgraded from `effective_status = retained_bounded` to `unaudited`
in subsequent audit-lane activity (it cycled through
`audited_conditional` and presently sits at `unaudited`).

The honest-stop question is then exactly:

> Does the parent's substantive claim load-bear on the dep's *audit
> grade* (which was weakened) — or only on a *structural fact* (rank-2
> carrier on the audited restricted classes plus locally-constant
> orientation line) that the parent's own runner re-verifies block-for-
> block, independently of the dep's grade?

This companion records that the second reading is the one supported by
the parent's runner and note text. The parent's runner directly
imports and exercises the carrier computation on the same restricted
classes (see §3 below), and the parent's load-bearing step is an
algebraic-structural statement about a locally-constant sign local
system commuting with linear maps and normalized projective pushforwards.

This companion is therefore audit-friendly evidence that the prior
reading of the parent's substantive content survives the dep's audit
grade change. It is not a re-audit and does not promote status; it
documents the load-bearing-step dependency surface in machine-checkable
form so the audit lane can decide whether to honor or re-test the prior
treatment in light of the dep weakening.

---

## 1. Parent recap and prior audit grade

The parent
[`SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md`](SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md)
addresses the following question:

> The oriented tensor-source lift `T_g(Y) = chi_eta(Y) * T_plus`
> twists an ordinary tensor source bundle by the APS
> determinant-orientation line. The remaining question is whether the
> ordinary tensor carrier is retained and whether the twist survives
> family/refinement transport.

The parent reaches the bounded conclusion

```text
FINAL_TAG: SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_FINITE_CONDITIONAL
```

via six runner checks:

1. **Carrier retention** on the audited restricted gravity classes
   (exact local `O_h` and broader finite-rank), a rank-two, scalar-
   blind, locally-additive tensor source-to-channel map `eta`;
2. **Orientation-line family transport**: `chi_eta` commutes with
   finite family/refinement transport (`max_commute_resid <= TOL`);
3. **Projective cylindrical transport**: normalized refinement leaves
   coarse response observables invariant
   (`max_projected_field_resid <= TOL`, `max_pair_observable_err <= TOL`);
4. **Ward/Bianchi-like transport**: linear constraints transport with
   the twist (`max_transported_constraint_resid <= TOL`);
5. **Nonlinear gate**: naive `h -> -h` closure is obstructed by even
   nonlinear jets (calibrated `nonlinear_even_resid > 0`);
6. **No-claim gate**: no negative-mass / shielding / propulsion /
   reactionless-force / physical-signed-gravity claim is asserted.

The prior `audited_clean` snapshot (codex-current-fresh-context,
`auditor_confidence=high`) recorded
`load_bearing_step_class=A` and
`runner_check_breakdown={A: 5, B: 1, C: 0, D: 0, total_pass: 6}`,
with chain_closure_explanation

> Within the bounded finite/projective scope, the ordinary tensor
> carrier comes from `tensor_source_map_eta_note`, which is already
> `audited_clean` with `effective_status retained_bounded`. The
> remaining transport claim is algebraic: a locally constant sign
> local system commutes with linear maps and normalized projective
> pushforwards, while nonlinear closure is explicitly left outside the
> claim.

That explanation phrases the chain *as if* the dep's audit grade is
load-bearing. The present companion's narrow observation is that the
parent's *runner* — which is what mechanically demonstrates the
substantive claim — does not depend on the dep's grade at all (see §3).

---

## 2. Invalidation cause

The audit ledger records

```text
previous_audits[0].invalidation_reason =
    dep_weakened:tensor_source_map_eta_note:retained_bounded->unaudited
```

This invalidation moves the parent from `audited_clean` back to
`unaudited` not because of any change in the parent's runner, note
text, prose, or computed outputs, and not because of any change in the
underlying mathematical content of the dep. It is a grade-propagation
event in the audit graph: the dep's `effective_status` was downgraded,
and the dep-weakening rule re-opens the parent for fresh re-audit work.

The dep's current state on `origin/main` is

| Field | Value |
|---|---|
| `claim_type` | `bounded_theorem` |
| `intrinsic_status` | `unaudited` |
| `effective_status` | `unaudited` |
| `effective_status_reason` | `awaiting_audit` |
| `prior_snapshot` | `audited_clean` (archived 2026-05-04), then `audited_conditional` (archived 2026-05-08), then `unaudited` |

The dep has *not* been restored to `retained_bounded` on `origin/main`.
This companion therefore does *not* use the "dep restored" angle; it
uses the "parent does not load-bear on the weakened content" angle.

---

## 3. Substance-vs-grade separation

The narrow auditable observation in this companion is:

**(C1) The parent's load-bearing substantive content does not load-bear
on the *audit grade* of `tensor_source_map_eta_note`.** The parent's
runner
[`scripts/signed_gravity_tensor_source_transport_retention.py`](../scripts/signed_gravity_tensor_source_transport_retention.py)
re-verifies the rank-two carrier directly on the same restricted
classes by importing `response_matrix` and `tm` from
[`scripts/frontier_tensor_source_map_eta.py`](../scripts/frontier_tensor_source_map_eta.py)
and computing the carrier numbers itself; it does not query, cite, or
consume any audit-status field of the dep. The remaining transport
steps (orientation-line family transport, projective cylindrical
transport, Ward/Bianchi-like transport, nonlinear gate, no-claim gate)
are algebraic-structural statements about a locally-constant sign
local system and a fixed universal block operator, computed entirely
inside the parent's runner from sympy/numpy primitives.

The companion records this separation by:

1. Re-running the parent's runner on the current `origin/main` head and
   confirming all six checks pass with identical FINAL_TAG
   (Block 1 of this companion's runner);
2. Re-verifying the carrier inputs (rank, scalar-blindness, mixed
   additivity, non-scalar block structure) on both restricted classes
   directly from
   [`scripts/frontier_tensor_source_map_eta.py`](../scripts/frontier_tensor_source_map_eta.py)
   (Block 2);
3. Confirming via static source-scan that
   [`scripts/signed_gravity_tensor_source_transport_retention.py`](../scripts/signed_gravity_tensor_source_transport_retention.py)
   contains zero references to audit-status fields (`audit_status`,
   `effective_status`, `intrinsic_status`, `retained_bounded`,
   `audited_clean`, etc.) (Block 3);
4. Confirming via static source-scan that the parent note
   [`SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md`](SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md)
   contains no claim that the substantive transport conclusion depends
   on the dep's audit grade (Block 4);
5. Counterfactual confirmation: re-executing the parent's runner with
   the dep's grade conceptually treated as `unaudited` (i.e., on the
   current `origin/main` head, which is exactly that state) yields
   identical pass count and identical FINAL_TAG (Block 5);
6. Locally-constant orientation line transport check at the algebraic
   level (commute residuals, additivity errors) independent of any
   dep grade (Block 6);
7. Nonlinear gate calibration consistency (`linear_odd_resid = 0`,
   `nonlinear_even_resid = expected_even`) independent of any dep grade
   (Block 7);
8. No-claim gate preservation across the runs (Block 8).

These are static and dynamic facts about the parent's runner and note;
they do not depend on the dep's audit-lane decisions.

---

## 4. Substance-unchanged assertion

The parent's runner FINAL_TAG on the current `origin/main` head is

```text
SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_FINITE_CONDITIONAL
```

with `SUMMARY: PASS=6 FAIL=0`. This matches the FINAL_TAG recorded in
the parent note and the prior `audited_clean` snapshot's
`runner_check_breakdown` (six total passes).

The parent's note text, runner code, and runner outputs are unchanged
relative to the snapshot under which it was audited_clean. The dep's
underlying mathematical content (the rank-two `eta` carrier on the
restricted classes) is also unchanged on `origin/main`; only the dep's
audit-lane grade has moved.

The substantive bounded claim of the parent is therefore unchanged,
and the parent's runner continues to mechanically demonstrate it. The
audit lane retains exclusive authority to decide whether the prior
`audited_clean` treatment can be honored under the dep's current grade
or must be re-derived; the present companion only provides the
machine-checkable evidence above to support that decision.

---

## 5. What this companion does NOT do

This companion explicitly does **not**:

- claim a new theorem;
- promote the parent's `effective_status` or `audit_status`;
- modify the parent note text, the parent's runner, or the dep's note
  or runner;
- claim that the dep
  [`tensor_source_map_eta_note`](TENSOR_SOURCE_MAP_ETA_NOTE.md) has
  been restored to any prior grade (it has not);
- assert that the parent's bounded scope is the only correct reading;
- close the parent's open nonlinear and continuum gates (those remain
  open exactly as the parent and its sibling continuum/graded note
  state them);
- weigh in on dep-resolution policy beyond the parent / dep pair named
  here;
- back-fill or rebut any prior auditor verdict; the audit lane sets
  `audit_status` independently.

This companion's narrow auditable observation is exactly (C1) in §3.

---

## 6. Audit-lane handoff

The audit lane decides whether and how to re-audit the parent under
the dep's current `unaudited` grade. The present companion supplies:

- block-level static and dynamic evidence that the parent's substantive
  conclusion is mechanically demonstrated by the parent's own runner
  with no audit-status dependency on the dep;
- a verification that the parent's runner continues to pass at the
  current `origin/main` head with the dep at `unaudited`;
- a static source scan that confirms zero audit-status references in
  the parent's runner;
- a static source scan that confirms the parent note does not load-bear
  on the dep's audit-status grade;
- a small set of self-checks (locally-constant orientation transport,
  nonlinear-gate calibration, no-claim gate) that exercise the
  remaining substantive content of the parent independent of the
  carrier dep.

If the audit lane chooses to re-honor the prior `audited_clean`
treatment of the parent under the present dep grade, this companion
records the basis on which that decision can be made. If the audit
lane chooses to re-audit from scratch or to escalate the dep
re-audit, this companion does not block that path; it only documents
the parent's substance-vs-grade dependency surface.

This companion is `claim_type=meta`, scope `audit_companion`. It is
not a status change.
