# tq55_a — criteria (written 2026-10-29, BEFORE tq55_a.py exists)

Owner: TQ55.md (Opus 5.5 worker, model claude-opus-5-5). Exact rational polynomial arithmetic, plain python
(`fractions` only; no floats, no sympy, no numpy).

## Question decided
Can conservation and symmetry of the stress tensor ALONE force the angular-momentum flux (ROTDEF's TQ) to vanish?
Claim to be tested: NO. In R^4 the "rotlet"
    sigma_{mu nu}(x) = (M_{mu a} x_a x_nu + M_{nu a} x_a x_mu) / |x|^6,   M antisymmetric,
is symmetric, homogeneous of degree -4, divergence-free on R^4 \ {0}, and carries angular-momentum flux
    Phi_J := \int_{S^3} n_mu sigma_{mu nu}(n) (Jn)_nu dOmega = (|S^3|/4) sum_{ab} M_{ab} J_{ab},
nonzero for M = J. Contrast: identically-conserved improvement tensors (d_mu d_nu - delta_{mu nu} Laplacian) Phi carry zero flux.

## Method
Functions are pairs (polynomial P with Fraction coefficients, k) meaning P(x)/|x|^k. Derivative:
d_mu (P |x|^-k) = [ (d_mu P)|x|^2 - k x_mu P ] / |x|^(k+2). Divergence-free <=> the numerator polynomial is identically 0.
Sphere integrals: exact normalized monomial moments on S^{d-1},
<prod n_i^(2k_i)> = prod_i [Gamma(k_i+1/2)/Gamma(1/2)] * Gamma(d/2)/Gamma(K+d/2), K = sum k_i, odd moments 0,
with Gamma(k+1/2)/Gamma(1/2) = (2k-1)!!/2^k (exact rationals). Flux reported as Phi_J/|S^3| (exact rational).

## PASS (all must hold)
- P0 (moment routine self-test, can fail): d=4: <n1^2> = 1/4, <n1^4> = 1/8, <n1^2 n2^2> = 1/24, and
  sum_i <n_i^4> + sum_{i!=j} <n_i^2 n_j^2> = 1 (= <|n|^4>).
- P1: for each of the 6 basis antisymmetric M = E_ab - E_ba (a<b), sigma is symmetric (exact) and all 4 divergence
  numerators vanish identically.
- P2: homogeneity: numerator polynomial of sigma is homogeneous of degree 2 and k = 6 (degree -4).
- P3: for M = J = E_12 - E_21: Phi_J/|S^3| = 1/2 exactly (= sum M_ab J_ab / 4 = 2/4).
- P4: for M = E_12 - E_21, J = E_34 - E_43: Phi_J/|S^3| = 0 exactly (orthogonal planes).
- P5 (improvement carries no flux): Delta = (d d - delta Lap) Phi for Phi = |x|^-2 and for Phi = x1 x2 |x|^-4
  (non-radial): divergence numerators vanish identically AND Phi_J/|S^3| = 0 for J = E_12 - E_21 and J = E_13 - E_31.

## Controls that MUST FIRE (each must give a NONZERO result; if any gives zero the check FAILS)
- C1: same sigma in R^4 with |x|^-5 or |x|^-7 instead of |x|^-6: some divergence numerator nonzero.
- C2: the R^3 analogue with |x|^-6 (d_mu x_mu = 3): some divergence numerator nonzero.
- C3: the antisymmetric combination (M_{mu a}x_a x_nu - M_{nu a}x_a x_mu)/|x|^6: some divergence numerator nonzero.
- C4: P3's flux with M = J replaced by a non-zero sigma built from M = E_12 - E_21 evaluated with J = E_12 - E_21
  but WITHOUT the second (nu<->mu) term of sigma: the result must differ from 1/2 (shows P3 is not automatic).

## FAIL
Any P fails, or any control returns zero / the PASS value. Output goes to tq55_a_out.txt verbatim.
