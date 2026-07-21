# Physical autonomous scalar phase schedule — Cycle 524 (2026-07-21)

Authority: none
Audit: unset

## Decision

The staggered/time-multiplexed route has a bounded constructive compiler on
the tested domains.  Three marker states, encoded in **two M2 per coarse
cell** with one locally excluded computational state, autonomously sequence
the supplied coin, one simultaneous commuting seam layer, and the supplied
contact phase.  A marker count is **state count, not time**.  No event,
duration, clock, closure, Record, or physical-energy conclusion is made.

For a connected patch, every cell carries a scalar marker
`q_x in {0,1,2}`.  The physical two-M2 carrier also has `|3>`, removed by the
local involution `C_use=I-2|3><3|`.  Every neighbor edge carries the bounded
four-M2 equality involution

`C_xy = 2 sum_{q=0}^3 |q,q><q,q| - I`.

The common `+1` space of all `C_use` and `C_xy` is exactly the three states
`|q>^tensor cells`, not a globally queried register.  The fixed local marker
permutation is `0 -> 1 -> 2 -> 0`, with `3 -> 3`.  The data action controlled
by the pre-increment marker is

| marker | bounded data layer |
|---|---|
| 0 | all supplied onsite Cycle-219 coins |
| 1 | all incident Cycle-230/Cycle-315 seam FSWAPs in the declared layer |
| 2 | all supplied onsite Cycle-230 contact phases |
| 3 | identity; this state is locally excluded from the code |

On the synchronized marker code the one-count unitary is

`F = |1><0| tensor K + |2><1| tensor S + |0><2| tensor D + |3><3| tensor I`.

Thus, with `E_schedule=|0>^tensor cells tensor E_physical`, the exact target is

`E_schedule G_coarse = F_physical^3 E_schedule`, with `G_coarse=D S K`.

This is state count, not time.  `F_physical` is a fixed autonomous local rule;
host queries = 0.  There is no global Jordan–Wigner ordering, no preferred
axis order, and no nonlocal parity service.

## What is supplied and what is new

Supplied, not re-derived here:

- the Cycle-219 common six-mode coin and one-particle mass fixture;
- the Cycle-230 contact coupling and free-plus-contact ordering;
- the Cycle-315 complete two-cell all-Fock M64 encoder, seam FSWAP, edge-role
  gauge, physical constraint checks, and bounded off-code completion formula;
- the Cycle-324 four-cell `n=0,...,2` degree-three star, joint S4 order role,
  three incident seam maps, and physical shell;
- Cycle-235's 24 proper-cubic frames;
- the sparse numerical linear-algebra engine.

New in Cycle 524:

- the three-state scalar phase field in two physical M2 per cell;
- the local unused-state and neighbor equality constraints;
- the autonomous three-count recurrence rather than a host-selected schedule;
- schedule-level all-frame covariance and group-product checks;
- marker transition deletion, constraint deletion, and desynchronization
  discriminators;
- the exact lifted recurrence test on fresh L5 and held L=6 physical encodings.

The completion of a bounded data layer `L` on the selected physical ray shell
is the already explicit bounded-patch formula

`A_E(L)=E L E^dagger + I-E E^dagger`.

It acts only on the declared finite patch.  It is not being called a primitive
M2 gate decomposition.  That primitive/recurrent-volume question remains
open.

## Executable fixtures and acceptance tests

Runner:
`scripts/physical_autonomous_scalar_phase_schedule_cycle524_2026_07_21.py`

Command:

```bash
/usr/bin/time -lp python3 scripts/physical_autonomous_scalar_phase_schedule_cycle524_2026_07_21.py
```

The runner regenerates rather than imports the verdict for:

- complete two-cell all-Fock dimension 4096, every `n=0,...,12`, on L5 and
  held L=6;
- the four-cell degree-three star dimension 301, total `n=0,...,2`, on L5
  and held L=6;
- `F^dagger F=I`, the inverse, and `F^3 E_schedule=E_schedule DSK`;
- each completed physical stage and the composed
  `E_schedule G_coarse = F_physical^3 E_schedule` identity;
- all 24 proper-cubic frames, the 576 frame group products, and scalar marker
  action;
- all six orders of the three star seams;
- the one-particle mass fixture;
- marker-transition deletion, equality deletion, unused-state deletion,
  desynchronization, lawful-domain rejection, and off-code identity.

Acceptance tolerance is `8e-10` in operator norm unless an exact integer rank,
zero sparse failure count, or raw-entry maximum is reported.

## Exact result summary

The final fresh execution passed `12/12` checks.  It took `142.26 s` wall
time, used `916,504,576` bytes maximum resident set size, and reported zero
swaps.  This final run tests the actual joint-S4 relational lift, not merely a
selected factor-order branch.

On both L5 and held L=6, the complete two-cell fixture has 4096 columns,
63,488 physical rays, 65,536 encoding nonzeros, processed Gram residual zero,
raw Gram maximum `1.7763568394002505e-15`, processed macro intertwining
residual zero, and raw macro maximum `1.1355484503437165e-15`.  Its bounded
patch is 87 M2 (83 inherited plus four marker M2).

On both L5 and held L=6, the star fixture has 301 columns, 89,296 shared
physical rays, and 2,143,104 nonzeros across the 24 order branches.  The
joint-S4 raw Gram maximum is `1.0547118733938987e-14`; its maximum raw stage
intertwining entry is `5.325648159082862e-16`, its processed macro residual is
zero, and its raw macro maximum is `4.653679312506933e-16`.  Its bounded patch
is 168 M2 (160 inherited including the joint S4 role plus eight marker M2).
These are constant-overhead finite-patch counts, not a recurrent-volume
theorem.

The schedule, inverse, three-count recurrence, marker constraint
commutators, two-cell and star schedule covariance, all 576 star group
products, all six star seam orders, and processed physical intertwining
residuals are zero.  Deleting the coin transition gives unitarity residual
one.  Deleting neighbor equality enlarges the two-cell marker code from rank
3 to 9 and the star marker code from rank 3 to 81; deleting the unused-state
constraint adds one synchronized state.  A desynchronized marker has zero
overlap with the schedule code after three counts.

The preserved Cycle-219 mass is `0.4534056541748851`; the two-cell and star
uniform one-particle residuals are respectively
`3.8571762755144336e-16` and `2.4097051235218626e-16`.

## Route comparison

The marker-free simultaneous seam layer succeeds: the three incident star
FSWAPs commute and all six products agree.  This eliminates any reason to
serialize axes or introduce an axis/chirality marker inside phase 1.

The marker-free full macro `D S K` is also an exact one-step packaged
operator, but it simply supplies the composed law; it does not autonomously
expose the three atomic stages.  A two-state marker can reproduce the macro
only by packaging `D S` (or another pair) inside one controlled phase.  That
is a valid lower-state implementation under a weaker interface, not a
counterexample to the conditional three-distinct-stage count.

The prior opposite-carrier/protected-shadow construction is comparison only.
Its success is not imported into this route.  Likewise, this route does not
import a preferred edge order from the older three-slot directional schedule.

## Full no-go-discipline stress test for the conditional minimum and residual walls

No broad impossibility is claimed.  The only minimum statement is conditional:
if coin, seam, and contact must remain three separately addressable atomic
layers, an orthogonal finite-state controller needs at least three control
states and therefore at least two M2.  A weaker interface may package layers
and use fewer states.

### N1 — alternative-route enumeration

| route | status | evidence/disposition |
|---|---|---|
| three-state scalar marker with local exclusion/equality | **ATTEMPTED** | constructive Cycle-524 route |
| four-state scalar marker with an idle/reset phase | **ATTEMPTED** | works algebraically but has one more code state at the same two-M2 cost |
| two-state marker with packaged `D S` | **ATTEMPTED** | exact, but weakens the separately addressable atomic-stage interface |
| marker-free simultaneous seam layer | **ATTEMPTED** | exact because all three star FSWAPs commute |
| marker-free packaged `D S K` macro | **ATTEMPTED** | exact supplied composition, not an exposed autonomous stage compiler |
| directional three-slot marker | **ATTEMPTED** | Cycle 324 tested it; unnecessary here because the three seams commute and the scalar phase needs no edge choice |
| opposite-carrier/protected-shadow compiler | **ATTEMPTED** | independently tested in Cycle 522; comparison only, not evidence imported into this route |
| primitive M2 decomposition of every completed stage | **OPEN / UNTESTED** | dense bounded completion is explicit but not decomposed |
| recurrent overlapping-star volume compiler | **OPEN / UNTESTED** | one star is not a volume theorem |
| clock/event/closure interpretation of marker count | **OPEN / UNTESTED** | belongs to the causal-time lane and is not supplied here |

### N2 — wall-independence audit

Here `yes` means the current evidence distinguishes the two walls; it does not
mean either wall is closed.

| wall A | wall B | A without B? | B without A? | independent evidence? |
|---|---|---:|---:|---:|
| W_primitive | W_volume | yes | yes | yes |
| W_primitive | W_prepare | yes | yes | yes |
| W_primitive | W_time | yes | yes | yes |
| W_primitive | W_full_number_star | yes | yes | yes |
| W_volume | W_prepare | yes | yes | yes |
| W_volume | W_time | yes | yes | yes |
| W_volume | W_full_number_star | yes | yes | yes |
| W_prepare | W_time | yes | yes | yes |
| W_prepare | W_full_number_star | yes | yes | yes |
| W_time | W_full_number_star | yes | yes | yes |

Evidence: the finite-patch recurrence can pass while primitive decomposition,
volume overlap, preparation, time interpretation, and star sectors `n>2`
remain separately absent.  Conversely, adding a preparation or time law would
not supply a primitive decomposition or enlarge the tested star sector.

### N3 — hidden-wall scan

The construction still imports the Cycle-219 coin, Cycle-230 coupling and
ordering, the Cycle-315/324 physical ray maps, finite lattice geometry,
selected sector constraints, the joint S4 role, exact marker initialization,
and the off-code completion formula.  It does not supply preparation,
relaxation back into the marker code, robustness to faulty constraints,
primitive gate depth, recurrent overlap consistency, a thermodynamic limit,
physical time, physical energy, Records, or probabilities.

### N4 — exact witness pinning

The constructive and deletion witnesses are
`scripts/physical_autonomous_scalar_phase_schedule_cycle524_2026_07_21.py:152`
(`phase_schedule`), `:224` (`marker_constraints`), `:298`
(`completion_controls`), `:326` (`joint_role_completion_controls`), `:440`
(`two_cell_covariance`), and `:475` (`star_covariance`).
The inherited physical witnesses are regenerated through Cycle-315
`joint_encoding` and Cycle-324 `multi_order_encodings`.  A fresh command,
branch head, runtime, RSS, swap, and exact residual block are recorded below;
no prose-only witness is accepted.

### N5 — residual matching

The tested residual is the claimed recurrence residual:
`||F_physical^3 E_schedule-E_schedule D S K||`.  Stage completion residuals,
Gram residuals, covariance residuals, frame group-product failures, constraint
commutators, and mass residuals are reported separately.  A small Gram error
is not substituted for a schedule result.  Deleting one marker transition
must produce order-one nonunitarity; deleting equality or exclusion must
increase the admitted marker rank.

### N6 — partial-closure paths

Even if primitive decomposition or recurrent-volume overlap later fails, this
finite two-cell/all-Fock and one-star/`n<=2` autonomous recurrence remains a
useful local compiler result.  Even if the marker is later reinterpreted or
replaced, marker-free simultaneous streaming remains valid.  None of the
residual walls collapses the completed bounded fixtures.

### N7 — strongest steelman

The strongest objection is that `A_E(L)` may hide a difficult dense local
unitary and that synchronizing markers across an extended lattice may require
preparation or fault correction not shown here.  Accepted.  The response is
narrow: the action, support, local constraints, inverse, code-space
intertwining, and covariance are explicit on bounded patches; primitive depth,
preparation, and recurrence across arbitrary overlaps remain open.

### N8 — cross-cycle echo

Cycles 315 and 324 already separate a successful bounded physical encoder
from the open primitive and volume walls.  Cycle 522 independently re-earned
a selected-carrier compiler while leaving schedule autonomy open.  Cycle 524
closes that schedule-autonomy item on the declared finite fixtures, but does
not turn the repeated primitive/volume/preparation gaps into an impossibility.
There is no shared route-independent obstruction and no axiom pressure.

## TOE dependency ledger and disposition

| wall | Cycle-524 movement | status after this route |
|---|---|---|
| `C_ref` | scalar marker and its constraints transform trivially; data schedule is tested under every proper-cubic frame | stronger finite-patch closure |
| `C_num` | complete two-cell all-Fock is retained; star remains `n<=2` | two-cell closed on fixture, star widening open |
| `C_wrap` | marker-free simultaneous three-seam layer recurs exactly on one shared-cell star | improved, recurrent volume still open |
| `C_int` | supplied contact remains a distinct autonomous phase and its deletion is discriminating | stronger finite-patch closure |
| `C_local` | two M2/cell, local exclusion/equality checks, bounded 87/168-M2 patches | constructive bounded closure; primitive decomposition open |
| `C_source` | no source-response law is constructed | unchanged/open |

Route disposition: the staggered route **passes on the declared finite code
spaces**.  Marker-free streaming is absorbed as a successful subroutine;
marker-free full composition is a weaker-interface packaging alternative;
directional serialization is unnecessary.  This is not a physical-time law,
not a recurrent-volume compiler, and not an axiom candidate.  No axiom
pressure follows.
