# Physical autonomous marker-recognition/token attempt — Cycle 631

Date: 2026-07-23
Branch: `codex/toe-cross-lane-campaign-20260718`
Authority: none
Audit: unset
Constitutional effect: none

The machine-readable status strings remain exactly `authority none` and
`audit unset`.

## Result

Cycle 631 makes a real but partial constructive advance above Cycles 629 and
630. On the supplied Cycle-629 marker sector it replaces the excluded raw
selector by an exact marker-safe computation. Each branch compute has 285
exact clean-scratch Toffoli macros plus 92 complement operations, or **7,787**
support-one/two primitives before nearest-neighbor movement. The computation
uses 23 negative-control complements, 142 conjunction-chain work sites, four
reusable parity sites, and one flag. Every marker is only a diagonal-phase
target or a CNOT control, so its computational value is unchanged at every
primitive. Work is physically placed at free roles outside the declared
Cycle-610 dynamic allocation, every two-site primitive is assigned a
Cycle-630 marker-free fine-NN move/apply/reverse route, and the same circuit
cleans every scratch site and the flag on uncompute.

The routed selector costs 142,711 fine-NN microsteps per compute and 285,422
for compute plus uncompute. With the Cycle-630 act word, the exact selected
selector-plus-act macro has 35,647,188 microsteps; all24 spatial realizations
therefore have 855,532,512 microsteps in aggregate. These are word lengths,
not physical rates or autonomous clock periods.

The finite route table also receives an exact abstract reversible successor.
A path of `d` edges has `2d` labeled states: `d-1` opening states, one apply
state, `d-1` closing states, and one same-endpoint renewal state. Across all
4,570 paths this is **393,824** states and transitions with an explicit inverse,
malformed-label rejection, and a deleted-transition control. This is a table
construction, not an implemented M2 automaton.

A nine-colour collision layer is constructive. A positive fine-NN edge is
coloured by `(axis, (positive-source coordinate - phi_axis) mod 3)`. Each
colour is a matching because an axis vertex can be incident only in the two
different residue classes `c` and `c+1`. Since `129L` is divisible by three,
the same statement holds through the seams on L3/L6/L7. The state-carried
`phi` action passes six translations; signed axis/residue permutation passes
all24 proper-cubic frames and all576 compositions. This is edge arbitration,
not causal time, a token, or a program generator.

The full selected-branch selector-plus-act word is explicitly counted in the
receipt. It consists of selector compute, the Cycle-630 conditional act word,
and clean selector uncompute. The exact count is bounded at fixed `K=129`, but
the route request and descriptor order are still supplied by a host table.

## Marker-safe exact Toffoli

The usual 15-gate Toffoli decomposition temporarily targets a control and is
therefore unsuitable when a control is an occupied marker. Cycle 631 instead
uses four clean parity sites and the exact phase identity

```text
4abc = a+b+c-(a xor b)-(a xor c)-(b xor c)+(a xor b xor c) mod 8.
```

The resulting sequence has two H, seven T/Tdg, and 18 CNOT gates. Its 27
primitives are executed on all eight computational inputs with the four
parity inputs clean. The unitary residual on that declared subspace is below
`1e-12`, all parity work returns clean, and neither control is ever a bit
target. Remote marker-control CNOTs move only the free target to a free
nearest neighbor of the marker, apply the CNOT, and reverse the route.

For branch `h`, the actual local occupancies tested are all 120 Cycle-629
anchor sites, the positive orientation site `h`, and the complemented other
23 orientation sites. All 24 lawful one-hot inputs recognize exactly one
branch. Zero-hot, two-hot, all-hot, and one-anchor-deleted inputs recognize no
branch. Deleting the final conjunction-to-flag macro destroys lawful
recognition. All scratch returns blank after compute except the flag and all
returns blank after uncompute.

The declared periodic selector domain also supplies neighbor-equal `h`.
Every unique recognizer route edge is translated by the six neighboring K129
cell displacements on L3/L6/L7; equal-phase copies have zero vertex
collisions. This does not enforce orientation equality or create phase
synchronization.

This is raw anchor plus exact-one recognition only. Cycle 629's supplied
`<=91` non-anchor weight condition remains a diagonal code-space premise; no
fine-NN comparator, equality enforcement, preparation, or repair circuit is
supplied.

## Token and program probes

The simplest physical sidecar is false. Translating a route by each of the six
unit offsets and requiring the translate to be marker-free and disjoint from
the data route leaves **1,919** of 4,570 routes with no allowed sidecar. That
is a route-specific failure of the single-adjacent-lane layout, not an
impossibility result.

The runner continues with two-lane and six-lane sidecars. At each path site a
token may occupy an axial neighbor. A lane change between non-opposite lanes
uses two NN steps through the diagonal connector while the data step pauses.
A dynamic program exhausts all 15 two-lane pairs and the full six-lane set,
records minimum lane changes, excludes markers and every data-path residue,
and reports exact successes and failures. Two lanes solve 4,536/4,570 paths.
The six-lane construction solves all 4,570: 2,651 use no lane change, 600 use
one, and 1,319 use two. This is a stronger geometric route-around, but it does
not choose its predecessor locally, encode its head state, generate its token,
or renew it.

Two local-program layouts are also attacked explicitly. A unary moving-head
tape needs at least one physical phase site per fine microstep, before opcode,
head, adjacency, data-exclusion, inverse, or renewal storage. Its exact lower
bound is 35,647,188 sites, versus `129^3-144 = 2,146,545` marker-free
roles—a 16.607 capacity ratio before those extra requirements. A one-step
stationary radius-one lookup sees at most seven M2 sites, or 14 raw binary
bits, below the 26-bit full program address. Both naive layouts fail. By
contrast, the 441,030 distinct literal stage descriptors fit numerically
below the free-role count, so compressed descriptor ROM plus a multistep local
decoder remains open. No minimum-content or shared-wall conclusion follows.

Cycle 617 Route B remains bounded prior collision machinery only: eight lanes,
capacity seven, and 28 adjacent compare-exchange stages. It is host scheduled,
is not causal time, and is not a CAR sign service. Cycle 631 does not inherit
or promote it.

## Covariance and periodic scope

The raw recognizer role list is generated from one base list by the
state-carried orientation `h`. The runner checks every role under all24 frames
and all576 frame compositions. The edge-colour map sends a negative axis
image from residue `c` to `-c-1 mod 3`; this is checked as a nine-label
permutation and under all576 compositions. Translating both the edge source
and state-carried `phi` leaves the relative colour invariant.

The L3/L6/L7 checks establish matching and seam consistency only. A single
selected token per translated coarse cell has disjoint equal-phase translates
because `K>1`; arbitrary requested token edges can be serialized by the
nine-colour matching. Neither observation creates the route request or
synchronizes a program clock.

## Full physical firewall

Cycle 631 does **not** construct:

- physical M2 storage and a local successor update for route identity/phase;
- a local clock-to-descriptor/gate ROM or moving-head interpreter;
- token genesis and recurrent clean renewal;
- fine-NN enforcement of the Cycle-629 `<=91` weight premise;
- a host-free recurrent `G_physical`;
- a literal physical encoder `E`;
- a physical-code leakage test or a residual for
  `E G_coarse = G_physical E`;
- fresh one-particle mass, contact, or wrap-seam fixture execution.

The coarse act population contains the inherited target descriptor families,
but Cycle 631 takes no inherited fixture credit. It does not call a coarse CAR
cell a physical-site compiler, wrapped phase physical energy, a generator
element a rate, or pointer copying a Record. It introduces no global
Jordan–Wigner ordering or parity service.

## Current N1–N8 discipline

N1 normalizes seven attempted families: marker-safe recognition, abstract token
successor, fixed sidecar, multilane sidecar, nine-colour arbitration, a padded
binary program clock, and local ROM/moving-head probes. Every counted row uses exactly `ATTEMPTED` or
`RULED OUT BY PRIOR`; open counterroutes are listed separately and do not
inflate family coverage.

N2 separates physical token storage, local program decoding, genesis/renewal,
weight enforcement, literal E/leakage, and host-free G/intertwiner. Every
directional pair is recorded separately; no common witness is asserted.

N3 records all load-bearing supplied structure: fixed K129, state-carried
`phi,h`, the supplied marker/weight sector, clean work, the host-materialized
Cycle-630 paths, and the finite descriptor order.

N4 uses exact citation rows with `same_scope`, `exact_match`, and
`use_as_closure`. The new raw selector narrows prior selector residuals, while
the physical controller and physical intertwiner residuals remain.

N5 records `per_element`, `per_site`, `per_mode`, `per_block`, and
`lattice_wide` resolutions. Bounded at fixed K does not mean an autonomous
lattice law.

N6 records each partial artifact with exact file, status, and `what_closes`.
N7 gives an actionable hostile steelman: a covariant multilane route-label
packet plus a local finite ROM, followed by weight enforcement and literal
E/G tests. N8 records applicability across Cycles 610, 617, 629, 630, and 631.

The broad-negative, minimum-content, shared-obstruction, and axiom-pressure
gates all remain `FAIL / DO NOT SHIP`. The narrow constructive selector,
abstract successor, and matching results may ship with their firewalls; the
single-sidecar and naive-ROM failures may ship only at their exact scopes.
There is no axiom pressure.

## Disposition and next campaign

The selector is the strongest constructive increment. It is computed from
actual marker occupancies, uses explicitly placed work, and returns that work.
The successor is only an abstract finite-state table. The fixed sidecar is
falsified. The bounded-change multilane scout identifies whether geometry
survives, but no physical head law follows from it. The nine-colour layer
solves collision arbitration conditional on requests and state-carried phase;
it is not time.

The optimal next campaign is to construct a bounded covariant multilane
route-label packet and a literal fine-NN multistep ROM/interpreter mapping
carried `(phi,h,clock,route,phase)` to an edge and gate, with explicit token
genesis and renewal. Only after that should the campaign enforce the `<=91`
sector and compose literal `E` and recurrent `G_physical` for fresh
intertwiner, leakage, deletion, L3/L6/L7, mass, contact, and seam tests.
