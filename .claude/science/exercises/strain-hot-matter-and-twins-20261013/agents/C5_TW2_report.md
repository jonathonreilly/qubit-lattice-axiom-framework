# C5 TW-2 report: twins as generations with realistic taste splitting — how much strain leak comes back

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-14, 12:56Z to about 13:35Z. No repository file was edited; nothing was downloaded; main's prior-art notes were read with `git show origin/main:…` into `S/../prior/`.
- **Memory:** OMP_NUM_THREADS=2, one process at a time; peak resident set ≤ 383 MB (340-node runs), all others ≤ 250 MB (`S/*.time`). No process of mine is still running.
- **Item:** `TESTS:9633-9645` (shared setting `:9613-9617`; FIXED readings `:9641-9644`; expectation `:9645`).
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX`/`vX` = `P/agents/C5_X_report.md` / `…_referee_verdict.md`; `S/` = `scratchpad/C5/TW2/scripts/` (copies of `f1_lib.py`, `f3_lib.py`, `f3_dirac.py`, `nf1_alg.py`, `nf1_sigma8.py` from `P/scripts/C5/NF1`, and `dirac.py`, `sublum.py`, `r1934_lib.py` in `S/../flat/`; imports unchanged — the relative layout was reproduced, so no repointing was needed). `main:` = `origin/main:docs/`.
- **Labels:** proved (complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED = from memory.

## 0. Plain words, and the reading

1. **What splitting the twins takes (proved; checked).** A staggered field has two identical "twin" copies (NF-1). To make them an electron and a muon you need a term that gives the two twins different masses. On this lattice the shortest such term is a hop across the face diagonal of a lattice square (cos k₁ cos k₂ in momentum space). Nothing at nearest-neighbour range does it. The term has to point along a lattice direction: the three possible terms rotate into each other like the three components of a vector, so no choice is rotation-symmetric. Any realistic splitting therefore picks a preferred lattice direction and breaks the rule's rotation and one-step translation covariance (`AX:57-58`). That is a price, not a derivation.
2. **The leak the test asked for is small (checked; sizes conditional).** Splitting does reopen the strain channel that NF-1 had closed, and it is proportional to the splitting σ, as expected. But the σ that real generations need is tiny in grid units (about 4e-21 for e–μ, 5e-20 for u–c). The reopened second-order strain response of the light twin is +0.124 σ e² per unit strain², about 11 times NF-1's multiplicative residual coefficient, and it is multiplied by σ, not by the Planck mass.
   - Earth crossing: about 1e-10 of F2's bound. Clock row: about 1e-12 of the bound. Only F2's binary-pulsar toy forecast (not an observational bound, per vF2) is exceeded, by about 6e3.
3. **But the same splitting opens a first-order leak that the pre-registration did not anticipate (checked; sizes conditional).** Because the splitting term picks a lattice direction, the light twin's mass now shifts *linearly* with the strain component along that direction: +0.045 σ e² per unit strain. This does not shrink with the grid spacing (it is a fixed fraction of σ/m_light). The nanohertz gravitational-wave background then drives a drift of m_p/m_e of about 2–6e-16 per year, **5 to 18 times the clock bound** (3.6e-17 per year), for the minimal splitting term with a 1.5 TeV fourth family. The electron side alone is ×14 and the proton side alone ×9.
   - This is branch dependent. With the next-longer splitting term (cos k₁ cos k₂ cos 2k₃) the first-order coefficient is 17 times smaller and the drift is 0.3–1 times the bound. A tuned one-number mixture of the two zeroes it at one loop.
4. **Third generation (counting proved; sizes conditional).** Twins come in pairs and there are three generations, so the third needs a partner: a fourth (vector-like) family, as NF-1 found. Heavier partners make the leak larger in proportion. A partner at the grid scale brings the Earth-row hazard back once m_b′ ≳ 2e13 GeV. With the minimal splitting term, even a 1.5 TeV b′ already puts the first-order clock leak at about ×6.
5. **The other decomposition (prior art on main).** Main's generation lane reads the 8 corners by Hamming weight, 1+3+3+1, with the hw=1 triplet as three generations. TW-2 assumes NF-1's decomposition instead: 8 = (4-component Dirac spinor) ⊗ (2 tastes). Under the Hamming reading the generation-separating operator is the Wilson/K0 term at grid strength. It is not a mass in the Dirac sense, and its hw=1 levels are already split by one loop at t = 0 and split linearly by strain at Planck strength (coarse checks). So that reading needs no fourth family, but it moves the leak back to F1's Wilson size or worse.
6. **Reading (worker):**
   - **SPLIT-SAFE** on the literal, pre-registered quantity (the reopened additive-mass strain *Hessian*). This holds in every branch run: ≤ 1.2e-10 of the Earth rows and ≤ 6e-13 of the clock row.
   - **Flagged for the referee:** the same splitting reopens a first-order channel that exceeds the clock row by ×5–18 for the minimal splitting family.
   - If "the leak" in the FIXED text includes first-order terms, the reading is SPLIT-HAZARD (clock row) for the minimal family. Across splitting-symbol branches it is OPEN, because the range-(1,1,2) branch sits at ×0.3–1.
   - The expectation's mechanism ("needed at grid-scale size, reopens ∝ σ") holds only for a grid-scale third-family twin or under the Hamming-weight reading.

## 1. Class, hypotheses, choices (stated before any title)

- **Arena:** NF-1's (`rNF1:59-99`). Z³ × ℝ; staggered field with the root's odd box symbol s = SymS(0.909103708), r = 0; one-loop U(1); Euclidean; external P = 0; Feynman gauge; Psym links; lift U = 1; photon Gph(2.9435) with its own separable SF flow. Couplings and the SM mapping are ESTIMATES copied from F1 (`rF1:247-252`).
- **Fermion flow:**
  - FB1 is the taste-blind staggered band, E² = Σ s(k_j)² (NF-1's flow; separable).
  - FB2 is each split band's own flow. It differs from FB1 only through M∂M = (m ± σg)(±σ∂g) = O(σ², mσ). So every O(σ) coefficient below is FB1 = FB2 (proved). Physical σ, m ~ 1e-20.
- **Strains** (diagonal, SF units t, F6's Q_E normalisation `rF6:182`):
  - Eg = diag(1, −1, 0), the registered one;
  - tet = diag(−1, −1, 2)/√3, the other E_g component, with the same Q_E = t².
  - T₂g is **not computed**: F1's frame photon is singular for T₂g (`TESTS:9391`; G-F5a).
- **Splitting family** (`TESTS:9636`, "taste-non-singlet mass, or an ε-odd hop"):
  - main: σ cos k₁ cos k₂ M₁₁₀ (§3a);
  - branches: two longer-range symbols of the same class; the body-diagonal direction; the ε-odd ("twisted") family.
- **Coefficients:**
  - Σ_τ(m, σ; t) = m A(t) + τσ B(t) + O(mass²), with τ = ± the taste block.
  - A = NF-1's singlet z.
  - Light twin (τ = −) with m = m_l + σ: δm_l = m_l A + σ(A − B).
  - **The leak is σ(A − B)**, with strain parts σ(A′ − B′)t + ½σ(A″ − B″)t².
- **Not computed:**
  - two loops; non-abelian beyond C_F; Yukawa/Higgs loops; T₂g;
  - F3-type O(t²) lifts beyond P-NF1b;
  - chiral electroweak couplings;
  - an on-shell (ω ≠ 0) treatment of the hw-lane levels;
  - any spontaneous mechanism for the splitting.

## 2. Prior art (counted once)

**C5:**
- **NF-1 + vNF1.** Θ and P_stag force Σ(0, 0) = 0 for all 64 entries (`rNF1:139-143`; `vNF1:7`). NF-1 counted 2 Dirac tastes per field and the T2 content SM + 3ν_R + one VL family (`rNF1:202-229`). The referee: "T2 is untested … taste splitting breaks Θ" (`vNF1:13`).
- NF-1's multiplicative z″ = +1.139e-2 is reproduced here to all digits (`S/tw2_conv_S_240.out:6-8` vs `P/scripts/C5/NF1/nf1_conv_M_240.out:7-9`).
- F1 + vF1: the mapping and the Wilson channel (`rF1:35-37,247-275`; `vF1:5-7`).
- F2 + vF2: rows (`rF2:95-106`); pulsar row a toy forecast (`vF2:9`); signed Earth bound (`vF2:5`).
- F6 + vF6: clock estimator and drift (`rF6:211-235`; `vF6:7`).
- F3/F4: lift and path freedoms start at O(t²) (`TESTS:9248,9309`).

**Main (read with `git show origin/main:…`; copies in `scratchpad/C5/TW2/prior/`):**
- **`THE_GENERATION_COUNT_IS_THE_SPATIAL_DIMENSION…_2026-09-03.md` (bounded, source-corrected 09-09)**, with `.claude/science/physics-loops/generation-correction-20260909/CORRECTION_HISTORY.md`.
  - What the note proves for supplied K1 + λM_W operators on finite tori:
    - the kernel is the 2^d corners;
    - on the corners, M_W = 2 hw with multiplicities C(d, k) (`:57-66`);
    - the hw=1 label algebra is M_3(C) with scalar commutant, "not a theorem that plain translations or the cycle are global symmetries of the whole K1 operator" (`:90-97`);
    - a central K0 corner projector exists (`:123-137`).
  - What is excluded or withdrawn (`CORRECTION_HISTORY:5-9`):
    - the continuous isolation window, since a noncorner wave collides at λ = 2/5 and 2/3 (`:80-86`);
    - algebraic nonselection on K0;
    - every physical generation or species reading, and kinetic selection (`:174-182`).
- **`CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES…_2026-06-08.md`.** The Dirac γ₅ is generation-blind. Generation (Koide) chirality needs a C₃-breaking operator on the generation R³ (`:58-69`). Open.
- **`C3_GENERATION_READOUT_CONTEXT…_2026-07-02.md`.** A naming definition only: singlet I and doublet B = J − I. It supplies no weights (`:19-28,48-53`).
- **`staggered-dirac-a1a2-realization-closure-20260710/`** (GOAL, NO_GO_LEDGER, HANDOFF; PR #5125 unmerged).
  - No-go: the four axioms do not select the staggered kinetic law or its eight-corner zero set. The countermodel is the I-SWAP exchange, whose Bloch symbol has a single zero (`NO_GO_LEDGER:7-11`).
  - NG-LABEL: a C₃ orbit gives no canonical bijection to named generations (`:28`).
  - So **both decompositions in §6, and NF-1's twins, are conditional on a supplied kinetic law** (NG-KIN0).
- **Further notes read** (from `git ls-tree … | grep -i -E "generation|hw1|taste"`):
  - `THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:21-25`: 8 = 1+1+3+3; the species reading is an open bridge (narrowed 2026-10-02); rooting is undefined.
  - `EMERGENT_LORENTZ_INVARIANCE…TASTE_CENSUS…_2026-09-03.md:5`: census 8 = spin 2 × chirality 2 × flavor 2, N_f = 2. This is NF-1's decomposition.
  - `GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING…_2026-05-23.md:29-35`: full S₃ forces ≤ 2 distinct hw=1 masses; any proper subgroup lifts this.
  - `THE_TASTE_SINGLET_SECOND_MASS_IS_A_BODY_DIAGONAL_IMAGINARY_HOP…_2026-09-03.md:64`: the taste-singlet second mass is the body-diagonal hop. My ε-odd class-111 operator (§3a) is that object; count once.
  - `STAGGERED_TASTE_IS_THE_QUBIT…_2026-06-04.md:9`: the d = 3 taste matrices span M_2(C).
  - `TASTE_SECTOR_MARGINAL_LV_B4_PROTECTION_ON_OS0…_2026-06-13.md:5-6`: a single taste carries an O(0.2) velocity anisotropy that cancels only over the taste orbit. This is the same family of effect as §3d's first-order term, on a different surface (4D OS0, velocities); count once as precedent.
- **None of these computes a strain response of split twins.** As far as these files go, §3b–§3e is new.
- **Comparators (RECALLED):** Kogut–Susskind taste structure and taste-non-singlet multi-link masses; Adams-type staggered-Wilson splitting (grid-scale taste splitting reintroduces additive renormalisation); LHC vector-like-fermion limits around 1.3–1.6 TeV for quarks.

## 3. Results

### 3(a) The minimal splitting family (proved; checked, `S/tw2_alg.out`)

**Legality.** A k-independent 8×8 M times a symbol g is a local staggered operator iff the folding rule P_m g(k)M P_m = g(k + πm)M holds, where P_m is multiplication by (−1)^{m·x}. Checked: P₁₁₁ = Γ_ε (`:1`). The dictionary images of P_m are (Clifford monomial) ⊗ (n_l·τ), with three orthonormal taste vectors n₁, n₂, n₃ (`:3-10`).

**Mass family** ({M, Γ_j} = 0, [M, Γ_ε] = 0; dictionary β ⊗ M_2), solved by folding class (`:11-20`):
- the singlet β⊗1 is on-site (ε);
- **β⊗(n_l·τ) lives only in the two-bit classes**, symbol cos k_i cos k_j with {i, j, l} = {1, 2, 3}: a face-diagonal hop of range √2;
- no single-bit (nearest-neighbour) class carries a mass.

**ε-odd family** ({M, Γ_ε} = 0) (`:21-30`):
- the NN hop along l carries iβγ₅⊗(n_l·τ);
- the body diagonal carries the taste-singlet iβγ₅⊗1, which is main's "second mass", counted once.
- Twisted masses add in quadrature, |M_±|² = m² + (μ₀ ± μ₃)². Splitting therefore needs the singlet body-diagonal and the NN triplet together.

**Position space** (L = 8; `:31-37`). O₁₂ = cos k₁ cos k₂ M₁₁₀:
- is hermitian; its hops are (±1, ±1, 0) only;
- is same-sublattice;
- is invariant under translation by 2;
- **commutes with S₁ and S₂ and anticommutes with S₃**;
- commutes with ε and anticommutes with h.
- The spectrum of h + mε + σO₁₂ at the corners is exactly |m − σ| (×4) and |m + σ| (×4).

**Rotations** (staggered sign-field representation, L = 4, unique per rotation; `:39-43`):
- C4[001]: O₁₂ → +O₁₂, O₂₃ → O₃₁, O₃₁ → −O₂₃;
- C2[100]: (O₂₃, O₃₁, O₁₂) → (+, −, −);
- C2[110] and C3[111] permute them with signs;
- ε is invariant under all of them.

**So the triplet transforms as a vector (T₁) (checked). There is no cubic-invariant taste-split mass (proved: T₁ has no invariant vector).** Any splitting fixes a lattice direction:
- **σO₁₂ keeps D4[001]**, with C2[100] compensated by S₁S₃;
- **it keeps translations only on an index-2 sublattice**: S₁S₂, S₃Θ and S_j²;
- the body diagonal would keep D3.

This conflicts with the rule's covariance (`AX:57-58`) unless it comes from a covariant rule by spontaneous breaking (not constructed). Price **P-TW2a** (§8).

### 3(b) Exact block reduction and the structure of Σ (proved; checked)

- **Dictionary reduction:** U M₁₁₀ U† = β⊗(n₃·τ) (`S/tw2_alg.out:15`). The photon is taste-blind and the Psym vertices are linear in H at the cube corners. So Σ₈(P = 0) = U†[Σ₄(+)⊗P₊ + Σ₄(−)⊗P₋]U, where Σ₄(τ) is F1/F3's formula with M_τ(k) = m + τσ cos k₁ cos k₂ (proved).
- **Checked with the direct 8×8 evaluator** (`S/tw2_sigma8_N24.out:2-8`, `_N32.out`):
  - the folding of the strained split law holds to 5e-15;
  - the β⊗(n₃·τ) coefficient equals the two-block (Σ₊ − Σ₋)/2 to all 13 printed digits at t = 0 and ±0.1 (Eg and tet);
  - β⊗1 ≤ 3e-20;
  - every other of the 64 components ≤ 7e-18.
  - (At N = 24 the absolute value is far from converged, because the midpoint grid misses the IR log. This is a same-grid identity check only.)
- **At O(σ) only β⊗(n̂·τ) appears (proved):** each 4×4 block keeps P, T and C, so Σ₄(0) ∝ β. **There is no spin–taste (b-vector) term at P = 0.**
- **Σ₊(0, σ) = −Σ₋(0, σ)** (proved by γ₅ conjugation; checked "sum 0.0", `S/tw2_conv_T_*.out`).
- **The E_g response is exactly even** (the k₁↔k₂ symmetry of the block; checked difference 0.0, `S/tw2_conv_EV_168.out`).

### 3(c) The coefficients and the leak, converged (checked; `S/tw2_conv_{S,T,L}_{168,240,340}.out`)

| quantity (per e², SF units) | 168 | 240 | 340 nodes |
|---|---|---|---|
| A″ (singlet, = NF-1 z″), m = 0.005 | +1.13824e-2 | +1.13949e-2 | +1.13990e-2 |
| A′ (tet; cubic symmetry ⇒ 0) | 8.6e-10 | 8.6e-10 | 8.6e-10 (O(d⁴) remnant of the t³ term) |
| B″ Eg, σ = 0.005 | −1.124278e-1 | −1.124153e-1 | −1.124117e-1 |
| B″ tet, σ = 0.005 | −2.66491e-2 | −2.66366e-2 | −2.66329e-2 |
| **B′ tet** | **−4.541594e-2** | −4.541594e-2 | −4.541594e-2 |
| static A − B (light twin at t = 0) | +0.2304 | +0.2304 | +0.2304 |

**Leak of the light twin (checked directly on the light block, m = σ; `S/tw2_conv_L_240.out:2-7`, `_340.out`):**
- **Hessian, Eg:** **+0.12374 σ e²** (σ = 0.01 and 0.005 agree to 4e-4; 168/240/340 agree to 1e-6).
- **Hessian, tet:** **+0.03800 σ e²**.
- **First order, tet:** **+0.045410 σ e²** per unit t.
- **Static:** +0.2303 σ e².
- It is linear in σ: B″/σ drifts 5e-4 relative from σ = 0.0025 to 0.02 (O(σ) corrections). Adding m_l = 0.0005 adds exactly m_l A″ (`L_240.out:3`). This answers probe (b), "the Hessian against σ".

**Branches of the splitting symbol** (`S/tw2_conv_RV_240.out`; leak = singlet minus symbol):

| splitting symbol (class) | leak Hessian Eg | leak Hessian tet | **leak first order (tet)** | static |
|---|---|---|---|---|
| cos k₁cos k₂ (main, range √2) | +0.1238 | +0.0380 | **+0.0454** | +0.230 |
| cos k₁cos k₂ cos 2k₃ (range (1,1,2)) | +0.1047 | +0.0073 | **+0.0026** | +0.440 |
| cos k₁cos k₂·(cos 2k₁ + cos 2k₂)/2 | +0.1024 | +0.0307 | **+0.0548** | +0.361 |
| ε-odd: iβγ₅[μ₀c₁c₂c₃ ± μ₃c₃], μ₀ = μ₃ = σ | −0.1129 | −0.0166 | **−0.0504** | −0.183 |

- The ε-odd row uses a γ₅-frame rotation of each block: Σ(twisted) = VΣ(β-law)V† with V = exp(π/4 βΓ₅′) commuting with α_j (proved).
- The first-order zero is reachable with a local symbol: −0.062 c₁c₂ + 1.062 c₁c₂cos 2k₃ (one tuned number, P-TW2b).

### 3(d) Why there is a first-order term (proved by symmetry; checked)

- σO₁₂ keeps D4[001]. Under D4, E_g splits into B₁ (diag(1, −1, 0)) and A₁ (the tetragonal diag(−1, −1, 2)). So **a term linear in the A₁ strain is allowed**, and it is computed nonzero (B′ = −0.0454). The singlet stays cubic and its linear term vanishes.
- Body diagonal (`S/tw2_sigma8_N24.out` (iii), `_N32.out`, coarse grid):
  - the light/heavy mass magnitude is even under both E_g strains (|v(+t)| = |v(−t)| for Eg). D3 has no E_g invariant, so there is no linear E_g mass term.
  - The taste direction rotates linearly with E_g strain (odd part 6.4e-5 at t = ±0.1): a strain-induced e–μ mixing at first order (suggested).
  - D3 leaves the trigonal T₂g shear invariant. So for the body diagonal the first-order mass term moves to T₂g (allowed; not computed).
- **For every splitting direction n̂,** the stabilizer leaves the traceless strain n̂n̂ − ⅓ invariant, so a first-order coupling is symmetry-allowed in every case (proved). It is nonzero for the minimal axis family (checked).
- **The first-order coefficient is lift- and path-independent at one loop** (reading). F3's dressings and F4's path families start at O(t²) (`TESTS:9248,9309`), and UD fixes the O(t) law.
- **It is a-independent:** δ ln m_l = e²L′(σ/m_l)t. Unlike F1/F6 it carries no M_P.

### 3(e) Needed σ, sizes, rows (`S/tw2_sizes.out`; mapping conditional, as F1/NF-1)

**σ needed (c)** (PDG masses RECALLED; `:1-10`):

| pair | σ (GeV) | σa |
|---|---|---|
| (e, μ) | 0.0526 | 4.3e-21 |
| (u, c) | 0.634 | 5.2e-20 |
| (d, s) | 0.0444 | 3.6e-21 |
| (τ, τ′), m_τ′ = 1 TeV | 499 | 4.1e-17 |
| (t, t′), m_t′ = 1.5 TeV | 664 | 5.4e-17 |
| (b, b′), m_b′ = 1.5 TeV | 748 | 6.1e-17 |
| (ν_τ, ν′), m_ν′ = 50 GeV | 25 | 2.1e-18 |

The needed σ is **not** grid-scale for any pair with a TeV-scale partner.

**Nucleon leak weight.** W_N = Σ_q⟨q̄q⟩_N(±σ_q) = 15.9 GeV for m_VLq = 1.5 TeV (12.0 at 1 TeV, 27.5 at 3 TeV): b-dominated 11.3, u 4.2 (`:11-14`). NF-1's multiplicative weight is 0.275 GeV.

**Hessian leak against the rows (d)** (`:16-21`):
- Eg: μ_ρ = 1.24e-39 eV² m³/kg (massive sign) gives:
  - **Earth crossing ×8.3e-11**; detector ×1.2e-10;
  - PTA ×1.6e-16; Galaxy/IGM ×4.6e-21;
  - pulsar toy ×6.2e3 (not an observational bound, `vF2:9`).
- tet: ×2.5e-11 (Earth).
- Electrons: ×6.9e-14 (Earth).
- Hot era: m_g²/H² ≤ 0.84 (massive sign; "no observational bound for the massive sign", `rF2:104`, `vF2:13`).

**Clock row, Hessian part** (F6's estimator, `:29-30`):
- d ln(m_p/m_e)/dQ_E = −0.217, rate 1.7e-30 to 2.2e-29 /yr: **×4.6e-14 to ×6.2e-13**.

**Clock row, first-order part** (`:31-40`; the slope of one orthonormal traceless component under the same NANOGrav spectrum, t_tet = −h_E2/√2):
- d ln m_e/dt = +0.467 and d ln m_p/dt = +0.308 (1.5 TeV), so d ln(m_p/m_e)/dt = −0.159.
- Rate 1.7e-16 to 6.4e-16 /yr: **×4.7 to ×17.8 the clock row**.
- Electron side alone ×13.8; proton side alone ×9.1. Twin pairs split along different axes would not cancel.
- The two sides cancel in μ at m_VLq ≈ 2.6 TeV with a common axis (a tuning; other clock comparisons would separate them; not assessed).
- Range-(1,1,2) symbol: ×0.3 to ×1.0. Tuned mixture: 0.

**Possible further consequence (suggested, outside the pre-registered rows; not sized).**
- The same first-order coupling makes ordinary matter carry a lattice-anchored tetragonal strain "charge" of ∂E/∂t ≈ 0.29 GeV per nucleon (≈ 0.3 m_N) and ≈ 0.47 m_e per electron.
- If strain is the metric and that charge gravitates, this is a static anisotropic stress far beyond solar-system bounds.
- That depends on the static-field registration, which is open (panel F's static row S).

### 3(f) Third generation (e) (counting proved; sizes conditional)

**Count.** Each charge sector has 3 generations and tastes come in pairs, so the third needs a partner. That means a fourth family (vector-like in SM terms) plus ν_R, the T2 content of NF-1 (count once, `rNF1:218-229`).

**Sizes by partner mass:**
- **TeV partners:** Hessian safe. The first-order clock leak with the minimal symbol is b-dominated, ≈ ×6.5 at m_b′ = 1.5 TeV, and grows ∝ m_b′.
  - Passing needs m_b′ ≲ 0.23 TeV, against LHC ≳ 1.3–1.6 TeV (RECALLED). **There is no window for the minimal symbol** (conditional).
  - With the range-(1,1,2) symbol the window reaches about m_b′ ≲ 4 TeV.
- **Grid-scale partners** (Adams-type splitting, expectation's case; `:41-46`):
  - Earth row ×0.48 at m_b′a = 1e-6, ×48 at 1e-4, ×1.4e5 at 0.3;
  - clock Hessian ×5 at 1e-2;
  - first-order clock ×5e8 already at 1e-8;
  - the light third-generation member also needs a Planckian static retune (static leak 0.23 e²σ ≈ 1e-3 M_P), a P-R19-34a-type clause for that species.
- **Is an extra vector-like family needed?** Within the taste reading: **yes**, and its mass is squeezed from both sides. Under the Hamming reading: no, but see §6.

## 4. Against the FIXED readings (`TESTS:9641-9644`), literal first

| reading | status |
|---|---|
| **SPLIT-SAFE** ("the leak at the needed σ is below every row") | **Met for the pre-registered quantity** (the reopened additive-mass strain Hessian, `TESTS:9634,9637`), in every branch run (Eg/tet strains, four symbols, FB1 = FB2 at O(σ), both decompositions of the light/heavy assignment): Earth row ≤ 1.2e-10, clock row ≤ 6.2e-13. The pulsar toy forecast is exceeded (×6e3), but vF2:9 records it as not an observational bound. |
| **SPLIT-HAZARD** ("the leak exceeds a row (name it)") | **Met for the clock row if "the leak" includes the first-order term the same splitting reopens** (×4.7–17.8 for the minimal symbol, conditional). It is not met by the Hessian. It is met by grid-scale third-family partners (Earth row) under either part. |
| OPEN | Applies if the first-order term counts and every admissible splitting symbol must agree: the range-(1,1,2) symbol gives ×0.3–1.0. |

**Worker reading: SPLIT-SAFE (literal, Hessian).** The first-order clock-row exceedance in the minimal family is flagged for the referee as the decisive item. Counted, it gives SPLIT-HAZARD (clock row) for the minimal family and OPEN across symbols.

**Conditions:**
- the canonical TT-pole bridge (`PRICE_NOTE:22`) for the Earth rows;
- the |t| = |h_+| strain reading and the NANOGrav background's reality (3.5–4σ) for the clock rows;
- one loop;
- the coupling estimates (e² = 0.1 and C_F g_s² = 0.4 at the grid scale; a factor of about 2–3 matters for the ×5–18);
- ⟨q̄q⟩_N values (RECALLED);
- vector-like partner masses (placeholders).

## 5. Against the expectation (`TESTS:9645`)

- **"Reopens the channel ∝ σ": borne out** (checked, linear in σ to 5e-4).
- **"Splitting needed at grid-scale size": not borne out** for generation pairs: σa ≈ 4e-21–6e-17. It holds only for a grid-scale third-family twin, or under the Hamming-weight reading (§6).
- **"SPLIT-HAZARD": not on the Hessian** (safe by ≥ 1e10). It holds instead through a mechanism not anticipated: the splitting must pick a lattice direction, and that opens an a-independent first-order strain coupling that exceeds the clock row ×5–18 in the minimal family.

## 6. The coordinator's question: two decompositions of the same 8 corners

- **TW-2 assumes NF-1's decomposition:**
  - 8 = (4-component Dirac) ⊗ (2 tastes); the kinetic term acts as α_j⊗1 (`rNF1:81-84`; main's census N_f = 2, `EMERGENT_LORENTZ…:5`);
  - twins = the taste doublet; generations = taste-split pairs; splitting operators = β⊗(n̂·τ) (§3a).
- **Under the Hamming-weight decomposition** (main: hw=1 triplet = 3 generations; `THE_GENERATION_COUNT…:57-66,90-97`):
  - **The hw grading is the eigen-decomposition of the Wilson/K0 operator, not of the Dirac structure.** In the dictionary, M_W(k = 0) = diag(2 hw) = 3·1⊗1 − α₁⊗1 + (α₃β)⊗(n·τ) + (α₁α₂α₃)⊗(n′·τ) (checked, `S/tw2_sigma8_N24.out` (iv)). It does not anticommute with α₂, α₃ (commutator norms 2, 4) and does not commute with Γ_ε (norm 6).
  - So an hw=1 corner state is one spin–taste component of the two Dirac tastes, not a Dirac species. This is consistent with the lane's own withdrawal of the species reading (`CORRECTION_HISTORY:9`; `THREE_GENERATION_CHIRALITY_BOUNDARY:21-25`).
  - **The separating operator is λM_W, with λ a supplied O(0.1–2) coefficient**, so σ_hw = 2λ/a: grid-scale, which is exactly the TW-2 expectation's case. The leak scales with λ/a, not with a physical σ. That is F1's Wilson class (count once: F1's +2.42e-2 e² Hessian and ×1.6e8 Earth row, conditional; vF1 OPEN on lift freedom).
  - **Coarse check** (λ = 0.1, FB1 flow, Σ at ω = 0 projected on the corners, not on-shell; N = 24/32 unconverged at 10–20%, `S/tw2_sigma8_N24.out`, `_N32.out` (iv); suggested):
    - Σ is exactly diagonal in corners (≤ 8e-18).
    - The three hw=1 corners already differ at one loop at t = 0: (0.0143, 0.0084, 0.0079) e² at N = 32, with the (100) corner off by ≈ 0.006 e². The KS η phases single out axis 1, so the C₃ cycle is not a symmetry of K1 + λM_W at one loop. This is consistent with `THE_GENERATION_COUNT…:93-97`.
    - E_g strain splits the triplet linearly by ~6–7e-3 e² per unit t in grid units, i.e. Planckian × t.
  - So under the Hamming reading **no fourth family is needed (count 3), but the result changes from "small, ∝ σ" to "F1-sized or worse, ∝ λ/a, with Planck-strength first-order strain splitting of the generation levels"**. In FIXED terms that is SPLIT-HAZARD on any row F1's channel exceeds (suggested). The rows cannot be applied literally, because the lane supplies no physical mass identification for the hw levels.
- **What main already proves or excludes** (§2):
  - Proved (bounded): the corner multiplicities, the M_3(C) label algebra, the central K0 projector.
  - Excluded: a continuous isolation window and any physical-generation identification.
  - Not selected by the axioms: the staggered law itself (a1a2 no-go, unmerged).
  - Unresolved: Koide/generation chirality needs a C₃-breaking operator (two-gates note).
  - TW-2 adds: taste splitting is necessarily direction-picking (T₁), and its first-order strain coupling is nonzero.

## 7. Strong words

- **"Proved"** (short, unrefereed): the folding-class classification of §3a (given the dictionary); T₁ ⇒ no invariant splitting; the block reduction; P/T/C ⇒ Σ ∝ β⊗(n̂·τ) at O(σ); FB1 = FB2 at O(σ); the symmetry-allowed first-order term for every direction; the twisted-family γ₅-frame equivalence; the counting.
- **"Checked":** every number in §3, grids stated.
  - Converged: 168/240/340 panel nodes, Richardson in d.
  - The hw-lane numbers are coarse and unconverged.
- **"Every branch"** means those run: two E_g strains; four splitting symbols plus the twisted family; FB1/FB2 at O(σ); U = 1 and Psym (F3/F4 freedoms start at O(t²): the Hessian could move under them, the first-order term not).
- **Not claimed:** two loops; T₂g; Yukawa/Higgs channels (F6's Higgs channel is untouched by any of this); the static anisotropic-stress consequence; an on-shell hw computation; any spontaneous origin of the splitting; electroweak chirality.

## 8. Prices (named, not adopted; no axiom text changes)

- **P-TW2a (new): a lattice-direction-fixed taste-splitting operator** (face-diagonal, β⊗(n̂·τ)).
  - It breaks the rule's covariance under translations (to an index-2 sublattice) and proper cubic rotations (to D4 or D3), against `AX:57-58`. It is also beyond nearest-neighbour range; the root already uses smooth long-range symbols (reading).
  - Alternative: a covariant rule plus spontaneous direction choice (not constructed).
  - Needed by any twins-as-generations route (NF-1's P-NF1a with T2 content, count once).
- **P-TW2b (new; tuning): splitting-symbol shape tuned to cancel the first-order strain coupling.**
  - One number per pair-field per loop order (one-loop zero at −0.062 c₁c₂ + 1.062 c₁c₂cos 2k₃).
  - Needed to about 10% to pass the clock row in the minimal family.
  - Dominated by P-R19-34a′ / panel F's single primitive (count once with F6, `rF6:290-303`), which re-imposes the light twin's mass condition on every strained law and removes both orders by construction. That returns to the clause NF-1 hoped to replace by symmetry.
- **Content (count once with NF-1):** a fourth (vector-like) family + 3 ν_R. With the minimal symbol, m_b′ has no window between LHC and the first-order clock leak (conditional).

## 9. Files (`S/` = `scratchpad/C5/TW2/scripts/`)

- `tw2_alg.py/.out`: the folding classes, the mass and twisted families, the position-space operator, the shifts, the spectrum and the staggered rotations. It writes `tw2_mass_ops.npy` and needs `nf1_alg.py/.out` (rerun here to regenerate `nf1_gammas.npy` and `nf1_dict.npy`).
- `tw2_conv.py` → `tw2_conv_{S,T,L}_{168,240,340}.out` (singlet, split, light block), `tw2_conv_EV_168.out` (evenness), `tw2_conv_RV_240.out` (symbol branches); `run_conv.sh`.
- `tw2_sigma8.py` → `tw2_sigma8_N24.out`, `tw2_sigma8_N32.out` (8×8 folding, reduction, body diagonal, hw lane).
- `tw2_sizes.py/.out`: σ table, rows, clock (Hessian and first order), grid-scale third family.
- `*.time`: peak memory. `../prior/`: main's notes read.
