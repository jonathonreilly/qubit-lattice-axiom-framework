# Historic intake: Periodic Torus Audit - Shapiro Delay Fix Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_log_like
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Fixes the single confirmed TRUE BUG: frontier_shapiro_delay.py's 1D periodic ring driver used raw math.hypot for Hamiltonian hopping weights, giving the wraparound edge weight 1/(n-1) instead of 1/1; a _min_image_hypot helper is added and _build_L/_build_H updated.

Original verdict: The periodic-torus audit NEEDS_REVIEW count is now 0 (5/5 PASS), norm = 1.000000 across all three drivers, and the active-queue item is eligible for closure pending reviewer acceptance.
Scope: One inline fix using only math and indexing.


## Why pulled (supervisor decision, on the record)

Real bug fixed in a published science runner (Shapiro-delay wraparound weight) — the periodic-torus audit closed at 0; audit work order on consumers.

## Provenance (pinned)

- Original path: `docs/PERIODIC_TORUS_AUDIT_SHAPIRO_DELAY_FIX_NOTE_2026-04-24.md`
- Source commit: `24c59e034ec99d92123a6f328333c105149c1d8b`
- git blob: `3202329b65c78fd2ad68715fd2668a91a8f6006b`
- sha256: `5e35f28f8790a70b4991840b1934a9db6c64ad4b3ec3730b0fd14830a3355f1a`
- Lines: 140; runners named: scripts/frontier_shapiro_delay.py, scripts/frontier_periodic_torus_diagnostics_audit.py

## Attached evidence (registered with, not as, this claim)

- `docs/PERIODIC_TORUS_AUDIT_BATCH_1_MANUAL_REVIEW_NOTE_2026-04-24.md` — Manual review of the 9 candidates.
- `docs/PERIODIC_TORUS_DIAGNOSTICS_CODE_AUDIT_NOTE_2026-04-24.md` — The systematic bug-recurrence scan.

## Flags carried

Documents that a published Shapiro-delay runner carried a wraparound-weight bug.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
