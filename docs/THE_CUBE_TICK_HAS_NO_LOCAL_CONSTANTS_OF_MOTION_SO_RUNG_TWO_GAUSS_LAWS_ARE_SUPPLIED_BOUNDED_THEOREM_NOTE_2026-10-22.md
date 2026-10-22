---
claim_id: the_cube_tick_has_no_local_constants_of_motion_so_rung_two_gauss_laws_are_supplied_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "CL-1's flat-edge cube tick without links, edge registers or splits (one fermion mode per site, two 2x2x2 tilings, face phase -1, step eps, mass angle mu, copy mass M) is a Gaussian unitary. Exact lemma: a Gaussian unitary has a nontrivial constant of motion supported on a region A, of any degree, iff its one-mode map has a nonzero invariant subspace inside A; checked by brute force on 2 of 5 modes (dimensions 1, 2, 4 as predicted). On an 8^3 torus the largest invariant subspace inside a vertex star, a face plaquette, the 27-site star neighbourhood and boxes of 4^3 and 6^3 sites is zero at five parameter points, including the involution point eps = pi/2. The quasienergy range matches the register band cos w = A S - (cos 2b - cos mu)/2, which is flat iff cos mu = cos 2eps; at mu = 2 eps the even half-tick is the identity and the only local constants of motion lie in single odd cubes. The tick's on-site commutant is one U(1), the mode number. Of the 96 affine classes mod 2Z^3 that keep the two tilings, 24 keep the rung-2 roles up to vertex-cube / edge-face duality, 12 keep them exactly and 6 of those are proper rotations. For qubit rules of one 2x2x2 cube gate on both tilings, keeping every vertex star and face plaquette at every half-tick forces a fixed Pauli on each cube's three edge sites (GF(2) rank 6 on all 16 cubes of a 4^3 torus); the image set under the tick's rotations forces a Pauli on all eight sites (rank 16); 4^3 blocks with two tilings leave every edge site unforced in at least one tiling (72 of 192 forced per tiling, 8^3 torus); 0 of 200 seeded random Clifford cube gates keep the 32 stars and plaquettes over a full tick. No star, plaquette or ice energy follows from the tick or from the least-information involution rule; the gauge group and the statistics are not selected."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_cube_tick_has_no_local_constants_of_motion_so_rung_two_gauss_laws_are_supplied_2026_10_22.py
---

# The cube tick has no local constants of motion, so rung-2 Gauss laws are supplied

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_tick_has_no_local_constants_of_motion_so_rung_two_gauss_laws_are_supplied_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The rung-2 cell-complex draft (emergent-gauge-composite) found emergent Z2 and U(1) gauge structure on one qubit per site of Z^3, read at rung 2, but supplied the star, plaquette and ice energy functions. This note asks whether those functions follow from the update rule: CL-1's cube tick, or the least-information involution rule of the ruleset brainstorm. A Gauss law is a local constant of motion, so the test is the local commutant of the update.

## Statement

1. Lemma (exact). Let U be a Gaussian (free-fermion) unitary on Majorana modes, acting on them by an orthogonal map O. A Majorana monomial of degree k maps to a combination of degree-k monomials, so U X U^dagger = X splits by degree into fixed vectors of the k-th exterior power of O. A fixed k-form lying in the exterior power of the modes on A has an O-invariant minimal support subspace inside A. Hence U has a nontrivial local constant of motion on A, of any degree, iff O has a nonzero invariant subspace inside A. For a number-conserving tick this is an invariant subspace of the one-mode map inside C^A. Brute force on 5 modes, A = 2 modes: commutant dimensions 1, 2, 4 for 0, 1, 2 planted eigenvectors on A, which is the predicted fixed-form count.
2. The CL-1 tick has no local constants of motion (exact on the torus tested). On an 8^3 torus the flat-edge tick (copy gate, even half-tick, copy gate, odd half-tick) is unitary and every cube hop is an involution. The largest invariant subspace inside the vertex star (7 sites), the face plaquette (5), the 27-site neighbourhood, and the 4^3 and 6^3 boxes is 0 at:
   - the involution point eps = pi/2, which is Ruleset A2's parameter-free step;
   - eps = 0.3; eps = 0.3 with mu = 0.1; and the same with copy mass MN = 0.2;
   - one seeded random point.
   So neither the stars nor the plaquettes, nor any other operator on those regions, nor any function of them, is conserved.
3. Where local constants exist (exact). The quasienergy range matches the register band cos w = A S - (cos 2b - cos mu)/2, with A = (cos 2b + cos mu)/2 and S in [-1, 1]. The band is flat iff A = 0, that is cos mu = cos 2eps. At mu = 2 eps the even half-tick is the identity, the quasienergies take two values, and the local constants are exactly the modes of whole odd cubes (8 in the 4^3 box, 64 in the 6^3 box). By the lemma, and because compact localized states need a flat band, this is the only family of local constants of motion. The cubes are decoupled there and nothing propagates, and the constants are cube modes, not stars.
4. What the tick does select (exact). The on-site phase symmetries of the tick are one U(1): the support graph of the one-mode map is connected (512 of 512 sites), and the mode number is conserved. This is the global group that CL-1's link clause ("registers valued in the update's symmetries of matter modes") would gauge. The tick derives the group. The locality of the constraint, the Gauss law at each block, is written into the link clause.
5. Symmetry mismatch (exact count). Mod 2Z^3 there are 96 affine classes that keep the two tilings, 48 per tiling, and 96 that keep the rung-2 roles up to duality. 24 classes do both. 12 keep the roles exactly, and 6 of those are proper rotations: the D3 about the body diagonal. The (1,1,1) offset between the tilings maps vertex sites to cube sites and edge sites to face sites, so the tick's symmetries realise the primal-dual exchange of the rung-2 complex. The tick's rotations about cube centres do not preserve the vertex/edge/face/cube grading. The draft's "24 rotations" are about vertex sites, and those are not symmetries of the two-tiling tick.
6. Margolus freezing (exact, GF(2)). Take any qubit rule of the Ruleset A2 shape: one gate on each 2x2x2 cube, on both tilings. If it keeps every vertex star and face plaquette at every half-tick, then each cube gate must commute or anticommute with the restriction of every star and plaquette to its cube. Products of conserved operators are conserved, so this holds for their whole span. On every cube of both tilings the restrictions span the full Pauli group of the cube's three edge sites (rank 6). So the gate is a fixed Pauli on the edge sites tensored with anything on the other five sites. The gauge sites never evolve and never couple to matter. If the rule is also covariant under the tick's rotations, the conserved set contains the images at every site (rank 16), and every cube gate is a Pauli, so nothing moves. The theorem uses only Pauli expansion, so it holds for any cube gate, not only Clifford ones.
7. Zoom evades the freezing (exact, sufficient condition only). With 4^3 blocks on two tilings offset by (2,2,2) (8^3 torus), 72 of 192 edge sites are forced frozen in each tiling. Every edge site is unforced in at least one tiling. This does not show that a dynamical rule exists there.
8. Full tick (finite diagnostic). 0 of 200 seeded random Clifford cube gates, the same on every cube of both tilings, keep all 32 stars and plaquettes of a 4^3 torus over a full tick. The identity keeps all of them: it is the least-information rule that moves nothing.

## Answers

- (1) The vertex stars and face plaquettes are not the conserved structure of the cube tick. The free CL-1 tick has no local constants of motion at all, except at the decoupled point mu = 2 eps, where its constants are cube modes.
- (2) The least-information update does not conserve Gauss-law stars automatically. The fermionic involution rule (eps = pi/2) conserves nothing local. A 2x2x2 qubit rule can keep them at every half-tick only by freezing the gauge sites, and random Clifford cube gates do not keep them over a full tick. Only the trivial rule keeps them for free.
- (3) The tick selects one global U(1), the mode number. Its local form, a U(1) Gauss law, needs CL-1's link clause. No Z2 or U(1) gauge field is generated. Charge statistics come from the clause "each site's qubit is one fermion mode". Fluxes on registers are bosonic. On the qubit route no dynamics survives, so no statistics are selected.

## Candidate rule and gate

Rule G (UNTESTED): Gauss laws are the local form of the tick's own on-site commutant, carried by registers on blocks of side >= 4, never on the 2x2x2 tick cubes.
1. No measured number is chosen. Pass.
2. No observed structure is named: the group is computed (U(1) per species). Pass.
3. Prediction: no dynamical gauge field lives on the tick's own cubes. This is structural only, with no measured test, so the rule is UNTESTED.
4. It bends no axiom. It restates CL-1's link clause plus the zoom bound.

The gate verdict on the original question: the star, plaquette and ice functions remain SUPPLIED. Deriving them is a failure of both the tick and Ruleset A2 as stated.

## Boundary

- Free tick only. Links, edge registers and splits make the tick interacting, so the lemma does not apply there. With links, Gauss's law is conserved because the dressed hop is written gauge-covariant, which is supplied. The edge-register pair totals are local constants by construction of the register.
- Torus sizes are 8^3 for the fermion tick and 4^3 or 8^3 for GF(2). The A1 regions go up to 6^3. "No flat band away from cos mu = cos 2eps" rests on the cited register band formula, of which A4 checks only the range.
- The freezing theorem assumes conservation at every half-tick. A full-tick, Floquet-type conservation by a 2x2x2 rule is not excluded beyond the random Clifford diagnostic.
- CL-2 (actuality) never changes the odds, so it adds no constant of motion. The least-surprise reading of CL-2 cannot generate a Gauss law.

## Notes used

- Narrowed: emergent-gauge-composite draft (its stars and plaquettes are not tick constants, and its 24 vertex rotations are not tick symmetries).
- Used: the CL-1 text and band formula (register); the Margolus spin-3/2 edge-hop note (cube tick); the info-min-law draft (least-surprise transport = CL-2); the brainstorm-rules Ruleset A2 (involution step).
- Cited on main: the seas' cancellation-zero note (closed stars only on flat bands; a consistent free-fermion statement); the note on what the walk conserves (bond currents, not local charges).
- Literature: Bergman-Wu-Balents PRB 78 125104 (flat bands and compact localized states); Kitaev 2003; Margolus 1984 (partitioned cellular automata).
