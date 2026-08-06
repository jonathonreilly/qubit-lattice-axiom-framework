# Historic intake: Cycle 713 — Value Gate, No-Go Discipline Gate, and Cluster-Cap Evaluation

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_analysis
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom load-bearing; assumes the parent Dirichlet lattice construction and an isolation condition on binding energy

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Gate record for a two-condition self-bound-source criterion (converged extent AND converged well depth): across the parent note's family, unscreened and screened Poisson satisfy both, biharmonic satisfies extent but not depth, and 'local' has no single branch; biharmonic's peak potential grows linearly with the box even for a prescribed fixed-extent source on Dirichlet and on a boundary-free torus out to N=96, so the divergence is a kernel property. The response-kernel bridge the audit asked for is supplied: the converged self-consistent field matches the same operator's matched point-source kernel outside the source to within ~1% median ratio at every box.

Original verdict: N1-N8 PASS with the claim demoted at N7 from an unconditional no-go against biharmonic to a bounded theorem under a named isolation condition, and narrowed from the field to the binding energy.
Scope: Four-member operator family (not all local operators), single particle with no Pauli pressure, finite box sizes so the limit is a fit not a proof, and only inside the extended branch below the collapse coupling; the binding-energy criterion is a stated isolation condition, not a neutral measurement.
Escape conditions (negative claims): Eight routes against NG-A, seven attempted: different coupling (g=10 and g=100 both give linear depth growth), boundary condition (torus with zero mode removed, growth persists to N=96), removing self-consistency (prescribed source, same growth), different source extent, sign convention (biharmonic given an attractive well by construction), operator rescaling (ruled out by argument — absorbed into g), larger boxes (N=96, increments still constant); Route 7 — referencing the potential to a fixed radius rather than the well bottom — ATTEMPTED AND SUCCEEDS: the biharmonic potential difference across a fixed window IS bounded, so NG-A is narrowed to the binding energy and makes no claim about local field differences. The note states that under a different choice of criterion biharmonic is not excluded.

## Why pulled (supervisor decision, on the record)

Two-condition self-bound-source criterion (bounded at N7, demotion honest) AND NG-C: the landed FROZEN_STARS_RIGOROUS_NOTE's 3D size-independence is not established by its own construction — an attack on a landed row that must reach the audit lane; also load-bearing for the GW-echo note's dependency.

## Provenance (pinned)

- Original path: `docs/CYCLE713_VALUE_NO_GO_AND_CLUSTER_CAP_GATES_2026-07-27.md`
- Source commit: `7f49811a6b10985f7137e78a01a369d7c3884f8b`
- git blob: `7b6e904b18e4a392f1812250ae6124487e35cf1a`
- sha256: `7e498b0639cfbca6aeab718ffc5787d210fc316ff748910b07224ac49fc9fa3b`
- Lines: 303; runners named: scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27.py, scripts/frontier_frozen_stars_rigorous.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Negative claim NG-C states the landed frozen-stars 3D lattice-size-independence is not established by its own construction (its 3D widths 2.52-5.08 over L=6..14 still growing, within 87-95% of the free box ground state); g=100 runs fail to converge at N>=20; author concedes the N7 steelman 'largely lands' and demotes the claim in response.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
