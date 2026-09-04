# Physical three-row spacious isolated pivot — Cycle 161

Date: 2026-07-15

Authority: none

Disposition: retained-grade bounded compiler/composition result; audit unset;
parked in the single draft campaign PR after the full runner passed

Companion runner:

```text
scripts/physical_three_row_spacious_isolated_pivot_cycle161_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, policy, or audit surface is
changed. Cycle 161 adds no transition row. It composes the unchanged Cycle-160
89,708-row candidate law, including the eight canonical case-role isolation
rows already priced there.

## Result

Three physical five-bit row records now drive the isolated four-case pivot
controller end to end. The apparatus does not receive literal product values,
commutation selectors, or a case label. It receives only `g1`, `g2`, and the
measured row `P` as row roles.

The causal chain is:

```text
g1 row -> four derived bits ---------\
                                          four ANDs -> three XORs -> c1
P row  -> four bits -> first fork ---/

g2 row -> four derived bits ---------\
                                          four ANDs -> three XORs -> c2
P row  -> the same four bits -> fork-/

c1,c2 -> one case record -> two isolated case cables -> two lane selectors
```

The bit pairing is the symplectic pairing, not ordinary coordinate order:

```text
generator bits  (0, 2, 1, 3)
measured bits   (2, 0, 3, 1)
```

Thus the two selector records are exactly `symplectic(g1,P)` and
`symplectic(g2,P)`. They enter the retained case table and cause exactly the
two retained row-choice selectors required by the tableau pivot case.

## Physical composition

Twenty nearest-neighbor paths share one guide/frame assignment:

```text
generator-to-commutator paths                         8
measured-fork-to-commutator paths                     8
selector-to-case paths                                2
case-to-isolated-lane paths                           2
total path occurrences                           14,368
unique path sites                                14,367
intended shared path site                             1
```

The single repeated path site is the case record itself, which is the source
of the two case-role isolation cables. No differently valued paths overlap.
The measured row first forms the already-proved two-port fork endpoints; the
long transports begin at those endpoints. The four lower continuations turn
outward in two axis-separated layers so their mandatory guide corners do not
conflict.

A representative apparatus has:

```text
initial finite guide/frame harness              201,035 records
derived records                                  16,889
successive deterministic states                  16,890
exact frontier edges                            120,355
longest causal chain                              2,749
dependency indegree counts      12 zero, 16,862 one, 15 two
```

All 16,889 dependency nodes close under a topological sort. H0 and H1 are
absent initially. The initial value content is exactly one `g1` row role, one
`g2` row role, and one measured-row role; every literal, product, XOR result,
case role, and lane selector is derived.

The 201,035-record harness is a compiled finite laboratory. It is not claimed
to grow autonomously, and its size is not claimed to be minimal.

## Exact values, schedules, and covariance

All four pivot cases pass as complete physical replays:

```text
(c1,c2) = (0,0), (0,1), (1,0), (1,1)
```

Every case has 16,890 states, 120,355 frontier edges, 201,035 initial records,
16,889 derived records, and no terminal write. The selected remote lane roles
are exactly the retained `LANE_OUTPUT` values.

The representative mixed case passes in all 24 proper-cubic orientations.
State count, initial count, derived count, selectors, case, lane roles, and
terminal closure are invariant. Two replay bookkeeping values vary with the
coordinate order chosen by the lexicographic scheduler. The accumulated
frontier-edge count ranges from 88,860 to 175,507, and the maximum simultaneous
frontier is:

```text
maximum 12   15 orientations
maximum 13    1 orientation
maximum 16    8 orientations
```

That variation is scheduling, not content. A separate factorized proof checks
33,806 realizable local history states, including every intended target and
every adjacent outside site that can change as records append. It finds no
wrong, early, dead, or parasitic write.

The case controller's physical domain requires commuting generator pairs. The
five-bit alphabet contains 544 ordered commuting `(g1,g2)` pairs, hence 17,408
valid ordered `(g1,g2,P)` triples. Their exact selector/case distribution is:

```text
(0,0)  5,888
(0,1)  3,840
(1,0)  3,840
(1,1)  3,840
```

For every valid triple the case returned by the retained pivot map is exactly
the pair of symplectic selectors.

## Causal controls

The initial enabled frontier is exactly the twelve row-bit writes. Deleting
either generator row suppresses exactly its four writes and leaves the other
generator plus the measured reader live. Deleting the measured row suppresses
exactly its four writes and leaves both generator readers live.

Each measured bit has exactly two first-generation children, one in each
two-port branch. Selector sites, case input sites, the case role, and both
remote lane selectors are absent initially. The dependency graph therefore
records reuse of one measured fact rather than two supplied copies.

## TOE-lane bridge

| Retained piece | Cycle 161 use |
|---|---|
| Cycles 154–159 | row readers, literal cables, and one measured row with two physical uses |
| Cycle 160 | output-ported AND/XOR commutators and isolated case-role cables |
| Cycle 152 | case table, lane table, row-copy table, and tableau pivot semantics |
| Cycle 151 | physical multiplication of commuting row roles |

Cycle 159's selector-to-router gate is closed. Cycle 160's supplied-product
boundary is closed. The remaining compiler interface is now narrower and is
not a negative physics result: bring the physical `g1`, `g2`, `P`, and
`g2*g1` row roles to the retained Cycle-152 copy branches, let the two lane
selectors choose the updated rows, and converge the two possible branch
locations on one recurrent row output.

The retained `COPY_TABLE` and physical commuting-row multiplier are concrete
closure routes. Therefore Cycle 161 does not claim that the remaining
interface is impossible, requires a new primitive, or requires an axiom. The
No-Go Discipline checklist explicitly rejects such a claim as premature.

## Scope

Cycle 161 does not derive occurrence or equal weights, autonomous guide/frame
growth, compact-law selection, a time rate, global permanence, or the exact
fundamental Admissibility rule. It does not complete the payload-row copy or
common-output interface. No axiom addition follows from this compiler result.

## No-Go Discipline

The companion checklist is:

```text
docs/work_history/repo/review_feedback/PHYSICAL_THREE_ROW_SPACIOUS_ISOLATED_PIVOT_CYCLE161_NO_GO_CHECKLIST_2026-07-15.md
```

Its result is `FAIL` for any no-go claim about the remaining payload/common-
output interface: multiple retained constructive routes remain unattempted.
The required demotion is applied here. Cycle 161 ships only the positive
partial closure above and queues the strongest retained route as the next
campaign target.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_three_row_spacious_isolated_pivot_cycle161_2026_07_15.py
```
