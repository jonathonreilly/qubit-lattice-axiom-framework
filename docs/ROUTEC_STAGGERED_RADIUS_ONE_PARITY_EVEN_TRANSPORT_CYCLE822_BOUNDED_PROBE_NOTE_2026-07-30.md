# Route C staggered radius-one parity-even transport — Cycle 822

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive probe, repaired fixed-type atlas, complete recurrent G dictionary

Claim type: bounded_theorem candidate

Runner:

- [`frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30.py`](../scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30.py)

Constitutional effect: none. This probe changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Stage, colour, slot, route, factor, and ordinal labels are supplied
circuit structure. They are not physical time, duration, cadence, rate, or
energy.

## Result up front

The original Cycle-822 receipt used local pair-parity checks. That was not a
valid certificate for one Cycle-821-style extended parity assignment: its
charged FSWAP and neutral SWAP route atlases reused 155 coordinates on
`(2,1,1)`, 2,035 on `(3,2,2)`, and 5,306 on `(5,3,2)`. The original parity
claim is withdrawn.

The repaired compiler freezes, for each complete finite fixture, one
coordinate assignment for the entire schedule:

- charged coordinates contain the charged O/I/L matter modes, carriers, and
  every coordinate of every fermionic FSWAP route;
- neutral coordinates contain all remaining persistent companion, syndrome,
  coframe, and owner-work modes, reserved neutral access ports, and every
  moved coordinate of every ordinary-SWAP route; and
- the charged and neutral sets are disjoint. No primitive can redefine these
  types locally.

One neutral access port is reserved next to every persistent coordinate.
Charged routes are compiled while treating persistent coordinates and all
reserved ports as obstacles. This pass now includes the pump/Bell/correction
pair gates, all seam pair rotations, and all landed two-site recurrent coin,
reverse-FSWAP, and contact factors. Only after that complete charged atlas is
frozen are neutral routes compiled with it as an obstacle set.

For the resulting finite atlas,

`P_ext = product(Z_r for r in charged coordinates)`.

Every elementary matrix is tested against the restriction of this same
coordinate-defined `P_ext` to its support. Since every elementary factor is
in the same commutant, every ordered prefix is in that commutant as well. The
runner counts every elementary factor and every prefix explicitly; there are
zero failures and zero untyped coordinate uses on every fixture.

## Construction and held results

The compile scope is the scheduled `pump`, `bell_measure`, and
`bell_correction` rows plus the complete landed recurrent `G` dictionary on
each listed fixture. Per cell, the nonseam dictionary contains 11 coin
factors (ten distinct two-site Givens matrices and one onsite phase), three
reverse-FSWAP factors, and 15 contact factors: 29 factors per cell. Every
two-site factor is routed on the same frozen charged atlas; the coin phase is
executed onsite. All recurrent seam semantic factors are compiled by the
existing diagonalize/accumulate/phase/uncompute algorithm.

The runner binds each landed instruction to its exact matrix digest and emits
all real/imaginary matrix entries. There are 13 unique nonseam opcodes, 12
two-site and one one-site. Their combined opcode dictionary digest is
`f238dc1fdd233c013f6dd31329912d17c5f0bb117bf2c882b9c2c275e1e9e32d`;
the landed Cycle-720 local dictionary digest is
`e778afeda360ccb834fafd4e8c782e2482e8b4f3cf5aca78c9d0d317fce07d14`.
Every matrix binding and charged-parity commutator has zero failures; maximum
unitarity residual is `9.42129743476075e-16`.

A parity-active pair is moved on the charged atlas by nearest-neighbour
FSWAPs, acted on by the exact Cycle-821 parity-even pair rotation, and
returned. Syndrome controls and one clean accumulator M2 per owner cell move
on the neutral atlas by ordinary SWAPs and are returned.

For an even Hermitian Pauli `P`, disjoint `X/Y` charged letters are paired.
Exact two-site rotations map each pair to one `Z`; onsite basis changes act
only on neutral companion modes. The resulting `Z` character is accumulated
into the owner-local work M2 with data-as-control CNOTs, locally phased by
`RZ(+-pi/2)` or controlled by the corresponding local CZ, and exactly
uncomputed. Every routed word returns its transported labels. No internal
route coordinate intersects the persistent palette.

| shape | cells | nonseam factors | seam factors | words | primitives | routes | charged/neutral M2 | type overlap | prefix failures | collisions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(2,1,1)` | 2 | 58 | 4 | 131 | 9,956 | 412 | 459 / 1,283 | 0 | 0 | 0 |
| `(3,1,1)` | 3 | 87 | 8 | 200 | 16,103 | 644 | 702 / 2,056 | 0 | 0 | 0 |
| `(3,2,2)` | 12 | 348 | 80 | 884 | 144,272 | 4,400 | 3,433 / 13,070 | 0 | 0 | 0 |
| `(5,3,2)` | 30 | 870 | 236 | 2,273 | 394,640 | 11,708 | 8,985 / 34,255 | 0 | 0 | 0 |

The support bounds are deliberately separate. The maximum source seam
support is 17 M2; after parity-even diagonalization the maximum Z-character
support is 16 M2. The earlier wording that called the latter a direct/source
bound was incorrect.

All 564,971 elementary primitives and all 564,971 corresponding prefixes
commute with their fixture's single fixed `P_ext`, with maximum matrix
commutator residual zero. All 17,164 routes are nearest-neighbour and
returned. Deleting one return exchange detects 15,848 label failures. The
maximum bounded route distance is 43. The owner-work accumulator has residual
zero for tested Z strings of weights one through four and both signs, and the
controlled-pair local matrix residual remains
`6.312164422641715e-16`.

Generic state execution independently routes every one of the 12 unique
two-site nonseam opcodes over a distance-three clean rail and returns it with
maximum residual zero. Deleting a return exchange gives minimum residual
`0.572521454844302`. The one-site phase forward/inverse residual is
`2.7755575615628914e-16`. On a dirty rail, replacing FSWAP by ordinary SWAP is
detected for 11 of 12 routed opcodes; onsite contact is diagonal and the two
routings coincide for that mutation. This is recorded, not inflated to 12.

The landed one-particle mass fixture is rerun: the coin eigen residual is
`2.594441202963249e-16`, the mass is `0.45340565417488515` versus Cycle 219's
`0.4534056541748851`, and the mass residual is
`5.551115123125783e-17`. Vacuum/one-particle contact and double-occupation
phase residuals are zero.

## Resource overhead against committed fixed-atlas Route C

| shape | base -> complete primitives | increase | ratio | charged increase | neutral increase | persistent increase |
|---|---:|---:|---:|---:|---:|---:|
| `(2,1,1)` | 8,822 -> 9,956 | 1,134 | 1.1285 | 73 | 55 | 0 |
| `(3,1,1)` | 14,360 -> 16,103 | 1,743 | 1.1214 | 101 | 54 | 0 |
| `(3,2,2)` | 137,308 -> 144,272 | 6,964 | 1.0507 | 302 | 63 | 0 |
| `(5,3,2)` | 377,226 -> 394,640 | 17,414 | 1.0462 | 748 | 484 | 0 |

The extension adds 28 charged route macros and one onsite phase per cell. It
adds no persistent M2; charged-atlas growth and neutral detours are reported
separately.

## Fixed schedule, covariance, and controls

The fixed block order is `pump`, `bell_measure`, `bell_correction`,
`recurrent_coin`, `recurrent_reverse_FSWAP`, `recurrent_seam`, then
`recurrent_contact`. The first three reuse the landed mod-3 owner colour and
17 family slots. Nonseam recurrent factors use the cell's mod-3 colour and
their landed within-cell ordinal as a slot: 11 coin, three reverse, and 15
contact slots. The seam layer uses the landed axis/checkerboard colour and
four factor slots per edge axis. No box-dependent greedy recolouring is used.

The executable collision graph compares every simultaneously occupied site
at every block ordinal and has zero edges on all four shapes. Erasing stage
separation produces 58, 85, 326, and 807 collision edges. Replacing the
transported colour assignment by a fixed colour is detected. These are
route-specific controls, not a schedule no-go.

On the base fixture, all 24 proper-cubic frames, eight translated coframe
origins, 192 frame/origin contexts, and 576 ordered frame products have zero
nearest-neighbour, palette, collision, fixed-type, colour-bijection,
coordinate-product, or colour-product failures. This is transported-program
covariance: it affinely transports the one compiled identity-frame program,
its fixed charged/neutral atlas, colours, and occupied-coordinate sets. It
does not rerun atlas construction independently in every frame. Holding the
carrier offset fixed in laboratory coordinates is detected in 23 of 24
frames.

Other active controls are:

- the pre-repair overlapping atlas is measured before the repaired compile;
- deleting the final return exchange from every nontrivial tested route
  leaves a label mismatch;
- retyping one charged route coordinate as neutral, or one neutral route
  coordinate as charged, creates one cross-type overlap; an FSWAP or SWAP on
  a mixed charged/neutral edge has commutator residual `2.8284271247461903`;
- FSWAP and ordinary SWAP agree on the supplied clean transport rail, while a
  dirty occupied rail gives residual `sqrt(2)`; and
- the clean-work Z accumulator is checked independently with residual zero.

## Direct imports and Cycle 734 boundary

The algorithm directly reuses Cycle 720 physical placement and recurrent
factor rows; Cycle 789 O/I/L palette, private atlas, colours, and fixed
stage/slot schedule; Cycle 794 exact factorwise recurrent composition; and
Cycle 821 carrier placement, atomizer, pair rotations, and bounded seams.

Current Cycle 734 is only a companion boundary, not a physical primitive.
Its pair template remains externally positioned, logical, and
non-nearest-neighbour. Route C neither imports it as carrier genesis nor
treats its adjacent-guard observation as a transport obstruction.

## Supplied / derived / open

### Supplied

- the landed finite Cycle-720/789/794/821 code domain, O/I/L resource,
  carrier, clean definite syndrome controls, private atlas, chart, and finite
  boundary;
- one clean accumulator M2 per owner cell and clean returned route rails;
- the fixed stage/colour/slot/ordinal program and transported proper-cubic
  coframe; and
- total extended-parity superselection as the observable domain and
  permission to retain the dirty carrier.

### Derived

- one immutable, disjoint charged/neutral coordinate partition for the full
  finite schedule and its single coordinate-defined `P_ext`;
- commutation of every elementary primitive and every prefix with that same
  `P_ext`;
- literal nearest-neighbour returned transport for every tested Cycle-821
  Bell/pump/correction atom, all 29-per-cell nonseam factors, and every
  recurrent seam factor;
- exact matrix/digest binding and generic returned-route execution for every
  unique landed nonseam opcode, plus the one-particle mass fixture; and
- the stated route, deletion, collision, wrong-stage, wrong-colour,
  fixed-offset, SWAP/FSWAP, support, and 24/8/576 covariance controls.

### Open

- autonomous genesis and renewal of clean route/accumulator M2, clean
  syndrome banks, carrier typing, coframe, and stage occurrence;
- a monolithic dense held-width executor rather than exact Pauli,
  local-matrix, returned-label, and landed factorwise substitution checks;
- translation-invariant duplicate-view gluing, periodic topology, and fault
  rejection/repair; and
- physical time, duration, source/gravity, Record/Born/history, and
  prediction bridges.

## Verdict

After withdrawal of the invalid pairwise certificate, the repaired and
extended Route C is a positive bounded compiler probe under one fixed global
coordinate type assignment per complete finite fixture. Its scope now covers
the prepared pump/Bell/correction program and the complete landed recurrent
G dictionary: coin, reverse-FSWAP, seam, and contact, including the mass
fixture. The clean rail/work domain and fixed circuit program remain supplied.
No no-go, minimum-resource, shared-obstruction, or axiom-pressure claim is
made.
