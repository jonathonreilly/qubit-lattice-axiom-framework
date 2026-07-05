# YT P1 Δ_R — Fermion-Channel Regulator-Dependence + Scalar /N_TASTE Double-Count: Resolution Note (2026-06-16)

**Claim type:** bounded_theorem
**Claim boundary:** bounded correction theorem for the P1 / Δ_R lattice-matching
surface: the scalar channel had an extra `/N_TASTE` division after a full-BZ
staggered integral, and the fermion channel with only a `k=0` continuum
subtraction is IR-regulator-dependent. The note invalidates the small
`Δ_R ≈ -3.27%` precision claim and records an O(50%) uncontrolled corrected
bound; it does not provide a new controlled top/Higgs prediction.

Status: **correction proposal (working-tree finding; NOT an audit verdict).** This
note documents two defects in the P1 / Δ_R lattice-matching computation and the
honest corrected value. Audit re-classification of the affected rows is the
lane's call, not this note's.

Authority touched (the buggy surface):
`scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py` and its note
`docs/YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md`.

**Primary runners:**
- [`scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py`](../scripts/frontier_yt_p1_bz_quadrature_full_staggered_pt.py)
- [`scripts/corrections/yt_p1_fermion_regulator_verification_memsafe.py`](../scripts/corrections/yt_p1_fermion_regulator_verification_memsafe.py)
- [`scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py`](../scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py)
- [`scripts/corrections/yt_p1_mt_compression_memsafe.py`](../scripts/corrections/yt_p1_mt_compression_memsafe.py)

**Cached logs:**
- [`logs/runner-cache/frontier_yt_p1_bz_quadrature_full_staggered_pt.txt`](../logs/runner-cache/frontier_yt_p1_bz_quadrature_full_staggered_pt.txt)
- [`logs/runner-cache/yt_p1_fermion_regulator_verification_memsafe.txt`](../logs/runner-cache/yt_p1_fermion_regulator_verification_memsafe.txt)
- [`logs/runner-cache/yt_p1_delta_r_corrected_bound_memsafe.txt`](../logs/runner-cache/yt_p1_delta_r_corrected_bound_memsafe.txt)

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  repo baseline Lattice + Quantum + Record language. The axiom baseline is an
  approved premise and is not a source of bounded status.
- [`YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md`](YT_P1_H_UNIT_RENORMALIZATION_FRAMEWORK_NATIVE_NOTE_2026-04-17.md)
  supplies the bounded `H_unit` scalar-bilinear lattice-PT setup.
- [`YT_P1_I_S_NATIVE_KERNEL_SETTLED_BOUNDED_THEOREM_NOTE_2026-06-16.md`](YT_P1_I_S_NATIVE_KERNEL_SETTLED_BOUNDED_THEOREM_NOTE_2026-06-16.md)
  supplies the narrowed kernel-fork result: scalar projection leaves the
  `D_psi^-1 D_g^-1` kernel but does not choose the final taste normalization.

---

## 1. Summary

The three-channel lattice-matching correction

    Δ_R = (α_LM/4π) [ C_F·Δ_1 + C_A·Δ_2 + T_F n_f·Δ_3 ]

was reported as **Δ_R = −3.27%** and used to land `m_t(pole) = 172.57 GeV`. Two
of its three channels are defective:

- **Δ_1 (C_F, scalar):** the scalar matching coefficient `I_v_scalar` divided a
  full-BZ integral by `/N_TASTE = 16`. The 16 tastes ARE the 16 BZ corners
  already covered by the full-BZ extent, so this is a **double-count**. Corrected
  `I_S = 32.4` (not 3.90); the runner's own `D_psi_full` docstring already says
  "do NOT divide by N_TASTE", contradicting the code.
- **Δ_3 (T_F n_f, fermion):** the fermion-loop integrand `F_g/D_psi²` is
  log-divergent at **all 16 BZ doublers** (`D_psi=Σsin²k_μ → 0` at each corner),
  but the continuum subtraction `4/(k²+m²)²` removes **only the k=0 doubler**.
  The result therefore **drifts with the IR regulator m²** and is NOT a matching
  constant: `I_SE_fermion ≈ 0.996` and `Δ_3 ≈ 1.328` are artifacts of the
  arbitrary `m²=0.01`. The `/N_TASTE²` divisor cannot fix this (a constant cannot
  cancel an m²-varying log). The taste-power question (`/16` vs `/256`) is moot.

**Δ_2 (C_A, gluonic) is clean and unchanged** (`D_g²` vanishes only at the
origin; its single log is correctly subtracted).

## 2. Verification (three independent methods, all memory-safe)

1. **Analytic power-counting.** Near every corner `c∈{0,π}⁴`, `D_psi → (k−c)²`
   and `F_g → w_c = #(zero components of c)`. The corner weights sum to
   `Σ w_c = 32` (each of 4 slots is zero in 8 of 16 corners); origin weight 4.
   So after single-corner subtraction
       d(lat−cont)/d log m² → −(32 − 4) = **−28**   (a clean constant would give 0).
2. **Numerics** (`scripts/corrections/yt_p1_fermion_regulator_verification_memsafe.py`,
   N≤32, single process): fermion single-corner slope ≈ **−36** (→ −28 as m²→0);
   scalar-control slope ≈ **−2.9** (≈0, clean); full-16-doubler subtraction
   collapses the slope (the doublers ARE the disease).
3. **Independent analytic cross-check:** confirmed the 32/28 corner count, the
   `−28` slope, the scalar-clean contrast, and that no "reduced-BZ" / "/256
   compensation" / "schematic-only" defense rescues the runner.

## 3. Corrected Δ_R (honest bound)

`scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py` (memory-safe,
N≤48, full-doubler subtraction + m²→0 extrapolation for the fermion channel):

| channel | corrected | runner |
|---|---|---|
| Δ_1 = 2·I_S − 6 (I_S=32.4) | C_F channel **+56.6%** | +1.7% |
| Δ_2 = −(5/3)·I_SE_gluonic   | C_A channel **−8.4%** (clean) | −8.4% |
| Δ_3 (full-doubler, C_f≈19–23) | T_F n_f channel **+0.3%…+5.4%** | +2.9% |
| **Δ_R** | **+49%…+54%** | **−3.27%** |

**Δ_R is an O(50%) uncontrolled quantity dominated by the scalar C_F channel**,
not the small −3.27% reported. Critically, that +56.6% scalar channel is the
**unimproved single-link 1-loop value, which is non-perturbative / uncontrolled**
(Lee–Sharpe hep-lat/0208018: unimproved staggered matching constants are O(tens)
and untrustworthy at one loop; smearing exists precisely to fix this). So the
honest message is "Δ_R is large and uncontrolled," NOT a new precise value.

## 4. Downstream impact

- The runner's `Δ_R = −3.27%` underwrote `m_t(pole) = 172.57 GeV` (vs PDG 2025
  `172.56 ± 0.31 GeV`). **It is not only the central value that fails — the claimed
  precision fails.** The framework's m_t residual budget (`P1 ≈ 1.92%`, "geometric
  bound `|Δ_R^total| ≤ 7.41%`" in `YT_P1_LOOP_GEOMETRIC_BOUND_NOTE_2026-04-17.md`)
  rests EXPLICITLY on `I_S ∈ [2, 6]` (`Δ_1 = 1.924%…5.772%`, that note's eqs.).
  The corrected `I_S = 32.4` gives `Δ_1 = +58.9%` — ~10× the `I_S=6` assumption —
  so the corrected `Δ_R ≈ +50%` **violates the framework's own ≤7.41% bound by
  ~7–10×.** So m_t is not controlled even at the ≤7% level claimed, let alone
  sub-percent.
- **What survives — quantified and cross-checked against the framework's QFP
  script** ([`scripts/frontier_yt_qfp_insensitivity.py`](../scripts/frontier_yt_qfp_insensitivity.py);
  [`scripts/corrections/yt_p1_mt_compression_memsafe.py`](../scripts/corrections/yt_p1_mt_compression_memsafe.py)
  independently checks the compression range): the clean `y_t/g_s = 1/√6`
  boundary with `g_s = √(4π·α_LM) = 1.068` (the framework's actual choice) gives
  `y_t(M_Pl) = 0.4358`, runs 17 decades down to
  `y_t(v) = 0.9727 → m_t = 169.4 GeV` (MS̄) → **`172.57 GeV` (pole, +1.9%
  K-series)**, reproducing the headline. The top-Yukawa IR quasi-fixed point
  focuses, but only **moderately** at this boundary: the framework's own runner
  gives local sensitivity **`dy_t(v)/dy_t(M_Pl) = 0.685`** (a 10% boundary shift
  gives about 3.1% in `y_t(v)`; upper-half focusing ratio `R ≈ 2`). That is real
  but **far too weak to control the corrected matching**: `Δ_R ≈ ±50%` takes
  `y_t(M_Pl) ∈ [0.22, 0.65]`, and the independent compression check gives
  **`m_t(pole) ∈ ~[114, 197] GeV`** after the same +1.9% pole conversion
  (asymmetric; the fixed point caps the ceiling near ~197 GeV but does not pin
  the value). The framework's QFP "insensitivity PASS" used an assumed boundary
  band `[0.3, 0.6]` (≈±15–30%) **predicated on the small buggy ~2% matching**; the
  corrected ±50% matching exceeds it. Net: the fixed point protects the *ceiling*,
  not the *precision*. m_t is uncontrolled across ~[114, 197] GeV; the
  **sub-percent bullseye is definitively not earned** and the ~2%/≤7.41%
  precision is invalidated.
- **Landscape context (why this downgrade is the correct, not an unusual, call):**
  NO established framework predicts m_t to controlled sub-percent. In the SM m_t
  is a **free input** (Yukawa coupling, not predicted). The best BSM "predictions"
  are ballpark at the few-percent level: multiple-point criticality (Froggatt–
  Nielsen 1996) `m_t = 173 ± 5 GeV` (~3%); asymptotic safety (Shaposhnikov–
  Wetterich 2009) uses m_t as an INPUT and outputs `m_H ≈ 126 GeV ± few GeV`; the
  top-Yukawa IR quasi-fixed point (Hill/Pendleton–Ross) gives an O(200 GeV)
  attractor, not a sub-% value. So a controlled sub-% m_t would be unprecedented —
  the framework's clean-route **ballpark** is honestly in the same class as the
  best existing attempts; only the sub-% bullseye was the over-claim.
- The narrow "±0.006 grid precision" claimed for `I_SE_fermion` is an artifact of
  holding m² fixed; shifting m² 0.01→0.001 moves it ~33%.
- `YT_P1_BZ_QUADRATURE_FULL_STAGGERED_PT_NOTE_2026-04-18.md` §2.5 incorrectly
  states the continuum subtraction "cancels the UV logarithm" for the fermion
  channel — it cancels only the origin doubler's log.

## 5. Blast radius (surfaces that cite Δ_R / I_SE_fermion / the buggy runner)

Correction banners/caveats have been added to these surfaces (this note does NOT
re-derive the claims; re-derivation and lane re-audit are owner/lane calls):
`YT_P1_DELTA_R_MASTER_ASSEMBLY_THEOREM_NOTE`, `YT_EW_DELTA_R_RETENTION_ANALYSIS_NOTE`,
`YT_P1_REP_A_REP_B_CANCELLATION_THEOREM_NOTE`, `YT_P1_DELTA_3_BZ_COMPUTATION_NOTE`,
`YT_P1_BZ_QUADRATURE_2_LOOP_FULL_STAGGERED_PT_NOTE`, `YT_P1_DELTA_R_2_LOOP_EXTENSION_NOTE`,
`YT_P1_DELTA_R_SM_RGE_CROSSCHECK_NOTE`, `YT_P1_I_S_LATTICE_PT_CITATION_NOTE`,
`YT_P1_LOOP_GEOMETRIC_BOUND_NOTE` (the ≤7.41% m_t-precision bound — rests on
`I_S ∈ [2,6]`, violated ~7–10× by the corrected `I_S=32.4`),
`YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE` (carries P1 as the m_t transport residual),
`YT_QFP_INSENSITIVITY_SUPPORT_NOTE` (focusing real but ~2×; protects the m_t ceiling, not its precision),
`HIGGS_MASS_RETENTION_ANALYSIS_NOTE`, `YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE`,
`MINIMAL_AXIOMS_2026-04-11` (the m_t/m_H lines), and the publication tables
(edit the SOURCE `QUANTITATIVE_SUMMARY_TABLE.md` / `DERIVATION_VALIDATION_MAP.md`;
the `_EFFECTIVE_STATUS.md` views auto-refresh via the pipeline — do NOT hand-edit them).

## 6. What this does NOT change

- The exact lattice-scale Ward theorem `y_t(M_Pl)/g_s(M_Pl) = 1/√6` (untouched).
- The C_A gluonic channel Δ_2 (verified clean).
- The qualitative existence of a finite fermion matching constant under proper
  full-doubler subtraction (~19–23 in lat−cont units) — but it is non-perturbative
  at single-link order, hence a bound, not a controlled result.

Reproduce: the two `scripts/corrections/*_memsafe.py` runners (single process,
N≤48, peak RAM < ~700 MB). Do NOT run full-BZ quadratures across parallel
processes — that is memory-unsafe.

## 7. Static sibling scan (2026-06-16) — reviewed BZ defects stay in the m_t / Δ_R lane

A static review scan of 11 prediction runners (spot-checked without running the
large quadratures) found the same defect class in three more BZ-quadrature
siblings, all in the P1/Δ_R → m_t lattice-matching lane. Each is now flagged
in-file with a correction banner:

- [`scripts/frontier_yt_p1_bz_quadrature_numerical.py`](../scripts/frontier_yt_p1_bz_quadrature_numerical.py)
  — both defects, **not firewalled**
  (feeds Δ_1 and Δ_3 of Δ_R); its Δ_R/m_t values are uncontrolled.
- [`scripts/frontier_yt_p1_bz_quadrature_2_loop_full_staggered_pt.py`](../scripts/frontier_yt_p1_bz_quadrature_2_loop_full_staggered_pt.py)
  — both defects in
  code but **firewalled** (a bound-clamp replaces the corrupt MC with the
  loop-geometric bound, so the headline m_t is unaffected). Its per-channel `J_X`
  envelopes are defective and must not be cited as 2-loop matching coefficients.
- [`scripts/yt_p1_i_s_native_bz_certificate_2026_06_11.py`](../scripts/yt_p1_i_s_native_bz_certificate_2026_06_11.py)
  — D1 only; its "I_S below
  [4,10]" verdict is itself a `/16` artifact (without it I_S ≈ 32, inverting it).

**Not affected by this defect class in the reviewed set** (they use separate
machinery):
- **m_H** — all three Higgs runners are closed-form mean-field `v/(2u_0)`; no BZ
  quadrature.
- **m_τ / charged-lepton (Koide-sector) masses** — computed from `α_LM/(4π)·C_τ`,
  BZ-independent; the BZ object is only a corroborating cross-check.
- **α_bare / EW gauge convention** (3D Z³, single-power, correct subtraction) and
  the RGE-based m_t/α_s runners (boundary-consistency, QFP) — no quadrature.

**Conclusion: this scan found an m_t-lane lattice-matching defect, not a
framework-wide precision collapse from this `/N_TASTE` / doubler bug.** m_H, the
lepton/Koide masses, and the EW couplings carry their own separate caveats.
