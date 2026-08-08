# Historic intake: No-Go Ledger (audit unblock block150)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_ledger
Stratum: pack_science_family
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Records that scripts/frontier_koide_lane_regression.py could not be registered as-is because a direct run EXITS NONZERO at TOTAL 395/381, with one subrunner reporting 3/6 and one expected-count entry stale.

Original verdict: Registration rejected pending a substantive Koide regression repair.
Scope: Runner registration.


## Why pulled (supervisor decision, on the record)

Verification-integrity: the Koide lane regression suite was FAILING (direct run exits nonzero at TOTAL 395/381, one subrunner broken) and registration was rejected pending substantive repair. The attached follow-up records the repaired 398/398 state AND that the registered runner is dominant-class D with ZERO asserts - audit should confirm both the repair and the assert gap.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/audit-unblock-block150-20260621/NO_GO_LEDGER.md`
- Source commit: `03baa0aed70d76959271562796f15c0c477d461d`
- git blob: `ac02b9f180a2c3ef53151aff574f0ddad558a12c`
- sha256: `7835fc4fdd3d28d7f0443347d5f9ca906479d8e415890189d51507bf946e5d07`
- Lines: 7; runners named: none

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/audit-unblock-block151-20260621/CLAIM_STATUS_CERTIFICATE.md` — The post-repair registration (koide_axiom_native_support_batch_note, regression 398/398, boundary verifier); RF: dominant class D with zero asserts.

## Flags carried

The Koide lane regression suite was FAILING (395/381 with a 3/6 subrunner) at 2026-06-21 - a live verification defect in a flagship lane.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
