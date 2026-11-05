---
claim_id: static_redshift_on_fixed_step_edges_needs_a_wider_edge_window_while_split_history_cannot_help_and_skipped_half_ticks_heat_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's fixed step with edge registers on a window [w L, 2L] (split children at L) and global ticks: on an isotropic cube the fixed step gives a lapse proportional to the edge, so lapse ratios on a slice are edge ratios and a static core never meets the window bottom iff its central redshift factor alpha_c >= w L/l_far (for every far phase in [L, 2L] iff alpha_c >= w); a split maps 2L to L in proper length, so no split history changes the edge ratio. In continuum GR with supplied equations of state (relativistic polytropes with K = 1, Gamma = 2, 2.5, 3, and the causal limit c_s = 1), alpha_c = alpha_s/h_c exactly, uniform density reaches alpha_c = 0 at the Buchdahl bound, alpha_c falls monotonically along each sampled stable branch, and the maximum-mass values are 0.462, 0.340, 0.271 and 0.240 (causal limit), so [L/8, 2L] holds every stable causal-limit star at every far phase; with the supplied mass and radii of J0740+6620, alpha_c is 0.447 to 0.606 by EOS, w = 1/2 fails at about 16% of far phases (Gamma 2.5, R = 12.39 km) and w = 1/4 at none. Register sizes for the wider window follow from a supplied per-tick speed bound. In a one-dimensional free-fermion split-step proxy, skipping a half-tick at the floor creates about 0.08 eps^2 excitations per skip boundary that later ticks never undo, and schedules with components below the band width pump excitations linearly; a supplied 3D estimate puts the transient far above neutron-star luminosities. Supplied model, finite diagnostic: continuum GR in place of register dynamics, supplied EOS and measured inputs, a 1D proxy of the 3D tick."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/static_redshift_on_fixed_step_edges_needs_a_wider_edge_window_while_split_history_cannot_help_and_skipped_half_ticks_heat_2026_10_22.py
---

# Static redshift on fixed-step edges needs a wider edge window, while split history cannot help and skipped half-ticks heat

Claim type: bounded_theorem.
Primary runner: `scripts/static_redshift_on_fixed_step_edges_needs_a_wider_edge_window_while_split_history_cannot_help_and_skipped_half_ticks_heat_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) reads each cube's tick from its edges with one fixed step eps0, so the lapse is set by the edges, and with edge registers each edge length lives in a finite window whose top 2L triggers the split into children at L. A static star's core has a lower lapse than the far region, so on a slice with global ticks its edges must be shorter than the far edges by the central redshift factor alpha_c. If alpha_c is small enough, the core's edges would have to sit below the window bottom. This note compares three ways the register could hold static redshift: (a) a wider window [w L, 2L] with children still at L; (b) skipping half-ticks in cubes at the floor; (c) letting the split history of a region set its edge ratio. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. What the window has to hold.

1. On an isotropic cube the fixed step gives N = sin(eps0) l/sqrt3, so the lapse ratio between two cubes is their edge ratio, and with global ticks the mean ratio l_c/l_far on any spherical slicing equals alpha_c. A window [w L, 2L] bounds lapse ratios on a slice to [w/2, 2/w].
2. A split maps an edge of 2L to two of L in proper length, so every cube of every split history has edges in the window. History changes cell counts, never the edge ratio: option (c) fails as posed, and with the window [L, 2L] the bound alpha_c >= L/l_far >= 1/2 holds whatever the history.
3. With window [w L, 2L], a static core never meets the floor iff alpha_c >= w L/l_far; for every far phase l_far in [L, 2L] iff alpha_c >= w (worst phase l_far = L, a far cell just made by a split).

B. Central redshift of stable static stars (continuum GR, G = c = 1).

4. From d ln alpha = -dp/(eps + p), alpha_c = alpha_s exp(-int dp/(eps + p)), which is alpha_s/h_c for a polytrope (h the enthalpy per baryon), alpha_s/sqrt(1 + 2 p_c/eps_s) in the causal limit and (3 alpha_s - 1)/2 at uniform density.
5. Uniform density reaches alpha_c = 0 at the Buchdahl bound 2M/R = 8/9 and is dynamically stable there, so GR alone puts no floor on alpha_c; a bound needs causality or a real equation of state.
6. Along each sampled stable branch alpha_c falls monotonically with central pressure, so its minimum is at the maximum-mass star. In the causal limit (c_s = 1, the most compact causal EOS) that minimum is just below 1/4, so [L/8, 2L] holds every stable causal-limit star at every far phase.

C. Option (a), the wider window.

7. With a supplied per-tick speed bound |d ln l| < sqrt2 sigma, sigma = sin(eps0)/sqrt3, a linear register on [w L, 2L] can resolve motion at its bottom iff 2S >= 1.22 (2 - w)/(w sin eps0); a logarithmic register (octave plus mantissa) needs about 0.85/sin eps0 levels per octave.
8. In [w L, 2L] the rms edge reaches 2L only when every register is full, so the split trigger, the split and the children at L are unchanged; the children's length L sits inside the window at the fraction (1 - w)/(2 - w) of the range.
9. Lapse ratios on a slice are bounded by 2/w, and the static core is stationary: the tick is the same unitary in every cube, the redshift is carried by edge values, and no time-dependent drive appears. (Stated in the runner, not computed.)

D. Option (b), skipped half-ticks (one-dimensional two-tiling free-fermion walk with a skip region of one third of a 160-site ring).

10. With no skip the vacuum is kept exactly.
11. One skipped tick creates p1 ~ c eps^2 excitations at each boundary of the skip region, at band quasi-energies, and later ticks never undo them.
12. A periodic skip schedule is a drive at frequencies 2 pi {k f}. A schedule of period 2 (f = 1/2) is off-resonant with the band and leaves only the transient; schedules with components below the band width (f = 0.9, f equal to the golden ratio's inverse) pump excitations linearly in time.
13. A skipped half-tick must carry zero proper time and make no record, or records per proper time would rise by 1/f in the core, a local measurable difference. (Stated in the runner, not computed.)

## Derivation

Item 1: on an isotropic cube gamma^ii = 1/l^2, and the fixed step sqrt3 N rms(1/l) = sin eps0 gives N = sin(eps0) l/sqrt3; a constant ratio N/l is checked on eight edge values. Items 2 and 3 follow from the split's proper-length map and the window; a sampling of 2000 random growth-and-split histories, with lengths clamped at L as the window does, illustrates item 2. Item 4 integrates the TOV equations from the centre with scipy (relative tolerance 1e-10) and compares the direct integral of nu with the enthalpy form. Item 5 is the closed form at 2M/R = 8/9. Item 6 scans 70 central pressures in [1e-3, 30] per EOS and refines the maximum with 25 more. Item 7 is arithmetic on the supplied speed bound. Item 8 samples 20000 random 12-edge cubes with edges uniform in [1/4, 2] plus 50 all-full cubes. Items 10 to 12 evolve the vacuum correlation matrix of the free walk exactly under the skip schedules and count the excitations as the trace against the upper-band projector.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Fixed-step lapse: N/l = sin(eps0)/sqrt3 on all eight sampled edges.
- Split histories: 2000 random histories keep every edge in [1.000, 2.000] (with the clamp at L, an illustration).
- TOV, Gamma = 2.5, p_c = 0.05: direct nu integral 0.6255150 against the enthalpy form 0.6255150 (asserted below 1e-6).
- Uniform density: alpha_c = 0 at 2M/R = 8/9 (below 1e-12); alpha_c = 1/2 at 2M/R = 5/9 and 1/4 at 0.75 are stated, not computed.
- Register sizes: 2S_min for a linear window, eps0 = 0.0075: 163 (w = 1), 490 (w = 1/2), 1143 (w = 1/4), log register 113 per octave (340 for three octaves); eps0 = 0.0375: 33, 98, 229, log 23 per octave (68 for three octaves).
- Split trigger in [L/4, 2L]: rms = 2L exactly on the all-full cubes and on no other sampled cube; the children's length sits at 0.429 of the register.
- No skip: maximum excitation 3.0e-15 over 40 ticks.

Item 3 (the floor condition) is stated in the runner, not computed separately.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Maximum-mass stars: Gamma = 2: 2M/R 0.429, alpha_c 0.462; Gamma = 2.5: 0.559, 0.340; Gamma = 3: 0.632, 0.271; causal limit: 0.708, 0.240. The runner asserts monotone alpha_c along each sampled stable branch and 1/8 < alpha_c^min(causal) < 1/4.
- One skipped tick (mass eps/3): eps = 0.3: p1 7.47e-03 (p1/eps^2 0.08), mean quasi-energy/eps 1.18; eps = 0.1: p1 8.06e-04 (0.08), 1.17; eps = 0.03: p1 7.23e-05 (0.08), 1.17.
- Skip schedules over 300 ticks at eps = 0.3 (excitations at tick 100 and at the end; slope from tick 100): f = 0.500: 0.04 to 0.04, slope 2.5e-07 per tick; f = 0.750: 0.01 to 0.01, slope -1.7e-07; f = 0.900: 0.22 to 0.68, slope 2.3e-03; f = 0.618: 0.04 to 0.08, slope 2.3e-04.

## Estimates against measurement

Estimates with supplied inputs (the J0740+6620 mass 2.08 solar masses and radii 12.39 km and 13.7 km from the two NICER analyses, GM/c^2 = 1.4766 km per solar mass, the polytropes and causal-limit EOS above, a rung L = sqrt(8 pi) l_P, a 5 km core radius, f_c ~ 1/2):
- J0740+6620 at R = 12.39 km: 2M/R 0.496, uniform-density value 0.565, Gamma = 2.5 0.447, Gamma = 3 0.485, causal limit 0.554. At R = 13.7 km: 2M/R 0.448, uniform 0.614, Gamma = 2.5 0.515, Gamma = 3 0.546, causal 0.606. Gamma = 2 does not reach these compactnesses. The window [L, 2L] (w = 1) fails for this star; w = 1/2 fails at 16% of far phases (Gamma = 2.5, R = 12.39 km, far phases taken uniform in log l_far); w = 1/4 fails at none.
- Skipped half-ticks in the J0740 core, using p1 = 0.08 eps0^2 from the one-dimensional proxy and E per quantum = hbar eps0/tau: eps0 = 0.0075 gives p1 4.5e-06, 6.8e+08 J per quantum, a flux of 2e+116 W/m^2 and 6e+124 W; eps0 = 0.0375 gives p1 1.1e-04, 1e+117 W/m^2 and 3e+125 W. The runner compares these with a supplied scale of about 1e27 W for observed neutron-star luminosities.

## Boundary

Supplied: the fixed step and window of the update law, global ticks, continuum GR and the TOV equations in place of register dynamics, the polytropes with K = 1 and the causal-limit EOS, the J0740+6620 mass and radii, the per-tick speed bound used in item 7 (taken from an earlier campaign result, not rederived here), the one-dimensional two-tiling free walk as a proxy of the three-dimensional tick, the skip region and schedules, the core radius, f_c and the luminosity scale of the estimate, and a uniform measure over far phases in log l_far. Forced, given those: lapse ratio = edge ratio under the fixed step; the floor condition alpha_c >= w L/l_far; that split history cannot change edge ratios; the enthalpy form of alpha_c and the Buchdahl limit; the maximum-mass values and J0740 values for the listed EOS; the excitation counts and pumping of the proxy. Not claimed: a bound on alpha_c for every causal EOS beyond the listed ones; a stable-branch scan finer than the sampled grid; a three-dimensional skip computation; that the luminosity estimate is a prediction beyond its supplied inputs; that the wider window is the register's unique floor rule; collapse through a horizon, which needs the shift law.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's fixed step, edge registers, window and split, and the records of the actuality law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/static_redshift_on_fixed_step_edges_needs_a_wider_edge_window_while_split_history_cannot_help_and_skipped_half_ticks_heat_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 5 s with about 90 MB resident, prints about 5.9 kB and ends with `TOTAL: PASS=18 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
