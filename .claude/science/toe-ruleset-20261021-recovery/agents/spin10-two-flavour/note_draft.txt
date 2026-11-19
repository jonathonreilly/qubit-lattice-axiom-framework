---
claim_id: the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "One site with two 16s of Spin(10) (32 complex modes c_{i alpha}, i = 1,2, Fock 2^32). With B_a = c_1^T M_a c_2 (M_a = (C Gamma^a)|_16, symmetric), the operators {T_ab, B_a, B_a^+, J = (N-16)/2} close into so(12) (66 generators, exact), the flavour SU(2) commutes with them, and sum_a {B_a, B_a^+} = 2 [144 - 2 S(S+1) - C2_10 - J^2] exactly (checked on the N <= 2 sectors, which is complete for number-conserving degree-4 operators). So C2(so12) = 144 - 2 S(S+1), and H_sym = -(g/2) sum_a {B_a, B_a^+} = -g F with F = 144 - 2S(S+1) - C2_10 - J^2. Ground state: unique at -144 g, N = 16, Spin(10) singlet, flavour singlet, particle-hole even. Gap 4 g, to the Spin(10)-singlet flavour-singlet states at N = 16 +- 4. Pair level B^+|GS> at 10 g, fermion level c^+|GS> at 13 g (exact eigenstates). Within fixed N = 16 the gap is >= 16 g. The naive ordering -g sum B B^+ = H_sym + 5 g (N - 16) has a two-fold charged ground state (N = 4, 8) at -168 g, so the particle-hole symmetric ordering (or a tuned chemical potential) is required. The two flavours enter only through the epsilon pair: for the two spin components of one Weyl 16 this is the Lorentz-scalar 10 bilinear. Contrasts: 16 x 16bar contains no 10 (the channel vanishes; a quadratic Dirac pairing is allowed, vector-like); 15 + 15 (no nu^c) has no unique particle-hole symmetric level (exact). Reduced Spin(6) analogue (2^8, full diagonalisation): identity exact, unique GS, gap 4 g, fermion gap 5 g. Slab (free model): a two-layer far region holds > 0.99 of the wall mode at k <= pi/8, yet freezing r = 1..4 far layers into a gapped product moves the branch r layers in with E = sin k unchanged. Not covered: inter-site hopping at finite g, the interacting slab, gauge fields, the continuum limit."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_forced_far_wall_term_has_a_unique_gapped_three_site_cell_state_but_a_strong_coupling_cell_only_moves_the_mirror_and_the_one_orbital_sixteen_site_has_only_two_spin10_singlets_bounded_theorem_note_2026-10-23
runner: scripts/the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_2026_10_23.py
---

# The Spin(10) pair square on two 16s is a Spin(12) Casimir with a unique singlet ground state and gap 4 g, but a frozen far region still moves the mirror

Claim type: bounded_theorem. Exact statements are labelled [T] and finite diagnostics [F].
Runner: runner.py, TOTAL: PASS=16 FAIL=0, 25 s, 113 MB peak, 4.5 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was run under a unique filename (scratch/spin10_two_flavour_test_run.py). Axioms unchanged. No rule adopted.

## Question

smg-strong-coupling (part D) showed that one orbital carrying the 16 has only two Spin(10) singlets (|0> and |F>), and
that its 10-channel term psi^T C Gamma^a psi vanishes by Pauli. With TWO 16s per site (psi_1, psi_2, 32 modes), take the
fewest-change Spin(10)-invariant four-fermion term, the 10-channel pair square. Then:
- express it through Casimirs;
- decide whether the ground state is unique and singlet;
- give the gap;
- name the symmetry it needs;
- contrast it with 16 + 16bar and 15 + 15;
- map it to the slab.

Repo first. This builds on:
- smg-strong-coupling (one-orbital 16, the 15 parity obstruction, A7 relocation, the free slab model reused here);
- block-quartic-smg (Spin(10) needs two orbitals and then gives exactly the pair square);
- the register's candidate unification law. Its statement "32 mirror modes under the pair square have a unique ground state
  ... gap 19.1 g, fermion gap 33.6 g (multiplicity-free so(12) x SU(2))" is for the charge-4 pair square
  Omega = sum B_a B_a + h.c. That is a different Hamiltonian, so it is neither recomputed nor contradicted here. The so(12)
  structure is the same, and this note gives it as an exact identity.
- main SPIN10_SYMMETRIC_ATOMIC_GAPS_..._NOTE_2026-09-14 (a supplied projector atom on 2 or 4 copies; its B_a matches the
  pair used here, epsilon over spin slots).
New here:
- the so(12) closure;
- the identity C2(so12) = 144 - 2 S(S+1);
- the closed-form spectrum and gaps for the number-conserving pair square;
- the ordering result;
- the 15 + 15 theorem;
- the two-layer relocation check.

## Pass criteria

The criteria were written before any run. They are in criteria_pre_run.txt; all targets were analytic predictions.
Two corrections were made after the run:
- E2 wording: "layer Ls - 2" was a typo for the third layer from the far end (index Ls - 3). The criterion's intent is
  unchanged.
- C4: no flavour-triplet singlets exist at N = 16, so the F = 140 level comes from N = 16 +- 4 only.

## A. One-body algebra (exact)

- A1 [T]. The 16 is built from five oscillators: 45 generators with Casimir 45/4. M_a = (C gamma_a)|_+ is symmetric and
  unitary, and span{M_a} carries the vector (Casimir 9).
- A2 [T]. Because M_a is symmetric, c_1^T M_a c_1 = 0. B_a is therefore the epsilon (flavour-antisymmetric) pair, and SU(2)
  flavour commutes with T, B, B^+ and J. When the two flavours are the two spin components of ONE Weyl 16,
  B_a = eps^{st} psi_s^T C Gamma^a psi_t / 2 is the Lorentz-scalar 10 bilinear. That is the Higgs-10 channel of
  You-He-Xu-Vishwanath 2018.
- A3 [T]. The 66 operators {T_ab, (B + B^+)/2, i(B - B^+)/2, J} are independent and closed. They satisfy the so(12)
  relations exactly:
  - so(12) = so(10) + u(1) + 10_{+1} + 10_{-1};
  - checked in the 64 x 64 Nambu representation, where it is a homomorphism.
- Structure: in the frame d = c_2^+, the modes (c_1, d) are the 32 of Spin(12), which is pseudoreal. Flavour SU(2) is the
  Lefschetz sl(2) of its symplectic form, and the Fock space is sum_p Lambda^p_0(32) x V_{(16-p)/2}.

## B. Casimir identity (exact)

- B1 [T]. sum_a {B_a, B_a^+} = 2 [144 - 2 S(S+1) - C2_10 - J^2]. The check on N <= 2 (529 states) is exact: an operator
  with c^+c^+cc, c^+c and 1 terms is fixed by its N <= 2 matrix elements. The error is 0.
  - Reading: C2(so12) := C2_10 + J^2 + (1/2) sum {B, B^+} = 144 - 2 S(S+1).
  - Derivation: the two-body part of C2(so12) on Lambda^2(32) = 1 + 495 is fixed by the singlet projector, which is
    L_+ L_- / 16 of the Lefschetz pair.
- B2 [T]. sum [B_a, B_a^+] = -20 J.
- B3 [F]. N = 3 random vectors agree to 6e-14.
- There is no extrapolation from smaller n: the n = 5 identity is proven directly.

## C. Spectrum (exact)

H_sym = -g F, where F = 144 - 2S(S+1) - C2_10 - J^2.
- C1 [T]. Standard Weyl Casimirs agree with the formula: (8,0^5) = 144 (it holds |0> and |F>), Lambda^1 = 33/2,
  Lambda^2_0 = 32, and (15/2, (1/2)^5) = 285/2.
- C2 [T]. The spherical irreps with C2 = 144 are (8,0) and (6,4). (6,4) is excluded by the weight bound
  mu_1 + mu_2 <= 8. The weight (8,0^5) has multiplicity 1, at S_z = 0. Cartan-Helgason then gives one K-fixed vector.
- C3 [T] (direct count, Weyl formula).
  - Spin(10) singlets occur only at N = 0 mod 4 (the centre Z4). By N = 0, 4, ..., 32 they number 1, 1, 1, 1, 27, 1, 1, 1, 1.
  - At N = 16 the flavour content is j = 0, 4, 8, one multiplet each. So exactly ONE Spin(10)-and-flavour singlet:
    the ground state is unique.
- C4 [T]. E0 = -144 g, and every excited state has Delta F >= 4:
  - centre-class minima: C2 = 16 (class 0, non-singlet), 9 (10), 45/4 (16, 16bar);
  - odd N has j >= 1/2 and |J| >= 1/2.
  The minimum is attained by the N = 12 and N = 20 singlets.
  - Gap = 4 g (charge-4 Spin(10)-singlet sector).
  - Pair level: B^+|GS> is an exact eigenstate (j = 0, 10, J = 1), at 10 g.
  - Fermion level: c^+|GS> is an exact eigenstate (j = 1/2, 16, J = 1/2), at 13 g.
  - At fixed N = 16 the gap is >= 16 g.
  The ground state is the K-fixed vector of the (8,0) irrep, the irrep that also holds |0> and |F>. So it is a
  "spherical-harmonic" superposition: Spin(10) x SU(2) x particle-hole symmetric, with no bilinear order (a unique state
  carries no symmetry-breaking expectation).
- C5 [T]. The naive ordering -g sum B B^+ = H_sym + 5 g (N - 16) gives E0 = -168 g, two-fold at N = 4 and N = 8 (charged).
  - Symmetry needed: particle-hole C (with the Spin(10) outer automorphism; sum M x M* is real, so C maps B -> -B^+), or
    equivalently the symmetric ordering.
  - Flavour SU(2) is automatic (Pauli forces the epsilon pair) and need not be imposed.
  - U(1)_N is conserved by this term; a Z4-only version is the register's Omega.
- C6 [T] contrasts.
  - 16 + 16bar: 16 x 16bar = 1 + 45 + 210 has no 10, so the channel vanishes. The singlet allows a quadratic Dirac pairing,
    which gives a unique gapped state trivially: vector-like, no SMG content. It does not fail, but it does not test SMG.
  - 15 + 15 (no nu^c): H conserves N and N1 - N2, and C maps (N, N1 - N2) -> (30 - N, -(N1 - N2)). A unique C-symmetric
    state would need N = 15 and N1 = N2, which is impossible. Every level is >= 2-fold for ANY such term: an exact failure,
    the two-flavour version of smg-strong-coupling D6.

## D. Reduced analogues (full diagonalisation)

- n = 4 has no analogue: 8s x 8s contains no 8v.
- n = 3 is a different type: Spin(8) 8s is real, so M is antisymmetric, the pair is flavour-symmetric, and flavour
  reduces to U(1).
- D1 [F]. n = 3 (4 x 2 modes, 2^8):
  - sum {B, B^+} = 2[16 - 4 S_z^2 - C2_6 - J^2] exactly, on the full Fock space (here C2(so8) = N'(8 - N'));
  - unique GS at -16 g, gap 4 g, fermion gap 5 g;
  - these are the same formulas' predictions, so the Casimir method is validated by brute force.
- D2 [F]. The 3 + 3 truncation has a 2-fold ground state, as the odd-modes-per-flavour theorem says.

## E. Slab mapping

- Second flavour. A layer-index flavour is not needed. The two flavours are the two spin components of the mirror's own
  Weyl 16, which every wall site already has (the earlier one-orbital result dropped spin). A second layer adds no second
  low-energy 16 of the same handedness: bulk-layer modes are gapped Dirac pairs.
- E1 [F]. The far-wall branch E = sin k has > 0.99 of its weight on the far two layers for k <= pi/8 (0.31 at pi/2).
  So a two-layer region does capture the wall mode.
- E2 [F]. Freezing the far r layers into a gapped product (m sz, m = 20) keeps E = sin k exactly. The weight on the frozen
  layers is 0.0025, and on the next layer 0.992. The result is the same for r = 1, 2, 3, 4.
- Reason: bulk-boundary correspondence. The free remainder is still a nontrivial slab whose new face carries the branch, and
  this is independent of how many layers are frozen or how much weight they held.
- So gapping over TWO layers does NOT avoid relocation at g >> t.
- What the site theorem supplies is the necessary condition (a unique symmetric site state with a gap at the mirror face).
  Sufficiency needs the coupled face at g ~ t, where the term acts on the mirror mode while it still hybridises with the
  bulk. That is the intermediate regime of Wang-Wen and Zeng et al., which no product-state theorem reaches.

## Rule wording (proposal, NOT adopted)

"Mirror-face pair rule: on each mirror-face cell, the two spin components of the cell's 16 carry
-(g/2) sum_a {B_a, B_a^+}, with B_a the unique Lorentz-scalar Spin(10)-vector pair, at a coupling comparable to the face
hopping."

Gate:
1. No measured number is chosen (g is free, not fitted): PASS.
2. No structure is inserted beyond the register's own 16 and Spin(10). The 10 channel is forced as the only bilinear
   covariant: conditional PASS.
3. It predicts the closed-form site spectrum (4 : 10 : 13 g, Delta at fixed N >= 16 g), but its PURPOSE (a gapped mirror in
   the slab) is not shown, and relocation applies at strong coupling: UNTESTED.
4. Axiom bent: none, if the 32 modes are a cell of sites (composite before atomic); "one qubit per site" is bent if they are
   put on one site.

Gate status: not adopted.

## Smuggling review

Supplied:
- the 16 with one orbital per weight;
- a two-valued flavour (identified with spin);
- the 10-channel form;
- the particle-hole ordering;
- the free slab with the m sz stand-in;
- Cartan-Helgason (cross-check only).

Forced:
- the so(12) closure;
- the Casimir identity;
- uniqueness;
- all gaps;
- the ordering result;
- the 15 + 15 obstruction;
- the absence of a 10 in 16 x 16bar.

Not shown:
- the lattice of sites with hopping;
- the interacting slab;
- gauge fields;
- the continuum limit.

Literature (supplied, cited not computed): Razamat-Tong 2021; Tong 2021; You-He-Xu-Vishwanath 2018; Wang-Wen 2018/2020;
Butt-Catterall-Hasenfratz SO(4) lattice SMG; Zeng-Zhu-Wang-You 2022.
