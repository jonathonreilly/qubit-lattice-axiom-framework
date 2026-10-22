---
claim_id: coefficient_one_hinge_sum_sets_the_hinge_area_unit_to_the_reduced_planck_length_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the response law's total phase, which carries minus the sum over hinges of area times deficit with coefficient one: the piecewise-flat curvature identity int sqrt(g) R = 2 sum_h A_h delta_h (checked in two dimensions on 20 random convex polyhedra, vertex deficits summing to 4 pi to 1.2e-14; the four-dimensional codimension-2 form cited from an earlier computation, not recomputed) makes coefficient one equivalent to u^2 = 8 pi G hbar/c^3 for the length unit u in which hinge areas are counted, u = sqrt(8 pi) l_P = 5.013 l_P (symbolic). Areas scale as b^2 and deficits are scale-free, so block edges of b_e cells have stiffness Lambda_b = b_e^2 Lambda_cell with the same G (area ratio 49.000000 and dihedral change 1.7e-15 at b = 7); the fixed-step lapse clause is unit-free, so the update law does not fix u. With the unit the register text names, the flat cell rung, L = sqrt(8 pi) l_P = 8.10e-35 m, hbar c/L = 2.435e18 GeV and a cell's edge stiffness L^2/(8 pi G hbar) = 1; the alternative reading u = site spacing gives L twice as long and stiffness 4. A table lists the register numbers that move between the two readings, each against its measured bound; none of the listed bounds changes verdict. Supplied model, finite diagnostic: the radian convention, the cited 4D hinge coefficient, and the supplied inputs of the estimates; the census of earlier runners' conventions is hand-entered."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/coefficient_one_hinge_sum_sets_the_hinge_area_unit_to_the_reduced_planck_length_2026_10_22.py
---

# A coefficient-one hinge sum sets the hinge area unit to the reduced Planck length

Claim type: bounded_theorem.
Primary runner: `scripts/coefficient_one_hinge_sum_sets_the_hinge_area_unit_to_the_reduced_planck_length_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3 in the three-law numbering) puts into the total phase minus the sum over hinges of area times deficit, with coefficient one, with areas counted in fixed proper units. The second variation is then the linearised Einstein operator, so the coefficient fixes G in terms of that unit. This note asks which length that is, whether anything else in the rules fixes it, and which register numbers move by a factor of 2 between the two readings found in earlier work: u equal to the site spacing (reading A, cell = 2 sites) or u equal to the cell rung L (reading B). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. The coefficient of the hinge sum.

1. Hinge identity: on a piecewise-flat space int sqrt(g) R = 2 sum_h A_h delta_h. The runner checks it in two dimensions (Gauss-Bonnet, R = 2K): on 20 random convex polyhedra the vertex deficits sum to 4 pi = (1/2) int sqrt(g) R. The codimension-2 cone form in four dimensions, the same factor 1/2 per cell, is cited from an earlier computation on Kuhn and coned-D4 carriers and is not recomputed here.
2. Coefficient one in the total phase, -(1/u^2) sum A delta = S_EH/hbar = (1/(16 pi G hbar)) int sqrt(-g) R, holds iff u^2 = 8 pi G hbar/c^3: the hinge area unit u is the reduced Planck length sqrt(8 pi) l_P = 5.013 l_P, whatever lattice length u is.
3. Scaling: areas go as b^2 and dihedral angles (so deficits) are scale-free, so block edges of b_e cells have stiffness Lambda_b = b_e^2 Lambda_cell with the same G. G fixes u, not the block.
4. The fixed-step lapse clause is unit-free (N -> N/lambda, gamma^ii -> lambda^2 gamma^ii leaves sqrt3 N rms(sqrt(gamma^ii)) unchanged), so nothing in the update law fixes u. Only the response law's choice of unit does. The current register text names it: areas and 4-volumes are counted in the flat cell rung length, the flat length of one cell's axis edge. That is reading B. (The runner's label says the text never names the unit; that describes the register text before this naming.)

B. The two readings (l_P = 1.616255e-35 m, M_P = 1.220890e19 GeV).

5. Reading A (u = site spacing): site 5.013 l_P, rung L = 10.027 l_P (1.62e-34 m), Lambda_cell = L^2/(8 pi G hbar) = 4, hbar c/L = 1.218e18 GeV.
6. Reading B (u = cell rung L): site 2.507 l_P, rung L = 5.013 l_P (8.10e-35 m), Lambda_cell = 1, hbar c/L = 2.435e18 GeV, the reduced Planck mass.
7. The two readings differ by exactly 2 in L and 4 in Lambda_cell.

C. Earlier runners' conventions (a hand-entered census, stated, not computed from the runners).

8. Of the lengths read from 33 earlier runners, 16 use a cube of 2 sqrt(8 pi) l_P (reading A), 15 use sqrt(8 pi) l_P, called a site in some (cosmology, Lambda-split, dark matter) and a cell in others, and 2 use a coarse cell of 4 sqrt(8 pi) l_P. No single convention was in use.

## Derivation

Item 1 draws 20 random point clouds of 40 to 59 points near the unit sphere, takes their convex hulls, and sums the angle deficits 2 pi minus the face angles at each vertex. Item 2 solves the coefficient equation for u with sympy. Item 3 computes face areas and dihedral angles of a random tetrahedron and of its copy scaled by 7. Item 4 simplifies the lapse clause under the unit change with sympy. Sections B and C are arithmetic on the readings.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Deficit sum: max |sum delta - 4 pi| = 1.2e-14 over 20 polyhedra.
- u = 2 sqrt2 sqrt(pi) sqrt(G) sqrt(hbar) = sqrt(8 pi G hbar) (symbolic).
- Scaling by 7: area ratio 49.000000, dihedral change 1.7e-15.
- Lapse clause invariant under the unit change (symbolic).
- Lambda_cell = 4 (A) and 1 (B); hbar c/L under B equals 2.435e18 GeV to 1e-3.

## Estimates against measurement

Register numbers that move from reading A to reading B, each against its measured bound (supplied inputs: the one-cell spread 0.2 at Lambda = 4 scaling as Lambda^(-1/2), the 22-spread margin to the window floor, the J0740+6620 core redshift factor 0.45 and the causal maximum 0.24 against the floor 1/8, the copy-mass coefficient c6 = 0.0833 and 0.0208, the nucleon lifetime 5.3e42 yr at 2.435e18 GeV scaling as the fourth power of the cell scale, v = 246.21965 GeV, the volume-mode single-cell spread 0.1794 at Lambda = 4, a Hubble patch of 5.7e21 m at recombination, the split keep-up bound 0.22 per tick at eps0 = 0.0375, and the inflation scale at r < 0.036):

| quantity | reading A | reading B | measured bound | verdict |
|---|---|---|---|---|
| one-cell zero-point spread (of L) | 0.20 | 0.40 | | |
| minimum block b_e: weak field / J0740 core / causal maximum | 5.0 / 13.5 / 38.2 | 10.0 / 27.0 / 76.4 | graviton mass, binary pulsars | block size moves |
| register sites per cell (weak-field minimum, eps0 = 0.0075) | 39.0 (b_e 6) | 7.1 (b_e 10); 0.91 (b_e 27) | | B is cheaper per cell |
| photon decay to e+e- threshold (PeV) | 78 / 110 | 110 / 156 | LHAASO 1.4 PeV | neither tested |
| v^2 over the cell scale (eV) | 4.98e-05 | 2.49e-05 | m3 about 0.05 eV | shortfall > 100 either way |
| nucleon lifetime at the cell scale (yr) | 3.3e+41 | 5.3e+42 | Super-K 2.4e34 | passed by > 1e7 either way |
| graviton cone \|c_g - 1\| at 100 Hz | 1.2e-80 | 2.9e-81 | GW170817 1e-15 | passed either way |
| free-fall spread (mu/eps)^2/4 | 2e-33 | 5e-34 | MICROSCOPE 3e-15 | passed either way |
| volume-mode single-cell spread; Hubble patch (independent / correlated) | 0.18; 9e-85 / 3e-56 | 0.36; 6e-85 / 1e-56 | CMB 1e-5 | passed either way |
| split keep-up H_max (1/t_P) | 1.01 | 2.03 | inflation scale | > 1e4 above either way |

The free-fall row is entered in the runner as supplied values (2e-33 and that divided by 4), not computed there. The register's earlier statement of about 10 to 16 cells per block is right only for weak fields under reading B.

## Boundary

Supplied: the radian (phase equals deficit in radians); the four-dimensional codimension-2 hinge coefficient, cited from an earlier computation; Planck-unit constants; the estimate inputs listed above; the hand-entered census of section C. Forced, given those: u^2 = 8 pi G hbar/c^3 from coefficient one; the b^2 scaling of block stiffness with the same G; the unit-freedom of the lapse clause; the values of both readings and the factor 2 in L and 4 in stiffness between them; the arithmetic of the table. Not claimed: a four-dimensional recomputation of the hinge identity here; an induced correction to long-distance G of order N_species/L^2, which would move L by an order-one factor; that the site spacing is a length of the geometry once sites are role-assigned; any prediction beyond the supplied inputs of the table.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the response law's hinge sum with coefficient one and its named unit (the flat cell rung); the update law's fixed-step lapse; the edge-block stiffness and the register numbers in the table. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/coefficient_one_hinge_sum_sets_the_hinge_area_unit_to_the_reduced_planck_length_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 60`, runs in about 0.1 s of compute (about 1 s with imports) with about 105 MB resident, prints about 4.3 kB and ends with `TOTAL: PASS=15 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output.
