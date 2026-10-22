---
claim_id: a_cube_tick_that_reads_its_own_lapse_and_edges_is_weyl_blind_so_its_vacuum_entropy_counts_cut_bonds_not_proper_area_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's cube tick with the hop between neighbours set by lapse over proper length (N sum_i W_i / l_i, no per-cube renormalisation): (i) with the lapse clause N|w| = sin eps0 this hop reproduces the register's cube unitary exactly (|dU| = 2e-18), so the per-cube normalisation is the lapse clause; (ii) freeing the lapse and reading each cube's step from sin eps_c = N_c|w_c| keeps the dressed cone exact cube by cube (the tick's maximum group velocity is (2/sqrt3) sin eps sites per tick at every step, ratio 0.99997 to 0.99998 at eps = 0.0375 to 1.3) and the rest phase mN per tick exact (to 1e-14); (iii) a cube reads only ratios of its own N and l_i, so a cube-wise 4D Weyl rescaling leaves the vacuum and every entropy unchanged (8^3 torus, factors over [1/8, 4]: |dS| = 7.4e-13), and a uniform spatial rescaling at fixed N changes S only through the Floquet step (dlnS/dlnA = -4.3e-4 at eps0 = 0.0375). The vacuum entropy is therefore eta times the number of cut bonds, not eta times proper area. Finite diagnostics: homogeneous strains are unchanged from the normalised tick (dlnS/dlnA = 0.457 transverse, dlnS = -0.911 eps normal at fixed area); random cube-wise edge factors at fixed N give a regression slope -0.31 against ln(proper cut area); a mass m makes the vacuum depend on m l, with dlnS/dlnA = -0.015, -0.048, -0.141 at m l = 0.25, 0.5, 1. The induced static action of the massless sea is Weyl invariant, coefficients 1 : -2 : 1 against Einstein-Hilbert's 2 : 4 : 0, so it has no Newtonian limit; a staggered mass induces an attractive static Newtonian coupling with G_N = 9.7 and 4.7 site^2 at m = 0.5 and 1. Estimates: Jacobson's G_J = 1/(4 eta) = 1.27 site^2 is 8.0 (cell-rung reading) or 32 (site reading) times the hinge-sum G. Supplied model, finite diagnostic: pi-flux sea and cube tick at eps0 = 0.0375, x-dependent static lapse and conformal factor, three readings of a non-uniform edge's length, staggered mass on both copies, planar cuts."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_cube_tick_that_reads_its_own_lapse_and_edges_is_weyl_blind_so_its_vacuum_entropy_counts_cut_bonds_not_proper_area_2026_10_22.py
---

# A cube tick that reads its own lapse and edges is Weyl-blind, so its vacuum entropy counts cut bonds, not proper area

Claim type: bounded_theorem.
Primary runner: `scripts/a_cube_tick_that_reads_its_own_lapse_and_edges_is_weyl_blind_so_its_vacuum_entropy_counts_cut_bonds_not_proper_area_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. A merged candidate ruleset reads Einstein's equations from vacuum entanglement (rule M5: entanglement of small regions is maximal at fixed volume), with Jacobson's coupling 1/(4G) = eta, where S = eta A. A companion computation (THE_CUBE_TICK_SEAS_ENTANGLEMENT_IS_BLIND_TO_THE_CONFORMAL_FACTOR_SO_A_JACOBSON_G_FROM_IT_HAS_NO_NEWTONIAN_PART_AND_EXCEEDS_THE_HINGE_SUM_G_BOUNDED_THEOREM_NOTE_2026-10-22, open PR #10011) found that the update law's sea is blind to the spatial conformal factor and attributed this to each cube normalising its hop. This note tests the proposed repair: the hop between neighbours is set by their proper separation, as in a discretised Dirac operator on a curved lattice, with no per-cube renormalisation. It asks whether S then scales as eta times proper area, computes G both ways from the same sea (Jacobson's entanglement route and Sakharov's induced action), and lists what the repair costs the update law. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Exact.

1. The normalisation is the lapse clause. The W_i anticommute, so the unnormalised hop N sum_i W_i / l_i squares to (N|w|)^2 with w_i = 1/l_i. Under the register's lapse clause, sqrt(3) N rms(w) = N|w| = sin eps0. The cube unitary cos(eps0) - i sin(eps0) R-hat is then identically cos(eps0) - i N sum_i W_i / l_i. The register's hop is already lapse over proper length. The conformal blindness comes from the clause that reads N from the edges, not from a separate normalisation.
2. Two variants of the repair.
   - R1 keeps the step eps0 on the unnormalised hop. The cube then applies the normalised hop at angle eps0|w|. Since the tick's maximum group velocity is (2/sqrt3) sin(eps) sites per tick at every step (item 6), light speed in proper units scales by sin(eps0|w|)/sin(eps0): x7.9 at edge l = 1/8 and x0.25 at l = 4. This breaks the cone clause (the dressed cone is no longer the null cone of the edges). R1 is rejected.
   - R2 frees the lapse. Each cube reads its step from sin(eps_c) = N_c|w_c|, with N_c a datum the update does not fix. The light cone is exact cube by cube for any lapse, provided N|w| <= 1.
3. 4D Weyl blindness. Under R2, as under the register, a cube reads only dimensionless ratios of its own data (N/l_i, l_i/l_j). A cube-wise rescaling (N, l) -> Omega (N, l) therefore leaves every step, the tick, the vacuum and every entropy unchanged, while proper areas scale by Omega^2. More generally, any tick read from a cube's own geometry with no external length standard has this property. A uniform spatial rescaling at fixed N leaves the static vacuum exactly unchanged (the ground state of cH is the ground state of H); in the tick only the step moves, an O(eps^2) Floquet effect.
4. Hence S = eta x (number of cut bonds) for the massless sea, never eta x proper area: with proper spacing a, eta_proper = eta/a^2 and G_J = a^2/(4 eta), constant in lattice units and varying as a^2 in proper units (x1024 across the edge window [1/8, 4]).
5. Induced static action. With a static lapse e^phi and conformal factor e^sigma, the vacuum energy (E = -L) is a functional of phi - sigma alone (item 3). Its gradient terms therefore stand in the ratio (grad sigma)^2 : grad phi.grad sigma : (grad phi)^2 = 1 : -2 : 1. The static Einstein-Hilbert action is (1/16 pi G)(2 : 4 : 0). In the general static form A(grad sigma)^2 + B grad phi.grad sigma + C(grad phi)^2 - rho phi, the Newtonian solution has Delta phi = rho/(B^2/(2A) - 2C). Weyl invariance makes B^2/(2A) - 2C = 0 (the operator matrix is singular, and the equations force rho = 0). The massless sea induces no Newtonian limit. Its N sqrt(h) R3 component alone would read 1/(4G) = 4 pi alpha, with alpha = B/4.

B. Finite diagnostics (supplied model).

6. Dressed cone (Bloch, 2x2x2 cell): v_max/((2/sqrt3) sin eps) = 0.99997, 0.99997, 0.99997, 0.99998, 0.99998 at eps = 0.0375, 0.3, 0.6, 1.0, 1.3 (the finite k-grid sets the deficit).
7. Massive tick: the rest phase equals mu = mN per tick to 1e-14 at every step, so rest energy couples to the lapse universally under a varying step. The inertial factor is 1 - (mu/eps)^2/4 plus a step-dependent remainder of 0.06 to 0.08 mu^2. That remainder is species-dependent, of order (m l)^2 with l the cube size, so it is negligible for any observed mass.
8. Weyl check on the 8^3 Floquet tick with random cube N and l: Weyl factors over [1/8, 4] give |dS| = 7.4e-13; spatial-only factors over [1/2, 2] at fixed N give |dS| = 0.41 (the repair does respond).
9. Homogeneous strains (planar (100) cut): R2 and the register give the same vacuum. dlnS/dlnA = 0.457 under transverse stretching (area law 1); dlnS = -0.911 eps under normal stretching at fixed area (area law 0). eta_100 = 0.196645 per site^2, unchanged.
10. Random cube-wise edge factors (ln lambda ~ N(0, 0.35^2)) at fixed N, static 8^3, 10 draws: S moves (spread 0.056 in ln S), but its regression slope against ln(proper cut area) is -0.31, not 1.
11. A mass is the only scale the sea can compare with l. With hop N/l and rest phase mN the vacuum depends on m l; a staggered mass enters the chains as sqrt(M^2 + m^2) (exact on 8^3: 22.70463714 both ways). eta(m l) = 0.1933, 0.1858, 0.1647, 0.1195 at m l = 0.25, 0.5, 1, 2. At fixed N/l, dlnS/dlnA = (1/2) dln eta/dln(ml) = -0.015, -0.048, -0.141: wrong sign for an area law.
12. Induced static coefficients (Lx = 32, 2x2 Bloch cell, 8^2 transverse momenta): e_ss = e_pp = 0.04956 and e_ps = -0.09911 for the massless sea (ratio exact to 1e-6, B^2/(2A) - 2C = 0 to machine precision); 4 pi alpha = 0.311 per site^2 against eta = 0.197. Different readings of a non-uniform edge's length in the hop (straight-edge proper length, geometric mean, arithmetic mean of the end factors) give 4 pi alpha = 0.416, 0.311, 0.624: the cell-scale coefficient is set by a reading the rule must supply.
13. A staggered mass (both copies) breaks Weyl invariance and gives B^2/(2A) - 2C > 0: an attractive static Newtonian coupling, G_N = 9.7 site^2 at m = 0.5 and 4.7 site^2 at m = 1.

## Derivation

Item 1 is algebra on one cube. Item 2 combines item 1 with item 6. Item 3: each cube's unitary is a function of eps_c and R-hat, both fixed by N_c/l_i and l_i/l_j. Item 5: E[phi, sigma] = F[phi - sigma] expanded to second order in a single Fourier mode; the static Einstein-Hilbert form uses int N sqrt(h) R3 for g = -e^(2 phi) dt^2 + e^(2 sigma) dx^2, with int sqrt(h) R3 = 2 int e^sigma (grad sigma)^2. The cone is computed from the Bloch tick by finite differences along k_x lines on a 4 x 4 transverse grid. The induced coefficients come from second differences of the filled-sea energy at s = 1e-3 for three wavevectors, fitted in q^2 to second order. eta(m) uses the transverse-momentum chain decomposition of the companion note (open chains of 600 sites, spline in ln u, 400^2 grid).

## Finite checks

Exact or closed-form checks (the runner asserts each):
- |U_CL1 - U_un| = 2e-18; |R_un^2 - sin^2 eps0| = 4e-20.
- Rest phase/mu - 1 below 2e-14 at six (eps, mu) pairs.
- Weyl rescaling on the 8^3 Floquet tick: |dS| = 7.4e-13; uniform static rescaling |dS| = 3e-13.
- Massive slab, 8^3: real space = chain sum to 1e-9.
- Massless induced coefficients 1 : -2 : 1 to 1e-6; B^2/(2A) - 2C = 0 to machine precision.

Finite diagnostics (supplied model, finite diagnostic): items 6 to 13.

## Estimates against measurement

| route (same sea, supplied content) | 1/(4G) per site^2 | G/G_hinge (cell rung, B) | (site, A) |
|---|---|---|---|
| Jacobson, eta_100 (massless) | 0.197 | 7.99 | 32.0 |
| N sqrt(h) R3 part of the induced action, three edge readings | 0.31 to 0.62 | 2.5 to 5.0 | 10 to 20 |
| induced static Newtonian coupling, massless | 0 (no Newtonian limit) | infinite | infinite |
| induced static Newtonian coupling, staggered mass m = 0.5 / 1 | G_N = 9.7 / 4.7 site^2 | 61 / 29 | 243 / 117 |

- Measured gravity has a Newtonian limit; the massless sea's induced action has none, and its entropy has no area response to the Weyl factor. Both agree with the companion result that the tick sea induces no Newtonian sector.
- The Weyl-breaking route (masses) has the right sign for the induced coupling but the wrong sign for the entropy response, and gives a G_N 30 to 60 times the hinge-sum G at cell-scale masses.
- In the continuum the entanglement and induced-action couplings coincide for spin-1/2 fields under a common covariant regulator. On the lattice they differ (0.197 against 0.31 to 0.62) because the cutoff is attached to the sites and Weyl-transforms with them.

## Boundary

Not claimed: the time-dependent (kinetic) part of the induced action; the copy mass on one copy only (the staggered mass gives both copies the mass); cuts other than (100); rishon, link and edge-register entanglement; any value of the physical G. The heat-kernel matching note on main (UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17) gives G = 3 pi/(N_f Lambda^2) with a fixed proper cutoff Lambda. This note narrows it for the cube tick: when the hop reads lapse over proper length, the cutoff Weyl-transforms with the cell, the massless Einstein-Hilbert term is absent, and only Weyl-breaking masses induce a Newtonian coupling. The note's supplied-cutoff result is not contradicted. The companion note (open PR #10011) attributes the blindness to the per-cube normalisation; item 1 narrows that attribution to the lapse clause, and item 3 extends the blindness to the repaired tick.

## Supplied vs forced

Supplied: the pi-flux sea and cube tick at eps0 = 0.0375; the repair's two variants; x-dependent static lapse and conformal factor; three readings of a non-uniform edge's length; staggered mass on both copies; planar cuts; readings A and B of the unit map. Forced, given those: items 1 to 5; the numbers in items 6 to 13; the table.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick (lapse clause, hop weights sqrt(gamma^ii), face phase -1, species angles), the response law's hinge sum and unit map, the edge window. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_cube_tick_that_reads_its_own_lapse_and_edges_is_weyl_blind_so_its_vacuum_entropy_counts_cut_bonds_not_proper_area_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 13 s with under 90 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draws are seeded; the run through `runner_cache.execute_runner` gave the saved output.
