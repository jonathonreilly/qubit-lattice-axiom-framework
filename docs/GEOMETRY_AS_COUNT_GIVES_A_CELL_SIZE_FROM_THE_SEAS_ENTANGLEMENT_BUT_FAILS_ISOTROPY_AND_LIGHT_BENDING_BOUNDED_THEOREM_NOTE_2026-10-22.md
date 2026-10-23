---
claim_id: geometry_as_count_gives_a_cell_size_from_the_seas_entanglement_but_fails_isotropy_and_light_bending_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Candidate rule tested (composite, least information): geometry is carried by counts, with each cut bond one area quantum a^2 for a universal a, so proper area = (number of cut bonds) x a^2. Exact: (i) with S = eta x N_bonds, Jacobson's argument gives G = a^2/(4 eta) (hbar = c = 1; no 8 pi enters this step), so a/l_P = 2 sqrt(eta), and the response law's hinge sum must then carry coefficient eta/(2 pi) in site units, not 1 (coefficient one needs eta = 2 pi on the site reading or pi/2 on the cell-rung reading); (ii) the Gaussian first law holds as an identity (dS = -5.055e-5 against d<K> = -4.958e-5 at d = 1e-4, remainder quadratic, ratio 100.0); (iii) on Z^3 the cut bonds per Euclidean area of a plane with normal n are |n|_1 (1, 1.4142, 1.7321 for (100), (110), (111)) and graph distance is the L1 distance, while the sea's cone is isotropic (speed 2.000000 along all three), so count lengths and areas differ from what matter measures by up to sqrt 3; count volume agrees; (iv) a split cascade whose blocks tick at their own light crossing makes the count geometry conformally flat, g = Omega^2 eta: PPN gamma = -1 (no light bending, no Shapiro delay) and vacuum R_ab = 0 admits no 1/r exterior field (R_xy = 6Mxy/r^5 for psi = -M/r); (v) count curvature comes in O(1) quanta: a 2D quadtree's refined patch carries deficits -0.2 pi, -0.1 pi, +0.4 pi at 28 vertices summing to 0, and equilateral 3- and 4-simplices tile no flat space (2 pi/arccos(1/3) = 5.1043, 2 pi/arccos(1/4) = 4.7668). Finite diagnostics: eta_100 = 0.19664 per cut bond for the one-mode pi-flux sea (0.04916 per Weyl), 0.02426 for a lattice scalar; slab entropy per cut bond is 0.1958, 0.1528, 0.1324 for (100), (110), (111) on 16^3 (per Euclidean area 0.1958, 0.2161, 0.2292), so S ~ A_E |n|_1^p with p = 0.285-0.287 (count: 1, Euclidean: 0), and a count-Jacobson G would vary by a factor of 1.48 with horizon orientation; the boost-local modular form holds to 0.9994 at transverse mass 0.1 and 0.835 at 2, and modes with M < 0.3 carry 2.3% of eta. Estimates: a = 0.887 l_P from the one-mode sea, 0.990 l_P with a two-scalar photon, 2.4-3.5 l_P if every Standard Model or Spin(10) field is counted as its own lattice sea, against the unit map's 2.507 l_P (cell rung) or 5.013 l_P (site). Gate: no fitted number and no named structure, but two predictions it was not built for fail measurement (gamma = -1 against Cassini; an O(1) direction dependence of G); FAILS as stated. Supplied model, finite diagnostic: static pi-flux sea as the tick's eps0 -> 0 limit, lattice scalars for gauge polarisations, planar cuts on antiperiodic tori, the tied block tick, the content rows."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/geometry_as_count_gives_a_cell_size_from_the_seas_entanglement_but_fails_isotropy_and_light_bending_2026_10_22.py
---

# Geometry as count gives a cell size from the sea's entanglement, but fails isotropy and light bending

Claim type: bounded_theorem.
Primary runner: `scripts/geometry_as_count_gives_a_cell_size_from_the_seas_entanglement_but_fails_isotropy_and_light_bending_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Two companion computations (open PRs #10011 and #10020) found that any cube tick reading only its own cube's ratios is blind to the 4D Weyl factor. Its vacuum entropy is therefore eta times the number of cut bonds, not eta times proper area, and Jacobson's G = a^2/(4 eta) varies as a^2 across the edge window. This note tests the least-information reading of that result. Geometry is carried by counts and not by edge-length registers: every bond is one fixed area quantum a^2 with a universal a, as in a causal set's "number = volume". Jacobson's argument would then fix the cell size in Planck units from the sea alone. The note computes that number, checks Jacobson's other premises, and tests whether site counts can carry the curvature Einstein's equations need. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Candidate rule

> "Counts are geometry. Every site-tick is one 4-volume quantum and every cut bond one area quantum a^2, with a the same everywhere. Lengths, areas and volumes are counts times powers of a. Edges carry no length register."

It bends the Lattice axiom, because curvature must live in connectivity (defects or splits). It also removes the edge-register clause of the update law.

## Statement

A. Exact.

1. Count Jacobson. Jacobson's argument uses δQ = T dS, with T = κ/2π and S = η_A A. It gives Einstein's equations with G = 1/(4 η_A); the 8π of 8πG appears only through the Raychaudhuri step, not in the coefficient. Count geometry sets η_A = η/a^2, so G = a^2/(4η) and a = 2 sqrt(η) l_P. The Weyl blindness found by the companion notes is then consistent rather than a defect. No conformal register exists to be blind to, G is the same everywhere in lattice units, and the a^2 variation of G_J disappears with the window. The response law's hinge sum must reproduce the same G, so its coefficient in site units becomes a^2/(8πG) = η/(2π). Coefficient one needs η = 2π on the site reading of the unit map, or π/2 on the cell-rung reading.
2. First law. dS = Tr[K dC] for every Gaussian change, and the remainder is the relative entropy, which is nonnegative and second order. It holds identically and constrains nothing. Jacobson's content lies entirely in the area coefficient and its universality.
3. Count lengths are not matter lengths on Z^3. A plane with unit normal n is crossed by |n|_1 = |n_x| + |n_y| + |n_z| bonds per unit Euclidean area. The graph distance is the L1 distance: the shortest path to (L, L, L) has 3L bonds against √3 L. The sea's light cone is isotropic, E = 2|q| along every direction. Count area and count length therefore disagree with the area and length that every species' propagation measures, by factors of up to √3 at all scales. This is an O(1) effect, not one suppressed by the Planck length. Count volume agrees, since sites per Euclidean volume are uniform.
4. Splits give only a conformal factor. A refined block is locally the same Z^3 with the same tick, and it ticks at the same fraction of its own light crossing. In count units a split is therefore a 4D conformal step, and the coarse-grained count geometry is g = Ω^2 η. Then g_00 = -(1 - 2M/r) forces g_ij = (1 - 2M/r) δ_ij, so PPN γ = -1, with no light deflection and no Shapiro delay. Linearised, R_ab = -2 ∂_a∂_b ψ - η_ab □ψ, and the vacuum condition R_ab = 0 forces ψ to be linear: there is no 1/r field outside a source (R_xy = 6Mxy/r^5 ≠ 0 for ψ = -M/r). This is Nordström's scalar gravity. A Weyl-flat metric cannot be Schwarzschild's exterior.
5. Count curvature comes in O(1) quanta. With regular unit-edge faces, a 2D quadtree with one refined 2x2 patch carries vertex deficits of -0.2π, -0.1π and +0.4π at 28 vertices, summing exactly to 0; it is a conformal bump. A count geometry built from equilateral simplices is never exactly flat: 2π/arccos(1/3) = 5.1043 and 2π/arccos(1/4) = 4.7668, with edge deficits +0.128 (n = 5) and -1.103 (n = 6) rad. Cubes are flat only with four cubes at every edge, and their deficit quanta are ±π/2. In 3D, a cube with hanging nodes has no shape fixed by counts. Count geometry therefore needs simplices, or shape data that is a register again. Weak fields (curvature ~ 1e-6 of a cell's inverse area at solar-system strength, far less in practice) need dilute, almost-cancelling O(1) quanta. That means disorder (as causal sets need), or a defect density that bends the Lattice axiom.

B. Finite diagnostics (supplied model).

6. Area coefficients from transverse-momentum chain decomposition ((100) cut, chains of 600 sites, a 400^2 grid, c = 1 tails of slope -0.1668 and -0.1662). The one-mode pi-flux sea gives η_100 = 0.19664 per cut bond; it is 2 Dirac = 4 Weyl, so 0.04916 per Weyl. A lattice scalar gives 0.02426.
7. Orientation dependence. Slab entropies on antiperiodic tori:

| cut | per cut bond, 12^3 | 16^3 | per Euclidean area, 16^3 |
|---|---|---|---|
| (100) | 0.19510 | 0.19578 | 0.19578 |
| (110) | 0.15213 | 0.15280 | 0.21609 |
| (111) | 0.13167 | 0.13235 | 0.22924 |

   The drift from 12^3 to 16^3 is at most 0.5%. The (100) slabs of width 4 and 5 lie within 0.8% of the infinite value. The (111) entry matches the lattice-ball value of 0.229 per geometric area in #10011. Fitting S ≈ η_100 A_E |n|_1^p gives p = 0.285 and 0.287 from the two diagonal cuts. A pure count law would have p = 1 and a Euclidean area law p = 0, so the vacuum is closer to Euclidean area than to bond count. A count-Jacobson G would vary with horizon orientation by a factor of 1.48. The Euclidean reading still varies by 17%: any Jacobson reading of this sea on the cubic lattice inherits a cubic anisotropy.
8. Bisognano-Wichmann. Per transverse mode, the lattice modular bond term at distance one is (2π/v) x the local energy to 0.9994 at M = 0.1, and to 0.8346 at M = 2. Modes with M < 0.3 carry 2.3% of η. The area coefficient is a cell-scale quantity, where the modular Hamiltonian is not a local boost.

## Estimates against measurement

a/l_P = 2 sqrt(η) (no fitting; the measured G sets only the unit):

| content (supplied) | η per bond | a/l_P | G_count/G_hinge (site) |
|---|---|---|---|
| one-mode sea (axiom content) | 0.1966 | 0.887 | 31.95 |
| sea + photon (two scalars) | 0.2452 | 0.990 | 25.63 |
| 1 family (16 Weyl) + 12 gauge + 4 Higgs, each its own sea | 1.4659 | 2.421 | 4.29 |
| 3 families + 12 gauge + 4 Higgs, each its own sea | 3.0391 | 3.487 | 2.07 |
| 1 family + Spin(10) 45 gauge, each its own sea | 2.9701 | 3.447 | 2.12 |

- The unit map names the site as 2.507 l_P (cell-rung reading, η = π/2) or 5.013 l_P (site reading, η = 2π).
- Composite before atomic. With one qubit per site, species are patterns of the same sites, so η per fine bond is the one-mode sea's (plus any link entanglement), and a = 0.887 l_P. The "each its own sea" rows violate the one-qubit axiom and are upper readings. The fact that the one-family row lies 7% from π/2 is a coincidence of that reading, not a derivation: it ignores vector contact terms, and η is non-universal (items 7 and 8).
- Sakharov comparison, same content: entanglement gives 0.0983 per Dirac, against the induced 4π c_G = 0.0624 (staggered) or 0.1297 (Wilson) from the induced-couplings computation. The two routes to G disagree at O(1) on the lattice.
- γ = -1 (item 4) is excluded by Cassini, γ - 1 = (2.1 ± 2.3)e-5, at about 9e4 σ. A 17-48% direction dependence of G (item 7) is excluded by planetary and lunar orbits (not recomputed here).

## Gate (anti-smuggling)

1. Measured number chosen: none. η is computed, and the measured G sets only the unit. Passes.
2. Observed structure inserted: none. The rule speaks only of sites, bonds and ticks. Passes.
3. Predictions it was not built for: γ = -1 for the tied-tick split cascade, FALSIFIED. The orientation dependence of the count G (1.48), FALSIFIED. The value a = 0.887 l_P, UNTESTED (not directly measurable).
4. Axiom bent: Lattice (geometry in connectivity: splits, defects or disorder). CL-1's edge-register clause is removed.

Verdict: the rule FAILS as stated on Z^3 with octree splits. What survives:
- Volume = number is consistent with matter (item 3).
- The count reading turns the Weyl blindness into a universal G in lattice units.
- a/l_P = 2 sqrt(η) is a derived relation, conditional on a count measure that is isotropic and matches matter's cone.

## Consequences and costs

- G becomes a prediction of fine content. Under composite before atomic it is fixed by the one-mode sea and the links, not by the species count.
- Equivalence principle. All species hop on the same graph, so free fall and the cone are universal (already CL-1). But on the regular lattice, the area measure gravity responds to (count) is not the metric light measures (Euclidean), so gravity and light disagree at O(1).
- Removed:
  - the edge registers;
  - the window [L/8, 2^(1+Δ) L];
  - κ and Δ (AX-4, FITTED), which would be one fewer fitted rule;
  - the lapse clause and the per-cube normalisation, which become identities.
- Lost with the edges:
  - TT gravitational waves;
  - the shift law and the constraints as edge-register laws;
  - the edge-register gravity-mediated-entanglement prediction, which would need superposed graphs;
  - with tied splits, everything except the conformal mode (item 4).

## Proposed repairs (UNTESTED)

- R-a, untied tick. A site may skip updates, so the lapse is a count of skipped ticks, independent of refinement. This gives static diagonal metrics (N, Ω), with γ set by the dynamics. It does not cure item 3 or 7 and gives no TT modes.
- R-b, random connectivity (Poisson sprinkling or Delaunay graphs). This restores isotropy statistically and is the causal-set route to Lorentz-compatible number = volume. It bends the Lattice axiom fully. Next test: η per bond on random 3D graphs, its isotropy, and whether count area matches the cone metric there.
- R-c, hybrid. Volume = count (which passes), with area read in the cone's Euclidean metric. It still meets the sea's 17% cubic anisotropy, which a rule would have to cancel.

## Boundary

Not claimed:
- the Floquet tick at finite eps0 (corrections ~eps0^2, 4.3e-4 at eps0 = 0.0375 per #10011);
- link, rishon or edge-register entanglement, and vector contact terms;
- cuts other than planar slabs;
- any dynamics of counts (Pachner-type moves);
- a continuum limit of count gravity.

Literature context (cited, not recomputed):
- Jacobson 1995 (equation of state).
- Dynamical and causal dynamical triangulations, which are geometry = count with equal edges. Their bare G is tuned to a critical coupling and is not predicted by content.
- Bombelli-Henson-Sorkin: Lorentz-compatible discreteness needs randomness.
- Kröner's defect theory: incompatibility = Einstein tensor of the defect metric, a possible carrier of smooth curvature in a lattice.

Earlier main notes:
- AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25 (Fermi-surface carrier) is neither used nor contradicted.
- The heat-kernel note UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17 (a supplied proper cutoff) is not contradicted.
- The finite-range scalar Cassini note on main (EXPONENTIAL_SCALAR_ORBIT_LIGHT_TIME_BOUNDED_THEOREM_NOTE_2026-10-14) treats a different, supplied scalar channel and is not used.

Companion results:
- Used and narrowed: #10011 and #10020 (Weyl blindness, η_100, Bisognano-Wichmann).
- Used: the unit map (cell rung √(8π) l_P) and the induced-couplings c_G.
- Related: #9876 (volume = number of records).

## Supplied vs forced

Supplied:
- the static pi-flux sea as the tick's eps0 -> 0 limit;
- lattice scalars for gauge polarisations and the Higgs;
- planar slab cuts on 12^3 and 16^3 antiperiodic tori;
- the tied block tick from the split clause;
- the content rows;
- the unit-map readings A and B.

Forced, given those: items 1-8 and the tables.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick and split clause, the response law's hinge sum and unit map, and the edge window. Zero premise weight; results that use it are conditional on it.

## How to run

```
python3 scripts/geometry_as_count_gives_a_cell_size_from_the_seas_entanglement_but_fails_isotropy_and_light_bending_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 6-8 s with about 245 MB peak resident, prints about 3 kB and ends with `TOTAL: PASS=9 FAIL=0`. Its random draws are seeded (20261022).
