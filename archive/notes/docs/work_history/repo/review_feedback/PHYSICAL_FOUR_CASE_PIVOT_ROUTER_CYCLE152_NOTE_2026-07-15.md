# Physical four-case pivot router — Cycle 152

Date: 2026-07-15

Authority: none

Disposition: local campaign-positive controller result; audit unset

Companion runner:

```text
scripts/physical_four_case_pivot_router_cycle152_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, policy, audit, commit, push,
or PR is changed.

## Result

Cycle 152 builds a physical four-case pivot router for the two-generator
stabilizer update exposed in Cycles 148–151. Given supplied commutation bits
`c1,c2`, the supplied rows `g1,g2,P`, and a supplied product row `g2*g1`, the
local record law selects and writes the correct pair:

```text
c1=c2=0: g1, g2
c1=1,c2=0: P,  g2
c1=0,c2=1: g1, P
c1=c2=1: P,  g2*g1
```

Every write is an ordinary local record enabled by its immediate neighbors.
There is no host-side branch inside a causal graph. One case record enables
two lane selectors; each selector enables exactly its selected physical row
copy. The two lanes may occur in either order.

This closes the local four-case routing atom, not the full measurement-update
machine. The commutation bits and product row are supplied at this interface;
Cycles 150–151 establish their physical atoms separately, but they are not yet
causally wired into this router. Its two rows also finish at case-dependent
output sites rather than a common recurrent interface. Deterministic
membership remains open in the commuting case: the machine does not yet tell
whether signed `P` is present, absent, or present with the opposite sign.

The result does not derive occurrence or equal weights. It routes a supplied
outcome's conditional update. No axiom addition follows.

## Compact physical law

The controller adds:

```text
case rows                                                4
lane-selector rows                                       8
selected row-copy rows                                 192
canonical rows total                                   204
proper-cubic raw rows                                4,896
Cycle-151 union rows                                77,420
combined rows                                        82,316
raw conflicts                                            0
```

The 192 row-copy contexts arise from all selected case/lane contexts over the
32 signed Pauli row roles. Identical contexts quotient automatically. The
compact embedding places some branch sockets beside case-input records, so
their actual local signatures include those already-present neighbors. This is
a layout dependency, not extra pivot content.

One shared, pre-existing marker role types every branch socket. The same role
is used throughout; no branch receives a private vocabulary item. Across all
1,024 combinations of a selected branch, row role, and wrong selector, no
wrong selector enables a write.

## Exhaustive causal controls

At identity, the runner checks all six generator bases of every stabilizer
state, all fifteen Pauli measurements, and both supplied outcome signs:

```text
60 states * 6 bases * 15 measurements * 2 signs      10,800
```

It then checks the canonical basis of every state in all 24 proper-cubic
orientations:

```text
24 rotations * 60 states * 15 measurements * 2 signs 43,200
combined causal graphs                                54,000
```

Every graph has exactly ten reachable states, thirteen edges, one terminal,
and maximum frontier two. All four commutation cases occur. The two lane
writes commute causally, while each selected row waits for its own lane token.
There are no wrong writes, dead nonterminals, or surviving enabled writes at
the terminal.

Deleting any direct parent from every canonical router row suppresses the
intended output. Adding the router rows preserves all 86,640 prior mixed
Clifford/measurement histories and preserves the Cycle-144 terminal's two
priced fronts.

## What the pass means structurally

The first compact layout attempt was under-typed: an unselected branch socket
could alias an older five-parent row. A shared marker removed that alias, but
the first test signature described each branch in isolation and omitted marker
and case-input records physically adjacent in the combined apparatus. Once
the signature described the actual neighborhood, all 54,000 graphs passed.

That is a physical-embedding repair inside the intended structure. The
scientific decomposition did not change:

```text
g1,g2,P
   -> physical commutation and commuting product
   -> four-case local controller
   -> two updated row records.
```

Had closure required branch-private roles or word-by-word exceptions, it would
have counted against this structure. It did not: one shared socket type and
the actual local neighbors suffice.

## N1 — Alternative routes

| Route | Outcome |
|---|---|
| Keep the expanded 1,800 update rows | exact predecessor implementation |
| Host-side four-case branch | rejected as final physical interface |
| One local case record and two selector lanes | positive in Cycle 152 |
| Give each branch a private marker role | unnecessary |
| Ignore adjacent apparatus records | falsified by the first layout test |
| Add a spatial isolation hop before fan-out | live modular-layout alternative |
| Literal-bit row multiplier and controller | live deeper compression |

## N2 — Pairwise conditions

| Pair | Relation | Treatment |
|---|---|---|
| `c1` vs `c2` | jointly select one of four cases | physical case row |
| first vs second lane | causally independent after case | both orders tested |
| selected vs unselected sockets | mutually exclusive | wrong-selector controls |
| router vs commutation atom | consumer vs supplied input | causal binding open |
| router vs product atom | consumer vs supplied input | causal binding open |
| conditional update vs occurrence | independent | occurrence open |

## N3 — Hidden-condition scan

All four bit cases, six bases per state, fifteen measurements, both signs,
thirty-two row roles, five branch sockets, actual adjacent case records, one
shared marker role, every proper-cubic orientation, every causal ordering,
parent deletions, wrong selectors, prior mixed devices, and bound fronts are
explicit. Product and commutation values are supplied rather than generated in
this apparatus; that condition is named rather than hidden.

## N4 — Residual matching

| Evidence | Residual consumed |
|---|---|
| Cycle 150 | physical commutation atoms exist |
| Cycle 151 | physical commuting product atom exists |
| Cycle 152 | physical four-case selection and routing |

Cycle 152 consumes controller selection and branch routing. It does not
consume atom-to-router wiring, deterministic signed membership, common output
joining, recurrent reuse, literal multiplier compression, occurrence/weight,
or law selection.

## N5 — Resolution and rhetoric

Tested: the complete finite two-qubit stabilizer domain and full proper-cubic
covariance. Not tested: arbitrary Pauli count, arbitrary tableau width, a
fully bound physical measurement machine, or a selected fundamental compact
law. Licensed phrase: “physical four-case pivot router,” not “measurement
update derived from the axioms.”

## N6 — Partial-closure paths

1. Bind the physical commutation outputs and product output into this case
   controller without supplied duplicates.
2. Classify signed membership in `{g1,g2,g1*g2}` for the commuting case.
3. Join case-dependent output sites into two common recurrent row ports.
4. Compare the compact role-level route with a literal-bit multiplier route.
5. Preserve all mixed histories after each composition.

## N7 — Strongest hostile steelman

A hostile reviewer should say that Cycle 152 routes already-computed answers:
the two bits and product are supplied, the output ports move with the case, and
the role alphabet still acts as a finite codebook. Correct. The narrower
advance is that the 1,800-entry update table is no longer needed to choose
updated rows: one finite covariant controller implements the exact four-case
pivot over every state, basis, measurement, sign, orientation, and causal
ordering without branch-private vocabulary.

## N8 — Cross-cycle echo

Cycle 147 supplied an expanded executable target. Cycle 148 exposed its exact
symplectic structure. Cycles 149–151 made row transformations, Boolean
commutation, and commuting multiplication physical. Cycle 152 adds the
controller that chooses the correct row sources. This is still the campaign's
intended bridge from a finite truth table toward reusable local machinery. The
next test is composition: whether the separately physical atoms form one
recurrent device without supplied intermediate answers.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_four_case_pivot_router_cycle152_2026_07_15.py
```
