# Historic intake: Sommerfeld Enhancement from Lattice Green's Function

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

Computes the Sommerfeld factor directly from the lattice Hamiltonian with no use of the analytic formula: 1D Numerov at N=20,000 gives 20/20 parameter points within 5% (errors 0.08% to 0.54%), converging as O(h^2) from 5.6% at N=500 to 0.07% at N=50,000; the Green's function resolvent cross-check reaches 2.4% error and 3D at L=16 shows ~30% error.

Original verdict: COMPUTED: the Sommerfeld factor is a lattice observable, closing the 'modelled' objection to its use in the DM ratio R = Omega_DM/Omega_b.
Scope: 1D chains up to N=50,000, Green's-function resolvent cross-check, and a 3D cubic lattice at L<=16 where the Bohr radius ~16 exceeds the box.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Sommerfeld computed from the lattice (20/20, no analytic formula) — closing the 'model input' objection WITH the 1D-only flag.

## Provenance (pinned)

- Original path: `docs/SOMMERFELD_LATTICE_GREENS_NOTE.md`
- Source commit: `36caf259d1430f5e589697ff433ada829fd79f46`
- git blob: `571adbf61ee215532cd3785f3c1e9b144b675d22`
- sha256: `f545827676b0363c30ee94ac0d4abca552fe224c2d1493c70d72a20cbe7a326b`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1946_SOMMERFELD_LATTICE_GREENS_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1946_SOMMERFELD_LATTICE_GREENS_NOTE.md)
- Lines: 97; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_sommerfeld_lattice_greens(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/SOMMERFELD_ANALYTIC_PROOF_NOTE.md` — Analytic Sommerfeld complement (proof-sketch step flagged).

## Flags carried

The headline 20/20 is 1D only; the 3D lattice result is ~30% off and the receipt path is an unfilled placeholder (logs/YYYY-MM-DD-...).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
