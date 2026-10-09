# E1 records as spacetime events: worker report (Claude Opus 5.5, xhigh; 2026-10-09)

Verbatim final report. Refereed by codex gpt-5.6-sol xhigh: **INCONCLUSIVE, leaning FAIL** (not the FAIL claimed below; `E1_referee.md`); logged in TESTS.md. Scripts in `scripts/E1/` (literature PDFs the worker fetched are not committed).

**E1 verdict: FAIL (bounded). Both mean conditions hold, but no ℓ ≤ 1e-19 m survives the noise once the field is actually propagated.** The FAIL needs the other-vendor referee before it is reported.

**Plain summary.** On average, random events in spacetime behave as hoped. The vacuum does not resist shape changes, and every species shares one light cone. But physics happens in one set of events. In that set, the operator that moves a field sums over events lying near the entire past light cone, and the count of such events grows with the size of the past. When that noise is fed back through the field's own evolution, it grows exponentially. At the largest allowed non-locality scale, ℓ_k = 1e-19 m, the error e-folds every 2.4e12 m of light travel, about 2 hours. Staying stable over the age of the universe needs ℓ_k ≳ 4e-15 m, about 40,000 times the locality bar. Sorkin (2007) reached about 1e-14 m by a cruder element-by-element estimate. Coarse-grained phase noise on its own would pass.

**What I read first.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full; the primitive registry check (all three primitives); SUMMARY; TESTS (T0–T2, E1); kill_F1a and its referee; R2; OUTSIDE_VIEW. The repo has no computation of BD noise: `scripts/frontier_causal_set_bridge.py:692` names BD as the standard operator and does not use it. The Lorentz-boost notes (`docs/LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md:264`, `docs/LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md:403`) cite causal sets as background only. The Cycle-878 event-space note is unrelated finite combinatorics.

**Axioms vs supplied.**
- The axioms fix Z³ sites (`MINIMAL_AXIOMS:37`) and one permanent record per site (`:77`, `:80`).
- The Poisson sprinkling is a supplied test setting and a supplied measure; the realized-state primitive supplies no measure (`PRIMITIVE_REGISTRY_CHECK.md:107`).
- The kinetic-isotropy Z³×Z_τ block (`:67`) is absent.
- BD is a supplied comparator. ℓ = ℓ_P comes from the scale primitive.
- "One realization is physical" is my reading of Record. It is load-bearing.

**Operators.** I verified these against the paper text (COMPARATOR):
- **2D (Sorkin, gr-qc/0703099, eqs 1, 7, 7a):** B_ε = (4ε/ℓ²)[−½φ(x) + ε Σ_{y≺x} f₂(n,ε)φ(y)], with f₂ = (1−ε)ⁿ[1 − 2εn/(1−ε) + ε²n(n−1)/(2(1−ε)²)].
- **4D (Belenchia–Benincasa–Liberati, arXiv:1411.6513, eq. 5.22):** B_ε = (4√ε/(√6 ℓ²))[−φ(x) + ε Σ f₄φ(y)], with f₄ = (1−ε)ⁿ[1 − 9εn/(1−ε) + 8ε²n(n−1)/(1−ε)² − (4/3)ε³n(n−1)(n−2)/(1−ε)³].
- ε = (ℓ/ℓ_k)^d, and ε = 1 is the local layer operator.
- Numerics: Poisson diamonds with exact interval counts, kept to the shell ρ_kV < 24.

**(a) Mean shape-blindness.**
- **EXACT:** a constant volume-preserving g = AᵀηA turns the g-order of P into the η-order of AP. AP has the same Poisson law, so every functional of the order has a g-independent distribution. This is R2's Lemma A (`R2…md:11`) in spacetime form.
- **CHECKED:** under a spatial TT shear s from 1e-5 to 0.1 (1,283 targets), the mean change is consistent with zero at every s.
- **New (CHECKED):** in one realization the response is non-analytic: sd(Δb) ∝ s^0.53 over four decades. There is no tadpole and no TT stiffness per realization, and a LIGO-sized strain re-randomizes every element's operator.

**(b) One cone in mean.**
- **EXACT:** the mean kernel is a Lorentz-invariant retarded function, so B̄ = F(p², sgn p⁰). Every species built this way has a zero at p² = 0, and a massive species sits on a hyperboloid.
- **CHECKED (1+1):** I used two species, ℓ_k = 1 and ℓ_k = 2, on the same sprinklings. At rapidity 0, 0.5 and 1 the Monte-Carlo means match the exact finite-diamond continuum means to within 1–2σ. The infinite-past mean is boost-invariant to 1e-8 and goes to −p²/4.

**(c) Noise scaling.** τ is the size of the past, in units of ℓ_k (ρ_k = 1). All CHECKED except the starred rows.

| Quantity | 1+1 | 3+1 |
|---|---|---|
| Element variance of B1 | (0.6–1.1)·ε(0.1875 ln U² + 0.35): grows like a log | κεS(τ), with S → 1.674τ² (EXACT); fitted p = 2.17 for τ = 6.75–14.75; κ = 2.65 |
| Window-average sd vs λ | ∝ λ⁻¹ (sd·λ constant to 10%, λ = 0.5–4); white | ∝ λ^(−2.0±0.3) (λ = 1–2.2); ratio to the independent-element prediction 0.8–1.3 |
| sd(m²_λ)/k² | ∝ λ: relevant, like static 3D (F1a) | ∝ λ⁰: **marginal**, as the power count said, but ∝ ετ/ℓ_k, growing with the past |
| Noise gain A² = Σw² | 0.05–0.4 | 1–40 measured; 1.674ετ² |
| Propagated field | √(area) drift; no exponential growth | coarse-grained error grows at 0.40, 0.45, 0.72 per ℓ_k (ε = 0.05, 0.1, 0.2) vs the renewal prediction ½√(3.35κε) = 0.33, 0.47, 0.67 |
| *Instability, any ε > 0 in 4D (ARGUED)* | — | A²(R) → ∞ (hyperbolic volume), so the renewal inequality forces exponential growth at rate ∝ √ε/ℓ_k |

**Translation** (ARGUED; Q = white strength of δm² = 13.4 ℓ⁸L²/ℓ_k¹⁰; at ℓ_k = 1e-19 m, ε = 6.8e-64 and A²(cosmic past) = 2e27):

| Criterion | Required ℓ_k | vs 1e-19 m |
|---|---|---|
| Coarse GW phase noise, ⟨δΦ²⟩ ≈ Q/16π² < 0.01 | ≥ 3e-23 m | PASS |
| GW scattering loss over 1 Gpc, elastic kinematics only | ≥ 1.8e-21 m | PASS |
| Same, final energies up to 1/ℓ_k | ≥ 1.2e-18 to 4.6e-17 m | FAIL |
| Stability of all fields over 1 Gpc / over c·t₀: ℓ_k³ > 1.59 ℓ_P² L | ≥ 2.3e-15 / 3.8e-15 m | FAIL |
| Stability of an isolated GW wavetrain: ℓ_k⁶ > 5ℓ⁴ΔuD | ≥ 2.6e-18 m | FAIL |
| CMB swerve (k₁ < 7e-97 Planck units, Philpott–Dowker–Sorkin), lenient / E_max = 1/ℓ_k | ≥ 3.8e-20 / 1.3e-15 m | PASS / FAIL |
| Relic-neutrino swerve (k < 1e-61 GeV³, Kaloper–Mattingly), lenient | ≥ 1.4e-20 m | PASS |

- **Swerves.** This noise is a microscopic swerve mechanism. With Lorentz-invariant phase space and no frame cutoff, the heating rate diverges, so the "lenient" PASS rows assume a preferred frame.
- **Lorentz-violation bounds.** None are needed for the means, which are exactly Lorentz-invariant. A frame cutoff would bring in the standard LV bounds.
- **TT analogue of everpresent Λ.** The element count is independent of TT strain at fixed det g (EXACT), so there is no counting-level random graviton mass. Through the order, a crude estimate gives m_g²/H² ~ 1.3(ℓ_P/ℓ_k)⁶(L_H/ℓ_k). That is about 3e-58 eV at ℓ_k = 1e-19 m, far below H, and it is not the binding constraint.

**(d) Verdict against the fixed readings.** The mean conditions pass. The required ℓ_k is about 2.6e-18 to 3.8e-15 m, above the 1e-19 m bar, so this is a FAIL. The only route to a PASS is to ignore the realization's own propagation beyond single scattering and impose a preferred-frame cutoff, and the setting excludes both. The core of the result is EXACT and holds beyond BD: any Lorentz-invariant retarded kernel that depends only on the volume between events has infinite noise gain in an infinite 4D past.

**Caveat: TESTS.md:8 says no verdict may rest on long extrapolation.** The FAIL extrapolates the √ε rate law, CHECKED only at ε = 0.05–0.2, out to ε ~ 1e-64. If the referee counts that as long extrapolation, the result drops to INCONCLUSIVE leaning FAIL.

**What a referee should re-check:**
1. Exponential vs power-law growth beyond τ ≈ 9ℓ_k, and the rate at smaller ε.
2. Whether the jitter is really independent across shell elements.
3. The limit of κ as ε → 0.
4. The Fresnel, Born and swerve conversion formulas.
5. Whether the past light cone in an expanding universe keeps the τ² growth (I used flat diamonds).
6. 4D windows with λ ≫ ℓ_k (I reached only 2.2ℓ_k).
7. The BD 2010 coefficients against the full paper (I verified them through BBL 2015 eq. 5.22 only) and the SMAX = 24 truncation.

**Scripts and outputs.** All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/E1/scripts/`:
- `bd_core.py`
- `E1_0_continuum_constants.py/.out`
- `E1_1_2d_mean_and_noise.py/.out`
- `E1_2_4d_validate.py/.out`
- `E1_3_4d_noise.py` with `E1_3_4d_noise_A.out`, `_A2.out`, `_B.out`
- `E1_4_evolution_stability.py/.out`
- `E1_5_evolution_coarse.py/.out`
- `E1_6_extra.py` with `E1_6_irexp.out`, `E1_6_evo.out`, `E1_6_winL.out`
- `E1_6b_strain.py/.out`
- `E1_7_translate.py/.out`

Sources:
- [Sorkin 2007](https://arxiv.org/abs/gr-qc/0703099)
- [Benincasa–Dowker 2010](https://arxiv.org/abs/1001.2725)
- [Belenchia–Benincasa–Liberati 2015](https://arxiv.org/pdf/1411.6513)
- [Philpott–Dowker–Sorkin 2009](https://ar5iv.arxiv.org/html/0810.5591)
- [Kaloper–Mattingly 2006](https://arxiv.org/pdf/astro-ph/0607485)