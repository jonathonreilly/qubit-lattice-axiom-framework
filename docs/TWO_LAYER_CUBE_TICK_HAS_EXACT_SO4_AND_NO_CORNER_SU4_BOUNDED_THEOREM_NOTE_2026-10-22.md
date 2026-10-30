---
claim_id: two_layer_cube_tick_has_exact_so4_and_no_corner_su4_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the supplied CL-1 cube tick (two tilings by 2x2x2 cubes offset (1,1,1), hop phases multiplying to -1
  around every unit face, equal edges, mu = 0, no copy mass) carried on two fermion modes per site (Ruleset C, which
  bends the Qubit axiom): the K-independent cell-local commutant is 1_8 x M_2 (number-conserving) plus one staggered
  on-site layer-singlet pairing eps x i sigma_y, a Lie algebra su(2) + su(2) = so(4) of dimension 6; no operator on
  corner labels other than 1 commutes with the tick; at the Dirac point K = 0 the first-order algebra is u(2) + u(2) on
  corners (one layer) and u(4) + u(4) on copy x layer (two layers), broken to the exact algebra at second order, and
  the lattice rotations act on the copy factor, leaving u(2) + u(2) = layer x {1, Gamma}; every hop-phase choice with
  product -1 on every face gives the same algebra up to a site gauge; N identical layers give u(1), so(4), so(6) for
  N = 1, 2, 3. Supplied model; finite diagnostic; no gauge group, chirality, family count or physical species is
  established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/two_layer_cube_tick_has_exact_so4_and_no_corner_su4_2026_10_22.py
---

# The two-layer cube tick has an exact so(4), and its corner labels carry no su(4)

Claim type: bounded_theorem. Runner: runner.py (32 checks, PASS=32 FAIL=0, about 7 s, under 250 MB).

## Question

Ruleset C (brainstorm, 2026-10-22) puts two fermion modes on each site and runs the CL-1 cube tick on both, with face
phase -1 and no copy mass. The hope was that the three corner bits of a 2x2x2 cell give an internal su(4) (three
colours from three axes), that the tick and layer bits give su(2) x su(2), and that corner parity grades 16 against
16-bar. The brainstorm named the decisive test: compute the commutant of the free two-layer tick and ask whether any
su(4) acting on corner labels commutes with both the tick and the rotations.

## Setting (supplied)

- Sites are Z^3, each with two fermion modes (layer bit). This bends the Qubit axiom.
- The cube hop is R = (W_1 + W_2 + W_3)/sqrt 3, where W_i hops along axis i with staggered phases (1, (-1)^x,
  (-1)^(x+y)). These phases multiply to -1 around every unit face, so R^2 = 1 on every cube.
- The tick is U = exp(+i eps R_odd) exp(-i eps R_even), with eps = 0.37 unless stated otherwise. Both layers get the
  same tick, so U_2 = U x 1_2.
- Bloch form uses one cell, which is one even cube: 8 corners x 2 layers = 16 modes.
- Cell-local operators are K-independent matrices.
- Pairing operators sum Delta_ab c_a c_b. They are conserved when U(K) Delta U(-K)^T = Delta for all K.

## Results

1. **The supplied tick (A1-A5).**
   - The phases multiply to -1 around every face, so both hops are reflections and U is unitary.
   - At K = 0 the tick is the identity, U(0) = 1, so all 8 bands are light there. At K = pi(1,1,1) all bands sit at
     |w| = 2 eps.
   - At generic K the bands are two quasi-energies +-w(K), each 4-fold.

2. **The exact commutant (B1-B8).**
   - At a single momentum the commutant only records band degeneracy: dimension 32, 64 and 32 at generic K, K = 0 and
     K = R. So it constrains nothing on its own.
   - Intersecting over momenta, the one-layer dimensions are 32, 16, 8, 4, 2, 1, 1 for 1, 2, 3, 4, 5, 6 and 10 momenta.
     The one-layer commutant is the scalars. Corner parity eps is not in it.
   - Two layers, number-conserving part: exactly 1_8 x M_2(C), the layer U(2).
   - Pairing part: none for one layer. For two layers there is exactly one, Delta = eps x i sigma_y, the on-site
     layer-singlet pair with the corner-parity sign.
   - The conserved charges were checked on the Nambu tick at fresh momenta. They form a Lie algebra of dimension 6,
     rank 2, with no centre and two simple ideals of dimension 3: su(2)_layer + su(2)_pair = so(4). Fermion number is
     the Cartan of su(2)_pair.
   - A site's four states split as (2,1) + (1,2): the odd sector is the layer doublet and the even sector the pair
     doublet. Site parity grades the two Spin(4) spinors. This is the only "16 versus 16-bar" structure present, and it
     belongs to Spin(4), not Spin(10).
   - Mechanism: R_even and R_odd are real and symmetric, and eps anticommutes with both. Hence eps U^T eps = U^-1, so
     eps x A, with A antisymmetric in the layers, is conserved.

3. **Corner labels (C1-C10).**
   - Exact: the only corner-label operator X x 1_layer that commutes with the tick is X = 1.
   - At the Dirac point, keeping only first order in K:
     - One layer: u(2) + u(2) on the 8 corners, which is Dirac(4) x copy(2) with chiral copy U(2)_L x U(2)_R. The
       centre is {1, Gamma}, where Gamma is the emergent chirality and is not corner-diagonal.
     - Two layers: u(4) + u(4) on copy x layer.
     - Second-order terms break both back to the exact algebra.
   - The emergent su(4) needs the layer bit and the copy bit. It does not come from the three axes, and it is not exact.
   - The rotations C4z and C3 about an even-cube centre are symmetries with a cell-periodic site gauge and no K shift,
     so they act on the light states at K = 0. They act on the copy factor. The first-order algebra that commutes with
     them is only span{1, Gamma} for one layer, and u(2) + u(2) = layer x {1, Gamma} for two layers.
   - So no su(4) commutes with both the tick and the rotations, exactly or emergently.
   - This is the brainstorm's spin-versus-taste tension, settled: the corners carry spin x Dirac index x copy, and the
     copy index turns under rotations.

4. **Hop-phase choices (D1-D6).**
   - All six axis orders of the staggered phases, each with a random cell-periodic site gauge, give the same dimensions
     (1, 4, 1).
   - Uniform complex phases e^(i q_i) also keep the face product at -1. They keep the layer U(2) and move the pair to
     total cell momentum 4q. That is a site-gauge image of the same operator, so the algebra is still so(4).
   - Every phase field with -1 on every face differs from another by a site gauge and holonomies, which are K shifts. So
     no admissible choice changes the algebra.
   - Controls:
     - Mass angle mu = 0.2: the same.
     - Face product +1 (R is then not a reflection): (1, 4, 1).
     - eps = 0.11 and eps = 1.2: the same.
     - At the special step eps = pi/2, where U = R_odd R_even, eps joins the one-layer commutant. This reproduces the
       span{1, eps} of the open block-tick note (PR #9884), which uses that step. The algebra becomes su(2)^4, the
       corner algebra stays abelian, and there is still no su(4).

5. **N layers (E1).**
   - N identical layers give 1_8 x M_N plus eps x (antisymmetric N x N), which is so(2N): u(1) for N = 1, so(4) for
     N = 2, and so(6) = su(4) for N = 3 (simple, dimension 15).
   - The internal algebra therefore comes from the layer count, never from the corner labels. An exact su(4) appears
     only when three modes per site are supplied.
   - The rung-1 parallel-cell note (U(8), SO(16) with staggered pairings) is the N = 8 case of the same mechanism.

## Verdict

Ruleset C, as stated (C1 + C2), is dead before any quartic or QMC is run:
- The free two-layer tick has the exact internal algebra so(4) = su(2)_layer + su(2)_pair.
- Its corner labels carry no internal generator.
- The only su(4) is an emergent Dirac-order flavour symmetry of copy x layer. The lattice breaks it at O(K^2) and the
  rotations break it.

CL-1's link rule values links in the update's exact symmetries, so only so(4) could be gauged.

## Gate (anti-smuggling)

- (1) Measured numbers: none chosen. The layer count 2 is supplied, a post-hoc risk as the brainstorm notes.
- (2) Observed structure by name: none written in. The hoped-for SU(4) x SU(2) x SU(2) was a prediction, not an input.
- (3) Prediction not built for: it predicted an exact corner su(4). That prediction is FALSIFIED here.
- (4) Axiom bent: Qubit (two modes per site).

Result: the rule passes the anti-smuggling items but fails its own decisive test. It is reported as a failure and not
adopted.

Re-routing an su(4) through N = 3 layers would supply the colour count by hand, failing item (1)/(2) unless something
forces N.

## What is not claimed

- Interactions: the C3 quartic is not studied.
- Chirality.
- The family count.
- Whether a rule that forces the layer count exists.
- That the exact so(4) is any measured group.

## Used / narrowed

- Used: CL-1 face-phase clause and its R^2 = 1 theorem (face-clause-unification).
- Consistent with: the open block-tick note #9884 (Dirac(4) x copy(2), copy in the E irrep, emergent U(2) broken at
  O(k^2)). Its exact span{1, eps} is specific to its step pi/2. At generic step only the scalars remain (D6).
- Consistent with: the open block-covariance note #9882 (copy U(2) broken by the coin).
- Consistent with: the rung-1 site-so10 and pati-salam drafts (the internal algebra comes from mode multiplicity).
