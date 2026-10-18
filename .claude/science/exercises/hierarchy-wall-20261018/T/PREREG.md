# T-SPIRAL pre-registration (written 2026-10-18 ~16:50Z, before any run)

Readings are fixed by `../TESTS.md` (SPIRAL-NATIVE / SPIRAL-ABSENT / OPEN) and are not changed here.

## Rule (landed objects only; nothing invented)
Two-state menu s = ±1 on the torus Z_L^d, d = 2 and 3. All sites start unrecorded.
- **Content (neighbour bias K).** Binary specialisation of class (P) of
  `ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_..._2026-09-06.md` (r(s|η) ∝ ψ(s) Π φ(s,η_y), φ symmetric,
  ψ uniform by possibility symmetry; φ(s,t) = e^{K s t}), formation reading (condition on recorded
  neighbours only): P(s | N) = e^{K s m}/(2 cosh K m), m = sum of recorded neighbour values.
- **Order (formation-rate coupling μ).** Record-determined clock of
  `FORMATION_RATE_FUNCTIONS_..._2026-09-24.md` (hazard F(R), constant between neighbour-record events):
  hazard e^{μ n}, n = number of recorded neighbours. μ = 0 is the uniform race of
  `ORDER_LAWS_FOR_EXTENDED_SOLDERED_SUPPORTS_..._2026-09-22.md`.
- **Irreversible:** a record never unlocks. Run until every site is recorded; the readable object is
  the finished record field. Both functions are cubic-covariant and nearest-neighbour; the hazard is
  even under s → −s.
- K < 0 maps to K > 0 by the sublattice flip on bipartite Z^d, so K ≥ 0 only.
- Why order-sensitive: `ORDER_BLIND_POSITIVE_FORMATION_IS_A_ONE_DEPENDENT_GIBBS_FIELD_..._2026-10-16.md`
  shows order-blind positive rules give 1-dependent fields (no nontrivial fixed point at all). The binary
  heat-bath rule is order-blind only at K = 0, so it lies outside that theorem.

## Method: matching Monte Carlo RG on the finished field
- Simulation: exact rejection-free kinetic Monte Carlo (hazard classes n = 0..2d), numba.
- Blocking: majority rule on b^d blocks, ties broken by a fair coin; b = 2 and b = 3.
- Observables on a (blocked) field: S2 = {nn correlation, plaquette 4-point};
  S5 = S2 + {face-diagonal pair, axis distance-2 pair, (2^d-block magnetisation)^2}.
- Matching (Swendsen-style, equal final sizes): R(θ) is defined by
  A^{(L)}_{n+1}(θ) = A^{(L/b)}_{n}(R(θ)), θ = (K, μ), primary n = 1, secondary n = 0;
  least squares in units of the observables' standard errors when |S| > 2.
- Grid: tanh K ∈ {0, 0.1, …, 0.9, 0.95}, μ ∈ {−3, −2, …, 9}. Each observable is fitted by a smoothing
  bivariate spline in (tanh K, μ) for each lattice size; R is solved on the surrogates.
- Fixed points: roots of R(θ) − θ from a seed grid, kept when inside the grid with residual < 1e-3.
  Jacobian of R by central differences on the surrogates; eigenvalues; Re/|Im| reported.
- Sizes: 2D b=2: L = 128 vs 64 (final 32); 2D b=3: L = 162 vs 54 (final 18); 3D b=2: L = 32 vs 16
  (final 8); 3D b=3: n = 0 only, L = 36 vs 12.
- Variants for "stable under block size and method": b ∈ {2,3}, S2 vs S5, n ∈ {0,1}.
- Side diagnostic: second-moment correlation length ξ of the fine field at every grid point.
- Memory: capped.sh (0.4 GB), one process at a time.

## Prediction stated before running (suggested, not proved)
Every finite (K, μ) has a finite causal past per site (decreasing-formation-time paths end at nuclei;
nucleation keeps positive density for finite μ, grain size ~ e^{μ/(d+1)}), so ξ is finite in the
interior and a real-space RG fixed point (ξ ∈ {0, ∞}) can sit only on the boundary: K = 0 (iid
coins) or μ = +∞ (single-nucleus growth). Both boundaries are invariant sets of the flow, so the
Jacobian there is triangular and its eigenvalues are real. Expected reading: SPIRAL-ABSENT for this
class, with any interior "fixed point" flagged as a truncation artefact if it moves with b or S.
If an interior complex pair appears in every variant with Re/|Im| ≤ 0.05, the reading is SPIRAL-NATIVE
regardless of this prediction.

## Scope
Only the class above (two couplings, one content rule, one clock family). No claim about v.

## Dated follow-up (2026-10-18T17:00Z): T-SPIRAL-2 added by the coordinator
`../TESTS.md` gained T-SPIRAL-2 (registered 16:56Z by the coordinator, without seeing these results).
It reached me at about 16:59Z, after the pre-registered grid runs (2D b=2,3; 3D b=2,3), the analysis,
and two 3D finite-size extension runs (`ext.py`, `ext2.py`, both labelled as not pre-registered) had
finished. I will report under both tests. Nothing above is changed.
- T-SPIRAL-2 readout, applied to the same fixed points: y = ln(λ)/ln b per e-fold of scale.
  SPIRAL2-NATIVE needs |Re y| ≤ 0.06 and |Im y| ≥ 1, the sign of the first Lyapunov coefficient, and
  stability across b and method. SPIRAL2-ABSENT: all real, or |Re y| ≥ 0.2.
- Also reported: (i) the RG here acts on the frozen (finished) record pattern, not on the spacetime
  process; (ii) whether a non-trivial fixed point exists under the absorbing (fully recorded) state;
  (iii) truncation-artefact checks. The exact-RG criterion used for (iii) is fixed now: an exact block
  map gives ξ(R θ) = ξ(θ)/b, so a fixed point needs ξ ∈ {0, ∞}. Any fixed point of the truncated
  matching at a coupling where ξ is finite and nonzero is a truncation artefact. One further check is
  planned: measure ξ at the 3D near-fixed points with L = 96 and 128.
