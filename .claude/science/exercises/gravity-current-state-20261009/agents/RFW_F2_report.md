# Lane RFW, probe F2: constructive Noether search at O(κ²) on Z⁴

Worker: Claude Opus 5.5 (same family as the supervisor). Run 01:48Z–02:25Z, 2026-10-12. No repository files were edited.
Scratch folder: `.../scratchpad/RFW/F2/`, holding 9 scripts, 8 `.out` files and this report.

Read first: TESTS.md "Lane RFW"; `agents/C4_K2_report.md`, `C4_K2_referee.md`, `C4_K2_referee_full.md`; `agents/RC_C3_referee.md`; `agents/RV4_S1_report.md` (Theorem D) and `RV4_S1_referee.md`; and the K2 scripts (`k2_scalar_stress_exact.py`, `k2_killing_closure.py`, `k2_graviton_gauge_killing.py`). The K2 symbols are re-derived in Fourier form in `f2_common.py` and checked there (§1).

## Reading against the fixed lines

**F2: FAIL (bounded).** This needs the codex referee before it is recorded.

| Fixed line | Status |
|---|---|
| PASS: an explicit local completion that is invariant through O(κ²) for non-uniform ξ, including the Killing sector, with a Ward identity giving μ_E = μ_T2 | **Not met.** No completion exists (below). There is no Ward identity, so μ_E and μ_T2 are not fixed |
| FAIL: proved that no completion exists in the stated class (range, polynomial order, finite field content) | **Met for K2's scalar.** Holds at every finite range r, not just r ≤ 3. All polynomial orders are covered, because only the h¹φ²ξ coefficient at O(κ²) is used. Fields are h and φ only. PROVED, same family: §2 and §4 |

The obstruction already appears in the cheapest necessary sector: constant ξ (a translation Killing field), at first order in the graviton momentum q. That first-order term is the rotation-charge part of the identity.

All field-dependent pieces either drop out or enter only through functions of q:
- the seagull;
- δφ linear in h;
- δh quadratic in φ;
- field-dependent parameters λ(ξ, h) and λ(ξ, φφ);
- the cubic h³ vertex.

The defect left to cancel is the matter's Leibniz factor cos p_c, a function of the matter momentum p. A function of q cannot cancel it.

**Continuum/SLAC control.** The same system solves to 1e-15.

## 1. Setting, unknowns and checks of the inputs

**Action and gauge map (K2, base-point labels).**
- S = S_FP(h) + S_m(φ) − (κ/2) Σ h_μν T_μν, with K7a placement.
- δh = ∇ξ + ∇ξ, δφ = κ L_ξ φ.

**Most general completion searched, at order ξ·h·φ·φ at O(κ²):**
- δh ⊃ κ A_ξ h: any linear stencil of range r. This includes field-dependent parameters ∇λ(ξ, h).
- δh ⊃ κ² X_ξ(φ, φ): range r. This includes ∇λ(ξ, φφ).
- δφ ⊃ κ² B_ξ(h, φ): any. This includes L_{λ(ξ,h)} φ.
- Seagull S₂(h, h, φ, φ): any.
- h³ vertex: any.

**Relaxations, which can only help existence.**
- A_ξ is not required to be a symmetry of the free FP action. The O(κ) pure-gravity condition is dropped.
- Coefficients may be complex.
- B is unrestricted in range.

**Input checks (CHECKED, `f2_common.py`).**
- The lattice FP symbol satisfies K(q)D(q) = 0 to 3e-16 at random complex q.
- K has rank 6.
- K2's O(κ) Noether identity holds in Fourier form at random complex momenta to 8e-16, for m² = 0, 0.75 and 3. The continuum version also holds.

## 2. Reduction: what survives at constant ξ (PROVED, same family)

Take ξ = c constant. A Killing field is a legitimate test: if δS = Σ ξ·R vanishes for all compactly supported ξ, then R ≡ 0, so δS also vanishes for constant ξ.

Take the coefficient of h(q)φ(k₁)φ(k₂), with q = −k₁ − k₂ and both k_i on the complex shell E(k_i) = 0. The pieces behave as follows:
- **Seagull:** δ₀h = Dc = 0, so it drops out.
- **B:** every B term multiplies E(k₁) or E(k₂), so it vanishes on shell.
- **X:** it enters as K(q)ᵀX(k₁, k₂). K is a sum of products of two differences, so this term is O(|q|²).
- **What is left:**

  Y(q; p) = i c·(f(p) + f(k₂)) W⊙T(p, k₂) + A_c(q)ᵀ W⊙T(p, k₂),  with k₂ = −p − q,

  and Y must be O(|q|²) along the shell.

Here W is the weight with which each of the 10 independent components h_μν enters the coupling: 1 for diagonal components, 2 for off-diagonal ones.

The term i c·(f(p) + f(k₂)) is O(q). So the necessary conditions are, for every shell point p and every tangent t (with t·∇E(p) = 0):

- **(Z)** A₀ᵀ T₀(p) = 0.
- **(F)** Σ_μ t_μ M_μᵀ T₀(p) + A₀ᵀ ∂T[t] = i (t·∇f_c(p)) T₀(p).

The quantities are:
- T₀(p) = W⊙T(p, −p);
- A₀ = A_c(0) and M_μ = ∂A_c/∂q_μ(0), which are **constant** 10×10 matrices.

**Forward lemma (PROVED from the O(κ) identity alone).** Expand the identity at k₁ = p, k₂ = −p − Q, to first order in Q. The result is T(p, −p)_μν = n_μ f_ν with n = ∇E(p), for any local symmetric stress paired with the pseudo-translation i f.

For K2, n = 2 sin p and f = sin p, so T₀ = 2 sin p ⊗ sin p. CHECKED to 1e-15 on shell; the deviation off shell is 1.9 (`f2_general_kinetic.out` (a)).

**Range dependence.** The range-r coefficients of A_c reach (A₀, M_μ) only through the map that sends each offset o to (1, i o). This map has rank 5 per matrix entry, i.e. it is onto, for every r ≥ 1; for r = 0 its rank is 1 (`f2_jet_system.out`). So the solvability of (Z)+(F) is the answer for every r ≥ 1 at once, and also for any A whose symbol is C¹ at q = 0.

## 3. Results of the linear systems (CHECKED)

### 3a. The 1-jet system (`f2_jet_system.py/.out`)

**Setup.**
- 200 complex shell points, 3 tangents each.
- The system decouples by output component: 50 unknowns per component.
- The residual is min‖Gu − b‖/‖b‖.

| System | m² = 0 | 0.25 | 1 | 3 |
|---|---|---|---|---|
| Continuum/SLAC symbols, any r ≥ 1 | 2.0e-15 | 2.0e-15 | 3.3e-15 | 1.4e-15 |
| K2 lattice scalar, any r ≥ 1 | **0.49** | **0.47** | **0.45** | **0.53** |
| K2 lattice scalar, r = 0 (on-site A only) | 0.97 | 0.96 | 0.95 | 0.96 |

**Details.**
- **Rank.** The rank is 46 of 50 per component. The 4 null directions are the M_μ with M_μᵀT₀ ∝ n_μ, which make no contribution.
- **Per component.** At m² = 1 the residuals are 0.28–0.56; every component is obstructed.
- **Natural candidate, no fit.** Any A_c whose 1-jet is a translation of h (for example i sin q_c or e^{iq_c} − 1) leaves a residual of 0.67 on the lattice and 8e-17 in the continuum.
- **Leibniz diagnostic.** Keep the lattice T and the lattice shell, but replace cos p_c by 1 in t·∇f_c. The lattice system then solves to 1.7e-15 (m² = 0.25 and 1).
- **So the cos k_c factor is the entire obstruction.** This is the Euclidean twin of C3's Q_ca = cos k_c sin k_a and of K2's [L_ω, D_ρ] = −ω S_ρ D_ν.

### 3b. The full finite-q system, with no jet reduction (`f2_full_system.py/.out`)

**Setup.**
- k₁ and k₂ are independent on the complex shell.
- A (range r_A) and X (range r_X) are explicit unknowns. B drops out on shell.

| System | Unknowns | Rank | Residual |
|---|---|---|---|
| Continuum: A of degree ≤ 1, X of degree ≤ 1 (m² = 0.25, 1) | 550 | 506 | 4.6e-15, 5.3e-15 |
| Lattice m² = 0.25: r_A = 1, X = 0 | 900 | 860 | **0.48** |
| Lattice m² = 0.25: r_A = 1, r_X = 1 | 1350 | 1216 | **0.32** |
| Lattice m² = 1: r_A = 1, X = 0 | 900 | 860 | **0.45** |
| Lattice m² = 1: r_A = 1, r_X = 1 | 1350 | 1216 | **0.30** |
| Lattice m² = 1: r_A = 2, X = 0 | 4100 | 3740 | **0.28** |
| Lattice m² = 1: r_A = 2, r_X = 1 | 4550 | 4096 | **0.24** |

**Rank deficiency is exactly the trivial directions.** In the A-only runs it is:
- 40 = 4 × 10 at r_A = 1;
- 360 = 9 × 40 at r_A = 2.

These are precisely the pure-gauge field-dependent parameters A = D(q)N(q), whose effect vanishes on shell.

**Why the finite-q residual falls with r while the obstruction does not.** At small momentum transfer |q| ≈ s:
- the unconstrained best fit has coefficient norms of 24, 266, 7.0e3 and 1.4e5 at s = 0.3, 0.1, 0.03 and 0.01. That is roughly s⁻²: the fit promotes second-jet terms to O(s);
- a bounded (ridge) fit returns to the 1-jet floor: 0.47 at s = 0.01, against 0.455 (`f2_coeff_growth.out`).

An exact solution has fixed coefficients, so it must satisfy the 1-jet system. The fall with r is a fitting artefact, not an approach to a solution.

### 3c. Other O(κ) data (`f2_general_kinetic.out`, `f2_dressed_translation.out`)

**Other local kinetic terms.** The pseudo-translation is f = ∇A/2. A local symmetric T then exists by K2's corollary, and T₀ = n⊗f by the forward lemma. In every case T₀ spans C¹⁰, so (Z) forces A₀ = 0. 1-jet residuals at m² = 0.25 / 1:

| Kinetic term | Residual (m² = 0.25 / 1) |
|---|---|
| Continuum | 5e-10 / 7e-10 (finite-difference Hessian) |
| Nearest neighbour | 0.51 / 0.47 |
| Improved, R = 2 | 0.43 / 0.39 |
| Improved, R = 3 | 0.38 / 0.41 |
| Two-step sin²k | 0.85 / 0.84 |
| Non-separable plaquette term, β = ½ | 0.65 / 0.60 |

**Dressed pseudo-translation for the nearest-neighbour action.** Take f = λ(p)∇A, with λ in a 19-dimensional family of even local trig polynomials, normalized on shell at the rest point. The best residual is 0.36 / 0.41.

**Trap found and excluded.** My first version normalized λ(0) = ½ off shell, and it "solved" to 1e-14. The solution has λ ≡ 0 on the whole shell (|λ| < 1e-14; `f2_dressed_inspect.out`). That means f is a trivial translation with no charge. It is a degenerate solution, not a completion.

## 4. Proof that (Z)+(F) has no solution for K2's scalar (PROVED, same family; `f2_witness.py/.out`)

Write v = sin p, so that T₀ = 2 v⊗v, and take c = e₀.

1. **A₀ = 0.** By (Z), A₀ᵀ(v⊗v) = 0 on the shell, and the values v⊗v span C¹⁰ (CHECKED: rank 10). So A₀ = 0.
2. **Rewrite (F).** It now says Σ_μ t_μ X_μ = 0 for all t with v·t = 0, where X_μ = M_μᵀ(W⊙v⊗v) − i δ_μ0 cos p₀ (W⊙v⊗v). Hence X_μ = v_μ Λ(p) for a single vector Λ(p).
3. **Eliminate Λ.** From v₁X₀ − v₀X₁ = 0, the (2,2) component gives

   cos p₀ · v₁ v₂² = P(v),

   where P is a fixed homogeneous cubic (M is constant). So on the shell, cos p₀ = P(v)/(v₁v₂²) is homogeneous of degree 0 in v.
4. **Witness.** Fix a complex direction u. On the ray v = s u, the shell condition reads Σ_μ ε_μ √(1 − s²u_μ²) = 4 + m²/2. This has 8 roots s, with various sign patterns ε. The 6 printed roots all have v₁v₂ ≠ 0 and give different values of cos p₀ (mpmath at 40 digits; every printed shell residual is below 3e-40, and the root filter is < 1e-30). For example, at m² = 0.25 the values are 1.032 and 1.600:
   - spread 11.2 at m² = 0.25;
   - spread 67.0 at m² = 1.

   That contradicts step 3. ∎

**Scope of the proof.**
- It holds for every finite range r.
- It also holds for any A whose symbol is C¹ at q = 0, provided X and B are entire.
- At the massless point and for other masses the result is the CHECKED least-squares residual (0.45–0.53); the witness construction is generic.

**What the proof shows (SUGGESTED reading).** Write V_ω = ω·v for the scalar's pseudo-rotation field. The quantity v₁∂₀f₀ − v₀∂₁f₀ is V_ω·∇f₀. The Noether 1-jet condition is therefore K2's closure condition (★), with the e(4) structure constants relaxed to arbitrary constant 10×10 matrices acting on stress components. Even that relaxation fails, because of the cos factor.

## 5. Ward identity and μ_E = μ_T2

**Not applicable.** No lattice completion exists, so there is no Ward identity to evaluate, and the uniform-strain response was not computed.

- In the continuum/SLAC control the completion exists: A_c = translation of h, X = B = 0. RV4 S1 Theorem D then gives μ_E = μ_T2.
- SUGGESTED link: the object that blocks the completion here, a non-constant Hessian of the dispersion on the shell (cos p_c), is the same one behind RV4's Jacobian μ_E. RV4 S1 identified μ_E − μ_T2 as the Ward defect.

## 6. Against the supervisor's expectation

| Expectation | Outcome |
|---|---|
| "F2's linear system has no solution for r ≤ 3" | **Confirmed, and extended to every finite r**, and to any A with a C¹ symbol |
| "At flat background the field-dependent parts vanish (C3 lemma)" | **Refined.** They do not all vanish: A and X contribute. But at constant ξ they depend only on the graviton momentum q, and they enter at O(q) only through constant matrices. They cannot absorb a factor that depends on the matter momentum p |
| Expected reading FAIL (bounded) | **Matches** |

## 7. Assumptions, scope and escapes

**Assumptions.**
- A1: K2's Euclidean Z⁴ setting, at ξ = 1.
- A2: K2's O(κ) data are fixed (T up to improvements, L_ξ up to trivial symmetries), as the brief states. Improvements and trivial symmetries drop out of the 1-jet.
- A3: local means finite range, and the proof also covers symbols analytic near q = 0 with entire X and B.
- A4: the graded Noether expansion (field count = power of κ).

**Not covered.**
- Changing the matter's Killing generators beyond the families checked. That is K2's conditional theorem; the dressed-λ and other-kinetic results are CHECKED only.
- Fermions.
- Multi-band matter, auxiliary fields, or infinite field content.
- The non-uniform-ξ equations and the h³ vertex were not assembled. They cannot rescue a failed necessary subsystem.

**Escapes (outside the class).**
- SLAC or non-local matter with linear f: the control solves.
- Perfect or quasi-local actions with a non-compact shell (K2's escape 1).
- Accepting invariance only at O(κ).

**Strong words.**
- "Exact" means agreement to 1e-15 at random complex momenta, or 40-digit mpmath.
- "PROVED" means a short argument under A1–A4, same family, not refereed.

## Files (this folder)

- `f2_common.py`: Fourier symbols (T, E, K, D, L) and the KD = 0 and O(κ) identity checks.
- `f2_jet_system.py` / `.out`: the 1-jet system, controls, the natural candidate, the Leibniz diagnostic and the rank of the jet map against r.
- `f2_full_system.py` / `.out`: the full finite-q system with explicit A and X unknowns (r_A ≤ 2, r_X ≤ 1), plus small-q runs.
- `f2_coeff_growth.py` / `.out`: coefficient blow-up of small-q fits, and the ridge return to the 1-jet floor.
- `f2_general_kinetic.py` / `.out`: the forward lemma check and the other kinetic terms.
- `f2_dressed_translation.py` / `.out`, `f2_dressed_inspect.py` / `.out`: dressed pseudo-translations, and the excluded λ ≡ 0 trap.
- `f2_witness.py` / `.out`: the 40-digit witness for §4.
- `F2_report.md`: this report.
