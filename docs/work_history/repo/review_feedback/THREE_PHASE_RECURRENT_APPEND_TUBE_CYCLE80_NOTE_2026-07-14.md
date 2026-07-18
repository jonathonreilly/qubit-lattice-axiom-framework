# Three-Phase Recurrent Append Tube — Cycle 80

**Date:** 2026-07-14  
**Status:** constructive recurrent-core result; attachment to the physical front remains open  
**Authority:** none. This is a local compiler probe, not an axiom, primitive,
retained theorem, registry entry, or law-selection result.

Companion runner:

    scripts/three_phase_recurrent_append_tube_cycle80_2026_07_14.py

## Result up front

A finite, fixed, proper-cubic, strict-nearest-neighbour, append-only record law
can renew without copying or erasing its old apparatus.

The construction is a 17-site transverse tube. The footprint is the smallest
found serial-layer class with three same-parity, fully caged launchers. Each
layer has:

- one seed written from the preceding layer's launcher;
- fifteen further records on a Hamiltonian causal chain; and
- a different launcher written last, only after its four transverse
  neighbours and rear neighbour exist.

The seventeenth record is the launcher. It is therefore both a five-neighbour
completion record and the end of a chain that has visited every site, with
exactly one open neighbour. It writes the next layer's seed. The three layer
alphabets cycle `A -> B -> C -> A`. Three phases are load-bearing: a two-phase
version allowed an old/current parent pair to be seen in the reverse order at
the opposite phase. The third phase removes that unordered-pair identity
instead of hiding it behind a scheduler.

The recurrent law has:

    51 canonical rows
    1,170 proper-cubic raw rows
    51 recurrent roles
    0 raw input conflicts.

Each of the three inductive layer transitions was exhausted independently.
Every asynchronous schedule completes the intended 17-site layer. The only
append then exposed is the exact seed of the next phase; it appears only at
the complete-layer mask. There are no wrong appends and no output conflicts.

The same table was also run through 3, 6, 9, 12, and 15 appended layers. The
largest bounded graph contains 256 states and 256 append edges: one state per
serial append plus the one correct outside-horizon seed edge. At
every horizon the only reported outside-horizon write is the correct next
seed. Translation periodicity plus the three exact one-layer transition
graphs supplies the induction; the longer horizons are independent
cross-cycle controls.

## Why this changes the recurrence picture

Cycle 66 correctly rejected a literal `+3d` copy of the Cycle-60 apparatus.
That failure was a failure of state copying, not of local continuation.
Cycle 80 uses the permanent record corpus as an event history. It appends a
thin new causal layer and leaves old launchers fully saturated. Nothing is
reset, moved, or overwritten.

This is the useful part of the Wolfram-style rewriting analogy, with an
important difference. The present framework cannot delete or replace a
subgraph. Its safe analogue is a token-event graph: old events remain and a
locally caged frontier appends the next event layer. Causal invariance here is
tested concretely as confluence under every asynchronous append order; it is
not assumed as a slogan.

## Scoped size bound

Seventeen is minimal only in the tested serial-layer class, not among every
possible recurrent strict-NN machine. A serial layer with an odd number of
sites must start and end on the same cubic-bipartite colour. Three cyclic
phases therefore need three distinct, same-colour launcher sites. Fully
caging those launchers requires at least eight opposite-colour transverse
neighbours. A Hamiltonian path with same-colour endpoints then needs colour
counts `9:8`, hence at least seventeen sites. The displayed footprint meets
that bound. Pipelined, non-Hamiltonian, larger-period, or non-tube mechanisms
are outside this minimality statement.

## Operational encoding consequence

Cycle 75 found 83 roles in the selected finite compiler and a seven-bit
physical lower bound. The 51 Cycle-80 roles are disjoint, so the composed
bounded alphabet contains 134 roles. The serial, no-starvation recurrence
therefore forces the operational word from seven bits to eight for this
selected route. The recurrent raw domain is disjoint from the selected
Cycle-60/Cycle-67/Cycle-72 extensional law, and their 198-row union has 4,376
single-valued proper-cubic rows.

This does not yet mean the recurrence rows have been fed through physical
comparator ports. It means the extensional tables do not collide and that the
next comparator probe must be eight-bit. This is a representation cost, not
new physical or constitutional content.

## Exact remaining obligations

This result closes `ABSTRACT_APPEND_ONLY_RECURRENT_CORE`. It does not close:

1. `NEXT_FRONT_TO_TUBE_NUCLEATION`: grow one completed A layer and its rear
   cap from the actual preparation-ready physical terminal without a supplied
   scaffold.
2. `TUBE_LAYER_TO_LOGICAL_FRONT`: bind one completed three-layer period to the
   next physical q/a/b/c and B/D/H continuation, rather than merely growing a
   geometrical event tube.
3. `EIGHT_BIT_RULE_PORT_REALIZATION`: extend Cycle 75's physical comparator by
   one bit, combine directional comparisons, and write the selected eight-bit
   output word.
4. `MULTI_FRONT_CONFLUENCE`: compose two nearby recurrent tubes and test
   overlap, collision, and resource sharing.

It also does not derive occurrence weights, actuality, probability, local
rate, clock calibration, mass structure, interactions, gravity, or an exact
physical-law selector. No axiom conclusion follows from this construction by
itself.

## Constitutional reading

The recurrence gap no longer supports adding a generic formation, reading,
clock, or storage-budget sentence to the axioms. A fully local append-only
renewal mechanism exists as a theorem candidate once its physical-front
attachment is supplied. The live constitutional question remains narrower:
whether the current Admissibility wording already fixes one complete physical
continuation law and its stable identity, or whether that identity is new
physics. Cycle 80 does not decide that question.

## Verification

    python3 scripts/three_phase_recurrent_append_tube_cycle80_2026_07_14.py
