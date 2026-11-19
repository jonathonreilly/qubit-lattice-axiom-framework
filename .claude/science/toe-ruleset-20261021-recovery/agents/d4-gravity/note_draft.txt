D4 event set sliced along a root: the hinge-sum gravity sector carries over at linear order, with a decoupled frame doublet and a 1e-80 graviton birefringence

Claim type: bounded_theorem (finite supplied-model numerics plus exact identities).
Runner: d4_event_set_root_sliced_hinge_sum_gravity_carry_over_2026_10_26 (16/16, 1.1 s, seeded; re-run identical).
Pre-registration: criteria_pre_run.txt (written before the first run).

VERDICT: PARTIAL (by the pre-registered rule). Everything the adopted gravity sector derives
carries over at linear order with no fitted number: one Einstein coefficient, two tensor waves on
the event cone, gamma = 1, one G, frame dragging. One pre-registered item was MISSED (G4, "only
metric modes are soft"): the D4 cone has two extra massless modes, the frame doublet, which are
degenerate in speed with the graviton and invisible to matter at the two-derivative level.

Carrier (supplied)
- Events: the D4 lattice. Hinges need simplices, so each Delaunay 16-cell is coned from its
  centre (the deep holes, i.e. the Voronoi 24-cell vertices). This is the W(F4)-symmetric "D4 cone"
  of main's #9714/#9772/#9774, here with the time-blind event law's time along a root.
- Per D4 cell: 48 4-simplices (3 hole types x 16 facets), 104 hinges, 36 edges (12 roots + 24
  spokes). The flat complex has every deficit 0 (to 2e-15).
- Root slicing, t = (1,1,0,0)/sqrt2. The 24 roots split 2/16/6:
  - the tick root spans two half-ticks; it is the site's tick fraction (lapse);
  - 16 pair-offset roots join each event to the 8 corners of its cube at the next half-tick;
  - 6 slice roots are the cube axes.
  Even slices sit on 2Z^3 and odd slices on 2Z^3 + (1,1,1). The root slicing IS the alternating
  two-tiling.

Theorems / exact identities
- [T] M1: each orthogonal root 4-frame satisfies sum (r.p)^2 = 4 p^2. So the frame doublet
  (rescaling the three frames by (a,b,c), a+b+c = 0) drops out of every W(F4) two-derivative matter
  term. It first enters at (r.p)^4, i.e. dimension 6, suppressed by (ka)^2.
- [T] M2: a uniform time stretch is a zero of the hinge sum, so the hinge sum leaves the
  tick/edge ratio free (as on the cubic carrier, B8 of tick-fraction-waves). "All 24 roots alike"
  fixes it (tick root = slice root), so the graviton cone is the event cone with no free tau.

Finite diagnostics (supplied model)
- G3: with every edge responding, the null space at generic k is vertex displacements only
  (nullity 16 = 4 vertex classes x 4; |QG|/|Q| 4e-12). There is no zero-action branch (contrast:
  the cubic Kuhn carrier has one).
- G4: the small-k spectrum has 16 exact zeros, 8 soft modes (x4 on halving k) and 12 cell-gapped
  modes (|eig| >= 16). The 8 soft modes are 6 metric + 2 frame-doublet modes. The doublet is flat
  at k = 0 and lives only on root edges (spokes fixed).
- R1: after integrating out the 12 gapped modes, the metric block is c times the linearised
  sqrt(g) R form, with c = 1.99970..1.99994 in all 6 directions (root, axis, generic).
  - Relative residual 5.2e-5 -> 1.3e-5 on halving k.
  - c = 2 is the D4 cell 4-volume. In cube-edge units that is 8, the same coefficient per unit
    4-volume as the cubic carrier, so G = 1/(8 pi kappa) carries over with the same kappa.
- R2: the frame doublet has its own kinetic term, -k^2 per unit norm (the sign of the tensor
  block, so not a ghost). Its mixing with the metric is O(k^3).
- R3/R4: the real-time root census along t at fixed spatial k finds 8 light roots:
  - 4 branches x (+-E): 2 tensor and 2 frame, |c - 1| <= 2.1e-4 at ka = .035;
  - each degenerate light pair is one pure metric mode plus one pure frame mode (frame share
    0.000 / 0.999);
  - everything else is cell-gapped (|E| >= 4.8).
  There is no scalar, vector or breathing metric mode.
- R5/R7: the graviton is birefringent at (ka)^2 (a = cube edge): c = 1 +- A(n) (ka)^2.
  - Angular law: A = (1/6) sqrt((1 - S)^2 - 12 P), with S = sum_{i<j} n_i^2 n_j^2 and
    P = n1^2 n2^2 n3^2 on the slice cube axes. A = 1/6 on an axis, 1/8 on a face diagonal and 0 on
    the body diagonal. The law was fitted on 5 directions and tested on 3 seeded random ones
    (misfit 1.4e-3).
  - The polarisation-averaged shift is zero (mean 7e-5, drift level). So the O(4)-type quartic
    terms give no on-shell shift, and the whole effect is the third, W(F4)-only quartic graviton
    term. Its size: splitting 2A = 1/3 (ka)^2 at most.
  - Contrast: matter and photons on D4 have dim-6 = 0 (#10094). The graviton is the one D4 field
    with a dim-6-like term, and it is pure birefringence.
- N1: a static point source gives gamma = 0.99999..1.00007 (gauge-invariant transverse spatial
  trace / h_tt) and a 1/k^2 potential.
- N2: G_N / G_T = 1.00010..1.00027.
- N3: frame dragging (the gravitomagnetic response to a transverse current) is 1.00002..1.00015
  of the continuum Lense-Thirring value.

Against measurement
- GW170817: the splitting at 100 Hz with the cell rung L = 8.1e-35 m is |dc| ~ 1e-80, against the
  bound 1e-15. The bound only needs L < 3e-2 m.
- GW birefringence and dispersion bounds pass by more than 60 orders.
- Hulse-Taylor follows from G_T = G_N (as on the cubic carrier).
- Frame doublet: it is sourced only through the O(k^3) mixing or dimension-6 matter terms, so its
  emitted power relative to the graviton's is ~(ka)^2 ~ 1e-80. Unthermalised, it has no N_eff
  effect (estimate).

Not tested
- beta = 1 (nonlinear): inherited only through the supplied Regge -> EH limit.
- Nordtvedt and alpha1 beyond linear order; the matter-side lapse reading in the D4
  zoom-fixed-point event weight; strong fields; the frame doublet's nonlinear couplings.

What changes vs the cubic two-tiling
Deleted:
- (i) CL-1's tick tie "sqrt3 N rms sqrt(gamma^ii) = sin eps0": replaced by "all 24 roots alike" (M2);
- (ii) the six-edge carrier choice and its Kuhn contrast;
- (iii) the special clause "tick fraction and pair offsets are response variables": automatic,
  since they are roots and every edge responds;
- (iv) "lapse in the step" is moot for the hinge sum. There is no step angle on D4; the lapse is
  the tick-root length.
Added:
- (a) hole vertices and their spokes (24 per cell) as edge registers, needed for simplicial hinges;
- (b) the frame doublet.
The tick-fraction / pair-tick-offset rule SURVIVES, as roots: the root slicing already alternates
the two tilings.

Proposed CL amendment (working, not adopted)
"On the D4 event set, the hinge sum is taken on the Delaunay 16-cells coned from their centres,
every edge responding. The tick fraction is the tick root and the pair offsets are the
half-tick roots."
Frame doublet, two options:
- (A) Accept it. Untested prediction: two massless strain waves, degenerate with the graviton,
  unsourced at dimension 4.
- (B) Remove it by a clause reading root registers through their cell metric (one more clause;
  not tested).
Net clause count about -2 under (A).

Smuggling gate
- No measured number chosen. The only scale is kappa, the approved reference.
- No observed structure named.
- Supplied: the coning (the hole vertices are not events); the line-integrated metric reading; the
  continuum sqrt(g) R form, used only as a comparator; the Regge -> EH limit for beta.
- Untested predictions: graviton birefringence 1/3 (ka)^2 with the stated angular law; the frame
  doublet.
- Bent clause: CL-1's tick tie (and, with the event law, CL-1's tick). Axioms unchanged.
- Gate: PASS for (A).

Cited
- Consistent with main's #9774: EH-form distance falling ~k^2 on the D4 cone (H11).
- Consistent with #9772: a common cone at k -> 0.
- Consistent with #9714: the D4 cone hides no curvature.
- Campaign PRs #10094 (time-blind D4) and #10098 (D4 zoom matter).
- Method reused from tick-fraction-waves and one-g.
