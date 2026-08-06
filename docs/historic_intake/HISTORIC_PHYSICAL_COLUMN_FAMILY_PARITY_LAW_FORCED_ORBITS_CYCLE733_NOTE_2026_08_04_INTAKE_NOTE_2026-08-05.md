# Historic intake: Ten of the cell's eleven nearest-neighbour costs obey a parity law, and the eleventh forces which pieces a dissection may use

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — inputs are the lattice adjacency of MINIMAL_AXIOMS_2026-06-29 and nothing else

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Of the eleven non-trivial column-subset costs on the single cell (2672 pieces), ten obey a parity law with certificates found by exact elimination, and the eleventh — the full spacetime cost reading all four columns — provably does not: four pieces are exhibited covering 228 sample points exactly twice with costs summing to the odd number 25. The odd part is carried entirely by tick-coupled pairs (the full cost equals spatial cost plus corner pairs stepping in the tick and exactly one lattice direction on all 2672 pieces; dropping that term leaves the identity on only 64). The spacetime floor is 144, attained by the 24 monotone paths, with 15800 minimising dissections drawing from exactly 192 of the 400 least-cost pieces (four whole symmetry orbits, each necessary), and every one of the 379200 single-piece holes over those minimisers has a unique filler.

Original verdict: The parity law is a property of the proper subsets of the columns, and the full spacetime cost is the single member of the family that escapes it — while being the one that behaves best under minimisation.
Scope: About this single cell only, proved by exhibiting certificates for its 2672 pieces; says nothing about any other object; the ceiling of the spacetime cost is not addressed at all and the 13 exhibited values are not a spectrum claim; the surviving-piece pool is measured by complete search, not derived by any rule.
Escape conditions (negative claims): The parity failure is not a failure to find a certificate but a hard obstruction (an explicit odd-sum double cover), scoped to this cell. The note records that an earlier cycle's attempt at a parity law ACROSS objects was refuted and is not revived. Certificates were found by elimination so none is claimed minimal, and the law is stated as robust to which certificate is used.

## Why pulled (supervisor decision, on the record)

Ten of eleven column-subset costs obey a parity law by exact elimination; the eleventh carries a HARD obstruction (explicit witness) — a clean split theorem.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026-08-04.md`
- Source commit: `1f4f4c1ea7734ba89852b09e5042b4ad5bc2592a`
- git blob: `5ff655c72b45bee5f8e5dfa89b7a1d6d90af495e`
- sha256: `94656ee9fb9e53f34fc7739e76b333e340185adf273c8004e565638cc6d58480`
- Lines: 292; runners named: scripts/physical_column_family_parity_law_forced_orbits_cycle733_2026_08_04.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Notes that the two minimum principles are not the same: every spacetime minimiser also has least spatial cost, but the converse is refuted by an exhibited dissection.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
