# Bare-metal literal egress and finite bind — Cycle 190

Date: 2026-07-16

Status: bounded positive; retained typed egress reaches a generated,
value-neutral all-five status tree and ordered five-literal consumer.

## Authority and predecessor freeze

Cycle 190 takes the shortest live route named by the Cycle-183 obstruction:
leave recurrent endpoint support with the retained typed `H0/H1` cable before
splitting the literal.

```text
Cycle-183 predecessor commit  63b96566526c3f4749f630cd5c6ec6a2b0c40b7a
Cycle-183 runner hash         84f86a4fca065970d7030bff21e3b94c72556af4c21915de155093049d4a9402
Cycle-183 note hash           cde386e605505f2e932e862efeb1328377524eb56a1cc5ccb4deebdcfdf1a72a
```

No foundation, axiom, primitive, registry, queue, policy, audit, predecessor,
push, or PR surface is changed.

## Construction

The five generated Cycle-180 endpoints are:

```text
(-26,  3, -1)
(-26, 15, -1)
(-26, 27, -1)
(-26, 39, -1)
(-26, 51, -1)
```

For each lane, the retained typed cable runs in the `-x` direction through
`x=-45`. Its open terminal port is then generated as the same literal:

```text
terminal bits
(-46,  3, -1)
(-46, 15, -1)
(-46, 27, -1)
(-46, 39, -1)
(-46, 51, -1)
```

That generated bit, not the recurrent endpoint, is the common source of two
retained cable branches:

1. a short typed branch terminates into one value-neutral `MEMBER5` leaf;
2. a long typed branch preserves `H0/H1` to one ordered consumer port.

The five status leaves join first at:

```text
J01       (-56,  9, 0)
J23       (-56, 33, 0)
J0123     (-66, 21, 0)
JFINAL    (-76, 40, 0)
```

Only `J01` and `J23` are first cross-bit ancestry sites. `JFINAL` has ancestry
`{0,1,2,3,4}`. Its value-neutral status bus gates five ordered consumer
records:

```text
(-89,  3, -30)
(-89, 15, -30)
(-89, 27, -30)
(-89, 39, -30)
(-89, 51, -30)
```

The consumer values are exactly the ordered input literals. No site carries a
five-bit word or a 32-valued payload.

## Exact price

The retained cable contributes all 96 of its proper-cubic raw rows literally;
all 96 are already present in the Cycle-178 common law. Cycle 190 adds exactly
two fresh onsite roles:

```text
EGRESS_CAP       supplied inert structural discriminator
MEMBER5          generated value-neutral finite-membership status
```

`MEMBER5` is never supplied. The compiled local-law price is:

```text
compiled canonical rows                         16
  recurrent egress adapters                       4
  terminal H0/H1 egress                           2
  H0/H1 -> MEMBER5 conversion                     2
  value-neutral status tree                       6
  ordered H0/H1 consumer                          2
proper-cubic raw rows                            342
merged full-law rows                         102,338
raw-law conflicts                                  0
base-row overlaps                                  0

supplied apparatus records                     3,016
  retained MARK frames                         2,517
  retained P0 cable guides                       465
  EGRESS_CAP                                      34

generated extension records                      768
  retained typed cable records                   465
  generated terminal bits                          5
  value-neutral status records                   293
  terminal consumer records                        5
```

The cap role has no payload semantics. It distinguishes interfaces that would
otherwise be proper-cubic aliases:

- two caps at each compact recurrent endpoint close the Cycle-183 inherited
  `H0` and self-copy seam;
- one cap identifies each generated terminal bit and each `H -> MEMBER5`
  conversion;
- guarded multi-parent joins cannot fire from either parent alone; and
- two consumer caps prevent a literal-only consumer premise from
  impersonating the `H -> MEMBER5` conversion.

## Exact execution result

All 32 five-bit words pass one exact carrier-to-egress-to-tree-to-consumer
history under the merged local law:

```text
states per history                           2,289
direct causal edges                          4,232
minimum-order maximum frontier                  18
maximum-order maximum frontier                  16
adjacent unordered dynamic pairs                 0
declared recurrent exits                         10
failed words                                      0
```

Both causal replays close on exactly the declared recurrent exits. Dynamic
edge signature deletion is exact, and observed ancestry equals the intended
ancestry for every extension record in all 32 words.

The endpoint controls are:

```text
local endpoint -> first-stem edge deletions     160 / 160
complete-boundary endpoint absences             160 / 160
total                                            320 / 320
```

When one recurrent endpoint is absent, exactly those extension records whose
ancestry does not contain that lane remain reachable. `JFINAL` and all five
consumers remain absent.

## Proper-cubic covariance and inherited schedule wall

On a completed recurrent boundary, the new 768-record egress construction
passes all 24 proper-cubic orientations:

```text
states                                             769
direct causal edges                                772
adjacent unordered pairs                             0
orientation failures                                 0

min/max frontier profile
  (10, 6)                                            4
  ( 6, 6)                                           16
  ( 6,10)                                            4
```

The differing frontier widths are coordinate-order profiles; state count,
edge count, outputs, ancestry, terminal closure, and local law are identical.

Cycle-178 did not claim arbitrary rotated-coordinate schedule confluence. Its
unchanged full recurrent history has this exact 24-orientation profile before
Cycle-190 egress is attached:

```text
pass                                                 7
early inherited T_H0 discovery alias                 9
inherited maximum-replay alias                        8
```

The same profile occurs when the completed Cycle-190 apparatus is asked to
re-run the predecessor under those rotated lexicographic schedules. This note
therefore makes the narrower claim actually tested: the new egress is fully
proper-cubic covariant on the retained completed-boundary contract, while the
predecessor's stronger arbitrary-schedule theorem remains unclaimed. Cycle
190 does not silently widen into a repair of Cycle 178.

## Reusable coordinate and map contract

The runner exports the following read-only surfaces for downstream probes:

```text
ENDPOINTS                 five recurrent source ports
TERMINAL_BITS             five generated H0/H1 fork sources
STATUS_CABLE_PATHS        five retained literal-to-status branches
LITERAL_CABLE_PATHS       five retained literal-to-consumer branches
STATUS_PORTS              five generated MEMBER5 leaves
BIT_PARENTS               five terminal literal parents
CONSUMER_SITES            five ordered terminal outputs
SCAFFOLD                  supplied apparatus map
extension_expected(word)  generated extension map
apparatus(word)           full initial/expected/exit contract
NEW_RAW                   exact Cycle-190 proper-cubic law delta
FULL_RAW                  retained law plus Cycle-190 delta
```

For a selected lane `i`, the minimal egress source contract is
`ENDPOINTS[i] -> TERMINAL_BITS[i]`, followed by
`STATUS_CABLE_PATHS[i]` and `LITERAL_CABLE_PATHS[i]`.

## Bare-metal and TOE reading

This result supports a concrete distinction among three events:

1. a recurrent literal reaches an executable open port;
2. a terminal record is generated and can then be copied into independent
   downstream uses;
3. a later multi-input consumer forms only when both its literal lineage and
   all-five status lineage are present.

No observer, external reader, clock role, probability weight, or global word
is needed for that finite composition. A “read” can therefore be modelled as
another local record-forming interaction, not as an extra kind of event.

The probe does **not** establish witness independence in the physical sense:
both downstream branches share one generated terminal ancestor. It also does
not prove irreversibility, Born weights, a local time rate, particle identity,
mass, gravity, or a storage-limited simulation ontology.

TOE-lane consequences are correspondingly bounded:

- **formation/readout:** generated write, later copy, and gated consumption
  compose under one local append-only law;
- **information:** five distributed literals acquire one generated
  value-neutral finite-membership lineage without becoming a 32-valued word;
- **matter:** this is a finite binding mechanism, not particle identity;
- **time:** causal order is present, but no clock or time-rate theorem is
  added;
- **probability/quantum:** untouched; no Born or coherence claim follows;
- **gravity/capacity:** untouched; apparatus cost is explicit bookkeeping,
  not evidence for a universal storage budget.

## Axiom consequence

No axiom addition follows from Cycle 190.

The positive construction removes the exact Cycle-183 reason for proposing an
extra “formation by read” axiom: the retained local record grammar can already
carry a generated fact out of recurrent support, copy it into two downstream
uses, form a value-neutral finite-membership lineage, and gate ordered terminal
records. If a final axiom sentence is later required, this probe constrains it
away from observer language and away from making a clock the cause of locking.
It does not by itself force a two-independent-witness biconditional.
