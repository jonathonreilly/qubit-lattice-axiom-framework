---
claim_id: skip_patterns_carry_the_tick_fraction_on_clocks_but_every_skip_front_makes_pairs_so_the_lapse_is_read_into_the_cube_step_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Can a discrete, local tick-or-skip rule carry CL-1's adopted tick fraction N = 1 + Phi? Exact: a deterministic error-diffusion (sigma-delta) skip gives tick count floor(a0 + sum N), error < 1 tick, Allan deviation proportional to 1/tau (fitted slope -1.03); a skip drawn with independent odds per site gives sqrt(N(1-N)/tau) (slope -0.51). Against clocks neither is excluded: 7.6e-48 at 1e4 s (bound 1e-18) and <= sqrt(t_P/1 s) = 2.3e-22 at 1 s (best clocks ~1e-16). Exact (exhaustive): on the two offset tilings, the only site sets that are unions of whole cubes of both tilings are the empty set and everything (2 of 4096 on a 12-ring, 2 of 256 on the 4^3 torus), so every skip front leaves sites with an unpaired half-tick. Finite diagnostic (1D split-step Floquet sea, 64 sites): each front boundary creates 0.10 eps^2 pairs (eps = 0.05, 0.2, 0.5) of energy ~2.1 eps per tick, which persist; a uniform skip creates none. Exact: any coupling of two sites' skips disagrees at rate >= |N_i - N_j|, attained by a shared-threshold rule (skip iff u(t) < 1 - N, u the van der Corput sequence of the global step count: measured 1.01 x |dN|); independent rules and sigma-delta (after desynchronising in |Phi|/|dN| ticks) disagree ~30 times more on the test ring, and pair creation tracks disagreement (ratio 0.5-0.6 to the per-event value for all four rules). Estimate: even the minimal rule makes ~1e102 W/m^3 of vacuum pairs in Earth's field (eps = 0.05; ~1e103 at 0.5), so every skip reading is excluded. Finite diagnostic: reading N into the cube's step instead (sin eps_cube = N sin eps0, mu = m N; every site ticks every half-tick) scales the low quasi-energies by N to 1e-4 and, being static for a static source, creates 0 pairs (2e-15 over 1500 ticks). Self-consistency (3D, 21^3, point source): every skip pattern's measured fraction solves the hinge-sum stationarity equation, to 12/(T |K psi|) (sigma-delta), log T/T (shared threshold), T^-1/2 (independent odds). Not derived: the 3D per-bond pair yield (1D value used), eps0's value, nonlinear self-consistency."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/skip_patterns_carry_the_tick_fraction_on_clocks_but_every_skip_front_makes_pairs_so_the_lapse_is_read_into_the_cube_step_2026_10_23.py
---

# Skip patterns carry the tick fraction on clocks, but every skip front makes pairs, so the lapse is read into the cube step

Claim type: bounded_theorem.
Primary runner: `scripts/skip_patterns_carry_the_tick_fraction_on_clocks_but_every_skip_front_makes_pairs_so_the_lapse_is_read_into_the_cube_step_2026_10_23.py` (23 PASS, 0 FAIL, ~1 s, ~130 MB).

## Question

CL-1's adopted clause ("Tick fraction and tick offsets") treats a site's tick fraction N as a continuous response variable of the hinge sum, and it lists "what sets a site's skips" as open. On each global step a site either ticks or skips, so N would be a long-run fraction of discrete ticks. Is there a discrete, local, non-fitted skip rule whose fraction reproduces N = 1 + Phi without noise that measurement excludes?

## Rules used (rederived where used)

- CL-1. The half-ticks alternate between two tilings by 2x2x2 cubes offset by (1,1,1). Each species applies exp(-i(eps - mu/2)R) on even cubes and exp(+i(eps + mu/2)R) on odd cubes. The light-crossing sentence fixes the per-tick proper time. That pin is the reason a free N must otherwise be realised by skips.
- The adopted tick-fraction clause, with its static solution from tick-skip-gamma (lap psi = -4 pi G rho, Phi = -psi) and one-g (the static kernel is the lattice Laplacian).
- CL-2. Skip or tick is a transition (staying included). Its odds are the target fraction.
- A skip means a cube applies only if none of its sites skips. The opposite convention gives the same counts (B1 is convention-free).

## Results

### Theorems (exact)

1. Sigma-delta (A1, A2). With accumulator a += N and a tick when a >= 1, the count is n(T) = floor(a0 + sum_t N_t), so |n - sum N| < 1 for every T, including a varying N. The phase error is bounded, so the Allan deviation is <= sqrt 2 t_tick/tau.
2. Independent odds (A3, A4). The count is binomial with variance T N(1-N). That is white frequency noise, sigma_y = sqrt(N(1-N) t_tick/tau) <= sqrt(t_tick/tau).
3. A skip front cannot be clean (B1, B2). For a skip to leave no site with one half-tick but not the other, the ticking set must be a union of whole even cubes and also a union of whole odd cubes. Proof: on any axis line, even cubes cover the pairs {2j, 2j+1} and odd cubes cover {2j+1, 2j+2}, so the set is the whole line or none of it. Repeating this along each axis leaves only the empty set or everything. Exhaustive checks: 2 of 4096 sets on a 12-ring and 2 of 256 cube unions on the 4^3 torus.
4. Discordance bound (C1). For Bernoulli marginals p_i and p_j, every coupling has P(exactly one skips) >= |p_i - p_j|. The comonotone (shared-threshold) coupling attains this. Over a run, neighbours must disagree at least |n_i - n_j| ~ |N_i - N_j| T times. No rule does better.
5. Step-angle reading (C6, E1). If N enters the cube's step (sin eps_cube = N sin eps0, mu = m N) and every site ticks every half-tick, a static source gives a static update. Its Floquet vacuum is then exactly stationary.

### Finite diagnostics

- Pair yield (B3-B5). Split-step Floquet sea, 64 sites, lower quasi-energy band filled.
  - A front boundary creates c eps^2 pairs, with c = 0.101, 0.099 and 0.108 at eps = 0.05, 0.2 and 0.5.
  - The energy per pair is 2.10, 2.15 and 2.14 x eps hbar/tick (band edge).
  - A uniform skip creates < 1e-12 pairs. The created pairs persist under later full ticks (1e-15 change).
- Gradient ring (C2-C5). 1500 ticks, N from 1 to 0.95.
  - The shared van der Corput threshold disagrees at 1.013 x mean|dN| per bond per tick.
  - Independent odds disagree at 1.0 x 2N(1-N). Sigma-delta with common or random offsets reaches the same order, about 30 times the minimum.
  - Pairs created / (c eps^2 x disagreement events) = 0.60, 0.49, 0.56 and 0.56 for the four rules.
  - Every rule reproduces the target fraction (max |n/T - N| <= 1e-2).
- Step-angle reading (C6, E1). It creates 2.4e-15 pairs over 1500 ticks. The lowest quasi-energies scale by N to 9.5e-5 at eps0 = 0.05 and 0.2, with N = 0.7 and 0.9, so clocks run at the lapse.
- Self-consistency with the hinge sum (F1-F4). 21^3 Dirichlet box, point source, GM = 0.05.
  - The stationarity residual |K(Phi_meas + psi)|/|K psi| is 1.3e-2, 1.3e-3 and 1.3e-4 at T = 1e3, 1e4 and 1e5 for sigma-delta.
  - It is 9.7e-5 at T = 2^16 for the shared threshold. Independent odds give 4.4e-2 at T = 1e4 and 4.4e-3 at T = 1e6.
  - The fixed point is reached in one pass at linear static order, because the lapse equation does not contain N.
  - The measured -Phi r/GM is 0.90, 0.78 and 0.67 at r = 2, 3 and 4 (Dirichlet screening; continuum 1). Axes agree to 1e-5.

### Estimates against measurement

- Clocks. Sigma-delta gives 7.6e-48 at 1e4 s against 1e-18. Independent odds give 2.3e-22 at 1 s (2.3e-25 with |Phi| = 1e-6) against ~1e-16. Clock comparisons exclude neither rule. Phase random walk under independent odds after 4e17 s: ~1e-16 s (negligible).
- Vacuum pairs (D1). Assumption: the 1D per-boundary yield applies per discordant gradient bond, and the tick is sin(eps) a/(sqrt 3 c) with a = sqrt(8 pi) l_P (CL-1 light speed). The minimal rule then disagrees (g/c^2) a times per bond per tick. Power density ~ 0.6 c E_pair eps hbar g/a^4 (proportional to eps): 7.6e101 W/m^3 at eps = 0.05 and 8.3e102 at 0.5. It would stay below 1 W/m^3 only if eps < ~1e-102. Independent and sigma-delta rules are ~1.6e41 times worse (2|Phi|/(|grad Phi| a) at Earth's surface). Every skip reading is excluded by roughly 100 orders.

## Verdict and the rule to name

- No skip rule works. Clock noise is never the problem. Every skip front is a lattice-scale unpaired half-tick that creates vacuum pairs, and the minimum disagreement rate is forced by the gradient of N (theorem 4).
- Proposed working rule (lapse-in-the-step), replacing "what sets a site's skips":
  > "Every cube ticks every half-tick. The tick fraction N of the tick-fraction clause is the lapse read into the cube's step: sin(eps_cube) = sqrt 3 N rms sqrt(gamma^ii), with rest phase m N per tick."
  - This is CL-1's own light-crossing sentence with N taken from the response, not pinned.
  - Every tick-fraction result (gamma, beta, waves, one G) used N only as a continuous field, so all of them carry over. The count reading's "one bond per taken tick" becomes coordinate light speed N/Omega per tick.
- Gate.
  - (1) No number is chosen.
  - (2) No observed structure; the rule names only cubes, steps and edges.
  - (3) Predictions it was not built for: zero vacuum pair creation in any static field; clock rate equal to N up to O(eps0^2); a ceiling N <= 1/(sqrt 3 sin(eps0) rms sqrt gamma^ii) on the lapse (UNTESTED).
  - (4) Bends CL-1's "the lapse is not free" sentence. No axiom is touched.
  - PASSES.
- Global step and Lorentz.
  - Skip rules need the global step index: sigma-delta iterates on it, and the minimal rule reads its binary digits. Their tick pattern therefore lives on the lattice slicing, and pair production would depend on the frame. They are moot because they are excluded.
  - The step-angle reading adds no pattern, and no slicing beyond CL-1's existing global half-tick. Its Lorentz violation is CL-1's existing dimension-6 cubic term.
  - For scale: any skip-count residual would be <= t_tick/tau ~ 5e-44 at 1 s, far below Hughes-Drever/SME clock-anisotropy bounds (~1e-27 to 1e-29 fractional). This is a rough comparison.

## Smuggling review

- Supplied:
  - the 1D split-step sea as the yield model (the 3D CL-1 yield per bond is not computed);
  - the lower-band Floquet vacuum;
  - the skip convention for cubes;
  - eps0, whose value the register does not state;
  - the van der Corput sequence as the shared threshold (the golden-ratio Kronecker sequence gives the same up to log factors);
  - the 1 W/m^3 scale, which is generous.
- Forced:
  - the unpaired half-tick (theorem 3);
  - the discordance floor (theorem 4);
  - clock-noise scalings;
  - stationarity of the static step-angle update.

## Boundary

- No 3D CL-1 cube-unitary yield.
- No nonlinear (beta-order) self-consistency.
- No moving-source adiabaticity bound for the step-angle reading. It is expected to be power-suppressed in gradient x wavelength, but that is not computed.
- No link or edge-register interplay with eps_cube.

## Uses / narrows

- Uses: CANDIDATE_LAWS_v3 CL-1 (tick-fraction clause, light-crossing sentence), CL-2 (transport odds), agents/tick-skip-gamma (static solution), agents/one-g (Laplacian kernel).
- Narrows: the R-a count reading of agents/random-connectivity. "Lapse = taken-tick fraction" is kinematically fine but dynamically excluded. The tick-fraction clause's open item "what sets a site's skips" is answered: nothing may. N is the step.
