# Historic intake: Claim Status Certificate - DM Runner Stale-Path Cleanup

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_correction
Stratum: pack_science_family
Era: may_june_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Eight DM runners had stale read('docs/X.md') calls referencing notes deliberately deleted by the 2026-04-16 trim commit d2e754fdc, producing FileNotFoundError-driven audited_conditional / audited_failed verdicts. Removing the dead reads and their dependent checks restores all eight to FAIL=0, 69 PASS / 0 FAIL total, without reverting the trim or removing load-bearing physics.

Original verdict: Audit-hygiene cleanup; allowed and forbidden PR wordings are enumerated explicitly.
Scope: Eight leaf-criticality claim rows with author-declared support or bounded status.


## Why pulled (supervisor decision, on the record)

Verification-integrity: eight DM runners carried stale read('docs/X.md') calls to notes deliberately deleted by the 2026-04-16 trim commit d2e754fdc, silently failing with FileNotFoundError; allowed and forbidden PR wordings enumerated. Companion block (eight further runners) and the two-cohort synthesis attached.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/audit-stale-path-dm-cluster-20260501/CLAIM_STATUS_CERTIFICATE.md`
- Source commit: `b06766c8d740abcfc5c627feed8368a8bbadf68b`
- git blob: `0c85d7636fb0d38cb15c506a48361d6acd35f65a`
- sha256: `ce827d7b64213b5dda6886c7f91b293fb56884be3f2c4120d3bbfda02b6d6d82`
- Lines: 74; runners named: scripts/frontier_dm_neutrino_breaking_triplet_axiom_law_attempt.py, scripts/frontier_dm_leptogenesis_projection_theorem.py, (and six more DM runners)

## Attached evidence (registered with, not as, this claim)

- `.claude/science/physics-loops/audit-stale-path-dm-cluster-20260501/CLAIM_STATUS_CERTIFICATE_BLOCK02.md` — Companion cleanup (PR #246's sibling): eight further runners split into deleted-note removal and archived-note redirects; sixteen runners total across the two blocks.
- `.claude/science/physics-loops/audit-stale-path-dm-cluster-20260501/CLAIM_STATUS_CERTIFICATE_BLOCK03.md` — Two-cohort synthesis of the 2026-05-01 audit ledger: Cohort A = 16 runner stale-path bugs addressed by the paired PRs.

## Flags carried

Eight runners were silently failing on deleted notes and their audit verdicts were noise, not physics - a systemic verification-integrity finding.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
