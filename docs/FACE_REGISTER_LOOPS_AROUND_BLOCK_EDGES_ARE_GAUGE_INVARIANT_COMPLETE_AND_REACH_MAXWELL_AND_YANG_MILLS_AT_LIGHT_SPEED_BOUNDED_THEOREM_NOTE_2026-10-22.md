---
claim_id: face_register_loops_around_block_edges_are_gauge_invariant_complete_and_reach_maxwell_and_yang_mills_at_light_speed_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For link registers on the faces of a gauge factor's B_f-blocks (2S rishon modes per end, Gauss's law per block), take as loops the cycles of blocks around each block-edge segment (four faces in the bulk; three or four faces of mixed sizes beside a split block, 72 triangles and 774 squares on the tested slab) and as loop operator Re tr of the ordered product of the faces' link operators. Exact: for U(1) at S = 1/2, 1 (square and hanging triangle) the loop of domain-normalised raisers V, and of rishon bilinears, conserves every block's rishon number, and an open string does not; every U(1) register up to S = 2 has V of definite charge with V^dag V a projector; SU(2) and SU(3) rishon links are covariant at each end (polar part too), and the many-body loop commutes with every colour Gauss generator (SU(2) square, dimension 65536; SU(3) hanging triangle, dimension 262144) while a wrongly contracted link fails. The loop set is complete: dim ker(curl) = (blocks - 1) + 3 on a 4^3 torus and on a hanging slab. With face weight h/A and loop weight l/S (flat: 1/B_f), electric g^2/2 and magnetic 1/(g^2 T): for the tested fields (three Fourier modes per component, wavelength 24 cells) the lattice magnetic energy approaches (1/2) int B^a B^a with the full Yang-Mills commutator (26% of the test energy), with errors at B_f = 1, 2, 3 whose ratios are consistent with O(B_f^2), for U(1), SU(2) and SU(3) (finite diagnostic; the continuum limit and its order are not proved); with the face value defined as B_f^2 E at the face centre (a supplied sampled definition) the electric energy equals (1/2) int E^a E^a exactly for the tested trigonometric fields when no frequency sum or difference aliases on the B_f grid, while with the face value defined as the flux integral it is not exact (sinc factors; 3.4e-2 and 7.4e-2 at B_f = 2, 3); the harmonic photon is omega^2 = (4/B_f^2) sum sin^2(k_i B_f/2) with speed 1 for every B_f, independent of g; weights (N/sqrt gamma) gamma_ij per block, with off-diagonal terms through the block's mean face values and mean loop fluxes, give the null cone N^2 gamma^ij k_i k_j at O(k^2) in a diagonal and a sheared metric, with both energy forms positive definite at every k. Subtracting the vacuum phase once gives zero vacuum phase at every edge value and exactly omega per photon; the superseded extra subtraction leaves minus half the zero-point, edge-dependent. Across a hanging face the uniform-E and in-plane uniform-B patch tests are exact, a normal B costs an extra layer of B/6 per interface, and at the two cavity sizes tested the spectrum moves toward the c = 1 continuum (max deviation 0.297 -> 0.084 as blocks halve, torus 4x4x8 child units), with that layer behaving as a first-order term (effect 0.042 -> 0.027) (finite diagnostic). Finite diagnostics of supplied models: single-loop register truncation at supplied couplings (U(1) gap 5.6x at S = 1/2, 1.44x at S = 3, 1.01x at S = 6; SU(2) 2.5x at j = 1/2; SU(3) 1.07x at p + q = 1), with a supplied identification of register size with representation cutoff. Not established: the small-S dressed coefficients, the shift's entry into the weights, extreme register values, bending and shear on face registers, the off-diagonal pairing as the only covariant choice."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/face_register_loops_around_block_edges_are_gauge_invariant_complete_and_reach_maxwell_and_yang_mills_at_light_speed_2026_10_22.py
---

# Face-register loops around block edges are gauge-invariant and complete, with a light-speed harmonic photon and Yang-Mills energies approached on tested fields

Claim type: bounded_theorem.
Primary runner: `scripts/face_register_loops_around_block_edges_are_gauge_invariant_complete_and_reach_maxwell_and_yang_mills_at_light_speed_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. After its fourth review, CL-1 puts each gauge factor's link registers on the faces of that factor's B_f-blocks. The blocks are made of whole even cubes, so only odd-cube hops cross a face. Each register is 2S rishon modes at each end, and Gauss's law holds per B_f-block. CL-3's plaquette phase is still written for the superseded site-bond layout (six skew loops per bond). This note supplies the plaquette law for face registers and checks it. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

Local labels and sources (2026-11-14). CL-1 and CL-3 are the update and response laws of the originating three-law register and its fourth review (review 4, L2), supplied model text with zero premise weight; they are not the entries of the same number in `docs/CANDIDATE_LAWS.md`, and the review-4 text is not in this repository (recorded only in the consolidation map). #9926 is [this note](LINK_REGISTERS_BUILT_FROM_RISHON_FERMION_MODE_SITES_CARRY_EXACT_U1_AND_SU3_GAUSS_LAWS_AND_SIT_COVARIANTLY_FROM_ZOOM_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md) and #9928 is [this note](LINK_REGISTER_SPLIT_TRANSPORT_AND_RESPONSE_GIVE_A_COVARIANT_LEVEL_MATCHED_ZOOM_MAP_BORN_EXPONENTIAL_DECAY_AND_THE_MAXWELL_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-22.md); #9931 and #9917 are not in this repository and are recorded only in the map.

Correction (2026-11-14). The held version called the electric energy exact for band-limited fields and stated O(B_f^2) convergence and cavity convergence as results. The electric identity holds for a sampled face value, not for the flux integral (C2 below), and the convergence statements are finite diagnostics at the mesh sizes tested.

Repo check. On origin/main no note gives a face-register plaquette on nested blocks. The note builds on, or narrows, four open PRs:
- #9926 (link-zoom): rishon links, Gauss's law as cluster number, and the 8-rishon plaquette on a cubic site.
- #9931 (site-registers): skew loops for the site-bond layout. That layout no longer hosts a measured factor.
- #9917 (links-metric): the site reading of the plaquettes in lapse, shift and metric.
- #9928 (register-consistency): the photon band, the Coulomb law and the vacuum standard for cubic registers.

This note carries the cubic-layout results over to nested face registers with hanging faces, and adds the non-abelian and small-S checks. It narrows the register's "[cubic] layout has no extra mode" to a computed rank statement (B1).

## Proposed law text (replaces CL-3's "Plaquette phase" paragraph)

> "Plaquette phase. For each gauge factor, the registers on the faces between consecutive blocks around each segment of a B_f-block edge form one loop. A segment is a stretch along which the same blocks meet. A loop has four faces in the bulk, and three or four faces of mixed sizes where a block's neighbour has split. The loop operator is the real part of the trace of the ordered product of those faces' link operators, the rishon bilinears normalised on their domain: V for a face crossed along its orientation, V^dagger against it. The plaquette phase per tick is N times a sum of two parts. The electric part is g^2/2 times each face register's electric Casimir times h/A, where A is the face's proper area and h is the proper distance, along its normal, between the centres of the two blocks it joins. The magnetic part is 1/(g^2 T) times (n - Re tr) of each loop times l/S. Here l is the loop's proper segment length, S is the proper area of the polygon of its blocks' centres projected across the segment, n is the dimension of the link representation, and T is the trace normalisation of the factor's generators in it. Where a block's cell metric is not diagonal, each block counts its share with the weights (N/sqrt(gamma)) gamma_ij, diagonal terms per face and per loop, and off-diagonal terms through the block's mean face values of normals i and j and the mean loop fluxes along i and j. Each term is shared equally among the blocks it touches. The electric and magnetic coefficients are those at which the vacuum's dressed coupling of that factor, at a fixed proper wavelength and in a uniform field of every proper direction, is a constant of that factor, the same for both and in every cell."

In flat cells h/A = l/S = 1/B_f, where B_f is the block side in cell rung lengths. The Total phase already counts the plaquette phase among the update's terms and subtracts one vacuum phase of the same edges (review 4, L2), so the law has no subtraction clause of its own.

## Statement

A. Gauge invariance per B_f-block (exact).
1. U(1). V has definite charge: it moves one rishon from end X to end Y, and V^dag V is a projector, for every register size S from 1/2 to 2. So around any closed cycle of blocks, each block gains one rishon and loses one, and every closed loop conserves every block's Gauss generator for every S. This holds for any number of faces and any face sizes. The full many-body check confirms it for S = 1/2 and S = 1 on a bulk square and a hanging triangle (a coarse block with two face pieces). An open string fails.
2. SU(N). The rishon link U^{ab} = c_{X,a} c_{Y,b}^dagger transforms as Omega_X U Omega_Y^dagger at each end, and so does its polar (domain-normalised) part. Re tr of the many-body loop commutes with every colour Gauss generator of every block: max |[W, G]| = 0 for the SU(2) square (dimension 65536) and the SU(3) hanging triangle (dimension 262144). Transposing the colour contraction on one link breaks invariance (0.25).

B. Completeness (exact). In both of the following, curl.grad = 0 and dim ker(curl) = (blocks - 1) + 3:
- a 4^3 torus (192 loops);
- a half-split slab, 243 blocks with 774 square and 72 triangular loops.

So every non-gauge face configuration other than the three torus holonomies changes some loop. The face layout needs no skew loops and has no stiffless extra mode, unlike the site-bond layout.

C. Classical continuum (finite diagnostics except C2a).
1. Magnetic part: for the tested fields (three Fourier modes per component, amplitude 0.1, wavelength 24 cells), the sum over loops of (1/(g^2 B_f T)) Re tr(1 - U_loop) approaches (1/2) int B^a B^a with F = dA - dA + i g [A, A].
   - Relative error at B_f = 1, 2, 3: U(1) 6.1e-3, 2.9e-2, 8.0e-2; SU(2) 2.1e-2, 8.2e-2, 1.8e-1; SU(3) 2.0e-2, 8.0e-2, 1.7e-1.
   - The error ratios, 3.9 to 4.8 and 2.1 to 2.8, are consistent with O(B_f^2). Three mesh values do not prove the continuum limit or its order; no analytic error estimate is supplied here.
   - The commutator changes the test energy by 26%, so the check covers the non-abelian term.
2. Electric part.
   - 2a (exact, for a supplied definition). Define the face value as the sample Phi = B_f^2 E(face centre)/g. Then (g^2/(2 B_f T)) sum tr Phi^2 is a Riemann sum with cell volume B_f^3, and for a trigonometric-polynomial field it equals (1/2) int E^a E^a exactly whenever no nonzero sum or difference of two field frequencies is a multiple of the grid's n = L/B_f points per axis (a discrete-orthogonality identity of the uniform grid; the centre offset itself is not what makes it exact, and a jittered sample breaks it). For the tested fields that holds at B_f = 2, 3 (deviation 2e-16); control: at B_f = 12 (n = 2) the frequency 2k aliases to 0 and the identity fails (deviation 0.25).
   - 2b (negative result kept). With the face value defined as the actual flux, the integral of E over the face, each Fourier component carries a factor sinc(k_perp B_f/2) per transverse direction, so the identity is not exact: deviation 3.4e-2 and 7.4e-2 at B_f = 2, 3 for the tested U(1) field (ratio 2.20, about B_f^2), and 3.0e-2 and 6.6e-2 for SU(3). Midpoint equality is a property of the sampled definition, not of the flux.

D. Harmonic photon (exact).
1. Flat cells: omega^2 = (4/B_f^2) sum sin^2(k_i B_f/2) for both polarisations, plus one gauge zero. The speed is 1 cell per unit time as k -> 0 for B_f = 1, 2, 3 and 24, along axes, face diagonals and body diagonals, at any g. The relative normalisation c_E c_B = 1/(2 B_f^2) [U(1)] is the light-cone condition.
2. Metric weights. With (N/sqrt gamma) gamma_ij, and the off-diagonal terms paired through block means, both branches reach N^2 gamma^ij k_i k_j at O(k^2):
   - diagonal metric (lapse 0.7, B_f = 3): relative error 3.1e-5 at k B_f = 0.02;
   - sheared metric (lapse 1.1, B_f = 2): relative error 5.0e-5.
   Both energy forms equal gamma o (c c^T) plus a non-negative diagonal, so they are positive definite at every k (Schur product).

E. Small S. These are finite diagnostics of a supplied model: one isolated loop of 4 faces, Kogut-Susskind character basis truncated at the register size.
1. Weak coupling (g^2 = 0.03), untruncated: the gap is the harmonic value set by the same c_E c_B: 2/B_f for U(1) (0.992 of it), and 4/B_f, the first class-function level, for SU(2) (0.995) and SU(3) (0.991).
2. At supplied couplings (alpha = 1/137, 0.0338, 0.118), the gap over the untruncated gap is:
   - U(1): 5.58 at S = 1/2, 4.00 at 1, 2.17 at 2, 1.44 at 3, 1.01 at 6;
   - SU(2): 2.54 at j_max = 1/2, 1.83 at 1, 1.12 at 2;
   - SU(3): 1.07 at p + q = 1.
   So at small S the bare Hodge coefficients do not give the light cone. CL-3's dressed-coupling clause ("the same for both") must set them, and the register text already makes it do so.

F. Vacuum subtraction (exact on a harmonic 4^3 torus; one exact S = 1 loop). With one subtraction of the vacuum phase of the same edges, the vacuum's phase is 0 at every edge dilation and a one-photon state's phase is exactly omega. The superseded text also subtracted the plaquette's vacuum Born mean, which leaves -<H_B>_vac: half the zero-point by the virial theorem (-76.2 at lam = 1, -58.6 at 1.3). That gives a spurious vacuum energy and edge force. At S = 1, <H_B>_vac = 0.592, nonzero. Review 4's L2 is therefore required, not cosmetic.

G. Hanging faces after a split. The coarse face holds four child-face registers, each joining the unsplit block to one child, and the unsplit block's Gauss law counts all four.
1. Patch tests:
   - uniform E in every direction, and uniform B along the interface: exact (deviation 0);
   - normal B: an extra layer of B/6 per interface, with B the unsplit side, because the hanging loops' centre polygons tilt.
2. Cavity spectrum (torus 4x4x8 child units, half split, 72 then 576 blocks; finite diagnostic at two sizes):
   - the lowest 21 modes move toward the c = 1 continuum, with max deviation 0.297 -> 0.084 (ratio 3.5) as all blocks halve; two sizes establish no convergence order;
   - the B/6 layer behaves as a first-order term (effect 0.042 -> 0.027, ratio 1.56 at these coarse sizes);
   - removing it by rescaling the first child layer's normal-edge loops makes the spectrum slightly worse (mean deviation 0.173 and 0.064, against 0.160 and 0.055), so the plain rule is kept.
   At Planck-scale blocks the first-order term is of order k B, about 1e-30 at accessible wavelengths (estimate).

## Smuggling check

Forced by the stated requirements:
- the loop set: the smallest gauge-invariant closed products, which B shows complete;
- the trace closure, by covariance;
- h/A and l/S in flat bulk cells (1/B_f), from the patch tests;
- the electric-magnetic product, from the light cone;
- the single subtraction, by F.

Supplied, and named:
- the coupling g per factor (the law's dressed-coupling clause fixes the dressed value; the bare g is supplied);
- the register size S;
- B_f;
- the convention T (1 for U(1) with unit charge; 1/2 for SU(N) fundamental), which cancels against the generator normalisation;
- the choice of block centres as the polygon vertices at hanging faces, which produces the B/6 layer;
- the pairing of off-diagonal metric terms through block means (positive and correct at O(k^2), not shown unique);
- V (domain-normalised) rather than the bare bilinear as the U(1) link in the loop, chosen to match CL-1's dressing;
- the cavity box, the test fields, and the couplings 1/137, 0.0338 and 0.118;
- in E, the identification of register size with a representation cutoff;
- in C2a, the face value as the centre sample B_f^2 E rather than the flux integral.

No measured number enters the law. The measured couplings appear only in diagnostic E2.

## Open

- The shift enters through CL-1's block-pair rotation; it is not in the weights here.
- Registers at extreme values: V_loop vanishes there.
- The small-S dressed coefficients, which need a many-loop calculation.
- Bending and shear on face-register plaquettes (#9917 is site-read).
- Children within register range.
- Whether another covariant off-diagonal pairing exists that is exact at the hanging face for normal B.
- An analytic estimate of the magnetic continuum error (C1) and of the cavity convergence (G2); the electric energy with flux-integral face values beyond the tested fields.

The runner ends with `TOTAL: PASS=16 FAIL=0` and exits nonzero if any check fails.
