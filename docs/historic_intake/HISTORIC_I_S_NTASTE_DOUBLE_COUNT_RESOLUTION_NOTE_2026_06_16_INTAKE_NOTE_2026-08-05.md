# Historic intake: I_S resolved: the /N_TASTE division is a double-count bug; native I_S = 32.4

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Reconstructing the published unimproved single-link staggered scalar constant c_S = -29.3551 (Lee-Sharpe Table I) with the framework's own BZ machinery gives -29.3070 (0.16%) WITHOUT the /N_TASTE division and -14.8405 with it, proving the division is a double-count (the 16 tastes are the 16 BZ corners already inside the full-BZ integration); the corrected I_S = 32.4367, not 3.9023.

Original verdict: The prior 'settled I_S = 3.90' is wrong by the /N_TASTE factor and every row consuming integrate_I_v_scalar_full or integrate_I_SE_fermion must be re-audited; the P1 direct C_F channel moves 3.75% -> 31.20% and the Delta_1 channel 1.74% -> 56.64%.
Scope: MS-bar, mu = 1/a, tadpole u0 = <P>^(1/4) convention, single-link (unimproved) regulator whose literature band is ~29-39, not the smeared-action [4,10] band.


## Why pulled (supervisor decision, on the record)

Overturns PR #4128's settled I_S = 3.90 by reconstructing the published Lee-Sharpe constant to 0.16% — a live double-counting bug in functions consumed by landed rows; audit work order.

## Provenance (pinned)

- Original path: `docs/I_S_NTASTE_DOUBLE_COUNT_RESOLUTION_NOTE_2026-06-16.md`
- Source commit: `11a9af724b5a03693706bfacdfa07757cc04b9db`
- git blob: `3d7a50b0c7d487cf3c6b3e4a571508518e315123`
- sha256: `f48920c2af82bd046a5b5bd3fc0a0b12e2fa79a4f93d91e251aba3dc617591df`
- Lines: 77; runners named: scripts/i_s_ntaste_double_count_resolution_2026_06_16.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Documents a live double-counting bug in two integration functions plus a mis-attributed literature band whose two errors offset, making the wrong value look plausible; huge downstream corrections (1.74% -> 56.64%).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
