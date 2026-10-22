---
claim_id: the_filtered_quartic_chain_is_symmetric_and_gapped_at_intermediate_coupling_and_the_half_filled_3d_toy_has_free_face_fermi_lines_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the cube-filtered SU(4)-singlet quartic toy (4 flavours, -g sum_x (c1c2c3c4 + h.c.) on the filtered modes, NN hopping t at mu = 0 as in the 3D toy QMC): (1) on any torus with two transverse sizes equal to 2 (L x 2 x 2) the cube vectors span exactly the L - 1 off-face modes of the transverse-symmetric sector and each equals the 1D two-site filter (a_x + a_{x+1})/sqrt2 four times, so the interaction is the 1D filtered chain with coupling 4g and all other modes are free face spectators; at mu = 0 that sector's band is -2t cos q - 4t <= -2t (a filled band, gapped at g = 0), so this ladder cannot test the massless-to-gapped question; (2) in the half-filled 3D toy the face planes k_i = pi carry the free Fermi lines cos k_j + cos k_l = 1, where the filter vanishes: those modes commute with H_int, are exact zero modes on the L = 4, 6, 8 tori, and make the toy gapless at every g/t; (3) on open chains the alternating mode (-1)^x is outside the filter span ([n_face, H_int] = 0). Finite diagnostics on the bare 1D chain (Dirac points at pi/2; L = 4 exact sector diagonalisation, L = 6, 8 two-site DMRG at chi <= 96; face mode lifted): for g/t >= 4 the charge-1, charge-2 pair (the 6 of SU(4)), adjoint and neutral gaps stay of order t (pair gap 1.40, 1.76, 1.83 t at L = 4, 6, 8 for g/t = 4) while the free gaps fall as 1/L, the pair structure factor stays at its free value 1/2 within 0.04, pair correlations fall more than 10x over four sites, and there is no density or bond dimerisation; for g/t <= 1 the gaps are within about 1.5x of free. So in 1D a symmetric gapped window exists from about g/t = 2 to the largest coupling computed (16), with no pair order; nothing here decides 3D, where the face Fermi lines (item 2) keep the toy gapless. Supplied model, finite diagnostic: the toy content and quartic, the hopping and mu = 0, open chains, sizes, chi, seeds, the face lift, the sector penalty."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_filtered_quartic_chain_is_symmetric_and_gapped_at_intermediate_coupling_and_the_half_filled_3d_toy_has_free_face_fermi_lines_2026_10_22.py
---

# The filtered quartic chain is symmetric and gapped at intermediate coupling, and the half-filled 3D toy has free face Fermi lines

Claim type: bounded_theorem.
Primary runner: `scripts/the_filtered_quartic_chain_is_symmetric_and_gapped_at_intermediate_coupling_and_the_half_filled_3d_toy_has_free_face_fermi_lines_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its one open chirality wall is symmetric mass generation of the mirror family. The proposed mechanism is a pair square built on cube-averaged modes, whose form factor prod cos^2(k_i/2) vanishes on the zone faces. Two results bear on it. A strong-coupling study on sheared tori found the face composite gapped, but product states favour translation-breaking order, so the 3D phase was left undecided. A sign-free QMC of the 3D toy then found long-range charge-2 pair order at g = infinity, which is the bilinear phase, and no order at g/t = 4 and T = 1/8. This note asks the remaining question in geometries that numerics can reach exactly or at DMRG quality: is there a symmetric gapped window at intermediate g/t, with the pair channel included? It does not use the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) beyond the cubic lattice.

Model (the 3D toy QMC's toy): four flavours a_f per site, H = -g sum_x (C_x + C_x^+) - t sum_<xy>,f (a_fx^+ a_fy + h.c.), with C_x = c1 c2 c3 c4 and c_f(x) = sqrt8 times the cube average (normalised, {c, c^+} = 1). The chemical potential is mu = 0. Conserved quantities are SU(4), Z4 of mode number and Q = (n0 - n3, n1 - n3, n2 - n3). There is no SU(4)-singlet bilinear mass. The candidate orders are the pair c_a c_b (the 6, Z4 charge 2), the flavour bilinear (the adjoint) and translation breaking (density or bond waves).

## Statement

A. Exact.

1. Width-2 collapse. On L x 2 x 2 (and on L x 2 in 2D, or any cross-section with sizes 2), every cube covers the whole cross-section. The cube vectors therefore lie in the transverse-symmetric sector and span its L - 1 off-face modes. Each equals the 1D filter (a_x + a_{x+1})/sqrt2, four coincident copies per x, so H_int is the 1D filtered chain with coupling 4g. Every k_perp != 0 mode has a filter zero and is a free spectator. With the toy-QMC hopping (transverse wrap counted twice), the transverse-symmetric band is -2t cos q - 4t <= -2t, a filled band at mu = 0. So the L x 2 x 2 ladder is gapped already at g = 0 and cannot test whether the interaction gaps a massless mirror. The genuine quasi-1D test is the bare chain with band -2t cos q and Dirac points at +-pi/2, where |f|^2 = 1/2.
2. Face Fermi lines in 3D. On the face plane k_x = pi the free energy is -2t(-1 + cos k_y + cos k_z), which vanishes on the line cos k_y + cos k_z = 1. The filter vanishes on the whole plane. So those modes commute with H_int and are exactly free, gapless fermions at every g/t, and on the 4^3, 6^3 and 8^3 tori they are exact zero modes (12 of the 20 zero-energy momenta at L = 4, 12 of 24 at L = 6, 12 of 68 at L = 8). The half-filled 3D toy can never be fully gapped. Its pair order or disorder concerns only the off-face sector, and its finite-torus spectra carry exactly degenerate free face multiplets. In 1D the face q = pi sits at +2t, away from the Fermi points, so this obstruction is absent there.
3. Open-chain face mode. On an open chain the alternating vector (-1)^x is orthogonal to every two-site filter vector, so [n_face, H_int] = 0. The diagnostics lift it with 10 n_face (a supplied free term) to remove a free spectator, not to gap the mirror.

B. Finite diagnostics, bare 1D chain at mu = 0 (gaps in units of t; the ratio to the free gap on the same open chain is in brackets).

| g/t | L | particle | hole | pair (6) | adjoint | neutral | S_pair(0) |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 0.60 (0.98) | 0.78 (1.49) | 1.17 (0.95) | 1.38 (1.22) | 1.34 | 0.487 |
| 1 | 6 | 0.45 (0.84) | 0.61 (1.38) | 0.88 (0.82) | 1.07 (1.09) | - | 0.495 |
| 1 | 8 | 0.37 (1.07) | 0.54 (1.73) | 0.67 (0.97) | 0.89 (1.35) | - | 0.503 |
| 2 | 4 | 0.63 (1.01) | 1.41 (2.71) | 1.13 (0.92) | 2.01 (1.77) | 1.83 | 0.465 |
| 2 | 6 | 0.60 (1.12) | 1.10 (2.46) | 0.90 (0.84) | 1.76 (1.79) | 1.36 | 0.504 |
| 2 | 8 | 0.65 (1.88) | 0.87 (2.79) | 0.83 (1.19) | 1.77 (2.67) | 1.22 | 0.537 |
| 4 | 4 | 0.93 (1.50) | 1.62 (3.12) | 1.40 (1.13) | 3.92 (3.44) | 1.95 | 0.444 |
| 4 | 6 | 1.37 (2.55) | 1.73 (3.88) | 1.76 (1.64) | 2.90 (2.96) | 2.48 | 0.495 |
| 4 | 8 | 1.26 (3.63) | 1.98 (6.33) | 1.83 (2.63) | 3.13 (4.74) | 2.76 | 0.514 |
| 8 | 4 | 1.94 (3.13) | 2.53 (4.86) | 2.49 (2.02) | 8.52 (7.48) | 3.30 | 0.443 |
| 8 | 6 | 1.47 (2.73) | 3.73 (8.39) | 2.83 (2.63) | 4.99 (5.08) | 5.35 | 0.467 |
| 8 | 8 | 1.80 (5.20) | 3.51 (11.2) | 2.89 (4.17) | 6.19 (9.37) | 4.69 | 0.487 |
| 16 | 4 | 4.10 (6.63) | 4.67 (8.96) | 4.91 (3.97) | 18.0 (15.8) | 6.46 | 0.445 |
| 16 | 6 | 1.98 (3.69) | 6.87 (15.4) | 3.60 (3.35) | 9.34 (9.51) | - | 0.453 |
| 16 | 8 | 2.67 (7.68) | 5.94 (19.0) | 4.74 (6.82) | 9.26 (14.0) | - | 0.480 |

L = 4 is exact. L = 6 and 8 are DMRG, with gap uncertainties of about +-0.02-0.2 t: the seed spread and last-sweep drift are 1e-3 to 2e-2 g, multiplied by g/t. The free S_pair(0) is exactly 1/2. The table is from chi 96 production runs (prod3.py in the probe folder, same engine). The runner recomputes L = 4 exactly at every coupling and L = 6 at g = 4t (ground, pair and particle sectors) at chi 64; there it gives pair gap 1.87 t (1.74x free) and particle gap 1.43 t (2.66x free), against 1.76 t and 1.37 t at chi 96. The chi 64 truncation error is 6e-3 g at L = 4. The L = 8 rows are recorded production values, not recomputed by the runner.

4. Weak coupling (g/t <= 1). Every gap tracks the free 1/L gaps within about 1.5x, the hole and adjoint sectors in the upper part of that range. At these sizes this is indistinguishable from the massless chain.
5. Window (g/t = 2 to 16). The gaps stay of order t or larger as L grows from 4 to 8, while the free gaps fall from 0.62 t to 0.35 t (particle). Their ratios to free grow with L in every sector. In particular the pair gap does not close as 1/L, which quasi-long-range pair order (the 1D remnant of the 3D toy's pair phase) would require. The neutral gap stays at or above 1.2 t. The pair is the softest charged channel relative to free, so it is the leading competitor, but it is not condensing.
6. No order. S_pair(0) stays within 0.04 of its free value 1/2 (0.537 at g/t = 2, L = 8 is the largest). <P_1^+ P_y> falls from 0.022 at y = 3 to 0.002 at the end of the L = 8 chain (g/t = 4). Bond energies and densities are reflection symmetric with no period-2 alternation at the centre (centre densities 1.541 and 1.540 at L = 8). The neutral ground state is unique at L = 4 in every coupling.
7. Strong coupling. The particle gap is set by t (1.3-2.7 t for g/t = 4-16), consistent with the near-face shell g|f|^2 < t, which in 1D is an empty band near +2t. The other gaps grow with g.

## What transfers to 3D, and what would be needed

- Does a symmetric gapped window exist in this geometry? Yes, as a finite diagnostic, from about g/t = 2 up to 16, with no pair, flavour or translation order at L <= 8. That 1D can host it is not surprising: a continuous SU(4) order cannot form there, and the competing pair channel stays short-ranged.
- Does it survive widening? Not tested beyond width 1. Width 2 adds nothing: it collapses exactly onto this chain (A1) and at mu = 0 becomes a filled band. Width 3 (k_perp = 0, +-2pi/3) is the first new geometry. It needs a 12-mode rung, with DMRG bond dimensions and memory beyond the 300 MB budget, so it is not computed.
- Transfer is blocked at present for two reasons. First, 1D cannot order continuously, so the absence of pair order here says nothing about the 3D toy's pair phase at g = infinity. Second, in the half-filled 3D toy the free face Fermi lines (A2) make every phase gapless. The toy QMC's "no order at g/t = 4" therefore cannot be a fully gapped symmetric phase of that toy, and comparisons should use the off-face sector only. A 3D test of the actual wall needs a free part whose Fermi set misses the faces, as for the real mirror, whose massless point is the zone centre with face partners gapped by their own free terms. One choice is mu != 0 with the Fermi surface away from k_i = pi, or a face-gapped band such as the sheared-torus note's (1 - cos q)/2. The question is then whether the pair order seen at g = infinity melts into a gapped symmetric state at intermediate g/t, as it does here in 1D.

## Derivation

A1 builds the cube matrix on the 6 x 2 x 2 torus, projects onto the transverse-symmetric modes and compares each column with the chain filter. It also diagonalises the toy-QMC hopping matrix in that sector. A2 lists, on L^3 tori, the momenta with zero free energy and zero filter weight. A3 uses the bit-basis sector Hamiltonian (explicit Jordan-Wigner strings) for the commutator and compares it with the dense contraction of the matrix-product operator on two sites. The operator is built by automata: the quartic over emitted-flavour sets, the face projector and hopping as two-state strings, and the sector penalty lam (Q_i - t_i)^2 as a number-square automaton. B diagonalises each charge sector exactly at L = 4. C runs two-site DMRG on a mode-ordered MPS (one qubit per mode) without charge labels. The sector is selected by the exact penalty, and the neutral excitation by an orthogonality penalty. Bond dimensions run 48, 64 and then 96, with noise 1e-3 to 1e-5 in the first three sweeps; the result is the best of two seeds. A charge-labelled DMRG built first was correct at saturating chi but stuck in wrong charge-sector patterns at L = 8 (0.3-0.6 g above the true ground state, confirmed by <Q^2> = 1e-4 for the unlabelled state), so it was not used.

## Boundary

Not claimed: anything about the 3D toy's phase diagram, the Spin(10) interaction, widths >= 3, or L > 8. L = 10 at chi 96 had seed spreads up to 0.18 g and hit the memory limit, so it was discarded. Also not claimed: a thermodynamic-limit gap. Gaps of order t at L <= 8, growing relative to free, are a finite diagnostic, not a proof. Nor is any statement about the real mirror's Weyl dispersion, since the toy has non-chiral flavours.

## Supplied vs forced

Supplied: the toy content (4 flavours, SU(4)-singlet quartic) and its filter; the hopping and mu = 0 (taken from the 3D toy QMC); open chains; the sizes, chi, seeds and sweep schedule; the face lift 10 n_face; the penalty weights. Forced, given those: the width-2 collapse and its filled band; the free face Fermi lines of the half-filled 3D toy; the decoupling of the open-chain face mode; on these chains, the sector gaps and correlations tabulated above.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites and nearest-neighbour admissibility. They fix none of the supplied inputs.
- [Candidate-law register](CANDIDATE_LAWS.md): the far-rung cube-filtered pair square and the symmetric-mass-generation route. Zero premise weight.
- Sibling probes: composite-band-3d (sheared tori, 6-ring, product-state bias), filtered-smg-1d, toy-qmc (3D pair order at g = infinity). Cited, not rechecked.

## How to run

```
python3 scripts/the_filtered_quartic_chain_is_symmetric_and_gapped_at_intermediate_coupling_and_the_half_filled_3d_toy_has_free_face_fermi_lines_2026_10_22.py
```

Needs numpy and scipy. It is self-contained and declares `AUDIT_TIMEOUT_SEC = 120`. It runs in about 18 s with about 150-180 MB peak resident (checked through scripts/runner_cache.execute_runner from a clean origin/main worktree, exit 0), prints about 4.6 kB and ends with `TOTAL: PASS=7 FAIL=0`. Seeds are fixed. It has no self-kill or resource guard.
