# Spec F3 — collision-free epoch composition on one literal site map

Runner: `scripts/frontier_cycle721_collision_free_epoch_composition_2026_07_28.py`
Cache:  `logs/runner-cache/frontier_cycle721_collision_free_epoch_composition_2026_07_28.txt`

## Claim being constructed (bounded, conditional on the Cycle-720 supplies)

On one literal site map (the Cycle-720 union boxes), the four stages

  (A) local Choi pump preparation (tree word + plaquette words),
  (B) input Bell coupling (the F1 compiled measurement words; or the F2
      Clifford word as declared alternate input leg),
  (C) retained correction-bank application (private-dual corrections
      conditioned on retained syndrome registers, as controlled words),
  (D) the recurrent matter word G_physical,

compose into a single explicitly scheduled epoch word such that:

1. GLOBAL REGISTER-LIVENESS TABLE: every physical M2 register carries an
   explicit liveness interval per schedule slot (owner stage, role:
   data/ancilla/syndrome/route-rail); the runner verifies ZERO collisions —
   no register is claimed by two stages in the same slot, and every
   cross-stage handoff (e.g. syndrome written by B, read by C) is an
   explicit ordered edge. Per the Cycle-54 caution, this is schedule-time
   state accounting, NOT static signature disjointness: the checker walks
   the composed schedule slot-by-slot and tracks register state
   (clean/live/retained-dirty) with a named failure for any premature
   write to a register whose consumer has not yet fired.
2. All stage-internal routing words retain their returned-work property
   through composition (route rails freed between stages only via explicit
   return words; census reported).
3. End-to-end algebra: on the held small boxes with exact sector matrices,
   the composed epoch equals the intended composite channel
   (prepare; couple; correct; update) exactly — residual at machine scale —
   and the composite intertwines with the coarse logical word
   (E_channel G_coarse = G_physical E_channel extended through the epoch).
   On larger boxes, tableau-level verification, exhaustive over the
   stabilizer/row families (no sampling).
4. The epoch schedule is a fixed finite table (explicit slot list in the
   cache); no runtime global queries; ordinals are circuit structure only.
5. Deletion controls: deleting one handoff edge, one correction bank entry,
   or one return word each produces a named nonzero residual / dirty
   register census. Hostile stage-interleave control produces a named
   failure.
6. Box ladder, signed covariance of the entire composed schedule
   (24 x 576 x 8; schedule keys transported), unchanged fixtures.

## Honest boundary

- The one-time epoch, clean initial banks, sector labels, root/router, and
  program content remain SUPPLIED; no renewal, multi-source composition,
  autonomous genesis, or boundary-free law is claimed (those stay in the
  Cycle-720 Open list).
- A PASS retires exactly "a collision-free composition of Choi preparation,
  Bell coupling, correction controller, and recurrent matter word on one
  literal site map" at bounded_theorem ceiling, nothing more.
- Same prose boundaries as SPEC_F1/F2.

## Dependency

Stage B consumes the F1 (primary) or F2 (alternate) compiled words via
their in-repo constructors — F3's runner may import nothing from other
runners at runtime if the campaign convention is self-containedness; in
that case it re-instantiates the constructions per the extracts and pins
byte-equality of shared construction code blocks by SHA-256 in the cache.
Decide per the extract's import-graph finding and record the choice in the
cache header.
