# C5 R18-2 report: (S)'s sharpest prediction — must the electroweak vacuum be the true minimum, and is that consistent with the measured inputs?

**Worker.** Claude Opus 5.5 (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13 01:53Z–02:20Z. No repository file was edited. Nothing was downloaded: every measured input is **RECALLED**.

**Scratch folder** `S/` = `.../scratchpad/C5/R18-2/`:
- `S/PREREG.md` — inputs, σ formula, tuning criterion, and the "primary row decides" rule, written before any stability run.
- `S/scripts/smrge.py` — two-loop SM RGEs, one-loop λ_eff, Buttazzo NNLO matching (RECALLED), optional singlet and vector-like extras.
- `S/scripts/r182_a_sm_stability.py/.out` — (a), (b).
- `S/scripts/r182_c_lattice.py/.out` — (c).
- `S/scripts/r182_d_stabilizers.py/.out` — (d) scans.
- `S/scripts/r182_e_extras.py/.out` — a variational bound, a two-field global-minimum grid, and vector-like boundaries.
- `S/scripts/r182_f_coeffcheck.py/.out` — sensitivity to the two-loop transcription.
- `S/recheck/` — the R17-7 and R17-3 runners, copied and rerun.

Every script runs in under 3 minutes with `OMP_NUM_THREADS=2`.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (AX); `C5_R17-7_referee_verdict.md` (vR17-7); `C5_R17-3_referee_verdict.md` (vR17-3).
- In TESTS: C5 method `TESTS:2302-2320`; Round 17 rules `TESTS:5688-5706`; R17-3 `TESTS:5786-5812`; verdicts `TESTS:5998-6016`; R17-7 `TESTS:6018-6047`; R17-10/11 and verdicts `TESTS:6206-6336`; Round 18 head and item `TESTS:6392-6511`.
- In part: R17-7 report §0, §4(c)–(d), prices (`C5_R17-7_report.md:1-60,200-262,300-367`); S23 lines on P93/P125/W10 (`C5_S23_synthesis.md:282,323,387,447,508-509,549,628-634`); S20 P93/P94 (`C5_S20_synthesis.md:388-389`); `C4_F3_referee.md:17` (hierarchy vs. precision tuning).

**Labels.** proved / checked (numerics this run) / suggested / reading / comparator. RECALLED marks every number from memory.

---

## 0. Reading against the FIXED readings (`TESTS:6501-6505`)

**Worker reading: NEEDS-STABILIZER, on the pre-registered primary inputs. The σ condition is fragile.**

1. **SM-only metastability beyond 2σ: met on the primary row, at 2.28σ** (checked; `r182_a_sm_stability.out:35`).
   - **Primary inputs:** M_t = 172.57 ± 0.29 GeV, the PDG-2024 direct average (RECALLED), with a ±0.5 GeV pole-mass ambiguity (RECALLED).
   - **It is fragile.** The tension falls to ≤ 2σ if:
     - the pole-mass ambiguity is ≥ 0.64 GeV (`:41`);
     - or the cross-section pole mass 172.4 ± 0.7 is used: 1.81σ (`:40`);
     - or the theory error on my bound is ≥ 0.51 GeV (`:42`).
   - Without any ambiguity the tension is 3.09σ (`:36`). The full range across the declared rows is **1.5–3.1σ**.
2. **An explicit stabilizer with stated content puts the electroweak vacuum at the global minimum below 1/a** (checked). This is a real singlet with a Higgs portal and a VEV:
   - benchmark m_S = 1e7 GeV, λ_S = 0.2, λ_HS = +0.25;
   - stable for M_t up to 174.5 GeV (`r182_d_stabilizers.out:45-50`);
   - two-field RG-improved grid minimum ≥ 0 = V(v, w) up to M_P (`r182_e_extras.out:10`).

   A second, scale-protected family also works: vector-like Dirac 5-plets with no Yukawa coupling, n5 ≥ 2 (`r182_e_extras.out:14-26`).

**LATTICE-STABILIZES: not met, by a factor ≥ 4e15** (checked; a bounded no-go in the EFT class, for the referee).
- A Planck-suppressed φ⁶ needs coefficient c ≥ 4.4e11 in units of 1/a² (`r182_c_lattice.out:2`).
- The lattice's own dimension-6 terms give |c| ≲ 1e-4 (`:21-23`).
- Independent of any lattice-scale physics, the region h·a ≤ 1e-3 alone forces Λ̃ ≥ 2.6e108 ρ_Λ (`r182_e_extras.out:3`).

**SM-STABLE: not met on the primary row.** It *is* met on two sensitivity rows: ambiguity 1.0 GeV, and the cross-section pole mass.

**If the referee rules the 2σ condition undecidable** under RECALLED inputs and an unsettled ambiguity convention, the reading falls to **OPEN**. That is the expectation's named failure mode (`TESTS:6511`). Three results stand either way:
- the exclusion of LATTICE-STABILIZES;
- the stabilizer constructions;
- the prediction M_t(pole) ≤ 170.9 GeV for (S) with SM-only content.

**Against the expectation (`TESTS:6506-6511`).**
- **"SM-only metastability is a 2–3σ tension": confirmed.** Primary 2.28σ, range 1.5–3.1σ.
- **"Lattice-scale operators cannot act at the 1e10–1e11 GeV instability scale": confirmed and quantified.** h_I(λ_eff) = 1.8e11 GeV; λ(μ) = 0 at 3.2e10 GeV.
- **"A singlet threshold stabilizes over an O(1) window, so it is content, not a tuning": confirmed for the dimensionless parameters only.**
  - λ_HS ∈ [0.095, 0.395] at λ_S = 0.2; λ_S ∈ [0.07, 0.275] at λ_HS = 0.25; m_S over 8 decades, 1.8e3–1.8e11 GeV (`r182_d_stabilizers.out:53-55`).
  - **But m_S·a ∈ [1.5e-16, 1.5e-8].** On a lattice with an unprotected elementary scalar, that is a precision tuning of one relevant parameter: per species, (m_S a)² ≲ 2e-16, the class of the Higgs hierarchy.
  - The registered expectation did not name this cost.
  - The vector-like fermion family avoids the additive tuning: chirally protected Dirac masses renormalize multiplicatively. It still carries a hierarchy, "not automatically a precision tuning" (`C4_F3_referee.md:17`).
- **Removed hypothesis:** R17-7's SM-only content (`TESTS:6492`).

---

## 1. Inputs, conventions, method (declared in `S/PREREG.md` before any run)

**Inputs (all RECALLED):**
- M_h = 125.20 ± 0.11 GeV;
- α_s(M_Z) = 0.1180 ± 0.0009;
- M_W = 80.369 GeV;
- M_t, primary: 172.57 ± 0.29 GeV (PDG 2024 direct average);
- pole-mass ambiguity: ±0.5 GeV primary, with rows at 0 / 0.3 / 1.0;
- alternatives: ATLAS+CMS Run-1 172.52 ± 0.33; cross-section pole mass 172.4 ± 0.7;
- ρ_Λ = 2.5e-47 GeV⁴.

**Matching at μ = M_t (comparator, RECALLED).** Buttazzo et al. 2013 NNLO MS-bar fit formulas for λ, y_t, g₃, g₂, g_Y, including their two-loop thresholds. At the primary inputs: (g_Y, g₂, g₃, y_t, λ) = (0.35843, 0.64764, 1.16516, 0.93286, 0.12617) (`r182_a_sm_stability.out:2`).

**Running.**
- Two-loop SM RGEs for g_Y, g₂, g₃, y_t, λ, in the convention V = λ(|H|² − v²/2)². This is my own transcription of the standard results (RECALLED). Three-loop running enters only through the comparator.
- λ_eff(h): one-loop Landau gauge at μ = h, with top, W and Z; Goldstone and Higgs loops dropped; times e^{4Γ}. The prefactor cannot change the sign.

**Criterion.**
- Stability: min over h ∈ [1 TeV, M_P] of λ_eff ≥ 0, with M_P = 1/a = 1.2209e19 GeV (a = ℓ_P).
- V_EW ≈ −1.2e8 GeV⁴ is negligible against λh⁴ at h ≳ 1e3 GeV.
- σ: n_σ = (M_t − M_t,crit)/√(s_mt² + s_amb² + s_th² + (∂M_tc/∂α_s · s_αs)² + (∂M_tc/∂M_h · s_Mh)²), with s_th = 0.30 GeV declared.

**Transcription check (checked; `r182_f_coeffcheck.out`).**
- The repo runner `scripts/frontier_higgs_mass_full_3loop.py:239-279` carries different two-loop coefficients:
  - y_t: 131/80 g₁², 1187/216 g₁⁴, 9/4 g₂²g₃², −6λy_t²;
  - λ: different y_t⁴g² terms.
- Swapping them in moves λ(M_P) by 5.3e-4. That is ≈ 0.08 GeV in M_t,crit, inside s_th.
- The RECALLED comparator does not decide between the two transcriptions: its own three-loop shift is the same size.
- **Suggested, not load-bearing.** The repo's −6λy_t² together with +6λ² mixes two λ normalizations. The standard pair, in this convention, is (−12λy_t², +6λ²).

---

## 2. (a) λ(μ), instability scale, stability bound

**Central profile (checked; `r182_a_sm_stability.out:4-19`):**

| μ (GeV) | λ(μ) | λ_eff(h = μ) | y_t |
|---|---|---|---|
| 1e3 | +0.0967 | +0.1270 | 0.852 |
| 1e8 | +0.0144 | +0.0248 | 0.590 |
| 1e10 | +0.0022 | +0.0073 | 0.534 |
| 1e11 | −0.0019 | +0.0013 | 0.511 |
| 1e12 | −0.0051 | −0.0033 | 0.489 |
| 1e14 | −0.0091 | −0.0092 | 0.453 |
| 1e17 | −0.0113 | −0.0124 | 0.407 |
| 1.22e19 | −0.0110 | −0.0122 | 0.380 |

- **Minima:** λ_min = −0.0113 at 3.6e17 GeV; λ_eff,min = −0.0125 at 4.6e17 GeV.
- **Instability scale:** λ(μ) = 0 at **3.2e10 GeV**; λ_eff(h) = 0 at **1.8e11 GeV**.
- **One-loop running alone** would give λ(M_P) = −0.029 (`:21`), so the two-loop terms matter.

**Comparator (RECALLED; `:23-26`).** The Buttazzo fit λ(M_Pl) = −0.0143 − 0.0066 δM_t + 0.0018 δα_s + 0.0029 δM_h:
- at their reference point, mine is −0.01507 against −0.01430 (difference −0.0008, ≈ 0.12 GeV in M_t);
- at the primary inputs, −0.01099 against −0.01010.
- The RECALLED instability scale of 1e10–1e11 GeV is reproduced.

**Absolute-stability bound (checked; `:28-32`).**
- **M_t,crit = 170.88 GeV** from λ_eff, and 170.83 GeV from λ(μ), at M_h = 125.20 and α_s = 0.1180.
- Using h_max = the reduced M_P instead of 1/a changes nothing: the minimum sits at 4.6e17 GeV.
- **Sensitivities:** ∂M_tc/∂M_h = 0.494; ∂M_tc/∂α_s = +0.35 GeV per 0.0009.
- **Comparators (RECALLED):**
  - the Buttazzo bound in M_h form gives 171.01 GeV at our inputs;
  - Buttazzo's "M_t < 171.36 ± 0.46 GeV at M_h = 125.66 GeV, α_s = 0.1184" compares with mine there, **171.26**.
  - Agreement is to 0.10–0.13 GeV, inside s_th.

## 3. (b) Tension in σ (checked; `r182_a_sm_stability.out:34-42`)

| Inputs | σ_tot (GeV) | n_σ |
|---|---|---|
| **PRIMARY: PDG-2024 direct 172.57 ± 0.29, ambiguity 0.5** | 0.742 | **2.28** |
| direct, ambiguity 0 | 0.549 | 3.09 |
| direct, ambiguity 0.3 | 0.625 | 2.71 |
| direct, ambiguity 1.0 | 1.141 | 1.48 |
| ATLAS+CMS Run-1 172.52 ± 0.33, ambiguity 0.5 | 0.759 | 2.16 |
| cross-section pole 172.4 ± 0.7 | 0.841 | 1.81 |

The primary row reaches exactly 2σ at an ambiguity of 0.64 GeV, or at s_th = 0.51 GeV.

**Plain statement.** With SM-only content, (S) predicts **M_t(pole) ≤ 170.9 GeV** (± ~0.4 GeV theory and inputs; two-loop, RECALLED inputs). The direct measurements sit 2.3σ above that on the primary convention. A clean pole-mass determination (a threshold scan) would turn this into a sharp test (suggested).

## 4. (c) Can φ⁶/M_P² or the lattice's own dispersion stabilize?

**c1. Required φ⁶ (checked; `r182_c_lattice.out:1-3`).**
- V = λ_eff h⁴/4 + c h⁶/M² ≥ V_EW for all h ≤ M_P needs **c_min = 4.4e11** with M = 1/a, or 1.7e10 with the reduced M_P.
- The binding point is h = 2.9e11 GeV, just above h_I.
- Equivalently, a unit-coefficient φ⁶ would need its scale at **Λ₆ ≤ 1.8e13 GeV ≈ 1.5e-6/a**. That is new physics far below 1/a, not a lattice-scale term.

**c2. With an O(1) coefficient the potential is bounded below, but a deeper minimum survives (checked; `:6-10`).**

| c | V_min (GeV⁴) | h·a at the minimum | Λ̃/ρ_Λ |
|---|---|---|---|
| 1 | −1.0e68 | 0.046 | 4.0e114 |
| 100 | — | 0.005 | 3.9e110 |

Λ̃/ρ_Λ is 4e112 to 4e116 across c = 10 to 0.1. These are consistent with R17-7's 1e112–3e120 (`vR17-7:37-40`).

**c3. The lattice's own dispersion (checked to order of magnitude; `:12-23`).** The one-loop zero-point sum with field-dependent mass M = yh/√2, lattice minus continuum, gives a dimension-6 term c_lat h⁶a².
- **Box law** (exact relativistic dispersion inside the cubic zone): J = 1.80e-3, below the inscribed-sphere bound 2.57e-3. For the top, **c_lat = +1.5e-6**, with the stabilizing sign.
- **Nearest-neighbour (sin) boson:** a² M⁶ ln(1/Ma) term. Log-extrapolated to the physical M·a = 5e-9, |c_lat| ~ 1e-4.
- **Shortfall ≥ 4e15.**
- **What a lattice can and cannot touch (reading).** Corrections at h ~ h_I are O((h_I a)²) ≈ 2e-16 relative. Between M_t and 1e16 GeV the running is fixed by the low-energy content. So lattice structure at a = ℓ_P can modify only the region h·a ≳ 1e-3, and the instability starts eight decades below it.

**e1. A lattice-independent lower bound (checked, under H-EFT; `r182_e_extras.out:1-7`).**
- **H-EFT:** the RG-improved effective potential is valid, as the minimum energy density at fixed ⟨h⟩, wherever h·a ≤ 1e-3.
- Under H-EFT, e₀ ≤ min V_eff over that range, so Λ̃ = κ(V_EW − e₀) is bounded below.

| Range | V_eff minimum (GeV⁴) | Λ̃ ≥ |
|---|---|---|
| h·a ≤ 1e-3 | −6.5e61 | **2.6e108 ρ_Λ** |
| h·a ≤ 1e-5 | — | 2.0e100 ρ_Λ |
| h·a ≤ 1e-7 | — | 7.8e91 ρ_Λ |

- Even at M_t = 171.5 the bound is 8.1e107 ρ_Λ.
- This bound does not depend on what the lattice does near 1/a.

**c4. Field-range reading (suggested).** A qubit-composite Higgs whose amplitude is bounded by h_max would need h_max·a < 1.5e-8 (`r182_c_lattice.out:25-26`). That is a stipulated small number, not an O(1) lattice-scale term.

**Answer to (c).** No. The field values involved are h ~ 2e11–1e16 GeV (h·a ~ 1e-8 to 1e-3), against the instability scale 1.8e11 GeV. Within the stated EFT class, φ⁶/M_P² with O(1) coefficients and the lattice dispersions fall short by ≥ 4e15. The (S) residual from that range alone is ≥ 1e108 ρ_Λ.

## 5. (d) Minimal stabilizers

### d1. Real singlet with portal and VEV (Lebedev; Elias-Miró–Espinosa–Giudice–Lee–Strumia 2012; comparator RECALLED)

**Potential:** V = λ_H(|H|² − v²/2)² + (λ_S/4)(S² − w²)² + (λ_HS/2)(|H|² − v²/2)(S² − w²).

**Proved (elementary):**
- (v, w) is the global tree-level minimum, with V = 0, iff 4λ_Hλ_S > λ_HS². This is positive-definiteness of the quadratic form in X = |H|² − v²/2 and Y = S² − w², for either sign of λ_HS.
- Integrating out S at tree level gives λ_SM = λ_H − λ_HS²/(4λ_S), so the condition is λ_SM(m_S) > 0.

**One-loop singlet β functions (derived from the general φ⁴ formula; checked by hand):**
- 16π² β_λH ⊃ +λ_HS²/2;
- 16π² β_λHS = λ_HS(12λ_H + 6λ_S + 4λ_HS + 6y_t² − 9/2 g₂² − 3/2 g_Y²);
- 16π² β_λS = 18λ_S² + 2λ_HS².

**Scan (checked; `r182_d_stabilizers.out:1-43`).** Conditions:
- λ_eff,SM > 0 below m_S;
- λ_H,eff > 0, λ_S > 0, and copositivity for λ_HS < 0, above m_S, up to M_P;
- |λ| < 4.

Results:
- Stable windows exist for every m_S from 1e3 to 1e10 GeV and none at ≥ 1e11 GeV, which sits above h_I.
- λ_S ≳ 0.3–0.4 fails |λ| < 4 because of λ_S's Landau pole, except at high m_S. Checked at m_S = 1e7 GeV: λ_S(m_S) = 0.3 runs to 33 by M_P, and 0.4 diverges near 2e16 GeV.

**Benchmark (checked).** m_S = 1e7 GeV, λ_S = 0.2, λ_HS = +0.25 (w = 1.58e7 GeV):
- min λ_H,eff = 0.119; λ_S(M_P) = 0.71; λ_HS(M_P) = 0.56;
- stable at M_t = 171.5, 172.57, 173.5 and 174.5 GeV (`:45-50`);
- RG-improved two-field grid over h, s up to M_P: min V/(h² + s² + w²)² = +7.3e-5 ≥ 0, so (v, w) is the global minimum (`r182_e_extras.out:9-12`);
- mixing ~1e-5, so the M_h matching is unaffected.

**Windows (checked; `r182_d_stabilizers.out:53-55`):**

| Parameter (others fixed) | Stable range |
|---|---|
| λ_HS | [0.095, 0.395] |
| λ_S | [0.070, 0.275] |
| m_S | [1.8e3, 1.8e11] GeV |

**(S) conditions.** (v, w) is the global minimum, so V_EW = e₀ and Λ̃ = 0 ≥ 0, with no deeper minimum. That holds at tree level, RG-improved; the one-loop potential in the singlet direction is not computed.

**Tuning or content.**
- **The dimensionless parameters are content.** Each window is O(1), and the threshold δ = λ_HS²/(4λ_S) ∈ [0.013, 0.29] is a tree relation among couplings, so it is radiatively stable.
- **The scale is not free.** m_S must lie below h_I ≈ 2e11 GeV, so m_S·a ≤ 1.5e-8.
  - For an unprotected elementary lattice scalar, the bare mass² is additively renormalized at O(a⁻²). Holding (m_S a)² ≤ 2e-16 is **a precision tuning of one relevant parameter** (counterterm basis: per scalar species).
  - It is the same class as the Higgs hierarchy, which the campaign's bill does not count.
  - It is content only if a protection or transmutation mechanism is supplied, which is not done here.

### d2. Vector-like Dirac 5-plets, no Higgs Yukawa (one-loop gauge shift Δb_i = 2n5/3; their two-loop gauge terms neglected)

**Checked (`r182_e_extras.out:14-26`; `r182_d_stabilizers.out:57-72`).**
- n5 = 1 never suffices.
- For n5 ≥ 2 the largest stabilizing M_F is:

| n5 | M_F,max at M_t = 172.57 | M_F,max at M_t + 2σ (173.15) |
|---|---|---|
| 2 | 1.9e4 GeV | 3.4e3 GeV |
| 3 | 1.9e5 GeV | 2.8e4 GeV |
| 4 | 9.9e5 GeV | 1.3e5 GeV |
| 6 | 8.8e6 GeV | 1.1e6 GeV |
| 8 | 3.6e7 GeV | 4.4e6 GeV |

- All are perturbative to M_P for n5 ≤ 8 (g_Y(M_P) = 2.2 at n5 = 8 and M_F = 1 TeV is borderline).
- **Mechanism:** larger g₃ drives y_t down faster, and larger g₂, g_Y add positive gauge terms. At n5 = 2, M_F = 1 TeV: y_t(M_P) = 0.33 against 0.38.

**Tuning or content.**
- **Content:** an integer n5 and one mass.
- With chirally protected lattice fermions (the KS remnant U(1)_ε; comparator RECALLED) the Dirac mass is multiplicatively renormalized. The hierarchy M_F·a ~ 1e-15 is then technically natural and radiatively stable: a hierarchy, "not automatically a precision tuning" (`C4_F3_referee.md:17`).

**Costs (reading/comparator, RECALLED).**
- Stable coloured and charged states need M_F ≳ 1.5–2 TeV (LHC long-lived searches) and a decay channel or low reheating (relics). A tiny mixing Yukawa ≲ 1e-3 provides decays without affecting running.
- For n5 = 2 the window at M_t + 2σ is narrow, [~2e3, 3.4e3] GeV, so n5 ≥ 3 is the robust version.
- Taste multiplicity on a KS lattice would change the counting of n5 (not computed).
- **Prediction:** new coloured vector-like states below ~2e4–2e5 GeV for minimal content (suggested).

### Comparison: (S′-start), P125

(S′-start) needs no stabilizer and no M_t condition: C is the minimum of the starting basin. It pays instead with:
- a basin structure;
- a first reading;
- loss of positivity;
- P94′ (`vR17-7:42`; `C5_S23_synthesis.md:549`).

So the choice is between:
- (S) + [M_t ≤ 170.9 GeV, or a singlet with one scalar-mass tuning, or n5 ≥ 2–3 chirally protected vector-like 5-plets below ~1e4–1e7 GeV];
- (S′-start) + P94′.

## 6. (e) Prices and counting (named, never adopted)

| Price | Content | Axiom/source | Numbers (basis: rule `TESTS:5700`) |
|---|---|---|---|
| **P93 (sharpened)** | Our vacuum is the global minimum. With SM-only content: **M_t(pole) ≤ 170.88 GeV** (two-loop; RECALLED inputs), at 2.28σ on primary inputs (1.5–3.1σ). Otherwise new content below h_I ≈ 1.8e11 GeV | `AX:187`; vR17-7 | 0 if SM-STABLE |
| **P-r182a** | Real singlet with portal and VEV; m_S ∈ [1.8e3, 1.8e11] GeV, λ_HS ~ [0.1, 0.4], λ_S ~ [0.07, 0.28] | content; no axiom | 0 dimensionless tunings; **1 scalar-mass tuning (per species), (m_S a)² ≤ 2e-16**, unless protected |
| **P-r182b** | n5 ≥ 2 vector-like Dirac 5-plets (no Yukawa), M_F ≤ 1.9e4 GeV (n5 = 2) to 3.6e7 GeV (n5 = 8) | content; needs chirally protected lattice fermions (KS U(1)_ε, an existing framework structure; reading) | 0 tunings; 1 technically natural hierarchy |
| P125 | (S′-start) + P94′, the comparison | as S23 | 0 numbers |
| — | LATTICE-STABILIZES excluded in the EFT class (§4) | — | — |

**Enforced or stipulated.**
- (S) is a stipulated number-free principle, not forced (vR17-3:17; round-18 rule).
- P93 is not forced by the four texts.
- The stabilizer content is stipulated.
- No number is enforced by a symmetry, except the singlet's tree relation and the fermion mass's multiplicative renormalization.

**Radiative stability.**
- (S) tracks loops by definition.
- The singlet's dimensionless window is stable; its mass is not, unless protected.
- The fermion family is stable.

## 7. Round-17/18 rules

- **Whole-zone v_max.**
  - No lattice law is constructed. The analysis is the continuum SM EFT (v = 1).
  - The c3 dispersions: box law v_max = 1 inside the zone; nearest-neighbour boson v = cos(k/2) ≤ 1.
  - No gauge-field symbol is used.
- **Lemma-M locality:** no TT or stress vertex is used.
- **Number-free ≠ forced:** see §6.
- **Bounded spectral classes:** "gapped" is not used.
- **Certificates:** no relaxation conflict is claimed. The LATTICE-STABILIZES exclusion is an explicit inequality inside a stated EFT class (H-EFT, operators suppressed by (h a)²), not a certificate.
- **Counterterm basis:** per scalar species, for the singlet mass.
- **Physical controls:** the comparator reproductions (§2). These are published-number comparisons, not controls in a target phase.
- **Readout bridges:** none; there is no finite-slot claim.
- **Forks.** SM-stable / lattice / new content. Excluded and not examined:
  - anthropics and P94 branching (setting);
  - active compensation (setting);
  - Higgs non-minimal coupling ξh²R and Hubble-scale effects (they act only at h ≳ M_P/√ξ ≫ h_I for ξ ≲ 1e8; reading);
  - non-EFT field-range bounds (reading, c4);
  - dimensional-transmutation origins of m_S (not tested).
- **Generic-GR comparison:** the stability analysis is particle physics, model-independent of the lattice except in §4(c3–c4).
- **Changed hypothesis:** SM-only content was removed (§0).

## 8. Prior art (counted once) and rechecks

- **R17-7 / vR17-7.** The SM numbers λ_min ~ −0.015 near 1e17 GeV and λ(M_P) ~ −0.013 were RECALLED order-of-magnitude values (`r177_gridvac_sector_cov.out:15-18`). This run replaces them with λ_min = −0.0113 (−0.0125 for λ_eff) at the primary inputs. The 1e112–3e120 ρ_Λ range is unchanged in order. The new lattice-independent lower bound is ≥ 2.6e108 ρ_Λ from h·a ≤ 1e-3.
- **R17-3 / vR17-3.** (S) is number-free and unforced (`vR17-3:17,19`).
- **P93 and P125:** `C5_S20_synthesis.md:388`; `C5_S23_synthesis.md:508,549`.
- **Repo Higgs-vacuum lane (counted once):**
  - `docs/VACUUM_CRITICAL_STABILITY_NOTE.md:22-45`: λ(M_Pl) = 0 boundary condition OPEN.
  - `docs/HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md:57,86`: framework y_t(v) = 0.918 ± 3%, bounded, Ward gate open.
  - `docs/P3_VACUUM_STABILITY_KNIFE_EDGE_IN_YT_ROBUSTNESS_NARROW_THEOREM_NOTE_2026-06-08.md`: the stability forecast is a central-value call.
  - **Reading.** The framework's own bounded y_t(v) = 0.918 sits about 0.8% below the measured MS-bar value, ≈ −1.4 GeV in M_t. That is near the boundary found here. If it were established it would make (S) nearly price-free; it is not established.
  - `scripts/frontier_higgs_mass_full_3loop.py`: two-loop coefficient discrepancy (§1; suggested; ≤ 0.1 GeV effect). Its "~10 GeV" two-to-three-loop shift claim was not used.
- **Rechecks (`S/recheck/`).**
  - All 6 R17-3 runners and 4 of 5 R17-7 runners reproduce their archived `.out` byte for byte.
  - `r177_enthalpy_orders.py` fails as archived: it imports `r113_profiles` from `../recheck/R11-3`, which is not beside it. With `scripts/C5/R11-3/r113_profiles.py` placed at that path, it reproduces byte for byte. **Archive path defect (minor).**

## 9. Notes for the referee

1. **LATTICE-STABILIZES excluded (bounded no-go), class:**
   - SM content to h ≤ 1e16 GeV;
   - V_eff valid as the constrained minimum energy for h·a ≤ 1e-3 (H-EFT);
   - lattice operators suppressed by (h a)^{2n}.

   Check c_min (§4 c1), the c3 order of magnitude, and the variational step e₀ ≤ min V_eff (e1). Not covered: lattice laws whose low-energy Higgs sector is not the SM Higgs above some scale ≪ 1/a. That case counts as stabilizer content, not "lattice at a = ℓ_P alone".
2. **The σ classification.** The primary row (pre-registered) gives 2.28σ, and the conclusion flips at an ambiguity of 0.64 GeV. Decide whether NEEDS-STABILIZER or OPEN is the honest fixed reading under RECALLED inputs.
3. **The singlet's tuning status.** "Content" for its couplings, but one relevant scalar-mass tuning on the lattice. Is that the right application of `TESTS:5700` and `C4_F3_referee.md:17`?
4. **The vector-like family.** One-loop gauge shifts only. Check that the omitted two-loop terms do not move M_F,max by more than about a factor 2 (suggested: small).
5. **Strong-word check.**
   - "global minimum": tree-level RG-improved two-field grid, not the full one-loop two-field potential.
   - "≥ 4e15": c_min / max |c_lat|, an order of magnitude.
   - "predicts M_t ≤ 170.9 GeV": (S) + SM-only + two-loop, RECALLED inputs, ± ~0.4 GeV.

## 10. Files

All under `S/`:
- `R18-2_report.md`;
- `PREREG.md`;
- `scripts/smrge.py`;
- `scripts/r182_{a_sm_stability, c_lattice, d_stabilizers, e_extras, f_coeffcheck}.py`, each with its `.out`;
- `recheck/R17-7/*.rerun`, `recheck/R17-3/*.rerun`, and `recheck/recheck/R11-3/r113_profiles.py`, the copy that resolves the archived import.
