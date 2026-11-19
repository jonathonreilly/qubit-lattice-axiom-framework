---
claim_id: random_connectivity_makes_count_area_isotropic_but_a_one_qubit_hop_loses_its_cone_and_a_free_tick_count_carries_light_bending_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Two repairs of the count-geometry rule are tested. R-b, random connectivity: sites form a Poisson point set and the connectivity is its Delaunay complex (Voronoi dual). Exact: (i) for ANY point set the Voronoi weights w_ij = A_ij/(2|d_ij|) obey sum_j w_ij d_ij = 0 and sum_bonds w d d^T = (V/2) 1, so the affine cone tensor of a first-order hop is exactly isotropic in every realisation (divergence theorem per cell); (ii) the Voronoi Wilson-Dirac hop annihilates every constant spinor (untuned k = 0 zero mode); (iii) the Poisson ensemble is rotation invariant, so every ensemble-averaged count or entropy is isotropic. Finite diagnostics: cut bonds per Euclidean area 4.972, 4.956, 5.020 (+-0.03-0.04) for (100), (110), (111) at N = 2000 (Z^3: 1, 1.414, 1.732), with per-cut scatter 0.67/sqrt(N_cut); jittered Z^3 keeps a 5-12% cubic count anisotropy until the jitter reaches ~0.5 spacing; a two-level (one-qubit) hop on a Poisson-Voronoi graph, whether it carries bond directions or is generic, has a finite density of states at E = 0 (5.5% and 7.1% of states within 5% of the bandwidth, size independent): no cone; the four-level Voronoi Wilson-Dirac hop keeps a cone (E_1 L/(sqrt3 pi) = 0.838, 0.862 at N = 343, 729); the metric-free Kaehler-Dirac operator d + d^T on the Delaunay complex has exactly the Betti numbers 1, 3, 3, 1 as zero modes and 1/L low modes, but its three form-degree branches move at 1.96, 0.53 and 0.33; the Wilson-Dirac sea's entropy per cut bond is 0.0387, 0.0398, 0.0393 (+-0.0004-0.0006) for the three cuts ((111)/(100) - 1 = +0.015 +- 0.018) against -0.273 per bond for the same hop on Z^3. R-a, independent tick count: exact: with lapse N = 1 - U (taken-tick fraction) and spatial factor Omega = 1 + gamma U (site density^(1/3)) the linearised vacuum Ricci is R_00 = 0, R_ij proportional to (gamma - 1), so Ricci-flat response forces gamma = 1; a skip-tick chain carries Shapiro delay and deflection proportional to (1 + gamma) (447.1 vs 446.2 ticks exact), while the tied tick N = Omega carries none. Estimates: eta = 0.0393 per cut bond for one Wilson-Dirac sea, a/l_P = 2 sqrt(eta) = 0.396 per area quantum (mean spacing 0.887 l_P); statistical G anisotropy at 1 AU ~ 7e-47 against an order-of-magnitude orbit requirement ~1e-10. Gate: R-b passes clauses 1-2 and the isotropy prediction, but the one-qubit hop loses its cone, so a cone needs bond-direction data (a metric register, which the count rule removed) or one mode per simplex with a degree-speed rule (UNTESTED); the preferred rest frame of a spatial sprinkling is an UNTESTED risk against preferred-frame bounds. R-a passes the gate as kinematics: it allows gamma = 1, and forces it only together with a Ricci-flat response."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/random_connectivity_makes_count_area_isotropic_but_a_one_qubit_hop_loses_its_cone_and_a_free_tick_count_carries_light_bending_2026_10_22.py
---

# Random connectivity makes count area isotropic, but a one-qubit hop loses its cone; a free tick count carries light bending

Claim type: bounded_theorem.
Primary runner: `scripts/random_connectivity_makes_count_area_isotropic_but_a_one_qubit_hop_loses_its_cone_and_a_free_tick_count_carries_light_bending_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The geometry-as-count probe (agents/geometry-as-count) tested the rule "counts are geometry: every cut bond is one area quantum a^2". It found that on Z^3 count area is taxicab (|n|_1 cut bonds per Euclidean area) while the sea's cone is isotropic, so a count-Jacobson G varies by 1.48 with horizon orientation. It also found that tied-tick splits give a conformally flat geometry with PPN gamma = -1. It proposed two repairs and left both UNTESTED: R-b, random connectivity, and R-a, an untied tick. This note tests both. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Candidate rules

> R-b: "Sites are a Poisson point set of fixed density; neighbours are its Delaunay neighbours. Counts are geometry."

> R-a: "A site may skip a tick. The lapse is the fraction of ticks a site takes, counted against the asymptotic tick, independent of refinement."

R-b bends the Lattice axiom (Z^3 is replaced by a random complex). R-a changes CL-1's universal tick: every site no longer updates on every step. Whether the axioms' own update text requires every site on every step still has to be checked.

## A. Exact

1. **Voronoi closure and exact affine isotropy (any point set).** Take the Voronoi cell of r_i, with face areas A_f, outward normals n_f = d_ij/|d_ij| and face centroids c_f. The divergence theorem applied to x - r_i gives V_i 1 = sum_f A_f n_f (x) (c_f - r_i), and sum_f A_f n_f = 0. With w_ij = A_ij/(2|d_ij|), the second identity is sum_j w_ij d_ij = 0. Write c_f - r_i = d_ij/2 + t_f, with t_f in the face. The two cells sharing a face contribute A n (x) (d/2 + t) and A (-n) (x) (-d/2 + t), so the t terms cancel. Summing over cells gives sum_bonds A_ij |d_ij| n n^T = V 1, that is, sum w d d^T = (V/2) 1. This is exact in every realisation. It holds for any first-order hop i w_ij Gamma.d_ij, so the affine (unrenormalised) cone metric of such a hop is exactly isotropic. Runner A1: 1.4e-15 and 1.1e-15.
2. **Untuned massless point.** The Voronoi Wilson-Dirac hop, i w alpha.d - r w beta off-site and + r w beta on-site, annihilates every constant spinor. This follows from closure plus the Laplacian structure, so k = 0 is massless with no tuned parameter (A2).
3. **Ensemble isotropy.** The Poisson process is invariant under rotations. Its Delaunay and Voronoi complexes are covariant functions of the points, so every ensemble mean (cut-bond density, entropy, renormalised speed) is isotropic. A single realisation fluctuates, and the runner measures those fluctuations (B1, B6).
4. **R-a: two counts carry two potentials.** In the static weak field ds^2 = -N^2 dt^2 + Omega^2 dx^2:
   - N is the fraction of global ticks a site takes, so proper time per tick is fixed.
   - Omega^3 a^-3 is the number of sites per coordinate volume, which is "volume = number".
   - These are two independent integers per region, so N = 1 - U and Omega = 1 + gamma U with any gamma are kinematically available.
   - Light hops one bond (proper length a) per taken tick, so its coordinate speed is N/Omega. The delay is (1/a) integral (Omega/N - 1) dx, which equals (1 + gamma)/a integral U dx at first order, and the deflection is 2(1 + gamma)M/b.
   - The linearised Ricci tensor (sympy, A3) is R_00 = 0, R_xx = -M(gamma - 1)(2x^2 - y^2 - z^2)/r^5 and R_xy = -3M(gamma - 1)xy/r^5. Vacuum Ricci-flatness therefore forces gamma = 1, and gamma = -1 reproduces geometry-as-count's R_xy = 6Mxy/r^5.
   - The tied tick of the split clause is N = Omega, which is gamma = -1 with no bending.
5. **R-a discrete check (A4).** Sites sit at coordinate spacing a/Omega, and each takes a deterministic fraction N of the global ticks (an accumulator). A signal hops one site per taken tick. At M/b = 0.05 the delay is 447.1 ticks against the exact integral 446.2 (first order: 438.2). The b -> 2b change, the discrete deflection, is 73.6 against 73.4. With the tied tick both delays are 1 tick (quantisation).

## B. Finite diagnostics (supplied model; seeded, density 1, antiperiodic tori)

6. **Count area isotropic (B1).** Poisson-Delaunay cut bonds per Euclidean area, 6 seeds, mean degree 15.5:

| N | (100) | (110) | (111) |
|---|---|---|---|
| 500 | 5.093 | 5.001 | 5.032 |
| 2000 | 4.972 +- 0.027 | 4.956 +- 0.034 | 5.020 +- 0.042 |
| Z^3 | 1 | 1.414 | 1.732 |

   The largest deviation is 0.9 sem. The per-cut relative scatter is 0.67/sqrt(N_cut), a pure 1/sqrt(count) law.
7. **Jittered lattices are not enough (B2).** Delaunay of Z^3 + Gaussian jitter sigma gives the following ratios:

| jitter sigma | (110)/(100) | (111)/(100) |
|---|---|---|
| 0.05 | 1.116 | 1.052 |
| 0.3 | 1.048 | 1.049 |
| 0.5 | 1.004 | 1.005 |

   The cubic anisotropy fades only once the long-range order is effectively gone.
8. **A one-qubit hop has no cone on a random graph (B3).** Two two-level hops were tried on Poisson-Voronoi graphs, N = 216 and 343:
   - the frame hop i w sigma.d_ij, which carries bond directions;
   - a generic random 2x2 hop, which carries no directions.

   Both have a finite density of states at E = 0. The fraction of states within 5% of the bandwidth is 0.056 and 0.055 (frame) and 0.072 and 0.070 (generic), independent of size. The same frame hop on Z^3 6^3 has none. The cone rule's codimension argument (agents/why-three-dims) needs translation invariance. On a random graph the doubler region of the frame hop scrambles into a zero-energy band, and a two-component hop has no Wilson mass to lift it.
9. **A four-level hop keeps a cone (B4).** The Voronoi Wilson-Dirac hop (r = 1) has lowest level E_1 = 0.652 and 0.521 at L = 7 and 9. That gives E_1 L/(sqrt3 pi) = 0.838 and 0.862, so E is proportional to 1/L, a cone with renormalised speed about 0.86 of the affine value 1. A finite DOS would instead give E_1 proportional to 1/N. The lowest-20 shell spreads by 4.7-4.8%, which is disorder splitting; on Z^3 the shell is exactly degenerate.
10. **Metric-free Kaehler-Dirac (B5).** D = d + d^T on the periodic Delaunay complex uses unit incidence weights and no embedding data.
    - d^2 = 0 holds exactly, and the zero modes are exactly the Betti numbers 1, 3, 3, 1 of the 3-torus. They are protected by topology, not by translation invariance.
    - The low modes scale as 1/L: speeds 1.906, 0.521, 0.327 at N = 343 against 1.957, 0.531, 0.329 at N = 729, for the d0, d1 (curl) and d2 branches. Every degree has a cone.
    - The three speeds differ by up to 6x, so there is no single cone. A single cone needs the Hodge-star (dual-volume) weights, which are metric data, or a degree-weight rule (below).
11. **Entropy per cut bond isotropic (B6).** Wilson-Dirac half-filled sea (one Dirac = 2 Weyl), N = 343, 6 seeds. The entropy is computed from the real-antisymmetric form H = iA, with S = sum h((1 + nu)/2) over eig(Gamma_A^T Gamma_A).

| cut | per cut bond (Poisson) | per Euclidean area | Z^3 7^3 per bond | Z^3 per area |
|---|---|---|---|---|
| (100) | 0.0387 +- 0.0006 | 0.1937 | 0.2184 | 0.2184 |
| (110) | 0.0398 +- 0.0005 | 0.1995 | 0.1793 | 0.2535 |
| (111) | 0.0393 +- 0.0004 | 0.1963 | 0.1587 | 0.2748 |

    (111)/(100) - 1 is +0.015 +- 0.018 on Poisson graphs, against -0.273 per bond and +0.258 per area on Z^3. The per-cut scatter is 3.2% at 490 bonds, which is 0.70/sqrt(N_cut). Count area and cone-metric area are therefore proportional with an orientation-independent constant: the count rule's area quantum is consistent with the cone on random graphs, and not on Z^3.

## Estimates against measurement

- Cell size. The count-Jacobson relation G = a^2/(4 eta), with a^2 the area per cut bond, gives eta = 0.0393 per bond (0.0196 per Weyl) and a/l_P = 2 sqrt(eta) = 0.396. With 5.005 cut bonds per spacing^2, the mean spacing is rho^(-1/3) = 0.887 l_P. This equals geometry-as-count's a/l_P on Z^3 to three digits, because the per-area coefficients happen to agree (0.1965 vs 0.19664). The contents (one Wilson-Dirac against the four-Weyl pi-flux sea) and the readings differ, so this is a COINCIDENCE, not a result. eta depends on the supplied Wilson r and on the content.
- Anisotropy of G.
  - Requirement. No published bound on a cubic (l = 4) anisotropy of G was found. Order estimate (mine, not recomputed from ephemerides): a non-central l = 4 part epsilon of the solar potential precesses Mercury's perihelion by about epsilon rad per orbit. Anomalous perihelion residuals are about 3e-3"/cy, or about 3.5e-11 rad per orbit, so epsilon must be at most about 1e-10. The nearest published analogues are the preferred-frame parameters, |alpha_2| of about 2e-9 (pulsars) and |xi| of about 4e-9.
  - Random-graph value. The ensemble anisotropy is exactly zero (A3). Realisation scatter is 0.7/sqrt(N_cut), about 0.7 l_P/1 AU, or about 7e-47 for Planck-size quanta. This PASSES by about 36 orders. Z^3 fails at O(1) (0.26-0.48).
- Light bending (R-a). The count geometry can carry gamma = 1. Cassini (gamma - 1 = (2.1 +- 2.3)e-5) is met if and only if the response is Ricci-flat outside sources (A3). Under the tied tick it is not.

## Gate (anti-smuggling)

R-b (random connectivity):

1. Measured number chosen: none. The density sets the unit. The Wilson r = 1 is supplied for the B4/B6 model only. Passes.
2. Observed structure inserted: none in the rule. But the cone in B4/B6 uses the bond vectors d_ij and the Voronoi areas, which are embedding geometry. That is exactly the length/direction register the count rule removes. The metric-free alternative (B5) needs one mode per simplex and a rule fixing the degree speeds. So "counts only + one qubit per site + a cone" FAILS (B3). Conditional pass only with a direction register (a smuggling risk; it bends the count rule) or with Kaehler-Dirac plus a degree-speed rule (UNTESTED).
3. Predictions it was not built for:
   - (p1) Count area isotropy at the 1/sqrt(N_cut) level. PASSES the orbit requirement.
   - (p2) A one-qubit hop has no cone (finite zero-energy DOS). This contradicts massless or light propagating fermions unless the hop carries more structure. It also removes the translation-invariance premise of the cone rule, so the d = 3 selection of agents/why-three-dims is no longer available: Kaehler-Dirac cones exist in any d.
   - (p3) A rest frame. A spatial sprinkling per tick defines one. The dependence of eta on horizon velocity relative to the graph is UNTESTED. An O(v^2) effect at v of about 1e-3 would exceed the alpha_2 bounds by about 1e3. Spacetime (causal-set) sprinkling avoids a rest frame (Bombelli-Henson-Sorkin, cited) but conflicts with a global tick.
4. Axiom bent: Lattice (Z^3 becomes a Poisson-Delaunay complex). With Kaehler-Dirac, also Qubit (one mode per simplex rather than per site).

Verdict R-b: count-area isotropy is REPAIRED, exactly in the ensemble and to about 1e-46 at orbit scale. The cone is not repaired for the one-qubit hop. The rule as stated FAILS; it survives only with one of two additions: a direction register, or a degree-weighted Kaehler-Dirac complex (proposed below, UNTESTED).

R-a (free tick count):

1. No measured number. Passes.
2. No named structure. Passes. The asymptotic reference tick is a supplied foliation, which is a cost.
3. Predictions: gamma = 1 is ALLOWED and forced only with a Ricci-flat response, so it is conditional on CL-3. Second-order beta is UNTESTED. N <= 1, since a site can only skip ticks, so no region ticks faster than the reference clock; this is consistent with attractive gravity and UNTESTED cosmologically.
4. Bends CL-1's universal tick, not an axiom (to be confirmed against the axiom text).

Verdict R-a: PASSES as kinematics. It cures gamma = -1 in principle. It does not supply TT waves or a shift (frame dragging is measured by LAGEOS and GP-B), so the count geometry still lacks the vector and tensor sectors.

## Proposed rule (UNTESTED): one cone for every degree

> "Matter is one mode per simplex of the connectivity complex, and it hops by the coboundary d and its transpose, with one weight per form degree fixed so that every degree shares one cone."

- d^2 = 0 makes masslessness topological (zero modes = Betti numbers).
- The degree weights are 1/c_k from the ensemble: two dimensionless ratios computed by the rule, not measured.
- On Z^3 this structure is the Kaehler-Dirac form of staggered fermions, the framework's own matter.
- Tests still needed:
  - IR spin content and taste count on a random complex;
  - whether one weight per degree yields a single isotropic cone, not just equal shell speeds;
  - the entanglement eta of that sea;
  - whether the degree weights are forced, or are three numbers chosen to match.

## Speculation (not claimed)

- An anisotropic sprinkling (direction-dependent Delaunay statistics) might carry a TT strain as a count.
- Site drift might carry a shift.
- Neither is computed.

## Boundary

Not claimed:
- Lorentz behaviour of eta for moving horizons;
- Floquet ticks (only static Hamiltonian seas are used);
- the Kaehler-Dirac sea's entropy and spin content;
- interacting stability of the random-graph cone;
- the dynamics that would fix gamma (CL-3 or Jacobson are assumed for A3's "iff");
- second-order PPN;
- cuts other than planar slabs on tori.

Finite sizes are N <= 2000 (counts), N <= 729 (spectra) and N = 343 (entropy).

Literature (cited, not recomputed): Christ-Friedberg-Lee 1982 (random-lattice field theory, Voronoi weights); Bombelli-Henson-Sorkin 2009 (Lorentz-compatible discreteness needs spacetime randomness); Kaehler 1962 and Becher-Joos 1982 (Kaehler-Dirac and staggered fermions); Will, Living Reviews 2014 (PPN bounds); Bertotti-Iess-Tortora 2003 (Cassini).

## Relation to repo notes

- Narrows agents/geometry-as-count. Its item 3 and item 7 anisotropies are Z^3 artefacts that random connectivity removes. Its item 4 (gamma = -1) is a tied-tick artefact that R-a removes kinematically. Its R-c is not needed for isotropy on random graphs.
- Conflicts with agents/why-three-dims in one respect: the cone rule's codimension argument assumes translation invariance, which R-b removes. Under R-b, d = 3 is not selected by CONE.
- The main-branch Lorentz notes using Poisson sprinkling (LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE, frontier_causal_set_bridge.py) treat spacetime sprinkling. They are not used here; they are relevant to (p3).
- ACTION_NORMALIZATION_NOTE's gamma = 1 readout is a different (field-identification) route and is not used.

## Supplied vs forced

Supplied:
- Poisson density 1 and the Delaunay/Voronoi construction;
- Voronoi weights and bond vectors for the frame and Wilson hops (embedding data);
- Wilson r = 1;
- unit incidence weights for Kaehler-Dirac;
- antiperiodic tori, slab cuts and seeds;
- for R-a: the asymptotic reference tick, the profiles N = 1 - U and Omega = 1 + gamma U, and the Ricci-flat response used for "iff".

Forced, given those: A1-A5 exactly; B1-B6 as finite diagnostics.

## How to run

```
python3 scripts/random_connectivity_makes_count_area_isotropic_but_a_one_qubit_hop_loses_its_cone_and_a_free_tick_count_carries_light_bending_2026_10_22.py
```

Requirements and behaviour:
- Needs numpy, scipy and sympy, and is self-contained.
- Declares `AUDIT_TIMEOUT_SEC = 120`.
- Runs in about 17 s with about 256 MB peak resident.
- Prints about 3.3 kB and ends with `TOTAL: PASS=11 FAIL=0`.
- Its random draws are seeded (20261022).
