# C3 lane G-L: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** FAIL (worker reading; same family, unrefereed). Under the TESTS.md rule a FAIL must go to the codex sol referee before it is recorded. Basis: an exact law at leading order in l, exact at every l for plane waves, checked numerically in two independent focusing backgrounds with exact causal order. It gives a density-independent O(1) mismatch: the link mean's cone weight is nu^{-1/2}, GR's is Delta^{1/2}, and nu > 1 under focusing, so where GR magnifies, the link mean demagnifies.

**Plain summary:** Suppose a massless signal travels only by single hops along links. Behind a lens, its average strength comes out wrong, and the error does not shrink as the grain gets finer. In GR, focusing squeezes the beam and makes the image brighter. On links, focusing makes each link's empty region (the space between its two ends) bigger. A bigger empty region makes the link rarer, so the image gets dimmer. Example: a lens that doubles the amplitude in GR gives links about 0.82 of the unlensed amplitude, a factor of 2.4 off. Near a caustic GR's amplitude grows without limit while the link average goes to zero. I derived the law exactly and checked it two ways: in a plane-wave spacetime, where the causal order has a closed form, and in a conformally flat lens, where the causal order is exactly the flat one. The answer is the same at three densities. One-hop link readout therefore mis-lenses: FAIL by the fixed reading, pending the codex referee. This does not change the flat-background PASS verdicts (E1-prime, E1-prime-b, G-B).

# C3 lane G-L: link-only lensing (worker report)

**Provenance**
- Worker: Claude Opus 5.5, max effort. Same family as the exercise authors. **Unrefereed.**
- Pre-registration: `PREREG.md`, stamped Sat Oct 10 02:53:19 UTC 2026, before any computation.
- Runs: 02:55:11–02:58:54Z, OMP_NUM_THREADS=2, each under 1 min.
- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md sections E1′, E1′-b, C3 lane G and lane G-L; `agents/C3_exercise_G_graviton.md` §§2–6 (N1 and the Van Vleck by-product); `agents/supervisor_E1p_b.md`.
- Code reuse: none. I wrote a closed-form Brinkmann plane-wave order instead of reusing `e1p_core` or `ga_core.tau2`. N1 had already checked G-A's Rosen τ² by Monte Carlo against the same kind of needle-volume formula, in a vacuum wave.
- No repository files were edited.

## 1. Result

**EXACT at leading order in τ; exact for all τ in plane waves.** Take the null geodesic γ from y toward x, with affine parameter λ ∈ [0, Λ] and no conjugate points. The interval volume is

  V(y,x) = (π/24) τ⁴ ν(y,x),
  ν = Δ(y,x)^{1/2} · ⟨ [Δ(y,z_λ) Δ(z_λ,x)]^{-1/2} ⟩_w,  w(λ) = 6λ(Λ−λ)/Λ³,

where Δ is the Van Vleck determinant of each null sub-segment.

**EXACT (Mecke and the Poisson void probability).** The mean link kernel is

  E[aL] = a·exp(−ρV) → (1/2π) ν^{-1/2} δ(τ²)  as ρ → ∞,

with corrections of O(ℓ²/r²), as in flat space.

**COMPARATOR (Hadamard/DeWitt; Poisson–Pound–Vega).** GR's retarded kernel is (1/2π) Δ^{1/2} δ(τ²) plus a tail.

**Mismatch.** M = link/GR = (νΔ)^{-1/2}. It is coordinate-free (a ratio of two kernels on the same cone) and independent of ρ.

**First-order laws (EXACT algebra; CHECKED in gl_C).**
- ln Δ = Λ⁻¹ ∫ λ(Λ−λ) R_kk dλ
- ln ν = Λ⁻³ ∫ λ²(Λ−λ)² R_kk dλ
- Under null-energy focusing (R_kk ≥ 0), ν ≥ 1, so the link mean de-magnifies while GR magnifies. The two effects have opposite sign at first order.
- With Weyl shear only (vacuum), both effects are second order. Every O(1) case tested still has ν > 1.

## 2. Derivation (EXACT unless labelled)

**Setup.**
- In null Fermi coordinates (λ, w, ξ) along γ, x = γ(Λ) + δn with k·n = −1, so τ² = 2Λδ.
- The future cone of y is w ≥ ½ ξᵀP_y ξ, with P_y = J′J⁻¹. Here J is the Jacobi map from y: J(0) = 0, J′(0) = I.
- The past cone of x is w ≤ δ − ½ ξᵀP_x ξ, with P_x = −K′K⁻¹. Here K(Λ) = 0, K′(Λ) = −I.
- The volume element is 1 + O(ξ²/L_c²).

**Cross-section and volume.**
- The cross-section integral is ∫(δ − ½ ξᵀQξ)₊ d²ξ = πδ²/√det Q, with Q = P_y + P_x.
- The Wronskian KᵀJ′ − K′ᵀJ is constant, and equals K(0)ᵀ = J(Λ). Hence Q = K⁻ᵀ J(Λ) J⁻¹ and det Q = det J(Λ) / (det J · det K).
- So V = πδ² ∫₀^Λ √(det J(λ) det K(λ) / det J(Λ)) dλ. Using Δ(y,z) = λ²/det J gives the law in §1. In flat space ν = 1.

**Plane waves (Brinkmann form).** Write ds² = −2 du dv − xᵀK(u)x du² + dx².
- The exact world function is σ = −Δu Δv + (Δu/2)[x·x′], evaluated on the boundary-value solution.
- For an axis pair the two cones are exactly these quadrics, and √−g = 1. The law therefore holds for every τ, not just in the needle limit.
- By the Heisenberg isometries, ν and Δ depend only on (u_y, u_x).
- The conformally coupled scalar is Huygens on plane waves (Günther), so GR has no tail and the comparison is clean. **COMPARATOR.**

**Conformally flat g = Ω²η.** The causal order is exactly the flat order. Write ⟨·⟩ for the uniform average in flat affine parameter.
- ν = ⟨Ω⁴⟩_w / ⟨Ω²⟩².
- Δ = ⟨Ω²⟩² / (Ω_x² Ω_y²).
- GR's kernel is exact by conformal invariance: Ω_x⁻¹ Ω_y⁻¹ G_flat = (1/2π) Δ^{1/2} δ(τ_g²).
- Link/GR = Ω_x Ω_y / ⟨Ω⁴⟩_w^{1/2}.
- This is an independent derivation. It agrees with the general first-order law (integrate by parts twice).

**Thin lens (convergence κ, shear γ, at fraction a of the baseline).**
- GR: μ = Δ = 1/det(I − S), with S = diag(κ+γ, κ−γ).
- Link: ν = √μ · I, where I = ∫ 6t(1−t) √D(s(t)) dt, D(s) = (1 − sκ)² − s²γ², and s(t) is the sub-segment lens weight.
- Example: a = ½, κ = ½ gives I = 3/4 and ν = 3/2 exactly. GR amplitude ×2; link amplitude ×0.816; M = 0.408.
- At a caustic (μ → ∞), the link amplitude goes as μ^{-1/4} → 0.

**Cannot be absorbed (ARGUED, using standard Hadamard transport).**
- Any local operator g^{ab}∇_a∇_b + A^a∇_a + B has a δ-coefficient Δ^{1/2}·exp(−½∫_γ A). For a thin lens with both endpoints in flat regions, that factor is a fixed constant across the lens.
- M is not: it depends on where the lens sits along the ray. At the same μ = 4, M = 0.408 at a = ½ and 0.426 at a = ¼.
- So the link mean is not the leading part of the retarded Green function of any local wave operator. No endpoint rescaling a → a·f(x)f(y) repairs it.
- Flux through a lensed beam is not conserved, because Δ^{1/2} is the flux-conserving transport weight.

## 3. Numerics (CHECKED)

**(A) `gl_A_planewave`: sandwich plane wave, exact σ, Monte Carlo interval volume.**
- 24 settings: 8 backgrounds × {axis pair, off-axis x, larger Δv = 2e-2}, 2e6 samples each.
- V_MC/V_formula agrees within 3σ in every setting. The largest deviation is |z| = 2.52; all others have |z| ≤ 1.80. Zero samples landed at the box edge.
- Results:

| case | Δ | GR √Δ | link ν^-½ | M | νΔ |
|---|---|---|---|---|---|
| Ricci f=1 | 1.671 | 1.293 | 0.938 | 0.726 | 1.90 |
| Ricci f=2 | 3.106 | 1.762 | 0.860 | 0.488 | 4.20 |
| Ricci f=3 | 6.921 | 2.631 | 0.758 | 0.288 | 12.06 |
| Weyl f=2 | 1.162 | 1.078 | 0.973 | 0.902 | 1.23 |
| Weyl f=3 | 1.454 | 1.206 | 0.931 | 0.772 | 1.68 |
| Weyl f=3.6 | 1.811 | 1.346 | 0.891 | 0.662 | 2.28 |
| mixed | 3.802 | 1.950 | 0.807 | 0.414 | 5.84 |

**(D) `gl_D_vanvleck_fd`: an independent check of the Van Vleck value.** Δ = |det ∂_y∂_x σ| from finite differences of the exact σ equals the Jacobi formula to 6 digits, for 4 backgrounds, for both axis and off-axis timelike pairs.

**(B) `gl_B_conformal`: static conformal lens, Ω² = 1 + A·exp(−|x−c|²/w²), R = 100, w = 10.**
- Method: the actual source integral φ_link = q·a·∫dt exp(−ρV_g(t)). V_g comes from a Monte Carlo over the flat diamond, with no needle approximation. The comparison is with the exact GR field.
- The ratio is independent of density, at ℓ = 1, 0.5 and 0.25:

| case | GR √Δ | predicted link/GR | measured link/GR (ℓ = 1 / 0.5 / 0.25) |
|---|---|---|---|
| A = 1 | 1.177 | 0.7653 | 0.7654 / 0.7652 / 0.7651 |
| A = 3 | 1.532 | 0.4857 | 0.4857 / 0.4855 / 0.4854 |
| A = 3, lens at quarter | 1.527 | 0.5426 | 0.5431 / 0.5429 / 0.5429 |
| A = 3, impact parameter 6 | 1.371 | 0.5866 | 0.5865 / 0.5863 / 0.5863 |

- The flat control gives 1.0000. The worst agreement with the needle prediction is 0.1%.

**(C) `gl_C_thinlens`: thin-lens table.**
- At a = ½:
  - κ = 0.3: μ = 2.04, GR amplitude 1.43, link amplitude 0.91, M = 0.64.
  - κ = 0.9: μ = 100, GR 10, link 0.43, M = 0.043.
  - γ = 0.99 (pure shear): μ = 50, GR 7.09, link 0.42, M = 0.059.
- First-order laws against the exact sandwich: ln ν agrees to 0.05% at k = 0.01 and to 1% at k = 0.2. ln Δ agrees likewise.

## 4. Reading (fixed in TESTS.md)

**FAIL clause:** "a controlled law shows a density-independent O(1) mismatch."
- **The law:** exact at leading order in ℓ, and exact at every ℓ for plane waves.
- **The checks:** two independent focusing backgrounds with exact causal order, plus a finite-difference check of Δ.
- **Density independence:** checked directly in (B).
- **Size:** M = 0.29–0.90 for μ = 1.2–7, and M → 0 at caustics.

**Worker verdict: FAIL.** It needs the codex sol referee.

The exercise guessed the scaling as "ν^{-1/2}Δ⁻¹". The rescue it left open, V ≈ (π/24)τ⁴Δ⁻¹, is excluded: under focusing ν ≥ 1 (νΔ = 1.2–12 in A), not Δ⁻¹.

## 5. Scope and hypotheses
- **What was tested:**
  - The **mean** only, of the massless one-hop G₀ = aL with the flat normalisation a.
  - A Poisson sprinkling of a fixed curved metric, using that metric's true causal order. The E1′ axiom conflicts apply: Lattice replaced, causal order supplied, records treated as events.
- **Geometric conditions:** no conjugate points between source and observer (images outside caustics), and curvature scale much larger than the needle width. Corrections are O(width²/L_c²); there are none for plane waves.
- **Tensor bridge:** not derived. In GR geometric optics each polarisation amplitude carries the same Δ^{1/2}, so the mismatch should transfer (ARGUED).
- **Not covered:**
  - other link-only readouts: environment-weighted links, density-normalised counts, BD-operator inversion, multi-hop relays;
  - a non-uniform event density that tracks focusing (that would be a supplied, metric-aware density);
  - GR's tail term in generic spacetimes such as Schwarzschild. The link mean has no tail, which is a further but subleading mismatch.
- **Unchanged:** the flat-background verdicts E1′/E1′-b (PASS for the scalar proxy) and G-B (INCONCLUSIVE).

## 6. Translation and price (ARGUED; suggested)
- **Observable consequence.** Any massless field carried by one-hop links (the graviton proxy, or light if light rode links) would make strongly lensed images dimmer than unlensed ones instead of brighter. The error is O(1) and independent of distance and ℓ.
- **Updated graviton price.** The third item on the graviton exercise's price list was "link-only readouts that reproduce Van Vleck focusing". It now reads: one-hop link-only readout fails it (worker, unrefereed). A surviving substrate needs either:
  - a readout whose mean weights the cone by Δ^{1/2}, i.e. a transport law for the null expansion along chains (supplied derivative structure); or
  - an event density or law that knows the focusing.

  Both are additions to the setting.

## Files (scratch: /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-L/)
- PREREG.md
- gl_A_planewave.py / .out
- gl_B_conformal.py / .out
- gl_C_thinlens.py / .out
- gl_D_vanvleck_fd.py / .out

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** FAIL, supported with corrections. This is a bounded FAIL for the pre-registered setting: the mean of the massless one-hop link kernel G0 = aL (flat a) on a Poisson sprinkling with the true causal order of the metric. Exact law: link/GR = M = (nu*Delta)^(-1/2), independent of density. For O(1) focusing M is O(1) away from 1: 0.29 to 0.90 in the worker's plane waves, 0.49 to 0.77 in direct field ratios for conformal lenses, and tending to 0 at caustics. This is the TESTS.md FAIL clause ("a controlled law shows a density-independent O(1) mismatch"). PASS is excluded: no NEC background with nonzero focusing along the ray gives M = 1. The result is still same-family and unrefereed. A FAIL needs the codex sol referee before it enters the price list.

**Issues:** I found no defect that touches the verdict. The derivation steps I re-did by hand all hold: the Wronskian identity det Q = det J(L)/(det J det K); the cross-section integral pi*delta^2/sqrt(det Q); the cone weight int a*exp(-rho*nu*pi*s^2/24) ds = nu^(-1/2)/(2 pi); the first-order laws (constant R_kk gives ln Delta = r L^2/6 and ln nu = r L^2/30, both consistent); and the thin-lens closed forms (<s> = (1-a)^2 + a^2, so M = 0.408 at a = 1/2 and 0.426 at a = 1/4). The plane-wave world function sigma = -du dv + (du/2)[x.x'] also re-derives. Corrections:

(1) The claim "Under NEC, nu >= 1" is established only at first order for general backgrounds, so the §1 bullet must not read as exact. It is exact in three narrower places. (a) Thin lenses with kappa < 1: D(s) >= D(1) for s in [0,1]. (b) All conformally flat backgrounds (new checker lemma): R_kk = 2 f''/f with f = 1/Omega, so NEC means f is convex; then f <= its linear interpolant, and the Feynman-parameter identity gives link/GR <= 1. (c) Numerically: 564 random admissible NEC piecewise plane-wave profiles give min nu = 1.0003 and max M = 0.9992. The §6 statement "lensed images dimmer instead of brighter" is ARGUED, not proved. It is also relative to flat at equal affine distance, a convention: in the conformal lens, GR's field equals the coordinate-flat value.

(2) Lane (B) is a net-focusing background but violates NEC in the Gaussian wings, where f = Omega^-1 is concave and R_kk < 0. The report should say "net focusing (Delta > 1)", not "focusing backgrounds" in the NEC sense. This does not affect FAIL.

(3) Scope: the mismatch is tied to null focusing along the ray, not to curvature as such. In de Sitter, f is linear along null rays, so link/GR = 1 exactly; checked to 1e-9. The worker's law predicts this, which is a consistency check. Under NEC violation the sign reverses: a conformal bump with A = -0.5 gives link/GR = 1.128. Add this to §5.

(4) Lane (D) imports sigma from gl_A, so it is not independent of the sigma implementation. The checker's own derivation (v1) covers this.

(5) Lane (B) reuses the same 4 MC diamond sets at every density, so its "density independence" comes from correlated samples. The checker's deterministic quadrature (v2) closes this gap.

(6) §6 says the mismatch is "independent of distance"; that is imprecise. M depends on the lens strength and on where the lens sits along the ray. What is true is that M is not suppressed by distance or by l.

(7) "Cannot be absorbed" is correctly labelled ARGUED. It covers only second-order local operators, and it uses collinear configurations in which the ray crosses the lens identically while the lens position a changes.

(8) Weak-field Schwarzschild, tails, and the tensor bridge were not done, as the report says. The setting's "or" makes this acceptable.

**Re-runs:** All runs used OMP_NUM_THREADS=2, in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-L/verify/ (no repo edits). Each was under 1 minute.

(a) Worker scripts gl_A (20 s), gl_C and gl_D re-run. gl_A's output is byte-identical to the reported .out. gl_C and gl_D reproduce the reported numbers (I = 3/4, nu = 3/2; Delta from finite differences equals Jacobi to 6 digits; first-order ln nu matches to 0.05% at k = 0.01 and 1% at k = 0.2).

(b) v1_planewave_quad.py (independent): a smooth sin^2 sandwich wave, transverse Jacobi maps by my own RK4, and the exact interval volume by deterministic 2D grid plus Gauss quadrature of (gap)_+. The gap comes from the exact sigma; no quadric assumption is used. Cases: flat, Ricci 3/6/12, Weyl 6/9, mixed (8,-2); axis and off-axis pairs; dv = 1e-3, 0.3 and 2 (tau^2 up to 4). V/((pi/24)tau^4) equals nu(law) to 1.0e-6 in every case, with no box clipping. The plane-wave law is therefore CONFIRMED exact for all tau. Values of M: 0.64 (Ricci 3), 0.36 (Ricci 6), 0.018 (Ricci 12, near caustic), 0.84 / 0.63 (Weyl), 0.52 (mixed).

(c) v2_conformal_quad.py (independent): deterministic quadrature over the boosted flat diamond, then the source-worldline integral at l = 1, 0.5, 0.25, 0.125. Results:
- flat: 1.0000
- A=1: 0.7657 -> 0.7653 (predicted 0.7653)
- A=3: 0.4861 -> 0.4857 (predicted 0.4857)
- A=3 at quarter: 0.5429 -> 0.5426
- A=3 with b=6: 0.5868 -> 0.5866
- A=-0.5: 1.1275 -> 1.1280

All converge to the needle prediction with O(l^2) corrections and are density-independent. This confirms the worker's (B) table.

(d) v3_nec_search.py: 900 random piecewise NEC plane-wave profiles, 564 of them free of conjugate points. Min nu = 1.0003, max M = 0.9992 (both from weak pure-Weyl profiles).

(e) v4_conformal_sign.py: de Sitter link/GR = 1 (to 1e-9). Convex (NEC) f gives 0.22; concave f gives 2.09. The Gaussian lenses of (B) have R_kk < 0 over their wings.
