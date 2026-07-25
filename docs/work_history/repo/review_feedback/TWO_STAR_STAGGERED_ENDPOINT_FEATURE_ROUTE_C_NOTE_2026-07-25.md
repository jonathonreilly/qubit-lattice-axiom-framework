# Two-star staggered endpoint-feature Route C

Date: 2026-07-25
Status: **positive bounded partial**
Authority: **none**
Audit: **unset**

## Result

Route C closes two finite surfaces and keeps their join explicit.

First, a lawful half-edge chart is supplied as a one-hot qutrit encoded by two
`M2` factors:

```text
blank = 00, Z-chart = 10, X-chart = 01.
```

On this chart the endpoint incidence is `z XOR x` and the endpoint tag is
`x`.  A fixed 29-gate word extracts both endpoint features, SWAP-transports
them to a comparator, applies

```text
(-1)^[ I_left I_right (tag_left XOR tag_right) ],
```

uncomputes every comparator and transport factor, and swaps the two endpoint
role registers.  The word is an exact coherent unitary, not a measurement or
a basis-state-only lookup.  Its nine-state code intertwiner residual is zero
and all ten work factors return on every lawful chart pair.

Second, two adjacent maximal stars are combined as one 12-cell patch.  Their
common coarse edge is owned once, so the union has eleven rather than twelve
stream edges.  The actual bounded update

```text
G_two-star = contact * eleven distinct-port FSWAPs * twelve-cell coin
```

is executed on all 2,629 hard-core vacuum/one/two columns of the 72-mode
patch.  This is a logical Fock update built from the landed coin, seam and
contact matrices.  It is not an `M64^12 -> M2` physical encoding theorem.

The two results compose only at the explicitly supplied half-edge-chart
interface.  A full physical encoding that prepares those charts from the
landed Cycle-311 branch superpositions remains open.

## Exact executable results

The runner reports 7 PASS / 0 FAIL and terminal

```text
TWO_STAR_QUTRIT_SIGN_AND_NLE2_UPDATE_CLOSED_FULL_PHYSICAL_E_OPEN
```

Feature/order circuit:

- 16,384 computational-basis states checked for a bijective monomial action;
- 9 lawful qutrit-pair code states;
- coherent code intertwiner residual `0`;
- full-unitary raw residual `0`;
- work-return failures `0`;
- 29 gates per edge: 16 CNOT, 10 SWAP, 2 Toffoli and 1 controlled phase;
- deleting the phase gate causes 2 lawful failures;
- mutating its control causes 1 lawful failure.

Binding to landed branch grammar:

- L5 train branch-term pairs: 83,244, with 1,200 positive physical order
  signs and zero feature, qutrit, schedule or work-return failures;
- held L6 branch-term pairs: the same 83,244 cases and the same zero-failure
  result without refit;
- the 59,460 arm-arm cases per size commute; the 23,784 center-arm cases
  contain every positive sign.

Two-star update:

- 12 coarse cells, 72 modes and 11 unique coarse edges;
- dimensions `(vacuum, one, two) = (1, 72, 2,556)`;
- 88,309 coin nonzeros and 2,629 stream nonzeros;
- 180 nontrivial two-particle contact columns;
- coin unitarity raw residual `6.661438741028268e-16`;
- stream unitarity raw residual `0`;
- contact unitarity raw residual `2.226534750406793e-17`;
- complete update unitarity raw residual `6.66144839573683e-16`;
- two-particle update unitarity raw residual `6.66144839573683e-16`;
- one-particle mass `0.45340565417488493` versus Cycle219
  `0.4534056541748851`, residual `1.6653345369377348e-16`;
- uniform one-particle eigen residual `7.066438185755257e-16`.

Covariance and placement:

- all 24 proper-cubic frames and 264 routed program-edge frame cases;
- maximum update covariance residual and raw maximum both `0`;
- all 576 frame products, 1,514,304 exterior Fock phase cases and 6,336
  program-edge product cases with zero failures;
- exhaustive 16,384-state endpoint-reversal covariance with zero failures;
- 750 translated/oriented L5 fixtures and 1,296 held-L6 fixtures with zero
  collisions or edge-identification failures and no refit.

The fixed feature program has 319 supplied gate ordinals and SHA-256

```text
9d652d0177736464830b2c8f14744c2bb4d74c2cb94049894a60f55e8584b850.
```

The ordinal is a circuit-order label.  It is not physical time, a clock rate,
energy, occurrence or a framework Record.

## Shared-outer and deletion controls

The coherent qutrit controls satisfy the exact operator identity between the
canonical and reversed `Z/X` order on an arbitrary shared outer `M2`; the
operator residual is zero.

A direct attempt to copy `Z` and `X` information from that same outer factor
with CNOT and Hadamard-conjugated CNOT, phase the two copied bits, and echo the
copy does not implement the target.  Its target residual is
`1.9999999999999996` and its returned-work leakage is
`0.9999999999999996`.  Thus the qutrit role controls are load-bearing supplied
structure; basis switching or measurement is not being hidden as extraction.

Other active controls are:

- deleting the unique shared seam: update residual `2`;
- servicing the shared seam twice: update residual `2`;
- deleting contact: residual `0.3678930670560824`;
- reversing the free/seam/contact order: residual `1.990327350532773`;
- dirty feature-work genesis: nonreturn detected;
- four unlawful qutrit rows and four unlawful Fock rows: all rejected.

## Resources

The finite two-star sign layer supplies:

- 44 half-edge role `M2` factors (two qubits for each of 22 half-edges);
- 110 clean returned work `M2` factors (ten for each unique edge);
- 11 edge modules and 319 fixed feature gates.

These are explicit resources for this construction, not a minimum.  The
Toffoli/controlled-phase primitives are not lowered here to a cubic
nearest-neighbor Clifford+T placement.

## Supplied

- the landed Cycle-311/315/330 vacuum/one/two branch grammar;
- the Cycle219 `beta=-0.3` coin and Cycle230 `g=0.37` contact;
- one lawful blank/Z/X qutrit chart on each half-edge;
- the `Z_internal + Z_outer` versus `X_outer + X_endpoint-tag` chart
  identification;
- ten clean work factors per unique edge;
- the 29-gate edge word, unique-edge ownership order and 319-state program
  ordinal;
- two adjacent centers, the finite vacuum/one/two domain, a chart orientation,
  the rotated 24-member schedule family and L5/L6 periodic fixtures.

## Derived

- a coherent graded endpoint-role swap with exact work return;
- exact incidence/tag transport and physical `Z/X` order phase;
- zero branch-sign errors on every landed L5 and held-L6 comparator case;
- one-owner consistency at the shared port of two overlapping maximal stars;
- an actual number-preserving 2,629-column free/FSWAP/contact update;
- unchanged one-particle mass and active seam/contact/order controls;
- all-24 covariance, all-576 products and L5/L6 translation compatibility;
- active rejection of the naive shared-outer basis-switch echo.

## Open

- a physical unitary that derives or prepares the qutrit charts from the
  Cycle-311 branch superpositions;
- an end-to-end `M64^12 -> M2` encoding intertwining the sign circuit and the
  two-star free/seam/contact update;
- coherent consistency constraints tying the six half-edge charts belonging
  to one cell branch;
- nearest-neighbor placement and primitive synthesis for the feature module;
- `n>2`, unrestricted simultaneous branch superpositions and recurrent
  overlapping-star streaming;
- autonomous preparation, work renewal, collision control and a physical
  controller;
- physical time, rate, energy, source, gravity, Record, occurrence,
  probability or Born meaning;
- any minimum, impossibility, shared-obstruction or axiom-pressure conclusion.

## Reproduce

```bash
python3 scripts/frontier_two_star_staggered_endpoint_feature_route_c_2026_07_25.py
```
