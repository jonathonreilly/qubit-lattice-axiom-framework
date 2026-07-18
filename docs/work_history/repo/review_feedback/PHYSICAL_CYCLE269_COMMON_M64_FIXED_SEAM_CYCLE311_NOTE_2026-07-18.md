# Physical Cycle-269 common six-mode M64 fixed seam — Cycle 311

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none

Companion runner:

```text
scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py
```

## Result up front

Cycle 311 constructs one bounded common physical code for every local
six-mode occupation label `n=0,...,6`.  The input is the complete
64-dimensional input code

```text
direct sum from n=0 to 6 of wedge^n(C^6).
```

The fixed-seam unitary closure has one vacuum vector and two comparator slices
for each of the other sixty-three occupation labels.  It is therefore a
127-dimensional seam closure, not a fictitious 128-column isometry:

```text
1 + 2(64-1) = 127.
```

Vacuum input and vacuum output are physically identical.  A separate rank-64
embedding selects the M64 input slice from this closure.

Even sectors use direct fixed-Wilson rays: vacuum for `n=0`, the complete
Cycle-305 pair basis for `n=2`, the Cycle-308 Hodge representatives for
`n=4`, and the filled six-mode ray for `n=6`.  Odd sectors use the Cycle-308
complement-carrier rule uniformly.  An odd logical label `S` is encoded as an
oriented coherent sum over `d` outside `S` of the even physical ray for
`S union {d}` with one outward carrier.  The branch counts are five for
`n=1`, three for `n=3`, and one for `n=5`.

All sectors share one physical ambient coin.  On the logical seam it is the
direct sum of wedge^n(C) on every input slice and identity on every separated
slice.  Literal collision-safe stream/catch-up exchanges the slices.  The
input contact is

```text
exp(i binom(n,2) g),  g=0.37,
```

and contact is identity after separated stream.  With the declared order
coin, then stream/catch-up, then contact, the constrained encoder satisfies

```text
E G_coarse = G_physical E
```

for each component and their composition.  A coherent random vector with
nonzero amplitudes across all sectors has composition residual below
`2.0e-16`; full-matrix intertwiners are below `2.0e-15`.

This is a common fixed-seam compiler.  It is not a number-changing law, not a
recurrent volume update, and not a full-Hilbert compiler.

## Shared-vacuum quotient and literal microbasis

The 127 columns expand into 255 flagged microsectors:

| logical number | seam columns | branches per column | microsectors |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 12 | 5 | 60 |
| 2 | 30 | 1 | 30 |
| 3 | 40 | 3 | 120 |
| 4 | 30 | 1 | 30 |
| 5 | 12 | 1 | 12 |
| 6 | 2 | 1 | 2 |
| total | 127 | — | 255 |

Without the stream-role flag there are 225 physical occupation/tag rays.
Exactly thirty rays occur twice, and all thirty are raw `n=1` input/output
carrier-role exchanges.  Their unflagged 225-by-127 encoding has rank 126 and
Gram operator residual one.  This is an exact collision result for this raw
candidate, not a general negative statement about local encodings.

A local flag `f=t` resolves those literal collisions.  The resulting
255-by-127 map is an isometry.  The flag is not left as supplied logical
metadata.  Add one homogeneous companion M2 `r` and impose the Cycle-306
relational constraint

```text
C_role = K_exchange X_r = +1.
```

Here `K_exchange` is the complete signless physical stream-role exchange on
the 255 flagged microsectors.  The constrained encoder is

```text
E = (E_flag |0>_r + K_exchange E_flag |1>_r) / sqrt(2).
```

The flagged shell has rank 127.  Tensoring it with `r` gives rank 254.  The
bare exchange-`+1` intersection has rank 64, whereas the relationally
constrained intersection has rank 127 and equals `E E^dagger` to residual
`3.01e-15`.  The constraint involution, constraint eigenvalue, shell
commutator, and isometry residuals are zero up to `2.35e-15`.  Thus `r` is a
gauge companion, and `f` is a constrained seam role; neither is a free sector
label.

## No supplied number label

Odd logical sectors carry one additional physical matter occupation and even
sectors do not.  Consequently the pairs with the same physical number are
`n=1/n=2`, `n=3/n=4`, and `n=5/n=6`.  They remain locally distinguishable on
both slices through a relation already present in the matter distribution:

| logical number | physical matter count | body-occupation parity |
|---:|---:|---:|
| 0 | 0 | even |
| 1 | 2 | odd |
| 2 | 2 | even |
| 3 | 4 | odd |
| 4 | 4 | even |
| 5 | 6 | odd |
| 6 | 6 | even |

For odd input columns the logical particles occupy the body and the carrier
is outside; after stream the carrier occupies the body and the logical
particles are outside.  Body parity is odd on both slices.  For direct even
columns body parity is even on both slices.  The executable checks this for
every branch at every anchor for `L=3,4,5,6`.  No extra number register is
present, and body/neighbor parity is tested as relational occupation data,
not called a supplied sector label.

## One common physical update

Let `E_flag` be the 255-by-127 isometry, `P=E_flag E_flag^dagger`, and `K` the
complete logical direct-sum coin comparator.  The flagged ambient coin is

```text
A_K = E_flag K E_flag^dagger + I - P.
```

For every flagged operator `A`, the role-gauge lift is

```text
Phi(A) = A |0><0|_r + K_exchange A K_exchange |1><1|_r.
```

This lift commutes with `C_role` and intertwines on the constrained code.
The same construction is applied to the literal stream permutation and the
physical occupation-counting contact.  At `beta=-0.2,-0.3,-0.4` and held
`beta=-0.35`, coin, stream, contact, and composed residuals are below
`2.0e-15`; coin/composition unitarity and explicit inverse residuals are below
`9.1e-15`.

At nominal `beta=-0.3`, the ambient coin contains 4,152 active off-diagonal
microterms.  Every term preserves physical number, and its Pauli transition
commutes with all inherited `B_v Z_port(v)` constraints, local checks, and
fixed Wilsons.  There are zero number-changing matrix elements.  The dense
matrix-unit coefficients are supplied local structure pending primitive
synthesis; they are not host-side selection during the update.

The input contact phases measured from actual physical cell occupancies are
`exp(i binom(n,2)g)` for all `n=0,...,6`.  Every separated-slice branch has
unit contact.  In particular, the new blocks are vacuum identity,
`exp(i10g)` for `n=5`, and `exp(i15g)` for `n=6` on input.

The complete exterior-power dimensions are `1,6,15,20,15,6,1`.  Every block
is unitary through trained and held beta, and the determinant identities have
maximum residual below `3.3e-15`.  The `n=6` coin is the literal determinant
of the six-mode coin.

## Covariance, translations, held size, and locality

The common logical code carries the complete exterior representation at each
number.  The flagged and role-gauge microbases carry the corresponding signed
permutation.  All 24 proper-cubic frames pass:

- all 576 group products;
- flagged and constrained isometry covariance;
- exchange-constraint covariance;
- ambient coin, stream, contact, and composed-update covariance; and
- logical composed-update covariance.

The maximum floating covariance residual is `1.61e-15`.  All 27 L=3
translations test 6,885 literal branches with zero face-phase or tag failure.
The geometry/Gram/constraint sweep covers all anchors at training `L=3,4,5`
and held L=6, including 216 held encoders.

The bounded patch uses 30, 34, 38, or 42 face M2, twelve collision-safe port
M2, and two role-gauge M2.  It therefore uses at most fifty-six M2.  The
maximum single branch representative uses 45 M2 including roles; the maximum
exchange transition uses 32 M2.  Installed homogeneous overhead is
twenty-three M2 per cell: fifteen face, six port, one `f`, and one `r`.
These bounds are independent of lattice size.  There is no global
Jordan-Wigner order, nonlocal parity service, preferred axis order, or
host-side branch, direction, number, or role query.  The outer fixed-seam
schedule and application remain supplied.

## Leakage, deletion, and lawful-domain controls

Independent destructive controls give:

- deleting the role flag gives Gram operator residual `1` and rank 126;
- deleting `C_role` leaves rank 254 instead of 127;
- the standalone exchange-`+1` selector retains only rank 64;
- deleting one `n=1` carrier branch gives Gram residual `0.2`;
- deleting one `n=3` carrier branch gives Gram residual `1/3`;
- incomplete `n=2,3,4` cubic orbits leak under the coin with norm
  `0.9428090415820635` or larger;
- deleting the largest ambient coin coefficient gives intertwiner residual
  `0.6610601530612619` and unitarity residual `0.8264572537262524`; and
- deleting each nontrivial contact phase for `n=2,...,6` gives residuals from
  `0.36789306705608243` to `1.9225504059505998`.

Repeated or out-of-range labels, a duplicate vacuum slice, invalid sectors or
bodies, malformed/nonfinite coins, and aliased periodic `L=2` are rejected.

## Supplied structure and novelty boundary

Supplied are:

1. the fixed `+++` Wilson, all-`B=+1` reference ray;
2. one body-cell address and six proper-cubic direction labels;
3. the Cycle-269 face dictionary, framing repair, Hodge/insertion signs, and
   outer-edge orientation phases;
4. six zero-initialized collision-safe port M2 per cell;
5. one flag M2 and one `r` gauge-companion M2 per cell;
6. the Cycle-219 six-mode coin coefficient matrix;
7. the Cycle-230 coupling `g=0.37` and coin-stream-contact schedule;
8. the fixed-seam domain, common shell projector, initial lawful code state,
   and dense local matrix-unit coefficients; and
9. preparation of the fixed reference and arbitrary logical/carrier coherent
   amplitudes.

Derived are the single-vacuum 64-to-127 seam quotient, complete `n=0,...,6`
exterior-power blocks, new `n=5,6` physical columns, all physical contact
counts, the raw-collision census, relational number-role separation, the
rank-127 role-gauge code, physical coin/stream/contact/DSK intertwiners,
coherent cross-sector closure, unitarity/inverses, constraint preservation,
frames, translations, held-size closure, support, leakage, deletion, and
lawful-domain controls.

Equivalently, the construction contains 255 flagged microsectors and 510
role-gauge microsectors.  It tests coherent cross-sector superpositions, the
same-physical-number pairs, and thirty raw n=1 collisions explicitly.  The
locally constrained role is not a free sector label.

Exterior powers, auxiliary-fermion encodings, Hodge duality, and bounded
matrix-unit completions are prior-art territory.  Cycle 311 claims only this
explicit common construction and its residuals on the repository substrate.
No global novelty priority is asserted.

The one-particle mass fixture is unchanged at all trained beta and held
`beta=-0.35`, with relative residual at most `3.34e-16`.  Wrapped coin phase is
not called physical energy, contact phase is not called mass, a matrix-unit
generator is not called a rate, and compiler slices are not called time.  No
Record, source, gravity, resource, occurrence, or Born/probability claim is
made.

In contract language: one-particle mass fixture unchanged; no number-changing
law is claimed.

## Exact boundary

The construction is reference-relative and fixed-seam.  Absolute reference
preparation, conditional carrier preparation, arbitrary coherent position,
primitive synthesis of the dense local blocks, overlapping simultaneous
shells, collision arrivals, actual separated-cell onsite recurrence,
number-changing interactions, and a common sea-state compiler remain open.

The identity comparator on a separated slice is not asserted to be the
actual separated-cell onsite coin.  No number-changing or recurrent/full-
Hilbert law has been compiled.  These are implementation and extension
targets, not evidence for a shared substrate obstruction.

There is no broad no-go claim and no axiom pressure.

## No-go discipline gate

The candidate broad negative tested here is: “No bounded local common
fixed-seam M64 code can close without a supplied sector label.”  The gate
rejects it because Cycle 311 is a constructive counterexample on its declared
code space.

**Broad gate status: FAIL / DO NOT SHIP.**  The rank-126 raw unflagged result
is retained only for that exact candidate.  It is not generalized into an
impossibility, minimum-content, or axiom-pressure statement.

### N1 — alternative-route enumeration

| route | honesty | exact disposition |
|---|---|---|
| direct fixed-Wilson even sectors | **ATTEMPTED** | succeeds for complete `n=0,2,4,6` |
| coherent complement carrier | **ATTEMPTED** | succeeds for complete `n=1,3,5` with five, three, and one branches |
| one shared-vacuum seam quotient | **ATTEMPTED** | succeeds with 64 input and 127 independent seam columns |
| raw occupation/tag rays without role data | **ATTEMPTED** | exact candidate has thirty doubled `n=1` rays and rank 126 |
| standalone exchange-`+1` selector | **ATTEMPTED** | retains rank 64 rather than the required 127 |
| one-extra-M2 relational role gauge | **ATTEMPTED** | succeeds with rank 127 and exact local constraint preservation |
| staggered/time-multiplexed role schedule | **OPEN / UNTESTED** | remains a distinct constructive alternative and is not needed for this result |

The five successful or live attacks are enough to make the proposed broad
negative fail.

### N2 — wall-independence audit

The residuals are implementation/extension targets, not claimed
constitutional walls.  Their pairwise implication audit is:

| pair | first closes second? | second closes first? | disposition |
|---|---:|---:|---|
| reference preparation / primitive synthesis | no | no | independent tasks |
| reference preparation / coherent-position preparation | no | no | independent tasks |
| reference preparation / recurrent closure | no | no | independent tasks |
| reference preparation / overlapping shells | no | no | independent tasks |
| reference preparation / number-changing law | no | no | independent tasks |
| primitive synthesis / coherent-position preparation | no | no | independent tasks |
| primitive synthesis / recurrent closure | no | no | independent tasks |
| primitive synthesis / overlapping shells | no | no | independent tasks |
| primitive synthesis / number-changing law | no | no | independent tasks |
| coherent-position preparation / recurrent closure | no | no | independent tasks |
| coherent-position preparation / overlapping shells | no | no | independent tasks |
| coherent-position preparation / number-changing law | no | no | independent tasks |
| recurrent closure / overlapping shells | no | no | independent tasks |
| recurrent closure / number-changing law | no | no | independent tasks |
| overlapping shells / number-changing law | no | no | independent tasks |

No wall is inflated by a downstream duplicate.

### N3 — hidden-condition scan

The fixed reference, body anchor, six directions, orientations, ports, role
M2, constraint candidate, coin, coupling, schedule, shell projector, dense
coefficients, state preparation, sizes, and tolerances are all inventoried.
The prohibited-premise phrase-family scan over the executable release files
has zero hits.  No hidden condition is promoted after the N2 audit.

### N4 — residual matching

| exact witness | witness residual | Cycle-311 use | match? |
|---|---|---|---:|
| `PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md:46` | bounded face/tag matrix units realize one six-mode coin | common ambient matrix-unit grammar | yes |
| `PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md:20` | all fifteen pair labels, including antipodal pairs | complete `n=2` block | yes |
| `PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md:43` | `K_exchange X_r` enforces rather than supplies seam role | common 127-column role constraint | yes |
| `PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md:23` | complement carrier realizes complete `n=3` | uniform odd-sector carrier rule | yes |
| `PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md:25` | direct Hodge representatives realize complete `n=4` | uniform even-sector direct rule | yes |

No prior route failure is cited as a witness for a shared obstruction.

### N5 — rhetoric and resolution audit

| resolution | tested | exact disposition |
|---|---:|---|
| raw physical ray | all 255 occurrences | thirty doubled `n=1` role rays in the unflagged candidate |
| encoded seam column | all 127 | exact constrained isometry; raw rank loss no longer applies |
| M64 input | all 64 basis labels and coherent cross-sector vectors | rank 64 and exact common DSK intertwiner |
| local block | all coin, stream, contact, role-constraint, and composed matrices | bounded fixed-seam closure |
| body anchor and size | every anchor at `L=3,4,5,6` | Gram, occupation, relation, support, and held-size closure |
| proper-cubic/translation orbit | all 24 frames and all 27 L=3 translations | exact local covariance |
| overlapping recurrent lattice | not tested | no negative statement |
| number-changing/full physical Hilbert space | not tested | no negative statement |

The only negative phrase retained is the rank-126 statement about the exact
raw unflagged matrix.

### N6 — partial-closure paths

The local `f+r` relational gauge is the executed partial-closure path: it
retires the free-role import without a convention change or axiom.  The
shared-vacuum quotient retires the fictitious second vacuum column.  The
complete exterior direct sum retires separate supplied number-block
interfaces while leaving physical number encoded in occupation relations.
Primitive synthesis, recurrence, overlaps, and number-changing interactions
remain direct constructive campaigns.

### N7 — hostile steelman

A hostile reviewer should reject the candidate no-go: the claimed missing
sector label is an artifact of looking only at raw tag collisions.  Existing
matter occupation parity already separates every equal-physical-number pair,
and a single local gauge companion turns seam role into a constrained
relation.  Cycle 311 executes the resulting 64-to-127 common encoder and its
510-sector physical update.  Even if this gauge later fails under overlapping
recurrence, the time-multiplexed route remains untested, so there is no
route-independent obstruction.

### N8 — cross-cycle echo

Cycle 302 retired a copied direction reference through an oriented coherent
shell.  Cycle 305 retired incomplete-pair leakage by adding the antipodal
orbit.  Cycle 306 retired a free seam flag through one relational gauge
companion.  Cycle 308 retired the bare-odd-syndrome limitation through a
coherent complement carrier.  Cycle 311 repeats that constructive pattern:
it combines the complete sectors, quotients the shared vacuum, and enforces
the remaining role relation locally.  Past route failures supply no axiom
pressure.

Gate disposition: **FAIL / DO NOT SHIP for the broad negative.**

## Six-wall dependency ledger

| wall | Cycle-311 movement | still open |
|---|---|---|
| `C_ref` | cross-number sectors now share one fixed-Wilson reference-relative encoder | absolute reference genesis/preparation, cross-Wilson equivalence, conditional carrier preparation |
| `C_num` | common `n=0,...,6` M64 input and 127-dimensional fixed seam close; `n=5,6` added; no supplied number label | number-changing interactions, recurrent/full-Hilbert and sea-state compilers |
| `C_wrap` | unchanged; role slices and ordered compiler substeps are not time | physical event equivalence, recurrence clock, interval and rate calibration |
| `C_int` | one ambient direct-sum coin, literal stream/catch-up, and actual `exp(i binom(n,2)g)` contact intertwine on the common seam | separated-cell onsite recurrence, overlapping arrivals, recoil, carrier interactions beyond one step |
| `C_local` | one rank-127 constrained code, 23 M2/cell, at most 56-M2 support, all frames/translations, held `L=6`, leakage and deletions close | primitive one-/two-M2 synthesis, arbitrary preparation/position, simultaneous patches and volume-wide scheduling |
| `C_source` | unchanged; occupations and dimensionless phases are not source data | energy/action/stress observable, source/resource response, gravity/clock/tensor bridge, realized history |

## TOE lane update

These are evidence-weighted planning scores, not probabilities or audit
verdicts.

| TOE lane | integrated | strict floor | conditional | maturity | Cycle-311 disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 61% | 27% | 86% | 3.2/5 | raised narrowly by one coherent common M64 code and local gauge enforcement; Record/occurrence remains open |
| causal time / clock | 33% | 17% | 60% | 1.7/5 | unchanged; compiler order and role slices are not physical time |
| inertia / matter | 71% | 32% | 92% | 3.8/5 | raised by complete local occupation-number coverage and preserved one-particle mass fixture; recurrence and dressed inertia remain open |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged; no source or response observable is selected |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 | current campaign baseline reflects the separate synced Born PR; Cycle 311 adds no probability or occurrence result |
