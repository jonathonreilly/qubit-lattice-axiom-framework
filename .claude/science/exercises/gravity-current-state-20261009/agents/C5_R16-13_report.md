# C5 R16-13 report: fermion zero-point loops in the graviton cone and the shear — does their sign lift R16-9's conflict?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-12 23:48Z to 2026-10-13 00:55Z. No repository file was edited. No downloads, no web lookups.

**Scratch.** `S/` = `.../scratchpad/C5/R16-13/`. Scripts and `.out` files are in `S/scripts/`. Every run used `OMP_NUM_THREADS=2`. Most took under 4 min; `content6.py` (3 + 1) took 8.7 min. One 5-knob solve (`content5.py`) ran 13.6 min wall, above the 10-minute limit, with two jobs sharing the CPU. Its twin was stopped unfinished (`root5_4_22.out`).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: C5 method and readings (`:2302-2320`), round 16 (`:5037-5592`), my item (`:5593-5613`).
- Reports and verdicts:
  - `agents/C5_R16-9_report.md`, all. Its referee verdict appeared during the run (`scratchpad/C5/ref_R16-9/R16-9_referee_verdict.md`, `vR16-9`): **NOT CONFIRMED, reading OPEN**.
  - `C5_R16-3_report.md` and verdict (`vR16-3`).
  - `C5_R14-3_report.md:1-140` and verdict (`vR14-3`).
  - `C5_R13-5_report.md` and verdict (`vR13-5`).
  - `C5_R11-1_report.md` and verdict (`vR11-1`).
  - `C5_R9-9_report.md` and verdict (`vR9-9`).
  - `C5_R9-2_report.md:200-260`.
  - `C5_R10-5_report.md:185-240` and verdict (`vR10-5`).
- Scripts: `scripts/C5/R10-5/r105_tt_paired.py`, `scripts/C5/R16-1/{sublum,r161_laws}.py`, `scripts/C5/R16-3/{zz,laws,floor_scan}.py`. These were copied unmodified into `S/scripts/`.

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **The Dirac vertex and its identity (proved; checked).** I extended R10-5's vielbein vertex to any Dirac band, Wilson bands included, and proved a one-line identity for the fermion's graviton-cone shift (§3.2):
   - **Ξ_F = (N_c/8)⟨|G|²(|∂_z c|² − 1)/E³⟩ − (N_c/32)⟨|V|²(5v_z² − 1)/E⁵⟩.**
   - The second term is −N_c times the scalar formula of R16-3 on the fermion's band.
   - The first term (the "a-term") is new for non-unit-speed bands. It is ≤ 0 whenever |∂_z c| ≤ 1, which every D1 edge satisfies.

   The strain shear mass flips sign exactly: μ^F = −N_c μ^s[E] (stipulated universal flow).
2. **Signs (checked).** On R14-1's D1(1.4, r), a 4-component Dirac sea pushes the graviton cone **out** in both polarizations and gives a **negative** μ_E:

   | quantity (m = 0.01, r = 0.3) | value per Dirac field |
   |---|---|
   | Ξ_T2g | +5.46e-3 |
   | Ξ_Eg | +2.83e-3 |
   | μ_E | −2.95e-2 |

   All three have the sign opposite to a gapped (G-type) scalar. So fermion μ_E does have the opposite sign, as the item expected.
3. **New row: Wilson-Dirac seas give a T₂g shear mass (proved mechanism; checked).** For a separable scalar, μ_T2 = 0 (R9-2's Liouville argument). The 4-component Wilson mass m + ΣW(k_j) couples the directions. So the T₂g strain flow has divergence W′(k_x)W′(k_y) ≠ 0, and μ_T2 ≠ 0:
   - D1 edges: 1e-6 to 1e-5;
   - Dirac edges with flats: up to 5e-2.

   R16-9's count row "μ_T2 = 0 at one loop" (`R16-9_report.md:224`) fails once Wilson fermions are included (the R16-9 referee already flagged it as coupling-specific).
4. **A common zero exists, in a non-SM content (checked).** The content (§3.4, `root6_2_2_1.out`, `verify_root6.out`):
   - 2 real scalars on R14-1's G(2.5647);
   - 2 real scalars on R14-3's G_w(1.7406, 0.7413);
   - 1 four-component Dirac field on D1(1.3133, r = 0.5731).

   It has Ξ_T2g = Ξ_Eg = μ_E = 0 at the common mass m = 0.01. The residuals are ≤ 6e-14 at solver resolution and ≤ 3.7e-6 at higher resolution, against per-species scales of 1e-3 to 3e-2.
   - **Subluminal on every edge.** The scalars have |σ′| ≤ 1 (class 𝒮), with whole-zone v_max 0.999998 and 0.999995. The Dirac edge has r < 1/√3, so v_max ≤ 1 by Lemma V1.
   - **The count is 3 continuous edge tunings** (b₂, b_f, r). The (b₂, b_f, r) Jacobian is nonsingular (det 6.8e-8), and a 3-knob re-solve from a perturbed start returns the same root.
   - **Light mass.** Re-solved at m = 0.001 with the same three knobs (r = 0.5758, still below 1/√3 = 0.57735).
5. **The lift has four caveats (checked).**
   - **μ_T2 ≠ 0 at the root:** its total is −3.5e-5 (m = 0.01) and −3.9e-5 (m = 0.001). This is a 4th condition the FIXED readings do not list; zeroing it needs a 4th tuning (not attempted).
   - **The four scalars sit on two different edges.** A Higgs doublet's components would share one edge. With **one** scalar edge (4 + 1) every solve stalled at r = 1/√3, with residuals ~1.5e-4.
   - **SM counts were not reached.** With 4 scalars + 22.5 Dirac fields, residuals are ~1e-2. The fermion birefringence, Ξ_F,T2g − Ξ_F,Eg ≥ +2.6e-3 per Dirac field in every Dirac law tested, times 22.5, exceeds what 4 scalars offset.
   - **r is near the cap:** 0.7% below 1/√3 at m = 0.01 and 0.27% below at m = 0.001.

**Against the FIXED readings (`TESTS:5609-5611`): LIFTED (worker reading), on the letter, with the caveats above.**
- **LIFTED** asks for an explicit mixed-species content, all edges subluminal, E_g = T₂g = μ_E = 0 at a common light mass, checked, with the count. All of that is met, with count 3.
- **The physically relevant version is not shown.** That would be SM content with one Higgs edge, and μ_T2 = 0 as well. It stays OPEN.
- **Expectation** ("LIFTED with one more tuning", `TESTS:5613`): met in count. R16-3's 2 cone tunings plus 1 edge parameter (r or b_f) replace R16-9's non-shape shear knob. But it needs a content with two scalar edges, and it leaves μ_T2.

---

## 1. Hypotheses, class and stipulations (stated before any title)

- **Scalar edges.** R14-3's separable class 𝒮: ε² = m² + Σg(k_i), g = σ², |σ′| ≤ 1. Families used:
  - R14-1's G(b);
  - R14-3's G_w(b, w);
  - R16-3's convex mix of A = G(1.0), C2 = Zz(1.0, 0.35, 0.47, 0.03) and C = Zz(1.0, 0.35, 0.43, 0.03).

  Vertex: R9-9's M (main) or U (one run). The supplied zero-point vacuum is +ε/2 per real scalar.
- **Dirac edges.** These are 4-component Wilson bands h = Σs(k_j)α_j + (m + ΣW(k_j))β, E² = Σs_j² + (m + ΣW_j)², with s odd and s(π) = 0:
  - **D1(b, r):** R14-1's, as coded in R16-1's `r161_laws.py`. s is R13-4's odd symbol S(b), and W′ = r√(1 − s′²).
  - **DG(b, w, r):** s′ = 1 − sstep((k−b)/w) − sstep((k−k₂)/w), with k₂ = π − b − w. This is D1 with a flat (s′ = 0) plateau of length π − 2b − 2w.
  - **DZ(b, ℓ, n_z, w_t, r):** D1 with n_z zigzag segments (s′ = ∓1, length ℓ, turns of width w_t) after the box.

  In all three, W′ = r√(1 − s′²) and a mirror box s′ = −1 on [π − b, π]. The doubler at π is lifted by W_π.
  - The 8-component Clifford-flat realization (R10-5) is used only as the calibration control.
- **TT vertex: stipulated (vertex V0).** R10-5's Clifford-index vielbein (`C5_R10-5_report.md:195`), extended to 4-component Wilson bands:
  - T₂g: Γ = ½(s(k_x)α_y + s(k_y)α_x).
  - E_g: Γ = ½(s(k_x)α_x − s(k_y)α_y).
  - q ∥ z. Γ depends only on k_⊥, and the Wilson mass term does not couple to TT. That last choice is a stipulation; the Wilson-coupled variant G_β ∝ R_xR_y is coded (`dirac.py`, `lamW`) but was not run.
  - This is the "Belinfante-symmetrized lattice stress" of the item, in vielbein form, at q ∥ axis.
- **Ward requirement.** Standard first-order W1, assumed. R13-5's Lemma P1 builds the scalar pair-channel completion; its fermion version is "argued, not run" (`C5_R13-5_report.md:181`). No second-order identity, standard or deformed, is used.
- **Shear (stipulated, SF).** R9-2's universal strain flow dk/de = ½h·p with p = ∇(E²/2) (`C5_R9-2_report.md:221-226`), applied to each species' vacuum energy per mode:
  - +ε/2 for a real scalar;
  - −(N_c/2)E for an N_c-component Dirac sea.

  So μ^F = −N_c μ^s[E]. This is R14-3's "Dirac-sea reading (−ε) multiplies μ_E by −2" (`C5_R14-3_report.md:57`) per negative-energy state. General (non-separable) form, derived here from R9-2's Liouville formula μ = −⟨(div v)(v·∇ε_vac)⟩:
  - μ_E^s = −(1/8)⟨(H_xx − H_yy)(p_x² − p_y²)/ε⟩;
  - μ_T2^s = −(1/2)⟨H_xy p_x p_y/ε⟩;
  - H = Hess(ε²/2).
- **Vacuum.** Supplied zero-point / filled sea, one loop. In the empty Fock vacuum, every quantity here is 0.
- **Meaning of Ξ.** The bare-cone shift, not the dressed split (`vR9-9` item 5).
- **Masses.** m = 0.01 (main), 0.03, 0.1, 0.3. One common mass for all species.
- **Round-16 head rules (`TESTS:5039`).**
  - Whole-zone v_max: stated for every law used in a solve (§3.5).
  - Frame-tied kernels: none introduced.
  - Ward statements: standard W1, assumed.
- **Excluded:**
  - exact pairing (P46);
  - deformed W2;
  - the photon and gluon loops (optional in the item; no vector TT vertex was built, so not computed);
  - q off-axis;
  - two loops;
  - matter-side graviton-loop shifts.

## 2. Prior art (each counted once)

- **R10-5 Theorem PT** (`C5_R10-5_report.md:191-235`; `vR10-5:2`, algebra confirmed, vertex stipulated). The Clifford-flat 8-component fermion vertex, and Ξ_B + Ξ_F = ⟨g(|c′|² − 1)/E³⟩. My identity contains PT's fermion part as the N_c = 8 separable case.
- **R11-1 Theorem N\*** (`vR11-1:3`). Fermion TT weights have positive totals and boson weights negative ones. Interval cancellation needs both statistics with matched measures. Its 𝒞_A holds only unit-speed Clifford-flat fermions (`C5_R11-1_report.md:73-79`); class (D) is excluded (`:93`).
- **R16-3** (`vR16-3`). The v_z form Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩ (`C5_R16-3_report.md:109`), and the scalar E_g/T₂g zero at μ_E = +6.0e-3 to +6.6e-3.
- **R16-9** (`vR16-9`: NOT CONFIRMED, OPEN). No scalar edge in 𝒮 was found with Ξ_Eg = Ξ_T2g = μ_E = 0; the best was μ_E = +1.255e-3. Named gap P-R16-9b: no Dirac or photon TT/shear vertex (`R16-9_report.md:231-235,273`).
- **R14-3** (`vR14-3`). The K₄ form of μ_E, the G_w shear root (w* = 0.344371 at m = 0.01), and Theorem B.
- **R13-5** (`vR13-5:15-19`). Pairing cancels the stipulated TT response and leaves 2κm²J₂.
- **R9-2.** The strain-flow method; μ_T2 = 0 by Liouville for separable bands (`C5_R9-2_report.md:227`).
- **Repo grep.** I searched the packet's agents and TESTS for "a-term", "Wilson-Dirac shear", "μ_T2" and "fermion shear". The only fermion TT vertex is R10-5's (Clifford-flat). The only fermion shear statement is R9-2/R14-3's −2× remark. No Wilson-fermion TT identity and no Dirac μ_T2 exists in the chain.

---

## 3. Results

### 3.1 Rechecks of archived runners (checked; `validate.out`, `scan_dg.out`)

- **Dirac evaluator vs R10-5.** I used a general N_c pair-weight evaluator with R10-5's exact grid-shift method. On R10-5's 8-component control (sin k, ½(1 − cos k)) at m = 0.3, N = 96 and 160:
  - α_F = +0.03588, Ξ_F = −0.004195, as `r105_tt_paired.out` (all printed digits).
  - The closed form of my identity gives −0.004195 (T₂g) and −0.013653 (E_g), equal to the evaluator.
- **Strain formula vs V3.** The NN scalar at m = 1 gives μ_E^s = +1.9703886419e-3 at N = 64 and 96 (V3: +1.97038864e-3); μ_T2^s = 0.
- **zz.py (R16-3) on R14-3's G_w(1.4, w) at m = 0.01.** μ_E(w = 0.3444) = +5.4e-8, consistent with R14-3's root w* = 0.344371 (`vR14-3:2`). G(1.4) gives μ_E = +4.338e-3, Ξ_M,T2g = −1.689e-3, Ξ_M,Eg = −8.49e-4.

### 3.2 (a) The Dirac TT vertex and its IBP identity

**Theorem DT (proved).**
- **Hypotheses.**
  - h(k) = c(k)·γ with Clifford generators γ_a ({γ_a, γ_b} = 2δ_ab), N_c components, E = |c| > 0.
  - Vertex Γ = G·γ with G real and independent of k_z, and c·G independent of k_z. This holds for V0 on every band above: c·G = s_x s_y (T₂g) or (s_x² − s_y²)/2 (E_g).
  - Π_F(ω, q) = −⟨2t(k, k+qẑ)(E+E′)/((E+E′)² − ω²)⟩ + seagull, with t = tr[P₊(k′)ΓP₋(k)Γ].
- **Then:**

  Ξ_F := (∂_{q²} + ∂_{ω²})Π_F = (N_c/8)⟨|G|²(|∂_z c|² − 1)/E³⟩ − (N_c/8)⟨(c·G)²(5v_z² − 1)/E⁵⟩, with v_z = ∂_zE.

  Equivalently, with |V|² := 4(c·G)² (= 4s_x²s_y² for T₂g, (s_x² − s_y²)² for E_g) and A_zz = Hess_zz(E²/2) − 1, the second term is −(N_c/32)⟨|V|²A_zz/E⁵⟩ (A-form).

**Proof.**
1. **Pair weight.** Use Γγ_bΓ = 2G_bΓ − |G|²γ_b and tr γ_a = 0. Then t(k, k′) = (N_c/4)[|G|²(1 + ĉ·ĉ′) − 2(ĉ·G)(ĉ′·G)], with ĉ = c/E.
2. **β.** β = −⟨2t₀/(2E)³⟩ = −(N_c/8)⟨|G|²/E³ − (c·G)²/E⁵⟩.
3. **α.** Set φ(a, b) = 2t/(E_a + E_b) along k_z, which is symmetric. Periodicity gives ⟨∂_b²φ⟩ = −⟨∂_a∂_bφ⟩ at a = b, so α = ½⟨∂_a∂_bφ⟩.
4. **The derivatives.** ĉ·ĉ′ = 0 and |ĉ′|² = (|c′|² − E′²)/E². With c·G independent of k_z:
   - t_a = (N_c/2)(c·G)²E′/E³;
   - t_ab = (N_c/4)[|G|²(|c′|² − E′²)/E² − 2(c·G)²E′²/E⁴].

   Substituting gives α = (N_c/8)⟨|G|²|c′|²/E³ − 5(c·G)²E′²/E⁵⟩.
5. **Sum.** α + β gives the statement. The A-form follows from Theorem T's total derivative ∂_z(∂_zE/E⁴) (`vR9-9` item 2), which holds for any band, separable or not. ∎

**Normalization.** Fixed against the scalar by the static first-order energy: both give δE = −h·(s_x s_y)/E in the continuum. This is the same convention R10-5's paired cancellation used. The N_c = 8 separable case is exactly R10-5's PT fermion part (§3.1).

**Checks** (`d1_run.out`, `dfam_check.out`). The independent grid-shift α + β agrees with the identity:
- D1(1.4, 0.3), m = 0.3: shift method +5.0604e-3 (N = 144), A-form +5.0638e-3 (N = 192).
- DG(1.0, 0.25, 0.3), m = 0.3: T₂g +8.1928e-4 (shift) against +8.1941e-4 (GL quadrature); E_g −3.56367e-3 against −3.56347e-3.
- DG(0.8, 0.5, 0.5): T₂g −5.7396e-4 against −5.7395e-4.

**Reading.**
- The fermion term is not simply "−N_c × scalar". The a-term is a fermion-only, boson-sign piece: a slower graviton whenever the 1D velocity norm |∂_zc| < 1.
- On D1, |∂_zc|² = s′² + r²(1 − s′²) < 1 wherever |s′| < 1. Every D1 edge has such points, because s must return to 0 at π.

**Shear for Dirac seas (proved under SF).**
- μ_E^F = −N_c μ_E^s[E] and μ_T2^F = −N_c μ_T2^s[E].
- For the 4-component Wilson band, div v_T2g = H_xy = W′(k_x)W′(k_y), which is not identically zero. So μ_T2^F ≠ 0 generically.
- It is zero for separable (Clifford-flat 8-component) bands, where H_xy ≡ 0.

**Lemma V1 (proved): subluminality of Wilson-Dirac edges.**
- **Statement.** If |s′| ≤ 1 and s′² + 3W′² ≤ 1 pointwise (so r ≤ 1/√3 for W′ = r√(1 − s′²)), then |∇E| ≤ 1 on the whole zone, for every m ≥ 0.
- **Proof.** With M = m + ΣW_j, Cauchy–Schwarz gives (s_js′_j + MW′_j)² ≤ (s_j² + M²/3)(s′_j² + 3W′_j²) ≤ s_j² + M²/3. Summing over j gives |∇E|² ≤ (Σs_j² + M²)/E² = 1. ∎
- This covers D1, DG and DZ for any s-profile. Sampled v_max for the laws used is in §3.5.

### 3.3 (b) Signs and sizes on D1 (checked; `d1_run.out`)

Values per 4-component Dirac field, V0 vertex, uniform grid N = 192 (convergence N = 96/144/192 in the `.out`; μ_E moves 1.2% from 144 to 192):

| law | m | Ξ_T2g | Ξ_Eg | a-term | μ_E^F | μ_T2^F |
|---|---|---|---|---|---|---|
| D1(1.4, 0.3) | 0.3 | +5.064e-3 | +2.582e-3 | −8.13e-4 | −2.79e-2 | +4.4e-7 |
| D1(1.4, 0.3) | 0.01 | +5.464e-3 | +2.831e-3 | −8.53e-4 | −2.95e-2 | −1.16e-6 |
| D1(1.4, 1/√3) | 0.3 | +5.103e-3 | +2.688e-3 | −5.83e-4 | −2.71e-2 | +1.54e-5 |
| D1(1.4, 1/√3) | 0.01 | +5.629e-3 | +3.019e-3 | −6.20e-4 | −2.91e-2 | −1.28e-5 |

**Signs.** Against a G-type scalar (G(1.4), m = 0.01: Ξ_M = −1.69e-3 / −8.5e-4, μ_E = +4.34e-3), the D1 fermion has the **opposite sign in all three** (checked). Against R16-3's scalar cone zero (Ξ_s = 0, μ_s ≈ +6e-3), the fermion μ_E is opposite as needed. But the fermion's Ξ is not zero, so adding it moves the cone.

**DG and DZ families** (`scan_dg.out`, `dz_scan.out`; GL quadrature, 36 + 6 laws at m = 0.01).
- Every sign of Ξ_T2g, Ξ_Eg and μ_E^F occurs. Examples:
  - DG(0.6, 0.1, 0.1): Ξ_T2g = −9.4e-3;
  - DG(1.2, 0.2, 0.3): Ξ_Eg = +5.5e-5;
  - DG(0.6, 0.1, 0.5): μ_E^F = +3.8e-2.
- μ_T2^F reaches +4.97e-2 (DG(0.6, 0.1, 0.5)). Flats with W′ = r make H_xy = r².
- **Birefringence.** Ξ_F,T2g − Ξ_F,Eg > 0 in **every** Dirac law tested. The smallest gap is +2.6e-3 (D1(1.4, r)). Zigzag stretches *increase* it: DZ(1.0, 0.15, 4, 0.03, 0.5) gives +4.1e-3.

  So no Dirac law tested has its own cone zero in both polarizations (checked over the tested families; not proved).

### 3.4 (c) Mixed content: the joint zero

Content: N_s real scalars plus N_D 4-component Dirac fields at one common mass m = 0.01. The totals are N_sΞ_s + N_DΞ_F and N_sμ_s + N_Dμ_F. Every solve used `scipy.optimize.least_squares` with box bounds. The knobs are continuous edge parameters; the species counts are fixed.

| run (`.out`) | content | knobs | end point | totals (Ξ_T2g, Ξ_Eg, μ_E) | μ_T2 total |
|---|---|---|---|---|---|
| `root3_4_1_M` | 4 + 1 | G(b_A), D1(b_f, r) | b_A = 1.8807, b_f = 1.2757, **r = 0.5773 (bound)** | (+1.49e-4, −1.76e-4, −1.0e-5) | −4.9e-5 |
| `root4_4_1_M` | 4 + 1 | G_w(b_A, w_A), D1(b_f, r) | same point; w_A at its G end (bound); r at bound | same | same |
| `root4_4_1_U` | 4 + 1 (U vertex) | as above | b_A = 0.439, b_f = 0.561, r at bound | (+1.29e-3, −1.15e-3, +4.0e-5) | +2.5e-3 |
| `solve_4_1_all` | 4 + 1 | G_w + DG(b, w, r) | r and w_f at bounds | (+7.4e-5, −9.6e-5, −5.2e-6) | +9.9e-6 |
| `root_4_1_M` | 4 + 1 | 3-corner scalar mix + DG | v at bound | (+5.2e-5, −8.9e-5, −5.2e-6) | +8.5e-6 |
| `root5_4_1` | 4 + 1 | R16-3 zigzag simplex + DG (5 knobs) | left the simplex; invalid | (−2.2e-3, −2.3e-3, −2.3e-3) | +8.0e-4 |
| `root3_4_22_M` | 4 + 22.5 (SM-like) | G(b_A), D1(b_f, r) | bounds | (+2.3e-2, −3.6e-2, −8.6e-4) | +1.3e-1 |
| `solve_4_22_all` | 4 + 22.5 | G_w + DG | bounds | (+7.8e-4, −4.4e-2, −6.0e-3) | +1.6e-1 |

- **Every 4 + 1 run ends at a bound.** The binding bound is r = 1/√3, exactly Lemma V1's subluminality limit, together with the G end of the scalar family or the narrowest DG step. The residual is about 3% of the per-species Ξ scale.
- **Why it sticks (reading).** For one scalar edge and one Dirac edge, a common zero needs two ratio equalities, which are independent of the counts:
  - Ξ_Eg/Ξ_T2g (scalar) = Ξ_Eg/Ξ_T2g (fermion);
  - μ/Ξ_T2g (scalar) = μ/Ξ_T2g (fermion).

  Then one scale equation fixes the overall size. In the families tried, the fermion's Eg/T2g ratio stays at or below ~0.54 and falls further with flats or zigzags, while the scalar ratio at the matching μ/T2g ratio sits slightly above it. The fermion ratio rises with r, and r is capped by subluminality.
- **SM-like counts (4 + 22.5).** The fermion birefringence must be offset by four scalars. That needs ≤ ~1.4e-3 per Dirac field; the minimum found is 2.6e-3.
- **For one scalar edge, "not found" ≠ impossible.** Each solve is a local optimization in a finite family. Not tried:
  - Wilson-coupled TT vertices (variant VW);
  - several distinct fermion edge families in one content;
  - non-separable scalars;
  - the photon or gluon loops;
  - a superluminal r > 1/√3 (excluded by the item).

**The root: two scalar edges + one Dirac edge** (`content6.py` → `root6_2_2_1.out`; verified in `verify_root6.out`, `resolve_light.out`).

| item | value |
|---|---|
| content | 2 real scalars on G(b₁) + 2 real scalars on G_w(b₂, w₂) + 1 Dirac (4-comp) on D1(b_f, r); M vertex; V0; SF |
| root, m = 0.01 | b₁ = 2.5647270310, b₂ = 1.7406074658, w₂ = 0.7412942016, b_f = 1.3133236385, r = 0.5731174634 |
| per species (Ξ_T2g, Ξ_Eg, μ_E) | G(b₁): (−9.45e-4, −5.48e-4, +1.093e-2); G_w: (−1.810e-3, −8.53e-4, +2.523e-3); D1: (+5.511e-3, +2.801e-3, −2.690e-2) |
| totals at solver resolution | (−3.2e-15, −1.9e-15, +5.6e-14) |
| totals, scalar n = 2¹⁶, ν = 4000; fermion GL (4,10) | (−6.7e-8, −4.1e-8, +3.7e-6) |
| μ_T2 total | **−3.54e-5** (not zero; unlisted row) |
| Jacobian 3×5, singular values | 3.2e-2, 4.6e-3, 1.0e-3 (rank 3) |
| 3-knob block (b₂, b_f, r), b₁ and w₂ frozen | det 6.8e-8; fsolve from a perturbed start returns the same root, residual ≤ 2.5e-14 |
| m-drift at fixed knobs | residual (1.3e-5, 8.2e-6, −4.6e-5) at m = 0.001; re-solved there with the same 3 knobs: b₂ = 1.73634, b_f = 1.31009, r = 0.57581 |
| whole-zone v_max (m = 0.01) | G(b₁) 0.999998, G_w 0.999995 (bisection); D1 ≤ 1 (Lemma V1), sampled 0.999990 |

- A second content, 3 + 1 scalars + 1 Dirac, approached a root with residuals ≤ 7e-7 at r = 0.518 (`root6_3_1_1.out`; nfev cap reached, not converged).
- **The count.** The FIXED conditions are 3, met by 3 continuous edge parameters, each held to roughly 1e-13 relative (R16-3's GW precision argument, `C5_R16-3_report.md:276`; comparator). The other two knobs (b₁, w₂) are law choices that are not fine-tuned (the root moves continuously with them).
- **Adding μ_T2 = 0** makes it 4 conditions and needs a 4th knob (not attempted).
- **Against R16-9's bill** (`R16-9_report.md:229`): R16-9 had 2 shape tunings plus 1 non-shape shear knob. This content has 3 shape tunings, now shared across species, plus the μ_T2 row.

### 3.5 Whole-zone v_max at the one-scalar-edge closest approach (checked; Lemma V1). The root's v_max is in the §3.4 table.

All values from `vmax_close.out`:
- **Scalar G(1.880700).** max|σ′| = 1.000000000, no gapped valley, whole-zone v_max = 0.999996 at m = 0.01 (separable bisection, zz.py).
- **Dirac D1(1.275743, 0.577300).** v_max ≤ 1 (Lemma V1, proved). Sampled lower bounds at m = 0.01: 0.999989 (81³ grid) and 0.999992 (121³ grid). W_π = 0.1646.
- **Tails.** Not computed for these laws. D1's are Gevrey-class (R16-1); DG laws with w_f ≈ 0.005 steps would carry long hopping tails (reading).

### 3.6 (d) Relation to R11-1's N\*: does an untuned cancellation re-enter?

- **N\* itself (refereed)** covers unit-speed Clifford-flat fermions only. There the fermion TT weight is exactly −(scalar form), and interval cancellation forces measure-level pairing (`vR11-1:3`).
- **What Theorem DT adds.** On non-unit-speed bands the fermion carries an extra a-term with the boson sign.
  - **Suggested** (proof sketch for separable Clifford-flat bands with |c′| ≤ 1): the a-term enters with an E⁻³ kernel. Its small-τ Laplace coefficient is (N_c/8)⟨|G|²(|c′|² − 1)⟩ ≤ 0. Vanishing on a mass interval then needs |c′| = 1 wherever |G|² ≠ 0, i.e. the unit-speed case, and N\* applies.
  - For 4-component D1 the mass enters non-affinely (M = m + ΣW), so N\*'s Laplace step does not apply. Interval cancellation is outside every proof here.
- **Reading.** Every cancellation attempted here is a point tuning at a light mass, carried to all light species at O((ma)²) (analyticity as in R16-3/R14-3). It is not an untuned cancellation. Nothing found re-opens an untuned route.
- The only known untuned route is still exact pairing (P46), which the item excludes. Even P46 needs Clifford-flat (separable) fermions to avoid μ_T2, because D1-type Wilson fermions cannot pair the T₂g shear with separable scalars.

### 3.7 (e) Prices (named, not adopted)

- **P-R16-13a (stipulations).** The V0 vielbein TT vertex for Wilson-Dirac fermions and the SF strain flow for Dirac seas. Both are law data (P-TTV, P63(iii)); source/action gate `AX:187`; dynamics downstream `AX:114-130`.
- **P-R16-13b (new row).** A Wilson-Dirac sea carries a T₂g shear mass μ_T2^F ∝ ⟨W′_xW′_y p_xp_y/E⟩ ≠ 0. Removing it costs one more tuning per Wilson-fermion edge, or the Clifford-flat 8-component realization (an enlarged site fibre against `AX:47`, as R11-1's P42).
- **P-R16-13c (the lift's bill).** In V0 + SF, the scalar conflict lifts by mixing species:
  - 3 continuous edge tunings at ~1e-13 each;
  - a content with two scalar edge families, which is not the SM Higgs doublet;
  - a Wilson-Dirac edge within 0.3–0.7% of the subluminal cap r = 1/√3;
  - plus P-R16-13b for μ_T2.

  With one scalar edge, or at SM counts, the alternatives remain: pairing (P46), a shear counterterm (R16-9's P-R16-9a), or the empty Fock vacuum.
- **Photon/gluon TT vertices:** still not built (R16-9's P-R16-9b, narrowed to vectors).
- No axiom text changes. Sizes would use a = ℓ_P only through the scale-reference primitive (`AX:189-190`); none are quoted here.

---

## 4. Against the FIXED readings (`TESTS:5609-5611`)

**Worker reading: LIFTED, on the letter of the clause.**

- **LIFTED: met, with count 3.**
  - Explicit mixed content: 2 real scalars on G(2.5647), 2 real scalars on G_w(1.7406, 0.7413), 1 Dirac field on D1(1.3133, 0.5731).
  - Every edge is subluminal: scalars |σ′| ≤ 1; Dirac by Lemma V1.
  - E_g = T₂g = μ_E = 0 at m = 0.01 (re-solved at m = 0.001), checked at two resolutions. Three tunings, with a nonsingular Jacobian.
  - **Prescription scope:** M scalar vertex, V0 Dirac vertex, SF shear flow, supplied vacuum, assumed standard W1, axial q, bare-cone Ξ.
- **What LIFTED does not cover (must travel with it):**
  - μ_T2 = −3.5e-5 at the root. Wilson-Dirac seas make this row nonzero, and the FIXED clause does not list it.
  - The two scalar edge families. With one scalar edge (Higgs-doublet-like), no root was found: every solve stalled at r = 1/√3 with residuals ~1.5e-4.
  - SM counts (4 + 22.5) were not reached (residuals ~1e-2).
- **PERSISTS: not met, and false as worded.** Fermion loops *can* cancel μ_E at a graviton-cone zero.
- **What the referee should check first.** That V0 (Wilson mass not coupled to TT) and SF are acceptable stipulations. Under a different Dirac vertex the root moves or disappears.
- **What changed relative to R16-9** (now refereed OPEN, `vR16-9`):
  - the fermion sign premise is confirmed (checked);
  - with **one** scalar edge, the obstruction moves from the shear to polarization balance (birefringence), checked in the tested families; a second scalar edge family removes it;
  - a new row, μ_T2 ≠ 0 for Wilson-Dirac seas, enters the count.

**Expectation check.** "Fermion μ_E has the opposite sign, so the conflict is LIFTED with one more tuning" (`TESTS:5613`):
- First half: confirmed (checked, D1; most DG).
- Second half: met in count (3 = R16-3's 2 + 1 edge parameter), but only with two scalar edge families and with μ_T2 left nonzero. With one scalar edge it was not found.

## 5. Strong-word check

- **"Proved"** is used only for:
  - Theorem DT (identity);
  - μ^F = −N_cμ^s under SF (one line);
  - div v_T2g = W′_xW′_y (so μ_T2 ≠ 0 is generic, with nonvanishing checked);
  - Lemma V1.
- **"Checked"** is used for every number:
  - grid (N ≤ 192) or tensor Gauss–Legendre quadrature, with convergence lines in the `.out` files;
  - the identity against R10-5's grid-shift method to ≤ 2e-4 relative;
  - calibration to V3 and R10-5.
- **"Every Dirac law tested"** refers to the 36 DG and 6 DZ scan laws, the two D1(1.4, r) laws, and the solver end points. It is not a theorem.
- **"Not found"** means local least squares from the stated starts with box bounds. No global search was done and no certified bound exists.
- **Not claimed:**
  - photon or gluon loops;
  - the Wilson-coupled vertex variant;
  - off-axis q;
  - dressed poles;
  - any W2;
  - a no-go;
  - uniqueness of the root;
  - a lift at SM counts or with one scalar edge.

## 6. For the referee

1. Theorem DT. The pair weight from Γγ_bΓ = 2G_bΓ − |G|²γ_b, the symmetric-φ step α = ½⟨∂_a∂_bφ⟩, and the need for c·G to be k_z-independent.
2. Whether V0, with the Wilson term not coupling to TT, is a fair "Belinfante-symmetrized" stipulation, and whether SF (μ^F = −N_cμ^s) is the right fermion strain prescription.
3. Lemma V1's weighted Cauchy–Schwarz.
4. The μ_T2^F ≠ 0 row, and whether it belongs among R13-8's counted conditions.
5. Whether the stalled 4 + 1 solves (r at 1/√3) suggest a proof route. The two-ratio matching (Eg/T2g, μ/T2g) between the scalar and fermion families is the candidate.
6. The root (`verify_root6.out`): rerun it independently, especially the fermion part with a different quadrature. Also decide whether a content with two scalar edge families and μ_T2 ≠ 0 should count as LIFTED or be read as OPEN.

## 7. Files (all in `S/scripts/`)

- **Copied unmodified:**
  - `zz.py`, `laws.py`, `floor_scan.py` (R16-3);
  - `sublum.py`, `r161_laws.py`, `r85_box_qed_copy.py` (R16-1).
- **New:**
  - `dirac.py`: general N_c pair-weight evaluator, grid-shift α, strain μ.
  - `aform.py`: A-form for D1.
  - `dfam.py`: DG family, Lemma V1 docstring, tensor-GL evaluator, sampled v_max.
  - `dz.py`: DZ family.
  - `validate.{py,out}`: R10-5 and V3 calibration.
  - `d1_run.{py,out}`: D1 signs.
  - `dfam_check.{py,out}`: GL against uniform grid against shift method.
  - `scan_dg.{py,out}`: DG scan plus scalar G_w values.
  - `dz_scan.{py,out}`: zigzag Dirac edges.
  - Solvers `content.py`, `content2.py`, `content3.py`, `content4.py` and `content5.py`, with their `.out` files (`solve_*`, `root_*`, `root3_*`, `root4_*`, `root5_*`); `.npy` files hold end points.
  - **The root:** `content6.py` → `root6_2_2_1.{out,npy}` and `root6_3_1_1.out`; `verify_root6.{py,out}` (resolution, m-drift, Jacobian, 3-knob re-solve, v_max); `resolve_light.{py,out}` (m = 0.001).
  - `vmax_close.{py,out}`: v_max at the one-scalar-edge closest approach.
  - `root5_4_22.out`: run stopped unfinished.
