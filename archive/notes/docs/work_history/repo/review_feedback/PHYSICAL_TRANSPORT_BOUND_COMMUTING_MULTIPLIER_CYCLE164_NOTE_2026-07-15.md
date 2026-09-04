# Physical transport-bound commuting multiplier — Cycle 164

Status: parked constructive result on the single bare-metal compiler PR.

## Question

Can transported physical row records enter the retained commuting-row
multiplier and can its derived product leave through the retained row cable,
without supplying the product or adding another transition row?

This is the distinct product-generation interface left after Cycle 163 closed
selector-gated payload choice and fixed common outputs.

## Result

Yes. Cycle 164 composes the retained atoms under the unchanged 96,620-row
candidate law.

Two independent row cables terminate at the multiplier's two physical input
sites. The multiplier waits for both rows, writes their exact signed commuting
product, and that new row becomes the source of an output cable. The product
record and every downstream copy are absent initially.

The exhaustive identity census covers all 544 ordered commuting pairs of the
32 signed two-qubit Pauli rows. Every causal graph has:

```text
reachable schedule states       42
canonical schedule edges        66
terminal history classes         1
maximum frontier                 2
wrong/dead/parasitic writes       0
```

The representative apparatus also passes all 24 proper-cubic orientations.
Deleting either source suppresses exactly its input branch and prevents the
multiplier/product cable while leaving the other independent input branch
enabled.

## Candidate-law accounting

Cycle 164 adds no canonical or raw row. It uses exactly the Cycle-163 law:

```text
candidate raw rows          96,620
Cycle-164 raw-row delta           0
conflicts                         0
```

The apparatus uses the already-retained physical row roles, frame/guide
structure, commuting multiplier, and row cable. No product literal, selector
bit, case value, coordinate, orientation, or schedule is supplied.

## Bare-metal reading

The product is not a host calculation copied into the lattice. Both operands
arrive as records; their shared local neighborhood enables one product record;
that record then behaves like any other physical row and can be transported.
This is the intended bare-metal composition rule: a derived record may become
the causal source of the next retained local mechanism.

## TOE-lane consequence and exact residual

The conditional stabilizer-update chain now has positive physical mechanisms
for all distinct payload operations: row transport/forking, commuting product,
selector-gated two/three-way choice, directional convergence, and fixed common
outputs.

The remaining build is joint placement rather than a newly identified
operation: route the three physical `g1`, `g2`, and `P` sources to the two mux
modules and this multiplier; route this product cable to the fifth mux bus;
and place the mux selector sites at the two derived controller-lane outputs.
That end-to-end geometry still has to pass, so Cycle 164 does not claim the
full physical pivot is complete or that no further compiler repair can appear.

Nothing here addresses occurrence, outcome choice, weights, local time,
permanence, or fundamental-law selection. No axiom, primitive, registry,
policy, or audit edit follows.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_transport_bound_commuting_multiplier_cycle164_2026_07_15.py
```
