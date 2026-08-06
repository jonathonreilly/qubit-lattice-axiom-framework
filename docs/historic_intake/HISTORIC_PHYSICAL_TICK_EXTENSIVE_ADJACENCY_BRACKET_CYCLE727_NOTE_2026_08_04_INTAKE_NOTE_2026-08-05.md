# Historic intake: Exact adjacency-cost bracket for dissections of a two-tick box

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_theorem
Stratum: fork_pr_only
Era: post_reset_2026_06_29 — LATTICE axiom of MINIMAL_AXIOMS_2026-06-29 supplies nearest-neighbour adjacency of Z^3 and nothing else; time is not an axiom, the tick is the direction of monotone record accumulation with no adjacency of its own

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Over every minimal-volume corner dissection of one lattice cell carried through TWO ticks (24 corners, 17280 minimal pieces of volume 1 out of 42504, 48 pieces per dissection) the adjacency cost is exactly [216, 256] — exactly twice the one-tick bracket [108, 128] at both ends — with both ends carrying an exact integer certificate (denominators 2 and 288) and both attained by piece-by-piece certified witnesses. Extensivity was not a safe guess: stacking makes cost subadditive so the floor could have come in strictly below 216, nothing bounded the ceiling by 256, and 11936 of the 17280 minimal pieces straddle the tick seam.

Original verdict: The adjacency cost is extensive across a tick boundary — nothing here derives a metric, a curvature, or a field equation, only an exact combinatorial cost the geometry lane's constructions must pay.
Scope: Exact for minimal-volume corner pieces only, the same class as Cycle 725; a statement about two ticks (whether every longer run does the same is open, and the ceiling side has no subadditivity argument at all); the spatial block is still a single lattice cell.
Escape conditions (negative claims): The adjacency charge weights spatial pairs and ignores tick separation, which the note attributes to the axiom's own asymmetry rather than a modelling choice — and identifies as the reason the answer can be extensive (the tick adds pieces without adding chargeable pairs). A framework later giving the tick its own weight would be asking a different question, and the newly introduced tick-span charge is named as where such a weight would go. Certificate denominators 2 and 288 are not claimed minimal.

## Why pulled (supervisor decision, on the record)

Adjacency cost is exactly extensive across a tick boundary (complete enumeration, 17,280 pieces); the two-tick bracket.

## Provenance (pinned)

- Original path: `docs/PHYSICAL_TICK_EXTENSIVE_ADJACENCY_BRACKET_CYCLE727_NOTE_2026-08-04.md`
- Source commit: `6b45fe0b1bf2694fe83b39ebbad5d912c46ae733`
- git blob: `ac24d4cbb54f53de5d11f2527bd29dd4a26c7a88`
- sha256: `92b0962e77832b19e39bc15138f46991c3d965ea2c8190de2cf80356fd9ceb84`
- Lines: 210; runners named: scripts/physical_tick_extensive_adjacency_bracket_cycle727_2026_08_04.py

## Attached evidence (registered with, not as, this claim)

- `docs/PHYSICAL_FACET_CHARGE_TICK_MIXED_SPLIT_CYCLE726_NOTE_2026-08-04.md` — Facet-charge additivity/superadditivity at the ceiling; extensivity-adjacent evidence.

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
