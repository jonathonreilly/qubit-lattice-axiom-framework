# Historic intake: Sphaleron Rate Coefficient and Magnetic Mass from Framework SU(2)

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

Derives two previously imported baryogenesis coefficients from the framework's own SU(2): kappa_sph = 21.3 +/- 3.8 versus imported 20 (0.3 sigma) via Chern-Simons diffusion, and c_mag = 0.369 +/- 0.029 versus imported 0.37 (0.0 sigma) from a 3D SU(2) plaquette-correlator screening mass at L=16, beta=8.

Original verdict: Two imports eliminated: the baryogenesis chain now has zero remaining physics imports beyond the declared boundary condition T_CMB = 2.7255 K.
Scope: 3D SU(2) Monte Carlo at L=12 and L=16, beta=8, with g = 0.653 fixed from the lattice action at g_bare = 1.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Two baryogenesis imports 'derived' — reproducing the external values they replace (0.3 sigma / exact) — pulled WITH the reproduction flag for audit.

## Provenance (pinned)

- Original path: `docs/SPHALERON_MAGNETIC_DERIVED_NOTE.md`
- Source commit: `ef06ee99afd7309695d0d2799dd1927cac3e0f13`
- git blob: `7800a7f1ec1f41b22632e3b22b8db024a5972ac5`
- sha256: `78c2ad7a5958fb0f7a6a6769606c7c0c1da0931cc14b5c82c92ae698e8aba472`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1958_SPHALERON_MAGNETIC_DERIVED_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1958_SPHALERON_MAGNETIC_DERIVED_NOTE.md)
- Lines: 90; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sphaleron_magnetic_derived(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

The 'derivation' reproduces the external values it replaces to within error bars and relies on the Moore-Rummukainen lattice measurement K_ASY = 10.8 +/- 0.7, so the independence from external input is arguable.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
