---
claim_id: cubic_matching_product_qubit_qca_schedule_orbit_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact 720-schedule classification for two supplied symmetric two-qubit gates on six proper-cubic nearest-neighbor matchings of an even periodic cubic qubit lattice, with a direct supplied-quasi-local extension to Z^3. For CZ, all schedules are one translation/proper-cubic-invariant graph-radius-one automorphism. For iSWAP and even side L>=6, the schedules give exactly eight distinct graph-radius-six macro-ticks, 90 schedules each; they form one proper-cubic and cyclic-conjugacy orbit but no member is invariant under every one-site translation. L=4 collapse and the exact reversal/inverse relation are explicit. The gate, tensor-product carrier, parity origin, and macro-tick convention are supplied; no arbitrary-QCA classification or physical process selection is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.py
---

# Cubic Matching-Product Qubit QCA Schedule-Orbit Classification

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This note changes no axiom,
approved primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.py`](../scripts/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.txt`](../logs/runner-cache/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.txt)

## Question

Can the six conflict-free matching layers from the overlap-order campaign be
composed into a genuine one-qubit-site circuit with a unique simultaneous
cubic tick?

The answer depends on the supplied two-qubit gate.

```text
commuting symmetric gate CZ
  -> one schedule-independent, translation/cubic-invariant
     graph-radius-one circuit automorphism;

noncommuting symmetric gate iSWAP
  -> eight graph-radius-six macro-ticks in one symmetry orbit,
     with no one-site-translation-invariant member.                 (1)
```

This is an exact process-class fork, not a gate-selection theorem.

## Existing-science reading gate

The actual strict-tick, simultaneous-Bloch, eta-twisted, finite-protocol,
overlap-order, and locality sources and runners were read before this attack.

- The approved
  [`minimal axioms`](MINIMAL_AXIOMS_2026-06-29.md) supply the simple-cubic
  nearest-neighbor graph and its translations/proper rotations, but no global
  tensor product, two-qubit gate, circuit schedule, tick, or clock.
- The context-only `KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK...` and
  `ETA_TWISTED_WALK_FAMILY...` sources concern `8 x 8` one-particle Bloch
  unitaries, not finite-depth qubit circuits.
- The preceding context-only
  `OVERLAPPING_EDGE_INSTRUMENT_ORDER_AND_TIME_RATE_NONSELECTION...` source
  proves that six matchings form one symmetry-stable family but supplies no
  coherent gate or layer order.
- The scalar CAR-QCA subblock closes the Bloch/CAR category gap only for
  Gaussian number-preserving automorphisms. The present source instead works
  directly on a supplied finite tensor product of qubits.
- No retained source classifies a many-body cubic-QCA index, finite-depth
  schedule orbit, or physical Admissibility-to-tick realization.

The matchings, circuit algebra, and schedule counts are recomputed here. No
prior negative tick result is proof authority.

## 1. Six matching layers

On the periodic cubic torus `(Z/LZ)^3` with even `L>=6`, define

```text
M_(mu,p)={{x,x+e_mu}: x_mu=p mod 2},
mu=1,2,3,  p=0,1.                                         (2)
```

Every layer is a perfect matching and the six layers partition all undirected
nearest-neighbor edges. Supply a symmetric two-qubit gate `G`, so reversing an
edge does not change its placement, and define

```text
L_(mu,p)(G)=product_(edge in M_(mu,p)) G_edge.             (3)
```

The factors inside one layer have disjoint support. A six-layer macro-tick is

```text
U_pi(G)=L_(pi_6)(G)...L_(pi_1)(G),       pi in S_6.        (4)
```

There are `6!=720` schedules. The macro-tick convention, rather than a single
layer, is an explicit clock-graining choice.

## 2. Commuting CZ closure

For `G=CZ`, all edge gates commute. Because (2) partitions the edges,

```text
U_pi(CZ)=product_(all nearest-neighbor edges e) CZ_e        (5)
```

for every `pi`. Equation (5) is invariant under every unit translation and
proper cubic rotation. It fixes every local `Z_x` and sends

```text
X_x -> X_x product_(y nearest x) Z_y,                      (6)
```

so it is a genuine one-qubit-site circuit QCA of exact graph radius one. This
is a positive conditional closure: schedule ambiguity disappears after the
commuting gate is supplied. The axioms do not select `CZ`.

## 3. Exact iSWAP schedule quotient

On a computational-basis edge,

```text
iSWAP |00>=|00>,       iSWAP |11>=|11>,
iSWAP |01>=i|10>,      iSWAP |10>=i|01>.                  (7)
```

Thus every circuit is a monomial unitary

```text
|x> -> i^(q_pi(x)) |P_pi x>,                              (8)
```

where `P_pi` is a site permutation and `q_pi` is a quadratic polynomial
modulo four. The runner computes both objects exactly, so equality in the
classification is equality of the full qubit unitary, not only of its
one-particle sector or support action. Every circuit fixes the vacuum with
phase one, so equality as automorphisms cannot hide a different global phase
inside this family.

Complete matching layers on distinct axes commute. The two parity layers on
one common axis do not commute for even `L>=6`. Therefore the product depends
only on the three signs

```text
epsilon_mu=+1  if (mu,0) occurs before (mu,1),
epsilon_mu=-1  otherwise.                                 (9)
```

All `2^3=8` sign triples occur. Holding a triple fixed imposes three pairwise
order constraints, so it has

```text
6!/2^3=90                                                   (10)
```

linear extensions. Direct exact evaluation confirms that different sign
triples give different `(P,q)` and hence different unitaries at `L=6`.

The all-even-size statement is analytic rather than an extrapolation from that
certificate. A layer on axis `mu` merely permutes occupations along that axis
and contributes the number of domain walls across its matching. A complete
layer on another axis preserves both that matching and its domain-wall count,
so complete layers on distinct axes commute on the full Hilbert space. On the
one-excitation sector,

```text
U_epsilon |x>
 = -|x + 2 sum_mu epsilon_mu (-1)^(x_mu) e_mu>.           (11)
```

The two same-axis orders and all eight displacement triples in (11) are
distinct for every even `L>=6`. This proves both the lower bound of eight and
the finite-size threshold independently of the phase-polynomial enumeration.

## 4. Spatial orbit but no invariant member

Signed axis permutations with determinant `+1` give the 24 proper cubic
rotations. Their parity action is already transitive on the eight `epsilon`
products. A unit translation along axis `mu` exchanges the two matchings on
that axis and flips `epsilon_mu`.

This is family covariance, not covariance of one law:

```text
translation along mu: U_epsilon -> U_(epsilon with mu flipped).   (12)
```

Because the two same-axis orders are distinct for `L>=6`, no fixed
`U_epsilon` is invariant under every one-site translation. Every member is
invariant under even translations, so supplying one sign triple selects a
period-two scheduling phase rather than destroying translation structure
altogether. Averaging the channels, adding a clock register that cycles the
phase, using a larger unit cell, or changing the gate are additional process
rules.

## 5. Cyclic phase, graph radius, and reversal controls

Moving the first layer of a word to the end is not generally exact equality.
It is the finite-depth conjugacy

```text
U_(pi_2,...,pi_6,pi_1)
 = L_(pi_1) U_pi L_(pi_1)^(-1).                           (13)
```

For iSWAP at `L>=6`, every one-step cyclic shift changes the exact product.
Across all schedules these shifts connect all eight products into one
cyclic-conjugacy orbit. Thus raw equality, spatial conjugacy, and cyclic
time-origin conjugacy are different statements. In particular, the eight
exact products are not eight QCA phases or index classes.

For either same-axis order, the two alternating iSWAP layers move the
computational `Z` support by two sites, with the direction determined by site
parity and `epsilon_mu`. The three axes commute, so after all six layers a
local `Z` support has moved nearest-neighbor graph distance

```text
2+2+2=6.                                                    (14)
```

The circuit depth gives the matching upper bound, hence every iSWAP
macro-tick has exact graph/`l1` automorphism radius six (and coordinatewise
`l_infinity` radius two). Calling this six-layer word “one tick” therefore
does not derive the edge-per-tick normalization or a physical rate.

Gatewise, for `g=iSWAP`,

```text
g^dag=(Z tensor Z)g.
```

Every matching is perfect. With `P=product_x Z_x`, this gives

```text
L_m^dag=P L_m,              L_m^2=P.                       (15)
```

The global parity `P` commutes with every number-preserving iSWAP layer.
Because a macro-tick contains exactly six layers, its six parity factors
cancel:

```text
U_pi(iSWAP)^dag = U_(reverse pi)(iSWAP).                   (16)
```

Literal schedule reversal with the same iSWAP gate therefore implements the
exact stroboscopic inverse in this grammar. Gatewise `iSWAP^dag` in reverse
order is the general adjoint construction and also works, but it is not
necessary here. Any of the 90 schedules with sign triple `-epsilon` implements
the same inverse, so literal word reversal is not unique. The runner checks
both constructions for all 720 schedules.

For clarity, this is an inverse control rather than a derived physical
time-reversal law. Computational-basis conjugation `K` fixes every complete
six-layer `U_epsilon`, whereas `U_epsilon^dag=U_(-epsilon)` is distinct at
`L>=6`; bare `K` is therefore not fixed-member Floquet time reversal. A
separately chosen proper rotation taking `epsilon` to `-epsilon` can be
combined with `K`, but that extra choice is not selected here.

At `L=4`, opposite two-site moves coincide on each axis. All eight products
collapse to one. The theorem excludes this small-torus alias and the runner
keeps it as a finite-size mutation control.

## 6. Infinite-lattice extension and finite certificate

Each matching layer is a formal product of mutually disjoint bounded-range
gates and therefore defines a locality-preserving automorphism of the
quasi-local qubit algebra on `Z^3`. The finite-torus equations use literal
unitaries and the operator `P`. On the infinite lattice, the corresponding
onsite parity automorphism replaces conjugation by a nonexistent quasi-local
global product operator, and it cancels six times in the same automorphism
identity. The local layer algebra behind (5)--(16) therefore extends the CZ
closure and eight-product iSWAP classification after a parity origin and
quasi-local tensor-product carrier are supplied. Formula (11) separates the
eight infinite-lattice automorphisms. The `L=6` enumeration is a finite exact
certificate of the full phase-polynomial bookkeeping; it is not used as
numerical evidence for stabilization.

The supplied parity origin is harmless for defining the circuit but is exactly
what prevents an individual iSWAP product from being one-site-translation
invariant. This mathematical extension does not turn the circuit into a
framework-selected physical update.

## 7. Result and boundary

The exact classification in the stated matching-product grammar is

| supplied gate | distinct products among 720 | spatial status | exact graph radius |
|---|---:|---|---:|
| `CZ` | 1 | one translation/proper-cubic-invariant automorphism | 1 |
| `iSWAP`, infinite `Z^3` or even `L>=6` | 8, each with 90 schedules | one proper-cubic/cyclic orbit; no member invariant under every unit translation | 6 |

The CZ row proves that a simultaneous global coherent circuit can close the
schedule seam without enlarging the local qubit. The iSWAP row proves that
symmetry of the schedule family does not select one noncommuting macro-tick.
Together they isolate gate commutation and clock graining as load-bearing
process content.

## Boundaries

- The finite tensor product, periodic torus, two-qubit gate, all-six-layer
  macro-tick, and computational-basis circuit semantics are explicit inputs.
- The infinite extension uses a supplied quasi-local tensor-product algebra
  and parity origin. Neither is derived from the one-site Qubit axiom.
- This is a genuine one-qubit-site circuit classification inside the two named
  gate families; the framework does not supply that global tensor realization.
- The result does not select iSWAP or CZ, a layer phase, a mixed/randomized
  rule, a clock register, or a physical macro-tick duration.
- It does not classify arbitrary qubit QCAs, other gates, partial schedules,
  larger cells, Hamiltonian exponentials, CAR automorphisms, CP instruments,
  or record-forming dilations.
- It establishes no QCA phase, index, or topological classification. All eight
  iSWAP products are depth-six circuits and lie in one cyclic-conjugacy orbit.
- The CZ automorphism spreads Pauli support but preserves computational-basis
  occupations; it is not an excitation-transport theorem.
- It does not identify either circuit with framework Record formation,
  probability, matter, gauge dynamics, a Hamiltonian, or a continuum theory.
- It does not establish that an axiom update is necessary. Commuting gates,
  clocked partitioned circuits, symmetrization, larger cells, and direct
  Admissibility-to-update realization remain live.

## Falsifiers

- A seventh matching label or a failure of the six layers to partition the
  nearest-neighbor edges for even `L>=6`.
- Two iSWAP schedules with the same `epsilon` but distinct full monomial
  unitaries, or two different `epsilon` values with the same unitary.
- An iSWAP macro-tick invariant under all one-site translations at `L>=6`.
- An iSWAP macro-tick with nearest-neighbor graph radius below six.
- Two CZ schedules with different unitaries, or failure of (6).
- Failure of the exact six-layer identity
  `U_pi(iSWAP)^dag=U_(reverse pi)(iSWAP)`.

## Reproduction

```bash
python3 scripts/cubic_matching_product_qubit_qca_schedule_orbit_2026_07_11.py
```

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  the simple-cubic adjacency and spatial symmetry. The tensor product, gates,
  schedule, and tick interpretation remain named conditional inputs.

Context only: the overlap-order, scalar CAR-QCA, one-particle simultaneous
tick, eta-twisted, and July tick/Admissibility sources. None is load-bearing
proof authority for equations (2)--(16).
