# Cycle-80 Recurrence Audit and Endpoint-to-Tube Nucleation — Cycle 85

**Date:** 2026-07-14
**Authority:** none
**Status:** scoped lower bound and induction verified; live endpoint attachment constructed
**Constitutional effect:** none

Companion runner:

```text
scripts/cycle80_recurrence_audit_endpoint_tube_nucleation_cycle85_2026_07_14.py
```

## Result

Cycle 80's recurrent core survives independent audit, with one correction to
its composition claim.

1. The 17-site bound is valid in the stated serial-layer class.
2. Indefinite continuation follows from a finite strict-nearest-neighbour,
   period-three induction quotient; it does not rest on extrapolating the
   tested 15-layer horizon.
3. Cycle 80's raw-domain calculation against Cycle 75 is arithmetically
   correct, but Cycle 75 literally selects Cycle 72's now-rejected endpoint
   table. That exact selected-law composition is stale.
4. Replacing it with the current live-safe, joint-endpoint Cycle 78 table
   yields a collision-free composition and an explicit finite bridge to the
   recurrent tube.

The attachment is not supplied. Starting with the actual Cycle-78 terminal,
26 strict-NN appends write exactly:

```text
17 Cycle-80 A-layer records
 9 finite bridge-guide records.
```

An existing generated `D1` record at `(2,3,0)` is the rear cap. It already has
both `Z_A` and `Z_C` in its mandatory ancestry. The bridge's `R_LA` launcher is
written last in the causal order: every one of the 26 bridge records is in its
mandatory ancestry. Only then can the Cycle-80 table write the first B seed.

Thus `NEXT_FRONT_TO_TUBE_NUCLEATION` is closed for this exact candidate-law
route. This is not a universal-law selection or axiom result.

## 1. The scoped 17-site lower bound

The claim is deliberately narrower than “every recurrent strict-NN machine
needs seventeen sites.” It applies to a transverse serial layer satisfying:

- one Hamiltonian causal path visits every layer site;
- each phase starts at the previous phase's launcher and ends at a different
  launcher;
- the three launchers lie on the same square-lattice colour; and
- every launcher has all four transverse neighbours inside the footprint.

Fix one launcher at the origin. Three distinct same-colour square-lattice
sites have at least eight distinct opposite-colour neighbours. The runner
checks this exactly, not heuristically. If the neighbour union had fewer than
eight sites, the three degree-four neighbourhoods' overlap graph would have to
be connected. Same-colour neighbourhoods overlap only at separation at most
two, so every connected triple lies within Manhattan distance four of the
anchor. Exhausting that finite box gives:

```text
minimum distinct opposite-colour neighbours: 8
anchored minimizing triples:                 18
```

A Hamiltonian path with same-colour endpoints has one more endpoint-colour
site than opposite-colour sites. Eight forced opposite-colour cage sites
therefore force at least `9+8=17` total sites. Cycle 80 attains the bound:

```text
even-colour sites: 9
odd-colour sites:  8
launcher-neighbour union: 8
total:             17.
```

Pipelined, non-Hamiltonian, larger-period, non-tube, or non-fully-caged
machines remain outside the claim.

## 2. Why the recurrence proof is genuinely unbounded

The proof uses locality and periodicity, not “it worked through layer 15.”

Every rule input lies at one of the six strict nearest neighbours. The layer
alphabet has exact period three. Consequently any potential append in a long
tube depends only on:

- the fixed rear boundary;
- one of three completed interior three-layer contexts; or
- one of three partial frontier transitions.

The runner exhausts a stronger four-completed-layer window for each current
phase. In every window:

```text
compiled conditions: 18
reachable states:     18
append edges:         18
complete layer:       reachable
wrong append:         0
output conflict:      0
outside write:        exact following-phase seed only.
```

Completed horizons 6, 7, and 8 separately cover the three phase residues and
the fixed rear/interior contexts. Each has exactly one enabled assignment: the
next seed. Nonseed rows for a phase require an already written predecessor of
that same phase, so the one-parent launcher row is the only way to introduce a
new phase.

This supplies the induction:

1. the completed A layer and rear cap expose exactly the B seed;
2. the relevant phase window exhausts every partial B-layer schedule and
   reaches exactly the completed B layer;
3. rear and interior contexts remain quiet because their strict-NN context is
   one of the finite checked period-three representatives;
4. the completed B layer exposes exactly the C seed; and
5. the same argument cycles `B -> C -> A -> B` without a horizon parameter.

The longer finite horizons remain useful controls, but they are no longer the
logical source of the unbounded claim.

## 3. Selected-law correction

Cycle 80 composes its recurrent rows with `c75.UNION_TABLE`. That object is
literally Cycle 72's union table. Cycle 77 and Cycle 79 subsequently showed
that Cycle 72/Cycle 76 endpoint variants have real mixed-history races. Raw
domain disjointness does not repair an unsafe component.

The correction uses the current Cycle 78 construction, whose B records all
have both endpoints in mandatory ancestry and whose current mixed audit is
green. Exact raw-domain census:

```text
Cycle-78 selected rows                 159 canonical / 3,464 raw
Cycle-85 bridge rows                    26 canonical /   606 raw
Cycle-80 recurrence rows                51 canonical / 1,170 raw
pairwise raw-domain intersections        0
corrected union                         236 canonical / 5,240 raw
multi-output raw inputs                   0.
```

The old operational word conclusion survives but its exact inventory changes:

```text
live Cycle-78 full source/row roles: 93
Cycle-80 recurrent roles:           51
finite bridge-guide roles:           9
overlap:                              0
total:                              153
```

Therefore `128 < 153 <= 256`: this exact live route still requires eight
bits. Cycle 80's older count of 134 is not the current selected-route count.

## 4. Bare-metal attachment geometry

The proper-cubic transform is

```text
R(x,y,z) = (-z,x,-y)
shift    = (3,4,1).
```

It maps Cycle 80's standard rear-cap coordinate `(-1,1,1)` onto the generated
Cycle-78 record

```text
(2,3,0): D1.
```

The A layer lies in physical plane `y=4`; recurrence grows outward through
`y=5,6,...`. No record is supplied and no existing record is overwritten.
The rear cap's content need not be `Z0`: Cycle 80 uses the cap as occupied
backstop, and no recurrent rule consumes its content.

The bridge begins from several exact terminal contexts and joins them into one
causal sweep. Nine guides resolve the places where a one-parent A role would
otherwise have rotational aliases. The load-bearing dependency spine is:

```text
A02 -> A12 -> A13 -> A23
                         \
N2 -> G0 -> G1 -> N0 -> A33 -> A32 -> A22 -> A21 -> A31 -> A41
                                                               \
H0 + N2 -> H1 -> H2 -> H3 -------------------------------> A40
                                                               |
                                      A40 -> A30 -> A20 -> A10
                                                               |
N1 --------------------------------------------------------> A00
                                                               |
                                      A00 + A02 -----------> A01
                                                               |
                      A01 + A10 + A12 + A21 + rear cap -> R_LA.
```

The exact local signatures add some extra joins, but never remove these. The
fixed-point ancestry calculation gives:

```text
mandatory launcher ancestors: 26 / 26 bridge records.
```

This matters. A simpler direct singleton construction was found first, but it
wrote the launcher midway through the layer; the recurrent one-parent seed row
then fired into an unfinished transverse site. The final bridge makes the
launcher the causal completion record, not merely the last row listed in a
script.

## 5. Exact endpoint/bridge graphs

From the completed live Cycle-78 terminal, with selected, bridge, and
recurrence rules all active:

```text
conditions:                 30
reachable states:          291
append edges:              780
complete bridge:             1 reachable
wrong/off-footprint writes:  0
output conflicts:            0
boundary write:              exact first B seed only.
```

The stronger graph starts at the completed Cycle-67 terminal and interleaves
all 47 Cycle-78 endpoint writes with all 26 bridge writes:

```text
declared additions:          73
conditions:                 109
reachable states:     1,305,172
append edges:         8,753,059
complete state:               1 reachable
wrong/off-footprint writes:   0
output conflicts:             0
boundary write:               exact first B seed only.
```

This graph allows bridge roots to form whenever their physical parents exist;
it does not serialize the endpoint and bridge by fiat.

## 6. Full mixed-history audit

The final scan goes back through all 242,033 reachable Cycle-60 states, all 67
Cycle-67 availability masks, and every locally available subset of the
combined 73-record Cycle-78/bridge continuation. Python big-integer masks are
used because the combined continuation exceeds 64 records.

```text
downstream availability masks                 18
interface candidates                         496
retained candidates                          245
mixed local contexts                     115,957
ancestry-certified wrong contexts          1,143
ancestry-certified target/output classes       60
causally feasible wrong contexts                0
feasible raw conflicts                          0
feasible Cycle-60 blockers                      0
feasible Cycle-67 blockers                      0.
```

The 1,143 wrong-looking static contexts all require a present record while one
of its mandatory ancestors is absent. None can be a first bad append.

The recurrence table is also quiet before tube completion for a structural
reason: the bridge writes only A roles; every nonseed B row requires a B
predecessor, and the only first-B row requires `R_LA`. Since all 26 bridge
records are mandatory ancestors of `R_LA`, recurrence cannot outrun the
bridge. Exact transformed horizons through nine layers independently show
only the proper next seed.

## 7. What is now closed—and what is not

For this exact candidate law, Cycle 85 closes:

```text
NEXT_FRONT_TO_TUBE_NUCLEATION
```

in the strong sense requested: a live-safe joint-endpoint terminal grows one
complete Cycle-80 A layer and a rear cap without any supplied record, then
hands off to the unbounded recurrent core.

It does not close:

- `TUBE_LAYER_TO_LOGICAL_FRONT`;
- eight-bit physical port construction or selected output writing;
- nearby multi-tube collision/resource sharing beyond the separate Cycle-84
  control;
- exact universal-law selection;
- occurrence weights, probability, rate, clock calibration, mass, gravity,
  continuum recovery, or empirical calibration.

No axiom sentence follows from this finite construction.

## 8. No-go discipline gate

No broad nucleation no-go is shipped. The only negative correction is that
Cycle 80's exact Cycle-75/Cycle-72 composition is not the current live-safe
selected route. The repair succeeds in this cycle.

### N1 — five distinct routes

1. **ATTEMPTED — keep Cycle 75/Cycle 72:** raw domains are disjoint, but the
   component has the live bare-`X_B` endpoint race established by Cycle 77.
2. **RULED OUT BY PRIOR — substitute Cycle 76:** Cycle 79 constructs exact
   schedules in which its `YS` row steals `P1` and `P3`.
3. **RULED OUT BY PRIOR — use Cycle 77 BY-first:** Cycle 79's comparison finds
   it mixed-safe but without no-B-before-both-endpoints, so it is the wrong
   source for the requested stronger attachment.
4. **RULED OUT BY PRIOR — use Cycle 79's caged two-layer guide:** the same
   comparison finds it mixed-safe but likewise without the joint-endpoint B
   invariant.
5. **ATTEMPTED — use current Cycle 78:** preserves both-endpoint ancestry,
   composes collision-free, and supports the successful bridge.

The bridge itself also tested direct A-layer staging, direct launcher-last
staging, a bare-`W2` auxiliary, and a bare-`BTG` seed. The first launched too
early; no direct launcher-last order existed in the tested embedding; the
bare auxiliaries created transient aliases. The final Hamiltonian causal sweep
with gated guides closes those exact failures.

### N2 — wall independence

The apparent “unsafe selected component” and “missing tube bridge” are not
independent final walls: replacing the component supplies the joint endpoint
record used as the bridge cap, and the successful bridge retires the second.
The collapsed residual set is empty for this scoped route. Logical-front
rebinding and physical eight-bit realization remain separate future tasks,
not hidden parts of this claim.

### N3 — hidden-wall scan

“By construction” has been replaced by exact graph and mixed-history counts.
The rear cap is not background or supplied context: its coordinate, content,
and both-endpoint ancestry are checked. “Selected” is used only for the named
finite Cycle-78 table and carries no universal-law authority. The induction
uses only checked strict-NN range and exact phase periodicity.

### N4 — residual matching

| Witness | Witness residual | Present residual | Match? |
|---|---|---|---|
| `MIXED_CYCLE76_CAGED_GUIDE_AUDIT_CYCLE79_NOTE_2026-07-14.md:43` | Cycle-72 bare-`X_B` live race | stale Cycle-72 component in Cycle 80 | yes |
| `MIXED_CYCLE76_CAGED_GUIDE_AUDIT_CYCLE79_NOTE_2026-07-14.md:87` | Cycle-76 `YS` theft of `P1/P3` | possible Cycle-76 substitute | yes |
| `JOINT_ENDPOINT_MIXED_REBIND_CYCLE78_NOTE_2026-07-14.md:16` | joint-endpoint live-safe endpoint | requested no-B-before-both source | yes |
| `THREE_PHASE_RECURRENT_APPEND_TUBE_CYCLE80_NOTE_2026-07-14.md:100` | supplied A-layer/rear-cap interface | endpoint-to-tube bridge | yes |

No general first-record or cosmological-nucleation result is cited as if it
were this finite endpoint handoff.

### N5 — rhetoric audit

The rejected statement is only “Cycle 75/Cycle 72 is a live-safe selected
component for Cycle 80.” Raw-table disjointness remains true. No statement is
made that recurrence, guides, or strict-NN attachment are impossible; the
successful Cycle-78 bridge disproves those broader phrasings.

### N6 — partial-closure scan

The correction needs no axiom, primitive, convention, or imported physical
law. It is retired by substituting the already constructed live endpoint and
adding a finite exact table whose inputs are existing record contents.

### N7 — hostile steelman

A hostile reviewer should say that the Cycle-75 defect is bookkeeping, not a
recurrence obstruction: later endpoint cycles may provide a live table with
the same extensional interface, and strict locality may let one late boundary
record seed the tube. That steelman is correct. Cycle 78 plus the generated
`D1` cap realizes it, so no no-go survives.

### N8 — cross-cycle echo

Cycles 52–57 already showed that a supplied renewal boundary can sometimes be
retired by a finite launcher-last builder. The same mechanism applies here:
separate finite nucleation from indefinite recurrence, make the launcher a
true completion record, and audit both tables live together. Cycle 85 uses
that retired-wall pattern rather than treating the supplied Cycle-80 source as
axiom-grade content.

**Gate outcome:** PASS for the narrow correction; broad no-go defeated by the
positive Cycle-78/85 construction.
