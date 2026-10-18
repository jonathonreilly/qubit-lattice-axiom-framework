# Findings log: gravity on the scale ladder (supplied models; finite floating-point checks)

## F1 (M1). Symmetry census of two-derivative quadratic forms (scratch/census.py)
Gauge-invariant forms under each group (invariant forms in parentheses):

| field | B4 | B4+ | K48 = S4 x inversion (the Kuhn complex) | OhT | OT | K12T |
|---|---|---|---|---|---|---|
| scalar k^2 | 1 | 1 | **2** | 2 | 2 | 3 |
| spin-1 | 1 (3) | 1 (3) | **2** (9) | 2 (7) | 2 (7) | 4 (15) |
| spin-2 | 1 (9) | 1 (9) | **2** (38) | 2 (26) | 2 (26) | 3 (67) |
| spin-2 mass | 0 (3) | 0 (3) | 0 (7) | 0 (6) | 0 (6) | 0 (11) |

So the complex's own symmetry plus linearised diffeo does NOT single out EH. A second form exists.

## F2 (M2). Metric universality of the Regge leading symbol (scratch/regge_project.py)
- The K48 gauge-invariant spin-2 pair is spanned by linearised EH of K48-invariant flat metrics
  g0 = delta + b u u^T, with u = (1,1,1,1). EH_g0 lies in the span (residual 1e-14) and is not
  proportional to EH_delta (misfit 0.42 at b = 0.3).
- Lengths l^2 = v^T g0 v give a Regge O(k^2) symbol of exactly -(1/4) sqrt(det g0) EH_g0:
  coefficients -0.250000, -0.370810 and -0.158114 at b = 0, 0.3, -0.15, matching -sqrt(1+4b)/4,
  with misfit <= 1.2e-7 (Richardson).
- So the graviton's leading form and cone are those of the edge-length metric. This is metric
  universality, not lattice symmetry.

## F3 (M3). A common cone at leading order (scratch/fem.py)
On the same complex, with the same g0 (b = 0 and 0.3), both fields match their continuum forms
to 1e-8:
- P1 (Whitney 0-form) scalar: leading symbol = sqrt(g) k g0^-1 k exactly (ratio 1.000000000).
- Whitney 1-form Maxwell: leading symbol = sqrt(g) x continuum F^2/2.

## F4 (M3). O(k^4) fingerprints at b = 0, by exact Schur elimination of lattice-only edge modes (scratch/onshell.py)
Write omega^2 = k^2 (1 + alpha k^2).
- Regge TT: alpha = -(1 + sum n^4)/12 for both polarisations (reproduces the OK4 note by an
  independent method).
- P1 scalar: the same law, exactly.
- Whitney Maxwell: birefringent and S4-only. Axis gives -0.1027 and -0.0859; face+ gives
  -0.0707 and -0.0665, against -0.0820 and -0.0636 for face-.

## F5. The exact lattice shell at b = 0 (scratch/exact_shell.py)
- On sum_mu 4 sin^2(p_mu/2) = 0 (the P1 scalar's exact shell, which is the hypercubic NN
  Laplacian's), the Regge 15x15 edge form has 7 machine-zero singular values (<= 1.4e-16),
  against 5 off shell (4 gauge plus the fifth branch).
- So both graviton polarisations propagate with exactly the scalar lattice dispersion at every
  sampled momentum (k up to 1.5; axis, face, body and generic directions).
- Whitney Maxwell does not: its 2nd and 3rd singular values are about 1e-4 there.
- At b != 0 (scratch/exact_b.py) the coincidence fails beyond leading order, and the fifth zero
  mode lifts. The all-orders match is special to the hypercubic edge metric.

## Phase 2 (after PR #9708 opened)
- F6. The pullback and the full form are different objects. The line-map pullback Q_h = M^T Q M is
  -(1/4) sqrt(det g0) EH_g0 at every b. With the non-metric edges eliminated (Schur), the full form
  matches it only at b != 0: at b = 0.3 and 0.05 the misfit is 1e-6. At b = 0 the eliminated block has
  an eigenvalue falling as k^2, so the reduction is singular (schur2.py, schur3.py). The first PR
  version stated C3 without this distinction; it was corrected in the second commit.
- F7. The fifth null direction (fifth*.py):
  - present on every diagonal background tested (a stretched tick keeps it);
  - lifted linearly in b, with singular value about 66 b;
  - modulo gauge, its metric part is EXACTLY u u^T - 2*1 (cosine 1 - 1e-8).
- F8. On-shell P1 stress sources the fifth direction at a fixed 9-23% of its norm, at every momentum
  scale. Conserved continuum stresses through the line map do too (12%, 19%). Linear response in the
  15-edge carrier at b = 0 is therefore ill-posed in that channel.
- F9. Newtonian rung of the pullback: h_tt k^2 -> -2 isotropically (continuum -EH/4); on the axis the
  response is exactly -2/(4 sin^2(k/2)) at all k (newton2.py).
- F10. The pullback at O(k^4) is birefringent: axis -1/9 and -2/9, face -1/9 and -0.194, body -0.148
  doubly. This reproduces the OK4 F10 values. The pullback is also off the Hodge shell (qh_k4.py).
- F11. Cubical complex (cubical.py), standard facts:
  - d d* + d* d = phat^2 I on all 16 components;
  - the fine-lattice Kahler-Dirac operator d - d* squares to -Delta, with no doublers;
  - cubical Maxwell sits on the shell exactly;
  - the P1 scalar on Kuhn equals the NN Laplacian (4e-15);
  - naive/staggered fermions have the shell at doubled momentum, so the 2a rung.
  The repo's own DK carrier uses the sin^2 k shell (reader digest).
- F12. Regge nullity 7 holds on 25 random COMPLEX points of the variety sum 4 sin^2(p/2) = 0
  (variety.py).
- TENSION (K48 family): a real spectrum needs b = 0, but at b = 0 there is a matter-sourced flat
  direction. The pullback is free of it but birefringent at O(k^4). Next: a B4-symmetric
  triangulation (barycentric subdivision of the cubical complex).

## Phase 3 (PR #9714)
- F13. The Kuhn fifth null vector is NOT flat: D x != 0 (|Dx|/|D| ~ 0.6), while the deficit-map
  rank is E - 4. It is curvature the quadratic action Q = A'^T D does not see.
- F14. Barycentric subdivision (B4 incl. tick reflection, 384 orthoschemes, 240 edges, 16 vertex
  types): nullity 64 + 16, and the extras are curved and metric-carrying (bary*.py, flatq.py).
- F15. Lifting the hidden direction: a body-diagonal tilt gives Re k_t/|k| -> 0.27 (non-real at
  leading order). A spatial skew c (1,1,1,0) gives Re k_t/|k| ~ k^2, and the full form is
  -(1/4) sqrt(det g0) EH_g0 (skew*.py).
- F16. D4 cone (d4*.py; regge_generic.d4cone): D4 = Z^4 u (Z^4 + u/2) plus deep holes; 16-cells
  coned. 96 simplices, B4-symmetric, no orthoschemes.
  - nullity = 32 vertex displacements only;
  - full-form symbol -(1/4) EH;
  - P1 scalar has real energies and NO on-shell k^4 term (W(F4) symmetry);
  - graviton has two real shells omega^2 = k^2 (1 -+ c k^2), each 1 metric + 1 non-metric mode;
  - c^2 = [(1 - S2)^2 - 12 T]/144 predicts 3 further directions within 0.4%;
  - 8 massless non-gauge directions (EH needs 6): 2 non-metric partners.
- F17. Matter on the D4 cone:
  - P1 on every vertex sources the relative vertex-type (optical) displacements at O(1), which
    is inconsistent;
  - the uniform part is O(k);
  - a site-cell metric read through the holes (d4m/d4q) is blind to non-site displacements;
  - a static T_tt source through it gives graviton -2 (h_xx = -h_tt) plus one CONFORMAL partner
    (pattern = identity) at -2/3, so the total h_xx/h_tt = -1/2: the Brans-Dicke omega = 0
    pattern (gamma = 1/2 if read as usual; excluded by solar-system tests).
- F18. A recurring direction: the Kuhn fifth direction's metric part is u u^T - 2*1, and the D4
  partner's site-metric reading is 2*1 - u u^T (orientation-biased L) or pure conformal
  (symmetric L). Both live in the conformal / body-diagonal sector.
- NEXT: a carrier with no non-metric soft modes, or a local term giving them mass without
  breaking the lattice diffeos; a site-matter Ward identity on D4; the mechanism of the Kuhn
  shell at b = 0.
- F19. The D4 partners are NON-METRIC STRAINS (d4s.py):
  - partner 0 appears only in the body diagonals, in the alternating pattern s0 s1 s2 s3, which
    is invisible to any quadratic reading;
  - partner 1 shrinks the axes and face diagonals while stretching the body diagonals.

  The partner coupling therefore depends on the matter's metric reading (d4t/d4u/d4v):
  - face reading (Lsym): -2/3 conformal;
  - uniform least squares on delta(l^2): -0.074;
  - RELATIVE-STRAIN least squares (weights 1/l^4) over all 24 segments: the partner reading is
    O(k) and the static response is EXACTLY linearised GR (h_tt k^2 = -2, h_xx = -h_tt), with
    partner exchange (a/w)^2.

  PR #9714 is now at PASS=18. Open: whether that reading follows from a principle; a site-matter
  Ward identity; light bending and the dynamical partner coupling.

## Phase 4 (PR #9772)
- F20. Kuhn control: the relative-strain least-squares metric reads the fifth zero-action direction at
  O(1) (|L f| 0.69-0.75), so the strain reading does not rescue Kuhn (kuhn_strain.py).
- F21. Whitney Maxwell on the D4 cone (d4_maxwell*.py, d4_k6.py):
  - nullity = 8 vertex gauge; leading = continuum;
  - 3 massless non-gauge directions (no partners);
  - both polarisations on one shell with NO O(k^4) term;
  - O(k^6) beta_photon = -beta_scalar/4, both zero on the axis, scalar beta ~5e-4.

  Cone hierarchy on the D4 cone: spins 0, 1, 2 share the leading cone; spins 0 and 1 also share
  it through k^4; the graviton splits at k^4 via its partners.

## Phase 4 (PR #9774; scratch/phase4/, imports the #9714 runner as r14)
- F20. Pseudo-inverse trap: two vertex-displacement eigenvalues of the finite-difference edge form are about 1e-9,
  above pinv(rcond=1e-11). Off the axes the sources overlap them at O(k^2), so plain-pinv exchanges blow up
  (lb2). Always invert on the exact complement of range(G) (common.Qinv). The static-axis numbers in G17 are
  unaffected, because the overlap there is exactly 0.
- F21. Light bending and non-static exchange through the strain metric (lb1, lb3, shell):
  - null/dust test ratio = 1.99998 (1 + gamma = 2);
  - lattice-conserved Euclidean exchange alpha = -4, beta = +2 in 5-6 directions including the tick
    (linearised-EH form); partner share O(k^2);
  - on the Lorentzian shells, the reading of the non-metric null modes is ~0.27 |k| times the metric ones.
- F22. Site scalar Ward identity (ward, wpos, wfit, wamp2):
  - the violation is O(k) relative for corner and cell-averaged gradients;
  - the cause is the reading: per-component registration points (h_mumu at 1/2, 1/8; h_munu at 1/2, 1/4) plus
    off-support O(q^2) gradient entries from mixing the least-squares segment midpoints;
  - the gauge dependence of the on-shell scalar-scalar exchange is O(k^2); the distance from the EH formula
    is O(k).
- F23. Weighting principle (w1, w2, w3):
  - beta = 2 - (2/3) rho^2 with rho = 4(w_a - w_b)/(4 w_a + 12 w_f + 8 w_b), exact over 8 weightings;
  - the EH form holds iff w_a = w_b, which is the fourth-moment isotropy of the weighted segment directions;
    the face weight is free;
  - the reading is NOT the Euclidean M^+ (misfit 0.65 / 0.22).
- F24. Next targets:
  - a segment-wise matter coupling (stress at the segment midpoints) and its Ward order;
  - whether anything fixes the face weight;
  - O(k^4) through the reading.

## Phase 5 (PR #9821) — owner asked for items 2-5
- F25 (fermion): Whitney Hodge Laplacians on the D4 cone (whitney.py, dk*.py) have 1, 4, 6, 4, 1
  massless modes at lambda = k^2 (16 Dirac-Kahler components, no doublers), with a gap >= 25 and
  no O(k^4) on-shell term in any degree. So spins 0, 1/2 and 1 share the cone through k^4.
- F26 (RP; rp*.py): the Gaussian OS test discriminates (NN passes; higher-derivative and
  consistent-mass P1 fail). The D4 P1 scalar with lumped mass and the Whitney 1-form with diagonal
  mass are RP at both tick planes. All 72 P1 couplings are ferromagnetic or zero.
  Not done: fermion RP (Grassmann); graviton (conformal mode unbounded).
- F27 (partners; r2*.py): lambda sum delta_h^2 with lambda = -0.1 lifts the Kuhn fifth direction
  and gaps the D4 partners, with no tachyons (lambda = +0.1 gives tachyons on Kuhn). The static
  response is then linearised GR for every reading tested on both complexes.
  Caution: the line-map source with a least-squares readout is an inconsistent pair (gave -0.33);
  use a consistent left-inverse reading.
- F28 (bridge; poisson.py): the D4 static response is Poisson at leading order (Newton
  coefficient, nu = 1) but not an exact lattice Poisson equation (O(k^2) corrections, about
  8-16% at |k| = 1). The record side (which record observable sources T_tt, how lengths are
  registered) needs owner decisions on the vacuum and formation; it is not derived here.

## Phase 6 (PR #9822): carrier census and the zoom-out reading
- F29. canon_tri.py builds choice-free carriers: Z^4 plus half-integer orbits, Delaunay cells, and
  every non-simplicial face coned from its circumcentre. Hidden/partner profiles of all 16
  (census_tri.log):
  - hidden curvature only for {} (1) and {1,2,3,4} (16, i.e. Z^4 at half spacing);
  - 2 partners on {2}, {4}, {1,3}, {2,3}, {2,4}, {1,3,4};
  - clean (neither): {1}, {3}, {1,2}, {1,4}, {3,4}, {1,2,3}, {1,2,4}, {2,3,4}.
- F30. The O(k^4) Hodge (Dirac-Kahler) cone is exact ONLY on the even sets {2}, {4}, {2,4}, all of
  which carry partners. Every other set tested splits, including all partner-free ones
  ({1,2,3} not computed).
- F31. Carrier {1} (link midpoints):
  - leading form -(1/4) EH;
  - Hodge counts 1, 4, 6, 4, 1, with O(k^4) splitting |alpha| 0.007-0.031 by component;
  - graviton alpha about -0.03 to -0.04, weakly split;
  - P1 RP holds;
  - linearised GR statics for ANY consistent block reading, with no R^2 term.
- F32. OWNER 2026-10-18: "you can test points between the sites, but not use them ... zoom out".
  - Zoom x2: {1}'s vertices are exactly all 16 sites of each 2^4 block, and the D4 cone's are the
    8 even sites; other sets need zoom 4 or 8.
  - So gravity is a 2-rung triangulation of the sites.
  - A P1 field on every site sources the relative sublattice displacements at O(1), so gravity
    reads matter per block.

## Phase 7: record-to-geometry explorations (owner: "explore both"; EXPLORATIONS, NOT POSITIONS)
- Q1 (owner 2026-10-18): points between sites may be tested, not used; zoom out. That gives the
  2-rung carrier (F32).
- F33 (A, record pace sets the time length; paceA.py, paceA2.py):
  - Under the linear nearest-neighbour averaging rule (the unapproved Q7 clarification), the
    stationary pace deficit falls as 1/r, isotropic to a few %, slower near records (the time
    dilation sign).
  - If records HOLD a fixed pace (Dirichlet), mass grows with cluster SIZE, like a conductor
    (1 site 0.165, 33 sites 0.94): not additive.
  - If records DRAIN a fixed amount q of pace (source), mass is exactly additive (per record
    0.00510 for N = 1, 19, 33), with isotropic 1/r.
  - With lapse = pace, the 2-rung Regge carrier fixes the spatial lengths with nu = 1
    (F31/K4), so the static weak-field chain closes at leading order.
  - Needs, all unadopted: the linear averaging rule, records as drains, and pace = time length.
- F34 (B, distance from linked possibilities; linkB.py): Gaussian NN field with precision
  (-Delta + m^2).
  - The correlation-decay distance is isotropic at long range: anisotropy 2% at xi = 1,
    0.03% at xi = 3.3, emergent like (a/xi)^2.
  - A record (conditioning one site) changes distances only within ~xi: exponential falloff,
    and faster than r^-4 even near criticality. NOT Newtonian.
  - So B can supply the background geometry (where things are) but not the gravitational
    response; A supplies the response.
- Next question for the owner (Q3): does every record drain the same pace (mass = record
  count), or does a record drain according to its content (e.g. its energy)?
- F35 (Q3, owner: "explore both"; EXPLORATION). Is gravity's source the record count, or content?
  Tested on the 2-rung carrier {1} with the block reading (sourceQ3c.py).
  - The block reading maps a uniform lattice displacement EXACTLY onto the continuum gauge.
  - A conserved source T = P e_t e_t P has a Ward residual of 1e-15 at |k| from 0.004 to 0.03.
  - A count source at a formation event (T_tt appearing with no current) has an O(1) residual at
    every scale. Gravity's linear equations then have no solution.
  - So "same drain per record" is fine for static records but inconsistent when records form,
    unless formation moves conserved content from unrecorded possibilities into the record. That
    is the content rule.
  - Static consequences (analytic):
    - count rule: mass = N q, so binding energy does not gravitate, and the global pace falls as
      records accumulate (no steady state);
    - content rule: binding energy gravitates and there is no secular drift.
    - Both give a frozen zero-pace region (owner's 'full region = black hole' instinct) once the
      deficit reaches 1: r_h ~ 0.5 q N in lattice units with the linear drain.
