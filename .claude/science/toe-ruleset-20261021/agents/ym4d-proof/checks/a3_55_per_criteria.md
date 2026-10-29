# a3_55_per — pre-registered criteria (written before the script exists)

Worker: Opus 5.5 (claude-opus-5-5), ALIGN3_55 §1 (item (1): periodic harmonic/path repair by the method of images).
Arithmetic: python Fractions/ints only, `python3 -I -B`, stdout only (redirected by the shell to a3_55_per_out.txt). No floats in any verdict.
One run is the record. No criterion is edited after the script exists; any amendment is appended with a timestamp and reason before the script exists.

## Part I — 1D periodic cubic spline, L = 3, P ∈ {3, 5, 9} coarse knots (N = 3P fine sites)
Exact periodic spline weights a^per(y, J) from the circulant (1,4,1)/6 system; image first moments m_1(y, J) := Σ_n n·a^∞(y/3, J + nP)
computed as d/dz at z = 1 of the Floquet-twisted (c_{m+P} = z c_m) interpolation (exact derivative of the inverse matrix).
- **I0 (reproduction of Codex ALIGN2 F5, independent arithmetic).** Merged single (shortest) path per periodic node, constant 1-form 1, fine y = 1:
  P = 3 gives exactly −8/9; P = 5 gives exactly 40/99 and the weight row (238/297, 113/297, −10/99, 2/33, −14/99); P = 9 gives the weight row
  (1102, 521, −126, 34, −10, 6, −14, 50, −186)/1377 and a value v ≠ 0 with 1377·v − 3960 ∈ 27ℤ. PASS iff all hold.
- **I1 (images kill constants).** M^img(1)(y) := Σ_J[a^per(y,J)(y − 3J) − 3P·m_1(y,J)] = 0 for every fine y and every P ∈ {3,5,9}. PASS iff all zero.
- **I2 (left inverse).** M^img∘d = 1 − S_0R exactly as N×N matrices (M^img x(y) := Σ_J[a^per(y,J)I_0(J→y)(x) − m_1(y,J)Σx], I_0 the lifted
  path from 3J to y without wrapping), every P. PASS iff exact.
- **I3 (1D completion identity).** dM^img − 1 + S_1B = 0 exactly on all fine 1-forms (B = sum of the 3 fine links of a coarse link;
  S_1w := d S_0 g + (mean w)/3 with w = dg + mean), every P. PASS iff exact.
- **I4 (PER-2 (d)).** M^img = M^merged∘(1 − h) exactly (h = mean), every P. PASS iff exact.
- Controls (each must FIRE, i.e. the stated failure must occur): **CI1** dM^merged − 1 + S_1B ≠ 0 for every P (the merged operator fails the
  identity, Codex F5/F10); **CI2** the n = 0-path operator M^(0) (no image moment term) has M^(0)(1) ≠ 0 for some y, every P.

## Part II — d = 2, s3 (ternary 4-point Deslauriers–Dubuc, the table of a2_55_lp.py), image construction, exact
Models: coarse torus side T ∈ {3, 5}; level-1 side 3T, level-0 side 9T; k = 2. At T = 3 the level-1 → level-2 stencil wraps (3 coarse knots per
direction, offsets −1..2). B = 2D order-paired centred contour average (σ ∈ {(0,1),(1,0)}, y ∈ c + {−1,0,1}², contour P^σ(c→y)·S_y·P^σ(c′→y+3e_μ)^†).
S_1 = derived s3 mask in direction μ ⊗ s3 in the other direction (summation by parts of the fine differences).
- **II1.** At both levels of both models: M^img(const_ν) = 0 (ν = 0,1) and M^img∘d0 = 1 − S_0R (random rational functions, 3 seeds, plus all
  basis functions at level 1). PASS iff exact.
- **II2.** B∘d0 = d0∘R and d0∘S_0 = S_1∘d0 (all basis functions at level 1 of both models; random at level 0), S_1B(const) = const. PASS iff exact.
- **II3 (PER-3).** On ℤ² (no torus): for one link b of each of the 18 classes mod 3ℤ² the row Z_b of E^∞ = d0M^∞ − 1 + S_1^∞B^∞ satisfies ∂Z_b = 0;
  the cumulative-sum 2-chain F_b satisfies ∂F_b = Z_b with finite support; then on each torus level (T = 3: sides 9 and 27; T = 5: side 15) the
  torus matrix E_torus := d0·M^img − I + S_1·B (built from the torus operators, independently of Z_b) equals Ñ^per·d1 exactly, Ñ^per the
  periodisation of the F_b table. PASS iff ∂Z_b = 0 for all 18, ∂F_b = Z_b, and E_torus = Ñ^per d1 entrywise at all three tori.
- **II4 (PER-4, hierarchical).** Model T = 3, k = 2, l ∈ {0, 1}, 3 seeds: ⟨w, dλ_l⟩ (λ = Λ^img x) equals −⟨w, x_l⟩ + Σ_{m=l}^{1}⟨w_{m+1}, Bx_m − x_{m+1}⟩
  − Σ_{m=l}^{1}⟨Ñ_m^Tw_m, d1x_m⟩ (x_2 = 0, w_{m+1} = S_1^Tw_m). PASS iff exact for all.
- Controls (must FIRE): **CF1** merged-path M (one shortest path per periodic node) at level 1 of T = 3: M^merged(const) ≠ 0; **CF2** E^merged :=
  d0M^merged − I + S_1B at level 1 of T = 3 has E^merged(const) ≠ 0 (so no Ñ with E = Ñd exists); **CF3** II4 with the Ñ term dropped fails
  for at least one seed; **CF4** with S_1 replaced by the non-derived s3⊗s3 on links, ∂Z_b ≠ 0 for some class.

## Part III — CEN2 core (the quadratic cancellation LA-pol rests on), exact in a nilpotent algebra
4×4 strictly upper-triangular rational matrices A_0, A_1 (fixed small integers, 2 seeds); constant 2D fields; order-paired centred contours of
the coarse 0-link from c = (0,0) to c′ = (3,0); M̄(t) := avg of contour transporters for the field tA; log M̄(t) = c_1t + c_2t² + c_3t³ exactly.
- **III1.** c_1 = 3A_0 and c_2 = 0. **III2.** For V = tV_1 (V_1 a further fixed strictly upper-triangular matrix), the t²-coefficient of
  log(e^{−V}M̄(t)) equals −½[V_1, c_1 − V_1] exactly, and is 0 when V_1 = c_1. PASS iff all exact.
- Controls (must FIRE): **CIII1** lower-corner offsets {0,1,2}² give c_2 ≠ 0; **CIII2** a single contour (σ = (0,1), y = (1,1)) gives c_2 ≠ 0.

## Overall
OVERALL PASS iff I0-I4, II1-II4, III1-III2 all PASS and all controls CI1, CI2, CF1-CF4, CIII1, CIII2 FIRE. Otherwise OVERALL FAIL (recorded as such).

## What this check cannot decide (stated before running)
d = 4 (only d = 1, 2 are run); any norm bound or the k-, T-uniform size of A_Ñ, C_D, C_𝒞; the spline in d ≥ 2 (only d = 1); the polarised
inequality of LA-pol (only the exact vanishing of the constant–constant quadratic term); su(N) beyond the universal nilpotent algebra; the
nonlinear W_0 projection (only log of the average); weighted norms.
