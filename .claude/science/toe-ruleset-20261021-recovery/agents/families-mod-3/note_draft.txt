---
claim_id: three_fold_turn_anomaly_gives_family_count_zero_mod_three_under_a_supplied_mirror_term_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional: for the supplied chiral generator H' = (i/2)[W_o, W_e] on the cube objects of the candidate laws register, with N stacked supplied rung-1 (4,2) families, the three tastes other than the light one can be gapped keeping both SU(2)s and the k-twisted three-fold turn only if N(q_light + k) = 0 mod 3; the supplied mirror-term choice (the single-copy mirror top form O_A) fixes k = 2 and so N = 0 mod 3 with minimum 3, while the other twist k = 1 allows every N; the family count, the mirror rule, the generator and gappability (SMG, cited) are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/three_fold_turn_anomaly_gives_family_count_zero_mod_three_under_a_supplied_mirror_term_2026_10_21.py
---

# A three-fold-turn anomaly gives a family count of 0 mod 3 under a supplied mirror term

Claim type: bounded_theorem.
Primary runner: `scripts/three_fold_turn_anomaly_gives_family_count_zero_mod_three_under_a_supplied_mirror_term_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight and fixes no family count. This note asks whether the anomaly of the three-fold cube turn constrains the number N of stacked families once the doubler tastes of a supplied chiral generator are gapped. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the generator nor the mirror-gapping term. The result is conditional on both supplied choices, and the family count is not derived.

## Statement

Supplied: the cube objects of the register (one fermion mode per site, the spin-3/2 edge hop W, the face-diagonal hop F, copy sign s3 = -eps F); the chiral generator H' = (i/2)[W_o, W_e]; N families, each carrying the rung-1 internal (4,2) as 4 doublets of SU(2)_e (the weak group, even sublattice) and of SU(2)_o; the light taste (the Gamma taste of copy a, left-handed on the even sublattice, copy charge q_a = 2); and the twist rule. Let S be the three remaining tastes (Gamma copy b, R copy a, R copy b), R = pi(1,1,1).

Then S can be gapped keeping SU(2)_e x SU(2)_o and the turn twisted by exp(2 pi i k N_f / 3) only if N(q_a + k) = 0 mod 3. If the mirror is gapped by its own single-copy four-mode term O_A, only k = 2 survives, so N = 0 mod 3 and the smallest N is 3. Under k = 1 every N passes.

## Derivation

Window content. H' vanishes on an 8^3 grid only at Gamma and R, with H'(K+R) = -H'(K). At Gamma the even sublattice holds (q2, L) and (q1, R); at R the copy charges are the same and the handedness is flipped. The Z3_k x SU(2)_e^2 index per doublet is therefore +1 at Gamma and -1 at R for every k, because each window holds one L and one R doublet and the twist cancels. With 4 doublets per family the window indices are +4N and -4N, total 0. This narrows an earlier register reading that assumed both windows have the same handedness, as they do under the step-pi/2 tick.

Twist selection. The plain turn gives O_A charge 1 and the other copy's top form O_B charge 2. A twist k multiplies a four-mode term by w^k, so O_A keeps only k = 2 and O_B only k = 1. Among one-cube four-mode terms covariant under the 12 twisted tetrahedral turns, every twist has number-changing terms, and only k = 2 has a term built from mirror modes alone.

Anomaly of S. Per family, Z3_k x SU(2)_e^2 of S is -4(q_a + k) and Z3_k x SU(2)_o^2 is +4(q_a + k). Mode number must break (U(1)_N x SU(2)_e^2 = -4). There are 12 doublets per SU(2), so there is no Witten anomaly, and the Z16, Z3^3, Z3-gravity and translation parts vanish. By 't Hooft matching the gapped set must carry index 0, which gives the condition. By Cordova-Ohmori (cited) no symmetric topological order absorbs this anomaly, so the sector must stay gapless or break the turn or an SU(2). The mirror pair {Gamma-b, R-b} alone is anomaly-free for every k.

Rescues that fail. Sublattice twists (k_e, k_o) compatible with O_A never rescue N = 1, 2, 4 or 5. The R window alone carries -4 per family at every twist, but translations allow terms with two R fields, so it need not be gapped alone. The same condition follows if copy b is light with SU(2)_o as the weak group and O_B as the mirror term.

Loopholes. Taking k = 1 = -q_a removes the constraint, and one-cube number-changing terms that keep k = 1 exist. A family-dependent mirror rule allows every N >= 2, never N = 1. Breaking every twisted turn is excluded by the estimate below.

## Checks

The runner gives `TOTAL: PASS=14 FAIL=0` in 0.1 s.

- A1: H'(K+R) = -H'(K), the turn maps H'(K) to H'(R3 K), and H' vanishes only at Gamma and R on an 8^3 grid (residual 1e-15).
- A2, A3: the window content above, and the per-doublet index +1 at Gamma and -1 at R for every k, giving +-4N with total 0.
- A4: the turn on the 8 cell corners has charges {0^4, 1^2, 2^2}, so 4N(q + k) is reading-independent.
- B1, B2: O_A keeps only k = 2 and O_B only k = 1; the one-cube term counts are {(2,2): 10} at k = 0, {(0,4): 1, (2,2): 1, (3,1): 4} at k = 1 and {(1,3): 4, (2,2): 1, (4,0): 1} at k = 2.
- C1, C2: the anomaly algebra of S, and the allowed N per twist: [3, 6, 9] at k = 0 and k = 2, every listed N at k = 1; with copy b light and O_B, [3, 6, 9].
- C3, C4, C5: the O_A-compatible sublattice twists (0,1), (1,0), (2,2) never rescue N = 1, 2, 4, 5; the R window alone needs N = 0 mod 3; family-dependent twists allow N = 2 (for example t = (0,1)) and never N = 1.
- D1 to D3: in a 1+1D toy where each taste is a 3-4-5-0 multiplet, a neutral Lagrangian L forces K t in L, and the toy anomaly is -2N(q_a + k) per sector. For N = 1, 2, 3, 4, 6 each case is either obstructed or gapped by an explicit null, neutral Lagrangian with all Smith factors 1: k = 0 and k = 2 give x x G x G, and k = 1 gives G G G G G.

Estimates (not checks). With S gapped, N = 3 gives N_nu = 3, 2.0 sigma from the LEP value 2.984 +- 0.008; an ungapped R-a taste would double the active neutrinos (123 sigma off at N = 1). Lattice-scale loops would give a light-cone anisotropy of at least alpha/4pi = 6e-4 if every twisted turn broke, against |c_jk| below about 1e-18, so one twisted turn must stay exact. Since (2m)^3 cells hold m^3 rung-1 families, 2^n zooms never give 3 | N, so under k = 2 the one-family-per-cell rung-1 reading is excluded. The light charges are family-blind, so no mass or mixing pattern follows.

## Boundary

Supplied: H' (not adopted), the rung-1 (4,2) with SU(2)_e as the weak group, which copy is light, the mirror rule O_A and its family-blindness (not adopted), the toy charges with an internal Z3 standing in for the rotation. Cited: 't Hooft anomaly matching, crystalline equivalence, Cordova-Ohmori, Haldane's null-vector criterion, and the SMG conjecture for sufficiency in 3D. The condition N(q_a + k) = 0 mod 3 is forced given these inputs; N = 0 mod 3 holds only under the supplied mirror-term choice k = 2. No family count, mirror rule, chiral generator or gapped phase is established. The closest literature precedent is the Garcia-Etxebarria-Montero baryon-triality anomaly, which cancels only when the generation count is a multiple of 3.
