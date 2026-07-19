# Physical candidate dependency/depth-label dilation — Cycle 410

Date: 2026-07-18
Authority: none
Audit: unset

## Result

Cycle 410 extends the exact Cycle-406 coherent candidate label into a
preallocated local candidate-edge register and a reversible branchwise depth
oracle.  The oracle uses the actual Cycle-170/255 graph fixture: its named
completion `tail0` is at `(1,1,1)` with dependency depth four, and the fixed
Cycle-406 target is the adjacent site `(1,1,2)`.  When the Cycle-406
allocation-history M2 is one, a fixed local circuit writes:

- one candidate edge label from `tail0` to the target;
- one depth-label-valid bit; and
- the counterfactual child depth five in a three-bit register.

When the Cycle-406 candidate history is zero, those output registers remain
blank.  The same gate schedule runs in both cases.  There is no host branch
query, numerical threshold, outcome sampling, or state-dependent schedule.
The enlarged map has an exact inverse and satisfies

`E_410 G_410 = G_physical,410 E_410`

on the declared code space.

The output is a coherent reversible dependency/depth proposal, not an actual
edge or causal-depth member.  The actual Cycle-170/255 graph is never mutated,
no actual edge or Record is added, and actual causal depth remains four.  The
branchwise counterfactual label predicts five only for the graph that would
result if both the candidate Record and proposed parent edge were admitted.

All squared-norm quantities are sector weight, not probability or Born
weight.  Circuit layers are not time and dependency depth is dimensionless.
Dependency depth is not proper time.  No law or branch is selected.  No physical source,
stress, energy, or gravity is inferred.  No gravity or axiom pressure is
claimed.

## Fixed local oracle

The oracle represents 12 sites, one of which is the existing Cycle-406
allocation-history M2 and is not counted again.  It adds 11 M2:

- one candidate-edge bit;
- one depth-label-valid bit;
- three parent-depth bits initialized to binary four;
- three counterfactual-child-depth bits initialized blank; and
- three reversible bus bits initialized blank.

The schedule has 10 layers and 12 primitive gates.  It uses only CNOT and
Toffoli gates, every gate has at most three sites of connected
nearest-neighbor support, and no layer has a site conflict.  Together with
Cycle 406's 5,078-M2 common installation, the composed test contains 5,089
M2.  This is a bounded resource count, not a minimum claim.

The history bit first flips the edge label.  The edge flips the valid label
and fans into a three-site local bus.  Three Toffoli gates coherently copy the
actual parent-depth register into the output.  The declared parent depth is
four, binary `100`; because it is even, one further controlled CNOT flips the
least-significant output bit and gives binary `101`, or five.  The bus is then
uncomputed.  The parent-depth input, Cycle-406 state, and actual graph remain
unchanged.

Reverse gate order removes the depth-five label, valid label, and edge label,
restoring all 11 new M2 to their prepared state.  The physical operator is a
reversible label oracle, not a graph mutation.

## Actual and counterfactual graph certificates

The unmodified Cycle-255 fixture contains five permanent Records and five
nearest-neighbor dependencies.  Its two topological schedules give the same
depth profile and completion depth four.  Feeding the identical expected and
dependency maps into the Cycle-170 `dag_certificate` also returns depth four.

For validation only, Cycle 410 constructs a separate counterfactual graph
value with one new child event at `(1,1,2)` and parent `tail0`.  Cycle 255 and
Cycle 170 both return depth five for that value, with zero local-edge
failures.  This counterfactual object is used to validate the oracle's label;
it does not replace or mutate the actual graph.

The physical truth table is:

| Cycle-406 candidate history | candidate edge | valid | child-depth output |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 5 |

The parent-depth register remains four in both rows, workspace leakage is
zero, and reverse execution restores every input bit exactly.

## L5 and blind held-L6 composition

The Cycle-396 source laws, source depth three, initial column, Cycle-399
response interface, Cycle-406 payload dilation, graph fixture, edge/depth
oracle, and readout are frozen before blind held L6.  The same composed
circuit is applied at both A/C orientations.

| source route | A→C proposal-sector weight | C→A proposal-sector weight |
|---|---:|---:|
| unit-weight | `5.958479723237607e-06` | `5.958479723237605e-06` |
| coefficient-two | `3.0046754132975383e-05` | `3.004675413297537e-05` |

The proposal-sector weight equals both the exact Cycle-399 target-sector
weight and Cycle-406 candidate-label-sector weight.  L5 and blind held-L6
agree without retuning; A/C reciprocity and the unit/coefficient distinction
are preserved.  Both the Cycle-410 oracle inverse and the full Cycle-406 plus
Cycle-410 inverse have zero residual in all eight route/size/orientation
cases.  No branch is selected by this equality.

## Proper-cubic covariance

All 24 proper-cubic frames are tested.  The inherited Cycle-396 source update
has zero tested covariance residual and all 576 group products close.  All
rotated Cycle-406 and Cycle-410 gate supports remain connected
nearest-neighbor.

For every frame, the actual and counterfactual Cycle-255 graphs are rotated,
the parent/child endpoints and oracle micro-layout are rotated, and the fixed
oracle is run.  The observed proposal equals the rotated parent/child label,
the actual and counterfactual depth certificates remain four and five, all
graph edges remain local, and the inverse restores the rotated input.
Rotated graph, label, support, and inverse failures are zero.

## Identity and physical fixtures

The Cycle-410 gates act only on the candidate-history interface and 11 added
M2.  They do not modify the nested Cycle-406 key.  Therefore the complete
Cycle-364 predecessor Record and proposal payload, both Cycle-399 counter
Record identities/payloads, and every Cycle-406 candidate-register label are
preserved in every coherent branch.  The Cycle-399 Record hash remains
`2bc2b272629ef89db2910d9598e8ef523f4ac3c2d998b8bf5ff1d719c5da11e7`.

The matter-factor action is identity.  The retained fixtures are:

- Cycle-219 mass `0.4534056541748851`;
- global Q one;
- matter number `3.0 -> 3.000000000000002` within tolerance;
- zero coefficient-two and unit-weight local vector commutators; and
- 645 nontrivial Cycle-230 contact columns.

The six held matter Gram residuals remain at most `7.77e-16`; the inherited
source-factor intertwiner is `9.76e-15`; and the Cycle-406 and Cycle-410 basis
permutation residuals and oracle inverse are exactly zero.

## Deletion, leakage, and domain controls

Deleting any one of the following prevents an accepted complete proposal:

- candidate-edge latch;
- depth-valid latch;
- the high parent-depth copy;
- the successor increment; or
- the middle depth-bus link.

The nominal bus leakage is zero.  Deleting the proposed graph parent edge in
the counterfactual validation object changes the named Cycle-255 completion
depth and Cycle-170 child-output depth from five to one.  Cycle 170 still
reports global graph depth four because the original `tail0` chain remains in
that disconnected validation object.  Moving the child two sites from the
parent produces one explicit nonlocal-edge failure.  These checks show that
the proposed edge and depth-five child label are load-bearing within the
counterfactual, without adding either to the actual graph.

The declared encoder rejects a nonbinary candidate history, a parent-depth
label that disagrees with the actual graph, nonblank edge or depth outputs,
and a nonlocal child site.  The physical schedule itself is fixed and does
not inspect those values to choose gates.

## Actual-edge and causal-depth audit

The positive result is an exact reversible oracle with a deliberately narrow
codomain:

- branchwise, it labels the adjacent edge that would extend `tail0`;
- branchwise, it labels the child depth that the actual Cycle-170/255
  algorithms compute on the separately constructed counterfactual graph;
- globally, it preserves a coherent sum of blank and proposed labels;
- its inverse erases the edge/depth proposal exactly;
- the actual graph object retains its original five Records and five edges;
  and
- actual causal depth remains four.

Calling the output an actual edge would silently replace reversible
annotation with graph mutation.  Calling the ten circuit layers a duration
would violate the Cycle-255 recompilation firewall.  Cycle 410 does neither.

This is not an impossibility, minimum-content theorem, route-independent
obstruction, or axiom-pressure claim.  The N1–N8 negative-claim gate is not
triggered because no negative or minimum claim is shipped.

## Supplied, derived, and open inventory

Supplied:

- the exact Cycle-406 coherent candidate state and allocation-history M2;
- the actual Cycle-170/255 five-Record graph, named completion, depth
  algorithms, and parent depth four;
- one chosen adjacent counterfactual target and three-bit binary depth
  representation;
- 11 preallocated edge/depth/work M2 and the fixed 10-layer oracle;
- the Cycle-399/396 source/compiler stack, L5/L6 boundaries, initial column,
  and proper-cubic frames.

Derived here:

- exact reversible edge-label export, controlled parent-depth copy,
  depth-five successor label, workspace cleanup, and inverse;
- Cycle-170/Cycle-255 agreement on actual depth four and counterfactual depth
  five;
- L5/held-L6 reciprocal proposal weights, covariance, identity and fixture
  preservation, plus deletion/domain discrimination;
- the exact semantic separation between a coherent edge/depth proposal and
  actual dependency-graph extension.

Open:

- actual Cycle-364 Record formation and permanence;
- admission of one actual dependency edge and an actual depth-five member;
- law/outcome selection, autonomous predicate generation, renewal, and
  concurrency;
- normalized contextual statistics, frequency theorem, or Born law;
- metric normalization, interval/rate/proper time, physical source/stress,
  energy, or gravity interpretation.

No law or branch is selected.  No actual edge, Record, proper-time value,
probability/Born law, physical-source interpretation, gravity law, or axiom
edit is supplied.
