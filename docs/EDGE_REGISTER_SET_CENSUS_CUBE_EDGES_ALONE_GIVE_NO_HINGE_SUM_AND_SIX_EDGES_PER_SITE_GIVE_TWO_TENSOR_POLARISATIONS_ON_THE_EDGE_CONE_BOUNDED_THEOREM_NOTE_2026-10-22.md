---
claim_id: edge_register_set_census_cube_edges_alone_give_no_hinge_sum_and_six_edges_per_site_give_two_tensor_polarisations_on_the_edge_cone_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the linearised Euclidean Regge hinge sum around flat cells, with the update law's fixed lapse and zero shift (tick edges fixed, mixed edges slaved to the mean of their spatial ends): (cube edges) the edges of the update law's two cube tilings are exactly the 3 axis edges per site, each in one cube, with no triangle among them; at every momentum with all components nonzero their lengths are a flat vertex displacement, so with the other lengths slaved by stationarity they carry no stiffness, with the other lengths frozen they are three non-metric strains gapped at the cell scale, and with the diagonals frozen inside the slab their light branches are direction-dependent and off the edge cone; (Kuhn slice) with the 7 spatial Kuhn edges per site as registers there are 2 light branches on the edge cone at order k^2 with lattice corrections of order (ka)^2, plus 4 zero-frequency branches and one breathing strain; (six edges per site) with 3 axis edges plus the face diagonals joining even-sum sites (five tetrahedra per cube, alternating), 6 registers per site match the metric count, and exactly 4 light roots (the two tensor polarisations) lie on the edge cone within 6e-5 along the axis, body-diagonal and one generic direction at |k| = 0.02. The full 4D Freudenthal and 3D Kuhn controls reproduce the existing second-variation values. Supplied model, finite diagnostic: linear order, Euclidean continuation, a supplied slaving map, finite momenta; no register dynamics, no interaction, no continuum limit."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/edge_register_set_census_cube_edges_alone_give_no_hinge_sum_and_six_edges_per_site_give_two_tensor_polarisations_on_the_edge_cone_2026_10_22.py
---

# Edge-register set census: cube edges alone give no hinge sum, and six edges per site give two tensor polarisations on the edge cone

Claim type: bounded_theorem.
Primary runner: `scripts/edge_register_set_census_cube_edges_alone_give_no_hinge_sum_and_six_edges_per_site_give_two_tensor_polarisations_on_the_edge_cone_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) tiles the sites of Z^3 in two ways by 2x2x2 cubes and reads each cube's tick from its edges, with a lapse fixed by the edges (not varied) and no shift; its response law (CL-3) is a stationary phase that includes the Regge hinge sum. This note asks which set of edges, taken as registers, carries the hinge sum's spin-2 content: the tilings' cube edges alone, the 7 Kuhn edges per site, or the six-edge set (axis edges plus the even-sum face diagonals) on which the register's update law now places its edge registers. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the choices compared here.

## Statement

All statements are for the second variation of the Euclidean Regge action S_R = sum_t A_t delta_t around flat cells, written as a Bloch stiffness Q(k) in edge lengths; Lorentzian roots are read from the low-k transfer form with k_t -> i omega.

A. Cube edges alone.

1. The edges of the two cube tilings (offset by (1,1,1)) are exactly the axis edges of Z^3, 3 per site, each in exactly one cube; every site is a corner of one cube of each tiling, and cubes of different tilings share only corners. No face or body diagonal is a cube edge, so the set contains no triangle.
2. At every momentum with all three components nonzero, the map from vertex displacements to axis lengths has rank 3: every axis-length field there is a flat vertex displacement. A single cube with its 12 edges keeps 6 floppy shears.
3. Inside the 4D hinge sum with fixed lapse and zero shift: with all other lengths frozen, the three axis lengths are non-metric strains gapped at the cell scale (k = 0 eigenvalues -14, -2, -2); with the other lengths slaved by stationarity, the effective stiffness vanishes (consistent with item 2), so there is no graviton and no response; with the diagonals frozen inside the sync slab, the light roots have direction-dependent speeds, none equal to 1, and a wavevector along an axis keeps one branch only.

B. Controls on the full complexes (every edge a register).

4. The 3D Kuhn complex (7 edge classes) has 6 metric zero modes and one massive breathing mode at k = 0, with eigenvalue -24 in the raw S_R orientation, and 3 vertex-displacement zeros at generic k. The 4D Freudenthal complex (15 edge classes, 24 path simplices per 4-cell) has 11 zeros at k = 0 and massive eigenvalues -48, -16, -16, -16. These reproduce the values in the existing notes `CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09` and `CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09`.
5. On the 4D complex at generic k there are 5 exact zeros: 4 displacements and one flat branch that is not in the span of metric and gauge directions. At small k, 6 eigenvalues scale as k^2 and 4 are gapped at the cell scale.

C. Spatial Kuhn edges as registers, fixed lapse, zero shift.

6. The 7 registers per site give 2 light branches (4 roots +-E), 8 zero-frequency roots and one breathing strain that is either non-dynamical or massive at the cell scale. The light branches lie on the edge cone at order k^2: c_g = 1 - alpha (ka)^2, with alpha depending on direction and polarisation.
7. With the tick edge 0.7 a, the light branches stay on the edges' null cone, E = tau |k|.

D. Six edges per site.

8. Taking the 3 axis edges plus the face diagonals joining even-sum sites (five tetrahedra per cube, alternating between neighbouring cubes) gives 48 registers per 8-site cell, 6 per site, equal to the number of metric components. An independent slab code built from the spatial triangulation finds exactly 4 light roots, the two tensor polarisations, on the edge cone along each tested direction.

## Derivation

Item 1. Each cube owns the 12 axis edges between its corners. A cube of the even tiling spans coordinates {2m, 2m+1} along each axis, so it owns the axis edges whose lower end has an even coordinate along that axis; the odd tiling's cubes own those whose lower end is odd. Each axis edge therefore lies in exactly one cube of exactly one tiling, and there are 3 per site. Diagonals join corners of a cube but are not cube edges, and three axis edges cannot close a triangle.

Item 2. In Fourier space the axis length along direction i changes by (e^{i k_i} - 1) u_i(k), a diagonal 3x3 map that is invertible when every k_i is nonzero. A cube has 8 x 3 = 24 vertex coordinates, 6 rigid motions and 12 edges of rank 12, leaving 24 - 6 - 12 = 6 floppy modes.

Item 3. Slaving the other lengths by stationarity is the Schur complement of Q on the axis block. Since every axis field completes to a vertex displacement (item 2), and displacements carry zero action, the Schur complement vanishes. Freezing the other lengths instead keeps the axis block of Q, which has no zero mode at k = 0.

Items 4 to 8. Q(k) is assembled from the Schlaefli gradients of each simplex (finite-difference Hessians, Richardson-extrapolated) and the analytic Hessian of each hinge area. The sync slab replaces the tick edge by a fixed length tau and each mixed edge by the mean of its two spatial ends times the length ratio; the roots are those of det Q(k_s, z) = 0 with z = e^{-E}, from the Fourier coefficients of Q in k_t. Light roots are those with 0.5 < |E|/|k| < 2 and small imaginary part. The six-edge set has the metric count per site, so by counting no non-metric strain remains; this count is stated, not separately computed.

## Checks

The runner ends with `TOTAL: PASS=15 FAIL=0` in about 2 s.

Exact checks and identities (checked numerically):
- Cube edges on a 4^3 torus: 192 cube edges = 3 per site, each in exactly one cube; 64 sites in each tiling. That no diagonal is a cube edge and that the set has no triangle are stated, not separately tested.
- Rank of the axis-length map: minimum 3 over 200 random momenta; one cube keeps 6 floppy shears.
- 3D Kuhn control: 6 zeros and breathing eigenvalue -24 at k = 0; |Q G| = 1.4e-11 on vertex displacements at a random k.
- 4D Freudenthal control: 11 zeros and massive eigenvalues -48, -16, -16, -16 at k = 0. At a random k: 5 exact zeros, displacement residual |QG|/|Q| = 9e-12, and the remaining flat branch at distance 0.86 from the metric-plus-gauge span with weight 0.30 on spatial edges.
- Small-k census on the 4D complex: 5 zero, 6 scaling as k^2 (ratio over k-halving 4.000), 4 gapped at 16.0 or more. The split of the 6 into 2 tensor and 4 lapse, shift and trace channels is a reading, not computed.
- Axis registers with other lengths slaved: |Q_eff|/|Q_axis| = 3e-11 at four random momenta.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Axis registers, other lengths frozen: k = 0 eigenvalues -14, -2, -2.
- Axis registers, diagonals frozen, sync slab at |k| = 0.02: light-root speeds 0.0 and 0.816 (axis), 0.577 and 0.943 (face diagonal), 0.943 (body diagonal), 0.754 and 0.997 (direction (0.3, 0.5, 0.8)); closest distance to 1 is 3.0e-03.
- Spatial Kuhn registers, sync slab, |k| = 0.04 and 0.02 along axis, face and body diagonals: 4 light roots and 8 zero-frequency roots in every case, the other finite roots at |Re E| >= 18.4 per tick, 5 infinite roots, Fourier leak 3e-15. The attribution of the 8 zero roots to 3 residual spatial displacements and the fixed-lapse scalar is a reading.
- Light-branch deviation 1 - E/|k| at |k| = 0.04: axis 2.332e-4 (x2), 1.333e-4 (x2); face 1.749e-4 (x2), 1.0e-4 (x2); body 1.0e-4 (x4). As alpha in c_g = 1 - alpha (ka)^2: axis 0.146, 0.146, 0.083, 0.083; face 0.109, 0.109, 0.062, 0.062; body 0.062 (x4). Ratio of deviations over k-halving 3.99 to 4.01 (printed, not asserted); the check asserts deviations below 2e-3.
- Tick edge 0.7 a (k along an axis, |k| = 0.02): E/(tau |k|) = 0.99995, 0.99995, 0.999975, 0.999975; |QG|/|Q| = 6e-12; 8 zero roots.
- Independent slab code on the Kuhn slice: light E/|k| = 0.999767, 0.999767, 0.999867, 0.999867 and 8 zero roots, matching the spatial Kuhn result.
- Six-edge set: 48 registers per 8-site cell; 27 zeros at k = 0 (read as 6 uniform metric plus 21 staggered displacements; the split is not computed). At |k| = 0.02 along the axis, the body diagonal and (0.3, 0.5, 0.8): 4 light roots in each case, maximum |E/k - 1| = 6e-05, 3e-05, 4e-05; zero-frequency roots 48, 50, 48; unresolved near-zero roots 0, 0, 2 (largest |E| 0.002); lightest massive |E| 1.49, 1.20, 0.69.

## Boundary

Supplied: the Freudenthal and Kuhn carriers and the five-tetrahedron triangulation compared; the Euclidean continuation and the low-k transfer form; the sync-slab reading of the fixed lapse and zero shift, including the slaving of mixed edges to the mean of their spatial ends; the tick lengths 1 and 0.7 a; the finite-difference steps, the Fourier truncation and the sampled momenta. Forced, given those: that the cube edges are the axis edges with no triangle; their rigidity and the vanishing of their slaved stiffness; the control spectra; two light branches on the edge cone at order k^2 for the Kuhn and six-edge register sets; the metric count of the six-edge set. Not claimed: that the six-edge set is the only register set with this census (the register's update law now places edge registers on exactly this set; this note supplies the census behind that choice, not uniqueness); a full census of the six-edge set at every momentum (three directions at one |k| are tested, and two near-zero roots along the generic direction are unresolved); any statement beyond linear order; any interacting or truncated register dynamics; the sign or normalisation of the Lorentzian action; any continuum limit.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the two cube tilings, the edge registers and the fixed lapse and zero shift of the update law, and the hinge sum in the response law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/edge_register_set_census_cube_edges_alone_give_no_hinge_sum_and_six_edges_per_site_give_two_tensor_polarisations_on_the_edge_cone_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 2 s with about 70 MB resident, prints about 4.0 kB and ends with `TOTAL: PASS=15 FAIL=0`. Its random momenta are seeded; two repeated runs gave identical output apart from the elapsed-time line.
