# b4w55_1 — criteria (pre-registered; written before any b4w55 script exists)

Owner of this check: BFT4W55.md (Opus 5.5 worker, model claude-opus-5-5). Exact rational arithmetic (fractions.Fraction),
plain python, no floats in any verdict, no numpy/BLAS. Script: checks/b4w55_1_cen1.py (to be written after this file).
Output: checks/b4w55_1.out. One run; the verdict printed by that run is the verdict recorded.

## Model (what is built)
- Dimension d ∈ {2, 3}; L = 3; one root step l → l+1 on a periodic level-l lattice of side L·T_c, T_c = 4 coarse sites.
- Block of a level-(l+1) site X: B(X) = {LX + v : v ∈ {0,…,L−1}^d}; centre c_X = LX + ((L−1)/2)·𝟙.
- Linear root map Q (the linearisation used in BFT_A BL-2 (b): Q = Q_str − d∘h): for the coarse link c = (X, μ),
  (Qx)(c) = avg over axis orders σ (all d! orders) and y ∈ B(X) of the signed sum of x over the contour
  c_X → y (axial path, axes in order σ) → y + L e_μ (straight) → c_X + L e_μ (the go path translated by L e_μ, reversed).
  Weights w_{c,a} := coefficient of x(a) in (Qx)(c), exact rationals. Unwrapped displacements δ_{c,a} := m_a − m_c are
  recorded from the contour geometry (no torus wrapping occurs: contour extent ≤ 2L < L·T_c).
- Positions. **Centred convention (C):** level-l link a = (z, ν) at m_a = z + ½e_ν; coarse link c = (X, μ) at
  m_c = c_X + (L/2)e_μ. **Corner convention (K):** m_c^K = LX + (L/2)e_μ (level-(l+1) sites at the lower block corner).
- Commutator: [Q, ψ]x(c) := Σ_a w_{c,a}(ψ(m_a) − ψ(m_c))x(a) (ψ evaluated through the recorded δ_{c,a}).

## Pre-registered properties (each PASS/FAIL; the overall verdict is PASS iff all P-gates pass and all K-controls fire)
- **P1 (CEN1, exact, convention C).** For every coarse link c, every direction ν and every link direction μ′:
  Σ_{a: dir(a)=μ′} w_{c,a}(δ_{c,a})_ν = 0 exactly. (Equivalently [Q, ψ]x = 0 for every affine ψ and every
  direction-constant x.) FAIL if any of these numbers is nonzero.
- **P2 (CEN1 Taylor bound, convention C).** For 3 seeds, quadratic ψ(p) = pᵀCp + b·p (random rational C symmetric, b) and
  random rational x: for every c, |[Q, ψ]x(c)| ≤ Σ_a |w_{c,a}|·(|∇ψ(m_c)|_∞·|δ_{c,a}|_1·D_N(c)·g + |C|_max·|δ_{c,a}|_1²·|x|_∞),
  with g := max over links b and axes ν of |x(b + e_ν) − x(b)|, D_N(c) := max ℓ¹ distance between base points of two
  same-direction links in the support of w_{c,·}, |C|_max the largest entry modulus. FAIL if violated anywhere.
  (Disclosed: P2 follows from P1 and the triangle inequality; it tests the implementation of the decomposition, not new
  mathematics.)
- **P3 (exact commutator representation, any convention).** Energy 𝓑(u, x) := Σ_p du(p)dx(p) + κ Σ_c r(u)(c) r(x)(c) with
  r(x) := Q x_l − x_{l+1} (level-l plaquettes p; level-(l+1) unknowns x_{l+1}(c)); cutoff action (ψx)_l(a) = ψ_a x_l(a),
  (ψx)_{l+1}(c) = ψ_c x_{l+1}(c), with ψ_a, ψ_c, ψ_p independent random rationals. Claim, exactly, for 3 seeds and random
  rational u, x, κ: 𝓑(ψu, x) − 𝓑(u, ψx) = Σ_p G(p)dx(p) + Σ_b j_W(b)x_l(b) + Σ_c s(c) r(x)(c) + Σ_a j_S(a)x_l(a), where
  G(p) := Σ_{b∈∂p} ε_{p,b}(ψ_b − ψ_p)u_l(b), j_W(b) := −Σ_{p∋b} ε_{p,b}(ψ_b − ψ_p)du(p), s(c) := κ([Q,ψ]u_l)(c) with
  [Q,ψ]v(c) := Σ_a w_{c,a}(ψ_a − ψ_c)v(a), j_S(a) := −κ Σ_c w_{c,a}(ψ_a − ψ_c) r(u)(c). FAIL on any mismatch.
- **P4 (convention K leaves an uncancelled term, exact).** For every coarse link c = (X, μ), affine ψ with gradient b and
  direction-constant x: [Q, ψ]_K x(c) = (b·((L−1)/2)𝟙)·L·x̄_μ exactly, where [Q, ψ]_K uses m_c^K; and it is nonzero for the
  chosen b, x̄ (b·𝟙 ≠ 0, x̄_μ ≠ 0). FAIL if the identity fails or the value is zero.
- **P5 (row/column/reach constants used in BFT4W55 §4).** max_c Σ_a|w_{c,a}| ≤ L + d(L−1); max_a Σ_c|w_{c,a}| ≤ 2d + L^{1−d};
  max_{c,a}|δ_{c,a}|_1 ≤ d(L−1)/2 + L/2 (convention C). FAIL if any is exceeded. (These test the d = 2, 3 cases of the
  counting arguments; d = 4 is not run.)

## Designed controls (each must FIRE, i.e. make its property fail; a control that does not fire makes the run FAIL)
- **K1 (no centring).** Replace y ∈ B(X) by y ∈ B(X) + e_0 (contours still from c_X): P1 must fail.
- **K2 (corner convention in P1).** Run the P1 test with m_c^K: P1 must fail.
- **K3 (drop j_S).** Omit the j_S term in P3: P3 must fail.
- **K4 (one perturbed weight).** Add 1/997 to one nonzero w_{c,a} in the P1 test: P1 must fail.

## What this check cannot decide (stated before the run)
Nothing about k-uniformity, d = 4, the nonlinear S4' contours (only the linearised Q), norms of 𝔐^{(σ)}/N^{(σ)}, the
Wilson nonlinearity, or any analytic estimate. It decides only the exact algebra of the centring cancellation, its
dependence on the position convention, the commutator representation, and three combinatorial constants in d = 2, 3.
