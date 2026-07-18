# Live directional program and output writer — Cycle 90

Date: 2026-07-15  
Authority: none

## Question

Do the six-slot program representation and physical eight-bit output writer
remain valid against Cycle 89's corrected Cycle-85-selected law?

## Result

Yes, within the supplied-harness boundary.  The 236 live canonical rows become
236 distinct 48-bit direction-ordered programs.  The live arity census is
13/96/67/36/20/4 for arities one through six.  Exactly 742 of the 1,416 slots
are EMPTY, exactly 232 programs use at least one EMPTY slot, and the four full
rows output `I2`, `DONE`, `P2`, and `B1`.

The output writer adds 48 raw images, 24 of which safely alias identical-H1
rows.  The corrected live + binary + comparator + writer union has 5,452 raw
inputs and no output conflict.  All 256 output words traverse the exact
4,608-state writer graph.  All four full rows traverse their complete 48-bit
compare and 17-record write chains: 264 states, 260 edges, and four exact
terminals.  All 3,648 one-role substitutions stop before the output writer.
The 96 proper-cubic/translated pipeline controls are exact.

## Boundary and next probes

All streams and program rails are supplied.  This runner does not grow a
six-slot candidate from the Cycle-85 endpoint and does not select among the
236 supplied references.  The remaining named interfaces are:

- `OPEN_DIRECTION_TO_EMPTY_WORD`, tested historically in Cycle 86 and ported
  to the corrected live union in Cycle 92;
- `NEIGHBOUR_MACROBLOCKS_TO_ORDERED_STREAM`;
- `SERIAL_PROGRAM_SELECTION`, whose historical Cycle-87 gate is explicitly
  rejected in mixed geometry and replaced by a caged gate in Cycle 92;
- `SEED_TO_RULE_PORT_OUTPUT_HARNESS`.

Cycles 81, 82, 86, and 87 remain historical bounded routes.  No foundation edit,
registry edit, queue edit, audit verdict, or selected-law promotion follows.
No axiom addition follows from this bounded compiler port.
