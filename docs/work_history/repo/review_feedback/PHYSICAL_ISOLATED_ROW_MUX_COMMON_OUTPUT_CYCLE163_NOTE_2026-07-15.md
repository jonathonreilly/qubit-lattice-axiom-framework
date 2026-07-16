# Physical isolated row mux and common output — Cycle 163

Status: parked constructive result on the single bare-metal compiler PR.

## Question

Can the two derived pivot lanes select their physical row payloads and deliver
them to one fixed output site per lane, without a host-side branch, a
case-dependent output address, a new alphabet role, or backward contamination
of the inactive branches?

Cycle 162 supplied covariant transport for all 32 physical row roles. Cycle
163 tests the next exact residual: selector-gated row copy followed by a
many-to-one common-output join.

## Result

Yes, with one important mechanism correction found by the probe.

The first join used ordinary row cable cells all the way to the common site.
It selected and wrote the right row, but the completed common row then acted as
a fresh cable source and flowed backward into every inactive terminal branch.
That is a real local-law failure, not scheduler noise.

The repaired apparatus inserts a directional terminal motif between each
symmetric cable and the common join. Its fixed local shape distinguishes the
incoming cable side from the common-output side under proper-cubic rotations.
The 32 forward and backward signatures are distinct. A row can therefore enter
the terminal from its cable, while a later row at the common output cannot
re-enter an inactive cable.

No new onsite role is introduced. The socket and terminal motifs use only the
retained frame, guide, and shared router-marker roles in different local
relations.

## Compact candidate-law delta

```text
retained Cycle-162 law                              91,244
selector-gated row-copy rows                        3,840
common-output join rows                               768
directional terminal rows                             768
combined candidate law                             96,620
raw overlaps                                            0
raw conflicts                                           0
```

The gate table has 160 canonical rows: five selector sockets times 32 row
roles. Three relational socket patterns type the two lane-one branches and
three lane-two branches without branch-private vocabulary. The join and
directional terminal tables each have 32 canonical rows.

## Exact tests

- all five selector values in all 24 proper-cubic orientations: 120 complete
  apparatus graphs;
- every possible selected physical row for every selector at identity: 160
  complete apparatus graphs;
- exact selector deletion and selected-bus deletion suppression;
- deleting an unselected bus leaves the selected first write unchanged;
- one fixed common output per lane;
- no terminal backfeed, parasitic write, dead step, or surviving enabled write;
- the Cycle-161 three-row commutator/controller apparatus remains exact under
  the 96,620-row law;
- 768 row-fork graphs, 1,024 row-pair schedule proofs, 54,000 pivot-router
  graphs, and 86,640 retained unified histories remain exact.

## Bare-metal reading

This is a small but useful lesson about what “one common output” costs at bare
metal. A symmetric information wire cannot also be a clean many-to-one latch:
once the output becomes a record, symmetry makes it eligible to drive the
unused inputs backward. The terminal motif supplies local direction through
relational structure, not through a global arrow, coordinate, clock, or
host-side instruction.

That direction is compiler content. It describes how an apparatus is built
from the retained local alphabet. It does not say when records occur, choose an
outcome, assign a probability, define time, or change permanence. No axiom,
primitive, registry, policy, or audit edit follows.

## TOE-lane consequence and exact residual

The conditional stabilizer-update lane now has reusable physical atoms for
row reading, commutation, case selection, row transport, two/three-way payload
selection, and fixed common outputs. The output-address gap is closed.

The remaining end-to-end composition is narrower: route the already physical
`g1`, `g2`, and `P` rows to these five mux buses; feed routed `g2` and `g1` to
the retained commuting-row multiplier; and route its `g2*g1` output to the
fifth bus. That is a causal placement/composition task among retained positive
atoms. Cycle 163 makes no impossibility or axiom-need claim about it.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_isolated_row_mux_common_output_cycle163_2026_07_15.py
```
