# Cycle 716: same-code six-port admission bounded construction

Date: 2026-07-26

Authority: none

Audit: unset

Status: bounded constructive comparison

Claim type: bounded_theorem

Runner:
[`scripts/frontier_cycle716_same_code_six_port_admission_2026_07_26.py`](../scripts/frontier_cycle716_same_code_six_port_admission_2026_07_26.py)

Load-bearing dependencies:

- [`JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md`](JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md)
- [`PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md`](PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md)
- [`FINITE_PROPER_CUBIC_ADMISSION_TABLE_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-07-23.md`](FINITE_PROPER_CUBIC_ADMISSION_TABLE_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-07-23.md)

## Question

Can one shared physical-M2 code block expose all six seam-opportunity bits
incident on one M64 cell, feed them to more than one fixed local reversible
candidate law, and reach the landed finite proper-cubic admission discriminator
without a run-time truth-table ROM or a host-selected winner?

## Constructive result

Yes, for the bounded supplied block and for the `unique_quorum` candidate.  A
single canonical `3 x 3 x 3` PatchGraph+four-rail code contains the center and
its six neighbors.  The circuit uses each of the center's six logical endpoint
modes exactly once and instruments the six CAR seam transpositions with six
distinct retained pointers.  The center is not copied into six pair blocks.

Two separate compile-time gate words are executed:

- `unique_quorum`: accept exactly one opportunity;
- `odd_shells`: accept one, three, or five opportunities.

Both words copy the six-bit archive, compute the empty and collision features,
retain all admitted alternatives, retain all rejected alternatives, write the
scalar acceptance rails, and uncompute 16 feature-work bits.  The fixed words
contain no law-selector bit and no truth-table ROM.  Their supplied choice at
compile time is not derived as Nature's Admissibility.

The semantic unique-quorum output produces 64/64 well-formed landed lane-zero port
tuples and the unchanged discriminator identifies `unique_quorum` with all
four separating witnesses.  No winner convention is needed because every
admitted word has exactly one bit.

The odd-shell word is a second positive primitive candidate construction, but
its all-alternatives emission is not type-correct for the landed grammar:
26/64 words, exactly the accepted weight-three and weight-five rows, are
refused at `W-losers1`.  This is a precise representation mismatch.  It is not
a route-independent obstruction, no-go, minimum, or axiom-pressure result.

## Exact evidence

### Shared six-seam instrument

- 27 code cells, 162 matter modes, seven cells updated;
- six distinct center endpoint modes and twelve distinct total seam endpoint
  modes;
- 449 literal seam/contact basis rows: all 64 direction words plus 385 hostile
  rows;
- zero support, matter-target, pointer-truth, or scratch-cleanup failures;
- maximum phase residual `1.5895974606912448e-15`;
- maximum norm residual `1.2212453270876722e-15`;
- five dirty seam-ancilla rows refused by the declared code predicate; every
  dirty output differs from its clean comparator by `sqrt(2)` within floating
  precision.

Literal deletion controls change the target:

| deletion | changed/tested rows | maximum residual |
|---|---:|---:|
| first endpoint prewrite | 38/96 | `1.414213562373095` |
| first seam FSWAP | 60/96 | `1.9999999999999998` |
| first OR-Toffoli factor | 96/96 | `0.7653668647301795` |
| first onsite contact | 1/96 | `0.3678930670560825` |

The common free one-particle star update has residual
`3.352541507938339e-15`.  The one-particle mass is
`0.45340565417488526` versus the Cycle-230 fixture
`0.4534056541748852`, residual `5.551115123125783e-17`.  The unchanged
Cycle-230 pair reconciliation reports coin residual
`1.952777839357751e-16`, FSWAP residual zero, and 64-state contact residual
`2.149937642474629e-15`.

### Candidate words

For each candidate:

- all 64 clean basis equations pass;
- all 64 inverses return exactly;
- all 64 feature-work registers return clean;
- the coherent 64-row superposition residual is exactly zero;
- 1,536 word/frame rows have zero scalar or directional covariance failures;
- four dirty output/work rows are rejected and differ from the clean output;
- five representative gate deletions are active.

The unique-quorum word has 107 semantic gates.  The odd-shell word has 110.
The physical expansion checks `X = H S S H` to
`3.1560822113208575e-16` and the inherited H/T/CNOT Toffoli to
`7.346882794269506e-16`.

The actual expanded H/S/CNOT/T candidate subword is also executed on all 64
clean rows for each law, not only counted: it has zero equation or inverse
failures.  Its non-port registers begin clean on every row, and an executable
gate-kind scan finds no run-time table/ROM gate.  The law remains a supplied
compile-time choice between two separate words; no law-selector input wire is
present.

### Literal physical-M2 words

Both candidate laws use the same 594-qubit code, rank-432 stabilizer sector,
648 literal code M2 sites, 18 endpoint-register sites, six retained pointers,
and 45 additional candidate-register sites: 711 assigned M2 sites, with zero
placement collisions.

| candidate | primitive gates | routed gates | max route | touched M2 | route-only M2 | routed digest |
|---|---:|---:|---:|---:|---:|---|
| unique quorum | 33,712 | 1,341,906 | 104 | 14,011 | 13,300 | `6d44d067bdace91a067c4a85e59a551563240d46874bd3932235e400686922ac` |
| odd shells | 33,695 | 1,341,951 | 104 | 14,037 | 13,326 | `2666707c0c7098ccf6d7d983f08a1f791a1b7e860d1d658afc4c87c6833c6e80` |

Both routed words have zero non-nearest-neighbor, operand-order, route-return,
placement, or decoded-stabilizer failures.  The semantic directional output
relations are covariant under all 24 proper-cubic frames, and the six-direction
representation closes under all 576 ordered products.  For the routed words,
the current result is narrower: signed-permutation and translation actions
preserve their nearest-neighbor coordinate alphabet and assigned-site geometry.
The runner does not transform and re-execute the complete routed compiler in
each frame, so active physical naturality is open.

## Supplied, derived, and open

Supplied:

- the Cycle-712/713 code, gate alphabet, common coin/contact fixtures, and
  physical router;
- one prepared clean `3 x 3 x 3` code block;
- clean endpoint and candidate ancillas;
- the compile-time candidate-law choice and fixed controller order;
- route workspace;
- the landed five-table family and lane-zero grammar as a comparator.

Derived on that domain:

- six directional seam-opportunity pointers on one shared central-cell code;
- fixed local unique-quorum and odd-shell Boolean relations;
- coherent archive, admitted-alternative, rejected-alternative, collision, and
  empty outputs;
- a semantic unique-quorum stream accepted and identified by the unchanged
  discriminator, plus an exact primitive candidate-word implementation;
- proper-cubic covariance of the candidate relation, physical route-geometry
  compatibility, and preservation of the imported free/seam/contact/mass
  fixtures.

Open:

- Nature's fixed Admissibility and objective actuality;
- autonomous candidate-law selection or a genesis/enforcement theorem;
- a covariant winner-bearing grammar if multi-opportunity admitted words must
  be represented as a single-winner port;
- recurrent tiling and consistency of overlapping `3 x 3 x 3` blocks;
- one executed `E G = G_physical E` chain from the seam instrument through the
  routed candidate word into the unchanged discriminator;
- active-frame naturality of that full routed compiler;
- autonomous clean-ancilla supply;
- Record permanence, Born/history selection, source/gravity, and physical
  time.

The controller ordinal is not physical time, the contact phase is not called
energy, the acceptance rail is not actuality, and the copied output tuple is
not a framework Record.
