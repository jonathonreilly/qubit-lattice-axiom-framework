# C5 F6 report: the Higgs mass² strain Hessian under the root's SF law

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor, every C5 worker and panel F). Unrefereed. Run 2026-10-13, 21:40Z to 22:21Z. No repository file was edited. Nothing was downloaded; no web lookups (every observational number is the pre-registered one or RECALLED).
- **Memory:** OMP_NUM_THREADS=2; one heavy process at a time; peak resident set per run 0.31 / 0.72 / 0.41 / 0.37 / 0.40 GB (`/usr/bin/time -l` records in `S/*.err`). k-grids in z-slabs. No process of mine is still running.
- **Item:** `TESTS:9412-9446` (FIXED readings `:9441-9445`; expectation `:9446`).
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`; `pF/` = `P/agents/panel_F/`; `S/` = `scratchpad/C5/F6/scripts/`. `S/f1_lib.py` is an unmodified copy of `P/scripts/C5/F1/f1_lib.py`; `scratchpad/C5/F6/arch/` holds unmodified `dirac.py`, `sublum.py` (from `P/scripts/C5/R18-5`) and `r1934_lib.py` (from `P/scripts/C5/R19-34`).
- **Labels.** proved (complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED = from memory, not verified this run.
- **Read.** `AX` in full; `TESTS:9146-9474` (C5 follow-up F1–F5, Panel F record, F6, NF-1); `pF/SYNTHESIS.md` in full; `pF/pheno_statement.md` in full (T4 `:228-249`); `pF/condmat_statement.md:1-25,157-313` (T6 `:240-260`); `rF1` in full + `vF1`; `rF5` (grep: Higgs/scalar/(iv), `:139-142`); `rR19-31` in full + `vR19-31`; `rR19-21:1-80,170-245` + `vR19-21`; `rR18-9:1-90`; `rR19-11:100-160`; `rR19-12` (grep: scalar edge, `:21,73`); `rR9-9:1-60`; `rR19-35:64-72`; `PRICE_NOTE` (grep: (Σ), (S\*), (S_loc), P-R19-34a); scripts `P/scripts/C5/{F1,F3,F5,R19-31,R19-34}` (F1 lib reused; F3's dressing convention `f3_lib.py:1-70` and `f3_astar.out:1-2`; F5's `f5_c1.py/.out`; R19-31's `r1931_sqed_cross.py/.out`).

---

## 0. Plain words

1. **The Higgs mass does feel a uniform stretch of the grid, at grid strength, and nothing registered cancels it.**
   - Under the root's own strain rule (SF: every band's momenta flow with its own dispersion), the four one-loop pieces of the Higgs mass² all change at second order in the stretch t. The total, in grid units, is c_H = ∂²_tΣ_H·a² ≈ **+3.7e-3** on the main branch (R18-9 root, F1's law with U = 1, SM couplings at the grid scale), and +3.3e-3 to +1.6e-2 across every U = 1 branch and coupling set tried (checked numerics; SM couplings are an estimate).
   - The top-quark loop dominates (≈ 78%). The gauge loop is small (≈ 16%), because the Higgs edge and the photon edge are both continuum-like over most of the zone, so their flows almost coincide; the Higgs self-coupling loop is ≈ 6%.
2. **What that means for the Higgs vev.** Because the Higgs mass² is quadratically sensitive to the grid, a Planck-scale coefficient lands on a 125 GeV mass: δv/v ≈ −1.75e31 × t² (main branch). A passing stretch of t = 1e-21 (LIGO) moves v by ~2e-11. The nanohertz background seen by pulsar timing has t² ≈ 7e-29 in the relevant (E_g) components, so the uncorrected law would move v by about a thousand times itself: at face value there is no electroweak vacuum near the observed one in today's sky (suggested; linear response fails).
3. **Against observation (conditional on a = ℓ_P, the strain reading |t| = |h_+|, and the SM coupling estimate):**
   - **Clocks** (no graviton-mass bridge needed): the background's slow changes would make the proton-to-electron mass ratio drift by 90–1300 per year; clocks allow 3.6e-17 per year. **Exceeded by 2.6e18–3.5e19** on the main branch, 2.4e18–1.5e20 over all U = 1 branches.
   - **The Earth row** (through the canonical bridge): matter shifts the Higgs vev, which shifts the vacuum's strain stiffness by Δ(H†H)·c_H. That gives μ_ρ = 16π f_N|c_H|/m_H² = 1.5e-8 eV² m³/kg, **1e21 times F2's Earth-crossing coefficient**, tachyonic sign. This is the same channel as R19-21's (F)/F5's (iv-c), now with the coefficient computed on the root's SF law (count once).
   - **Control:** the uncorrected fermion channel (F1) through the same clock estimator exceeds by 6e6–8e7, the same order as the panel's ~2e8 (my estimator keeps only the E_g part of the background).
4. **Nothing registered covers it.** The scalar mass counterterm is a law datum fixed at zero strain (`rR19-31:62`). (S\*), (Σ) and (S_loc) are statements about what gravitates; at most (S_loc), which is OPEN, would remove the Earth-row term. None of them touches the Higgs mass parameter in the law, so the clock row stays. P-R19-34a covers fermion critical masses only. Panel F's P-R19-34a′ ("every mass parameter re-set on every uniformly strained law") covers it by construction and removes nothing observed.
5. **Found in passing, outside the pre-registered quantity: a larger Higgs channel.** On Wilson-type edges the vacuum's fermion condensate depends on strain (the same coefficient c₁ that R19-21 and F5 use). Through the top Yukawa it puts a strain-dependent Planck-cubed tadpole on the Higgs, δv/v ≈ 2e48–8e48 × t². P-R19-34a′, as worded ("every mass parameter"), does not name it; panel F's single primitive ("every zero-strain renormalization condition holds on every uniformly strained law", `pF/SYNTHESIS.md:83`) does.
6. **Reading (worker): SCALAR-HAZARD.** The expectation's "≥ 1e20" is met on the Earth row (bridge-conditional) but not on the bridge-free clock row, which gives ≥ 2.4e18.

---

## 1. Against the FIXED readings (`TESTS:9441-9445`), literal first

| reading | clause | status |
|---|---|---|
| **SCALAR-COVERED** | a registered clause makes Σ_H strain-covariant | **Not met.** The scalar mass counterterm is fixed at h = 0 (`rR19-31:62`). (S\*) (P177, `PRICE_NOTE:595`), (Σ) (P179, `:597`) and (S_loc) (P182, `:600`, OPEN) are source-side clauses: they say what gravitates and leave Σ_H(t) in the law unchanged (reading, from their texts). P-R19-34a (`rR19-34:177`; `PRICE_NOTE:679`) re-sets the fermion critical mass only; Σ_H's one-loop Hessian has no m_c(h) dependence at O(g², y², λ) (proved by inspection of the four loops). P-R19-31c (`rR19-31:257`) is about speed counterterms. P-R19-34a′ is panel F's proposal (`pF/pheno_statement.md:249`), not registered (`pF/SYNTHESIS.md:103`) |
| **SCALAR-HAZARD** | uncovered, and the predicted rate exceeds an observational bound | **Met (worker).** Uncovered (row above). Clock row: predicted \|d ln(m_p/m_e)/dt\| = 94–1260 /yr against 3.6e-17 /yr, ×2.6e18–3.5e19 (main), ×2.4e18–1.5e20 (all U = 1 branches and coupling sets) (§5.1). Earth row through the Higgs-induced stiffness: ×1.0e21 (main), bridge-conditional, tachyonic sign (§5.2) |
| SCALAR-SAFE | Hessian below tolerance in every branch | **Not met.** \|c_H\| ≥ 3.3e-3 in every U = 1 branch (§3.5). Passing the clock row needs \|c_H\| ≲ 1.4e-21 |
| OPEN | otherwise | not needed |

**Conditions on SCALAR-HAZARD** (each named, none hidden):
- one loop; F1's law with U = 1 as the setting fixes (`TESTS:9418`). F3's Dirac dressing family moves the top-loop piece (§3.3), and with two tuned dressing amplitudes c_H and F1's fermion Hessian can both be zeroed. That is a priced tuning (P-F6b, §8), not a registered law;
- a = ℓ_P (load-bearing, not asserted by the axioms, `pF/SYNTHESIS.md:44`): the clock rate scales as (ℓ_P/a)², and passing needs a ≳ 1.6e9–5.9e9 ℓ_P;
- |t| = |h_+| for a wave in grid axes (reading, as `pF/pheno_statement.md:171`);
- the SM coupling values at the grid scale (RECALLED; three sets bracket them, §3.5);
- the NANOGrav 15-yr background as a real GW background (comparator, 3.5–4σ, `pF/pheno_statement.md:265`);
- the top Yukawa in the root's vectorlike "22.5 Dirac fields on D1" convention (`rR18-9:37`; chiral SM couplings are owed, `pF/SYNTHESIS.md:53`).

---

## 2. Class, hypotheses, choices (stated before any title)

**Arena.** Z³ × ℝ, lattice units a = 1, Euclidean, one loop, external P = 0, E_g strain h = diag(1, −1, 0) in SF units t (v = (t/2)h·∇(E²/2), time-1 map; F1's units, `rF1:99-105`). H-cov equivalents are ×4 (t = −2h on soft modes, `rR19-31:60`).

**The scalar (Higgs) edge, identified** (`TESTS:9424`).
- The root's Higgs edge is R14-3's G_w(b_s, w = π − b_s) with fr = 1, which is SymG(b_s): ε_s² = m² + Σ_j h_s(k_j)², h_s = k on the box |k| ≤ b_s, h_s′ = 1 − sstep((|k| − b_s)/(π − b_s)) beyond. Sources: `rR18-9:37` ("4 real scalars on one Higgs edge G_w(b_s, w = π − b_s)"); `P/scripts/C5/R18-5/content4.py:7-11`; `rR19-12:73` (G_w with fr = 1 is SymG(b_s)).
- b_s = 2.526103698 (R18-9 refined root, `vR18-9:11`; `rR19-12:21`); 0⁺ root b_s = 2.590035 (`rR19-11:34`).
- This is R9-9's class (Z), a separable free scalar ε² = m² + Σu(k_i) (`rR9-9:42`), with u = h_s².
- R19-31's scalar was the NN complex scalar (`rR19-31:54,57`). It is used here as the control (C1) and as an SF comparison branch (§3.1).

**The strained law (F1's, `TESTS:9418`).**
- Scalar: K_t(q) = Σ_j h_s(φ^s_j(q_j))², where φ^s is the scalar's own 1D SF flow (p_j = h_s h_s′; separable, the same form as F1's photon flow `f1_lib.py:flowG1`). Photon Gph(2.9435) with flowed symbols d_{t,j} = d(φ^γ_j(q_j)) (F1). Dirac D1(0.909103708, 0.555604226) with F1's non-separable flow, B1 (flow mass 0.01) and B2 (flow mass 0).
- **The scalar lift is unique (proved).** Per component the scalar operator is a 1×1 symbol, so a k-dependent unitary dressing is a phase and drops out. For the doublet, gauge covariance allows only a U(1) phase. So SF's spectrum fixes K_t, and F3's dressing freedom does not exist for loops 1, 2 and 4.
- **Gauge paths are unique within F4's families (proved).** K_t is separable, so every scalar hop is axial. The shortest gauge path of an axial hop is the axial segment, where Psym, J, the staircases and SL all coincide. Minimal coupling by divided differences (the R8-5/R13-7/R19-34/F1 convention): V_j(0,q) = G_j(q_j)/d_j(q_j) and T_jj = G_j/d_j² with G_j = h_s(φ^s_j)², T_jk = 0 for j ≠ k; temporal vertex Q₀ and seagull 1.
- **Loop formulas (Q₀ done analytically; checked against quadrature to 9e-16, C4):**
  - (1) Σ_g/e² = ⟨Σ_j T_j/(2Ω) + E/(2Ω(Ω+E)) − Σ_j V_j²/(2ΩE(Ω+E))⟩, with Ω² = Σd_j² and E² = m² + K. This reduces exactly to R19-31's 4G_γ − G_s for the NN law under H-cov (C1).
  - (2) SU(2)×U(1): at one loop both diagrams carry Σ_a T^aT^a = C₂ (no ghost or gauge-self-coupling diagram enters the scalar 2-point function), so Σ = [(3/4)g² + (1/4)g′²]·Σ_g/e² for the doublet (Y = ½) on the same vector edge (proved; comparator: the continuum gauge coefficient 3[(3/4)g² + (1/4)g′²]Λ²/16π², RECALLED).
  - (3) top Yukawa (m_t = y_t h/√2, N_c = 3, e_vac = −2⟨E⟩ per Dirac field): Σ_Y = −N_c y_t²⟨c²/E³⟩ at the flowed momenta, propagator mass 0 (critical point).
  - (4) quartic V = λ(H†H)², 4 real components on the scalar edge: Σ_λ = 6λG_s with G_s = ⟨1/(2ε_s)⟩.
- **Gauge parameter (proved from the two Ward identities):** Σ_ξ/e² = (1 − ξ)·(−m²)⟨1/(4Ω³) − m²(E + 2Ω)/(4EΩ³(E+Ω)²)⟩. It vanishes identically at m = 0.
- Counterterm: the Higgs mass² counterterm is fixed at t = 0 (`TESTS:9418`; `rR19-31:62`), so ∂²_tΣ_H is the uncancelled response.

**Branches carried.**
- Root: R18-9 (main) and 0⁺.
- Higgs propagator mass: m = 0 (main; m_H a ~ 1e-17), 0.001 and 0.01 (the rows' m).
- Yukawa flow: Y-a/B1 (main: the flow is a law datum at mass 0.01), Y-a/B2 (at mass 0), and Y-b (the flow is recomputed at the actual fermion mass, the rows' convention used for R19-11's c₂).
- Lift: U = 1 (the setting); F3's G1 and G2 dressings at F1's fermion zero a* (`P/scripts/C5/F3/f3_astar.out:1-2`) as sensitivity branches.
- Couplings at the lattice scale, three sets (all RECALLED or ESTIMATE):
  - Planck-scale SM: g² 0.26, g′² 0.21, y_t 0.38, λ −0.013;
  - R19-31's gauge values with y_t 0.5, λ 0;
  - low-scale SM as an extreme bracket: g² 0.42, g′² 0.13, y_t 0.94, λ 0.13.

**Excluded:**
- two loops;
- T₂g: the photon is singular for T₂g (G-F5a, `TESTS:9391`). The E_g part alone gives a lower bound on the clock rate (§5.1, proved);
- a photon-side lift (a dressing of the frame-Maxwell operator, not computed, as in F1);
- static-field registration (pheno row S);
- other Yukawas (y² ≪ y_t²);
- a chiral SM edge.

---

## 3. (a) The four Hessians (checked unless stated)

### 3.1 Controls first (`S/f6_controls.out`, `S/f6_nn.out`)

| control | result | target |
|---|---|---|
| C1: R19-31's H-cov NN law, m = 0.1, step 0.02 | Σ(P=0) = 0.683592960; ∂²_hΣ = −5.318100e-1 | `r1931_sqed_cross.out:2-5`: 0.683592960, −5.318100e-1 (all digits) |
| C2: scalar edge = photon edge Gph(2.9435), m = 0 | integrand = 3/(2Ω) to 3e-16 at t = 0 and 0.01; Hessian −8.97965e-3 | 3 × the vector μ_E slope c₂^V = 3 × (−2.993e-3) = −8.979e-3 (`rR19-11:139`), the relabelling identity |
| C3: quartic loop at the 0⁺ root's b_s | ∂²_tG_s = −2.72156e-3 | 2c₂^s = 2 × (−1.361e-3) = −2.722e-3 (`rR19-11:139`; Lemma C, `rR19-31:115`) |
| C4: closed-form Q₀ integrals (loop and ξ-term) against quadrature | max diff 8.9e-16 | — |
| C5: Ward Σ_j d_jV_j − [K(q) − K(0)] at t = 0.3, 1000 points | 8.9e-16 | 0 |
| NN scalar + NN photon under **SF** (one common flow) | Hessian −6.0774e-3 = 3G_γ″ to all digits | relabelling lemma (`rF1:216-226`): pure Jacobian term. H-cov on the same law gives −0.133 per t², 22× larger |

### 3.2 Loop 1, U(1) (`S/f6_gauge.out`)

**Convergence:**
- R18-9 root, m = 0: +2.43441e-3 (174 nodes, d = 0.003), +2.43449e-3 (368), +2.43450e-3 (660), +2.43452e-3 (660, d = 0.0015), **+2.43452e-3** (948, d = 0.0015) per e² (`:2-6`). Converged to ≤ 1e-7 relative.
- H-cov-equivalent ×4: +9.738e-3.
- Against the setting's control `rR19-31:124` (−0.532 e² per h² under H-cov on the NN law): the root's SF law gives **55 times less and the opposite sign** (comparison of checked numbers).

**Branches:**

| branch | Hessian (e², SF) |
|---|---|
| m = 0.01 | +2.43448e-3 (`:9`) |
| m = 0.001 | +2.43452e-3 (`:10`) |
| 0⁺ root (b_s = 2.590035) | **+6.810e-4** (`:15`) |
| photon window b_γ ∈ [2.936, 2.947] (`rR18-9` §0 item 2) | +2.25e-3 … +2.52e-3 (`f6_scan.out:14-17`) |

**Gauge parameter.**
- X(m) = −7.77e-6, −8.37e-7, −1.07e-7 at m = 0.01, 0.003, 0.001 (∝ m², up to a log).
- d²_tX/m² ≈ 5–6e-4 (`:16-19`).
- At m_H a ~ 1e-17 the ξ-dependence of the Hessian is ~1e-37: Feynman, Landau and every ξ agree.

**Structural account (checked).**
- Σ_g(0) = 0.56596. Its parts are: tadpole 0.56480, temporal 0.09445, exchange −0.09328 (`:7`).
- Decomposition of the Hessian (`:11-14`):

  | strained | Hessian |
  |---|---|
  | scalar alone | +0.1577 |
  | photon alone | +0.3191 |
  | both (own flows) | +0.0024 |
  | K1: one common flow, the photon's | −2.84e-2 |
  | K2: one common flow, the scalar's | −3.94e-2 |

- So the cross term (−0.4744) cancels 99.5% of the separate responses. Both edges are linear (continuum-like) out to b_s = 2.526 and b_γ = 2.94. Where both are linear the two flows coincide and div v = 0, so relabelling is exact there. The residual comes from the zone shell where the scalar's flow bends.
- **Not protected.** In a b_s scan the loop-1 Hessian falls through zero near b_s ≈ 2.615 (between +6.8e-4 at 2.590 and −1.5e-4 at 2.620; `f6_scan.out:2-12`). b_s is fixed by the μ_E row, and both permitted roots give a nonzero value.

### 3.3 Loop 3, top Yukawa, per N_c y_t² (`S/f6_yuk_a.out`, `S/f6_yuk_b.out`)

**Convergence and branches:**
- Y-a/B1: +6.62554e-3 (126 nodes), +6.62484e-3 (232), +6.62479e-3 (232, d = 0.0015), **+6.62484e-3** (390) (`yuk_a:1-4`). Converged to 1e-7. Σ_Y(0) = −0.56183 per N_c y_t².
- B2: +6.6013e-3 (`:5`). 0⁺ root: +6.7602e-3 (`:6`).
- **Y-b** (flow tracks the actual mass): ½∂²_mμ_E = **+6.3477e-3** (`yuk_b:4`).
  - This agrees with F5's μ_E(m) values at the R18-9 root (`P/scripts/C5/F5/f5_c1.out:1`; ½ × 1.268e-2 = 6.34e-3) and with R19-11's 0⁺-root c₂ = +6.6e-3 (`rR19-11:139`).
  - So loop 3 is Lemma C's statement that c_H is the Dirac μ_E mass slope: count once with R19-11 and R19-21 for the coefficient. New here is its use as a Higgs mass² Hessian.

**F3's dressing (sensitivity, outside the U = 1 setting).**
- The D-H rotation (`f3_lib.py:3-8`) changes M′ but not E. So the Yukawa insertion, which is added after the dressing as in F3, sees c′² = E² − M′².
- Responses: dY/dε = −0.86770 (G1) and +0.26838 (G2) (`yuk_a:7-8`).
- At F1's fermion zero a* the Yukawa Hessian becomes −1.787e-2 (G1) or +1.096e-2 (G2).
- So this one piece inherits the F1 referee's lift freedom (`vF1:5`); loops 1, 2 and 4 do not (§2).

### 3.4 Loop 4, quartic (`S/f6_gauge.out:20-27`)

- ∂²_tG_s = **−2.67482e-3** at the R18-9 b_s, stable over 368/660/948 nodes to 4e-9; m = 0.01 gives −2.67476e-3.
- 0⁺ root: −2.72157e-3, which equals 2c₂^s (C3).
- Σ_λ″ = 6λ × that. It is almost flat in b_s: −2.52e-3 to −2.88e-3 over b_s ∈ [2.3, 2.8].

### 3.5 Total c_H = [(3/4)g² + (1/4)g′²]·H_g + N_c y_t²·H_Y + 6λ·H_λ (`S/f6_sizes.out`)

| branch | couplings | c_H | gauge / top / quartic |
|---|---|---|---|
| **R18-9, Y-a B1, U = 1 (main)** | Planck-scale SM | **+3.681e-3** | +6.0e-4 / +2.87e-3 / +2.1e-4 |
| same | R19-31 gauge, y_t 0.5, λ 0 | +5.547e-3 | +5.8e-4 / +4.97e-3 / 0 |
| same | low-scale bracket | +1.632e-2 | +8.5e-4 / +1.76e-2 / −2.1e-3 |
| R18-9, Y-a B2 | Planck-scale | +3.671e-3 | |
| R18-9, Y-b | Planck-scale | +3.561e-3 | |
| 0⁺ root, Y-a B1 | Planck-scale | +3.309e-3 | +1.7e-4 / +2.93e-3 / +2.1e-4 |
| R18-9, F3 G1 at fermion a* | Planck-scale | −6.931e-3 | top −7.7e-3 |
| R18-9, F3 G2 at fermion a* | Planck-scale | +5.557e-3 | |

- **Every U = 1 branch: +3.3e-3 ≤ c_H ≤ +1.6e-2** (checked, given the coupling sets).
- A coupling zero would need λ* = +0.216 at the grid scale (main; +0.19 to +0.33 in other branches), while the SM has λ(M_P) ≈ −0.01 (RECALLED). It is not available without changing the observed Higgs mass (reading).
- c_H/|Σ_H(0)| ≈ 3%: Σ_H(0) = −0.118 a⁻² (main couplings), and the fixed counterterm cancels it.
- **Comparator (RECALLED):** the hierarchy problem. Σ_H ~ Λ² × couplings. In the continuum a uniform strain is a coordinate change and leaves Σ_H unchanged (the relabelling Ward identity, `rF1:52`, `rR19-15:136-137`). On the torus no origin-fixing separable E_g flow preserves volume (`rF1:228-231`, with the referee's hypothesis `vF1:11`). So the strain sees a percent-level anisotropy of Λ², and that is multiplied by M_P².

---

## 4. (b) Conversion to vev shifts

**The mass² channel (pre-registered).**
- δv/v = −δm²/m_H², with δm² = ½c_H M_P²·Q_E (proved: V = −μ²|H|² + λ|H|⁴, m_H² = 2μ²). Here Q_E is the E_g quadratic in the strain, normalised so that the SF strain diag(−t, t, 0) gives Q_E = t²; by cubic invariance, Q_E = (h_E1² + h_E2²)/2.
- So **δv/v = −c_H·M_P²/(2m_H²)·Q_E = −1.75e31·Q_E (main)**, with M_P²/(2m_H²) = 4.76e33. The range over U = 1 branches is 1.6e31–7.8e31, and up to 2.3e32 with the dressings.
- Pheno's estimate was ~1e32 t² (`pF/pheno_statement.md:217`). The computed main value is 6× smaller, because the H-cov NN coefficient it used overstates the gauge piece (§3.2).
- Mapping: a = ℓ_P, M_P = 1.22089e19 GeV (`rR19-21:71`), m_H = 125.1 GeV, v = 246.22 GeV (RECALLED).
- **Sizes:**
  - LIGO-band, Q_E ~ 1e-42: δv/v ~ 2e-11, oscillating at 2f (invisible).
  - nHz background: ⟨Q_E⟩ = σ_a² = 7.0e-29 (`f6_drift.out:2`), so |δv/v| ≈ 1.2e3. Linear response fails: the uncorrected law has no electroweak vacuum near v in the observed background (suggested). The Higgs responds adiabatically, since 1/m_H ≪ 1/f.

**The tadpole channel (outside the pre-registered Σ_H(P = 0), reported because the plain question asks about vev shifts under real strain).**
- On Wilson-type edges the vacuum condensate C = ∂_m e_vac = −2⟨M/E⟩ = −0.6857 per field (condmat T6 had −0.686, `pF/condmat_statement.md:249`) depends on strain.
- Through the top Yukawa this is a strain-dependent Higgs tadpole: δv/v = −½(y_t/√2)N_c(∂²_tC)·M_P³/(m_H² v)·Q_E.
- ∂²_tC per field (`yuk_a:1-6`, `yuk_b:4`):

  | branch | ∂²_tC |
  |---|---|
  | Y-a B1 | −1.6127e-2 |
  | B2 | −1.568e-2 |
  | 0⁺ | −1.743e-2 |
  | Y-b | +1.0444e-2, which is c₁, reproducing F5's +1.0477e-2 forward difference and R19-11's 0⁺ c₁ = +1.069e-2 |

- **|δv/v| = 2.0e48–8.2e48·Q_E** (y_t 0.38–0.94; U = 1). The clock row is exceeded by 3e35–1.2e36 (`f6_sizes.out`, tadpole lines).
- **Count once:** this is the mixed derivative ∂_v∂²_tE_vac, the same coefficient as R19-21's (V) channel and F5's (iv-b), read in the other direction: strain moves v, not matter moves the stiffness.
- It is conditional on the vectorlike-Wilson Yukawa map (BO, `vR19-21` item 2). At t = 0 this tadpole is itself a Planckian tuning "missing from the bill" (`rR19-20:231`, suggested there).
- Labels: the coefficient is checked; the sizes are suggested.

---

## 5. (c) Against observation

### 5.1 Clocks (NANOGrav 15-yr background; `S/f6_drift.py/.out`)

**Spectrum (comparator, as pre-registered `TESTS:9435`).**
- h_c = A(f/yr⁻¹)^{−2/3} with A = 2.4e-15 and γ = 13/3.
- ⟨h_ij h_ij⟩ = 2∫h_c² dln f (RECALLED convention). Isotropy puts 1/5 of the power in each of the 5 traceless components.
- f_min = 1/(16 yr) or 1/(30 yr).
- **E_g only, as a lower bound (proved).** Q_E and the T₂g quadratic use disjoint, independent Gaussian components, so their drifts are uncorrelated. Leaving out T₂g can only lower the rms rate.

**Drift of Q_E** (two estimators):

| estimator | rms drift of Q_E |
|---|---|
| least-squares slope over T_obs = 10 yr, f_min 1/16 | **7.7e-30 /yr** (smallest) |
| least-squares slope over T_obs = 5 yr, f_min 1/16 | 2.1e-29 /yr |
| least-squares slope, f_min 1/30 (T_obs 10 / 5 yr) | 2.3e-29 / 5.6e-29 /yr |
| pheno's 2tṫ estimator from modes slower than 1/(5 yr) | 5.9e-29 (f_min 1/16) to 1.02e-28 /yr (f_min 1/30) |

**Rate and verdict.**
- d ln(m_p/m_e)/d ln v = f_N − 1 ≈ −0.7: m_e ∝ v, and m_p ∝ v^{f_N} with f_N = 0.30 (as `rR19-21:79`, RECALLED). ESTIMATE.
- **Main: |d ln(m_p/m_e)/dt| = 94–1260 /yr against 3.6e-17 /yr: ×2.6e18–3.5e19.** All U = 1 branches and coupling sets: ×2.4e18–1.5e20. Dressed branches: ×3.9e18–4.6e20.
- Passing needs |c_H| ≲ 1.4e-21, or a ≳ 1.6e9–5.9e9 ℓ_P (the rate scales as (ℓ_P/a)²).

**Control (F1's uncorrected fermion channel, same estimators).**
- d ln(m_p/m_e)/dQ_E = 8.2e17 − 2.90e19 = −2.81e19 (F1's mapping: e² = 0.1, nucleon weight 5.2, `rF1:248-251`).
- Rate: **×6.0e6–8.0e7.** Panel expectation ~2e8 (`pF/pheno_statement.md:181`). Same order: my estimator keeps only the E_g 2/5 of the power and uses a window slope.
- Ratio of the Higgs channel to the fermion channel: 4.4e11.

### 5.2 F2's rows through the Higgs-induced vacuum stiffness (bridge-conditional)

- **The term.** Δμ = Δ(H†H)·c_H/a², with Δ(H†H) = v²(δv/v)_matter and (δv/v)_matter = −f_Nρ/(v²m_H²) (`rR19-21:79`). Lemma C (`rR19-31:115`) identifies dE_vac/dΦ with Σ_H.
- **The coefficient.** The canonical mapping m_g²a² = 16πμ (`PRICE_NOTE:22`) then gives **μ_ρ = 16π f_N|c_H|/m_H²**. This is density-independent, and independent of a because the mapping builds in G = a² (proved, algebra). At fixed observed G it scales as (ℓ_P/a)².
- **Main:** μ_ρ = 1.53e-8 eV² m³/kg; Earth |m_g| = 9.2e-3 eV. Against F2's rows:

  | F2 row | bound | exceedance |
  |---|---|---|
  | 1, Earth crossing | 1.5e-29 | **×1.0e21** |
  | 5, Galaxy/IGM | 2.7e-19 | ×5.7e10 |
  | 7, PTA | 8e-24 | ×1.9e15 |

  Over all U = 1 branches the Earth row is exceeded by ×9e20–4.5e21.
- **Sign.** For c_H > 0 (every U = 1 branch) m_g² < 0, the **tachyonic** sign. vF2 confirmed the 1D Earth coefficient for the massive sign only; the negative sign "needs a signed waveform analysis" (`TESTS:9292`). The G1-dressed branch is massive. So the Earth-row exceedance is bridge-conditional and, for U = 1, sign-conditional. The clock row (§5.1) is neither.
- **Count once** with R19-21's (F) channel and F5's (iv-c) (`rF5:140`: Earth ≈ 0.02 eV, μ_ρ ≈ 7e-8).
  - New here: the coefficient on the root's actual SF law.
  - R19-21's gauge part used massive-vector-edge slopes, which equals my control C2 (−8.98e-3 per e²). The root's minimal coupling of the Higgs edge to the photon edge gives +2.43e-3: the opposite sign and 3.7× smaller.

---

## 6. (d) Coverage

| clause | covers Σ_H's strain response? | what it removes | removes anything observed? |
|---|---|---|---|
| scalar counterterm as registered (`rR19-31:62`) | No: fixed at h = 0 | — | — |
| (S\*) P177 / (Σ) P179 (`PRICE_NOTE:595,597`) | No. They are lowest-state source clauses; Σ_H(t) in the law and the vev's response are untouched (reading) | (the vacuum's own gravitating rows) | — |
| (S_loc) P182 (`PRICE_NOTE:600`; OPEN, `vR19-21:28`) | **Graviton side only.** Its backgrounds name the Higgs condensate (`rR19-21:45`). In background-field form (P-R19-31a, `rR19-31:255`) it removes the §5.2 Earth-row term by construction (suggested, count once with R19-31). It leaves the clock row, because it does not change the law | the Δ(H†H)·c_H stiffness | no (reading) |
| P-R19-34a (`rR19-34:177`) | No: it covers fermion critical masses only (proved: no m_c(h) in Σ_H″ at one loop) | — | — |
| **P-R19-34a′** (`pF/pheno_statement.md:249`; not registered) | **Yes, by construction** for the mass² channel, at every order if stated so | the clock drift, the Earth-row Higgs term, and the nonlinear vev loss | **No.** Clocks see no drift at 3.6e-17/yr, nor a potential dependence at 7(45)e-8 (`pF/pheno_statement.md:203`). The Einstein equivalence principle needs exactly this (comparator). Required precision: residual ≲ 1/(2.4e18–1.5e20) of c_H, so it must hold at all loop orders |
| panel F's single primitive (`pF/SYNTHESIS.md:83`) | Yes, and it also covers the §4 tadpole condition (the vev renormalization condition) | as above, plus the tadpole channel | no (reading) |

---

## 7. Against the expectation (`TESTS:9446`)

- **"SCALAR-HAZARD": borne out** (worker reading).
- **"by ≥ 1e20": partly.**
  - The bridge-free clock row gives ×2.6e18–3.5e19 on the main branch and ≥ ×2.4e18 everywhere. That is below 1e20 for most branches and estimators.
  - The bridge-conditional Earth row gives ×1e21 (tachyonic sign at U = 1).
  - The shortfall against the panel estimate comes from three things:
    - c_H in SF units is 3.7e-3, not the ~0.05 implied by `rR19-31:124` (H-cov, NN law);
    - the E_g projection;
    - the window-slope estimator.
- **"If so, the single primitive is needed": borne out, and slightly sharpened.**
  - P-R19-34a′ ("every mass parameter") covers Σ_H.
  - The tadpole channel (§4) is a linear, not a mass, condition. As worded only the single primitive names it.
  - Without either, the uncorrected law loses the observed electroweak vacuum in today's nHz background (suggested).

---

## 8. Prices (named, not adopted)

- **P-R19-34a′ (counted once with pheno T4): every mass parameter re-set on every uniformly strained law.**
  - 0 numbers under the law-functional convention (`vR19-24`); a function per class per order under codimension counting.
  - "Imposes rather than predicts" (`vR19-34` item 6, counted once).
  - Gate `AX:114-130`.
- **P-F6a (new): the Higgs tadpole (vev) condition holds on every uniformly strained law.**
  - It is needed beyond P-R19-34a′ unless panel F's single primitive is taken.
  - 0 numbers (same convention).
  - The t = 0 tadpole tuning it extends is itself unbilled (`rR19-20:231`).
- **P-F6b (new, tuning; dominated): zero c_H with F3's dressing family.**
  - G1 alone zeroes c_H at a = 4.90e-3. That is not F1's fermion zero a* = 1.41e-2 (`P/scripts/C5/F3/f3_astar.out:1`), so one amplitude cannot zero both.
  - G1 + G2 zero both at (a₁, a₂) = (6.28e-3, 4.48e-3) (Planck couplings, main).
  - Two numbers per channel, loop order, root and coupling set, tuned to ≲ 1e-21 absolute in c_H. The tadpole needs a third.
  - Dominated by P-R19-34a′ plus P-F6a (zero numbers).
- **Not viable: a coupling zero** (λ* ≈ +0.22 at the grid scale). It conflicts with the observed Higgs mass through running (reading, RECALLED).
- No axiom text changes.

---

## 9. Strong words and limits

- **"Proved"** (short, unrefereed):
  - the scalar lift is unique;
  - scalar gauge paths are unique within F4's families;
  - the group factor;
  - the ξ-term identity (zero at m = 0);
  - Ward by construction;
  - δv/v = −δm²/m_H²;
  - the E_g-only lower bound on the drift;
  - μ_ρ's independence of a under the canonical mapping;
  - "no m_c(h) in Σ_H″ at one loop".
- **"Checked":**
  - every Hessian in §3, converged to ≤ 1e-7 relative, with controls C1–C5 (C1 reproduces R19-31 to all digits; C2 and C3 reproduce R19-11's refereed-table slopes to 4 digits);
  - Y-b reproduces F5's slope;
  - the drift integrals.
- **Estimates and readings:**
  - every SM coupling (RECALLED);
  - f_N;
  - |t| = |h_+|;
  - a = ℓ_P;
  - the NANOGrav background's reality (3.5–4σ);
  - the clock bound value (pre-registered).
- **Not claimed:**
  - two loops;
  - T₂g;
  - a photon-side lift;
  - a chiral SM edge;
  - static-field registration;
  - the nonlinear end state of the vev in the background;
  - any refereed status.

---

## 10. Files (`S/` = `scratchpad/C5/F6/scripts/`)

- `f6_lib.py`: the SF-strained Higgs loops (gauge, quartic, Yukawa and tadpole, and the Y-b helper). It imports `f1_lib.py` and `../arch/` unmodified.
- `f6_controls.py/.out`: C1–C5.
- `f6_nn.py/.out`: the NN law under SF.
- `f6_gauge.py/.out/.err`: loops 1 and 4 (convergence, branches, decomposition, ξ-term).
- `f6_scan.py/.out/.err`: b_s and b_γ sensitivity.
- `f6_yuk.py` → `f6_yuk_a.out/.err` (Y-a, branches, dressings) and `f6_yuk_b.out/.err` (Y-b).
- `f6_drift.py/.out/.npy`: NANOGrav drift of Q_E.
- `f6_sizes.py/.out` with `f6_hy.json` and `f6_tad.json`: c_H assembly, δv/v, clock, Earth row, fermion control, dressing zeros, tadpole.
- `f6_quick.py`: the first timing probe.
