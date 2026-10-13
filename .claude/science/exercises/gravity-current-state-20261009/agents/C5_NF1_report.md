# C5 NF-1 report: the staggered-fermion strain control

- **Worker:** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13 from 21:40Z to about 22:20Z.
- **Hygiene:** no repository file was edited and nothing was downloaded. Every run used OMP_NUM_THREADS=2, and only one heavy process ran at a time. Two light 8×8 checks of about 120 MB overlapped one 240-node run.
  - Peak resident memory was ≤ 633 MB for every run except the four direct re-solves (`nf1_solve3_*`), which peaked at 0.90–0.95 GB, under the 1.0 GB cap.
  - No process of mine is still running.
- **Item:** `TESTS:9448-9474`. The FIXED readings are at `:9469-9473` and the expectation at `:9474`.
- **Paths.**
  - `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`.
  - `S/` = `scratchpad/C5/NF1/`. Scripts and `.out` files are in `S/scripts/`. Unmodified archive copies are in `S/arch/` (F1, F3, F5, R19-34, R18-5, R18-9), with a flat import copy in `S/flat/`. In the copies `f1_lib.py` and `f3_lib.py` only the import path was repointed.
- **Read:**
  - `AX` in full;
  - `TESTS:9146-9474`;
  - panel F: `SYNTHESIS.md`, `condmat_statement.md` (T4) and `skeptic_statement.md` (T2, T4), all in full;
  - rF1 and vF1;
  - rR19-34 and vR19-34;
  - vR9-1 and `TESTS:3600-3660,3839-3850`;
  - rR18-9 in full;
  - rR19-12 §0 and vR19-12;
  - rF5 (grep: knock-on, z″, (iv));
  - `f1_lib.py`, `f3_lib.py`, `f3_mat.py`, `f3_dirac.py`, `f5_mult.py`, `f5_sizes.py`, `lib9.py`, `smud_lib.py`, `dfam.py`, `dirac.py` and `sublum.py`.
- **Labels:** proved (a complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED means from memory.

## 0. Plain words, and the reading

1. **Strain cannot give a staggered fermion a mass (proved; checked).** I built a staggered fermion from the root's own momentum law: one mode per site, b_f = 0.909103708, no Wilson term. I strained it with the registered SF flow and coupled it to the root photon with F1's links.
   - Its zero-momentum self-energy is exactly zero at every strain and every loop order. This holds for every uniform strain channel (E_g, T₂g and trace), not only E_g, so the strain Hessian of the additive mass is identically 0.
   - **One correction to the panel.** The symmetry that does this is not the continuous "U(1)_ε" the panel named. With continuous time, U(1)_ε is not a symmetry of the law at all, even unstrained.
   - Two discrete symmetries survive instead:
     - a sublattice "chirality" (Θ), which flips the sign of the Hamiltonian under ε;
     - inversion combined with ε (P_stag).
   - Strain and gauge links keep both. Θ forces the self-energy to anticommute with ε and P_stag forces it to commute, so it must vanish.
2. **The controls work (checked).**
   - F3's dressing G₁, which breaks ε, brings the mass back: Hessian = 2a × (−0.883) e².
   - An explicit ε-breaking "ε-Wilson" term gives −1.7e-3 to −1.2e-2 e².
   - A dressing that respects ε keeps the zero.
3. **What remains is proportional to the particle's own mass (checked; sizes conditional).**
   - Multiplicative channel: z″ = +1.14e-2 e².
   - Mapped like F1, that is μ_ρ ≈ 2e-42 eV² m³/kg. It is 1.3e-13 of F2's Earth-crossing row and 7e-24 of the Galaxy/IGM row.
   - It sits about 10 times above F2's pulsar row, but that row is a toy forecast, not a bound.
4. **Two by-products (proved).**
   - There is no critical-mass counterterm, so F5's knock-on onto the vacuum μ_E row is zero.
   - The staggered vacuum is even in m, so the Wilson-c₁ part of R19-21's Higgs-vev channel (F5 residual iv-b, ×3e38) vanishes.
   - The even Higgs-mass² part (iv-c, ×5e21) is untouched. It is F6's channel.
5. **The cost is tastes (proved by counting; R9-1 arithmetic checked).**
   - Each staggered field is two identical Dirac copies, with the same charges and the same mass.
   - The SM's 22.5 Dirac fields would be 11.25 staggered fields, which is not an integer. Each charge type has 3 generations, which is odd.
   - So the SM count cannot be matched. There are two ways to resolve it:
     - **(T1) Give every SM field a twin.** This is R9-1's exclusion in kind: a twin electron alone adds 84 MeV to the Z width, against an error of 2.3 MeV.
     - **(T2) Pair the tastes across generations:** (e, μ), (u, c), (d, s). The odd third generation then needs a fourth, vector-like family plus 3 ν_R, made heavy by taste-splitting masses.
   - T2 is a content price. It is not computed here, and as far as checked it is not excluded by observation (suggested).
6. **Rows (checked; estimate scope).**
   - The staggered band is separable, so μ_T2 ≡ 0. The knob r, which R18-9 spent on μ_T2, is no longer needed, and neither is the row.
   - That leaves 3 rows with 3 tunings. Direct roots exist for all three content choices, but only at a small-box photon edge γG_w(0.6, fw 0.5), not at the root's photon.
   - Not recomputed: the off-axis rows, the charge rows (R19-12), the tadpole and the CC.
7. **Worker reading: NF-TASTE-WALL**, with the scope correction that the exact symmetry is the discrete pair (Θ, P_stag), not U(1)_ε (§4).

## 1. Class, hypotheses and choices (stated before any title)

**Arena.**
- Z³ × ℝ (continuous time), one loop for the numbers and all orders for the symmetry statements.
- U(1), Euclidean, external P = 0.
- Feynman gauge for the numbers; any covariant gauge for the proofs.

**Staggered law (`TESTS:9451`).**
- h = Σ_j η_j(x) S_j, with η₁ = 1, η₂ = (−1)^{x₁}, η₃ = (−1)^{x₁+x₂}.
- S_j has symbol s(k_j), where s = SymS(0.909103708) is the root's odd box symbol and r = 0.
- Reduced zone (8 offsets n ∈ {0,1}³): h(k) = Σ_j s(k_j) Γ_j, with Γ_j[n, n⊕ν_j] = (−1)^{n_j} and ν = (000, 100, 110). ε = (−1)^{x₁+x₂+x₃} gives Γ_ε[n, n⊕111] = 1.
- Mass term: m ε(x) χ†χ, so m Γ_ε.

**Strain.**
- SF of the staggered band E² = Σ s(k_j)² (+m²): dk/dτ = (t/2) h·p, with p_j = s(k_j) s′(k_j).
- For E_g, h = diag(1, −1, 0) and the flow is separable. T₂g and A₁ are also checked.
- The photon is Gph(2.9435) with its own separable flow (F1's B1). The photon is left unstrained in the T₂g and A₁ checks (F1's control branch), because the registered frame photon is singular for T₂g (`TESTS:9391`).

**Links.**
- F1's generalized (divided-difference) links on axis-ordered paths with Psym (`f1_lib.py:7-12`).
- For axial hops (E_g) every path family coincides: Psym, single orderings, staircases and the straight segment. For T₂g the hops leave the axes; the proofs hold for any c-number link functional.

**Dictionary (proved; checked).**
- (Γ₁, Γ₂, Γ₃, Γ_ε) is an 8-dimensional Cl(4) representation, unitarily equal to (α_j, β) ⊗ 1₂ (`nf1_alg.out:16-17`, 7.5e-16).
- So F1's and F3's reduced one-loop formulas apply to the staggered law with β → Γ_ε, and the staggered law is "F1's D1(b_f, r = 0)" under this map.
- The direct 8×8 evaluator agrees with F3's reduced formula to ≤ 5e-19 absolute on common grids (`nf1_sigma8_N32.out:8-19`).

**Branches (`TESTS:9453-9455`).**
- (A) the staggered law;
- (B) F3's G₁ dressing in staggered form, iΓ_εΓ_j sin k_j, which is the KS image of F3's G₁ with β → ε (control);
- (C) an explicit ε-breaking term, r_c Σ_j sin²k_j Γ_ε (control). It is π-periodic, so it is a legal staggered operator; it is same-sublattice and zero at all 8 corners.
- (D) an ε-respecting dressing, Σ_{j<k} iΓ_jΓ_k sin k_j sin k_k, as a mechanism check.

**Not computed:**
- two loops;
- non-abelian vertices beyond C_F;
- Yukawa, W/Z and Higgs loops;
- the T₂g photon law;
- the charge rows (R19-12) and off-axis rows (R18-13) for the staggered edge;
- the taste-splitting operators of option T2;
- chiral electroweak couplings. These are absent for the Wilson edge too (`rR19-34:74`).

## 2. Prior art (counted once)

- **Panel F.**
  - Condensed-matter T4 (`condmat_statement.md:216-224`): the proof that U(1)_ε survives SF, audited in §3(a).
  - Skeptic T2/T4 (`skeptic_statement.md:264-269,322-340`): s(k + π) = −s(k) and the π-periodic driving field, both reproduced here (`nf1_alg.out:2-8`).
- **R19-34:** `rR19-34:112-113`, the r = 0 and staggered per-axis zeros (H-cov).
- **F1/vF1 and F3** (`f3_resp_main.out:6`: L[G₁] = −0.8586 on the Wilson root).
- **F5:** `rF5:40,134,139,140`.
- **R18-9:** (S1) at `rR18-9:140-143`; the root record at `:225-229`.
- **R9-1/vR9-1:** `vR9-1:9`, `TESTS:3839-3842`.
- **Comparators (RECALLED):** Kogut–Susskind Hamiltonian staggered fermions (2 tastes in 3D); the 4D Euclidean U(1)_ε; Kawamoto–Smit spin diagonalization; LEP Γ_Z and N_ν; LHC vector-like fermion limits.

## 3. Results

### 3(a) The symmetry, proved, and the panel's proof audited

**L1. Flow compatibility (proved; checked).**
- s(π − k) = s(k) and s is odd, so s(k + π) = −s(k) (checked to 7.8e-15).
- Hence each p_j = s s′(k_j) is odd and π-periodic in every k_l. The time-1 flow of (t/2)h·p then commutes with k → −k and with k → k + πe_l for every l and every symmetric h.
- So s_{j,t} := s∘(Φ_t)_j satisfies s_{j,t}(k + πe_l) = (−1)^{δ_jl} s_{j,t}(k) and is odd. Checked for E_g to ≤ 1e-14 (`nf1_alg.out:3-8`).
- Every strained hop of η_j S_{j,t} is therefore odd along j and even across, so it joins opposite sublattices.
- Position space at L = 8 (`nf1_alg.out:9,14`): the spectrum equals the reduced-zone symbol to 1.8e-14, and the same-sublattice weight is ≤ 2e-15.

**L2. U(1)_ε is not a symmetry with continuous time (proved).**
- [Σ_x ε_x n_x, χ†_x χ_y] = (ε_x − ε_y) χ†_x χ_y ≠ 0 for every hop. In the Euclidean action, χ̄∂_τχ is not invariant under χ → e^{iθε}χ, χ̄ → χ̄e^{iθε}.
- This fails already at t = 0 and has nothing to do with strain (`nf1_alg.out:10`: ‖[ε, h]‖/‖h‖ = 2).
- U(1)_ε is a symmetry of the 4D staggered action with discrete time (comparator, RECALLED). The C5 arena has continuous time (rF1 §1).

**L3. The exact symmetries (proved).**
- **Θ** (Euclidean form): χ(x,τ) → ε_x χ(x,−τ), χ̄ → −χ̄ε_x, A₀ → −A₀(x,−τ), A_j → A_j(x,−τ).
  - The kinetic term is invariant by time reversal with the A₀ sign. Every hop is invariant because ε_xε_y = −1 (L1), for any link functional. The photon action and covariant gauge fixing are invariant. The mass term mχ̄εχ is odd.
  - In Hamiltonian form Θ is the antiunitary K·C_ε, with χ_x → ε_x χ_x† and E → −E.
  - ⇒ εΣ(ω,k)ε = −Σ(−ω,k).
- **P_stag:** χ(x) → ε_x χ(−x), A_j(x) → −A_j(−x), A₀(x) → A₀(−x).
  - Invariant because s_{j,t} is odd (L1), η_j(−x) = η_j(x), ε anticommutes with odd hops, d² is even with an odd photon flow, and uniform strain is inversion-even.
  - ⇒ Γ_ε Σ(ω,k) Γ_ε = Σ(ω,−k).
- Checked in position space with random U(1) links and t = 0.3: {ε, h[U]} = 0 and P h[U] P⁻¹ = h[U^P], both to 4e-15 (`nf1_pstag.out:8-10`).

**Theorem (proved).**
- At ω = 0 and k = 0, Σ both anticommutes and commutes with the invertible Γ_ε, so Σ(0,0) = 0. That covers all 64 entries, so both tastes, every mass structure (β⊗A and iβγ5⊗B), every uniform strain (E_g, T₂g, A₁) and every order in e.
- Hence δm(t) ≡ 0 and ∂²_t δm ≡ 0.
- The zero is gauge-parameter independent, because it holds in any covariant gauge.
- It holds for every lift V that commutes with ε and keeps P_stag (branch D checked). An ε-breaking lift re-admits the mass (branch B).

**Audit of the panel's T4.**
- **The conclusion is correct.**
- **Gaps:**
  1. The symmetry is misnamed: U(1)_ε does not exist here (L2).
  2. "εH_tε = −H_t" alone (that is, Θ) excludes only the ε-commuting masses. The ε-anticommuting "twisted taste" masses (iβγ5 ⊗ B) also open a gap, and excluding them needs P_stag, or the shift symmetry.
  3. The flow condition needs covariance under the per-axis π-shift, not only under the Π shift. It holds (L1).
  4. The links are generalized divided-difference links, not Peierls links. The argument holds for any c-number link functional.
  5. For T₂g strain the hops leave the axes. They are still opposite-sublattice.
- **The panel's own caveat is confirmed:** an ε-breaking dressing re-admits the mass.

### 3(b) The additive-mass Hessian and the controls (checked)

| branch | quantity | 156 nodes | 240 nodes | source |
|---|---|---|---|---|
| A, staggered, E_g SF | δm(t), t ∈ {0, ±0.003, 0.006, 0.05, 0.2} | 0 exactly | 0 exactly | `nf1_conv_A_240.out:2-7` |
| A | ∂²_t δm | 0 | 0 | `:8` |
| same grid, Wilson root (check) | δm; Hess_t | +0.041858391; +2.4238554e-2 | +0.041858390; +2.4240272e-2 (= F1 B1) | `nf1_conv_A_*.out:9` |
| A, direct 8×8, all 64 entries of Σ(0), E_g t = 0, ±0.1, 0.2 | max | — | ≤ 1.2e-17 (N = 32) | `nf1_sigma8_N32.out:3-6` |
| A, T₂g and A₁ (photon unstrained) | all entries | — | ≤ 5.4e-17 (N = 24) | `nf1_t2g_N24.out` |
| D, ε-respecting dressing, t ≤ 0.2 | all entries | — | ≤ 1.7e-17 | `nf1_sigma8_N32.out:21-25` |
| **B, G₁ dressing (control)** | L = dδm/dε | −0.8833075 | −0.8833075 | `nf1_conv_B_240.out:2` |
| B, G₂ | L | −1.4962585 | −1.4962585 | `:4` |
| **C, ε-Wilson r_c = 0.05 / 0.1 / 0.3 (control)** | δm(0); Hess_t | +0.01935 / +0.03864 / +0.11392; −1.7287e-3 / −3.5097e-3 / −1.2028e-2 | same, to 2e-9 | `nf1_conv_C_240.out:2-4` |

- **Control B.** Hess_t = 2aL (F3's form).
  - |Hess| ≥ 1e-3 e² for |a| ≥ 5.7e-4.
  - At F3's a* = 0.0141 it is −2.49e-2, the size of F1's channel.
  - The Wilson root's L is −0.8586 (`f3_resp_main.out:6`).
  - In position space G₁ creates same-sublattice hops of relative weight 2.7e-2 at a = 0.01, and leaves the spectrum unchanged to 1e-14 (`nf1_alg.out:11-13`).
- **Control C.** It also has nonzero T₂g and A₁ responses (`nf1_t2g_N24.out`).
- **Mapped like F1 (conditional;** `nf1_sizes.out:8-18`): an ε-breaking term must keep |Hess_t| ≤ 1.5e-10 e² to pass the Earth row.

### 3(c) The multiplicative channel (checked coefficient; sizes conditional)

**Coefficient.**
- z″ = ∂²_t[δm/m] = **+1.139e-2 e²**: +1.1375e-2, +1.1395e-2 and +1.1393e-2 at m = 0.0025, 0.005 and 0.01 on 240 nodes. 156 nodes agree to 2e-3 relative (`nf1_conv_M_240.out:7-10`).
- Method: F5's off-shell P = 0 estimator (`f5_mult.py`), photon Gph(2.9435).
- The Wilson root's value is −4.6e-3 (`rF5:134`).

**Sizes** (F1/F5 mapping: canonical TT-pole reading, a = 1/M_P with G = a², SM mapping an estimate; `nf1_sizes.out:2-5,21-24`):
- nucleons: μ_ρ = 2.0e-42 eV² m³/kg (massive sign);
- Earth crossing: ×1.3e-13;
- detector: ×2.0e-13;
- PTA: ×2.5e-19;
- Galaxy+IGM: ×7.3e-24;
- electrons: ×3.2e-15 of the Earth row;
- pulsar toy forecast: ×9.9 (F2's referee: a toy, not a bound, `TESTS:9294`);
- hot era: m_g²/H² ≤ 9e-4.

**By-products (proved).**
- m_c(t) ≡ 0, so F5's knock-on Δμ_E = −e_m m_c″ (+1.689e-2 per field on Wilson edges, `rF5:40,158`) is identically zero.
- Θ maps m → −m and is exact at every strain, so every vacuum quantity is even in m: c₁ = ∂μ_vac/∂m|₀ = 0.
  - So F5's residual (iv-b), "vev shift × Wilson c₁" (×3e38, `rF5:139`), is absent on staggered edges.
  - The even part (iv-c) (×5e21, `rF5:140`) remains. It is the Higgs mass² channel (F6), counted once there.

### 3(d) Tastes, R9-1 and the rows

**Count (proved by counting; the premise is a reading).**
- **The premise:** gauge links act on the single component, so both tastes carry identical charges. RECALLED: the only exact continuous internal symmetry of one staggered field is U(1)_V.
- One field is 1 mode per site. Its 8 corner modes = 8 = 4 ⊗ 2, which is 2 Dirac tastes (`nf1_alg.out:9,16`).
- The tastes are mass-degenerate: the mass is Γ_ε = β⊗1, and §3(a) forbids any radiative splitting at m = 0.
- Hence:
  - 22.5 = 2 × 11.25, which is not an integer;
  - a single Weyl ν is not a staggered field;
  - each SM charge sector has 3 generations, which is odd.
- **The SM count cannot be matched.**

**(T1) Twins** (one staggered field per SM Dirac field, N_s = 22.5).
- This is R9-1's L/G-out mechanism in kind: same-charge, same-mass corner copies, coupled point-locally.
- One twin electron adds Γ_ℓℓ = 83.984 MeV to Γ_Z, against σ = 2.3 MeV: 36σ (inputs `vR9-1:9`; checked arithmetic).
- All twins below M_Z/2 add about +2.5 GeV, doubling Γ_Z. Twin ν's give N_ν ≈ 6 (LEP ≈ 3, RECALLED).
- **Excluded.**

**(T2) Tastes as generations** (suggested; not computed).
- Pairs: (e, μ), (u, c), (d, s), (ν_e, ν_μ) and (τ, τ′), (t, t′), (b, b′), (ν_τ, ν′).
- Content: SM + 3 ν_R + one vector-like family, 32 Dirac = 16 staggered fields.
- **Requirements:**
  - taste-split bare masses (β⊗τ₃-type, which break the shift symmetry and break Θ softly);
  - a heavy fourth family (vector-like limits around 1–1.5 TeV, RECALLED);
  - m_{ν′} > M_Z/2.
- The light partners' additive shifts are proportional to the splitting: ≤ GeV for the pairs that make up the Earth's matter, about TeV for the third-generation pairs. So their strain channels are of multiplicative size (μ_ρ ≲ 1e-37, ≥ 1e8 below the Earth row; estimate).
- **Not computed:**
  - the splitting operators and their locality;
  - the mild tuning m ≈ m′ for τ, t and b;
  - electroweak chirality, which is common to both edges.

**Rows.**
- **μ_T2 ≡ 0 for every staggered field** (proved: separable band, R18-9 (S1); checked 0, `nf1_rows.out`). So R18-9's r knob and its row both drop out.
- **Per-field rows.** Staggered rows per field = ¼ × naive D1(b_f, 0) rows.
  - For μ_E and μ_T2 (traces over the free sea) this is proved by Kawamoto–Smit: the naive law is 4 staggered copies for every per-axis operator that is odd along its own axis and even across.
  - For the Ξ rows it is proved for the SF-generator form of UD at r = 0 (E_g: α_j s′p_j(k_j); T₂g: α_x s′(k_x) p_y(k_y)). That the archived finite-q midpoint UD implementation keeps this structure is a reading.
- **Values at b_f = 0.909, per staggered field:**
  - Ξ_T2g +4.95e-4, Ξ_Eg −1.02e-4, μ_E −5.28e-3 (`nf1_rows.out:7`);
  - Wilson root per Dirac field: +1.985e-3, +1.32e-4, −1.709e-2 (`:13`, reproducing R18-9's record).
- **Sea μ_E pull.** It is 6.5 times weaker: −0.059 for N_s = 11.25, against −0.385. R18-9's large-box photon (+0.342) can no longer be balanced.
- **Sampled map.** E_g-residual sign changes along b_f appear at γG_w(0.6, fw 0.5) (`nf1_rows.out`).
- **Direct roots** (checked; rows ≤ 1e-16; all edges subluminal; scalars G_w at fr = 1; m = 0.01; photon γG_w(0.6, 0.5(π − 0.6))):

| content | photon N | b_s | b_f | a | det J (σ_min) | source |
|---|---|---|---|---|---|---|
| N_s = 11.25 (formal) | 48 | 1.3285 | 1.2315 | −0.1072 | 7.8e-5 (1.3e-3) | `nf1_solve3_Ns11.25_N48.out` |
| N_s = 11.25 | 96 | 1.2699 | 1.1615 | −0.1072 | 7.2e-5 (1.3e-3) | `nf1_solve3_Ns11.25_N96.out` |
| N_s = 16 (T2) | 48 | 1.5361 | 0.9504 | −0.1068 | 1.1e-4 (1.6e-3) | `nf1_solve3_Ns16_N48.out` |
| N_s = 22.5 (T1) | 48 | 1.7706 | 0.7277 | −0.1062 | 1.7e-4 (2.0e-3) | `nf1_solve3_Ns22.5_N48.out` |

- **So the root can be re-solved with one fewer knob:** 3 rows and 3 tunings, against R18-9's 4 + 4 + window.
- **Caveats:**
  - The knob values move about 5% between photon N = 48 and 96, along the weak direction, as in R18-9.
  - Only one photon edge was solved. Whether that edge sits in a window or an open region is not mapped.
  - The photon is no longer Gph(2.9435), so every photon-dependent row moves: R19-12's charge rows, R19-31, and z″ (whose margin is 1e13).
  - The off-axis rows, the tadpole and the CC are not recomputed.

## 4. Against the FIXED readings (`TESTS:9469-9473`), literal first

| reading | clause | status |
|---|---|---|
| **NF-ZERO** | the symmetry is exact | **the named U(1)_ε: no** (L2, fails at t = 0, independent of strain). The protecting discrete remnant (Θ, P_stag): **yes**, at every uniform strain and with any link functional (proved; checked) |
| | Hessian ≡ 0 | **yes** (proved; exactly 0 checked) |
| | residual below F2's Earth row | **yes**, ×1.3e-13 (conditional mapping) |
| | no taste wall applies | **no** (§3(d)) → NF-ZERO not met |
| **NF-TASTE-WALL** | NF-ZERO on strain; taste content conflicts with the SM count or R9-1 | **met (worker)**. On strain: zero, with the symmetry-name correction. Taste: the SM count conflicts (11.25 is not an integer; 3 generations per sector is odd), and the twin assignment is excluded by R9-1's Z width (36σ from one twin electron) |
| NF-BROKEN | symmetry breaks and Hessian ≥ 1e-3 | **not met.** The Hessian is ≡ 0. Values ≥ 1e-3 appear only when ε is broken by hand (controls) |
| OPEN | otherwise | not met, unless "the symmetry" is held to mean U(1)_ε literally. Then neither NF-ZERO's first clause nor NF-BROKEN's second holds, and the literal reading would be OPEN. **Flagged for the referee** |

**Worker reading: NF-TASTE-WALL.** The strain channel is zero by a law-level discrete symmetry. The cost is a taste/count conflict whose minimal priced resolution (T2) is not shown to be observationally excluded.

## 5. Against the expectation (`TESTS:9474`)

- **"NF-ZERO on strain, then NF-TASTE-WALL overall": borne out,** with one correction: the mechanism is (Θ, P_stag), not U(1)_ε.
- **Not anticipated:**
  - all strain channels (T₂g and trace) are also zero;
  - μ_T2 vanishes identically, so the root re-solves with 3 knobs;
  - the vacuum knock-on and the Wilson-c₁ Higgs-vev channel vanish;
  - the taste wall is a count conflict that a heavy vector-like family plus ν_R can absorb at the level of observations checked here (suggested), rather than an outright exclusion.

## 6. Strong words

- **"Proved"** (short, unrefereed):
  - L1, L2, L3 and the theorem;
  - the dictionary;
  - the KS ¼ rule for per-axis odd/even-across operators (for the Ξ rows, the archived finite-q UD keeping that form is a reading);
  - μ_T2 ≡ 0;
  - c₁ = 0;
  - the zero knock-on;
  - the counting.
- **"Checked":** every number in §3, with the grids stated.
- **"Every strain":** uniform strains only. Non-uniform strain gives gradient terms, not computed.
- **"Every order":** perturbative. It assumes the regulated lattice theory keeps Θ and P_stag, which holds for the U = 1 law and for ε-commuting lifts.
- **Not claimed:**
  - two loops numerically;
  - Yukawa or Higgs loops;
  - the T₂g photon;
  - R19-12's charge rows;
  - the off-axis rows;
  - that T2's operators exist and are local;
  - electroweak chirality;
  - any statement about the Higgs channel (F6).

## 7. Prices (named, not adopted; no axiom text changes)

- **P-NF1a: the native staggered fermion (the `AX:178` route) with charge-identical taste pairing.**
  - Content: SM + 3 ν_R + one heavy vector-like family; masses from taste-split (shift-breaking) bare terms.
  - It replaces P-R19-34a for fermions, by symmetry rather than by clause. It also removes F5's knock-on and the Wilson-c₁ channel.
  - It leaves the Higgs mass² channel (F6) and the multiplicative residual (safe).
  - Gates: `AX:120-123`, `AX:178`.
  - Twins (T1) are excluded (R9-1).
- **P-NF1b: the strained law's lift must keep Θ and P_stag** (ε-commuting dressings only). Without it, an F3-type ε-breaking dressing re-admits the channel (control B), and the F1 referee's lift ambiguity returns.
- **P-NF1c: the photon edge moves to the small box** γG_w(0.6, fw 0.5) for the 3-row re-solve, in place of R18-9's window P-R18-9a. Whether this is an open region or a window is not mapped.
- **Reading:** the root's site needs 16 modes per site (T2), against 90 for the Wilson edge. That still exceeds one qubit per site (`AX:47`; the skeptic's dimension count).

## 8. Files (`S/scripts/`)

- `nf1_alg.py/.out`: algebra, flow compatibility, position-space checks, G₁ in position space, and the dictionary. Saves `nf1_gammas.npy` and `nf1_dict.npy`.
- `nf1_poslib.py` (an extract of `nf1_alg`) with `nf1_pstag.py/.out`: P_stag and Θ with random links.
- `nf1_sigma8.py` → `nf1_sigma8_N24.out`, `nf1_sigma8_N32.out`: the direct 8×8 Σ(0) for A–D, against F3's reduced formula.
- `nf1_t2g.py` → `nf1_t2g_N24.out`: T₂g, A₁ and E_g with the photon unstrained.
- `nf1_conv.py` → `nf1_conv_{A,B,C,M}_{156,240}.out`: converged values via F1/F3 (A: zero plus the F1 check; B: L[G₁], L[G₂]; C: the ε-Wilson Hessian; M: z″).
- `nf1_sizes.py/.out`: F2-row sizes.
- `nf1_rows.py/.out` with `nf1_rows_naive.npy`: staggered rows and the sampled re-solve map.
- `nf1_solve3.py` → `nf1_solve3_*.out`: direct 3-row roots.
- `*.time`: peak memory per run.
- `run_conv.sh`.
- Copies (imports repointed only): `f1_lib.py`, `f3_lib.py`, `f3_dirac.py`, `f5_sizes_copy.py`.
