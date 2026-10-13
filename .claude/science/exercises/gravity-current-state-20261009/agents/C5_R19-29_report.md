# C5 R19-29 report: face1's Schur completion. Does face1 still have to vanish once the A₁ gauge block is included?

**Author and provenance.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 07:10Z to about 07:55Z. I edited no repository file and downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `scratchpad/C5/R19-29/`. Scripts and `.out` files are in `S/scripts/`.
- Unmodified copies: `S/scripts/arch17_4/` (R17-4 `zz.py`, `offaxis.py`), `S/scripts/arch18/` (all of `P/scripts/C5/R18-5/`), `S/scripts/kernels.py` (R19-23), `S/scripts/root_refR18-9.npy` (R18-13's copy of vR18-9's retuned root). `S/scripts/vwface_copy.py` is R18-13's `vwface.py` with only its import path repointed.
- `OMP_NUM_THREADS=2`. Every run took under 75 s.

**Read.**
- `AX` in full.
- `P/TESTS.md`: R19-29 (`:8573-8593`); the referee records at about 07:08Z (`:8549-8571`, R19-23 at `:8559-8564`); R19-5's verdict (`:7747-7752`); R19-9's verdict (`:7862-7872`); R19-15 and R19-19 (`:8128-8137`); R19-26 (worker, `:8532-8545`).
- `P/agents/`: `C5_R18-13_report.md` and verdict, `C5_R19-12_report.md` and verdict, `C5_R19-23_report.md` and verdict, and `C5_R9-9_report.md` and verdict, all in full.
- Also: `C5_R19-5_report.md` (grep hits; P-R19-5a at `:276-279`), `C5_R13-5_report.md:143-160` (Lemma P1), and `C5_R17-4_report.md:28,197-200` (the P-Tad trace counterterm is linear).
- Scratch: `ref_R19-23/REFEREE_VERDICT.md` and `REFEREE_CHECKS.out`.

**Runners rechecked before use (checked).**
- **Scalar.** My A₁ library gives the scalar TT rows of the root's scalar edge. They converge to R17-4's archived evaluator (U, E1): at m = 0.3, N = 96, face1 is −4.5081e-4 against −4.5039e-4 and E_g is −3.5630e-4 against −3.5616e-4 (`rowcheck_m0.3.out`).
- **Dirac.** My Dirac block reproduces R18-13's `dface.py` face1 at D1(0.906378, 0.554179), m = 0.3: +6.0801e-4 at N = 48, against +6.0655e-4 (`dirac_m0.3_N48.out`; `P/scripts/C5/R18-13/dface_validate_m0.3.out:1`).
- **K_EH.** R19-23's K_EH annihilates my gauge directions to 2e-21, and its TT normalization is exact (`pole_m0.3_N40.out:5-7`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics run here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Of the two A₁ gauge directions, the time direction never mixes with face1 (proved; checked for all three species).**
   - With the time components that exact pair-channel conservation fixes, Π(face1, g₀) = 0 identically, at every ω and q. This is R13-5's Lemma P1, which is the completion R19-5 uses for U and UD.
   - The check gives |Π_{1g₀}| ≤ 1e-19 for U, UD and VWa-geo at the root data.
   - The longitudinal direction gₙ does mix: Π(face1, gₙ) = κs³ + O(s⁵). That mixing is generically nonzero, as the expectation said. At R18-13's solution κ_tot = −1.28, and photons supply 98% of it.
2. **That mixing reaches the face1 pole only at O(s⁴), provided the vacuum's degree-0 longitudinal (bulk) entry λ_nn is nonzero (proved; checked by exact pole roots).** The on-shell Schur term, at the leading orders, is
   - Schur/s² = κ²s² / (4λ_nn + (c₄ + 8X)s²) + higher order.
   - So when λ_nn ≠ 0, the face1 speed coefficient is the raw TT row, and R18-13/R19-12's zero, knobs and Jacobian stand unchanged.
   - When λ_nn = 0, the coefficient is row − κ²/(c₄ + 8X), an O(1) shift.
   - R19-23's 9–65% gaps came from random kernels with no degree-0 part and with g₀ mixing. Both are absent in the actual P1 response at the root.
3. **λ_nn is not a bill row and was never computed.**
   - In R18-13's route (route A), it is the bulk part of the vacuum's uniform-strain Hessian (R19-15 Lemma H) at the root. No registered knob, row or clause zeroes it. The tadpole counterterm is linear, so it does not touch it (`C5_R17-4_report.md:200`).
   - It is therefore generically nonzero (suggested). It vanishes only by a coincidence, or under a clause that subtracts the whole uniform static response, such as (S\*) (`TESTS:8128-8131`).
4. **The λ_nn = 0 branch (checked).** The shift at R18-13's solution is +1.08 in R18-13's totals units, against the pre-solve face1 total of +2.64. A Schur-completed zero still exists with the same two data:
   - w_o is unchanged, because face2 is an isolated A₂ pole;
   - w_d moves from −1.172 to **+0.753**, with face-block Jacobian determinant −3.62 (nonsingular);
   - a second root at w_d = −0.473 lies 0.03 from the point where the leading-order formula breaks down.

5. **Dirac convention (the coordinator's R19-30 heads-up; bracketed, checked).**
   - Every Dirac number here uses the **rows' convention**: R18-13's `dface.py` and R18-5's `xiud`, with the UD vertex real at the pair midpoint and no residual placement phase. These are the refereed rows on which R18-13/R19-12 zeroed face1, and the construction R19-30 says has the rows "identical" once re-placed.
   - I did not use R19-5's code.
   - My model of R19-5's literal pair block multiplies component ij by e^{±iq·p_ij}. It independently reproduces R19-30's raw shift: +1.107e-2 per field at m = 0.3 and +1.296e-2 at m = 0.01, so +0.292 on the face1 total (`dirac_lit_m0.3_N40.out`, `dirac_lit_root_N64.out`).
   - It also breaks H6: Π(e₁, g₀) becomes imaginary, ∝ s³ (y = −4.80e-2 s³ per field at m = 0.01). The time direction then mixes at O(s²) even when λ_nn ≠ 0, adding +0.052 to the face1 total.
   - So under the literal convention the reading would be **FACE1-SHIFTS**: same knobs, w_d → −1.377 (from −1.172), w_o unchanged, Jacobian unchanged (§3.7).

**Reading (worker): FACE1-HOLDS** in route A, in the rows' convention, conditional on λ_nn ≠ 0 (one inequality, generic, uncomputed). The alternatives are **FACE1-SHIFTS** if the bulk entry is subtracted (λ_nn = 0), or if R19-5's literal, unrepaired Dirac pair block is used.
- Axis irreps follow the R19-23 referee's corrected decomposition: 4A₁ + B₁ + B₂ + 2E (`TESTS:8560`). The face decomposition is 5A₁ + A₂ + 2B₁ + 2B₂, with gauge image 2A₁ + B₁ + B₂.

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Setting (`TESTS:8578-8581`).**
  - R9-9's tree graviton. On its box d(q) = q; every s used here has |q_i| ≤ 0.2 for the massive species and ≤ 0.53 for photons.
  - The quadratic symbol is s_EH·K_EH − εΠ (R19-23's `kernels.py`, unchanged).
  - Face direction n = (1,1,0)/√2; e₁ = aa − bb with a = (1,−1,0)/√2, b = ẑ (e:e = 2).
  - The A₁ block is {e₁, h₀₀, h₀ₙ, h_nn, h_aa + h_bb}. The gauge directions are g(ξ) = p⊗ξ + ξ⊗p with p = (−ω, q), ξ ∈ {t, n}.
- **H1 (vertices).** R18-13's vertices at vR18-9's root (b_s, b_f, r, a) = (2.526104, 0.909104, 0.555604, −0.176095), b_γ = 2.9435, m = 0.01, with (w_d, w_o) = (−1.171554, −0.195418) (`C5_R18-13_report.md:282`):
  - U with R17-4's E1 extension, τ_ij = f_if_j, extended to all spatial components by the same tensor;
  - UD at the pair midpoint (P-R18-5c);
  - VWa-geo with the own-direction data.
- **H2 (time components) = R13-5 Lemma P1** (`C5_R13-5_report.md:145-160`, refereed): F^{0j} = Σ_i D_iF^{ij}/E and F^{00} = Σ_j D_jF^{0j}/E in the creation channel; the annihilation channel is the conjugate.
  - This is exact W1 in the pair channel. R19-5's referee confirms it for U and UD, including the own-direction smearings, in the channel-decoupled class (P-R19-5a; `TESTS:7747-7750`).
  - For the photon, P1 exists pointwise (E > 0 off the measure-zero soft corner). A torus-wide exact photon completion is OPEN (R19-9 NOT CONFIRMED, `TESTS:7862-7872`; R19-26 worker).
  - Only pair channels enter the one-loop vacuum bubble (`C5_R19-5_report.md:128`).
- **H3 (seagull).** Ultralocal: no q or ω dependence (R9-9 H-seagull, `C5_R9-9_report.md:48`; inherited by R18-13).
- **H4 (degree 0).**
  - The total degree-0 spatial block is the uniform-strain Hessian (R19-15 Lemma H, `TESTS:8128`). Its shear rows are zero at the root (R18-9's paid μ_E and μ_T2).
  - There are no degree-0 h₀ν terms. This is the "solid" class of R19-23 §3.3 (suggested there), with m₀ = m₁ = m₄ = 0 (referee, `TESTS:8562`).
  - The remaining degree-0 datum on the A₁ gauge block is λ_nn := nn:Π⁰:nn. At μ = 0 it is the bulk coefficient λ_b.
- **H5.** First order in ε at fixed q, then q → 0 for the row. This is R19-23's scope (referee: "leading one-loop pole shifts").
- **H6.** Inversion and time-reversal symmetry of the vertices: the two pair orderings have equal, real-symmetric Gram matrices. Checked for all three species through the identities below.
- **Excluded:**
  - two loops;
  - finite temperature;
  - nonlinear orders;
  - q-dependent seagulls (see §3.5);
  - body-diagonal rows;
  - the soft-corner modification of the photon kernel (R19-9), which is O(r⁴) and does not enter s² coefficients;
  - R19-26's F-re-placement, which is 1 + O(q⁴) and so does not enter κ or c₄.

## 2. Prior art (each counted once)

- **R19-23 + verdict.**
  - The Schur formula δω²/ε = Π₁₁ − Π_{1G}Π_{GG}⁻¹Π_{G1} (`TESTS:8561`; `C5_R19-23_report.md:156-160`).
  - The irreps (verdict item 1).
  - Its random-kernel trials are degree-2 only, with A = 0 (`P/scripts/C5/R19-23/r1923_modes.py:72,95`).
  - P-R19-23a (`C5_R19-23_report.md:241`).
- **R18-13 + verdict.** Lemma O, the triangular Jacobian with determinant E0T0/16, the solve (w_d, w_o) and the 7-knob count (`C5_R18-13_report.md:180-205,278-299`).
- **R19-12 + verdict.** The same face pair, billed in route A (`C5_R19-12_report.md:270`).
- **R9-9.** The bubble normalization −¼⟨VV′/(εε′)·E/(E² − ω²)⟩ (`C5_R9-9_report.md:118`), the ultralocal seagull, and "completion assumed" (`:47`).
- **R13-5 Lemma P1; R19-5 (P-R19-5a).** These supply the time components.
- **Grep.** I searched `P/agents/*.md` and `TESTS.md` for "A₁", "Schur", "bulk", "λ_b", "gauge block" and "h_nn".
  - The only prior A₁/Schur treatment is R19-23 (random kernels).
  - "bulk" appears only as λ_b in R19-23's solid kernel and in the referee's symbolic checks (`ref_R19-23/REFEREE_CHECKS.out`: scalar determinant ∝ 3λ_b + μ_E; static U/U_GR = 1 when μ_E = 0).
  - No item computes the A₁ off-diagonal block or the vacuum's bulk entry.

---

## 3. Results

### 3.1 (a) The A₁ gauge block under P1. Lemma C (contact). Proved; checked

**Statement.**
- Write Γ(A, B) for the pair Gram form summed over internal states. It is real symmetric, and the same in both orderings (H6):
  - scalar: Γ = τ_Aτ_B/(8ε₊ε₋);
  - Dirac: Γ = (N_c/4)[A·B(1 + u·v) − (u·A)(v·B) − (u·B)(v·A)];
  - photon: ½tr(P₁N_AP₂N_Bᵀ).
- Let Π(e, e′; ω, q) = −⟨Γ(e_a, e′_a)/(E − ω) + Γ(e_b, e′_b)/(E + ω)⟩. Here e_{a,b} = e_sp ± sym(q⊗w)/E + e₀₀ q⊗q/E², with w_j = e_{0j} + e_{j0}.
- Then for q = s n:
  - (i) Π(e₁, g₀) ≡ 0, for every ω, q and spatial e₁.
  - (ii) Π(e₁, gₙ) = −4s⟨Γ(e₁, nn)/E⟩. This is ω-independent: a contact term.
  - (iii) Π(g₀, g₀) = −8s⁴⟨Γ(nn, nn)/E³⟩.
  - (iv) Π(g₀, gₙ) = 8ωs³⟨Γ(nn, nn)/E³⟩.
  - (v) Π(gₙ, gₙ) = −8s²⟨Γ(nn, nn)/E⟩.
  - An ultralocal seagull adds only q- and ω-independent spatial terms. It cannot add to (i), because e₁ is traceless and there is no invariant three-index tensor.

**Proof.**
- With P1, g(ξ) acting on the a-ordering amplitude gives 2ξ_ν(E − ω)a^{0ν}, and on the b-ordering amplitude −2ξ_ν(E + ω)b^{0ν}. These cancel the denominators, so the result is ω-independent.
- For ξ = t: a^{00} = b^{00} = q⊗q/E² (two sign flips). So Π(e₁, g₀) = −2⟨Γ(e₁, qq)/E² − Γ(qq, e₁)/E²⟩ = 0 by symmetry of Γ.
- For ξ = n: a^{0n} = −b^{0n} = (q·M·n)/E. The two terms add, giving (ii).
- (iii)–(v) are the same algebra on both sides. ∎

**Checked.**
- **(i) and (ii).** For U, UD and VWa-geo with the root's a and (w_d, w_o): |Π_{1g₀}| ≤ 6e-22, 2e-21 and 6e-19. Π_{1gₙ} and Π_{g₀g₀} are the same to 10 digits at four or five ω values. Π_{g₀gₙ} is exactly linear in ω (`struct_m0.3_N48.out:4-8`, `dirac_m0.3_N48.out:3-6`, `photon_N24.out:4-6,11-13`).
- **(ii), (iii), (v) closed forms.** They equal the direct block to 10 digits (`struct_m0.3_N48.out:9-10`).

### 3.2 (b) The Schur-completed face1 condition. Theorem Q. Proved under H1–H6; checked

**Statement.**
- Let D(s) := Π_tot(e₁, gₙ)/s and G(s) := Π^bubble(gₙ, gₙ)/s². Define:
  - κ := lim (D(s) − D(0))/s²;
  - c₄ := lim (G(s) − G(0))/s²;
  - X := ⟨Γ(nn, nn)/E³⟩ at s = 0;
  - λ_nn := nn:Π⁰_tot:nn.
- At the root, D(0) = 2e₁:Π⁰_tot:nn = 0. The proof: cubic symmetry makes Π⁰ = λP_A + μ_EP_E + μ_TP_T with e₁ ⊥ A₁, and both μ are zero (H4).
- On shell (ω = s):

  Schur/s² = Π_{1G}Π_{GG}⁻¹Π_{G1}/s² = κ²s² / [4λ_nn + (c₄ + 8X)s²] + O(s⁴).

**Proof.**
- By (i) only (Π_GG⁻¹)_{nn} enters.
- By (iii)–(v) and H4: det Π_GG = −8s⁶X[4λ_nn + G(s) − G(0) + 8s²X].
- So (Π_GG⁻¹)_{nn} = Π_{g₀g₀}/det = 1/(s²[4λ_nn + (c₄ + 8X)s² + …]).
- Multiply by Π_{1gₙ}² = κ²s⁶ + …. ∎

**Consequences.**
- **λ_nn ≠ 0:** the Schur term is O(s⁴). The face1 pole coefficient equals R18-13's raw row at every order the row is defined.
- **λ_nn = 0:** the coefficient is row − κ²/(c₄ + 8X).
- **The crossover** is at s² ~ 4|λ_nn|/|c₄ + 8X|. If λ_nn > 0 and c₄ + 8X < 0 (the root's sign), the formula has a pole there: the TT branch crosses the longitudinal gauge branch and first-order theory fails nearby (suggested). The physical relevance needs |λ_nn| ≲ s_phys² ~ 1e-80 for GW momenta at a = ℓ_P, which is fine-tuned (reading).

**Checked by exact roots of det[s_EH K_EH − εΠ]** on the full 5-dimensional A₁ block (`pole_m0.3_N40.out:8,10,11`; root scalar edge, m = 0.3, q = 0.02):

| λ_b | ε | exact pole (ω² − q²)/(εq²) | raw row | row − Schur |
|---|---|---|---|---|
| 0 | 1e-6 | −4.033735e-4 | −3.928316e-4 | −4.033733e-4 |
| 0.01 | 1e-6 | −3.928322e-4 | −3.928316e-4 | −3.928319e-4 |
| 0.01 | 1e-7 | −3.928349e-4 | −3.928316e-4 | −3.928319e-4 |

- My secant root-finder did not converge at λ_b = 0, ε = 1e-7: a flat secant step returned NaN.
- **Scaling (checked; `struct_m0.3_N48.out:20-39`, `dirac_m0.3_N48.out:12-19`).**
  - At λ_b = 1e-3, 1e-2 and 1e-1, Schur/s² falls by a factor of 4 per halving of s, and scales as 1/λ_b.
  - At λ_b = 0 it tends to a constant: +7.536e-6 for the scalar (closed form κ²/(c₄ + 8X) = +7.537e-6) and +2.646e-4 for the Dirac.

### 3.3 (c) The root numbers. Checked

`root_N{64_64_48,96_96_96,128_128_128}.out`. Totals use R18-13's convention: 4 scalars, plus 22.5 Dirac with dface's e:e = ½ (that is, ¼ of the e:e = 2 kernel), plus 12 vectors (`C5_R18-13_report.md:90-93`).

| N (scalar, Dirac, photon) | κ_tot | c₄,tot | 8X_tot | photon share of κ | −κ²/(c₄ + 8X) |
|---|---|---|---|---|---|
| 64, 64, 48 | −1.149 | −3.308 | +1.402 | 97.8% | +0.693 |
| 96, 96, 96 | −1.185 | −2.705 | +1.404 | 97.8% | +1.079 |
| 128, 128, 128 | −1.281 | −2.926 | +1.403 | 98.0% | +1.077 |

- **Precision.** The scalar and Dirac entries are converged to about 1e-3 relative. The photon's κ and c₄ are extracted from grid shifts with s = 0.069–0.37, and from N = 96 to 128 they move by about 8%. So I quote the λ_nn = 0 shift as **+1.08 ± 0.1** (checked sequence, suggested error).
- **The bubble's own degree-0 entries** (totals, for information): 2e₁:Π^b(0):nn = −0.288 and 4nn:Π^b(0):nn = −25.9 (N = 128).
  - At the root, the first is cancelled by the seagull and strain-flow terms (H4).
  - The second is not cancelled by anything registered. λ_nn = 0 would need the seagull's bulk entry to equal +6.47 exactly (reading).

**(c) Re-solve.**
- **λ_nn ≠ 0 (route A as registered).** Nothing moves:
  - (w_d, w_o) = (−1.171554, −0.195418) at N = 224;
  - face Jacobian [[1.676, 3.471], [0, 6.943]], determinant 11.639;
  - the axial 4 × 4 block is untouched, because E_g and T₂g are isolated B₁/B₂ poles (Lemma I);
  - rank 6;
  - **7 continuous law knobs**, as in vR18-13.
- **λ_nn = 0 branch** (`resolve_N128.out`, `resolve_scan_N128.out`, `verify_root_N128.out`).
  - face2 is an isolated A₂ pole, so w_o stays at −0.195418.
  - κ and c₄ are exactly linear in w_d at s → 0 (fit curvature ~1e-6).
  - The Schur-completed face1 total f(w_d) = 1.676(w_d − w_d0) − κ(w_d)²/(c₄(w_d) + 8X) has two roots:
    - **w_d = +0.75313**: df/dw_d = −0.52, face-block determinant −3.62 (nonsingular, sign flipped). Directly re-evaluated at Ng = 128, f = −1.4e-6.
    - **w_d = −0.47329**: determinant +146.7, but only 0.031 from the singular point c₄ + 8X = 0 at w_d = −0.5043, where the leading-order formula fails. Not reliable (suggested).
  - The knob count is unchanged (two off-axis data), but the face1 condition becomes nonlinear in w_d.
  - At w_d = +0.753 the u_d stencil is nonnegative (weights 0.247, 0.377, 0.377). Corollary N (signed stencils needed) applies to the raw rows only.
- **Convention sensitivity (checked; `dirac_weight_sensitivity.out`, `resolve_uniformD.out`).**
  - If the Dirac kernel entered the totals at the same e:e = 2 weight as the scalars and photons, the shift would be +4.53 and the roots would move to w_d = +2.899 or −0.800. In that case R18-9's root itself would also change; this is not done here.
  - The λ_nn ≠ 0 conclusion does not depend on this convention.

### 3.4 (d) Is the correction O(1) relative to the raw row?

- **Route A, λ_nn ≠ 0:** no. The relative correction is κ²s²/(4λ_nn) → 0. It is a quartic-dispersion term, not a speed term (proved, Theorem Q).
- **λ_nn = 0:** yes. +1.08 in totals units, against the pre-solve face1 total +2.64 and the own-direction lever 1.676 per unit w_d (checked).
  - Per species at m = 0.3 (self-contained, λ = 0): scalar 1.6% and Dirac 11% of its own raw row.
  - The photon carries 98% of κ.
- **R19-23's 9–65%** (`C5_R19-23_report.md:161-172`) came from A = 0 random kernels with Π_{1g₀} ≠ 0. Under P1, Π_{1g₀} ≡ 0, so those numbers do not transfer (reading).

### 3.5 What would break FACE1-HOLDS (scope)

- **A q-dependent cubic seagull** of the form h₀₀ Σ_i ∂_i²h_ii gives Π_{1g₀} ∝ s³. With Π_{g₀g₀} ~ s⁴, that produces an O(s²) shift (proved by the same algebra). H3 excludes it, as R9-9 and R18-13 did.
- **A time component that is not P1**, that is, not exactly conserved in the pair channel. Π_{1g₀} then becomes generically nonzero, as in R19-23's random kernels.
- **λ_nn = 0**, or more generally gₙ lying in the null space of the degree-0 gauge block. If degree-0 h₀ν terms are present, the condition is that (D⁰)⁻¹_{nn} stays finite. That is again a single equality (proved).

### 3.7 Dirac convention bracket (the coordinator's heads-up on R19-30; checked)

- **Convention used throughout this report.**
  - The UD vertex G(k̄) is real at the pair midpoint, with legs k ± q/2 and no residual placement phase in midpoint variables. This is R18-13's `dface.py` (`P/scripts/C5/R18-13/dface.py:1-10`) and R18-5's `xiud`.
  - I reproduce dface's face1 to 0.2% (`dirac_m0.3_N48.out:8-10`).
  - These are the refereed rows that R18-13 and R19-12 zeroed. R19-30 (worker, referee running) says they coincide with its phase-restored, parity-re-placed construction.
- **Literal R19-5 model** (`r1929_dirac_lit.py`; R19-30 report §0 item 2 describes the code: "pair block puts UD(k̄) in the same slot with no phase").
  - Component ij of the pair kernel carries e^{±iq·p_ij}, with p_ii = e_i and p_ij = (e_i + e_j)/2. P1 time components are built from the phased kernel, and the Gram form is Hermitian.
  - Results:

    | | rows' convention | literal model (either sign) |
    |---|---|---|
    | raw face1, m = 0.3, N = 40 (dface units) | +5.954e-4 | +1.1663e-2 (Δ = +1.107e-2; R19-30: +1.110e-2) |
    | Π(e₁, g₀) at s = 0.05 | ≤ 3e-21 | ∓4.681e-6 i, ω-independent, ∝ s³ |
    | Schur/s² at λ_b = 0.01, s = 0.08 → 0.02 (e:e = 2) | 2.5e-6 → 1.6e-7 (→ 0) | −1.140e-2 → −1.187e-2 (→ constant) |
    | root m = 0.01: raw face1 shift per field | — | +1.2958e-2 (R19-30: +1.30e-2) |

- **Reading.**
  - The literal block breaks H6: the relative phase between zz and the xx/yy/xy components makes the pair Gram form complex.
  - So Π_{1g₀} ≠ 0, and the time-diffeo direction mixes at O(s²) whatever λ_nn is.
  - At the root, in R18-13's totals: the raw face1 total rises by 22.5 × 1.2958e-2 = +0.292, and the g₀-channel Schur term adds (5.625y)²/(8X_tot) = +0.052 (`dirac_lit_root_N64.out`).
  - Both are independent of w_d and w_o, because the photon and scalar have Π_{1g₀} = 0.
  - Re-solve (λ_nn ≠ 0): Δw_d = −0.344/1.67645 = −0.205, so (w_d, w_o) = (−1.377, −0.195). Same Jacobian (determinant 11.639) and the same 7 knobs.
  - That is FACE1-SHIFTS in this convention, a small-shift version.
  - If R19-30's repair is adopted, the rows' convention applies and §§3.1–3.4 stand.

### 3.6 Side remark (suggested)

- Under a TT-only (S\*\*) subtraction (`TESTS:8024`) combined with (S\*), λ_nn = 0 and the raw row is 0 by construction. The face1 pole is then −κ²/(c₄ + 8X) ≠ 0.
- A (Σ)-type clause that replaces the whole O(p²) response (`TESTS:8252`) also removes κ. Count once with R19-19/R19-20.

---

## 4. Against the FIXED readings (`TESTS:8588-8592`)

**Worker reading: FACE1-HOLDS, in route A (R18-13/R19-12), in the rows' Dirac convention, under H1–H6, conditional on λ_nn ≠ 0.** λ_nn is one inequality, generic, and not computed.

| clause | status |
|---|---|
| all-rows zero survives with the Schur row | yes. The Schur term is O(s⁴) when λ_nn ≠ 0 (Theorem Q, proved). The physical face1 coefficient equals the raw row (checked by exact poles) |
| same knob count | yes: 6 equality tunings + 1 window = 7 (unchanged) |
| nonsingular Jacobian | yes: face block determinant 11.639 (R18-13), axial block unchanged; rank 6 |

- **FACE1-SHIFTS is the reading if λ_nn = 0.** That happens if the bulk entry is subtracted, as by (S\*), or tuned away. The zero survives with the same knob at (w_d, w_o) = (+0.753, −0.195), face-block determinant −3.62 (checked, R18-13 convention). The second root, −0.473, is unreliable.
- **FACE1-SHIFTS also applies if R19-5's literal, unrepaired Dirac pair block is used** (§3.7, the R19-30 bracket). Then (w_d, w_o) = (−1.377, −0.195), with the same knobs and Jacobian. The raw shift is +0.292 and the g₀-channel Schur term +0.052 (checked, model of the literal code).
- **FACE1-FAILS:** not met in any branch.

**Against the expectation (`TESTS:8593`).**
- "The off-diagonal gauge mixing is generically nonzero at one loop" is half right:
  - Π_{1gₙ} ≠ 0 (κ_tot = −1.28);
  - Π_{1g₀} ≡ 0 under exact pair-channel W1.
- The gₙ mixing reaches the pole only at O(s⁴) unless the bulk entry vanishes. So the expected FACE1-SHIFTS holds only in the λ_nn = 0 branch.

**What a referee must decide.** Whether "λ_nn ≠ 0, generic and unpaid" is acceptable as stated, or whether the bulk entry has to be computed. The bulk entry is the isotropic strain Hessian under the root's SF convention, with the CC counterterm's O(h²) part. I did not compute it, because the bulk channel of the strain flow is not volume-preserving and I could not fix its measure term from the registered sources in time.

## 5. Prices (named, not adopted)

- **P-R19-23a: discharged in route A**, conditional on λ_nn ≠ 0. It needs no number, only the inequality. Its inputs are P1 (refereed for U and UD; photon OPEN) and the ultralocal seagull (inherited).
- **P-R19-29a (new, conditional): λ_nn ≠ 0.** The vacuum's degree-0 bulk entry must not vanish. It costs zero numbers; it is an inequality. If a later clause subtracts the bulk, as (S\*) does, this is replaced by the λ_nn = 0 re-solve above (same knob, different w_d).
- **No axiom text is touched.** Stress, seagull and source are downstream (`AX:114-130,187`).

## 6. Strong-word check

- **"Identically zero" (Π_{1g₀})** is proved under P1 + H6 and checked to ≤ 6e-19 for three species. It is not claimed for non-P1 time components.
- **"Exactly"** is used for the ω-independence of the contact terms (algebraic) and the exact linearity of κ and c₄ in w_d at s → 0 (the O(s²) factor of u is linear in w).
- **"Proved"** covers Lemma C and Theorem Q, under H1–H6. Both are short and unrefereed.
- **"Generic" (λ_nn ≠ 0)** is suggested, not checked.
- **"Converged":** scalar and Dirac to about 1e-3; photon κ and c₄ to about 8%.
- **Not claimed:**
  - the value or sign of λ_nn;
  - the λ_nn = 0 numbers under any convention other than R18-13's;
  - that my phase model is exactly R19-5's code. It reproduces R19-30's raw shift to 3 digits, but the g₀ term (+0.052) is from my model only;
  - exact torus-wide photon W1;
  - two loops, finite T, body rows;
  - π⁰ health (R19-23's open item);
  - one law at both masses.

## 7. For the referee

1. **Lemma C(i).** Check the sign structure of P1 in the two orderings (R13-5: "annihilation channel = complex conjugate", with D(−q) = −D(q)\*), and the Gram symmetry. The script check is `struct_m0.3_N48.out:4-8`.
2. **Theorem Q's determinant algebra**, in particular Π_{g₀gₙ} = 8ωs³X on shell, which gives the +8X.
3. **Whether H4 (solid, μ = 0, ultralocal seagull) holds at the actual root**, and whether any registered convention forces λ_nn = 0.
4. **The photon's κ and c₄ extraction** with grid shifts. A finer N and smaller s would tighten the λ_nn = 0 branch numbers.
5. **The R19-30 bracket.** Is my phase model (component ij × e^{±iq·p_ij}, with P1 built from the phased kernel) the same as R19-5's literal code, including how it treats the time components?

## 8. Files (`S/scripts/`)

- **Library:** `a1lib.py` (scalar U/E1 A₁ block, P1, seagull).
- **Structure checks:**
  - `r1929_struct.py` → `struct_m0.3_N48.out`;
  - `r1929_dirac.py` → `dirac_m0.3_N48.out`;
  - `r1929_photon.py` → `photon_N24.out`.
- **Normalization and pole:**
  - `rowcheck.py` → `rowcheck_m0.3.out`;
  - `r1929_pole.py` → `pole_m0.3_N40.out`.
- **Root numbers:** `r1929_root.py` → `root_N64_64_48.out`, `root_N96_96_96.out`, `root_N128_128_128.out`.
- **λ_nn = 0 re-solve:**
  - `r1929_resolve.py` → `resolve_N128.out`;
  - `r1929_resolve_scan.py` → `resolve_scan_N128.out`;
  - `r1929_verify_root.py` → `verify_root_N128.out`;
  - `r1929_resolve_uniformD.py` → `resolve_uniformD.out`;
  - `dirac_weight_sensitivity.out`.
- **R19-30 bracket (literal R19-5 Dirac pair block, modelled):**
  - `r1929_dirac_lit.py` → `dirac_lit_m0.3_N40.out`;
  - `r1929_dirac_lit_root.py` → `dirac_lit_root_N64.out`.
