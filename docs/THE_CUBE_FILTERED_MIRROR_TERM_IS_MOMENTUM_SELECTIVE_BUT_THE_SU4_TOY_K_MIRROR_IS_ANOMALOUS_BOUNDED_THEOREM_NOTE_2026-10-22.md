---
claim_id: the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "SU(4) toy of the momentum-selective mirror requirement. Band (supplied): a real band with Weyl nodes only at K = 0 and R = pi(1,1,1), of opposite chirality (Karsten-Wilczek form composed with a unimodular momentum map, realified with complex structure J); light h, mirror -h, light-mirror pairing w prod sin^2(k_i/2) (1 at R, 0 at K); cube-filtered SU(4) quartic (rows 8^-1/2 sum over the cube, form factor 8 prod cos^2(k_i/2)) on the mirror only. Exact: the toy is sign-free (weights det(M)^4, M real); the light K modes and the whole R sector never enter the interaction, so at every coupling and every finite size the light gap at K is 0 and the light-mirror gap at R is the free paired value; the quartic keeps Z4_J x Z4_N x SU(4), which forbids every bilinear mass and pair at K; the K mirror is 8 Weyl of one Z4_J charge (Z16 index 8), so a symmetric trivially gapped K mirror is anomaly-forbidden in this toy. Finite diagnostics (sign-free CT-INT, L = 4 at beta = 8 for g/t = 0.25, 2, 4, 6; L = 4, 6 at beta = 4 for g/t = 2): the L = 4 K-mirror gap is O(g) already at g/t = 0.25 (finite-size zero-mode atom), so it is not a bulk gap; at g/t = 2 the gap falls 2.18 -> 1.53 from L = 4 to 6 with no pair or mass order; at L = 4 pair correlations grow steadily with g/t (xi/L 0.18 -> 0.42). No symmetric gapped window is established; at L <= 6 the K-mirror gap is inconclusive. Not Spin(10), not the CL-1 tick."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
  - the_filtered_quartic_toy_with_a_face_gapped_band_is_symmetric_and_gapped_at_moderate_coupling_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
runner: scripts/the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_2026_10_22.py
---

# The cube-filtered mirror term is momentum-selective, but the SU(4) toy's K mirror is anomalous

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_2026_10_22.py`.

The [light-partner note](THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md) put the requirement in exact form: the mirror term must gap the mirror symmetrically at the zone centre K = 0 while the mirror stays Dirac-paired with the light copy at the corner R = pi(1,1,1). The cube-filtered quartic has form factor prod cos^2(k_i/2), which is maximal at K and zero at R: it is momentum-selective by construction. This note tests that in a sign-free SU(4) toy. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## Why not the pi-flux band

The real pi-flux band of the [block-quartic note](THE_BLOCK_LOCAL_QUARTIC_GAPS_THE_DIRAC_MIRROR_SYMMETRICALLY_AND_RELEASES_THE_LIGHT_PARTNERS_BOUNDED_THEOREM_NOTE_2026-10-22.md) puts all 8 zero modes at fine momenta (+-pi/2)^3. A real filter has |f(k)| = |f(-k)|, and the cube filter takes the value 1/8 at every one of them, so that band cannot test momentum selection. The toy uses a band whose nodes sit at K and R.

## Statement

1. (Band; theorem.) d(p) = (sin k1, sin k2, sin k3 + r(2 - cos k1 - cos k2)) with k = (p1 - p2, p2 - p3, p3) and r = 1. The map is unimodular, so the hops stay on the lattice. d vanishes only at p = 0 and p = R, with chiralities +1 and -1 (off-node local minima of |d| are >= 1.000). The complex Weyl band d.sigma is realified to 4 real orbitals per site. Its complex structure J commutes with H. The J = +i sector carries h; the J = -i sector carries the conjugate copy, with flipped chirality. This mirrors the eps sectors of the light-partner census.
2. (Model; theorem.) Light h, mirror -h, and pairing w f_R(k) 1 with f_R = prod sin^2(k_i/2). Then H(k)^2 = d^2 + w^2 f_R^2. At L = 4 the only zeros are the 8 K modes (light + mirror). The R sector sits at exactly w. H_int = -g sum_v (psi_v1 psi_v2 psi_v3 psi_v4 + h.c.) with psi_(c,alpha) = 8^-1/2 sum over the cube at c, on the mirror only. The normalisation is that of the toy-QMC notes.
3. (Sign; theorem.) The weights are g^2n det(M)^4 with M real.
4. (Exact decoupling; theorem.) The filtered rows have zero overlap with the mirror R modes (4e-16), and f_R(K) = 0. So the light K modes and the entire R sector (light and mirror) are absent from H_int.
   - Light gap at K = 0 at every coupling, every size and every order.
   - Light gap at R = the free paired value w at every coupling.

   Two of the four requirements hold by construction. They are not dynamical results.
5. (Symmetry and anomaly; theorem.)
   - Z4_J (c -> J c) maps filtered rows to +-rows, so H_int keeps Z4_J x Z4_N x SU(4).
   - At K every mirror mass pairs J = +i with J = -i (each sector holds one Weyl), so it is Z4_J-odd. Every pair is Z4_N-odd. All bilinears at K are forbidden.
   - The K mirror is 8 left-handed Weyl of one Z4_J charge, with J^2 = fermion parity. Its Z16 index is -8, and the light K modes carry +8 (8 mod 16 either way; the R sector cancels within itself). A symmetric, trivially gapped K mirror would leave the light K modes as the only low content, with index 8 != 0 against an on-site, anomaly-free lattice Z4_J. So in this toy a symmetric trivial gap of the K mirror is forbidden. The allowed outcomes are symmetry breaking (pair or mass order), a gapless mirror, or a topologically ordered gap.
6. (Finite diagnostics, g = 1, w = t/2.) The light gap at K and the gap at R are exact, as in item 4.
   - (a) Weak coupling, g/t = 0.25, L = 4: the K-mirror midpoint gap is already 0.90(2) at beta = 8 and 0.75 at beta = 4 (live run). The K zero modes form a finite atom, on which the filtered quartic acts with strength 64 g / L^3. An L = 4 K gap is a finite-size effect, not evidence of a bulk symmetric gap.
   - (b) g/t = 2, beta = 4, L = 4 -> 6: K gap 2.18(16) -> 1.53(5), shrinking. S_pair/N 0.188 -> 0.039 (ratio 4.8, against a volume ratio of 3.375), xi/L 0.250 -> 0.116. The Z4_J-odd mass channels stay below their free values (1.73 -> 1.69, free 1.77/1.78). There is no order at g/t = 2, and the gap is not shown to survive L -> infinity.
   - (c) beta = 8, L = 4: pair xi/L is 0.175, 0.263, 0.382, 0.424 at g/t = 0.25, 2, 4, 6; S_pair/N is 0.115, 0.199, 0.336, 0.382 (free about 0.08-0.09). The Z4_J-odd mass channel 2 rises above free at g/t >= 4 (1.89 vs 1.77; 2.23 vs 2.03). This is the same trend toward strong-coupling pair order seen in the face-gapped and toy QMC. L = 6 at g/t = 4 and 6 was not run.

## Verdict on the four conditions

- Light K gap zero: holds, exactly, by construction.
- Light R gap about w: holds, exactly, by construction.
- Mirror K gap opens: seen at L = 4 at every coupling, including g/t = 0.25, so it is not diagnostic. At g/t = 2 it shrinks from L = 4 to 6. Inconclusive at this size.
- No order: holds at g/t = 2 (L = 4 -> 6). At g/t >= 4 the correlations grow at L = 4, and this is untested at L = 6.

No window where all four hold is established. In this SU(4) toy, a trivially gapped symmetric window is ruled out by item 5 whatever the numerics show. The dynamics can only pick among order, gaplessness or topological order at K.

## What this means for the requirement (estimate, not computed)

The obstruction in item 5 is a counting statement: the K mirror alone must carry Z16 index 0 under the symmetry the mirror term keeps. The SU(4) toy fails with index 8. In the framework the K mirror is G_R(eps+), G_L(eps-) per member of the Spin(10) 16, which is 32 Weyl of one charge under a Z4 inside U(1)_eps, or 16 per eps sector: index 0 mod 16. So the anomaly does not forbid the momentum-selective phase for the Spin(10) content. It does forbid it for any toy with fewer than 16 Weyl per charge at K. A meaningful sign-free test needs 16 Weyl at K, for example two tastes per flavour with taste-mixing filtered rows, so that only the diagonal Z4_J survives. This is the next probe. The obstruction also requires the mirror term to keep a Z4 of U(1)_eps; whether the cube-filtered pair square on the CL-1 tick does so is not checked.

## Derivation

- (1-2) The node set follows because the Karsten-Wilczek d vanishes only at k = 0 and (0,0,pi) for r > 1/2 (sin k1 = sin k2 = 0 forces corner values of k1, k2, and then |r(2 - c1 - c2)| >= 2r > 1 unless k1 = k2 = 0), and the map p -> k is a bijection of the torus sending R to (0,0,pi). Chirality is sign det(dd/dp). (H +- ...)^2 follows because the pairing is proportional to the identity in spin, and the light and mirror blocks are h and -h.
- (4) The cube row has amplitude 8^-1/2 prod(1 + e^{ik_i}), which is zero when any k_i = pi. f_R(K) = 0. H0 is momentum-diagonal.
- (5) The anomaly is the Z16 classification of Spin x_Z2 Z4 in 3+1 dimensions: one Weyl of charge 1 generates it. The lattice Z4_J is on-site, so the ultraviolet index is 0.
- (6) CT-INT is the block-quartic engine (pair, local and shift moves; its exact-diagonalisation check is in that note), here with translation-invariant tables for the filtered rows. K-mode propagators come from filtered-row-to-mode tables. Gaps use the midpoint estimator, a lower-bound-style band of mean +- 2 sigma from 8 jackknife bins. S_pair = sum G_vv'^2 / N over filtered rows. S_B = 4 Tr[B G B (1 - G)] / N over the 4 on-site Z4_J-odd masses.

## Checks

A1 band nodes and chirality; A2 real H, [J, H] = 0, zeros and the R level; A3 exact decoupling; A4 Z4_J closure, J-odd masses and the index count; B1 sign plus engine sum rule and drift; C1 live weak-coupling finite-size caveat. TOTAL: PASS=6 FAIL=0 (55 s, 110 MB).

Recorded production values (prod.py, 82 s segments, seeded; no PASS depends on them):

| beta = 8, L = 4 | g/t = 0.25 | 2 | 4 | 6 |
|---|---|---|---|---|
| mirror K G(beta/2) | 0.0134(11) | -0.0004(7) | 0.0045(23) | 0.0044(35) |
| mirror K midpoint gap | 0.90(2) | > 1.5 | 1.18(13) | 1.18(19) |
| S_pair/N (free) | 0.115 (0.090) | 0.199 (0.089) | 0.336 (0.085) | 0.382 (0.078) |
| pair xi/L | 0.175 | 0.263 | 0.382 | 0.424 |
| light K gap / R gap | 0 / exact | 0 / 0.108 | 0 / 0.030 | 0 / 0.014 |

The R gaps are the exact (2/beta) ln cosh(beta w / 2), the midpoint value for a level at w.

At beta = 4 and g/t = 2, from L = 4 to 6: gap 2.18(16) -> 1.53(5); S_pair/N 0.188 -> 0.039; xi/L 0.250 -> 0.116.

## Clause count and law text

No law change is proposed. Tested candidate (NOT proposed for adoption):

> "Mirror term. The mirror copy carries the cube-filtered singlet charge-4 term; the light-mirror pairing carries the corner form factor prod sin^2(k_i/2)."

Smuggling check:
- Supplied: the band (the KW form, r and the unimodular map are choices; uniqueness is not checked), the corner form factor f_R (chosen so as to be 0 at K), w = t/2, the filter normalisation, sizes, betas and seeds.
- Forced: the decoupling of K-light and of R (exact, given the two form factors), the Z4_J x Z4_N x SU(4) symmetry, and the index-8 obstruction.
- The two satisfied conditions are satisfied by the choice of form factors, not by dynamics. In the framework, f_R would have to be derived, and the light-partner note shows that no eps-preserving cell-local light-only mass exists. A momentum-dependent light-mirror pairing is a supplied 3-hop term.

## Boundary

- SU(4) toy, not Spin(10). The band is not the CL-1 cube tick or H'.
- L <= 6, beta <= 8. No Binder ratio. No L = 6 at g/t = 4 or 6.
- The L = 4 K gap is dominated by the zero-mode atom (6a).
- The midpoint estimator is lower-bound style.
- The anomaly statement assumes the standard Z16 classification applies to the lattice Z4_J with J^2 = fermion parity. Topological order is not tested.
- The engine was checked here by the sum rule and the free limit, not by a fresh exact diagonalisation of this model.
