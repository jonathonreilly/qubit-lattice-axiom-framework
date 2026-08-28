# Preregistration Amendment 1: clean-wake / tagged-wake discriminator

This amendment is committed before any Block 225 runner is written or
executed.  It narrows the first Stage-A test without changing the carrier,
seam automaton, contact quotient, or decision boundaries.

## Exact untagged control

The frozen Block-224 single-wave prose lets both a quiet root acknowledgement
and a prior-contact rollback return as `L_c`.  If either return erases its wake
before the seam consumes it, there are histories with the same complete
seam-local cylinder

```text
A--A + two bound L arrivals + clean restored wake
```

but incompatible obligations: the quiet history must enter success cleanup
and the contact history must enter abort cleanup.  The primary must construct
the shortest such pair and classify the untagged/two-pass realization as a
visible-state alias.  It may not use query history to separate the rows.

This is a negative control on that realization only, not on the nine-state
seam controller or on distributed higher-block memory.

## Frozen live repair

The first candidate repair is a provenance-preserving domino:

- a good root acknowledgement reaches its endpoint as an exact `L` arrival
  with a clean `P/R--L` wake;
- a contact/abort return reaches its endpoint as an exact `L` arrival while a
  labelled `T--L` wake remains attached;
- the `T` retains the load-bearing return-child dart and the `L` retains the
  matching parent-side incidence supplied by the visible neighbor pattern;
- the seam atomically latches the appropriate `S/A/U` pair state before the
  final tagged wake is erased;
- two exact good confirmations are consumed atomically by the nine-state seam
  controller; absence of a tag is never inferred merely from delay.

The good and abort source cylinders must remain disjoint under endpoint
exchange, every proper-cubic transport, complement, width-two parallel ports,
and every tested Y neighbor-retention context.  A scalar endpoint-only Kraus
row is forbidden; the complete directional wake is part of the source
projector.

## First-stop rules

Stop the repair at the first one of:

1. a width-two `T_0--L` and `T_2--L` wake collapses to the same source;
2. moving or consuming the domino erases one labelled dart;
3. a Y cleanup requires the center to store a third dart after its neighbor
   mark has vanished;
4. good and abort wakes share one complete visible source but require
   different seam outputs;
5. two hostile service orders leave different surviving marks or outcomes.

If the primary executes only the finite seam and distributed-capacity model,
the strongest authorized positive class remains
`positive-record-qnd-seam-controller-open-distributed-compiler`.  Full local
dynamics, CP completeness, fair liveness, Record writing, and TOE movement
remain open until separately executed.

