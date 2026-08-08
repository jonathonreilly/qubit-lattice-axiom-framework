# Historic intake: No-go and failed-route ledger

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_correction
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Historical code invalidation: the old 5.024e-3 residual is invalidated as an endpoint-response diagnostic — central finite-difference gives relative error 3.8e-7 for the positive adjoint exponent versus 3.25e-1 for the old negative exponent (reproducible runner bug); calling the affine residual 'nonlocal' is an unsupported semantic bridge, repaired to 'affine-projection remainder'.

Original verdict: runner bug finding plus semantic repair
Scope: historical invalidation plus route-selection observations; no global no-go


## Why pulled (supervisor decision, on the record)

Historical code invalidation on the record: the old 5.024e-3 residual is INVALID as an endpoint-response diagnostic - a central-finite-difference runner bug plus semantic repair; downstream consumers of the old number must re-derive.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/yt-bridge-affine-remainder-20260711/NO_GO_LEDGER.md`
- Source commit: `901176782dc16fe598fd8a1ff31f60cb5cdd01e3`
- git blob: `b623fd1f92059082fa850c36ad65b4d6d8cd6e0a`
- sha256: `5bc6d4993e1c618ec485d449ed6b2795b6486460e892ae483aa9c7f7c1445ab5`
- Lines: 39; runners named: none

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
