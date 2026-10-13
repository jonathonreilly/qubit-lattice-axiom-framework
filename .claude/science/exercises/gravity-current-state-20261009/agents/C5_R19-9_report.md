# C5 R19-9 report: the exact W1 photon stress, built and checked; the 6-knob SM root re-solved with it

**Author and status.**
- Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 04:41Z to 05:20Z.
- No repository file was edited. Nothing was downloaded; no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `.../scratchpad/C5/R19-9/`. My scripts and `.out` files are at top level of `S/`. `S/arch18`, `S/arch18_13`, `S/arch18_9`, `S/arch17_4`, `S/arch99`, `S/arch9` hold unmodified copies of `P/scripts/C5/{R18-5, R18-13, R18-9, R17-4, R9-9, R19-5}/`.
- Every run used `OMP_NUM_THREADS=2` and took ≤ 5 min. Machine load 2.8–9.9; at most three of my jobs at once.

**Read.**
- `AX` in full.
- `P/TESTS.md`: C5 method (`:2302-2319`); my item (`:7544-7568`); R19-5 item (`:7317-7349`); the R18-12/R18-13/R19-1..3 verdicts (`:7490-7542`).
- `P/agents/C5_R19-5_report.md` (all), and its referee verdict, which appeared during my run: `scratchpad/C5/ref_R19-5/R19-5_referee_verdict.md` (`vR19-5`): **CONFIRMED WITH CORRECTIONS, OPEN**. Its item 6 says exactly what this item has to do: the photon completion was an outline and the corner numbers an under-resolved size estimate.
- `P/agents/C5_R18-13_report.md` (§§0–3.6, Lemmas C, O, S) and its verdict (`TESTS:7505-7517`); `P/agents/C5_R18-9_report.md` grep hits and `C5_R18-9_referee_verdict.md` (`vR18-9`); R8-2 Construction A (`C5_R8-2_report.md:73-92,192`) and R13-5 Lemma P1 (`C5_R13-5_report.md:143-182`) through R19-5's and vR19-5's citations.

**Runners rechecked before use (checked).**
- R18-13 `vwface.vertex_geo`: my generalization `lib199.vertex` (placement P and own-direction u passed as arrays) equals it to 0.0 on 300 random inputs (`r199_exact_r0.1.out:2`).
- R18-13's exact-shift Richardson, rerun with my glue code at N = 128: Ξ_face1(root a + w) = −1.307497e-2, equal to R19-5's archived `r195_corner_N128.out` value −1.30750e-2 (`r199_corner_grid_N128.out`).
- R18-9 `jac.py` rerun at vR18-9's retuned root (`root_refR18-9.npy`) with the N = 224 photon line: det −3.2045e-4, σ_min 6.28e-4, matching vR18-9's det −3.2056e-4, σ_min 6.31e-4 (`r199_jac_refroot.out`; `vR18-9:13`).
- R17-4 `offaxis` and R18-13 `dface` at the retuned root give scalar face rows (−4.5764e-4, −6.2775e-4) per field, equal to R18-13's `scal_offaxis_N224.out` (`r199_facejac_N96.out:2`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **The exact photon stress exists and is built (checked to ≤ 6.5e-14).**
   - It is glued from three pieces, each an exact solution of W1 where it is used:
     - **corner** (both legs within r of k = 0): the ordinary continuum Maxwell stress. There the lattice photon *is* the continuum photon (σ = k inside the box) and the graviton divergence *is* q (d = q for |q| ≤ 1), so the textbook conservation law is exact.
     - **one soft leg**: VW's own spatial kernel, with time components from inverting the Sylvester map. With one leg soft and one hard, the map never has a zero, and on the soft side the inverse is a power series in h(k_soft), so it is smooth through k = 0.
     - **both legs hard** (the rest of the torus): VW's pair block with R13-5's P1 time components, and a fresh scattering block, R8-2's "dust" kernel, written in closed form: M^{μν} = g^μ g^ν × (energy density), g = (1, Δ_j/(ω₁+ω₂)), Δ_j a one-dimensional divided difference.
   - The glue is a smooth partition of unity. W1 is linear and pointwise, so the glued kernel is exact everywhere (R8-2's gluing lemma).
   - W1 holds on the physical (Gauss-law) block to ≤ 3.4e-14 relative and ≤ 6.5e-14 absolute over 10 targeted families and 40,000 dense random pairs, at r = 0.1 and 0.05. The kernel is μν-symmetric, Hermitian, cubic-covariant, continuous across the Brillouin-zone faces (in the twisted sense of the rotated frame), has ∫T⁰⁰ = H, and has Lemma F's forward values.
   - Its spatial **pair** block equals VW (root a, w_d, w_o) wherever a leg lies outside the corner ball, to 8e-16. That is the only part of the stress the TT rows see.
2. **Single soft legs: the Gauss-law bookkeeping is the continuum's.** The kernel is defined modulo terms that vanish when ∇·E = 0. W1 holds on the physical block, exactly as the continuum Maxwell stress is conserved only on the constraint surface (its full-space residual is O(1), checked). The transverse projector at a soft leg has no limit, but the kernel does: it is analytic in h(k_soft).
3. **Corner cost (proved form, checked value).** The rows change by exactly C_e·r⁴ per vector, with C computed by exact quadrature:
   - C_T2g = C_Eg = 6.671e-5, C_face1 = 2.967e-4, C_face2 = 1.609e-4 (smooth corner profile; a sharp ball would be 3.9× larger).
   - At r = 0.1 the 12-vector totals move by 8.0e-8 (axial) and 3.6e-7 / 1.9e-7 (face1 / face2). At r = 0.05 by 5e-9 and 2.2e-8 / 1.2e-8.
   - A grid check converges to these values (N = 96 → 128 at r = 0.4: 4.5% → 1.9% on T₂g; at r = 0.8: 0.5%).
   - R19-5's sampled cube numbers were the right order but are not usable as values (vR19-5 item 6).
4. **The 6-knob root re-solves with the exact vertex (checked).** This was done in the campaign's own evaluator model (R18-9's axial evaluator, the archived off-axis evaluators, photon N = 224), plus the exact-vertex corner term.
   - Without the corner term, the model's root reproduces R18-9's stored root to 6e-10 and R18-13's (w_d, w_o) to 1e-7.
   - With it, at r = 0.05 and 0.1, all six rows (T₂g, E_g, μ_E, μ_T₂, face1, face2) re-solve to ≤ 3.3e-11. The body row follows by Lemma C.
   - Knob shifts at r = 0.1: b_s +2.9e-6, b_f +2.3e-7, r_D +1.2e-7, a −7.6e-9, w_d −1.4e-7, w_o −2.5e-8. At r = 0.05 they are 16× smaller (∝ r⁴; they agree with linear response).
   - The largest shift is 16× smaller than the root's existing quadrature ambiguity along its ill-conditioned b_s direction: vR18-9's converged-quadrature retuning moved b_s by −4.7e-5.
   - The bill is unchanged: 6 equality tunings + 1 window selection. Exactness adds only untuned law data (r, the glue profile, the scattering kernel).
5. **Worker reading: PHOTON-EXACT** (unrefereed), within the inherited scope: one loop, the supplied vacuum, ultralocal seagull, SF, R18-13's VWa-geo off-axis extension, class 𝒢 (P-R19-5a), linearized W1 only (not W2), m = 0.01 only.

---

## 1. Class, conventions, hypotheses (stated before any result)

**Fields and W1 (lib199.py docstring).**
- Photon in R17-12's rotated frame (`arch18/photon.py:3-6`): continuum Maxwell with momentum vector σ(k), σ_l = sgn(k_l)d_γ(|k_l|), antiperiodic. Field basis ψ = (Ẽ, B̃) ∈ ℂ⁶; i∂_tψ = hψ with h(k) = [[0, −X], [X, 0]], Xv = σ × v. The rotated frame is the Fourier transform with each component's true position, so cubic rotations act as signed permutations and a BZ-face wrap k_l → k_l ± 2π acts as T_l = diag(Ẽ_l → −Ẽ_l; B̃_m → −B̃_m, m ≠ l).
- Stress T^{μν}(q) = Σ ψ†(k₁)M^{μν}(k₁,k₂)ψ(k₂), q = k₁ − k₂.
- Graviton: R9-9's D_j(q) = d(q_j)e^{iq_j/2}, d = q on |q| ≤ 1, 2 sin(q/2) beyond 2.5 (`arch99/r99_graviton.py:19-25`). With T^{0j} on the j-link and T^{ij} at (î + ĵ)/2 (R9-9's 09-14 placement, `C5_R9-9_report.md:100`), the phases cancel (proved: two lines of algebra, lib199 docstring; the same reduction R9-9 used for Construction A) and W1 reads
  h(k₁)M^{0ν} − M^{0ν}h(k₂) = Σ_j d(q_j)M^{jν}, with (H-sym) M^{j0} = M^{0j}.
- **Exact** means: on the physical block P_T(k₁)·P_T(k₂), where P_T = h²/ω² is the transverse (Gauss-law) projector, to machine precision at every sampled point of T³ × T³.
- **Sign.** VW's T_ij = c_ic_j[E_iE_j + B_iB_j − ½δ(E² + B²)] is the Maxwell stress; the momentum flux is its negative. The continuum check fixes SIGN = −1 (residual 3e-15; SIGN = +1 gives O(1), `r199_exact_r0.1.out:4-5`). The TT rows see |amplitude|², so the sign does not enter them.

**Input data (counted once).**
- Photon edge γG_w(2.9435, 0.198093) (`TESTS:7554`); VWa-geo (R18-13) at a = −0.176095005 (vR18-9 retuned) and (w_d, w_o) = (−1.171554, −0.195418) (R18-13 N = 224).
- σ inside the box is used as exactly k (the law's definition). The archived tabulation reproduces it to ~1e-12 relative, which showed up as a 2e-12 residual of the continuum piece before this was fixed; outside the box the archived tabulated increment is used.

**Hypotheses carried (not derived).**
- One loop; supplied vacuum; ultralocal seagull; SF for the μ rows; the TT rows Ξ_e = ∂_{q²}Π_e + ∂_{ω²}Π_e see only the spatial pair block (R19-5 §1, confirmed in scope by vR19-5 item 3).
- Class 𝒢 (R19-5): pair and scattering kernels are independent law data. P-R19-5a, counted once.
- R18-9's root (vR18-9, O(q) convention) and R18-13's off-axis extension and own-direction data.
- Linearized W1 only. W2 (W15/T_pf) is not addressed.

**Removed hypothesis (`TESTS:7558`):** conservation only at O(q), for the photon.

## 2. Prior art (each counted once)

- **R19-5** (worker) + **vR19-5**: the outline (Sylvester inversion, shell division, continuum corner; `C5_R19-5_report.md:204-213`), P-R19-5a/b (`:276-283`), what would close (`:303-305`); referee item 4 (removable limits on coordinate planes must be implemented), item 6 (photon not built; corner values under-resolved).
- **R8-2 Construction A** (`C5_R8-2_report.md:73-92`): the dust kernel F⁰⁰u⊗u with telescoping divided differences, and pointwise gluing. My scattering block is this, for the two photon bands.
- **R13-5 Lemma P1** (`C5_R13-5_report.md:143-182`): pair-channel time components by division by ω₁ + ω₂.
- **R18-13**: VWa-geo, Lemma O (own-direction rows), Lemma C (body row), the N = 224 photon face rows (`arch18_13/photface_N224.out`).
- **R18-9 + vR18-9**: the axial root, Jacobian, retuned root (`vR18-9:13`), scope (`vR18-9:23`).
- **Textbook comparator:** the continuum Maxwell stress tensor is conserved only on shell and on the Gauss constraint surface (RECALLED; checked here numerically).
- **Grep.** `P/agents/*.md` and `TESTS.md` for "dust kernel", "Sylvester", "soft leg", "Gauss-law", "corner": only R8-2, R13-5, R19-5 and its item text. No prior numerical photon completion.

---

## 3. Results

### 3.1 (a) The exact photon stress (proved construction; checked)

**Pieces (lib199.py).**

- **M_C (corner).** T⁰⁰ = ½(E² + B²), T^{0j} = (E × B)_j, T^{ij} = −[E_iE_j + B_iB_j − ½δ_ij(E² + B²)], all fields at one point (c = 1, P = 1, u = 1). Used on U_r = {|k₁|, |k₂| < r}, r ≤ 0.2, where σ = k (box edge 2.94) and d(q) = q (|q_l| ≤ 2r ≤ 1). Exact there on the physical block: this is the continuum conservation law (comparator; checked 3e-15 / 6e-15 relative at r = 0.1 / 0.05).
- **M_B (both legs hard).** Channel split by the spectral projectors Π±(k) = (h² ± ωh)/2ω².
  - Scattering blocks, closed form (proved): with S± = ½Π±(k₁) I(k₁,k₂) Π±(k₂), g⁰ = 1, g^j = Δ_j/(ω₁ + ω₂), Δ_j = (σ_j(k₁)² − σ_j(k₂)²)/d(k₁_j − k₂_j):
    M⁰⁰ = S₊ + S₋, M^{0j} = g^j(S₊ − S₋), M^{ij} = g^ig^j(S₊ + S₋).
    Proof: Σ_j d_jg^j = (ω₁² − ω₂²)/(ω₁ + ω₂) = ω₁ − ω₂, which is λ₁ − λ₂ on the ++ block and −(λ₁ − λ₂) on the −− block; then both W1 equations hold identically. ∎
  - I(k₁,k₂) = diag(cos(s_a/2); Π_{b≠a}cos(s_b/2)), s = k₁ − k₂, is the fibre identification (site-averaged energy density). It equals 1 at s = 0 and carries the rotated frame's face twist. With I = 1 the kernel still satisfies W1 but jumps by O(1) across the BZ faces: it is not covariant under the twist. That is why I is needed (checked, `r199_fiber_check.out`).
  - Δ_j has a removable limit on the planes q_j = 0 (vR19-5 item 4); it is implemented (|q_j| < 1e-7: 2σσ′ at the midpoint).
  - Pair blocks: VW's spatial pair block Π±M_VWΠ∓ and P1: M^{0j}_{±∓} = ±Σ_i d_iM^{ij}/(ω₁ + ω₂), M⁰⁰_{±∓} = ±Σ_j d_jM^{0j}/(ω₁ + ω₂).
- **M_A (one soft leg).** M^{ij} = M_VW^{ij} in all channels. Time components by X = Σ_{λ₁,λ₂} Π_{λ₁}(k₁)RΠ_{λ₂}(k₂)/(λ₁ − λ₂), with λ₁ ∈ {±ω₁, 0} (full left) and λ₂ ∈ {±ω₂} if the left leg is soft (mirror otherwise). λ₁ − λ₂ ≠ 0 because the hard leg's ω exceeds the soft leg's on the support. Equivalently X = −Σ_n h(k₁)ⁿR(h₂⁺)ⁿ⁺¹, analytic in h(k₁) (proved: geometric series, ratio ω₁/ω₂ < ¼ on the support).
- **Glue.** M = χ_C M_C + (1 − χ_C)[φ_A(|k₁|)M_A^L + φ_A(|k₂|)M_A^R + (1 − φ_A(|k₁|) − φ_A(|k₂|))M_B].
  - χ_C = φ(|k₁|/r)φ(|k₂|/r), φ = 1 − sstep(2x − 1) (C^∞; 1 on [0, ½], 0 beyond 1); φ_A(x) = φ(8x/r).
  - Each piece is an exact solution on the support of its weight: M_A is off the shell there, since one leg is < r/8 and the other > r/2; M_B has both legs ≥ r/16. W1 is linear and pointwise, so the glued kernel is exact (R8-2 Lemma G).
  - Smoothness: C^∞ on the twisted torus², given C^∞ σ, c (G_w profiles), d and φ (proved by inspection). Hence quasi-local, with super-polynomial decay. That is the same locality class as VW itself, whose c = d′ is a C^∞, non-analytic profile.

**Checks** (`r199_exact_r0.1.out`, `r199_exact_r0.05.out`, `r199_dense.out`, `r199_exact_extra.out`, `r199_cov.out`):

| check | r = 0.1 | r = 0.05 |
|---|---|---|
| W1, 10 targeted families: uniform; near shell (\|ω₁−ω₂\| ~ 1e-9); forward incl. exact q_l = 0 planes; one soft leg each side; corner; corner on shell; annulus r/2..2r; mixed; near BZ faces | max rel 3.4e-14 (forward family; others ≤ 2.1e-14), max abs 6.5e-14 | max rel 3.4e-14, max abs 6.5e-14 |
| W1 dense: 10⁴ uniform pairs + 10⁴ pairs with log-uniform leg sizes 1e-6..π (all four pieces used) | ≤ 6.4e-16 rel, ≤ 2.2e-15 abs | ≤ 8.4e-16 rel, ≤ 1.8e-15 abs |
| μν symmetry / exchange Hermiticity (physical block) | 0 / 6.9e-16 | 0 / 6.9e-16 |
| reality: reflected-transposed M(−k₂,−k₁)ᵀ also satisfies W1 | 6.7e-15 | — |
| (H-E): P_T M⁰⁰(k,k) P_T = ½P_T, i.e. ∫T⁰⁰ = H | 3.9e-16 | 3.9e-16 |
| Lemma F forward scattering values (v_j, v_iv_j) | 3.3e-16 | 3.3e-16 |
| spatial pair block = VW(root a, w_d, w_o) where a leg is outside U_r; = continuum inside U_{r/2} | 8.0e-16; 0 | 6.1e-16; 0 |
| soft leg: eigen-sum = Neumann series | 4.4e-16 | — |
| soft leg: spread of the kernel over 6 directions at \|k₁\| = 1e-2, 1e-4, 1e-6, 1e-8 | 7.2e-3, 5.2e-5, 8.9e-7, 7.3e-9 (∝ \|k₁\|), against 0.6–0.9 for P_T(k₁) | — |
| BZ-face continuity (twist T_l), at 1e-7 / 1e-9 from the face | jump 2.1e-7 / 1.9e-9 (∝ gap) | same |
| cubic covariance, C₄z, C₃(111), C₂(110), half of the pairs in the corner region | ≤ 8.9e-16 | — |
| continuum piece W1 on the FULL 6×6 space (no Gauss projection) | relative residual 1.0 | — |

**Gauss-law bookkeeping at a single soft leg (proved; the item's request `TESTS:7556`).**
1. Physical fields obey σ(k)·Ẽ(k) = 0 (Gauss) and σ·B̃ ≡ 0. So T^{μν} depends on M only through P_T(k₁)MP_T(k₂), and M is defined modulo left- and right-longitudinal kernels (position space: terms ∝ ∇·E or ∇·B).
2. W1 is required, and holds, on the physical block. That is also the continuum standard: the Maxwell stress obeys ∂_μT^{μν} = 0 only when ∇·E = 0 (its full-space residual is O(1), last table row).
3. At a soft leg k₁ → 0 the projector P_T(k₁) has no limit, so no representative restricted to the physical block can be continuous there. The longitudinal-left freedom of item 1 is what removes this: on (full-left) ⊗ T₂, the Sylvester solution is the Neumann series −Σh₁ⁿR(h₂⁺)ⁿ⁺¹, analytic in h₁. Its limit at k₁ = 0 is −R h₂⁺, independent of direction (checked: spread ∝ |k₁|). Its physical block is the unique off-shell solution.
4. No obstruction arises: with the left leg's full spectrum {0, ±ω₁}, λ₁ − λ₂ ∈ {−λ₂, ±ω₁ − λ₂} ≠ 0 whenever ω₁ < ω₂. A single-soft-leg Gauss-law obstruction (the example class of PHOTON-OBSTRUCTED, `TESTS:7566`) therefore does not exist in this class (proved).
5. At k₁ = 0 exactly (measure zero; absent from the midpoint grids used): Ẽ(0) is a constant flux mode and B̃(0) = 0. There are no photon quanta there; the kernel value is the limit.

### 3.2 (b) Corner cost (proved form; checked value)

**Proposition K (proved).**
- In U_r the photon is continuum and the stencils P(s_l), u(s_l) depend on s = q only, with P = 1 − (λ/2)s² + …, u = 1 − (w/2)s² + …, λ = ¼ + 2a.
- So N_C − N_VW = q²N′ + O(q⁴) on pairs, N′ = −dN_VW/dq² at q = 0. At q = 0 nothing changes, so the ∂_{ω²} part is unchanged.
- Hence, per vector, exactly:
  δΞ_e(r) = −(1/(2π)³)∫d³k φ(|k|/r)² · 2tr(P N_C P N′ᵀ)/(2|k|) = C_e r⁴, with C_e = −I_φ ∫F_e dΩ/(2π)³.
  Here tr(P N_C P N′ᵀ) = |k|²F_e(k̂) (both amplitudes have degree 1), and I_φ = ∫₀¹x³φ² dx = 0.0644271 (a sharp ball would give ¼).
- F_e is a polynomial of degree ≤ 8 in k̂, so 40 × 80 Gauss–Legendre × trapezoid quadrature is exact. N′ comes from a 4-point difference that is exact for the cubic vertex. ∎
- C is exactly linear in (λ, w_d, w_o) and vanishes at the continuum point λ = 0, w = 0 (checked: 0.0).

**Values** (`r199_corner_rows.out`), per vector at the root data:

| row | C_e | d/da | d/dw_d | d/dw_o |
|---|---|---|---|---|
| T₂g = E_g = xz(q ∥ y) | +6.670790e-5 | −1.3056e-3 | 0 | 0 |
| face1 | +2.966678e-4 | −8.160e-4 | −1.632e-4 | −3.264e-4 |
| face2 | +1.609195e-4 | −6.528e-4 | 0 | −6.528e-4 |
| body | +3.129885e-4 | −5.803e-4 | −1.451e-4 | −5.803e-4 |

- The O_h relation (Lemma C) holds for the shift to 2.9e-18, and the C₄ control xz − T₂g to 1e-19.
- T₂g = E_g exactly. Suggested reason: on the axis the continuum kernel and the s_z-only multipliers are symmetric under rotation about z, and T₂g and E_g are related by a 45° rotation.
- The w-derivatives are in the ratio 1 : 2 : 4, which is Lemma O(iv) with E0 = T0.

**Sizes.**

| r | per vector T₂g, E_g / face1 / face2 | 12 vectors: T₂g, E_g / face1 / face2 |
|---|---|---|
| 0.05 | 4.17e-10 / 1.85e-9 / 1.01e-9 | 5.0e-9 / 2.2e-8 / 1.2e-8 |
| 0.1 | 6.67e-9 / 2.97e-8 / 1.61e-8 | 8.0e-8 / 3.6e-7 / 1.9e-7 |
| 0.2 | 1.07e-7 / 4.75e-7 / 2.58e-7 | 1.3e-6 / 5.7e-6 / 3.1e-6 |

**Grid validation** (R18-13's exact-shift Richardson, glued amplitude; `r199_corner_grid_N96.out`, `r199_corner_grid_N128.out`):

| r, N | T₂g grid / formula | face1 grid / formula | face2 grid / formula |
|---|---|---|---|
| 0.8, 96 | 2.7192e-5 / 2.7324e-5 (−0.5%) | 1.1968e-4 / 1.2152e-4 (−1.5%) | 6.4914e-5 / 6.5913e-5 (−1.5%) |
| 0.4, 96 | 1.6303e-6 / 1.7077e-6 (−4.5%) | 6.6327e-6 / 7.5947e-6 (−12.7%) | 3.5953e-6 / 4.1195e-6 (−12.7%) |
| 0.4, 128 | 1.6760e-6 / 1.7077e-6 (−1.9%) | 7.1660e-6 / 7.5947e-6 (−5.6%) | 3.8869e-6 / 4.1195e-6 (−5.6%) |

- The grid error falls by a factor of 2.2–2.4 from N = 96 to 128, toward the formula. At r ≤ 0.1 the grid cannot resolve the ball, which is why R19-5's cube values were only sizes (vR19-5 item 6). My values replace them.
- **Comparison with R19-5 (suggested).**
  - From Proposition K's integrand, a sharp ball of radius 0.1 gives 2.6e-8 (T₂g) and 1.15e-7 (face1) per vector (×¼/I_φ).
  - A sharp cube of half-width 0.1 gives about 2.45× more (the cube/ball ratio of ∫|k| d³k, ignoring the angular weight): about 6e-8 and 2.8e-7.
  - R19-5's cube values at N = 128 (3.5e-8, 8.7e-8; `arch9/r195_corner_N128.out`) are 2–3× low. That is consistent with about 4 grid points per side: right in order, under-resolved in value, as vR19-5 item 6 said.
- **The corner cost depends on the glue profile** only through I_φ·r⁴. Both are untuned law data.

### 3.3 (c) Re-solve of the 6-knob root (checked)

**Model** (`r199_resolve.py` docstring; every evaluator archived and unmodified):
- **Axial rows** T₂g, E_g, μ_E, μ_T₂: R18-9's `lib9`:
  - 4 real scalars, U;
  - 22.5 Dirac, UD at GL q = (4,10);
  - 12 vectors, with Ξ exactly quadratic in a, using full-precision N = 224 coefficients recomputed here (`r199_photquad_N224.out`, 295 s). The 7-digit header of `solve4k_N224.out` moved the ill-conditioned b_s direction by 1.6e-4 (`r199_resolve_rounded.out`).
  - The μ rows are SF of the bands only, so the corner does not enter them (proved).
- **Off-axis rows** face1, face2:
  - scalars: R17-4 `offaxis` (U, E1);
  - Dirac: R18-13 `dface` at GL(4,10);
  - photon: R18-13's N = 224 values at a₀ = −0.1760950036 (`photface_N224.out`), exactly linear in (w_d, w_o) (Lemma O(ii)), with an a-slope from N = 96 (`r199_facejac_N96.out`).
- **Exact-vertex corner:** +12·C_e(a, w_d, w_o)·r⁴ on T₂g, E_g, face1 and face2 (§3.2; exact in (a, w)).
- **Solver:** quasi-Newton with a fixed Jacobian.
  - J_axial is R18-9's `jac.py` rerun at the retuned root.
  - J_face,axial comes from central differences (`r199_facejac_N96.out`). It reproduces R17-4's U identity face2 ≡ T₂g in the b_s column: −5.6655e-4 against J_axial's −5.6655e-4.
  - The (w_d, w_o) block is 12 × R18-13's N = 224 w-derivatives, which are exact because the rows are linear in w (Lemma O(ii)).
  - det J = −3.73e-3; σ_min = 6.28e-4.

**Results** (`r199_resolve.out`):

| r | b_s | b_f | r_D | a | w_d | w_o | all six rows max\|·\| |
|---|---|---|---|---|---|---|---|
| 0 (O(q) convention, same model) | 2.5261507546 | 0.9091029701 | 0.5556036793 | −0.1760950036 | −1.1715542064 | −0.1954184345 | 9.3e-11 |
| 0.05 (exact vertex) | 2.5261509280 | 0.9091029843 | 0.5556036868 | −0.1760950040 | −1.1715542151 | −0.1954184361 | 3.3e-11 |
| 0.1 (exact vertex) | 2.5261536398 | 0.9091031976 | 0.5556037986 | −0.1760950112 | −1.1715543466 | −0.1954184593 | 3.1e-12 |
| 0.2 (exact vertex) | 2.5261980113 | 0.9091066163 | 0.5556055905 | −0.1760951257 | −1.1715564493 | −0.1954188303 | 3.8e-12 |

- **The r = 0 row is the O(q) root again.**
  - Its axial knobs equal R18-9's stored N = 224 root (2.5261507552, 0.9091029701, 0.5556036793, −0.1760950036; `arch18_9/solve4k_N224.out`) to 6e-10.
  - Its (w_d, w_o) equal R18-13's (−1.17155412, −0.19541845) to 1e-7.
  - At vR18-9's retuned point the same model gives axial residuals (9.2e-8, 7.5e-8, −1.695e-6, 1.0e-8). These match vR18-9's converged-quadrature residuals at the stored point with the opposite sign (`vR18-9:5-8`). So the two roots differ only by Dirac quadrature, and that difference moves b_s by 4.7e-5.
- **Shifts versus r = 0:**

  | r | Δ(b_s, b_f, r_D, a, w_d, w_o) |
  |---|---|
  | 0.05 | (1.73e-7, 1.42e-8, 7.43e-9, −4.8e-10, −8.76e-9, −1.55e-9) |
  | 0.1 | (2.885e-6, 2.275e-7, 1.192e-7, −7.63e-9, −1.402e-7, −2.474e-8) |
  | 0.2 | (4.73e-5, 3.65e-6, 1.91e-6, −1.22e-7, −2.24e-6, −3.96e-7) |

  - Linear response −J⁻¹δR gives, per unit r⁴, (2.97e-2, 2.28e-3, 1.20e-3, −7.64e-5, −1.40e-3, −2.47e-4) (`r199_linresp.out`). At r = 0.1 that is (2.97e-6, 2.28e-7, 1.20e-7, −7.6e-9, −1.40e-7, −2.47e-8).
  - It agrees with the Newton shifts to 3 digits for the other five knobs. For b_s it agrees to 3% at r = 0.1 and 7% at r = 0.05. Suggested causes: the fixed J was taken 4.7e-5 away along the ill-conditioned direction, and the μ_E evaluator's noise floor (±3e-10) puts a ~1e-8 floor on b_s.
- **Why b_s moves most.** The corner adds the same amount to T₂g and E_g, and the root's weakest direction (σ_min = 6.3e-4; `vR18-9:13`) is mostly b_s. The photon's own knob a moves by only 8e-9, because the corner acts on both axial rows equally and a moves them almost equally.
- **Other quadratures (suggested).** In vR18-9's converged-quadrature model the same linear response applies, because δR and J change negligibly. The exact-vertex root there is vR18-9's retuned root plus the Δ above.
- **Edges stay subluminal (checked, `r199_vmax.out`).** At every r the scalar whole-zone v_max is 0.999997446 (archived `ZLaw.vmax`, as R18-9 used), and the Dirac r_D stays < 1/√3 (Lemma V1). The photon edge is not a knob here. The Jacobian was not recomputed at the new points; with shifts ≤ 3e-6 its change is negligible (suggested).

**Direct check of the off-axis rows** (`r199_direct_r0.1.out`, `r199_direct_r0.out`). The photon face rows were evaluated directly with R18-13's `vwface.xi_geo` at N = 224, at the solved (a, w_d, w_o), with no linearization, plus scalars, Dirac and the corner:

| point | face1 total | face2 total |
|---|---|---|
| exact-vertex root, r = 0.1 | −1.847e-6 (vec −2.345112282e-2, corner +3.560e-7) | −4.437e-7 (vec −4.526232770e-2, corner +1.931e-7) |
| O(q) root, r = 0 | −1.847e-6 (vec −2.345073793e-2) | −4.437e-7 (vec −4.526210296e-2) |

- The two are identical to 4 digits. So the corner is fully absorbed by the knob shifts.
- What remains is the evaluator's own finite-q, w-quadratic artefact. R18-13 reported it at its solve (−5.9e-6, −3.0e-6, −1.7e-6 on face1 at N = 160, 192, 224; `C5_R18-13_report.md:61,280-282`). The referee accepted that level for ALL-ROWS-ZERO (`TESTS:7505-7517`).
- **Direct-evaluator solve (checked, `r199_direct_solve_r0.1.out`).**
  - One Newton step in (w_d, w_o) on the direct N = 224 face rows at the r = 0.1 exact-vertex root gives (w_d, w_o) = (−1.1715533772, −0.1954183954).
  - The direct face totals there are −2.7e-11 and −2.2e-11. The axial rows are unaffected (Lemma O(iii)), and the corner's w-dependence enters at ~1e-13.
  - So with every row evaluated directly, all six rows are zero to ≤ 3.3e-11 at r = 0.1.
  - Same at r = 0.05 (`r199_direct_solve_r0.05.out`): the direct face totals before the step are −1.847e-6 / −4.437e-7 (the same artefact). After the step to (w_d, w_o) = (−1.1715532457, −0.1954183722) they are −2.9e-12 / −4.8e-12.
  - This (w_d, w_o) step, 9.7e-7 and 6.4e-8, removes the N-dependent artefact; it is not a corner effect. The same step applies at r = 0.

**Rows at the final r = 0.1 exact-vertex point** (b_s, b_f, r_D, a) = (2.5261536398, 0.9091031976, 0.5556037986, −0.1760950112), (w_d, w_o) = (−1.1715533772, −0.1954183954):

| T₂g | E_g | μ_E | μ_T₂ | face1 | face2 | body |
|---|---|---|---|---|---|---|
| 3.3e-13 | 2.6e-13 | 3.1e-12 | 2.4e-16 | −2.7e-11 (direct) | −2.2e-11 (direct) | fixed by Lemma C. A direct evaluation carries the photon's finite-q O_h residual: R18-13 found −3.1e-5 total at N = 224 (−2.4e-6 per vector), falling with N (§3.4 there) |

- The axial values are from `r199_direct_r0.1.out:1`. The T₂g/E_g photon parts are exact in a at N = 224, and the corner is semi-analytic.

### 3.4 (d) Prices (named, not adopted)

- **P-R19-5a (count once; used).** The exact stress keeps VW's spatial **pair** block, but its scattering block is R8-2's dust kernel where both legs are hard, and VW's where one leg is soft. So the exact operator is not VW as one geometric operator: it is in class 𝒢 (independent pair and scattering law data). This is consistent with R19-5's correction of P-R18-13c. Lemma S does not bite, because the placement data live in the pair block only.
- **P-R19-5b (count once; now explicit).** The soft-corner continuum clause:
  - the photon stress equals the continuum Maxwell stress on U_r;
  - the glue (φ, r, and the soft-leg radius r/8) is untuned law data;
  - row cost exactly C_e·r⁴ (§3.2), absorbed by the six existing tunings (§3.3);
  - no new equality tuning.
  - Whether the corner clause is *necessary* (R19-5's "power-law tails otherwise") was not tested here.
- **R19-9 stipulations (new, row-irrelevant):**
  - (i) the fibre identification I(k₁,k₂) of the energy density in the scattering block. Any smooth, face-covariant I with I(k,k) = 1 works; mine is the site average.
  - (ii) exactness is on the Gauss-law block. This is a scope statement shared with the continuum, not a price.
- **Not paid here:** W2 (W15/T_pf; vR19-5 item 1 keeps W15 class-scoped), the seagull's Ward status, the LV tadpole, the CC, two loops, radiative stability, one law at both masses (m = 0.001 not run).
- **Axioms.** No axiom text changes. The stress is downstream source/action content (`AX:187`), and the photon and graviton dynamics are downstream of Admissibility (`AX:114-130`), under the qualification clause (`AX:85-90`). Cubic covariance uses only the proper rotations the Lattice axiom supplies (`AX:37-41`).

---

## 4. Against the FIXED readings (`TESTS:7564-7567`)

**Worker reading: PHOTON-EXACT** (unrefereed).

| reading | status |
|---|---|
| **PHOTON-EXACT** ("the exact photon completion is checked to ≤ 1e-12 and the SM root is re-solved with all rows zero. Checked.") | **Met.** W1 ≤ 6.5e-14 abs / 3.4e-14 rel over 10 targeted families and 4×10⁴ dense pairs at r = 0.1 and 0.05, including the corner, both soft legs, the shell, the forward diagonal with removable limits, and BZ faces (§3.1). Root re-solved with all six rows zero to the evaluators' noise floor (§3.3). |
| **PHOTON-OBSTRUCTED** | **Not supported.** An explicit completion exists; the example obstruction (single soft leg, Gauss law) does not occur (§3.1, item 4). |
| **OPEN** | Not needed. |

**Expectation (`TESTS:7568`), "PHOTON-EXACT with knob shifts ~1e-6": matched.** The largest shift is 2.9e-6 (b_s) at r = 0.1 and 1.7e-7 at r = 0.05; every other knob moves by ≤ 2.3e-7.

**Scope of the reading** (each inherited, not added):
- one loop, supplied vacuum, ultralocal seagull, SF μ rows (vR19-5 item 3; `vR18-9:23`);
- R18-13's VWa-geo off-axis extension and own-direction data, UD midpoint, U/E1;
- the campaign's finite-resolution evaluators (photon N = 224, Dirac GL(4,10), R17-4 scalar);
- m = 0.01 only;
- linearized W1 only.

## 5. Strong-word check

- **"Exact"**: an algebraic identity on the physical block, checked to ≤ 6.5e-14 at every sampled point. It holds at every point by construction (proved: each piece by explicit algebra, glue by linearity). The numerics confirm the implementation; they are not an enclosure.
- **"Over the torus"**: 10 targeted families plus 4×10⁴ random pairs, two radii. Not every point (impossible), but the identity is pointwise algebraic.
- **"Smooth" / "quasi-local"**: proved by inspection for C^∞ inputs. The numerics use the archived tabulated σ, c (interpolated), plus exact σ = k in the box.
- **"Re-solved"**: a quasi-Newton solve of the six rows in the stated evaluator model to its noise floor, plus a direct N = 224 check of the photon face rows. Not a converged-quadrature root. The model's absolute knob location carries the pre-existing quadrature ambiguity (§3.3), which is larger than the exact-vertex shift.
- **"Proved"** is used for: the dust-kernel scattering block, the Neumann-series smoothness at a soft leg, the no-obstruction statement, Proposition K (r⁴ form), the rotated-frame phase cancellation, and covariance by inspection. All are short arguments under the stated hypotheses.
- **Not claimed:** W2; uniqueness of the completion; necessity of the corner clause; anything at m = 0.001, two loops, or for the tadpole/CC rows; that VW as one geometric operator (class 𝒯) has an exact completion.

## 6. For the referee

1. The dust-kernel scattering block and its face-covariant fibre identification I (`lib199.piece_B`, `fiber_id`). Is I = site average an admissible energy-density placement? Any smooth covariant I with I(k,k) = 1 works for W1.
2. The rotated-frame reduction D → d (phases absorbed by R9-9's placement; lib199 docstring).
3. The Gauss-law scope: W1 on P_T·P_T, with the continuum's own full-space failure as comparator.
4. Proposition K and the grid convergence (N = 96 → 128).
5. The re-solve model (§3.3): fixed Jacobian, photon face a-slope from N = 96, and the direct N = 224 check.

## 7. Files (`S/`)

- `lib199.py`: the construction.
- `r199_exact.py` → `r199_exact_r0.1.out`, `r199_exact_r0.05.out`: all checks of §3.1.
- `r199_exact_extra.py` → `.out`: Gauss-law scope; reality.
- `r199_dense.py` → `r199_dense.out`: 4×10⁴ pairs.
- `r199_cov.py` → `.out`: cubic covariance.
- `dbg_wrap.py`, `dbg_wrap2.py` (diagnosis), `r199_fiber_check.py` → `.out`: with I = 1 the kernel satisfies W1 but jumps by 0.70 across BZ faces; with the site-averaged I the jump is 2.1e-9 at 1e-9 from the face.
- `r199_corner_rows.py` → `r199_corner_rows.out`, `r199_corner_grid_N96.out`, `r199_corner_grid_N128.out`; `corner_coeffs.npy`.
- `r199_facejac.py` → `r199_facejac_N96.out`, `facejac.npy`.
- `r199_jac_refroot.out`: R18-9 `jac.py` rerun.
- `r199_photquad.py` → `r199_photquad_N224.out`, `photquad_N224.npy`.
- `r199_resolve.py` → `r199_resolve.out` (full-precision coefficients), `r199_resolve_rounded.out` (7-digit header coefficients; produced by an earlier revision of the script, reproducible with `--rounded`); `resolve_sols.npy`.
- `r199_linresp.py` → `.out`.
- `r199_direct.py` → `r199_direct_r0.1.out`, `r199_direct_r0.out`; `r199_direct_solve.py` → `r199_direct_solve_r0.1.out` and `r199_direct_solve_r0.05.out`.
- `r199_vmax.py` → `.out`: edges stay subluminal.
