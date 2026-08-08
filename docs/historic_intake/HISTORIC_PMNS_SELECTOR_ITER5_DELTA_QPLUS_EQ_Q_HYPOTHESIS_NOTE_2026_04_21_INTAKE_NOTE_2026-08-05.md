# Historic intake: PMNS Selector Iter 5: delta q_+ = Q = 2/3 - Observationally Admissible at 3 sigma, Not Exact

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

High-precision re-pin gives delta_hp q_hp = 0.667711063424943 vs 2/3 = 0.666666666666667, a +1.044e-3 (0.16%) deviation that FAILS at both 1e-8 and 1e-4 and passes only at 1e-2; imposing the constraint exactly with PDG s12^2 and s13^2 as inputs predicts sin^2 theta_23 = 0.544693 (0.06% from PDG central). Runner 6 PASS, 3 FAIL.

Original verdict: delta q_+ = 2/3 is NOT an exact identity at the pinned point but is observationally admissible at 1 sigma when imposed.
Scope: Also records a correction: the iter-5 initial draft used the wrong PMNS extraction convention (descending, no row permutation) giving angles 0.454, 0.185, 0.168 before correcting to ascending plus row permutation (2,1,0).
Escape conditions (negative claims): Either the identity is exact and the 0.0003 shift in sin^2 theta_23 is a genuine prediction, or it is 2/3 plus a framework-native correction.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The honest kill: delta*q_+ = 2/3 FAILS at 1e-4 (0.16% deviation at high precision) — settles the iter-5 identity as a near-miss; the sharp-tolerance record.

## Provenance (pinned)

- Original path: `docs/PMNS_SELECTOR_ITER5_DELTA_QPLUS_EQ_Q_HYPOTHESIS_NOTE_2026-04-21.md`
- Source commit: `3e6bd338e2ec8576efe54b92d68bf4f792dce1c0`
- git blob: `eb7a64c109f3d9bd26559e73658b78e84b4fbf6f`
- sha256: `d5c37c28323e01d73d8d23937b59ac909661d258cd1e6058012462e3f1d4f052`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1588_PMNS_SELECTOR_ITER5_DELTA_QPLUS_EQ_Q_HYPOTHESIS_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch05/1588_PMNS_SELECTOR_ITER5_DELTA_QPLUS_EQ_Q_HYPOTHESIS_NOTE_2026-04-21.md)
- Lines: 185; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_pmns_selector_iter5_precision_delta_qplus_product(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/PMNS_SELECTOR_ATTACK_BACKLOG_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER10_GATE_CLOSURE_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER1_DOUBLET_AMGM_NEGATIVE_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER2_WDET_CONSTRAINED_NEGATIVE_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER3_BRANNEN_PHASE_WEAK_HINT_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER6_SECOND_CUT_DET_H_EQ_E2_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER8_VARIATIONAL_1D_CURVE_NEGATIVE_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.
- `docs/PMNS_SELECTOR_ITER9_ABCC_AND_SELECTOR_REFORMULATION_NOTE_2026-04-21.md` — Selector-iter chain member; carried by the near-miss/failure records.

## Flags carried

Explicitly records the identity FAILS at 1e-4, yet the downstream iter-10 / proposal / theorem notes present it as a retained identity; also documents a corrected extraction-convention error in its own first draft.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_strong_intermediate_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
