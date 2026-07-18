# Physical Cycle-269 overlap-aware two-cell seam — Cycle 315

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit status is edited or proposed.

Companion runner:

```text
scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py
```

Methodology freshness: the no-go-discipline procedure, freshness instructions,
and case studies were read directly from freshly fetched `origin/main` at
`17cb0c5c32e753ef1297b185fbd1e8c6d41920c2`. The dirty worktree was not moved.

## Result up front

Cycle 315 constructs the first overlap-aware full-number physical seam between
two neighboring Cycle-311 M64 cells. The declared logical space is the complete
two-cell Fock space `M64 tensor M64`, with total `n=0,...,12`:

```text
H_edge = direct sum from n=0 to 12 of wedge^n(C^12),
dimension = 2^12 = 4,096.
```

Multiply the actual Cycle-311 role-gauge columns on the shared physical M2
patch, then reduce face paths against the same fixed-Wilson vacuum while
retaining every port, cell-role, and gauge occupation. The resulting maps
`E_AB` and `E_BA` each have 4,096 orthonormal columns in 63,488 occupied
physical rays. The cold run finds raw Gram entries at machine roundoff and
minimum Gram eigenvalue at least `0.999999999999997` at `L=3,4` and held
`L=6`.

The two endpoint orders are not equal physical codes. Their plain difference
has operator norm `1.999999999999993`, the local fermionic sign
`(-1)^(n_A n_B)` leaves residual `1.998627750723`, and their code-overlap map
is not unitary. Cycle 315 does not hide that result as a global occupation
order.

Instead it doubles the local AB/BA edge role, adds one local edge-role flag and
one local edge gauge companion `r_e`, and imposes

```text
C_edge = K_(AB<->BA) X_(r_e) = +1.
```

The doubled flagged shell has rank 8,192. Tensoring `r_e` gives rank 16,384;
the `C_edge=+1` sector has rank 8,192. Its rank-4,096 oriented input is one
endpoint slice, while a frame that reverses the edge endpoints selects the
other slice. The flag is a constrained local edge role, not a free global
ordering label.

On this constrained seam the explicit two-cell update is

```text
U_edge = D_contact S_FSWAP Gamma(C direct-sum C),
```

where `C` is the Cycle-219 six-mode coin, `S_FSWAP` is the literal fermionic
swap of the two outer-edge modes, and

```text
D_contact |S_A,S_B> =
  exp(i g [binom(|S_A|,2)+binom(|S_B|,2)]) |S_A,S_B>,
g=0.37.
```

For each edge role `q=AB,BA`, the bounded physical shell completion is

```text
A_q(U) = E_q U E_q^dagger + I - E_q E_q^dagger.
```

The edge gauge lift applies `A_AB direct-sum A_BA` on one `r_e` block and its
`K_(AB<->BA)` conjugate on the other. Constraint involution, constraint
eigenvalue, constraint commutator, physical intertwining, and seam unitarity
all vanish after the declared numerical tolerance; the companion raw maxima
are recorded separately. Randomized full-shell inverse residuals are at most
`3.69e-16`.

This is a bounded dense matrix-unit completion on one two-cell/one-edge seam.
It is the full `n=0,...,12` two-cell Fock compiler on that seam. It is not a
recurrent volume and not a proof that edge constraints commute when several
edges share a cell. Primitive realization and the volume application schedule
remain supplied rather than derived.

## Cell-role gauge is load bearing

Removing the Cycle-311 cell role-gauge completion before multiplying the two
cells gives Gram operator residual `1`. The exact overlap seam is
therefore a gain from the Cycle-311 relational construction, not a formal
tensor product of unextended rays.

Directly identifying AB and BA is also not lawful. The unflagged unordered
sum `(E_AB+E_BA)/sqrt(2)` remains full rank on this test but has Gram residual
approximately one, minimum Gram eigenvalue `0.666666666667`, and column norms
between one and `sqrt(2)`. The edge flag plus `r_e` relation repairs the metric
without choosing a volume-wide order.

The construction uses no global Jordan-Wigner string, global parity service,
volume-wide cell order, preferred axis, or host-side endpoint query. The local
edge owner is a covariant role: twelve proper-cubic frames preserve it and
twelve reverse it. Endpoint reversal acts inside the doubled edge seam.
No global ordering is used.

## Exact sector and update controls

| total number | dimension | Gram residual after tolerance | update unitarity after tolerance |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 12 | 0 | 0 |
| 2 | 66 | 0 | 0 |
| 3 | 220 | 0 | 0 |
| 4 | 495 | 0 | 0 |
| 5 | 792 | 0 | 0 |
| 6 | 924 | 0 | 0 |
| 7 | 792 | 0 | 0 |
| 8 | 495 | 0 | 0 |
| 9 | 220 | 0 | 0 |
| 10 | 66 | 0 | 0 |
| 11 | 12 | 0 | 0 |
| 12 | 1 | 0 | 0 |

The coin has 627,264 active logical coefficients, FSWAP has one signed entry
per column, and contact is nontrivial on 4,047 columns. The ordered factors do
not commute: `||[S,K]||=1.877706015765` and
`||[S,D]||=1.597241526398`. This protects coin, then edge FSWAP, then contact;
it does not call the compiler sequence physical time.

All contact phases are computed from the actual two-cell logical occupation
split. The sectors include simultaneous neighboring and same-cell
configurations through all twelve particles. The physical update is the joint
overlap-aware matrix-unit action; it is not the product of two independently
applied overlapping shell projectors.

## Raw machine residuals and exact combinatorial zeros

The runner reports both the unpruned maximum matrix entries and the tolerance-
processed operator residuals. Signed-permutation identities for FSWAP,
endpoint roles, frame group law, and translations are exact combinatorial
zeros. Coin, Gram, constrained-isometry, and covariance calculations carry
floating arithmetic and retain their raw machine-scale maxima in the output.

| calculation | raw maximum before tolerance pruning | processed residual |
|---|---:|---:|
| physical Gram, `L=3,4,6` | `1.776356839400e-15` | 0 |
| constrained edge-role Gram | `2.220446049250e-16` | 0 |
| `C_edge` eigenvalue and update intertwining | 0 | 0 |
| complete two-cell coin unitarity | `2.886580207820e-15` | 0 |
| literal FSWAP unitarity | 0 | 0 |
| contact unitarity | `1.122147886578e-16` | 0 |
| composed update unitarity | `2.664535472615e-15` | 0 |
| 24-frame update covariance | `2.167779754566e-16` | 0 |

The ambient AB/BA intertwiners are exact after sparse cancellation. Four
normalized random ambient vectors per edge role give inverse residuals between
`3.54e-16` and `3.69e-16`. These tests include off-code identity completion;
they are not code-only logical comparisons.

## Covariance, translations, held size, and mass

All 24 proper-cubic frames are tested. Twelve preserve the endpoint role and
twelve reverse it. The logical exterior representation includes the signed
cell exchange when endpoints reverse. The frame representation is unitary,
the axis-mapped coin-FSWAP-contact update is covariant, and all reported
post-tolerance residuals vanish.

The edge-role geometry passes 93,312 proper-cubic group-product tests and
4,374 `L=3` translation tests with zero failures. The physical Gram test is
unchanged at training `L=3,4` and held `L=6`: 4,096 columns, 63,488 physical
rays, and 65,536 nonzero amplitudes at every size.

The uniform two-cell one-particle vector has mass
`0.4534056541748851`, exactly the Cycle-219 fixture at displayed precision,
with eigenvector residual `3.857176275514e-16`. Contact phases are not called
mass. Wrapped phase is not called physical energy, a matrix unit is not called
a rate, and no compiler slice is called time.

## Physical M2 and constraint inventory

The observed two-cell patch union is:

| component | M2 count |
|---|---:|
| face M2 | 55 |
| port M2 | 22 |
| two cell flags | 2 |
| two cell gauge companions | 2 |
| new edge flag plus edge `r_e` | 2 |
| total patch union | 83 |

The largest joint branch uses 65 M2 including the edge-role pair. Installing
two edge-role M2 on each of the three undirected positive-axis edges per cell
raises homogeneous overhead from Cycle 311's 23 to 29 M2 per cell. These are
observed construction counts, not minima.

All audited branch words have zero inherited `B_v Z_port(v)` constraint
commutator failures and zero local-check/fixed-Wilson commutator failures.
`C_edge` is an additional local non-Pauli matrix-unit constraint on the edge
shell. Its primitive gate synthesis remains supplied.
Multi-edge constraint commutation remains open and untested.

## Leakage, deletion, and lawful-domain controls

The destructive controls are:

| deletion | residual |
|---|---:|
| one carrier-role amplitude `-0.223606797750 i` | Gram `0.05` |
| one FSWAP column | unitarity `1` |
| active off-diagonal coin coefficient | unitarity about `0.760509` |
| all nontrivial contact | `1.991150088371` |
| edge role gauge relation | shell rank 16,384 instead of constrained rank 8,192 |

The runner rejects total-number requests above twelve, an invalid edge axis,
repeated cell directions, and aliased `L=2`. It also retains the raw unordered
Gram failure as an independent deletion of the edge relation.

## Supplied-structure inventory

Supplied are:

1. the Cycle-269 fixed-Wilson reference and face/port dictionary;
2. the Cycle-311 cell flag, cell `r`, conditional odd carrier, and preparation;
3. one addressed neighboring-cell pair and one undirected physical edge;
4. the local endpoint-role flag and one edge `r_e` M2;
5. the non-Pauli relation `C_edge=K_(AB<->BA)X_(r_e)`;
6. the complete `M64 tensor M64` logical input rather than a number cutoff;
7. the Cycle-219 coin, Cycle-230 coupling, and coin-FSWAP-contact order;
8. dense local matrix-unit coefficients and off-code identity completions;
9. preparation of the fixed reference and arbitrary amplitudes in the
   4,096-column input; and
10. primitive realization and application of the bounded 83-M2 actions.

Derived are the shared-site AB and BA isometries, the raw-order mismatch, the
edge-role gauge repair, every `n=0,...,12` exterior block, the literal boundary
FSWAP, two-cell contact restrictions, ambient intertwiners and inverses,
constraint preservation, endpoint-reversing covariance, group law,
translations, held-size closure, mass preservation, and deletion residuals.

Still open are simultaneous three-cell/two-edge consistency, commutation of
edge constraints sharing one cell, all-edge recurrent stream, recurrent
contact arrivals and recoil, primitive synthesis, arbitrary position/reference
preparation, and a volume-wide full-Fock compiler.

## Prior-art and novelty boundary

Cycle 235 supplies the local total-even face/Gauss algebra. Cycle 308 supplies
the oriented odd carriers and direct higher-number rays. Cycle 311 supplies
the common M64 cell and its relational cell role. Cycle 312 identifies the
bounded physical overlap patches and shows why bare even-pair multiplication
does not reproduce exterior dynamics.

Cycle 315 claims only the explicit two-cell product reduction, its 4,096-
column isometry, the local edge-role gauge repair, and the bounded physical
coin-FSWAP-contact completion on this repository substrate. Exterior powers,
fermionic swaps, auxiliary gauge codes, and matrix-unit unitary completions
are prior-art territory. Global novelty priority is not asserted.

Thirring machinery is not used or compared.

## Exact boundary and TOE ledger

`C_local` advances from a one-pair block factorization to one full-Fock
two-cell edge overlap. `C_num` advances because every total sector through
twelve coexists on that overlap, removing the local total-number cutoff import.
`C_int` advances only for the two-cell contact restriction; recurrent arrivals
remain open. `C_ref` retains the fixed
reference and local role preparation. `C_wrap` and `C_source` are unchanged.

| wall | Cycle-315 movement | still open |
|---|---|---|
| `C_ref` | local endpoint order becomes a constrained edge role | reference genesis and conditional preparation |
| `C_num` | complete two-cell total `n=0,...,12` overlap | number-changing laws and volume full Fock |
| `C_wrap` | unchanged | physical event equivalence, interval, clock, and rate |
| `C_int` | exact one-edge FSWAP plus two-cell contact matrix | multi-edge arrivals, recurrent contact, recoil |
| `C_local` | 83-M2 overlap seam, local edge gauge, frames and held size | shared-cell edge-constraint compatibility, primitive synthesis, volume schedule |
| `C_source` | unchanged | action/energy/stress/source response and gravity relation |

Planning maturity becomes: operational quantum / Records `3.2/5`
(`61/27/87`), causal time / clock `1.8/5` (`34/17/62`), inertia / matter
`4.0/5` (`73/34/94`), gravity / source / resource `2.0/5` (`39/16/65`), and
Born / probability / realized history `1.8/5` (`33/14/82`). Only the matter
and local-compiler evidence moves. No Record, source, clock, occurrence, or
probability result is added.

## No-Go Discipline Gate

The candidate broad negative that physical M2 overlaps cannot carry arbitrary
fermion number is defeated on one edge. The different broad claim that no
local extension can close a recurrent volume is also not earned: multi-edge,
generic non-Pauli, and time-multiplexed variants remain open.

Gate status: **FAIL / DO NOT SHIP the broad negative.**

### N1 — alternative routes

| route | marker | actual attack and disposition |
|---|---|---|
| raw product of unextended cell rays | **ATTEMPTED** | non-isometric on the shared patch with Gram residual `1` |
| product of Cycle-311 cell-role gauge codes | **ATTEMPTED** | succeeds with 4,096 orthonormal columns through held `L=6` |
| direct AB equals BA identification | **ATTEMPTED** | fails with physical order residual `1.999999999999993` |
| local fermionic parity-sign identification | **ATTEMPTED** | fails with residual `1.998627750723` |
| unflagged unordered AB/BA superposition | **ATTEMPTED** | remains full rank but has Gram residual about one |
| doubled edge role plus relational edge r_e | **ATTEMPTED** | succeeds with exact constrained rank 8,192 and covariant endpoint reversal |
| generic non-Pauli multi-edge gauge | **OPEN / UNTESTED** | could enforce compatible order relations when several edges share a cell |
| staggered or time-multiplexed overlap schedule | **OPEN / UNTESTED** | could avoid simultaneous edge constraints; no physical schedule is supplied here |
| three-cell/two-edge joint matrix completion | **OPEN / UNTESTED** | is the next finite discriminator for recurrent assembly |

The successful local gauge and three open constructive variants block every
route-independent negative.

### N2 — wall-independence audit

The remaining collapsed target set is `W_multiedge`, `W_recurrent`,
`W_synthesis`, `W_prepare`, and `W_schedule`.

| left | right | closing left closes right? | closing right closes left? | independent? |
|---|---|---:|---:|---:|
| W_multiedge | W_recurrent | no | no | yes |
| W_multiedge | W_synthesis | no | no | yes |
| W_multiedge | W_prepare | no | no | yes |
| W_multiedge | W_schedule | no | no | yes |
| W_recurrent | W_synthesis | no | no | yes |
| W_recurrent | W_prepare | no | no | yes |
| W_recurrent | W_schedule | no | no | yes |
| W_synthesis | W_prepare | no | no | yes |
| W_synthesis | W_schedule | no | no | yes |
| W_prepare | W_schedule | no | no | yes |

`W_multiedge` is compatibility of several edge constraints on one cell.
`W_recurrent` is the full translated stream/contact law. `W_synthesis` is a
primitive bounded-gate realization. `W_prepare` is reference and carrier
preparation. `W_schedule` is an autonomous covariant application order.

### N3 — hidden-condition scan

The literal procedure-trigger scan runs over both Cycle-315 release paths and
must return zero. The fixed reference, addresses, orientations, complete
two-cell domain and sector decomposition, edge roles, constraints, dense
coefficients, off-code completion, coupling, order, preparation, sizes, and
tolerances are listed above.

### N4 — residual matching

| exact witness | witness residual | Cycle-315 use | match? |
|---|---|---|---:|
| Cycle-235 local even-algebra result | bounded face/Gauss physical words | inherited constraint grammar | yes |
| Cycle-308 oriented carrier result | lawful odd `n=3` and even `n=4` physical rays | cell branch basis | yes |
| Cycle-311 common M64 result | one rank-64 local cell with relational role | each factor of the two-cell product | yes |
| Cycle-312 pair-sector overlap result | bounded patches and physical order mismatch | exact overlap target and raw comparator | yes |
| exact Cycle-315 runner witnesses | two-cell Gram, edge gauge, update, covariance, and deletion | current retained result | yes |

The current numerical witnesses are pinned to exact executable locations:

| current witness | exact file and line |
|---|---|
| complete `M64 tensor M64` physical isometry | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1248` |
| physical AB/BA order mismatch | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1272` |
| local edge-role gauge repair | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1280` |
| full coin-FSWAP-contact update | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1297` |
| on-code and off-code ambient completion | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1315` |
| 24-frame covariance and endpoint reversal | `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:1334` |

No route-specific Cycle-312 failure is cited against generic multi-edge gauge
or time-multiplexed completion.

### N5 — rhetoric and resolution audit

| resolution | tested | disposition |
|---|---|---|
| one Cycle-311 cell | all 64 labels | predecessor common M64 isometry retained |
| one two-cell physical overlap | all total `n=0,...,12` labels | exact joint code and update |
| one endpoint order | AB and BA separately | each isometric; physical codes differ |
| one edge-role gauge | complete doubled shell | exact local repair |
| frames/translations/held size | all 24 frames, L3 translations, held L6 | exact family covariance and stable Gram |
| several edges sharing a cell | not tested | no compatibility or negative claim |
| recurrent volume/full Fock | not tested | no closure or negative claim |

The retained negative wording is restricted to the exact raw products and
unflagged unordered candidate.

### N6 — partial-closure paths

Cycle 235 supplies the constrained face algebra. Cycle 308 supplies oriented
odd carriers. Cycle 311 supplies a local cell role gauge. Cycle 312 supplies
the bounded overlap patches. Cycle 315 applies the same relational repair on
one edge and closes the arbitrary-number seam there. Generic non-Pauli
multi-edge constraints, an explicit three-cell joint matrix, or a staggered
edge schedule remain direct construction paths. No premise edit is requested.

The optimal next attack is the smallest three-cell/two-edge patch: build both
edge constraints on the shared cell, test their commutator and joint rank, and
solve the two-FSWAP braid/contact update through low total number before
widening to the complete three-cell logical space.

### N7 — hostile steelman

A hostile reviewer should reject a recurrent-volume no-go because the only
new difficulty is compatibility between several already successful bounded
edge gauges. The single-edge construction has exact arbitrary-number Gram,
FSWAP, contact, constraint, frame-reversal, translation, and held-size
closure. A three-cell joint non-Pauli matrix completion can correlate the two
edge roles, and a staggered schedule can avoid imposing them simultaneously.
Neither route has been tested. The one-edge success is evidence for another
constructive cycle, not constitutional pressure.

### N8 — cross-cycle echo

| prior result | retirement mechanism | Cycle-315 lesson |
|---|---|---|
| Cycle 235 closed-face parity boundary | bounded even-algebra operator map | preserve the useful local algebra after a state-route limitation |
| Cycle 306 free seam role | one relational gauge companion | convert a copied role into a local constraint |
| Cycle 308 bare odd syndrome | oriented complement carrier | enlarge the local code before declaring a parity obstruction |
| Cycle 311 raw cell-role collision | cell flag plus relational `r` | raw rank loss can be repaired without a free label |
| Cycle 312 global pair projector | bounded block factorization | a global-looking completion can decompose on the right code |
| Cycle 315 endpoint order | doubled edge role plus relational `r_e` | local ordering mismatch can become covariant gauge data |

Every echo supports the open multi-edge attack. No shared obstruction and no
axiom pressure follow.

## Verification

```text
python3 scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py
```
