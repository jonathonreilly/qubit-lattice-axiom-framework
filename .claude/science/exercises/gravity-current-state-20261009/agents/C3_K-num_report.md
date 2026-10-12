# C3 lane K-num: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee (lane K): INCONCLUSIVE; K-num rejected as a lane FAIL (bounded side result only); K-ana partially supported** (C3_K_referee.md).

**Verdict (worker):** FAIL, bounded to the implemented coupling (H1-H6): Euclidean scalar QED on Z^4 with one natural, universal "corner-metric" coupling to K7a-placed h, and a photon-mass IR regulator. One of the 5 anisotropic W(B4) forms (cA4, coefficient of q^2 sum_mu h_mumu^2) comes out at O(e^2) with |cA4|/|kappa2| = 0.229, i.e. 0.057 of the equivalent Einstein-Hilbert coefficient. It converges geometrically in box size to about 1% and is more than 400x above the 1e-4 threshold under every IR regulator tried. A second anisotropic combination (cA1+cA5) is also nonzero, at 0.26. The fixed setting's "best available stress" (K3a's optimized range-R stress) was NOT implemented, so for that setting the reading stays undecided (INCONCLUSIVE). Only 2 of the 5 anisotropic combinations were determined. Needs the codex sol referee before it is recorded.

**Plain summary:** I computed the O(e^2) induced quadratic action of K7a's staggered h on Z^4 for a stand-in of the fixed setting. The stand-in is Euclidean scalar QED with a natural, universal "corner-metric" coupling, not K3a's optimized stress, which has no Z^4 form and was not built. The action is exact in h, and the code matches an independent brute-force calculation to 3e-8. For waves along a lattice axis, the two transverse-traceless polarizations get different O(q^2) coefficients at O(e^2). No O(4)-invariant action, so no gauge-invariant one, allows that, and the difference isolates one of the 5 anisotropic W(B4) forms; a second anisotropic combination is also nonzero. With a photon-mass IR regulator the coefficient converges as the box grows (steps 2.1e-5, 5.1e-6, 1.0e-6, 2e-7) to 0.23 of the same-order TT coefficient (0.057 of the equivalent Einstein-Hilbert coefficient). It is unchanged by precision, gauge-parameter and q-grid checks and falls only mildly as the regulator is reduced (0.30 to 0.17); massless-photon runs do not converge at sizes I can reach. Read against the fixed criterion this is a FAIL for the tested coupling: keeping the grid with it costs a graviton-speed tuning on top of the mass tunings. It is not a test of the optimized stress, it determines only 2 of the 5 anisotropic combinations, and it needs the referee.

# Lane K (numeric worker), campaign C3: the cost of keeping the grid

**Worker:** Claude Opus 5.5, max effort, working independently of the analytic worker on this lane.
**Time:** 00:51Z (start), 01:06:29Z (PREREG stamped, before any computation), runs 01:11–01:33Z.
**Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/K-num/`
**Repository files:** none edited. **Downloads:** none. **CPU:** OMP/MKL/VECLIB threads = 2, every single run under 4 min, memory under 1 GB.

## Verdict

**FAIL against the fixed numeric criterion, bounded to the implemented coupling (H1–H6 below).**
- The O(e²) induced action contains a converged, nonzero anisotropic two-derivative form.
  - In the monomial basis, that form is A4 = q² Σ_μ h_μμ².
  - Its size is |cA4|/|κ₂| = 0.229. This is the pre-registered primary ratio, against the same-order TT image of the gauge-invariant form.
  - Against the equivalent Einstein–Hilbert coefficient 4κ₂ it is 0.057.
  - Either way it is more than 400× the 1e-4 FAIL line.
- A second anisotropic combination is also nonzero: cA1+cA5, with |cA1+cA5|/|κ₂| = 0.26.
- **Not decided:** the fixed setting's "best available stress (K3a's optimized range-R stress)" was **not** implemented. For that setting the lane stays **INCONCLUSIVE**.
- Per the C3 rules this FAIL goes to the codex sol referee before it is recorded.

## 1. What I read (in full unless stated)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines).
- **The packet:**
  - `TESTS.md`: the rules at the top and the whole "Campaign C3" section, including lane K's fixed readings.
  - `SUMMARY.md`, all of it.
  - `agents/B1_report.md` §5 (Test 2, plus Tests 1 and 3 for context).
  - `agents/B_referee.md`: items 1–18, the strongest combined statement and the ranked tests. Item 18 and ranked test 2 say to separate mass, kinetic anisotropy and higher-derivative terms, and that PASS means an exact identity or a systematic zero, not a small number.
  - `agents/kill_F2.md` and `agents/kill_F2_referee.md`.
- **Candidate pack `TEST_LOG.md`:** K7a, K3a, K3a′, K3a″, W1 (and the "where gravity stands" table).
- **Code read:** `test_K3a2/k3a2_lib.py` (all), `dense_e2.py` (first 80 lines), `decomp_L24.json`.
  - K7a's scripts were not re-run. I used K7a's placement and 9/4/1 count, and re-derived the count myself (below).

## 2. Setting and hypotheses (pre-registered in `PREREG.md`, 01:06:29Z)

- **H1. Lattice.**
  - A Euclidean Z⁴ torus L₁ × Lp³, periodic.
  - Hypercubic (kinetic-isotropy) regulator.
- **H2. K7a placement.**
  - h_μμ sits on sites; h_μν (μ≠ν) sits at plaquette centres x+(e_μ+e_ν)/2.
  - h_μν(x) = ε E_μν cos(q·pos), with q = (2πn/L₁) e₀ along a lattice axis, n = 0 (uniform), 1, 2, 3.
- **H3. Matter.**
  - One complex scalar of charge 1 and mass m.
  - A noncompact U(1) photon with the Wilson plaquette action.
  - Lorenz gauge fixing with parameter λ; constant photon modes removed.
  - **Not** staggered fermions.
- **H4. Coupling (a "corner metric").** At each site x and hyperoctant s ∈ {±}⁴, the corner metric is g_μμ = 1+h_μμ(x) and g_μν = h_μν(x+(s_μe_μ+s_νe_ν)/2).
  - Scalar: Σ_{x,s} (1/16) √g g^{μν} conj(D^s_μφ) D^s_νφ + m² Σ_x (1/16)Σ_s √g |φ|².
  - Photon: Σ_{x,s} (1/64) √g g^{μρ}g^{νσ} F^s_μν F^s_ρσ, with corner plaquettes.
  - The coupling is exact in h, W(B4)-covariant, exactly U(1)-gauge invariant and universal (light and matter see one metric), with the correct continuum limit.
  - It reduces to the standard actions at h = 0.
  - Its stress is natural, not optimized, and **not** exactly conserved.
- **H5. Order and formula.**
  - Γ = −log Z.
  - At O(e⁰): Tr log M_φ(h) + ½ log det K_A(h).
  - At O(e²): Γ₂ = ⟨M₂[A,A]⟩ − ½⟨(J·A)²⟩_c, an exact Wick contraction with the free propagators in background h. Ratios do not depend on e.
- **H6. IR regulator (added after the first runs; disclosed).**
  - An h-independent photon mass μ²A² is added to the photon operator. Matter and photon are both massive, so finite-size effects decay exponentially.
  - Gauge-parameter independence survives, because range(∇) remains an invariant subspace. This was checked numerically.
  - The massless photon was run first. It does not converge at reachable sizes (§5.6), which is why H6 was added.
- **H7. Directions.** Only q along a lattice axis was computed.

**Observable.**
- Π(q;E) := 4 × (the ε² coefficient of Γ/V), or 2 × that for uniform h.
- It is extracted from exact Γ at ε and 2ε with Richardson (q ≠ 0, where Γ is even in ε), or at ±ε and ±2ε (q = 0).
- Each channel is fitted as Π(q) = Π₀ + Π₂q² + Π₄q⁴ (+Π₆q⁶).

## 3. Method

**Algebra (EXACT; `forms.py`, `out_forms.txt`).**
- Reynolds averaging over all 384 elements of W(B4) gives a 9-dimensional space of two-derivative forms.
- Basis:
  - O(4)-invariant: I1 = q² h:h, I2 = |hq|², I3 = (qhq) tr h, I4 = q²(tr h)².
  - Anisotropic: A1 = Σ q_μ² h_μμ², A2 = Σ q_μ² h_μν², A3 = Σ q_μ² h_μμ tr h, A4 = q² Σ h_μμ², A5 = Σ q_μ q_ν h_μν h_μμ.
- The gauge-variation map has a 1-dimensional null space, EH = (I1 − 2I2 + 2I3 − I4)/4. That is K7a's Q, and it reproduces the 9/4/1 count.
- **Axis images (q = e₀).**

| Channel | Value in the basis |
|---|---|
| TT-E = (h11−h22)/√2 | c1 + cA4 |
| TT-T2 = h12 (normalized) | c1 |
| V = h01 | c1 + ½(c2+cA2) |
| S00 = h00 | Σ of all 9 coefficients |
| STR = tr⊥/√3 | c1 + 3c4 + cA4 |
| X (S00 × STR cross term) | (√3/2)(c3+cA3) + √3 c4 |

- **What the axis channels determine.** Six combinations: c1, **cA4 = Δ_TT := Π₂(TTE) − Π₂(TTT2)**, c2+cA2, c4, c3+cA3, and **cA1+cA5**.
  - Any O(4)-invariant form, and hence the gauge-invariant one, has Δ_TT = 0 and cA1+cA5 = 0 (EXACT).
  - In any basis of the anisotropic complement, Δ_TT = Σ_f w_f c_f, so max|c_f| ≥ |Δ_TT|/Σ|w_f|.
- **Pure-gauge channels (EXACT for K7a's placement).** At q ∥ e₀, h01 at x₀+½ and h00 at sites are lattice pure-gauge modes.
  - For example, ξ₁(x₀) = ε sin(qx₀)/(2 sin(q/2)).
  - In a gauge-invariant action these channels vanish at every q.

**Numerics (`knum_lib.py`).**
- Mixed representation: x₀ in real space, transverse directions in momentum space.
- The scalar is built in L₁×L₁ blocks and the photon in 4L₁×4L₁ blocks, both exact in ε.
- Propagators are taken to transverse real space by FFT.
- The exchange term is a sum over link pairs, with one link fixed at transverse position 0 by translation invariance. It uses the bilinear current terms generated from the corner action.
- The seagull term is local.

## 4. Validation and controls (CHECKED)

| Check | Result |
|---|---|
| Independent brute force (`bruteforce.py`): real-space M(A) built with explicit link phases; Γ₂ = ½Σ_n λ_n ∂²_t log det M(t v_n) over photon eigenmodes; L₁=4, Lp=3, random full E, q = 0 and π/2, ε = 0.15 | Γ₀ agrees to 2e-13. Γ₂ agrees to 5–6e-8 (3e-8 relative); the h-induced part of Γ₂ agrees to 3e-5 relative (`out_bruteforce.txt`) |
| W(B4) covariance (relabel transverse axes: TTE ↔ TTE_23, TTT2 ↔ TTT2_13; L₁=32, Lp=4) | Identical to ≤ 2e-12 |
| Gauge-parameter independence, λ = 0.5 vs 1 (Lp=6, μ²=1) | cA4 = −5.246733e-5 vs −5.246730e-5 |
| ε precision and Richardson, ε = 0.02 vs 0.01 | cA4 = −5.246764e-5 vs −5.246730e-5. Unextrapolated values differ by about 1e-4 relative, as ε² predicts |
| q-grid and fit: L₁ = 32 vs 24 (different q values); 4-parameter vs 3-parameter q-fit | −5.2489e-5 vs −5.2488e-5; −5.2488e-5 vs −5.2467e-5 |
| W(B4) mass relation V(q=0) = TTT2(q=0), which links axis 0 to the transverse axes | Lp=10: 1.27338e-3 vs 1.27332e-3 |
| Noise per realization | Not applicable: the computation is deterministic, with no sampling |

Note: numpy's batched `slogdet` on this Mac prints spurious floating-point warnings (divide by zero, overflow). All log-determinants are finite and match the brute force.

## 5. Results

### 5.1 The O(e²) anisotropy witness and its convergence

Settings: m² = 1, μ² = 1, L₁ = 24, the same 3-parameter q-fit (n = 0, 1, 2) in every row. Numbers are coefficients per e², per cell.

| Lp | cA4 = Δ_TT | κ₂ = TT kinetic coefficient | \|cA4\|/\|κ₂\| | \|cA4\|/\|4κ₂\| | Step in cA4 |
|---|---|---|---|---|---|
| 6 | −5.2467e-5 | −1.1073e-4 | 0.474 | 0.118 | |
| 8 | −3.1348e-5 | −1.1009e-4 | 0.285 | 0.071 | +2.11e-5 |
| 10 | −2.6286e-5 | −1.0963e-4 | 0.240 | 0.060 | +5.06e-6 |
| 12 | −2.5255e-5 | −1.0949e-4 | 0.231 | 0.058 | +1.03e-6 |
| 14 | −2.5060e-5 | −1.0946e-4 | 0.229 | 0.057 | +1.9e-7 |

- **The steps fall geometrically,** by about ×0.2 per two sites, so the limit is about −2.50e-5. This is a direct computation, not a long extrapolation.
- **Channel values at Lp=14:** Π₂(TTE) = −1.220e-4 and Π₂(TTT2) = −9.69e-5.

### 5.2 IR-regulator dependence (largest box per regulator)

| m² | μ² | Lp | cA4 | κ₂ | \|cA4\|/\|κ₂\| | \|cA4\|/\|4κ₂\| | Convergence |
|---|---|---|---|---|---|---|---|
| 2 | 2 | 10 | −1.370e-5 | −4.519e-5 | 0.303 | 0.076 | steps 3.9e-6, 4.6e-7 |
| 1 | 1 | 14 | −2.506e-5 | −1.095e-4 | 0.229 | 0.057 | §5.1 |
| 1 | 0.5 | 10 | −2.491e-5 | −1.186e-4 | 0.210 | 0.053 | steps 2.2e-5, 5.4e-6 |
| 1 | 0.25 | 14 | −2.235e-5 | −1.238e-4 | 0.181 | 0.045 | step 2.1e-7 (12 → 14) |
| 1 | 0.1 | 12 | −2.142e-5 | −1.277e-4 | 0.168 | 0.042 | single size |

- The ratio falls only mildly as μ decreases and is levelling off (0.23 → 0.18 → 0.17).
- **μ → 0 (ARGUED).** Power counting with massive charged lines gives an IR-finite O(q²) coefficient at O(e²), so the limit should be finite. Simple fits give 0.14–0.16. That limit is argued, not computed.

### 5.3 Axis decomposition into W(B4) forms (Lp=12, μ² = m² = 1)

| Order | c1 (I1) | **cA4** | c2+cA2 | c4 (I4) | c3+cA3 | **cA1+cA5** |
|---|---|---|---|---|---|---|
| O(e²) | −9.687e-5 | **−2.526e-5** | 1.948e-4 | −6.616e-5 | −4.595e-5 | **2.800e-5** |
| O(e⁰) | 1.265e-2 | **2.568e-2** | −2.702e-2 | 5.891e-3 | −2.362e-2 | **1.270e-2** |

- **Second witness, cA1+cA5 (μ²=1):**

| Lp | cA1+cA5 | \|cA1+cA5\|/\|κ₂\| |
|---|---|---|
| 6 | 4.10e-5 | 0.37 |
| 8 | 3.32e-5 | 0.30 |
| 10 | 2.90e-5 | 0.26 |
| 12 | 2.80e-5 | 0.26 |

  - The steps fall (−7.8e-6, −4.2e-6, −9.9e-7), so the limit is about 2.77e-5.
- **The isotropic part is not Einstein–Hilbert-shaped either.** EH requires c4 = −c1 = +9.7e-5; the measured c4 is −6.6e-5.
- **Undetermined:** cA2, cA3 and cA5 separately. They need an off-axis q, which was not run.

### 5.4 Mass terms (separated per referee item 18) and pure-gauge channels

- **W(B4) mass numbers** for α h:h + β Σh_μμ² + γ(tr h)², at Lp=10, μ²=1:

| Order | α | β | γ |
|---|---|---|---|
| O(e²) | 1.2733e-3 | −1.0941e-3 | 1.0e-5 |
| O(e⁰) | 0.2982 | −0.1790 | −0.0935 |

  - The consistency check on STR converges with box size: at O(e²), 2.154e-4 measured vs 2.092e-4 predicted.
- **Pure-gauge channels at Lp=12 (O(e²)).** In a gauge-invariant action both would be identically zero.
  - V: mass 1.274e-3, q² coefficient 5.2e-7.
  - S00: mass 1.89e-4, q² coefficient −1.15e-5.
  - So the Ward-identity violation is mostly a mass term in the pure-gauge channels, but it is genuinely O(q²) in the TT channels.
- **Comparator (COMPARATOR only):** K3a″ (walker fermions, Hamiltonian, uniform strain) had two TT shear numbers of opposite sign, about 1e-2 per e² per cell. The model and normalization differ.

### 5.5 Free level, O(e⁰)

- The natural coupling is already strongly anisotropic at O(e⁰): Π₂(TTE) = 0.0383 vs Π₂(TTT2) = 0.01265, so |cA4|/|κ₂| ≈ 1.0 for every regulator.
- The O(e⁰) masses are cutoff-sized.
- K3a says an exact free stress exists, so this free-level part could in principle be removed by designing the coupling. The O(e²) part is the subject of the test.

### 5.6 Massless photon (μ = 0, m² = 0.25, L₁ = 32): NOT converged, not used for the verdict

| Lp | \|cA4\|/\|κ₂\| at O(e²) | Π₂^(e²)(TTE) |
|---|---|---|
| 4 | 3.68 | 9.1e-3 |
| 6 | 6.67 | 1.95e-4 |
| 8 | 0.18 | −3.5e-4 |

- The O(e²) TTE mass follows a + b/Lp⁴ (b ≈ 0.91, a ≈ −5e-5), checked on three sizes.
- **Diagnosis (ARGUED).** The massless photon's direction-dependent k→0 integrand gives Riemann-sum errors of order (L₁/Lp)/V, and these errors are amplified in Π₂ by 1/q². This is why H6 was added.
- The free level converges in this series too (0.79 → 0.89 → 0.91).

### 5.7 Non-universal coupling family (Lp=8, μ²=1)

- Here matter sees x_f h and the photon sees x_γ h, giving cA4 = A x_f² + B x_f x_γ + C x_γ².
- A = −8.92e-5 (matter only), C = −3.29e-5 (photon only), B = +9.07e-5.
- B² − 4AC < 0, so no real ratio x_f/x_γ removes cA4 at this size. Like K3a″'s face channel, the zero cannot be bought by a non-universal coupling. This holds at Lp=8, which is not converged.

## 6. Reading against the fixed criterion

- **FAIL criterion:** "any of them converged at ≥ 1e-4 relative to the gauge-invariant form".
  - cA4 has converged to about 1% in Lp, at 0.229 (same order), 0.057 (EH-equivalent), and 0.17–0.30 across regulators.
  - cA1+cA5 is 0.26.
  - Both are stable under ε, λ and the q-grid. So the criterion is met for the implemented coupling.
- **PASS** would need an exact identity or a systematic approach to zero. Neither is seen: the witness converges away from zero.
- **Consequence (ARGUED).** For this coupling, keeping the grid costs a graviton-speed tuning on top of the W(B4) mass numbers. A ≥10% relative splitting of the induced TT speed² is far above the GW170817 level.

## 7. Labels

- **EXACT:**
  - the 9/4/1 dimension count and the basis;
  - O(4)-invariant forms give Δ_TT = 0 and cA1+cA5 = 0;
  - Δ_TT = cA4 in the monomial basis;
  - V and S00 at q ∥ axis are pure gauge for K7a's placement;
  - λ-independence holds with an h-independent photon mass (invariant subspace).
- **CHECKED:** every number in §4–§5.
- **ARGUED:**
  - the μ → 0 limit;
  - the finite-size mechanism of §5.6;
  - the physical speed-tuning consequence;
  - any statement about the optimized stress.
- **COMPARATOR:** K3a″ and K7a.
- **Strong words:**
  - "Converged" means the last step is below 1% of the value, with geometric steps.
  - "FAIL" is scoped to H1–H6.

## 8. What a referee should re-check

1. **Scope.** Is H4, a natural universal corner-metric coupling of scalar QED, an acceptable stand-in for "the best available stress"?
   - The O(e²) anisotropy depends on the coupling.
   - A designed or optimized stress, with K3a′'s defect falling as about R^-2.9, could shrink it.
   - Fermions (staggered or walker) were not run.
2. **Normalization.** I pre-registered the same-order ratio (0.229).
   - At physical α, against the free-level induced TT coefficient, the number is |cA4| e²/κ₂^(0) = 2.50e-5 × 0.0917 / 0.0255 ≈ 9e-5, just **below** 1e-4.
   - Against 4κ₂^(0) it is 2.2e-5.
   - In that normalization the free level itself is O(1) anisotropic (§5.5). The referee should rule on the normalization.
3. **IR.** The massless-photon runs did not converge. The μ → 0 limit is argued, not computed. Check the trend in §5.2.
4. **Coverage.** Only 2 of the 5 anisotropic combinations were determined, from axis q only. An off-axis q (2D supercell) is the next computation.
5. **Formula.** Re-derive Γ₂ = ⟨M₂[A,A]⟩ − ½⟨(J·A)²⟩_c and re-run `bruteforce.py`. It is independent: it builds the real-space matrix with explicit phases and uses photon eigenmodes.
6. **Larger box.** Check Lp = 16 for μ² = 1 and 0.25, and cA1+cA5 at Lp = 14.
7. **Pure-gauge claim.** Confirm that h01 and h00 at q ∥ e₀ are exact K7a pure-gauge modes.

## 9. Files (all in the scratch folder above)

**Code and pre-registration**
- `PREREG.md`, `prereg_stamp.txt` (01:06:29Z).
- `knum_lib.py` (the library), `knum_lib_x.py` (non-universal variant).
- `bruteforce.py` with `out_bruteforce.txt`; `forms.py` with `out_forms.txt`.
- `run_channels.py`, `run_channels_x.py`.
- `analyze.py`, `table.py`, `summary.py`, with outputs `out_summary.txt` and `out_table.txt`.

**Raw results** (`res_<tag>.json`; logs `log_<tag>.txt`)
- Massive-regulator runs: tags M24p{6,8,10,12,14}mu1, M24p10mu1b, M24p12mu1b, M24p{6,8,10}mu05, M24p{12,14}mu025, M24p12mu01, H24p{6,8,10}mu2, M32p6mu1.
- Checks: M24p6mu1lam05, M24p6mu1eps02.
- Non-universal coupling: XF24p8mu1, XG24p8mu1.
- Massless: L16p4, L32p4, L32p6, L32p8, L64p6. The L32p6, L32p8 and L64p6 runs were stopped early and are partial.
- Derived fit files: res_X*, res_Y_*.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** False

**Corrected verdict:** Lane K is INCONCLUSIVE. It was not computed in the fixed setting: lattice QED (staggered fermions, as in K3a) coupled through K3a's optimized range-R stress. That stress is a 3D Hamiltonian momentum charge with no Z^4 stress tensor, so the fixed setting probably cannot be implemented as written and should be re-registered. It should not be recorded as a lane K FAIL.

The worker's computation is a bounded side result for a substitute model. The model is Euclidean scalar QED on Z^4 with:
- K7a's placement;
- the natural corner-metric coupling, which has no conserved stress;
- cutoff-scale masses (scalar m^2 in {1, 2});
- an h-independent photon mass, added after the first runs (mu^2 in [0.1, 2]).

The side result (CHECKED: reproduced, extended to Lp=16, insensitive to regulator form at about the 13% level): in that model the O(e^2) induced action has a converged, nonzero W(B4)-anisotropic two-derivative term. Delta_TT = cA4 gives |cA4|/|kappa2^(e2)| = 0.2286 at mu^2 = 1, Lp = 16, and 0.17 to 0.30 across the regulators. cA1+cA5 is also nonzero, at about 0.26.

What the side result covers: it rules out protection for this implementation only (referee item 18). It does not decide whether the best stress, or any conserved stress, removes the anisotropy. Two further limits:
- The worker's own pre-registered primary setting (m = 0.5, massless photon) did not converge. By the pre-registered mapping that is INCONCLUSIVE.
- In the physical normalization (e^2 = 4 pi alpha, against the free-level TT coefficient) the ratio is about 9e-5, below the 1e-4 line.

If it goes to the sol referee, it should be labelled as the bounded substitute-model result, not as a lane K FAIL.

**Issues:** 1. Wrong setting, so the fixed FAIL does not apply. TESTS.md lane K fixes "K7a's staggered h on Z^4, coupled to lattice QED through the best available stress (K3a's optimized range-R stress)". The worker ran a complex scalar, not lattice-QED fermions, with a natural corner-metric coupling, not the optimized stress. The FAIL reading is defined for the fixed setting. The worker itself says the fixed setting stays INCONCLUSIVE, yet the headline reads "FAIL against the fixed numeric criterion". That claims more than was computed, which breaks headline-scope discipline. Referee item 18 (B_referee.md:202-208) says a failed scalar matter model "excludes that implementation, not an entire substrate class".

2. The result cannot answer the test's question. K7a (TEST_LOG.md:28) already says that without exact gauge invariance the 5 anisotropic forms are allowed, and that protection "hangs on K3a", i.e. on a conserved stress. The implemented coupling has no conserved stress, and its Ward identity is badly broken:
   - free-level (O(e^0)) anisotropy |cA4|/|kappa2| is about 1.0;
   - O(e^0) masses are cutoff-sized (0.298, 0.119);
   - the O(e^2) mass in the pure-gauge V channel is 1.27e-3, about 12 times |kappa2^(e2)|;
   - the q^2 coefficient in the pure-gauge S00 channel is nonzero (-1.15e-5).
   So nonzero O(e^2) anisotropy is the generic expectation here. It cannot separate anisotropy generated by the interaction from the coupling's own non-conservation, which is exactly what the best-stress setting was meant to remove. For this coupling the speed tuning is already needed at O(e^0), so the stated FAIL consequence adds nothing.

3. Departure from the worker's own pre-registration. PREREG.md (01:06:29Z) set the primary as m = 0.5 with a massless photon, and maps "no convergence" to INCONCLUSIVE. That primary run did not converge (report section 5.6), so it reads INCONCLUSIVE. H6 (an h-independent photon mass, with m^2 raised to 1) was added after seeing those runs. The converged FAIL comes from that post-hoc setting.
   - The H6 mass mu^2 A^2 is itself a non-covariant, diffeomorphism-breaking term of cutoff size, so it adds Ward-identity breaking at the same order.
   - My covariant-Proca replacement, with the same mass at h = 0, moves cA4 by 9-13%: -4.76e-5 vs -5.25e-5 at Lp=6, and -2.29e-5 vs -2.63e-5 at Lp=10.

4. Continuum scaling is not addressed, though referee item 18 asks for it. Every converged run has m^2 and mu^2 at or above 0.1 in lattice units, so correlation lengths are at most about 3 sites. The physical regime m*a -> 0 is untested. The mu -> 0 limit is only argued, and the direct massless-photon runs did not converge.

5. The FAIL depends on normalization. The same-order ratio (0.229) was pre-registered. In the physical normalization (e^2 = 4 pi alpha, against the free-level TT coefficient) the ratio is 9.0e-5 (2.2e-5 against the EH-equivalent 4*kappa2^(0)). That is below the 1e-4 FAIL line. Referee item 18 says fixed thresholds are not substitutes for physical normalization. (Physically a 1e-5 speed split would still conflict with GW170817, but that is ARGUED and outside the fixed line.)

6. The independent check is narrower than stated. bruteforce.py imports the same corner_metric (a, C, bbar) as the fast code and tests only the massless-photon (mu^2 = 0) path. It validates the O(e^2) Wick formula, not the coupling definition or the H6 path. This is minor.

7. Only 2 of the 5 anisotropic combinations were determined, from axis q only. That is enough for "any of them", so it is not a defect for a FAIL, but it limits the decomposition.

The numbers themselves hold up. All values, the 9/4/1 form count, the axis images and the pure-gauge identification of h01 and h00 at q along e0 were reproduced or re-derived by hand.

**Re-runs:** All runs used OMP/MKL/VECLIB = 2 and finished in under 3 minutes each. My scripts are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/K-num/verify/. They import the worker's knum_lib read-only.

(a) Reproduction, repro.py (24 6 1 1 1 0.01). I re-extracted the uniform-h value with my own 5-point stencil.
   - O(e^2): cA4 = -5.246730e-5, kappa2 = -1.107298e-4, ratio 0.4738.
   - O(e^0): ratio 1.0100.
   - Identical to the worker's M24p6mu1.

(b) Brute-force re-run (out_bruteforce_rerun.txt): dG0 = -2.3e-13 and 1.1e-13; dG2 = 5.2e-8 and -6.3e-8. This matches the worker's output.

(c) New larger box, Lp = 16, mu^2 = m^2 = 1 (out_Lp16_mu1.txt).
   - O(e^2): cA4 = -2.5025e-5, kappa2 = -1.0945e-4, ratio 0.2286.
   - The step from Lp = 14 is +3.5e-8, after +1.9e-7, a factor of about 0.18. The steps are geometric, so the mu^2 = 1 value has converged.
   - O(e^0): ratio 1.0074.

(d) Regulator-form check, proca.py. The h-independent photon mass is replaced by a metric-covariant Proca mass, (1/2) mu^2 sum_{x,s} (1/16) sqrt(g) g^{munu} A'_mu A'_nu, which equals the original at h = 0.
   - Lp = 6: cA4 = -4.762e-5, ratio 0.426 (worker's form: -5.247e-5, 0.474).
   - Lp = 10 (out_proca_Lp10.txt): cA4 = -2.286e-5, ratio 0.206 (worker's form: -2.629e-5, 0.240).
   - The O(e^0) TTE mass moves from 0.119 to 0.056.
   - So the anisotropy survives the change of regulator, but the number depends on the regulator at the 10-15% level.

(e) By hand, I re-derived the axis images of the 9 forms (TTE = c1+cA4, TTT2 = c1, V = c1 + (c2+cA2)/2, S00 = sum of all 9, STR = c1 + 3c4 + cA4). I also re-derived the EH null vector (I1 - 2I2 + 2I3 - I4)/4, and confirmed that h01 and h00 at q along e0 are K7a pure-gauge modes. I checked the arithmetic of the physical-alpha figure: 2.50e-5 x 0.0917 / 0.0255 = 9.0e-5. I checked that the photon normalization is (1/4)F^2, so e^2 = 4 pi alpha is the right conversion.

Not run: anything in the fixed setting (fermions with K3a's optimized stress), m^2 -> 0, and off-axis q.
