---
claim_id: cube_tick_cannot_carry_the_shift_and_a_block_rung_insertion_reads_shift_and_shear_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the cube update tick of the candidate laws register, no copy-blind cube reading tilts the cone or shears two degenerate copies, and exact-at-rest cube insertions carry the shift only locked to a helicity term; a supplied block-rung frame insertion (2x2x2 blocks of cubes, two offset block tilings) reaches every shift and shear term, keeps every rest phase and drags every species by exactly -b, and in supplied test fields gives finite diagnostics of bending 2, frame dragging and alpha1 = alpha2 = 0; the block tiling, the insertion form, the edge reading and any physical metric or gravity law are not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/cube_tick_cannot_carry_the_shift_and_a_block_rung_insertion_reads_shift_and_shear_2026_10_21.py
---

# The cube tick cannot carry the shift, and a block-rung insertion reads shift and shear

Claim type: bounded_theorem.
Primary runner: `scripts/cube_tick_cannot_carry_the_shift_and_a_block_rung_insertion_reads_shift_and_shear_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update tick reads lapse and spatial metric from a cube's edges, but an earlier reading left out the shift g_0i and the off-diagonal shear g_ij. This note shows that one cube cannot carry the shift, and supplies a reading one rung up that can. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the reading nor the block tiling.

## Statement

On the cube rung (2^3 sites, one fermion mode per site, the register's hop and copy sign): no copy-blind cube reading tilts the cone; two degenerate copies cannot be sheared by a scalar K1K2 term; and exact-at-rest cube insertions reach every stretch, shear and frame rotation, but the shift only together with the helicity term (sqrt3/2) b_i d_ijk K_j Sigma_k.

On the supplied block rung (even cubes taken as sites, tiled by 2x2x2 blocks, with a second block tiling offset by one cube), an insertion X = sum_i J_i (x) (-theta_i + shear part), with sin 2 theta_i = b_i, applied on the first block tiling after the even half-tick and undone on the second, reaches all 48 light terms, keeps every rest phase exact, and drags every species and both copies by -b.

## Derivation

Flow (T1). For any pair of cube unitaries det U(K) = det U_o det U_e, so the 8 quasi-energies sum to a constant at each K. A drag of -b on the light bands needs +b on four others, so no copy-blind reading tilts the cone.

Reflections (T2). If both half-ticks are reflection exponentials and the light copy is exact at rest, the first-order velocities anticommute with R. The light spectrum is then symmetric under w -> -w and carries no shift, so the shift must be an extra factor.

Shear sign (T3). For a copy-blind massless reading at any step, the diagonal of {H1, H2} is nonnegative on corners lying on their face's main diagonal and nonpositive on the rest. A scalar K1K2 term must vanish.

Cube rung (T4). Readings exact for every species at rest are insertions S after the even half-tick, undone across the other tiling. Their light-copy image has rank 40 of 48. The pure shift has residual sqrt(3/5) and comes only with the helicity partner; the inversion-odd piece exists per cube only as the copy current i[N_i, s3], where s3 = i sqrt3 sum W_j W_k. The cause is that the axis hops' copy-flip parts sit at 120 degrees in the copy plane.

Block rung (T5). Moving whole cubes keeps each site's overlap state, so the drag does not twist spin, and the insertions reach rank 48. The cube-pair rotation gives a drift of exactly sin 2 theta at first order in K, to all orders in theta. With no shift or shear the insertion is the identity, so all static results of the box reading stand.

Copy-mass placement. If every cube gave the copy mass in every half-tick, the light helicities would split as K^2 off the axes. Wrapped around the even half-tick only, there is no splitting and the rest phases are the same. The register text should place the copy mass on the even cubes.

## Checks

The runner gives `TOTAL: PASS=17 FAIL=0` in 12 s.

- A1: sqrt3 W_i and i[N_i, sqrt3 W_i] are six anticommuting generators; s3 commutes with the light Dirac algebra, is kept by the 12 tetrahedral turns and flipped by the 12 odd ones (7e-15).
- A2, A3, A4: the flow theorem (spread of sum w 3e-15 on random cube unitaries), the reflection theorem (max |{H_i, R}| 3e-16) and the shear-sign theorem (6 random readings).
- A5: cube-rung light image of rank 40/48, pure-shift residual 0.7746 = sqrt(3/5), partner coefficients +0.8660.
- A6: copy mass in every half-tick splits helicities 1.69e-4 at |K| = 0.08 (slope 2.00); on the even half-tick only, 2e-15.
- B1, B2: block-rung rank 48; rest phases exact to 6e-16; tilt/(-b.K) between 0.99998 and 1.00004 for light and heavy species; helicity split 1e-15.
- B3: (w + b.K)^2 = v_i v_j (1 + sigma)_ij K_i K_j with second-order errors (tilt, shear errors 6e-7, 5e-3 at 1x and 2e-7, 5e-4 at 0.1x); massive shear weight 1.0877 against a formula value of 1.0882 at mu/eps = 1/6.
- B4: the insertion is a vector or tensor under the 24 block rotations (1e-17); the tick with copy mass keeps the 12 tetrahedral turns (24 at M = 0); J_i is odd under inversion.
- C1: a packet moving along y in b_y(x) is pushed at the eikonal rate (lattice/eikonal 1.0022 massless, 0.9976 massive); a curl-free b_x(x) pushes at most 1e-4 as much.
- C2: packets along (1, +-1, 0) in h_xy(z) bend at the eikonal rate (0.9999) with opposite signs; the box reading gives 3e-10.
- D1: in two fixed-4-volume gauges with lattice-measured light speeds, 1 + gamma = 2.0000 on axis, face, body and generic rays (max deviation 1e-5); the box reading gives 1 + sum k^4 (1.5000 face, 1.3333 body).
- D2: parts feeling v x B make a rotor precess at -B/2; with coefficient 1 this gives the frame-dragging formula G J cos(dec)/(2 c^2 a^3).
- D3: for a source moving at w = (0.12, -0.09, 0.07), the lattice-read lapse, shift and cone match the boosted metric, with fitted alpha1 = +1.3e-6 and alpha2 = +7.6e-7 (box reading: alpha1 = -6.62).
- E1, E2: with no shift or shear the insertion is 1 (drag deviation 3e-7, spin commutator 0); sin 2 theta = b gives the drift to all orders (drift/b - 1 = 3e-7 at |b| = 0.15); the implicit null-cone rule converges for a shear of 0.15 (error 3e-6).

Estimates (not checks). The frame-dragging formula gives 39.1 mas/yr for Gravity Probe B, against a measured -37.2 +- 7.2 (0.95 +- 0.18), and the LAGEOS rate 30.7 mas/yr. The cube-rung shift reading would give a 3.1 GeV muon about 11 eV of spin energy, against a g-2 precession of 1e-9 eV measured to 2e-7, which excludes it. The copy mass in every half-tick would give eta of about 11 for a cube of 10 Planck lengths, against the Crab bound of about 1e-7. In the lattice frame the shift is about 4Uw: 4e-9 from the galaxy, 5e-11 from the Sun at 1 AU. The alpha diagnostics assume that the register's gravity law gives the metric in the lattice frame.

## Boundary

Derived: the flow, reflection, shear-sign, cube-rung and zoom theorems, and the exact drift law. Supplied: the block tiling one rung up (range one cube, a proposal not derived from the axioms), the forms of J_i and V_j (from a family that is not unique), the edge reading of lapse and inverse metric, the placement of the insertion between half-ticks, the copy-mass placement, the test fields, gauges, packets, cube size and measured numbers. Not established: that photons, which are links, read the same metric (needed for radio bending of 2); dragging of an elementary spin at rest, which needs a curl term; second-order shift-shear cross terms in strong fields; and any adopted reading or physical gravity law.
