# Physical row-role literal fanout — Cycle 153

Date: 2026-07-15

Authority: none

Disposition: local campaign-positive representation adapter; audit unset

Companion runner:

```text
scripts/physical_row_role_literal_fanout_cycle153_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, policy, audit, commit, push,
or PR is changed.

## Result

Cycle 153 builds a local physical adapter from one row record to five literal
bits. The source is exactly one of the 32 signed-Pauli row roles used by the
Cycle-149/151/152 row machines. Five neighboring targets write the row's exact
`(x0,x1,z0,z1,phase)` values as ordinary `H0` or `H1` records. The apparatus
contains no literal input bits.

This closes the representation mismatch between the role-level row buses and
Cycle 150's literal-bit commutation circuit. It does not yet place the adapter,
commutation circuit, multiplier, and pivot router into one apparatus. Bit
transport and duplicate use remain open, especially because `P` must feed both
commutation calculations. The result is a finite role-level adapter, not a
derivation that this codebook is the selected fundamental law.

The tested five-bit fixture is terminal: all six neighbors of each output are
occupied by its source and typing parents. It proves the exact role-to-literal
map but exposes no fresh cable port. A transport-ready consumer therefore
requires a separately tested port-bearing fanout; one must not attach a cable
to the sealed Cycle-153 fixture by diagrammatic fiat.

It does not derive occurrence or equal weights. It only makes supplied row
content physically available to already-established Boolean machinery. No
axiom addition follows.

## Local construction

Five distinct pre-existing roles mark the five bit positions. The source row
is at the center; each bit target sees:

```text
one row role + one position role + four quiet frame records.
```

The construction adds:

```text
32 rows * 5 bit positions                            160 canonical rows
proper-cubic images                                  960 raw rows
Cycle-152 union                                   82,316 raw rows
combined law                                      83,276 raw rows
conflicts                                              0
```

The position roles are reused context tokens from the established alphabet;
no new role or ontology is introduced. The four equal frame parents leave a
six-orientation orbit for each canonical row.

## Causal and corruption controls

The five writes are independent after the source exists. Their exhaustive
causal graph is the five-dimensional Boolean cube:

```text
reachable states                                      32
edges                                                  80
terminal states                                         1
maximum frontier                                        5
```

All 32 source rows in all 24 proper-cubic orientations give 768 exact graphs.
Every terminal contains the five correct literal records and enables nothing
else.

Deleting the sole row source suppresses all five outputs. Deleting any one
position token suppresses exactly its associated bit while the other four
retain their complete 16-state/32-edge causal cube. The runner checks all
3,840 row/position/orientation deletion cases. Deleting any direct parent from
all 160 canonical rows gives 960 additional controls; none retains the
intended output.

The merged law is then used to replay all 54,000 Cycle-152 router graphs, all
86,640 prior mixed Clifford/measurement histories, and the Cycle-144 bound
terminal. No predecessor frontier or terminal changes.

## What this resolves—and what it does not

Before Cycle 153 the physical pieces used two representations:

```text
row transformations / multiplier / router: one of 32 row roles
commutation circuit:                         five H0/H1 records.
```

Cycle 153 gives a physical one-to-five value bridge with no duplicated row
source. It does not by itself give a composable transport port, nor solve the
geometry of transporting row bits into two commutation devices,
copying the measured row's compatible classical content for both uses, or
joining the router's case-dependent row outputs into recurrent ports.

## N1 — Alternative routes

| Route | Outcome |
|---|---|
| Supply five row bits beside every circuit | rejected as final binding |
| Encode a row as five records from the outset | live literal-only architecture |
| Decode one row role locally to five bits | positive in Cycle 153 |
| Direct role-pair commutation ROM | exact but larger role-level alternative |
| Serially expose one bit at a time | live lower-frontier alternative |
| Claim the 32-role codebook is fundamental | not licensed |

## N2 — Pairwise conditions

| Pair | Relation | Treatment |
|---|---|---|
| row role vs literal tuple | exact bijection | all 32 checked |
| five bit writes | causally independent | full Boolean cube |
| position roles | distinct semantic sockets | five established roles |
| source deletion vs index deletion | global vs one-output loss | separated controls |
| adapter vs commutation circuit | producer vs consumer | physical binding open |
| conditional update vs occurrence | independent | occurrence open |

## N3 — Hidden-condition scan

All 32 row roles, five bit positions, all H0/H1 outputs, six direct parents,
five concurrent writes, all asynchronous orders, 24 orientations, source and
index deletions, direct-parent deletions, full merged-law conflicts, prior
router histories, prior mixed histories, and bound fronts are explicit. The
source row itself remains supplied, as it must at this adapter boundary.

## N4 — Residual matching

| Evidence | Residual consumed |
|---|---|
| Cycle 149 | physical signed-row roles |
| Cycle 150 | literal-bit commutation consumer |
| Cycle 153 | physical role-to-literal adapter |

It consumes the representation mismatch. It does not consume spatial bit
transport, measured-row fanout to two consumers, atom-to-router binding,
deterministic membership, common output joining, occurrence/weight, or law
selection.

## N5 — Resolution and rhetoric

Tested: the complete finite signed two-qubit Pauli alphabet and all proper
cubic orientations. Not tested: arbitrary Pauli width, an asymptotically
compact decoder family, a combined update apparatus, or a selected universal
law. Licensed phrase: “physical row-role literal fanout,” not “symplectic
content derived from the axioms.”

## N6 — Partial-closure paths

1. Build a port-bearing row decoder and transport its outputs into the physical
   commutation circuit.
2. Reuse or copy decoded `P` bits into the second commutation circuit.
3. Bind the two output bits and multiplier row to the Cycle-152 router.
4. Add signed membership and common recurrent output ports.
5. Compare this adapter route against a literal-only row representation.

## N7 — Strongest hostile steelman

A hostile reviewer should say the adapter is a 160-row decoding table whose
meaning comes from the assigned row-role dictionary. Correct. The narrower
advance is physical and exact: the existing finite row codebook no longer
requires five host-supplied bit duplicates to drive Boolean machinery. One
permanent row record locally exposes all five bits, covariantly, under every
causal schedule, without disturbing any retained device.

## N8 — Cross-cycle echo

Cycle 148 identified the exact five-bit symplectic representation. Cycle 149
gave each tuple a physical row role. Cycle 150 implemented literal Boolean
commutation. Cycles 151–152 retained row roles for multiplication and routing.
Cycle 153 connects those strands. The next campaign step is no longer a
representation invention; it is a composition test over physical adapters,
wires, two commutation circuits, one multiplier, and the four-case router.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_row_role_literal_fanout_cycle153_2026_07_15.py
```
