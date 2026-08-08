# Historic intake: Hawking Analog: Thermal Spectrum Near Propagator Horizon

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The near-horizon spectrum is NOT thermal (Gaussian R^2 = 0.007-0.71, mean 0.40, never above 0.9) while the far-field control IS quasi-thermal (R^2 0.82-0.94), and the Hawking scaling T versus kappa fits at R^2 = 0.13 with slope -9.28 - the wrong sign against a predicted +0.16; the diagnosis is that f > 1 makes S = L(1-f) negative, so the norm grows from 1.0 to 164 and the surface amplifies rather than traps.

Original verdict: FALSIFIED - the f = 1 surface is a phase-inversion boundary that amplifies outgoing modes, not an absorbing horizon.
Scope: 41^3 lattice, four mass strengths giving horizons at r_h = 2.9-6.8 and surface gravity 0.22-0.61.
Escape conditions (negative claims): Three requirements named for a genuine analog: a mechanism to absorb or trap ingoing amplitude (f = 1 freezes phase but does not attenuate), quantum fluctuations converting frozen-phase modes to outgoing radiation, and an action enforcing a one-way membrane - none present in the classical path-sum.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

HAWKING ANALOG FALSIFIED: f = 1 is a phase-inversion boundary that AMPLIFIES outgoing modes (factor 164) — the strong-field lane's central negative with three requirements named.

## Provenance (pinned)

- Original path: `docs/HAWKING_ANALOG_NOTE.md`
- Source commit: `ef9409dce218a93968f1b70c767a13512ea54d47`
- git blob: `88b4716c4b50e122f27133ca4a9f8c675c7f2029`
- sha256: `f7908ee91eff155eec4297b4917d606898f8f5d764e164d7332d3f2c2e4c8c50`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/672_HAWKING_ANALOG_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/672_HAWKING_ANALOG_NOTE.md)
- Lines: 91; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hawking_analog(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/HAWKING_3D_QUENCH_NOTE.md` — 3D quench stepping stone; own warnings intact.
- `docs/HAWKING_BOGOLIUBOV_QUENCH_NOTE.md` — 1D Bogoliubov quench; thermality collapse flagged.

## Flags carried

Reports amplitude amplification by a factor of 164 - the wavepacket gains energy crossing the high-field region, which would be a conservation problem for any downstream use of the f > 1 regime.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
