---
claim_id: the_tick_fraction_and_pair_offsets_answering_the_hinge_sum_are_constraints_and_leave_exactly_two_tensor_waves_on_the_edge_cone_with_the_quadrupole_coefficient_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Linear order about flat count geometry, time-dependent, under the tick-fraction rule (a supplied candidate rule with zero premise weight, not adopted): the site tick fraction N (tick edge, one per site), the tick offset of each neighbour pair (mixed edge, one per spatial edge) and every spatial edge answer the CL-3 hinge sum. Lattice (Euclidean linearised Regge on prisms over the campaign's spatial triangulation, axis edges plus even-sum face diagonals, 13 edges per site): the tick-fraction and offset block has no tick-to-tick coupling and its null space is exactly time relabelling, so N and offsets are constraints (derived from the combinatorics, not assumed); at two random momenta the null space is vertex displacements only; the numerically found transfer spectrum at |k| = 0.02 (three directions; roots common to two random rank completions, finite tolerances) has 32 finite roots per 8-site cell, the tensor branch at the 8 folded momenta, two polarisations each, and no other root was found there (no scalar, vector, breathing, zero-frequency or gapped root); at the light root (|k| = 0.05, 0.025) the two physical vectors are transverse-traceless; in 18 sampled cases out to |k| = 1.5 (tau = 1 and 0.7, tau = tick edge / spatial edge) both polarisations follow sinh(E/2) = tau [sum_i sin^2(k_i/2)]^(1/2) to 1e-9, so at those cases the tensor cone is the edges' null cone with no birefringence; the sampled census is a numerical diagnostic, not a proof of the full spectrum at every k; with the non-metric modes responding, the effective action on smooth metrics is 8.0000 x the Gamma-Gamma form of sqrt(g) R in all ten components (residual 7.5e-6, falling as k^2). Continuum (supplied Regge limit, sympy): n and beta carry no second time derivative; the scalar/vector sector has no wave; TT L2 = (1/2)(hdot^2 - h'^2) and static L2 = -2|grad Phi|^2 from the same sqrt(-g) R, so G_T = G_N; quadrupole P = (G/5)<dddQ dddQ>, 32/5 for a circular binary. Contrast: on the Freudenthal (Kuhn) carrier the same rule leaves one zero-action non-metric branch at the sampled momenta, whose cell-averaged metric has an O(1) non-gauge part. Not derived: the Lorentzian continuation, the flat tick/edge ratio (the hinge sum leaves it free; c_gw = c_light needs CL-1's light-crossing tick clause), the register-level dressed graviton cone, the source conservation identity, nonlinear order."
upstream_dependencies:
  - minimal_axioms
  - edge_register_set_census_cube_edges_alone_give_no_hinge_sum_and_six_edges_per_site_give_two_tensor_polarisations_on_the_edge_cone_bounded_theorem_note_2026-10-22
  - a_site_tick_count_and_a_site_density_answer_the_hinge_sum_through_one_operator_so_light_bends_twice_the_newtonian_amount_bounded_theorem_note_2026-10-23
runner: scripts/the_tick_fraction_and_pair_offsets_answering_the_hinge_sum_are_constraints_and_leave_exactly_two_tensor_waves_on_the_edge_cone_with_the_quadrupole_coefficient_2026_10_23.py
---

# The tick fraction and pair offsets answering the hinge sum are constraints and, at the sampled momenta, leave only two tensor waves on the edge cone, with the quadrupole coefficient

Claim type: bounded_theorem.
Primary runner: `scripts/the_tick_fraction_and_pair_offsets_answering_the_hinge_sum_are_constraints_and_leave_exactly_two_tensor_waves_on_the_edge_cone_with_the_quadrupole_coefficient_2026_10_23.py` (19 PASS, 0 FAIL, about 8 s, about 110 MB peak).

Model status (2026-11-14). The update law (CL-1) and the response law's hinge sum (CL-3) of the originating three-law register are used here as supplied conditional model definitions with zero premise weight. The originating register text ("CANDIDATE_LAWS_v3") is not in this repository, and these clauses are not the entries of the same number in [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md). The tick-fraction rule quoted below is a candidate rule from that register; it is tested here, not adopted.

## Question

The tick-fraction rule (proposed in the originating register as a working rule: "a site's tick fraction, and the tick offset between each pair of neighbouring sites, are response variables: like the edges, they take the values that make the CL-3 hinge sum stationary") gives gamma = beta = 1, alpha1 = 0 and Lense-Thirring in static and stationary states. Its register entry lists waves as open. In a time-dependent state the edges change from tick to tick, and the deficits at hinges that contain a tick direction matter. Does the same rule give gravitational waves as measured?
- (i) exactly two tensor polarisations, with no scalar, vector or breathing mode;
- (ii) the matter/light limiting speed (GW170817);
- (iii) the quadrupole energy-loss coefficient (Hulse-Taylor)?

The linearised Einstein equation is not imported. The lattice results come from the rule's own hinge sum, and the continuum coefficients come from expanding sqrt(-g) R, the supplied Regge limit.

## Setup

- Carrier: prisms over the campaign's spatial triangulation, the edge-register set of edge-modes (3 axis edges plus the face diagonals joining even-sum sites, five tetrahedra per cube, alternating). Each prism is split into four 4-simplices by a global vertex order.
- Edges per site: 6 spatial, 1 tick (the tick fraction N) and 6 mixed (one per spatial edge, the pair offset). All 13 respond; that is the rule.
- Contrast carrier: Freudenthal (Kuhn), with 7 + 1 + 7 edges per site.
- Hinge sum: the Euclidean linearised Regge second variation.
  - Simplex Schlaefli gradients are differenced and Richardson-extrapolated; triangle areas use an analytic Heron Hessian.
  - Bloch form on the 8-site cell, Fourier in the tick direction. It is exactly a Laurent polynomial of degree 1 in z = e^{-E} (leak 3e-15).
- Roots: the matrix polynomial is singular, since displacements make it vanish identically. Its finite roots are found by adding a random rank-completing perturbation of the null rank and keeping the roots common to two independent perturbations.
- Supplied: the Euclidean continuation (Lorentzian tau^2 -> -tau^2, E -> i w), and the Regge limit (1/16 pi G) int sqrt(-g) R used only for the continuum coefficients.

## Results

### Theorems (exact, sympy, given the supplied Regge limit)

1. **The lapse and shift are constraints** (A1, A2).
   - Expand sqrt(-g) R to second order in a scalar/vector plane-wave sector (n, beta_z, beta_x, h_zz, h_xx = h_yy). No equation contains a second time derivative of n or beta.
   - n enters linearly. Its equation is the Hamiltonian constraint d'' = 0. The beta equations are the momentum constraints.
   - In vacuum the sector has no wave: d = 0, beta_x = 0, and h_zz is fixed by n and beta_z (gauge).
2. **Two tensor waves at the hinge-sum speed** (A3). The TT sector gives L2 = (1/2)(a_t^2 - a_z^2 + b_t^2 - b_z^2).
3. **One coupling** (A4, A5, A7).
   - The static gamma = 1 sector from the same expansion gives L2 = -2|grad Phi|^2.
   - A record's phase -m dtau couples as (1/2) h_mn T^mn.
   - Hence box h^TT = -16 pi G T^TT and lap Phi = 4 pi G rho with the same G, so G_T / G_N = 1.
4. **The quadrupole formula** (A6).
   - The outgoing flux of the derived L2 is (1/32 pi G) sum hdot_ij^2. The retarded field is h^TT = (2G/r) Lambda Qddot. The angular integral of Lambda is 8 pi/5, done exactly.
   - So P = (G/5) <dddQ dddQ>, and a circular binary gives (32/5) G mu^2 r^4 Omega^6.

### Lattice theorems and finite diagnostics (campaign carrier, every edge responding)

1. **No extra zero directions** (B1). The generic null space is 32 per cell = 4 displacements x 8 sites (|QG|/|Q| = 5e-12).
2. **N and offsets are constraints, derived from the rule's combinatorics** (B3).
   - Tick and mixed edges lie in one slab, so their block of the hinge-sum Hessian has no z^{+-1} term (6e-16). They couple only to the spatial edges of the two slices they join.
   - Their equations are therefore algebraic: constraints, not propagating variables.
   - The block's null space has dimension 16 = 2 per site and is spanned, to 4e-8, by the time-relabelling (u_t) parts. The per-site tick fraction is a relabelling where it has no action, as the per-site offset was in tick-fraction-frame-dragging.
3. **Sampled census: two polarisations, no other root found** (B4; a numerical diagnostic). At |k| = 0.02 along the axis, the body diagonal and (0.3, 0.5, 0.8):
   - every finite root found is accounted for: 32 per cell = 2 polarisations x (+-E) x 8 folded momenta k + pi(0/1, 0/1, 0/1), matching the tensor branch to <= 5e-8;
   - 4 roots are light, with |E/k - 1| <= 3.6e-5;
   - no scalar, vector, breathing, zero-frequency or gapped root is found at these momenta.
   - The roots of the singular matrix polynomial are those common to two random rank-completing perturbations, matched to finite tolerances. This is not a symbolic rank or dispersion proof, and other momenta are not censused (large k only for the tensor branch, item 5).
   - For comparison, with the lapse fixed and the shift zero on the same carrier (edge-modes E3) there are 48-50 zero-frequency roots besides the 4 light ones. Responding N and offsets remove them.
4. **The two physical vectors are transverse-traceless tensor waves** (B5).
   - At the light root the nullity is 34 = 32 + 2.
   - Fitted to a metric plus displacement, the trace and longitudinal parts of the electric curvature R_0i0j are <= 2e-4.
   - The non-metric admixture falls as k (0.021, then 0.011).
5. **Tensor dispersion at the sampled cases, no birefringence there** (B6). Both polarisations follow sinh(E/2) = tau [sum_i sin^2(k_i/2)]^(1/2) to 1e-9, in 18 cases with |k| = 0.3, 1, 1.5, three directions, and tau = 1 and 0.7. At small k, E = tau |k|: the edges' null cone. That the formula holds at every k is not shown, and other branches are not censused at these k.
6. **One coefficient for all ten components** (B7).
   - With the non-metric modes integrated out (they respond), the lattice effective action on smooth metrics equals c times the Gamma-Gamma form of sqrt(g) R, with c = 8.0000 = the cell's 4-volume.
   - The relative residual is 3.0e-5 and then 7.5e-6 as |k| halves (falling as k^2).
   - The static Newtonian/TT ratio of that form is 4, the sympy value (-2)/(-1/2).
   - This checks the supplied Regge limit at quadratic order on this carrier. The bare restriction without the non-metric response is not proportional (residual 0.57).
7. **The hinge sum leaves the flat tick/edge ratio tau free** (B8). A uniform change of the tick edge is a zero of the hinge sum.

### Contrast (B2)

On the Freudenthal (Kuhn) carrier the same rule leaves one zero-action non-metric branch at the sampled momenta: nullity 5 = 4 + 1, with 95% of its weight on tick and mixed edges. Its cell-averaged metric keeps an O(1) non-gauge part (0.56 at |k| = 0.05 and 0.025). A source reading that average would couple to an undetermined direction. The campaign carrier has no such branch. That is a new reason for the six-edge register set once N and offsets respond.

### The speed tie (ii)

- The graviton's label speed is tau blocks per tick (B6). It is set by the same edges every species reads.
- The walk's light speed is sin(eps)/sqrt 3 blocks per tick (CL-1 band, quoted).
- The two agree iff tau = sin(eps)/sqrt 3, i.e. iff the proper tick is that fraction of the edges' light crossing. That is CL-1's clause ("the tick is a fixed fraction of each cube's light crossing").
- The hinge sum does not fix tau (B8), and nothing else in this computation does. So:
  - the tie is CL-1's clause, not a hinge-sum output;
  - there is no second free number, because one ratio sets both cones;
  - in a wave N, the edges and the walk's proper tick move together, as long as the walk reads the local edges (CL-1: "every species reads the same edges").
- At the register level the dressed-cone clause of CL-3 (dressed hop weights) is still needed. This note does not re-derive it.

### Lattice dispersion and measurement (C1-C4)

- Lorentzian reading (supplied continuation): sin(w/2) = tau s(k), so c(k) = 1 + (ka)^2 (tau^2 - sum khat_i^4)/24. With CL-1's tau = sin(eps)/sqrt 3 <= 1/sqrt 3 <= (sum khat^4)^(1/2), the graviton is never superluminal.
- GW170817 (-3e-15 < dc < 7e-16): |dc| <= 1.2e-77 at 100 Hz for block edges up to 100 cells of 8.1e-35 m. The bound alone constrains the step only to a < 0.13 m. As k -> 0, c_gw = c_light exactly, given the tie.
- Hulse-Taylor (0.9983 +- 0.0016): the rule predicts G_T / G_N = 1, at 1.06 sigma. A separate tensor coupling such as 0.81 (the unsubtracted sea in the register) would be 118 sigma off.
- Since no scalar or vector mode exists, there is no dipole or breathing radiation.

## Verdict

- (i) On the campaign carrier, at the sampled momenta: two TT polarisations and no other root found (|k| = 0.02, three directions); every-k absence of other modes is open (a symbolic rank or dispersion proof is not supplied). In the supplied continuum sector (A1-A3) the scalar and vector sectors have no wave. N and offsets act as constraints, which follows from the rule's slab combinatorics (no tick-to-tick coupling); that their null space is exactly time relabelling is checked at one k.
- (ii) YES at k -> 0, given CL-1's light-crossing tick clause. This is the same single ratio, not a separate number, but the hinge sum does not derive it. The lattice dispersion is O((ka)^2/24) and passes GW170817 by about 62 orders.
- (iii) YES: 32/5 with G_T = G_N from one hinge coefficient. The lattice confirms that single coefficient across all ten metric components.

## Gate

- No new rule is proposed. The supplied tick-fraction rule (a candidate, not adopted) is tested.
  - (1) No measured number is chosen.
  - (2) No structure is inserted.
  - (3) Predictions it was not built for:
    - two polarisations only, at the sampled momenta;
    - no birefringence;
    - the exact lattice dispersion sinh(E/2) = tau s(k), with no superluminality at CL-1's tau;
    - the quadrupole coefficient;
    - removal of the fixed-lapse zero-frequency branches;
    - the Kuhn carrier's zero-action defect.
  - (4) It bends CL-1, as the candidate rule proposes.
- Within the sampled census and the supplied continuum limit, the wave tests pass. The speed tie rests on CL-1's supplied tick clause.

## Smuggling review

Supplied, not forced:
- the Euclidean continuation to Lorentzian frequencies;
- the Regge limit sqrt(-g) R, used for the continuum coefficients and checked on the lattice at quadratic order by B7;
- the record phase -m dtau;
- the conservation identity int T^ij = Qddot/2, including binding stresses;
- the retarded boundary condition and the flux readout;
- the carrier (the campaign's triangulation, with Kuhn as the contrast);
- CL-1's light-crossing tick, for the speed tie;
- the block size used in the bound;
- the measured comparison numbers.

Forced, given those:
- the constraint status of N and offsets;
- the sampled mode census (a numerical diagnostic);
- the TT polarisations;
- the dispersion formula;
- the single coefficient;
- the quadrupole coefficient.

No linearised Einstein equation is input. The continuum equations are Euler-Lagrange equations of the expanded sqrt(-g) R, and the lattice ones are the hinge sum's own.

## Boundary

- Linear order only: no memory effect, no nonlinear wave interaction, no backreaction.
- Euclidean lattice with a supplied continuation. No Lorentzian Regge or rapidity-deficit computation is done.
- Register-level dynamics is not touched: dressed weights, zero-point spread and walls.
- Eccentric orbit averaging (Peters-Mathews) is not derived; only the ratio to GR is tested.
- The walk's band speed is quoted, not re-derived.
- One |k| is used for the full census (0.02, three directions); large k is checked only for the tensor branch. No statement about other modes at every k is made.
- The near-degenerate polarisation split is resolved only to about 1e-6 at the light root.

## Uses / narrows

- Uses:
  - edge-modes, [EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22.md](EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22.md) (#9932, carried in this PR): the carrier, the fixed-lapse census (narrowed here: responding N and offsets remove its zero-frequency roots at the sampled momenta), and the Kuhn controls;
  - tick-skip-gamma, [A_SITE_TICK_COUNT_AND_A_SITE_DENSITY_ANSWER_THE_HINGE_SUM_THROUGH_ONE_OPERATOR_SO_LIGHT_BENDS_TWICE_THE_NEWTONIAN_AMOUNT_BOUNDED_THEOREM_NOTE_2026-10-23.md](A_SITE_TICK_COUNT_AND_A_SITE_DENSITY_ANSWER_THE_HINGE_SUM_THROUGH_ONE_OPERATOR_SO_LIGHT_BENDS_TWICE_THE_NEWTONIAN_AMOUNT_BOUNDED_THEOREM_NOTE_2026-10-23.md) (#10040, carried in this PR): gamma = 1 and the static coefficient;
  - tick-fraction-beta (#10048) and tick-fraction-frame-dragging (#10050): logged sources, not in this repository and recorded only in the consolidation map; the static coefficient, per-pair offsets, the per-site relabelling being pure gauge, and the record coupling are taken from them as historical reported results, unverified here, and the runner re-derives what it uses (A4, A5);
  - CANDIDATE_LAWS_v3 (the originating register, not in this repository): the CL-1 tick-fraction clause and band, and CL-3's hinge sum and dressed-cone clause, used as supplied definitions.
- Consistent, at the sampled momenta, with the originating register's mode count (two tensor polarisations on the edge cone under the fixed lapse).
- The originating register listed waves as open under the tick-fraction clause; this note supplies, at the sampled momenta and given the supplied continuation and CL-1's tick clause, two TT polarisations, c_gw = edge cone and quadrupole 32/5.
- The Kuhn-carrier zero-action branch: the source says it is consistent with a main note it names only as SCALE_LADDER_GRAVITY_..._COMMON_CONE (two main notes match that pattern; the phrase was not found in either, so the remark is a historical reported statement, unverified here) and with edge-modes C2 (#9932's C2 check, carried).
