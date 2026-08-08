# Historic intake: YT FH/LSZ Common-Window Response Provenance

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Diagnoses the fitted dE/ds instability as an artifact of the production fitter's per-source-shift fit-window selection: at 46 ready chunks the original slopes have relative stdev 0.9040 with signatures splitting into multiple tau-min classes and every high slope (dE/ds > 3) occurring only in mixed-window chunks, while recomputing all shifts on the common late window tau=10..12 gives mean 1.4256769178257236 with relative stdev 0.005504 and spread ratio 1.024. PASS=11 FAIL=0.

Original verdict: The whole ~5.9 spread ratio that dogged the chunk sweep is a fit-window selection artifact, but the common-window fit uncertainty is still not production grade and the canonical-Higgs/source-overlap gates remain open.
Scope: Provenance/support result; not a physical readout switch.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The fit-window artifact diagnosis: the ~5.9 spread ratio across ~30 checkpoints was the fitter's per-shift window selection — the campaign's central instrument correction.

## Provenance (pinned)

- Original path: `docs/YT_FH_LSZ_COMMON_WINDOW_RESPONSE_PROVENANCE_NOTE_2026-05-04.md`
- Source commit: `a455dfaf94665dcee02888de65e80923a8e0154e`
- git blob: `e3cdbd8a3eab3ba6700dede8b51711194a1ffd8c`
- sha256: `9c939db4beda289393c1cd3972cdd66874783212f0094c0c13845dab7a70f090`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2227_YT_FH_LSZ_COMMON_WINDOW_RESPONSE_PROVENANCE_NOTE_2026-05-04.md](../../archive_unlanded/historic_intake_originals/branch07/2227_YT_FH_LSZ_COMMON_WINDOW_RESPONSE_PROVENANCE_NOTE_2026-05-04.md)
- Lines: 56; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_yt_fh_lsz_common_window_response_provenance(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Shows that the source-slope outliers reported as physics-neutral across ~30 checkpoint notes were an analysis artifact of the fitter's window selection.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
