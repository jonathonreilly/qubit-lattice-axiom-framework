# Historic intake: The local move structure of the single cell's least-cost cuttings — Cycle 734

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — cites MINIMAL_AXIOMS_2026-06-29 with nearest-neighbour adjacency and proper cubic rotations only

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

By complete search over the one-cell four-cube, the adjacency-cost floor 144 is reached by 15800 24-piece cuttings drawing on 192 of the 400 least-cost pieces, and that floor is locally rigid: no cost-keeping move exists on two pieces (all 288 refillable pairs are flat-square re-cuts costing 1 or 2 more) or on three (of 649600 triples, 40512 admit a second refill and 0 at least cost — the cheapest alternatives cost 19/20/21 against the floor 18). The smallest cost-keeping change replaces exactly four pieces (46128 times), and every such move is the swap of the two floor cuts of one of five regions up to symmetry (families of sizes 12, 12, 24, 24, 48), an involution; connectivity by moves on up to k pieces gives groups [349, 349, 157, 61, 61, 13, 1] for k = 4..10.

Original verdict: The floor is locally rigid and globally connected — nearly a quarter of all pairs of floor cuttings share no piece while no pair differs in fewer than four.
Scope: Scoped to the single cell of one lattice step and one tick, with this adjacency cost and least volume; no statement about cells of other extent, other adjacency, other costs, or the lattice as a whole; time enters only as the fourth column and no result depends on an arrow (the tick flip is kept in the symmetry group).
Escape conditions (negative claims): The absences at two and three pieces are proved by exhaustive pair/triple examination; the absence at five is only measured by a complete census, and the note keeps the two standings apart. It does not say what the largest local re-cut away from the floor is, nor whether the four-piece flip is smallest for costs above the floor — both explicitly open. Whether the per-region binary switches can be thrown independently is not measured. The 192-piece pool and the 5 region shapes are measured by search, not derived from symmetry.

## Why pulled (supervisor decision, on the record)

Complete search: floor 144 reached by 15,800 cuttings on 192 pieces; locally rigid, globally connected — the floor's move-structure theorem.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md`
- Source commit: `b480d7684c6a9e50cd7947f3e482b238c6eeb2ad`
- git blob: `1eef4287ac8ec6c2dd2d8386d8ce8247fe8b4271`
- sha256: `b3b73b7ba07df7770ab6d2227f51a9e1da2c84d712ac013d90c7355063f67400`
- Lines: 193; runners named: scripts/physical_least_cost_cutting_flip_and_move_ladder_cycle734_2026_08_04.py (named in artifacts section)

## Attached evidence (registered with, not as, this claim)

- `docs/PHYSICAL_LOCAL_EXTREMALITY_RULE_CELL_CYCLE730_NOTE_2026-08-04.md` — Per-piece extremal localization; refines the bracket into local membership tests.

## Flags carried

Records that testing the scope of the integrality argument moved the claim: all 336 volume-2/3 sets read some corner in fractions so the whole-number proof route is special to least volume, but 0 of them reach past their own corners so the containment conclusion is not — the note claims only the narrower fact.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
