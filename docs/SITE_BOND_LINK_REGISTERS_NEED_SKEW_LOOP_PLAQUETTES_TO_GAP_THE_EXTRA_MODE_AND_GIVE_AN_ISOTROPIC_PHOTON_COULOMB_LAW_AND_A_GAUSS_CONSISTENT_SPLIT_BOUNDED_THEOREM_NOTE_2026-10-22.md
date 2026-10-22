---
claim_id: site_bond_link_registers_need_skew_loop_plaquettes_to_gap_the_extra_mode_and_give_an_isotropic_photon_coulomb_law_and_a_gauss_consistent_split_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's site-bond layout of link registers (one register per site, on the bond from the centre of its even-tiling cube to the centre of its odd-tiling cube): the register bonds are the nearest-neighbour bonds of the body-centred centre lattice, so the gauge-invariant values are 3 per centre, the two photon polarisations plus one extra; the earlier plaquettes (cubic squares on the even-centre lattice with each centre bond the mean of its four two-site register paths) leave 4 of the 6 values per 2^3 cell with zero stiffness at every momentum, and 2 when the odd tiling's squares are added; the 12 axis-diagonal skew register loops per cell zero only the photon pair at q -> 0, gap the extra over a 14^3 scan of the primitive zone (lowest eigenvalue 8 against 24 at q = 0), give a photon isotropic at order q^2 with degenerate polarisations and a dimension-six birefringence b (qa)^2 with b = 1/12 on face diagonals and 0 on axes and body diagonals, while planar rhombi alone leave a third massless mode; least electric energy under Gauss's law gives the Coulomb law with coefficient 1 within 2% on a 48^3 lattice; for the split, coarse totals with child-centre shares 1, 1/2, 1/4 (corner, edge midpoint, face centre) make every parent Gauss law the weighted sum of child Gauss laws exactly, the shares are fixed by covariance and the Gauss sum, no covariant integer assignment exists, an integer covariant skeleton passing exists, and the coarse map sends long-wavelength child photons onto the parent photon pair with leakage growing as q^2 (finite diagnostic). The large-S ring-exchange coupling (alpha = 0.071 at S = 3/2 on skew loops) is an estimate with supplied U and K. Quadratic spectra only; no register dynamics is computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/site_bond_link_registers_need_skew_loop_plaquettes_to_gap_the_extra_mode_and_give_an_isotropic_photon_coulomb_law_and_a_gauss_consistent_split_2026_10_22.py
---

# Site-bond link registers need skew-loop plaquettes to gap the extra mode, and give an isotropic photon, the Coulomb law and a Gauss-consistent split

Claim type: bounded_theorem.
Primary runner: `scripts/site_bond_link_registers_need_skew_loop_plaquettes_to_gap_the_extra_mode_and_give_an_isotropic_photon_coulomb_law_and_a_gauss_consistent_split_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) tiles the sites of Z^3 in two ways by 2x2x2 cubes offset by (1,1,1) and places each link register on a site, on the bond from the centre of the site's even-tiling cube to the centre of its odd-tiling cube. Its response law (CL-3) reads a plaquette phase on those registers. This note asks how many gauge-invariant values that layout carries, which plaquette set gives them stiffness, what the photon and the static law are, and how a block split passes the registers to its children. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the couplings used here.

## Statement

Geometry.

1. Each site is the midpoint of its own bond from even to odd centre, with offset in {+-1}^3; sites and bonds are in bijection. The centres form the body-centred lattice and the register bonds are its nearest-neighbour bonds, 8 per centre. The centre lattice is Bravais with one centre and 4 bonds per primitive cell, so the gauge-invariant values are 3 per centre (6 per 2^3 cell).
2. The smallest register loops (4-cycles) per 2^3 cell are 12 skew quads, whose two diagonals both lie along axes, and 12 planar rhombi, with one axis diagonal and one face diagonal (faces of the rhombic dodecahedron). Each register lies in 6 loops of each kind.

Quadratic plaquette spectra (H = (U/2) sum E_b^2 + (K/2) sum_p F_p^2, omega^2 = U K lambda with lambda the eigenvalues of curl^dagger curl off the gauge directions).

3. The earlier plaquettes, cubic squares on the even-centre lattice with each centre bond's value the mean of its four two-site register paths, give no stiffness to the extras: of the 6 gauge-invariant values per 2^3 cell exactly 4 have lambda = 0 at every momentum. Adding the odd tiling's centre squares in the same way still leaves 2 flat zero branches.
4. Skew register loops zero only the photon pair at q -> 0. The one extra branch per centre is gapped at the cell scale (lambda = 24 at q = 0, lowest value 8 on a 14^3 scan of the primitive zone). The photon is isotropic at order q^2 (lambda = 2 q^2) with degenerate polarisations; at order q^4 the pair splits as lambda_+- = 2 q^2 (1 - q^2/12 +- b q^2) with b = 0 on axes and body diagonals and b = 1/12 on face diagonals, a dimension-six birefringence Delta v/c = b (qa)^2.
5. The gapped extra at q = 0 is the pattern A_d = d1 d2 d3 on the four bond directions d: + toward one tetrahedron of each cube, - toward the other. It is invariant under the 12 tetrahedral rotations and odd under the 12 that the copy mass breaks.
6. Planar rhombi alone are not enough: their extra branch is gapless at q = 0, a third massless mode with lambda_extra ~ q^2. Skew and planar loops together also gap the extra (lambda = 24 at q = 0, lowest 16.78 on the scan) with photon lambda = 6 q^2.
7. Zone folding: the 6 branches of the 2^3 cell are the primitive cell's 3 at q and at q + (pi, pi, pi). Of the 4 extras per 2^3 cell, 2 are the photon's own folded copy and only 2, one per centre, are new modes.

Coulomb law.

8. Least electric energy under Gauss's law on the register lattice gives E = -grad phi with Lap phi = q on the centre lattice. Static charges +-1 on even centres shift the energy by -U G(R) with 4 pi R G -> 1 isotropically: 8 bonds of length sqrt3 per centre and 1/4 centre per site volume give (8 x 3/6)(1/4) = 1. The Coulomb coefficient is 1, with alpha = U/(4 pi c).

Split.

9. Coarse totals for site registers: each parent register's value is the flux of its even cube's children into the child centres on the cube's boundary nearest the parent register's odd end, shared with weight 1 at the corner (the parent odd centre itself), 1/2 at edge midpoints and 1/4 at face centres. With these weights every parent Gauss law is the weighted sum of child Gauss laws, R D_c = D_p S exactly.
10. The shares are fixed: an edge-midpoint (face-centre) child centre is equidistant from 2 (4) parent odd centres that the parent cube's symmetries permute transitively, so covariance makes the shares equal and the Gauss sum makes them add to 1. For the same reason no covariant integer assignment exists, and assigning such a centre to a parent even centre would join two even centres.
11. A skeleton passing exists that is integer, local and covariant: a parent register's bond is two collinear child bonds; its value rides the outer half (child even centre to parent odd centre), the inner half carries the child charge minus that value, and every other child value is 0. Every child Gauss law holds for any split of the parent charge over its children, and the coarse totals return the parent values.
12. The coarse map sends each long-wavelength child photon (skew loops) into the parent photon pair at the same momentum, with leakage into the parent extras growing as q^2.

## Derivation

Item 1. With even centres at 2 floor(x/2) + 1/2 and odd centres at 2 floor((x - 1)/2) + 3/2 per coordinate, their midpoint is the site x and their offset is +-1 in each coordinate. The two centre sets are the two cubic sublattices of a body-centred lattice, and +-1^3 offsets are its nearest-neighbour vectors. One gauge parameter per centre removes one of its 4 bonds.

Items 3 to 7. In Bloch form each plaquette set gives a matrix C(q) on the 4 primitive (or 8 conventional) bond amplitudes; the physical spectrum is that of C^dagger C projected off the gauge columns. Item 5 follows because d1 d2 d3 is invariant under the even permutations and sign pairs that preserve each tetrahedron and changes sign under the rest. Item 7 is the folding of the body-centred zone into the simple-cubic one by the vector with e^{iG.v} = -1 on odd centres.

Item 8. The lattice Green's function of the centre lattice approaches 1/(4 pi kappa_eff R) with kappa_eff set by the bond count, bond length and volume per centre, which multiply to 1 as stated.

Items 9 and 10. The sum of child Gauss laws over a parent even cube counts the flux leaving the cube through each boundary child centre; distributing each boundary centre's flux over the parent odd centres nearest it, with shares summing to 1, gives the parent Gauss law term by term.

Item 11. On each parent bond the outer child half reproduces the parent value at the parent odd centre; at the child even centre the two halves meet with net flux equal to the child charge; all other bonds are 0, so the remaining child Gauss laws hold trivially.

## Checks

The runner ends with `TOTAL: PASS=16 FAIL=0` in about 1 s. It uses numpy only and builds no Fock space.

Exact checks and identities (checked numerically):
- Geometry on an 8^3 site torus: 512 sites, 512 distinct bonds, 64 cells; 12 skew and 12 planar 4-cycles per cell, the planar ones coplanar.
- Earlier plaquettes: 4 zero physical branches at each of 30 random momenta; nonzero eigenvalues 0.896 and 2.694 at a sample momentum. With the odd tiling's squares added: 2 zero branches.
- Extra mode pattern: overlap with d1 d2 d3 equal to 1.000000000000, lambda = 24.000.
- Zone folding: maximum deviation 3.6e-15 between the conventional spectrum and the primitive spectra at q and q + (pi, pi, pi). The conventional q = 0 spectrum on skew loops is [0, 0, 0, 8, 8, 8, 24] beyond the gauge directions (printed, not asserted).
- Split on 2^3 parent cells (4^3 child cells): max |R D_c - D_p S| = 0.0e+00; boundary child centres with 1, 2, 4 nearest parent odd centres: 8, 24, 24. Skeleton passing on 20 random parent Gauss configurations with random integer charge splits: maximum residual 0.0e+00.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Skew loops: extra at q = 0 24.000, lowest on the 14^3 zone scan 8.000; kappa = lambda/q^2 = 2.0000 along axis, face, body and generic directions with polarisation splitting below 1e-5 q^2 at |q| = 1e-3; order-q^4 coefficient of the mean -0.0833 in all five directions tested; birefringence b = 0.0000 (axis), 0.0833 (face diagonal), 0.0000 (body diagonal), 0.0507 (direction (1,2,3)), 0.0533 (direction (2,1,0)), from |q| = 0.02.
- Skew plus planar loops: extra at q = 0 24.000, lowest on the scan 16.780; kappa 6.0000; order-q^4 coefficients -0.0833, -0.1389, -0.1574, -0.1389, -0.1189 (axis, face, body, (1,2,3), (2,1,0)).
- Planar rhombi alone: extra at q = 0 4.0e-14; lambda_extra/q^2 = 4.000 against photon kappa 4.000.
- Coulomb coefficient 4 pi dG/d(1/R) over R .. 2R on a 48^3-cell torus with the torus background r^2/(6V) removed: along an axis 0.987, 0.991, 0.984 at R = 8, 12, 16 sites; along the body diagonal 1.014, 1.007, 1.007 at R = 4 sqrt3, 6 sqrt3, 8 sqrt3 (tolerance 2%).
- Coarse map of child photons: leakage into the parent extras 2.5e-05, 1.6e-04, 6.2e-04 at |q| = 0.02, 0.05, 0.1 (child units), over three directions. The check asserts weight above 0.99 and growing leakage; the q^2 scaling is read from these values (ratios 6.4 and 3.9 against 6.25 and 4).

## Estimates against measurement

- Large-S ring exchange on register loops, with supplied U = 2 J S(S+1) N_p and K = 2 J [S(S+1)]^2 (N_p loops per register): alpha(S) = sqrt(N_p/(kappa S(S+1)))/(4 pi). At S = 3/2: skew 0.0712, planar 0.0503, both 0.0581 (the cubic edge layout gives 1/(2 pi sqrt(S(S+1))) = 0.0822). The hypercharge link's cell-scale target alpha_Y/36 = 5.0e-4 (supplied) would need sqrt(S(S+1)) of about 275 (skew), 195 (planar) or 225 (both).

## Boundary

Supplied: the plaquette sets compared, the quadratic Hamiltonian with independent U and K, the large-S ring-exchange values of U and K, the coupling target 5.0e-4, the torus and scan sizes, the random momenta and Gauss configurations, and the skeleton's zero rest (the register's split uses a vacuum-weighted rest instead). Forced, given the layout: 3 gauge-invariant values per centre, the zero-stiffness branches of the earlier plaquettes, the gapped extra, isotropy and polarisation degeneracy of the photon at order q^2 on skew loops, the face-diagonal birefringence, the gapless extra for planar rhombi alone, Coulomb coefficient 1, the coarse-total shares 1, 1/2, 1/4, the absence of a covariant integer assignment and the existence of the skeleton passing. Not claimed: that skew loops are the unique plaquette set; a gap at every point of the zone beyond the 14^3 scan; any interacting or truncated register dynamics (only quadratic spectra are computed); the value of alpha, which here depends on supplied U and K; that the skeleton passing is the register's split rule; re-derivation on skew loops of the earlier link-metric results; any continuum limit.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the two tilings and the site-bond link registers of the update law, the plaquette phase of the response law and the block split. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/site_bond_link_registers_need_skew_loop_plaquettes_to_gap_the_extra_mode_and_give_an_isotropic_photon_coulomb_law_and_a_gauss_consistent_split_2026_10_22.py
```

Needs numpy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 50 MB resident, prints about 5.8 kB and ends with `TOTAL: PASS=16 FAIL=0`. Its random momenta and configurations are seeded; repeated runs gave identical output apart from the elapsed-time line.
