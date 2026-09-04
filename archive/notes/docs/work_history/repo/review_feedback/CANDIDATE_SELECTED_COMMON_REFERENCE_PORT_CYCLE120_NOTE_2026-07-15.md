# Candidate-selected common reference port — Cycle 120

Date: 2026-07-15

Authority: none

Disposition: bounded positive construction with explicit downstream residuals

Write scope: runner + review note only

Companion runner:

```text
scripts/candidate_selected_common_reference_port_cycle120_2026_07_15.py
```

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited or selected here.

## Result

Cycle 120 closes the bounded construction named by Cycle 116:

```text
CANDIDATE_SELECTED_COMMON_REFERENCE_PORT
```

The construction has all four elements needed at this resolution:

1. two distinct candidate source records, generated rather than supplied;
2. one physically formed selector whose permanent content differs between two
   lawful histories;
3. a causal route from each selector content through the corresponding source
   value; and
4. one literal common port whose final record is `H0` on the selector-zero
   history and `H1` on the selector-one history.

The two exact terminal classes are therefore:

```text
selector-zero/H0  = R_C00 at (6,1,1), H0 at (6,2,0)
selector-one/H1   = R_C01 at (6,1,1), H1 at (6,2,0).
```

Both classes use the same candidate law, the same 264-record source, the same
two generated candidate records, the same selector site, and the same output
site.  No selector, carrier, or port record is supplied.

This is a schedule-realized selector.  The local address race determines which
permanent selector content forms.  Conditional on the formed selector, every
remaining schedule exhausts to the matching value at the common port.  The
finite graph establishes availability and conditional confluence; it does not
supply an occurrence probability, fairness rule, or rate for the two selector
histories.

## Literal relational construction

Cycle 117 grows the two candidate sources inside its retained completion
surface:

```text
D0 = (5,2,1) = H1
D1 = (5,1,0) = H0.
```

The labels `D0`, `D1`, and the coordinates are audit handles.  The physical
identity of each record is its exact relational neighbourhood in the grown
apparatus.  Neither source is a member of the 264-record supplied source.

The new route uses these sites and contents:

```text
one guard             (5, 2, 2)  -> R_C20
zero pre-guard        (4,-1, 1)  -> R_C10
zero mid-guard        (5,-1, 1)  -> R_C11
zero guard            (5, 0, 1)  -> B1
selector guard        (6, 0, 1)  -> COMPLETE
guard image           (5, 0, 2)  -> COMPLETE
one address           (5, 1, 2)  -> R_C30
selector token        (5, 1, 1)  -> R_C40 or R_C41
selector relay        (6, 1, 1)  -> R_C00 or R_C01
zero carrier          (6, 1, 0)  -> B_0_2
one carrier           (6, 2, 1)  -> B_1_2
common port           (6, 2, 0)  -> H0 or H1.
```

The zero history is:

```text
zero guard lineage + COMPLETE cage
    -> selector token R_C40 before the one address can form
    -> common selector relay R_C00
R_C00 + D1=H0
    -> B_0_2
TZ + B_0_2
    -> H0 at the common port.
```

Because records are permanent, formation of `R_C40` occupies the selector
site and prevents the later one-address history from revising it.

The one history is:

```text
one guard + one address R_C30 before selector formation
    -> selector token R_C41
    -> common selector relay R_C01
R_C01 + D0=H1
    -> B_1_2
TZ + B_1_2
    -> H1 at the same common port.
```

The two selector-relay signatures differ only in the recorded branch token;
the relay site and its `COMPLETE` cage are identical.  Each carrier then
consumes both that selector content and the selected source value.  The port
decodes the resulting carrier to a literal `H` value rather than merely to a
status label.

## Why the cage is load-bearing

An unguarded mux row can alias old rail fronts because a small local signature
may recur far from the intended device.  The retained construction instead
grows a three-record zero-side lineage and a `B1`/`COMPLETE` self-cage.  In the
bare predecessor terminal, `B1` has exactly two lawful `COMPLETE` images:

```text
(6,0,1) and (5,0,2).
```

On the zero history both images form.  On the one history, the one-address
record occupies the second image site first and blocks it.  This is not a
supplied branch flag: it is the local geometric consequence of the same
address race that fixes the selector.  It also balances both complete
histories at 92 new writes above the source.

All 14 canonical mux rows are expanded through the 24 proper cubic rotations.
Their 318 distinct raw signatures are disjoint from the full Cycle-117 table.
The union is output-single-valued:

```text
new canonical rows                            14
new proper-cubic raw rows                    318
Cycle-117 raw rows                         8,312
full raw candidate-law rows                8,630
raw overlap/conflict                            0 / 0.
```

The unequal raw-orbit count is caused by rotational stabilizers, not missing
images.  Every raw row has all 24 proper-cubic images in the full table with
the same output.

## Exhaustive asynchronous graph

The companion runner uses an alternative-aware compiler because the selector,
selector relay, and common port each admit two counterfactual outputs while a
formed record still occupies its site exactly once.  It exhausts every
reachable local-subset history from Cycle 100's 264-record source:

```text
inherited generated records                    82
alternative-aware actions                      97
reachable states                          133,270
append edges                              790,154
complete terminals                              2
terminal writes                                92 / 92
maximum enabled frontier                       11
unexpected enabled sites                        0
bad or multivalued transitions                  0
provenance-order violations                     0.
```

The terminal partition is exact:

```text
(R_C00,H0) : 1 terminal
(R_C01,H1) : 1 terminal.
```

No reachable `H0` port record precedes its zero selector, zero carrier, `H0`
source, or guard lineage.  No reachable `H1` port record precedes its one
selector, one carrier, `H1` source, one address, or guard lineage.  The zero
terminal contains the second `COMPLETE` guard image and excludes the one
address.  The one terminal contains the one address and excludes that guard
image.  Both candidate sources survive unchanged in both terminals.

Both complete terminals expose only the inherited repaired-rail front.  Thus
neither branch leaves an accidental third computation available.

## Rail, late-growth, covariance, and corruption controls

Each terminal retains all 96 exact singleton repaired-rail appends.  The new
mux table has zero matches on all 97 rail-only prefixes, and its nearest
support is seven lattice steps from the tested rail.  Locality therefore gives
the exact combined product:

```text
product states                         12,927,190
product edges                          89,438,858.
```

The stronger late-growth control appends 101 complete rail slices, 1,212
additional records, to each selector terminal.  Both histories reach 1,568
total records and expose the exact next rail record.

Covariance controls check:

```text
full-law raw-row images                    207,120
rotated and translated selector terminals       48
covariance failures                              0.
```

All eight one-bit changes to the original source word and wrong `VALID` or
wrong `READY` are independently exhausted.  None reaches the common port;
all have zero bad transitions, zero unexpected fronts, and zero provenance
violations.  Their exact graph censuses are retained by the runner.  The
typed-`H0` alternate additionally exhausts to two partial terminals:

```text
states                                      88
edges                                      238
terminal sizes                             7, 8
common-port records                           0.
```

These are rejection and compatibility controls, not occurrence statistics.

## Bare-metal read chronology

This construction fixes the chronology that the earlier conceptual probes
left ambiguous:

1. both source records form and lock first as part of the Cycle-117 writer;
2. the address race forms one permanent selector record;
3. the selector and selected source jointly make one carrier available; and
4. that new carrier makes a new record available at the common port.

Reading neither forms nor finishes locking the source.  It creates a later,
distinct record whose content has exact ancestry in an already permanent
source record and an already permanent selector record.  The common port does
not revise the source, and a clock is not used to complete the lock.

The test therefore supports a local-law account of selection and copying.  It
does not support read-caused formation, later locking, a second-witness
formation rule, a clock-lock rule, or a compute/storage-budget principle.
Those remain separate candidate hypotheses and cannot be promoted by this
construction.

## Exact closure and residuals

Closed here:

```text
I3 at bounded two-candidate resolution:
two fixed generated values + one formed selector + one literal common port.
```

The bounded positive is stronger than Cycle 118's two fixed values at two
successive port cells.  It is also stronger than Cycle 114's common-reference
schedule fork because a branch-specific selector record now lies in the
causal ancestry of the final value.

Not closed here:

```text
an externally settable selector or user-address input;
arbitrary selection among all eight word positions;
arbitrary candidate values or candidate count;
repeated selection and reset semantics;
the grown 236-program association source;
selection of the final exact law L*;
an occurrence weight, probability, fairness rule, or rate;
the physical law of record formation itself.
```

The schedule race is sufficient for the existence of two lawful formed
selector histories.  It is not yet a controllable address bus.  The result
must not be advertised as RAM, general multiplexing, bank-wide compiler
selection, or a probability derivation.

## Primitive and constitutional firewall

The registered primitive scopes are consumed literally:

- scale reference supplies units conversion only;
- kinetic isotropy supplies the `c_t=c_s` form only; and
- realized-state reference supplies pointwise realized-state comparison only.

None supplies the candidates, selector, address race, carrier, common port,
readout map, schedule, occurrence weights, or a formation rule.

The 14 probe rows are candidate exact-law content under Admissibility.  Their
presence in the tested union does not select them into Nature's final law
`L*`.  Exact-law selection remains open.

The constitutional delta is zero.  Existing Admissibility permits the tested
local relational rows, and existing Record language supplies formation,
permanence, and content-only readout at the level this runner consumes.  No
axiom addition follows from a bounded positive compiler construction.  In
particular, the construction supplies no evidence that reading, a second
witness, a clock, or a resource limit is what makes a record form.

## No-go-discipline gate (N1–N8)

Status: PASS for the bounded positive; FAIL for a universal no-go, unique
minimum, final-law selection, or axiom claim.

### N1 — alternative-route enumeration

| route | marker | exact result |
|---|---|---|
| Cycle 118's inherited two-value serial path | `ATTEMPTED / POSITIVE FOR I2` | It physically consumes `H1` then `H0`, but uses different successive port sites and has no selector. |
| Bare two-row mux beside the fixed sources | `ATTEMPTED` | Old-front signatures alias; it does not retain a clean inherited computation. |
| Reuse inherited `R_A` roles as selector contents | `ATTEMPTED` | Early predecessor signatures activate before the intended source/address provenance. |
| Unguarded new `R_C` mux | `ATTEMPTED` | It reaches both values locally but aliases rail prefix 9. |
| Bulk remap to unused non-rail roles | `ATTEMPTED` | Rotation images still encounter inherited `H0` side signatures; role novelty alone is not a cage. |
| `B1`/`COMPLETE` self-caged `R_C` mux | `ATTEMPTED / POSITIVE` | The retained construction closes the bounded same-port target under every reachable append schedule. |
| Cycle 119's common `R_B00` role port | `INDEPENDENT POSITIVE` | It grows one fixed allocator role and has no value-selecting alternate selector history. |
| Full 236-program bank route | `LIVE` | It requires a grown program/reference/output association source and is not implied by the two-candidate probe. |

The positive route is sufficient for the bounded target.  No route census is
used to claim that its 14-row realization is unique or minimal.

### N2 — wall-independence audit

The former I3 wall is closed only at two fixed candidates: a formed selector
now controls one literal common port.  The remaining walls are separable:

```text
W0 bounded candidate-selected port        closed here
W1 external/multi-candidate/236 control   open downstream construction
W2 exact-law selection                    open law-selection problem
W3 occurrence weight or rate              open dynamics/probability problem.
```

Closing `W0` does not collapse `W1`–`W3`.  Conversely, failure to close any
one downstream wall does not erase the bounded positive.

### N3 — hidden-wall scan

The construction fixes the two source positions, their values, the probe-law
table, and the initial 264-record source.  The selector branch is chosen by
lawful append order.  No random scheduler, uniform measure, fairness
assumption, external address bit, hidden clock, or injected selector is used.

The chief hidden dependency is therefore visible: the local table is a probe
law, not the selected `L*`.  A second visible dependency is that the candidates
are fixed rather than arbitrary.  Neither is converted into an axiom premise.

### N4 — residual matching

The result matches Cycle 116's exact next object and Cycle 118's stated I3
residual: two candidates, a candidate/address record in output ancestry, and
one common logical port.  Cycle 119 is relevant only by analogy because its
common port records a fixed role, not a selected source value.  No broader
bank-wide or final-law residual is cited as closed.

### N5 — rhetoric audit

Here “candidate-selected” means exactly that the terminal value is a function
of the physically recorded selector content.  “Common” means the identical
lattice site `(6,2,0)` in both histories.  “Every schedule” means every state
reachable under the runner's finite append semantics.  It does not mean every
possible dynamics, external controllability, recurrence, typicality, or
probability.

### N6 — partial-closure path

This bounded positive is retained independently of whether the live routes to
eight-position selection, a 236-program association, or final-law selection
later succeed.  The immediate constructive strengthening is an externally
settable grown selector that keeps the same common-port and corruption
contracts.  A distinct lane must address recurrence or reset before repeated
read semantics are claimed.

### N7 — hostile steelman

The strongest objection is that this is a hand-designed schedule race, not an
address register controlled by a user or another grown computation.  That
objection is correct as a limit and is why external setting remains open.  It
does not defeat the narrower theorem: both selector contents are formed by
the same local law, both are causal ancestors of different values at one
physical port, and the exhaustive graph contains no third or mismatched
terminal.

A second objection is that probe-row compatibility is not evidence that
Nature chose these rows.  That is also correct.  The runner establishes an
existence construction under one exact candidate table and nothing about
`L*` selection.

### N8 — cross-cycle echo

Cycle 114's schedule fork reached two values at one reference but lacked an
address record.  Cycle 118 read two fixed values but used different output
cells.  Cycle 119 reached one common role port but lacked value selection.
Cycle 120 combines the missing bounded interfaces without inheriting the old
rail alias: the self-cage is the new repair.  The remaining external-control,
bank-wide, law-selection, and rate walls are named rather than silently
recycled as a total no-go.

## Reproduction

From the repository root:

```bash
python3 scripts/candidate_selected_common_reference_port_cycle120_2026_07_15.py
```

The retained runner exits nonzero on any source mismatch, primitive-scope
leak, table overlap, multivalued row, graph-census drift, provenance violation,
terminal mismatch, rail alias, late-growth failure, covariance failure,
corruption leak, typed-`H0` leak, scope overclaim, or missing N1–N8 disclosure.
