---
claim_id: the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Two parts. (I) CL-1 tick (step-pi/2 generator H'), exact: the fine cube-filtered mirror term keeps no Z4 inside U(1)_eps (only fermion parity); the same filter applied one rung up (over the 8 cells of a cell cube, on eps-pure mirror cell orbitals) keeps Z4_eps, vanishes at the cell corner R, and is orthogonal to the light copy at K; a corner pairing w (1 - B)/2 Y keeps eps, leaves the 8 K zero modes and gaps R with no new zero on a 12^3 grid; the K mirror carries Z16 index 2 per mode member under Z4_eps. (II) SU(4) MODEL (not a rule) with 16 Weyl at K: two tastes per flavour of a K/R Weyl band, taste-mixing spin-twisted cube-filtered rows on the mirror, light paired at R only. Exact: sign-free (det(M)^4, M real); light K and the whole R sector are decoupled by construction; an exhaustive search of the band commutant finds every Z4-type symmetry of H_int at Z16 index 0 mod 16 (taste-diagonal rows keep an index-8 symmetry). Correction to momentum-selective-mirror: the one-taste obstruction is Z4 of mode number, not Z4_J (the two J sectors are time-reversal partners of equal chirality). Finite diagnostics (sign-free CT-INT, beta = 4, L = 4, 6, g/t = 2, 4, 8, short L = 6 runs): g/t = 8 shows no order (S_pair/N falls 8-11x against volume 3.4) and a K-mirror gap 0.93-1.05 g at L = 6, 40x the zero-mode-atom baseline but half its L = 4 value (2.2(5)); g/t = 2 shows pair correlations that do not fall with volume; g/t = 4 is seed-dependent. Survival of the K gap as L -> infinity is not established: inconclusive."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_cube_filtered_mirror_term_is_momentum_selective_but_the_su4_toy_k_mirror_is_anomalous_bounded_theorem_note_2026-10-22
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
runner: scripts/the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.py
---

# The zoomed filtered mirror term keeps the chiral Z4, and the 16-Weyl toy is anomaly-free with an unsettled K gap

Claim type: bounded_theorem.
Primary runner: `scripts/the_zoomed_filtered_mirror_term_keeps_the_chiral_z4_and_the_16_weyl_toy_is_anomaly_free_with_an_unsettled_k_gap_2026_10_22.py`.

The [light-partner note](THE_LIGHT_COPY_ZONE_CORNER_PARTNERS_ARE_VECTOR_LIKE_ONLY_THROUGH_THE_SUBLATTICE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-22.md) requires a mirror term that gaps the mirror symmetrically at K = 0 while the mirror stays Dirac-paired with the light copy at the corner R, and that keeps a Z4 inside U(1)_eps. The [momentum-selective note](THE_CUBE_FILTERED_MIRROR_TERM_IS_MOMENTUM_SELECTIVE_BUT_THE_SU4_TOY_K_MIRROR_IS_ANOMALOUS_BOUNDED_THEOREM_NOTE_2026-10-22.md) found its one-taste toy blocked by a Z16 index of 8. This note (I) checks the symmetry on the CL-1 tick and (II) runs the 16-Weyl toy. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

## I. The CL-1 tick (exact)

Setting: H' = (i/2)[R_o, R_e] on 8-site cells, cell momentum K, sublattice sign eps, copy sign s (mirror s = -1), as in the light-partner runner.

1. (C1) Every fine 2x2x2 cube, in every alignment, holds 4 sites of each eps. So e^(i theta eps) maps the cube row r to e^(i theta) r_+ + e^(-i theta) r_-, which has the same support. That is a multiple of r only for theta = 0 or pi, and at theta = pi/2 the image is orthogonal to r (|<r, U r>| = 6e-17). **The fine cube-filtered term keeps no Z4 inside U(1)_eps, only fermion parity.** As written in the register, the term breaks the symmetry the light copy's chirality needs.
2. (C2) The fix is one rung up (zoom). Take the rows psi_(C,u) = 8^-1/2 sum over the 8 cells of the cell cube at C of u . c_cell, with u an eps-pure mirror cell orbital. The space s = -1, eps = +-1 has dimension 2 per sign per cell, and [eps, s] = 0.
   - Each row picks up the phase i^eps under Z4_eps, so a charge-4 product of one eps sign keeps Z4_eps. U(1)_eps is broken to Z4.
   - The cell form factor prod(1 + e^(iK_j)) is exactly 0 at R.
   - At K, H'(0) = 0 and s is exact there. The rows lie in s = -1, so they are orthogonal to the light copy (overlap 2e-16).
   So the light K modes and the whole R sector never enter the zoomed term, exactly as in the toy.
3. (C3) Corner pairing: w {(1 - B)/2, Y}/2. Here B = (R_oR_e + R_eR_o)/2 is a 2-hop term, (1 - B)/2 is 0 at K and 1 at R, and Y is taken from the 4-dimensional space of eps-even masses at R. Every element of that space pairs light with mirror.
   - At w = 0.3: eps is conserved (2e-16), K keeps its 8 zeros, the R gap is 0.283, and min |E| off K on a 12^3 grid is 0.283.
   - The free tick therefore realises the required corner structure. This is the light-mirror pairing at R that the toy supplies as w prod sin^2(k/2).
4. (C4) Under Z4_eps the K mirror is, per mode member, G_R(eps+) and G_L(eps-). The chiralities are +1 and -1 for charges +1 and -1, so both are left-handed with one charge. The index is 2 per member. A symmetric trivial gap of the K mirror under this term needs n = 0 mod 8 members per cell: the register's 16 passes, and 15 (no gauge-singlet member) fails.

## II. The 16-Weyl SU(4) model (the SU(4) is a model, not a rule)

5. (Model, A1-A2) Two tastes per flavour of the realified K/R Weyl band of the momentum-selective note: mirror -h, light +h, pairing w prod sin^2(k_i/2) diagonal in taste.
   - Mirror rows are r_(alpha,+-) = (e_(alpha,1) +- e_(sigma alpha,2))/sqrt2 with sigma = spin flip. They are orthonormal and taste-mixing, and they entangle taste with spin, so no symmetry of the band rotates them to taste-diagonal rows.
   - H_int = -g sum over cubes and rows of (psi_1 psi_2 psi_3 psi_4 + h.c.), with psi = 8^-1/2 sum over the cube.
   - At L = 4 the only zeros are the 16 K modes per flavour. Every R mode sits at w.
   - The filter is exactly 0 at R, so light K and the whole R sector are decoupled. The light K gap is 0 and the R gap is the free paired value at every g, by construction.
6. (A3, symmetry and anomaly; theorem) The commutant of the mirror band has dimension 8. Searching it exhaustively for unitaries that map every row to i^k times a row gives:
   - Taste-mixing rows: a group of 32 elements with 16 elements of Z4 type (U^2 = (-1)^F), every one with Z16 index 0 mod 16.
   - Taste-diagonal rows: 128 elements, including an index-8 symmetry (the mode phase on one taste only).
   - The two J sectors are time-reversal partners. They have the same chirality and J-charges +-1, so Z4_J is vector-like (index 0). The chiral symmetry is Z4 of mode number: index 16 = 0 with two tastes, and 8 with one.

   Correction: the momentum-selective note's index-8 obstruction is real, but it belongs to Z4_N, not Z4_J. Its item 5 labels it wrong, and the conclusion stands.
7. (A4) Sign: the row tables are real (max |Im| = 0) and the 4 flavours see the same real M, so the weights are g^2n det(M)^4 >= 0.
8. (A5, exact ED) Zero-mode atom baseline. Projected to K, the quartic is -g(64/L^3) sum (Q + Q^+) on 4 identical 8-mode blocks. At beta = 4 its K midpoint gap is 0.465 g (L = 4) and 0.025 g (L = 6), with level gaps 1.000 and 0.296 g.
9. (Finite diagnostics; recorded production, prod3.py, 82 s segments, g = 1, w = t/2, beta = 4)

| | L = 4 | L = 6 seed 1 | L = 6 seed 2 |
|---|---|---|---|
| g/t = 2: K gap | 2.26(22) | 2.14(35) | 1.34(19) |
| S_pair/N (free) | 1.98 (0.169) | 1.69 (0.054) | 1.33 |
| xi/L | 0.71 | 0.89 | 0.82 |
| g/t = 4: K gap | unresolved (G(beta/2) 0.0006(33)) | 1.05(8) | 1.24(17) |
| S_pair/N | 2.02 (0.146) | 0.46 (0.044) | 0.90 |
| xi/L | 0.74 | 0.47 | 0.61 |
| g/t = 8: K gap | 2.20(51) | 1.05(3) | 0.93(5) |
| S_pair/N | 1.12 (0.122) | 0.141 (0.036) | 0.106 |
| xi/L | 0.54 | 0.24 | 0.18 |

The J-odd mass channels (all 20 K masses; every K mass is J-odd and every pair is Z4_N-odd) are below free in every run: S/N 404-476 against 532-547.

The L = 6 runs are short: 77-101 sweeps, 38-50 measurements, <2n> about 1850-2020. At g/t = 4 the spread between seeds exceeds the jackknife error.

Reading:
- g/t = 8: no order to L = 6. S_pair/N falls 7.9-10.6x against a volume ratio of 3.375, and xi/L falls. The K gap at L = 6 is about 1 g, 40x the zero-mode atom, so it is not the atom. But it is half its L = 4 value.
- g/t = 2: pair correlations do not fall with volume (ratio 1.2-1.5) and xi/L does not fall. This is consistent with pair order, or with MC that is too short.
- g/t = 4: undecided.

The trend is the reverse of the one-taste toy: symmetric at strong coupling, correlated at weak coupling, as for anomaly-free SMG.

## Verdict

- Light K massless: exact (by construction in the model; on the tick, orthogonality at K plus Z4_eps).
- R paired: exact (decoupling; the tick's corner pairing realises it in the free band).
- Z16 index 0: yes (model, exhaustive within the band commutant; tick: 0 for n = 0 mod 8).
- Sign-free: yes.
- Z4 inside U(1)_eps: lost by the fine cube filter (C1). Kept by the zoomed filter (C2).
- Mirror K gap survives L -> 6 with no order: at g/t = 8 there is no order and a gap of about 1 g at L = 6, but the gap halves from L = 4 to 6. At g/t = 2 the pair correlations persist.

Overall: **INCONCLUSIVE.** The anomaly no longer forbids the momentum-selective symmetric phase, and the strong-coupling data are compatible with it, but no L-independent gap is shown.

## Rule text (tested candidate, NOT adopted; for AX-7)

> "AX-7 (Mirror term, zoomed). The mirror term acts one rung above the site: on each cube of eight cells, for each sublattice sign, it is the charge-4 term of that sign's mirror cell modes, averaged over the eight cells, that is invariant under every mode rotation the update keeps, with one coupling everywhere. The light-mirror pairing at the cell corner is the cell-local sublattice-even light-mirror term weighted by (1 - B)/2, B the symmetrised product of the two tilings' reflections."

Smuggling check (anti-smuggling gate):
- (1) Measured numbers chosen: none. The values g and w are supplied constants. The toy's g/t, w = t/2, sizes, betas and seeds are model settings, not fitted.
- (2) Observed structure inserted by name: the rule names no gauge group or content. It selects the term by "invariant under every rotation the update keeps", but which group that is comes from the register's CL-1 mode content, where Spin(10) and the 16 per cell are register inputs. The uniqueness of the pair square was shown for Spin(10) in the block-quartic note, not derived here. So the content is inherited from CL-1, not forced by this rule. The SU(4) flavour group and the flavour and taste counts are a MODEL. The rule also chooses: the eps-pure split (forced by Z4_eps, C1-C2), the rung (forced by C1), the mirror copy (register), the form factor (1 - B)/2 and the choice of Y within its 4-dimensional space (not unique; supplied).
- (3) Prediction it was not built for: the symmetric K gap needs the member count per cell n = 0 mod 8 (C4). Fifteen fails and 16 passes, so the rule needs a gauge-singlet member per family (a right-handed neutrino). It is consistent with neutrino masses, but not a sharp test. The dynamical claim (a symmetric gapped K mirror) is UNTESTED beyond L = 6.
- (4) Axiom bent: nearest-neighbour admissibility (the term spans 4x4x4 fine sites, and the corner term is 2-hop in cells). It also uses the role-block layout of AX-2 (bends Lattice).

Gate result: the rule passes (1) and (4). It passes (2) only conditionally, since it inherits CL-1's content. Its prediction (3) is weak and its central dynamical claim is untested. It is NOT adopted.

## Boundary

- The SU(4) model is not Spin(10), and the band is not the tick. The tick checks are free-band and symmetry-level only. The zoomed term on the tick was not simulated.
- Symmetry search: unitary symmetries inside the band commutant only. Antiunitary (Pin+) indices, lattice-symmetry combinations and mixed gauge anomalies are not computed.
- QMC: beta = 4 only, L <= 6, short L = 6 chains, a midpoint estimator (lower-bound style), no Binder ratio. The xi/L at L = 4 is contaminated by the K zero modes.
- No L = 8 and no beta = 8 at L = 6. These are the decisive next runs: g/t = 8 and 16 at L = 6 with longer chains, and L = 8.
