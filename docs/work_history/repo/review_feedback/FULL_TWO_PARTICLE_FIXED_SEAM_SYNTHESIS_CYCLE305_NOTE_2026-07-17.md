# Full two-particle fixed-seam synthesis — Cycle 305

Date: 2026-07-17

Type: constructive fifteen-wedge synthesis with strict N1--N8 review

Status: exact one-step `n=2` fixed-seam comparator; recurrent separated-cell
volume update remains unbuilt

Authority: none

Audit: unset

Companion artifacts:

```text
scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py
docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md
scripts/full_two_particle_fixed_seam_synthesis_cycle305_2026_07_17.py
```

## Retained constructive result

Cycle 305 constructs one exact 30-column `E_x` containing all fifteen
unordered direction pairs and both endpoint slices.  The twelve perpendicular
pairs and three antipodal pairs are both load bearing: deleting the antipodal
orbit leaves `wedge^2(C)` leakage of operator norm
`0.9428090415820635`.  Every one of the four two-edge path representatives for
an antipodal pair reduces to the same fixed-reference ray with phase zero.

The input-slice coin is the exact Cycle-219 exterior-square action on the
colocated two-particle sector.  The separated slice receives identity in the
unitary comparator completion:

```text
K_seam |p,0> = sum_q [wedge^2(C)]_(q,p) |q,0>,
K_seam |p,1> = |p,1>.
```

This correction is essential.  `wedge^2(C) tensor I_2` would apply an onsite
two-particle coin to particles occupying different cells.  It is not the
actual Cycle-230 volume law and is not retained.

The Cycle-230 one-step order is coin, then stream/catch-up, then contact:

```text
G_seam = D_coarse S_coarse K_seam,
E_x G_seam = G_physical,seam E_x.
```

For the forward `t=0` domain, stream separates every pair before contact, so
the subsequent contact is identity.  The reverse `t=1` branch is present only
to make a unitary comparator and is not recurrent physics.  Stream/coin and
stream/contact have nonzero commutators; contact/coin commute.  No ordering is
silently exchanged.

The 900 local matrix units, 27,000 products, projector transport, constraints,
all 24 frames, 576 frame products, all 27 translations, training `L=3,4,5`,
held `L=6`, deletion controls, and lawful-domain controls pass.  The fixed-seam
shell uses relative-state and matrix-unit support 42--54 M2 with inherited
overhead 21 M2 per cell.  Complete contact and stream products remain
extensive products of bounded factors; the 54-M2 census is not their lattice
union support.

## Exact scope and six-wall ledger

| wall | Cycle-305 movement | still open |
|---|---|---|
| `C_ref` | the fixed `+++` Wilson reference vacuum, zero tags, body anchor, direction frame, and representative phase are explicit imports | absolute reference preparation, physical reference genesis, cross-sector equivalence |
| `C_num` | all fifteen `n=2` wedges close exactly, including three antipodal columns required by the coin | odd parity, `n=0,1,3,4,5,6` in this interface, overlapping number sectors, full Fock |
| `C_wrap` | unchanged because compiler schedule and slice order are not physical time | recurrent clock, interval, rate calibration, event equivalence |
| `C_int` | one-step Cycle-230 order is exact; forward post-stream contact is identity and the contact restriction is explicit | collisions arriving in one cell, recoil, coupling/resource selection, recurrent interacting volume law |
| `C_local` | one exact `E_x`, complete `wedge^2(C)` input action, bounded comparator, stream/catch-up, covariance, translations, and held size coexist | actual separated-cell onsite coin, coherent position growth, primitive synthesis, simultaneous shells |
| `C_source` | unchanged; pair occupations and dimensionless phases supply no source law | moving source/response observable, reciprocal response, gravity/clock/tensor bridge |

The fixed reference lives in `C_ref`.  It is not used to explain `C_wrap`.
`C_wrap` stays unchanged solely because the schedule is not time.

## Resolution and semantic boundary

“Full two-particle sector” means all fifteen local direction wedges at one
supplied body position.  It does not mean a recurrent volume update, coherent
position, simultaneous shells, or full Fock.  “Physical comparator” means an
explicit bounded matrix-unit polynomial whose restriction is tested on
`im(E_x)`.  It does not mean that the identity completion on separated pairs
is the onsite law at their distinct cells.

The wrapped coin phase is not physical energy.  A matrix element or generator
element is not a rate.  The slices are not time.  The contact phase is not a
mass, source, gravity field, Record, occurrence, or Born weight.

## No-Go Discipline Gate

The narrow factual negative is retained: the 30-column fixed seam is not the
actual recurrent separated-cell volume update.  Cycle 304 directly applies
that separated-cell coin and finds leakage `0.9929474834848379` from the
fifteen-column output orbit.

The candidate broad negative—“no bounded extension can close the recurrent
two-particle or full-Fock volume update”—is unsupported.  The constructive
routes below defeat closure of that claim.

**Gate status: FAIL for the candidate broad negative; do not ship it.**

### N1 — alternative routes

| route | marker | attempted attack and disposition |
|---|---|---|
| perpendicular-only pair code | **ATTEMPTED** | attempt the coin on the twelve direct octahedron edges; it fails narrowly with antipodal leakage `0.9428090415820635`, so it cannot support a broad substrate negative |
| four antipodal path representatives | **ATTEMPTED** | attempt every bounded intermediate path for all opposite pairs; all reduce to one phase-zero physical ray, defeating a path obstruction |
| full fifteen-pair exterior square | **ATTEMPTED** | attempt the exact `wedge^2(C)` block on every unordered pair; exterior action, unitarity, determinant, trace, covariance, and held beta all succeed |
| two-slice exterior-square law | **ATTEMPTED** | attempt `wedge^2(C)` on both slices; review rejects the separated-slice interpretation, so the result is narrowed rather than promoted to recurrent physics |
| input-slice unitary comparator | **ATTEMPTED** | attempt `wedge^2(C)` only on colocated input pairs with identity completion; the bounded 30-sector polynomial succeeds exactly |
| Cycle-230 coin-stream-contact order | **ATTEMPTED** | attempt the declared order on the forward input domain; the intertwiner succeeds and post-stream contact is exactly identity |
| autonomous local matrix units | **ATTEMPTED** | attempt a literal physical polynomial instead of a dense label matrix; all algebra, projector, constraint, and deletion controls succeed |
| signed-wedge cubic action | **ATTEMPTED** | attempt both proper-cubic pair orbits and all group products; all physical face/tag columns and 576 products succeed |

Eight distinct routes use exact honesty markers.  Several succeed and one
failure is scope-specific, so the broad negative fails N1.

### N2 — wall-independence audit

After collapsing output-slice interpretation into the recurrent-volume task,
the remaining conditions are `W_reference`, `W_recurrent`, `W_position`,
`W_overlap`, and `W_primitive`.  Both closure directions are audited for every
pair.

| first condition | second condition | closing first closes second? | closing second closes first? | independent? | reason |
|---|---|---:|---:|---:|---|
| `W_reference` | `W_recurrent` | no | no | yes | preparing the fixed ray supplies no separated-cell update; a relative recurrent rule can retain the imported ray |
| `W_reference` | `W_position` | no | no | yes | reference preparation supplies no position amplitudes; a relative position code need not prepare the ray |
| `W_reference` | `W_overlap` | no | no | yes | one prepared vacuum does not close simultaneous-shell collisions; overlap closure can remain reference relative |
| `W_reference` | `W_primitive` | no | no | yes | preparing a ray does not decompose the dense polynomial; a gate synthesis does not prepare the Wilson sector |
| `W_recurrent` | `W_position` | no | no | yes | a local recurrent rule does not prepare a spatial superposition; a position encoder does not specify the separated-cell coin |
| `W_recurrent` | `W_overlap` | no | no | yes | one-pair recurrence does not close overlapping pairs; an overlap rule need not select the one-pair volume action |
| `W_recurrent` | `W_primitive` | no | no | yes | an exact recurrent block can precede native synthesis; a native decomposition does not choose the volume block |
| `W_position` | `W_overlap` | no | no | yes | one-pair position growth and multipair collision closure test different domains |
| `W_position` | `W_primitive` | no | no | yes | spatial amplitudes do not decompose a local polynomial; gate decomposition does not grow position support |
| `W_overlap` | `W_primitive` | no | no | yes | multipair closure and native decomposition are independent algebraic tasks |

All ten directional pairs remain independent.  They are constructive tasks,
not repeated witnesses for one obstruction.

### N3 — hidden-condition scan

The fixed reference, body address, six directions, antipodal representative
gauge, zero port tags, Cycle-219 coin, Cycle-230 coupling and order,
input-domain restriction, identity comparator completion, beta/size split,
tolerances, and matrix-unit polynomial are explicit.

The literal skill-trigger scan reports zero hits across all four Cycle-305
package paths: physical runner, physical note, synthesis runner, and this
note.  The scan is a prose control and supplies no physics premise.

### N4 — residual matching

| file and line witness | witness residual | claimed residual | match? |
|---|---|---|---:|
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:497` | all four opposite-pair paths reduce to one fixed-vacuum ray | antipodal state existence/path independence | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:589` | exact Gram, fifteen-pair census, support, constraints | one 30-column fixed-seam encoder | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:664` | matrix-unit algebra and projector transport | bounded physical comparator polynomial | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:732` | exterior action/unitarity/determinant/trace | `wedge^2(C)` on the colocated input sector | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:830` | separate and composed restricted matrix residuals | one-step fixed-seam comparator | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:845` | Cycle-230 order and both nonzero commutators | ordered coin-stream-contact comparator | yes |
| `scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py:1181` | perpendicular-only leakage `sqrt(8)/3` in the input coin | need for the three antipodal input columns | yes |
| `docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md:43` | actual separated-cell coin leakage `0.9929474834848379` | current fixed orbit is not recurrent-volume invariant | yes, narrow residual only |
| `docs/work_history/repo/review_feedback/COHERENT_CUBIC_PAIR_ORBIT_SYNTHESIS_CYCLE303_NOTE_2026-07-17.md:257` | constructive proposal to enlarge the wedge address set | impossibility of wedge closure | no; dropped as negative support and executed constructively here |

The required repo echo search also returned older axiom, observability, source,
and labeling no-go files.  Their residuals differ from separated-cell CAR
closure, so none is counted as support for the broad negative.

### N5 — rhetoric and resolution audit

| resolution | tested | untested; broad-negative status |
|---|---|---|
| per path | four two-edge representatives for each antipodal pair | other representative gauges are unnecessary after exact stabilizer-ray equivalence; no broad negative |
| per pair | all fifteen unordered input pairs and both endpoint tag patterns | higher local particle numbers; no broad negative |
| per slice | exact input coin and identity output comparator | actual separated-cell onsite coin leaves this seam; narrow negative only |
| per block | matrix-unit comparator, stream, contact, inverse, and Cycle-230 ordered composition | native gate sequence; no broad negative |
| per anchor | every anchor at `L=3,4,5,6`, tested separately | one state coherent across anchors; no broad negative |
| lattice-wide | covariance family and extensive products of bounded factors | autonomous recurrent volume closure; no broad negative |
| full Fock | `n=2` only in Cycle 305 | `n=0,1,3,4,5,6`, overlaps, and sea state; no broad negative |
| semantics | dimensionless operators and compiler order | time, energy, rate, source, gravity, Record, occurrence, probability; no broad negative |

The only retained negative is resolution matched: this particular fixed seam
is not invariant under the actual separated-cell coin.  Nothing here excludes
an enlarged recurrent code.

### N6 — partial-closure paths

| constructive path | current evidence/status | what it could close |
|---|---|---|
| close the actual separated-cell coin orbit by adding its leaked columns | Cycle 304 measures the exact leakage and Cycle 305 supplies the full local input wedge | `W_recurrent` without new axioms |
| grow a translated direct sum and solve local address transport | all Cycle-305 translations and frame products are exact | `W_position` while retaining the reference import |
| add simultaneous shells with explicit tag-pattern collision tests | six collision-safe ports already retire the single-shell ownership conflict | `W_overlap` and higher even sectors |
| decompose the 210-term comparator into native controlled rotations | exact matrix-unit algebra and projector transport are already available | `W_primitive` |
| prepare or operationally supply the fixed-Wilson ray and test sector changes | the stabilizer rank and every relative column are exact | narrow or retire `W_reference` |

All are constructive non-axiom paths.  No convention-only repair is mislabeled
as new physics, and no new primitive or axiom is requested.

### N7 — hostile steelman

A hostile reviewer should reject the broad negative.  Cycle 304 already tells
you exactly how the true separated-cell coin exits the bounded output orbit,
and Cycle 305 shows that adding only three missing pair columns was enough to
retire the previous input-coin leakage.  Add the measured separated-cell
output columns, close them under the independent onsite coins and the existing
collision-safe stream, and solve the enlarged finite invariant-subspace
problem.  The exact signed-wedge representation, matrix-unit algebra, and
translation family remove the main symmetry and ownership excuses.  Until
that explicit closure attempt fails at growing sizes with matched residuals,
there is no credible route-independent obstruction.

This countercase is strong, so the broad negative is premature.

### N8 — cross-cycle echo

The required repository search was run over the prescribed negative phrases
and all `NO_GO_LEDGER.md` paths.  Generic axiom, source, observability, and
labeling entries were residual mismatches and were dropped under N4.  The
relevant compiler echoes are constructive retirements:

| earlier seam | actual retirement mechanism and witness | status | reuse here |
|---|---|---|---|
| catch-up tags collided on shared cells | six half-edge auxiliary ports and XOR-controlled disjoint swaps, `PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md` | single-layer ownership seam retired | keep explicit local ownership before inferring overlap obstruction |
| localized pair rays lacked coherent directions | one 24-column signed-wedge orbit, `COHERENT_CUBIC_PAIR_ORBIT_SYNTHESIS_CYCLE303_NOTE_2026-07-17.md` | perpendicular direction coherence retired | enlarge exact tag-sector bases rather than compare labels |
| physical coin and pair orbit had zero tag overlap | bounded flag-labeled fixed-seam comparator, `PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md` | label-identification error retired by a literal common refinement | add physical sectors instead of declaring incompatibility |
| twelve perpendicular wedges leaked under the coin | three path-independent antipodal columns, Cycle-305 physical runner line 1181 | complete local `wedge^2(C)` input sector retired | close the measured separated-cell leakage by the same finite-orbit method |
| a two-slice exterior-square completion overclaimed the law | restrict `wedge^2(C)` to colocated input and use identity only as comparator completion, Cycle-305 physical note line 72 | scope error retired | keep comparator and recurrent-law claims separate |
| compiler order risked being read as time | restore Cycle-230 coin-stream-contact order and test commutators, Cycle-305 physical runner line 845 | order mismatch retired | preserve ordered algebra without calling it time |

The repeated retirement mechanism is explicit enlargement plus exact finite
operator tests.  That mechanism remains available for the recurrent seam.

## Gate disposition

N1--N8 is complete for the narrow factual boundary and the candidate broad
negative.  The narrow boundary is retained: this 30-column completion is a
one-step fixed-seam comparator, not the actual recurrent volume law.

The broad Gate is FAIL.  No shared obstruction was identified.  No axiom
pressure was established.  The correct disposition is constructive partial
closure with named, independently testable continuations.
