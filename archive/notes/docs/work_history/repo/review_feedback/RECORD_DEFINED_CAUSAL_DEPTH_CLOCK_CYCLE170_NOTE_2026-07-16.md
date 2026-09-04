# Record-defined causal-depth clock — Cycle 170

**Type:** bounded_theorem

Status: parked constructive O↔T bridge on the current Cycle-166 candidate law.

Authority: the explicit `expected` / `dependencies` DAG emitted by the
[Cycle-166 physical joint stabilizer apparatus](PHYSICAL_JOINT_STABILIZER_UPDATE_CYCLE166_NOTE_2026-07-16.md).
This note changes no axiom, primitive, registry, policy, or audit surface.

## Question

Can the physical stabilizer update carry its own discrete clock reading, using
only the causal order of records that actually have to form?

## Result

Yes, in a narrow operational sense.

Give every initial record depth zero. For each required dynamic record `v`,
define

```text
d(v) = 1 + max d(parent),
```

where the maximum over an empty dynamic-parent set is zero. The operational
commit depth of the update is the largest depth of its two recurrent output
records.

Every declared dependency edge in the tested apparatus joins nearest-neighbor
sites. Every critical chain is therefore a visible chain of record commits,
not a count inferred from the scheduler's loop iterations.

For all four valid update branches, the latest output is also the deepest
dynamic record. The resulting dimensionless relative duration is:

| case `(c1,c2)` | dynamic records | dependency edges | roots | sinks | lane-1 depth | lane-2 depth | operation depth | records in output causal past |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `(0,0)` | 30,633 | 30,636 | 15 | 5 | 4,036 | 3,970 | **4,036** | 22,317 |
| `(0,1)` | 30,637 | 30,640 | 15 | 5 | 4,036 | 3,974 | **4,036** | 22,807 |
| `(1,0)` | 30,703 | 30,706 | 15 | 5 | 4,106 | 3,970 | **4,106** | 23,021 |
| `(1,1)` | 30,831 | 30,834 | 15 | 5 | 4,106 | 4,098 | **4,106** | 25,958 |

The branch-dependent statement is exact: `c1=1` selects the longer lane-1
record path and adds 70 commits, raising the update depth from 4,036 to 4,106.

## Exact layer profiles

Let `L(k)` be the number of dynamic records at depth `k`. Each profile sums to
the corresponding dynamic-record count above.

All four cases share:

```text
depths       L(k)
1            15
2-11         19
12-411       22
412-427      20
428-435      18
436-491      16
492-1149     14
1150-1227    13
1228-1269    12
1270-1331    11
1332-1399    10
1400-1424     9
1425-1498     8
1499-1545     7
1546-1669     6
1670-1984     5
1985-2058     4
2059-2305     3
2306-2630     2
2631-2908     3
```

The exact tails are:

```text
(0,0): 2909-3970 -> 2; 3971-4036 -> 1
(0,1): 2909-3974 -> 2; 3975-4036 -> 1
(1,0): 2909-3970 -> 2; 3971-4106 -> 1
(1,1): 2909-4098 -> 2; 4099-4106 -> 1
```

The verifier hashes the full uncompressed sequences:

```text
(0,0) d13aeee419088ef5c052c6fd5aacd241574a48ae2209c84a074e323c2e4e0627
(0,1) 2172b45e39b58351779b89f118df3842caf0109c41adb25d9e9c53add66e331f
(1,0) 741637eb0dd40958c5b9892572c7b6402664ace49c86c99aca20138980420bd2
(1,1) ec6fcee756ac9fb9f222dc90e95efdab6fa989004e8b4e47a70efc6b08ae6d53
```

## All-edge causal integrity

The depth recurrence uses 122,816 declared dynamic edges across the four
cases:

```text
(0,0) 30,636
(0,1) 30,640
(1,0) 30,706
(1,1) 30,834
total  122,816
```

Every edge receives an exact local availability test. For each child, the
verifier reconstructs its nearest-neighbor formation signature from fixed
initial neighbors plus all declared dynamic parents. The complete signature
must enable exactly the child's expected role. Each declared parent is then
removed separately, and the expected child role must cease to be enabled.

All 122,816 declared dynamic edges pass. There are zero:

- earlier adjacent dynamic records omitted from the parent set;
- declared parents outside the earlier nearest-neighbor set;
- complete signatures with the wrong or ambiguous child output; and
- decorative parents whose removal leaves the claimed child enabled.

Thus the longest paths and layer profiles are computed from physically
load-bearing record dependencies, not inflated metadata.

## Rotation and scheduler separation

All four DAGs were transformed through all 24 proper-cubic rotations. All 96
case/rotation instances reproduce the exact per-case profile, output depths,
critical depth, and hash.

For every rotated DAG, both lexicographically minimal and maximal linear
extensions were constructed and replayed. All 192 replays recover the same
depth and profile.

Scheduler work is not invariant. Using the Cycle-166 diagnostic
`sum(current enabled-frontier size)` gives:

| case | minimum-order range over rotations | maximum-order range over rotations | distinct totals in each family |
|---|---:|---:|---:|
| `(0,0)` | 252,122–399,165 | 252,122–398,786 | 24 / 24 |
| `(0,1)` | 251,170–399,169 | 251,170–398,790 | 24 / 24 |
| `(1,0)` | 250,974–399,305 | 250,974–398,926 | 24 / 24 |
| `(1,1)` | 250,718–399,433 | 250,718–399,054 | 24 / 24 |

The sequential enabled-frontier maximum ranges from 15 to 20 depending on
rotation and linear order, while the synchronous causal-layer maximum remains
22. Thus scheduler effort, scheduler order, enabled width, layer width, total
record count, and causal depth are distinct quantities.

For the unrotated presentation, minimum/maximum scheduler work is:

```text
(0,0) 269,149 / 263,639
(0,1) 268,513 / 263,651
(1,0) 269,499 / 263,303
(1,1) 269,435 / 263,687
```

## Record-visible refinement controls

The selected output routes have physically different record lengths:

```text
lane 1: 404 or 474 records
lane 2: 318, 322, or 446 records
```

Three exact comparisons separate local latency, global completion, and record
count:

1. `(0,0) -> (0,1)` adds four lane-2 records and four lane-2 depth units, but
   does not change the 4,036 global depth because lane 1 remains later.
2. `(0,0) -> (1,0)` adds seventy lane-1 records and raises both lane-1 and
   global depth by exactly seventy.
3. `(1,0) -> (1,1)` adds 128 lane-2 records and raises lane-2 depth by 128, but
   leaves global depth at 4,106 because lane 1 remains later.

These are actual alternate record paths under the same candidate law. The
clock reads the longest causal refinement, not the total number of committed
records.

## Parent-deletion controls

The existing twenty strategic parent deletions were rerun for every case,
giving eighty physical controls.

They cover source-to-tap, trunk-to-splitter, both case inputs, both multiplier
inputs, and each selected lane's case, selector, bus, terminal, and common
output parent. Every pair is a nearest-neighbor relation in the actual
apparatus. Removing the named parent when the child would otherwise be enabled
suppresses that child in all eighty controls.

The longest-path result is therefore not being read from decorative DAG
metadata whose declared edges can be removed without affecting record
formation.

## Physical parallel composition

Two complete caged copies were translated by `(2000,0,0)`. Across the full
sets of initial and dynamic sites there are zero overlaps and zero
nearest-neighbor cross-contacts. Local signatures in one copy therefore cannot
depend on the other.

All sixteen case-pair unions have:

```text
combined layer profile = profile A + profile B
combined depth         = max(depth A, depth B).
```

Two unions were also replayed physically, one causal layer at a time:

```text
(0,0) || (1,1): 61,464 dynamic records, depth 4,106, max layer 44
(1,1) || (1,1): 61,662 dynamic records, depth 4,106, max layer 44
```

In both runs the actual law-enabled set equals the declared layer at every
depth and is empty after completion. The second test doubles the dynamic
record count from 30,831 to 61,662 while leaving depth unchanged at 4,106.
This is the direct count-versus-duration control.

## Serial composition

At the abstract dependency level, serial composition is exact. Take a renamed
copy of a second DAG and add the first operation's latest output as a parent of
each of the second DAG's fifteen roots. For all sixteen ordered case pairs:

```text
serial profile = profile A followed by profile B
serial depth   = depth A + depth B.
```

The possible serial depths are 8,072, 8,142, and 8,212.

That is an abstract dependency composition, not a routed physical serial
apparatus.

Zero-cost serial gluing is unavailable for the present geometry. The two
generator source records have separation

```text
(480,0,0), squared length 230,400,
```

while the two recurrent output records have separation

```text
(320,-70,80), squared length 113,700.
```

No proper-cubic rotation, with either output ordering, maps one pair to the
other. A physical serial apparatus therefore needs visible transport or a
recompiled aligned output interface. Its transport commits must be included in
the serial clock reading.

This is an exclusion of zero-cost rigid identification for these exact ports,
not a serial-composition no-go.

## O↔T bridge

The O lane supplies a concrete conditional operation with two final recurrent
records. The T lane can assign that operation a coordinate-free discrete
reading from its causal record order:

```text
duration(update) = maximum required output commit depth.
```

The reading is:

- independent of proper-cubic presentation;
- independent of which valid linear scheduler realizes the partial order;
- sensitive to visible causal-path refinement;
- max-compositional for independent parallel operations; and
- additive for abstract serial dependency composition.

That is enough for an operational commit-depth clock and dimensionless relative
duration under this candidate law.

## Scope

This is not a continuous rate. It is not metric time. It does not supply
seconds, a conversion scale, a lapse, Lorentz symmetry, a causal-cone speed theorem,
stationarity, or a continuum limit. It is not a Lorentz or lapse result.

The four tested fixtures do not establish universality over arbitrary quantum
operations, arbitrary compiled geometries, or arbitrary candidate laws.

No axiom conclusion follows. In particular, no new Record wording, time axiom,
primitive, or registered premise is proposed.

## No-Go Discipline Gate

Status: **PASS for the exact seam exclusion; FAIL for a general serial no-go.**

### N1 — alternative routes

1. **ATTEMPTED AND OPEN:** route both recurrent rows to a translated second
   apparatus with visible row cables.
2. **OPEN:** recompile the common-output pair with the same relative separation
   as the next generator-source pair.
3. **OPEN:** insert a reusable two-row adapter or splitter/transport bundle.
4. **OPEN:** compile two updates jointly so the first common outputs are the
   second update's native sources.
5. **ATTEMPTED AT DAG LEVEL:** impose serial dependency links abstractly; this
   gives exact additivity but is not itself physical routing.

Those live routes defeat a general serial no-go.

### N2 — wall independence

The present physical residual is one collapsed interface fact: the two output
ports cannot be rigidly identified with the two next-source ports. Transport
cost and output-layout redesign are alternative closures of that same seam,
not independent constitutional walls.

### N3 — hidden-condition scan

The load-bearing conditions are explicit: the Cycle-166 candidate law, its
declared dependency DAG, initial records at layer zero, one unit per required
commit edge, and the tested four fixtures. “Operational clock” is not used as
a hidden conversion to metric time.

### N4 — residual matching

[Cycle 166](PHYSICAL_JOINT_STABILIZER_UPDATE_CYCLE166_NOTE_2026-07-16.md)
supports physical closure and scheduler confluence for this apparatus. It does
not claim serial-port alignment, a continuous rate, or a time axiom. No broader
negative is attributed to it.

### N5 — rhetoric audit

The exclusion applies only to rigid proper-cubic identification of these two
specific output sites with these two specific source sites. It is not extended
to transported links, redesigned ports, other compiled updates, or the lattice
as a whole.

### N6 — partial closure and axiom classification

Visible row transport or aligned recompilation is an ordinary compiler/geometry
path under fixed axioms. The current serial seam is not evidence that new
constitutional physics is required.

### N7 — strongest hostile steelman

A hostile reviewer can preserve the positive clock theorem and defeat the
serial exclusion by routing the two outputs through already retained row
transport mechanisms, then counting those extra commits. The mismatch proves
only that the link is not free; it does not show that the link cannot exist.

### N8 — cross-cycle echo

Cycle 166 itself closed multiple earlier interface seams by adding splitters
and integrated selector/gate geometry. Cycle 167 similarly moved sign decoding
to a distinct port after two exact interfaces failed. The repeated successful
mechanism is geometry repair with visible record cost, which remains available
for serial depth.

## Verification

- [Cycle-170 executable certificate](../../../../scripts/record_defined_causal_depth_clock_cycle170_2026_07_16.py)

```text
python3 -m py_compile \
  scripts/record_defined_causal_depth_clock_cycle170_2026_07_16.py

PYTHONPATH=scripts python3 \
  scripts/record_defined_causal_depth_clock_cycle170_2026_07_16.py
```
