# C3 lane G-A: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: FAIL, narrowly scoped to the fixed-coordinate coupling (picture I) and ensemble-RMS noise. The second-chaos bound and the Rosen causal order check out. The local BD action alone triggers FAIL, so the imported 1e-19 m bar is not needed** (C3_G-A_referee.md).

**Verdict (worker):** FAIL (bounded; needs the codex sol referee before it is recorded). A controlled lower bound (Poisson second-chaos inequality) shows that the per-realization crackle dominates the quadratic action at LIGO amplitude, at Planck density, for every registered functional. Local BD: sd >= 2.1e120 hbar against an EH kinetic-term scale of 7.5e38 hbar per wavelength cell, ratio 2.8e81. Smeared BD at l_k = 1e-19 m: ratio >= 3e2 (cell) and >= 1.3e3 (coherent detector volume). Link count: sd >= 3.1e121 links. The response is non-analytic: a step function of h (EXACT). The mean conditions (no mass term, k^2 kinetic term) are not established; they are COMPARATOR/ARGUED only, and the FAIL branch does not need them. Smeared BD with l_k above ~3e-19 m is neither excluded nor shown to pass.

**Plain summary:** We took one fixed random scatter of spacetime events and asked whether a passing gravitational wave can be described as a gentle deformation of the cause-and-effect order between them. It cannot. Even a wave as weak as those LIGO detects tilts light cones enough, over any distance longer than about 1e-24 m, to rewire nearly every long, almost light-like connection inside each wavelength-sized region, so the order changes in jumps rather than smoothly. We proved a lower bound on how much those jumps shake the standard causal-set action: about 1e81 times the wave's own action, and still about 300 times when the action is averaged over the 1e-19 m locality scale. A mere change of coordinates produces the same jumps, so the problem is in pinning a wave onto fixed events, not in the graviton itself. This is a FAIL for the test as posed, and it needs the outside referee before it is recorded.

# G-A: the order itself as the graviton (Campaign C3, lane G)

**Worker:** Claude Opus 5.5, max effort, 2026-10-10, 00:50–01:31Z.
**Pre-registration:** `PREREG.md`, stamped 01:01:52Z, before any G-A computation.
**Status of the setting:** a test setting only. The E1/E1′ axiom conflicts apply: Lattice is replaced, the causal order is supplied (records carry no time), and records-as-events conflict with "one record per site". No repository file was edited.

## Verdict against the fixed reading: FAIL (bounded; needs the codex sol referee)

- **The per-realization response is not analytic.** It is a step function of the amplitude h (EXACT). This is E1's crackle (CHECKED).
- **A controlled law shows the crackle dominating the quadratic action at physical h** for every registered functional. The law is a Poisson chaos lower bound, given in section (c).
  - **Local BD action:** sd(ΔS) ≥ 2.1e120 ħ, against an Einstein–Hilbert (EH) kinetic-term scale of 7.5e38 ħ per wavelength cell. Ratio 2.8e81.
  - **Smeared BD at ℓ_k = 1e-19 m** (the packet's locality bar): ratio ≥ 3.1e2 for a wavelength cell and ≥ 1.3e3 for a coherent detector volume.
  - **Link count:** sd ≥ 3.1e121 links. This beats the EH scale unless each link carries less than 2.4e-83 ħ.
- The FAIL branch, "a controlled law showing crackle noise dominating the quadratic action at physical h", is therefore met.
- **The mean conditions were not established here:** no mass term, pure gauge zero in the bulk, TT kinetic term ∝ k². The FAIL branch does not need them.
- **Not class-wide.** Smeared BD with ℓ_k above about 3e-19 m (4e-19 m for the detector volume) is not excluded by this bound and not shown to pass.

## What I read (in full)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all three primitives).
- `TESTS.md`: the rules and Campaign C3 (lane G readings), plus the E1, E1′ and E1′-b sections.
- `SUMMARY.md` §7–9.
- `agents/E1_report.md` and `agents/E1_referee.md`.
- `agents/E1p_report.md` and `agents/E1p_referee.md`.
- `agents/supervisor_E1p_b.md` and `agents/E1p_b_referee.md`.
- `scripts/E1/bd_core.py`, `E1_6b_strain.py` and `.out`, `scripts/E1p/e1p_core.py`.

**What is supplied rather than derived:**
- the Poisson measure;
- the causal order;
- ℓ = ℓ_P (from the scale primitive);
- the BD action and its mean tending to EH (Benincasa–Dowker 2010; COMPARATOR).

## Setting (as pre-registered)

**Sprinkling and region.**
- Density ρ = 1 (ℓ = 1), in coordinates.
- W is a causal diamond of coordinate height T.
- One sprinkling per realization, reused for every metric.

**Metrics.**
- **TT wave (+ polarization).** The exact Rosen plane wave
  - ds² = 2du dv − [exp(h cos ω(t−z) · e₊)]_ij dx^i dx^j, with u = (t−z)/√2, v = (t+z)/√2 and e₊ = diag(1,−1).
  - This equals η + h e₊ cos(k·x) + O(h²), with k null along z.
  - det g = −1 exactly, so the coordinate sprinkling is a faithful sprinkling of g. The O(h²) completion is a choice, stated as such.
- **× polarization:** the + wave rotated by 45° about z.
- **Pure gauge:** the exact volume-preserving diffeomorphism x → x + (h/ω) sin ω(t−z).
  - Its metric is η + h(∂ξ+∂ξ) + O(h²), with ∂·ξ = 0.
  - The order of P under φ*η is the flat order of φ(P).
- **Constant det-1 strain:** the E1 control.
- **Wavelengths:** ω₁ = 2π/T, ω₁/10 and 4ω₁.

**Functionals on pairs inside W.**
- The relation count R.
- The link count N₀.
- The interval counts N₁, N₂, N₃.
- The local BD sum Σ = −N + N₀ − 9N₁ + 16N₂ − 8N₃, with S_BD/ħ = −(ℓ/l_p)²(4/√6)Σ and l_p² = 8πG.
- The smeared BD action, through the exact scaling law in section (c).

## Method

**1. The exact causal order of the wave (EXACT, derived here).**
- Along any future causal curve u is nondecreasing, since g(V, ∂_v) = V^u.
- Parametrize the curve by u. Then 2dv ≥ ẋᵀgẋ du, and minimizing ∫ẋᵀgẋ du at fixed Δx gives ẋ = g⁻¹P, with a unique minimizer by strict convexity.
- So q ∈ J⁺(p) iff Δu > 0 and 2Δv ≥ ΔxᵀS⁻¹Δx, where S = ∫_{u_p}^{u_q} g⁻¹ du.
- The Lorentzian distance is τ² = Δu(2Δv − ΔxᵀS⁻¹Δx).
- S is evaluated by the Jacobi–Anger expansion with 10 Bessel terms.
- **Checks (CHECKED):**
  - the formula agrees with the first-order straight-line formula to relative O(h): 4e-4 of hR² at h = 1e-3;
  - at h = 1e-13 every flat count is reproduced exactly.
- **Shell closure (EXACT).** By the reverse triangle inequality, the shell τ² < 13.5 is closed under intervals. So the interval counts n ≤ 3 are exact, up to a truncation of order e⁻²⁴.

**2. Runs.**
- T = 10: 40 realizations, N ≈ 1300.
- T = 13: 24 realizations, N ≈ 3740.
- Both on 22 settings.
- Saturation runs: T = 10 (30 realizations) and T = 16 (8 realizations, N ≈ 8570), up to h = 1.

**3. The controlled crackle law:** section (c).

**4. The physical translation:** section (d).

## Results

### (a) The response is a step function (EXACT), E1's crackle (CHECKED)

**EXACT.** In a bounded W, every pair's relation and every interval count is a step function of h with finitely many jumps. So ΔF(h) is piecewise constant, identically zero for |h| < h*(realization) with h* > 0, and not analytic in h.

**Fraction of realizations with ΔN₀ = 0 and ΔBD = 0 (CHECKED):**

| T | h | ΔN₀ = 0 | ΔBD = 0 |
|---|---|---|---|
| 10 | ≤ 1e-6 | 1.00 | 1.00 |
| 10 | 1e-5 | 0.88 | 0.85 |
| 10 | 1e-4 | 0.25 | 0.05 |
| 13 | 1e-7 | 0.96 | 0.96 |
| 13 | 1e-6 | 0.83 | 0.75 |
| 13 | 1e-5 | 0.25 | 0.21 |

**Crackle against h at T = 13** (24 realizations):

| h | sd ΔR | sd ΔN₀ | sd ΔBD | E[# link-status changes] |
|---|---|---|---|---|
| 1e-6 | 0.50 | 0.40 | 11.7 | 0.42 |
| 1e-5 | 1.39 | 1.71 | 30.7 | 2.2 |
| 1e-4 | 3.70 | 8.81 | 97 | 27.8 |
| 1e-3 | 11.3 | 20.4 | 433 | 310 |
| 1e-2 | 37.0 | 92.9 | 1287 | 3116 |
| 0.1 | 120 | 221 | 4230 | 30045 |
| 0.3 | 454 | 304 | 5655 | 77475 |

**Before saturation.**
- The number of link-status changes is linear in h: local slopes 1.05, 1.00, 1.00 and 0.97 between h = 1e-4 and 3e-2. To first order the change probability of each pair is ∝ |δσ| ∝ h (Mecke; EXACT at leading order).
- The sd grows like h^0.4 to h^0.6. These are local slopes, not a universal exponent.
- Var ΔN₀ / E[# changes] is 1 to 3 at T = 10 and 13, and 2.4 to 6.9 at T = 16.
- At h ≥ 1e-2 a single realization's ΔBD is of typical size, with no heavy tail: the median of |ΔBD − mean| is 0.66–0.81 sd, against 0.674 for a Gaussian.

**Saturation.**
- Saturation sets in once hR² ≫ ℓ² for most pairs.
- At T = 16 and h = 1, the link-status changes already reach 0.59 × 2E[N₀]: the old and new link sets are becoming disjoint.
- **At physical parameters** hL²/ℓ² ≈ 4e60 in a wavelength cell, so the regime is deeply saturated.
- Every link longer than ℓ/√h ≈ 3e10 ℓ_P ≈ 5e-25 m is re-drawn (ARGUED from the exact flip condition). The surviving fraction of a cell's links is about 3e-61.

### (b) Pure gauge, constant strain, helicity and wavelength (CHECKED; T = 13, sd)

| setting | sd ΔN₀ at h = 1e-2 | sd ΔBD at h = 1e-2 | sd ΔN₀ at h = 0.1 | sd ΔBD at h = 0.1 |
|---|---|---|---|---|
| TT +, ω₁ | 93 | 1287 | 221 | 4230 |
| TT × | 85 | 1523 | 230 | 6076 |
| pure gauge (exact volume-preserving diffeo) | 163 | 2269 | 518 | 5562 |
| constant det-1 strain | 82 | 2022 | 306 | 4239 |
| TT, ω₁/10 | 84 | 2030 | 312 | 4352 |
| TT, 4ω₁ | 57 | 650 | 256 | 3527 |

- **The crackle is not a TT stiffness.** Pure gauge, and the constant strain that leaves the law exactly invariant, crackle as much as the TT wave. The crackle is the re-randomization of a fixed sprinkling by any change of metric, including a mere coordinate change.
- **Helicity.** + and × are equal in law (EXACT: rotation about z, and the diamond is rotation invariant). The measured differences are about 1.7σ or less.
- **k → 0.** The long-wavelength wave (ω₁/10) reproduces the constant-strain values.

### (c) The controlled crackle law (the load-bearing result)

**Inequality (EXACT).** By the Poisson chaos (Fock-space) expansion of Last–Penrose (2011), for ΔF = F_h − F₀ in L²:

  Var ΔF ≥ (ρ²/2)∫∫(E D²_{y,x}ΔF)² ≥ ρ² ∫_{x∈W}∫_{y≺₀x} (e_h − e₀)²,  with e(y,x) = E[D²_{y,x}F].

- Restricting to pairs that are timelike in flat space drops only nonnegative terms.

**The kernel (EXACT formula).** It follows from Mecke's formula and the Poisson identities E[f(N+1) − f(N)] = g′(λ) and E[Δ²f(N)] = g″(λ), where g(λ) = E f(Poisson(λ)). For F = Σ over related pairs of f(n), and an interior pair that is timelike in flat space with τ² = s:

  E(s) = g(V) + 2Φ₁(√s) + T₄(√s),  with V = πτ⁴/24,

  Φ_k(T) = (π/2)∫_T^∞ dp ∫_p^∞ dq (q−p)² g^(k)(πp²q²/24),

  T₄(τ) = (π/2)∫_0^∞ dp ∫_p^∞ dq (q−p)² Φ₂(√((τ+p)(τ+q))).

- By Lorentz invariance it depends only on s (EXACT).
- **Weights.**
  - Links: g = e^−λ.
  - Local BD: g = e^−λ(1 − 9λ + 8λ² − 4λ³/3), g′ = e^−λ(−10 + 25λ − 12λ² + 4λ³/3), g″ = e^−λ(35 − 49λ + 16λ² − 4λ³/3). These agree with direct Poisson sums to 8 digits.
- **Values of E(s):**

| s | 0.25 | 0.56 | 1.0 | 1.56 | 2.25 | 4.0 |
|---|---|---|---|---|---|---|
| links | −29.5 | −7.14 | −1.45 | 0.092 | 0.363 | 0.119 |
| local BD | 7.76 | 2.19 | −0.42 | −1.43 | −1.24 | 0.67 |

- **Checks.**
  - Φ_k and T₄ by an independent adaptive quadrature in (t, r): agree to 6 digits.
  - Direct-sprinkling Monte Carlo of D²N₀ at s = 1.5625, 1500 realizations: 0.0913 ± 0.0268 against 0.0919.
    - Every term matches within 0.3σ: direct term 0.723 ± 0.012 vs 0.727; the two one-sided terms 0.321 ± 0.020 and 0.319 ± 0.019 vs 0.321; the pair term 0.0087 ± 0.0030 vs 0.0076.
  - Direct Monte Carlo of D²Σ_BD:
    - at s = 4: 0.593 ± 0.116 against 0.668;
    - at s = 2.56: two runs of 1500 and 8000 realizations pool to −1.32 ± 0.28 against −0.867, a 1.6σ difference.
    - The per-realization sd is about 27, so the BD checks are noisy.
  - An earlier joint-uniform Monte Carlo estimate of T₄ (`mc_terms_B`) was too inefficient to be valid. Only its Φ₁ column is usable.

**Smeared BD (EXACT).** E f₄(Poisson(λ), ε) = g(ελ). So for the pair weights εf₄ (with ρ_k = ερ), E_ε(s) = ε E₁(s√ε). The bound for S_ε is then exactly ε^(5/2) times the local bound. No extrapolation in ε is involved.

**Containment (EXACT, up to e⁻²⁴ tails).** Every point a, b or z that enters E D²_{y,x}F with V < 23.9 lies in the diamond I(y − λΔ, x + λΔ), where Δ = x − y, λ = s_c/s − 1 and s_c = 13.5. So the windowed kernel equals E(s) for pairs whose extended diamond lies inside W.
- At T = 10–16 almost no long pair meets this condition.
- So the unrestricted, infinite-space estimator overestimates the link kernel there (measured Var / estimator = 0.36–0.57 at h ≤ 0.1).
- It is a valid bound only with the containment restriction.

**Saturation (controlled).** If |τ_h² − τ₀²| ≫ s_c, every interval containing both y and x has volume at least V_h(y,x), or at least πd⁴/24 at spacelike distance d. So e_h is e⁻²⁴-small wherever e₀ lives.
- At physical parameters |δσ| ~ hR² ~ 1e57 ℓ² for the contained pairs.
- The exceptions are a fraction of order s_c/(hR²) ~ 1e-57.

**Result.**

  Var ΔF ≥ ∫ ds E(s)² Γ_W(s_c/s − 1)  (Planck units),

with Γ_W = ∫_W d⁴x ∫ dΩ R_max²/4 and R_max = min(d₊/λ, d₋/(1+λ)) along each null direction. Γ_W was computed by Monte Carlo to about 0.2%.
- **Wavelength cell** (a 4-box of side L): I_link = 0.0170·L⁶ and I_BD = 0.0191·L⁶, with Var S ≥ (ℓ/l_p)⁴(16/6)·I_BD.
- **Robustness of I_BD:**
  - halving or doubling the indirect kernel terms gives 0.0158–0.0276, which changes sd by at most 20%;
  - dropping the indirect terms entirely gives 0.0133;
  - 95% of I_BD comes from s ≥ 1.
- In the saturated regime the bound does not depend on h, while the EH action scales as h².

### (d) Translation (ℓ = ℓ_P = 1.616e-35 m; h = 1e-21; λ = 1e6 m)

**The comparator for "the mean quadratic action"** (COMPARATOR: BD 2010, mean tends to EH). I use one kinetic term of the EH action, S_kin = h²ω²V/(64πG). The on-shell EH action of a null TT wave is zero, so this is the generous choice.

| region | S_kin (ħ) | links: sd ΔN₀ ≥ | local BD: sd ΔS ≥ (ħ) | ratio | smeared BD at ℓ_k = 1e-19 m: ratio | ℓ_k* where bound = S_kin |
|---|---|---|---|---|---|---|
| wavelength cell λ⁴ | 7.5e38 | 3.1e121 | 2.1e120 | 2.8e81 | 3.1e2 | 3.2e-19 m |
| (4 km)³ × c·0.1 s | 1.4e33 | 2.5e116 | 1.7e115 | 1.2e82 | 1.3e3 | 4.2e-19 m |

- **Links.** For the crackle to stay below S_kin, each link would have to carry less than 2.4e-83 ħ (wavelength cell). With the BD link coefficient, (4/√6)/(8π) ≈ 0.065 ħ per link, the crackle is 2.0e120 ħ.
- **Smeared BD at 1e-18 m.** The bound's ratio is 3e-3, so the bound alone does not decide. It is only a lower bound.
- **Planck-length convention.** Taking ℓ to be the rationalized Planck length lowers the local ratio by about 5 and raises the smeared ratio by about 600. The FAIL holds either way.
- **Other amplitudes.**
  - Local BD: the crackle exceeds S_kin(h) for every h ≤ 1 in a wavelength cell (ARGUED: the saturated bound is h-independent, and below saturation sd ∝ h^½, which exceeds h²).
  - Smeared BD at 1e-19 m: the bound falls below S_kin only for h ≳ 2e-20.

### (e) The mean response: what is and is not established

**EXACT.**
- A constant det-1 strain leaves the law invariant (E1).
- A volume-preserving pure gauge changes the law only through the region: the law on W under φ*η equals the law of the η-order on φ(W).
- + and × are equal in law.
- In the det-1 form the sprinkling is faithful, so E[F] is a diffeomorphism-invariant functional of (g, W).
- A boost along z maps the null-wave family to itself with ω → e^(±η)ω. So any bulk mean response density is independent of ω: either zero or a mass term.

**CHECKED: every mean at T ≤ 16 is boundary-dominated,** because W is fixed in coordinates.
- At T = 13 and h = 0.1, ΔR is:
  - −951 ± 139 for pure gauge;
  - −803 ± 50 for the constant strain;
  - +128 ± 24 for the TT wave at ω₁;
  - +945 ± 15 for the TT wave at 4ω₁.
- BD means at T = 16:
  - −9911 ± 2670 for the TT wave at h = 0.3;
  - −8406 ± 2419 for pure gauge at h = 0.1.
- The bulk O(h²) response is not resolved.

**NOT ESTABLISHED at finite ℓ:**
- no mean mass term;
- pure gauge zero in the bulk mean;
- a TT kinetic term ∝ k².

These rest only on the BD 2010 comparator (the EH action vanishes on-shell, and pp-waves are VSI, so every local curvature scalar vanishes; COMPARATOR) and on an argument from a diffeomorphism-invariant mean with zero BD tadpole (ARGUED). The FAIL branch does not need them.

## Verdict under the pre-registered map

- **Per functional:**
  - FAIL(links);
  - FAIL(local BD);
  - FAIL(smeared BD at ℓ_k = 1e-19 m).
- **Lane: FAIL**, since FAIL holds for every registered functional with ℓ_k ≤ 1e-19 m.
- **Scope:**
  - a classical TT wave imposed on a fixed sprinkling;
  - order-only functionals;
  - Planck density.

**Strongest correct statement.** In the records-as-events test setting, the causal order of a fixed Poisson sprinkling cannot carry a LIGO-strength gravitational wave as a smooth deformation. The wave re-draws essentially all long near-null relations in every wavelength cell. The resulting per-realization change of the Benincasa–Dowker action exceeds the wave's EH kinetic action, by the controlled second-chaos lower bound:
- by about 2.8e81 for the local action;
- by 3e2 to 1.3e3 for the action smeared at ℓ_k = 1e-19 m;
- by at least a factor 1 for any smearing scale up to ℓ_k ≈ 3e-19 m.

The same crackle appears for a pure coordinate change. The obstruction is the fixed-sprinkling construction, not a graviton mass.

**Not excluded:**
- a graviton carried by the order's own dynamics, as in a sum over orders (G-C);
- smeared BD with ℓ_k ≳ 3e-19 m (open; an upper bound is needed);
- functionals that are not order-only.

**Connection to E1′.** E1′ propagated a field on a fixed order. G-A shows that the order itself cannot be bent smoothly, realization by realization.

## What a referee should re-check

1. **The Rosen causal relation and the τ² formula:** the minimization, uniqueness, no conjugate points for |h| ≤ 1, and the shell closure via the reverse triangle inequality.
2. **The use of the chaos inequality:**
   - that ΔF is in L²;
   - that (1/2)ρ²∫∫ over ordered pairs equals ρ²∫∫ over y ≺ x;
   - that e_h is negligible on e₀'s support, including the wave's curvature inside the needle.
3. **The kernel:** the four-term decomposition of D²_{y,x}F, the measure (π/2)(q−p)² dp dq, and the reduction of T₄ to ∫Φ₂(τ(a,x)) da.
4. **The containment diamond** I(y − λΔ, x + λΔ) with λ = s_c/s − 1, and the cut s_c = 13.5 (V < 23.9) for the tails of the BD weights.
5. **The smeared-BD scaling and normalization:** E_ε(s) = εE₁(s√ε), and the prefactor (ℓ/l_p)²(4/√6)√ε.
6. **The comparator choices:**
   - using the EH kinetic-term scale as "the mean quadratic action" (the on-shell value is zero);
   - the normalization of the link count.
7. **The pre-registered lane map.** It takes ℓ_k ≤ 1e-19 m from the packet's E1 locality bar, while the G-A reading leaves the smearing scale unspecified.
8. **Typical realizations.** That a typical realization shows |ΔS| ~ sd at physical scales is ARGUED, by a central limit theorem for Poisson U-statistics (Reitzner–Schulte 2013), not proved here. At accessible sizes the median of |ΔBD − mean| is 0.66–0.81 sd.

## Files

All files are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-A/

**Pre-registration**
- `PREREG.md`

**Core code**
- `ga_core.py`
- `test_core.py`

**Crackle runs**
- Script: `run_A.py`
- Data and logs: `A_T10_s101.json`, `A_T13_s202.json`, `A_T10.log`, `A_T13.log`
- Analysis: `analyse_A.py`
- Outputs: `analyse_A_T10.out`, `analyse_A_T13.out`, `typical_A.out`

**Saturation runs**
- Script: `run_S.py`
- Data: `S_T10_s303.json`, `S_T16_s404.json`
- Analysis: `analyse_S.py`
- Outputs: `analyse_S_T10.out`, `analyse_S_T16.out`

**Kernel**
- Script and output: `kernel_B.py`, `kernel_B.out`
- Tables: `E_link.npy`, `E_bd.npy`

**Kernel checks**
- `quad_check_B.py` and `.out`
- `t4_check_B.py` and `.out`
- Direct Monte Carlo for links: `mc_direct_B.py`, `mc_direct_tau1.25.out`
- Direct Monte Carlo for BD: `mc_direct_bd_B.py`, `mc_direct_bd_tau1.6.out`, `mc_direct_bd_tau1.6_b.out`, `mc_direct_bd_tau2.0.out`
- `mc_terms_B.py` and `.out`: the Φ₁ column is valid; the T₄ column is an invalid, inefficient estimator.
- `mc_check_B.py`: killed as too slow; its output file is empty.

**Translation**
- `phys_C.py`, `phys_C.out`
- `robust_C.py`, `robust_C.out`

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** G-A: FAIL (bounded). It still needs the codex sol referee before it is recorded (TESTS.md:443).

Setting: the fixed-sprinkling records-as-events test setting. A wavelength-cell region (λ = 1e6 m, h = 1e-21) at Planck density, with the mean quadratic action taken as one EH kinetic term, S_kin = h²ω²V/(64πG) = 7.5e38 ħ. For a null wave this choice is generous, since the bulk on-shell quadratic action is zero.

A controlled law shows the crackle noise dominating that action. The law is the exact Last–Penrose second-chaos inequality, with an exact kernel, an exact containment lemma, and saturation, since |δσ| ~ hR² ≫ s_c away from a vanishing set of directions. It gives:
- **Local BD:** sd(ΔS) ≥ 2.1e120 ħ, a ratio of 2.8e81.
- **Link count:** sd ≥ 3.1e121 links. This is a FAIL for any per-link action of 2.4e-83 ħ or more; with the BD coefficient, 0.065 ħ per link, the noise is 2.0e120 ħ.
- **Smeared BD:** sd ∝ ℓ_k^-5. The ratio is 312 at ℓ_k = 1e-19 m and reaches 1 at ℓ_k ≈ 3.2e-19 m (4.2e-19 m for the detector volume).

**Scope corrections to the worker's wording:**
1. **The locality bar is imported.** The lane-level FAIL depends on ℓ_k ≤ 1e-19 m, taken from the E1 reading (TESTS.md:176). The G-A reading (TESTS.md:449-461) does not state a smearing scale. Under the G-A reading alone, the result is FAIL for links, local BD, and smeared BD with ℓ_k ≲ 3e-19 m. Smeared BD with ℓ_k > 3e-19 m is INCONCLUSIVE: the bound is only a lower bound, and no PASS conditions were established. The margin at the bar is modest: a factor 312 in action is a factor 3.2 in ℓ_k, or about 18 in h.
2. **The bound is on the spread, not on each realization.** What is controlled is the realization-to-realization sd of ΔS. That a typical single realization shows |ΔS| ~ sd is ARGUED (a Poisson U-statistic CLT, not verified). So "the per-realization change exceeds S_kin" should read "the per-realization noise (sd) exceeds S_kin".
3. **No mass-term claim either way.** "The obstruction is ... not a graviton mass" should be weakened. The obstruction found is re-randomization under any metric change, pure gauge included. The mean mass term, pure gauge zero in the bulk mean, and TT ∝ k² are not established, and the FAIL does not use them.

**Issues:** No load-bearing error was found. Every formula and number I re-derived or re-ran checks out. The issues are about scope and wording.

(1) **Lane FAIL rests on an imported bar.** The lane-level FAIL depends on the ℓ_k ≤ 1e-19 m locality bar. The worker took it from E1's reading (TESTS.md:176) and put it in PREREG.md before computing, but the fixed G-A reading never states it. Without the bar, smeared BD above about 3.2e-19 m is INCONCLUSIVE, not FAIL. The margin at the bar is thin: ratio 312, which is ℓ_k × 3.2 or h × 18. The ratio scales ∝ λ/h², so across the LIGO band the 2 kHz end is the weakest, at about 47.

(2) **"Per-realization" wording overstates the bound.** The second-chaos inequality bounds the variance only. A variance lower bound does not control a typical realization, and the CLT step is ARGUED. Accessible-size medians are 0.44–0.81 sd and excess kurtosis runs from −1 to +1. The worker labels typicality ARGUED in the re-check list, but the "Strongest correct statement" still says "per-realization change ... exceeds".

(3) **"Not a graviton mass" is unearned.** The mean mass term was not established either way.

(4) **The surviving-link fraction is too small.** "Surviving fraction about 3e-61" ignores the directions where the wave barely changes the separation. These are near the propagation axis, on the e+ nodal planes and at phase zeros, and they contribute about s_c·log(hL²)/(hL²) ~ 1e-59 to 1e-58. This has no effect on the verdict.

(5) **Minor misquotes of the worker's own data:**
- the local sd slopes for N0 run 0.23–0.71, not "0.4 to 0.6";
- Var ΔN₀ / E[changes] is 7.02 for pure gauge at h = 1, T = 10 (S run), not within "1 to 3 at T = 10".

(6) **Link-count FAIL depends on a normalization.** It needs a per-link action of at least 2.4e-83 ħ. The worker stated this; it is noted here for completeness.

(7) **The BD kernel's direct-sprinkling Monte Carlo check is weak.** At s = 2.56 it is 1.6σ off, and the worker's own mc_terms Φ₁ for BD at T = 1 is 2.3σ off quadrature. This is immaterial: my independent quadrature reproduces the kernel, the links Monte Carlo checks the same four-term structure to within 0.3σ per term, and I_BD changes by at most about 20% in sd under ×0.5 to ×2 changes of the indirect terms.

**Comparator choice is conservative.** Comparing against an EH kinetic term rather than the on-shell bulk value, which is zero for a null wave, only makes the FAIL harder to reach. Linear O(h) boundary terms of the coordinate-fixed region are not "the quadratic action" and were correctly excluded.

**Re-runs:** My check scripts and outputs are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-A/verify/. All runs used OMP_NUM_THREADS=2 and took under 10 minutes.

(a) **phys_C.py re-run:** the output is identical, line for line except the gamma lines. It gives sd local BD 2.127e120 ħ, ratio 2.83e81, smeared ratio 312 at 1e-19 m, ℓ_k* 3.15e-19 m, detector ratio 1.31e3 at 1e-19 m and ℓ_k* 4.2e-19 m. Output in phys_C_rerun.out.

(b) **kernel_indep.py:** I derived the four-term decomposition of E D²_{y,x}F myself and evaluated it with my own code.
- It works in (t, σ = t² − r²) coordinates instead of the worker's null (p, q), with g^(k) built by direct Poisson sums of Δ^k f, which reproduce the closed-form BD polynomials to 1e-15.
- E(s) at s = 0.25, 0.5625, 1, 1.5625, 2.25, 2.56 and 4 matches the worker's E_link.npy and E_bd.npy to at least 5 digits. Examples: links −29.528 / −1.4451 / 0.1187; BD 7.7565 / −0.4228 / −1.4245 / −0.8668 / 0.6679.

(c) **gamma_indep.py:**
- Γ_W/L⁶ for the unit 4-box by Sobol sampling with the exact timelike Δ, exact containment of both y − λΔ and x + λΔ, and the exact measure R²/(2√(R²+s)). It agrees with the worker's null-ray formula within 0.1–0.9% at λ = 0.5, 2, 5 and 12.5.
- Recomputed bound integrals: I_link = 0.01702 and I_BD = 0.01902, against the worker's 0.0170 and 0.0191.

(d) **rosen_check.py:**
- Brute-force maximization of proper time over 60-segment curves parametrized by u, at h = 0.3, ω = 0.9. It reproduces the code's exact Rosen τ² to about 1e-6 relative in 5 random pairs, where the flat τ² differs by up to 40%.
- The smeared-BD identity E f(Poisson(λ), ε) = g(ελ) is verified to 1e-10 at ε = 0.5, 0.1, 0.01 and λ = 0.5, 3, 20.

(e) **Analytic checks:**
- The containment lemma holds: for a ≺ y with τ²(a,x) ≤ s_c, (τ+p)(τ+q) ≤ s_c gives q ≤ s_c/τ − τ = λτ, tight for null a.
- The chaos-term factor is right: (1/2)∫∫ over all ordered pairs is at least ∫∫ over y ≺ x.
- The smeared scaling is right: E_ε(s) = εE₁(s√ε), so Var scales as ε^{5/2} and sd as ε^{5/4} = ℓ_k^-5.
- Saturation holds at physical scale for the smeared kernel too: hR²/ℓ_k² ~ 1e29 ≫ s_c.

(f) **Worker's tables:** the analyse_A and analyse_S tables agree with the JSON outputs.
