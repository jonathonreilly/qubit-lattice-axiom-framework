# Historic intake: Generation Fermi-Point Theorem Note

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

A ten-line algebraic proof: staggered Dirac zeros at the 2^d BZ corners, Wilson mass m(p) = 2 hw(p), grouping 1+3+3+1 in d = 3, so the lightest nonzero level has degeneracy C(3,1) = 3 with the three species at distinct lattice momenta hence exactly distinguishable by translation invariance - and C(d,1) = d makes d = 3 the unique dimension giving three.

Original verdict: REPLACES the Z_3 superselection approach as the primary generation argument, moving the lane from 'open with overclaiming attempts' to 'bounded with a clean honest theorem'.
Scope: Requires only that the lattice has a physical minimum spacing - explicitly much weaker than the Z_3 Hamiltonian symmetry, Berry protection, or continuum-obstruction assumptions the earlier arguments needed.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Fermi-point theorem: ten-line proof replacing superselection as the lane's primary argument — with the Hamming-to-continuum mapping honestly open.

## Provenance (pinned)

- Original path: `docs/GENERATION_FERMI_POINT_THEOREM_NOTE.md`
- Source commit: `ca26c2003ca26e1284c10f42976edd32dd9e92ea`
- git blob: `1ee94564567fe1191dae3ded39f45fa5133d2cf3`
- sha256: `7abfc168a825b6f025a37edec8fbb52da8999c9b0e9219ebfb165bb3c7cf1c09`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/618_GENERATION_FERMI_POINT_THEOREM_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/618_GENERATION_FERMI_POINT_THEOREM_NOTE.md)
- Lines: 166; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_generation_fermi_point(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/GENERATIONS_RIGOROUS_NOTE.md` — Orbit decomposition; restatements forced by 607.
- `docs/GENERATIONS_WEAKNESS_ANALYSIS_NOTE.md` — Weakness analysis forcing Z_3-not-S_3 language.
- `docs/GENERATION_NIELSEN_NINOMIYA_NOTE.md` — Poincare-Hopf upgrade of the orbit structure.

## Flags carried

Leaves open the precise mapping between its 1+3+3+1 Hamming decomposition and the orbit algebra 1+1+3+3 used elsewhere in the same lane.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
