# Historic intake: GW150914 Echo Search: Blind Sweep + Harmonic Analysis

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_measurement
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

A 1000-period blind sweep of public LIGO O1 H1/L1 16 kHz strain finds its top peak at 121.6 ms (3.0 sigma) which is exactly 2.00x a 60.7 ms fundamental sitting between the non-spinning (58.1 ms) and Kerr (67.7 ms) predictions; the 60.7 ms peak has the strongest cross-detector coincidence in the scan (H1 1.166 versus L1 1.162), while the predicted 67.7 ms itself ranks only #118/1000 at 1.0 sigma.

Original verdict: CONSISTENT with the frozen-star prediction but not confirmed; the decisive next step is testing t_echo ~ M ln(M/M_Pl) scaling across multiple BBH events.
Scope: A blind autocorrelation first pass, not a detection pipeline; matched-filter analysis with injections is needed to assess false-alarm rate.


## Why pulled (supervisor decision, on the record)

The GW echo SEARCH: top peak 121.6 ms at 3.0 sigma exactly 2.00x a subharmonic, five self-listed caveats — the observational leg of the echo trilogy (prediction 3611, zeroing 416).

## Provenance (pinned)

- Original path: `docs/GW150914_ECHO_SEARCH_NOTE.md`
- Source commit: `99ef2ccb002832073a889f715d7ef060ea24bb16`
- git blob: `5a9c1acebe21b18d2ef8e560d404da2bb0f90ffa`
- sha256: `3aa90a92c1faea24cf85d7f8bae88e06df3922f8d7eeb1e10cfb25ca9c481f90`
- Lines: 153; runners named: scripts/gw150914_echo_search.py, scripts/gw150914_echo_definitive.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Lists five statistical caveats itself: the trials factor on a 3-sigma peak in 1000 trials, a global H1-L1 correlation of -0.10, no coincident peaks in the two top-5 lists, no matched filter or injections, and the 2:1 ratio possibly being coincidental. Directly at odds with the sibling gravity lane's four-mechanism 'echo amplitude = 0' conclusion.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
