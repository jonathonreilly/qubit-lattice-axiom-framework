---
claim_id: one_qubit_site_monomial_rotations_make_c4_invariant_charges_bosons_fermions_need_a_cluster_gauge_or_a_spread_charge_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Supplied class: commuting Pauli stabilizer codes on one qubit per site of Z^3 with no local logical operators. A rotation acts monomially if it moves each site's qubit to the image site with at most a single-site Clifford, a Pauli frame and a phase. Exact: (1) for a monomial involution s and any Pauli P, omega(P, sP) is the sum over fixed sites of omega(P_x, c_x P_x). (2) All 10 homomorphisms O -> S3 = Sp(2,2) and every C4 -> S3 kill the square of a C4. So an axis C2 relabels no site of its axis, and [P, R P] = +1 for every Pauli P. (3) For a C2 R preserving the code, with legs T1, T2 = R T1 and T3 on the axis whose excitations at the junction and at the far end of T3 are R-invariant, the Levin-Wen sign is theta = lambda_R sigma_R, with lambda_R = [T1, R T1] and sigma_R = [T1, T3 R(T3)]. If R = Q^2 for a C4 Q that preserves those excitations, sigma_R = +1. (4) Hence, under a monomial C4 action about a point, every charge with a C4-invariant local excitation is a boson. That includes the vertex-star charge of any rotation-covariant twisting of the rung-2 composite toric code, and the 'one Majorana per direction' structure cannot be realised at one qubit per site. Checks: 3000 seeded lemma instances; 4^7 star strings; a D3-invariant BKSF code on an L = 14 edge torus with GF(2)-solved C2-invariant dressings gives theta = -1, lambda = +1, sigma = -1 for the edge C2. Positive model, one qubit per fine site: 7-site stars at 3Z^3 carry 12 Jordan-Wigner Majoranas on their 6 arm sites. B = Z on the arms (a nearest-neighbour star), R = ZZ on fine nearest-neighbour arm pairs, and S = BKSF plaquettes (diameter 8 fine steps). The terms commute, log2 dim = 3 at coarse L = 3 and 4, and the charge is a fermion (theta = -1). All 24 rotations preserve the code when they act by a star-local Majorana permutation (non-monomial); the bare permutation preserves 6 of 24. There lambda(axis C2) = -1 and sigma = +1. Not claimed: non-Pauli commuting projectors (Walker-Wang), charges with no C4-invariant excitation (shell-spread), dynamics, or any physical identification."
upstream_dependencies:
  - minimal_axioms
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
  - majorana_per_direction_cubic_fermion_code_has_one_species_covariant_under_all_cubic_rotations_bounded_theorem_note_2026-10-17
  - site_localizable_stabilizer_code_fermion_cannot_carry_the_spin_half_class_direction_shell_bounded_theorem_note_2026-10-17
  - one_qubit_cubic_covariant_nearest_neighbour_stabilizer_rules_have_no_three_dimensionally_mobile_defect_bounded_theorem_note_2026-10-17
runner: scripts/one_qubit_site_monomial_rotations_make_c4_invariant_charges_bosons_fermions_need_a_cluster_gauge_or_a_spread_charge_2026_10_22.py
---

# With one qubit per site, single-site rotations make every C4-invariant point charge a boson: fermions need a cluster gauge or a spread charge

Claim type: bounded_theorem.

## Question

The rung-2 composite cell complex (draft emergent-gauge-composite, PR #10021)
gives an emergent Z2 gauge theory with nearest-neighbour stars that is
invariant under all 24 rotations, but its charge is a boson. Its fermionic
(BKSF) twist keeps only 6 of 24 rotations. Is there a one-qubit-per-site,
rotation-covariant commuting rule with a fermionic point charge? Or does
something forbid one?

## Setting

- Commuting Pauli stabilizer codes on qubits at the sites of Z^3, one per
  site, with no local logical operators (a zero-syndrome local Pauli is a
  stabilizer).
- A rotation acts **monomially** if it sends the qubit at x to the qubit at
  Rx, with at most a single-site Clifford c_x, a Pauli frame and a phase.
  This is the strict reading of "rotations move sites". "Up to the gauge"
  read as a single-site relabelling is included.
- The rotations form a group action: R^2 is a phase or a Pauli frame.
- The excitation of a Pauli T is its character g -> [T, g] on the stabilizer
  group, read near a point.

## Results

1. **Involution lemma (exact).** For a monomial involution s and any Pauli P,
   omega(P, sP) = sum over the sites fixed by s of omega(P_x, c_x P_x).
   Swapped pairs cancel because c and c^-1 preserve omega. With a bare
   permutation, P and sP always commute.
2. **Axis C2 relabels nothing on its axis (exact).** Single-qubit Cliffords
   modulo Paulis and phases form Sp(2,2) = S3.
   - The stabilizer of a site x acts on x's labels through a homomorphism
     Stab(x) -> S3.
   - Every site on a C4 axis is fixed by the whole C4, and every
     homomorphism C4 -> S3 kills the square.
   - At the rotation centre, all 10 homomorphisms O -> S3 kill the three
     axis C2. Their kernel contains V4.
   - So for an axis C2 R, [P, R P] = +1 for every Pauli P.
   - An edge C2 can relabel the sites on its axis: 9 of the 10
     homomorphisms move it.
3. **Lattice spin-statistics identity (exact).** Let R be a C2 about a point
   p that preserves the code. Take three legs (hop products moving the charge
   out of p): T1, T2 = R T1, and T3 along the R axis to a point F. Their
   excitations near p, and the excitation of T3 near F, are R-invariant.
   Write S3 = T3^-1 R(T3); it is a stabilizer, since it is zero-syndrome and
   local. Then

   theta = [T1,T2][T1,T3][T2,T3] = lambda_R * sigma_R,

   with pair sign lambda_R = [T1, R T1] and axis sign sigma_R = [T1, S3].

   Proof:
   - [T2,T3] = [R T1, T3] = [T1, R T3] = [T1, T3][T1, S3].
4. **C4 kills the axis sign (exact).** Suppose R = Q^2, where Q is a C4 about
   the same axis that preserves the excitations at p and F. Then
   sigma_R = +1.

   Proof:
   - Write Q(T3) = T3 S_Q, with S_Q a stabilizer. Then
     R(T3) = T3 S_Q Q(S_Q), so S3 = S_Q Q(S_Q).
   - [T1, Q(S_Q)] = [Q^-1 T1, S_Q]. Here Q^-1 T1 is a leg along another
     perpendicular direction, with the same excitation near the axis.
   - [X, S] for a stabilizer S depends only on X's character on generators
     near S, and S_Q lives near the axis. So [Q^-1 T1, S_Q] = [T1, S_Q].
   - Hence sigma_R = [T1, S_Q]^2 = +1.
5. **Theorem (from 2–4).** Under a monomial action of a C4 about a point p,
   any point charge with a C4-invariant local excitation at p (and at its
   translates along the axis) has theta = lambda * sigma = (+1)(+1): it is a
   **boson**. The cases covered include:
   - (a) A site or cube centre with the full cubic group O, and face or edge
     centres with D4.
   - (b) Every rotation-covariant twist of the rung-2 composite toric code
     whose charge is a violated vertex-site star (an O-invariant
     excitation). No such twist can be fermionic while the rotations stay
     monomial.
   - (c) "One Majorana per direction" (six mutually anticommuting operators
     permuted by O) cannot exist at one qubit per site, because
     gamma_{+a} and gamma_{-a} are swapped by an axis C2 (checked
     exhaustively on the 7-site star). The covariant Majorana-per-direction
     code on main needs a three-qubit on-site Clifford.
6. **Checks on known fermion codes.**
   - D3-invariant BKSF code, bare permutations, L = 14 edge torus: the
     ordering x+ x- y+ y- z+ z- is invariant under C3(111) and C2(1,-1,0).
     The plain hop legs are not C2-covariant: the rotated axis leg violates
     16 plaquettes. Local dressings solved over GF(2) make the junction and
     far-end excitations C2-invariant. The results are theta = -1 (the bare
     and dressed T-junctions agree), lambda = +1 (no qubit lies on an edge-C2
     axis) and sigma = -1. The edge C2 carries the statistics, consistent with
     the spinorial class in the main bare-permutation note. D3 has no C4, so
     item 5 does not apply.
   - An earlier dressing that constrained only generators fully inside a
     ball gave a spurious +1 because it left excitations outside the ball.
     The runner now checks the whole torus.
7. **Positive composite model (exact; supplied).** One qubit per fine site.
   - Coarse vertices sit at 3Z^3. Each coarse vertex owns a 7-site star; its
     6 arm sites carry 12 Majoranas in a Jordan-Wigner order fixed inside the
     star. The other 20 of every 27 sites are idle, fixed by single-site Z.
   - Terms:
     - B = Z on the six fine nearest neighbours of the vertex site;
     - R = ZZ on the fine nearest-neighbour arm pairs of adjacent stars;
     - S = BKSF plaquettes over 4 stars (fine diameter 8).
   - Checks:
     - the terms commute;
     - log2 dim = 3 at coarse L = 3 and 4;
     - the T-junction is -1, so the vertex charge is a fermion;
     - all 24 rotations preserve the code when they move stars and permute
       each star's Majoranas as directions;
     - the bare permutation preserves only 6 of 24.
   - The gauge is a star-local Clifford, not monomial: X on one arm maps to
     a 2-site Pauli. In line with item 3, lambda(axis C2) = -1 and
     sigma = +1, so the statistics rides on the cluster gauge.
   - The fermion's axis-C2 class here is the non-spinorial one, as in the
     Majorana-per-direction note (A4 x| Z4, eta(axis C2) = +1).

## Reading (interpretation, not claimed)

- With one qubit per site and rotations that move single sites, a fermion
  cannot be a C4-symmetric point defect. It can be fermionic in two ways:
  - **Spread composite.** The charge has no C4-invariant excitation, and the
    statistics sit in the axis sign sigma = -1: under a 180-degree axis
    rotation it is spinorial. Main finds the same signature in the corner
    code's shells (E1/2 + ...).
  - **Cluster gauge.** The rotation acts by a cluster Clifford, which
    reaches full O but gives a non-spinorial axis class.
- The first way joins exchange sign -1 to "half-turn squares to -1" (a
  lattice spin-statistics link). It is also what the composite-before-atomic
  principle suggests.
- No construction of the spread-composite type with a monomial O action is
  given here. That is the open problem this narrows the search to.

## Anti-smuggling gate

- **The theorem.** It is not a rule, so the gate does not apply, and it uses
  no measured input.
- **Candidate reading AX-monomial.** The rule "a rotation moves each site's
  qubit with at most a single-site relabelling" bends no axiom; it sharpens
  the covariance reading of Lattice + one qubit per site.
  - (1) No fitted numbers.
  - (2) No observed structure is named.
  - (3) An unbuilt-for prediction: every emergent point fermion is a
    spread composite, and its axis-C2 sign is -1. That is half-integer-spin
    behaviour under half-turns, consistent with the measured spin-1/2 of
    all elementary fermions. It is UNTESTED beyond the BKSF and composite
    checks.
  - (4) It bends no axiom.
  - Result: PASS as a candidate reading; it is not adopted.
- **The positive composite model.** It FAILS as an electron candidate.
  - Its covariance needs a cluster gauge, so it bends the strict reading.
  - It is supplied: Jordan-Wigner order, star placement and idle sites.
  - Its fermion is not spinorial under axis C2, against the measured
    spin-1/2.
  - It is kept as an existence proof only.

## Boundary

- Pauli stabilizer codes only. Non-Pauli commuting projectors such as
  Walker-Wang models with an sVec input are not covered. Walker-Wang on the
  cubic lattice also needs a framing or projection choice.
- Not covered: actions twisted by non-Clifford functions of the stabilizers,
  such as W = prod exp(-i pi B/4), and charges whose minimal excitations are
  not C4-invariant.
- The dressing step in item 6 is a finite GF(2) solve on one code. Items
  1–5 are proofs, checked on finite instances.

## Notes used

- Narrowed / extended:
  - ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT.
    Main covers star supports; this note covers any support under C4.
  - SITE_LOCALIZABLE_STABILIZER_CODE_FERMION_CANNOT_CARRY_THE_SPIN_HALF_CLASS.
    Item 3 is an exact Pauli-code form of the lambda = theta eta relation
    that main uses conditionally.
- Reproduced:
  - BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR
    and BKSF_..._BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY (lambda = +1
    under bare C2, edge C2 spinorial).
- Explained:
  - MAJORANA_PER_DIRECTION_CUBIC_FERMION_CODE (why it needs an on-site
    three-qubit Clifford).
  - BKSF_..._SIX_DIRECTION_QUBITS_PER_SITE (its on-site Clifford is the
    cluster gauge of item 7).
  - CORNER_FERMION_QUBIT_CODE (CZ networks = a cluster gauge; its spinorial
    shells = the spread route).
- Campaign: emergent-gauge-composite draft (PR #10021).
- Literature: Levin-Wen PRB 67 245316; Bravyi-Kitaev 2002; Chen-Kapustin
  PRB 100 245127 (spin-structure dependence of 3D bosonization).
