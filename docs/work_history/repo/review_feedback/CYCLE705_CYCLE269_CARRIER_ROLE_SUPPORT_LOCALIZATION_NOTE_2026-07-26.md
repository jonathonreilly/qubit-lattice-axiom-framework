# Cycle 705 Cycle-269 carrier/role support-localization attack — 2026-07-26

Authority: none

Audit: unset

## Scope and disposition

This checkpoint attacks Route C on the physical graph that was actually
landed in Cycles 269, 311, and 315.  It does **not** treat the seven-mode K7
encoder of Cycle 655 as a physical-site compiler.  Cycle 655 supplies only the
38-factor decoded target word.

**Correction / supersession.**  This note supersedes the earlier exploratory
reading that a four-cell “2x2” fixture was isometric.  That prototype's first
four cells were not the literal closed square.  Reconstructing the exact
square coordinates exposes six overlaps immediately.  All dispositions below
use the corrected literal `2x2` and the held `3x3` replication; the earlier
isometry reading must not be reused.

The strongest constructive result is:

- the phase-aware Cycle-311 carrier/port/flag/r state map is an exact isometry
  on a three-cell L-shaped tree at total `n<=2`;
- the same physical substrate has exact full-Fock capacity for one cell
  (`2^6=64`) and two adjacent cells (`2^12=4096`), so the result is not a
  claim that this graph realizes only `n<=2`;
- every matter-edge `Ahat/B` FSWAP summand on the actual graph has support at
  most 11 M2 and commutes with all inherited local port constraints;
- the local Cycle-230 contact is exact on every carrier branch and through the
  Cycle-311 role-gauge lift;
- the one-cell common state map is exact under all 24 proper-cubic frames, all
  576 frame products, and all 27 `L=3` translations; and
- the Cycle-219 one-particle mass fixture remains
  `m=0.4534056541748851`, with uniform-state residual
  `3.88950e-16`.

The support-local compiler does not close.  Two independent defects are
explicit:

1. the raw tensor-product common state map first ceases to be an isometry on
   a closed `2x2` plaquette, with six off-diagonal Gram overlaps of magnitude
   `1/400`; the held `3x3` repeats that exact six-overlap motif on each of its
   four elementary plaquettes; and
2. the bounded matter-only `Ahat/B` FSWAP candidate preserves all direct
   even-number code sectors but already has the wrong decoded action there;
   it also leaks the odd carrier rays and 56 of 64 columns of the actual
   constrained role-gauge input code.  On the two-cell total-`n<=2` seam it
   leaks 58 of 79 columns.

Consequently no physical `G_physical` satisfying

```text
E G_coarse = G_physical E
```

has been constructed for the Cycle-655 target word on recurrent physical
patches.  A dense projector completion and a 24-block held-size Gram whitener
close their algebraic diagnostics, but both are target-fit constructions and
are not accepted physical laws.  This is a route-specific failure, not a
shared substrate obstruction.  The broad impossibility gate fails and there
is no axiom pressure.

## Exact target contract

| Field | Contract |
|---|---|
| Target statement | construct one bounded-overhead local state map `E` and bounded physical update on the Cycle-269/311/315 graph that exactly intertwine the Cycle-655 decoded free-plus-contact word |
| Domain | recurrent six-mode cells; full `6N`-mode Fock space is the final target; `n<=2` is an explicitly weaker probe domain |
| Allowed premises | landed Cycle-269 graph/checks/Wilsons, Cycle-311 port/flag/r shell, Cycle-315 reference reducer, Cycle-219 coin, Cycle-230 contact, Cycle-655 decoded target factors |
| Forbidden weakenings | K7 as physical substrate, global Jordan-Wigner order, nonlocal parity service, host branch selection, dense target-fit completion counted as local physics, program order called physical time |
| Edge cases | vacuum, all number sectors locally and on two cells, L tree, closed `2x2`, held `3x3`, internal and outer seams, translations, 24 frames and 576 products, deletion and leakage |
| Completion witness | exact Gram, local constraints, bounded individual summands, shared-register consistency, contact and seam action, mass fixture, covariance, and exact recurrent intertwiner |
| Non-closure outcomes | a local or two-cell dense lift, a whitened finite Gram matrix, an operator algebra without a preserved code, or a state map without a physical update |

The tested narrow claim is only that the declared raw common `E` and declared
bare `Ahat/B` physical word fail on the listed fixtures.  No quantifier over
all local gauge extensions is introduced.

## Reconstructed physical substrate

For `N=L^3` coarse cells the Cycle-269 square-pyramid dual graph has:

- `6N` matter vertices;
- `12N` internal triangular-face M2 and `3N` shared outer-square M2, hence
  `15N` face M2;
- degree five at every matter vertex;
- `8N` triangle and `3N` octagon elementary checks, rank `9N-2`;
- three Wilson rows, leaving fixed-Wilson reference exponent `6N-1`; and
- the `6N` matter `B_v` rows, which together with local checks and Wilsons
  select a unique reference ray.

The runner rebuilds these ranks at `L=3` and held `L=6`:

| `L` | `N` | face M2 | local checks / rank | fixed-Wilson exponent | fixed-Wilson-plus-`B` exponent |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 405 | `297 / 241` | 161 | 0 |
| 6 | 216 | 3,240 | `2,376 / 1,942` | 1,295 | 0 |

The Cycle-311 extension installs per coarse cell six port M2, one stream-role
flag `f`, and one companion `r`, for `15+6+1+1=23` physical M2 per cell on a
periodic volume.  The six local constraints are

```text
B_v Z_port(v) = +1.
```

The relational role constraint is

```text
C_role = K_exchange X_r = +1.
```

On one cell its flagged shell has 255 microsectors, the role-gauge shell has
510, the shared-vacuum seam code has dimension 127, and the physical input
rank is 64.  The constraint involution, eigenvector, and Gram residuals are
respectively `0`, `0`, and `2.34990e-15`.  No free number-register label is
introduced.

This graph is the common-`E` substrate.  Cycle 655 contributes the following
decoded target census only:

| Factor | Count |
|---|---:|
| coin phase | 1 |
| coin Givens | 10 |
| reverse FSWAP | 3 |
| seam FSWAP | 9 |
| contact phase | 15 |
| **total** | **38** |

## Phase-aware state-map attack

The raw patch map multiplies the actual Cycle-311 local carrier/role rays in a
declared cell order.  Exact Pauli phases are reduced against the unique
fixed-Wilson-plus-matter reference.  The local `r` companion is put in its X
basis so vacuum spectators do not create a fake `2^N` enumeration.  No
amplitude is dropped.

| Fixture | Cells | Logical dimension (`n<=2`) | Physical rows / nonzeros | max `|E†E-I|` | Shared rows | Pair collisions |
|---|---:|---:|---:|---:|---:|---:|
| L triomino | 3 | 172 | `43,741 / 43,741` | `1.04361e-14` | 0 | 0 |
| closed `2x2` | 4 | 301 | `87,115 / 87,121` | `0.0025` | 6 | 6 |
| held `3x3` | 9 | 1,486 | `519,997 / 520,021` | `0.0025` | 24 | 24 |

Thus the first state-map defect is loop-local rather than a generic
large-volume growth.  On each elementary four-cell plaquette, the six
collisions come in two direction-mode copies of the three pairing identities

```text
(a,b) <-> (c,d),
(a,c) <-> (b,d),
(a,d) <-> (b,c),
```

with overlap signs `(+,+,-)` and magnitude `1/400` per direction-mode copy.
The held `3x3` has four elementary plaquettes, producing 16 positive and 8
negative overlaps.  Reversing the complete cell multiplication order leaves
the same 24 logical collision pairs and the same maximum residual.  This
rules out that one phase-order reversal; it does not rule out a different
local gauge.

The exact inverse-square-root repair has 24 independent size-two blocks,
touches 48 logical columns, and changes the Gram eigenvalues
`0.9975,1.0025` to one with residual `1.55431e-14`.  Its 1,534-nonzero
whitener is reported as a dense/target-fit diagnostic only.  It is not a
physical preparation, constraint, or update.

Deleting one carrier coefficient on the `2x2` probe produces Gram residual
`0.05`, so the normalization control is sensitive to the actual branch data.

## Bounded physical-word attack

For a physical graph edge `(u,v)`, define the inherited port-preserving even
generator

```text
Ahat_uv = A_uv X_port(u) X_port(v)
```

and the standard abstract FSWAP polynomial candidate

```text
F_uv = (B_u + B_v + i B_u Ahat_uv - i B_v Ahat_uv)/2.
```

The runner exhausts all 405 physical edges on `L=3`.  Every individual Pauli
summand commutes with every port constraint.  The maximum summand support is
10 M2 on an internal triangular face and 11 M2 on an outer square face.  This
is a genuine bounded-support even-algebra result on the actual graph, not a
K7 or path-chord surrogate.

The state-map compatibility result is negative for this word:

| Input map / sector | Leaky columns | Maximum leakage probability | Target-intertwiner Frobenius residual |
|---|---:|---:|---:|
| raw direct `n=0` | 0 of 1 | 0 | 0 |
| raw direct `n=2` | 0 of 15 | 0 | 4.89898 |
| raw direct `n=4` | 0 of 15 | 0 | 4.89898 |
| raw direct `n=6` | 0 of 1 | 0 | 0 |
| raw carrier `n=1` | 2 of 6 | 0.84 | 2.36643 |
| raw carrier `n=3` | 12 of 20 | 1 | 5.65685 |
| raw carrier `n=5` | 2 of 6 | 1 | 2 |
| constrained role-gauge full M64 | 56 of 64 | 1 | 10.73313 |
| constrained two-cell outer seam, total `n<=2` | 58 of 79 | 1 | 8.24621 |

The local full-M64 FSWAP intertwiner Frobenius residual is
`10.7331262920`; the two-cell outer-seam residual is `8.24621125124`.
Physical output norms remain unitary to `3.34e-16`, so this is code leakage,
not a malformed Pauli polynomial.  Deleting the last `B Ahat` summand gives
norm residual `0.75`.

The phase-aware audit also scans all four coefficient/orientation conventions
`+1,-1,+i,-i` for `Ahat`.  The best case is `-1`, but it still leaks 52 of 64
constrained columns and has target residual `9.23760430703`; the other three
leak 56 columns.  Thus the retained failure is not an untested quarter-turn
phase convention.  This finite scan does not exclude a different
carrier-aware operator dressing.

This separates three facts that were previously easy to conflate: the actual
matter graph realizes bounded even operators; preservation of a code sector
does not imply the correct decoded action; and the landed carrier/role state
map is not invariant under the bare operator representation.  Rephasing
columns cannot repair leakage outside the code projector.

The local contact is different.  The physical occupation-count phase equals
`exp(i binom(n,2) g)` on every input carrier branch, equals one on the
separated stream slice, and its role-gauge-lift intertwiner residual is
exactly zero for `g=0.37`.  The contact therefore survives this attack; the
free/seam factor does not.  Since one essential FSWAP factor fails, the full
38-factor target composition is not claimed.

The algebraic completion

```text
G_fit = E F E† + (I - E E†)
```

is unitary and intertwines exactly on the 64-column local code, but it is a
dense target-fit shell operator.  It does not meet the bounded individual
summand or law-generation contract and is not counted as a constructive
compiler.

## Full-Fock, covariance, mass, and lawful-domain boundary

The exact Cycle-315 two-cell map was rerun on every number sector:

```text
1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1.
```

These sum to 4,096.  The sparse physical encoding has shape
`63,488 x 4,096`, 65,536 nonzeros, and Gram residual
`1.77636e-15`.  Therefore it would be incorrect to call `n<=2` the capacity
of the actual graph.  The exact statement is: full Fock closes for one and
two cells; this Cycle-705 recurrent patch attack only constructs a raw common
map on the L tree at `n<=2`, and full Fock on L/`2x2`/`3x3` remains
unconstructed.

For covariance, the one-cell phase-aware common map has zero branch,
flagged-map, and constrained-map residual under all 24 proper-cubic frames.
All 576 representation products close exactly.  All 6,885 translated branch
tests across the 27 `L=3` translations pass.  The plaquette collision is
expressed as the full three-pairing orbit on a square and is therefore a
covariant defect, not a repaired compiler.  No claim of recurrent covariant
success is made.

The lawful domain fixes local checks, the three reference Wilson signs, all
six port constraints, and the relational role constraint.  The runner tests
constraint commutators, state-map Gram matrices, physical leakage, coefficient
and summand deletions, train versus held host sizes, order reversal, all number
sectors on two cells, and exact mass/contact fixtures.

The six local port constraints have rank six; deleting any one lowers their
rank to five and admits the corresponding unlawful binary sector.  The
role-constrained shell has rank 127, while removing `C_role` doubles the
admitted flagged role shell to rank 254.  Five malformed calls—number 7,
stream slice 2, two-cell number cutoffs `-1` and 13, and aliased periodic
host `L=2`—are all actively rejected.  These controls distinguish a lawful
code-space result from an ambient-shell coincidence.

## Supplied structure and novelty boundary

Supplied rather than derived:

1. the Cycle-269 periodic proper-cubic graph, local face order, local checks,
   and three fixed Wilson signs for the reference reducer;
2. the Cycle-311 carrier superpositions over unoccupied odd-sector
   directions, six port M2, flag `f`, companion `r`, and role constraint;
3. the fixed cell multiplication order, plus the explicitly tested reverse;
4. the Cycle-219 `beta=-0.3` coin and the Cycle-230 coupling `g=0.37`;
5. the Cycle-655 decoded 38-factor word;
6. `L=5` periodic placements for train patches and `L=6` for held `3x3`;
7. exact real/complex coefficients and the fixed reference-vacuum phase
   convention; and
8. for diagnostics only, the target-derived Gram whitener or dense projector
   completion.

Not supplied: a global Jordan-Wigner string, nonlocal parity service, K7
physical encoder, host-side carrier branch selector, or physical-time meaning
for the factor sequence.  No pointer copy is called a Record, no generator
element is called a rate, and no wrapped phase is called physical energy.

The new result is a finite exact computational characterization of this
specific landed carrier/role substrate: first-loop Gram collisions, their
plaquette pairing structure, and the carrier-code leakage of the actual
bounded matter-edge word.  It is not a literature priority claim and does not
establish minimum physical content.

## TOE dependency effect

| Wall | Cycle-705 effect |
|---|---|
| `C_ref` | sharpened, not retired: fixed Wilsons, `B` reference rays, carrier branches, flags, and `r` are explicit; the first closed plaquette exposes a missing local consistency datum or gauge |
| `C_num` | improved locally: full one- and two-cell Fock sectors are exact; recurrent L/plaquette/volume full Fock remains unconstructed, and the growing-patch probe is only `n<=2` |
| `C_wrap` | unchanged: multiplication order and the 38-factor sequence are compiler order, not causal time or realized winding history |
| `C_int` | split result: the local Cycle-230 contact is exact, while the free/seam FSWAP word leaks the actual common code |
| `C_local` | sharpened: all elementary physical summands are bounded and constraint preserving, but raw `E` fails on the first plaquette and no carrier-aware bounded update closes |
| `C_source` | unchanged: no conserved physical energy/stress/source ledger is constructed |

The calibrated TOE maturity scores remain unchanged:

| Lane | Score |
|---|---:|
| operational quantum / records | 2/5 |
| time / clock | 1/5 |
| inertia / matter | 3/5 |
| gravity / source | 2/5 |
| Born / probability | 1/5 |

This probe strengthens the operational/matter dependency map but does not
construct occurrence, irreversible Record semantics, causal time,
gravity/source selection, or Born weights.

## No-go-discipline N1-N8 gate

The fresh `origin/main` no-go-discipline skill and its proof-search-governance
normalization were applied.  User instruction forbids editing registries in
this campaign, so the route-family registry is recorded here rather than in
`APPROACH_REGISTRY.md`.

Gate status: **FAIL / DO NOT SHIP the broad negative.**

The only retained negative is:

> The raw fixed-order Cycle-311 carrier product is not an isometry on the
> tested closed plaquettes, and the bare `Ahat/B` word does not preserve the
> tested Cycle-311/315 carrier-role codes.

### N1 — normalized alternative-route enumeration

Families are distinguished by mathematical object, load-bearing mechanism,
and terminal obligation rather than artifact name.

| Family | Object / mechanism / terminal obligation | Strength | Status | Concrete evidence / reopen condition |
|---|---|---|---|---|
| raw carrier product plus bare even word | tensor product of Cycle-311 rays / fixed carrier superposition and `Ahat,B` algebra / recurrent intertwiner | target-equivalent | **blocked-local** | L Gram closes; `2x2` and `3x3` collide; local and outer FSWAP leak. Reopen only with a new carrier-aware dressing or state map |
| local dense role-gauge lift | finite shell projector / conjugation by exact encoded target / bounded physical decomposition | weaker | **provisional** | Cycle 311 and the present `G_fit` close locally, but locality/law generation is the terminal unsolved obligation |
| plaquette collision whitener | inverse square root of local Gram blocks / six-pairing square correction / compatible all-volume local isometry | unknown/comparable | **provisional** | exact `2x2` and held blocks exist; reopen by replacing the target-fit matrix with one plaquette gauge constraint and proving overlap consistency |
| joint permutation-role gauge | joint `S_k` orbit shell / relational role qubits / shared-register recurrent update | weaker | **provisional** | Cycles 319/324/330 close finite `n<=2` stars; arbitrary overlap and full Fock are terminal obligations |
| local plaquette/edge sign gauge | local Z2 incidence field / holonomy cancels square pairings / local constraints plus carrier-aware update | target-equivalent | **unexplored** | no Cycle-705 construction; the six-pairing plaquette residual is a concrete input |
| alternative auxiliary-Majorana even code | different bounded block algebra / encoded local parity rather than complement carriers / exact recurrent common `E` | target-equivalent | **unexplored** | not tested on the Cycle-269 installed registers |
| staggered or time-multiplexed code | slot-labelled local code / returned-work covariant schedule / exact macrostep without preferred physical frame | target-equivalent | **unexplored** | no physical schedule, covariance proof, or leakage test was built here |
| larger-patch full-Fock role code | `2^(6N)` joint shell / overlap-aware relational roles / L, `2x2`, and `3x3` full-Fock intertwiner | target-equivalent | **unexplored** | exact full one/two cell is the base; no three-cell full-Fock construction exists |

Five target-equivalent families remain unattempted or only locally
provisional.  Therefore N1 alone blocks a general impossibility or
minimum-content claim.

### N2 — condition-independence audit

The actual remaining conditions are:

- `W_state`: raw common-`E` Gram collision on closed plaquettes;
- `W_operator`: carrier/role-code leakage under the bare even word;
- `W_full-number`: no recurrent full-`6N` Fock map beyond two cells;
- `W_locality`: dense gauge lifts and whiteners lack bounded physical
  realization;
- `W_order`: the common product still supplies a cell ordering; and
- `W_schedule`: no autonomous staggered returned-work macrostep.

They are not one wall.  `W_state` and `W_operator` are independent because the
L map is isometric while the local FSWAP already leaks, and the direct even
sectors are invariant while the constrained state map is not.  The whitener
solves the tested `W_state` diagnostic without solving `W_operator` or
`W_locality`.  Full two-cell Fock solves neither recurrent number nor
plaquette consistency.  Reversing order leaves `W_state` but does not test a
local gauge that removes order.  Exact 24-frame one-cell covariance does not
solve any of these extension walls.

### N3 — hidden-wall scan

Explicit supply includes reference Wilson signs, reference `B` eigenvalues,
carrier amplitudes, ports, `f/r`, the role constraint, cell order, exact target
factors, `beta`, `g`, periodic host and placements, and diagnostic target
matrices.  The physical preparation of the fixed reference, genesis of the
role sector, full-volume constraint compatibility, autonomous factor
schedule, and full-Fock recurrent domain are not derived.  No success is
silently upgraded from `n<=2`, one cell, two cells, or a dense shell.

### N4 — residual matching

The runner reproduces the landed structural invariants: `15N` face M2,
local-check rank `9N-2`, 23 installed M2 per cell, 255/510 role shells,
rank-64 local input, rank-4096 two-cell input, all 24/576 covariance checks,
Cycle-219 mass, Cycle-230 contact, and the Cycle-655 38-factor census.  The
new residuals are matched across resolutions: six `1/400` overlaps on one
`2x2`; four copies and 24 overlaps on held `3x3`; identical pairs under order
reversal; local constrained FSWAP leakage in 56/64 columns; outer seam leakage
in 58/79 columns; and residual at least `9.2376` under the four phase/orientation
choices.  These are not the path-chord support residuals of Cycle 703 and are
not evidence about the K7 target encoder.

### N5 — resolution and rhetoric audit

Resolutions tested are one cell full M64, two cells full `2^12`, an L tree at
`n<=2`, literal `2x2` at `n<=2`, held `3x3` at `n<=2`, all actual graph edges,
one local internal FSWAP, one actual outer seam, 24 frames, 576 products, and
27 translations.  Not tested are L/`2x2`/`3x3` full Fock, arbitrary volume,
an infinite lattice, autonomous preparation, or every possible local gauge.
Accordingly “fails this raw map/word” is admissible; “the substrate cannot
compile CAR” is not.

### N6 — partial-closure paths

Positive islands remain large: full local and two-cell Fock state capacity;
exact L-tree common `E`; bounded, port-preserving even-algebra summands;
exact contact; exact local covariance; exact dense shell completions; and
local size-two Gram repair blocks.  These are direct construction paths, not
near-misses erased by the failure.  In particular, a plaquette role/gauge may
turn the observed local collision into a locally enforced relation, and a
carrier-aware dressing may preserve it under `Ahat/B`.

### N7 — steelman

The strongest actionable next attempt is a **plaquette-incidence role gauge**:

1. add or identify one bounded Z2 role datum for each elementary coarse
   plaquette, with a local stabilizer tying it to the four incident carrier
   branches;
2. assign its two values to the two physical rays in each of the six observed
   collision pairs, so the raw `2x2` Gram matrix is exactly diagonal without
   an inverse-square-root fit;
3. test simultaneous shared-edge consistency on the four overlapping
   plaquettes of `3x3`, then on a held cube, before fitting any update;
4. dress `Ahat_uv` by only the incident plaquette-role operators and require
   zero leakage for local full M64 and the two-cell outer seam;
5. demand that the same algebraic rule transports under all 24 frames and all
   576 products, with no fixed exterior ordering; and
6. only after state and operator closure, run the full 38-factor target and
   full-Fock held-size controls.

This is not “try more auxiliaries.”  It targets the measured four-cell
pairing invariant with a bounded incidence object and has an immediate
falsifier: inconsistent role assignment on two adjacent plaquettes or
nonzero dressed-FSWAP leakage.

### N8 — cross-cycle echo

Cycle 235 exposed the closed-face parity boundary of the even algebra; Cycle
269 retained the Wilson-subsystem graph; Cycle 311 repaired a one-cell
carrier-role collision; Cycle 315 achieved full two-cell overlap-aware Fock;
Cycles 319/324/330 supplied increasingly joint finite `n<=2` role shells; and
Cycle 703 produced open-BKSF/local-plaquette decoders and rephase/cohomology
routes.  Those are multiple retirement mechanisms, not repeated proof of one
obstruction.  The present first-plaquette collision is precisely where a
Cycle-311 cell role may need a Cycle-703-style plaquette incidence relation.
Cycle 655 remains a target-word baseline only.  There is no cross-cycle echo
supporting a constitutional no-go.

## Route-C disposition and next retasking

Route C on the literal Cycle-269/311/315 substrate is **not closed**:

- **constructive:** bounded physical even summands, exact contact, exact
  L-tree state map, exact full one/two-cell Fock, exact local covariance;
- **falsified candidate:** fixed-order raw carrier product plus bare `Ahat/B`
  word;
- **diagnostic only:** collision-block whitener and dense projector lift;
- **not tested:** plaquette-incidence gauge, alternative auxiliary-Majorana
  block, staggered macrostep, and full-Fock multi-plaquette role code.

The optimal next Route-C campaign is the N7 plaquette-incidence role gauge,
because the failure has become a local six-pairing square invariant with an
exact held-size replication and a direct leakage falsifier.  No axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit-status
file was changed.

## Reproduction

Runner:

```text
scripts/frontier_cycle705_cycle269_carrier_role_support_localization_2026_07_26.py
```

Cached output:

```text
logs/runner-cache/frontier_cycle705_cycle269_carrier_role_support_localization_2026_07_26.txt
```

Expected terminal line:

```text
SUMMARY pass=21 fail=0
```
