# C5 F5 report: the strain-covariant critical mass (P-R19-34a) tested as a rule

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 17:37Z to 18:42Z. No repository file was edited. Nothing was downloaded.
- **Memory:** OMP_NUM_THREADS=2; one heavy process at a time (sequential queues `S/queue*.sh`); peak resident set ≤ 0.7 GB per run (largest 0.68 GB) (`/usr/bin/time -l` records in `S/*.err`). One validation run was stopped and its grid reduced before it reached a memory-heavy step. No process of mine is still running.
- **Item:** `TESTS:9322-9379`. FIXED readings at `:9366-9375`; expectation at `:9376-9379`.
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`; `S/` = `scratchpad/C5/F5/scripts/`. `S/f1_lib.py`, `S/f3_*.py`, `S/f4_lib.py` are unmodified copies from `P/scripts/C5/{F1,F3,F4}`; `scratchpad/C5/F5/arch/` holds unmodified `dirac.py`, `sublum.py`, `dfam.py`, `zz.py` (from `P/scripts/C5/R18-5`) and `r1934_lib.py` (from `P/scripts/C5/R19-34`).
- **Labels.** proved (complete short argument, unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED = from memory.
- **Read.** `AX` in full; `TESTS:9146-9379` (the C5 follow-up: F1–F5 and the referee records); `rF1` in full + `vF1`; `rF2:93-106` + `vF2`; `rF3` and `rF4` in full; `rR19-34` + `vR19-34` in full; `rR19-24:1-120` + `vR19-24`; `rR19-31` + `vR19-31` in full; `rR19-35` in full; `rR18-9:1-140` + `P/scripts/C5/R18-9/jac_N160.out`; `rR19-21` (grep and `:18-60,195-240`) + `vR19-21`; `rR19-11` (grep, c₁); `PRICE_NOTE:1-40,590-682`; F1's, F3's and F4's scripts.

## 0. Plain words

**In one paragraph.** In this model space is a fine grid, and every matter particle sits on it with a built-in correction that is normally cancelled by hand, so the particles come out light. Earlier probes found that the cancellation works only when the grid is undistorted. Squeeze the grid and the particles get heavier or lighter, which inside the Earth would make gravitational waves too heavy to pass through it, contradicting what LIGO saw. The proposed fix is to re-apply the same cancellation whatever the squeeze. I tested that fix.
- It is a clean, unambiguous rule. It removes the problem in every version of the model built so far. It changes nothing we have measured; it actually restores the expected behaviour that a particle's mass doesn't depend on how space is squeezed.
- It does not finish the job, for two reasons:
  1. A larger effect of the same kind, coming through the Higgs field, is untouched by it and still needs a separate fix that is itself unproven.
  2. The fix nudges the empty-space properties that an earlier, finely tuned solution was balanced on. That knocks the solution off balance unless another separately proposed rule (which simply declares those empty-space properties non-gravitating) is also adopted.

**What the rule is.** The root puts every fermion on a Wilson-type lattice edge. The term that removes the lattice's extra fermion copies acts like a mass, so quantum corrections push every fermion's mass up by a Planck-sized amount. The root cancels this with a "critical mass" counterterm, set so that the fermions come out light, but set only for the unsheared grid. F1 showed that when the grid is sheared the correction changes and nothing re-sets the counterterm, so every fermion's rest mass depends on the shear. Inside ordinary matter that would give gravitational waves a mass large enough that GW170817 could not have crossed the Earth (F1, 1.6e8 over F2's bound). P-R19-34a says: re-set the counterterm on every uniformly sheared grid, by the same condition the root already uses on the unsheared one ("fermions stay light").

**What I found.**
1. **It is a well-defined rule.** At rest, the fermion's self-energy has only a mass part (space and time reversal and charge conjugation forbid the rest), so "stay light" is one equation per strain per fermion species, and it has exactly one solution near the free one. Under the campaign's convention for clauses it costs no numbers. Counted as conditions, it is one function of strain per fermion class, i.e. two numbers per class per loop order at second order in shear.
2. **It removes F1's effect in every version computed so far** (F1's branches, F3's dressings, F4's path families), because it refers only to each law's own fermion mass, not to how the law was built. It also makes F3's and F4's tuned zeros unnecessary.
3. **Its local form is ultralocal.** Its first corrections for a slowly varying shear are suppressed by (lattice spacing × wavenumber)², about 1e-81 for LIGO waves.
4. **What it leaves from the fermions themselves is tiny.** The part proportional to the fermion's own mass is about 1e-13 of F2's Earth bound; the magnetic-moment and photon pieces are smaller still.
5. **Two things remain.**
   - (a) **Higgs-sector channels** (R19-21): matter shifts the Higgs field, which shifts every fermion mass seen by the grid's vacuum, and the vacuum's shear resistance depends on those masses. A rule about fermion criticality does not touch this. It is far larger than F1's channel (|m_g| about 5 MeV inside the Earth, worker estimate; 1.4e-9 eV in intergalactic gas, referee-confirmed arithmetic). Only (S_loc) removes it, and (S_loc) is OPEN.
   - (b) **A knock-on on the vacuum.** The re-set counterterm also acts on the vacuum's own fermion condensate. That shifts the vacuum's shear row μ_E by almost exactly the Dirac sea's own μ_E times the coupling (ratio −0.99 per unit e²). That is enough to throw the tuned R18-9 root out of its range, unless (S\*) or (Σ) is adopted, which absorb it by definition.
6. **Nothing observed is removed.** At zero strain the law is unchanged, so every spectrum, mass and source at rest is unchanged. The rule restores what general relativity expects: a fermion's rest mass does not depend on shear. Without it, any static traceless lattice strain would give composition-dependent free fall many orders of magnitude above the MICROSCOPE limit.
7. **One gap.** The registered texts give no interacting photon law for an off-diagonal (T₂g) shear, and F1's construction does not extend to it (it becomes singular). So the T₂g part of the counterterm, and the knock-on on the μ_T2 row, are not computed for the registered law. One regular, unregistered stand-in gives a nonzero T₂g part, about a third of the E_g one. That stand-in also shows the size depends strongly on how the photon is strained near the zone edge.

**Reading (worker): RULE-PARTIAL.** It covers the F1 channel in every variant and is well defined, local and number-free under the clause convention. But a residual channel exceeds F2's bounds (the Higgs-sector channels of item (iv)), and the knock-on moves the root. With (S_loc) and (S\*) or (Σ) also granted, every clause of RULE-WORKS is met, conditionally on those named, unadopted completions.

## 1. The reading against the FIXED readings (`TESTS:9366-9375`), literal first

| reading | clause | status |
|---|---|---|
| **RULE-WORKS** | one number-free clause that uniquely fixes m_c(h) | **met** under the law-functional convention (`vR19-24:11`, `vR19-34:21`): one clause; m_c(h) unique by the implicit function theorem (§3.1). Under the codimension convention it is not number-free (a function of h per class; 2 per class per order at O(h²), traceless) |
| | covers the channel in every variant | **met** (proved by construction, §3.1(a5)), for every F1/F3/F4 variant, at all orders, for uniform strain |
| | every residual below F2's Earth row and the hot-era rows | **not met.** (i)–(iii) pass by ≥ 1e10 (§3.2). **(iv) fails:** R19-21's Higgs-sector channels (vev shift × the vacuum's mass slope c₁; Higgs mass² × ⟨φ†φ⟩) survive the rule and exceed F2's Earth row by ~5e21 (even part) to ~3e38 (Wilson c₁) in μ_ρ, and the hot-era tachyonic row (count once with R19-21) |
| | the knock-on absorbed or zero | **not met on the bare law**: Δμ_E = −e_m·m_c″ ≠ 0 (checked: +1.689e-2 per Dirac field per unit e²), which the root's linear retune cannot absorb inside its knob ranges (suggested). **Met under (S\*) or (Σ)** (absorbed by definition) |
| | nothing observed changed | **met** (proved for every h = 0 quantity; suggested/comparator for EP and LLI, §3.4) |
| **RULE-PARTIAL** | covers the F1 channel, but a residual exceeds a bound or the knock-on moves the root | **met. Both:** residual (iv) exceeds; the knock-on moves the root (bare law) |
| RULE-FAILS | ill defined, non-local beyond O(a·∂h), or changes observed physics | not met: well defined (§3.1), ultralocal with O((aq)²) corrections, nothing observed changed |
| OPEN | otherwise | not needed. The T₂g coefficient is uncomputable on the registered texts (§3.1(d)); that is a law gap, not a gap in the rule (branch MF: γ′ ≠ 0) |

**Worker reading: RULE-PARTIAL**, naming (1) residual (iv), R19-21's Higgs-sector channels, which no fermion-criticality clause can reach, and (2) the knock-on onto the vacuum rows, which moves the R18-9 root unless (S\*)/(Σ). Conditional: with (S_loc) [P182, OPEN] and (S\*) [P177] or (Σ) [P179] granted, all five RULE-WORKS clauses are met. Number-freedom then holds in the law-functional convention only, and the hot-era residual is R19-31's O(g²T⁴) speed-row term, ≈ 2e-3–4e-2 H², which needs P-R19-31c for its fermion part.

## 2. Class, hypotheses and what was computed (stated before titles)

- **Arena (F1's, `rF1:99-105`).** Z³ × ℝ, one loop, U(1) (non-abelian only through C_F), Euclidean, external P = 0, Feynman gauge, per e². SF strain flow in SF units t (v = (t/2)h·p, Φ_t its time-1 map); E_g unit strain h = diag(1, −1, 0). R18-9 root D1(0.909103708, 0.555604226) with Gph(2.9435); 0⁺ root D1(0.915438682, 0.568280847). Main branch B1 (Dirac flow at the rows' m = 0.01; Psym links).
- **The rule as tested (`TESTS:9335-9337`).** On the uniformly strained law L_h, the bare mass of each Dirac species is m₀(h) = m_c(h) + m, where m_c(h) is defined by "the pole mass at m = 0 vanishes", at every uniform strain h (traceless and trace), at every loop order. At one loop m_c(h) = −e_s²·δm(h), with δm(h) = the β part of Σ(P = 0) on L_h at critical propagator mass.
- **New code.** `S/f5_lib.py` generalizes F1's law and mass formula to an arbitrary uniform symmetric h (3D Dirac and photon flows, all eight Psym box corners flowed). On F1's E_g it reproduces F1's unmodified library to ≤ 7e-18 at t = 0, 0.003, 0.006 (`S/f5_validate.out:1-4`), and on the half zone (`:5-7`). Diagonal strains are regular in this class; the off-diagonal (T₂g) case is singular (§3.1(d)).
- **Mapping for sizes.** F1's (`P/scripts/C5/F1/f1_sizes.py:1-6`; canonical TT-pole reading conditional, `PRICE_NOTE:22`; SM mapping an ESTIMATE): each residual is sized as a ratio R to F1's channel in the same matter, μ_ρ = R × 2.424e-21 eV² m³/kg (`P/scripts/C5/F1/f1_envscale.out:1`). F1's history numbers are reproduced by `S/f5_sizes.py` (`S/f5_sizes.out:18-21`).
- **Not computed:** two loops; non-abelian vertices beyond C_F; Yukawa/W/Z loops (argued, §3.2(iv)); the registered law's T₂g Hessian (§3.1(d); one unregistered regular branch, MF, is sized); on-shell (vs Euclidean P = 0) multiplicative slope; the A₁ (trace) bridge to the metric; a nonlinear retune of the R18-9 root.

## 3. Results

### 3.1 (a) Definition

**(a1) The clause.** "On every uniformly strained law, each Dirac species' bare mass is re-set so that its pole mass at zero bare physical mass vanishes, at every order" (the h = 0 criticality condition, extended to all uniform strains).

**(a2) One scalar condition per strain and species (proved, short).**
- The root's H(k) is invariant under P (β·, k → −k), T (antiunitary, k → −k) and C (`rF3:107-115`, checked there to ≤ 7e-16). The SF flow is odd and real (p = ∇(E²/2) is odd), so Φ_t commutes with k → −k and with complex conjugation, and L_h keeps P, T and C for every uniform h. Psym, F3's symmetric dressings and F4's reversal-symmetric families keep them too (`rF3:107-115`; `rF4:39-42`).
- At P = 0, the 16 Dirac structures split as: α_j, γ₅, βγ₅ (P-odd); Σ_j, βΣ_j (T-odd); 1 in the Hamiltonian form (C-odd at zero density). Only β survives.
- So Σ(P = 0) = δm(h)·β for **every** uniform strain, including strains whose principal axes are not lattice axes (no rotation is needed). "Fermions stay light" is exactly one real equation per species per strain.

**(a3) Uniqueness (proved: implicit function theorem; slope checked).** The pole mass is m_pole(m₀, h) = m₀ + e²Σ(h; m₀) + O(e⁴), with ∂m_pole/∂m₀ = 1 + e²z(m). Checked on B1 (`S/f5_mult_240.out:7-10`; 156 nodes agree to 1e-4): z = +0.396, +0.361, +0.325, +0.290 at m = 0.0025, 0.005, 0.01, 0.02, i.e. positive and growing only logarithmically as m → 0 (the IR log). So ∂m_pole/∂m₀ > 1 > 0, m_pole is strictly increasing in m₀, and the zero m_c(h) exists and is unique in the perturbative neighbourhood, at every h where δm(h) is defined.

**(a4) m_c(h) at one loop (checked; per e², SF units).** By cubic symmetry with inversion, the O(h²) part of δm on symmetric h has three invariants: δm = δm₀ + α tr h + β (tr h)² + γ Σ_i h_ii² + γ′ Σ_{i≠j} h_ij² (the flow is quadratic in h at O(t²), so the second derivative is a quadratic form in h).

| strain direction (B1, R18-9 root, 156 nodes) | d_t δm | d²_t δm | source |
|---|---|---|---|
| E_g, diag(1, −1, 0) | +1.9e-16 (even) | **+2.4238554e-2** (F1's value at this grid; converged F1 value +2.42401e-2) | `S/f5_nn_156.out:4`; `rF1:200` |
| nn = e_z e_z (rank one along an axis; R19-35's n is [110], §3.3) | **−1.6251820e-2** | **+1.8487429e-2** | `S/f5_nn_156.out:2` |
| isotropic, 1 | **−4.8755459e-2** | **+9.3671199e-2** | `S/f5_nn_156.out:3` |
| T₂g, e_x e_y + e_y e_x | — | **not computable in F1's class** (§3.1(d)) | `S/f5_t2g_diag.out` |

- **Cubic consistency (checked).** From E_g, γ = 6.0596e-3; from nn, β = 3.1841e-3; then iso predicts 18β + 6γ = 9.3671e-2 against +9.3671199e-2 computed, and 3 × (−1.6251820e-2) = −4.8755460e-2 against −4.8755459e-2. This checks the general-h code on non-E_g strains.
- **The one-loop critical mass, explicitly** (per species, SF units, R18-9 root, B1):

  m_c(h) = m_c(0) − e_s²[α tr h + β (tr h)² + γ Σ_i h_ii² + γ′ Σ_{i≠j} h_ij²] + O(h³),

  with **α = −1.6252e-2, β = +3.1841e-3, γ = +6.0596e-3** (156 nodes; E_g's converged 4γ = 2.42401e-2 moves γ by 6e-5 relative), and γ′ not computable (§3.1(d)). The linear trace term is nonzero: on the h = 0-fixed law the pole mass moves at first order under trace strain (§3.4). The rule fixes all of these by the one clause.

**(a5) Coverage in every variant (proved by construction; numbers cited).** The clause refers only to the pole mass of whatever law is in force. For each variant the counterterm's E_g curvature is minus that variant's own Hessian, so the corrected δm(h) ≡ δm(0) identically, at all orders in h, for uniform strain:

| variant | additive Hessian the counterterm carries (e², SF) | source |
|---|---|---|
| F1 B1 / B2 / 0⁺ root | +2.42401e-2 / +2.42611e-2 / +2.45350e-2 | `rF1:200-205` |
| F3 dressing V_t = exp(i t² a G) | Hess_F1 + 2a·L[G], with L[G₁] = −0.8586, L[G₂] = −1.5021; any real a | `rF3:31-35,41-44` |
| F4 families J / S_M / SL / signed mixtures | +2.43289e-2 / +2.495e-2 … +2.590e-2 / ≈ +2.591e-2 / H_P + Lλ + Qλ² | `rF4:21-26,129-136` |

- The counterterm's value differs from variant to variant; the clause does not. No variant needs a separate number or tuning.
- **Consequence (proved).** P-F3a (a* to 6e-9) and P-F4a (λ* to 6e-9) become unnecessary under the rule: the dressing coefficient a and the path family are then free O(t²) law data with no additive-mass consequence (count once with `rF3:237`, `rF4:149,180`).

**(a6) Numbers under both conventions (reading).**
- **Law-functional convention** (`vR19-24:11`, item 4; `vR19-34:21`, item 6): **0 numbers, 1 clause.** It "imposes rather than predicts" (`vR19-34:21`), like D1∞ (P188) and (S\*) (P177).
- **Codimension convention** (`rR16-2:231` and `TESTS:5470` as quoted at `rR19-24:43-44`; P73 = P188 under a codimension count, `PRICE_NOTE:621`): one function m_c(h) per fermion class per loop order. Truncated at O(h²) that is **2 per class per order in the traceless sector** (E_g γ and T₂g γ′), or **4 with the trace** (α, β, γ, γ′). This is on top of the existing h = 0 critical tuning (one per class, already on the root's bill). With 4 classes (u-type, d-type, charged lepton, neutrino) that is 8 (16) per order; per species more.

**(a7) The local version (proved: locality and parity; suggested: size).**
- For a slowly varying graviton field h(x), the local counterterm is ψ̄(x)[m_c(h(x)) − m_c(0)]ψ(x): ultralocal (one site), number-free, fixed entirely by the uniform clause.
- **The first gradient correction is O(a²∂²h), not O(a∂h), in the mass channel (proved).** A term ψ̄ψ × (one derivative of h) needs a scalar built from ∂_k h_ij, a rank-3 tensor; under inversion it is odd, and ψ̄ψ is even. Bilinears that inversion does allow at O(∂h) (vector or tensor ones, e.g. ψ̄γ^iψ ∂_j h_ij, which is further T-odd for a static strain) are not mass terms. They belong to the O(e²) stress vertex, are constrained by W1, and the rule does not touch them.
- **Size (suggested).** The uniform clause fixes the ψ̄ψhh contact at zero graviton momentum q; the one-loop self-energy varies at relative O((aq)²). For a 100 Hz wave, aq ≈ ℓ_P·2πf/c ≈ 3.4e-41, so the unfixed remainder is ~1e-81 of F1's channel. The matter fermions' own momenta enter separately, as the speed rows ((i′) in §3.2).

**(a8) What the rule is, structurally (reading).** SF leaves every free band's k = 0 energy unchanged (Φ_t(0) = 0), so the free rest mass is strain-independent for every h, trace included. One loop breaks this through the Wilson additive mass. The rule restores, at every order, exactly the property the registered strain law already has for free bands.

**(d) The T₂g coefficient: not computable on the registered texts (proved; checked).**
- F1's photon is "Maxwell in frame components with flowed symbols d_{t,j}(q) = d([Φ^γ_t q]_j)" (`rF1:120`), which is regular for diagonal h because then [Φ^γ_t q]_j depends on q_j alone and vanishes only at q_j = 0.
- For h = e_x e_y + e_y e_x the photon flow moves q_y by (t/2)p^γ(q_x), so d_{t,y}(q) vanishes on the surface q_y* ≈ −(t/2)p^γ(q_x) ≠ 0. There the link difference L_y = D_t(B + q_y e_y) − D_t(B) does not vanish. The generalized-link vertex V_y = L_y/d_{t,y} then diverges like 1/(q_y − q_y*), and |V_y|² is not integrable across the surface.
- **Checked** (`S/f5_t2g_diag.out`):
  - At (q_x, q_z) = (1.3, 0.7) and t = 0.003, d_{t,y} vanishes at q_y* = −1.950e-3, which equals −(t/2)p^γ(q_x) to four digits. There |L_y^c| ≈ 1.9e-3 ≠ 0.
  - |L_y^c|²/d²_{t,y} = 3.4e2 and 3.8e4 at |q_y − q_y*| = 1e-4 and 1e-5 (∝ 1/ε²). The E_g control gives exactly 1.000 at every ε.
  - The T₂g quadrature of δm at t = 0.003 does not converge: +0.550 (80 nodes/half-axis), +0.0632 (110), +1.345 (156), against E_g's +0.0418585 at the same t and grids. (`S/f5_validate.out:9-10` shows the integrand is nonetheless even in t and the domain reduction is right.)
- So the T₂g interacting law needs a construction no registered text supplies: a frame map E(q) with E(q)·d(q) = D̃(q) that keeps the link denominators vanishing only at q_j = 0, with its own branch choices. This is a law gap (like F1's item 4-5 freedoms), not a defect of the rule: the clause is defined on whatever T₂g law is registered. **γ′ of the registered law, and therefore the registered T₂g knock-on on μ_T2, are not computed.**
- **A sizing branch, MF (NOT registered; checked as a computation, its law-status is a stated choice; `S/f5_mf.py`).**
  - **Construction.** A constant vielbein E = exp((t/2)h) acts on link fields that keep the unstrained odd lattice symbols. So the link denominators vanish only at q_j = 0 (regular for every h), the propagator is exp(−th)_jl/(Q₀² + d·exp(th)·d), and the Psym seagull acquires off-diagonal entries. Their closed form is derived in the script docstring.
  - **Checks.** The two-photon longitudinal Ward identity Σ_jl d_j d_l T^M_jl = M_t(q) holds to 2-3e-16, and the one-photon Ward to 4e-16, for E_g, T₂g and nn[110] at t = 0.3 (`S/f5_mf_ward.out:1-3`). At t = 0, MF equals F1's law to all digits.
  - **What MF changes.** In the photon's linear region MF equals the SF photon. It differs only near the photon box edge (|q_j| > 2.9435), where MF stretches the symbol and the SF frame photon does not. So MF is **not** SF-consistent for the photon's free band at the edge.
  - **Results** (156 nodes; Richardson d/2d agree to 1e-9; dm(t) = dm(−t) exactly):
    - **E_g: +8.6215e-3**, against the registered SF law's +2.4239e-2 on the same grid (`S/f5_mf_Eg156.out:3`). A factor 2.8 smaller, same sign.
    - **T₂g: +2.6962e-3** (`S/f5_mf_T2g156.out:3`); +2.6963e-3 on 240 nodes (`S/f5_mf_T2g240.out:3`), converged to 4e-5. So in MF, γ′ = 6.74e-4 and γ = 2.155e-3, with **γ′/γ = 0.31**.
  - **Reading.**
    - The additive Hessian is dominated by the zone-edge region, where the Wilson term lives: the photon's zone-edge strain prescription alone moves the E_g value by ×2.8. So a branch value of γ′ indicates order of magnitude only. Scaled by the E_g ratio, γ′ ~ 2e-3 (Hess_T2g ~ 8e-3). Both are positive.
    - The one regular realization computed is anisotropic (γ′ ≠ γ) and has a nonzero T₂g response.
    - Side observation for F1's referee: this is one more law freedom, the photon zone-edge strain, that moves the unruled Hessian at O(1) without changing its sign. The rule covers it.

### 3.2 (b) Residual channels after the rule

All sizes use F1's mapping (§2) and are read against F2's rows (`rF2:95-106`): Earth crossing ≤ 1.5e-29 eV² m³/kg (row 1, checked 1D model; positive-mass sign confirmed, `vF2` item 2); Galaxy+IGM ≤ 2.7e-19 (row 5); hot era tachyonic ≲ 4e3–8e3 H² per e-fold (row 9, history dependent, `vF2` item 5); hot era massive: no bound within the adiabatic tensor-only model (row 10, `vF2` item 6).

| channel | coefficient | Earth: R and μ_ρ | Earth row 1 | hot era | covered by | label |
|---|---|---|---|---|---|---|
| **F1 (reference)** | Hess_t +2.424e-2 e² | R = 1; 2.4e-21 | ×1.6e8 | m_g²/H² +4.9e13 (150 GeV) … +1.2e16 (1 GeV) | **the rule (exactly)** | `rF1:255-281` |
| **(i) multiplicative**, m_f z″ ⟨ψ̄ψ⟩ | z″_t = **−4.6e-3 e²** (SF, Euclidean P = 0; −4.587e-3, −4.605e-3, −4.681e-3 at m = 0.0025, 0.005, 0.01 on 240 nodes; 156 nodes within 1%) | nucleons R = 3.3e-22 (Σ_q m_q⟨q̄q⟩_N ≈ 0.275 GeV, RECALLED σ-terms and heavy-quark trace-anomaly weights); μ_ρ = 8.0e-43 | **×5.3e-14 (passes)** | −1.3e-4 to −3.5e-4 H² (tachyonic sign; passes row 9 and \|m_g\| < H) | not covered; below bounds | checked coefficient; sizes estimate (`S/f5_mult_240.out:7-10`; `S/f5_sizes.out:4-5,18-21`) |
| (i′) matter speed rows (strain dependence of the fermions' O(p²) kinetic term; P = 0 criticality does not fix it) | κ″ not computed; bracket 0.01–1 e² | R = 8e-22 – 8e-20; μ_ρ ≤ 1.9e-40 | ≤ ×1.3e-11 (passes) | R19-31's O(g²T⁴) residue: \|m_g²\|/H² ≈ 2e-3 (computed Higgs part) to ≈ 4e-2 (fermion bracket), count once (`rR19-31:176-186`; `vR19-31` item 4) | P-R19-31c (D1∞ at every strain), not this rule | suggested |
| **(ii) Pauli/clover term** from F3's dressing | δa ≈ 4a t²(mℓ_P) (`rF3:52,205`) | R ≤ 3e-56 (\|a\| ≤ 1, fully polarized electrons in 50 μT) | passes | negligible | not needed. The rule absorbs the dressing's additive part for every a | suggested (`S/f5_sizes.out:9-10`) |
| **(iii) photon** | no mass at any strain: the generalized-link law obeys Ward at every t (`rF1:30,177,185-190`; R19-31 Lemma W, `rR19-31:107-113`); the in-medium ω_p² = e²n_e/m_e moves only through (i) | O(k²) photon strain response × nuclear Coulomb energy (~2.2 MeV/nucleon): R ≈ 1.4e-24 – 1.4e-22 | passes | Debye/HTL: no g²T² cross term (`vR19-31` item 2, abelian) | Ward (law) | proved (mass zero); suggested (sizes) |
| (iv-a) Yukawa-loop additive mass of fermions | part of the total pole mass | — | — | — | **the rule** (its condition is on the total pole mass, any loop) | proved |
| **(iv-b) Higgs vev shift × the vacuum's mass slope c₁** (Wilson edges): matter shifts v, so every fermion mass the lattice sea sees shifts, and ∂μ_vac/∂m = c₁ ≠ 0 | c₁ (μ_E) +1.069e-2 per field (0⁺ root, `r1921_history.py:4`). Checked here on the R18-9 root: dμ_E/dm = +1.048e-2 (m from 0 to 0.005) and +1.057e-2 at m = 0.01 per field (`S/f5_c1.out:1-2`), R19-11's slope to 2%. Independent arithmetic with it (f_N = 0.3, v = 246 GeV, m_H = 125 GeV, RECALLED; Σn m a = 4.395e-17, `r1921_history.py:27`) gives Earth δv/v ≈ −7.5e-27 and \|m_g\| ≈ 5e6 eV, tachyonic sign | IGM \|m_g\| = 1.42e-9 eV (`vR19-21:25`, arithmetic confirmed); Earth ≈ 5 MeV (`rR19-21:211`, suggested); μ_ρ ≈ 4.5e9 | **×3e38 (fails)**; Galaxy/IGM row ×1.8e28 | (V) (vev shift, odd and even parts): \|m_g\|/H ≫ 1 from 1 MeV to ~1e15 GeV, with tachyonic windows; 1.5e24 at T_c (`rR19-21:22-34`) | **not by the rule**; only (S_loc) (P182, OPEN) or twisted edges (P-R19-11c, leaves (iv-c)) | count once with R19-21 |
| **(iv-c) Higgs mass² strain response × ⟨φ†φ⟩** (= the vacuum's even mass slope, by R19-31's Lemma C) | R₂ / c₂ (`rR19-21:205`; `rR19-31:115-118`) | Earth ≈ 0.02 eV (`rR19-21:211`, suggested); μ_ρ ≈ 7e-8 | **×5e21 (fails)** | (F) (thermal ⟨\|φ\|²⟩ × R₂): \|m_g\| ≫ H, T² scaling, sign flip at 563 GeV (`rR19-21:28-34`; `vR19-21` item 3) | **not by the rule**; (S_loc) in background-field form (P182 + P-R19-31a) | count once with R19-21 / R19-31 |

- **Why (iv-b) and (iv-c) are out of the rule's reach (proved).** The rule changes the bare mass's strain dependence m_c(h). These channels are the vacuum's dependence on the actual masses, ∂_m μ_vac = ∂²_t e_m (and its scalar analogue), multiplied by a physical, matter-induced mass shift. Neither factor contains m_c(h).
- **Structure (reading).** On Wilson edges there are three ψ̄ψ-type cross terms between the state and chiral breaking:
  1. ⟨ψ̄ψ⟩_matter × e²δm″: F1's channel, removed by the rule;
  2. ⟨ψ̄ψ⟩_vac × m_c″: the knock-on of §3.3, absorbed only by (S\*)/(Σ);
  3. δm_f(matter) × ∂²_t⟨ψ̄ψ⟩_vac: R19-21's channel, removed only by (S_loc).
  The rule trades (1) for (2) and leaves (3).

### 3.3 (c) Knock-on onto the vacuum rows at the R18-9 root

- **Formula (proved).** With m₀(h) = m_c(h) + m and e(h, m) the vacuum's lowest-state energy per Dirac field (H4 units: e = −2⟨E∘Φ_h⟩, `rR19-35:19`), d²_t e(t, m + Δm_c(t))|₀ = e_tt + 2e_tm·Δm_c′ + e_m·Δm_c″. The rule adds Δm_c(t) = −e_s²[δm(t) − δm(0)].
- **Inputs (checked; `S/f5_nn_156.out`).**
  - e_m = ∂e/∂m = −2⟨M/E⟩ = **−0.69693438** per field at m = 0.01 (finite difference and direct agree to all digits, `S/f5_nn_156.out:5`; R19-21 had −0.6923 at m = 0 on the 0⁺ root, `rR19-21:50`).
  - e_tm = ∂_t∂_m e = **+3.519457e-2** per field along e_z e_z and +1.055848e-1 along h = 1. That is 3 times the e_z e_z value, as cubic symmetry requires: a linear functional of h sees only tr h (`S/f5_nn_156.out:6`). e_t along e_z e_z (the one-point slope) is −0.3042 per field (`:8`).
  - **Row checks.**
    - e_tt along E_g = −1.71003e-2 against the registered −1.709412e-2 per field (3.6e-4 relative; finite-difference step 0.01, 156 nodes) (`S/f5_nn_156.out:7`).
    - R19-35's λ_nn uses n = (1,1,0)/√2 (`rR19-29:63`), not a lattice axis. On my grid the rank-one form −(w/12)⟨u⁴/E³⟩ gives **+2.16444e-2 for n = [110]**, against R19-35's +2.164325e-2, and +1.73710e-2 for n = z. My finite-difference SF Hessian along e_z e_z reproduces the latter (+1.73667e-2) (`S/f5_nncheck2.out:1-2`; `S/f5_nncheck.out`). Units are therefore pinned to R19-35's.
- **μ_E (E_g, traceless; e_tm·Δm_c′ = 0 by evenness).** Δμ_E per Dirac field = −e_m·e_s²·Hess_t = **+1.6894e-2 e_s²** (with F1's converged +2.42401e-2). Against the free Dirac row −1.70941e-2 per field (`rR19-35:34`), the ratio is **−0.988 per unit e²**. I have no derivation of this near-equality (suggested coincidence, cf. R19-34's unexplained ratio ≈ −0.97, `rR19-34:104`).
- **Size at the root (estimate).** Σ_fields e_s² ≈ 7.65 with F1's mapping (18 quark fields × C_F g_s² = 0.4, 4.5 lepton fields × 0.1; up to ~10 with electroweak loops). So Δμ_E,total ≈ +0.13. The root's own budget is: Dirac −0.3846, photons +0.3421, scalars +0.0425 (`rR19-35:35`); the root holds it at ≤ 7e-11 (`rR18-9:31-40`).
- **Does it move the root? Yes, on the bare law (suggested, linear).** The root's μ_E knob response (`P/scripts/C5/R18-9/jac_N160.out:7-11`, third column of J⁻¹) is (b_s, b_f, r, a) = (40.26, 0.543, 0.283, −0.0031) per unit residual. A residual of 0.13 asks for Δb_s ≈ 5.2 rad, outside b_s ∈ (0, π). Even a coupling sum of 1 (Δμ_E = 0.017) asks for Δb_s ≈ 0.68. The retune leaves the linear neighbourhood and plausibly the scalar family. A nonlinear retune was not attempted.
- **Scope of "moves the root" (reading).** The root's rows are zeroed at O(e⁰) (free matter loops). Every O(e²) vacuum correction moves them, including the uncomputed two-loop vacuum bubble with its h = 0 counterterm insertion, E₂″ − δm(0)∂²_t e_m. So the root is re-set order by order in any case (codimension convention). The rule's piece is one definite O(e²) term, and it is large: about 99% of the free Dirac row per unit e². Whether the total O(e²) correction is large is not known here.
- **μ_T2.** The knock-on is −e_m·e_s²·Hess_T2g with Hess_T2g = 4γ′ (unit T₂g strain; E_g's is 4γ = 2.424e-2), so it needs γ′. Not computable on the registered texts (§3.1(d)). It is nonzero unless γ′ = 0, which no symmetry forces (cubic symmetry allows γ′ ≠ γ).
  - **Branch MF (sizing only).** Δμ_T2 = +1.88e-3 e_s² per field, ≈ +0.014 in total (Σe_s² ≈ 7.65; about 3 times more if scaled by the E_g ratio).
  - The root's μ_T2 knob response (fourth column of J⁻¹, `jac_N160.out:8-11`) is (480.7, 49.1, 41.5, −0.42) per unit residual. A residual of 0.014 asks for Δb_s ≈ 6.9, Δb_f ≈ 0.71 and Δr ≈ 0.60, far outside the knob ranges (r ≤ 1/√3). So μ_T2 also moves the root on the bare law (suggested, linear, branch value).
- **λ_nn and the one-point function (h = nn carries trace).**
  - For R19-35's n = (1,1,0)/√2, h = nn has tr h = 1, Σh_ii² = ½ and Σ_{i≠j}h_ij² = ½. So d²_t δm = 2β + γ + γ′ and d_t δm = α (a linear functional sees only the trace).
  - Δλ_nn per field = −e_s²[e_m(2β + γ + γ′) + 2e_tm·α] = **e_s²(+9.81e-3 + 0.697γ′)**. For n along a lattice axis (fully computed, no γ′) it is +1.4028e-2 e_s².
  - With Σe_s² ≈ 7.65, Δλ_nn ≈ +0.075 + 5.3γ′ (≈ +0.107 if γ′ = γ), against the bare λ_nn = −0.1246 (completion A, `rR19-35:54`). So the knock-on is as large as λ_nn itself and can move it through zero (at γ′ ≈ 9e-3 for Σe_s² = 7.65). Branch MF's γ′ = 6.7e-4 would give ≈ +0.079 (this mixes the registered α, β, γ with a branch γ′). That would switch R19-29's face1 branch, since FACE1-HOLDS needs λ_nn ≠ 0 (`rR19-35:13`). λ_nn is completion-dependent at O(7) anyway (P-R19-35a).
  - **One-point function:** Δτ = e_m·Δm_c′ = **−1.133e-2 e_s²** per field per unit tr h (≈ −0.087 in total), against R19-35's τ = −0.611 (`rR19-35:55`). The one-point counterterms (P-Tad, (S)) must be re-set to absorb it.
- **Absorbed by (S\*)/(Σ)? Yes, by definition (proved).** The counterterm is part of the law on L_h, so the lowest state's energy at uniform strain h contains Δm_c(h)·∂_m e. (S\*) (P177) subtracts the lowest state's whole uniform-static response, i.e. the full degree-0 kernel (`rR19-35:68`). (Σ) (P179) implies (S\*) and also removes the degree-2 kernel (`rR19-35:69`). So under either, μ_E, μ_T2 and λ_nn are zero by construction and the knock-on has no effect.
- **The cone rows Ξ_Eg and Ξ_T2g are unchanged at O(e²) (proved).** For traceless h the counterterm has no linear term (Δm_c′ = 0 by C₂/C₄ evenness), so it enters only as a q-independent ψ̄ψhh contact: a degree-0 kernel. In the trace sector the linear vertex (−e_s²α h_ii ψ̄ψ) does enter q-dependent bubbles at O(e²); those are A₁ rows (face1/h_nn), not computed.

### 3.4 (d) Observed physics

- **Everything at h = 0 is unchanged (proved).** m_c(0) is the existing critical mass, so the unstrained law, its spectrum, every pole mass, T⁰⁰ and all h = 0 rows are identical. For traceless h, Δm_c = O(h²), so the linear source T^{ij} at h = 0 is also unchanged. Only the matter's response to strain changes, and that response is F1's channel itself.
- **What the rule removes is not observed; it restores GR behaviour (comparator; suggested sizes).** In GR a traceless spatial strain does not change a scalar rest mass. Without the rule the root's law has a species-dependent rest-mass–shear coupling ½e_s²Hess_t t²/a per particle (`rF1:83,290`; 0.0121 e²/a per unit t²).
  - Per nucleon (13 × 0.4 coupling weight) that is δm/m ≈ 8e17 t². Per electron (e² = 0.1) it is ≈ 3e19 t².
  - **EP (MICROSCOPE, Ti/Pt, |η| ≲ 1e-14, RECALLED and rounded).** Composition enters through Z/A (electrons) and isospin/binding (nucleons): Δ(δm/m) ~ 1e15–1e16 t².
  - If the lattice frame near Earth carries a static traceless strain t(x) = λΦ(x) (Φ_⊕ ≈ 7e-10), the differential acceleration is η ≈ 2Δ(δm/m)/t² × λ²Φ ≈ 1e7 λ². That is excluded unless λ ≲ 3e-11. Even a second-order strain t ~ Φ² gives η ~ 1e-11.
  - **With the rule** the only leftover is (i). Per nucleon it is δm/m ≈ ½·0.4·4.63e-3·(0.275/0.938) ≈ 2.7e-4 t², whose composition-dependent part (binding and isospin, 1e-3–1e-2 of it, plus electrons) is Δ(δm/m) ≈ 3e-7–3e-6 t². So η ≈ (4e-16–4e-15) λ², at or below MICROSCOPE's level for λ ≲ 1.
  - All of this is conditional on the lattice-frame reading (`PRICE_NOTE` P175; R19-17's W/A), which fixes whether such a strain exists. The rule is the safe side in every case.
- **LLI for matter (comparator, RECALLED, no number quoted).** Clock-comparison (Hughes–Drever-type) tests see no anisotropic rest-mass shifts. Without the rule, the strained rest mass depends on how the strain is oriented relative to the lattice axes (γ for E_g, γ′ for T₂g; cubic symmetry does not tie them, and branch MF gives γ′/γ = 0.31). With the rule both are zero at all orders. The leftover (i) is δm/m ≈ 3e-22 for t ~ 1e-9.
- **The trace sector (suggested; the A₁ bridge is not analysed).** On the fixed-m_c law the pole mass moves linearly under isotropic SF strain: d_t δm = −4.8755e-2 e² per unit t (checked), a Planck-enhanced coupling of ⟨ψ̄ψ⟩ to h_ii (a "rest-mass pressure"). The rule's trace part removes it, again restoring GR's behaviour (cold matter has p ≈ 0; Cassini-type trace bounds, `rF2:106`). How SF trace strain maps to the metric is unregistered (P-R19-35a, `PRICE_NOTE:680`), so this is a direction, not a number.
- **Refereed rows.** The rows built at h = 0 (speed, charge, D1/D1∞) and the traceless Ξ cone rows at O(e²) are unchanged (proved above); A₁ rows that see the linear trace vertex were not computed. The vacuum shear rows μ_E/μ_T2 and λ_nn move at O(e²) on the bare law (§3.3); this is the only change, and (S\*)/(Σ) remove it by definition.

## 4. Against the expectation (`TESTS:9376-9379`)

- **"RULE-WORKS for the additive channel":** borne out within the rule's own scope: one clause, unique, all variants covered, ultralocal, its own residuals tiny, nothing observed removed.
- **"The residual multiplicative channel is suppressed by m_f·a, ~1e-22 or less, far below the Earth row":** borne out. R = 3.3e-22 for nucleons, 8e-24 for electrons; μ_ρ = 8e-43, i.e. 5e-14 of the Earth row. The coefficient itself is smaller than R19-34's H-cov one: z″_t = −4.6e-3 (SF) against −0.0717/4 = −0.018 (H-cov in SF units).
- **"The knock-on onto the vacuum rows is nonzero, but (Σ) absorbs it by stipulation":** borne out. It is nonzero and large (−0.99 × the Dirac sea's own μ_E per unit e²). (S\*) also absorbs it, not only (Σ).
- **"Without (Σ), it moves the root":** borne out (suggested, linear: Δb_s ≈ 40 × Δμ_E leaves the knob's range).
- **"So: RULE-WORKS given (Σ), otherwise RULE-PARTIAL":** **not borne out as stated.** Given (Σ), RULE-WORKS still fails on residual (iv): R19-21's Higgs-sector channels, which the expectation's residual list ("Yukawa/scalar, by estimate") anticipated but did not size, survive any fermion-criticality clause. RULE-WORKS needs (S_loc) as well.
- **Not anticipated:**
  - the T₂g law gap, and (branch MF) the ×2.8 sensitivity of the unruled Hessian to the photon's zone-edge strain;
  - the linear trace-sector term (d_t δm ≠ 0 for iso and nn strain);
  - the rule makes P-F3a/P-F4a unnecessary.

## 5. Prices (named, not adopted)

- **P-R19-34a (counted once; `rR19-34:177-180`; `PRICE_NOTE:679`).** Tested here.
  - Law-functional convention: 0 numbers, 1 clause.
  - Codimension convention: a function per fermion class per order, i.e. 2 per class per order (traceless, O(h²)) or 4 with the trace.
  - Gates: `AX:114-130` (the counterterm is law content; the axioms do not supply it); `AX:85-90` (named conditional).
  - Covers F1/F3/F4 in every variant. Dominates P-F3a and P-F4a, which become unnecessary.
- **Needed with it for RULE-WORKS (counted once, not new):**
  - (S_loc) (P182, OPEN, `vR19-21`) for residual (iv);
  - (S\*) (P177) or (Σ) (P179) for the knock-on.
  - Alternatives for (iv-b) only: twisted edges (P-R19-11c), which leave (iv-c), or leaving the root for chirally symmetric edges.
- **Registration gap (new, not a price): G-F5a, the T₂g-strained interacting photon/gauge law.** F1's frame class does not extend (§3.1(d)). It is needed for γ′, μ_T2's knock-on and every interacting T₂g row under SF. Branch MF (§3.1(d)) is a regular stand-in that sizes it but is not SF-consistent at the photon edge.
- **No axiom text changes.**

## 6. Strong words

- **"Proved"** (short, unrefereed):
  - one scalar condition per strain (P, T, C);
  - uniqueness (IFT, with the slope checked);
  - coverage of every variant (by construction);
  - the parity exclusion of O(a∂h) mass gradients;
  - the knock-on formula;
  - absorption by (S\*)/(Σ) (definitional);
  - Ξ unchanged at O(e²) in the traceless sector;
  - the T₂g singularity of F1's frame class;
  - (iv) is out of the rule's reach.
- **"Checked":**
  - the general-h library against F1 (≤ 7e-18);
  - the cubic-invariant consistency of the nn/iso/E_g derivatives (to ~1e-9 relative);
  - z(m) and z″;
  - e_m;
  - e_tm and the row reproductions (E_g row to 3.6e-4; R19-35's [110] rank-one entry to 5e-5);
  - the T₂g non-convergence;
  - branch MF: its Ward identities, t = 0 equality and Hessians (the numbers are checked; the branch is a stated, unregistered choice).
- **"Estimate":** every SM-mapped size (couplings, σ-terms, Coulomb energies, field strengths RECALLED).
- **"Fails"** for (iv) rests on R19-21's numbers: IGM arithmetic referee-confirmed (`vR19-21:25`); the Earth figure is suggested (`rR19-21:211`). F2's Earth row is a 1D model sensitivity (`vF2` item 2). With the IGM figure alone, (iv-b) exceeds F2's Galaxy/IGM row (row 5) by ~2e28.
- **Not claimed:**
  - two loops;
  - non-abelian or Yukawa loop values;
  - γ′ (T₂g);
  - the on-shell multiplicative slope;
  - a nonlinear retune of the root;
  - the A₁ bridge;
  - that (S_loc) works (it is OPEN).

## 7. Files (`S/` = `scratchpad/C5/F5/scripts/`)

- `f5_lib.py`: F1's law for a general uniform symmetric strain h (3D flows; Psym corners).
- `f5_validate.py` → `f5_validate.out`: (1) f5 against F1's unmodified library; (2) the half zone; (3) T₂g evenness and domain (the values are the singular ones, see `f5_t2g_diag.out`); (4) coarse midpoint free-row check (E_g at the root to ~1%; superseded by the GL rows in `f5_nn_156.out`).
- `f5_mult.py` → `f5_mult_156.out`, `f5_mult_240.out`: z(m), z″ (the 240-node grid moves z″ by ≤ 1%).
- `f5_nn.py` → `f5_nn_156.out`: δm along nn, iso and E_g; e_m, e_tm, row checks, the one-point term.
- `f5_t2g_diag.py` → `f5_t2g_diag.out`: the T₂g singularity.
- `f5_nncheck.py`, `f5_nncheck2.py` → `.out`: the rank-one form of R19-35's Lemma R1 for n = z, [110] and [111] (unit check for λ_nn).
- `f5_c1.py` → `f5_c1.out`: the vacuum's mass slope dμ_E/dm (the (iv-b) coefficient).
- `f5_sizes.py` → `f5_sizes.out`: residual sizes and F1-mapping reproduction.
- `f5_t2g.py`: the T₂g Hessian driver for F1's frame class. Not run past the diagnostic, because that class is singular for T₂g.
- `f5_mf.py` → `f5_mf_ward.out`, `f5_mf_Eg156.out`, `f5_mf_T2g156.out`, `f5_mf_T2g240.out`: branch MF (Ward checks; E_g and T₂g Hessians).
- `queue1.sh`, `queue2.sh`, `queue3.sh`; `*.err`: `/usr/bin/time -l` memory records.
- Unmodified copies: `f1_lib.py`, `f3_lib.py`, `f3_dirac.py`, `f3_mat.py`, `f4_lib.py`; `../arch/`.
