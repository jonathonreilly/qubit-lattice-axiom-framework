---
claim_id: d4_time_blind_events_kill_dimension_six_liv_for_scalar_fermion_photon_but_the_slicing_decides_locality_and_sign_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "Supplied free models on the D4 event lattice with one factor per nearest pair, the same for all 24 root directions. (T) Aut(D4) = W(F4) (1152 built by closure). sum_r (r.p)^4 = 12 (p^2)^2 exactly, and the scalar kernel is K = 6p^2 - (p^2)^2/2 + (p^2)^3/36 - J6/90 + O(p^8), with J6 = sum p_i^6 + 15 sum_(i<j<k) p_i^2 p_j^2 p_k^2. The naive Dirac vector is O(4)-covariant through p^3 and first breaks at p^5. (F) Reynolds counts over W(F4): the gauge-invariant photon kernels are 1 at p^2 and 1 at p^4 (the O(4) one; also for the 576 rotations). For the graviton: 1 at p^2 (Einstein), but 3 at p^4 against O(4)'s 2; the extra one is birefringent on shell. On-shell (p0 = iE) dispersion: no k^2 term in v - 1 (|coeff| < 5.4e-9) for the scalar, the overlap fermion and both triangle-plaquette photon polarisations. All share one dim-8 pattern p^2 = kappa J6, with kappa = 1/540, 1/90, 1/1440 (ratios 1 : 6 : 3/8; b_e = 16 b_gamma). The naive operator has 72 nondegenerate zeros (chirality sum 0). The Wilson term lifts all 71 doublers (smallest mass 2), and the overlap at m0 = 1 obeys GW to 1.3e-15 with D = 2 at every doubler. Site-reflection positivity holds for time along an axis and along a root (a control fails). Axis slicing: cosh E = (6 - sigma2 + m^2/4)/|sigma1| has E = infinity on the real surface sum cos k_i = 0, so H is not exponentially local; v - 1 = +(1/240, 4/810) k^4 (face, body), superluminal. Root slicing (events = the centre sites of the active cubes, c x half-tick = a): the analyticity strip is the mass shell (0.1224 vs m/sqrt6 = 0.1225); v - 1 = (-1.67e-2, -1.98e-2)(ka)^4, subluminal. (E) With E* = 1.217e18 GeV: axis e -> e gamma opens at 1.1e20 eV and p -> p gamma at >= 1.4e21 eV; root gamma -> e+e- opens at 1.9e20 eV; nuclei are stable to ~1e21 A eV. All are above every observed particle. Verdict (pre-registered rule): WORKS in the root slicing; the axis/site reading FAILS locality."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/d4_time_blind_events_kill_dimension_six_liv_for_scalar_fermion_photon_but_the_slicing_decides_locality_and_sign_2026_10_26.py
---

# D4 time-blind events: dimension-six LIV vanishes for scalar, fermion and photon; the slicing decides locality and sign

Runner: runner.py. TOTAL: PASS=17 FAIL=0 in 8.6 s, seeded, AUDIT_TIMEOUT_SEC = 120, 3.3 k characters, 254 MB peak.
Criteria were fixed before any computation (criteria_pre_run.txt). The runner was re-run under a unique filename and gave identical output.

Labels: [T] exact, [F] finite diagnostic in a supplied model, [E] estimate against measurement, [S] reading.
The axioms are unchanged, CL is not edited, and nothing is adopted.

Pre-run deviations, stated:
- C2b pre-registered "count zeros". The count, 72, is far above the 16 I expected. It is reported as found.
- C5b's first-written text claimed both collinear processes were closed in the root slicing. A kinematic recheck showed that gamma -> e+e- opens at an asymmetric split. The check was rewritten to compute that threshold, 1.9e20 eV.
- RP memory: the brief asks for < 300 MB. The first version peaked at 568 MB, so the Reynolds step was rewritten (randomised range plus a square solve) to 254 MB. The results are unchanged.

## Builds on, uses, contradicts
- agents/lorentz-new-approaches (menu P1 + check.py).
  - CONFIRMED: quartic isotropy (5-design), and dimension 8 as the first LIV for the scalar.
  - REPRODUCED: the axis-slicing numbers +4.2e-3 (face) and +4.9e-3 (body). Exactly, they are 1/240 and 4/810.
  - NARROWED, three ways:
    - (a) "No dim-6 LIV in any sector" is a symmetry theorem for spin 0, 1/2 and 1. It is NOT one for spin 2: W(F4) admits one extra curvature-squared invariant.
    - (b) "The real-time step is exponentially local" is FALSE in the axis slicing the menu used. It is TRUE in the root slicing.
    - (c) "Same pattern for every species up to coefficient" is CONFIRMED, with coefficients 1 : 6 : 3/8.
- agents/zoom-fixed-point-tick: its open item, an unprotected radiative dim-6 coefficient C (needed < 5.5e-5), is CLOSED here by symmetry for spin <= 1, to all orders.
  - Fermion: by Solomon's theorem, the W(F4) vector covariants have degrees 1, 5, 7, 11, so there is no cubic covariant beyond p^2 p. Lambda^2 covariants start at degree 6.
  - Photon: counted (C3a).
  - So no dressed condition is needed.
- agents/nuclear-vacuum-breakup: its minimal rescue ("leading correction vanishes at p^4 for every species") is delivered by an exact symmetry rather than a tuned tick. The walls move to about 1e21 A eV.
- main, docs/SCALE_LADDER_GRAVITY_D4_CONE_FERMION_CONE_REFLECTION_POSITIVITY_CURVATURE_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-18.md and ..._COMMON_CONE_SPINS_ZERO_ONE_TWO_... (landed).
  - Their D4 = Z^4 u (Z^4 + u/2) is D4*, which is similar to our D4. Their time index is a hypercubic axis of D4*, which is a ROOT direction of our D4.
  - So their carrier is our root slicing (the cube-centre reading). It is consistent: there, the scalar is RP with lumped (nearest-neighbour) mass, and the fermion cones are O(k^4)-clean.
  - Their carrier is a B4 finite-element (Whitney/Regge) complex, not the 24-alike weight. Nothing there is contradicted.
  - Their curvature-squared term is the place where our extra W(F4) R^2 invariant (C3b) would enter.
- main, scripts/quartet_metric_check_2026_09_15.py uses the exact 24-cell 4th moment. Consistent.
- The main "ADMISSIBILITY_D4_*" notes use D4 as an unrelated label.
- Literature, supplied: Solomon (1963) for covariants of reflection groups; W(F4) invariant degrees 2, 6, 8, 12; Osterwalder-Schrader; Ginsparg-Wilson / Neuberger; Jacobson-Liberati-Mattingly vacuum Cherenkov kinematics (re-derived inline).

## Theorems and exact facts
- [T] C0. Aut(D4) = W(F4), of order 1152. It is generated by W(B4) and the reflection in (1,1,1,1)/2.
- [T] C1 (sympy).
  - sum_r (r.p)^2 = 12 p^2 and sum_r (r.p)^4 = 12 (p^2)^2.
  - sum_r (r.p)^6 = 20 (p^2)^3 - 8 J6.
  - K(p) = sum_r (1 - cos r.p) = 6p^2 - (p^2)^2/2 + (p^2)^3/36 - J6/90 + O(p^8).
- [T] C2a. s_mu = sum_r r_mu sin(r.p) = 4 sin p_mu sum_(nu != mu) cos p_nu = 12 p_mu - 2 p^2 p_mu + d_mu S6/720 + ...
- [T] Hence the on-shell condition of every W(F4)-symmetric free field is p^2 = kappa J6 + O(p^8). There is no (p^2)^2 effect on shell, and the first LIV is at dimension 8. The overlap's poles satisfy s(p)^2 = 0 on its physical branch.
- [T] Exact axis-slicing band. cosh E = (6 - sigma2 + m^2/4)/|sigma1|, where sigma1 = sum cos k_i and sigma2 = sum_(i<j) cos k_i cos k_j.
- [T] Root slicing (k = 0): 4z^2 + 16z - 20 = 0 gives z = 1 and z = -5. So there is a heavy staggered time mode at E2 = arccosh 5 = 2.29 hbar/a, with positive weight (site-RP). This was computed by hand and is not in the runner.

## Finite diagnostics
- [F] C2b. The naive D4 Dirac operator has 72 zeros mod 2 pi D4*: 8 of class |A| = 0, 24 of class 2, 32 of class 3 (cos = +-1/2 points) and 8 of class 4. All are nondegenerate (|det J| >= 256), and the chirality sum is 0. A random search found no zeros off the grid.
- [F] C2c-d. The Wilson masses wK/12 at the doublers are 2, 9/4, 7/3 and 8/3, so the overlap window is 0 < m0 < 2. At m0 = 1 the GW residual is 1.3e-15, D(0) = 0, and D = 2 at all 71 doublers: one Dirac cone.
- [F] C3a. W(F4) gauge-invariant photon kernels:
  - at p^2: 1, which is F^2;
  - at p^4: 3 invariant, of which 1 is gauge-invariant, and that one is O(4);
  - the same holds for the rotation subgroup (chiral matter).
  - So dim-6 photon LIV is forbidden to all orders.
- [F] C3b. Graviton:
  - at p^2, one diffeo-invariant kernel (Einstein): one metric for spin 2 at dimension 4;
  - at p^4, 3 against O(4)'s 2;
  - on shell the extra one is birefringent (plus = -cross) and vanishes along the body diagonals. Its coefficient in a D4 Regge action is uncomputed.
- [F] C3c. Triangle plaquettes, the smallest D4 loops: 32 per site (192 ordered). The gauge mode is exact. The 8 extra link modes (12 links against 4 components) are heavy: 72 against Z = 24, i.e. m^2 = 3 in D4 units.
- [F] C2e, C3d, C3e. The axis-slicing v - 1 coefficient of k^4 in each direction:

  | direction | scalar | fermion | photon (both polarisations) | -J6/1080 |
  |---|---|---|---|---|
  | axis | 0 | 0 | 0 | 0 |
  | face | 4.17e-3 | 2.50e-2 | 1.56e-3 | 4.17e-3 |
  | body | 4.94e-3 | 2.96e-2 | 1.85e-3 | 4.94e-3 |

  - Sphere average (scalar): 1/315 = 3.17e-3 (exact from the sphere moments). This is the isotropic, boost-like part, and it is nonzero.
- [F] C4a. Site-reflection Hankel test (N_t = 24, m^2 = 0.09): minimum relative eigenvalue -1.4e-16 (axis) and -9e-17 (root). The control, an antiferro two-step coupling, gives -0.15. Link reflection is not a lattice symmetry of either slicing (axis: t -> 1 - t swaps the parity; root: it maps D4 to D4 + r/2). So T is not positive; T^2 is.
- [F] C4b-c. Root slicing, in units of (k a)^4 with a the site spacing:
  - axis (slice-lattice) 0, face -1.67e-2, body -1.98e-2, generic -1.58e-2;
  - sphere average -1.27e-2;
  - fermion x 6 and photon x 3/8, as before.
  - The sign flips with the slicing (a slicing dependence the menu predicted).
- [F] C4d. Axis slicing: sigma1 = 0 at real k = (pi/2, pi/2, pi/2), so E = infinity on a real surface and the strip is 0. The reconstructed H is unbounded on a real-momentum surface, and e^(-iH) is not exponentially local. Root slicing: the nearest singularity is the mass-shell branch point (0.1224 against m/sqrt6 = 0.1225). The leading two-slice coupling (the same cube at t +- 2) is a constant 2, so there is no lattice singularity nearer.

## Estimates against measurement [E]
E* = 1.217e18 GeV = hbar c / a. Free coefficients; the proton is treated as an elementary fermion, which gives an upper bound on its LIV.

| process | threshold | observed |
|---|---|---|
| axis slicing (superluminal), e -> e gamma | p_th = (m^2 E*^4 / (10 b_e))^(1/6) = 1.1e20 eV (body) | electrons ~1e13-1e15 eV |
| axis slicing (superluminal), p -> p gamma | 1.4e21 eV | UHECR 3e20 eV, Amaterasu 2.4e20 eV |
| root slicing (subluminal), gamma -> e+e- | 1.9e20 eV (body) | LHAASO 1.4e15 eV |

- Axis slicing:
  - gamma -> e+e- is closed: b_gamma = b_e/16 exactly, so the symmetric split is exactly marginal.
  - Superluminal dim-8 stabilises nuclei (the parent note's concavity).
- Root slicing:
  - e -> e gamma is closed.
  - gamma -> e+e- opens only at an asymmetric split (max_x x(1-x)[16(x^5 + (1-x)^5) - 1] = 0.79).
  - Nuclei are stable to P_inst/A ~ 9.9e20 eV (parent formula).
- Both slicings: time of flight is unmeasurable. GZK photopion is unchanged: the shift at 1e20 eV is about 3e-8 GeV^2, far below m_pi m_p. Graviton dim-6, if present, is (E_GW/E*)^2 ~ 1e-62.

## What must be rebuilt
1. CL-1's cube tick becomes a D4 history weight, with real time from the OS transfer over two half-ticks. The cadence/tick-fraction constant disappears (c dt = a is forced). Whether the adopted tick-fraction response clause survives as geometry (lapse from the edges) needs checking.
2. Fermions:
   - The naive weight has 72 zeros. The cube walk's 16-taste structure, and the copy sign/copy mass that picks one light copy, do not carry over.
   - The overlap on the D4 Wilson kernel replaces them (GW exact, one cone). The register's history-level overlap clause is reused.
   - Fermion RP on D4 is UNTESTED: the time-crossing hop w - i gamma.r is a projector only when w|r| = 1.
   - The domain-wall slab D4 x Z keeps W(F4) (the fifth direction is orthogonal). UNTESTED.
3. Links. Triangle plaquettes; 8 heavy link vectors per site at the cutoff need a reading, or the links must be reduced.
4. Gravity. Regge/hinge sums on the D4 Delaunay complex, which can build on the main D4-cone carrier. Its p^4 term must not pick the extra W(F4) invariant, or it carries harmless dim-6 GW birefringence.
5. Records. The arrow breaks W(F4) in the STATE. The induced LIV, proportional to the record density, is uncomputed.
6. The rule must name the slicing: time along a root, which is the cube-centre reading. The site-parity reading is non-local.

## Simplification ledger
- Deleted (4):
  - the cadence constant (CFL forced to 1);
  - the dressed-cone clause: one metric at dimension 4 for spins 0, 1/2, 1 and 2 is forced to all orders, which also solves CPS;
  - the proposed dim-6 dressed-zoom clause, for spin <= 1;
  - the repaired kernel / m0 window of the cube walk.
- Added (2): the "24 alike" weight clause and the slicing clause. The overlap clause is reused.
- Changed: the copy sign is to be rebuilt.
- Net: about -2 clauses.

## Verdict (pre-registered rule): WORKS in the root (cube-centre) slicing; the axis (site-parity) reading FAILS exponential locality
- C1, C2, C3 (H3 true for the photon), C4 (RP, no dim-6, exponentially local in the root slicing, whose slices are 2Z^3 subsets of the sites) and C5 all pass.
- Caveats that keep this short of adoption:
  - fermion RP is untested;
  - the spin-2 dim-6 invariant is allowed;
  - the record-state LIV is uncomputed;
  - the copy-sign / family structure must be rebuilt.

Proposed CL text (UNTESTED, not adopted): "Events are the centre sites of the active tiling's cubes, one half-tick apart with c x half-tick = a; they form the D4 lattice. A history's odds are a product of one local factor per pair of nearest events, the same for all 24 nearest directions; matter is weighted by the overlap of the 24-direction Wilson kernel and links by their triangle loops. Records grow along a root of D4 (the direction in which a site's cube recurs), and the real-time step is the Osterwalder-Schrader transfer over two half-ticks."

Gate:
- (1) No fitted number. c dt = a, kappa and the ratios are forced; w = 1 and m0 = 1 are inert choices inside forced windows.
- (2) No observed structure is named.
- (3) Untested predictions:
  - no dim-6 LIV for spin <= 1;
  - a subluminal dim-8 pattern proportional to J6, zero along the slice axes, with species ratios 1 : 6 : 3/8;
  - gamma -> e+e- above ~2e20 eV;
  - a heavy staggered time mode at 2.29 hbar/a;
  - 8 heavy link vectors;
  - allowed graviton dim-6 birefringence.
- (4) It bends CL-1 (tick -> D4 history weight + OS transfer). The Z^3 axiom is kept, since events are a subset of the sites. The step is exponentially local, which the owner allowed on 2026-10-23.
- PASS.

## Smuggling review
- Forced or exact: W(F4); the expansions; the invariant counts; the J6 pattern; kappa; the exact band formulas; the zero count; GW.
- Supplied:
  - free Gaussian/fermion models;
  - triangle plaquettes as the link action;
  - Wilson w = 1 and m0 = 1;
  - the overlap construction;
  - E* = hbar c / a;
  - the parent nuclear formula;
  - observed values (LHAASO, TA, Auger, electron spectra).
- Nothing is fitted.

## Open
- Fermion RP on D4 (the projector condition).
- The coefficient of the W(F4)-only R^2 term in a D4 Regge action.
- Record-state LIV.
- Copy sign and families on D4 (72 zeros: does the family structure live there?).
- Gauged index with the D4 overlap.
- Reading of the heavy link vectors and of the staggered time mode.
