# C5 R14-3 report: subluminal edges — can any subluminal box law cancel the free shear mass μ_E or the graviton-cone shift Ξ?

**Author.** Claude Opus 5.5 probe. Same model family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 21:13Z to about 21:45Z. No repository file was edited. No downloads, no web lookups.

**Scratch.** `S/` = `.../scratchpad/C5/R14-3/`. Scripts and outputs are in `S/scripts/`. Each run took under 2.5 min at `OMP_NUM_THREADS=2`.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: the C5 method and readings (`:2302-2320`); R8-2 and Theorem E (`:3455-3466`, verdict `:3550-3557`); R9-2 (`:3643-3672`, verdict `:3889-3900`); R9-9 (`:3862-3872`, verdict `:3939-3950`); R11-3 (`:4157-4176`, verdict `:4417`); R13-4/R13-5 worker readings (`:4705-4733`, `:4767-4776`); R14-1 (`:4779-4817`); R14-3 (`:4830-4844`, my item).
- `agents/C5_R14-1_report.md` (all); `C5_R9-2_report.md` §5 (`:217-252`) and its verdict; `C5_R9-9_report.md` §§1, 3.4 (`:32-160`) and its verdict; `C5_R8-2_report.md` (Theorem E, through R8-2's verdict); R13-4's Lemma V (through R14-1 §5(b) and its referee).
- The R14-1 referee verdict, which appeared during this run: `scratchpad/C5/ref_R14-1/REFEREE_VERDICT.md:1-19` (CONFIRMED WITH CORRECTIONS, PASS; §5 at `:13`: "A ≤ 0 is confirmed for the constructed S/G families, not for all subluminal bands"; "the tested positive μ_E values are finite-family evidence only").
- The scripts `scripts/C5/R9-2/r92_shear.py`, `r92_shear_tune.py`, `scripts/C5/R9-9/r99_tt_selfenergy.py`, `r99_profiles.py`, `scripts/C5/R14-1/sublum.py`, `r141_shear.py`.

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **(a) is false. A subluminal edge can cancel the shear mass.** The simplest example is R14-1's own gapped band G(b), with one change: the band flattens beyond the box over a width w instead of over the whole edge.
   - R14-1's G(1.4) (w = 1.74) gives μ_E = +4.33e-3.
   - Narrower drops give μ_E < 0: −2.5e-4 at w = 0.2.
   - At w* = 0.3444 (m → 0), μ_E = 0 to 1e-13.
   - Every member has 0 ≤ h′ ≤ 1. So it is subluminal for every mass and every d (R14-1's bound, refereed), and A ≤ 0 holds pointwise.
   - Checked three ways: a separable Laplace evaluation, the direct 3D zone grid, and R9-2's original A-form.
2. **Why the sign flips (proved rewriting).** μ_E is minus the cubic (l = 4) anisotropy of the gravitating-momentum distribution. A band that rolls off slowly leans toward the body diagonals, giving μ_E > 0. A band that flattens abruptly piles weight at f = 0 on some axes, giving μ_E < 0. The continuum has exactly zero.
3. **The tuning is one per edge shape, not one per species (proved, checked).** μ_E(m) is analytic in m² near 0, so w*(m) = w*(0) + 0.056m² + …. All light species that share the edge are cancelled by one choice, with residual O((ma)²). This corrects R9-2's price wording "one mass-dependent tuning per species" (`C5_R9-2_report.md:243,258`) for light species.
4. **(b) holds on a large class (proved), and fails outside it (checked).**
   - **Theorem B.** Take any law with |σ′| ≤ 1, where g = σ², whose √g has no gapped valley: every local minimum of g is a zero of g. Then Ξ < 0 for every nonzero vertex of R9-9's class, at every mass.
   - This needs no pointwise A ≤ 0. It covers S(b), G(b), the flattened bands of item 1, terrace bands with A up to +56, and the nearest-neighbour scalar.
   - **Outside that class:** two explicit subluminal laws with gapped edge valleys, 0.71/a and 0.94/a below the box face, have Ξ_{M,Eg} > 0 and Ξ_{U,Eg} > 0 at light mass. T_2g stayed negative in every law tried.
5. **What this does to the item's dilemma (reading).**
   - **The shear.** It needs no superluminal edge, only one edge-shape tuning, and only under the supplied zero-point vacuum. The empty Fock vacuum still gives zero.
   - **The graviton cone.** In the no-valley class no edge shape can zero Ξ; that is proved. Making Ξ_{E_g} ≥ 0 needs Planck-mass edge valleys plus a tuning, and T_2g was not achieved.
   - **So the choice is not "causality or tuning".** Causality costs nothing in either sector. Tuning, or valley structure plus tuning, remains.

**Against the FIXED readings (`TESTS:4841-4844`): REFUTED (worker reading; referee required).** I give explicit, checked subluminal laws with μ_E = 0 (§3.2) and with Ξ ≥ 0 (§3.4). DERIVED is out, because (a) fails. Separately, Theorem B proves (b) on the stated no-valley class (§3.3).

---

## 1. Class and hypotheses (stated before any title)

- **Laws.** Separable one-band box laws, ε(k)² = m² + Σᵢ g(kᵢ) (d = 3, m > 0), as in R8-2, R9-2, R9-9 and R14-1.
  - g = σ², with σ ∈ C²[0, π], σ(0) = 0 and σ′ = 1 on [0, b] (the box: g = k²).
  - g is extended evenly and 2π-periodically; C² needs σσ′(π) = 0.
  - Odd-symbol laws (ε² = m² + Σs², s odd) are the case σ = s, s(π) = 0. Even "gapped" forms are the case σ(π) > 0.
  - Notation: f = g′/2 = σσ′ (R8-2's forward momentum density p) and A = g″/2 − 1 = σ′² − 1 + σσ″ (Theorem E's anomaly, axis component).
- **Class 𝒮: subluminal for every mass.** Here |σ′| ≤ 1 on [0, π].
  - **Why this class (proved).** |∇ε|² = Σfᵢ²/(m² + Σgᵢ) ≤ Σgᵢ/(m² + Σgᵢ) < 1. Conversely, if |σ′(k₀)| > 1 then along (k₀, 0, 0) the speed tends to |σ′(k₀)| > 1 as m → 0.
  - So 𝒮 is exactly "subluminal for all light species sharing the edge", the physical case (m·a ≪ 1).
  - It contains R14-1's S(b) and G(b) (`C5_R14-1_report.md:45-48`) and R13-4's odd symbols.
  - Laws subluminal only above some mass are treated separately (§3.5).
- **Class 𝒰₀ ⊂ 𝒮: no gapped valley.** On every maximal arc of the circle where g > 0, √g is unimodal. Equivalently, there are no k₁ < k₂ < k₃ in such an arc with g(k₂) < min(g(k₁), g(k₃)). Flat stretches are allowed.
- **Shear.** R9-2's conditional free shear (`C5_R9-2_report.md:219-231`, method confirmed `C5_R9-2_referee_verdict.md` item 6):
  - E_g uniform-strain susceptibility of R8-2's universal box ⊕ edge stress;
  - supplied scalar zero-point vacuum +ε/2, RN-L1 normalization.
  - The Dirac-sea reading (−ε) multiplies μ_E by −2, so it has the same zeros.
  - In R8-2's actual empty Fock vacuum, μ_E ≡ 0 (refereed, `TESTS:3897`). Everything here is conditional on the supplied vacuum.
- **Graviton cone.** R9-9 Theorem T (refereed, `TESTS:3945`): Ξ = (1/32)⟨|V|²A_zz/ε⁵⟩.
  - Class 𝒱: q ∥ z, |V|² ≥ 0 depending only on (k_x, k_y), ultralocal seagull.
  - Vertices evaluated: M (minimal metric: T_2g 4g_xg_y, E_g (g_x − g_y)²) and U (forward-stress: T_2g 4f_x²f_y², E_g (f_x² − f_y²)²), as at `C5_R9-9_report.md:44-46`.
  - The R9-9 referee's caveats carry over: the pair stress's Ward completion is assumed; Ξ is the graviton-cone shift relative to the bare cone, not a dressed graviton–matter split (`C5_R9-9_referee_verdict.md` items 1, 5).
- **Not addressed.**
  - Non-separable laws, Wilson–Dirac laws (R14-1 §6), and q off-axis.
  - Matter's own one-loop speed shift (R11-1(b)).
  - T_2g–E_g mass splits; two loops.

## 2. Prior art (each counted once)

- **R9-2** (refereed): edge-carried μ_E = −0.2057 (literal L), +7.976e-3 (R8-2 gapped G) at m = 1; t* = 0.287922 in the L→G family (`TESTS:3897-3900`).
- **R14-1** (refereed CONFIRMED WITH CORRECTIONS, PASS; `ref_R14-1/REFEREE_VERDICT.md:13,19`):
  - A ≤ 0 pointwise in S/G, hence Ξ < 0 there;
  - μ_E > 0 for S(1.4), G(1.4) and R8-2-gapped (+5.063e-3, +3.525e-3, +7.976e-3);
  - the t* edge is superluminal (d = 3 v_max = 1.734 per the referee);
  - "whether some subluminal edge does [cancel μ_E]: open" (`C5_R14-1_report.md:181`).
- **R9-9 Lemma N** (with the referee's richness caveat): no band has Ξ = 0 for *all* abstract vertices (`C5_R9-9_report.md:152`). Theorem B below is a different statement: a sign for every vertex on a band class.
- **R9-9 G-edge sign proof** (A_zz ≤ 0 ⇒ Ξ < 0, `C5_R9-9_report.md:147-150`). Theorem B removes the pointwise hypothesis.
- **V3** NN-scalar μ_E = +1.97038864e-3 (comparator, `PRICE_NOTE:290-295`). Reproduced in R9-2's calibration.

---

## 3. Results

### 3.1 Two exact rewritings (proved) and the evaluator (checked)

**(R1) Shear as a cubic anisotropy.** Integrate R9-2's closed form μ_E = −(1/8)⟨(f′_x − f′_y)(f_x² − f_y²)/ε⟩ by parts in k_x (periodic; ∂_xε = f_x/ε):

  μ_E = (1/12)⟨(3f_x²f_y² − f_x⁴)/ε³⟩ = −(5/72)⟨K₄(f)/ε³⟩, where K₄(p) = Σpᵢ⁴ − (3/5)|p|⁴ (d = 3).

- K₄ > 0 along cube axes and < 0 along body diagonals.
- **Kurtosis form.** Write ε⁻³ = Γ(3/2)⁻¹∫t^{1/2}e^{−tε²}dt. Then

  μ_E = [12Γ(3/2)]⁻¹ ∫₀^∞ t^{1/2} e^{−tm²} E₀(t)[3F₂(t)² − F₄(t)E₀(t)] dt, with (E₀, F₂, F₄)(t) = ⟨(1, f², f⁴)e^{−tg}⟩_{1D}.

- The bracket is the kurtosis defect of the e^{−tg}-weighted 1D law of f. For the continuum Gaussian (f = k, g = k² on ℝ) it vanishes identically: the Lorentz control.

**(R2) Graviton cone without second derivatives.** Integrating by parts in k_z gives ∫A(B + g)^{−5/2}dk = ∫[5f² − (B + g)](B + g)^{−7/2}dk. Hence

  Ξ = (1/32)⟨|V|²(5f_z² − ε²)/ε⁷⟩.

For the four vertices both pieces factorize: (1D moments) × Laplace integral (`S/scripts/lap.py`).

**Calibration (checked, `calib.out`, `lapcheck.out`).**
- The Laplace evaluator reproduces R14-1 to 7–8 digits:
  - G(1.4): μ_E = +3.52543170e-3 (m = 1) and +4.25201261e-3 (m = 0.3), against `r141_shear_extra.out` +3.525432e-3 and +4.252013e-3;
  - S(1.4): +5.06312821e-3, against +5.063092e-3 at R14-1's N = 480.
- The 3D grid in both forms agrees.
- Ξ (all four vertices) agrees between the A-form, the IBP form and the Laplace form to 4–7 digits.
- v_max (d = 3, exact for separable laws by bisection on max_k(f² − λg)) gives G(1.4), m = 0.3: 0.993864, as R14-1's referee found.

### 3.2 (a) is false: subluminal laws with μ_E < 0 and μ_E = 0 (checked; the IVT step proved)

**The one-step family G_w(b)** (`verify_a.out`, `root_w.out`):
- σ′ = 1 − sstep((k − b)/w) on [b, π]. R14-1's G(b) is the case w = π − b.
- **Subluminal.** 0 ≤ σ′ ≤ 1, so G_w is in 𝒮 for every w.
- **A ≤ 0.** σ″ ≤ 0, so A ≤ 0 pointwise, as R14-1's §5(d) proof applies verbatim.

μ_E at m = 0.1:

| b | w = π − b (R14-1's G) | w = 1.0 | 0.5 | 0.2 | 0.1 | 0.05 |
|---|---|---|---|---|---|---|
| 0.4 | +1.59e-3 | −9.8e-5 | −1.59e-4 | −1.60e-4 | −1.57e-4 | −1.56e-4 |
| 0.8 | +2.46e-3 | +4.2e-5 | −3.00e-4 | −4.19e-4 | −4.48e-4 | −4.61e-4 |
| 1.4 | +4.33e-3 | +1.54e-3 | +3.01e-4 | −2.51e-4 | −4.08e-4 | −4.82e-4 |

**The root at b = 1.4** (bisection; μ_E is continuous in w):

| m | w* | \|μ_E(w*)\| | v_max (d = 3) | A range |
|---|---|---|---|---|
| 1.0 | 0.389586 | 8e-15 | 0.928124 | [−8.86, 0] |
| 0.3 | 0.349416 | 6e-14 | 0.992718 | [−9.68, 0] |
| 0.1 | 0.344939 | 2e-14 | 0.999177 | [−9.78, 0] |
| 0.01 | 0.344371 | 3e-14 | 0.999992 | [−9.80, 0] |

- **Independent 3D-grid check** at m = 0.3, w*:
  - IBP form: −5.1e-10 (N = 240), −8.1e-11 (N = 400);
  - A-form: +6.6e-6 (N = 240), +6.6e-9 (N = 400);
  - for comparison, G(1.4) is +4.252e-3.
  - At w = 0.25: Laplace −1.70647e-4, grid N = 400 −1.70646e-4. At w = 0.35: +1.04355e-6 and +1.04347e-6.
- **Ξ at the root is negative for all four vertices**, as Theorem B requires. At m = 0.01: M,T2g −2.96e-3, M,Eg −1.04e-3, U,T2g −3.41e-4, U,Eg −3.29e-4.
- **Quasi-locality (checked, `tails.out`).** The 1D hopping kernel |ε_r| (m = 0.3) of G_w* is 4.5e-8 at r = 128 and 2.0e-13 at r = 512, against S(1.4)'s 9.6e-8 and 6.7e-13 (R14-1's accepted law). Same Gevrey class.

**Backups** (`root.out`, `verify_a.out`):
- Monotone "terrace" bands, with 0 ≤ σ′ ≤ 1 and a flat stretch then a second rise:
  - E1 (b = 0.6): μ_E = −1.3796e-3 at m = 0.3; Laplace −1.379626e-3, grid N = 560 −1.379630e-3.
  - E2 (b = 1.4, sharp): −4.97e-4; grid N = 560 −5.0005e-4.
- These have A up to +13 and +56: pointwise A > 0 inside 𝒮.
- The convex interpolation σ′_t = (1 − t)σ′_{G(1.4)} + tσ′_{E2} stays in 𝒮. Its root is t* = 0.8833 (m = 1), 0.8928 (0.3), 0.8939 (0.1), 0.8940 (0.01), with |μ_E| ≤ 2e-12 and v_max < 1. Grid N = 560 gives |μ_E| ≤ 2e-6 at t*, against 4.25e-3 at t = 0.

**Mechanism (reading, from R1).**
- A slow roll-off keeps |f| spread like a cube's corners: diagonal-leaning, μ_E > 0. This was the NN scalar's and R14-1's case.
- An abrupt flattening puts a large measure at f = 0 on one axis while the others stay large: axis-leaning, μ_E < 0.
- R9-2's literal edge was axis-leaning for a different reason: |f| exceeded √g, the superluminal tail.

**Mass dependence: one tuning per edge shape (proved; checked).**
- **Argument.** Suppose g > 0 off k = 0 and g = k² on the box. The full-line Gaussian moments obey 3G₂² = G₄G₀ exactly. Every remaining term of 3F₂² − F₄E₀ carries a box tail or an edge moment, which is O(poly(t)·e^{−tg_*}) with g_* = min(b², min_edge g) > 0.
- So t^{1/2}E₀[3F₂² − F₄E₀] decays exponentially, and μ_E(m) is real-analytic in m² for m² > −g_*. Hence μ_E(m) = μ_E(0) + O(m²), and the root moves by O(m²).
- **Checked.**
  - G_w: w*(m) − w*(0.01) = 0.0561·m² (m = 0.3) and 0.0568·m² (m = 0.1).
  - Mix at fixed t*(0.01): μ_E(m) = 7.05e-9 − 6.6e-5·m², from m = 3e-4 to 1 (`resid.out`, `resid2.out`; resolution-independent at n = 2^15–2^18).
- **Consequence (reading).** At a = ℓ_P every known particle has ma ≲ 1.4e-17. So a single edge-shape choice cancels the conditional shear of every light scalar species sharing that edge, to residual ~1e-34·|dμ_E/dm²|.
- **Dated correction to recommend.** R9-2's "one mass-dependent edge tuning per species" (`C5_R9-2_report.md:243,258`) should read "one edge-shape tuning per edge, mass-dependent only at O((ma)²)". R9-2's own roots, 0.287922 (m = 1) and 0.297708 (m = 0.3), are consistent with O(m²).

### 3.3 Theorem B: (b) holds on the no-valley class 𝒰₀ (proved; checked)

**Statement.** Let σ ∈ C²[0, π], σ(0) = 0, σσ′(π) = 0, |σ′| ≤ 1, with g = σ² in 𝒰₀. Then for every B > 0:

  I(B) := ∫_{−π}^{π} A(k)(B + g(k))^{−5/2} dk < 0.

Hence, for every m > 0 and every vertex in 𝒱 with |V|² ≥ 0 not a.e. zero:

  Ξ = (1/32)(2π)⁻³∫d²k_⊥|V|²(k_⊥) I(m² + g(k_x) + g(k_y)) < 0.

The box is not needed. The NN scalar is covered (σ = 2 sin(k/2), σ′ = cos(k/2) ∈ [0, 1]).

**Proof.**
1. By (R2), I(B) = 2∫₀^π [5h²h′² − (B + h²)](B + h²)^{−7/2}dk, with h = |σ|. Here h is Lipschitz, |h′| = |σ′| ≤ 1 a.e., and h²h′² = σ²σ′².
2. **Rising stretch** (0 ≤ h′ ≤ 1). Pointwise, 5h²h′² ≤ 5h²h′ and B + h² ≥ (B + h²)h′. So the integrand is ≤ (4h² − B)(B + h²)^{−7/2}h′, and strictly negative where h′ = 0.
3. Since d/dx[−x(B + x²)^{−5/2}] = (4x² − B)(B + x²)^{−7/2}, the AC change of variables gives ∫_rise ≤ F(h_hi) − F(h_lo), with F(x) := −x(B + x²)^{−5/2} ≤ 0.
4. A falling stretch gives the same bound with |h′|.
5. In 𝒰₀, [0, π] splits into unimodal bumps between zeros of g, each ≤ [F(P) − F(0)] × 2 = 2F(P). If h(π) > 0 there is a final nondecreasing piece up to π (symmetry plus unimodality on the arc through π forces the peak at π), which contributes ≤ F(h(π)).
6. All terms are ≤ 0. The piece containing the box has peak ≥ b > 0, so its term (2F(P) or F(h(π))) is strictly negative. So I(B) < 0. ∎

**What it adds.**
- Pointwise A ≤ 0 is not needed. In 𝒰₀, A can be large and positive (E2: A up to +56), and Ξ is still negative.
- This answers the R14-1 referee's scope caveat (`ref_R14-1/REFEREE_VERDICT.md:13`) on a class much larger than S/G.

**Checked (`ibcheck.out`).** I(B) by the A-form and the IBP form agree, and I(B) ≤ the piecewise bound 2Σ[F(h_hi) − F(h_lo)] at B = 1e-4 … 10:
- S(1.4): −0.81 ≤ −0.74 at B = 1e-4;
- G(1.4): −0.149 ≤ −0.075;
- G_w*: −0.693 ≤ −0.327;
- E2: −0.776 ≤ −0.259.

All are negative. All 𝒰₀ laws in this report have Ξ < 0 for all four vertices.

### 3.4 Outside 𝒰₀: explicit subluminal laws with Ξ ≥ 0 (checked; the IVT step proved)

- **Search** (`xiopt.py`). σ′ on [b, π] is a Gevrey-blended interpolation of 8 node values in [−1, 1], last node 0. So |σ′| ≤ 1 by construction: in 𝒮. Each Ξ_v at m = 0.1 was maximized by random search plus Nelder–Mead.
- **Witnesses** (exact ±1 nodes; `wit_b.out`):
  - **W08:** b = 0.8, nodes (−1, 1, 1, −1, −1, 1, 1, −1). max|σ′| = 1.000000. Edge local minima of g: 0.498 (k = 1.19 and 2.23), and 0.865 at π.
  - **W14:** b = 1.4, nodes (−1, 1, −1, −1, −1, 1, 1, −1). Edge minima 1.769, 0.889 (k = 2.46), and 1.232 at π.
  - The deepest valleys sit below the face value b² (W08: 0.498 < 0.64; W14: 0.889 < 1.96). All are gapped at O(1)/a: no light doublers.

| law | m | v_max (d = 3) | Ξ_{M,Eg} | Ξ_{U,Eg} | Ξ_{M,T2g} | Ξ_{U,T2g} |
|---|---|---|---|---|---|---|
| W08 | 1.0 | 0.8829 | −1.646e-4 | −1.63e-4 | −1.04e-3 | −5.85e-4 |
| W08 | 0.3 | 0.9874 | **+2.393e-5** | −2.58e-5 | −9.91e-4 | −5.19e-4 |
| W08 | 0.1 | 0.9986 | **+9.948e-5** | **+3.27e-5** | −8.92e-4 | −4.50e-4 |
| W08 | 0.01 | 0.99999 | **+1.106e-4** | **+4.14e-5** | −8.77e-4 | −4.40e-4 |
| W14 | 0.3 | 0.9926 | **+6.10e-6** | −1.83e-5 | −7.98e-4 | −4.67e-4 |
| W14 | 0.1 | 0.9992 | **+4.17e-5** | **+1.05e-5** | −7.65e-4 | −4.39e-4 |
| W14 | 0.01 | 0.99999 | **+4.66e-5** | **+1.45e-5** | −7.60e-4 | −4.35e-4 |

- **Independent 3D grid**, m = 0.3, N = 160/240/320:
  - W08 Ξ_{M,Eg}: A-form +2.32e-5/+2.39e-5/+2.37e-5; IBP +2.40e-5/+2.39e-5/+2.39e-5.
  - W14: A-form +5.9e-6/+9.0e-6/+6.4e-6; IBP +6.8e-6/+6.2e-6/+6.1e-6.
  - The Laplace values at two resolutions agree to 7 digits.
- **Mechanism (checked, `ibcheck.out`).** I(B) > 0 at small B: W08 +18.0 at B = 1e-4, +0.136 at B = 1. It is negative only for B ≳ 3. The bound sits above it (+24.1, +0.51), so the valleys' −2F(V) terms are what Theorem B forbids.
- **A law with Ξ_{M,Eg} = 0 exactly** (proved from the checked endpoint signs). The convex interpolation σ′_t = (1 − t)σ′_{G(0.8)} + tσ′_{W08} stays in 𝒮 (σ′(π) = 0 at both ends) and moves Ξ_{M,Eg} continuously from < 0 (G(0.8) ∈ 𝒰₀) to > 0. The intermediate-value theorem then gives a law with Ξ_{M,Eg} = 0, at any fixed light m. This is a tuning.
- **Not found (suggested only).**
  - Ξ_{T2g} ≥ 0 for either vertex: best −8.4e-4 (M) and −1.9e-4 (U) over both searches.
  - Any Ξ ≥ 0 when the valleys are required to stay above the face value (σ ≥ b on the edge, i.e. every edge state above R8-2's ceiling √(m² + b²); `xiopt_face.out`). Best: M,Eg −2.07e-4, U,Eg −1.15e-4, M,T2g −8.0e-4 at b = 1.0 and 1.4.
  - So positivity was found only with valleys below the box-face energy. A theorem for the face-gapped class is open.

### 3.5 Mass-dependent subluminality does not rescue the literal edge (checked, `scan1.out`)

- R9-2's literal L edge (b = 2, b₂ = 3.1) stays superluminal up to at least m = 6 lattice units: v_max (d = 3) = 3.67, 2.95, 2.39, 1.98, 1.45 at m = 1, 2, 3, 4, 6.
- μ_E < 0 throughout, and its Ξ changes sign between m = 3 and 4.
- So no "heavy enough to be subluminal" escape exists at any physical (sub-Planckian) mass.

---

## 4. Against the FIXED readings (`TESTS:4841-4844`)

**REFUTED (worker reading; referee required).** The item's (a) and (b) are both false in the stated class 𝒮 (subluminal one-band laws, even or odd; all witnesses gapped at O(1)/a). The witnesses are explicit and checked:
- **μ_E = 0:** G_{w*}(1.4), with w* = 0.344371 (m = 0.01), 0.349416 (m = 0.3), 0.389586 (m = 1). Members of R14-1's own G-type family (0 ≤ σ′ ≤ 1, A ≤ 0); |μ_E| ≤ 6e-14 (Laplace), ≤ 1e-10 (3D grid). Strictly negative μ_E: G_w(1.4) at w ≤ 0.2; E1; E2.
- **Ξ ≥ 0:** W08 and W14, with Ξ_{M,Eg} > 0 and Ξ_{U,Eg} > 0 at light mass. Ξ_{M,Eg} = 0 on the interpolating family.

**DERIVED is not available.** (a) fails even inside 𝒰₀ and even with A ≤ 0 pointwise.

**Additional proved result (unrefereed): Theorem B.** (b) holds on 𝒰₀, the subluminal laws with no gapped edge valley: Ξ < 0 for every vertex in 𝒱, at every m.

## 5. What it means for the item's dilemma (`TESTS:4838`) (reading)

- **Shear sector.** Lattice-scale causality and shear cancellation are compatible. The cancellation is still a tuning: one edge-shape parameter, here the drop width w, shared by all light species with that edge up to O((ma)²). It applies only to the supplied zero-point vacuum. In the empty Fock vacuum there is nothing to cancel.
- **Graviton-cone sector.**
  - For every edge without a gapped valley, Ξ < 0 is forced for every vertex (Theorem B). No edge-shape tuning inside 𝒰₀ can zero it.
  - Zeroing Ξ_{E_g} needs valley structure below the box-face energy (extra heavy band pockets at 0.7–0.94/a) plus a tuning. Ξ_{T_2g} was not brought to zero.
  - So the graviton sector costs birefringence or two tunings. Matter's own graviton-loop speed shift (R11-1(b)) is a separate, uncomputed item here.
- **Revised dilemma.** The choice is not "causality at the lattice scale versus tuning". It is tuning (shear) and "tuning plus heavy edge-valley structure, or an unremovable Ξ < 0" (graviton). A superluminal edge buys nothing that a subluminal one cannot.

## 6. Prices (named, not adopted)

- **P-W*: edge-shape tuning for the conditional shear.** The edge dispersion beyond the box is downstream dynamics content: Admissibility does not choose a Hamiltonian or transfer operator (`AX:116-123`). Choosing w = w* is a tuning, not an axiom change. Its m-dependence is O((ma)²).
- **P-V: heavy edge valleys to reach Ξ_{E_g} ≥ 0.** These are extra band minima at O(1)/a below the box-face energy, plus a tuning. Their effect on R8-2's Theorem E edge fall and on R14-1's restriction lemma: the box states are untouched, and only the edge spectrum changes (suggested).
- **Inherited.**
  - The supplied zero-point or sea vacuum (`AX:184-187`, source/action and persistence open).
  - R9-9's assumed Ward completion of the pair stress.
  - R14-1's box-route prices.
- **No axiom text changes.**

## 7. Strong-word check

- **"Proved"** is used for:
  - (R1), (R2);
  - Theorem B;
  - the 𝒮 characterization;
  - analyticity of μ_E(m) in m²;
  - the intermediate-value existence of μ_E = 0 and Ξ_{M,Eg} = 0 laws, given the checked endpoint signs.
- **"Checked"** is used for every number. Methods: Laplace-separable evaluation at 1D n = 2^13–2^18, cross-checked with the direct 3D zone grid (N up to 560) in both forms; and v_max by exact separable bisection on 2·10⁵ 1D points.
- **"Exactly zero"** is never claimed numerically. The roots are |μ_E| ≤ 6e-14 (Laplace) and ≤ 1e-10 (grid).
- **"Every"** is used only inside Theorem B's hypotheses.
- **Not claimed:**
  - a theorem for face-gapped valleys;
  - Ξ_{T2g} ≥ 0;
  - anything about the dressed graviton–matter split;
  - anything in the empty Fock vacuum, where μ_E ≡ 0 and Ξ ≡ 0 (`C5_R9-9_report.md:108`);
  - certified interval bounds.

## 8. For the referee

1. **(R1).** The by-parts identity, and that it equals R9-2's refereed closed form. Check numerically with `lapcheck.out` and `verify_a.out`; G(1.4) and S(1.4) reproduce R14-1.
2. **The G_w(1.4) root.** Is G_w in R14-1's refereed subluminal G-form class (0 ≤ h′ ≤ 1, `ref_R14-1/REFEREE_VERDICT.md` §4)? Do the w* values and the 3D-grid sign changes at w = 0.25 and 0.35 reproduce?
3. **Theorem B.** The pointwise inequality in step 2 (uses 0 ≤ |h′| ≤ 1); the AC change of variables for h = |σ| across zeros; and the unimodality decomposition, including the arc through π.
4. **W08/W14.** |σ′| ≤ 1; the existence of gapped valleys; Ξ_{M,Eg} > 0 at m ≤ 0.3, on the 3D grid.
5. **Analyticity.** The exponential decay of the kurtosis defect.

## 9. Files (all in `S/scripts/`)

- `prof.py`: laws, 3D-grid μ_E and Ξ, v_max.
- `lap.py`: the Laplace-separable evaluator.
- `calib.{py,out}`, `lapcheck.{py,out}`: calibration.
- `scan1.{py,out}`: literal edge at heavy m; first valleys and terraces.
- `terr14.{py,out}`, `terr14b.{py,out}`: terrace searches.
- `root.{py,out}`: E1, E2 and the Mix root.
- `root_w.{py,out}`: the G_w root.
- `verify_a.{py,out}`: 3D grid for (a); the G_w table.
- `resid.{py,out}`, `resid2.{py,out}`: the m² law.
- `concave.{py,out}`: random concave edges. μ_E < 0 occurs for b ≤ 1.0, consistent with the G_w table.
- `wit_b.{py,out}`: the (b) witnesses.
- `xiopt.{py,out}`, `xiopt_face.{py,out}`: searches.
- `ibcheck.{py,out}`: Theorem B bound.
- `tails.{py,out}`: kernel tails.
