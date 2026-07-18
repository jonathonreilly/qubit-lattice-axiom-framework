# Coherent proper-cubic pair-orbit synthesis — Cycle 303

Date: 2026-07-17

Type: constructive coherent-orbit synthesis with strict N1--N8 review

Status: one exact fixed-anchor coherent direction orbit for stream/contact;
coin, position growth, reference preparation, and full Fock remain open

Authority: none

Audit: unset

Constitutional effect: none. No protected scientific surface is edited or
proposed.

Companion runner:

```text
scripts/coherent_cubic_pair_orbit_synthesis_cycle303_2026_07_17.py
```

## Result

The preceding localized rays now form one common linear map rather than a
collection selected one ray at a time. At each supplied coarse-cell anchor
`x`, twelve perpendicular identical-pair wedge addresses and two stream slices
give the twenty-four-dimensional isometry

```text
E_x = sum_(a,t) P_(x,a,t)|Omega_+++><x,a,t|,
E_x^dagger E_x = I_24.
```

The exact Gram identity follows from twenty-four distinct auxiliary tag
patterns. It makes `E_x` one linear isometry on every coefficient vector. It
does not supply a preparation circuit for the columns or amplitudes.

The same complete physical stream/catch-up product and the same Cycle-230
contact product restrict to the full image of `E_x` and obey

```text
E_x S_coarse = S_physical E_x,
E_x C_coarse = C_physical E_x,
E_x (C_coarse S_coarse) = (C_physical S_physical) E_x,
E_x (S_coarse C_coarse) = (S_physical C_physical) E_x,

S_coarse = I_12 tensor X_2,
C_coarse = I_12 tensor diag(exp(i g),1),
g=0.37.
```

These 24-by-24 objects are restricted physical matrices on `im(E_x)`, not
full-Hilbert matrices. Equality on the complete basis, rather than three
sampled amplitude vectors, earns arbitrary coherent address superpositions.
The first composition is the actual Cycle-230 stream-then-contact order from
`G_g=W_g Gamma(SC)`; the second is its reverse-order comparator. Exchanging
them has norm residual `0.36789306705608243`.

## Symmetry, antisymmetry, and exact controls

The address states are one identical CAR pair. Source/carrier reversal changes
both stream slices by the same minus sign and leaves the tags unchanged. The
roles are wedge slots, not independent species.

Every proper-cubic frame acts with declared wedge signs: `+1` when the mapped
ordered pair agrees with the declared target order and `-1` when it reverses.
The sign is fixed before the transformed Pauli phase is inspected. Results are:

- 15,552 transformed physical columns over all 24 frames and all 27 `L=3`
  anchors, with zero declared-sign or common-slice-phase failure;
- all 576 signed frame-group products, maximum residual zero;
- transitive coverage of all twelve addresses;
- 17,496 transformed columns over all 27 translations and all 27 source
  anchors; and
- all 729 translation-group products, maximum residual zero.

Every column remains in the same local-check, fixed-Wilson, and
`B_v Z_port(v)=+1` constraint space. The full anchor families at training
`L=3,4,5` and held `L=6` contain 648, 1,536, 3,000, and 5,184 columns,
respectively. Gram, action, inverse, constraint, and held-size failures are
zero. The largest floating superposition residual is
`2.220446049250313e-16`.

Deletion controls retain exact scope. Removing catch-up or one stream factor
leaves the declared ray space. The unique active contact projector is the
source/carrier pair; its deletion changes the input by
`|exp(i g)-1|=0.36789306705608243`. Removing one stream-slice column gives
closure residual one, and removing one address gives frame-covariance leakage
one.

## State support versus operator support

A column uses 3--19 M2 relative to the supplied reference. The relative-state
union across one orbit is 42, 46, 50, or 54 M2. That relative-state union is
not operator support.

The complete stream/catch-up product has extensive union `21 L^3` M2, and the
complete contact product has extensive union `15 L^3` face M2. Their locality
is carried by bounded factors: an outer stream/catch-up factor uses 11 M2 and
a complete cell contact block uses 18 face M2. No 54-M2 global update or
preparation circuit follows from the representative census.

## Supplied structure and exact boundary

Load-bearing supplied structure is:

1. one global fixed `+++` Wilson, all-`B=+1`, zero-tag reference ray;
2. one supplied cell anchor and six physical direction labels;
3. the identical-pair wedge convention and graph-edge orientation;
4. six auxiliary port M2 per cell and their local constraints;
5. the Cycle-269 `A/B/FSWAP` and collision-safe catch-up products;
6. the Cycle-230 contact form and coupling `g=0.37`;
7. the Cycle-230 stream-then-contact order and reverse-order comparator; and
8. the training/held split, tolerances, frame, translation, inverse, deletion,
   and lawful-domain fixtures.

The fixed reference is not prepared. The result is fixed-anchor: the family
of translated `E_x` maps is covariant, but no state superposes different cell
anchors. The actual Cycle-219 six-mode coin is not executed on this code. Odd
states, distinguishable source species, larger even sectors, simultaneous
patches, and a full-Fock compiler are absent.

Compiler order and stream slices are not physical time. The coupling and
wrapped phase are not physical energy or a rate. No source, gravity, Record,
occurrence, probability, or Born meaning is attached.

## Updated six-wall dependency ledger

| wall | Cycle-303 movement | still open |
|---|---|---|
| `C_ref` | the fixed `+++` Wilson reference, zero tags, phase origin, and anchor are explicit imports; all relative columns use the same ray | absolute preparation, cross-Wilson equivalence, and physical reference genesis |
| `C_num` | the identical even pair and all twelve perpendicular direction addresses are exact; role reversal does not create species | odd physical state, independent source/species register, full-Fock state |
| `C_wrap` | unchanged because schedule/operator order is not time | event equivalence, recurrent clock, interval and rate calibration |
| `C_int` | materially advanced: contact and stream act separately and in declared order on one coherent 24-column code | coin-closed interaction domain, coupling/resource selection, recoil and dressed-mass ledger |
| `C_local` | materially advanced: one linear `E_x`, exact Gram, coherent directions, constraints, declared frame signs, translations, deletion, and held size coexist | coherent position growth, actual coin on this code, preparation, simultaneous patches, full Fock |
| `C_source` | unchanged; wedge slots and contact phase supply no source law | moving source/response observable, reciprocal response, gravity/clock/tensor bridge |

## TOE lane update

These are evidence-weighted planning estimates, not audit verdicts or
probabilities.

| TOE lane | integrated | strict floor | conditional | maturity | disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 58% | 25% | 81% | 3.0/5 | raised narrowly: one coherent direction orbit now has exact state and two-operator action; position, coin, occurrence, and Record remain open |
| causal time / clock | 33% | 17% | 60% | 1.7/5 | unchanged; slices and operator order are not time |
| inertia / matter | 66% | 29% | 86% | 3.5/5 | raised narrowly: coherent identical-pair transport/contact preserves the coarse mass firewall; odd-state and dressed inertia remain open |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged; no source or response observable is selected |
| Born / probability / realized history | 33% | 14% | 79% | 1.7/5 | unchanged; coherent amplitudes are not promoted to occurrence or probability |

## No-Go Discipline Gate

The scoped candidate negative—“one linear coherent proper-cubic pair orbit
cannot carry exact physical stream and contact restrictions”—is
constructively false on the declared fixed-reference domain.

The candidate broad negative—“no coherent-position or full-Fock compiler can
extend this substrate”—is unsupported. The current result and the constructive
routes below defeat closure of that claim.

**Gate status: FAIL for the candidate broad negative; do not ship it.**

### N1 — alternative routes

| route | marker | disposition and witness |
|---|---|---|
| separately selected localized rays | **ATTEMPTED** | the preceding lift produced exact individual two-column patches; the orbit result shows this was a staging point, not a terminal limit |
| one 24-column orbit isometry | **ATTEMPTED** | exact Gram and complete-basis action succeed at every anchor through held `L=6` |
| unsigned frame permutation | **ATTEMPTED** | it omits exchange signs and therefore does not match the transformed physical pair columns |
| declared signed-wedge frame action | **ATTEMPTED** | all frame columns and 576 group products succeed with the same sign on both slices |
| one common stream/contact restriction | **ATTEMPTED** | both separate intertwiners, the Cycle-230 order, and its reverse comparator have zero matrix residual |
| all-anchor translation family | **ATTEMPTED** | all translations at every `L=3` source anchor and 729 group products succeed, while cross-anchor state superposition remains unbuilt |
| identical-pair role reversal | **ATTEMPTED** | both columns acquire one common minus and retain the same tags, rejecting a false two-species reading |

Seven distinct routes use the exact honesty marker required by the skill. The
successful routes refute the scoped negative. They do not prove the broader
positive compiler, and they prevent a broad no-go from shipping.

### N2 — wall-independence audit

After collapsing state-map and action-on-that-map into one local coin
condition, the remaining set is `W_reference`, `W_coin`, `W_position`, and
`W_fock`. The table audits both closure directions for every pair.

| first condition | second condition | closing first closes second? | closing second closes first? | independent? | reason |
|---|---|---:|---:|---:|---|
| `W_reference` | `W_coin` | no | no | yes | preparing the reference supplies no six-mode coin; a relative coin need not prepare the reference |
| `W_reference` | `W_position` | no | no | yes | one reference ray supplies no address amplitudes; a relative position map can retain a supplied ray |
| `W_reference` | `W_fock` | no | no | yes | reference preparation does not close particle-number sectors; a fixed-reference Fock code can remain relative |
| `W_coin` | `W_position` | no | no | yes | a local direction coin supplies no position encoder; position coherence does not fix the coin coefficients |
| `W_coin` | `W_fock` | no | no | yes | a pair-sector coin need not close higher sectors; a Fock state map does not select the local coin |
| `W_position` | `W_fock` | no | no | yes | one-pair position coherence and simultaneous many-pair closure test different domains |

No condition follows from another in the tested direction table. These are
four independent constructive tasks, not four witnesses for one obstruction.

### N3 — hidden-condition scan

The reference ray, anchor, wedge convention, auxiliary ports, contact coupling,
operator order, sizes, tolerances, and relative-action scope are explicit. The
literal skill-trigger scan reports zero hits in each of the four package paths:
the physical runner, physical note, synthesis runner, and this note. The scan
is a prose guard and supplies no physics premise.

### N4 — residual matching

| file and line witness | witness residual | claimed residual | match? |
|---|---|---|---:|
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:397` | exact Gram and 24-column orbit census | one fixed-anchor coherent orbit | yes |
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:505` | restricted 24-by-24 action semantics | full-Hilbert physical operator | no; dropped from that claim |
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:509` | stream/contact/both-order matrix residuals on `im(E_x)` | coherent stream/contact orbit | yes |
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:802` | declared wedge-sign failures | proper-cubic action on the same orbit | yes |
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:809` | translation group products | coherent superposition across anchors | no; covariance of a family is not a position state |
| `scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py:937` | one-address deletion covariance leakage | load-bearing transitive address set | yes at orbit resolution only |
| `docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COHERENT_CUBIC_PAIR_ORBIT_NOTE_2026-07-17.md:78` | relative-state union versus extensive products | bounded global operator support | no; dropped from that claim |

Only exact orbit-level matches are retained. Gram, covariance, deletion, and
state-support residuals are not pooled into coin, position, full-Hilbert, or
full-Fock evidence.

### N5 — rhetoric and resolution audit

| resolution | tested | not tested; broad negative status |
|---|---|---|
| per representative | exact physical stabilizer/tag ray, support 3--19 M2 | preparation word; no negative earned |
| per address | all twelve perpendicular wedges and both slices | opposite wedges and larger sectors; no negative earned |
| per block | restricted stream, contact, inverse, Cycle-230 order, and reverse-order comparator on 24 columns | actual six-mode coin on this code; no negative earned |
| per anchor | one linear `E_x` at every anchor, tested separately | one state coherent across anchors; no negative earned |
| lattice-wide | extensive products of bounded factors and covariance of the anchor family | full-Hilbert action and autonomous volume update; no negative earned |
| full Fock | not tested | `n=0,1,3,4,5,6`, overlapping patches, and sea state remain open; no negative earned |
| semantics | exact dimensionless phases and compiler order | time, energy, rate, source, gravity, Record, occurrence, Born meaning; no negative earned |

“Coherent orbit” means address amplitudes inside one fixed-anchor 24-column
code. It does not mean coherent position, a prepared state, or a full-Fock
compiler. “Bounded support” applies to representatives and local factors at
the resolutions stated above, not to the extensive product union.

### N6 — partial-closure paths

| constructive path | evidence/status | what it could close |
|---|---|---|
| apply a local matrix-unit coin to the orbit span | the Cycle-302 physical coin artifact supplies an exact bounded matrix-unit mechanism on constrained tag sectors; interface not yet executed here | `W_coin` on a common fixed-reference code |
| enlarge the perpendicular orbit before applying the exterior-square coin | new finite local calculation queued; no constitutional change needed | closure under the actual six-mode coin if perpendicular pairs mix with missing pair addresses |
| form a coherent translated direct sum with local address transport | all-anchor translation matrices and group products already close exactly | `W_position` while retaining the reference import explicitly |
| synthesize or operationally supply the fixed-Wilson ray and audit cross-sector equivalence | current reference rank is exact but preparation is open | retire or narrow `W_reference` |
| add higher-number sectors one at a time with literal constraints and deletion tests | the current even-pair code gives a tested base sector | `W_fock` without assuming a full sea at once |

All are constructive non-axiom paths. None licenses silent new physics, and
none requires axiom language at this stage.

### N7 — hostile steelman

A hostile reviewer should reject any broad obstruction immediately: you
already have one exact 24-column coherent stream/contact code here and an exact
bounded six-mode matrix-unit coin in the Cycle-302 artifact. Put their physical
tag sectors in one finite body-and-neighbor neighborhood, enlarge the wedge
address set if the coin demands it, and solve the common invariant-subspace
equations directly. The current declared-sign representation, collision-safe
ports, and zero-leakage constraints remove the obvious symmetry and ownership
excuses. Until that finite constructive attack fails with matched residuals,
the claim that coin or full-Fock extension is impossible has no support.

This countercase is convincing, so the broad negative is premature.

### N8 — cross-cycle echo

| earlier seam | actual retirement mechanism and witness | status | reuse here |
|---|---|---|---|
| overlapping catch-up swaps | collision-safe XOR catch-up on disjoint half-edge port pairs, `PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md:20-38` | local collision retired | reuse explicit auxiliary sectors before inferring a routing obstruction |
| decoded rays lacked a physical state map | bounded `A`/tag representatives acting on one fixed reference, `PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md:229-239` | localized state seam retired | extend exact columns rather than compare labels |
| coarse contact lacked a physical representative | substitute `n_v=(I-B_v)/2` and keep all fifteen local pairs, `PHYSICAL_CYCLE269_LOCAL_CONTACT_INTERTWINER_NOTE_2026-07-17.md:28-38` | local contact seam retired | compile future number sectors with literal projectors |
| selected localized rays lacked coherent direction amplitudes | collect orthogonal tag sectors into one linear `E_x`, this note and physical runner line 397 | twelve-address coherence retired | use the same exact-Gram mechanism across positions or added wedges |
| frame maps carried exchange signs | compare physical columns to declared wedge signs and verify all group products, physical runner lines 645-801 | proper-cubic sign seam retired | solve future coin-interface phases as a finite representation problem |
| a 54-M2 state census could be mistaken for an operator bound | compute both local-factor and complete-product unions, physical runner lines 375-411 | resolution overclaim retired | keep state, factor, block, and lattice-wide support separate |

The repeated retirement mechanisms are explicit auxiliary structure, exact
state maps, finite representation algebra, and resolution-matched tests. Each
remains available before escalation.

Disposition: **no shared obstruction was identified** and **no axiom pressure
was established**. The coherent orbit is a retained constructive advance; the
remaining conditions are implementation campaigns.

## Optimal next campaign

Compile the actual Cycle-219 coin on the same declared orbit or its smallest
proper-cubic enlargement. Require one common `E` for coin, stream, contact, and
their declared order; distinguish literal state overlap from name matching;
keep the fixed reference in `C_ref`; and test whether opposite pair addresses
or another bounded auxiliary sector are required. Position growth and
reference preparation remain separate campaigns.

## Verification

```text
python3 -m py_compile \
  scripts/physical_cycle269_coherent_cubic_pair_orbit_2026_07_17.py \
  scripts/coherent_cubic_pair_orbit_synthesis_cycle303_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/coherent_cubic_pair_orbit_synthesis_cycle303_2026_07_17.py
```
