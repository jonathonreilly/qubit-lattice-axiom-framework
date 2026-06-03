# RP Two-Step Discharge via C2-Tightening Companion Link

**Date:** 2026-06-03
**Type:** meta
**Claim type:** meta
**Status:** review-loop source proposal. This note adds no axiom, no theorem,
no numerical prediction, and no audit verdict. The independent audit lane sets
audit and effective status.
**Primary runner:** [`scripts/frontier_rp_two_step_discharge_via_c2_tightening_companion_link_verifier.py`](../scripts/frontier_rp_two_step_discharge_via_c2_tightening_companion_link_verifier.py)
**Cached runner output:** [`logs/runner-cache/frontier_rp_two_step_discharge_via_c2_tightening_companion_link_verifier.txt`](../logs/runner-cache/frontier_rp_two_step_discharge_via_c2_tightening_companion_link_verifier.txt)
**Authority role:** ledger-pairing note. It records that the conditional
re-audit guidance attached to the parent reflection-positivity row already has
its named finite-algebraic discharge piece on `origin/main` as a paired
companion note + runner + cache. This note creates the cross-reference for the
audit pipeline; it does not modify either source note and does not lift any
status.

## 0. Why this note exists

The parent row

```text
axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
```

is `audited_conditional` (`effective_status = audited_conditional`, terminal
audit on `origin/main`). The auditor verdict's `notes_for_re_audit_if_any`
field names a specific re-audit instruction:

```text
tighten the C2 p != 0 statement to sin(p) != 0 or separately prove the
real-spectrum exceptional modes are still non-positive.
```

A companion source note + paired runner + cache that performs exactly the
second disjunct (and which is fully consistent with the first re-wording) was
landed on `origin/main` on 2026-06-02:

```text
rp_two_step_transfer_matrix_singular_mode_c2_tightening_note_2026-06-02
```

The discharge piece is shipped but the parent text does not cite it. The
audit pipeline therefore sees two independent rows with no cross-reference and
no signal that the discharge guidance is already addressed by an on-`main`
companion.

This note records the cross-reference. It does **not** modify the parent text,
does **not** modify the companion text, and does **not** assert a status lift.
The audit lane decides whether the existing companion is sufficient as a
discharge of the conditional verdict; if it is not, no science changes.

## 1. Parent recap

```text
note_path:    docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md
ledger_id:    axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
claim_type:   bounded_theorem
audit_status: audited_conditional
effective:    audited_conditional
scope:        Free U=1 staggered-only 1+1d finite periodic lattice with m>0
              and canonical phases; fermion-sector two-step transfer
              positivity only, not the fixed-gauge or interacting closure.
```

The parent's C2 reads (verbatim, parent §C-list):

```text
C2 single-step non-positivity -- spec(T_even), spec(T_odd) are genuinely
complex for p != 0 (max |Im eig| > 1e-3), so the single-step T_hat is not a
positive operator.
```

The `p != 0` quantifier is exactly the surface the auditor identified for
either rewording or a separate finite proof of the `sin(p) = 0` exceptional
modes.

## 2. The discharge companion (on `origin/main` 2026-06-02)

```text
note_path:    docs/RP_TWO_STEP_TRANSFER_MATRIX_SINGULAR_MODE_C2_TIGHTENING_NOTE_2026-06-02.md
ledger_id:    rp_two_step_transfer_matrix_singular_mode_c2_tightening_note_2026-06-02
claim_type:   bounded_theorem
runner:       scripts/frontier_rp_two_step_transfer_matrix_singular_mode_c2_tightening_2026_06_02.py
cache:        logs/runner-cache/frontier_rp_two_step_transfer_matrix_singular_mode_c2_tightening_2026_06_02.txt
cache_exit:   0
cache_scorecard: PASS=20 FAIL=0
authority_role (verbatim from companion):
              "conditional algebraic companion to
               AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md".
```

The companion's own §1 claim is the finite singular-mode statement: at
`sin(p) = 0`, the one-step matrix `T_even(m) = [[-2m, 1], [1, 0]]` has real
eigenvalues `lambda_+(m) in (0, 1)` and `lambda_-(m) < -1`, so the one-step
operator is indefinite at the exceptional modes; the two-step square has
non-negative spectrum `{lambda_+^2, lambda_-^2}`. This is the second disjunct
of the auditor's re-audit instruction, restricted to the parent's free `U = 1`
surface.

## 3. The cross-reference claim

This meta note records the pairing:

```text
The C2 statement of the parent row
  axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
is paired, on origin/main as of 2026-06-03, with the finite singular-mode
companion
  rp_two_step_transfer_matrix_singular_mode_c2_tightening_note_2026-06-02
whose claim and paired runner address the auditor's named re-audit instruction
("tighten the C2 p != 0 statement to sin(p) != 0 or separately prove the
real-spectrum exceptional modes are still non-positive") on the parent's free
U=1 1+1d surface.
```

That is the entire cross-reference content. It is a ledger-pairing
observation. It is not a theorem, not a numerical prediction, and not an
audit verdict.

## 4. What this note does NOT do

This note does not:

- modify the parent note `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`;
- modify the companion note `RP_TWO_STEP_TRANSFER_MATRIX_SINGULAR_MODE_C2_TIGHTENING_NOTE_2026-06-02.md`;
- modify either paired runner or its cached output;
- author or predict an audit verdict on either row;
- lift the parent from `audited_conditional` to any higher status;
- promote the companion from `unaudited` to any higher status;
- assert that the companion is sufficient to discharge the conditional
  verdict -- that decision is the independent audit lane's;
- add a repo-wide axiom, primitive, or physics import;
- assert anything about the gauge-nontrivial (`U != 1`) extension or the
  many-body Grassmann/Berezin decaying-mode selection;
- assert that any downstream chain closure is reached by this pairing.

The pairing is recorded so the audit pipeline can see the companion when it
re-audits the parent. If the audit lane declines to treat the companion as a
sufficient discharge, no science changes; the parent stays
`audited_conditional` and the companion stays at whatever status the audit
lane assigns it on its own merits.

## 5. Audit-lane handoff

This is a meta-routing note. The independent audit lane is the sole authority
for:

- the parent's audit status (currently `audited_conditional`);
- the companion's audit status (currently `unaudited`);
- whether the companion is a sufficient C2 discharge for re-audit;
- any downstream chain-closure reclassification.

No outside framing or comparator is admitted by this note. The references in
this note are restricted to two on-`origin/main` source notes, their paired
runners, and their cached outputs.

## 6. Precedent

The repo already has meta-scope companion-link and routing notes such as

- [`PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md`](PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27.md);
- [`CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md`](CONVENTIONS_UNIFICATION_COMPANION_NOTE_2026-05-08.md);
- [`RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md`](RADIAN_UNIT_CONVENTION_RECLASSIFICATION_NOTE_2026-05-10_radianconv.md).

This note follows the same `claim_type = meta` pattern: language and ledger
routing, no theorem promotion.
