---
claim_id: the_zoom_ladder_adds_no_family_charge_so_its_characters_give_no_mass_tower_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the three families read as the turn-fixed zoom-3 characters (j,j,j) of the update law's tick translations, read on the whole zoom ladder (zoom 3^n, n = 2, 3, 4) with vacua (spurions) carrying characters and a rung-m vacuum weighted eps^m: each family character has exactly one image 3^(n-1)(j,j,j) in Z_{3^n}^3, and the next rung's translations act trivially, so the ladder adds no family charge; any spurion set closed under conjugation gives the 12, 23 and 13 family pairs one common suppression (300 random spurion systems), holomorphic sets at most two; in Z_N every negation-closed family triple has at most two pair-difference classes, so a three-distance texture needs k -> -k broken in the family sector (exhaustive for N in {6, 8, 9, 16, 18, 27, 32, 81}); with doublet and singlet families on the same subgroup the Dirac entries depend only on differences, so the cheapest class is a full permutation and all three masses are of one order for every Higgs character and rung (exhaustive for Z_9, Z_27). Fit-free ensembles (complex O(1) coefficients, 200 samples per cell, 1548 cells over 2 zooms, family triples, 2 weight laws, every Higgs character, eps in {1/3, 1/2}) give no sample within a factor 3 of all seven quark targets and none of the 144 rule-forced cells hits the mass ratios, while a supplied ordered U(1) Froggatt-Nielsen control hits at rate 0.075 (finite diagnostic, with its look-elsewhere count). On the two-rung (Z_9^3) assignment the Nelson-Barr arg det(M_u M_d) = 0 exactly for 1-3 heavy copies; a family-pair tower spurion keeps theta_bar real for at most two heavy copies but makes it generic for three, and at dimension five with the tower's own eps = 1/3 gives median |sin theta_bar| 0.10: a tower spurion and the Nelson-Barr zero clash unless the spurion is CP-even to 1e-10. Supplied model, finite diagnostic: the family-character reading, the eps^m weight law and eps values, the coefficient ensemble, the hit window, the measured mass and mixing targets, the heavy-copy content and the theta_bar bound."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_zoom_ladder_adds_no_family_charge_so_its_characters_give_no_mass_tower_2026_10_22.py
---

# The zoom ladder adds no family charge, so its characters give no mass tower

Claim type: bounded_theorem.
Primary runner: `scripts/the_zoom_ladder_adds_no_family_charge_so_its_characters_give_no_mass_tower_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its family structure is read from the turn-fixed characters (j,j,j) of the update law's tick translations T(2 e_i) at zoom 3 (characters of 2Z^3/6Z^3). A Froggatt-Nielsen mass tower needs family charges at three distinct spurion distances and a small ratio eps. The zoom ladder (zoom 3, 9, 27, ...) supplies a natural candidate: a block of edge L ticks 1/L as often, so a rung-m vacuum would carry eps^m with eps = 1/3 per zoom-3 step (eps = 1/2, the octree split, is the alternative). This note asks whether reading the family characters on the whole ladder gives such a tower, and whether a tower spurion is compatible with the zoom-3 Nelson-Barr zero of theta_bar. Mass entries psibar_R,i psi_L,j H need total character q_L,j - q_R,i + h = 0 after spurion insertions; H~ carries -h. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Theorems.

1. Inflation. The zoom-3 family characters (j,j,j) have exactly one image at every rung, 3^(n-1)(j,j,j) in Z_{3^n}^3, and the next rung's translations T(6 e_i) act trivially on all three. The ladder adds no family charge: the families still form the order-3 subgroup {0, psi, psi^2}.
2. No tower from any rung. The pair characters are psi, psi and psi^2 = psi^*. Any spurion set closed under conjugation (sigma and sigma^* at one weight) gives f(psi) = f(psi^*), so the 12, 23 and 13 pairs open at one common suppression whatever the rungs and weights. Holomorphic sets give at most two (with 12 = 23).
3. k -> -k. In Z_N every family triple closed under negation is {0, k, -k} (or {N/2, k, -k}); its pair differences fall into at most two classes up to sign, so it has at most two spurion distances, while generic triples reach three. A three-distance texture needs k -> -k broken in the family sector. The runner states that the tick keeps k -> -k.
4. Dirac entries carry differences. With doublet and singlet families on the same subgroup S (as the reading forces), M = sum_g eps^f(g+h) P_g with P_g permutation matrices, so the cheapest class is a full permutation and all three masses are of one order, for every Higgs character h and every rung. The ladder gives no mass hierarchy.

B. Fit-free ensembles against measurement (finite diagnostic).

5. For the rule-forced assignment (inflated zoom-3 characters), every rung, every h, both weight laws and eps in {1/3, 1/2}, the median m1/m3 stays of order one and no sample hits the quark mass ratios.
6. A supplied ordered U(1) charge with three distinct distances passes the same test, while the best of the ladder's 1548 textures does not: the test can detect a tower, and the ladder does not supply one.

C. Nelson-Barr on the two-rung assignment (Z_9^3 characters).

7. Zoom-9 vacua with non-inflated characters fill no entry at renormalisable order, because every field character is inflated. The zoom-3 Nelson-Barr texture is unchanged and arg det(M_u M_d) = 0 exactly.
8. A family-pair (tower) spurion lambda must carry a light-subgroup character. At renormalisable order it fills the heavy-heavy block qc_a X_b (a != b), with lambda above and lambda^* below the diagonal. The texture stays block-triangular, so theta_bar = arg det M_hh: real for N_h <= 2 heavy copies (det = M_0 M_1 - c c' |lambda|^2), generic for N_h = 3 (the lambda^3 cycle of the three copies). The determinant formulas are stated; the runner checks the resulting theta_bar.
9. Even with N_h = 1, the same spurion enters the light block at dimension five (H lambda l Q / Lambda) with the tower's own strength eps = 1/3, giving theta_bar ~ eps against the bound |theta_bar| < 1e-10. A tower spurion would have to be CP-even to 1e-10, a supplied condition.

## Derivation

Item 1 enumerates the characters k of Z_{3^n} with exp(2 pi i 2k/N) = exp(2 pi i 2j/3) for n = 2, 3, 4. Item 2 computes the least spurion cost f(c) to reach each character by a shortest-path search over spurion monomials, for 300 random spurion systems (1 to 5 characters, costs uniform in [0.5, 4], zoom 9 to 81), with and without conjugates. Item 3 enumerates every triple in Z_N for N = 6, 8, 9, 16, 18, 27, 32, 81 and counts pair-difference classes up to sign. Item 4 builds the exponent matrix f(s_L - s_R + h) for every h in Z_9 and Z_27 with rung-graded costs and checks that its minimum is attained on a full permutation. Items 5-6 draw complex coefficients with |c| log-uniform in [1/3, 3] and uniform phase, 200 samples per cell, multiply by eps^E, take singular values and the CKM matrix from the doublet-side vectors, and count samples within a factor 3 of every target; the best cell is the one with least summed squared log-distance of the medians (chi). Items 7-9 build random real-coefficient mass matrices on Z_9^3 characters with heavy masses 1e3, vacua of random phase, and compute |sin theta_bar| from det(M_u) det(M_d) over 400 samples.

## Finite checks

Exact or enumerated checks (the runner asserts each):
- Inflation images: Z_9: [0, 3, 6]; Z_27: [0, 9, 18]; Z_81: [0, 27, 54].
- Conjugation-closed spurion sets: all 300 systems give one suppression for the three pairs; holomorphic sets at most two. Example: a pure zoom-9 spurion reaches the pair character at degree 3 (eps^6 with rung-2 weight 2 per insertion); with the zoom-3 spurion, eps^1 for every pair.
- Pair-difference classes (negation-closed maximum, all-triples maximum): (2, 3) for each N in {6, 8, 9, 16, 18, 27, 32, 81} (asserted for N > 6; N = 6 printed).
- Dirac permutation structure: asserted for all h in Z_9 and Z_27 with rung-graded weights.
- Two-rung Nelson-Barr: max |sin theta_bar| 2e-16 for N_h = 1, 2, 3, with no entry filled by the zoom-9 vacua.

Finite diagnostics (supplied model, finite diagnostic):
- Rule-forced cells: 144 cells, minimum median m1/m3 0.18, maximum joint hit rate 0.000.
- Best cell of all 1548: N = 27, S = {0, +-4}, unit weight law, h = 15, eps = 0.33, chi = 5.17; medians u32 3.3e-02, u21 7.2e-03, d32 3.6e-02, d21 7.7e-03, V_us 2.1e-02, V_cb 1.0e+00, V_ub 2.0e-02, e32 3.7e-02, e21 6.2e-03.
- Look-elsewhere: 1548 cells x 200 samples: 0 samples hit all seven quark targets; 62 samples hit the four quark mass ratios.
- Anarchy null: joint 0.000, masses 0.000. Positive control (supplied U(1) charges Q = (3, 2, 0), u = (4, 1, 0), d = (1, 0, 0), eps = 0.22): joint 0.075, masses 0.135, chi 0.87.
- Tower spurion at renormalisable order: median |sin theta_bar| 0.00 (N_h = 1), 0.00 (N_h = 2), 0.31 (N_h = 3); the runner asserts the maxima for N_h = 1, 2 below 1e-9.
- Tower spurion at dimension five, N_h = 1, eps = 1/3: median |sin theta_bar| 0.10.

The random draws use a fixed seed (20261022).

## Estimates against measurement

Targets as supplied: m_t : m_c : m_u = 1 : 7e-3 : 1e-5, m_b : m_s : m_d = 1 : 2e-2 : 1e-3, m_tau : m_mu : m_e = 1 : 6e-2 : 3e-4; |V_us|, |V_cb|, |V_ub| = 0.225, 0.042, 0.0037; |theta_bar| < 1e-10. A hit is within a factor 3 of each target. The lepton ratios are printed for the best cell and are not scored. These are fit-free ensemble comparisons, not fits; the positive control shows the test can register a tower when one is supplied.

## Boundary

Not claimed: a mass hierarchy or mixing from any other reading of the families; family characters that break k -> -k (item 3 says what such a reading would need, not that one exists); spurion weight laws other than rung-graded eps^m and the unit law; coefficient ensembles other than the stated one; the Nelson-Barr result beyond dimension five or with other heavy-copy content; the statement that the tick keeps k -> -k and the determinant formulas of item 8 (stated); any value of eps from the rules.

## Supplied vs forced

Supplied: the reading of the families as turn-fixed zoom-3 characters and of a rung-m vacuum as weight eps^m; eps in {1/3, 1/2}; the coefficient ensemble and the factor-3 hit window; the measured mass and mixing targets; the U(1) control charges; the heavy-copy content, heavy masses and the theta_bar bound. Forced, given those: the unique inflation of the family characters; one common suppression for conjugation-closed spurion sets; at most two distances for negation-closed triples; masses of one order from difference-only Dirac entries; arg det(M_u M_d) = 0 on the two-rung assignment; theta_bar real for at most two heavy copies with a renormalisable tower spurion, generic for three.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's tick translations and their zoom-3 characters, the lapse clause (a block of edge L ticks 1/L as often) read as the eps^m weight, the octree split, and the zoom-3 Nelson-Barr structure. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_zoom_ladder_adds_no_family_charge_so_its_characters_give_no_mass_tower_2026_10_22.py
```

Needs numpy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 4 s with about 80 MB resident, prints about 4.1 kB and ends with `TOTAL: PASS=9 FAIL=0`. Its random draws use a fixed seed; two repeated runs gave identical output apart from the runtime line.
