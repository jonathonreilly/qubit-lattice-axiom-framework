# Preregistration Amendment 1: relational confirmation barrier

This amendment is committed before any Block 226 runner is written or
executed.  It resolves a semantic ambiguity between the Block-225 capacity
controller and the panel's physical candidate.

## Capacity inventory is not a selected law

Block 225 proved that all nine `U/S/A` endpoint pairs exist and that one
exchange-symmetric macro-controller can be written.  It did not derive or
select that macro-controller as physical dynamics.  Block 226 therefore
reconstructs the nine states as available capacity but does not import the
Block-225 macro transitions as a physical law.

The frozen physical candidate uses a relational barrier:

1. the first good `H-L-A` arrival remains physically present and attached to
   its original `A-A` seam; it is not replaced by a scalar absence flag;
2. two reciprocal, seam-bound clean `H-L-A` arrivals are consumed atomically
   with the first inherited merge/erode action; there is no persistent scalar
   success state;
3. a tagged `T-L-A` arrival is consumed only in the row that atomically changes
   both seam endpoints to `S-S` failure;
4. `S-S` holds every already-returned good arm as an abort-cleanup confirmation
   and remains guarded until both exact attached arms are clean;
5. asymmetric `U/S/A` pairs may encode which failure-cleanup confirmation has
   been consumed, but endpoint exchange must map every such row to its partner;
6. `LOCK/BG` remain identity-QND and are never the terminal macro-output of
   this classifier.

Thus `SS` in this physical candidate is a failed barrier, not the abstract
Block-225 success-cleanup label.  This is an explicitly preregistered new
candidate semantics, not a post-result retuning.

## Hostile terminal pair

The physical success row and abort row must have disjoint complete inputs:

```text
SUCCESS source: reciprocal A-A plus two attached clean H-L-A confirmations
ABORT source:   reciprocal A-A plus at least one attached tagged T-L-A return
```

If both can be enabled from one complete visible state, or if erasing one wake
makes their sources coincide, stop with
`scoped-tagged-echo-nonconfluent-critical-pair`.  Do not use action priority to
hide overlapping physical input projectors.

A contact on a restored clean wake is a new supplied event only if the exact
old query has no remaining dart or guard naming that site.  The runner must
derive this from its state, not assume it from elapsed time.

