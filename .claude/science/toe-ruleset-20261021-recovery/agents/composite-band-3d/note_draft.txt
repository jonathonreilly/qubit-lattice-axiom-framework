---
claim_id: the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the cube-filtered quartic interaction at g -> infinity (c_x = sqrt8 times the cube average of the site modes, one charge-4 quartic per cube): the filtered modes have {c_x, c_y^+} = prod_i (1, 1/2, 0)[|x_i - y_i|] and on L^3 span exactly the (L - 1)^3 off-face momenta (rank 27 at L = 4, 125 at L = 6), so face modes are free spectators; the sheared tori T_n = Z^3/Lambda_n (n = 1, 2, 3, det L) are legitimate 3D tori carrying only the lines (q,0,0), (q,q,0), (q,q,q), on which the cube filter is exactly ((1 + e^iq)/2)^n with the faces X, M, R at q = pi; overlapping filtered terms do not commute (toy norms 0.866, 0.484, 0.248 for overlaps 1/2, 1/4, 1/8), so the limit has no atomic form; [e_k, H_int] = sum_x conj(A_xk) D_x with a three-fermion D (identity error below 1e-12 on T_1, L = 4); for mode-product states <h(c_y)> = e_atom sum_m beta_m(y)^4 for any charge-4-only quartic. Toy diagnostics (4 flavour modes, one SU(4)-singlet quartic c1c2c3c4 + h.c. per cube, not Spin(10)): open clusters of up to 5 cubes have unique ground states; on T_1, T_2, T_3 at L = 4, 6 the face composite D(face)|GS> has no weight below 0.5 and lowest pole 0.9-2.3 atom units, with and without a face-gapped free band; t = 0 is singular at the faces (near-face modes almost free); a two-cube linked-cluster expansion fails the 1D control (about 0 against the exact 1.01), so it does not decide 3D. The gapped face composite is a finite diagnostic on these tori; the 3D question stays undecided. Supplied model, finite diagnostic: the toy content and quartic, the cluster shapes, the torus sizes and shears, the free band, the atom units."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_2026_10_22.py
---

# The strong-coupling face composite has no atomic limit and stays gapped on sheared tori

Claim type: bounded_theorem.
Primary runner: `scripts/the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. One route to chiral matter without doublers gaps the doubler modes at the zone faces with a strong multi-fermion interaction, applied at a far rung through a cube filter: each cube carries a quartic in the cube-averaged modes. The route needs a symmetric phase in which the three-fermion composite stays gapped at the faces X, M and R. A composite band that flattens to zero there would bring the doublers back as composites. An earlier 1D filtered probe found the composite gapped there (the runner cites it; not rechecked here). This note asks what can be decided in 3D at g -> infinity. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Exact structure (any charge-4-only quartic unless marked toy).

1. Filter kernel and span. With c_x = sqrt8 times the cube average b~_x, {c_x, c_y^+} = prod_i (1, 1/2, 0)[|x_i - y_i|]. On an L^3 torus the c_x span exactly the (L - 1)^3 off-face momenta. So H_int lives there, and face modes are free spectators.
2. Sheared tori. T_n = Z^3/Lambda_n (det Lambda_n = L) carries only the momenta (q,0,0), (q,q,0) or (q,q,q) for n = 1, 2, 3. On it the cube filter becomes ((1 + e^iq)/2)^n, with the faces X, M, R at q = pi and the exact 3D zero order |f|^2 ~ cos^(2n)(q/2). These are legitimate 3D tori of transverse size one cell (no transverse coordination).
3. No atomic limit (toy, exact). Overlapping filtered terms do not commute: ||[h_x, h_y]|| = 0.866, 0.484, 0.248 for overlaps 1/2, 1/4, 1/8, and 0 for disjoint cubes. A two-term cluster cannot reach 2 E_atom (energy per term -0.901, -0.970, -0.992). So at g -> infinity the composite moves at order g through the overlap, not at t^n/g^(n-1).
4. Composite operator. [e_k, H_int] = sum_x conj(A_xk) D_x, with D_x three-fermion and A_xk proportional to f(k) e^ikx. D(face) is nonzero. The runner states, and does not separately compute, that its propagator is exactly the kernel Sigma/|f|^2. The commutator identity is checked.

B. Mode-product states.

5. For any charge-4-only quartic (Spin(10) included), a product of per-mode atomic singlets has vanishing cross-mode terms by Z4, so <h(c_y)> = e_atom sum_m beta_m(y)^4. The site product gives 1/2^d per term and the cube solid (5/4)^d/2^d. The best product, found by quartimax optimisation, is non-uniform: products favour translation breaking, more so in 3D.

C. Toy exact diagonalisation at g -> infinity. The toy has 4 flavour copies and one SU(4)-singlet quartic c1c2c3c4 + h.c. per cube on the same filter. It is not Spin(10). Each term is normalised so a lone term (the atom) has gap 1.

6. Open clusters of up to 5 cubes (1D to 3D shapes) have a unique ground state (gap > 0.1). The exact energy per term lies only 0.3-9% below the best mode product. The face-signed composite lies below the uniform one, so open clusters do not separate it from the soft near-face elementary modes.
7. On T_1, T_2, T_3 (L = 4, 6), D(face)|GS> has no weight below 0.5. Its lowest pole is 0.9-2.3 atom units at X, M and R, with and without a face-gapped free band h = 0.25(1 - cos q)/2. There is no flattening on these tori, and every ground state has K = 0.
8. t = 0 is singular at the faces. The elementary energy is eps(q) ~ c|f(q)|^2 with c = 1.4-1.6, vanishing at the faces, so near-face modes are almost free, and softer for higher n. The T_3 neutral gap is made of near-face pairs. Every t = 0 propagator zero is pinned at w = 0. The runner attributes this to particle-hole times inversion, which is stated. The shell g|f|^2 < t around each face is weakly coupled at any g.
9. With the free band the propagator zero leaves w = 0 and moves monotonically away toward the face, or leaves the window. It disperses into the gapped face composite on all three lines.
10. On the 6-ring T_1 the ground state is unique with K = 0, <h_x> is uniform, and the connected <h_0 h_d> decays without period-2 alternation: there is no cube solid.

D. The method's limit. A two-cube linked-cluster estimate of the composite band puts the 3D composite below zero at X, M and R. In 1D the same estimate predicts about 0 where the exact ring gives 1.01. Overlap 1/2 is not small, so the expansion does not decide 3D. This is a negative result for the method, not for the 3D question.

## Derivation

Item 1 builds the cube-average matrix on 4^3 and 6^3 tori and computes the rank of its Gram matrix and its first row. Item 2 checks det Lambda_n = L, the face periodicity, the binomial weights of the quotient filter and |filter|/|cos(q/2)|^n near q = pi at L = 6. Item 3 builds each term in a flavour-blocked Fock basis, cross-checked against an independent dense Jordan-Wigner build of 8 modes (256 states) for the nearest-neighbour pair, and computes operator norms and ground energies for the four relative positions. Item 4 compares both sides of the commutator identity on T_1, L = 4. Item 5 checks the product-state identity on the pair. It then optimises the per-term energy over orthogonal mode bases by an iterated polar (quartimax) update from identity, Hadamard (cube-solid) and three seeded random starts, on an 8-ring and a 4^3 torus. Items 6-10 diagonalise H_int, dense for at most 2000 states and Lanczos (scipy eigsh) above that, in fixed-charge and fixed-momentum sectors. They read the composite spectral weight of D(face)|GS> by exact eigendecomposition or a 70-step Lanczos continued fraction, and find propagator zeros as sign changes of G(w) on a 4001-point grid. Item D estimates the band from two-cube clusters at the three relative positions and sums over the 26 neighbours.

## Finite checks

Exact checks (the runner asserts each):
- Filter Gram rank: 27 at L = 4 and 125 at L = 6, equal to (L - 1)^3; the kernel row matches prod_i (1, 1/2, 0).
- Sheared-torus filter weights: n = 1: [1, 1]/2; n = 2: [1, 2, 1]/4; n = 3: [1, 3, 3, 1]/8.
- Toy commutator norms 0.866, 0.484, 0.248, 0.000 and energies per term -0.901, -0.970, -0.992, -1.000 (overlaps 1/2, 1/4, 1/8, disjoint). The flavour-blocked engine reproduces the dense 256-state spectrum.
- Commutator identity error below 1e-12 (T_1, L = 4).
- Product-state identity error below 1e-12.

Finite diagnostics (supplied model, finite diagnostic):
- Mode products. 1D ring of 8: site 0.500, solid 0.625, best 0.692 (std 0.13). 3D 4^3: site 0.125, solid 0.244, best 0.368 (std 0.19). The best-to-site ratio is about 1.4 in 1D and 2.9 in 3D.
- Open clusters (energy per term exact / best product; neutral gap; lowest composite pole, uniform and face-signed):

| cluster | E/term | gap | uniform | face-signed |
|---|---|---|---|---|
| line3 | -0.867 / -0.823 | 0.40 | 1.09 | 0.27 |
| line5 | -0.839 / -0.771 | 0.14 | 0.92 | 0.11 |
| plate 2x2 | -0.818 / -0.766 | 0.36 | 1.02 | 0.24 |
| tripod4 | -0.850 / -0.816 | 0.48 | 1.00 | 0.31 |
| tet4 | -0.927 / -0.924 | 1.31 | 1.19 | 0.77 |
| cube5 | -0.813 / -0.764 | 0.34 | 0.97 | 0.23 |
| star3d5 | -0.853 / -0.823 | 0.43 | 0.98 | 0.29 |

- Sheared tori (E0 per term at L = 4, 6; neutral gap; lowest and mean face-composite pole; propagator zero at q = 0, pi/3, 2pi/3 with the free band m = 0.25):

| torus | E0/term | neutral gap L4 / L6 / m = 0.25 | D(face) lowest/mean L4; L6; m = 0.25 | zeros at m = 0.25 |
|---|---|---|---|---|
| T_1 (X) | -0.831, -0.809 | 1.355 / 0.552 / 0.927 | 1.83/1.88; 1.01/1.62; 1.11/1.52 | -0.36, -0.43, -0.54 |
| T_2 (M) | -0.797, -0.786 | 0.815 / 0.116 / 0.724 | 1.91/2.05; 0.91/2.29; 1.27/2.26 | -0.26, -0.32, -0.56 |
| T_3 (R) | -0.795, -0.797 | 0.386 / 0.012 / 0.747 | 2.27/2.52; 2.31/2.58; 1.36/2.59 | -0.18, -0.21, none in window |

- Face-composite weight below 0.5: below 1e-12 on every torus. D norm^2 at the face (L = 6): 0.228, 0.095, 0.042 for T_1, T_2, T_3. The runner asserts a weight below 1e-12 and a lowest pole above 0.85 on every torus.
- Near-face softness. eps/|f|^2 on T_1: 1.45, 1.44, 1.55, 1.55, 1.44. eps(2pi/3) on T_1, T_2, T_3: 0.388, 0.082, 0.009. The T_3 gap goes from 0.012 at t = 0 to 0.747 with the free band. Every t = 0 zero lies within 5e-3 of w = 0.
- 6-ring T_1: <h> = -0.809, and connected C(d = 1, 2, 3) = -0.1007, 0.0186, 0.0013.
- Linked-cluster estimate: G +3.22, X -1.21, M -1.47, R -1.62. The 1D estimate is +0.01, against the exact 1.01.

The random starts use fixed seeds.

## Boundary

Not claimed: any statement about the true 3D thermodynamic limit (the sheared tori have transverse size one cell, and the clusters are at most 5 cubes); the Spin(10) interaction, since only the toy SU(4)-singlet quartic is diagonalised (items 1, 2 and 4 and the identity of item 5 hold for any charge-4-only quartic, Spin(10) included); finite g or finite t beyond the one free band; the kernel statement for the D propagator and the particle-hole times inversion reason for the pinned zeros (stated); a decision of the 3D gap question, which stays undecided; that the strong-coupling cluster expansion is the right method (it fails the 1D control).

## Supplied vs forced

Supplied: the toy content (4 flavour modes, one SU(4)-singlet charge-4 quartic per cube); the atom units; the cluster shapes; the torus sizes L = 4, 6 and the shears Lambda_n; the free band h = 0.25(1 - cos q)/2; the Lanczos depth, grid and thresholds; the seeds of the random starts. Forced, given those: the filter kernel and the (L - 1)^3 off-face span; the exact restriction of the cube filter to ((1 + e^iq)/2)^n on the sheared tori; the non-commutation of overlapping terms and so the absence of an atomic limit; the three-fermion composite identity; the mode-product identity; on these tori and clusters, the gapped face composite and the near-face softness at t = 0.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the cube structure of the update law, the far-rung cube filter, and the symmetric-mass-generation route for gapping the face modes. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_strong_coupling_face_composite_has_no_atomic_limit_and_stays_gapped_on_sheared_tori_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 26 s with at most about 270 MB peak resident (230-267 MB measured), prints about 5.2 kB and ends with `TOTAL: PASS=11 FAIL=0`. Its random starts use fixed seeds; two runs gave identical output apart from the timing lines.
