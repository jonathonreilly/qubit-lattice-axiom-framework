# C5 R16-1 report: is the electron–photon split a theorem on Wilson edges (including the subluminal D1(r))?

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 22:18Z to about 22:55Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R16-1/`. Scripts and outputs are in `S/scripts/`. `OMP_NUM_THREADS=2`; every run took under 6 min.
- `r161_laws.py`: D1(r) (R14-1's construction, W tabulated by a C² cubic spline instead of R14-1's linear interpolation) and R8-5's BQ law with a free photon choice, both with periodic wrapping.
- `r161_heavy.py`: the closed form of the linear coefficient L (Theorem W), in two independent quadratures.
- `r161_validate_L.{py,out}`, `r161_validate_D1.{py,out}`, `r161_onshell_aniso.py`: L against R13-7's on-shell runner at large m.
- `r161_signW.{py,out}`: Lemma K sampling; L over D1(b, r), photons and λ; BQ r-family; laws outside (H2′).
- `r161_firstorder.{py,out}`: L against the first-order W″-moment; the tadpole piece; whole-zone v_max.
- `r161_tuneL.{py,out}`: a law outside (H2′) tuned to L = 0, and its next coefficient.
- `r161_lemmaK2.{py,out}`: Lemma K′'s b₀, and sampling without a size bound.
- `r161_vmax_BQ.{py,out}`: whole-zone v_max of every BQ law used.
- `r161_validate_more.{py,out}`, `r161_twoforms.out`, `r161_vmax_D1.{py,out}`: more closed-form checks; the two quadratures to 7 digits; D1's v_max with analytic derivatives.
- `r161_mscan.{py,out}`: probe (c), Δ_λ(m) on D1(1.4, 1/√3) at three resolutions.
- `r161_partner_gl.py`, `r161_partner_check.out`, `r161_partners.{py,out}`, `r161_partner_mscan.{py,out}`, `r161_partner_hires.{py,out}`, `r161_selectron_smallm.{py,out}`, `r161_combine.{py,out}`: probe (d), 𝒬_W^P.
- After a periodic-wrap fix to `BQLaw` (R8-5's `Law` is valid only on [−π, π], which matters for R13-1's finite-q shifts), I reran `r161_validate_L`, `r161_signW`, `r161_firstorder` and `r161_partners`. Their outputs are unchanged.
- Unmodified copies: `r137_onshell.py`, `r85_box_qed_copy.py`, `r101_dirac_moment_copy.py` (R13-7 archive), `sublum.py` (R14-1), `r131_photon_sqed.py`, `r131_electron_sqed.py` (R13-1).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method (`:2302-2320`); R9-1 verdict (`:3838-3848`); R13-1 item and result (`:4578-4596`, `:4715-4722`); R13-7 result (`:4844-4858`); Round 16 (`:5037-5061`), with the new rules at `:5039`.
- Agents: `C5_R13-7_report.md` and verdict; `C5_R8-5_report.md` and verdict; `C5_R14-1_report.md` (§§0, 1, 6, 7) and verdict; `C5_R13-1_report.md` (§§0, 3.3) and verdict; `C5_R10-1_referee_verdict.md`; `C5_S17_synthesis.md` (§1.1, the wall map, P61, P73, §5 R16-1).
- `SUMMARY.md` §§21–25 (grep for the split).
- Scripts: `scripts/C5/R13-7/*`, `scripts/C5/R14-1/{sublum,r141_wilson}.py`, `scripts/C5/R13-1/r131_*.py`.

**Labels.** proved (complete under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `vR13-7` = `P/agents/C5_R13-7_referee_verdict.md`, and likewise.

---

## 0. In plain words

1. **Yes, the no-go holds on the Wilson edges physics would use, including D1(r).** On a Wilson edge, the heavy electron's speed shift grows linearly in its mass, δc_e = L·m + O(1). I found the exact coefficient L and proved that it is **strictly positive** on a class that contains D1(r ≤ 1/√3) at b = 1.4, 1.2, 1.0 with every registered (H2′) photon, and also R8-5's r ≤ 1 Wilson boxes with such photons. The photon's coefficient dies away (O(m⁻²)). So Δ_λ(m) → +∞, Δ_λ is not identically zero, and since Δ_λ is real-analytic in m (Lemma A, extended), it **cannot vanish on any open mass interval**. Worker reading: **DERIVED**, pending the referee.
2. **What L is (proved; checked to ≤ 1e-4 relative on four laws).** In the heavy limit, the electron's upper components are a lattice particle whose energy is m + Σ_j W(k_j): the Wilson term is a momentum-dependent rest energy, O(1) and independent of m. Its photon cloud gives the energy an O(1) dependence on momentum, which is an O(m) speed shift. The coefficient is
   L = ½⟨∂²_{q_x} Ω(q; u)|_{u=W(q_x)}⟩, with Ω(q; u) = u[D² − d_x²(1 − A′)] / (2 d_x² W_γ D (D + u)),
   where W_γ = √(Σd_j² + λ²), D = W_γ + W(q_y) + W(q_z), A′ = W(q_y)²/d_y² + W(q_z)²/d_z², and the derivative acts on the photon side only. To first order in W it is exactly the "zero-mean W″-moment" the R13-7 worker suggested, with R13-7's heavy weight w: L ≈ ¼⟨W″(q_x) w(q)⟩ = ¼⟨W(q_x) w″(q)⟩ (checked to within 3–6% on D1).
3. **Why its sign is fixed (Lemma K, proved).** For fixed u > 0, Ω is convex in the photon momentum q_x wherever the photon symbol is 2 sin(q/2) or q, provided either W ≤ |d| and λ ≤ d(b) (Lemma K), or the photon is 2 sin(q/2) on the Wilson edge and the box half-width is b ≥ 0.51, with no bound on the size of W (Lemma K′). Since Ω(q; 0) = 0, the integrand is zero where W = 0 and positive where W > 0. On D1, max W/|d| = 0.06 (b = 1.4) to 0.19 (b = 1.0) and b ≥ 1.0, so both conditions hold with a wide margin.
4. **The size on D1(1.4, 1/√3), naive photon, λ = 0.05** (checked; three resolutions agree to ≤ 2e-4 for m ≤ 3):
   - L·16π² = +0.2266 (and +0.502 at b = 1.2, +0.820 at b = 1.0);
   - Δ_λ(0⁺) = −10.877 e²/16π², that is c_e − c_γ ≈ −6.3e-3;
   - Δ_λ rises smoothly to −6.65 at m = 3, crosses zero once near m ≈ 24 (an isolated zero, as Lemma A allows), and then grows linearly.
5. **Outside the class the sign is not fixed** (checked). If the photon's plateau transition sits on the Wilson edge (outside H2′), L changes sign across R8-5's own shapes (S3 −0.287, S8 −0.983, S1 +2.505). A law tuned to L = 0 still has a nonzero next coefficient, c₀ ≈ −2.15. The size condition W ≤ |d| is not needed when b ≥ 0.51 and the photon is naive on the edge (Lemma K′, proved). This covers R8-5's heavy-edge series (r up to 32), where L > 0 checked. Below b = 0.51 without the size condition, I have only samples (W/d up to 1e3, all positive; suggested).
6. **Partners (𝒬_W^P).**
   - Two matched selectrons with R13-1's gauging only add to the photon side. That contribution is O(m⁻²), so the theorem carries over unchanged (proved).
   - R13-1's full minimal SQED also has a selectron–photino loop on the electron. It is suppressed by the heavy selectron's 1/(2ε) normalization, so it changes δc_e by O(1) and leaves L unchanged (suggested by power counting; checked bounded to m = 102.4).
   - On D1 with partners, Δ(0⁺) ≈ −10.05 (selectrons only) or −18.81 (with the Yukawa loop).
7. **Physical meaning (reading).** This is a no-go for a *structural* zero, as in R13-7. It does not say the split needs one tuning per mass. At physical masses (m a ≲ 1e-17) the linear term is negligible, and one tuning of Δ(0⁺) is still the cheapest named price (P73). The theorem closes the gap S17 named: the DERIVED subclass is no longer only the R9-1-excluded literal edge.

---

## 1. Hypotheses and classes (stated before any title)

- **Common setting (registered, `TESTS:5044-5049`).** Z³ × ℝ, continuous time; one loop; Feynman gauge; non-compact photon with mass λ > 0; Peierls coupling, so the lattice Ward–Takahashi identity is the **standard** exact one (R8-5, `C5_R8-5_report.md:140`). On-shell c_e as in R13-7: E(p)² = m_phys² + c_e²p² + O(p⁴) along an axis, δc_e := (c_e² − 1)/2. The photon coefficient is R10-1's refereed Theorem-D moment (`vR10-1:5`). Units: per e², printed ×16π².
- **Class 𝒬_W (registered).** Electron h(k) = Σ_j s(k_j)α_j + (m + Σ_j W(k_j))β, as in R8-5's BQ law (`C5_R8-5_report.md:118`). s is odd, 2π-periodic, C², with s = k on [−b, b], b > 0. W is even, 2π-periodic, C², with W = 0 on [−b, b] (box exactness). The photon has t = d² even, periodic and C², t > 0 off 0, t = q² + O(q⁴), and (H2′) on the electron edge: d(q) ∈ {2 sin(q/2), q} wherever W(q) > 0 (R13-7's photon class, `vR13-7:17-22`).
- **Subclass 𝒬_W⁺ (where Theorem W is proved).** 𝒬_W plus:
  - (H0) W ≥ 0 and W ≢ 0. This says p = 0 is the bottom of the heavy band; with W < 0 somewhere, the heavy electron at rest could decay.
  - (H3) ρ(q) := W(q)/|d(q)| ≤ 1 for all q, and λ ≤ d(b) := |d(b)|. If ρ ≤ 1/√2 everywhere, then A′ ≤ 1 and the λ clause can be dropped. D1 has ρ ≤ 0.19.
    **or (H3′)** d(q) = 2 sin(q/2) on supp W, and b ≥ b₀ = 0.505. Here b₀ is the smallest b for which (C_b) holds: 2(6 − t)τ(t + τ) ≥ 3(2 − t)t² on [τ, 2], τ = 2 − 2cos b. (H3′) puts no bound on the size of W and none on λ.
  - Extra charged species (optional): any finite set that couples to the electron only through the photon, with one-loop photon coefficients real-analytic in m and bounded as m → ∞. Examples: species of fixed mass, or the matched selectrons of 𝒬_W^P.
- **Members, with whole-zone v_max (S17 rule, `TESTS:5039`).**

| law | max W/|d| | v_max (m = 0.1, 0.3, 1) | in 𝒬_W⁺? |
|---|---|---|---|
| D1(r = 1/√3), b = 1.4 / 1.2 / 1.0, naive photon or photon box (b/2, b) | 0.063 / 0.129 / 0.190 | ≤ 1 (proved for r ≤ 1/√d, `vR14-1:13`). The sup is 1.000000, attained on the body diagonal inside the slab (analytic derivatives, `r161_vmax_D1.out:1-3`); so r = 1/√3 is luminal at isolated points, and r < 1/√3 gives v_max < 1. Theorem W covers every r > 0 | yes |
| R8-5 BQ boxes, r ≤ 1, H2′ photon (e.g. naive) | 1.000 (at q = π) | S1: 3.21, 3.31, 3.59; S3: 4.58, 4.65, 4.88 (checked, `r161_firstorder.out:11-12`) | yes (needs λ ≤ d(b₁)) |
| R8-5 BQ boxes with R8-5's own photons (S1–S8) | — | 2.31–8.02 over S1, S2, S3, S5, S7, S8 (`r161_vmax_BQ.out:1-6`) | no: violates (H2′) |
| BQ r > 1 (R8-5's heavy-edge series), naive photon | r | 219 at r = 32 (`r161_vmax_BQ.out:8`) | yes via (H3′) when b₁ ≥ 0.505 (S3: b₁ = 2); S5-type b₁ = 0.5 only sampled |

  Every R8-5 Wilson box I checked is strongly superluminal over the whole zone, by factors of 2.3 to 8 at r = 1 (checked). This is consistent with R13-4's Lemma V for odd-symbol laws. This is why the S17 rule matters here: of the members listed, only D1 is subluminal.
- **𝒬_W^P (registered variant).** 𝒬_W plus two complex selectrons with R13-1's gauging: ε(k)² = E(k)², vertex Γ = 2S(k_y)S′(k_y) + W′(k_y)[M(k) + M(k+q)] (`C5_R13-1_report.md:196`). (P-a) is selectrons only. (P-b) additionally has R13-1's photino and Yukawa (y² = 2e²) loop on the electron (`C5_R13-1_report.md:51`).
- **Excluded (registered).** λ = 0; non-Peierls vertices; two loops; N=4 content. **Also excluded here:** b = 0 (plain Wilson, W″(0) ≠ 0, where the tadpole term changes form); Clifford-flat 8-component electrons; general ℓ¹ gauge generators.
- **Subtractions, named before the runs.**
  - "δc_e − Lm = O(1)": the subtraction is Lm, with L from the closed form.
  - "δc_γ = O(m⁻²)" and "partner loop bounded": absolute, no subtraction.
  - Selectron P_M: R13-1's Ward/f-sum subtraction χ(0) on the same nodes (`C5_R13-1_report.md:195`).
  - Fits δc_e = Lm + c₀ + c₁/m: an extrapolation, stated as such.

## 2. Prior art (each counted once)

- **R13-7 and verdict.**
  - Lemma A, Theorem H and Theorem Sgn are confirmed for the literal edge (`vR13-7:5-24`). The subclass is DERIVED; Wilson edges are not covered (`vR13-7:30`).
  - The Wilson control saw linear growth with a shape-dependent sign, and the worker suggested a zero-mean W″-moment (`C5_R13-7_report.md:144-148,202`).
  - Here: the exact coefficient, and its sign on 𝒬_W⁺.
- **R8-5** (`vR8-5:7`). Non-decoupling along the r-deformation. That is a different deformation from the electron mass used here, as R13-7 also noted (`C5_R13-7_report.md:86`).
- **R14-1** (`C5_R14-1_report.md:184-211`; `vR14-1:13`). D1(r), its proved subluminality for r ≤ 1/√d, and the corner masses m + nW_π.
- **R9-1** (`TESTS:3838-3840`). The literal edge is EXCLUDED under G-out. D1's corners have mass m + 0.095n/a, Planckian at a = ℓ_P, so they are not same-mass copies (reading).
- **R10-1** Theorem D (`vR10-1:5`), used for c_γ.
- **R13-1** (`vR13-1:30-31`). Partner gauging and Lemma LIT. The 24-law negative-Δ numbers are model results (`vR13-1:27`).
- **S17** (`C5_S17_synthesis.md:63,177`). The gap R16-1 targets.

## 3. Results

### 3.1 Lemma A_W (analytic rigidity on Wilson edges). Proved

- **Claim.** In 𝒬_W with (H0) and λ > 0, m ↦ Δ_λ(m) is real-analytic on (0, ∞). The same holds with extra species as in 𝒬_W⁺, and in (P-a). So Δ_λ vanishes on an open interval only if Δ_λ ≡ 0 on (0, ∞).
- **Proof.**
  1. E_k(m)² = (m + w(k))² + |s(k)|² with w = ΣW ≥ 0, so E_k ≥ m = E₀.
  2. For |m − m₀| < m₀/4, |E_k(m)² − E_k(m₀)²| ≤ ¾E_k(m₀)². So E_k(m) is analytic, uniformly in k.
  3. At p = 0 the normal on-shell denominators are W_γ + E_k − E₀ ≥ λ − O(|m − m₀|), and the Z-graph denominators are ≥ 2m₀ − O(|m − m₀|).
  4. The vertex factors |δ_j|²/d_j² are bounded and m-independent, and n_k = h_k/E_k is analytic.
  5. So the on-shell integrand and its p-derivatives at p = 0 are analytic in m and uniformly bounded on the compact zone. The q-integral is analytic by dominated convergence.
  6. The Theorem-D moment has E ≥ m₀ − O(δ), so it is analytic too. The selectron moments in (P-a) have ε = E ≥ m₀.
  7. Apply the identity theorem on the connected (0, ∞). ∎
- **What is new.** Only the explicit (H0): R13-7's "the same holds for BQ Wilson electrons, since E > 0" (`C5_R13-7_report.md:96`) needs E_k ≥ E₀, not just E > 0.
- **Not claimed.** The converse "all asymptotic coefficients vanish ⇒ Δ ≡ 0" (`vR13-7:24`) is not needed here: L ≠ 0 suffices.

### 3.2 Theorem W (the linear coefficient). Proved; checked

**Claim.** In 𝒬_W with (H0), as m → ∞, δc_e(m) = L·m + O(1). Here

L = ½ ∂²_p ⟨Ω(q; W(p − q_x))⟩|_{p=0} = ½ ⟨[∂²_{q_x} Ω(q; u)]_{u = W(q_x)}⟩, and δc_γ(m) = O(m⁻²).

**Proof.**
1. **Heavy expansion.** Take p on the x-axis in the box, M_k = m + w(k), and a = n_p, b = n_k. Uniformly in q (s and w are bounded, and every denominator is ≥ λ), with up to two p-derivatives:
   - a, b → β̂ + O(1/m), and 1 − a·b = O(1/m²);
   - E_k − E_p = w(k) − w(p) + O(1/m). It is O(1), not O(1/m), because the Wilson term is a momentum-dependent rest energy;
   - Z-graphs: X₋ is bounded and the denominator is ≥ 2m, so they contribute O(1/m) to δE;
   - tadpole: a·τ = τ_β + O(1/m), with τ_β(p) = Σ_j⟨[W(p_j+q_j) + W(p_j−q_j) − 2W(p_j)]/(4d_j²W_γ)⟩;
   - normal graphs: −X₊/(2W_γ(W_γ + E_k − E_p)), with X₊ = Σ_jΔW_j²/d_j² − 1 + O(1/m) and ΔW_j = W(p_j) − W(k_j).
   So δE(p) = δE⁽⁰⁾(p) + R_m(p), where the remainder R_m and its first two p-derivatives are O(1/m). (R8-5's refereed Σ, continued on shell as in `vR13-7:3`.)
2. **Algebra.** For |p| < b, W(p) = 0. Use q_x → −q_x on the x-tadpole. Then δE⁽⁰⁾(p) = ⟨Φ(q; 0)⟩ + ⟨Ω(q; W(p − q_x))⟩, with Φ(q; u) = u/(2tW_γ) + (1 − A′ − u²/t)/(2W_γ(D + u)) and Ω = Φ(q; u) − Φ(q; 0). Here t = d_x² and D = W_γ + B′, B′ = W(q_y) + W(q_z). The first term does not depend on p.
3. **From energy to speed.** F = 2E_pδE, E_p² = m² + p², and F is even in p. So c_e² − 1 = ∂_{p²}F|₀ = m δE″(0) + δE(0)/m, that is, δc_e = m·∂_{p²}δE|₀ + δE(0)/(2m) = Lm + O(1).
4. **Photon-slot form.** Shift q_x → q_x + p. The p-dependence then moves to the photon side, and Ω's argument becomes W(q_x). Ω(q; 0) = 0, and on supp W we have |q_x| ≥ b, so t ≥ d(b)² > 0 and differentiating under the integral is legitimate.
5. **The photon side.** In the Theorem-D moment with M = m + w, the terms a x²/E³ and c₁(h·h′)X/E⁵ are O(m⁻³), and AX²/E⁵ and c₂X/E³ are O(m⁻²). R13-7 had already stated O(m⁻²) for Wilson-BQ terms (`C5_R13-7_report.md:122`). ∎

**Checked.**
- **Against the on-shell runner.** I fitted δc_e = Lm + c₀ + c₁/m at m = 25.6, 51.2, 102.4, λ = 0.05 (`r161_validate_L.out`, `r161_validate_D1.out`, `r161_validate_more.out`):

| law | on-shell fit L·16π² | closed form L·16π² (two quadratures) |
|---|---|---|
| BQ S1 r = 1, photon (1, 2) | +2.4437 (N = 48), +2.5348 (N = 64) | +2.50461 / +2.50461 |
| BQ S3 r = 1, photon (2, 3) | −0.2576 (N = 48), −0.2878 (N = 64) | −0.28650 / −0.28650 |
| D1(1.4, 1/√3), naive photon | +0.22655 (GL q_x, Np = 48/64/96) | +0.22655 / +0.22655 |
| D1, R13-7's uniform N = 64 grid | +0.108 (under-resolved: about 3 points across the 0.34-wide slab) | — |
| D1(1.0, 1/√3), naive photon | +0.82043 / +0.82044 (GL, two resolutions) | +0.82042 |
| D1(1.4, 1/√3), photon box (0.7, 1.4) | +0.22679 / +0.22678 | +0.22678 |
| BQ S3 r = 1, naive photon (in 𝒬_W⁺) | +0.50669 / +0.50669 | +0.50664 |

- **Runner consistency.** The anisotropic runner equals R13-7's runner on its own grid to 1e-8 (`r161_validate_D1.out:1`).
- **R13-7's data.** R13-7's archived N = 64 slopes for S1/S3 (2.540 and −0.276, `r137_mscan.out`) agree with the closed form to within 1.4% and 3.7%.
- **The tadpole piece.** κ_T·16π² = ⟨W″/(4d_x²W_γ)⟩·16π² = +4.011 for S1. This matches R13-7's "tad"-column slope of 4.064 at N = 64 (`r161_firstorder.out:4`, κ_T column).
- **First order in W** (`r161_firstorder.out:1-6`). L ≈ ¼⟨W″w⟩ = ¼⟨W w″⟩. This gives +0.0403 vs exact +0.0401 (D1, r = 0.1), +0.2327 vs +0.2266 (D1(1.4, 1/√3)) and +0.871 vs +0.820 (D1(1.0, 1/√3)). For the R8-5 r = 1 shapes it is off by 18–90%.
- **The photon side.** |δc_γ| ≤ 2e-4 at m ≥ 6.4 on D1 (`r161_mscan.out`).

### 3.3 Lemma K and the sign. Proved; checked

- **Lemma K.** Fix q⊥ and u > 0. Write T = d_y² + d_z² + λ², s = √(t + T), ρ_j = W(q_j)/|d_j|. Assume ρ_j ≤ 1 and λ ≤ d(b), and that t(q) = 2 − 2cos q (naive photon) or t = q² on the q-range considered. Then ∂²_qΩ > 0.
- **Proof.**
  1. Write Ω = g(t)/t, with g = (u/2)h(s) and
     h(s) = A′/(s + B′ + u) + B′(2 − A′)/((s + B′)(s + B′ + u)) + K₀/(s(s + B′)(s + B′ + u)).
     Here K₀ = B′² + T(1 − A′). Check: multiplying out gives A′s² + 2B′s + B′² + T(1 − A′) = D² − t(1 − A′).
  2. The coefficients are nonnegative:
     - A′ ≥ 0 and B′ ≥ 0;
     - 2 − A′ ≥ 0, because each ρ_j ≤ 1;
     - K₀ = d_y² + d_z² − (ρ_z d_y − ρ_y d_z)² + λ²(1 − A′). If A′ ≤ 1, K₀ ≥ B′² ≥ 0. If A′ > 1, both ρ_j > 0, so |q_y|, |q_z| > b and d_y, d_z ≥ d(b). Then K₀ ≥ min(d_y, d_z)² − λ² ≥ 0.
  3. Each term of h is a nonnegative coefficient times a product of factors 1/(s + c) with c ≥ 0. Each such factor is positive, nonincreasing and convex, and so is their product, since (fg)″ = f″g + 2f′g′ + fg″ ≥ 0. With s(t) increasing and concave, g is nonincreasing and convex in t: g_t = h′s′ ≤ 0 and g_tt = h″s′² + h′s″ ≥ 0.
  4. Direct differentiation, with t′² = t(4 − t) and t″ = 2 − t, gives ∂²_qΩ = (6 − t)(g/t² − g_t/t) + (4 − t)g_tt ≥ (6 − t)g/t² > 0 for t ∈ (0, 4]. For t = q²: ∂²_qΩ = 6(g/t² − g_t/t) + 4g_tt > 0.
  5. g > 0, because if B′ = A′ = 0 then K₀ = T > 0. ∎
- **Lemma K′ (no size bound on W). Proved.** Let d = 2 sin(q/2) on supp W ⊂ {|q| ≥ b}, with b ≥ b₀ = 0.505 (condition (C_b)). Then ∂²_qΩ > 0 wherever u > 0, for every W ≥ 0 and every λ > 0.
  - **Proof.**
    1. Split by the numerator N = T + 2B′s + B′² + tA′: Ω = Ω₁ + Ω₂, with Ω₁ = g₁/t, g₁ = (u/2)(T + 2B′s + B′²)φ, Ω₂ = (uA′/2)φ, and φ = 1/(s(s + B′)(s + B′ + u)).
    2. g₁ has only nonnegative coefficients without (H3). So, as in Lemma K, ∂²_qΩ₁ ≥ (6 − t)g₁/t² ≥ (6 − t)(u/2)(T + B′²)φ/t².
    3. φ is convex in t and |φ_t| ≤ 3φ/(2s²). So for t ≤ 2, ∂²_qΩ₂ ≥ −(uA′/2)·3φ(2 − t)/(2(t + T)); for t ≥ 2, ∂²_qΩ₂ ≥ 0.
    4. On supp W, t ≥ τ. If A′ > 0, some W-leg is outside the box, so T ≥ τ and B′² ≥ A′τ.
    5. Hence ∂²_qΩ ≥ (u/2)φ{(6 − t)T/t² + A′[(6 − t)τ/t² − 3(2 − t)/(2(t + τ))]}. The bracket is ≥ 0 by (C_b), and the first term is > 0. ∎
  - **(C_b) margins.** b = 1.0: +14.4; b = 1.2: +27.2; b = 1.4: +45.0; b = 0.5: −0.06 (`r161_lemmaK2.out:1`).
  - **Sampled** (4e5 each; W/d up to 1e3, λ up to 10, u up to 1e3): min ∂²_qΩ/Ω = +0.045 at b = 0.505, +0.11 at b = 1.0, +0.17 at b = 1.4. Below b₀ (b = 0.3, 0.5) it is +0.027 and +0.048, still positive, but not covered by the proof (`r161_lemmaK2.out:2-6`).
- **Corollary.** In 𝒬_W⁺, L > 0 strictly. The integrand of L is zero where W(q_x) = 0 (since Ω(·; 0) ≡ 0) and positive where W(q_x) > 0 (by (H2′), and (H3) with Lemma K or (H3′) with Lemma K′). W is continuous and W ≢ 0.
- **Checked** (`r161_signW.out`).
  - **Sampling.** 4e5 random samples per row: min ∂²_qΩ/Ω = +0.56 (naive) and +1.20 (continuum) at ρ ≤ 1. It stays positive at ρ ≤ 2, 4 and 16 (+0.44 … +0.20).
  - **L·16π² on D1** (lines 11-64):

| b | r = 1/√3 | r = 0.4 | r = 0.1 |
|---|---|---|---|
| 1.4 | +0.2266 | +0.1582 | +0.0401 |
| 1.2 | +0.5017 | +0.3523 | +0.0903 |
| 1.0 | +0.8204 | +0.5779 | +0.1491 |

    These are at λ = 0.05 with the naive photon. The photon box (b/2, b) changes them by ≤ 0.0004, and λ ∈ {0.01, 0.2} by ≤ 0.001. L is λ-continuous down to λ = 0: on supp W the integrand has no IR singularity.
  - **Beyond (H3).** BQ boxes with the naive photon have L > 0 for every r ∈ {1, …, 32} and all three boxes (lines 65-82). Up to r = 32, W/d reaches 32. Boxes (1, 2) and (2, 3) are covered by Lemma K′; box (0.5, 1.5) is just below b₀ and only checked.

### 3.4 Corollary: the interval no-go on Wilson edges. DERIVED (worker)

For every law in 𝒬_W⁺ at fixed λ > 0:
- δc_e = Lm + O(1) with L > 0 (Theorem W, with Lemma K or Lemma K′);
- δc_γ = O(m⁻²), and any extra species contribute a bounded amount;
- so Δ_λ(m) → +∞, and Δ_λ ≢ 0;
- by Lemma A_W, **Δ_λ vanishes on no open mass interval**.

The class contains D1(r) for every r ≤ 1/√3 at b = 1.4, 1.2 and 1.0, with any (H2′) photon. It also contains R8-5's r ≤ 1 boxes with (H2′) photons (for λ ≤ d(b₁)), and every R8-5 box with b₁ ≥ 0.505 and the naive photon at any r. Theorem W does not use |s′| ≤ 1 or any property of s beyond C², oddness, periodicity and box exactness.

### 3.5 Outside 𝒬_W⁺ (the REFUTED direction). Checked

- **Without (H2′),** with the photon plateau transition on the Wilson edge, L takes both signs. R8-5's shapes at r = 1 give S1 +2.505, S2 +0.483, S3 −0.287, S5 +8.168, S7 +1.080, S8 −0.983 (`r161_signW.out:84-89`). D1 with an on-slab photon transition stays positive (+0.202, +0.214; `r161_signW.out:90-91`).
- **Tuning L to zero.** In the family BQ(b₁, b₁ + 1, r = 1) with photon box (b₁, b₁ + 1), L vanishes at b₁* = 1.75137691 (`r161_tuneL.out:2`). There the on-shell δc_e = −2.657, −2.405, −2.275 at m = 25.6, 51.2, 102.4, identical at two resolutions. The fit gives L·16π² = +0.0001 and **c₀ = −2.16**, or −2.14 with L fixed at 0, and c₁ ≈ −13. So the next coefficient is nonzero, and Δ → c₀ ≠ 0 (checked; not proved). This tuned law is superluminal, with v_max = 4.40 (m = 0.1) and 4.72 (m = 1) (`r161_vmax_BQ.out:7`). This repeats R13-7's pattern beyond (H2) (`vR13-7:26`).
- **No interval-zero law found.** REFUTED is not met.

### 3.6 Probe (c): Δ_λ(m) on D1(b = 1.4, r = 1/√3), naive photon, λ = 0.05. Checked

- **Method.** Composite Gauss–Legendre panels on every axis, refined near q = 0 (down to 0.0125) and across the slab. Resolutions R1 = (6, 4), R2 = (8, 6) and R3 = (12, 8) GL nodes per panel for (q_x, q⊥): 300×200², 400×300² and 600×400² nodes. Richardson step h = min(0.02, m/8) (`r161_mscan.out`). Units: e²/16π².

| m | δc_e | δc_γ | Δ_λ (R1 / R2 / R3) |
|---|---|---|---|
| 0.005 | −10.1981 | +0.6757 | −10.8738 / −10.8738 / −10.8738 |
| 0.01 | −10.1956 | +0.6749 | −10.8705 / −10.8705 / −10.8705 |
| 0.02 | −10.1903 | +0.6734 | −10.8637 (all three) |
| 0.05 | −10.1722 | +0.6683 | −10.8405 (all three) |
| 0.1 | −10.1356 | +0.6581 | −10.7937 (all three) |
| 0.2 | −10.0424 | +0.6317 | −10.6742 (all three) |
| 0.4 | −9.7987 | +0.5605 | −10.3592 (all three) |
| 0.8 | −9.2034 | +0.3898 | −9.5932 / −9.5931 / −9.5932 |
| 1.2 | −8.5970 | +0.2428 | −8.8398 / −8.8397 / −8.8397 |
| 1.6 | −8.0463 | +0.1431 | −8.1895 / −8.1893 / −8.1894 |
| 2.0 | −7.5662 | +0.0826 | −7.6488 / −7.6486 / −7.6487 |
| 2.5 | −7.0569 | +0.0415 | −7.0985 / −7.0983 / −7.0983 |
| 3.0 | −6.6298 | +0.0211 | −6.6509 / −6.6507 / −6.6507 |
| 6.4 | −4.8106 | −0.0001 | −4.8105 / −4.8101 / −4.8102 |
| 12.8 | −2.8092 | −0.0002 | −2.8090 / −2.8083 / −2.8085 |
| 25.6 | +0.3781 | −0.0000 | +0.3781 / +0.3796 / +0.3792 |

- **Δ_λ(0⁺) = −10.877** (linear extrapolation from m = 0.005, 0.01; the resolutions agree to 1e-4). So c_e − c_γ ≈ −6.3e-3, about 2.4e16 times the 2.66e-19 photon-decay bound (`C5_R8-5_report.md:261`).
- **Shape.** Δ_λ is smooth and monotone on [0.005, 25.6]. It changes sign once, near m ≈ 24 (from the fit Lm + c₀ + c₁/m with L = 0.2266, c₀ = −5.13, c₁ = −7.44). This is an isolated zero, allowed by Lemma A_W.
- **Comparison.** R13-7's uniform N = 64 runner under-resolves D1 (§3.2). The GL panels converge to 4 digits.

### 3.7 Probe (d): 𝒬_W^P

- **(P-a) Selectrons only. Proved; checked.** With matched masses, the selectron photon coefficient is O(m⁻²). Each R13-1 term is a ratio such as Γ²/ε⁵ with Γ ~ W′m, or ∂²ε²/ε³ ~ mW″/m³. The electron's self-energy is unchanged at one loop. So Theorem W and §3.4 carry over: Δ^{Pa} → +∞ with the same L. Checked: the two-selectron δc_γ is −3.2e-3, −3.0e-4 and −3e-5 at m = 6.4, 12.8 and 25.6 (`r161_partner_mscan.out`), and decays at least like m⁻² through m = 102.4 on R13-1's own runner (`r161_partners.out`).
- **(P-b) R13-1's minimal SQED (plus the photino and its Yukawa loop). Suggested; checked.**
  - The selectron–photino loop carries the heavy selectron's normalization 1/(2ε) ≤ 1/(2m). Its normal denominator is ω(q) + ε(p − q) − E_p ≥ (1 − v)|q|.
  - So δE_partner and its p-derivatives are O(1/m). Its contribution to δc_e is m·O(1/m) = O(1), and L is unchanged (power counting; sketch).
  - Lemma A_W here needs the massless photino's threshold singularity, ~1/|q|, to stay integrable under complex m. I argue that it does, but have not written it out (suggested).
  - Checked: the partner δc_e on D1 is −1.088, −0.479 and −0.185 at m = 6.4, 12.8 and 25.6 (GL, R1). It stays bounded on R13-1's own runner (two grids, D1 and BQ S3 naive): |δc_e^partner|/m ≤ 9e-3 at m = 25.6 and ≤ 4e-3 at m = 102.4 (`r161_partners.out`).
  - Values for the partner legs: `r161_partner_mscan.out` (R1, R2), `r161_partner_hires.out` (R3 subset), `r161_selectron_smallm.out` (q-extrapolation control).
- **The selectron leg needs q ≪ m.** With R13-1's q = 2π/256 the small-m values are biased: −1.066 at m = 0.005, against −0.831 with q = 2π/4096 (`r161_selectron_smallm.out`). The table below uses the controlled values.

**Δ_λ(m) with partners on D1(1.4, 1/√3), naive photon, λ = 0.05** (`scripts/r161_combine.out`). Units: e²/16π². The electron's photon loop and the Dirac δc_γ are R2 values from §3.6. The selectron δc_γ uses Nref = 4096 for m ≤ 0.05 and Nref = 256 (q = 0.025 ≪ m) above. The (12,8) subset for the selectron leg agrees to ≤ 6e-4.

| m | δc_γ(2 selectrons) | δc_e(partner loop) R1 / R2 / R3 | Δ^{Pa} (R2) | Δ^{Pb} (R2) |
|---|---|---|---|---|
| 0.005 | −0.8310 (q-controlled) | −8.7459 / −8.7457 / — | −10.0428 | −18.7886 |
| 0.01 | −0.8299 (q-controlled) | −8.7310 / −8.7310 / −8.7310 | −10.0406 | −18.7716 |
| 0.02 | −0.8278 (q-controlled) | −8.7009 / −8.7009 / — | −10.0359 | −18.7369 |
| 0.05 | −0.8216 (q-controlled) | −8.6068 / −8.6068 / — | −10.0189 | −18.6257 |
| 0.1 | −0.8100 | −8.4399 / −8.4399 / −8.4399 | −9.9837 | −18.4236 |
| 0.2 | −0.7798 | −8.0835 / −8.0835 / — | −9.8943 | −17.9778 |
| 0.4 | −0.6979 | −7.3463 / −7.3463 / — | −9.6613 | −17.0075 |
| 0.8 | −0.4996 | −5.9954 / −5.9954 / −5.9954 | −9.0935 | −15.0889 |
| 1.2 | −0.3253 | −4.9163 / −4.9163 / — | −8.5144 | −13.4307 |
| 1.6 | −0.2034 | −4.0873 / −4.0873 / — | −7.9859 | −12.0732 |
| 2 | −0.1266 | −3.4524 / −3.4524 / — | −7.5220 | −10.9744 |
| 2.5 | −0.0715 | −2.8559 / −2.8558 / — | −7.0268 | −9.8826 |
| 3 | −0.0420 | −2.4125 / −2.4124 / −2.4124 | −6.6087 | −9.0211 |
| 6.4 | −0.0032 | −1.0878 / −1.0877 / — | −4.8069 | −5.8946 |
| 12.8 | −0.0003 | −0.4788 / −0.4787 / — | −2.8080 | −3.2867 |
| 25.6 | −0.0000 | −0.1851 / −0.1850 / −0.1850 | +0.3795 | +0.1945 |

- **Δ^{Pa}(0⁺) ≈ −10.045 and Δ^{Pb}(0⁺) ≈ −18.81** (linear extrapolation from m = 0.005, 0.01).
- **Sign changes.** Both cross zero once, near m ≈ 24–25, and then grow like Lm, with the same L, because the partner leg tends to a constant (−0.185 at m = 25.6, still shrinking).
- **Comparison with R13-1.** On D1 the partner loop is −8.7 at small m. That is close to R13-1's literal-edge values (−5.4 to −11.7), not its gapped-edge values (−1.6 to −1.8) (`C5_R13-1_report.md:218-225`). D1's corners are light (W_π = 0.095/a), so this is the expected side (reading). R13-1 had λ = m; here λ = 0.05 is fixed.


### 3.8 Physical size, self-force and Ward (S17 rules; reading)

- **Size at physical masses.** At a = ℓ_P an electron has m ≈ 4e-23. The linear term is L·m·e²/16π² ≈ 5e-27 on D1(1.4), unobservable. The physical statement is R13-7's: a structural zero is excluded, and one tuning of Δ(0⁺) remains the cheapest named price (P73, `C5_S17_synthesis.md:227`; the count is R16-2's question).
- **Self-force on a moving compact body.** No new frame-tied kernel is introduced. The quantity computed is itself the one-loop frame-tied self-energy of a uniformly moving charge.
  - At constant crystal momentum there is no self-force.
  - Its inertia is renormalized: 1/m_kin = 1/m + 2e²L_raw + O(e²/m), where e²L_raw = (e²/16π²)(L·16π²).
  - On D1(1.4) this caps the kinetic mass of an elementary Wilson-edge charge at m_kin ≲ 1/(2·5.8e-4·0.227) ≈ 3.8e3/a.
  - This bites only for super-Planckian elementary charges. Composite bodies are not covered (reading).
- **Ward.** Standard: the exact lattice U(1) WT identity of Peierls coupling (`C5_R8-5_report.md:140`). No deformed identity is used.

## 4. Against the FIXED readings (`TESTS:5057-5060`)

**Worker reading: DERIVED** (same family, unrefereed; the codex referee is required).
- **The class.** 𝒬_W⁺ is stated in §1. It contains D1(r ≤ 1/√3) at b = 1.4, 1.2, 1.0 with every (H2′) photon, at fixed λ > 0. It also contains R8-5's r ≤ 1 boxes with (H2′) photons (λ ≤ d(b₁)), and R8-5 boxes with b₁ ≥ 0.505, the naive photon and any r.
- **The proof.** Lemma A_W (§3.1), Theorem W (§3.2), Lemma K or K′ (§3.3), §3.4.
- **The numbers.** Checked in §§3.2–3.6.
- **REFUTED: not met.** Outside 𝒬_W⁺, L takes both signs, but a law tuned to L = 0 keeps c₀ ≈ −2.15 (§3.5). No untuned interval-zero law exists in 𝒬_W⁺, by proof.
- **Variant 𝒬_W^P.**
  - (P-a), selectrons only: DERIVED-level, by the same proof (§3.7).
  - (P-b), with the photino Yukawa loop: SUGGESTED. Power counting and the Lemma A_W extension are sketched, and the partner leg's boundedness is checked.
- **Scope that must travel with the reading.**
  - one loop, Feynman gauge, Peierls, λ > 0;
  - b > 0 box laws with W = 0 on the box and W ≥ 0; plus either W ≤ |d| (and λ ≤ d(b) if A′ > 1), or a naive photon on the edge with b ≥ 0.505;
  - (H2′) photons on supp W;
  - extra species bounded on the photon side.
- **Not covered.**
  - λ = 0 (L itself is λ-continuous, but Lemma A needs λ > 0);
  - plain Wilson without a box;
  - Clifford-flat electrons;
  - non-Peierls or ℓ¹ generators;
  - photon transitions on the Wilson edge, where L takes both signs;
  - two loops.

## 5. Prices (named, not adopted)

- **No axiom text is touched.** Dynamics is downstream (`AX:114-130`), and the theorem is a law-level statement.
- **No new price.** The result closes S17's "W1 open only because the proof does not cover the used law" (`C5_S17_synthesis.md:192`) for the Peierls one-loop Wilson class. On D1, the subluminal Dirac edge of P61, the split has no structural zero, so removing it still costs P73: one tuning of Δ(0⁺), here −10.88·e²/16π² at λ = 0.05, by a counterterm or a shape condition. That this one tuning serves every light species is R16-2's question, not settled here.
- **Reading.** D1's corner doublers have mass m + nW_π, with W_π = 0.095/a at b = 1.4. They are Planckian at a = ℓ_P, so R9-1's same-mass Z-width exclusion (`TESTS:3840`) does not transfer to D1. A refereed Z-width check on D1 has not been done.

## 6. Strong-word check

- **"Proved":**
  - Lemma A_W (identity theorem, given (H0) and λ > 0);
  - Theorem W (a uniform 1/m expansion with dominated convergence, at R13-7 Theorem H's level of rigor; O(1/m) remainders bounded, not computed);
  - Lemma K and Lemma K′ (closed-form calculus; b₀ = 0.505 from a 1-D numerical minimum of the polynomial in (C_b), checked on a 20001-point grid);
  - the corollary;
  - (P-a).
- **"Checked":** every number, with grid, λ, h and m in the `.out` files.
  - The L closed form agrees with on-shell fits: to ≤ 1e-4 relative on four members with GL q_x nodes, and to ≤ 1.2% on R8-5's S1/S3 with R13-7's uniform N = 64 grid. The residual there is under-resolution of the uniform grid.
  - In §3.6 the three resolutions agree to ≤ 2e-4 for m ≤ 3, and to ≤ 1.5e-3 at m = 12.8 and 25.6.
- **"Strictly positive"/"cannot vanish":** only in 𝒬_W⁺ at λ > 0.
- **(H3) removed** only under (H3′), that is, b ≥ 0.505 with the naive photon (Lemma K′). Below that it is suggested, from sampling.
- **Not claimed:**
  - any statement at λ = 0, or for the full registered 𝒬_W without (H0) and without one of (H3)/(H3′);
  - a sign of c₀ (the O(1) term);
  - anything at two loops or for non-Peierls vertices.

## 7. For the referee

1. **Theorem W's heavy expansion** (§3.2, step 1): that X₊ → Σ_jΔW_j²/d_j² − 1 and E_k − E_p → w(k) − w(p) uniformly, with p-derivatives. Check against `r161_validate_L.out` and `r161_validate_D1.out`.
2. **The algebra Φ(u) − Φ(0) = Ω** and the photon-slot shift (step 4). `r161_heavy.py` computes both forms independently; they agree to 2–4e-7 relative (`scripts/r161_twoforms.out`), the p-difference's own finite-difference error.
3. **Lemma K:** the decomposition of h(s) (multiply out), the K₀ ≥ 0 case split under (H3), and the identity ∂²_qΩ = (6 − t)(g/t² − g_t/t) + (4 − t)g_tt. **Lemma K′:** the bounds |φ_t| ≤ 3φ/(2s²) and B′² ≥ A′τ, and (C_b) at b₀ = 0.505.
4. **Lemma A_W's added hypothesis (H0).** Whether W ≥ 0 should be read as part of the registered 𝒬_W.
5. **(P-b):** whether the power-counting sketch for the partner loop and the photino-threshold analyticity suffice, or must be written out.

## 8. Files

All in `S/scripts/`, listed in the header. No downloads.
