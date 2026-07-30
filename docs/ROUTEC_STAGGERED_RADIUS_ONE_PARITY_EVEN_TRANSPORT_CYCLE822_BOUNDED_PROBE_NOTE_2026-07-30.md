# Route C staggered radius-one parity-even transport — Cycle 822

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive probe, repaired fixed-type atlas

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
reserved ports as obstacles. The complete charged atlas is then frozen, and
all neutral routes are compiled with that atlas as an obstacle set. This is
the smallest repair used here: the atom and seam algorithms are unchanged;
only the route atlas is rebuilt around an immutable type partition.

For the resulting finite atlas,

`P_ext = product(Z_r for r in charged coordinates)`.

Every elementary matrix is tested against the restriction of this same
coordinate-defined `P_ext` to its support. Since every elementary factor is
in the same commutant, every ordered prefix is in that commutant as well. The
runner counts every elementary factor and every prefix explicitly; there are
zero failures and zero untyped coordinate uses on every fixture.

## Construction and held results

The compile scope is exactly the scheduled `pump`, `bell_measure`, and
`bell_correction` rows plus every recurrent seam semantic factor on each
listed fixture. It does not synthesize or independently retest the 29-per-cell
nonseam recurrent coin, reverse-FSWAP, and contact factors, and it does not
rerun the one-particle mass fixture. Those remain landed/imported Cycle-821/
794 context, not Cycle-822 Route-C results.

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

| shape | cells | words | seam factors | source support max | post-diagonal Z support max | primitives | routes | type overlap | global-prefix failures | collision edges |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(2,1,1)` | 2 | 73 | 4 | 5 | 4 | 8,822 | 356 | 0 | 0 | 0 |
| `(3,1,1)` | 3 | 113 | 8 | 5 | 4 | 14,360 | 560 | 0 | 0 | 0 |
| `(3,2,2)` | 12 | 536 | 80 | 17 | 16 | 137,308 | 4,064 | 0 | 0 | 0 |
| `(5,3,2)` | 30 | 1,403 | 236 | 17 | 16 | 377,226 | 10,868 | 0 | 0 | 0 |

The support bounds are deliberately separate. The maximum source seam
support is 17 M2; after parity-even diagonalization the maximum Z-character
support is 16 M2. The earlier wording that called the latter a direct/source
bound was incorrect.

All 537,716 elementary primitives and all 537,716 corresponding prefixes
commute with their fixture's single fixed `P_ext`, with maximum matrix
commutator residual zero. All 15,848 routes are nearest-neighbour and
returned. Deleting one return exchange detects 14,532 label failures. The
maximum bounded route distance is 43. The owner-work accumulator has residual
zero for tested Z strings of weights one through four and both signs, and the
controlled-pair local matrix residual remains
`6.312164422641715e-16`.

## Fixed schedule, covariance, and controls

The fixed block order is `pump`, `bell_measure`, `bell_correction`, then
`recurrent_seam`. The first three reuse the landed mod-3 owner colour and 17
family slots. The seam layer uses the landed axis/checkerboard colour and four
factor slots per edge axis. No box-dependent greedy recolouring is used.

The executable collision graph compares every simultaneously occupied site
at every block ordinal and has zero edges on all four shapes. Erasing stage
separation produces 26, 35, 167, and 402 collision edges. Replacing the
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
  Bell/pump/correction atom and recurrent seam factor; and
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

After withdrawal of the invalid pairwise certificate, the repaired Route C
is a positive bounded compiler probe under one fixed global coordinate type
assignment per complete finite fixture. The clean rail/work domain and fixed
circuit program remain supplied. No no-go, minimum-resource, shared-
obstruction, or axiom-pressure claim is made.
