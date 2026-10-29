Reviewer model: claude-opus-5-5

# SRCAN55 — the analyticity route to SRC (source-inserted RG) — Opus 5.5 worker deliverable

UTC start: 2026-10-29T01:40:42Z
Write scope: this file and `checks/sa55_*` only. No git. Append-only.

## PRE-STATED (written before any derivation; statements only)

### Targets
- **T1 (perturbed RG).** Formulate the layer-1 RG with a complex, position-dependent coupling
  g(x) = g + δg(x) (or the equivalent perturbation of 1/g², whichever is the parameter the banked
  estimates actually carry), δg slowly varying and small on the scale set by the contraction margin.
  List every place the coupling enters BFT-0/1/2 (Theorem BFT-E on 𝒞_glob, GV55.md), the composite
  contraction (Theorem K^{(σ)} for 𝔉_k), and the soft kernel, and for each say whether the banked
  estimate survives uniformly on a complex polydisc — CONFIRMED / NOT-VERIFIED / REFUTED per entry.
- **T2 (Cauchy → SRC-κ).** Derive SRC-κ (separated conditional cumulant bounds, exponential decay at
  ℓ_ref, uniform in a, R, small coarse fields) from (analyticity on the polydisc) + (Cauchy estimates) +
  (a stated locality property), and say exactly which locality is needed and whether BFT-3 as drafted in
  BFT34_55.md supplies it.
- **T3 (scope).** State precisely what the route does NOT cover: large coarse fields (UNIV55 N3), SRC-M
  (the eight O(g_bare²) matching constants), the per-step RLF conditioning on U_K, and anything else found.

### What would count as a refutation of the route (or of a step of it)
- **R1 (generation).** If the 47 local gauge-invariant functionals of SRC-κ are NOT all obtained as
  derivatives of the effective action with respect to local couplings of terms the layer-1 RG already
  carries (or can carry within its banked norms), then "analyticity in g(x)" alone does not give SRC-κ
  for all 47; the route then needs sources for operators outside the coupling family, i.e. a different
  (larger) perturbation class.
- **R2 (non-analytic dependence).** If any banked estimate depends on the coupling non-analytically —
  e.g. through large/small-field indicator functions with g-dependent thresholds, a background field
  defined by a real minimisation of a g-dependent functional, |g| or Re(1/g²) positivity used with a
  margin that a complex perturbation of the stated size destroys, or a reflection-positivity /
  monotonicity step — then analyticity on the polydisc fails at that point unless that dependence is
  frozen (held at the unperturbed g) and the frozen version is shown still to close.
- **R3 (quantitative).** Cauchy's estimate on a polydisc of radius r per site costs r^{-n} for an
  n-point cumulant. If the admissible radius (set by the contraction margin) is too small relative to the
  sup bound of the perturbed effective action for the resulting cumulant bounds to have the size and
  uniformity SRC-κ demands (uniform in a and R; correct power of g), the route fails quantitatively, and
  I will say by how much.
- **R4 (locality).** If the exponential decay at ℓ_ref in SRC-κ needs a decay of the *derivative*
  structure (connected/truncated in the separated points) that analyticity + sup bounds do not supply
  without an additional cluster/polymer locality statement, then BFT-3-type locality is a genuine extra
  input and I will state it as such (not as "inherited automatically").
- **R5 (slowly varying / (F_R)).** If the slowly-varying condition is not compatible with Cauchy
  estimates at separated points (Cauchy needs independent per-site radii, slowly-varying constrains the
  perturbation to be smooth), the two requirements conflict and I will state the resolution or the gap.

### Verdict labels
CONFIRMED (I re-derived the load-bearing step), NOT-VERIFIED (could not settle; say what is missing),
REFUTED (give the correct statement and derivation). "The file says PROVEN" is not evidence.

