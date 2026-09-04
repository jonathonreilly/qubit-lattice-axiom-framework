# Dressed-spoke parity gauge — Cycle 273

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset

## Question and disposition

Can matter dressing repair the Cycle-267 reference-spoke parity endpoint so
that a bounded family simultaneously:

- commutes with every spoke and elementary loop;
- has commuting rank `N-1` on `N=L^3` cells;
- is invariant under translations and all 24 proper-cubic frames;
- retains both total-parity sectors at `L=3,4,5,6`;
- preserves the local matter `B/A` algebra, or supplies an exact dressed
  replacement;
- uses constant support and overhead; and
- reaches a common physical encoding and Cycle-230 free/contact/seam
  intertwiner?

Cycle 273 obtains one important positive result and one sharply scoped
remaining conflict.

For direction `d`, let `B=gamma_0...gamma_5` be local chirality and define

```text
P_d = B gamma_d,
D_d = P_d(matter mode d) P_d(reference).
```

Within the declared 19-dimensional one-star Pauli-centralizer quotient,
`D_d` is the unique parity-flipping word supported on the reference register
and matter block `d`.  Its matter factor cancels the exact spoke and
elementary-loop leakage of the Cycle-267 reference-only `P_d` endpoint.
This retires the priority leakage question constructively.

A uniform family `D_d(i)D_d(j)` on every cubic edge is commuting, has rank
`N-1`, preserves both reference parities, and gives exponent `V=6N` after the
three inherited Wilson choices.  It has constant support.  It nevertheless
fixes one gamma direction and fails 20 of 24 frames.  It also makes the
selected original matter `B_d` anticommute with the six equality constraints
incident on its cell, although every original `A` word survives.  A complete
bounded dressed-`B` replacement was not constructed.

The all-frame direction-labelled family removes all spoke/loop leakage, but
its six local endpoints anticommute pairwise.  It has exactly `15N` mutual
constraint anticommutators.  The complete full-star search strengthens this
route-specific statement: among 64 parity-flipping centralizer words fixed by
the stabilizer of one directed axis, no scalar word exists and every six-word
proper-cubic orbit has all 15 pairwise anticommutators.

Treating those `3N` direction-labelled pair words as subsystem gauge
generators is lawful but over-reduces the logical exponent.  Their quartic
plaquette center is commuting and all-frame, but it is parity-even at every
cell and has rank `2N-2`, not `N-1`.

No tested route therefore supplies the complete physical compiler or the
intertwiner

```text
E G_coarse = G_physical E.
```

This is a bounded Pauli/factorized-pair result.  Larger onsite registers,
non-Pauli constraints, overlapping multicell dressings, and broader 2-form
or subsystem constructions remain live.  There is no axiom pressure.

## Lawful domain and inherited code

The executable certificate is

```text
scripts/dressed_spoke_parity_gauge_cycle273_2026_07_17.py
```

The domain is the periodic cubic coarse lattice with `L>=3`.  Sizes
`L=3,4,5` are construction samples; `L=6` is held out.  Every rank is exact
GF(2) or phase-aware Pauli rank.

The explicit size-control label is held-out `L=6`.

The Cycle-267 reference-spoke code has, per cell:

```text
six matter gamma modes             18 M2 factors
one reference gamma mode            3 M2 factors
total                              21 M2 factors
```

Its bounded elementary-loop rank is `14N-2`; adding three supplied Wilson
rows gives rank `14N+1`.  Before auxiliary reduction its exponents are
`7N+2` and `7N-1`.  The full loop code has

```text
P_matter = P_reference,
```

and both signs of reference parity exist.  None of the three Wilson sector
choices is relabelled as a locally enforced constraint.

The local gamma chart remains

```text
gamma_0 = XII   gamma_1 = YII
gamma_2 = ZXI   gamma_3 = ZYI
gamma_4 = ZZX   gamma_5 = ZZY.
```

## Exact one-star symplectic reduction

Take one three-qubit reference register and the six adjacent three-qubit
matter registers.  This is 21 qubits, so raw enumeration would contain
`4^21` Pauli words.  The runner does not perform that search.

It restricts to the star:

- all six spoke words;
- every elementary-loop word intersecting the star; and
- for the matter-algebra control, every original or spoke `A` word
  intersecting the star.

After duplicate restrictions are removed:

| constraint family | distinct restrictions | GF(2) rank |
|---|---:|---:|
| six spokes | 6 | 6 |
| elementary loops | 32 | 17 |
| spoke plus loop union | 38 | 23 |

The symplectic commutation kernel therefore has dimension

```text
42 - 23 = 19,
```

or `2^19=524,288` phase-free centralizer vectors.  Reference-parity flipping
is one nonzero linear functional on this kernel, so exactly `2^18=262,144`
centralizer words flip it.  This quotient enumeration, rather than the raw
physical dimension, is the completeness surface used below.

### Reference-only control

Restricting support to the three reference qubits gives equation rank six and
nullity zero.  Thus there is no reference-only parity flip in the local
centralizer.  This matches Cycle 267's distribution: its 32 reference-only
parity-flipping Paulis leak 1, 3, or 5 spokes.

### Unique one-spoke dressed endpoint

For support on matter block `d` plus the reference, the restricted system has
12 variables, rank 11, and nullity one for every `d`.  Its unique nonzero word
is

```text
D_d = (B gamma_d)_matter,d (B gamma_d)_reference.
```

The support weights for `d=0,...,5` are

```text
6, 6, 4, 4, 2, 2.
```

Each word flips reference parity and commutes with all 38 spoke/loop
restrictions.  The uniqueness claim is only within the declared two-block
restriction of the 19-dimensional star centralizer.

The six `D_d` transform into one another under every proper-cubic frame, with
zero vector-action failures.  At a common cell they form a complete local
Clifford set:

```text
<D_d,D_e>_symplectic = 1, d != e,
```

giving all 15 pairwise anticommutators.

### Full-star dressed control

The stabilizer of one directed axis contains four proper-cubic frames.  The
complete 19-dimensional centralizer contains exactly 64 parity-flipping words
fixed by that subgroup.  Their matter-block support distribution is:

| matter blocks touched | candidates |
|---:|---:|
| 1 | 2 |
| 5 | 14 |
| 6 | 48 |

There is no parity-flipping word fixed by all 24 frames.  For every one of the
64 directed-axis candidates, the six proper-cubic orbit elements have all 15
pairwise anticommutators.  Thus adding more matter blocks inside this one-star
Pauli quotient does not repair the factorized direction-orbit conflict.

This does not cover an operator whose elementary constraint overlaps two or
more stars in a nonfactorized way.

## Uniform one-spoke equality family

Fix one label, say `d=0`, and put

```text
C_ij = D_0(i) D_0(j)
```

on every nearest-neighbor cubic edge.  The words commute because the same
onsite Pauli is used at each incidence.  The cubic incidence span has rank
`N-1`.

| `L` | `N` | base local/full rank | pair rank | local exponent | full exponent | target `V` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 376 / 379 | 26 | 165 | 162 | 162 |
| 4 | 64 | 894 / 897 | 63 | 387 | 384 | 384 |
| 5 | 125 | 1748 / 1751 | 124 | 753 | 750 | 750 |
| 6 held out | 216 | 3022 / 3025 | 215 | 1299 | 1296 | 1296 |

Both reference-parity signs are phase-consistent at every size.  The local
exponent remains `V+3`; exact `V` still consumes all three Wilson rows.

The maximum endpoint support is six qubits and the maximum pair support is
12.  With the inherited period-64 placement, overhead and physical diameter
are constant in `L`.  The macrocell origin, routing, and frame action remain
supplied.

This equality code retains cat order.  The nearest-neighbor product-input
unitary preparation-depth lower bounds at `L=3,4,5,6` are respectively

```text
2, 3, 3, 5.
```

An algebraic code isometry is therefore not being called a bounded physical
encoder.

### Leakage and deletion

The dressed family has exactly zero spoke and elementary-loop
anticommutators.  Deleting its matter factor restores the Cycle-267 formulas:

```text
reference-only pair/spoke leakage       6N
reference-only pair/loop leakage       24N.
```

Deleting all six cubic-edge equalities incident on one cell lowers the pair
rank from `N-1` to `N-2` and creates one extra logical qubit.

### Covariance and matter algebra

The construction is invariant under all translations, but only four frames
fix its directed gamma label.  It fails 20 of 24 proper-cubic frames.

All original matter/reference `A` edge words commute with the new equality
family.  The original matter `B_0` at each cell anticommutes with the six
equalities incident there, giving `6N` exact leakage incidences.  The other
five matter `B` words do not have that particular leakage.  Therefore the
original complete local matter `B/A` algebra is not a codespace algebra for
this route.

The simple product `B_0 B_reference` repairs commutation with the equality but
changes its edge-incidence pattern, so it is not the same six-mode `B` word.
A complete mutually commuting bounded dressed-`B` family with the original
`A` incidence was not constructed.  This is an unfinished algebra compiler,
not a proof that broader dressed replacements do not exist.

## All-frame directional pair family

On a positive-axis bond use `D_(+axis)` at the source and `D_(-axis)` at the
target.  The complete family is permuted by every proper-cubic frame and by
translations.  Matter dressing removes all spoke/loop leakage.

At each cell the six incident constraints contain the six distinct `D_d`.
Every pair anticommutes, giving

```text
15N mutual constraint anticommutators.
```

The `L=3` physical rows have rank 81 before being rejected as commuting
stabilizers.  The route closes covariance and local-code leakage, but not the
commuting-constraint requirement.

## Subsystem and quartic routes

### Directional subsystem gauge

Keep the `3N` noncommuting directional pairs as subsystem gauge generators.
They are independent modulo the full loop code.  Their symplectic Gram rank is

```text
N-1 for odd N,
N-2 for even N.
```

| `L` | `N` | gauge rank | Gram rank | center rank | anticommutators | subsystem exponent | target |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 81 | 26 | 55 | 405 | 120 | 162 |
| 4 | 64 | 192 | 62 | 130 | 960 | 286 | 384 |
| 5 | 125 | 375 | 124 | 251 | 1875 | 561 | 750 |
| 6 held out | 216 | 648 | 214 | 434 | 3240 | 970 | 1296 |

Reference parity remains an independent central label, but the subsystem
quotient removes too many logical degrees to reproduce the six-mode Fock
dimension.  This is not the desired rank-`N-1` auxiliary reduction.

### Quartic plaquette center

Multiply the four directional pair gauges around every elementary coarse
plaquette.  There are `3N` displayed plaquette words.  They commute with one
another, with the base code, and with every onsite reference parity.  Their
rank modulo the base code is exactly

```text
2N-2
```

at all four sizes.  Because each plaquette touches every corner in two
parity-flipping endpoints, it is parity-even cell by cell.  It therefore does
not impose a pairwise parity equality, even if an `N-1` subset of its row span
is selected.  The full all-frame quartic orbit also overconstrains relative
to the desired auxiliary rank.

## Cycle-230 fixture and missing intertwiner

The runner rechecks, without modification:

```text
beta                              -0.3
contact coupling g                 0.37
predecessor rest mass              0.4534056541748851
L=3 principal-sea rank             73
```

This is the unchanged predecessor rank-73 seam fixture.

No tested route simultaneously has all-frame covariance, commuting rank
`N-1`, preserved or exactly replaced matter algebra, and bounded arbitrary
input preparation.  Consequently no common `E` is prepared, and the runner
does not claim encoded free propagation, FSWAP, contact, Cycle-230 seam, mass,
or iteration intertwining.

The predecessor mass and seam numbers are regression fixtures, not evidence
that the dressed gauge implements them.

## Supplied structure

The construction still imports:

1. the Cycle-267 square-pyramid matter/reference-spoke graph;
2. the displayed six-gamma chart and Clifford frame action;
3. three Wilson sector choices for every exact exponent-`V` count;
4. a period-64 macrocell origin and bounded routing;
5. the physical sea/vacuum and initial code state;
6. a preparation operation for cat/equality order;
7. `beta=-0.3`, `g=0.37`, and the Cycle-230 coin/contact data; and
8. the restriction to phase-free Pauli endpoints on one star and factorized
   nearest-cell pair constraints.

No Jordan-Wigner ordering or global parity service is used by the displayed
local constraints.  The Wilson choices and growing cat preparation are
separate explicit imports.

Coherent parity and gauge carriers are code data, not Records.  Circuit
layers, schedule steps, and preparation depth are compiler resources, not
physical time.  No energy, rate, occurrence, source, or realized-history
interpretation is introduced.

## Prior-art boundary

Local higher-dimensional fermion-to-qubit maps, graph-superfast encodings,
and 2-form gauge bosonization are established prior art.  In particular:

- Chen and Kapustin, [*Bosonization in three spatial dimensions and a 2-form
  gauge theory*](https://arxiv.org/abs/1807.07081), keep broader 2-form and
  topological-sector routes live.
- Setia, Bravyi, Mezzacapo, and Whitfield,
  [*Superfast encodings for fermionic quantum simulation*](https://arxiv.org/abs/1810.05274),
  provide the relevant bounded-degree graph-encoding context.

Cycle 273 claims only the exact quotient census and route comparison on this
repository's reference-spoke fixture.  Global novelty is not established.
No result uses the Thirring engine.

## No-go discipline gate

The scoped negative is:

> Within the declared one-star Pauli centralizer and factorized nearest-cell
> pair grammar, no tested family simultaneously supplies commuting rank
> `N-1`, translation/all-frame covariance, both parities, preserved matter
> algebra, bounded preparation, and locally enforced Wilson completion.

It is not a general local-fermionization, subsystem, or multicell no-go.

### N1 — Alternative-route enumeration

| route | marker | exact outcome |
|---|---|---|
| reference-only endpoint | **ATTEMPTED** | no parity-flipping vector in the local centralizer; Cycle-267 leakage distribution reproduced |
| uniform one-spoke dressed equality | **ATTEMPTED** | unique local dressing cancels leakage; commuting rank `N-1` and both parities; 20 frame failures and `6N` matter-`B_0` leakage |
| direction-labelled one-spoke orbit | **ATTEMPTED** | all-frame and zero code leakage; `15N` mutual anticommutators |
| full-star dressed endpoint | **ATTEMPTED** | all 64 axis-stabilized parity flips enumerated; zero scalar flips and every orbit has 15 conflicts |
| directional subsystem gauge | **ATTEMPTED** | lawful gauge family, but subsystem exponents 120/286/561/970 are below target |
| quartic plaquette center | **ATTEMPTED** | all-frame commuting rank `2N-2`; parity-even at every cell |

Larger-register, non-Pauli, nonfactorized two-star, wider multicell, and
measurement-assisted routes are `LIVE / UNTESTED`.  Their live status blocks
any broader no-go.

### N2 — Wall-independence audit

After collapsing endpoint leakage into the algebra wall—it is retired by
`D_d` for the `A`/loop surface—the remaining walls are:

```text
W_C = all-frame covariance of a rank-N-1 commuting equality family;
W_A = a complete codespace matter B/A algebra or exact dressed replacement;
W_P = bounded arbitrary-input preparation;
W_W = local/topological treatment of the three Wilson degrees.
```

| pair | first closes second? | second closes first? | independent? | separator |
|---|---:|---:|---:|---|
| `W_C/W_A` | no | no | yes | uniform pairs close rank/commutation but leak `B_0`; an algebra dressing would not restore the 20 frames |
| `W_C/W_P` | no | no | yes | a covariant stabilizer law can retain cat-order preparation depth; a prepared state need not make checks covariant |
| `W_C/W_W` | no | no | yes | local pair covariance does not choose torus Wilson sectors; supplied Wilson rows do not repair local frame action |
| `W_A/W_P` | no | no | yes | an exact logical algebra need not have bounded preparation; a prepared code need not preserve the coarse algebra |
| `W_A/W_W` | no | no | yes | Wilson selection changes topological rank, not onsite `B/A` incidence |
| `W_P/W_W` | no | no | yes | preparing local equality order does not select Wilson data; supplied Wilson eigenvalues do not prepare the cat input |

No wall follows from another at the tested resolution.  They are work targets,
not proposed axiom sentences.

### N3 — Hidden-wall scan

The phrases and close variants required by the discipline were checked.
Every load-bearing condition is explicit: periodic `L>=3`, the gamma chart,
one-star support, phase-free Pauli words, factorized pairs, unit translations,
the period-64 macrocell, three Wilson choices, product-input unitary
preparation, supplied sea/vacuum, and supplied Cycle-230 values.  “By
construction” is used only for displayed algebra whose rank is rerun.
“Background,” “canonical,” “registered,” “naturally,” “obviously,” and
“standard QFT” supply no proof step.

### N4 — Residual matching

| witness | predecessor residual | Cycle-273 residual/use | match? |
|---|---|---|---:|
| Cycle 267 reference-only census | every reference parity flip leaks at least one spoke | `D_d` adds the exact matter factor and retires this leakage | yes |
| Cycle 267 uniform pair | rank `N-1`, 20 frame failures, `6N/24N` spoke/loop leakage | same rank/frame count; dressing changes leakage to zero but exposes matter-`B_0` leakage | yes, narrowed |
| Cycle 267 directional pair | all-frame, `15N` mutual conflicts, `6N/24N` leakage | same `15N`; dressing retires spoke/loop leakage | yes, narrowed |
| Cycle 267 Wilson ledger | exact exponent `V` needs three extensive rows | full exponent remains `V`, local exponent remains `V+3` | yes |
| Cycle 267 cat preparation | equality order has growing product-input unitary depth | same `2,3,3,5` lower-bound sequence | yes |

Cycle 268/272 covariance results are context only; their reference-pair and
orientation-carrier residuals are not used as authority for this distinct
dressed-spoke centralizer claim.

### N5 — Rhetoric and resolution audit

- “Unique one-spoke dressing” means the nonzero solution in each declared
  reference-plus-one-matter-block restriction, not uniqueness in all Pauli
  codes.
- “No scalar parity flip” means the complete 19-dimensional phase-free Pauli
  centralizer on one star; signs do not change symplectic commutation.  It does
  not cover non-Pauli unitaries or larger support.
- “Every orbit conflicts” means all 64 directed-axis-stabilized candidates in
  that quotient with factorized pair constraints.  A nonfactorized multicell
  constraint was not tested.
- Rank, parity, deletion, subsystem, and quartic claims are lattice-wide at
  `L=3,4,5,6`; only `L=6` is held out.  They are not continuum theorems.
- “Matter algebra not preserved” refers to the literal original `B_0` under
  the uniform family.  No universal dressed-algebra impossibility is claimed.

### N6 — Partial-closure path scan

The cycle retires real imports without constitutional change:

1. matter dressing closes spoke and elementary-loop leakage exactly;
2. the uniform route closes rank, both parities, translation covariance,
   bounded support, deletion, and full-sector exponent;
3. the direction-labelled route closes proper-cubic covariance and local-code
   leakage;
4. the subsystem calculation gives the exact Gram/center/exponent disposition;
5. the quartic calculation isolates a commuting all-frame center and shows
   why it is the wrong parity operator.

The next constructive paths are a nonfactorized two-star centralizer, a
larger onsite Clifford register, a subsystem selection with a rank-`N-1`
parity-changing center, or a 2-form treatment of Wilson data.  None requires
an axiom conclusion at this stage.

### N7 — Steelman

A hostile reviewer should reject any broader negative: the one-star theorem
forces a Clifford conflict only when a bond constraint factorizes into one
parity-flipping endpoint at each cell.  A two-star or plaquette-supported
Pauli can overlap neighboring constraints at two cells, canceling local
anticommutators without factoring through the six `D_d`; a larger reference
register can contain a scalar parity-flipping centralizer; a non-Pauli gauge
can evade the phase-free Pauli quotient; and a selected subsystem center may
remove only `N-1` auxiliary degrees while treating Wilson sectors as lawful
2-form data.  These routes are supported in broad concept by 3D bosonization
and graph-superfast encoding prior art and were not exhausted here.  This
steelman is decisive, so Cycle 273 remains a partial narrowing.

### N8 — Cross-cycle echo

Cycle 245 is a direct warning against broad closure: a marked-charge/common-
Wilson gauging route constructed an exact odd-sector state isometry while
leaving ordinary-M2 CAR and preparation open.  Its mechanism—enlarge the
gauge/resource contract and keep Wilson data explicit—remains available to a
future subsystem or 2-form treatment here.

Cycle 267 located unavoidable leakage only for reference-only endpoints.
Cycle 273 retires that exact residual with `D_d`, demonstrating why a
route-specific failure was not constitutional evidence.  The obstruction has
moved from local-code leakage to the joint covariance/commutation/algebra
contract.  Cycle 261's three Wilson degrees remain separate; Cycle 230's mass
and seam remain predecessor fixtures.  The same pattern may recur: a wider
local law could retire the present factorized-pair conflict.  There is no
shared substrate obstruction and no axiom pressure.

Gate status: **PASS for the scoped one-star Pauli/factorized-pair negative;
FAIL for any broader no-go.**

## Six-wall ledger and maturity

| wall | Cycle-273 change | residual |
|---|---|---|
| `C_ref` | unique one-spoke dressing and complete 19-dimensional star census | macro origin, frame action, cat preparation, sea/vacuum supplied |
| `C_num` | uniform dressed family gives rank `N-1`, both parities, exponent `V` with Wilson rows | uniform route loses 20 frames and original `B_0`; all-frame route is noncommuting |
| `C_wrap` | Wilson increment remains exactly three and separate | no locally enforced/topological preparation of the three sectors |
| `C_int` | all original `A` words and predecessor mass/contact values preserved diagnostically | no complete matter `B/A` replacement, common `E`, free/contact/seam update, or iteration intertwiner |
| `C_local` | constant 21-M2 overhead, endpoint/pair support at most 6/12, exact deletion and held-size controls | bounded arbitrary-input encoder and successful all-frame commuting family absent |
| `C_source` | unchanged | no energy, action, stress, source, or gravity law selected |

Campaign-wide maturity is not recomputed from this one route-specific probe.
The Cycle-270 reconnaissance baseline remains:

| lane | integrated maturity | strict substrate floor | conditional bridge maturity |
|---|---:|---:|---:|
| operational quantum / Records | 42% | 18% | 63% |
| causal time / clock | 32% | 17% | 58% |
| inertia / matter | 58% | 24% | 77% |
| gravity / source / resource | 34% | 12% | 58% |
| Born / probability / realized history | 30% | 14% | 74% |

These are planning estimates, not probabilities or audit verdicts. The first
column is the primary campaign percentage; the second counts only current
physical-substrate closure without silently selecting a candidate law; the
third grants every named import.

## Next campaign

The highest-value next object is a **two-star nonfactorized symplectic
centralizer**:

1. include two neighboring reference stars and their shared/coarse-neighbor
   matter endpoint blocks;
2. quotient by all overlapping spoke, elementary-loop, and local matter-`A`
   restrictions;
3. search bond words that flip parity at both cells but do not factor as
   `D_left D_right`;
4. demand that the complete translation/proper-cubic orbit commute at both
   one-cell and two-cell overlaps;
5. compute rank, parity sectors, algebra, deletions, and held-out sizes before
   considering Cycle-230 synthesis.

Only if that closes should the campaign synthesize the actual free coin,
FSWAP, contact, and seam block and test `E G_coarse=G_physical E`.
