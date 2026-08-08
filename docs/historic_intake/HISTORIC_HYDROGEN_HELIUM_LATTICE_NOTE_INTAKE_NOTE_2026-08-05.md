# Historic intake: Hydrogen and Helium from Cl(3)/Z^3 Axioms

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

The lattice operator -Delta_{Z^3} - g/|r| reproduces the 1/n^2 Rydberg ratios to within 4.3% (E_2/E_1 = 0.25857, E_3/E_1 = 0.11132, E_5/E_1 = 0.03857) with an emergent Bohr radius r_0 = 2/g exactly and 13 bound states in d=3; helium Hartree gives |E(He)|/|E(He+)| = 1.342 vs 1.424 (-5.7%), improved to 1.4357 by a Jastrow VMC capturing 70% of the correlation energy; alpha_EM comes out at 0.21% via the 4-segment taste staircase.

Original verdict: Hydrogen structural predictions confirmed and helium variational bound computed; the Hartree equations are derived as stationarity conditions rather than imported, and d=3 selection is confirmed by the finite Rydberg series.
Scope: N = 20-60 lattices, g_EM = 0.5, g_nuc = 1.0; Z >= 3 unreliable because the Bohr radius 2/(Z g_EM) falls below 2 sites; absolute energies in eV blocked by the undreived electron mass.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Lattice hydrogen: Rydberg ratios to 4.3% with emergent Bohr radius, plus the correction that the earlier '27% gap' was a perturbative artifact.

## Provenance (pinned)

- Original path: `docs/HYDROGEN_HELIUM_LATTICE_NOTE.md`
- Source commit: `426fe9dd53ab0a03af34d10371bff360121b1902`
- git blob: `8dfb6c0de8465ae555f717cfd029f08ca1dfe1c0`
- sha256: `caf2c56ee105c438c554f03cc667842c7564db439e00fc41a78ed26c1e07422f`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch03/720_HYDROGEN_HELIUM_LATTICE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch03/720_HYDROGEN_HELIUM_LATTICE_NOTE.md)
- Lines: 171; runners named: historic runner (unpinned, not in this packet): `scripts/hydrogen_from_graph_dynamics(.py)`; historic runner (unpinned, not in this packet): `scripts/helium_hartree_scf(.py)`; historic runner (unpinned, not in this packet): `scripts/helium_jastrow_vmc(.py)`; historic runner (unpinned, not in this packet): `scripts/alpha_em_from_axioms(.py)`; historic runner (unpinned, not in this packet): `scripts/helium_isoelectronic_series(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

n >= 3 degeneracy counts are WARN (finite box lifts the n^2 degeneracy); H- is unbound under the product ansatz; the isoelectronic series past Z = 2 is discretization-dominated.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
