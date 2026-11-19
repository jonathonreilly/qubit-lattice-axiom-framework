---
claim_id: the_tick_offset_between_neighbours_answering_the_hinge_sum_drags_frames_with_the_lense_thirring_coefficient_so_ppn_alpha1_is_zero_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Stationary, slowly rotating source at first order in its angular momentum J, on a flat background, under the tick-fraction rule extended to the tick offset between neighbouring sites (the shift beta, one value per neighbour pair). Stationary means edges and offsets repeat every tick. The hinge sum over sheared prisms is taken in its supplied Regge limit (1/16 pi G) int sqrt(-g) R4. Exact (sympy): at second order in the offset, sqrt(-g) R4 has the same Euler-Lagrange equations as K_ij K^ij - K^2 with K_ij = -(d_i beta_j + d_j beta_i)/2, with coefficient one, the same hinge sum that gives the static (1/16 pi G) int N sqrt(h) R3. A record's phase per taken tick -m dtau carries +m v.beta at linear order. Stationarity in the offset then gives curl curl beta = -16 pi G rho v. A per-site offset (beta = grad f, a relabelling of tick counters) drops out identically. The equation is solvable only if the record current is conserved, and the curl of beta does not depend on the longitudinal weight. For a rotating ball the exterior is beta = -2G (J x x)/r^3, and the gyroscope precession -(1/2) curl beta = (G/r^3)[3(J.rhat)rhat - J], the Lense-Thirring form with the GR coefficient. A moving point source gets beta = -4 U w, which is the boosted static field iff gamma = 1. With tick-skip-gamma's gamma = 1 this gives PPN alpha1 = 0 and (4 gamma + 4 + alpha1)/8 = 1. A frozen offset, or a per-site offset only, gives no frame dragging and alpha1 = -8. Finite diagnostic: on an L = 14 periodic lattice with offsets on edges, the slip field is gauge-weight independent to 5e-12 and beta = -4 V to 6e-14; on an isolated (Lb = 96) loop it approaches the continuum field as about 1/r^2 (2.9% at r = 10). Not derived: the Regge limit of sheared prisms, the gyroscope readout, discretisation corrections, preferred-frame effects at lattice order, interiors, and second order in J."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_tick_offset_between_neighbours_answering_the_hinge_sum_drags_frames_with_the_lense_thirring_coefficient_so_ppn_alpha1_is_zero_2026_10_23.py
---

# The tick offset between neighbours answering the hinge sum drags frames with the Lense-Thirring coefficient, so PPN alpha1 is zero

Claim type: bounded_theorem.
Primary runner: `scripts/the_tick_offset_between_neighbours_answering_the_hinge_sum_drags_frames_with_the_lense_thirring_coefficient_so_ppn_alpha1_is_zero_2026_10_23.py` (22 PASS, 0 FAIL, ~21 s, ~200 MB peak).

## Question

The tick-fraction rule ("a site's tick fraction is a response variable: like the edges, it takes the value that makes the total phase stationary") forces gamma = 1 (tick-skip-gamma) and beta = 1 (tick-fraction-beta) for static sources. A rotating source is stationary but not static. Its prisms are sheared, because a site's tick lines up with a neighbour's tick at an offset. Does the rule fix that offset, and does it give frame dragging with the GR coefficient (PPN alpha1 = 0; Gravity Probe B Omega = (G/c^2 r^3)[3(J.rhat)rhat - J])? Neither the Kerr metric nor the GR momentum constraint is imported as the answer.

## Setup (rules used, rederived where used)

- Variables:
  - the site tick fraction N;
  - the spatial edges h;
  - the tick offset between neighbouring sites, beta.
- What "stationary" means here: every tick repeats the same edges and offsets, so the edges do not change between ticks.
- CL-3 response: one hinge sum, (1/8 pi G) sum_h A_h delta_h, with a single coefficient over every hinge.
  - Static prisms give (1/16 pi G) int N sqrt(h) R3 (tick-skip-gamma).
  - Sheared prisms add deficits at the spacelike hinges between successive slices. In the supplied Regge limit the whole sum is (1/16 pi G) int sqrt(-g) R4, with ds^2 = -N^2 dt^2 + |dx + beta dt|^2.
- Proposed extension (the rule-internal choice): the tick offset of each NEIGHBOUR PAIR is a response variable. It takes the value that makes the total phase stationary, as the tick fraction and the edges do.
- Source: a record's phase advances by -m dtau per taken tick, with dtau = sqrt(N^2 - |v + beta|^2) dt. This is the same record readout used for perihelion in tick-fraction-beta.
- Readout: gyroscope precession Omega = -(1/2) curl beta (the frame-dragging part; supplied).

## Results

### Theorems (exact, sympy)

1. **The shear hinges carry the static coefficient** (A0, A1). With N = 1 and flat edges, sqrt(-g) = 1 exactly. At second order in the offset, sqrt(-g) R4 and K_ij K^ij - K^2 (with K_ij = -(d_i beta_j + d_j beta_i)/2) have identical Euler-Lagrange equations. So the offset enters the hinge sum with coefficient one and the sign fixed relative to the static N sqrt(h) R3 part. Nothing is weighted separately.
2. **How the source's momentum couples** (B1). Expanding the record's phase per taken tick gives a linear term +m v.beta. A moving record crosses tilted timelike hinges, and the tilt shifts its proper time by v.beta per tick. So the matter action contains + int (rho v).beta: the momentum density couples to the offset through the same record flux that crosses the hinges.
3. **The offset equation** (C1). Stationarity in beta gives (1/16 pi G) curl curl beta + rho v = 0, that is, lap beta - grad div beta = 16 pi G rho v. This is derived from the rule's stationarity in the new variable; it is not imported as a constraint.
4. **A per-site offset is pure gauge** (C2, G1). If the offset is a difference of per-site tick counters, beta = grad f, the equation vanishes identically and the source term integrates to -int f div(rho v) = 0. Such an offset relabels ticks; it has no slip around a plaquette (d1 d0 = 0) and cannot drag frames. Frame dragging lives in the circulation of the offset around a loop of neighbours, so the offset must be a per-neighbour-pair quantity (composite before atomic: a pair, not a site).
5. **Consistency and gauge independence** (C3, G4). The divergence of the offset equation is div(rho v) + (lambda - 1) lap(div beta)/(8 pi G).
   - The equation is solvable only if the record current is conserved (stationary record flux).
   - With a different longitudinal weight (lambda != 1), the result is div beta = 0 and curl beta is unchanged.
   - Frame dragging therefore depends only on the coefficient of the transverse shear. The register's supplied shift wave law, whose stationary state at most fixes the gauge part, cannot change it.
6. **Lense-Thirring with the GR coefficient** (D1-D3). For a uniformly rotating ball, int rho x_k x_m = (I/2) delta_km, so the Coulomb solution beta = -4G int rho v/|x - x'| has exterior beta = -2G (J x x)/r^3. That field solves the source-free equation and is divergence-free. Then Omega = -(1/2) curl beta = (G/r^3)[3(J.rhat)rhat - J], exactly the GP-B/LAGEOS form.
7. **alpha1 = 0** (E1, E2).
   - A point source moving at w relative to the lattice gets beta = -4 U w from the same equation.
   - Boosting the static field (g00 = -(1 - 2U), g_ij = (1 + 2 gamma U) delta_ij) gives g0i = -2(1 + gamma) U w.
   - The two agree iff gamma = 1. In PPN form, alpha1 = 8 - 4(1 + gamma) = 4 - 4 gamma.
   - With gamma = 1 from tick-skip-gamma, derived independently, alpha1 = 0 and (4 gamma + 4 + alpha1)/8 = 1. The static hinges (the lapse and R3 coefficient) and the shear hinges (the K-terms) come from one hinge sum, and that shared origin is what makes them meet.

### Option table (F1)

| Rule-internal choice for the offset | Frame dragging / GR | alpha1 |
|---|---|---|
| per-pair offset responds, single hinge sum (c = 1) | 1 | 0 |
| offset frozen (beta = 0, every neighbour ticks in step) | 0 | -8 |
| per-site offset only (beta = grad f) | 0 | -8 |
| tilt hinges given a separate weight c | 1/c | 8/c - 8 |

### Finite diagnostics

- **L = 14 periodic cubic lattice**, with offsets on edges, slips on plaquettes and a 2x2 current loop:
  - d1 d0 = 0 exactly, and the loop current is conserved (G1, G2);
  - d1^T d1 beta = -16 pi G j solves to residual 5e-13 (G3);
  - the slip field curl beta agrees across gauge weights 1 and 3 and minres without gauge fixing to 5e-12 (G4);
  - beta_x = -4 V_x, with V the Newtonian-normalised lattice potential of the momentum density, to 6e-14 (G5). The factor 4 = 16 pi G / 4 pi G is the lattice form of the Lense-Thirring coefficient.
- **Isolated loop** (each component solved by FFT, Lb = 96, using G5): the lattice slip flux over the continuum Neumann integral of the same square loop is 1.154, 1.064 and 1.029 at r = 4, 7, 10, on both axis and equator. The grid error falls as about 1/r^2 (G6). The axis/equator ratio matches the continuum loop (-1.87 vs -1.87 at r = 10) and tends to the point-dipole value -2.

### Against measurement (test only)

- GP-B: rule ratio 1, i.e. 39.2 mas/yr (GR's published value), against 37.2 +- 7.2: 0.28 sigma. Frozen or per-site offset: 0 mas/yr, excluded at 5.2 sigma.
- LAGEOS (~10%): the rule passes; a frozen offset fails.
- Lunar ranging |alpha1| < ~1e-4: rule alpha1 = 0 passes; a frozen offset (alpha1 = -8) fails by about 1e5 times the bound.
- A separate tilt-hinge weight is bounded by GP-B (2 sigma) to 0.76 < c < 1.72. The single hinge sum gives c = 1 with nothing chosen.
- INFO: the circular polar-orbit average of D3 for a uniform-rotation Earth model is 40.8 mas/yr; the published 39.2 uses the mission orbit and Earth model.

## Proposed working rule (tick-fraction rule, stationary completion) and gate

> "A site's tick fraction, and the tick offset of each neighbour pair, are response variables: like the edges, they take the values that make the total phase stationary."

- Bends CL-1: every site no longer ticks in step with every neighbour, because offsets between neighbours are allowed. The axioms are unchanged.
- Gate:
  - (1) no measured number is chosen; G and the hinge coefficient are those of the static sector;
  - (2) no observed structure is inserted; the rule names only sites, neighbour pairs, ticks and edges;
  - (3) predictions it was not built for: the Lense-Thirring coefficient and angular pattern, alpha1 = 0, conservation of the record current as a solvability condition, and the per-site offset being pure gauge;
  - (4) bends CL-1.
- PASSES on frame dragging.

## Smuggling review

Supplied, not forced:
- the Regge limit of the sheared-prism hinge sum to (1/16 pi G) int sqrt(-g) R4 (the step that puts the K-terms in with coefficient one; standard Regge convergence, not computed on sheared prisms here);
- the gyroscope readout Omega = -(1/2) curl beta (spin transport in the read geometry);
- the record phase -m dtau with dtau read in the sheared geometry (as in tick-fraction-beta);
- a flat background, first order in J and in GM, and asymptotic decay;
- the PPN parametrisation, used only to name alpha1.

Forced, given those inputs:
- the offset equation and its coefficient;
- the gauge status of per-site offsets;
- the solvability condition;
- independence from the longitudinal weight;
- the Lense-Thirring field;
- alpha1 = 0, given the separately derived gamma = 1.

No Kerr metric and no momentum constraint is input: the equation is the rule's own Euler-Lagrange equation in beta.

## Boundary

- Interiors (a rotating body needs holding stresses; open, as in tick-fraction-beta).
- Second order in J and cross terms with the static field (J times GM).
- Time-dependent offsets (waves): the register's shift wave law is not re-derived from this rule.
- Lattice-order preferred-frame effects. alpha1 = 0 is shown in the continuum limit; O(a^2) corrections from the lattice frame are not computed.
- The 1/r^2 grid error and the box error at r <~ 10.

## Uses / narrows

- Uses: agents/tick-skip-gamma (gamma = 1, the static prism reduction), agents/tick-fraction-beta (record readout, all edges respond), and CANDIDATE_LAWS_v3 CL-3 (the momentum-constraint-and-shift clause: there the shift is the constraint's multiplier, and stationarity "does not fix the shift").
- Narrows that clause: in a STATIONARY state the constraint does fix the curl of the shift, and that is all of frame dragging. The supplied wave law can only set the gauge (gradient) part, so mu_s and kappa do not affect GP-B or LAGEOS.
- Consistent with open PR #9950 (zero shift with slips fails on rotating flows): a frozen offset is excluded here by GP-B at 5.2 sigma and by alpha1.
- Consistent with open PR #9904 (a supplied block-rung insertion gives frame dragging and alpha1 = 0 as finite diagnostics): here the coefficient follows from the hinge sum, with the matter coupling read from -m dtau.
- The tick-fraction rule's "frame dragging: open" now reads: GR coefficient, forced, given that per-pair offsets respond and the sheared-prism Regge limit holds.
