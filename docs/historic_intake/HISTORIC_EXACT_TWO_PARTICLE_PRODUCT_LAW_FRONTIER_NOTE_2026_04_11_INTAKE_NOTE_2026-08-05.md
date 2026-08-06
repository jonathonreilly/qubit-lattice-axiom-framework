# Historic intake: Exact Two-Particle Product Law Frontier Note

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

The reported M1*M2 product law is not independent of the model: the interaction is hard-coded as V(x1,x2) = -G s1 s2/|x1-x2|^p, so the fitted gamma ~ 1 is a response to an encoded bilinear kernel rather than a derivation; the genuine content is only the exact-vs-Hartree divergence at strong coupling on a 1D open-boundary toy lattice.

Original verdict: Hold off main - a useful frontier control, not a mainline emergent Newton product law.
Scope: Audit of one commit and script; the model is a 1D toy, not the repo's primary staggered/open-cubic architecture, and there is no frozen/static-source control.
Escape conditions (negative claims): Three named requirements for promotion: use a source-only kernel or self-consistent field update where the mass product is not pre-encoded; add a frozen/static-source control; and replay the observable on the primary staggered/open-cubic surface (or justify the 1D lane).

## Why pulled (supervisor decision, on the record)

Circularity identification: the M1*M2 product law responds to a hard-coded bilinear kernel — promotion requirements named; integrity result.

## Provenance (pinned)

- Original path: `docs/EXACT_TWO_PARTICLE_PRODUCT_LAW_FRONTIER_NOTE_2026-04-11.md`
- Source commit: `2636abd8f737971f487693030f8d611230380048`
- git blob: `6187ba00f4e32b5f56d8e8c2895a868c639dbfe8`
- sha256: `6a699fa6d14eac6c31f1c0037d72171e8db9c25b2020df90f525217c04d5bde4`
- Lines: 73; runners named: scripts/exact_two_particle_product_law.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Identifies a circularity in a sibling lane's headline claim (the product law is built into the ansatz).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
