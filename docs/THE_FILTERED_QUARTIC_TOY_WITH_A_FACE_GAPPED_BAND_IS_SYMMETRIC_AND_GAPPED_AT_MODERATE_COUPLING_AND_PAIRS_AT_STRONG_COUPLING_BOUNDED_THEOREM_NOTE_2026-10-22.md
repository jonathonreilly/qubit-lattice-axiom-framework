---
claim_id: the_filtered_quartic_toy_with_a_face_gapped_band_is_symmetric_and_gapped_at_moderate_coupling_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the supplied cube-filtered SU(4)-singlet quartic toy with a real face-gapped free band eps_k = t sum_i (1 - cos k_i)/2 (Fermi set = Gamma only; X, M, R at t, 2t, 3t), and its interpolation lam (on-site quartic) + (1 - lam) (cube-filtered quartic): the interaction expansion stays sign-free (weights det(M)^4, M real, for any real band and any real mix of vertex orbitals). Finite diagnostics at L = 4, 6 and beta = 4, 8 (live at beta = 4, recorded at beta = 8): at g/t = 1 and 2 the filtered model has no pair, flavour or translation order (S_pair/L^3 falls about as 1/L^3, xi/L falls) and keeps L-independent pair and zone-centre gaps; at g/t = 4 xi/L is flat (crossover); at g/t >= 8 the strong-coupling pair order of the toy QMC survives (xi/L rises with L, pair gap closing); the on-site model (lam = 1) is symmetric and gapped at g/t = 8; lam = 0.5 at g/t = 8 is borderline. The symmetric window sits on the weak side of the pair phase, next to a free point whose only gapless mode is a quadratic touching at Gamma, not a Dirac cone. The Binder ratio, L > 6 and the Spin(10) content are not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_cube_filtered_quartic_toy_is_sign_free_and_pairs_at_strong_coupling_bounded_theorem_note_2026-10-22
  - the_filtered_quartic_chain_is_symmetric_and_gapped_at_intermediate_coupling_and_the_half_filled_3d_toy_has_free_face_fermi_lines_bounded_theorem_note_2026-10-22
  - the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_bounded_theorem_note_2026-10-22
runner: scripts/the_filtered_quartic_toy_with_a_face_gapped_band_is_symmetric_and_gapped_at_moderate_coupling_and_pairs_at_strong_coupling_2026_10_22.py
---

# The filtered quartic toy with a face-gapped band is symmetric and gapped at moderate coupling, and pairs at strong coupling

Claim type: bounded_theorem.
Primary runner: `scripts/the_filtered_quartic_toy_with_a_face_gapped_band_is_symmetric_and_gapped_at_moderate_coupling_and_pairs_at_strong_coupling_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) leaves one chirality wall: symmetric mass generation of the mirror family by the far-rung cube-filtered pair square. The [toy QMC note](THE_CUBE_FILTERED_QUARTIC_TOY_IS_SIGN_FREE_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) found that the supplied SU(4) toy is sign-free and pair-ordered at g -> infinity. The [filtered-chain note](THE_FILTERED_QUARTIC_CHAIN_IS_SYMMETRIC_AND_GAPPED_AT_INTERMEDIATE_COUPLING_AND_THE_HALF_FILLED_3D_TOY_HAS_FREE_FACE_FERMI_LINES_BOUNDED_THEOREM_NOTE_2026-10-22.md) found two things. The half-filled nearest-neighbour band used there has free Fermi lines on the face planes, where the filter vanishes. And the 1D filtered chain has a symmetric gapped window. This note reruns the 3D toy with a real band whose Fermi set avoids the faces: the face-gapped band of the [face-composite note](THE_STRONG_COUPLING_FACE_COMPOSITE_HAS_NO_ATOMIC_LIMIT_AND_STAYS_GAPPED_ON_SHEARED_TORI_BOUNDED_THEOREM_NOTE_2026-10-22.md). It scans g/t and interpolates to the on-site SU(4) quartic. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged; the toy and the band are supplied.

## Statement

1. (Sign.) For any real free band and any vertex set of real orbital rows (cube-filtered rows with coupling (1 - lam) g, on-site rows with lam g), each configuration of n quartic and n conjugate vertices has weight prod(couplings) det(M)^4 with M real. So the face-gapped band and the whole interpolation are sign-free.
2. (Face-gapped band.) eps_k = t sum_i (1 - cos k_i)/2 vanishes only at Gamma; it equals t, 2t, 3t at X, M, R, and the free Fermi set is the single point Gamma. No face mode is gapless at any coupling.
3. (Scan, lam = 0, g = 1.) At L = 4 to 6 and beta = 4 and 8:
   - g/t = 1, 2: pair-disordered and gapped. S_pair/L^3 falls about 3 to 3.5x (the volume ratio is 3.4) and xi/L falls. The pair gap and the zone-centre single-particle gap are L-independent within errors. There is no translation or density order.
   - g/t = 4: xi/L is flat (0.335 -> 0.349), S_pair/L^3 falls 1.9x and the pair gap shrinks. This is the crossover.
   - g/t = 8, 16, infinity: xi/L rises with L and S_pair/L^3 falls only 1.5-1.6x. The pair gap closes toward 0. This is the pair order of the toy QMC.
4. (Interpolation at g/t = 8.) lam = 1, the on-site quartic: no pair correlations (xi/L about 0.004) and every gap about 0.6-0.9, L-independent; symmetric and gapped. lam = 0.5: xi/L flat (0.284 -> 0.279) and S_pair/L^3 falling 2.1x, borderline. lam = 0: pair-ordered. At g/t = 8 the filtered point is cut off from the on-site symmetric phase by pair order, with the boundary near lam = 0.5. Whether the filtered symmetric window at g/t <= 2 connects to the on-site phase was not scanned.

## Derivation

Statement 1 is the toy-QMC sign argument with the vertex operators drawn from the stacked real rows [A_cube; 1]. Each flavour's time-ordered expectation is the same det M, with M the real free propagator between orbital rows. The couplings enter as positive vertex factors. The runner checks trace = det^4 for mixed configurations to 1e-15. The engine adds local pair moves: the conjugate vertex goes on the same orbital within a time window of 1, with the matching proposal ratios. It reproduces exact diagonalisation of a mixed lam = 0.5 ring.

The diagnostics are as follows. S_pair(0) = sum_xy <D_x D_y^+>/L^3 with D = c1 c2 (the 6 of SU(4)), evaluated per configuration as G^2. xi is the second-moment length. Gaps use the midpoint estimator -(2/beta) ln(2 G(beta/2)/(G(0+) + G(beta-))), which gives 0 for a zero mode. It is quoted as the band from mean ± 2 sigma, so it is a lower-bound-style number, not a fitted gap. The cube-term susceptibility chi_h(Q) comes from vertex counts.

## Checks

- `[PASS] A1` mixed-vertex traces = det(M)^4 >= 0 with a real face-gapped band.
- `[PASS] B1` engine vs exact for the lam = 0.5 ring (-0.9154 ± 0.0101 vs -0.9154).
- `[PASS] C1` g/t = 2: S_pair/N falls 3.6x from L = 4 to 6, xi/L falls 0.255 -> 0.162, pair-gap lower end 0.43 at both sizes, zone-centre gap lower end >= 1.67.
- `[PASS] C2` g/t = 8: xi/L 0.355 -> 0.374, S_pair/N falls only 1.85x.
- `[PASS] C3` no translation order in the filtered runs (chi_h <= 0.65).
- `[PASS] C4` lam = 1 control at g/t = 8: xi/L 0.005, zone-centre gap lower end 0.42.

Recorded production values (prod.py, 430 to 5300 sweeps per point, lam = 0 unless stated; printed by the runner as recorded, no PASS depends on them):

| beta = 8 | xi/L (L = 4 -> 6) | S_pair/N (L = 4 -> 6) | pair-gap band, L = 4; L = 6 | zone-centre gap lower end |
|---|---|---|---|---|
| g/t = 1 | 0.184 -> 0.116 | 0.055 -> 0.016 | [1.42,1.55]; [1.41,1.54] | >= 1.6; >= 1.5 |
| g/t = 2 | 0.241 -> 0.179 | 0.063 -> 0.021 | [0.50,0.61]; [0.33,0.51] | >= 1.3; >= 0.9 |
| g/t = 4 | 0.335 -> 0.349 | 0.080 -> 0.043 | [0.25,0.28]; [0.07,0.15] | >= 0.95; >= 0.84 |
| g/t = 8 | 0.370 -> 0.426 | 0.081 -> 0.052 | [0.16,0.20]; [0.05,0.09] | >= 1.0; >= 1.4 |
| g/t = 16 | 0.393 -> 0.464 | 0.085 -> 0.054 | [0.14,0.18]; [0.00,0.07] | >= 1.2; >= 0.7 |
| g/t = inf | 0.407 -> 0.501 | 0.082 -> 0.056 | [0.15,0.17]; [0.01,0.04] | >= 1.1; >= 1.1 |
| g/t = 8, lam = 0.5 | 0.284 -> 0.279 | 0.064 -> 0.030 | [0.13,0.20]; [0.06,0.14] | >= 0.9; >= 0.5 |
| g/t = 8, lam = 1 | 0.004 -> 0.003 | 0.011 -> 0.003 | [0.84,0.92]; [0.77,0.87] | [0.64,0.71]; [0.56,0.64] |

At beta = 4: g/t = 2 has xi/L 0.247 -> 0.176 and pair gap [0.44,0.54]; [0.41,0.65]; g/t = 8 has xi/L 0.368 -> 0.384 and pair gap [0.20,0.24]; [0.03,0.11]. The largest chi_h is 0.34-1.6 across all runs, noisy at L = 6 and never growing with beta. The face-composite (three-fermion) estimators are too noisy for gaps here (their lower ends are 0 to 3). In the pair phase the near-face elementary at k = (2pi/3)^3 softens to the free band value (about 0.05-0.14), consistent with the weakly coupled near-face shell.

## Estimates against measurement

None. This is a statement about a supplied toy's phase diagram.

## Boundary

Supplied: the toy content (four modes per site, one SU(4)-singlet quartic per cube on the cube filter, not the Spin(10) pair square), the face-gapped band and its zero chemical potential, the on-site interpolation lam, sizes L = 4 and 6, beta = 4 and 8, seeds and g = 1.

Decision rule (literature review): a window counts only where S_pair/L^3 -> 0, the gap is L-independent and Binder curves do not cross. At g/t = 1-2 the first two hold at L = 4 and 6, and the Binder ratio is not computed. So the window is supported as a finite diagnostic, not established.

Caveats:
- The free point next to the window has only a quadratic touching at Gamma. A quartic interaction is irrelevant there in 3D, so the window may be the trivially gapped side of this band rather than a gapped Dirac mirror. A band with a genuine Dirac point off the faces (for example a staggered real mass with a Wilson-type face lift) is the next test.
- g/t < 1 is not scanned.
- The toy's g = infinity pair order (toy QMC) is confirmed and is not removed by gapping the faces. Symmetric mass generation in this toy, if it occurs, lies at g/t <= 2-4, on the weak side of the pair phase. That is consistent with the 1D window's lower edge, but not with a window inside the strong-coupling regime.
