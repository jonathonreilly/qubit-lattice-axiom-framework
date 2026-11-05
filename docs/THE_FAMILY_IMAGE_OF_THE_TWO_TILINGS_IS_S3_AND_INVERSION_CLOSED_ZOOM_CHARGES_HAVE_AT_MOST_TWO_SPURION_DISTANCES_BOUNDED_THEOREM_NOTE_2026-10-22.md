---
claim_id: the_family_image_of_the_two_tilings_is_s3_and_inversion_closed_zoom_charges_have_at_most_two_spurion_distances_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's two cube tilings ({0,1}^3 + 2n even, offset by (1,1,1) odd), enumerated over the 48 signed permutations: about a site 12 keep both tilings (the equal-sign signed permutations, D3d) and 6 keep even cubes even (C3v, the copy mass); about a cube centre all 48 (O_h) do both. The tetrahedral rotations A4 meet the site rotations only in the 3-element turn about (1,1,1), so A4 is not a site symmetry. About a cube centre the body diagonals give 1 + 3 with the 3 irreducible, the signed axes an irreducible 3, and the unsigned axes 1 + 1' + 1'' (character norms 1, 1, 3); with spin 1/2 attached, the signed-axis and permuted-axis triplets have equal characters on all 24 rotations. On the zoom-3 families (characters (j,j,j) of T(2 e_i)) the translations and the cube-centred inversion generate an image of order 6, non-abelian, with character norm 2: S3 with 3 = 1 + 2. At zoom b (b = 2..12) the turn fixes exactly b diagonal positions and period 2 conserves b / gcd(b,2) characters on them. Three distinct cyclic distances first occur in Z_6, and every negation-closed triple in Z_N (N < 40) has at most two, so with inversion unbroken no zoom gives three spurion distances. The turn-anomaly filter with at least 6 conserved characters leaves b = 9, 12, 15, ..., 30 (b <= 30). With one triple for doublets and singlets and one Higgs the down exponent matrix is the transpose of the up one, so up and down have identical leading mass exponents; in Z_N every exponent of m1 m2 / m3^2 is at most 2 floor(N/2), below the 10.9 (eps 0.22) the up quarks need for Z_6 and Z_9. Seeded random-coefficient ensembles (960 rule-shaped cells; 1944 and 40000 cells with independent supplied triples) reach a joint hit rate of at most 0.000, 0.000 and 0.025, against 0.058 for a supplied U(1) control, with look-elsewhere fraction 0.0001. Estimates: tribimaximal mixing (which needs an A4 triplet the site group lacks) pulls theta13 by -37 sigma, and the residual groups that do exist force a zero mixing entry. Supplied model, finite diagnostic: the zoom-3 and zoom-b family readings, the anomaly filter rule, the spurion distance laws, eps, the coefficient distribution and hit window, the U(1) control charges, and the measured masses, mixings and neutrino counts."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_family_image_of_the_two_tilings_is_s3_and_inversion_closed_zoom_charges_have_at_most_two_spurion_distances_2026_10_22.py
---

# The family image of the two tilings is S3, and inversion-closed zoom charges have at most two spurion distances

Claim type: bounded_theorem.
Primary runner: `scripts/the_family_image_of_the_two_tilings_is_s3_and_inversion_closed_zoom_charges_have_at_most_two_spurion_distances_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It reads the three families as the turn-fixed characters of the update law's tick translations, and measured fermion masses span five orders of magnitude within a sector. A Froggatt-Nielsen-type hierarchy needs a family grading with three distinct pairwise spurion distances. This note asks whether the rules' structure supplies one: the point groups of the two tilings, the A4 or S4 triplets that exist, the zoom-b characters, and the textures they allow. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Point groups of the two tilings (exact, enumerated over the 48 signed permutations).

1. About a site the tilings keep 12 maps, the signed permutations with equal signs (D3d), and 6 of these keep even cubes even (C3v), as the copy mass requires. About a cube centre all 48 (O_h) keep both tilings and even cubes even. The counts are computed; the group names are stated.
2. The tetrahedral rotations A4 (12 elements) meet the site group only in the 3-element turn about (1,1,1). A4, and hence S4, is not a site symmetry; it is one only about a cube centre.
3. Cube-centred A4 triplets. The four body diagonals give 1 + 3 with the 3 irreducible. The signed axes (the hop vector) give an irreducible 3. The unsigned axes give 1 + 1' + 1'': permuted axes are the Z_3 characters again, since the Klein four-group acts trivially on them.
4. With spin 1/2 attached, E1/2 x T1 and E1/2 x (A1 + E) have equal characters on the binary octahedral group; they differ only on half-turns, where chi_1/2 = 0. The lattice spectrum cannot tell a signed-axis triplet from permuted axes, so the low-energy Dirac operator decides. The runner states that the cubic-cell result (Dirac walk times 1_F) gives F = A1 + E; it does not recompute it.
5. Family image. On the zoom-3 families, the characters (j,j,j) of T(2 e_i), the site space group acts through T(2 e_i) and the cube-centred inversion j -> -j only. The image is S3 with 3 = 1 + 2: no A4 or S4 triplet, and families 1 and 2 form the degenerate doublet. The runner states, and does not check, that the turn and the mirrors fix each family.

B. Families at zoom b (exact, enumerated).

6. At zoom b the turn fixes exactly the b diagonal positions (the rest are three-cycles), all with the same turn charge, so there are b chiral families. The update law's period 2 conserves only b' = b / gcd(b, 2) characters of T(2 e_i) on them: for even b, positions j and j + b/2 are one character.
7. Three distinct cyclic distances first occur in Z_6 ({0, 1, 3}). In every Z_N with N < 40, a negation-closed triple has at most two. With the tick's k -> -k (inversion) unbroken, no zoom gives three spurion distances.
8. Anomaly filter. With the register's conditional count rule (the turn-SU(2) anomaly 4N mod 3 vanishes for the light families and for any gapped set) and b' >= 6, zoom 7 fails (4 x 7 = 1 mod 3), and the viable zooms up to 30 are 9, 12, 15, ..., 30. The smallest are 9 (Z_9) and 12 (Z_6). The runner states that both need b - 3 chiral families removed by a family-selective symmetric gapping term that no law supplies.

C. Textures, M_ij ~ eps^f(q_Qi - q_Rj +- h), with f the spurion distance and the conjugate Higgs carrying -h.

9. Down is the transpose of up. With one triple for doublets and singlets (as the positions force) and one Higgs, E_d = E_u^T exactly. Up and down then have identical leading mass exponents for every triple, h and spurion law, and log_eps(m1 / m3) <= 3 max f.
10. Cyclic ceiling. In Z_N every entry costs at most floor(N/2) above the cheapest, so the permutation through the cheapest entry bounds log_eps(m1 m2 / m3^2) <= 2 floor(N/2), for any doublet and singlet triples and any h. The up quarks need 10.9 at eps = 0.22 or 15.0 at eps = 1/3 at leading order, so Z_9 (ceiling 8) and Z_6 (ceiling 6) cannot hold the up tower. The runner states, without asserting, that the anomaly-filtered zooms that can start at b = 15 (eps 0.22) or b = 21 (eps 1/3).

D. Ensembles and leptons: finite diagnostics and estimates (items 11-14 below).

## Derivation

Item 1 maps every cube of both tilings, in doubled coordinates, by x -> c + R(x - c) and records whether the image is a cube of the same or the other tiling. Item 2 intersects the tetrahedral rotations with the site rotations. Items 3 and 5 compute character norms over the group; item 5 generates the group from the translation and inversion matrices on the three characters. Item 4 compares (tr R - tr |R|) cos(theta/2) with zero on every rotation. Items 6-8 enumerate positions and triples. Item 9 builds the exponent matrices for every three-distance triple, every h and both spurion laws (unit steps, and a rung-graded law on Z_9), and compares the tropical leading exponents. Item 10 enumerates translation classes of triples. The ensembles draw complex coefficients with log-uniform moduli in [1/3, 3] and uniform phases, take singular values and the mixing matrix, and count a hit when all four mass ratios and three mixing entries lie within a factor 3 of their targets.

## Finite checks

Exact or enumerated checks (the runner asserts each):
- Tiling maps: site 12 / 6, cube centre 48 / 48.
- |A4| = 12, |A4 cap site rotations| = 3.
- Character norms over A4: diagonals minus the trivial 1, signed axes 1, unsigned axes 3.
- Spin-1/2 characters equal on all 24 rotations.
- Family image: order 6, non-abelian, character norm 2.
- Zoom b: (b, fixed, b') = 2:2,1; 3:3,3; 4:4,2; 5:5,5; 6:6,3; 7:7,7; 8:8,4; 9:9,9 (checked to b = 12).
- First Z_N with three distances: N = 6; largest distance count of negation-closed triples (N < 40): 2.
- Viable b <= 30: [9, 12, 15, 18, 21, 24, 27, 30].
- E_d = E_u^T and equal tropical exponents for every case; largest log_eps(m1 / m3) at one triple 7 (Z_6, Z_9, Z_15).
- Largest log_eps(m1 m2 / m3^2): Z_9 7, Z_15 13; translation classes of three-distance triples: Z_9 6, Z_15 24.

Finite diagnostics (supplied model, finite diagnostic):

11. Rule-shaped grading (one three-distance triple for all fields, one Higgs, Z_6 / Z_9 / Z_15, unit or rung-graded spurions, eps in {1/3, 0.22}): 960 cells x 100 draws. Best joint hit rate 0.000, best mass-only 0.040, best median chi^2 3.25 (Z_15, S = (0, 1, 6), h = 6). The supplied U(1) control (charges Q (3, 2, 0), u (4, 1, 0), d (1, 0, 0), eps 0.22, 2000 draws) gives joint 0.058, mass-only 0.136 and chi^2 0.78; anarchy gives joint 0.000. No cell reaches half the control (asserted), and up and down cannot differ.
12. Independent supplied triples for Q, u^c and d^c (eps 0.22, 40 draws per cell): Z_9 over all 1944 cells has largest hit rate 0.000, as the ceiling requires. Z_15, 40000 sampled of 207360 cells, has largest 0.025 (Q (0, 1, 6), u (0, 2, 6), d (0, 1, 11), h = 9). The fraction of cells with any hit is 0.0001, and the fraction at half the control or more is 0.0000. The hit fraction over cells is the look-elsewhere price; a Z_15 hit is then a supplied cyclic Froggatt-Nielsen charge.

All draws use one fixed seed (20261022).

## Estimates against measurement

Supplied measured inputs: light neutrino count N_nu = 2.984 +- 0.008 from the Z width, with a fourth chiral family excluded by Higgs rates (stated); mass targets m_t : m_c : m_u = 1 : 7e-3 : 1e-5 and m_b : m_s : m_d = 1 : 2e-2 : 1e-3, |V_us|, |V_cb|, |V_ub| = 0.225, 0.042, 0.0037, so the up-to-down hierarchy ratio (m_u m_c / m_t^2) / (m_d m_s / m_b^2) is 3.5e-03; lepton mixing s12^2 = 0.307(12), s13^2 = 0.0220(6), s23^2 = 0.45-0.58.

13. Tribimaximal mixing (exact A4 residual symmetries, which need an A4 triplet the site group lacks): s12^2 = 1/3 pulls +2.2 sigma and s13 = 0 pulls -37 sigma. Excluded by theta13.
14. The residual groups that do exist (charged leptons keep the family Z_3 and neutrinos keep inversion, or the reverse) fix a column or row (0, 1/sqrt2, 1/sqrt2) in the character basis, which the runner computes. That is a zero in the mixing matrix, whose smallest measured entry is |U_e3| = 0.148. Placing the zero at U_e3 gives s13^2 = 0, -37 sigma. The runner states that pure character-against-position mixing gives all |U|^2 = 1/3.

## Boundary

Not claimed: any statement with inversion (k -> -k) broken beyond the distance count of item 7 and the textures of items 9-12; a mechanism that removes the b - 3 extra chiral families of item 8 (stated as absent from the laws); the group names of item 1, the F = A1 + E result of item 4 and the family-fixing of item 5 (stated); the zooms named at the end of item 10 (stated); textures beyond leading tropical order; coefficient distributions other than the supplied one; that no other grading of the families exists in the rules; the lepton estimates beyond the residual groups named; any experimental exclusion beyond the pulls computed.

## Supplied vs forced

Supplied: the zoom-3 family reading and its zoom-b extension; the register's conditional anomaly count rule and the threshold b' >= 6; the spurion laws (unit steps, the rung-graded Z_9 law) and the texture form with one Higgs; eps in {1/3, 0.22}; the coefficient distribution, draw counts, sampling of Z_15 cells and the factor-3 hit window; the U(1) control charges; the measured masses, mixings and neutrino count. Forced, given those: the tiling point-group counts; A4 not a site symmetry; the A4 triplet decompositions about a cube centre; the equal spin-1/2 characters; the S3 family image; b fixed positions and b / gcd(b, 2) conserved characters; at most two distances for negation-closed triples; the viable zoom list; E_d = E_u^T with identical leading exponents; the cyclic ceiling 2 floor(N/2); the computed tribimaximal and zero-entry pulls.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's two cube tilings, copy mass and tick translations T(2 e_i), the turn-fixed family reading, and the conditional anomaly count rule. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_family_image_of_the_two_tilings_is_s3_and_inversion_closed_zoom_charges_have_at_most_two_spurion_distances_2026_10_22.py
```

Needs numpy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 19 s with about 60 MB resident, prints about 5.3 kB and ends with `TOTAL: PASS=14 FAIL=0`. Its random draws use a fixed seed; two runs gave identical output apart from the runtime line.
