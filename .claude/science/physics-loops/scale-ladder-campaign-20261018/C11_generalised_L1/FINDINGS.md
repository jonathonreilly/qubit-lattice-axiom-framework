# C11 findings: generalised L1 (per-letter additive speed at ±k*)

Provenance: a worker of the same model family. **Unchecked.** Saved by the supervisor from the hand-back (the worker's file write was blocked). The model code is `../B26_check/mymodel.py` (an independent from-scratch build), imported read-only; no other repo or campaign code is used.

**Runner.** `c11_generalised_L1.py`: **TOTAL PASS=28 FAIL=0**, about 20 s on 3 threads. Three earlier failing logs record the worker's own errors:
- `_firstrun.log`: a √2 in the τ normalisation; a wrong expectation that {±U_R} is 2O; B26 words with no isolated doublet.
- `_secondrun.log`: an inaccurate raw eigenphase-slope check.
- `_thirdrun_directslope.log`: an O(δ²) check, worst error 1.4e−4 against a 1e−4 tolerance. The fix, Richardson extrapolation, was chosen after seeing this result (disclosed). The main DPT checks were unaffected.

**Answer.** The lemma holds:
- every product of O-covariant letters has an untilted isotropic cone on an isolated D± level at ±k*;
- its speed is |Σ_j v_j|, with one real coefficient per (letter, doublet, ±k*).

Two further outcomes:
- **Phase.** c_U/u_U is purely imaginary, so the real quantity is v = c_U/(i·u_U).
- **4-fold levels.** B20's 4-fold statement (equal speeds, opposite chirality) does **not** carry over to generic exp(iH) letters.

## Setup

- Bloch matrices X(k) = Σ_a X_a e^{ik·a}, with k* = (π/2)(1,−1,1).
- A gauge-dressed rotation acts by X ↦ U_R X(Rᵀk+πλ) U_Rᵀ.
- Letters are C¹ unitaries with U_R U(Rᵀk+πλ) U_Rᵀ = χ(g)U(k), χ ∈ {A1, A2}. Finite range is not needed.

Model facts (certified numerically to machine precision, runner §1–2):
- **F1.** All 24 proper rotations fix ±k* mod 2π, so the little group is O and ρ(g) = U_R.
- **F2.** {±U_R} (48 elements) has 13 involutions, so it is **GL(2,3)**, the non-split double cover isoclinic to 2O. Relifting odd elements by i gives 2O; no conjugation, Schur argument or χ_A2 relation changes. Which of D± is "E1/2" is a convention; what is fixed is D− ≅ A2⊗D+ and D− ≇ D+.
- **F3.** 12 = D₊ ⊕ D₋ ⊕ 2G3/2: D± are irreducible, inequivalent and of multiplicity 1. χ_{D−} = χ_A2·χ_{D+} for all 24 g, so A2⊗E1/2 ≅ E5/2. The complement has no D± content, and the commutant has dimension 6.
- **F4.** On each D_b the T1 triples in End(D_b) form a 1-dimensional, traceless space. This gives a unique Hermitian triple τ^{(b)} with τ_iτ_j = δ_ij + iε_ijk τ_k.
- **F5.** Hom(D₊,D₋) contains no T1 and contains T2 = T1⊗A2 once; End(D) contains no T2.

## Lemma and proof

**Definition.** P_b U†∂_iU P_b = i·v_U^{(b)}(k₀)·τ^{(b)}_i with v real, for b = ±1 and k₀ ∈ {±k*}.

**Statement.** Let W = U₁⋯U_m with ∏χ_j = +1, and let D_a be an isolated 2-fold level of W(k₀). Then:
- (a) W preserves D_a and is a scalar there.
- (b) P_a W†∂_iW P_a = i·(Σ_j v_j^{(b_j)})·τ^{(a)}_i, with b_j = a·∏_{l>j}χ_l.
- (c) The level is an untilted isotropic cone of speed |Σ_j v_j^{(b_j)}|, with chirality sign(Σv) in the frame τ^{(a)}.

**Proof.**
1. *Schur.* A1 letters are scalars (phases) on D₊ and D₋ by multiplicity 1. A2 letters intertwine ρ with A2⊗ρ, so they swap D₊ ↔ D₋. A word with ∏χ = 1 is A1.
2. *Wigner–Eckart.* ∂U transforms as χ⊗T1. Then M_i = P_b U†∂_iU P_b is a T1 triple in End(D_b), so M = c·τ by F4. There is no tilt part, since O has no invariant vector. Unitarity makes M anti-Hermitian, so c = iv with v real, and P∂UP = u·iv·τ.
3. *Additivity.* W†∂W = Σ_j V_j†(U_j†∂U_j)V_j with V_j = U_{j+1}⋯U_m. On D_a, V_j is a unitary intertwiner up to a character, so V_j†τ^{(b_j)}V_j = τ^{(a)} by F4.
4. *Cone.* First-order DPT gives eigenphases ±(Σv)|q|, and the Berry charge is sign(Σv) up to a global convention. ∎

**Corollaries.**
- v_{UV}^{(b)} = v_V^{(b)} + v_U^{(χ_V b)}, and v_{U⁻¹}^{(b)} = −v_U^{(χ_U b)}.
- Every A2 letter is A0·U′ with U′ an A1 letter, and v_{A0·U′} = v_{U′}: A2 letters only swap the label.
- On the old palette, Σv = a·(√2/3)·n_eff with n_eff = Σ_p (−1)^{#A0 to the left}·p. This is B20's L1 and B26's sign-flipped n_eff, with chirality matching B20.

## Checks (all PASS)

- **§1–2:** F1–F5, 11 checks.
- **§3, letters:** 29 letters, each covariant with its declared χ, scalar (A1) or swapping (A2), with v real (worst residual 8e−11).

  | Letter | v on D₊ | v on D₋ |
  |---|---|---|
  | S | +√2/3 | −√2/3 |
  | S², S⁻¹, S⁻² | 2v_S, −v_S, −2v_S | same pattern |
  | R_L, Rt, E±, exp(iθR_L) (θ = π/6, π/3, π/2, 5π/6, 0.7317), random symmetric on-site | 0 | 0 |
  | A0·S^a (A2) | a·v_S^{(b)}, b = input label | |
  | generic exp(iH) | real, letter-dependent (e.g. 0.694) | e.g. −0.061 |

  - The zero for f(R_L) also follows exactly from Daleckii–Krein: P∂f(R_L)P = f′(r)·P∂R_L P = 0.
  - For generic letters, v^{(+)} + v^{(−)} ≠ 0 and v(+k*) ≠ v(−k*).
  - The expected constants come from B20 L1, B26_check and C8.
- **§4, random words:** 260 even-A2 words of length 2–6, half with a generic exp(iH) letter. They give 956 isolated D± levels; 84 degenerate levels were excluded.
  - Speed = |Σv| (worst 1.3e−9); isotropy spread and tilt 3e−11.
  - The signed identity (b) holds entrywise (worst 1.3e−9).
  - Direct diagonalisation with Richardson extrapolation (300 levels × 3 directions): worst 3e−8.
- **§5, B26 reproduction:** 404 doublets; speed = |n_eff|·√2/3, with |n_eff| ≠ |n_raw| in 192 of them.
- **§6, 4-fold D₊⊕D₋ levels:** 192 levels, made 4-fold by appending Z = exp(iα·P_{D₊}) (v = 0).
  - The first-order D₊↔D₋ block vanishes (F5): no mixing.
  - There are two untilted isotropic cones at |Σv^{(+ path)}| and |Σv^{(− path)}| (worst deviation 1.8e−9).
  - Old-palette words have equal speeds and opposite chirality (72 levels; B20's 4-fold L1).
  - **Generic exp(iH) words:** the speeds differ in 120/120 levels, and both cones have the same chirality in 35/120 (net first-order node charge ±2). This does not contradict the global Nielsen–Ninomiya count, but L2's net-chirality bookkeeping would need to be redone for generic letters.

## Status

- **Exact, given F1–F5:**
  - the scalar and swap action;
  - A2⊗E1/2 ≅ E5/2;
  - one real v per (letter, doublet, ±k*), with c/u imaginary;
  - the path-additive formula;
  - untilted isotropic cones at |Σv| on isolated D± levels;
  - L1 and B26's n_eff as special cases;
  - no first-order mixing at 4-fold levels.
- **Numerical:** F1–F5 (machine precision) and all agreement figures.
- **Scope:**
  - Covers only isolated 2-fold D± levels at ±k*.
  - Says nothing about other momenta, G3/2 levels, or odd-∏χ words.
  - Does not cover O_h characters, antiunitary letters, or subgroup-covariant letters (e.g. exp(π/4·A0)).

## Open

- An independent check with a different implementation of the T1 frame and the path bookkeeping; a symbolic proof of F3–F4.
- Higher orders at k*: O(q²) is a scalar on D by Schur; O(q³) could be anisotropic. Neither is computed.
- When generic letters give equal 4-fold speeds.
- What same-chirality 4-fold nodes mean for L2/L3 in enlarged palettes.
- G3/2 levels, where per-letter coefficients become 2×2 matrices that need not add.
