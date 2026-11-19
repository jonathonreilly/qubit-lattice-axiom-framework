---
claim_id: far_layers_reading_a_smoothed_field_decouple_the_mirror_from_field_strength_but_not_from_gauge_turns_topology_or_long_wavelengths_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For a supplied 2D euclidean U(1) toy (a 1+1D world) on an 8 x 8 antiperiodic torus times Ls = 8 layers (Shamir slab, wall height M = 1, Pauli-Villars subtraction), with layer s reading a smoothed copy of the links (gradient flow with flow time growing in s, or rung-s block-flux averaging): (A) flow, block-flux averaging and anchor transports are gauge covariant per site, so the whole slab is exactly gauge invariant; flow and block averaging keep the topological charge and the harmonic part of the holonomy, while coarse Wilson lines with anchor transports (the naive zoom reading) concentrate flux and lose the charge mod 2 pi; a nearest-neighbour smoothing step is stable only for eps <= 1/(2d) and grows the flux variance by at most one cell^2 per step, so n layer-local steps smooth over at most sqrt(n) cells, while reading rung-s blocks reaches 2^s; (B, C) the light end keeps the full photon coupling, the far mirror's photon coupling falls to ~1e-4, both ends keep the full pure-gauge coupling, the smoothed slab's photon response equals the light end's alone to < 3% with no gauge-variant term, and for 3-4-5-0 the anomalous terms of the light end alone cancel (sum chi q^2 = 0) while a real gauge-variant term remains; (D) the flowed far field keeps index q Q for q = 1, 3, 4, 5, and the Q = 1 slab keeps one near-zero mode whose left vector is the far mirror's (spread, not removed): the mirror sits in every 't Hooft vertex; (E) estimates: smoothing radius r needs (r/a)^2 layer-local steps but log2(r/a) zoom layers (136 for the Earth radius, 200 for the horizon); no added Gamma_Z or alpha running for r >> 1/m_e; a once-thermal mirror gives Delta N_eff = 2.25 (excluded), an unpopulated one ~0. Supplied model, finite diagnostic; no rule is adopted."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_rung_ladder_is_a_domain_wall_direction_with_exact_inflow_but_bounded_speed_makes_its_coarse_rungs_a_charged_tower_bounded_theorem_note_2026-10-22
runner: scripts/far_layers_reading_a_smoothed_field_decouple_the_mirror_from_field_strength_but_not_from_gauge_turns_topology_or_long_wavelengths_2026_10_22.py
---

# Far layers that read a smoothed field decouple the mirror from field strength, but not from gauge turns, topology or long wavelengths

Claim type: bounded_theorem.
Primary runner: `scripts/far_layers_reading_a_smoothed_field_decouple_the_mirror_from_field_strength_but_not_from_gauge_turns_topology_or_long_wavelengths_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The [rung-dimension note](THE_RUNG_LADDER_IS_A_DOMAIN_WALL_DIRECTION_WITH_EXACT_INFLOW_BUT_BOUNDED_SPEED_MAKES_ITS_COARSE_RUNGS_A_CHARGED_TOWER_BOUNDED_THEOREM_NOTE_2026-10-22.md) proposed a layer rule: a full-density layer coordinate inside each role block, with exact free chirality, but vector-like couplings, because the far-end mirror reads the same links (its E2). The [cube-filtered quartic note](THE_CUBE_FILTERED_QUARTIC_TOY_IS_SIGN_FREE_AND_PAIRS_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md) found that a symmetric gapping of the far mirror pairs instead. This note tests the remaining route named there. In the Grabowska-Kaplan construction (2016), layer s reads the gauge field smoothed by gradient flow, with flow time growing with s. The far mirror then sees an almost pure-gauge field. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are unchanged.

Repo check: origin/main and the open PRs contain nothing on Grabowska-Kaplan, smoothed far layers or flowed domain walls. The gradient-flow hits on main (DM Wilson path notes, record semigroup, cycle923) concern other flows. No open PR matches Grabowska, Kaplan, gradient flow, smoothed or far layer. This note builds on and narrows rung-dimension-chirality E1 to E3 and B1/B2, and it cites ladder-wall E3 and toy-qmc.

## Statement

A. The smoothing rule in framework terms.
1. Theorem (covariance per site). Write U(p, p+mu) -> g(p) U g(p+mu)^*. A layer reading th_s[th] is covariant if th_s[g.th] = g.th_s[th]. Then every layer's mode at p turns with the same g(p), and the whole slab is gauge invariant. Three readings are covariant: gradient flow, because the force comes from sin F; block-flux averaging, because the added correction a[F] = d_B^+(block mean - F) on a block's interior links depends only on F; and anchor transports, which replace a fine link by -phi(p) + Abar(c_p, c_q) + phi(q) with phi the Wilson line from the block anchor. Averaging parallel links without transports is not covariant (A1: residuals 2e-15, 2e-15, 2e-15 against 3.09).
2. Theorem (topology and holonomy). The sum of plaquette changes vanishes, so flow keeps the topological charge Q while no plaquette passes pi, and it keeps the mean holonomy (the harmonic part) exactly. It relaxes to the uniform flux 2 pi Q/L^2. Block averaging keeps Q, and the whole-torus block gives the uniform field at once. The naive zoom reading (coarse Wilson lines with anchor transports) piles each block's flux onto its corner plaquettes: max|F| goes from 0.80 to 2.28, and Q is lost mod 2 pi. So a coarse link coarse-grains the field but does not smooth it. The reading GK needs is "spread the block's flux", not "read the block's Wilson line" (A2).
3. Theorem (reach). An explicit nearest-neighbour flow step is stable if and only if eps <= 1/(2d), because the largest plaquette-Laplacian level is 4d. The flux variance then grows by 2 d eps <= 1 cell^2 per step (measured: 0.500 at eps = 1/8, 0.999 at 1/4; at eps = 0.26 the staggered mode grows 5e6-fold in 200 steps). So n layer-local steps smooth over r <= sqrt(n) cells. Reading rung-s blocks reaches 2^s. This is the diffusive counterpart of the bounded-speed theorem (rung-dimension C2): local smoothing is slow, and only the zoom hierarchy is fast (A3).

B. Free slab. The eight lowest modes are a light pair at each antiperiodic momentum (+-pi/8, +-pi/8). They sit on the end layers, P_- on layer 0 and P_+ on layer Ls - 1 (minimum chiral end weight 0.977, singular value 0.541 against 1.00 for the next) (B1).

C. Decoupling.
1. Field seen by each end: the light-mode layer weights times the field each layer reads. The light end sees a photon (transverse) mode in full (1.000). The far mirror sees 1e-4 to 5e-4 of it at k = 2 pi/8 and 0 at 4 pi/8, for both flow and block reading. Both ends see a pure-gauge mode in full (1.000000): the mirror is blind to field strength but still turns under gauge transformations, GK's "fluff" coupling (C1).
2. Effective action (DW minus PV, exact second derivatives). The smoothed slabs are exactly gauge invariant (pure-gauge rows <= 5e-15). Their photon response equals that of the light end alone (far layers cut) to under 3%: 0.2578/0.2624 against 0.2562 at k1, and 0.3282/0.3286 against 0.3280 at k2, relative to the unsmoothed slab. The cut slab has an imaginary pure-gauge x photon term (0.153i, 0.191i), which is the light Weyl's anomaly; in the smoothed slab the far end's fluff coupling cancels it. The ratio to the unsmoothed slab is not 1/2, because the modulus of a 2D chiral determinant is fixed only up to a local term (Jackiw-Rajaraman), so only the comparison smoothed = cut carries meaning (C2).
3. Theorem (3-4-5-0, quadratic order). Each species' response is q^2 times the unit response. The mirror-image slab (light right-hander on layer Ls - 1) has the complex-conjugate response, by g5-R5 hermiticity. So for the cut slab the anomalous terms sum to sum chi q^2 = 9 + 16 - 25 = 0 (1e-15 numerically), while its real pure-gauge term sums to sum q^2 > 0 (7.76, 22.7) and must be removed by a counterterm. The smoothed slab is gauge invariant with no counterterm at all (C3).

D. Topology and holonomy: the mirror's 't Hooft vertex.
1. On a Q = 1 lump, the index of the near-layer field and of the flowed far-layer field (spectral asymmetry of g5 D_W(-1)) are both q Q, for q = 1, 3, 4, 5 (D1).
2. In the Q = 1 slab, one near-zero mode remains with or without smoothing: sigma_0 = 5e-4 unsmoothed and 4e-7 with GK layers, against 0.43 for the next. Its right vector is the near-end left-handed zero mode at the lump (weight 0.94). Its left vector is the far mirror's psi-bar P_- zero mode (weight 0.998). Smoothing only spreads it: the IPR goes from 2.31 to 1.19, where 1 means uniform. Every topological event therefore moves chi q Q light units and the opposite number in the mirror. The 't Hooft vertex includes the mirror and is not suppressed: one event has one action (D2).
3. Theorem (holonomy). Smoothing keeps the harmonic part (A2), so under a 2 pi winding the mirror's levels still cross q times (rung-dimension B2/E2). In 1+1D a winding in time is the topological charge, which is the coupling of D1 and D2 (D3).

E. Estimates against measurement, with a = sqrt(8 pi) l_P and r the far layer's smoothing radius.
1. Layer count. Layer-local flow needs (r/a)^2 steps: 1e33 for r = 1/M_Z, 1e43 for 1/m_e, 1e82 for the Earth's radius, 1e120 for c/H0. The zoom reading needs log2(r/a) layers: 54.6, 72.0, 135.9 and 200.1. The last equals the R_H of rung-dimension D2: the deepest layer reads the horizon-size block (E1).
2. Gamma_Z and alpha. The mirror couples at momentum k only through the filter f(k): exp(-k^2 t) for flow, about 1/(k b) per direction for a rung-b block. For r >> 1/m_e it adds nothing to Gamma_Z (the unsmoothed e^c' alone adds 35.5 MeV per family) and nothing to the running of alpha between m_e and M_Z. The layers are full density with equal layer gaps, so there is no tower (E2).
3. N_eff. What remains of the mirror is a massless conjugate copy of the content. It is fully charged for wavelengths longer than r, for holonomy and for topology, and it couples to gravity. If it ever shared a temperature with the SM above the electroweak scale, Delta N_eff = 48 (10.75/106.75)^(4/3) = 2.25, against Planck's 2.99 +- 0.17: excluded. So it must never thermalise. Soft production at r = R_Earth gives Gamma/H ~ alpha^2 M_P r^-3 T^-4 = 6e-3 at T_CMB, and less at higher T. Topology events make only k ~ 1/r quanta. If the mirror starts empty, Delta N_eff ~ 0 (E3, a dimensional estimate).
4. Speculation: the dark sector. As it stands the far mirror is dark radiation of zero abundance, not dark matter. A far-layer Yukawa reading the smoothed Higgs would give it the light masses, because the vev is a k = 0 mode and survives smoothing. That would make it a stable, nearly inert massive copy whose abundance is set only by initial conditions. Not tested (E4).

## Candidate law text (not adopted)

Layer rule (rung-dimension-chirality, unchanged):
> "Each matter cell is a role block whose matter sites, in a fixed order, are layers 0..Ls-1. Each half-tick hops every layer's modes to its neighbour layer through W(1 - g5)/2 and to the same layer of the neighbour cell through the cube tick; matter is read at layer 0."

New reading clause (zoom smoothing; it unifies the layer coordinate with the zoom ladder):
> "Layer s reads rung s: its cell-to-cell hops carry the links plus the correction, a function of the link fluxes alone, that spreads each rung-s block's flux evenly over that block, refreshed once per rung-s tick."

Rejected forms:
- "layer s reads its rung-s coarse links": this fails A2, because it concentrates flux and loses topology.
- "layer s+1 reads layer s's links flowed one nearest-neighbour step": this fails E1, because it needs (r/a)^2 layers.

## Smuggling check

Supplied: the 2D U(1) toy (L = 8, Ls = 8, M = 1, antiperiodic boundary conditions), Shamir's slab and the PV subtraction, the flow profile (0, 0, 0, 0, 10, 30, 80, 200 steps at eps = 1/8), the block profile (1, 1, 1, 1, 2, 4, 8, 8), the minimal-norm block correction, the probes, the lump, a = sqrt(8 pi) l_P, H0, R_Earth as the illustrative r, and the PDG and Planck inputs.

Forced, given those: per-site covariance and gauge invariance of the slab; conservation of Q and holonomy; flux concentration under anchor reading; the stability bound and the diffusive reach; the light content; the photon blindness and pure-gauge visibility of the far end; smoothed = cut for the photon; the sum chi q^2 = 0 cancellation; the real gauge-variant remainder of the cut; the far index q Q; and the mirror zero mode in the Q = 1 slab.

Choices that are not forced:
- The layer-to-rung identification: which layers stay unsmoothed, and the doubling per layer.
- The "evenly spread" target. It is a box filter; a gaussian is smoother but cannot be reached locally.
- The lopsidedness. Only layer 0 reads fine links. The reason given is that the layer index is the zoom direction (fine to coarse), so the asymmetry is the hierarchy's own. A symmetric reading (both ends smoothed) leaves no charged light fermion, and the measured weak interaction is chiral.

Not derived:
- That the block hierarchy carries refreshable block-flux data for quantum link registers. The correction acts over block range 2^s; it is admissible only as a rung-s block operation at the rung-s rate (compute, use, uncompute, depth ~2^s per rung tick).
- The non-abelian version. It needs adjoint transports to the anchor to spread a block's flux, and it is untested.
- That the mirror starts empty.

## Boundary

The toy is 2D euclidean U(1), quadratic order in the probe on a free background, plus exact index and singular-vector checks on one lump. These are not established:
- SU(2) x SU(3) behaviour.
- 3+1D behaviour (the electroweak 't Hooft vertex with mirror legs is argued, not computed).
- Higher orders in q, where sum chi q^4 does not vanish.
- Real-time dynamics of the far layers.
- A rule adoption.

The far mirror is not removed. It is cut off from field strength above 1/r, and it keeps the pure-gauge (fluff), holonomy, topology and long-wavelength couplings, plus gravity. Its charge appears in Gauss's law smeared over r.

Clause count. The layer rule plus the reading clause add two clauses. Together they would replace the register's mirror pair-square (the first sentence of "Mirror and vacuum", which fails by pair order), so the net count is +1, or 0 if the layer and reading clauses are merged into one. The cost is about 64 Ls one-mode sites per family per cell, which at Ls of about 136 to 200 means a role block of about 34^3 for three families.
