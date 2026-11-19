---
claim_id: site_read_links_in_the_full_metric_bend_light_by_two_on_every_ray_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "With a supplied site reading of the link plaquettes in the lapse, shift and full spatial metric of each site's two cubes, the link action equals the 3+1 split of covariant Maxwell, keeps gauge invariance and the Gauss law, and has the edges' null cone at every order in the field, while one-to-one Yee pairing cannot read shear; in supplied weak static fields lattice packets give 1 + gamma = 2 on every ray tested, Shapiro coefficient 1 and the GR frame-dragging delay; the sea's response to cell anisotropy is not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/site_read_links_in_the_full_metric_bend_light_by_two_on_every_ray_2026_10_21.py
---

# Site-read links in the full metric bend light by two on every ray

Claim type: bounded_theorem.
Primary runner: `scripts/site_read_links_in_the_full_metric_bend_light_by_two_on_every_ray_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law reads the links' plaquette phase in proper area, which is defined for diagonal cells, and it lists photon bending as not yet checked. This note extends the reading to a full metric with lapse, shift and shear. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the reading nor the metrics used.

## Statement

Links sit on the bonds between even-cube centres, and their spatial plaquettes are the faces crossed by odd-centre bonds. Each site joins one even cube to one odd cube; it counts the three bonds of its odd cube's centre cell that meet at its even centre and the three faces of that cell that contain it. Per tick and per site, reading the metric of its two cubes,

L_s = (1/8)[ (1/2) Et.(sqrt(gamma)/N) gamma^ij Et - (1/2) B.(N/sqrt(gamma)) gamma_ij B ],   Et_i = F_0i - beta^k F_ki,

with B at mid-tick. Then:

1. -1/4 sqrt(-g) F.F equals this split identically.
2. Static pure gauge solves the field equation and the Gauss charge is conserved for any lapse, shift and shear.
3. Both polarisations obey (w + beta.K)^2 = N^2 gamma^ij K_i K_j up to lattice O(K^2), at every order in the field and without calibration.
4. In a diagonal cell the link band equals the register's fermion band at every K.
5. Pairing each link only with its own dual face (one-to-one Yee) makes the band even in each K_i, so the plain placement cannot read shear.

In supplied weak static fields, lattice photon packets give 1 + gamma = 2 on every ray tested, a Shapiro coefficient of 1 and the GR frame-dragging delay.

## Derivation

The identity is the 3+1 decomposition of the covariant Maxwell action: the shift enters only through the electric plaquette taken along the slice normal, and the inverse metric and shear enter through the two site weights. The action uses links only through B = curl A and Et, so it is gauge invariant and the Gauss charge div D is conserved by every tick. For a diagonal cell with gamma^ii = f_i^2 the link band (2 sin w/2)^2 = N^2 tau^2 sum f_i^2 (2 sin K_i/2)^2 coincides with the fermion band sin^2(w/2) = sin^2(eps) sum f_i^2 sin^2(K_i/2)/sum f_i^2 at every K, because the tick law sets sin eps = sqrt3 N tau rms(f). With one-to-one pairing every weight is diagonal, so the cone has no K_i K_j term.

The minimal change that reads shear lets each site pair the three links that meet at its even centre, so shear couples links sharing a centre, with a range of one cell. The carriers and gauge group are unchanged, the weights are positive for any positive gamma (a sum of positive forms), and without shear the placement is exactly Yee.

## Checks

The runner ends with `TOTAL: PASS=13 FAIL=0`. Among its lines:

- `[PASS] A1 theorem (3+1 identity, exact rationals): -1/4 sqrt(-g) F.F = 1/2 (sqrt(gamma)/N) gamma^ij Et_i Et_j - 1/2 (N/sqrt(gamma)) gamma_ij B^i B^j, Et_i = F_0i - beta^k F_ki`: the symbolic difference is 0.
- `[PASS] A2 theorem: ... static pure gauge solves the field equation and the Gauss charge div D is conserved by every tick, for any lapse, shift and shear`: |M(0).grad| = 2e-15 and the Gauss drift over 200 ticks is 3e-12.
- `[PASS] A3 theorem (continuum limit = covariant Maxwell): for strong lapse, shift (0.1 c) and shear (0.15) both polarisations obey (w + beta.K)^2 = N^2 gamma^ij K_i K_j up to the lattice O(K^2); no birefringence at leading order`: deviation 6e-8 at |K| = 1e-3, growing by 4.00 at 2e-3.
- `[PASS] A4 theorem: in a diagonal cell ... the link band ... is the [tick-law] band ... at EVERY K`, to 1e-15. With the copy mass the light fermion band shifts by a dimension-six term; at eps = 0.3, M = 0.5 the coefficient is -0.0833 on the axis, -0.0208 on a generic ray and 0 on the body diagonal, a pattern seen at that one point only.
- `[PASS] B1 theorem: pairing each link only with its own dual face (the one-to-one Yee Hodge) makes every weight diagonal ...: the plain placement cannot read shear`, to 2e-16.
- `[PASS] B2 minimal change`: same carriers and gauge group, positive weights, Yee when gamma is diagonal, and stable, with the radiating roots on |z| = 1 to 5e-13 at shear 0.15 and shift 0.15 c.
- `[PASS] B3 the shift drags both photon polarisations by exactly b at every order in b (0.15 c tested)`, error up to 7e-7.
- `[PASS] C1 lattice photon packets follow the eikonal of the lattice dispersion ... for lapse, gamma_ii, shear, shift and the radial-gauge gradient on rays`: ratios 1.0000 +- 1e-4.
- `[PASS] C2 shear pushes the (1,1) and (1,-1) packets oppositely; the one-to-one placement does not push (second order only); a curl-free shift b_z(z) pushes nothing`.
- `[PASS] D1 photon bending 1 + gamma = 2 on every ray, in the radial and the second trace-fixed gauge ...; no out-of-plane bending. One-to-one placement: 1 + sum k^4 (4/3 on the body diagonal)`. The site reading gives 2.000000 on the axis, face, face-xz, body and generic rays; one-to-one gives 2.0000, 1.5000, 1.5000, 1.3333 and 1.4850.
- `[PASS] D2 Shapiro delay (packet group delay along the ray): coefficient of -4 GM ln b is (1 + gamma)/2 = 1 on every ray`.
- `[PASS] D3 photon frame dragging: the Lense-Thirring shift ... delays the photon by -4 G J.(e x k)/b, the GR value`.
- `[PASS] D4 photon = fermion cone in every direction, at every order in the field`: at shear 0.15 they agree to 4e-7 once the fermion's hop weights and shear parts are set by the register's null-cone clause. Before that calibration the fermion is off by 8e-3, about 0.36 sigma^2, so the null-cone clause has to hold exactly, not only to first order.

Bending is computed from local response along rays and checked with packets in gradients; no full 1/r ray propagation was run.

## Estimates against measurement

Taking a cube as 2 sqrt(8 pi) Planck lengths: the copy-mass term gives about 1e-25 and the shear term about 3e-32 at 1.4 PeV, against the LHAASO bound 3e-19; the LEP check at 104.5 GeV gives about 6e-34 against 1e-11; the lattice correction to gamma at 8.4 GHz is about 8e-64, against the VLBI and Cassini bounds 1e-4 and 2.3e-5. An uncalibrated fermion shear error of about 0.36 sigma^2 would be about 4e-13 at galactic sigma ~ 1e-6, which LHAASO would exclude.

## Boundary

Supplied: the extension of proper area to the covariant Maxwell form; the site pairing (natural, but not shown unique); B at mid-tick; the site reading the mean of its two cubes; temporal gauge; the fermion tick code; the gauges, as stand-ins for the register's stationary edges; and the measured numbers. Not computed: the sea in anisotropic or sheared cells, the reading at the site-phase level, time-dependent fields and the compact nonlinearity. Open risk: under the fixed-4-volume clause no static gauge is both diagonal and trace-fixed, so cells are anisotropic at order U, and the register's scalar dressed clauses fix no tensor; this could leave light with a gamma - 1 set by an uncomputed shape coefficient. Holding each link's dressed cone to the edges' null cone in every cell would remove it; that is adopted to meet measurement, not derived.
