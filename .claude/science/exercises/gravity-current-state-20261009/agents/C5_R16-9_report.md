# C5 R16-9 report: one law, every cone — can one subluminal edge family meet the photon, electron and graviton cones and the shear condition together? What is the bill?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 23:09Z to 23:46Z. No repository file was edited. No downloads, no web lookups.

**Scratch.** `S/` = `.../scratchpad/C5/R16-9/`. Scripts and `.out` files are in `S/scripts/` (Dirac recheck in `S/scripts/dirac/`). Every run took under 4 min at `OMP_NUM_THREADS=2`. Superseded (unconverged, no-gradient) runs are kept in `S/scripts/superseded/` and not used.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method and readings (`:2302-2320`); R13-5 (`:4668-4678`, `:4707-4714`); R13-7 (`:4736-4745`, `:4844-4858`); R13-8 (`:4747-4757`, `:4803-4807`); R14-1 (`:4781-4802`, `:4808-4813`); R14-3 (`:4830-4843`, `:4915-4922`); round 16 (`:5037-5149`, `:5210-5221`, `:5246-5257`, `:5359-5369`); my item (`:5371-5400`).
- `agents/C5_R16-1_report.md`, `C5_R16-2_report.md`, `C5_R16-3_report.md` (all), and the three referee verdicts that appeared during the run: `scratchpad/C5/ref_R16-1/REFEREE_VERDICT.md` (`vR16-1`), `ref_R16-2/REFEREE_VERDICT.md` + `R16-2_referee_verdict.md` (`vR16-2`), `ref_R16-3/REFEREE_VERDICT.md` (`vR16-3`).
- `agents/C5_R14-3_report.md` (§§ used below) and `C5_R14-3_referee_verdict.md` (`vR14-3`); `C5_R13-8_referee_verdict.md` (`vR13-8`); `C5_S17_synthesis.md` (W1–W5, P61–P73: `:177-181`, `:215-217`, `:227`); `SUMMARY.md` §26 (`:677-714`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **The listed conditions fall into two blocks that share no knob (proved, from refereed lemmas).** The charged-matter cones depend only on the Dirac edge, the photon edge and the counterterms (R16-2 Lemma Q, `vR16-2:5`). R9-9's graviton vertex is a scalar-loop vertex, so the graviton cone (E_g, T₂g) and the shear μ_E, as they are defined in this chain, depend only on the scalar edge. In the stated SM content there are no physical charged scalars (`C5_R16-2_report.md:85`), so the scalar edge does not enter the charge block. The question splits into "does each block close?" and the count adds.
2. **Charge block: closes with tunings only, never with a subluminal shape (refereed inputs).** R16-1 (DERIVED, `vR16-1:3,19`) and R16-2 (OPEN, conditional count, `vR16-2:17`) leave 3 tunings (one per (spin, |q|) class) or 7 (one per species). A zigzag Dirac edge does not help: the Peierls tadpole is *exactly* −πw(π) + ∫(q − S)w′ (`R16-2_referee_verdict.md:66-72`), and pulling S further below q makes it more negative (proved, §3.6).
3. **Gravity block: the graviton cone and the shear condition do not fit on one subluminal scalar edge (checked, class-wide, referee needed).** R16-3 (refereed) zeroes E_g and T₂g with two edge-shape tunings. Adding μ_E = 0 fails everywhere I looked:
   - I built a relaxation that provably contains every law in R14-3's subluminal class 𝒮, for the M vertex (Lemma R, §3.2). Over 203 parameter cells of it, at m = 0.1 and 0.01, the smallest μ_E found at a graviton-cone-feasible point is **+1.25e-3** (it is +1.4e-3 to +6e-3 in typical cells). The dual search (best graviton cone with μ_E ≤ 0) never reaches zero: best min(Ξ_Eg, Ξ_T2g) = **−1.07e-3**.
   - For the U vertex, a second relaxation that is valid for both vertices (Lemma R_U, §3.2) gives a smallest μ_E of **+1.3e-4** at m = 0.01, and **+3.0e-4** at m = 0.1 with b ≥ 0.3. A slope-resolved search agrees (+5.4e-4). The U margin is thin.
   - The only negative μ_E values ever found needed something no law can do. They used fast states at levels near π, which σ ≤ k forbids, or "flat" climbs between levels, which the coarea constraint forbids (§3.4).
   - **Why (proved identity, plain reading).** For fast zigzag states, μ_E is a weighted average of a(5a − 1) and the graviton cone is a weighted average of a²(a − 1), where a(t) is the band's running "dimension" (§3.3). The cone needs a > 1 somewhere; the shear needs a < 1/5 to dominate. Flats lower μ_E but lower the cone with them.
4. **So JOINT fails on the shape family, and the cheapest fix is one non-shape knob.** That knob is an E_g shear-mass counterterm, or pairing (P46), or the empty Fock vacuum, where Ξ ≡ μ_E ≡ 0 (`C5_R16-3_report.md:38`). With it, the bill for the listed conditions is **6 tunings** (3 charge + 2 graviton-cone shape + 1 shear) with per-class counterterms, or **10** with per-species counterterms. In R13-8's rows it is **9 + CC**, or 13 + CC, against R13-8's N_s + 7 = 16 + CC (§3.7).
5. **Two holes the item's conditions do not cover (reading).**
   - E_g and T₂g are the *axis* TT speeds only. Cubic symmetry leaves two more TT speed rows off-axis, which nobody has computed.
   - The Dirac, photon and gluon zero-point loops also shift the graviton cone and the shear, but no vertex for them exists in the chain. If they enter as sums with the opposite sign for fermions (R13-5's stipulated convention), the scalar-edge conflict might be lifted by those edges. That is unchecked.

**Against the FIXED readings (`TESTS:5396-5399`): CONFLICT (worker reading; referee required, because the claim is class-wide).** The conflicting pair is {graviton cone: Ξ_Eg = Ξ_T2g = 0} against {μ_E = 0} on one subluminal scalar edge in 𝒮. This holds for both vertices via proved relaxations (Lemma R for M, Lemma R_U for both) plus scans. The margin is μ_E ≥ +1.25e-3 for M and ≥ +1.3e-4 for U. The demonstration is a multi-start scan of a superset, not a certified global minimum. If the referee requires a proof, the reading falls to OPEN. The expectation (`TESTS:5400`, "CONFLICT or OPEN with P62") is met.

---

## 1. Hypotheses and class (stated before any title)

- **Laws.**
  - **Scalar edge:** R14-3's separable class 𝒮. ε² = m² + Σᵢ g(kᵢ), g = σ², σ ∈ C², σ(0) = 0, σσ′(π) = 0, |σ′| ≤ 1 (`C5_R16-3_report.md:33`). The box is σ = k on [0, b]. The edge is required to stay above a valley floor σ ≥ s_min > 0, so there are no extra light zeros.
  - **Dirac edge:** R14-1's D1(b, r): h = Σ s(k_j)α_j + (m + ΣW(k_j))β, W′ = r√(1 − s′²) (`C5_R16-2_report.md:51`). The "D1/zigzag hybrids" are D1 with zigzag stretches in s.
  - **Photon:** R8-5's Peierls photon. Nondecreasing d is needed where Lemma T′ is used.
- **Graviton cone.**
  - R9-9 Theorem T with its M and U vertices, q ∥ z (`C5_R16-3_report.md:35-36`).
  - **Ward requirement: standard first-order W1, assumed, not built** (`vR16-3:17`). No second-order identity, standard or deformed, is used.
  - **Vacuum:** the supplied scalar zero-point vacuum.
  - Ξ is the bare-cone shift, not the dressed split (`vR16-3:17`).
  - Defined for scalar loops only. Dirac, photon and gluon loop contributions are **not defined** in the chain and are not computed.
- **Shear.** μ_E = (1/12)⟨(3f_x²f_y² − f_x⁴)/ε³⟩ = −(5/72)⟨K₄(f)/ε³⟩ (`vR14-3:5-8`), for the scalar edge, in the supplied vacuum.
- **Charge block.** One-loop Peierls QED, Feynman gauge, fixed λ > 0, as in R16-2 (`C5_R16-2_report.md:45-87`). The SM content there is nine charged Dirac flavours.
- **Counterterms.** Counted as in R16-2: each edge-shape equation, the photon counterterm, and each matter counterterm counts once, under readings (i) per species and (ii) per (spin, |q|) class (`C5_R16-2_report.md:66-70`). For gravity, a counterterm is not part of "the stated family" (edge shapes). Where I use one, it is named as a price.
- **Masses.** m = 0.1 and 0.01 (plus 0.03 spot checks), inside the registered m ≤ 0.3. Ξ and μ_E are real-analytic in m² on 𝒮 with a gapped edge (`vR14-3:18`; `C5_R16-3_report.md:221`), so m ↓ 0 is continuous.
- **Round-16 head rules (`TESTS:5039`).**
  - Every law states its whole-zone v_max.
  - No frame-tied kernel is introduced.
  - Every Ward statement is the standard W1, assumed.
- **Tail clause.** Raw Fourier coefficients |ε_r| of ε_1D = √(0.09 + g), **nothing subtracted** (as R16-3).
- **Excluded:**
  - pairing (used only as a named escape);
  - deformed W2 (R16-5);
  - q off-axis;
  - two loops;
  - non-separable scalar laws;
  - W±;
  - Dirac/photon/gluon TT and shear vertices (not in the chain).

## 2. Prior art (each counted once)

- **R16-3** (`C5_R16-3_report.md`; `vR16-3`, CONFIRMED WITH CORRECTIONS).
  - Z1 and the convex-mix simultaneous E_g/T₂g zero (M at m = 0.1 confirmed to 1.5e-17, `vR16-3:13`).
  - The relaxed monotonicity F₂ ≤ G₁ for vertex M (`C5_R16-3_report.md:142`).
  - P62 "not found" (`:228-234`; `vR16-3:13`).
  - Tails corrected to |ε_128| = 3.67e-5 (`vR16-3:17`).
- **R16-2** (`vR16-2`, OPEN confirmed). Lemma Q, Lemma T′ and its exact IBP identity (`R16-2_referee_verdict.md:61-88`), the conditional 7/3 count, and the finding that κ_γ is replaceable (`vR16-2:13`).
- **R16-1** (`vR16-1`, DERIVED). On D1 (0 < r ≤ 1/√3) the split cannot vanish on a mass interval, so it needs a tuning. D1 has v_max ≤ 1, with equality at r = 1/√3 (`vR16-1:15`).
- **R14-3** (`vR14-3`). The K₄ form of μ_E, the G_w shear root (P62), Theorem B on 𝒰₀, and analyticity.
- **R13-8** (`vR13-8:15-22`). The P,T-even rows: N_s speeds + 1 graviton speed + 3 anisotropies + 2 masses + 1 LV tadpole. μ_T₂ vanishes for V3's local one-loop coupling.
- **R13-5** (`TESTS:4707-4714`). Matched pairing cancels the *stipulated* TT response. This is the only place fermion TT contributions appear, and only by stipulation.
- **S17** P61–P63, P73 (`C5_S17_synthesis.md:215-217,227`).
- **Grep.** I searched `agents/`, `TESTS`, `SUMMARY` for "Young", "occupation measure", "coarea", "one law", "every cone".
  - "Young" appears only in R16-3's relaxed problem (`C5_R16-3_report.md:141-145`). That problem has no flats, no μ_E and no path constraint. Lemma R below extends it, and it is counted once.
  - Other hits (R6-1, R12-4, RC_C1) are unrelated.

---

## 3. Results

### 3.1 Rechecks of the archived runners (checked; `recheck.out`, `dirac/r169_dirac_check.out`, `relaxed_validate.out`)

- **R16-3 `zz.py` (copied unmodified):**
  - NN scalar at m = 1: M,T2g −1.903007e-3, M,Eg −8.301857e-4, U,T2g −2.289166e-4, U,Eg −6.883237e-5; μ_E +1.97038864e-3. These are R9-9's and V3's values to all printed digits.
  - Z1 at m = 0.3: M,T2g +3.904715e-4, U,T2g +2.810149e-4, μ_E +1.2273e-2, v_max 0.984560. These are R16-3's and the referee's values.
  - G(1.4): μ_E(m = 1) = +3.52543170e-3, as R14-3.
  - R16-3's zeros re-evaluated at their printed (u, v): M m = 0.1 residuals ≤ 5e-9 (rounding of the 6-digit weights), μ_E +6.19e-3. U m = 0.1: μ_E +6.57e-3. M m = 0.01: μ_E +6.04e-3. All are as reported.
- **R16-2 Dirac runner (copied unmodified):** D1(1.4, 1/√3), naive photon, m = 0.1, N = 128, λ = 0.02 gives F₁/₂ = −10.0481 (tadpole −9.7582) and G₁/₂(0.05) = +0.6645. These are exactly R16-2's numbers (`r162_dirac_family_N128.out:34`).
- **My relaxed evaluator against `zz.py`:** on box + flat laws (b = 1.0, 0.7; wt = 0.002), M and U Ξ and μ_E agree to ≤ 1e-3 relative. The difference is the wt smoothing.

### 3.2 Lemma R: a relaxation containing every law in 𝒮 (proved)

Fix b and s_min. For σ ∈ 𝒮 with box [0, b] and edge σ ≥ s_min on [b, π], let ν be the edge's occupation measure on (level h = σ(k), slope s = |σ′(k)|), of mass π − b. The M-vertex Ξ_Eg, Ξ_T2g and μ_E are functionals of the 1D zone moments E0, F2, F4, G1, G2 (`zz.py:58-92`). Then:

- **(R1) Mixture.** Replace each (h, s) by mass s² at (h, s = 1) and 1 − s² at (h, s = 0).
  - E0, G1, G2 (functions of h) and F2 (∝ s²h²) are unchanged.
  - F4 goes from s⁴h⁴ to s²h⁴ ≥ s⁴h⁴.
  - Ξ_M,Eg and Ξ_M,T2g depend only on (E0, F2, G1, G2), so they are unchanged.
  - μ_E ∝ ∫t^{1/2}e^{−tm²}E0(3F2² − F4E0)dt decreases or stays equal, since E0 > 0.
- **(R2) Occupation.** The edge's levels form an interval [lo, hi] ∋ b (continuity). By the coarea formula, mass at levels in any A ⊂ [lo, hi] is ≥ ∫_{σ⁻¹(A)}|σ′|dk ≥ |A|. (R1) preserves the level marginal.
- **(R3) σ ≤ k.** σ(0) = 0 and |σ′| ≤ 1, so edge mass at levels ≥ h is ≤ π − h.

So the set 𝓡(b, s_min) = {box + measures on levels × {0, 1} obeying (R2), (R3)} contains the M-data of every law in 𝒮 with that box and floor, with μ_E lowered or equal. Hence:

  min{μ_E : Ξ_M,Eg ≥ 0, Ξ_M,T2g ≥ 0} over 𝓡  ≤  the same minimum over 𝒮. ∎

- (R2) in this form uses total mass ≥ |A|, which is weaker than coarea, and so enlarges 𝓡. That is allowed for a lower bound.
- For U, Ξ_U depends on F4, so (R1) is not monotone there. Lemma R_U below handles both vertices.

**Lemma R_U (proved; both vertices).** For each level bin A of the edge, set M_A = ∫_{σ⁻¹(A)} dk, P_A = ∫ s² dk and Q_A = ∫ s⁴ dk. Every law in 𝒮 satisfies:
- 0 ≤ Q_A ≤ P_A ≤ M_A, since s ≤ 1.
- P_A² ≤ Q_A M_A (Cauchy–Schwarz).
- M_A P_A ≥ |A|² on bins inside the visited interval. By coarea, |A| ≤ ∫|σ′|dk, and ∫ s dk ≤ √(M_A P_A).
- M_A = 0 outside [lo, hi], and (R3) holds.

The five zone moments are exact linear functions of (M, P, Q): E0, G1, G2 from M; F2 from P·g; F4 from Q·g². Every Ξ_v and μ_E is a function of those five moments. So this set contains the exact data of every law (no monotonicity is needed), up to level discretization, and it lower-bounds min μ_E at Ξ_v ≥ 0 for v = M and U alike. ∎ (`relaxed_UV.py`)

### 3.3 A fast-state identity (proved; checked to 1e-3 in `aform_check.out`)

For fast-only bands (f² = g a.e., so M = U), set Φ0 = E0, a(t) = −2tΦ0′/Φ0 = 2t⟨g⟩_t ≥ 0, and ω = t^{−1/2}e^{−tm²}Φ0³ > 0. Then, with the zone integration making the boundary terms vanish (a ~ 2t⟨g⟩ as t → 0):

- Ξ_T2g = C_X ∫ ω a²(a − 1) dt,
- Ξ_Eg = C_X ∫ ω (a − t a′)(a − 1) dt, with a − ta′ = 2t²(ln Φ0)″ ≥ 0,
- μ_E = C_μ ∫ ω a (5a − 1 + 2m²t)/(4t) dt,

where C_X = 1/(32Γ(5/2)) and C_μ = 1/(12Γ(3/2)).

**Proof.** W_T2g = 4Φ0′² and W_Eg = 2Φ0²(ln Φ0)″, J = Φ0(a − 1). Then E0(3F2² − F4E0) = Φ0³(2L′² − L″) with L = ln Φ0. One integration by parts on the ta′ term gives the μ_E line. ∎

Checked on a box + fast-atom measure (m = 0.1, b = 1, atoms at levels 0.5 and 0.3): the moment forms give Ξ_T2g +2.311254e-3, Ξ_Eg +5.247907e-4, μ_E +7.4177e-3; the a-forms give +2.311254e-3, +5.247918e-4, +7.4246e-3. The 1e-3 relative difference in μ_E comes from the numerical a′.

**Reading.** The graviton cone needs a > 1 (pair states faster than the box's a = 1; compare R16-3's v_z² > 1/5). The shear needs the UV region a < 1/5 to win, and it weighs that region by an extra 1/t. Fast zigzags at low levels make a overshoot 1, which makes μ_E positive. Flats lower μ_E (−F4·E0 term) but also add −E0 to J. This is the trade-off the scans below measure. It is not a proof of conflict.

### 3.4 The M-vertex scan of 𝓡 (checked; `relaxed_path*.out`, `relaxed_dual_m0.1.out`)

**Method.**
- 60 levels on [s_min, π]. Masses at s ∈ {0, 1}; b, lo and hi fixed per cell.
- SLSQP with exact gradients (gradient check to 6 digits, first line of each `.out`), 5–15 random starts per cell.
- Constraints (R2), (R3), plus Ξ_M,Eg ≥ 0 and Ξ_M,T2g ≥ 0.

**Cells.**
- b ∈ {0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.7};
- lo ∈ {s_min, 0.15, …, b}, s_min ∈ {0.05, 0.08, 0.15};
- hi ∈ b + {0, 0.25, 0.5, 1.0, 1.5, 2.0, 2.5}.

**Results.**

| m | cells with a graviton-cone-feasible point | smallest μ_E found | where |
|---|---|---|---|
| 0.1 | 152 | **+1.255e-3** | b = 0.15, lo = 0.05, hi = b (`relaxed_path_small_smin0.05.out`) |
| 0.1 (s_min = 0.15, b ≥ 0.3) | — | +1.558e-3 (b = 0.3), +2.544e-3 (b = 0.6), +4.84e-3 (b = 1.0), +5.96e-3 (b = 1.2) | `relaxed_path_m0.1_{a,b,c}.out` |
| 0.01 | 51 | **+1.434e-3** | b = 0.4, lo = 0.15, hi = b (`relaxed_path_m0.01.out`) |

- No cell gave μ_E ≤ 0 at a feasible point (0 of 203).
- In 84 further cells (mostly high climbs, hi ≥ b + 1.5) no point with both Ξ_M ≥ 0 was found at all.
- **Dual** (`relaxed_dual_m0.1.out`, 23 cells): maximizing min(Ξ_M,Eg, Ξ_M,T2g) subject to μ_E ≤ 0 gives at best **−1.07e-3** (b = 0.6, lo = 0.3, hi = 1.6).
- **Path constraints decide it (checked).**
  - Without the occupation constraint (R2), the same optimizer reaches negative μ_E at b = 1, m = 0.1:
    - −3.16e-3 without (R3) (`relaxed_grad_noR3_m0.1.out`), using a fast atom of mass 0.21 at level 3.14;
    - −2.38e-3 with (R3) (`relaxed_grad_withR3_m0.1.out`), using fast atoms of mass 0.05 at levels 2.99 and 3.09.

    Both need fast states near level 3. (R2) forbids them: a path from σ(b) = 1 to level 3 must occupy every level in between, which costs ≥ 2 of the 2.14 available edge length.
  - A three-atom global grid without path constraints gives +2.08e-3 (`relaxed_grid_m0.1.out`; 9.1e6 measures).
- **Explicit laws (checked; `opt3_*.out`, `nearest.out`).** Free-segment laws P(N) in 𝒮 (σ′ ∈ [−1, 1] on N segments, C^∞ steps, wt = 0.03), optimized directly, reach graviton-cone zeros with:
  - μ_E = **+3.05e-3** (M zero, b = 0.6, N = 16; v_max 0.995196);
  - μ_E = **+2.13e-3** (U zero, same skeleton; v_max 0.995198);
  - for comparison, R16-3's zeros have +6.0e-3 to +6.6e-3.

  So the gap to μ_E = 0 is about 2e-3 in explicit laws and ≥ 1.25e-3 in the relaxation.

### 3.5 The U vertex: scan of Lemma R_U, plus a slope-resolved search (checked; `relaxed_UV_*.out`, `relaxed_pathU4_*.out`, `relaxed_pathU2_m0.1_a.out`)

**Lemma R_U scan (`relaxed_UV.py`).**
- 50 levels; variables (M, P, Q) per level. Exact gradients.
- Two phases: maximize min(Ξ_U,Eg, Ξ_U,T2g) first, then minimize μ_E from feasible points. 6–8 random starts per cell.
- Cells: b ∈ {0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0, 1.4}, lo = s_min ∈ {0.03, 0.05, 0.15}, hi ∈ b + {0, 0.15, 0.25, 0.5, 0.75, 1.0}.

**Results.**
- **m = 0.1:** smallest μ_E found = **+2.55e-4** (b = 0.1, hi = 0.6, m ~ b, degenerate). In the light-box regime b ≥ 0.3 it is ≥ +3.0e-4 (b = 0.3, hi = 0.8).
  - b = 0.4: +5.1e-4 (hi = 0.9); also +7.1e-4 with s_min = 0.05.
  - b = 0.7: +2.0e-3.
  - b ≥ 1.0: no point with both Ξ_U ≥ 0 was found except at hi = b (+5.7e-3).
- **m = 0.01:** smallest μ_E = **+1.32e-4** (b = 0.3, hi = 0.8); b = 0.5: +6.3e-4. This is the thinnest margin in the report.
- **Level-grid check** (`relaxed_UV_U_m0.01_b0.3_L100.out`, 100 levels instead of 50, m = 0.01, b = 0.3): hi = 0.55 gives +1.39e-4 (50 levels: +1.53e-4). The margin moves by ~10% and keeps its sign. hi = 0.8 gives +1.332e-4 (50 levels: +1.322e-4).
- For the same Lemma R_U set with the M vertex: +2.0e-3 (b = 0.4, hi = b) and +3.4e-3 (hi = 0.9) (`relaxed_UV_M_b0.4.out`). This is consistent with §3.4.

**Slope-resolved search (`relaxed_pathU4.py`; not a relaxation).**
- Slopes s ∈ {0, 0.2, 0.4, 0.6, 0.8, 0.9, 1}, 40 levels, coarea constraint Σ_s s·mass ≥ bin width, plus (R3), two phases.
- m = 0.1: smallest μ_E = +5.44e-4 (b = 0.4, hi = 0.9). Other cells: +1.36e-3 (hi = b), +2.11e-3 (b = 0.7), +4.27e-3 (b = 1.0).
- m = 0.01: +1.01e-3 (b = 0.4).
- This agrees with the relaxation to ~10%.
- Climbs to hi ≥ b + 0.5–1.5 found no point with both Ξ_U ≥ 0 (best min(Ξ_U) −1.2e-4 to −9.2e-4).
- **The only negative value** (−4.4e-4 at b = 0.4, hi = 1.9, `relaxed_pathU2_m0.1_a.out`) came from the weaker occupation constraint. That constraint lets the climb from 0.4 to 1.9 be made of flats, which coarea forbids: a climb needs ∫|σ′|dk ≥ Δh. Under coarea the same cell has no graviton-cone-feasible point.
- **Explicit mixes** (`simplexU_m0.1.out`). Convex σ′-mixes of R16-3's corners with five terrace corners (all with μ_E < 0) never reach U,Eg ≥ 0, U,T2g ≥ 0 with μ_E below +6.3e-3. Mixing σ′ averages slopes; it does not place flats at levels.

### 3.6 The charge block on the stated family (proved; refereed inputs)

- **Independence (proved).**
  - By Lemma Q (`vR16-2:5`), species i's speed shift depends on (its spin's edge, the photon edge, λ, m_i), and the photon shift on the matter edges only.
  - R9-9's Ξ and μ_E depend on the scalar edge only.
  - With no charged scalars in the SM setting, the two blocks share no edge parameter.
  - At one loop, matter counterterms do not enter Ξ or μ_E. Their effect there is O(e²κ), two-loop (reading).
- **No subluminal Dirac shape zero (inherited; proved part plus checked part).**
  - The referee-confirmed identity is ∫_b^π (S′ − 1)w = −πw(π) + ∫_b^π (q − S)w′, with w′ ≤ 0 for a nondecreasing photon (`R16-2_referee_verdict.md:66-72`).
  - A zigzag stretch in s keeps S ≤ q further below q. So, for two edges S ≤ S̃ ≤ q on [b, π] with the same endpoints, tadpole(S) − tadpole(S̃) = ∫_b^π (S̃ − S)w′ ≤ 0 (proved). **A D1/zigzag hybrid's tadpole is ≤ that of any pointwise-higher edge in 𝒞.** Zigzags only move the dominant term further negative.
  - The exchange remainder is not bounded (`vR16-2:11`), so "no zero" stays checked, not proved (R16-2 Lemma F).
- **Doubler cost of Dirac zigzags (proved).** In D1, W′ = r√(1 − s′²) vanishes wherever |s′| = 1. So zigzag stretches add nothing to W_π = r∫_b^π√(1 − s′²)dk, and the corner masses m + nW_π fall as zigzag length grows. At a = ℓ_P, W_π = 0.095/a is still Planckian, so this is a cost, not an exclusion (reading).
- **Count (refereed, conditional).** 3 tunings with per-(spin, |q|) counterterms, 7 with per-species counterterms (`vR16-2:13,17`). The photon-side condition can be a counterterm, a matter-class counterterm, or (on superluminal literal edges) a shape equation; it counts once (`vR16-2:13`).
- **Precision (comparator):** each tuning holds to ~1e-16 (`C5_R16-2_report.md:250`).

### 3.7 (b) The bill for SM content, in R13-8's rows (reading, built from refereed parts)

| R13-8 row (P,T-even, `vR13-8:15`) | R13-8 | this family | status |
|---|---|---|---|
| matter speeds (charged), incl. photon side | N_s = 9 | **3** (per class) / **7** (per species) | R16-2 conditional; R16-1 DERIVED |
| graviton speed + axis birefringence (E_g, T₂g along an axis) | 2 of 4 TT-speed rows | **2** edge-shape tunings on the scalar edge, per chosen vertex | R16-3 refereed (locally independent, `vR16-3:13`) |
| two off-axis TT anisotropies | 2 | **2** (not computed; q off-axis is outside R9-9's form) | suggested |
| E_g shear mass μ_E | 1 | **1**, but *not* an edge shape when the graviton cone is shape-tuned (§3.4–3.5): a shear-mass counterterm, pairing, or the empty vacuum | this report (CONFLICT, worker) |
| T₂g shear mass | 1 | **0** at one loop (vanishes for V3's coupling, `vR13-8:22`) | refereed |
| LV tadpole | 1 | **1** (not computed) | — |
| CC | 1 | 1 | P51 |
| **total** | N_s + 7 + CC = 16 + CC | **9 + CC** (per class) / **13 + CC** (per species) | — |

- **The listed conditions alone** (photon, electron, graviton axis cones, shear): **6** per class, **10** per species. This matches the registered "about 5–6" for the class reading, but only if the shear is paid by a non-shape knob.
- **Vertex.** The vertex is a law datum (P63(iii)). Only one vertex is physical, so "2 per vertex" is 2, not 4.
- **Other zero-point edges (reading; not computed).** The photon, gluon and Dirac sea also carry zero-point stress. Two conventions:
  - *Per-edge:* every such edge needs its own graviton-cone and shear zeros, +3 per edge.
  - *Sum:* the totals vanish. Then the other edges are extra knobs, and under R13-5's stipulated opposite-sign fermion vertex they could absorb the scalar edge's μ_E. That would lift the CONFLICT at no extra count.

  Neither convention can be computed until a Dirac (and photon) TT/shear vertex exists. This is the largest open item.
- **Precision (comparator).**
  - Graviton cone: |Ξ| ≲ 1e-16 against edge values ~1e-3, so each of the two shape tunings holds to ~1e-13 relative (`C5_R16-3_report.md:276`).
  - Charge block: ~1e-16 each.
  - The drift from the light-mass limit is O((ma)²) ≲ 1e-34 (`vR14-3:18`; `C5_R16-3_report.md:223`).

### 3.8 (c) Whole-zone v_max and hopping tails (checked; `nearest.out`, `recheck.out`)

No law in the shape family meets every listed condition, so there is no single "resulting law". The best composite is:

- **Scalar edge:** R16-3's M zero, (u, v) = (0.955978, 0.024523) in the A, C2, C simplex.
  - v_max = 0.998292 (m = 0.1), max|σ′| = 1 exactly.
  - Tails |ε_128| = 3.67e-5 (`vR16-3:17`, referee-corrected).
  - μ_E = +6.19e-3, paid by a counterterm.
- **Dirac edge:** D1(1.4, 1/√3). v_max ≤ 1, with equality at r = 1/√3 (`vR16-1:15`). W_π = 0.095. Plus the 3 (or 7) counterterms.
- **Nearest-approach shape laws** (this report, graviton-cone zero on one vertex, lowest μ_E found):

  | law | v_max (m = 0.1 / 0.03) | max\|σ′\| | min edge g | \|ε_128\| | \|ε_256\| | \|ε_512\| |
  |---|---|---|---|---|---|---|
  | M-best (opt3 M, b = 0.6, N = 16) | 0.995196 / 0.999564 | 1.000000000 | 0.0360 | 1.4e-5 | 5.5e-6 | 6.1e-7 |
  | U-best (opt3 U, b = 0.6, N = 16) | 0.995198 / 0.999564 | 1.000000000 | 0.0362 | 6.8e-6 | 1.0e-6 | 3.5e-7 |

  These tails are of the same order as R16-3's corrected zero law (1e-5 at r = 128), against 4.5e-8 for R14-3's G_w* (`C5_R16-3_report.md:246`).
- **m-transfer of these zeros (checked).** The M-best zero tuned at m = 0.1 has Ξ_M,Eg = +2.3e-4 at m = 0.03. Its valley floor g = 0.036 is close to m², so its m² expansion converges slowly. The common-setting statement needs valleys well above m², as R16-3's zeros have (g ≈ 0.14).

### 3.9 (d) Prices (named, not adopted)

- **P-R16-9a (new): the shear is not a shape condition once the graviton cone is shape-tuned.**
  - On one subluminal scalar edge in 𝒮, P62 (shear zero) and P-Z (zigzag graviton-cone zero) are incompatible (worker CONFLICT; referee required).
  - The shear then needs one non-shape knob:
    - an E_g shear-mass counterterm (1 tuning); or
    - pairing P46; or
    - the empty Fock vacuum, where Ξ ≡ μ_E ≡ 0; or
    - a superluminal edge (R9-2's t*, v_max 1.6, `TESTS:4834`), which gives up P61.
  - Axiom text: none. Edge dispersions and counterterms are downstream dynamics (`AX:114-130`). The supplied vacuum and the vertex are source/action gates (`AX:187`).
- **P-Z (R16-3, refereed):** zigzag scalar edge, valleys at 0.35–0.9/a, tails ~1e-5 at r = 128 (corrected), two tunings at ~1e-13.
- **P73 refined (R16-2):** 3 tunings (per class) or 7 (per species), each ~1e-16.
- **P-TTV (P63(iii)):** the vertex is a law datum.
- **P-R16-9b (named gap, not a price yet).** Dirac, photon and gluon TT and shear vertices. Without them the gravity block is defined for scalar loops only, and the per-edge or sum convention cannot be chosen.
- **Uncomputed rows:** two off-axis TT speeds and the LV tadpole (+3).
- No axiom text changes. Sizes use a = ℓ_P, the scale-reference primitive (`AX:189-190`).

---

## 4. Against the FIXED readings (`TESTS:5396-5399`)

**Worker reading: CONFLICT. Referee required.**
- **The pair.** {Ξ_Eg = Ξ_T2g = 0} and {μ_E = 0} cannot both hold on one subluminal scalar edge in 𝒮, in R9-9's prescription with the assumed W1 and the supplied scalar vacuum.
- **M vertex:**
  - Lemma R (proved) reduces 𝒮 to a superset 𝓡.
  - A 203-cell multi-start scan of 𝓡 finds μ_E ≥ +1.25e-3 at every graviton-cone-feasible point it reaches.
  - In the dual search under μ_E ≤ 0, the best min(Ξ_Eg, Ξ_T2g) found is −1.07e-3 (23 cells).
- **U vertex:** Lemma R_U (proved) plus a scan finds μ_E ≥ +1.3e-4 (m = 0.01) and ≥ +3.0e-4 (m = 0.1, b ≥ 0.3). A coarea-constrained slope-resolved search agrees (≥ +5.4e-4). The U margin is about 10× thinner than M's.
- **Masses:** m = 0.1 and 0.01. **Parameter range:** b ∈ [0.15, 1.7] (M) and [0.1, 1.4] (U); s_min ∈ {0.03, 0.05, 0.08, 0.15}. Cells with m ≳ b are degenerate (the box species are not light) and are reported but not relied on.

**Why not JOINT.**
- No explicit law meets μ_E = 0 together with the graviton cone. The best explicit approaches have μ_E = +2.1e-3 (U) and +3.1e-3 (M).
- Every other listed condition is met:
  - the charge block by 3 (or 7) tunings (refereed, conditional);
  - E_g and T₂g by 2 shape tunings (refereed).

**Why the CONFLICT is not a proof.**
- The scans are local optimizations from random starts. A positive minimum found is an upper bound on the cell's true minimum, so the evidence is "no μ_E ≤ 0 point was found by either the primal or the dual search on a provable superset", not a certified bound.
- The level grid (60 or 40 levels) and the finite b grid are discretizations.
- Class-wide, so the fixed rule requires a referee. If the referee does not accept a scan, the reading is **OPEN**.
- Not covered: totals including Dirac, photon or gluon zero-point loops (no vertex); q off-axis; non-separable laws; the deformed W2.

**Expectation check.** The expectation was "JOINT without P62 and with a count of about 5–6. CONFLICT or OPEN with P62" (`TESTS:5400`).
- Without P62, the conditions are met, with count 5 (3 + 2) under the class reading.
- With P62 there is a CONFLICT on the shape family, and the count becomes 6 with one non-shape knob.

## 5. Strong-word check

- **"Proved"** is used only for:
  - Lemma R (mixture, coarea occupation, σ ≤ k) and Lemma R_U (per-level moments with Cauchy–Schwarz and coarea);
  - the fast-state a(t) identity;
  - block independence (from Lemma Q and the scope of R9-9's vertex);
  - the D1/zigzag tadpole monotonicity (from the refereed IBP identity);
  - the W_π statement.
- **"Checked"** is used for every number. Methods: Laplace moments as in R16-3, exact-gradient SLSQP, rechecks against archived outputs.
- **"Cannot both hold" / "conflict"** means not found on a proved superset by primal and dual multi-start scans. No certified global minimum.
- **"Never"** appears only for "the only negative values found were path-infeasible", which is about my runs.
- **Not claimed:**
  - anything for Dirac, photon or gluon gravity contributions;
  - the off-axis TT rows;
  - gauge invariance (W2);
  - dressed poles;
  - two loops;
  - a proof of R16-2's Lemma F.

## 6. For the referee

1. **Lemma R.** That (R1) lowers μ_E and preserves Ξ_M exactly; that (R2) total-mass occupation follows from coarea; that (R3) is necessary; and that the union over (b, lo, hi) cells covers 𝒮 for the stated b and s_min ranges.
2. **The a(t) identity**, including the IBP boundary terms (a ~ 2t⟨g⟩ at t → 0 on the zone).
3. **Whether a primal + dual multi-start scan of a superset is an acceptable "demonstration"** for CONFLICT. If not, which rigorous bound (e.g. a moment SDP over 𝓡) would be needed.
4. **Lemma R_U and the U search.** That M P ≥ |A|² and P² ≤ QM are necessary per level bin; that the coarea constraint Σ_s s·mass ≥ |A| is necessary; and that the only negative-μ_E point (`relaxed_pathU2_m0.1_a.out`, hi = 1.9) violates it. The U margin (+1.3e-4 at m = 0.01, b = 0.3) is thin enough that the level discretization should be checked.
5. **The count table §3.7**, especially:
   - whether μ_T₂ = 0 at one loop carries over to zigzag edges (`vR13-8:22` is for V3's coupling);
   - whether the off-axis TT rows are independent of the axis rows.
6. **The sum versus per-edge convention** for zero-point loops of other species. This decides whether the CONFLICT is physical or an artefact of R9-9's scalar-only vertex.

## 7. Files (all in `S/scripts/`)

- **Copied unmodified** from the archive `scripts/C5/R16-3/`: `zz.py`, `laws.py`, `floor_scan.py`, `simul2.py`. From `scripts/C5/R16-2/`, in `dirac/`: `r162_*.py`, `r137_onshell.py`, `r85_box_qed_copy.py`, `r101_dirac_moment_copy.py`, `r141_wilson_copy.py`, `sublum.py`.
- **Rechecks:**
  - `recheck.{py,out}` (R16-3 numbers);
  - `dirac/r169_dirac_check.{py,out}` (R16-2 D1 numbers);
  - `relaxed_validate.{py,out}` (relaxed evaluator against `zz.py`).
- **Explicit-law optimizer:** `opt3.py` → `opt3_*.out`. `nearest.{py,out}`: v_max and tails of the best explicit laws. `realize.py`: a law builder (not used for a result).
- **Relaxation:**
  - `relaxed_grad.py` (with R3 only) → `relaxed_grad_withR3_m0.1.out`; `relaxed_grad_noR3.py` → `relaxed_grad_noR3_m0.1.out`. Exact gradients, no occupation constraint; their negative values are path-infeasible.
  - `relaxed_path.py` (+ `_hi`, `_small` variants) → `relaxed_path_*.out`.
  - `relaxed_dual.py` → `relaxed_dual_m0.1.out`.
  - `relaxed_grid.py` → `relaxed_grid_m0.{1,01}.out`, the three-atom global grid.
- **U vertex:**
  - `relaxed_pathU.py`, `relaxed_pathU2.py`: weak occupation constraint (superseded by U4).
  - `relaxed_pathU3.py`, coarea, single phase; it found no feasible start; kept for the record.
  - `relaxed_pathU4.py` → `relaxed_pathU4_*.out`: coarea, two-phase, slope-resolved search.
  - `relaxed_UV.py` (Lemma R_U, both vertices) → `relaxed_UV_*.out`; `run_UV.sh` batches; `relaxed_UV_L.py` (level count via RLEV) → `relaxed_UV_U_m0.01_b0.3_L100.out`.
  - `relaxed_dump.py` → `dump_U_b0.4_hi1.4.out`, `.npy`.
  - `simplexU.{py,out}`: explicit convex mixes, partial (stopped after 4 of 5 corners; no feasible point below μ_E = +6.3e-3).
- **Identity check:** `aform_check.{py,out}`.
- **`superseded/`:** `relaxed.py` runs without gradients (unconverged), not used.
