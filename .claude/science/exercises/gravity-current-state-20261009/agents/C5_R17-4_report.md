# C5 R17-4 report: the cone bill's uncomputed rows (off-axis graviton speeds, LV tadpole) and the shear-row certificate

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 00:08Z to about 00:55Z. No repository file was edited. No downloads, no web lookups. No pending R16/R17 scratch report was used (R16-13's folder holds `scripts/` only; no report existed at 00:32Z).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `S/` = `.../scratchpad/C5/R17-4/`. Scripts and `.out` files are in `S/scripts/`. Every run took under 2 min at `OMP_NUM_THREADS=2`.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `P/TESTS.md`: C5 method (`:2302-2320`), round-17 rules and my item (`:5688-5713`, `:5816-5845`). `P/agents/C5_S20_synthesis.md` (Q3 `:483-497`, R17-4 draft `:730-758`). `C5_R16-3_report.md` (all) and `vR16-3`; `C5_R16-9_report.md` (all) and `vR16-9`; `C5_R13-8_report.md:1-200` and `vR13-8`; `C5_R9-9_report.md:28-200` and `vR9-9`; `C5_R11-3_report.md:104-158` and `C5_R11-3_referee_verdict.md:30-48`. Archived runners `P/scripts/C5/R16-3/` (copied unmodified into `S/scripts/`), `P/scripts/C5/R16-9/opt3.py`, `relaxed_pathU4.py` (read), `P/scripts/C5/R13-8/r138_onshell_loop.py` (read).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **The general off-axis formula (proved; checked to 1e-10 on a direct grid).** For a pair vertex that depends only on the pair's relative momentum (extension E1, stated in §1), the graviton-cone shift for any direction n and TT polarization e is
   Ξ(n, e) = (1/32)⟨W_e A_nn/ε⁵⟩ − (1/192)⟨(n·∇)²W_e/ε³⟩, with A_nn = n·Hess(ε²/2)·n − 1.
   On an axis the second term vanishes and this is R9-9's Theorem T. Cubic symmetry leaves four independent numbers (R13-8's count, re-checked), which I take as Ξ_Eg and Ξ_T2g on the axis plus the two face-diagonal polarizations. The body-diagonal value follows: Ξ_body = (8Ξ_face1 + 4Ξ_face2 − 3Ξ_Eg)/9.
2. **For the U vertex, one off-axis row is free and one is new (proved).**
   - Ξ_face2 ≡ Ξ_T2g for every law in 𝒮. So it vanishes whenever the axis T₂g row does.
   - Ξ_face1 = (3Ξ_Eg + Ξ_T2g)/4 − (1/128)⟨K₆(f)/ε⁷⟩. Here K₆ = f_x⁶ − 15f_x⁴f_y² + 30f_x²f_y²f_z² (symmetrized) is the sixth cumulant of the pair "velocity" f = σσ′. It is zero for a Gaussian, which is the continuum control. At the axis zeros the face row is exactly −⟨K₆/ε⁷⟩/128.
   - So for U the off-axis rows cost **one** further condition, not two. The shear μ_E is the fourth cumulant (R14-3); this row is the sixth.
3. **That one condition was not met together with the axis zeros anywhere I looked (checked; search, not a proof).**
   - On R16-3's U zero (m = 0.1, 0.03, 0.01): Ξ_face1 = −8.94e-4, Ξ_body = −7.95e-4, as large as untuned corner values.
   - The zigzags that zero the axis rows make the f-distribution narrow, and that makes K₆ > 0.
   - Over 98 explicit laws, 360 terraced zigzags, free-segment optimizers, and a slope-resolved occupation-measure search over 46 cells with an axis-feasible point (m = 0.1 and 0.01): the face row was always negative at points where both axis rows are ≥ 0. The largest value found was −1.12e-4.
4. **R9-9's M vertex has no local off-axis extension. In fact its axis T₂g amplitude is not local either (proved, Lemma M).** M sets |V_T2g|² = 4g_xg_y. Any continuous pair amplitude that is covariant under the proper rotation C₂ about y must vanish on the zone face k_x = π. M's does not vanish there, because g(π) > 0 on every doubler-free law in 𝒮. U's amplitude f_xf_y does vanish there, since σσ′(π) = 0. So R16-3's and R16-9's M-vertex rows use a vertex with no absolutely summable real-space kernel on the laws where they were tuned.
5. **The off-axis rows depend on how the vertex is extended off the axis (checked).** A product-of-legs extension (E2, the type R13-8 used) agrees with E1 on the axis but not off it. On P-Z's sharp-turn edges the E2 off-axis rows are O(1): Ξ_face1 = +1.41/+0.70/+0.35/+0.17 for turn widths 0.03/0.06/0.12/0.24 (Z1 skeleton, scaling as 1/width), against −2e-4 to −9e-4 for E1. That is a further vertex datum (P63(iii) extended to O(q²)), not something R9-9 fixes.
6. **The LV tadpole is a separate condition that no edge shape can meet (proved from refereed lemmas).** In the supplied zero-point vacuum, ρ + p ≥ ρ > 0 for every law in 𝒮 and both stresses (R11-3 Corollary P with its referee's scope). On R16-3's zero laws, ρ + p_U = 0.604–0.611 and ρ + p_M = 0.625–0.633 per real scalar in lattice units (w_U = 0.283–0.288). It needs a non-shape knob, the trace-tadpole counterterm.
7. **The bill (reading, conditional).** For U with E1 the gravity block becomes 2 (axis shape) + 1 (K₆ row) + 1 (shear) + 1 (tadpole). That makes **8 + CC per class, or 12 + CC per species**, against R16-9's 9 + CC / 13 + CC. If the K₆ row cannot be shape-tuned with the axis rows, which is what the search suggests, it needs a non-shape knob too. The count stays the same, but the zigzag route then no longer pays for the cone by shape alone.
8. **(f) was not completed (done without R16-13's report).** I did not produce an enclosure. An outward-rounded bound on a nonconvex cubic moment problem over continuous (b, lo, hi, s_min, m) needs a global method (branch-and-bound or a verified moment-SOS relaxation) that I could not build in the time. Reading: OPEN.

**Against the FIXED readings (`TESTS:5838-5841`); worker reading, referee required.**
- **COUNTED-ROWS, second clause, in part (U vertex, E1):** proved that one of the two off-axis rows (face2) vanishes identically given the axis zeros.
- **The other off-axis row (the K₆ row): OPEN.** The search suggests CONFLICT with the axis zeros in 𝒮, but there is no certified enclosure.
- **Tadpole:** a separate condition that no shape can satisfy (proved).
- **M vertex:** off-axis rows undefined (Lemma M).
- **(f):** OPEN. Neither CERTIFIED-CONFLICT nor JOINT.

---

## 1. Class, hypotheses, excluded realizations (stated before any title)

- **Laws.** R14-3/R16-3's separable class 𝒮: ε² = m² + Σᵢ g(kᵢ), g = σ², σ ∈ C², σ(0) = 0, σσ′(π) = 0, |σ′| ≤ 1 (`C5_R16-3_report.md:33`), with an edge floor σ ≥ s_min > 0, so there is no doubler (`C5_R16-9_report.md:38`, R16-9's convention). f := σσ′, which is odd, periodic and C¹ with f(π) = 0. Masses m = 0.1, 0.03, 0.01. The supplied scalar zero-point vacuum; in the empty Fock vacuum everything here is zero (`C5_R9-9_report.md:110`).
- **One-loop TT self-energy.** R9-9's Π(ω, q) = S₂ − ¼⟨|V|²/(ε₊ε₋)·E/(E² − ω²)⟩ (`C5_R9-9_report.md:118`; normalization refereed, `vR9-9:7-12`), with the pair written symmetrically as (k + q/2, −k + q/2). Ξ := ∂_{q²}Π + ∂_{ω²}Π along q = s n, so c_T² − 1 = 2κ_lat Ξ (`C5_R9-9_report.md:120`). The seagull is ultralocal (ω- and q-independent), so it drops out.
- **Off-axis extension E1 (stated; the item asks for it, `TESTS:5825`).** The TT pair vertex is V_e(k) = Σ e_ij τ_ij(k), with k the relative momentum and no further q-dependence. Two choices of τ:
  - U: τ_ij = f_i f_j (forward value εv_iv_j, `C5_R9-9_report.md:46`);
  - M: τ_ij = σ_iσ_j (`:45`).

  Inside the box (σ = k) E1 equals the exact continuum TT pair vertex, since e·q = 0. On the axis it is R9-9's class 𝒱.
- **Alternative extension E2 (comparison only).** V = Σ e_ij f(k₁ᵢ)f(k₂ⱼ) on the two legs, the product type of R13-8's runner (`P/scripts/C5/R13-8/r138_onshell_loop.py:67,81-82`). It equals E1 on the axis and in the box.
- **Ward requirement: standard first-order W1, assumed, not built** (as R9-9, `C5_R9-9_report.md:47`; `vR16-3:17`). W1 does not constrain TT components. No second-order identity, standard or deformed, is used.
- **Polarizations (all normalized e:e = 2, as R9-9's Eg/T2g):**
  - axis (001): Eg = diag(1, −1, 0) and T2g = xy + yx;
  - face (110): face1 = aa − bb and face2 = ab + ba, with a = (1, −1, 0)/√2, b = ẑ;
  - body (111): aa − bb with a = (1, −1, 0)/√2, b = (1, 1, −2)/√6.
- **Excluded (per item):** Dirac/photon/gluon vertices (R16-13); pairing; deformed W2; two loops; non-separable laws; matter's own graviton-loop shift (Ξ is the bare-cone shift, not the dressed split, `vR16-3:17`).
- **Round-16/17 head rules.**
  - v_max is stated for every law (§3.8).
  - No frame-tied kernel is introduced.
  - Ward: standard W1, assumed.
  - Gauge-field v_max: the graviton symbol is R9-9's d(q). I prove |v| ≤ max_i|d′(qᵢ)| and d′ ≤ 1 (from ρ′ ≤ 0), but did not check d′ ≥ −1 numerically.
  - The counting basis is stated in §3.9.
  - No Λ mechanism is proposed; the tadpole counterterm is *stipulated*.
  - Physical control: §3.4.
  - No readout-bridge claim is made.
  - Forks are not offered as exhaustive (E1/E2 and M/U are examples; the vertex is a law datum).
  - No initial-state claim is made.
  - Changed hypothesis: q off-axis (R16-3 restricted q ∥ axis, `TESTS:5829`).
- **Tail clause.** Raw |ε_r| of ε_1D = √(0.09 + g), **nothing subtracted** (as R16-3).

## 2. Prior art (each counted once)

- **R16-3** (`vR16-3`, CONFIRMED WITH CORRECTIONS): the axis v_z form, P-Z zigzags, the common Eg/T2g zero (`vR16-3:7,13`). Its "q off-axis not addressed" is at `C5_R16-3_report.md:41,312`.
- **R16-9** (`vR16-9`, OPEN): Lemmas R/R_U, the bill 9 + CC / 13 + CC with "two off-axis rows not computed" and "LV tadpole not computed" (`C5_R16-9_report.md:222,225,274`; `vR16-9:15`).
- **R13-8** (`vR13-8`, OPEN): the P,T-even TT degree-2 on-shell rank is 4 = c_T + 3 anisotropies (`vR13-8:3-9`). It also computed **off-axis directions** with an E2-type local metric vertex for NN, box-L and Dirac, with an anisotropy span of 3/3 over four masses (`vR13-8:13`; `C5_R13-8_report.md:157-178`). That is the only prior off-axis loop. It uses a product-of-legs vertex, not R9-9's M/U.
- **R9-9 Theorem T** (`C5_R9-9_report.md:122-131`; `vR9-9:7-12`).
- **R11-3** Lemma Tad, Identity W, Corollary P (`C5_R11-3_report.md:108-129`), with its referee's scope (`C5_R11-3_referee_verdict.md:41`) and "two independent tadpole renormalization conditions in the linear preferred-time EFT" (`:47`).
- **R14-3** (R1): μ_E = −(5/72)⟨K₄/ε³⟩ (`C5_R16-3_report.md:234`, confirmed `vR14-3:5`).
- **C3 K-num** (`C3_K-num_report.md:170,251`): "off-axis q … not run".
- **Grep.** In the packet and `docs/` I searched "off-axis", "face diagonal", "body diagonal", "sixth cumulant", "K₆". The hits are the items above plus unrelated geometry uses (C3 G-L pairs, RV4, B). No prior off-axis identity or K₆ row was found.

---

## 3. Results

### 3.1 Rechecks of archived runners (checked; `validate.out`, `evalzeros.out`, `tadpole.out`)

- **R16-3 `zz.py`.** My general off-axis code reproduces it on the axis. NN m = 1: M,T2g −1.903007307e-3, M,Eg −8.301856729e-4, U,T2g −2.289166113e-4, U,Eg −6.883236561e-5, all equal to R9-9's table. G(1.0) and Z1 at m = 0.3 agree to all 10 printed digits (Z1 M,T2g +3.904715285e-4, the referee's value).
- **R16-3's U zeros, re-solved by Newton.** (u, v) = (0.964879, 0.007410) at m = 0.1, (0.955996, 0.015995) at 0.03, and (0.955208, 0.016763) at 0.01. These equal `C5_R16-3_report.md:208-210` to 6 digits. All are in the simplex with max|σ′| = 1.000000000.
- **R16-3's M zero.** |ε₁₂₈| = 3.67e-5 reproduces the referee's correction (`vR16-3:17`).
- **R11-3 NN control (m = 1).** ρ = 1.3000, p_U = 0.0991, w_U = 0.076, w_M = 0.282, equal to `C5_R11-3_report.md:139`.

### 3.2 (a) The off-axis identity (proved; checked)

**Derivation.** Write ε± = ε(k ± sn/2) and D = n·∇.
- ε₊ε₋(ε₊ + ε₋) = 2ε³ + s²[(3/4)ε²D²ε − (1/2)ε(Dε)²] + O(s⁴).
- So α := ∂_{s²}Π(0, sn) = (1/64)⟨W(3D²ε/ε⁴ − 2(Dε)²/ε⁵)⟩, and β := ∂_{ω²}Π = −(1/32)⟨W/ε⁵⟩. β is the same as R9-9's.
- Integrate by parts once on the torus (W periodic and C¹):

  **Ξ(n, e) = (1/32)⟨W_e(5v_n² − 1)/ε⁵⟩ − (3/64)⟨(DW_e) v_n/ε⁴⟩,  v_n = Dε.**

- Using D(Dε/ε⁴) = [Hess_nn(ε²/2) − 5(Dε)²]/ε⁵ (R9-9 step 3) and ⟨DW·Dε/ε⁴⟩ = (1/3)⟨D²W/ε³⟩ gives the equivalent form

  **Ξ(n, e) = (1/32)⟨W_e A_nn/ε⁵⟩ − (1/192)⟨(n·∇)²W_e/ε³⟩,  A_nn = Σᵢ nᵢ² (g″(kᵢ)/2 − 1)** (separable laws). ∎

- If DW = 0 this is Theorem T and R16-3's v_z form, which covers every axis polarization.
- With R9-9's asymmetric pair (k, k − q) and k_z-independent W it reproduces α = (5/32)⟨W(∂ε)²/ε⁵⟩ (`C5_R9-9_report.md:128`).

**Checks** (`validate.out`; Laplace-separable evaluator `offaxis.py`):
- **Direct 3D grid.** Π(0, sn) at s = 0.08, 0.04, 0.02 with Richardson, plus β on N = 64 and 96 grids, NN band, U vertex, m = 1 and 0.5. All five functionals agree with the closed form to ≤ 1.1e-10 relative. Example, m = 1: face1 −1.245452931e-4, face2 −2.289166113e-4, body −1.895035215e-4.
- **Cubic structure (`basis.out`).** Random O_h-invariant rank-6 forms give an on-shell TT map of **rank 4**, confirming `vR13-8:7-9` independently. The linear relation is **Ξ_body = (8Ξ_face1 + 4Ξ_face2 − 3Ξ_Eg)/9**. There is no face-polarization mixing and the body pair is degenerate. Every computed law satisfies the relation to ≤ 2e-18 (absolute).
- **Basis of the four TT speed parameters:** {Ξ_Eg, Ξ_T2g, Ξ_face1, Ξ_face2} (rank 4, checked). After the axis zeros the off-axis content is (Ξ_face1, Ξ_face2).

### 3.3 Lemma M: R9-9's M vertex is not local where it was tuned (proved)

**Statement.** Let ρ(K) be any continuous, 2π-periodic pair amplitude, real or complex, for the T₂g stress component T_xy at q → 0. Suppose it is covariant under the proper rotation C₂ᵧ: (x, z) → (−x, −z) (`AX:38,57-58`). Then ρ(π, K_y, 0) = 0 for every K_y. Hence no such amplitude has |2ρ|² = 4g(K_x)g(K_y), M's T₂g vertex (`C5_R9-9_report.md:45`), on any law with g(π) > 0. In particular this holds on every doubler-free law in 𝒮, including Z1 and all of R16-3's and R16-9's zero laws (min edge g = 0.142–0.152).

**Proof.**
1. C₂ᵧ maps T_xy → −T_xy and K → (−K_x, K_y, −K_z). So ρ(−K_x, K_y, −K_z) = −ρ(K_x, K_y, K_z).
2. At K_x = π, K_z = 0, periodicity (−π ≡ π) gives ρ(π, K_y, 0) = −ρ(π, K_y, 0) = 0.
3. M requires |ρ(π, K_y, 0)|² = g(π)g(K_y) > 0 for K_y ≠ 0. Contradiction. ∎

**Consequences.**
- An absolutely summable real-space stress kernel has a continuous symbol, so M's T₂g vertex has a kernel that is not summable (a jump at the zone face, i.e. ~1/r tails).
- Off the axis, the interference of off-diagonal and diagonal components, e.g. face1's V = (g_x + g_y)/2 − σ_xσ_y − g_z, makes M's E1 integrand discontinuous. The IBP then fails. Checked: for NN-M the closed form misses the direct grid by 25–30%, while U agrees to ≤ 1.1e-10.
- U is unaffected: f(π) = 0, so f_xf_y vanishes on the face.
- **Reading.** R16-3's M-vertex numbers are correct integrals, but of a vertex that no local law realizes on doubler-free edges. Of R9-9's two vertices, only U can be "the physical vertex" (P63(iii)).

### 3.4 U-vertex identities (proved; checked)

Notation: a6 = ⟨f_x⁶/ε⁷⟩, a42 = ⟨f_x⁴f_y²/ε⁷⟩, a222 = ⟨f_x²f_y²f_z²/ε⁷⟩, b4 = ⟨f_x⁴/ε⁵⟩, b22 = ⟨f_x²f_y²/ε⁵⟩ (any axis labels, by symmetry). Apply §3.2's first form, drop terms odd in any one fᵢ, and integrate by parts once in one variable. With ∂ₓε⁻⁵ = −5fₓ/ε⁷ this gives ⟨φ(fₓ)f′ₓψ/ε⁵⟩ = 5⟨Φ(fₓ)fₓψ/ε⁷⟩, where Φ′ = φ. The result:

- Ξ_Eg = (5/16)(a42 − a222) − (1/16)(b4 − b22);  Ξ_T2g = (5/8)a222 − (1/8)b22. These are R16-3's U forms in another notation.
- **Ξ_face2 = Ξ_T2g identically.** Here V = √2 f_z(f_x − f_y). The (DW)·S term gives −(10/32)a42 + (30/32)a222 and the W S² term gives (10/32)(a42 − a222); together these are (5/8)a222. The W term gives −(1/8)b22. ∎
- **Ξ_face1 = −a6/128 + 45a42/128 − 5a222/16 − 3b4/64 + b22/64 = (3Ξ_Eg + Ξ_T2g)/4 − (1/128)⟨K₆/ε⁷⟩**, with K₆ := a6 − 15a42 + 30a222 (as a 3D average). ∎
- **Ξ_body = (Ξ_Eg + 2Ξ_T2g)/3 − (1/144)⟨K₆/ε⁷⟩**, from the O_h relation.
- **Laplace form.** ⟨K₆/ε⁷⟩ = Γ(7/2)⁻¹∫dt t^{5/2}e^{−tm²}E0³κ₆(t), where κ₆ = μ₆ − 15μ₄μ₂ + 30μ₂³ is the sixth cumulant of f under the 1D tilted measure e^{−tg}dk/E0.

**Checks.**
- face2 − T2g = 6e-14 on G(1.0). On wt = 0.03 zigzags it is 5e-8, a numerical f′ error against values ~1e-3 (`evalzeros.out`).
- The moment form (`fastU.py`) equals the general symbolic code to 1e-9 relative on G(1.0) and 6e-5 on C2 (`scanU.out`, first lines).

**Physical control (proved, analytic).** In the continuum with a Lorentz-invariant regulator (f = k, ε² = m² + k²), DW = 0 for every TT e (W depends only on k ⊥ n) and A_nn = 0. So Ξ ≡ 0 for every (n, e). Equivalently, κ₆ = 0 for the Gaussian tilt: 15 − 45 + 30 = 0. This is the same observable in a model known to have an isotropic cone.

### 3.5 (b) The off-axis rows on the axis-zero laws, and the search for a common zero (checked)

**On R16-3's U zeros (E1; `evalzeros.out`).**

| m | (u, v) in (A, C2, C) | Ξ_Eg, Ξ_T2g | Ξ_face2 | **Ξ_face1** | Ξ_body | v_max |
|---|---|---|---|---|---|---|
| 0.10 | (0.964879, 0.007410) | ≤ 9e-15 | 5e-8 (= T2g, identity) | **−8.940e-4** | −7.946e-4 | 0.998293 |
| 0.03 | (0.955996, 0.015995) | ≤ 9e-15 | 5e-8 | **−8.960e-4** | −7.964e-4 | 0.999846 |
| 0.01 | (0.955208, 0.016763) | ≤ 9e-15 | 5e-8 | **−8.961e-4** | −7.965e-4 | 0.999983 |

**Independent check of the m = 0.1 value (`grid_mom.out`).** A direct 3D zone grid of the derivative-free moment form, with no Laplace step, gives Ξ_face1 = −9.007e-4, −8.931e-4 and −8.957e-4 at N = 240, 480 and 720, against Laplace −8.940e-4. At N = 720 the axis rows are −2.7e-6 and −1.3e-6, which is the grid's resolution of the wt = 0.03 turns. The f′-containing IBP form does not converge on a 3D grid at N ≤ 720 (`grid_face.out`), because f′ has spikes of width 0.03 and the grid has about 3 points per turn. Its 1D-resolved Laplace value agrees with the moment form to 6e-5 (§3.4).

So ⟨K₆/ε⁷⟩ = +0.1144 at the zero. Size (comparator normalization, `C5_R16-3_report.md:276`): 16π|Ξ_face1| ≈ 0.045 in c_T² at a = ℓ_P, against GW170817's ~1e-15. The row needs the same ~1e-13 relative tuning as the axis rows.

**Corners at m = 0.1 (U, E1).**

| law | Ξ_Eg | Ξ_T2g | Ξ_face1 |
|---|---|---|---|
| G(1.0) | −2.11e-4 | −4.01e-4 | −2.79e-4 |
| C2 | +9.8e-6 | +3.72e-4 | −9.33e-4 |
| C | −1.90e-4 | +6.8e-5 | −1.08e-3 |
| Z1 | +5.94e-4 | +6.15e-4 | −2.30e-4 |

Every corner has face1 < 0, so the origin is not in their hull.

**Searches for Ξ_Eg = Ξ_T2g = Ξ_face1 = 0 in 𝒮 (U, E1).**
- **Explicit laws (`scanU.out`).** 98 laws (terraces, Zz zigzags, G(b), Gw, drop-to-floor), m = 0.1: Ξ_face1 < 0 for all 98.
  - Terraces have K₆ < 0 (the row's own term is positive, up to +1.5e-4), but their axis rows are −1e-3 to −6e-3.
  - Zigzags have positive axis rows but K₆/128 ≈ 5e-4 to 2e-3.
- **Terraced zigzags (`tzscan.out`).** These add flats (f = 0) at the valley and peak levels to put K₆ < 0 weight where the zigzag sits. TZ(b, V, A, lv, lp): b ∈ {0.6, 1.0}, valley V ∈ [0.2, 0.6], amplitude A ∈ [0.04, 0.3], flat lengths lv ∈ [0, 0.25], lp ∈ {0, 0.06}, turn width 0.02. That is 360 laws at m = 0.1 and 0.01. Of these, 71 (m = 0.1) and 80 (m = 0.01) have both axis rows ≥ 0. Their largest Ξ_face1 is −2.30e-4 and −2.08e-4, and no law has Ξ_face1 ≥ 0. Flats at the valley did not help in this family.
- **Free-segment optimizers (`opt4_*.out`, `opt5_*.out`).** These are R16-9's P(N) family at m = 0.1, b = 0.6 and 1.0: N = 16 with 8 starts each (`opt4`), and N = 24 with 2 starts each (`opt5`, stopped early). The max-min and least-squares searches converge to gentle laws with all three rows ≈ −1e-4 to −2e-4, which is Theorem B″'s side. No start reached min(Eg, T2g, face1) ≥ 0.
- **Slope-resolved occupation-measure search (`relaxTT*.out`).** This uses R16-9's `relaxed_pathU4` constraints: coarea per visited level bin, σ ≤ k, edge mass π − b, slopes {0, 0.2, …, 1}, 40 levels. It maximizes Ξ_face1 subject to Ξ_Eg ≥ 0, Ξ_T2g ≥ 0, with exact gradients and 5–8 starts per cell.
  - Cells: b ∈ {0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4}, hi ∈ b + [0, 1.5], s_min = 0.15 (also 0.05), m = 0.1 and 0.01.
  - **46 cells had an axis-feasible point. In every one, max Ξ_face1 < 0.** The largest was −1.21e-4 (m = 0.01, b = 0.6, hi = 0.7). At m = 0.1 the largest was −1.47e-4 (b = 0.8). The optimum is usually interior (Ξ_Eg, Ξ_T2g ≈ +1e-3).
  - 74 cells had no axis-feasible point at all.
  - **Finer grid (`relaxTT_L.py`, 80 levels, 11 slopes {0, 0.1, …, 1}; two cells, stopped after the first cell of each run to respect the 10-min limit).** m = 0.01, b = 0.6, hi = 0.65 gives max Ξ_face1 = **−1.12e-4**. m = 0.1, b = 0.3, hi = 0.6 gives −2.39e-4, attained at Ξ_Eg = Ξ_T2g = 0 to 1e-13, with μ_E = +2.9e-4. Refining the grid moved the best value by about 8% and did not change its sign.
  - This search is **not a relaxation**: slope quantization is an inner approximation, as R16-9 said of its U4 search (`C5_R16-9_report.md:192`).
- **Mechanism (reading).** The axis rows need fast low-lying pair states. That is a(t) = 2tμ₂ > 1, R16-9's fast-state reading (`C5_R16-9_report.md:123-137`). Fast states at a few low levels make the f-distribution two-point-like, and that gives κ₆ > 0 (κ₆ = 16c⁶ for a two-point f = ±c). Making κ₆ < 0 needs flats, f = 0 mass at the same low levels, of about 58–92% weight (three-point window p ∈ (0.079, 0.421)). Those flats lower the axis rows. Pointwise in t, a kurtotic tilt with x = tμ₂ ≳ 0.46 could make the face integrand positive. The coarea and σ ≤ k path constraints, plus the box's Gaussian tail, apparently prevent it from winning in the integral. Not proved.
- **Count.** For U with E1, the four TT speed parameters need **3 shape conditions** (Eg, T2g, K₆). The fourth row (face2 − T2g) vanishes identically. No law was found meeting all three, so the third may need a non-shape knob.

### 3.6 Extension dependence (checked; `ext_e2.out`, `e2rows.out`, `e2_wt.out`)

- **E2 formula (proved).** For symmetric e the first-order term cancels. V_E2 = V₀ + s²V₂ with V₂ = ¼Σ e_ij[nᵢ²f″ᵢf_j − nᵢn_jf′ᵢf′_j], so **Ξ_E2 = Ξ_E1 − ¼⟨V₀V₂/ε³⟩**.
- Checked against an independent direct E2 grid on NN to all printed digits. NN m = 1: E2 face1 +4.428000e-4 against E1 −1.245e-4; E2 face2 +7.996e-4 against E1 −2.289e-4.
- **On 𝒮 laws (m = 0.1, U).**
  - Axis rows: identical under E1 and E2.
  - G(1.0): E2 face1 +2.62e-3.
  - C2 and C: +1.36 and +1.66.
  - R16-3's U zero: E2 face1 **+1.29**, face2 **+3.55**, body +2.72.
  - On the Z1 skeleton E2 face1 = +1.41, +0.70, +0.35, +0.17 for turn width 0.03, 0.06, 0.12, 0.24. It scales as 1/wt and is resolution-stable between 2^14 and 2^15 samples.
- **Reading.** Off the axis, a product-of-legs vertex picks up the edge's f″ at every sharp turn. P-Z needs turn widths ≲ 0.1–0.15 for the axis zeros (`C5_R16-3_report.md:130-139`), so with E2 its off-axis graviton cone is shifted at O(1) in lattice units, about 10³ times the axis corner values. E2-type vertices were not grid-checked on 𝒮 laws (Laplace evaluator only; NN grid-checked). Which extension is physical is a law datum. E1 and E2 are two examples, not an exhaustive fork.

### 3.7 (c) The LV tadpole (proved from refereed lemmas; checked)

- **Separate, and not shape-tunable.** Lemma Tad: ρ = ⟨ε⟩/2, p_U = ⟨Σf²/ε⟩/6, p_M = ⟨Σg/ε⟩/6 (`C5_R11-3_report.md:108-115`). Pointwise ε/2 + Σf²/(6ε) ≥ ε/2 > 0, and likewise for M because Σg ≥ 0 on 𝒮. That is Corollary P in its refereed scope: "every positive dispersion for U, and every band with nonnegative spatial kinetic contribution for M" (`C5_R11-3_referee_verdict.md:41`). So **ρ + p ≥ ρ > 0 for every law in 𝒮**, and no edge shape, tuned or not, zeroes the tadpole row in the supplied vacuum.
- **Not fixed by the speed rows.** They are degree-2 shape conditions; the tadpole is degree 0. At linear order it is an independent renormalization condition (`C5_R11-3_referee_verdict.md:47`), paid by the trace counterterm c_h∫h_ii (*stipulated*), by exact signed pairing, or by the empty vacuum. Radiative stability of that counterterm was not checked here. R11-3's referee notes that neither a nonlinear completion nor radiative stability is supplied (`C5_R11-3_referee_verdict.md:47`).
- **Numbers (checked, `tadpole.out`; per real scalar, lattice units):**

  | law | m | ρ | ρ + p_U | ρ + p_M | w_U | w_M |
  |---|---|---|---|---|---|---|
  | M zero | 0.1 | 0.4703 | 0.6041 | 0.6251 | 0.285 | 0.329 |
  | M zero | 0.01 | 0.4675 | 0.6021 | 0.6233 | 0.288 | 0.333 |
  | U zero | 0.1 | 0.4762 | 0.6107 | 0.6331 | 0.283 | 0.329 |
  | U zero | 0.01 | 0.4734 | 0.6088 | 0.6312 | 0.286 | 0.333 |

  Each is about 10¹²³ ρ_Λ at a = ℓ_P (R11-3's scale, comparator).

### 3.8 (d) v_max and raw tails (checked; `tadpole.out`, `evalzeros.out`)

No law met every row, so there is no single resulting law. Values for the zero laws used:

| law | v_max (m = 0.1 / 0.01) | max\|σ′\| | \|ε₁₂₈\| | \|ε₂₅₆\| | \|ε₅₁₂\| | \|ε₁₀₂₄\| |
|---|---|---|---|---|---|---|
| R16-3 M zero (m = 0.1) | 0.998293 / 0.999983 | 1.000000000 | 3.67e-5 | 3.85e-7 | 4.87e-8 | 1.39e-10 |
| R16-3 U zero (m = 0.1) | 0.998293 / 0.999983 | 1.000000000 | 3.76e-5 | 4.03e-7 | 7.96e-8 | 1.70e-10 |

Nothing is subtracted. These are R16-3/R16-9's tails; zeroing the off-axis row would need further edge structure (flats at low levels, §3.5), which this probe did not realize.

### 3.9 (e) The bill in R13-8's P,T-even rows (reading; conditional)

| R13-8 row (`vR13-8:15`) | R16-9 | **this probe (U, E1)** | basis / status |
|---|---|---|---|
| charged-matter speeds | 3 / 7 | 3 / 7 | per (spin, \|q\|) class / per species; R16-2 conditional |
| graviton speed + axis anisotropy (Eg, T2g) | 2 shape | 2 shape | per scalar edge, per vertex (`vR16-3:13`) |
| two off-axis anisotropies | 2 (not computed) | **1** (face2 ≡ T2g, proved; the K₆ row is the one condition) | shape if achievable; no law found → likely a non-shape knob (q²-dependent TT seagull, i.e. a Ward-defect counterterm, `C5_R9-9_report.md:55`; or the E1/E2 vertex datum) |
| E_g shear mass μ_E | 1 non-shape | 1 | R16-9 (OPEN, `vR16-9:3`) |
| T₂g shear mass | 0 | 0 | V3's coupling (`vR13-8:22`) |
| LV tadpole | 1 (not computed) | **1, proved never shape-zeroable** | trace counterterm, stipulated |
| CC | 1 | 1 | |
| **total** | 9 + CC / 13 + CC | **8 + CC per class / 12 + CC per species** | conditional bookkeeping |

- **With M:** the off-axis rows are undefined (Lemma M), and M is non-local on the axis too.
- **With E2:** face2 ≠ T2g (NN: +8.0e-4 against −2.3e-4), so 2 off-axis conditions remain (9 + CC). The zigzag edges then carry O(1) off-axis shifts.
- **Precision:** every gravity row at ~1e-13 relative (`C5_R16-3_report.md:276`); charge rows at ~1e-16.

### 3.10 (f) The shear-row certificate (not completed; done without R16-13's report)

- **Not attempted to completion.** The FIXED clause needs an outward-rounded enclosure of min μ_E over Lemma R_U's set (per-level (M, P, Q), coarea, Cauchy–Schwarz, σ ≤ k), uniformly in continuous b, lo, hi, s_min and m ∈ [0.01, 0.1], subject to Ξ_U,Eg = Ξ_U,T2g = 0. Every functional is cubic in moments that are linear in about 150 variables per cell, so the problem is nonconvex. Fixed-multiplier Lagrangian bounds would themselves need a global nonconvex minimization.
- **What a certificate needs (suggested).** Either:
  - interval branch-and-bound over the cell parameters, with verified bounds on the cubic t-integrals; or
  - a moment-SOS relaxation of the level × slope measure with verified SDP rounding.

  I estimate both at hours of work.
- **Reframing (reading).** If the full graviton cone (all four TT rows) is the target, the search in §3.5 suggests that for U with E1 no full-cone zero exists in 𝒮. The shear row is then moot on the shape route, and the R16-9 question narrows to axis-only zeros, as registered.
- **Reading for (f): OPEN.** Neither CERTIFIED-CONFLICT nor JOINT.

---

## 4. Against the FIXED readings (`TESTS:5837-5841`)

**Worker reading; referee required.**
- **COUNTED-ROWS: met in part, by its second clause, for the U vertex with E1.** Proved and checked: Ξ_face2 ≡ Ξ_T2g for every law in 𝒮, so that off-axis row vanishes identically given the axis zeros. The TT speed block is then 3 shape conditions (Eg, T2g, K₆), not 4.
- **The remaining off-axis row (K₆): OPEN, with a suggested CONFLICT.**
  - No law found has Ξ_Eg = Ξ_T2g = 0 with Ξ_face1 = 0: 98 explicit laws, 360 terraced zigzags, two optimizers, and 46 axis-feasible cells of a slope-resolved search, max Ξ_face1 = −1.12e-4 (finer grid).
  - This is a search, not an enclosed superset, so it does not meet CONFLICT. R16-9's analogous scans were read OPEN (`vR16-9:3`).
  - The first clause (an explicit law with all rows zero) is not met.
- **Tadpole row:** a separate condition, and no shape zeroes it (proved, from refereed R11-3 lemmas).
- **M vertex:** no clause applies. Its off-axis rows are undefined, and its axis T₂g amplitude is non-local on doubler-free laws (Lemma M, proved).
- **(f):** OPEN. Neither CERTIFIED-CONFLICT nor JOINT.

**Expectation check.**
- The expectation was "COUNTED-ROWS with two further shape conditions; main alternative a CONFLICT inside separable 𝒮" (`TESTS:5842-5844`).
- Instead there is **one** further condition for U (one row vanishes identically), and that condition looks unmeetable with the axis zeros in 𝒮 (suggested, not certified).
- The prior no-go's changed hypothesis (q off-axis) does matter. It exposes two things the axis computation could not see: a sixth-cumulant row, and a vertex-extension datum.
- For (f) the expectation "CERTIFIED-CONFLICT for M" is moot, because M is non-local (Lemma M).

## 5. Prices (named, not adopted)

- **P-K6 (new, conditional on U with E1).** The off-axis TT cone needs ⟨K₆(f)/ε⁷⟩ = 0, a sixth-cumulant condition on the scalar edge's velocity distribution. It is one tuning to ~1e-13. If shape cannot meet it with the axis zeros (suggested), it needs a non-shape knob: a q²-dependent TT seagull (Ward-defect counterterm) or a vertex datum. Axiom cost: none; downstream dynamics (`AX:114-123`).
- **P-TTV₂ (refines P63(iii)).** The vertex is a law datum, and so is its O(q²) off-axis extension (E1 against E2 change the off-axis rows by O(1) on P-Z edges). Source/action gate `AX:187`.
- **P-LocM (new).** Keeping R9-9's M vertex on a doubler-free edge costs a non-summable stress kernel (Lemma M). Equivalently, M is excluded as a local law, and only U-type vertices with f(π) = 0 remain.
- **P-Tad (sharpened).** The LV tadpole is never shape-zeroable in the zero-point vacuum. One trace counterterm (stipulated), exact signed pairing, or the empty vacuum.
- **Inherited:** P-Z (R16-3), P73 (R16-2), R16-9's shear knob, the assumed W1, the supplied vacuum, and the bare-cone scope.
- **No axiom text changes.**

## 6. Strong-word and rule check

- **"Proved"** is used only for:
  - the off-axis expansion and its two IBP forms (§3.2);
  - Lemma M;
  - the U identities (face2 ≡ T2g, the face1/K₆ formula, the body formula via the O_h relation);
  - the E2 correction formula;
  - the continuum control;
  - tadpole positivity (from refereed R11-3 lemmas).
- **"Checked"** is used for every number: Laplace-separable evaluation, a direct 3D grid on NN, random O_h tensors, and re-solved Newton zeros.
- **"Every / never / identically":**
  - "every law in 𝒮" appears in the proved identities and in tadpole positivity;
  - "never shape-zeroable" applies to the tadpole only;
  - "all 98 / every one of 46 cells" are search statements about my runs.
- **Not claimed:**
  - CONFLICT for the K₆ row;
  - any certified bound;
  - Dirac/photon/gluon rows;
  - W2 (standard or deformed);
  - dressed poles;
  - non-separable laws;
  - the physical choice between E1 and E2.
- **Round-17 rules:** v_max is given for every law used (§3.8); the gauge-symbol v_max is stated only as a bound (§1); the counting basis is stated (§3.9); the tadpole counterterm is stipulated; the control is physical (§3.4); forks are not exhaustive (§3.6); the changed hypothesis is named (§4).

## 7. For the referee

1. §3.2's expansion (ε₊ε₋(ε₊ + ε₋) to O(s²)) and the two IBP forms. The direct-grid agreement (≤ 1.1e-10) is for U on NN.
2. Lemma M: the C₂ᵧ covariance of a pair amplitude at q → 0, and whether continuity (summability) is the right locality requirement.
3. The U identities (§3.4): the parity reductions and the single-variable IBP (f periodic, f(π) = 0).
4. The R16-3 U zero's Ξ_face1 = −8.94e-4. It is reproduced by the derivative-free moment form on a 3D grid (−8.957e-4 at N = 720). A direct Π(0, q) finite-difference check needs q ≪ wt = 0.03 and N ≫ 700; I did not do it.
5. Whether a certified bound on max Ξ_face1 at {Ξ_Eg, Ξ_T2g ≥ 0} is reachable. The functional is a cubic t-integral of moments; the coarea and σ ≤ k constraints are as in R16-9.
6. The E2 numbers on 𝒮 laws (Laplace only; the f″ spikes scale as 1/wt).

## 8. Files (`S/scripts/`)

- **Copied unmodified** from `P/scripts/C5/R16-3/`: `zz.py`, `laws.py`, `floor_scan.py`, `simul2.py`.
- `basis.{py,out}`: O_h on-shell TT rank and the body relation.
- `offaxis.py`: general E1 evaluator (sympy expansion plus Laplace moments).
- `validate.{py,out}`: axis recheck and the direct 3D grid. Its main block was wrapped in `if __name__ == "__main__"` after the run, for import; the logic is unchanged.
- `dbg.py`: diagnosis of the M mismatch (discontinuous integrand).
- `fastU.py`: U rows from five moments, plus K₆ and μ_E.
- `evalzeros.{py,out}`: U zeros re-solved, corners.
- `scanU.{py,out}`: 98-law scan. `tzscan.{py,out}`: terraced zigzags.
- `opt4.py`, `opt5.py` → `opt4_*.out`, `opt5_*.out`: free-segment searches. `opt5` was stopped early; its partial outputs are kept.
- `relaxTT.py`, `run_relax*.sh` → `relaxTT_*.out`: slope-resolved search. `relaxTT_L.py` → `relaxTT_L80_*.out`: the finer grid, partial (killed at about 7 min).
- `tadpole.{py,out}`: ρ, p, v_max and tails.
- `grid_mom.{py,out}`: 3D grid of the moment form on the U zero. `grid_face.{py,out}`: 3D grid of the f′ form (unresolved; kept for the record).
- `ext_e2.{py,out}`: direct E2 grid on NN. `e2rows.{py,out}`: the E2 correction formula. `e2_wt.{py,out}`: turn-width scaling.
