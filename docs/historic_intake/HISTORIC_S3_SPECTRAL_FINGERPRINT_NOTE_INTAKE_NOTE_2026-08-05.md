# Historic intake: S^3 Spectral Fingerprint Test — Honest Quantitative Audit

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

The periodic cubic lattice spectrum matches T^3, not S^3: T^3 wins the ratio RMSE at every size L = 4..20 (S^3 RMSE 0.561 to 0.762), zero out of 12 degeneracy levels match S^3 across L = 8..30, and the spectrum converges to continuum T^3 as O(1/L^2) (max relative error 3.7e-3 at L=30).

Original verdict: The lattice spectrum confirms T^3 as it must; this is orthogonal to the S^3 axiom-chain derivation and neither confirms nor refutes it.
Scope: Graph Laplacian on periodic cubic lattices L = 4..30 and open-BC balls; exact analytic eigenvalue formula used for the degeneracy test.
Escape conditions (negative claims): The negative is scoped to periodic/open cubic lattices; testing S^3 spectrally would require directly discretizing S^3 (icosahedral or hypercube-based), named as a separate project.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The lattice-spectrum fact: periodic cubic spectrum matches T^3 not S^3 at every size — WITH its own 'ALL TESTS PASS' framing flag; scopes the numerics honestly.

## Provenance (pinned)

- Original path: `docs/S3_SPECTRAL_FINGERPRINT_NOTE.md`
- Source commit: `ccab562ebde768c686cd884f8c8429266485f466`
- git blob: `e1a488f9bf352c5459406074f6c0a9490ca96524`
- sha256: `adc98a5230047538ebfecdee7eb3787e14346b958b1be7d7789114c560cf0969`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1875_S3_SPECTRAL_FINGERPRINT_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1875_S3_SPECTRAL_FINGERPRINT_NOTE.md)
- Lines: 136; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_s3_spectral_fingerprint(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Status line reads 'ALL TESTS PASS' for a test whose finding is that the lattice does not match S^3; the reconciliation is that the lattice test was never a test of the claim.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
