---
claim_id: the_cube_tastes_are_two_doublets_and_no_symmetry_protects_a_family_triplet_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For CL-1's cell (one fermion mode per site, face phase -1, the Margolus cube tick on both tilings, Bloch over 2Z^3) with the 24 cube-centred rotations realised up to a +-1 site gauge: the cell rep is spinorial, spin (from the velocity matrices) times taste with the taste factor projectively linear; the four tastes are E + E of O (one E per chirality), never 1 + 3; every rotation-invariant mass gaps all four alike; the cell-local commutant of the full tick over all k is the scalars (dim 1, also with rotations and with the copy mass; 3 sampled momenta give 8, an undersampled upper bound), and the copy mass leaves one light Dirac family. On the cell x qubit: hops W_i x (a + b sigma_i) satisfy R^2 = 1 only qubit-blind on pi flux or as qubit = spin on zero flux; with the qubit locked the flavour is G_3/2 per chirality (no 1, no 3), unlocked 2E. On the zero-flux qubit = spin hop the corners give L = 1 + 3, R = 3 + 1; singlet and triplet Dirac masses are independent under rotations and every translation class, the on-site staggered mass gaps both equally, Z4 is taste-blind, no translation class separates the masses, and a range-3 free-hop charge forbids the triplet mass; that charge is broken by the tested random link background and by one flux-carrying link, and kept by constant-phase and pure-gauge links (other charges and backgrounds not searched). Comparisons with mixing and the Z width are estimates. Three families are not derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_cube_tastes_are_two_doublets_and_no_symmetry_protects_a_family_triplet_2026_10_22.py
---

# The cube's tastes are two doublets, and no symmetry tested protects a family triplet

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_tastes_are_two_doublets_and_no_symmetry_protects_a_family_triplet_2026_10_22.py` (30 PASS / 0 FAIL; A8, D2 and D4 are printed and not counted).

**Repair 2026-11-14 (PR 10129 hold).** Two statements of the source version were wrong and are corrected below, with the counterexamples kept. (1) The source said the tick's internal symmetry algebra over all k has dim 8. That value came from three sampled momenta and is an upper bound only; the all-k commutant is the scalars (A11, A11u; this agrees with [#10044](THE_TWO_TILING_TICK_HAS_NO_CELL_LOCAL_FAMILY_SYMMETRY_AND_A_TURN_TRIPLET_FORCES_TURN_INVARIANT_MIXING_TO_BE_CP_BLIND_BOUNDED_THEOREM_NOTE_2026-10-22.md)). (2) The source said the free-hop charge Q_f is broken by any link field. Constant-phase and pure-gauge links keep it exactly (C8w), so the statement holds only for the tested flux-carrying backgrounds (C8, C8f). The A8 Schur step is argued and printed, not counted; D2 and D4 compare with supplied measured values and are printed as estimates, not counted.

**Local labels (2026-11-14).** CL-1 here names this note's supplied cube-tick update law (one mode per site, face phase -1, Margolus tick on both tilings). It is not entry CL-1 of [`CANDIDATE_LAWS.md`](CANDIDATE_LAWS.md), and it carries no premise weight. "The register" and "the merged ruleset" (branch agents/minimal-toe-merged) are source-branch texts that are not in this repository; what this note uses from them is stated as a supplied assumption where it is used.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. This note asks whether the family number 3 follows from the taste structure of the 2^3 cell without fitting. It tests the reading in the merged ruleset (agents/minimal-toe-merged), where the qubit's Bloch axes are tied to the lattice axes and the flavour space becomes 2 x (1 + 3). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged. The result is negative: the cell's tastes are not 1 + 3, and where a 1 + 3 does occur, no symmetry protects the triplet.

## Repo context used

- The corner orbit count 8 = 1 + 1 + 3 + 3 and the hw = 1 triplet ([THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE](THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md), [GENERATION_AXIOM_BOUNDARY_NOTE](GENERATION_AXIOM_BOUNDARY_NOTE.md)). That count is a permutation of corner LABELS. Section 1 shows that the compensated rotations do not act on the cell states as that permutation.
- The register's face-clause unification: compensated half-turns anticommute, giving the double cover. This is reproduced in A4.
- copies-generations: 4 cosets give S4 with 1 + 3, on a different supplied tick. families-mod-3 and family-register: 3 from a supplied mirror term or a zoom-3 register. Those routes are conditional and untouched here. These three are source-branch notes that are not in this repository (families-mod-3 and family-register are #9903 and #9915 in the consolidation map's logged table); they are historical reported results, unverified here.
- The register line on translation characters: they force family-diagonal masses. That point is reproduced for the corner triplet (D3).

## 1. CL-1's cell: four tastes = E + E (exact)

- The velocity matrices A_i = i dU/dk_i of the massless cube tick form Cl(3) on the 8 cell states. They give an isotropic cone and the spin su(2) S = -(i/4) eps [A, A]. (A1-A2)
- All 24 cube-centred rotations are tick symmetries up to a +-1 site gauge. The cell rep is spinorial: the compensated half-turns anticommute. (A3-A4)
- Write each rotation as V = rho(spin) tau(taste). The taste factor is projectively LINEAR: its half-turn lifts commute. (A5) After a phase i on the odd axis permutations, tau is a genuine rep of O. Per chirality its characters are (2, 2, -1, 0, 0), which is the 2-dim irrep E. (A7)
- So 4 tastes = E + E. The three axis half-turns act trivially, so the taste rotations factor through S3, and E = (permutation of the 3 axes) - (singlet). The cell carries d - 1 = 2 tastes per chirality, not d. (A9)
- Theorem (A8). A 1 + 3 is impossible on any one-mode cell of this kind. The chirality chi = iA1A2A3 commutes with every rotation and is traceless on taste. By Schur's lemma it would be a scalar on a 1 and on a 3, and the trace would then be +-1 +-3, which is never 0.
- Every rotation-invariant cell mass gaps all four tastes alike. (A10)
- The cell-local commutant of the full two-tiling tick, over all k, is the scalars (dim 1). The all-k commutant lies inside the commutant over any finite set of momenta and contains the scalars; at 12 and 20 sampled momenta it is already dim 1, so the all-k value is exactly 1. The same holds with the rotations added and with CL-1's copy mass. So no exact cell-local taste symmetry is left. (A11) Negative result kept: three sampled momenta give dim 8, which the source version reported as the all-k value; it is an undersampled upper bound (A11u). Control: with the odd tiling removed the update is k-independent and the routine reports a commutant of dim 32 (A11c). The copy mass leaves 4 light states: 2 spin x 1 taste per chirality, which is one Dirac family. (A12) This is the register's "one light family".

## 2. Cell x qubit (merged ruleset): the lock gives no 1 + 3 either

- Theorem (B1). Consider hops W_i x (a + b sigma_i) with face phase +-1. CL-1's reflection condition R^2 = 1 holds only in two cases:
  - pi flux with b = 0: the qubit is blind to the hop;
  - zero flux with a = 0: the qubit is the spin, and the cell has no Clifford structure.
  No hop has both a cell spin and a dynamically locked qubit.
- In the qubit-blind case the lock is a relabelling only. SU(2)_qubit stays exact, and every invariant mass is flavour-universal. (B5)
- If the qubit is locked by hand, flavour = E x E_1/2 = G_3/2 per chirality. This is spinorial (its half-turn lifts anticommute), so it contains no 1 and no 3. Every invariant mass gaps all 16 states alike. (B2-B3)
- Unlocked, the flavour is 2E. Masses split the 16 only as 8 + 8, never as 12 + 4. (B4)
- Correction to the merged ruleset's T1-T2. The 2 x (1 + 3) assumed a spinorial taste factor. The computed taste factor is linear (E), so locking a spinor qubit to it gives G_3/2. The 2 x (1 + 3) does not occur on the computed cell.

## 3. The one place a 1 + 3 occurs: zero flux, qubit = spin (two modes per site)

- There are 8 Weyl corners, with chirality (-1)^hw. Rotation covariance forces the qubit to be locked. L = hw0 + hw2 = 1 + 3 and R = hw1 + hw3 = 3 + 1. The triplet is the axis vector, so 3 = d here. (C1)
- Exact one-site translations forbid every mass. (C2)
- Allowing masses at momentum pi(1,1,1), with face-diagonal translations and rotations kept, gives 4 real mass parameters. The singlet and triplet masses are independent (rank 2), so a light triplet needs the codimension-2 tuning m_t = 0. (C3)
- None of the 8 translation classes separates them. Each class allows both masses or forbids both. (C4)
- The shortest mass, the on-site staggered (-1)^(x+y+z), gaps singlet and triplet equally. (C5)
- The Z4 is taste-blind and allows every Dirac mass. (C6)
- A swap-type protecting charge exists for the free hop. It is Q_f = sum_k f(k) n_k with f = sum cos k_i - 3 prod cos k_i, a range-3 hop charge. It is 0 on both singlet corners and +-4 on paired triplet corners, so it allows the singlet mass and forbids the triplet's. No translation class does this (C4). Other charges were not searched. (C7)
- Covariantised on a 4^3 torus, Q_f does not commute with H on the tested seeded random link background (phases of size 0.3): ||[Q_f, H]|| / ||Q_f|| = 0.575 (C8). One link phase of 0.3, which puts flux on four plaquettes, also breaks it: 0.041 (C8f). So Q_f does not protect the triplet against general link fields.
- Negative result kept, with its witness (C8w): Q_f is not broken by every link field. Take T_i = e^{i a_i} S_i with constant phases a_i. All T_i and T_i^+ commute, Q_f is a polynomial in C_i = (T_i + T_i^+)/2 times the spin identity, and H = sum_i (T_i - T_i^+)/(2i) x sigma_i, so [Q_f, H] = 0. A gauge transform conjugates Q_f and H by one diagonal unitary and keeps this. The runner finds 9e-17, 3e-16 and 5e-16 for constant phases (0.7, -1.3, 2.1), a random pure gauge, and their sum. Which flux-carrying backgrounds break Q_f in general is not shown.
- No loop-induced triplet mass is computed here. The source version's estimate (alpha/4 pi) m_s rested on supplied inputs (one gauge loop at coupling alpha, m_s at the cell scale) and on the 'any link field' statement above; it is withdrawn.

Answer to the coordinator's decisive test: NO, for the symmetries tested. Rotations, the 8 translation classes and the Z4 do not forbid triplet masses while allowing the singlet's; the free-hop charge does on free, constant-phase and pure-gauge links, but not on the tested flux-carrying backgrounds. N_f = 3 is FITTED on this route.

## 4. Against measurement (estimates)

- A family triplet under O: O keeps all 3 degenerate, and D4 or D3 keep a degenerate pair. Three distinct masses need the residual group to be D2, C4, C3 or smaller. (D1)
- Mixing. If the up and down sectors share a residual group, V is a permutation, which gives |V_us| = 0 against 0.2250. If one keeps C3 and the other D2, |V_ij| = 1/sqrt3, which gives |V_ud| = 0.577 against 0.97435. Both are excluded, so masses and mixing need generic breaking and the route predicts no mixing. (D2)
- In section 3 the three triplet pairs carry distinct fcc characters, so every fcc-invariant mass matrix is family-diagonal. There is no mixing until fcc is broken in the family sector, which is a further supplied breaking. (D3)
- Z width, N_nu = 2.9840 +- 0.0082. Four degenerate light families (sections 1-2) are excluded at 124 sigma. One light family (CL-1's copy mass) is excluded at 242 sigma. Three requires the tuning of C3. (D4)
- The conditional prediction requested ("a degenerate triplet at leading order plus a heavy fourth taste") holds only on the tuned branch m_t ~ 0 of section 3. There the triplet is also vector-like, so chirality is still a separate wall.

## Gate verdict (anti-smuggling)

- "Three families from tastes" FAILS item (1) on every tested hop.
  - On CL-1's one-mode cell, the number 3 does not appear: the count is 1 light family, or 4 alike.
  - On the qubit = spin hop, 3 = d appears, but keeping the triplet light is a tuned value (m_t = 0).
- Reported owner principle (2026-10-22, quoted in the source branch; unverified here and not a premise): the 1 + 3 needs a second mode on every site, either the qubit-as-spin of section 3 or the extra qubit label of section 2. Each is a per-site addition and is flagged as a SMUGGLING RISK. A combination of sites (the 2^3 cell's corners, section 1) gives E + E and no 3.
- Item (3): the route predicts no mixing and no mass pattern without further supplied breaking.
- Item (4), axioms bent: section 3 bends the qubit axiom (two modes per site).

## Scope

Supplied: the CL-1 tick at eps = 0.3; the cube-centred rotation group; the hop family W_i x (a + b sigma_i); masses at k = 0; the momentum-pi(1,1,1) mass channel; the free-hop charge; seeded random link phases of size 0.3, one single-link phase, constant phases and one random pure gauge. Not tested:
- protecting charges other than the free-hop charge and the translations;
- link backgrounds other than those listed;
- interacting masses beyond the link-field commutator;
- improper rotations;
- other tick candidates (for example the block-of-eight cosets);
- the conditional count-3 routes (the mod-3 anomaly under a supplied mirror term; the zoom-3 register).
