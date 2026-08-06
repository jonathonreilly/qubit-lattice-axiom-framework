# Historic intake: Staggered Two-Body X-Directed Flux Refinement Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Same x-directed run as idx 1982 restated as a hold: partner force 45/45 attractive, x-flux both-inward 45/45 with R^2 ~ 0.007, impulse both-inward 30/45 and 0/15 at side=18 with R^2 ~ 0.016.

Original verdict: The x-flux gate is a strong qualitative sign check but the impulse is non-convergent and the lane still lacks trajectory closure; remains a hold.
Scope: Open cubic staggered surface, sides 14/16/18, d=3..7, three placements, mass 0.30, G=50, mu2=0.001, N_steps=10, 45 rows; sourced from historical commit 9ad140f.
Escape conditions (negative claims): Escape requires a genuinely new conserved-current observable or a different graph geometry, not another shell-flux or impulse variant.

## Why pulled (supervisor decision, on the record)

The honest hold: x-flux 45/45 is a sign gate only (R^2 ~ 0.007), the impulse is non-closing — with the duplicate-reporting flag on its sibling.

## Provenance (pinned)

- Original path: `docs/STAGGERED_X_FLUX_REFINEMENT_NOTE_2026-04-11.md`
- Source commit: `19d8a91324fd072c483d416c05f036571dda7805`
- git blob: `5816007b71a5d678869ac1eac096466d3c4838c8`
- sha256: `68faf45389d3dfae22bdfb7338e46c2fee520d1b99247a226f85493ba557216a`
- Lines: 85; runners named: none

## Attached evidence (registered with, not as, this claim)

- `docs/STAGGERED_TWO_BODY_XFLUX_REFINED_NOTE.md` — The same run framed as an upgrade — flag carried.

## Flags carried

Reports the same run as idx 1982 without new computation; sourced from a historical commit rather than a rerun.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
