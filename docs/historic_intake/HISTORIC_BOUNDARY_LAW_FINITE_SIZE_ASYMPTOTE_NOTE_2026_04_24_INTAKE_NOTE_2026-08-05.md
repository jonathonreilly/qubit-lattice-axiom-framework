# Historic intake: Boundary-Law Gravity-Suppression Finite-Size Asymptote Note

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

The gravity suppression ratio fits r = 1 - C(G)/side to RMS residual < 2% at every G (C(5) = 2.63, C(10) = 4.21, C(20) = 6.09) and the G=0 baseline slope is nearly size-independent (0.2007 to 0.2110 across seven sides), but the unconstrained two-parameter fit does NOT asymptote to exactly 1.0.

Original verdict: A sharper finite-size characterization: the suppression is a 1/side effect whose asymptote is not certified at 1.0, and the lane stays bounded.
Scope: Sides 8-16, G in {0, 5, 10, 20}; runner 3/5 PASS with B.2 and B.3 as real falsifying findings.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Boundary-law terminal: gravity suppression is a 1/side finite-size effect (RMS<2% fits), asymptote not certified — two of its own checks failing as genuine falsifications, on the record.

## Provenance (pinned)

- Original path: `docs/BOUNDARY_LAW_FINITE_SIZE_ASYMPTOTE_NOTE_2026-04-24.md`
- Source commit: `e24f8f7827355bbcee85c2fd6ec5bab0793e3fac`
- git blob: `fbac0a084a582f4c313b67a315e359a9eb82d18b`
- sha256: `e34884459515369a1bb107ce6fa32ad28b87f7c73fd251a0d373d7db2eb00a9b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/117_BOUNDARY_LAW_FINITE_SIZE_ASYMPTOTE_NOTE_2026-04-24.md](../../archive_unlanded/historic_intake_originals/branch01/117_BOUNDARY_LAW_FINITE_SIZE_ASYMPTOTE_NOTE_2026-04-24.md)
- Lines: 177; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_boundary_law_coefficient_stability​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_boundary_law_finite_size_asymptote​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_boundary_law_robustness​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/BOUNDARY_LAW_COEFFICIENT_STABILITY_NOTE_2026-04-24.md` — Seed-stability + the universality falsification; sharpened same-date.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Two of five checks fail as genuine falsifications of the note's own stronger hypotheses.
- Supersession (as known at extraction): Sharpens the coefficient-stability note of the same date.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
