# Batch 9 (U9-R2), first bounded pass: the anisotropy's zero-Hessian equality decided by an exact cubic term

Unit `J:derive:deferred-20260924-stability:a1`, worker `w-macbookpro9927a-jbeaa` (Claude Opus 5.5), 2026-09-25.
This is an owner-requested deferred-science recovery.

- **Provenance.**
  - origin/main is `cf1b55b9e574e3c118e37b5bb504af9fd8ca8d34`.
  - The batch landed in `fbe9f0f0154402d8afa07a8d12c920df2d9d0848`. Blocks 84, 85, 88 and 89 are byte-identical there and on origin/main.
  - All 52 frozen sources of PRs 8652, 8657, 8665 and 8678 match the manifest SHA256 (check.py Q1; `RECOVERY_STATUS.json`, built by `make_status.py`).
- **Related work by this worker (disclosed).**
  - `the-anisotropic-state` a1 (label `w-macbookpro90c72-j5081`; Grok-refereed "HIT: confirmed") worked block 89's log-rate path. It covered convexity, F″(0), the absence of a global minimum, and the walk.
    - Its cubic, E_sea‴(0) = −6.94, was only executed. Here it is reproduced exactly as −6.9362 (step 3).
    - That unit did not treat block 88's arithmetic-mean path.
  - Related problems named by the task, with their outcomes:
    - `the-record-gas-chessboard-threshold` a2: #9034;
    - `the-two-wall-level-rule-on-every-ring` a2: #8763;
    - `the-reach-three-coupling-beyond-first-order` a3: no HIT.
    - These answer different questions (U9-R1/R3 topics) and are not reused.

## 0. Target chosen

The review finding U9-R2 lists "zero Hessian equality and unexamined directions remain open". Both landed notes leave the equality case of the traceless anisotropy open:
- **Block 88 T3:** "A zero anisotropy coefficient alone does not settle a minimum; higher orders can matter."
- **Block 89:** "at equality higher-order analysis is needed", and T3 "neither this nor T2 proves global stability".

The frozen PR8665 source adds its own open items:
- `GOAL_block88.md` fixes "single-axis and traceless modes", and nothing beyond them.
- `CHECKER_block88_findings.md` item 5 records "Endpoint property executed, not proved" (W3, 0 of 301 α).

This pass decides the anisotropy's equality case in both supplied constraints. It then reduces the endpoint property to one exact inequality and leaves that open.

## 1. Setting (landed notes)

- **Rates.** Positive bond rates on the three axes, with the anisotropy traceless in the constraint's own variable:
  - block 88 (fixed arithmetic mean): (1+2ε, 1−ε, 1−ε);
  - block 89 (fixed mean log rate): (e^{2ε}, e^{−ε}, e^{−ε}).
- **The law.** In either variable its cost is 36βε² per site, exactly quadratic (block 88 T1; block 89 premises).
- **The sea.** E_sea(ε) = −F(ε), with F(ε) = ⟨√Q_ε⟩ the continuum zone average.
  - Q = (1+2ε)²a + (1−ε)²b for block 88, and Q = e^{4ε}a + e^{−2ε}b for block 89.
  - Here a = s_x², b = s_y² + s_z², S = a + b = |s|², s_j = sin k_j and u_j = s_j².
  - σ₁ = S, σ₂ = Σ_{i<j}u_iu_j and σ₃ = u₁u₂u₃.
- **Path energy.** E(ε) = 36βε² − [F(ε) − F(0)].
- **Known quadratic coefficients (landed).**
  - Block 88: 36β − χ_a/2, with χ_a = 9⟨ab/S^{3/2}⟩.
  - Block 89: 36β − (χ_a + 2J)/2, with J = ⟨|s|⟩.

## 2. Statement

**(a) The cubic coefficients.** The cubic coefficient e₃ of E_sea along the path is:
- arithmetic mean: e₃ = (3/2)⟨(σ₁σ₂ − 9σ₃)/|s|⁵⟩ = (3/2)⟨Σ_i u_i(u_j − u_k)²/|s|⁵⟩ > 0;
- mean log rate: e₃ = −⟨(σ₁³ + 9σ₁σ₂/2 + 81σ₃/2)/(3|s|⁵)⟩ < 0.

**(b) At each quadratic threshold** (β = χ_a/72, respectively (χ_a + 2J)/72), E(ε) = e₃ε³ + O(ε⁴). So ε = 0 is not a local minimum along the path.
- In linear rates it descends towards ε < 0: a weaker special axis, heading towards planes.
- In log rates it descends towards ε > 0: a stronger special axis, heading towards chains.

**(c) Linear rates, above threshold.** For every β ∈ (χ_a/72, χ_a/72 + 1.22·10⁻⁵), the path point ε = −0.00667 has E < E(0), although the quadratic coefficient is positive.

**(d) Float only (not claimed exact).** The linear path's minimum leaves ε = 0 at β* ≈ 0.02715, near ε ≈ −0.37. The quadratic threshold is 0.02615.

## 3. Steps

**Step 1: differentiation under the average. PROVED.**
- For |ε| ≤ ε₀ ≤ 1/3 and S > 0, Q_ε lies between m₀S and M₀S, where m₀ = (1−2ε₀)² and M₀ = (1+2ε₀)² for block 88. The log case is analogous.
- √Q_ε is smooth in ε, and each ε-derivative is homogeneous of degree 1 in s, so it is bounded by C_n|s|, which is integrable.
- Dominated convergence therefore gives F^{(n)}(ε) = ⟨∂_ε^n√Q_ε⟩. The set S = 0 is null.
- **Axis symmetrisation.** The zone measure is invariant under permuting the axes, and every integrand depends only on (u₁, u₂, u₃). So ⟨g⟩ equals the average of g's three special-axis versions.
- **The domain [0, π/2]³.** sin² has period π and is symmetric about π/2. So the zone average equals the average over k ∈ [0, π/2]³, on which each u_j = sin²k_j is increasing.

**Step 2: the arithmetic-mean path. PROVED; CHECKED S1.**
- Q = S + D₁ε + D₂ε², with D₁ = 4a − 2b and D₂ = 4a + b.
- Its discriminant is 4D₂S − D₁² = 36ab, so d²√Q/dε² = 9ab/Q^{3/2} exactly, for every ε. That makes √Q convex and E_sea concave in ε.
- The Taylor coefficients of √Q at 0 are:
  - first order: D₁/(2|s|), whose three axis versions sum to zero, so F′(0) = 0;
  - second order: 9ab/(2|s|³), giving block 88's χ_a;
  - third order: −D₁D₂/(4S^{3/2}) + D₁³/(16S^{5/2}) = −(9/2)ab(2a − b)/S^{5/2}.
- The axis average of the third-order term is −(3/2)(σ₁σ₂ − 9σ₃)/S^{5/2}.
- The identity σ₁σ₂ − 9σ₃ = u₁(u₂−u₃)² + u₂(u₃−u₁)² + u₃(u₁−u₂)² ≥ 0 holds, with equality only on u₁ = u₂ = u₃.
- Hence F₃ = −e₃ with e₃ = (3/2)⟨Σ u_i(u_j−u_k)²/|s|⁵⟩. The integrand is continuous on S > 0 and positive on an open set, so e₃ > 0.

**Step 3: the mean-log path. PROVED; CHECKED S2.**
- The same expansion applies with Q = e^{4ε}a + e^{−2ε}b.
- First order: the axis versions cancel.
- Second order: the axis average is 9ab/S^{3/2} + 2|s|, which is block 89's χ_a + 2J.
- Third order: the axis average is (σ₁³ + 9σ₁σ₂/2 + 81σ₃/2)/(3S^{5/2}), in which every term is ≥ 0. So e₃ = −(that average) < 0.
- **Float (N1).** e₃ = −1.156039, i.e. E_sea‴(0) = −6.9362, the earlier unit's −6.94. In arithmetic mean, e₃ = 0.183258. Finite differences agree to 10⁻³.

**Step 4: the equality case. PROVED.**
- The law has no cubic part, so E(ε) = ηε² + e₃ε³ + O(ε⁴), with η the landed quadratic coefficient.
- At η = 0 the sign of e₃ε³ decides: E < 0 for small ε of sign −sgn(e₃).
- So the uniform rates are not a local minimum along the path at either threshold. The anisotropy's local stability along the path is exactly η > 0.
- This settles the equality clauses of block 88 T3 and block 89 T3 for this path only.

**Step 5: a rigorous window above threshold, arithmetic mean. PROVED; CHECKED R1, R2.**
- **Fourth derivative.** d⁴√Q/dε⁴ = −(27/2)ab[2D₂Q − (5/2)Q′²]/Q^{7/2} (symbolic).
- **Bound.** On |ε| ≤ ε₀ we have |Q′| ≤ 4(1+2ε₀)S, D₂ ≤ 4S and ab ≤ S²/4. Hence |d⁴√Q| ≤ 162M₀|s|/m₀^{7/2}, and averaging with J ≤ √(3/2) (Jensen; ⟨S⟩ = 3/2) gives |F⁗| ≤ 162M₀√(3/2)/m₀^{7/2}.
- **Constants.** With ε₀ = 1/100, K := sup|F⁗|/24 ≤ (27/4)(51/50)²(12248/10⁴)/(49/50)⁷ ≈ 9.9080, an exact rational.
- **Lower bound on e₃.** Exact lower sums on 24³ boxes of [0, π/2]³ use the fact that u is increasing in k: on each box u_i ≥ u_i,lo, (u_j−u_k)² ≥ gap², S ≤ S_hi, and √S_hi is rounded up. They give e₃ ≥ 0.13210.
- **Conclusion.** Put t = e₃,lo/(2K) = 0.00667 ≤ ε₀. Then E(−t) ≤ ηt² − e₃t³ + Kt⁴ ≤ t²(η − e₃,lo²/(4K)), which is < 0 for 0 < η < 4.403·10⁻⁴.
- In β, that is (χ_a/72, χ_a/72 + 1.22·10⁻⁵).

**Step 6: the global picture. Float only (N2).**
- **Arithmetic mean.**
  - The path is bounded: the rates stay positive for ε ∈ (−1/2, 1).
  - A scan of 751 values of ε gives min E < E(0) iff β < 0.02715, attained near ε = −0.37.
  - The endpoint ε = −1/2 alone (the special axis decoupled) gives 0.02704. The quadratic threshold is 0.02615.
  - So the window in which the path's minimum is away from ε = 0 while the quadratic coefficient is positive is about 4% of β, extending towards planes.
- **Log rates.** The path is unbounded below for every β, since F grows like e^{2ε}⟨|s_x|⟩; this was refereed in the-anisotropic-state. So only step 4's local statement carries information there.

**Step 7: unexamined intermediate-q directions, reduced and left open. PROVED reduction; formula ASSUMED; float margins N3.**
- **The claim.** The frozen W3 "endpoint property" says that f(q) = χ̃(q)/2 − α(1 − cos q) is maximised at q ∈ {0, π} for every α ≥ 0.
- **Chord lemma.** Write c = 1 − cos q ∈ [0, 2] and X(c) = χ̃/2, with chord slope s = (X(2) − X(0))/2 ≥ 0. Then the endpoint property holds for all α ≥ 0 iff X lies on or below its chord.
  - *If X is below its chord:* X(c) − αc ≤ X(0) + (s − α)c ≤ max(X(0), X(2) − 2α).
  - *If X(c₀) lies above the chord:* at α = s the point c₀ beats both endpoints.
- **The response function.** From the second-order trace formula (Daleckii–Krein, ASSUMED):
  χ̃(q) = ⟨sin²(k₁ + q/2) G(sin k₁, sin(k₁+q); m)⟩,
  with G(x, y; m) = [x/√(x²+m²) − y/√(y²+m²)]/(x − y) and m² = s_y² + s_z².
  - It reproduces χ̃(0) = χ_a/9 and χ̃(π) = χ/3, and matches the frozen ring values.
- **Margins.** The chord margins are positive at the sampled q, but shrink to 0.0009 at q = π − 0.05. The q → π expansion (a possible p² log p term) decides it.
- **Open:** the chord inequality on all of [0, π].

## 4. ASSUMED
- The Daleckii–Krein second-order trace formula. It is used only for step 7's float formula; no exact claim rests on it.
- Standard calculus: dominated convergence, Taylor's theorem with Lagrange remainder, and Jensen's inequality.

## 5. First failing step and next obligations
- Nothing fails for the stated residual. Step 6's global window is float only, and step 7 is open.
- The ranked obligations are in `RECOVERY_STATUS.json`:
  1. the chord inequality for χ̃(q) (the endpoint property of W3);
  2. the equality case of block 89's log-rate alternation: it is even in δ, and its quartic coefficient involves the divergent ⟨S^{−3/2}⟩, so a δ⁴ log expansion is needed;
  3. the crowd-threshold bounds of block 85;
  4. U9-R3 wall spectra (PRs 8660, 8662);
  5. U9-R1 (PRs 8626, 8628, 8632);
  6. U9-R4/R5 (PRs 8692, 8696, 8703, 8710).

## 6. Review demotions preserved
- Two path Hessians, or a path cubic, do not classify all perturbations. No complete instability map is claimed.
- No physical transition, formation, dynamics or clock normalisation is inferred. The two constraints remain different supplied models.
- Block 84's restricted sufficiency and the finite-grid cusp caveats are untouched. Historical scans stay historical.

## 7. Reproduce
From the repository root, `python3 probes/work/derive/deferred-20260924-stability/w-macbookpro9927a-jbeaa/check.py` runs in about 16 s. `make_status.py` regenerates `RECOVERY_STATUS.json`, and needs the frozen heads fetched.
