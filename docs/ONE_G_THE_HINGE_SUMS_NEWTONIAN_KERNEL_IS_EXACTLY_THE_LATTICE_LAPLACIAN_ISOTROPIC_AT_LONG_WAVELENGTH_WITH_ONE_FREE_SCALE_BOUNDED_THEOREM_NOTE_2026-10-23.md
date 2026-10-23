---
claim_id: one_g_the_hinge_sums_newtonian_kernel_is_exactly_the_lattice_laplacian_isotropic_at_long_wavelength_with_one_free_scale_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Under the adopted rules (CL-3 hinge sum with coefficient kappa on the six-edge carrier; the tick fraction, the pair offsets and every spatial edge responding per CL-1's tick-fraction clause), linear static order. Finite diagnostics (lattice, every edge responding): the static kernel of the tick edges, where a record's phase -m dtau couples, is K(k) = -2 kappa x 4 sum_i sin^2(k_i/2)/tau, the nearest-neighbour lattice Laplacian, to 2e-10 at all 511 nonzero momenta of the 8^3 torus and 5e-10 at 164 wedge momenta of 16^3; the same holds at tau = 0.7 and on the Freudenthal (Kuhn) carrier (to 7e-8); so at long wavelength the Newtonian coupling is direction independent (K/(-2|k|^2) = 0.999967, 0.999983, 0.999989 along (100), (110), (111) at |k| = 0.02), and the only anisotropy is the Laplacian's 1 - (ka)^2 sum khat^4/12 (0.8% between (100) and (111) at the 16^3 torus's lowest momentum). The six-edge carrier's count area (edges crossed per Euclidean area 3.000, 3.536, 3.464; axis edges alone 1, 1.414, 1.732) is direction dependent, but the hinge sum uses each hinge's Heron area in the edges' own lengths, so the count-area exclusion (17-48%) does not apply to the adopted rule. Exact (sympy, given the supplied Regge limit): the static reduction of (kappa/2) int sqrt(g) R gives Psi = Phi and K_Phi = -2 kappa |k|^2, matching the lattice at kappa = 1, so G_N = 1/(8 pi kappa); the Regge replica entropy of the same hinge sum is 2 pi kappa A = A/(4G) with the same G; the hinge sum is homogeneous of degree 2 in the edges, so kappa is its only number and no register size, register step or block size enters G. Toy (10-site ring): the Sakharov induced edge term scales with content (-3.578 per species) and the vacuum standard's same-edge reference removes it whole (5e-15), while a fixed flat reference leaves -0.342. Verdict: one G, isotropic, equal in Newton, horizon entropy and (citing tick-fraction-waves) tensor waves; its value is one free scale, 8 pi G = u^2/kappa, and kappa = 1 is the units statement that names the cell rung u = sqrt(8 pi) l_P, i.e. the approved scale_reference_primitive read as the reduced Planck mass. Supplied, not derived: the Regge limit, Euclidean-static equivalence, the record coupling, the toy's edge reading of hops, and the lattice values of the sea's entanglement (0.0983 per Dirac) and induced (4 pi c_G = 0.0624 staggered, 0.1297 Wilson) coefficients, which differ at O(1) and are both vacuum shares removed by the vacuum standard."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - candidate_laws
runner: scripts/one_g_the_hinge_sums_newtonian_kernel_is_exactly_the_lattice_laplacian_isotropic_at_long_wavelength_with_one_free_scale_2026_10_23.py
---

# One G: the hinge sum's Newtonian kernel is exactly the lattice Laplacian, isotropic at long wavelength, with one free scale

Claim type: bounded_theorem.
Primary runner: `scripts/one_g_the_hinge_sums_newtonian_kernel_is_exactly_the_lattice_laplacian_isotropic_at_long_wavelength_with_one_free_scale_2026_10_23.py` (11 PASS, 0 FAIL, about 12 s, about 97 MB peak).

## Question

Under the adopted rules, is there one Newton constant, and is it isotropic? The adopted rules are:
- the CL-3 hinge sum on the six-edge carrier;
- edges that are quantum edge registers (CL-1);
- the tick fraction and pair offsets responding (CL-1's tick-fraction clause).

The count-geometry probe (geometry-as-count) found two problems for its own reading:
- a count-area G that varies by 17-48% with horizon orientation;
- two sea routes to G (entanglement 0.0983 per Dirac, induced 4π c_G = 0.0624 or 0.1297) that disagree at O(1).

This note asks:
1. Does either problem reach the adopted rule?
2. What sets G's value?

## Setup

- Carrier and hinge sum: the same as tick-fraction-waves. That means prisms over the campaign's spatial triangulation, 13 edges per site, and the Euclidean linearised Regge second variation, Bloch-transformed on the 8-site cell. The code is copied, so the runner is self-contained.
- Newtonian kernel: a static source (k_4 = 0) is put on every site's tick edge, since that is where a record's phase -m dτ couples. Every other edge responds, through the pseudo-inverse of the full hinge-sum Hessian.
  - At k_4 = 0 the tick edges are gauge invariant: static displacements leave them unchanged.
  - K(k) is the inverse of the uniform tick-edge response.
- Continuum normalisation: the static metric diag(-(1+2Φ), (1-2Ψ)δ_ij) in sympy's expansion of √(-g) R. This is the supplied Regge limit.

## Results

### Finite diagnostics (lattice, every edge responding)

1. **The Newtonian kernel is exactly the nearest-neighbour Laplacian (A1).** K(k) = -2κ · 4 Σ_i sin²(k_i/2) / τ.
   - On all 511 nonzero momenta of the 8³ torus it holds to 2e-10.
   - On 164 irreducible-wedge momenta of 16³ it holds to 5e-10.
   - The face diagonals do not appear in it. No closed form is derived here.
2. **Independent of the free tick/edge ratio and of the carrier (A2).**
   - At τ = 0.7, K = -2 lap / τ. In Φ = δN/τ this is -2 lap per proper 4-volume, the same G.
   - On the Freudenthal (Kuhn) carrier, K = -2 lap.
   - Both hold to 7e-8.
3. **Isotropy (A3).**

   | | (100) | (110) | (111) |
   |---|---|---|---|
   | K/(-2\|k\|²) at \|k\| = 0.02 | 0.999967 | 0.999983 | 0.999989 |
   | at \|k\| = 2π/16 | 0.98721 | 0.99359 | 0.99572 |

   - The direction dependence is exactly the Laplacian's, 1 - (ka)² Σ k̂⁴/12 + ... The (111)-(100) spread at 2π/16 is 0.00851, against a leading k²/18 = 0.00857.
   - On the torus momenta 2πn/L with n = (100), (110), (111), the three values coincide at each L: 0.94964 (L = 8), 0.97736 (L = 12) and 0.98721 (L = 16). This is because every nonzero component equals 2π/L.
   - The tensor sector is already isotropic at long wavelength: sinh(E/2) = τ [Σ sin²(k_i/2)]^{1/2} (tick-fraction-waves B6).
4. **Which area enters (B1).**
   - Count area on the six-edge carrier: the edges crossed per Euclidean area are 3.000, 3.536 and 3.464 for (100), (110) and (111), a max/min of 1.179. Axis edges alone give 1, 1.414 and 1.732.
   - The hinge sum instead uses each hinge's Heron area, computed from the edges' own lengths. The carrier's (100) hinges tile the unit area to 1e-12.
   - The response built from these areas is the isotropic Laplacian (item 3).
   - So the count reading of area is not the area the adopted hinge sum uses. The count-area exclusion (17-48%, geometry-as-count) does not apply to the adopted rule.
   - What remains of that note's anisotropy is the sea's entanglement per Euclidean area (17%). That belongs to the vacuum, which the vacuum standard subtracts; it is not G (item 8).

### Theorems (exact)

5. **Normalisation, G_N = 1/(8πκ) (A4, sympy, given the supplied Regge limit and the Euclidean-static equality of √g R).**
   - The static Euler-Lagrange equation for Ψ is -4 lap(Ψ - Φ) = 0, so Ψ = Φ (γ = 1).
   - The reduced equation is E_Φ = 4 lap Φ.
   - The hinge sum is κ Σ A δ = (κ/2) ∫ √g R. Its reduced kernel is K_Φ = -2κ|k|², which is the lattice's -2 at κ = 1.
   - Hence 1/(16πG) = κ/2, so G = 1/(8πκ), and lap Φ = 4πG ρ.
6. **One G in entropy (C1).**
   - Replica trick on the same hinge sum: ln Z_n = 2πκ A (1 - n) - n I_1.
   - S = (1 - n ∂_n) ln Z_n at n = 1, which gives 2πκ A = A/(4G) with the G of item 5.
   - So the Jacobson/Wald entropy and the Newtonian coupling come from one κ. The area is again the hinges' Heron area.
7. **κ is the hinge sum's only number (C2).**
   - The hinge sum is homogeneous of degree 2 in the edges, so its Hessian is unit-free. Scaling a random 4-simplex by 3 changes it by 8e-12, and Heron's Hessian by 3e-16.
   - Neither the register size s, nor the register step, nor the block size b_e enters.
   - So 8πG = u²/κ in whatever unit u the edges are counted.
   - The edge register's zero-point scale (cell stiffness L²/(8πGħ) = 1 in the register) is κ restated. It is not a second determination of G.

### The Sakharov route on the adopted content (C3, toy) and the comparison (C4, supplied)

8. **Toy: 10-site ring, 5 fermions, hops e^{-h_i} (a supplied edge reading).**
   - The raw vacuum energy responds to an edge modulation with d²E0/dh² = -3.5777 per species (-7.1554 for two). An induced 1/G would therefore scale with content.
   - A fixed flat reference leaves -0.3416.
   - The vacuum standard's same-edge reference leaves 5e-15 at five random edge sets.
   - So under the adopted CL-3 the Sakharov term is removed whole, and G does not depend on matter content. This agrees with induced-G, which did the exact 252-configuration Fock version; this toy only re-derives the identity.
   - It also agrees with induced-response: the sea's induced static scalar sector has no Newtonian part at all, so it could not have supplied one G.
9. **Entanglement against induced (supplied lattice numbers).**

   | route, per Dirac | value | ratio to entanglement |
   |---|---|---|
   | entanglement (geometry-as-count) | 0.0983 | 1 |
   | induced 4π c_G, staggered (induced-couplings) | 0.0624 | 0.635 |
   | induced 4π c_G, Wilson (induced-couplings) | 0.1297 | 1.319 |

   - So there is no lattice identity between the two routes.
   - In the continuum they pair (Susskind-Uglum; Kabat), with contact-term ambiguities for gauge fields. This is cited as supplied.
   - Under the vacuum standard both are vacuum shares on the same edges. The induced action is subtracted (item 8), and its paired entanglement is matter entropy in the generalised entropy, not a second G.
   - The hinge's 1/(4G) is 2πκ per u², which is π/2 per site² on the cell-rung reading or 2π on the site reading.
   - Treating the sea's entanglement as the horizon entropy would give a G 8 times (cell rung) or 32 times (site) the hinge G. That is a reading the adopted rules do not use. The entanglement is also blind to the conformal mode (g-from-entanglement), so it cannot carry gravity.

## Estimates against measurement

- Direction dependence of G at 1 AU, on blocks of at most 100 cells of 8.1e-35 m: (ka)²/18 = 6.4e-87. Preferred-location bounds are |ξ| < 3.9e-9 (Shao-Wex 2013, supplied). Passes by about 78 orders.
- Tensor and Newtonian couplings: G_T = G_N (tick-fraction-waves C3; Hulse-Taylor 1.06σ).
- The value of G: the measured G only sets the unit. There is no dimensionless test.

## Verdict

**(b): one free scale.**
- There is one G. It is isotropic at long wavelength and the same in Newton, in horizon entropy and in tensor waves. It does not depend on τ, on the carrier or on matter content.
- Its value is 8πG = u²/κ. The CL-3 text's κ = 1 names the cell rung u = √(8π) l_P, so ħc/u = 2.435e18 GeV, the reduced Planck mass.
- That is the approved scale_reference_primitive (one dimensionful reference, a^{-1} = M_Pl, read as the reduced Planck mass on the cell rung). It is not a derived number.
- The answer is not (a). The register does not set G: κ is the hinge sum's only number, and the edge-register zero-point scale follows from κ rather than fixing it.
- The answer is not (c). Under the adopted vacuum standard neither sea route is a G, so the two O(1)-different sea coefficients are not two values of G.
- κ = 1 would carry dimensionless content only if the rules predicted some other lattice-scale observable in Planck units, for example ρ* = 3/(4πG l²) or the lattice dispersion (ka)²/24. None is measured.

## Gate

- No new rule is proposed. The adopted rules are tested.
  - (1) No measured number is chosen.
  - (2) No structure is inserted.
  - (3) Predictions it was not built for:
    - the exact Laplacian kernel;
    - no τ, carrier or content dependence of G;
    - an entropy G equal to the Newtonian G.
  - (4) No axiom is bent.

## Smuggling review

Supplied:
- the Regge limit (κ/2)∫√g R, and the equality of static Euclidean and Lorentzian √g R;
- the record coupling -m dτ to the tick edge;
- the replica construction (a conical deficit 2π(1-n) on the hinges);
- the toy's hop reading e^{-h};
- the continuum Susskind-Uglum/Kabat pairing;
- the lattice values of η and c_G from geometry-as-count and induced-couplings;
- the cell-rung reading of u (unit-map);
- the preferred-location bound.

Forced, given those:
- the kernel's exact Laplacian form and its isotropy;
- G = 1/(8πκ) and its independence of τ, carrier, s and b_e;
- S = A/(4G) with the same G;
- the vacuum standard's whole removal of the induced term.

Runner history: the first run had 2 FAILs, both criterion bugs and not physics.
- A3 compared against the leading-order k²/12 term where the pre-set intent was "the Laplacian's anisotropy". The exact Laplacian ratio is now used, and the leading-order value is printed.
- C6 tested a float for equality with 0. It now uses a 1e-12 tolerance.

## Boundary

Not claimed:
- linear static order is the only order computed: there is no nonlinear Newtonian or post-Newtonian G;
- the Euclidean lattice with the supplied static equivalence;
- no register-level (quantum edge) dressing of the kernel;
- the edges' own unsubtracted zero-point loops, dG/G = C W4/b_e², are not evaluated (induced-G: |C| <~10, so <= 1.5e-2 at b_e = 10);
- no derivation of the lattice Laplacian closed form;
- no generalised-second-law test with the sea's entanglement as matter entropy;
- no physical identification beyond the unit map.

## Uses / narrows

- Uses:
  - tick-fraction-waves (carrier, code, and B6/C3 for tensor isotropy and G_T = G_N);
  - unit-map (κ = 1 ⇔ u = √(8π) l_P; the update law is unit-free);
  - induced-G (vacuum standard removes the induced edge action; edge loops);
  - induced-response (no induced Newtonian part);
  - induced-couplings (c_G);
  - g-from-entanglement (η, conformal blindness);
  - geometry-as-count (η per Dirac, count-area anisotropy).
- Narrows geometry-as-count: its 17-48% exclusion and its Sakharov/entanglement mismatch apply to the count reading and to the subtracted sea, not to the adopted hinge-sum G.
- Narrows the register's "Open: the count value of G" in the tick-fraction clause to: G is the hinge sum's single scale, set by the units primitive. The count value is not G under the vacuum standard.
- Consistent with the main notes SCALE_REFERENCE_PRIMITIVE_NOTE (units only; a/l_P = 1 not derived) and UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17. The latter's induced G = 3π/(N_f Λ²) is a supplied-regulator coefficient, which the adopted vacuum standard removes. It is not contradicted as mathematics, but under the adopted rules it is not the gravitational G.

## How to run

```
python3 scripts/one_g_the_hinge_sums_newtonian_kernel_is_exactly_the_lattice_laplacian_isotropic_at_long_wavelength_with_one_free_scale_2026_10_23.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 12 s with about 97 MB peak resident, prints about 3.7 kB, is seeded (20261023) and ends with `TOTAL: PASS=11 FAIL=0`.
