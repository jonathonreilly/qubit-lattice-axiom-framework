---
claim_id: a_cube_tick_read_from_its_edge_lengths_and_duration_in_weak_static_fields_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For a supplied reading of the cube tick from its three axis edge lengths and its proper duration, the half-ticks stay unitary reflections, the massless cone is the null cone of the edges, clocks at rest run at proper time exactly, and in supplied weak static fields packets fall universally up to (mu/eps)^2/4 and light is pulled by (1 + gamma) times the Newtonian value; growing edges redshift photons against atoms; the reading cannot carry shift or shear and leaves the sea's tensor/Newtonian mismatch; no adopted reading, vacuum clause, frame dragging or link reading is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_cube_tick_read_from_its_edge_lengths_and_duration_in_weak_static_fields_2026_10_21.py
---

# A cube tick read from its edge lengths and duration in weak static fields

Claim type: bounded_theorem.
Primary runner: `scripts/a_cube_tick_read_from_its_edge_lengths_and_duration_in_weak_static_fields_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update has each cube read its unitary from its own edges, and its response law needs matter to depend on edge lengths. This note tests one concrete reading: each cube reads only its three axis edge lengths L_i and its proper tick duration tau. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the fields or packets used.

## The reading

The cube's hop R is the sum of the axis parts W_i of the spin-3/2 edge hop, each weighted by 1/L_i, scaled so that R^2 = 1. Its step obeys sin eps = sqrt 3 tau rms(1/L_i), and a species of mass m uses mu = m tau. The half-ticks are exp(-i(eps - mu/2)R) on even cubes and exp(+i(eps + mu/2)R) on odd cubes. With equal edges R = W and this is the register's update.

Within the family of one reflection per cube from the span of the W_i, the reading is forced: requiring the cone to be the null cone of the edges fixes the weights at 1/L_i and the formula for eps, and requiring clocks at rest to run at proper time fixes mu = m tau and puts the mass phase on R. With the mass phase on W instead, the rest phase is 0.099916 rather than 0.1.

## Theorems

1. sqrt 3 W_i are Clifford generators and W is their sum over sqrt 3. So R is a traceless reflection for every edge set, each half-tick is unitary with det 1, and the quasi-energies sum to 0 in any geometry.
2. All 8 bands of the box tick obey cos w = A S_f(K) + (cos 2 eps + cos mu)/2, with S_f = sum f_i^2 cos K_i / sum f_i^2. At K = 0 every phase is +-mu for any edges, so a clock at rest runs at m times proper time.
3. The massless cone is the null ellipsoid v_i = tau/L_i of the edges.
4. Each of the 24 proper cube rotations fixes W and maps R(f) to R(rotated f).
5. w(K) = w(-K) and the cone has no K_i K_j cross terms, so a cube read from its axis lengths and duration cannot carry a shift (tilted tick edges) or a shear between axes.
6. A massless species evolves identically under (N, L) and Omega(z)(N, L). Null geodesics are conformally invariant, so this is the right invariance for light.
7. For g = e^{2s} eta, sqrt(-g) R = -6 e^{2s}(s'' + s'^2), a total derivative plus 6 e^{2s} s'^2. The Einstein-Hilbert action depends on the conformal factor, so a sea that sees only tau/L cannot induce it, and any q^2 term it does induce breaks the relation between tensor and Newtonian couplings.

## Checks

The runner gives 17 PASS and 0 FAIL. These are finite diagnostics of supplied models, with eps0 = 0.3 and N = 1 + Phi, L = 1 - gamma Phi, Phi = g z, g = 2e-5.

- Reflection property 7.3e-15; band law 3.7e-15 and rest phases 1.0e-15; null-cone deviation 3.9e-8 at |K| = 1e-3; rotations 3.1e-15. A massless species is unchanged under a conformal rescaling to 4.7e-16 after 300 ticks, against 0.11 for a massive one.
- Free fall: a slow packet falls at -c_m^2 dPhi/dz for gamma = 0 and 1 to 2.8e-4, where c_m^2 is the band's rest energy over inertial mass. The lapse alone drives the fall.
- Universality: species differ only through c_m^2/c_0^2 = 1 + mu^2(1/6 - 1/(4 sin^2 eps)) + O(mu^4). At mu = 0.03 against 0.12 the packets and the band both give 0.0365, and the leading formula 0.0364.
- Light: the transverse pull over c^2 g is 0.99980 at gamma = 0 and 1.99982 at gamma = 1. A hop-angle reading with eps proportional to N/L multiplies the pull by eps cot eps (0.96981 against 0.96982 predicted); the cone reading has no such factor.
- Climbing a lapse step a photon keeps its quasi-energy with transmission 1.000000, wavenumber 0.36145 against 0.36146 and exit speed 0.18560 against 0.18561. Frequency over the local clock rate falls by N_low/N_high.
- Sea response: the massless sea's response to the cone ratio is -9.55 c0 (eps to 0) to -16.0 c0 (eps to pi/2) per block per tick, traceless. A zero at pi/2 exists only for the hop-angle reading (-0.0025 c0), where light also decouples.
- With a supplied tensor gradient coefficient of 0.00483 c0 per Dirac copy and a Regge coefficient of 0.5 c0 at the site rung, the ratio of sea to Regge term is 0.23, 0.93 and 3.71 at rungs 0, 1 and 2, against 0.002 needed for Hulse-Taylor. G grows as the rung cell area while the sea lives on sites, so no rung lets the bare term dominate. The mismatch remains.
- Edges growing at fixed tau: the photon keeps its band (0.9999999) and its quasi-energy falls as 1/L (ratio 0.4999987 at |K| = 0.05, 0.49994 at 0.37), while the atom's rest phase stays 0.1000. So photons redshift against atoms by L_obs/L_emit, for any lapse schedule by the conformal invariance.
- Splits: a 2^3 split at fixed tau resets eps and moves about 0.06 eps^2 of every light mode to the other band (0.061 at eps = 0.3, 0.055 at 0.1). A 2^4 split that also halves the ticks keeps eps, moves only about 0.043 K^2, and halves photon and atom phases together. A fixed-step reading halves the photon alone (0.5010).
- The matter phase per tick is -E tau to O(eps^2), with deviation 9.9e-5 at eps = 0.087.

## Against measurement (estimates)

- Clocks at rest: the Pound-Rebka shift gh/c^2 = 2.455e-15 follows exactly, measured at 0.9990 +- 0.0076 of that value.
- Deflection at the solar limb is (1 + gamma)/2 x 1.751 arcsec, and the cone reading adds nothing. The hop-angle reading gives gamma_light - 1 = -2 eps^2/3, so Cassini would need eps < 0.0061.
- The lattice violation of universality is about mu^2/(4 sin^2 eps) per species, independent of eps: 1.5e-44 for the electron, 1.7e-33 for the top quark and 5.6e-38 for 1 GeV of binding, against the MICROSCOPE bound of about 3e-15.
- Missing shift: the reading predicts no frame dragging, against the Gravity Probe B value of -37.2 +- 7.2 mas/yr. Dropping g_0i formally gives alpha1 = -8 and alpha2 = -1, against bounds near 1e-4 and 1.6e-9. The reading is therefore incomplete for moving sources.

## Boundary

Supplied: the reflection family and the box reduction to three axis lengths plus one duration, the identification of proper length and duration with the response law's edges, eps0, gamma = 1 from the response law, the field profiles, packets and their extrapolation, the sea branch, the cited tensor and Regge coefficients, the split maps, a = sqrt(8 pi) l_P and all measured numbers. A vacuum-reference clause that would remove the sea's tensor/Newtonian mismatch is a candidate only and is not tested here. Not established: the reading as an adopted law, shift and shear, the link plaquette reading, the vacuum clause, and the many-body effect of split flips.
