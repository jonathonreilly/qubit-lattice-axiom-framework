# ui55_2 — criteria (pre-registered BEFORE any ui55_2 script exists)

Owner file: UIR55.md §4 (U3: the leading coefficient). Worker: claude-opus-5-5. Written 2026-10-29 (UTC).
Purpose: an independent exact re-derivation, from continuum Feynman rules, of the residue that Theorem TEL attributes to the
n-independent fine Wilson functional: σ_⊥ = −(21/22)β_0^std per unit log in u-units, the ghost's −(1/22)β_0^std, β_0^std = 2N·2b_0.
It is a CONTROL (the brief's item 3), not a proof of anything n-uniform. The lattice-to-continuum step (FLOW Lemma U-Tay,
FINE-IR-gen, CL-V) is not tested here. Arithmetic: sympy exact symbolic/rational only; no floats in any verdict. nice 10.

## Method (fixed now)
- P1 (S³ moments): ⟨Π n_i^{2a_i}⟩ := Π(2a_i − 1)!!/Π_{j=0}^{|a|−1}(4 + 2j) (Gaussian factorisation); cross-check ⟨n_1²⟩, ⟨n_1⁴⟩,
  ⟨n_1²n_2²⟩ by direct sympy integration over S³ in hyperspherical coordinates (measure sin²ψ sinθ dψdθdφ, |S³| = 2π²).
- P2 (vertices derived from the operator, not typed in): act with O_c := Σ_μ(−i∂_μ − q a δ_{μ1})²·1 + s·iq·F (F_{μν} = ∂_μa_ν − ∂_νa_μ as a
  matrix on the vector index; the scalar case is the 1×1 operator without F) on u·e^{ik·x}, with a(x) = (ε/2)(e^{iϑ}e^{ipx_2} + e^{−iϑ}e^{−ipx_2});
  extract V_+(k) (coefficient of εe^{iϑ}, transfer +pe_2), V_−(k) (coefficient of εe^{−iϑ}, transfer −pe_2), Ô_2 (ϑ-free ε² part).
- P3 (integrand): f(k, p) := tr Ô_2/|k|² − ½Σ_± tr[V_∓(k ± pe_2)V_±(k)]/(|k|²|k ± pe_2|²) (O_0 = |k|²·1); with k = R·n, |n| = 1, p = 1, expand
  f(Rn, e_2) − f(Rn, 0) in t = 1/R to order t⁴; h(n) := the t⁴ coefficient; c_3(n) := the t³ coefficient.
- P4: ⟨h⟩ over S³; the p²log(1/p) coefficient of the ε²-density is C = q²⟨h⟩/(8π²) ((2π)^{-4}|S³| = 1/(8π²)).

## PASS conditions
- L0: ⟨c_3⟩ = 0 (the t³ term is odd and does not contribute to the log).
- L1: ⟨h_S⟩ = 1/12, i.e. C_S = q²/(96π²) = q²c_g (FLOW's c_g = 1/(96π²)).
- L2: ⟨h_V⟩/⟨h_S⟩ = −20 with s = 2 (C_{K_F} = −20q²c_g).
- L3: per positive root, transverse group (vector − ghost, complex fields) C_V − C_S = −21q²c_g; full group (vector − 2·ghost)
  C_V − 2C_S = −22q²c_g; ratio exactly 21/22.
- L4: Σ_{i<j}(h_i − h_j)² = NΣh_i² − (Σh_i)² identically (sympy, N = 2, 3, 4), hence = N² when Σh_i = 0 and Σh_i² = N (⟨H, H⟩ = 1 in
  ⟨X, Y⟩ = −(1/N)tr XY).
- L5: u-unit conversion (Codex §3.1's chain: density difference divided by the Wilson-wave density P²/4, i.e. slope = 4 × density
  coefficient per positive root, summed with Σq_α² = N²): transverse slope −84N²c_g = −7N²/(8π²); ghost slope −4N²c_g = −N²/(24π²);
  their sum −88N²c_g = −β_0^std with β_0^std := 2N·2b_0, b_0 := 11N/(48π²); and −84/88 = −21/22.
## Designed-FAIL controls (each must FIRE: the displayed equality must be FALSE)
- Lc1: spin coupling s = 1: ⟨h_V⟩/⟨h_S⟩ = −20.
- Lc2: product-of-marginals moment ⟨n_1²n_2²⟩ := 1/16 in place of 1/24: ⟨h_S⟩ = 1/12.
- Lc3: the FN-1 slip, β_0 := 2N·b_0: 88N²c_g = 2N·b_0.
Overall PASS iff L0-L5 hold and Lc1-Lc3 all fire. Outputs: checks/ui55_2_out.txt (unaltered), checks/ui55_2_err.txt.
