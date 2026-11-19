---
claim_id: tetrahedral_four_mode_term_gaps_both_copies_and_a_pair_across_tetrahedra_gaps_one_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "On the cube tick of the candidate laws register, each tetrahedron has one four-mode term (its top form, a Fidkowski-Kitaev term keeping a Z4 of mode number); the mirror map fixes it, so it gaps both light copies and cannot select one; the two copies are the eigenspaces of s3 = -S F at every step, and a supplied term pairing one F-pair from each tetrahedron is the only four-mode term on a single copy, leaving the other copy exactly free at zero momentum in one cube and on a 4x2x2 torus; the residual Z4 is anomaly-free per family only with n^c; light-copy gaplessness at nonzero momentum, the rung-1 gap, chiral gauge couplings and any adopted rule are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/tetrahedral_four_mode_term_gaps_both_copies_and_a_pair_across_tetrahedra_gaps_one_2026_10_21.py
---

# The tetrahedral four-mode term gaps both copies, and a pair across tetrahedra gaps one

Claim type: bounded_theorem.
Primary runner: `scripts/tetrahedral_four_mode_term_gaps_both_copies_and_a_pair_across_tetrahedra_gaps_one_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It suggests that a term changing mode number by four could gap the mirror copy. This note tests a four-mode term on one tetrahedron of a cube and the related pair term, and does the anomaly bookkeeping of the residual Z4. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither term. The literal tetrahedral hypothesis fails.

## Statement

1. Each tetrahedron of a cube has exactly one four-mode term, its top form (O_e, O_o). The 12 even rotations fix each, the 12 odd ones swap them, and the mirror M = (odd rotation)(inversion) fixes both with phase +1. So every tetrahedral term keeps M and cannot select a copy.
2. At every step the tick's two light copies are the eigenspaces of s3 = -S F, with S the sublattice sign and F the face-diagonal spin-3/2 hop. Each tetrahedron holds one F-pair of each copy, and S = g5 s3 holds only at step pi/2.
3. O_e is (copy-B pair)(copy-A pair) on one tetrahedron, so it mixes the copies. O_A and O_B, one F-pair from each tetrahedron, are the top forms of one copy; O_B is the only four-mode term supported on a single copy among the 6 with its character. It breaks the 12 odd rotations and M and keeps Z4.
4. At zero momentum the top form plus h.c. is a Fidkowski-Kitaev term and gaps both copies; g(O_B + h.c.) leaves copy A exactly free and gaps copy B.
5. The residual Z4 of mode number is Spin-Z4 up to a gauge transformation, and is anomaly-free per family only with n^c.

## Derivation

Statements 1 and 3 follow from the characters of the 70 four-mode terms of a cube under the 24 rotations, inversion and M. Statement 2 uses F^2 = 1, [F, S] = 0 and {F, W} = 0, so every half-tick conserves s3; s3 commutes with W and every [C_a, W], hence with the light algebra, and momentum breaks it at O(K^2). The 12 even rotations forbid every copy-mixing bilinear.

Zero momentum. At mass 0 the tick at K = 0 is the identity, with 8 zero modes at every step. A tetrahedron's 8 Majoranas are even under the antiunitary c -> c^dag, and generic invariant interactions leave a unique state only for 8 Majoranas (the Z8 count). The top form plus h.c. is a real quartic Majorana term. Since tr(W P_B) = 0, O_B commutes with every free half-tick; O_e does not.

Anomalies. On every Weyl field X = 5(B-L) - 4Y = 1 mod 4 and exp(i pi X/2) = exp(i pi N/2)(-1)^F z_SU(2). Per family with n^c, the Z4 anomalies vanish and the Z16 index is 0 (N) and 16 = 0 mod 16 (X); without n^c it is 1 and 15. Instantons allow Z_k of N exactly when k divides 4, so the register's "must change mode number by four" should read: mode-number conservation must break, Z4 is the largest residual, and it survives exactly when every term has Delta N = 0 mod 4. The Z4 rule Delta N = 3 Delta B + Delta L = 0 mod 4 allows B-L-conserving proton decay and Delta L = 4, and forbids Majorana masses, neutrinoless double beta decay, n-nbar oscillation and B+L-conserving proton decay to all orders.

Rung 1. On a 2x2x2 cell the tetrahedral top form is a colour singlet with B - L = 0 but weak isospin 2 on even cells and hypercharge from -2 to 2 on odd cells. A cell has no SM-invariant four-mode term on even cells and two on odd cells (uude and uddn type). Under the register's link clause the literal term would delete the W and hypercharge links.

## Checks

The runner gives `TOTAL: PASS=13 FAIL=0` in 7.6 s.

- A1: 70 terms, 7 rotation-invariant (5 M-even, 2 M-odd), 10 tetrahedral-invariant; M phases +1, +1; M U(K) M^+ = U(-RK) to 5e-15.
- A2: copies match the eigenspaces of -SF to 1e-11, 4e-11, 3e-10 at steps pi/2, 0.3, 0.04; |[s3, U(K)]| slope 2.00; |S - g5 s3| = 0.70, 0.96 at 0.3, 0.04.
- A3: three-fold-turn charges (1, 1, w, w^2); the three-fold turn alone would allow 4 mixing bilinears; 6 terms with O_B's character (4 inversion-even), O_B the only one-copy one.
- B1: degeneracies {2: 2, 4: 2, 6: 2, 8: 1}; Majorana order 4 in the top form.
- B2: (degeneracy, gap) = (1, 1.000) for O_e + O_o, (16, 1.000) for one tetrahedron and for O_B; |[G(e^iW), O]| = 4e-16 for O_B against 0.36 for O_e.
- C1: on the 16-mode 4x2x2 torus, 8 zero modes and |w| at K = (pi,0,0) of 1.231 (step pi/2) and 0.0462 (step 0.04).
- C2: with the static stand-in h = i log(tick) and g = 1, the tetrahedral term leaves a unique ground state (gap 0.395, 0.826 at steps pi/2, 0.04) and the one-copy term exactly 16 states, 2/4/6/4 over N mod 4 (gap 1.028, 0.343).
- C3: with the term inside each cube unitary at step 0.04, the uniform copy-A modes commute with the interacting tick to 5e-16 for the one-copy term, against 0.46 for the tetrahedral term.
- D1: Casimir 6; hypercharge weights 1:4:6:4:1.
- E1, E2, E3: the Z4 identification, the anomaly sums and the selection rule above.
- F1: the arithmetic of the estimates below.

Estimates (not checks). With an O(1) coefficient at Lambda = M_P/3 and W0 = 0.15 GeV^2, tau(p -> e+ pi0) is about 3e46 yr against the bound of 2.4e34 yr, safe for Lambda above about 4e15 GeV. n-nbar oscillation and neutrinoless double beta decay are forbidden, consistent with present bounds, so neutrinos are Dirac. Every four-mode piece here conserves B - L, so sphalerons leave no baryon excess, against eta_B = 6.1e-10. The B - L link survives unless a Delta L = 4 piece is added.

## Boundary

Forced: uniqueness and characters of the tetrahedral form, M fixing it, the copies as eigenspaces of -SF, the 2 + 2 split of each tetrahedron, the absence of covariant copy-mixing bilinears, tr(W P_B) = 0, the Z8 count, the anomaly sums and the Z4 selection rules. Supplied: the four-mode terms and their strength g, which copy is the mirror (one handedness bit, the explicit parity violation), the static stand-in in C2, the rung-1 gauge generators and chiral assignment, Lambda, W0 and measured bounds. Cited: Z16 for Spin-Z4, existence of symmetric mass generation for an anomaly-free 16, the sphaleron factor 28/79. Negative results: the tetrahedral term keeps M and gaps both copies; at rung 1 the literal term breaks SU(2)_L or U(1)_Y; no baryon excess follows. Not established: gaplessness of the light copy at nonzero momentum in large systems, the rung-1 SM-invariant form and its gap, chiral gauge couplings at the register's step (a sublattice-assigned SU(2) is vector-like at eps <= 0.04), and any adopted rule.
