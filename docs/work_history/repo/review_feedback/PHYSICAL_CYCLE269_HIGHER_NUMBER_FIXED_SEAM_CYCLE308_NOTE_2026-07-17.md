# Physical Cycle-269 higher-number fixed seams — Cycle 308

Date: 2026-07-17

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

```text
scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py
```

## Result up front

Cycle 308 constructs two bounded, reference-relative higher-number interfaces
on physical Cycle-269 M2 sites:

1. all twenty logical triples and both comparator slices in one 40-column
   `n=3` encoder, using one coherently distributed physical carrier over the
   three unoccupied outward ports; and
2. all fifteen logical quadruples and both comparator slices in one 30-column
   `n=4` encoder that closes directly in the fixed-Wilson total-even sector.

The logical input blocks carry the complete `wedge^3(C)` and `wedge^4(C)` of
the Cycle-219 six-mode coin.  The separated slices receive identity only as an
explicit identity comparator completion.  This is not a recurrent volume
update and does not claim that identity is the actual separated-cell onsite
coin.

The declared Cycle-230 order is coin, then stream/catch-up, then contact:

```text
G_3 = D_3 S_3 K_3,
G_4 = D_4 S_4 K_4,
E_n G_n = G_physical,n E_n.
```

The onsite contact is not reused from the two-particle seam.  With
`g=0.37`, its input phases are

```text
D_3|t=0> = exp(i 3g)|t=0>,
D_4|t=0> = exp(i 6g)|t=0>,
D_n|t=1> = |t=1>.
```

Those exponents are the actual Cycle-230 pair counts
`binom(3,2)=3` and `binom(4,2)=6`.  After forward stream every logical
particle is in a different neighboring cell, and the `n=3` carrier is alone
in the body cell, so subsequent contact is identity.  The nontrivial reverse
branch is tested only as a comparator completion.

## The even `n=4` construction

Let `Q` be an ordered four-direction subset and `Q^c` its ordered two-mode
complement.  Choose the full six-occupation ray `P_6` from three bounded
antipodal paths and define the oriented Hodge representative

```text
P_Q = epsilon(Q,Q^c) P_6 P_(Q^c)^dagger.
```

The Levi-Civita sign `epsilon(Q,Q^c)` is essential.  It makes the literal
physical column transform as the signed `wedge^4` basis, including frames
whose six-direction permutation is odd.

The executable also enumerates every perfect matching of every quadruple,
all available antipodal intermediate paths, and both pair-word orders.  At
each of `L=3,4,5,6`, all 252 words have the requested four occupations and
reduce to the same fixed-reference ray.  Their exact relative phases are
`{0:102, 1:24, 2:102, 3:24}`.  Thus the different path words are phase-gauge
representatives, not different physical states.  No pairing or path ordering
is promoted to physics.

The direct encoder is

```text
E_4 = sum_Q sum_(t=0)^1 |P_(Q,t)><Q,t|,
```

with fifteen logical quadruples, thirty logical columns, and thirty distinct
literal microstates.  It uses no parity carrier.

## The odd `n=3` carrier construction

The Cycle-269 face code exposes the total-even matter algebra: the product of
all displayed `B_v` occupation parities is identity.  A bare three-occupation
syndrome is therefore outside this declared code domain.  Cycle 308 does not
infer an odd carrier from the earlier `n=1` comparator and does not call a
free phase flag a fermion.

Instead, for a triple `S` and each of its three complement directions
`d notin S`, construct one literal branch with:

- the three logical occupations at the supplied body cell;
- one additional physical matter carrier at the outward neighbor on port
  `d`; and
- the matching port tags required by `B_v Z_port(v)=+1`.

Every branch has four physical matter occupations and is lawful in the
total-even face code.  The encoded logical column is the coherent sum

```text
|Phi_S> = (1/sqrt(3)) sum_(d notin S)
          epsilon(S,d) eta_d |P_(S,d)>,
```

where `epsilon(S,d)` is the insertion orientation and `eta_d` is the fixed
outer-edge orientation phase supplied by the Cycle-269 `A` dictionary.  The
three branches are orthogonal because their literal occupation/tag patterns
are different.  Their squared amplitudes sum to one exactly.  Consequently,
the `n=3` encoder has logical dimension forty, while its literal physical
microbasis has dimension 120:

```text
20 triples x 2 slices = 40 logical columns,
40 columns x 3 carrier branches = 120 literal microstates.
```

This distinction is load bearing.  Deleting one branch gives Gram residual
`1/3`; it is not a redundant enumeration.

On the input slice, every carrier is alone in a neighboring cell and the
three logical particles share the body cell.  Complete physical stream swaps
all four occupied endpoints: the three logical occupations move to their
three neighbors and the carrier moves into the otherwise empty body port
`d`.  There are no double-occupied outer edges, and port catch-up follows the
occupations autonomously.  On the output slice every occupied cell contains
one particle, so contact is identity.

The complement sum is mapped into itself by every proper-cubic frame.  The
`epsilon eta` coefficient is precisely the orientation repair needed for the
physical branch sum to carry `wedge^3`, rather than an untracked Hodge sign.
There is no preferred carrier direction, no global Jordan–Wigner ordering,
no nonlocal parity service, and no host-side carrier selection.

This construction supplies the odd-sector parity carrier on the declared
fixed seam.  Preparation of its conditional coherent superposition remains
open, as do its overlap and recurrent-volume behavior.

## Complete exterior-power coins

For `n=3,4`, the coefficient matrix is evaluated from every minor:

```text
[wedge^n(C)]_(I,J) = det C[I,J].
```

The runner uses the full 20-by-20 and 15-by-15 matrices, not an orbit sample.
For training `beta=-0.2,-0.3,-0.4` and held `beta=-0.35`, it checks:

- exterior action on generic decomposable `n`-vectors;
- unitarity of the complete matrix;
- `det(wedge^n C)=det(C)^binom(5,n-1)`; and
- covariance with every proper-cubic exterior representation.

The earned logical comparator is

```text
K_n = blockdiag(wedge^n(C), I),
```

where the displayed blocks mean input slice and separated slice.  In the
runner's interleaved ordering, `wedge^n(C)` occupies the even-indexed
input-slice rows and columns.

## Literal ambient matrix-unit completion

For each sector, let `E_n` be the literal microbasis isometry and
`P_n=E_n E_n^dagger`.  Cycle 308 constructs the ambient physical comparator

```text
K_physical,n = E_n K_n E_n^dagger + I - P_n.
```

The first term is expanded in bounded physical branch matrix units.  For
`n=3`, a transition from source branch `b` to target branch `a` has coefficient

```text
(K_n)_(i,j) alpha_(i,a) conjugate(alpha_(j,b)).
```

The executable checks those amplitude weights term by term.  Identity on the
orthogonal complement makes the displayed ambient comparator unitary; it is
not assigned recurrent-law meaning.

The physical inventories are:

| sector | logical matrix units | matching products | literal transition microterms | active comparator coefficients | expanded active microterms |
|---|---:|---:|---:|---:|---:|
| `n=3` | 1,600 | 64,000 | 14,400 | 348 | 3,132 |
| `n=4` | 900 | 27,000 | 900 | 210 | 210 |

Every branch transition maps its exact physical representative, and every
transition commutes with all inherited face/Wilson stabilizers and local
`B_v Z_port(v)` constraints.  The runner constructs the full ambient matrices,
checks `K_physical,n E_n=E_n K_n`, unitarity and inverse on the declared
ambient microbasis, and uses those matrices—not a hardcoded logical image—in
the physical `D S K` composition.

## Stream, contact, and composition residuals

At every body anchor for `L=3,4,5` and held `L=6`, both sectors test the
literal physical stream/catch-up permutation, physical occupation-counting
contact, ambient matrix-unit coin, and their composition.  Each sector tests
432 encoders.

The final cold run records the following nominal `beta=-0.3` residuals.  The
stream and contact intertwiners are exact zero; the ambient coin and composed
residuals are at floating roundoff:

| residual | `n=3` | `n=4` |
|---|---:|---:|
| ambient physical coin intertwiner | `1.8337104151503998e-15` | `6.637442841777097e-17` |
| physical DSK intertwiner | `1.8337104151503998e-15` | `6.637442841777097e-17` |
| ambient unitarity/inverse | `5.1816506042999435e-15` | `2.6862645623197677e-15` |
| physical code leakage | `1.7149641763737896e-15` | `0` |

The trained and held-beta ambient coin/DSK sweeps also pass.  Their largest
ambient coin unitarity residual is `7.262441272646427e-15` for `n=3` and
`3.558701124877353e-15` for `n=4`.

The declared order is protected by noncommutation:

| residual | `n=3` | `n=4` |
|---|---:|---:|
| `||[S,K]||_2` | `1.9946299293034573` | `1.9999948451220562` |
| `||[S,D]||_2` | `1.0538866004066028` | `1.7913973713600952` |
| forward post-stream contact | `0` | `0` |
| reverse comparator contact | `4.7131241581706425` | `6.9380521857173925` |

Contact commutes with the input-slice coin comparator because it is scalar on
the complete fixed-number input block.  This does not license exchange with
stream.

## Covariance, orbit closure, and translations

The twenty triples form two proper-cubic occupation orbits of sizes 8 and 12.
The fifteen quadruples form two orbits of sizes 3 and 12.  Neither orbit alone
is coin invariant: each incomplete-orbit coin leakage has operator norm
`0.9428090415820635`.  The complete exterior-power bases close that leakage.

The physical covariance census is:

| sector | frame/anchor branch-slice tests | group products | L=3 translation branch-slice tests |
|---|---:|---:|---:|
| `n=3` | 77,760 | 576 | 3,240 |
| `n=4` | 19,440 | 576 | 810 |

All phase, tag, carrier-map, group-law, and translation residuals are exactly
zero under all 24 proper-cubic frames and all 27 L=3 translations.
Complete-coin covariance residuals are approximately `9.84e-16` and
`1.07e-15`.  The literal 120- and 30-dimensional signed microbasis frame
matrices are unitary exactly and satisfy `R_micro E=E R_logical` exactly.
Ambient physical coin and DSK covariance residuals are
`9.96162733947567e-16` for `n=3` and `1.0666845157356562e-15` for `n=4`;
physical stream and contact covariance are exact zero.  The Hodge and
complement orientation conventions are explicitly
supplied in the formulas above; they are not hidden frame choices.

## Support, overhead, and constraints

For every anchor at every tested size, both sector interfaces have the same
bounded patch-union census:

```text
face M2 union                    30, 34, 38, or 42
port M2 union                    12
total patch union                42, 46, 50, or at most 54 M2
maximum n=3 literal branch       31 M2
maximum n=4 literal branch       34 M2
installed homogeneous overhead  21 M2 per cell
```

The installed overhead remains fifteen face plus six collision-safe port M2
per cell.  The `n=3` carrier uses an existing physical matter vertex and its
existing port tag; no new species or M2 site is added.  The patch unions are
relative-state and matrix-unit support.  Complete lattice stream and contact
remain extensive products of bounded local factors, not one 54-M2 global
operator.

Exact Gram, occupation, local-check, fixed-Wilson, and port-constraint leakage
counts are zero through held `L=6`.

## Leakage, deletion controls, and lawful-domain controls

The runner detects:

- deleting either proper-cubic occupation orbit, with coin leakage
  `0.9428090415820635` in both sectors;
- deleting one of the three `n=3` carrier branches, with Gram residual `1/3`;
- deleting the `epsilon eta` carrier phases, with coefficient-space residual
  `sqrt(2)` and failed physical covariance;
- deleting auxiliary catch-up, which leaves every tested streamed literal
  state outside the code;
- deleting an active logical coin coefficient, which breaks unitarity;
- mutating an active ambient physical matrix-unit coefficient, which breaks
  both `K_physical E=E K` and ambient unitarity—the residual pairs are
  `(0.255879507294021,0.595200765832624)` for `n=3` and
  `(0.34045188744302696,0.4673119189904847)` for `n=4`;
- deleting contact, with residuals
  `|exp(i3g)-1|=1.0538866004066025` and
  `|exp(i6g)-1|=1.7913973713600952`; and
- deleting one stream column, with unit closure leakage.

Lawful-domain controls reject repeated directions, a carrier on an occupied
logical port, out-of-range directions, sectors other than 3 or 4, malformed
bodies and coefficient matrices, and aliased `L=2`.

## One-particle mass firewall

Cycle 308 imports the unchanged Cycle-219 six-mode coin.  It rechecks the
one-particle mass fixture unchanged at all three training beta values and held
`beta=-0.35`.  The higher exterior powers and Cycle-230 contact phases are not
called new mass derivations.  Wrapped phase is not called physical energy,
and a matrix or generator element is not called a rate.

## No-Go Discipline Gate

The narrow retained negative is only this domain statement: a bare syndrome
with exactly three occupied Cycle-269 matter vertices is absent from the
declared fixed-Wilson total-even face code.  The executable proves the
displayed `B_v` product is identity and checks every single-face Pauli
generator has even `B`-syndrome parity.

The candidate broad negative—“no bounded physical M2 encoding can carry the
local odd sector”—is false on the tested fixed seam.  The complement-port
carrier is a constructive counterexample.

**Gate status: FAIL for the candidate broad negative; DO NOT SHIP it.**

### N1 — alternative routes

| route | marker | actual attack and disposition |
|---|---|---|
| bare three-occupation face syndrome | **ATTEMPTED** | tests the existing face algebra without a carrier; every generator has even syndrome parity, so only this direct grammar is excluded |
| one selected complement-port carrier | **ATTEMPTED** | makes every branch even and streams correctly, but selecting one of the three complement directions breaks the required cubic treatment and is not retained |
| equal positive complement sum | **ATTEMPTED** | removes the selected direction but drops the insertion/edge orientation; the explicit deletion fixture gives 544 frame failures |
| oriented coherent complement carrier | **ATTEMPTED** | succeeds: three normalized orthogonal branches, exact physical stream/contact, all frames, and held size |
| arbitrary quadruple matching paths | **ATTEMPTED** | all 252 words are the same fixed-reference ray with exact recorded phase; path choice is not an obstruction |
| oriented Hodge quadruple basis | **ATTEMPTED** | succeeds directly in the total-even fixed-Wilson sector and carries the complete signed `wedge^4` action |
| one proper-cubic occupation orbit | **ATTEMPTED** | each sector's smaller basis leaks under the coin by `0.9428090415820635`; the complete two-orbit basis closes |
| ambient branch matrix units | **ATTEMPTED** | succeeds with explicit amplitude weights, off-code identity completion, DSK intertwining, unitarity, covariance, and mutation controls |

All eight markers describe executed Cycle-308 tests.  Several constructive
routes succeed, so N1 itself rejects the broad negative.

### N2 — directed condition-independence audit

Use the collapsed condition set

```text
W_bare       direct three-occupation syndrome in the existing face grammar
W_prepare    preparation of the conditional complement carrier
W_recurrent  actual separated-cell recurrent volume coin
W_overlap    simultaneous overlapping fixed-seam patches
W_common     integration of all number sectors in one common Fock code
```

| first condition | second condition | closing first closes second? | closing second closes first? | independent? |
|---|---|---:|---:|---:|
| `W_bare` | `W_prepare` | no | no | yes |
| `W_bare` | `W_recurrent` | no | no | yes |
| `W_bare` | `W_overlap` | no | no | yes |
| `W_bare` | `W_common` | no | no | yes |
| `W_prepare` | `W_recurrent` | no | no | yes |
| `W_prepare` | `W_overlap` | no | no | yes |
| `W_prepare` | `W_common` | no | no | yes |
| `W_recurrent` | `W_overlap` | no | no | yes |
| `W_recurrent` | `W_common` | no | no | yes |
| `W_overlap` | `W_common` | no | no | yes |

All ten unordered pairs have both directions answered.  `W_bare` is retired
for the encoded logical sector by the carrier but remains a true statement
about the unextended face grammar.  None of the other conditions is evidence
for that narrow statement or for a shared obstruction.

### N3 — hidden-condition scan

The fixed Wilson signs, all-`B=+1` ray, body anchor, six directions, Hodge and
insertion orientations, outer-edge phases, zero port tags, carrier amplitudes,
Cycle-219 coin, Cycle-230 coupling/order, comparator identity completion,
training/held split, tolerances, and dense matrix-unit coefficients are all
listed explicitly.

The literal skill-trigger scan has zero hits across the Cycle-308 physical
runner, this note, and the strict synthesis runner.  This prose scan supplies
no physics premise.

### N4 — residual matching

| exact file and line witness | witness residual | Cycle-308 use | match? |
|---|---|---|---:|
| `scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py:566` | product of all displayed `B_v` is identity | bare odd syndrome is outside this declared face grammar | yes |
| `scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py:611` | coherent complement carrier gives lawful even branches | broad bounded-encoding negative | yes; it defeats the negative |
| `scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py:1019` | ambient physical coin and DSK intertwine through held size | fixed-seam constructive closure | yes |
| `scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py:1249` | literal microbasis and physical operators are frame covariant | no preferred-direction residual | yes |
| `docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md:43` | fixed Wilson signs leave total-even matter exponent | declared face-domain parity statement | yes |
| `docs/work_history/repo/review_feedback/HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md:55` | a lawful odd image follows from changed marked-reference data | impossibility of the local complement-port compiler | no; dropped as negative support and retained only as a constructive echo |
| `docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md:221` | deleting the antipodal `n=2` orbit causes coin leakage | odd parity/domain statement | no; used only as the finite-orbit closure analogy in N8 |
| `docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:39` | one extra M2 and a local relational constraint close a role-marker seam | direct three-occupation syndrome | no; used only as a constructive local-extension echo in N8 |

No mismatched earlier residual is counted as support for a negative claim.

### N5 — rhetoric and resolution audit

| resolution | tested | exact disposition |
|---|---|---|
| per face generator | every single `X` and `Z` face generator at `L=3,4,5,6` | syndrome parity is even in the declared face algebra |
| per bare triple | all twenty three-direction labels | no bare three-occupation Pauli ray in that algebra |
| per carrier branch | all sixty branch labels and both slices per anchor | each is a lawful four-occupation physical state |
| per encoded column | all forty `n=3` columns | exact normalized isometry; the narrow bare-syndrome statement no longer applies |
| per local block | full ambient coin, stream, contact, inverse, and DSK | constructive closure on the fixed seam |
| per anchor/size | every anchor at `L=3,4,5,6` | exact fixed-seam closure including held `L=6` |
| lattice-wide recurrent volume | not tested | no negative conclusion; actual separated-cell coin remains open |
| overlapping/full Fock | not tested | no negative conclusion; common code and overlaps remain open |

The phrase “absent” is therefore restricted to a bare three-occupation
syndrome in the already declared total-even face algebra.  It is not applied
to local carrier encodings, larger graphs, recurrence, or full Fock.

### N6 — constructive partial-closure paths

| constructive path | current state | what it can close without an axiom claim |
|---|---|---|
| coherent complement-port carrier | executed successfully in Cycle 308 | local logical `n=3` fixed seam |
| prepare the carrier with a bounded local gauge/resource circuit | open | `W_prepare` |
| close measured separated-cell coin images under translated carrier branches | open | `W_recurrent` |
| add simultaneous shells and test shared-port collision sectors | open | `W_overlap` |
| combine the existing `n=1,2,3,4` interfaces with explicit sector labels and `n=0,5,6` blocks | open | `W_common` |
| enlarge the bosonization graph by a covariant scalar auxiliary fermion | untested alternative | a different odd-sector realization |

The successful carrier is already the import-bearing partial closure.  No
new primitive or axiom is requested, and no convention change is mislabeled
as physics.

### N7 — hostile steelman

A hostile reviewer should reject any parity no-go immediately.  Cycle 308
has already written the counterexample: pair each logical triple with one
ordinary physical carrier in the covariant complement-port superposition,
retain the exact insertion and edge-orientation phases, and complete the local
coin with branch matrix units.  The resulting 40-column code has zero Gram,
constraint, stream, contact, DSK, frame, translation, and held-size failures.
Even if that particular carrier later fails under recurrence or overlap, an
enlarged scalar auxiliary mode or the marked-reference gauging mechanism of
Cycle 245 remains untested here.  Therefore only the bare-syndrome domain fact
survives; a route-independent obstruction does not.

### N8 — cross-cycle echo

The required repository negative-phrase search and `NO_GO_LEDGER.md` walk were
run.  Generic source, observability, labeling, and axiom-selection entries do
not match the local odd-syndrome residual and are not used.  The relevant
echoes are constructive:

| earlier result | retirement mechanism | Cycle-308 lesson |
|---|---|---|
| Cycle 245 parity-sector gauging | marked charge and changed flat Wilson data make an odd state image lawful | explicit carrier/reference data can extend a fixed parity presentation; do not infer a universal parity obstruction |
| Cycle 305 complete two-particle seam | adding three missing antipodal columns closes `wedge^2(C)` leakage | complete finite occupation orbits before declaring a coin obstruction |
| Cycle 306 relational role-marker gauge | one additional local M2 plus a non-diagonal constraint retires a free selector | test bounded gauge partners before treating a local-label failure as substrate-wide |
| Cycle 308 complement-port carrier | three oriented branches close the odd logical fixed seam with no new M2 species | the current candidate broad negative is directly retired |

N1, N6, N7, and N8 all contain constructive counterexamples or untested live
routes.  The candidate broad negative therefore fails the release gate.  The
narrow direct-domain statement is retained with no shared obstruction and no
axiom pressure.

## Six-wall dependency ledger

| wall | Cycle-308 movement | still open |
|---|---|---|
| `C_ref` | fixed-Wilson reference, Hodge orientation, complement-carrier orientation, body anchor, and zero port tags are explicit | absolute reference and conditional carrier preparation; cross-sector reference equivalence |
| `C_num` | complete local `n=3` and `n=4` exterior-power occupation bases close; odd logical number is represented by an explicit fourth physical carrier | a common `n=0..6` code, direct odd physical parity, number-sector-changing laws, full Fock |
| `C_wrap` | unchanged; slices and compiler substeps are not physical time | recurrence clock, event equivalence, rate calibration |
| `C_int` | actual `exp(i3g)` and `exp(i6g)` onsite contact restrictions and ordered `D S K` maps close on the fixed seams | collision arrivals, recoil, carrier interactions beyond one step, overlapping shells, recurrent interacting volume |
| `C_local` | bounded physical columns, matrix-unit coins, stream/catch-up, constraints, frames, translations, and held size coexist | separated-cell onsite recurrence, coherent position, primitive synthesis, simultaneous patches |
| `C_source` | unchanged; occupations and dimensionless contact phases supply no source law | moving source/response observable, reciprocal response, gravity/clock/tensor bridge |

`C_wrap` is unchanged because the schedule is not time.  The fixed reference
and carrier preparation imports stay in `C_ref`; they are not reassigned to
time or source.

## Supplied structure and novelty boundary

Supplied are:

1. the fixed `+++` Wilson, all-`B=+1` reference ray;
2. one body-cell address and the six Cycle-269 direction labels;
3. the Cycle-269 `A/B/FSWAP` dictionary, outer-edge orientation phases, and
   framing repair;
4. six zero-initialized collision-safe port M2 per cell;
5. the Cycle-219 coin coefficient matrix;
6. the Cycle-230 coupling `g=0.37` and coin-stream-contact order;
7. the Levi-Civita/Hodge convention and complement-carrier orientation;
8. the lawful fixed-seam domain and locally supplied dense matrix-unit
   coefficients; and
9. preparation of the fixed reference, arbitrary logical amplitudes, and the
   conditional carrier superposition.

Derived are the complete exterior-power matrices, literal physical columns,
carrier normalization, direct even-sector closure, physical contact counts,
ambient comparator completions, separate and composed intertwiners,
constraints, covariance, group laws, translations, held-size closure,
support, leakage, and deletion residuals.

Local auxiliary fermion encodings, exterior-power representations, Hodge
duality, and local fermion-to-qubit matrix-unit completions are prior-art
territory.  Cycle 308 claims only these explicit constructions and residuals
on the repository's Cycle-269 fixed-seam substrate.  Global novelty is not
established.

## Exact boundary

Cycle 308 is not a recurrent volume update, and the output identity is not an
actual separated-cell law.  Overlap remains open.  Absolute and conditional
carrier preparation remains open.  Coherent position, primitive synthesis,
collision arrivals, other number sectors in one common code, number-changing
laws, and a sea-state compiler remain open.  This is not a full-Fock compiler.

The carrier is code data, not a Record.  Compiler slices are not time.  The
contact phase is not a source or gravity field.  No Born/probability result is
claimed.  There is no broad no-go claim and no axiom pressure.
