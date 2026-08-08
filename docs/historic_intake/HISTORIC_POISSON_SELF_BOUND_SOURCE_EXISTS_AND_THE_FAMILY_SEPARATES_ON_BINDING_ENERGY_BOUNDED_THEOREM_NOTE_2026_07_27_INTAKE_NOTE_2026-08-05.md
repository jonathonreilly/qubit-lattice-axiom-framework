# Historic intake: A self-consistent source with a box-independent extent exists, and the operator family separates on the binding energy rather than on any decay exponent

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: closed_unmerged_never_landed
Era: post_reset_2026_06_29 — no axiom load-bearing; assumes the parent runner's Dirichlet graph Laplacian and operator family (verified against committed blobs in row P0)

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

With the source sign normalized per operator so none is handed a repulsive well, a self-consistent source whose extent is set by the coupling rather than the box exists, and the parent note's four-member family separates on whether the self-consistent binding-energy has a box-independent limit: Poisson converges (extent and depth, limits 0.2957 at g=20 and 2.7945 at g=50) and screened Poisson converges (extent 0.1633, depth limit 20.7219), while biharmonic has flat extent 2.6725-2.9127 but depth running 0.7874 to 3.7835 linearly in interior sites (b = 0.1507), and 'local' has no single branch (extent jumps 0.0245 to 7.5743). R10 supplies the missing response-kernel bridge: outside the source the self-consistent Poisson field matches the same operator's point-source kernel to median ratio 1.00013 to 1.00006 across N=25..49.

Original verdict: It supplies the response-kernel bridge and the sign normalization the ledger row asks for, but does not retire the row — the headline that self-consistency FORCES Poisson requires exhaustiveness this does not have, and the second gate depends on unmerged unaudited PR #5693.
Scope: Parent note's own Dirichlet lattice and four-member family, finite lattices up to N=52 (N=96 for kernel-only rows), supplied t=1 and mu^2=0.25, and a supplied isolation condition; explicitly not shown: that no other local operator passes, that the limits exist as proved limits rather than fits, or that the separation survives a multi-particle source.
Escape conditions (negative claims): The separation rests entirely on the stated isolation condition (an isolated object's binding energy must have a box-independent limit); row R14 shows the cost — biharmonic's local field differences across a fixed window ARE perfectly box-independent (1.15613 to 1.45532, bounded fit), so under a reference-to-fixed-radius choice biharmonic is not excluded at all. The hostile reading that this smuggles in an asymptotically-free Newtonian premise is accepted and the claim is demoted to a bounded theorem under a named condition rather than an unconditional no-go. Named falsifiers per row (e.g. exhibit a coupling at which converged biharmonic depth saturates).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Box-independent self-consistent source exists under per-operator sign normalization + the response-kernel bridge the ledger row asks for; carries the F1/F2 frozen-stars 3D-width finding (second independent attack on that landed note).

## Provenance (pinned)

- Original path: `docs/POISSON_SELF_BOUND_SOURCE_EXISTS_AND_THE_FAMILY_SEPARATES_ON_BINDING_ENERGY_BOUNDED_THEOREM_NOTE_2026-07-27.md`
- Source commit: `7f49811a6b10985f7137e78a01a369d7c3884f8b`
- git blob: `d7123f1b5cb03e8402c22527d3c7e94a5cf890a9`
- sha256: `8a77a0a2afe82d24aea653ae7051f717495c95cffdb23669e1c6b6f3065eb6ec`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3091_POISSON_SELF_BOUND_SOURCE_EXISTS_AND_THE_FAMILY_SEPARATES_ON_BINDING_ENERGY_BOUNDED_THEOREM_NOTE_2026-07-27.md](../../archive_unlanded/historic_intake_originals/recovery/3091_POISSON_SELF_BOUND_SOURCE_EXISTS_AND_THE_FAMILY_SEPARATES_ON_BINDING_ENERGY_BOUNDED_THEOREM_NOTE_2026-07-27.md)
- Lines: 137; runners named: historic runner (unpinned, not in this packet): `scripts/physical_poisson_self_bound_source_exists_cycle713_2026_07_27(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_frozen_stars_rigorous(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Rows F1/F2 find the landed FROZEN_STARS_RIGOROUS_NOTE's 3D width grows monotonically 2.5214 to 5.6336 over L=6..16 with no saturation and its gravitating state is 0.866-0.945 of the free box ground state, i.e. its lattice-size independence is not established by its own construction; the note states independent audit is still required before retained-grade treatment.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
