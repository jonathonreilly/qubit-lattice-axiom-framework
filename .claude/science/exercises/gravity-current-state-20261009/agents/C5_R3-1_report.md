# C5 R3-1: Γ_L-covariant laws on L₇ — existence, locality, per-realization EFT

**Worker.** Claude Opus 5.5 (probe R3-1), same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 12:27Z to about 13:30Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R3-1/`: this report; `r31_invariants.py/.out`, `r31_counting.py/.out`, `r31_lv_orbitsum.py/.out`, `r31_lv_scaling.py/.out` (+ `r31_lv_scaling_lib.py`), `r31_bragg_resonance.py/.out`, `r31_multishell.py/.out`, `r31_multishell2.py/.out`.
**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` (in full); `TESTS.md:2302-2704` (C5 method, round-1 results, round 2, round 3; R3-1 at `:2659-2670`); `agents/C5_O5_synthesis.md` (§0–§1); `SUMMARY.md` §§15–21; `PRICE_NOTE.md` (rows, prices, v6 delta headers); `C5_O1_referee.md`, `C5_O1_report.md` §3.3–3.6; `C4_B1_referee.md`; `RFW_F1_referee.md`; `R2-1/R2-1_report.md` (Theorem T; its referee run disconnected, `ref_R2-1/codex_run.log` tail, so Theorem T is unrefereed); `R2-2/R2-2_report.md`; `ref_R2-2/REFEREE_VERDICT.md` (**CWC**, arrived during this run).
**Status of the input.** The R2-2 referee confirms LRL's invariance in law, cocompactness of Γ_{L₇}, the uniform hard core and the Bragg gap |G²| ≥ (2π)²/7 (`ref_R2-2/REFEREE_VERDICT.md:9-16`). It leaves open exactly what R3-1 asks: "convergent effective dynamics … and per-realization O1 bounds remain open" (`:20,24`). So nothing below is conditional on a rejected LRL claim.
**Labels.** *proved* = complete argument here (same family, unrefereed); *proved mod RECALLED* = complete except for a named standard theorem; *checked* = numerical/exact computation in the scratch files; *suggested* = argued only; *reading* = interpretation; *comparator* = outside literature.

---

## 0. In plain words

- **What a law on one LRL realization can look like.** One realization is the lattice L₇ (boosted and shifted). Its exact symmetries are the lattice shifts and the infinite group Γ_L of integral boosts. A law that respects them can do anything on a single site (so interactions like φ⁴ are fine and strictly local). But any coupling between two different sites must have the same strength for every pair related by a Γ_L boost, and each such family is infinite (about T² members within distance T). So **every hopping term is "equal weight to infinitely many partners"**. Couplings cannot fall off with ordinary distance at all; they can only fall off with the invariant interval |x²| (proper time).
- **"Power-law tails with s > 2" (supervisor's thread, item 2) is half right.** Averaging a frame-dependent power law |x|^{-s} over Γ_L converges exactly when s > 2 (checked: the count exponent is 2.000). But the averaged kernel is again constant on each infinite family. So the price is not "power-law quasi-locality"; it is causal-set-type non-locality: unbounded valency with non-decaying weights along each boost family.
- **Such laws still make sense, if they are retarded.** A coupling to the past light cone only (like the causal-set d'Alembertian) gives a symbol that converges absolutely for every complex momentum in the forward tube. A time-symmetric coupling (an ordinary action) converges for no momentum at all. No invariant law has an ordinary (square-integrable) dispersion function on the momentum torus, except an on-site constant (Lemma M below). Retardation is allowed here without a preferred frame, because Γ_L is infinite (O1's Lemma E needs a finite group).
- **Polynomial Lorentz invariance holds, but it says little.** Every Γ_L-invariant polynomial is Lorentz-invariant (proved; checked exactly to degree 6, and 2 graviton mass forms = Fierz–Pauli). But a realization's dispersion has no Taylor expansion at zero momentum. Its low-energy content is non-polynomial.
- **Non-polynomial Lorentz violation is there, per realization.** For a single proper-time shell, the in-tube orbit sum depends on the direction of the momentum relative to the realization. That dependence is a Γ_L-periodic ("automorphic") pattern. Its relative size falls like (κτ)^{1.3–1.4} (expected ~(κτ)¹), but its absolute size grows like κ^{-0.9…-1.0} as the momentum κ → 0. Spreading the kernel over many shells can cancel it strongly (to ×0.03) or only weakly (×0.1–1), depending on the weights. Kernels smooth over proper times much longer than the lattice step were not tested.
- **At real momenta, Bragg resonances fill the band.** A real in-band momentum can never reach another in-band momentum via a Bragg vector (the hard core; proved). But it sits near infinitely many Bragg resonance cones of heavily boosted Bragg vectors. For a photon, their number doubles with every doubling of the Bragg vector's size (checked 15 → 1378). The realization's dispersion function is singular on those cones. How strong that per-realization effect is in physical units was not computed.
- **The boost-wall theorems do not reach these laws.** C3, RB, RFW and R2-1's Theorem T all assume a regular (smooth, periodic) band on the momentum torus. On LRL no such band can exist (Lemma M). So the theorems neither apply nor are refuted.
- **Net: INCONCLUSIVE.** The construction exists and converges in the tube. Polynomial-order Lorentz invariance is proved. But per-realization non-polynomial Lorentz violation is present, and whether it is small in physical units is open. The registered expectation that non-analytic and umklapp terms are "suppressed below the gap" is **not confirmed**.

---

## 1. Against the FIXED readings (`TESTS.md:2664-2668`)

| Reading | Status |
|---|---|
| **PASS** — "an explicit convergent Γ_L-covariant law with power-law (or better) couplings whose per-realization low-energy physics is Lorentz-invariant at all polynomial orders, proved" | **Not met.** (i) Explicit, interacting and convergent: yes, but only in the forward tube and only for retarded kernels (Prop. R). No invariant law has a convergent symbol at real momenta (Lemma M). (ii) "Power-law or better couplings": impossible in the Euclidean sense. Every off-site coupling is constant on infinite orbits (Lemma A). It holds only in the invariant interval. (iii) "LI at all polynomial orders": proved (Prop. B1), but vacuous, because the per-realization symbol has no Taylor expansion at p = 0 (§4.2). Non-polynomial per-realization LV is present (checked, §4.3). A literal reading of (iii) is satisfied; the low-energy physics is not shown to be Lorentz-invariant |
| **FAIL** — "proved non-convergent for every decay class, or per-realization LV at dimension ≤ 4" | **Not met.** Convergent constructions exist: the Poincaré series for s > 2, and retarded kernels in the tube. The LV found is non-polynomial (automorphic in the direction of p, log-periodic in \|p\|). It is not a dimension ≤ 4 polynomial operator, and its IR scaling is checked only in the tube and only for single-shell or short-range kernels |
| **INCONCLUSIVE** | **Returned** |

**Against the expectation** (`TESTS.md:2670`: "PASS for (a) at s > 2, and for (b) at polynomial order. Non-analytic and umklapp terms are suppressed below the gap. INCONCLUSIVE on (c)"):
- (a): s_c = 2 is confirmed for the averaging map, but the locality reading is wrong (§3.3).
- (b): the polynomial half is confirmed. "Non-analytic and umklapp terms suppressed below the gap" is **not confirmed**: §4.3 finds relative LV only ∝ (κτ)^{~1} and absolute LV growing like 1/κ in the tube; §4.4 finds resonances at every scale for real null momenta.
- (c): INCONCLUSIVE, as expected.

**Supervisor's thread (`TESTS.md:2653-2656`), item by item:**
1. "Every polynomial invariant tensor of Γ_L is Lorentz-invariant" — **proved / checked**. "So a Γ_L-covariant law has no LV operator at any polynomial order, in each single realization. This would beat set B's dimension ≤ 4 protection" — the first half is true but vacuous; **the second half is not established**. The per-realization effective action is not polynomial, and it carries non-polynomial LV (§4.3).
2. "A summable Γ_L-covariant law does not exist" — **proved again, and strengthened to ℓ²** (Lemma M). "Power-law couplings ~|x|_E^{-s} with s > 2 give convergent Γ_L-invariant (Poincaré-series) laws" — **convergence true** (s_c = 2). "If so, the price is quasi-locality with power-law tails, not full non-locality" — **refuted as stated** (proved): the averaged kernel is orbit-constant, so its Euclidean tails do not decay at all.
3. "Per-realization momentum is conserved modulo the dual lattice; in-band processes conserve exact momentum" — **proved for real in-band transitions**. "The C3/RB defects can only live at Planck-scale momenta" — **not established**. Per-realization LV feeds the in-band symbol through Bragg vectors of Euclidean size ~|G²|/M, which are trans-Planckian in the particle's own rest frame (§4.3–4.4).

---

## 2. Setting and hypotheses (stated before titles)

- **(S1)** One realization: X = g(L₇ + u). Without loss of generality, X = L₇ = diag(√7,1,1,1)ℤ⁴, with x² = Q₇(n) = −7n₀² + n₁² + n₂² + n₃².
- **(S2)** Its symmetry group is the integral Poincaré group Γ_L ⋉ L₇, where Γ_L = SO⁺(Q₇, ℤ). (RECALLED, refereed in R2-2: Γ_L is a cocompact lattice in SO⁺(1,3) by Borel–Harish-Chandra and Godement, `ref_R2-2/REFEREE_VERDICT.md:9`.)
- **(S3)** A "Γ_L-covariant law" is a law for fields on the sites of X that is invariant under Γ_L ⋉ L₇. Internal indices are either:
  - scalar or unitary (the C′ setting); or
  - a finite-dimensional, possibly non-unitary Lorentz representation (spinor, vector, tensor; §3.2).
- **(S4)** Momentum space: quasi-momenta p ∈ ℝ⁴/2πL₇*. Γ_L acts on that torus by the contragredient.
- **Outside the scope** (so titles do not exceed proofs):
  - laws that are covariant only in law (ensemble), not per realization. Per-realization covariance is what makes a law a functional of the point set alone;
  - fields off the sites, i.e. continuum fields coupled to the point set (RL-type couplings). §4.4 notes what changes;
  - curved spacetime (R3-3);
  - gravity (R3-2).

---

## 3. (a) Existence, convergence and locality

### 3.1 Lemma A: structure of invariant laws (proved; inputs RECALLED)

**Statement.**
- Any on-site term (a polynomial in φ_x) is invariant.
- An off-site coupling K(x, y) = K(y − x) must satisfy K(γd) = K(d) for γ ∈ Γ_L. It is therefore a function on Γ_L-orbits in L₇∖0.
- Every such orbit is infinite.

**Proof of the last point.** Suppose Γ_L·d were finite. Then a finite-index subgroup Γ′ would fix d. Γ′ is again a lattice, hence Zariski-dense (Borel density, RECALLED). So all of SO⁺(1,3) would fix d ≠ 0, which is impossible. □

**Checked** (`r31_invariants.out:21-25`). The orbit of the dual vector (0,1,0,0) under 36 SO⁺ generators grows 25 → 423 → 6951 → 114,776 → 1,895,226 at word lengths 1–5.

**Corollary (O1's C′ for L₇, proved).** Σ_d |K(d)| = ∞ unless K vanishes off-site. Each nonzero orbit contributes |K| × ∞.

### 3.2 Lemma M: no regular invariant symbol on the momentum torus (proved; new here; elementary)

**Statement.** Let σ ∈ L²(ℝ⁴/2πL₇*) be invariant under the Γ_L action. Then σ is constant almost everywhere. Equivalently, an invariant kernel K(d) = σ̂(d) is square-summable only if it is on-site.

**Proof.** σ̂(γd) = σ̂(d), and every nonzero orbit is infinite (Lemma A). Then Σ|σ̂|² < ∞ forces σ̂(d) = 0 for d ≠ 0. □

**Comparator.** This is Halmos' criterion for ergodicity of toral automorphisms (no finite orbits of nonzero characters), applied to Γ_L.

**Consequences.**
- No per-realization Γ_L-covariant law with any hopping has an L², continuous or C^k dispersion function on the Brillouin torus.
- The symbol can exist only as a distribution, or as a boundary value from a tube (§3.4).
- This is the momentum-space form of C′, strengthened from ℓ¹ to ℓ².

**Non-unitary internal action** (spinor, vector or tensor fields; K(γd) = R(γ)K(d)R′(γ)⁻¹). *Proved modulo RECALLED sector equidistribution.*
- Take a K-invariant inner product on W = Hom(V′, V). The K×K-average of ‖k₁a_r k₂ A‖² over the "sphere" of rapidity r equals ⟨A, M_r A⟩, with M_r = ∫_K k⁻¹a_{2r}k dk.
- M_r is a scalar on each K-isotypic block. Since tr(P_U H P_U) = 0 for H ∈ 𝔭 (𝔭 ≅ the vector representation of SO(3) has no invariants), Jensen's inequality gives M_r ≥ I.
- So orbit norms never decay on average.
- With equidistribution of Γ in KAK sectors (Gorodnik–Oh, RECALLED), Σ_γ‖γA‖² = ∞. If Σ‖γA‖ were finite, then eventually ‖γA‖ ≤ 1, so Σ‖γA‖² < ∞, a contradiction.
- Therefore the Lorentz-tensor index structure does not rescue summability. (This removes the "norm-preserving" qualifier that the O1 referee added to C′, `C5_O1_referee.md:15`, for this group.)

### 3.3 Proposition P: Poincaré series, s_c = 2 (proved mod RECALLED counting; checked)

**Statement.** For d ≠ 0, F_s(Γd) := Σ_{d′∈Γd} |d′|_E^{-s} converges iff s > 2. Hence K_s(d) := F_s(Γd) is a well-defined Γ_L-invariant kernel exactly when s > 2.

**Proof.**
- N_orbit(T) := #{d′ ∈ Γd : |d′|_E ≤ T} ~ c T² for timelike orbits (on H³) and for spacelike orbits (on dS₃).
- This is lattice-point counting with critical exponent δ = 2 for a lattice in SO(1,3) (RECALLED: Lax–Phillips/Patterson for H³; Duke–Rudnick–Sarnak and Eskin–McMullen for the affine symmetric space dS₃ = SO(1,3)/SO(1,2), using that Γ_d is a lattice in SO(1,2)_d because d^⊥ is a rational anisotropic form).
- Partial summation then gives the claim. □

**Checked** (`r31_counting.out:4-…`; r₃ by FFT, verified on m < 200).
- For 8 norm shells N ∈ {−7, −6, −3, −1, 1, 2, 3, 7} (4 timelike, 4 spacelike), the log-slopes of N(T) at T = 1024 → 4096 are 1.9994, 2.0012, 2.0004, 2.0016, 1.9985, 2.0008, 1.9953, 2.0005.
  - That δ = 2 is also a numerical confirmation that Γ_L has finite covolume: an infinite-covolume subgroup has δ < 2.
- Partial sums for s = 2 grow by a constant ≈ 2c·ln 4 per factor 4 in T, i.e. logarithmic divergence. For N = −7: 7.37, 11.37, 15.26, 19.15 (`:6`).
- s = 1.5 grows ∝ T^{1/2}.
- s = 2.5, 3, 4 converge (`:7`).
- Anisotropy: r₃(7n₀²) = 0 for every n₀ ≤ 1094 (`:2`).

**The locality reading (proved).** K_s is constant on each orbit, so Σ_y|K_s(x − y)| = ∞ for every s. Within Euclidean radius T, each orbit supplies about cT² partners of identical weight.
- The decay is only across orbits: K_s(Γd) ∝ |d²|^{-s/2} for timelike orbits (partial-summation estimate; the constant includes 1/(covol·|Stab|)).
- So the averaged law is local in the invariant interval and non-local in every Euclidean sense: the causal-set (BHS-type) price, not power-law quasi-locality.
- **This refutes the price wording in supervisor item 2.**

### 3.4 Proposition R: retarded laws converge in the forward tube, and only there (proved)

**Statement.** Let K(d) = F(Γd)·1[d past-timelike], with |F| ≤ C(1 + |d²|)^k. Then K̂(p) = Σ_d K(d)e^{ip·d} converges absolutely, and is holomorphic, on the forward tube T₊ = ℝ⁴ + iV₊. It is invariant under Γ_L and under p → p + 2πL₇*.

**Proof.** For v = Im p ∈ V₊ and d past-timelike, v·d = v₀|d₀| − v⃗·d⃗ ≥ (v₀ − |v⃗|)|d₀| ≥ ((v₀ − |v⃗|)/√2)|d|_E (signature −+++). The terms are bounded by C(1 + |d|_E²)^k e^{−c|d|_E}. □

**Converse (proved).**
- Since Γ_L is cocompact (G = ΓF with F compact), every orbit is coarsely dense in its hyperboloid sheet.
- Hence:
  - a nonzero kernel with any weight on a spacelike orbit, or on both time orientations, has |e^{ip·d}| unbounded on its support for every complex p, so its symbol converges nowhere;
  - a retarded kernel converges exactly on T₊.
- An invariant **symmetric** quadratic action has no convergent symbol anywhere. Γ_L-covariant dynamics must therefore be posed as retarded equations of motion, acting on fields that decay into the past.

**Explicit interacting law (proved to be well-defined in the tube).**
- (Kφ)_x = Σ_{y ≺ x} f(n(x, y))φ_y + λφ_x³ + m₀φ_x, with n(x, y) = #(L₇ ∩ causal diamond(y, x)).
- n is Γ_L ⋉ L₇-invariant, so this is the Benincasa–Dowker / Belenchia–Benincasa–Liberati kernel transplanted from a sprinkling to LRL, with f polynomially bounded (BD: f(n) e^{−εn}·poly).
- Prior art: the event route's BD kernels (`agents/E1_report.md:19-20`). Count once.
- The on-site φ⁴ (or Yukawa) vertex is strictly local and invariant.

**The arrow (reading).** Retardation is a time orientation in the law. O1's Lemma E (`C5_O1_report.md:157-163`) turns a law-level arrow into a preferred frame only for **finite** groups. Γ_L is infinite with no invariant vector (`r31_invariants.out:13`, degree 1: 0 invariants), so retarded LRL laws keep an arrow without a preferred frame. This bears on R2-5: set B's obstruction does not transfer.

---

## 4. (b) What survives in one realization

### 4.1 Proposition B1: polynomial invariants are Lorentz-invariant (proved mod RECALLED Borel density; checked exactly)

**Statement.**
- The Zariski closure of Γ_L contains SO⁺(1,3) (Borel density; Γ_L is a lattice).
- So any Γ_L-invariant polynomial tensor is SO⁺(1,3)-invariant.
- For one momentum p, that means polynomials in p².

**Checked exactly** (`r31_invariants.out:13-20`). Modular rank over two primes was used, after a floating-point SVD gave spurious counts at degree ≥ 4.
- Invariant polynomials in p of degree 1…6 have dimensions 0, 1, 0, 1, 0, 1, the Lorentz counts.
- There are 2 invariant quadratic forms on symmetric h_μν, the Fierz–Pauli mass-form count. This is a hint for R3-2.
- Generators: 36 products of pairs of 9 integral spacelike reflections; roots of Q₇-norm 1 and 2, e.g. (1,3,0,0), giving the cosh η = 8 boost of R2-2 (`:1-11`).

**Proposition B2 (proved).** If a Γ_L-invariant function is C^k at p = 0, each Taylor coefficient up to order k is a Γ_L-invariant homogeneous polynomial, hence Lorentz-invariant.

### 4.2 The per-realization symbol has no Taylor expansion at p = 0 (proved / suggested parts as marked)

- **(proved)** Lemma M excludes a regular symbol on the torus. Prop. R gives a symbol that is holomorphic only in T₊.
- **(proved, Poisson summation in the tube)** Choose F(Γd) = f(d²) with f smooth and vanishing for x² > −½. This is allowed because |x²| ≥ 1 on L₇∖0, so the summand is smooth. Then:
  - K̂(p) = ρ Σ_{G∈2πL₇*} F_c((p − G)²), where F_c is the continuum Lorentz-invariant transform;
  - the G = 0 term is exactly Lorentz-invariant (a function of p², holomorphic in T₊);
  - the G ≠ 0 terms are the umklapp/discrepancy part.
- **(proved, kinematics)** The Bragg cones {p : (p − G)² = 0} accumulate at p = 0. For G in a spacelike orbit with |G|_E → ∞, G is nearly null, and the cone's Euclidean distance from the origin is ≲ |G²|/|G|_E → 0.
- **(suggested, recalled hyperboloid transform)** F_c(q²) ≈ C₁/q² + C₂ log q² + … near q² → 0. Here C₁ = 4π∫τ f(−τ²)dτ comes from the infinite hyperboloid volume, not from the light cone.
  - Finitely many Lorentz-invariant moment conditions can remove the leading singular terms.
  - By Müntz–Szász, no nonzero compactly supported f removes all logarithmic terms.

**Net (b) at polynomial order.**
- Whatever part of the per-realization symbol is smooth is Lorentz-invariant (proved).
- The symbol's low-momentum content is not polynomial:
  - G = 0 gives Lorentz-invariant non-analytic terms;
  - G ≠ 0 gives realization-fixed singular cones accumulating at 0.

### 4.3 Per-realization non-polynomial LV in the tube (checked; interpretation suggested)

**Observable.** S(u, κ) = Σ_{x∈shell N, x₀>0} e^{−κ(−u·x)}: the symbol of a single-shell kernel at p = iκu (inside T₊, absolutely convergent). Its exact Γ_L-invariance in u is checked to 1e-16 (`r31_lv_orbitsum.out:14-16`). If the shell's points were exactly equidistributed on H³, S would be ν·4πK₁(κτ)/(κτ), independent of u.

**Results.**
- **A direction dependence exists.** An oblique u differs from a Γ_L-image by 4.1e-3, 2.6e-3 and 1.2e-3 at κ = 0.4, 0.2, 0.1 (N = −3; `r31_lv_orbitsum.out:17-19`).
- **Scaling** (64 directions with rapidity ≤ 0.7, 13 κ values from 0.8 to 0.025; `r31_lv_scaling.out:16,33`):

| Shell | Relative LV, std_u(S)/mean | Absolute LV, std_u(S) |
|---|---|---|
| N = −3 | ∝ (κτ)^{1.30} | ∝ (κτ)^{−0.88} |
| N = −7 | ∝ (κτ)^{1.39} | ∝ (κτ)^{−0.96} |

  - κ·std_u(S) stays between 1e-3 and 2e-2 over the whole range, with oscillation.
  - So the absolute LV of a single-shell term does not shrink as κ → 0. Its prefactor is ≈ (3–6)e-3 relative to the Lorentz-invariant part at κτ ~ 1.
- **Interpretation (suggested; spectral theory RECALLED).**
  - S(u) is a point-pair Poincaré series on the compact manifold Γ_L∖H³.
  - Its expansion in Laplace eigenfunctions has a constant term: the Lorentz-invariant ν·4πK₁/(κτ) ~ 1/κ².
  - Tempered eigenvalues λ = 1 + r² contribute ~(κτ)^{-1}·(κτ)^{±ir}ψ_j(u). That is relative ∝ κτ, log-periodic in κ, with direction dependence through automorphic eigenfunctions ψ_j.
  - Exceptional eigenvalues would make the relative slope < 1. The measured slopes (≥ 1.3) show no sign of them in this range.
  - This is the deterministic analogue of the √N fluctuation of a sprinkling (E1's per-realization noise): an equidistribution discrepancy instead of noise.
- **Many shells** (`r31_multishell.out:27-29`; `r31_multishell2.out:2-5`). Mixed:
  - 24 shells, each normalised to its LI part, summed with equal weight: relative LV 1.1e-5 at κ = 0.05, against a single-shell mean of 3.9e-4. That is a ratio of 0.028, below 1/√24 = 0.20; pairwise pattern correlations are −0.01 to −0.04.
  - Raw lattice sums over all shells −48 ≤ d² ≤ −1, sharp or Gaussian in d² with proper-time width Δτ ≈ 0.8–1.2, keep relative LV of 1e-5 to 1e-3, with no clean suppression.
  - **Suggested (Poisson + Bragg gap):** in the tube along imaginary p, |(p − G)²| ≥ |G²| − κ² ≥ (2π)²/7 − κ² in every frame. So a kernel smooth on a proper-time scale ℓ_k ≫ a should suppress the tube LV like the Fourier transform of f at frequency ~2π/(√7 a), super-polynomially in ℓ_k/a. This was **not checked at ℓ_k ≫ a**: the runs reach Δτ ≈ 1.

### 4.4 Real momenta: Bragg resonances at every scale (proved kinematics; checked counts)

**No in-band partner (proved; checked).**
- |G|_E ≥ √|G²| ≥ 2π/√7 in every frame. So two in-band quasi-momenta never differ by G ≠ 0.
- Checked: min |k − G|_E ≥ 6.19 on the 2π·L₇ shell used (`r31_bragg_resonance.out:2-5`).

**Resonances (checked).** Count dual vectors G (shell G² = 4π²) with |(k − G)²| < 1, per dyadic shell of |G|_E (`r31_bragg_resonance.out:2-5`):

| Momentum k | Resonant counts per dyadic shell |
|---|---|
| **Null, ω = 0.1** | 15, 50, 84, 160, 341, 683, 1378 (doubling: ∝ T/ω) |
| **Null, ω = 0.05** | 53, 170, 319, 676, 1318, 2774 (about twice, as ∝ 1/ω predicts) |
| **Timelike, at rest, M = 0.1** | 240, all in one shell [201, 402) (kinematics: G₀ ≈ \|G²\|/(2M) = 197) |
| **Timelike, rapidity 1** | 19, 44, 75 in three shells, then none |

**Meaning.**
- For a lattice field, k and k − G are the same Bloch mode. So these are not transitions. They are singular cones of the realization's symbol (§4.2) threading the in-band region.
- For a massive momentum they sit at a compact Bragg shell of Euclidean size ~|G²|/M; for a null momentum, at all scales.
- If F_c keeps a singular term at q² → 0, the per-realization dispersion of light near those cones is not Lorentz-invariant. The strength is set by the kernel's singular moments (C₁, C₂, …), not by ℓ_k (suggested).
- For continuum fields coupled to the point set (RL-type), the same G give genuine k → k − G mixing with ω′ ~ T. This agrees with R2-2's ω′ ≥ κ²/(4ω) (`R2-2_report.md:180`) and with the R2-2 referee's caution about forward dispersion and inelastic sectors (`ref_R2-2/REFEREE_VERDICT.md:18`).
- **Not computed:** the physical size of this effect for any explicit kernel.

---

## 5. (c) Momentum, S-matrix, and the boost-wall obstructions

- **Quasi-momentum conservation mod 2πL₇* (proved):** Noether/Bloch for the exact L₇ translations of Γ_L ⋉ L₇-invariant laws. With the hard core of §4.4, every real in-band process (asymptotic quasi-momenta all in band) conserves exact 4-momentum, at every order in the on-site coupling. This confirms supervisor item 3's first half and the R2-2 referee's "ideal one-to-one Bloch silence" (`ref_R2-2/REFEREE_VERDICT.md:18`).
- **Exact Poincaré covariance of the low-energy S-matrix below the Bragg gap: not established, and leaning no.**
  - The asymptotic states are defined by the per-realization symbol, which is Γ_L- but not Lorentz-invariant (§4.3, checked in the tube; §4.4 at real momenta, suggested).
  - The exact symmetry per realization is only Γ_L ⋉ L₇. Continuous boosts are emergent at best: for a single-shell term, the LV fraction of each orbit sum vanishes as κ → 0 (relative ∝ κ^{1.3}), but its absolute size grows (∝ κ^{-0.9}).
- **C3 / RB / RFW / Theorem T.** Their hypotheses are regular local lattice laws:
  - a smooth isolated Bloch band and summable couplings with first-moment boosts (C3: `SUMMARY.md:399`; RB: `C4_B1_referee.md:21`);
  - a regular scalar shell with a nonzero finite Fourier symbol (RFW: `RFW_F1_referee.md:23`);
  - an analytic periodic finite-fibre charge (Theorem T, H5: `R2-1_report.md:45`).

  By Lemma A and Lemma M these are **necessarily violated** by every Γ_L-covariant law with hopping. The obstructions therefore **do not apply as stated**. They are neither confirmed nor refuted on LRL.
- **Note for R3-2 (proved, Parseval as in Lemma M).** A Γ_L-equivariant vector-valued L² function on the torus has τ̂(γd) = γτ̂(d), so Σ_d‖τ̂(d)‖² = ∞ unless τ̂(d) = 0 for d ≠ 0. The surviving constant must be Γ_L-invariant, hence 0 (no invariant vector).
  - So no regular equivariant translation charge exists. The only exact translations per realization are L₇.
  - Theorem T's step 5 (analytic periodic charge equal to b·k on an open set) has its analogue built in. The exact charge is the sawtooth quasi-momentum, R2-1's excluded case X2.

---

## 6. Prior art (each counted once)

**In the repository and packet.**
- O1 Lemma C/C′ (`C5_O1_report.md:120-141`; referee `C5_O1_referee.md:15`): C′ is re-derived here for L₇ and strengthened to ℓ² and to non-unitary internal actions (§3.2).
- `C4_F2_report.md:98`: Zariski density and infinite orbits of O(3,1;ℤ), "locality fails" (suggested there; proved here for L₇ in the stronger form of Lemma M).
- R2-2 LRL and its referee.
- E1/E1′ BD kernels and per-realization noise on a sprinkling (`agents/E1_report.md:7,19-20`).
- PRICE_NOTE P2 (unbounded valency, `PRICE_NOTE.md:164`).

**Outside (RECALLED, comparators).**
- Borel density; Borel–Harish-Chandra; Godement.
- Lattice-point counting in H³ (Lax–Phillips, Patterson) and on affine symmetric spaces (Duke–Rudnick–Sarnak, Eskin–McMullen); sector equidistribution (Gorodnik–Oh).
- Halmos' ergodicity criterion for toral automorphisms.
- Sorkin 2007, Benincasa–Dowker 2010, Belenchia–Benincasa–Liberati 2015 (retarded Lorentz-invariant non-local kernels, moment conditions, mesoscale ℓ_k).
- Selberg/Harish-Chandra transform on Γ∖H³.

**No repository hits** for "Poincaré series", "Halmos" in this sense (the N-Q two-projection hits are a different use), or "toral automorphism".

**New here.**
- Lemma M (momentum-torus form).
- Prop. R's exact convergence domain.
- The orbit-constancy refutation of "power-law tails".
- The checked per-realization automorphic LV and its κ-scaling.
- The resonance-count growth for null in-band momenta.

---

## 7. Scope, outside realizations, strong words

**Proved here:**
- Lemma A (with RECALLED Borel density);
- Lemma M;
- Prop. R and its converse (with RECALLED cocompactness);
- B2;
- the kinematic statements of §4.2 and §4.4.

**Proved mod RECALLED:** Prop. P (counting asymptotics); B1 (Borel density); the non-unitary part of §3.2 (sector equidistribution).

**Checked:**
- invariant counts (exact modular rank);
- counting exponent 2.000 and s_c = 2;
- exact Γ-invariance of S(u);
- the LV scaling in the tube (two shells; 24- and 48-shell aggregates);
- resonance counts.

**Suggested:**
- the spectral-theory interpretation of the LV scaling;
- the Poisson/Bragg-gap suppression for mesoscale-smooth kernels in the tube;
- the singular-moment control of the real-momentum Bragg-cone LV;
- that the 1/κ absolute growth survives the Lorentz-invariant moment conditions a light particle needs.

**Not covered:**
- continuum fields coupled to the point set;
- mesoscale kernels with ℓ_k ≫ a (numerically);
- real-momentum magnitudes for any explicit kernel;
- curved spacetime;
- gravity;
- the ensemble-only (non-per-realization) laws.

**Strong words.**
- "Exactly" is used only for the Γ-invariance check (1e-16), the exact invariant counts, and quasi-momentum conservation.
- "Impossible" is used only for Lemma A/M consequences: Euclidean-decaying invariant hopping, and a regular invariant symbol.
- The LV exponents are fitted on noisy, log-periodic data: 1.30/1.39 relative, −0.88/−0.96 absolute. Read them as "≈ linear relative, ≈ 1/κ absolute", not as precise exponents.

**Script note.** `r31_lv_scaling.py` gained an `if m < 0: continue` guard after its run. That guard matters only for shells N ≤ −8 and does not affect the N = −3 and −7 outputs.

---

## 8. Price implications (named, none adopted)

For candidate E′ (LRL), beyond R2-2's list (`R2-2_report.md:322-328`):
- **Admissibility.**
  - "Nearest-neighbor" becomes "orbit-constant couplings to the whole causal past": unbounded valency with non-decaying weights along each Γ_L orbit (Lemma A).
  - "Probability distribution determined by nearest-neighbor conditions" becomes a retarded functional of the past light cone (Prop. R). An invariant time-symmetric action has no convergent symbol.
- **Lattice.** "Proper cubic rotations" becomes Γ_L, as in R2-2. The arrow can sit in the law (retardation) without a preferred frame.
- **Open cost.** The per-realization automorphic LV (§4.3) and the Bragg-cone singular structure (§4.4) must be shown small, or the kernel tuned. The number of conditions needed (finitely many Lorentz-invariant moments plus possibly infinitely many automorphic cancellations) is unknown.

---

## 9. Needs codex referee

- Lemma M and its non-unitary extension (§3.2).
- Prop. R's convergence domain and its converse (§3.4).
- Prop. P (s_c = 2) and the refutation of the "power-law tails" price (§3.3).
- The claim that per-realization non-polynomial LV is present, with its κ-scaling (§4.3; scripts `r31_lv_orbitsum.py`, `r31_lv_scaling.py`, `r31_multishell*.py`).
- The resonance-count kinematics (§4.4).
- The overall INCONCLUSIVE reading and the "expectation not confirmed" for the umklapp suppression clause.
