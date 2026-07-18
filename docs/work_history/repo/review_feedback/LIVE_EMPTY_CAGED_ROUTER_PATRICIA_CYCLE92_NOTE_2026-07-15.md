# Live EMPTY encoder, caged bit router, and Patricia inventory — Cycle 92

Date: 2026-07-15
Authority: none

## Question

Do the remaining physical EMPTY and serial-selector probes survive composition
with the corrected Cycle-85-selected compiler law, including inside the real
comparator/writer pipeline geometry?

## Results

They survive at the same bounded, supplied-harness grade.

The 59-record EMPTY source grows `11111111` only while the monitored physical
port is open.  Its two canonical rows add 36 disjoint raw inputs, taking the
corrected union to 5,488 single-valued inputs.  The complete asynchronous graph
still has 46 states, 73 edges, and one exact seventeen-record terminal.  All
3,850 base/rotated one-extra-neighbour controls are quiet; this includes every
one of the 153 live physical roles and a foreign control.  All 1,104 rotated
reachable states retain their exact frontier.

The old Cycle-87 gate does not survive that stronger question: despite a
single-valued raw union, its all-H rows fire 32 parasites in an actual
arity-five `R_LB` pipeline state.  Cycle 92 therefore does not reuse it.

The repaired twelve-record gate source places one already-live bridge guide in
each target cage: `T_G0` at the gate, `T_G1` at branch zero, and `T_H0` at
branch one.  These asymmetric guards retain a trivial proper-cubic stabilizer
and force every new row to contain a non-H content.  The gate's 84 raw rows are
disjoint from the prior union.  The final live compiler union has 5,572 raw
inputs and no multi-output input.  Both isolated branch graphs and all 144
proper-cubic/translated gate stages are exact.

The guard also closes the mixed-geometry leak structurally: all 15,576 stages
of the 236 equal-program pipelines and all 11,328 one-bit stopped contexts
contain only H0/H1, while every caged-gate row requires a bridge guide.  The
previously failing 66-state `R_LB` pipeline was directly re-executed with the
gate rows live and retained every exact frontier.

The corrected 236-program prefix trie has 8,239 nodes and 8,238 edges.  Its
compressed Patricia form has 471 nodes, 470 edges, 8,238 total edge-label bits,
and longest label 43 bits.  Every one of the 11,328 directed one-bit
perturbations was classified or rejected exactly; 28 happen to land on a
different valid live program.

## Boundary

The 59-record EMPTY source and twelve-record gate source are supplied.  The
three bridge-guide records must still be routed or grown into each gate cage.
The Patricia object is an exact combinatorial selector inventory, not yet a
physical embedding.  The remaining named interfaces are
`CANDIDATE_BIT_BUS_TO_ACTIVE_TRIE_NODE`, `PROPER_CUBIC_PATRICIA_EMBEDDING`, and
growth of the supplied sources from the official seed.  No seed-grown selector
is claimed.

Cycles 86 and 87 remain historical bounded routes.  No foundation edit,
registry edit, queue edit, audit verdict, or selected-law promotion follows.
No axiom addition follows from this bounded compiler port.
