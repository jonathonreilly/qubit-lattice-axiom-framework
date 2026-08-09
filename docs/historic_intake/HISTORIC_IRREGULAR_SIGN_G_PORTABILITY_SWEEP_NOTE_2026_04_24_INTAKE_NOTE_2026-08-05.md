# Historic intake: Irregular Off-Lattice Sign Lane — G-Portability Sweep Note

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

Over 150 rows the sign separator is fully G-portable at mu^2 = 0.1 (15/15 on all three observables at every G in {1,3,5,10,20}, medians +3.2e-2 to +6.4e-3) but REFUTED at mu^2 = 0.001, where pass rates go non-monotonic [1.00, 0.67, 1.00, 0.87, 0.33] and the median ball1 margin flips sign at G = 20 (-1.11e-7).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Portability established at mu^2 = 0.1 and REFUTED at 0.001 — explicitly retracts a prior gate's 93.3% strength; the sign lane's calibrated truth.

## Provenance (pinned)

- Original path: `docs/IRREGULAR_SIGN_G_PORTABILITY_SWEEP_NOTE_2026-04-24.md`
- Source commit: `b56c08d63577150b21539d9ae1282603cf880e0a`
- git blob: `a558cc9cc89e27402183be558315a9316b8a0bbe`
- sha256: `906511aeefaeddf9597da347aa4b08afca18cc1a56e0acb31797100335312c37`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/739_IRREGULAR_SIGN_G_PORTABILITY_SWEEP_NOTE_2026-04-24.md](../../archive_unlanded/historic_intake_originals/branch03/739_IRREGULAR_SIGN_G_PORTABILITY_SWEEP_NOTE_2026-04-24.md)
- Lines: 166; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_irregular_sign_g_portability_sweep​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_irregular_sign_core_packet_gate​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/IRREGULAR_SIGN_FAMILY_PORTABILITY_SWEEP_NOTE_2026-04-24.md` — Fourth-family portability; observable-dependent.
- `docs/IRREGULAR_SIGN_LOW_SCREENING_GATE_NOTE.md` — Gate diagnosis: packet-shape-dependent failure.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): 3/6 PASS — portability established at mu^2 = 0.1 across G in [1,20] and refuted at mu^2 = 0.001, where margins sit 4-7 orders of magnitude below the mu^2 = 0.1 peak and are sign-of-noise.
- Extraction scope (triage compression; may reflect later context): Three graph families x 5 seeds per cell; packet, observable, window and constructors identical to the original core-packet gate, only G swept.
- Extraction escape conditions (negative claims; triage compression): The low-screening refutation is tied to the centered core-packet observable; a different sigma or packet shape giving uniform pass at mu^2 = 0.001 would isolate the failure to the observable rather than the underlying sign physics, and the note suggests low screening may be a separate near-massless regime warranting a different observable.
- Extraction red flags: Explicitly retracts the strength of a prior gate result; host library versions differ from pinned.
- Supersession (as known at extraction): Downgrades the 2026-04-11 core-packet gate's 93.3% pass at mu^2 = 0.001 to a marginal weak-noise positive bias that does not survive a wider G sweep; predecessor to the family-portability sweep of the same date.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
