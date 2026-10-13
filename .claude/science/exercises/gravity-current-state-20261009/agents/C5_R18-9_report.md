# C5 R18-9 report: can all four cone/shear rows (Ξ_Eg, Ξ_T2g, μ_E, μ_T2) be zeroed with SM content under conserved vertices?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 03:00Z to about 03:45Z. No repository file was edited. No downloads, no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R18-9/`. My scripts and `.out` files are in `S/scripts/`. `S/arch18/` holds unmodified copies of `P/scripts/C5/R18-5/*`; `S/arch13/` of `P/scripts/C5/R17-13/*`; `S/arch17_4/` of `P/scripts/C5/R17-4/{offaxis,zz}.py`.
- Every run used `OMP_NUM_THREADS=2` and ran under 10 minutes (longest 526 s, `solve4k_N192.out`). Machine load was 4–16 from other jobs. I stopped three of my own background jobs early to keep my share at or below 6 threads (`photres.out`, `photres2_N160_{A,B}.out` are partial as a result).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`:
  - the C5 method and readings (`:2302-2319`);
  - the round-17 head rules (`:5688-5706`) and the round-18 head rules (`:6395-6406`);
  - R17-4 (`:5816-5845`, worker line `:5940-5946`, verdict `:6171-6178`);
  - R17-9 (`:6110-6128`, worker line `:6267-6282`, verdict `:6582-6586`);
  - R17-12 and R17-13 (`:6339-6383`, worker lines `:6601-6611`, `:6654-6663`, verdicts `:6795-6809`);
  - R18-5 (`:6631-6653`, worker line `:6779-6789`);
  - my item, `:6847-6869`.
- `P/agents/`: `C5_R18-5_report.md` (all); `C5_R17-13_report.md` (all of §§0–4) and `C5_R17-13_referee_verdict.md` (`vR17-13`); `C5_R17-4_report.md` (§0, §3.1 hits for face1/K₆).
- R18-5's referee verdict appeared before I started: `scratchpad/C5/ref_R18-5/REFEREE_VERDICT.md` (`vR18-5`), **CONFIRMED WITH CORRECTIONS**. It reproduces the root (`vR18-5:9-14`) and rules signed VW stencils in setting (`vR18-5:16-20`). Its item 3 adds that "the μ rows are vertex-independent only under stipulated SF" (`vR18-5:7`).

**Runners rechecked before use (checked).**
- `S/arch18/final_check.py`, run unmodified on R18-5's archived `smroot_C160.npy`, reproduces R18-5's `final_check.out` line for line (`diff` of the first 12 lines is empty; `scripts/recheck_final_check.out`). The totals are (+1.564e-6, +3.929e-6, +1.638e-8), with μ_T2 = +9.1104e-2.
- My `lib9.phot_quad` gives the photon Ξ as an exact quadratic in the stencil weight a. At R18-5's root it equals the direct evaluation to all printed digits (`timing.out`: T 1.613352e-3, E 2.001771e-3 at N = 48, both ways).
- On the μ_T2 = 0 curve, my V0 numbers equal R17-13's `curve2.out` (b = 0.15: r* = 0.317785, V0 T +3.9001e-4, E −4.5210e-3, μ_E −7.1912e-3; `diraccurve_m0.01.out:5`).
- R17-4's archived off-axis evaluator, applied to my root's scalar edge, returns the same axis rows as my scalar path (−6.226970e-4, −3.590288e-4; `scal_offaxis_N160.out`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Yes: an explicit SM-count root with all four rows zero exists in the stated families (checked).** The FIXED reading FOUR-ROW-ZERO is met on its letter.
   - **Content.**
     - 4 real scalars on one Higgs edge G_w(b_s, w = π − b_s), U vertex;
     - 22.5 Dirac fields on one D1(b_f, r) edge, UD vertex;
     - 12 vectors on one photon edge γG_w(2.9435, 0.198093) (R14-1's G(b) photon: linear over 94% of the zone), VWa vertex with a signed stencil;
     - common matter mass m = 0.01.
   - **The root at photon grid N = 224** (`solve4k_N224.out`):
     - (b_s, b_f, r, a) = (2.526151, 0.909103, 0.555604, −0.176095);
     - all four totals are ≤ 7e-11, against per-species contributions of up to 0.38;
     - r < 1/√3, so every edge is subluminal.
   - **It persists under resolution changes** (§3.5):
     - the knobs converge across photon N = 160 / 192 / 224;
     - a second photon edge gives an independent root;
     - so does m = 0.001, with the knobs retuned.
2. **Knob count: 4 tunings, plus one window condition on the photon edge (checked).**
   - The four declared knobs are tuned: scalar b_s, Dirac b_f, Dirac r and stencil a. det J = −3.2e-4 and σ_min = 6.2e-4 (transversal).
   - The photon edge is not tuned, but it must be moved. R18-5's photon edge γG_w(1.27, 0.26) cannot carry the four rows: with it, the μ_E row is short by at least 0.088 (§3.3).
   - The edge must sit in a window b_γ ≈ 2.936–2.947 (fw = 1, G_w scalars). That is an open condition, not an equality, but it is narrow: about 5% of the photon's turn width.
   - So the honest count is **4 tunings plus 1 constrained law datum** (the pre-registered "5 if needed", used as a window).
3. **Why it works (proved structure; checked numbers).**
   - **μ_T2 is a Dirac-only row (proved).** Under SF, μ_T2 = −½⟨H_xy p_x p_y/E⟩ with H = Hess(E²/2). Scalars and photons on separable edges have H_xy ≡ 0. So the Dirac edge must sit on R17-13's zero curve r*(b_f).
   - **μ_E is vertex-independent under SF** (`vR18-5:7`). So the expectation's mechanism ("UD's smaller Dirac μ_E pull") does not exist.
   - **The budget is large.** On the zero curve, 22.5 Dirac fields put μ_E at −0.144 to −0.40. Scalars give at most +0.064.
   - **What the stencil buys.** Under VW the signed stencil decouples a photon's Ξ from its μ_E. Large-box photons have μ_E^γ ≈ +0.0285 per vector. Their Ξ is about +0.2 at a = 0, but one stencil value (a ≈ −0.175) nearly zeroes both photon Ξ rows at once: a_T = −0.17306 and a_E = −0.17598.
   - **The binding condition.** It is the a-blind combination X = Ξ_Eg − ρΞ_T2g (ρ = E₁/T₁). It needs the small photon mismatch E₁(a_T − a_E) ≈ +3.3e-3 per vector to cancel the Dirac birefringence. That happens only for b_γ ≳ 2.93.
   - **Where the sampled conflict sits.** On the N = 48 map with b_γ ≤ 2.8, X stays negative wherever the μ_E row is solvable (−0.063 to −0.016; no sign change in 96 pairs). That region includes R18-5's photon edge (§3.4).
4. **What stays unpaid.**
   - **(c) Off-axis rows.**
     - For the scalars, face2 ≡ T₂g holds (R17-4's identity, re-checked to 5.6e-13).
     - **For UD Dirac fields it does not (checked, m = 0.3 and 0.1):** face2 − T₂g = −6.7e-5 and +7.2e-5 per field. So the off-axis rows are further conditions at the root, of order 22.5 × 7e-5 ≈ 1.6e-3.
     - The VW off-axis rows were not computed: the off-axis vertex extension is itself a law datum.
   - **Also unpaid:** the tadpole (P-Tad/P-vac′) and the CC.
   - **Stipulated, as before:** SF, the 𝔇 restriction behind UD, the signed stencil and O(q) conservation only.
5. **Expectation (`TESTS:6869`).**
   - "FOUR-ROW-ZERO with 4 knobs": met, with the photon-edge window added.
   - "UD's smaller Dirac μ_E pull plus the signed stencil should relax R17-13's budget shortfall": the outcome is right, the mechanism is wrong. μ_E does not depend on the vertex (SF). What relaxed the shortfall is the stencil decoupling photon Ξ from photon μ_E, which admits the large-box photons that R17-13 had to reject under VM (`C5_R17-13_report.md:241`).

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Setting (`TESTS:6852-6856`).**
- **Content (SM counts 4 + 22.5 + 12).**
  - **Scalars.** Real scalars, U vertex, on one Higgs edge G_w(b_s, w) in R14-3's family (`arch18/content4.py:7-11`). I use fr = w/(π − b_s) = 1 in the solves; the window scan also uses fr = 0.02.
  - **Dirac.** 4-component Wilson-Dirac D1(b_f, r) (R14-1; `arch18/content3.py`). UD vertex, with the midpoint prescription (R18-5 §1, P-R18-5c).
  - **Vectors.** VWa (R17-12), placed on one photon edge γG_w(b_γ, w_γ) with d′ ∈ [0, 1] (`arch18/photon.py:39`).
    - The stencil is P = (1 − a)cos(s/2) + a·cos(3s/2), with λ = ¼ + 2a (`arch18/r1712_lib.py:50-53`). Note that the code's argument `lam` is the weight a.
    - The photon μ_E is 2 × the scalar formula with a mass regulator of 1e-3, the R17-9/R17-12/R18-5 convention (`arch18/smud_lib.py:29`).
- **Physics.**
  - One loop, axial q.
  - Supplied zero-point vacuum or filled sea; ultralocal seagull.
  - SF strain flow for every shear row (stipulated, P-R16-13a).
- **Masses.** m = 0.01 (main) and m = 0.001.
- **Knobs (declared before running).**
  - The four pre-registered knobs: scalar edge (b_s at fixed fr), Dirac b_f, Dirac r, stencil a.
  - The photon edge (b_γ at fw = 1) is the pre-registered fifth, "if needed".
  - Bounds: |a| ≤ 1, r ≤ 1/√3, b_γ < π.
- **Excluded (`TESTS:6856`):** VU, VM, V0 (except as a comparison column), the M vertex, pairing, superluminal edges.

**Families stated before results.**
- Scalar: G_w only.
- Dirac: D1 only (not DG, and not two Dirac edges).
- Photon: γG_w only, and one photon edge for all 12 vectors.
- Stencil: two-offset VWa.

**Hypotheses carried, not derived.**
- **W1 at O(q) only.** No vertex has an exact W1 completion (`vR18-5:20`; `vR17-12`, `TESTS:6799-6801`).
- **The 𝔇 restriction that makes UD unique** (P-R18-5b; `vR18-5:7`).
- **SF.**
- **Signed stencils.** In setting per `vR18-5:16`.

**Round-18 head rules.**
- **Locality of vertices (`TESTS:6403`).**
  - U has Lemma M's zero (`vR17-4:7`).
  - UD is spinor-covariant without that zero, which is allowed for spin-½ legs (Lemma M′, confirmed `vR18-5:5`).
  - VW: the per-leg factor c = d′ vanishes at the zone face for γG_w (d′(π) = 0, `d'` range in `verify_root_N160.out`), so its face amplitude vanishes whatever the stencil (suggested; the face test itself is R17-12's).
- **Whole-zone v_max for every edge**, including the gauge field: §3.5.
- **Counterterm basis:** per edge (one Higgs edge, one Dirac edge, one photon edge, one stencil).
- **Certificates.** Any CONFLICT claimed from a relaxation must state its enclosure first (`TESTS:6406`). No CONFLICT is claimed here; the §3.4 sign map is a sampled map, not a certificate.

## 2. Prior art (each counted once)

- **R18-5 + vR18-5.**
  - The 3-row root (U + UD + VWa, a = −0.1227), with μ_T2 = +0.091 unpaid (`C5_R18-5_report.md:60-75`).
  - μ_E and μ_T2 are vertex-independent under SF (`:59`; `vR18-5:7`).
  - Signed stencils are in setting (`vR18-5:16-20`).
  - Its photon edge γG_w(1.271, 0.260) is the one §3.3 excludes for four rows.
- **R17-13 + vR17-13.**
  - Form P: μ_T2^F = (N_c/2)⟨q_xq_y/E⟩ (`C5_R17-13_report.md:131-133`).
  - The zero curve r*(b) (`:225-228`), which ends at r = 1/√3, b ≈ 0.949.
  - The VM-era μ_E budget shortfall of 2.5–6×. Its stated cause: photons with μ_E^γ ≳ 5e-3 had Ξ_γ,T2g ≳ +0.02 (`:232-243`, `:241`). Not enclosed (`vR17-13:15`).
  - μ_T2 vertex-independent (`vR17-13:11`).
- **R17-12 + verdict.** VW; Lemma I (O(q²) stencils are free law data); W1 at necessary order only (`TESTS:6795-6801`).
- **R17-4 + verdict.**
  - U identities: face2 ≡ T₂g, and face1 = (3E_g + T₂g)/4 − ⟨K₆/ε⁷⟩/128 (`C5_R17-4_report.md:20`; `TESTS:5943`).
  - Off-axis rows depend on the vertex extension (P-TTV₂).
  - The LV tadpole is separately payable (`TESTS:6171-6178`).
- **R16-9 and R14-3.** The μ_E row and its sign structure, used only through R17-13's budget.
- **Grep.** I searched `P/agents/*.md` and `TESTS.md` for "a-blind", "photon box near π", "b_γ ≈ 2.9", "face2" with Dirac, and "four-row". Hits: R17-13's VM photon grid (`photgrid.out`, which reaches b_γ = 2.8 under VM), R18-5's signed-stencil root, and R17-4's scalar identities. There is no prior UD off-axis value and no large-box-photon four-row search.

---

## 3. Results

### 3.1 Structure (proved)

**(S1) μ_T2 is carried by the Dirac sea alone.**
- Under SF, μ_T2 = −½⟨H_xy p_xp_y/E⟩ per mode, with H = Hess(E²/2) (`C5_R17-13_report.md:80`).
- For any separable band, E² = Σ_j g(k_j) + const, so H_xy ≡ 0. That covers the G_w scalars and the γG_w photons (ω² = Σ d(k_j)²).
- So total μ_T2 = 22.5 μ_T2^F(b_f, r), and the four-row problem needs the Dirac edge on R17-13's zero curve. The archived code returns 0 for scalars and photons by construction (`arch18/smud_lib.py:29`, `content4.py:11`); (S1) is the reason that is correct. ∎

**(S2) The photon Ξ is an exact quadratic in a.** The VWa vertex is affine in a (`r1712_lib.py:53`). The pair weight Σ_pol|amp|² is therefore quadratic in a, and Ξ is linear in the pair weight. Three evaluations (a = 0, ±1) fix it. Checked against a direct evaluation (`timing.out`). The quadratic coefficient is a grid artefact that falls with N: −1.5e-6 at N = 160, −3.9e-7 at N = 224, against linear coefficients of about 1.15. ∎

**(S3) The a-blind row.** Write the photon rows as T(a) ≈ T₀ + T₁a and E(a) ≈ E₀ + E₁a, and set ρ = E₁/T₁. Then the combination

  X := Σ_species (Ξ_Eg − ρΞ_T2g) = 4(S_E − ρS_T) + 22.5(F_E − ρF_T) + 12·x_γ,  with x_γ = E₀ − ρT₀ = E₁(a_T − a_E), a_T = −T₀/T₁, a_E = −E₀/E₁,

does not depend on a, up to the O(a²) grid artefact. Rows (Ξ_T2g, Ξ_Eg, μ_E, μ_T2) = 0 are equivalent to (Ξ_T2g = 0 solved by a; X = 0; μ_E = 0; Dirac on the zero curve). ∎

### 3.2 The ingredients (checked)

**Dirac rows on the μ_T2 = 0 curve under UD**, per field, m = 0.01 (`diraccurve_m0.01.out`, `diraccurve2_m0.01.out`):

| b_f | r* | Ξ_T2g | Ξ_Eg | μ_E | ×22.5 μ_E |
|---|---|---|---|---|---|
| 0.06 | 0.3002 | −1.039e-3 | −2.141e-3 | −6.421e-3 | −0.1445 |
| 0.30 | 0.3501 | −4.56e-4 | −1.776e-3 | −8.643e-3 | −0.1945 |
| 0.60 | 0.4306 | +5.51e-4 | −1.038e-3 | −1.2247e-2 | −0.2755 |
| 0.90 | 0.5509 | +1.936e-3 | +9.1e-5 | −1.6931e-2 | −0.3809 |
| 0.9489 (end, r = 1/√3) | 0.5774 | +2.203e-3 | +3.18e-4 | −1.7811e-2 | −0.4008 |

UD lowers Ξ_T2g relative to V0 along the whole curve; V0 is shown in the `.out` files. The curve at m = 0.001 is within 1% of these values (`diraccurve_m0.001.out`). There it ends below b_f = 0.94.

**Scalars** (G_w, U, 128 laws; `scalscan_m0.01.out`):
- μ_E^s ∈ [−5.8e-4, +1.606e-2] (max at b_s → π);
- Ξ_T2g ∈ [−7.1e-4, −4.8e-5];
- Ξ_Eg ∈ [−4.1e-4, −1.3e-4].

So the scalar part of X, 4(S_E − ρS_T), is at most about +2.4e-3.

**Photons** (γG_w, VWa, 50 edges at N = 48, `photscan_N48.out`; resolution rows in `photres.out` and `photres2_N160_*.out`):
- μ_E^γ grows with the box. It is ≤ +3e-3 for b_γ ≤ 1.0 and reaches +0.0258 at (2.8, fw = 1).
- x_γ is negative (−1.5e-3 to −3.6e-3) for every edge with μ_E^γ ≥ +7e-3 and b_γ ≤ 2.4. It turns positive only at b_γ ≳ 2.6.

| edge (fw = 1) | N | μ_E^γ | ρ | x_γ | a_T |
|---|---|---|---|---|---|
| b_γ = 2.6 | 48 / 96 / 128 | +2.2418e-2 | 1.0447 | +3.543e-4 / +3.489e-4 / +3.486e-4 | −0.1705 |
| 2.8 | 48 / 96 / 128 | +2.5823e-2 | 0.9985 | +1.865e-3 / +1.923e-3 / +1.924e-3 | −0.1720 |
| 2.9 | 96 / 128 / 160 | +2.7672e-2 | 0.9758 | +2.828e-3 / +2.835e-3 / +2.838e-3 | −0.1727 |
| 2.95 | 160 | +2.8636e-2 | 0.9645 | +3.328e-3 | −0.1731 |
| 3.0 | 96 / 160 | +2.9625e-2 | 0.953 | +3.875e-3 / +3.842e-3 | −0.1735 |

### 3.3 R18-5's photon edge cannot carry the fourth row (checked bound from sampled maxima)

With the photon fixed at R18-5's γG_w(1.271203, 0.259986), μ_E^γ = −6.452e-4 per vector. The most favourable sampled μ_E total is then

  4 × max μ_E^s + 12 μ_E^γ + 22.5 × max_curve μ_E^F = 4(0.016055) − 0.007742 − 0.14448 = **−0.088**.

The last term is at b_f = 0.06, and |μ_E^F| shrinks only slowly toward b_f → 0 (−6.42e-3 → about −5.9e-3 by extrapolation). So with R18-5's photon edge the four declared knobs cannot reach μ_E = 0 in these families. This is a sampled-maxima bound, not an enclosure. **The photon edge must move (the pre-registered fifth knob).**

### 3.4 Where the four rows conflict and where they do not (checked map; sampled)

**`feas.py` on the N = 48 photon grid** (50 edges × 15 Dirac curve points × 128 scalars):
- For each (photon edge, Dirac point) I locate the scalar μ_E level set (linear interpolation in fr) and solve the T₂g row for a.
- Result (`feas_N48.out`): 96 pairs have a solvable μ_E row. **On all of them the E_g residual is negative**, in [−0.063, −0.0156], with no sign change.
- The best pair is (2.8, fw 1) with b_f = 0.7.
- Of the remaining pairs, 526 are too negative in μ_E and 128 too positive.

**Reading.** For b_γ ≤ 2.8 the a-blind row X cannot be met where μ_E is. The photons with enough μ_E have too little x_γ. That region contains R18-5's edge and every photon R17-13 tried under VM.

**The corner.**
- x_γ keeps rising past b_γ = 2.8, and ρ falls toward 1. At b_f ≈ 0.9 the Dirac part of X is ≈ −0.040, and 12x_γ reaches that at b_γ ≈ 2.94 (table above).
- A model solve interpolating the N = 160 photon nodes (`model_solve_lin*.out`, `window_model.out`) locates the roots and the window (§3.6).
- The roots are then computed directly, with no interpolation (§3.5).

### 3.5 The root (checked)

**Main root (photon edge fixed at γG_w(2.9435, 0.198093), fw = 1).** Newton in the four declared knobs at fixed photon coefficients computed at each N (`solve4k.py`):

| photon N | b_s (fr = 1) | b_f | r | a | max |rows| | det J |
|---|---|---|---|---|---|---|
| 160 | 2.4904779 | 0.9063782 | 0.5541794 | −0.1760721 | 2.2e-10 | −3.151e-4 |
| 192 | 2.5167202 | 0.9083781 | 0.5552240 | −0.1760887 | 9.2e-11 | −3.191e-4 |
| 224 | 2.5261508 | 0.9091030 | 0.5556037 | −0.1760950 | 6.8e-11 | −3.205e-4 |

- **Convergence.** Knob differences are 0.026 then 0.0094 in b_s, and 2.0e-3 then 7.2e-4 in b_f. They fall by about ⅓ per step (geometric). A geometric extrapolation gives b_s ≈ 2.531 and r ≈ 0.5558, still interior.
- **Fixed-knob drift.** The photon-grid drift at fixed knobs, N = 192 minus N = 160, is (+2.9e-6, +2.7e-5) in (T₂g, E_g) totals.

**Record at N = 224** (`solve4k_N224.out`), per species and total:

| species (count) | Ξ_T2g | Ξ_Eg | μ_E | μ_T2 |
|---|---|---|---|---|
| real scalar, U, G_w(2.526151, w = 0.615442) (×4) | −6.2776e-4 | −3.6216e-4 | +1.06276e-2 | 0 (S1) |
| Dirac, UD, D1(0.909103, 0.555604) (×22.5) | +1.98457e-3 | +1.3215e-4 | −1.70941e-2 | −4e-18 |
| vector, VWa a = −0.176095, γG_w(2.9435, 0.198093) (×12) | −3.51181e-3 | −1.2706e-4 | +2.85089e-2 | 0 (S1) |
| **contributions** | −0.00251 / +0.04465 / −0.04214 | −0.00145 / +0.00297 / −0.00152 | +0.0425 / −0.3846 / +0.3421 | — |
| **total** | **−1.6e-12** | **−1.3e-12** | **+2.6e-11** | **−9e-17** |

**Checks at the N = 160 root** (`verify_root_N160.out`, `jac_N160.out`, `photxcheck_N160.out`, `photmu_reg.out`):
- **μ_T2 by three evaluators.** At high resolution the Dirac μ_T2 per field is:
  - −4.405e-10 (archived dfam, GL(6,12));
  - −4.438e-10 / −4.437e-10 (R17-13's independent lib13, form P, at (8,16) and (12,24));
  - −1.32e-9 (form I).

  These cancel KK + KM + MM = −1.30e-5 − 7.283e-4 + 7.413e-4. The GL(4,10) solve value of 1e-18 is a quadrature floor. The high-resolution residual, ×22.5 ≈ −1e-8, is removed by Δr ≈ 1.6e-7 (∂μ_T2/∂r = +2.79e-3 per field).
- **Dirac rows at GL (3,8)/(4,10)/(5,12)/(6,16).** Stable to 6e-11 (T₂g), 3e-12 (E_g) and 7e-8 (μ_E) per field between (4,10) and (6,16). ×22.5 that is ≤ 1.5e-6.
- **Dirac UD vertex against a brute-force finite-q grid** (independent of the pointwise formula). At the root's Dirac law at m = 0.3, N = 160: T₂g +1.521097e-3 vs GL +1.521118e-3; E_g +8.1136e-5 vs +8.1159e-5 (`udface_validate.out`). The same grid reproduces R18-5's D1(1.4, 0.3) value (+4.320506e-3 at N = 96).
- **Scalar quadrature.** n = 2^16 against 2^14 changes the rows by ≤ 1e-13.
- **Photon q-extrapolation** (R17-12 uses shift pair (1, 2)). Pair (1, 3) changes the per-vector Ξ by 2.0e-6 / 1.9e-6. Pair (2, 4) changes them by 1.9e-5, consistent with an O(q⁶) remainder that is about 64× smaller at (1, 2).
- **Photon μ_E.** Regulator 1e-2 to 1e-4 and quadrature n = 2^14 to 2^16 change it by ≤ 3e-10.
- **Transversality in the declared knobs.**
  - J has singular values (19.3, 0.649, 0.0405, 6.2e-4) and det = −3.15e-4.
  - The small direction is the a-blind row X: a residual of 1e-5 in X moves b_s by about 0.01.
  - That explains the resolution drift of b_s. It also means **the declared knobs control X only weakly; the photon edge controls it strongly** (x_γ moves by about 1e-2 per unit b_γ, per vector).
- **Subluminality, whole zone** (`verify_root_N160.out`):
  - **Dirac:** r = 0.554 < 1/√3, so v_max ≤ 1 (Lemma V1, `C5_R16-13_report.md:176-179`). Sampled v_max = 0.999986.
  - **Photon:** d′ ∈ [0, 1], so |∇ω| ≤ 1. v_max = 1, attained in the box.
  - **Scalar:** v_max = 0.999997.
- **Stencil.** Weights 1.176095 at z ± ½ and −0.176095 at z ± 3/2. P(0) = 1. λ = ¼ + 2a = −0.1022 (signed; in setting per `vR18-5:16`). It is finite-range and symmetric (covariant).

**Second, independent root at a different photon edge** (`solve4k_W2_N160.out`). Photon γG_w(2.9378, 0.203793), N = 160:
- (b_s, b_f, r, a) = (1.533595, 0.846635, 0.524795, −0.175570);
- totals ≤ 1.6e-11; det J = −1.78e-4; r < 1/√3.

**m = 0.001** (`solve4c_m0.001_N192.out`; photon N = 192, same photon edge):
- (b_s, b_f, r, a) = (2.574221, 0.914047, 0.566593, −0.176162);
- totals ≤ 6e-11; det J = −3.49e-4; r = 0.5666 < 1/√3.

The root persists at the lighter mass with **separately tuned knobs**, as for R16-13's and R18-5's roots (`C5_R18-5_report.md:276-279`). One law serving both masses is not shown. By R17-13's m-transfer reading, a law tuned at m → 0 leaves O(m) residuals (`C5_R17-13_report.md:230`).

### 3.6 The photon-edge window (suggested from the model; two points checked directly)

The model interpolates (T₀, T₁, E₀, E₁) through N = 160 photon nodes b_γ ∈ {2.9, 2.95, 3.0} at fw = 1. It then solves (b_γ, b_f, r, a) for 12 fixed G_w scalars (`window_model.out`):
- Roots with r ≤ 1/√3 exist for b_γ* ∈ [2.9361, 2.9469] (scalar b_s from 1.0 to 2.9 at fr = 1, and fr = 0.02 at b_s = 0.5, 1.0).
- Scalars with b_s ≥ 3.0 push r past 1/√3. That is the subluminality wall at the end of R17-13's curve.
- Two points of the window were confirmed directly, with no interpolation: b_γ = 2.9435 and 2.9378 (§3.5).

**Reading.**
- With G_w scalars the photon must be nearly linear: box ≈ 93.5–93.8% of the half-zone, turn width w = π − b_γ ∈ [0.195, 0.206].
- That is an open window, so it is not a tuning in the counting convention. But its width is about 5% of w.
- Wider scalar families, or fw < 1, may widen it. Not tested.

### 3.7 (c) Off-axis rows at the root (partial; checked where stated)

- **Scalars (R17-4's archived evaluator, E1, U)** (`scal_offaxis_N160.out`). Per real scalar at the N = 160 root:
  - face2 − T₂g = 5.6e-13, so R17-4's identity holds;
  - the O_h relation residual is 8e-19;
  - the K₆ term −⟨K₆/ε⁷⟩/128 = −2.88e-5;
  - so 4 scalars contribute face1 = −1.81e-3.
- **UD Dirac (new brute-force evaluator for any q direction, `udface.py`, validated in §3.5)** (`udface_offaxis.out`). The C₄ control (xz polarization with q ∥ y) equals T₂g with q ∥ z exactly. **face2 ≠ T₂g for UD:**

  | law | m | N | T₂g | face2 | face2 − T₂g | face1 − (3E_g + T₂g)/4 |
  |---|---|---|---|---|---|---|
  | root D1(0.906378, 0.554179) | 0.3 | 96 / 128 / 160 | +1.52110e-3 | +1.45388e-3 | −6.79e-5 / −6.73e-5 / −6.72e-5 | +1.654e-4 |
  | root D1 | 0.1 | 128 / 160 / 192 | +1.83544e-3 | +1.90726e-3 | +7.06e-5 / +7.15e-5 / +7.18e-5 | +4.146e-4 |
  | D1(1.4, 0.3) | 0.3 | 128 / 160 | +4.3249e-3 | +4.2464e-3 | −8.4e-5 / −7.8e-5 | +5.17e-4 |

  So for Wilson-Dirac fields under UD (with the midpoint prescription extended to all q), the face2 row is **not** fixed by the axis rows (checked). The difference changes sign between m = 0.3 and m = 0.1. At m = 0.01 it was not computed: the brute grid does not resolve the light-mass region at N ≤ 192.
- **VW vectors: not computed.** R17-12's VW placement is defined for q ∥ z only. An off-axis extension is a further law datum (P-TTV₂ type, `TESTS:5944`), and I did not choose one.
- **Reading.**
  - At the root, the off-axis rows (face1, face2) are not shown to vanish.
  - The Dirac contribution alone to face2 − T₂g is of order 22.5 × 7e-5 ≈ 1.6e-3 at m = 0.1–0.3 (suggested to persist at light mass), against axis-row contributions of about 0.04.
  - They are further conditions, unpaid here, consistent with R17-4's count (+1 K₆-type row per vertex extension, more if face2 ≢ T₂g).

### 3.8 (d) Prices and the bill (named, not adopted)

- **Used, not new:**
  - P-R17-12b with signed weights (the VWa stencil, a ≈ −0.176);
  - P-R18-5b (the 𝔇 restriction fixing UD);
  - P-R18-5c (the midpoint prescription; also used off-axis in §3.7);
  - SF (P-R16-13a);
  - P-R17-13a (μ_T2 as a Dirac-shape row).
- **P-R18-9a (new, suggested): the photon window.**
  - Placing SM content on one cone with all four axis/shear rows zero needs the photon edge in a narrow near-linear window (γG_w with b_γ ≈ 2.936–2.947 at fw = 1, for G_w scalars).
  - It is a law datum with an open (non-equality) condition. It replaces R18-5's photon edge, which is excluded for four rows (§3.3).
  - Source/action gate `AX:187`; dynamics downstream `AX:114-130`.
- **P-R18-9b (new, suggested): the UD off-axis rows.**
  - face2 ≢ T₂g for UD Dirac fields (§3.7). So the off-axis TT rows are not inherited from the axis rows for fermions, and need their own payment.
  - Size per field: about 7e-5 at m = 0.1–0.3.
- **Bill (reading, conditional; per-edge counterterm basis).**
  - The axis cone (E_g, T₂g) plus both shear rows (μ_E, μ_T2) at SM counts: **4 rows, paid by 4 tunings** (scalar b_s, Dirac b_f, Dirac r, stencil a), plus the photon-edge window. No pairing and no non-shape shear knob is used.
  - This removes R18-5's unpaid μ_T2 and R17-13's P-R17-13b conflict price within these families.
  - Unpaid:
    - the off-axis rows (scalar K₆, Dirac face1/face2, vector off-axis);
    - the LV tadpole (P-Tad, or P-vac′ under (d-i));
    - the CC.
  - The total count against S23 is not recomputed here.
- **No axiom text changes.** No sizes at a = ℓ_P are quoted beyond the tuning-precision comparator implicit in the residuals.

---

## 4. Against the FIXED readings (`TESTS:6864-6867`)

**FOUR-ROW-ZERO: worker reading MET (checked), with the knob count and scope.**

| clause | status |
|---|---|
| explicit SM-count content | 4 real scalars + 22.5 Dirac + 12 vectors; edges and stencil stated in §3.5 |
| conserved vertices | U, UD and VWa pass the O(q) forward (Lemma F) test (R17-12, R18-5, vR18-5). **O(q) only:** no exact W1 completion exists for any of them (`vR18-5:20`) |
| covariant, local | U (Lemma M zero); UD (Lemma M′, `vR18-5:5`); VW (face zero via d′(π) = 0; suggested); signed stencil finite-range and symmetric |
| all subluminal | Dirac r < 1/√3 (Lemma V1); photon d′ ∈ [0, 1] (v_max = 1); scalar 0.999997 |
| four rows zero at a common light mass | m = 0.01: totals ≤ 7e-11 at photon N = 224, root converging in N; μ_T2 residual ≈ 1e-8 total at high-order Dirac quadrature, removable by Δr ~ 1e-7 (transversal) |
| knob count | **4 tunings** (scalar b_s, Dirac b_f, Dirac r, stencil a), plus the photon edge moved into an open window (the pre-registered 5th knob, used as a window, not an equality) |
| second mass | m = 0.001 with separately tuned knobs (photon N = 192) |

**FOUR-ROW-CONFLICT: not claimed.**
- The sampled N = 48 map shows the four rows do conflict for b_γ ≤ 2.8 in these families (§3.4), which covers R18-5's photon edge (§3.3).
- That is a sampled statement, without enclosure, and it is not class-wide: the large-box corner is feasible.

**Expectation (`TESTS:6869`).**
- "FOUR-ROW-ZERO with 4 knobs": met, with a photon-edge window.
- The stated mechanism is not the one that operates:
  - μ_E is vertex-independent under SF (`vR18-5:7`), so UD exerts no smaller μ_E pull;
  - the relief comes from the stencil decoupling photon Ξ from photon μ_E, which admits large-box photons.

**Removed hypothesis** (μ_T2 left unpaid). Paid by one Dirac-shape condition (r slaved to b_f), at the price of moving the photon edge to the window.

## 5. Strong-word check

- **"Proved"** is used only for:
  - (S1) μ_T2 = 0 for separable edges under SF;
  - (S2) Ξ exactly quadratic in a;
  - (S3) the a-blind row.

  Each takes one line from stated definitions.
- **"Checked"** means numerics here at stated resolutions. It covers the roots, the convergence in N, the three μ_T2 evaluators, the brute-force UD validation and the off-axis UD values.
- **"Root"** means Newton from a model-located start: transversal (σ_min 6.2e-4 in the declared knobs), and converging in the photon grid N.
  - It is not a claim about the whole solution set.
  - The declared-knob Jacobian is ill-conditioned in the X direction, so knob values carry a resolution uncertainty of about 0.005 in b_s and 3e-4 in b_f at N = 224.
- **"Window"** is model-interpolated, except at the two points solved directly.
- **"Conflict for b_γ ≤ 2.8"** is a sampled N = 48 map. It is not an enclosure and not a CONFLICT claim.
- **"Excluded" for R18-5's photon edge** is a bound from sampled maxima (scalar max 0.016055 on 128 laws; Dirac curve sampled from b_f = 0.06). It is not certified.
- **Not claimed:**
  - exact W1 completion;
  - SF derived;
  - off-axis closure;
  - VW off-axis values;
  - one law serving both masses;
  - DG Dirac, two Dirac edges, or non-G_w scalars;
  - uniqueness;
  - anything at two loops.

## 6. For the referee

1. **(S1)–(S3)**, especially that μ_T2 ≡ 0 for separable scalar and photon edges under SF. This is why the code's hard-coded 0 is correct.
2. **Reproduce the N = 224 root** from `root4k_N224.npy` with an independent photon evaluator at N ≥ 224. The X row is weakly controlled by the declared knobs (σ_min = 6.2e-4), so check the root's persistence rather than the knob digits.
3. **Whether the photon-edge window counts as a fifth tuning.** It is an open condition about 5% wide in the turn width, and it was needed because R18-5's edge fails (§3.3).
4. **The UD off-axis evaluator** (`udface.py`). It reproduces the axis values and the C₄ control. Its face2 ≠ T₂g result should be checked, including whether another off-axis extension of UD's placement changes it.
5. **The scope of "conserved"** (O(q) forward test only), as in `vR18-5:20`.

## 7. Files (`S/scripts/`)

- **Library:** `lib9.py`, which imports `S/arch18` unmodified.
- **Rechecks:** `recheck_final_check.out`, `timing.{py,out}`.
- **Ingredients:**
  - `diraccurve.{py}` → `diraccurve_m0.01.out`, `diraccurve_m0.001.out` (`.npy`);
  - `diraccurve2.py` → `diraccurve2_m0.01.out`;
  - `scalscan.py` → `scalscan_m0.01.{out,npy}`;
  - `photscan.py` → `photscan_N48.{out,npy}`;
  - `photres.py` → `photres.out` (partial);
  - `photres2.py` → `photres2_N160_{A,B}.out`, parsed by `parse_nodes.py` into `photres2_N160_parsed.npy`.
- **Map:** `feas.py` → `feas_N48.out`.
- **Model and window:** `model_solve.py` → `model_solve_lin.out`, `model_solve_lin_scan.out`; `window2.py` → `window_model.out`.
- **Roots:**
  - `solve4k.py` → `solve4k_N160.out`, `solve4k_N192.out`, `solve4k_N224.out`, `solve4k_W2_N160.out`;
  - `solve4c.py` → `solve4c_m0.001_N192.out`;
  - `root4k_*.npy`, `root4c_m001_N192.npy`.
- **Checks:**
  - `verify_root.py` → `verify_root_N160.out`;
  - `jac.py` → `jac_N160.out`;
  - `photxcheck.py` → `photxcheck_N160.out`;
  - `photmu_reg.py` → `photmu_reg.out`.
- **Off-axis:**
  - `scal_offaxis.py` → `scal_offaxis_N160.out` (R17-4's evaluator in `S/arch17_4`);
  - `udface.py` → `udface_validate.out`, `udface_offaxis.out`.
