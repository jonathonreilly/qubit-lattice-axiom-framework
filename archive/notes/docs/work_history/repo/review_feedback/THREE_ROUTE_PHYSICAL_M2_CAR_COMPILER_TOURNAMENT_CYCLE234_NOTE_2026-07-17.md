# Three-route physical-`M_2` CAR compiler tournament — Cycle 234

**Date:** 2026-07-17

**Type:** adversarial tournament synthesis with conditional constructions and
named residuals

**Status:** no route satisfies the full local-encoding contract; strongest
result is an odd-volume sectorwise even-algebra representation with bounded
physical update gates

**Authority:** none

**Audit:** unset

**Constitutional effect:** none

**Packaging:** existing draft PR #5389 on the parking branch only

Companion runner:

```text
scripts/three_route_physical_m2_car_compiler_tournament_cycle234_2026_07_17.py
```

This synthesis changes no foundation, axiom, Qualification, primitive,
registry, policy, queue, or audit surface.

## Result up front

The Cycle-230 six-mode CAR cell has not yet been compiled into the physical
`M_2` substrate under the full declared contract.  The tournament nevertheless
produced three discriminating results rather than one undifferentiated failure.

| Route | Strongest construction | Decisive residual | Disposition |
|---|---|---|---|
| direct occupation block | six active qubits in a proper-cubic 27-site macrocell; exact onsite exterior coin, contact, mass fixture, and seam block | endpoint-local stream misses CAR interval parity; exact operator residual `2`; exact ordered image has growing support | bounded partial, declared local stream rejected |
| local gauge / auxiliary | scalar-reference BKSF graph with 24 abstract edge qubits/cell, 27 active physical carriers/cell, genuine local stabilizers, bounded update gates, and repaired 24-frame covariance | on odd volumes `B_r(x)=P_matter`, so a bounded-radius state encoding `E` is impossible; even `L=4` omits odd matter parity | conditional sectorwise/global even-algebra representation, not a local compiler |
| staggered / multiplexed | hostless four-phase logical schedule `C,A,B_all,W_g`, local synchronization, and no preferred axis at macrostep resolution | plain occupation code retains sign residual `2`; exact order changes have size-growing range; ordinary port frames fail the exterior coin in 22 frames | schedule component retained, compiler rejected |

The strongest positive result is Route 2's exact **sectorwise** identity

```text
E_sector G_coarse = G_physical E_sector
```

on odd finite tori with a supplied Wilson/spin sector.  Its update gates and
constraints have bounded physical support, but `E_sector` is a globally
prepared parity-correlated isometry.  It is not the local `E` requested by the
campaign.  The distinction is decisive and prevents a false compiler success.

No residual survives as a route-independent substrate obstruction.  Exact 3-D
bosonization, auxiliary-Majorana cancellation, generalized edge codes, and
distinguishable-walker antisymmetric sectors remain live.  There is no axiom
pressure.

## Frozen contract

For every lawful finite domain, the target was an isometry `E` and a physical
unitary `G_physical` satisfying

```text
E G_coarse = G_physical E,
G_coarse = W_g Gamma(B) Gamma(A) Gamma(C),
```

with all of the following at once:

1. a bounded-radius locality-preserving state encoding and constant overhead;
2. bounded physical update support and locally enforced auxiliary constraints;
3. no global Jordan-Wigner order, parity string, global parity bus, or host
   service;
4. covariance in all 24 proper-cubic frames;
5. the Cycle-219 one-particle mass fixture;
6. the Cycle-230 contact and seam block;
7. leakage, deletion, held-out-size, and lawful-domain controls; and
8. an explicit supplied-structure inventory.

An algebraically local observable map with a global state isometry does not
satisfy item 1.  A local update that acts correctly only after global parity
preparation does not satisfy item 3.  A route-specific failure does not count
against the other encodings.

## Exact route residuals

### Route 1: direct occupation block

The direct block uses the six face-center occupations of a supplied `3^3`
macrocell.  It exactly carries the `M_64` cell, its `2048`-dimensional even
algebra, `Gamma(C)`, and `W_g`.  Every Cycle-230 `B` partner is a physical
nearest neighbor.

For the declared endpoint FSWAP stream, exhaustive fixed-`N=2` tests give:

| `L` | two-particle states | wrong signs | fraction |
|---:|---:|---:|---:|
| 3 | 13,041 | 4,140 | `0.31746031746031744` |
| 4 | 73,536 | 19,008 | `0.2584856396866841` |
| 5 | 280,875 | 60,600 | `0.2157543391188251` |

One basis witness has exact and candidate amplitudes `-1` and `+1`.  Since the
remaining factors are common unitaries,

```text
|| E G_coarse - G_direct E || = 2.
```

The exact ordered image intertwines, but its maximum intervening-mode counts
at `L=3,4,5,6` are `108,288,600,1080`.  It is the forbidden global-order
solution.  Pure geometric frames preserve the endpoint stream but fail the
coin in `22/24` frames; the bounded exterior-sign repair fixes the coin but
makes the stream fail in all `23` nonidentity frames.

### Route 2: local gauge and its two falsified repairs

The scalar-reference graph has, per coarse cell,

```text
12 octahedral matter edges
 6 matter-reference spokes
 3 matter stream edges
 3 reference lattice edges
--------------------------------
24 abstract BKSF edge qubits.
```

Genuine local loop ranks are `457/460`, `1086/1089`, `2123/2126`, and
`5829/5832` for periodic `L=3,4,5,7`; the three missing ranks are torus Wilson
labels.  At `L=3`, local loops plus reference constraints have rank `483`, all
redundant relations reduce to `+I`, and three explicit Wilson loops raise the
rank to `486`.  Update/constraint commutator failures are zero.

The BKSF port formula is presentation dependent.  Raw geometric rotation gives
`12,948` generator mismatches at `L=3`; bounded vertex-local `CZ` order repairs
and edge-local `Z` orientation repairs reduce the count to zero in all 24
frames.  A spacing-16 physical layout uses 27 active `M_2` carriers per coarse
cell after bond sharing.  The largest local carrier support and routing radii
are finite and volume independent.

This architecture has three independent qualifications:

- On odd volume, local reference equality plus the superfast even-sector
  identity gives `B_r(x)=P_matter` at every cell.  If `E` had radius `R`, two
  product states equal on the `R`-ball but differing at one remote occupation
  would give local expectation gap `0` and required parity gap `2`.  The runner
  executes radii `0,1,2,4`; the analytic witness extends to every fixed `R`.
- On even `L=4`, the code contains two copies of the even-matter sector and no
  odd-matter sector.
- Bounded local constraints leave three torus Wilson spectators.  Selecting
  the cubic-invariant untwisted sector is supplied nonlocal boundary data.

The first attempted repair, one same-port shadow per matter mode, passes every
local dimension and local-gate test but fails global assembly across one
spectator mode:

```text
local residual = 0,
global residual = sqrt(8) = 2.8284271247461903.
```

This counterexample prevents concatenating a local pair isometry and a BKSF
rank calculation into a compiler.

The physical placement is also a macrocode, not a unit-translation theorem.
It is invariant under translations by 16 physical sites.  For unit physical
translations, the held-out layout audit finds exact active-set symmetric
differences `50 L^3` (`1350,3200,6250` at `L=3,4,5`).  A period-16 marker,
translation-orbit code, or autonomous marker construction remains supplied or
unbuilt.

### Route 3: staggered/time-multiplexed block

The retained logical schedule is

```text
q=0 Gamma(C), q=1 A, q=2 B_all, q=3 W_g, q -> q+1 mod 4.
```

Neighbor equality of `q` is a local constraint with zero ideal leakage.  All
three axis edge layers fire together, so the completed logical schedule has no
preferred axis.  This solves host-side phase control but not fermionization.

Periodic axial order searches retain `4,6,8` wrong two-particle signs at
`L=3,4,5`; all `6!` static orders at `L=3` retain four.  The exact correction
has maximum periodic range `1,2,3,4` at `L=3,5,7,9`.  Changing an `x`-fast JW
order to a `y`-fast order requires maximum Manhattan ranges `2,4,6,8,12` and
nearest-neighbor light-cone lower bounds `1,2,3,4,6` for `L=2,3,4,5,7`.

The all-axis logical schedule is macro-covariant, but BKSF-style physical
supports overlap.  Constant colorings exist; a literal labeled serialization
is not invariant under rotations that permute its color/axis successor.  Any
such program register is supplied update-law structure.

## Physics fixtures and controls

All three routes preserve or reproduce the following **only at their declared
resolution**:

| Control | Exact result | Boundary |
|---|---|---|
| one-particle rest mass | `0.4534056541748851` | supplied Cycle-219 candidate |
| curvature mass | `0.4534056690336209` | finite-difference fixture |
| forced-response mass | `0.45444242813733504` | inherited tolerance |
| held-out Route-2 mass residual at `beta=-0.35` | `3.6800564e-08` | sectorwise representation only |
| seam singular values | `0.49577141, 0.45566605` | local contact-generator block |
| raw `L=3` plane-wave norm divided by `g` | `0.024939455786930305` | includes `1/L^3` normalization |
| 24-frame seam residual | `1.2947314098277875e-15` | proper-cubic frames |
| contact deletion | exactly zero residual at `g=0` | does not repair free stream |

These coexistence tests do not turn wrapped phase into energy, select an
interaction, prove an instability rate, or produce a source ledger.

## Spatial-dimension and time firewall

The framework already supplies `Z^3` spatial adjacency through the Lattice
axiom.  This tournament uses that three-dimensional substrate and does not
derive it.  The framework's physical-time program is separate.

The variables `q`, gate layer, circuit depth, coloring phase, macrostep count,
and update order are compiler controls.  None is physical time, an elapsed
tick, a clock normalization, a metric, a rate, a winding history, or progress
on the emergent single-generator gate.  The approved kinetic-isotropy
primitive supplies only the structural graining form `c_t=c_s`; it does not
turn any compiler schedule into derived time.  A genuine bridge between the
spatial compiler and the causal-time lane remains open.

## Supplied structure consolidated

Across the tournament, the supplied structure includes:

- the Cycle-219 coin family, `beta`, and its mass interpretation;
- six Cycle-230 CAR modes/cell, CAR statistics, the contact, `g`, and gate
  order;
- finite torus, sea, phase cut, and spin/Wilson boundary data;
- macrocell scales and origins, physical carrier roles, blank patterns, and
  routing templates;
- occupation conventions in Routes 1 and 3;
- BKSF interaction graph, port orders/orientations, local frame gauges,
  Hermitian-log branches, reference repetition, and odd-volume domain in
  Route 2; and
- logical schedule registers, phase origin, colorings, and successor rules.

The approved primitive registry was checked at its current paths.  Scale
reference supplies units only; kinetic isotropy supplies only `c_t=c_s` form;
realized state supplies only pointwise evaluation at supplied realized data.
None selects the compiler, parity carrier, spin sector, macro origin, coin,
contact, schedule, sea, or source.

## TOE dependency ledger

| Wall | Tournament effect | Remaining dependency |
|---|---|---|
| `C_ref` | unchanged | phase origin, physical sea, and preparation remain selected inputs |
| `C_num` | sharpened | parity-sector bookkeeping is explicit, but no physical number reference or superselection derivation is supplied |
| `C_wrap` | unchanged | no schedule or Wilson/reference label is a clock or winding carrier |
| `C_int` | representation gain only | one supplied contact is carried through bounded blocks; selection, rate, and protection remain open |
| `C_local` | materially narrowed, still open | direct and staggered plain codes fail; gauge update gates and layout exist, but a bounded local all-size `E`, local spin-sector treatment, and translation-marker/admissibility realization remain unbuilt |
| `C_source` | unchanged | no conserved physical energy, stress, action, or gravitational source is selected |

The maturity scores remain:

| Lane | Score | Reason |
|---|---:|---|
| operational quantum / records | `2/5` | conditional channels and local algebra exist; no Record formation law or local state compiler |
| time | `1/5` | compiler schedules are not clocks; the causal-time bridge remains open |
| inertia / matter | `3/5` | three mass coordinates and local many-body fixtures coexist; compiler and law selection remain open |
| gravity / source | `2/5` | resource/gravity mechanisms exist conditionally; no source ledger from this work |
| Born / probability | `1/5` | normalized conditional channels do not derive occurrence weights |

These scores are maturity judgments, not probabilities that the framework is
correct.

## No-go discipline gate

The fresh `origin/main` no-go procedure and primitive-registry check were
applied.  N1–N8 **PASS** for the narrow route dispositions and **FAIL** for a
route-independent compiler impossibility, minimum content, uniqueness, or
axiom-pressure claim.

### N1 — alternative-route enumeration

| Route | Marker | Result |
|---|---|---|
| direct six-occupation block | **ATTEMPTED** | norm-2 stream residual; exact ordered support grows |
| static and dynamically reordered staggered codes | **ATTEMPTED** | norm-2 sign residual or size-growing correction depth |
| same-port pair shadow plus local lifts | **ATTEMPTED** | local residual zero, global assembly residual `sqrt(8)` |
| scalar-reference superfast code | **ATTEMPTED** | bounded update architecture; bounded local `E` contradiction and even-size failure |
| auxiliary-Majorana cancellation | **LIVE, NOT RULED OUT** | primary-source construction class not instantiated on this fixture |
| exact 3-D higher-form bosonization | **LIVE, NOT RULED OUT** | local duality with spin structure not instantiated on this fixture |
| distinguishable walkers plus antisymmetric sector | **LIVE, NOT RULED OUT** | published free route; contact/local code untested |
| infinite-volume quasi-local representation | **LIVE, NOT RULED OUT** | may alter finite global-parity bookkeeping; unconstructed |

Four live routes prevent a broad negative.

### N2 — wall-independence audit

The route residuals collapse to four implementation conditions:

- `R_order`: plain tensor occupations miss spatial CAR signs;
- `R_global`: local shadow lifts do not assemble globally;
- `R_sector`: scalar-reference full parity requires a nonlocal state isometry
  and fails even volume; and
- `R_marker`: physical role/layout and micro-schedule selection remain supplied.

They are not four axioms and do not multiply the six TOE walls.  Closing any
one does not close another.  In particular, a local CAR compiler would not
select a sea, number reference, clock, interaction, or source; none of those
five constructs the compiler.  The inherited 15 pairwise independence entries
among `C_ref,C_num,C_wrap,C_int,C_local,C_source` therefore remain unchanged.

### N3 — hidden-wall scan

The mandatory phrase scan promotes no authority shortcut.  Macro origins,
orders, parity sectors, spin sectors, port gauges, blank routing, schedule
phases, sea, coin, and contact are in the supplied inventory.  “Local” is
resolved separately for state encoding, update support, constraint support,
and physical routing; these are not conflated.

### N4 — residual matching

| Witness | Prior residual | Current match |
|---|---|---|
| Cycle 230 `M_64 -> M_2` boundary | physical graded-local compiler absent | exact target of all three attempts |
| Cycle 229 spatial-compiler boundary | spectral exterior lift is not an onsite compiler | direct order residual and gauge construction address precisely this interface |
| Cycle 219 mass fixture | conditional one-particle rest/curvature/force agreement | rerun as coexistence, not promoted to interacting mass |
| minimal `M_2` site interface | one physical site carries `M_2` | every active carrier is one qubit; macro origin/admissibility remain conditional |

External theorems bound constructions and scope; none substitutes for the
current exact residuals.

### N5 — rhetoric and resolution audit

The tournament tested per-cell algebra, per-edge signs, fixed one- and
two-particle sectors, odd/even finite sizes, local stabilizers, torus Wilson
sectors, all 24 frames, physical coordinates, deletion, leakage, mass, and the
seam generator block.  It did not test every encoding, infinite-volume state
preparation, an autonomous unit-translation marker, one selected
nearest-neighbor admissibility law, physical time, records, Born weights, or a
source.  Every negative is stated at the tested route and resolution.

### N6 — partial-closure paths

The live paths are direct exact 3-D bosonization, auxiliary-Majorana
cancellation, a different all-size parity reservoir, an infinite-volume
quasi-local formulation, and an autonomous macro-origin/admissibility
compiler.  These are constructive paths.  No axiom edit is requested.

### N7 — steelman

> The tournament has not shown that fermions cannot live on the physical
> substrate.  It has shown that two order-based tensor codes fail and that two
> tempting gauge repairs either lose global assembly or hide total parity in a
> nonlocal state preparation.  Exact bosonization already demonstrates how
> higher-form gauge structure and spin data can change this accounting, while
> auxiliary-Majorana and antisymmetric-walker constructions give other escape
> classes.  Until those routes are applied to the exact six-mode coin, contact,
> seam, and physical `M_2` interface, a shared obstruction is premature.

The steelman is convincing.  It blocks axiom pressure.

### N8 — cross-cycle echo

Cycle 229 separated finite Fock algebra from a spatial compiler; Cycle 230
constructed intrinsic spatial CAR and the contact seam but left the physical
site map open.  This tournament retires local capacity and much of the bounded
update/layout question, while exposing state-encoding, parity-sector,
spin-sector, and macro-origin conditions.  Earlier warnings that statistics
are not forced and wrapped phase is not energy remain applicable.  No prior
wall is retired by terminology.

## Optimal next campaign

The next highest-value discriminator stays inside `C_local`: instantiate an
all-size, bounded-radius local gauge encoding using exact 3-D bosonization and
auxiliary-Majorana cancellation as independent routes.  Test `L=3,4,5` on the
same coin/contact/seam fixture and require:

1. a bounded-radius state `E`, not only a local observable algebra;
2. both global matter-parity sectors at every held-out size;
3. locally treated spin/topological data without a parity bus or marked site;
4. all-24 frame covariance and unit-translation/macro-marker accounting; and
5. exact `E G_coarse = G_physical E` plus the existing physics and deletion
   controls.

If that campaign produces another negative, it still must pass N1–N8 against
the remaining generalized-edge and antisymmetric-sector routes before any
substrate or axiom inference.

## Verification

```text
python3 scripts/three_route_physical_m2_car_compiler_tournament_cycle234_2026_07_17.py
```

The three route runners and Cycle 230 remain independent regression controls.
