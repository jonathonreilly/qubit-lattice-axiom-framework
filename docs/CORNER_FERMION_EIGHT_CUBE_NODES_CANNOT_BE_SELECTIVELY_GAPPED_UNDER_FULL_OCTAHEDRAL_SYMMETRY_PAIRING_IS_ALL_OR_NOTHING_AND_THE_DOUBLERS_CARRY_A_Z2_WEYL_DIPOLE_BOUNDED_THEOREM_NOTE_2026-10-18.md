---
claim_id: corner_fermion_eight_cube_nodes_cannot_be_selectively_gapped_under_full_octahedral_symmetry_pairing_is_all_or_nothing_and_the_doublers_carry_a_z2_weyl_dipole_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model only: the corner fermion of the companion notes (12 corner modes per site of Z^3; flux square = plaquette = tube = pi, triangle = 0; translation-invariant gauge) with the gauge-dressed (PSG) lifts U_g of the 24 site rotations (real signed permutations, cocycle +-1) and the eight-node step W = S R_L U_H U_Lambda of the cross-rung note (item 6), whose node quasi-energy pi/2 carries 2-fold Weyl doublets at the eight cube points (pi/2)(+-1)^3: +-k* (little group O, isotropic) and the six doublers k* + pi e_i, -k* + pi e_i (little group D4, uniaxial). (T1, exact) For every PSG-symmetric translation-invariant Hamiltonian or step, det(U_g restricted to a 2-fold level) is a genuine 1-dim character, the same for every 2-fold level at +-k* and equal to its D4 restriction at every 2-fold level at a doubler; for the real signed-permutation lift it is A2 (B1 on D4), and rephasing the lifts by c(g) with c^2 = A2 relabels it A1 (lift label; the rule below is lift-independent). (T2, exact) A single pair condensate keeping all 24 rotations (U(1)-dressed allowed) has pair momentum Q in {0, R = pi(1,1,1)} and a character chi in {A1, A2}. (T3, exact) At Q = R every cube-point node pairs with itself, the singlet mass at K is allowed only if chi restricted to G_K equals det_K, and A1|D4 != A2|D4; hence chi = det allows it at all eight (generically nonzero) and chi != det forbids it at all eight: no full-O-symmetric pairing channel is selective; the O_h version (A2g, A2u allow all eight with |m_K| = |m_-K|; A1g, A1u forbid all eight) holds as well. (T4, exact enumeration plus numerical illustration) Breaking O, selective on-site Q = R channels exist only for subgroups of order <= 12 (25 subgroup-character pairs; for T exactly the two with chi(C3) = omega, omega-bar, which forbid the singlet at +-k* and allow it at all six doublers); numerically the T-omega channel shifts the +-k* BdG level off zero by delta ~ tau^2, so +-k* is not a protected point node. (T5, exact, using that E1/2 and E5/2 each occur once at k*) a chi = det pairing has zero matrix elements between the +-k* node doublet and every other level, and the particle-hole node 4-space is invariant under the full Floquet-BdG step: +-k* is gapless iff one complex number m_K vanishes, a tuning. (T6, exact given the integer chiralities) Q = 0 pairs K with -K of opposite chirality, so every BdG point carries charge +-2 and no small Q = 0 pairing gaps any node. (T7, exact bookkeeping given the numerically certified integer chiralities chi(k* + pi n) = (-1)^|n| chi(k*)) Weyl dipole b mod 2pi: six doublers pi(1,1,1), {+-k*} pi(1,1,1), all eight 0; only the empty set and all eight are anomaly-free among rotation-invariant subsets; the U(1)^2-Z2 counts equal b/pi mod 2. (T8, conditional on a Hamiltonian reading of the node sector, e.g. a C2-symmetric driving loop, and on Hall-vector quantisation of short-range-entangled states) O forces the total Hall vector to 0, {+-k*} contribute half a quantum per layer, so gapping the doublers alone into a symmetric short-range-entangled state with +-k* gapless is excluded and a compensating sector with b = R (mod 2pi) is required (gapless, topologically ordered or symmetry breaking); the obstruction is Z2-valued since O-invariant b mod 2pi lies in {0, R}. (T9, exact for number-conserving band Hamiltonians with linear 2-fold Weyl doublets; for steps conditional on a C2x-symmetric slice invariant) given translations and the dressed C2x lift (and the O-orbits for the doubler case), an integer slice invariant is incompatible with the level being crossed only at {+-k*} or only at the six doublers. (T10, numerical, uncertified) Floquet-BdG spectra illustrate T3-T6. Not covered: multi-condensate or translation-breaking pairings beyond the stated aside, antiunitary symmetries, a construction of the topologically ordered route, a local Floquet Hamiltonian for the step, other flux patterns or steps, the qubit-code realisation, any physical identification."
upstream_dependencies:
  - corner_fermion_odd_filling_is_forced_gapless_by_anticommuting_gauge_dressed_c2_lifts_bounded_theorem_note_2026-10-18
  - corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18.py
---

# Corner-fermion eight cube nodes cannot be selectively gapped under full octahedral symmetry: pairing is all-or-nothing, and the doublers carry a Z2 Weyl dipole

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited.
- **Exact:** T1–T3, T5, T6 and the bookkeeping of T7, with proofs and finite certificates. The subgroup enumeration in T4 is exact. T9 is exact for band Hamiltonians.
- **Conditional:** T8 on two named premises; T9 for steps.
- **Numerical:** the chiralities (two methods, rounded to integers), the T-ω level shift in T4, and the BdG spectra of T10.

Nothing is adopted.

**Provenance:** campaign block C1 of the scale-ladder campaign (2026-10-18).
- Drafted by a same-model-family worker.
- Checked by a fresh-context same-model-family agent (`C1_check`, PASS = 29), whose corrections are applied here.
- Written up, with a consolidated runner, by a third same-family agent.

None of these is an independent human reviewer.

## Question

The eight-node step has isotropic spin-½ Weyl doublets at ±k* and six uniaxial doublers. Constraint closure rejects the doublers (cross-rung note, item 5). Can they be removed by a gap while ±k* stay gapless, with every dressed rotation kept?

Two routes are examined:
- a superconducting (pairing) mass;
- a number-conserving interacting gap (symmetric mass generation).

## Setting

- **Model.** The corner fermion with the PSG lifts U_g of the 24 site rotations. These are real 12 × 12 signed permutations with U_g U_h = ±U_gh. They act on Bloch fibres by k ↦ M_g k + π s_g, and 21 of the 24 rotations have s_g ≠ 0.
- **Step.** W = S · R_L · U_H · U_Λ, as in the cross-rung note, item 6. At quasi-energy π/2 (the runner's convention) it has 2-fold Weyl doublets at the eight cube points K = (π/2)(±1)³:

  | Orbit | Points | Little group | Cone | Chirality |
  |---|---|---|---|---|
  | {k*} | k* = (π/2)(1, −1, 1) | O | isotropic, √2/3 | χ* |
  | {−k*} | −k* | O | isotropic, √2/3 | −χ* |
  | A | k* + πe_i | D4 about e_i | uniaxial (0.2467 axial, 0.5837 transverse) | −χ* |
  | B | −k* + πe_i | D4 about e_i | uniaxial (0.2467, 0.5837) | +χ* |

  - So χ(k* + πn) = (−1)^{|n|} χ*.
  - χ* = ±1 depends on the momentum and gauge convention: +1 in the runner's repo-model path, −1 in its independent path.
  - The mirror set at −π/2 has the opposite chiralities.
  - That no other momentum reaches π/2 is numerical (cross-rung note).
- **Pairing.** A term Σ_k c_k^T Δ(k) c_{Q−k}, with Δ(k) = −Δ(Q−k)^T, symmetric up to a character χ: U_g Δ(k) U_g^T = χ(g) Δ(M_g k + π s_g).
  - The singlet mass of a node doublet V = span(ψ₁, ψ₂) at K is m_K = ψ₁† Δ(K) ψ₂* (antisymmetric part).
  - The Floquet-BdG step is exp(−iτ[[0, Δ], [Δ†, 0]]) · diag(e^{−iπ/2} W(k), e^{iπ/2} W(Q−k)*).
- **Translations.** On the L = 4 torus, an on-site Q = R pairing is odd under odd translations. The sign is absorbed by the U(1) dressing e^{iπ|e|N/2}, so translations survive only U(1)-dressed (runner A7).

## Result

1. **T1: determinant lemma (exact; certified on 4 + 36 doublets in two implementations).** Let V be any 2-fold level of a PSG-symmetric Hamiltonian or step at a cube point K, with little group G_K.
   - **Character.** det(U_g|_V) is a genuine 1-dim character of G_K.
     *Proof.* U_g commutes with the Bloch operator at K and preserves V. With U_gU_h = ω U_gh and ω = ±1, det(U_g|_V)det(U_h|_V) = ω² det(U_gh|_V) = det(U_gh|_V). ∎
   - **Same at every level at ±k*.**
     - Every 2-fold level at ±k* carries E1/2 or E5/2 of the projective class. The fibre decomposes as E1/2 + E5/2 + 2 G3/2 (cross-rung note, item 2).
     - E5/2 ≅ E1/2 ⊗ A2, so det(E5/2) = A2² det(E1/2) = det(E1/2).
   - **Restriction at the doublers.**
     - The projective irreps of D4 in this class are two 2-dimensional ones, related by a real linear character, so they have equal det.
     - E1/2 restricted to D4 is one of them, so det_K = det_{k*}|_{G_K}. The cocycle is k-independent, so the same one acts at every K.
   - **Which character.** For the real signed-permutation lift it is A2 (B1 on D4).
   - **Lift-label caveat.** "A2" labels this lift. Rephasing U′_g = c(g)U_g with c(g)² = A2(g) gives equally valid symmetries, and for them det = A1 everywhere. The rule in T3 is lift-independent (runner B16). It follows that "only Q = 0, A1 under strictly undressed PSG" is a lift convention, not a physical restriction.
   - **Data.** The runner finds det = A2 at all 4 doublets at ±k* and det = A2|D4 at all 36 doubler doublets, for the eight-node step and four other PSG-symmetric steps and Hamiltonians, three of them random (B2).

2. **T2: pair channels (exact).**
   - **Pair momentum.** Under a dressed rotation the pair momentum maps as Q ↦ M_g Q, because the affine shifts cancel in Q.
     - C4z gives Q_x ≡ −Q_y and Q_y ≡ Q_x, so Q_x = Q_y ∈ {0, π}. C4x gives Q_y = Q_z.
     - Hence Q ∈ {0, R}, R = π(1,1,1). The runner confirms this in integer arithmetic on (π/2)Z³ and (π/4)Z³ (E1, E2).
   - **Character.** U(1) dressing allows any 1-dim character of O: A1 or A2.
   - **Completeness.** This covers a single condensate. A multi-dimensional pair irrep (E, T1, T2) with one component chosen breaks O; that case is T4.

3. **T3: selection rule, all-or-nothing under full O (exact).**
   - **Q = R pairs every node with itself,** since 2K ≡ R for all eight cube points (E1).
   - **Constraint on m_K.** For g ∈ G_K, invariance gives m_K(χ(g) − det_K(g)) = 0. So m_K = 0 unless χ|_{G_K} = det_K.
   - **Hence.** By T1 det_K = det|_{G_K} at all eight K. Since A1|D4 ≠ A2|D4 = B1:
     - **χ = det:** allowed at all eight nodes.
     - **χ ≠ det:** forbidden at all eight.
   - **Consequence.** No pairing channel that keeps all 24 dressed rotations gaps the doublers selectively. This holds for any PSG-symmetric Hamiltonian or step whose node levels are 2-fold.
   - **Certificates.**
     - On-site channel spaces: dim V_A2 = 5 and dim V_A1 = 2, out of 66.
     - Singlets: nonzero at all eight (A2); ≤ 1e−14 at all eight (A1).
     - Random range-1 k-dependent symmetric Δ(k): the same pattern (runner A8, A10, B5, B6).
   - **Tuning.** On V_A2 the eight node-singlet functionals have rank 3.
     - Keeping ±k* gapless needs m_{k*} = m_{−k*} = 0, two complex conditions. Imposing them leaves the six doubler singlets nonzero: an on-site example exists (A9).
     - With inversion it is one complex condition, since |m_K| = |m_−K|.
   - **O_h.** Including the 24 improper lifts (inversion maps K → −K and fixes no node), the channel dimensions are A1g 0, A1u 2, A2g 3, A2u 2.
     - A2g and A2u allow the singlet at all eight, with |m_K| = |m_−K|.
     - A1g and A1u forbid it at all eight (A12, B17).

4. **T4: scope, subgroup channels (exact enumeration; numerical consequence).** Once O is broken, selective channels exist. The runner enumerates all 30 subgroups H of O and all 1-dim characters of each (B18).
   - **Where they occur.** Selective on-site Q = R channels, with the singlet forbidden at ±k* and allowed at some doubler, occur for 25 (H, χ) pairs. All have |H| ≤ 12 (orders 2, 3, 4, 8, 12). None has H = O.
   - **T.** There are exactly two: χ(C3) = ω or ω̄. Each forbids the singlet at ±k* and allows it at all six doublers.
   - **±k* is still not protected (numerical).**
     - In the T-ω channel the node doublet couples to the G3/2 levels: E1/2 ⊗ G3/2 contains E, which contains ω under T.
     - At second order the 4-fold BdG level at ±k* is shifted off zero by δ ∝ τ² (log-log slopes 1.99 and 2.00) and stays 4-fold.
     - The point node therefore becomes a small near-zero region. The check reads it as a Bogoliubov shell. Its probe found exact zeros along only a fraction of directions, so whether it is a closed Bogoliubov Fermi surface or a tiny gap is not resolved.
   - **Hence.** "No selective symmetric channel" needs the scope "full O". The conclusion that ±k* masslessness is a tuning survives.

5. **T5: exact decoupling at ±k*.**
   - **Representation input (runner E5, exact character arithmetic in 2O):**
     - E1/2 ⊗ E1/2 = A1 + T1;
     - E1/2 ⊗ E5/2 = A2 + T2;
     - E1/2 ⊗ G3/2 = E + T1 + T2.
     So a 1-dim pair channel couples a 2-dim node irrep to exactly one 2-dim irrep type, itself or the other, and never to G3/2.
   - **Multiplicity caveat.** E1/2 and E5/2 each occur once at ±k*. So a χ = det pairing couples the node doublet only to itself. A χ ≠ det pairing couples it only to the other 2-dim level (B9).
   - **All orders.** The particle–hole node 4-space is invariant under the full Floquet-BdG step. This holds for range-1 A2 pairing at τ = 1.3 (B10), and the cross blocks are ≤ 1e−14 (A13, B9).
   - **Hence.** ±k* is gapless iff the single complex number m_K vanishes. This is exact for every pairing strength, but it is a tuning.

6. **T6: Q = 0 (exact given the chiralities).**
   - Q = 0 pairs K with −K, which have opposite chirality.
   - Each BdG point therefore carries charge χ_K − χ_{−K} = ±2 (A18). The runner confirms this by Berry flux of the particle and hole sectors: Q = 0 gives ±2 and Q = R gives 0 (B14).
   - So no small Q = 0 pairing gaps any node, doubler or not.
   - Of the eight Q = πp, partner chiralities are equal (gappable) iff |p| is odd. Only Q = 0 and Q = R are rotation invariant (A19).

7. **T7: anomaly table (exact bookkeeping; chiralities numerically certified).**
   - **Chiralities.** These are integers obtained two ways:
     - degenerate perturbation theory, sign det B (path A);
     - Berry flux of the upper band, rounded with residual ≤ 3e−8 (path B).
     The two agree (A4, B11, C2).
   - **Infrared symmetry.** Translations act on the node doublets as e^{ik*·e}(−1)^{n·e}. Removing the common U(1) phase leaves an infrared Z2³ "taste" (A15).
   - **Table.** The Weyl dipole is b = Σ χ_K K mod 2π, which is representative-independent for net-zero sets (A17):

     | Rotation-invariant subset | Net chirality | b mod 2π | U(1)²–Z2 counts mod 2 |
     |---|---|---|---|
     | six doublers (A + B) | 0 | π(1,1,1) | (1,1,1) |
     | {±k*} | 0 | π(1,1,1) | (1,1,1) |
     | all eight | 0 | 0 | 0 |

     Every other nonempty rotation-invariant subset has nonzero net chirality, so it cannot form a gapped sector on its own. Only the empty set and all eight are anomaly-free (A16, B12; integer version E3, for either sign of χ*).
   - **Not independent.** For net-zero sets the U(1)²–Z2 counts equal b/π mod 2 (B13, E3); they are one invariant, not two.

8. **T8: the Z2 Hall form (conditional).**
   - **Premise P1, Hamiltonian reading.** The node sector of the step has a local Hamiltonian description, or a C2-symmetric driving loop, in which a Hall-conductivity vector σ is defined and transforms as a vector under the dressed rotations. The B17 check found no local Floquet Hamiltonian for this step, which is gapless away from ±π/2. So P1 is a genuine premise.
   - **Premise P2, quantisation.** A symmetric short-range-entangled (SRE) gapped state has σ in the reciprocal lattice: an integer number of Hall quanta per layer.
   - **(a) Exact.** O has no invariant vector, so the total Hall vector of an O-symmetric state is 0.
   - **(b) Standard.** A gapless Weyl sector with dipole b contributes σ = b/2π modulo the reciprocal lattice. For {±k*} that is (½, ½, ½) mod Z³: half a quantum per layer along each axis.
   - **(c) Consequence.** Under P1 and P2, the state "±k* gapless, everything else gapped into an SRE state" would have σ ∈ (½, ½, ½) + Z³ ≠ 0. That is a contradiction.
     - So symmetric mass generation of the doublers alone into an SRE state is excluded.
     - So is gapping ±k* alone.
     - A compensating sector with b ≡ R (mod 2π) is required. It can be gapless (the doublers are one realisation), topologically ordered with half-quantised Hall response per layer, or symmetry breaking.
   - **Z2-valued.** O-invariant b mod 2π lies in {0, R} (E1). The "doublers are anomaly-required" wording of the first draft overstated this; what is required is some b ≡ R sector.
   - **Relation to anomaly matching.** The same statement can be phrased as matching of the mixed U(1)–translation anomaly carried by b. That phrasing needs the same premises. This is the field-theory "unquantised anomaly" argument, not a lattice theorem.

9. **T9: free-level slice obstruction.** Assume translations, U(1) and the dressed C2x lift.
   - **Geometry.** C2x has an odd affine shift θ_z = π and reverses the orientation of k_z-slices. An integer slice invariant ν(k_z), defined on slices where the level is not reached, therefore obeys ν(k_z) = −ν(π − k_z) (B15).
   - **Jumps.** Across the plane k_z = π/2, ν jumps by the net chirality J on that plane. The interval (−π/2, π/2) maps to (π/2, 3π/2), so J = 2ν(0) must be even.
   - **Parities (E4).** For a level crossed only at {±k*}, J = ±1. For one crossed only at the six doublers, J = ±1. Both are odd and so impossible. For all eight, J = 0.
     - For general Hamiltonians with linear 2-fold Weyl doublets (|χ| = 1), the chirality pattern follows from net-zero chirality (Nielsen–Ninomiya) and, for the doublers, constancy on O-orbits. Only the parity step uses C2x alone.
   - **Exact for band Hamiltonians.** There ν is the slice Chern number of the bands below the level. A number-conserving, translation- and C2x-symmetric band structure cannot have its Fermi level crossed only at ±k* or only at the six doublers. This is consistent with, and overlaps, the campaign's pointwise result that a pocket-free odd-filling state touches μ at all eight cube points (cross-rung note, items 7–8).
   - **For steps it is conditional.** A single-gap invariant needs a driving loop (a Rudner-type winding number), and the sign relation needs that loop to be C2x-symmetric. A non-symmetric loop shifts ν by a uniform integer and removes the constraint.

10. **T10: BdG illustrations (numerical, uncertified).** Gaps are min |ε| at quasi-energy 0, searched on a grid plus Nelder–Mead refinement.

    | Case | Pairing | C1 (N = 32) | C1_check (N = 20) | Runner `--bdg` (N = 20) |
    |---|---|---|---|---|
    | B1 | Q = R, A2, on-site, τ = 0.5 | all eight gapped, gap 0.098 | 0.055 | 0.0073, 0.045, 0.159 (three draws) |
    | B2 | Q = R, A1, on-site | nothing gapped; ±k* exact 4-fold zero | ±k* exact zero (τ = 0.3, 1.1) | same |
    | B3 | Q = 0, A1, on-site | zeros persist within 0.3 of every node | same at τ = 0.1 | same |
    | B4 | Δ(k) = w(k)·A, w O-invariant, w(±k*) = 0, w = 4 at doublers | ±k* gapless, isotropic BdG cones at √2/3; doublers gapped; outside min 0.11 | doubler gap ≥ 0.366 | doubler gap ≥ 0.109 |
    | B5b | on-site A2 with m_{±k*} tuned to 0 | ±k* gapless for all τ; doublers gapped 0.039 | 0.109 | 0.127 |
    | B5c | B5b + η × generic A2 | k* gap ∝ η (slope 0.99) | slope 1.007 | slope 1.011 |
    | T-ω | T, χ(C3) = ω, on-site | — | doublers gapped 0.061; ±k* shifted δ ∝ τ² | slopes 1.99, 2.00 |

    - Gap sizes depend on the random channel vector. The runner's B1 draw with gap 0.0073 is still clearly gapped, since numerical zeros here are about 1e−12.
    - B4's Δ(k) has strictly finite range; only the exponentiated pairing layer is quasi-local.
    - "No other zero" means none was found on the grid outside 0.35-balls around ±k*.

## What is not excluded

- A topologically ordered gapped doubler sector with half-quantised Hall response per layer. No construction is given. Fractional quantum Hall states in Weyl semimetals (Wang–Gioia–Burkov 2020) make this route plausible in principle.
- Gapping all eight nodes, b = 0. Pairing does it (B1). B7's twisted-torus LSM obstructs only a symmetric SRE state at odd ν, and it is conditional.
- Breaking translations or U(1) beyond the pairing considered here, or breaking O to a subgroup (T4).
- Tuned or form-factor pairings, as in B4 and B5b: ±k* gapless and doublers gapped, at the price of a tuning.

## How this bears on the lane (interpretation, not a claim)

- **Pairing route.** A symmetric pairing mass treats all eight cube points alike. Keeping ±k* massless while the doublers are gapped is a tuning, the Majorana analogue of the Wilson-fermion additive-mass problem. It also costs:
  - U(1): the species become Majorana;
  - undressed translations.
  The cones that survive in B4 and B5b are isotropic at √2/3, so they would pass the cone test numerically. The lapse-coupling premise of the closure route (B22) is still unmet.
- **Number-conserving route.** Under P1 and P2, the six doublers are one realisation of a b ≡ R compensating sector that ±k* require. A symmetric SRE gap for the doublers alone is excluded. A topologically ordered doubler sector is the remaining symmetric gapped option.
- **B7.** The odd-filling note's twisted odd tori (θ = ±k*, L = 1–11) see only ±k* and never the doublers (A20). So B7 forbids a symmetric SRE gapped state of all eight at odd ν (conditionally). It does not forbid "doublers gapped, ±k* gapless", which is gapless.

## Premises

- **Axioms used.** Lattice (Z³, unit translations, cube rotations about sites).
- **Supplied.**
  - The corner model, its flux pattern and gauge.
  - The eight-node step.
  - The pairing term (U(1)-breaking) for T2–T6 and T10.
  - The choice of symmetry: full O, O_h, or a subgroup in T4.
  - For T8, premises P1 and P2.
  - For T9 on steps, a C2x-symmetric slice invariant.
- **Standard facts used.**
  - Projective representations of finite groups and the 2O and 2D4 character tables.
  - Weyl-node charge counting in BdG.
  - Slice Chern numbers and their jumps at Weyl nodes.
  - The Hall response of a Weyl dipole.

## Relation to prior work

Bibliographic details are recalled from memory unless stated; only the two Burkov papers were confirmed by the check's search.

- **Weyl dipole and translation anomaly.**
  - Burkov–Balents, PRL 107, 127205 (2011).
  - Zyuzin–Burkov, PRB 86, 115133 (2012).
  - Wang–Zhang, PRB 87, 161107 (2013).
  - Thakurathi–Burkov (2020).
  - **Gioia–Wang–Burkov, PRR 3, 043067 (2021):** unquantised anomalies and the translation–U(1) mixed anomaly of Weyl dipoles. Confirmed by the check's search.
  - **Wang–Gioia–Burkov, PRL 124, 096603 (2020):** fractional quantum Hall states in Weyl semimetals, relevant to the topologically ordered route. Confirmed by the check's search.
  - Sehayek–Thakurathi–Burkov: named by the check only.
- **Symmetric mass generation.**
  - Wang–You (2022); Tong (2022); Razamat–Tong (2021).
  - Fidkowski–Kitaev (2010), interacting reduction.
- **Mirror fermions.** Eichten–Preskill (1986); Golterman–Petcher–Rivas.
- **Lattice fermions.** Staggered taste (Kogut–Susskind 1975); the Wilson additive-mass problem; Curci–Veneziano (1987); Nielsen–Ninomiya (1981); Karsten–Smit (1981).
- **Weyl superconductivity.** Cho–Bardarson–Kim–Moore (2012); Meng–Balents (2012); Bednik–Zyuzin–Burkov (2015); Li–Haldane (2018).
- **Standard ingredients.**
  - Double-group character tables (Bradley–Cracknell 1972; Koster et al. 1963).
  - 3D Hall quantisation in the reciprocal lattice (Halperin 1987).
  - Floquet winding numbers (Rudner–Lindner–Berg–Levin, PRX 3, 031005 (2013)).
- **New here,** for this model:
  - the determinant lemma in the gauge-PSG setting and its lift-label caveat;
  - the all-or-nothing rule under full O, with its subgroup scope;
  - exact decoupling at ±k*;
  - the eight-node dipole table, giving a Z2 obstruction;
  - the C2x-only slice parity;
  - the observation that B7's twisted tori see only ±k*.
  The anomaly argument itself is the known one.

## No-Go Discipline Gate

- **N1 — routes not covered.**
  - Multi-condensate pairings with O restored on average.
  - Pair-density waves at Q ∉ {0, R}, which break O.
  - Translation-breaking masses beyond the printed CDW aside.
  - Antiunitary symmetries.
  - Explicit construction or exclusion of a topologically ordered doubler sector.
  - Non-free number-conserving deformations other than symmetric SRE gapping.
  - Other steps, flux patterns, or the qubit-code realisation.
- **N2/N3 — scope.**
  - **T3** is quantified over every single-condensate pairing (on-site or any range) that keeps all 24 dressed rotations, possibly U(1)-dressed, of any PSG-symmetric Hamiltonian or step whose cube-point node levels are 2-fold. T4 shows that the scope "full O" is necessary.
  - **T5** needs E1/2 and E5/2 to occur once each at ±k*.
  - **T8** is conditional on P1 and P2.
  - **T9** is exact for band Hamiltonians and conditional for steps.
- **N4 — inputs.**
  - The character and null-space statements are floating-point linear algebra whose outputs are constrained to ±1 or to exact zeros (≤ 1e−14), plus integer arithmetic (E1–E4).
  - The chiralities are rounded integers from two methods.
  - The BdG gaps are uncertified grid searches.
- **N5 — wording.**
  - "Gapped" and "gapless" refer to the Floquet-BdG quasi-energy 0 (and π) or to the node quasi-energy of W.
  - "Selective" means gapping some but not all cube-point nodes because of a symmetry.
  - "Half a quantum per layer" refers to the Hall vector b/2π in lattice units.
  - "Taste" is the infrared Z2³ of translations after removing the U(1) phase. No species identification is implied.
- **N6/N7 — strongest objections.**
  - T8 rests on a Hamiltonian reading that the check could not supply for this step.
  - The anomaly argument is field-theoretic.
  - The topologically ordered route is open.
  - The BdG numerics depend on draws and grids.
  - The lift label could mislead if read as physical.
- **N8 — earlier claims.**
  - The note uses the PSG lifts, the k* decomposition and the eight-node step of the cross-rung note, and the twisted tori of the odd-filling note.
  - It changes neither.
  - It corrects the first-draft wording "doublers anomaly-required" to "some b ≡ R sector required".

## Independent check

A fresh-context agent of the same model family checked the C1 findings (`.claude/science/physics-loops/scale-ladder-campaign-20261018/C1_check/`: REPORT.md, chk*.py and logs; PASS = 29, FAIL = 0). It is not an independent human reviewer. It used its own code:
- the model rebuilt on a copy of `B7_check/chk_core.py`, with its own GF(2) gauge and a brute-force PSG over all 2¹⁵ (λ, τ) per O_h element;
- pairing built in real space;
- chiralities from Berry flux rather than degenerate perturbation theory.

Two of its first-run failures were its own wrong expectations, and it fixed a complex-conjugation bug before the final run.

- **Confirmed.**
  - The determinant lemma for five PSG-symmetric models.
  - The selection rule for full O and O_h.
  - The completeness of Q ∈ {0, R} for one condensate.
  - Decoupling (≤ 1e−14; node 4-space BdG-invariant).
  - The numbers in the anomaly table.
  - BdG cases B1, B2, B4, B5b and B5c, qualitatively.
- **Corrections applied here.**
  1. The lift-label caveat (T1). As a result, "undressed PSG allows only Q = 0, A1" is a lift convention.
  2. The subgroup scope (T4): selective channels exist once O is broken, but ±k* is still not protected.
  3. The multiplicity caveat for decoupling (T5).
  4. Three changes to the anomaly discussion:
     - the counts equal b/π, so they are not independent;
     - the cleaner Z2 Hall form (T8) is used;
     - the missing Floquet premise P1 is named;
     "anomaly-required doublers" becomes "some b ≡ R sector required".
  5. B4's Δ(k) has strictly finite range; only the exponentiated layer is quasi-local.
- **Added from the check.** The slice obstruction (T9, check L1) and the subgroup enumeration.
- **Runner provenance.**
  - The runner's section A follows the C1 worker's code path: the repo model, as in the cross-rung runner, with degenerate perturbation theory.
  - Section B follows the checker's code path: own gauge and PSG, Berry flux.
  - Agreement between A and B (section C) is implementation-level independence of the load-bearing linear algebra. It is not independence of reasoning: all three agents are of one model family.
  - Under `--bdg`, the first runner version required node gaps > 1e−2 in case B1 and failed on its random draw (0.0073). The criterion was changed to 1e−3 with three draws, and all values are reported (T10).
- **Not re-checked in the runner.**
  - C1's N = 32 BdG grids.
  - The probes on the T-ω near-zero region and on the Q = 0 zero displacement.
  - The translation-breaking CDW aside.

## Verification

```bash
python3 scripts/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18.py
python3 scripts/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18.py --bdg
```

- Default: `TOTAL: PASS=46 FAIL=0`, about 30 s on 4 cores. It covers sections A, B, E and C.
- With `--bdg`: `TOTAL: PASS=53 FAIL=0`, about 1 min. It adds the seven numerical BdG spot checks of section D.

Campaign scripts, all ending with FAIL = 0:
- `.claude/science/physics-loops/scale-ladder-campaign-20261018/C1_gap_the_doublers/` (PASS = 29);
- `.../C1_check/` (PASS = 29).

## Load-bearing sources

- [Odd-filling note (anticommuting C2 lifts, twisted tori)](CORNER_FERMION_ODD_FILLING_IS_FORCED_GAPLESS_BY_ANTICOMMUTING_GAUGE_DRESSED_C2_LIFTS_BOUNDED_THEOREM_NOTE_2026-10-18.md)
- [Long-wavelength note (affine action, k*)](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- Context, not a dependency: the scale-ladder cross-rung note (companion PR #9702; `SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md`) defines the eight-node step and the k* decomposition used for illustration.
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
