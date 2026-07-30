# Cycle 822 Route B: typed-spectator radius-one synthesis

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Runner:**
[`scripts/frontier_cycle822_route_b_radius_one_parity_even_synthesis_2026_07_30.py`](../scripts/frontier_cycle822_route_b_radius_one_parity_even_synthesis_2026_07_30.py)

**Landed input:**
[`LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md`](LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md)

**Other declared dependencies:**
[Cycle 720](RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md)
and [Cycle 789](THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md).

## Controlled claim

On the four finite Cycle-789 fixtures `(2,1,1)`, `(3,1,1)`, `(3,2,2)`, and
held `(5,3,2)`, every one of the 328 landed recurrent seam Pauli factors has
an explicit radius-one synthesis preserving the single Cycle-821 grading

\[
P_{\rm ext}=P_{\rm matter}\prod_c Z_c.
\]

The construction uses no clean seam accumulator. It separately reduces
charged matter letters with an arbitrary-state charged matter spectator and
neutral companion letters with an arbitrary-state neutral companion
spectator. If one charged and one neutral Z residue remain, an adjacent
charged-neutral `R_ZZ` quarter rotation supplies the joint phase. The
reduction is then uncomputed, returning both spectators for arbitrary joint
input states.

The maximum signed phase residual is `1.6256328932926792e-15`. All 328 source
rows reconstruct exactly, the maximum source support is 17 M2, the maximum
routed word is 2,461 radius-one primitives, and the maximum route distance is
28. There are zero Cycle-821 matter-parity-odd reduction generators, typed
route prefix failures, charged/neutral lane overlaps, or route-return
failures.

This is a finite supplied-program theorem. It is not a translation-invariant
routing law or an autonomous recurrent law.

## Required correction to the first reduction

The initially tempting reduction treated every M2 as charged. Replaying it
against the actual Cycle-821 grading gives 2,616 matter-parity-odd generators
among 3,760 generators:

| shape | odd | total |
|---|---:|---:|
| `(2,1,1)` | 12 | 16 |
| `(3,1,1)` | 24 | 32 |
| `(3,2,2)` | 672 | 968 |
| `(5,3,2)` | 1,908 | 2,744 |

That route is rejected. The positive construction pairs X/Y and reduces Z
only within one fixed type. When both types survive, it does not retype either
one; it applies the exact cross-type diagonal phase. This is a route repair,
not a no-go or substrate claim.

## Local dictionary and exact controls

The supplied adjacent dictionary is:

- onsite `RZ(theta)`;
- number-conserving `SWAP`;
- `CZ`; and
- parity-block `R_Q(pi/2)` for `Q` in `XX`, `XY`, `YX`, `YY`, or `ZZ`.

The four X/Y rotations conserve parity but are not exact particle-number
conserving: their number-commutator residual is `2`. The maximum dictionary
unitarity residual is `4.463374267214424e-16` and its parity residual is zero.
The Cycle-821 controlled-pair atom reconstructs with residual
`6.312164422641715e-16` and zero prefix-parity residual.

Deleting the axis rotation, changing its sign, or deleting the first forward
quarter rotation gives minimum residuals `0.7653668647301789`,
`1.4142135623730911`, and `0.7653668647301777`. Deleting route returns leaves
6,864 label mismatches. These are active route controls, not impossibility
evidence.

## Honest spatial overhead

The same finite compilation assigns every blank route-work coordinate a fixed
charged or neutral type. These are real physical M2 overhead even though they
carry no additional persistent state:

| shape | charged work | neutral work | total | per cell | per edge |
|---|---:|---:|---:|---:|---:|
| `(2,1,1)` | 35 | 17 | 52 | 26.0 | 52.0 |
| `(3,1,1)` | 60 | 34 | 94 | 31.33 | 47.0 |
| `(3,2,2)` | 1,412 | 495 | 1,907 | 158.92 | 95.35 |
| `(5,3,2)` | 3,793 | 1,337 | 5,130 | 171.0 | 86.95 |

No asymptotic scaling or minimum-resource claim is made. The A* search is
bounded to an eight-site fixture margin and 250,000 expansions per macro; the
largest observed count is 432.

## Covariance disposition

Affine transport of the already-computed program is exact for all 24
proper-cubic frames, eight tested origins, and 576 ordered frame products.
Uniform-translation recomputation is exact in 8/8 contexts.

The compiler itself is not proper-cubic covariant: only 1/24 frame
recomputations reproduce the identity-frame paths, with 16,340 macro
mismatches. Twelve normalized cross-shape template groups have 148 instance
mismatches. Therefore the finite A* atlas is supplied program structure, not a
translation-invariant local law.

## Supplied, derived, and open

Supplied:

- the landed finite O/I/L fixture, carrier, code domain, and semantic seam
  rows;
- the adjacent `R_Q` and `R_ZZ` dictionary;
- the bounded finite-box A* atlas, blank typed route-work M2, chart, and serial
  occurrence; and
- the total-parity domain.

Derived:

- type-preserving dirty-spectator reduction and exact uncompute;
- all 328 signed seam rotations with fixed Cycle-821 parity at every prefix;
- explicit radius-one returned routes and active deletion/sign controls; and
- the exact separation between transported-program covariance and compiler
  recomputation.

Open:

- a translation-invariant proper-cubic route generator and parallel recurrent
  schedule;
- derivation of the adjacent rotation dictionary from a more primitive fixed
  M2 law;
- the 29-per-cell nonseam recurrent factors, pump/Bell row assembly, genesis,
  enforcement, renewal, and autonomous occurrence; and
- time, source/gravity, Record/Born/history, and prediction bridges.

No no-go, minimum-content, or axiom-pressure claim is made.
