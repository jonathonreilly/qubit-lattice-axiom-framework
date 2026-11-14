# ba3 criteria (written 2026-10-28 ≈06:34 UTC, BEFORE checks/ba3_rough.py exists; BFT_A §12, session 3 of lane A)

Purpose: tests of the exact identities and deterministic inequalities pre-stated in BFT_A §12 (Lemma RS, Lemma BR-1,
Lemma CR-1, Lemma TS, Lemma Λ, Lemma LR-pot) on real-space chains and finite-dimensional su(2) data. These are tests of
algebra, code and constants, not of any k-uniform estimate (k ≤ 2 only). Proposition SPD, Propositions/Theorems W,
Theorem G♯-rough and Theorem H-lin_inv are NOT tested by ba3.

Common: d = 4, L = 3, the S4' root map and chain matrices of checks/c26_led.py and the CG/LSMR code of checks/ba2_lin.py
(imported, read-only). Fixed seeds. Every CG solve must reach relative normal-equation residual ≤ 1e-10 (**R0**).

- **R1 (Lemma RS, Lemma BR-1)** k = 2, T = 2, κ ∈ {(1, 1), (0.5, 2)}. j := d_1^*ψ + c (ψ random level-1 2-form, c random
  constant 1-form); smooth part Pj := least-squares projection of j onto Q_1^T(C_2), C_2 spanned by d_2^*(level-2
  2-forms) and the 4 constant 1-forms; w := j - Pj.
  - R1a: ||d_1^*w||_∞ ≤ 1e-11||w||_∞; max over the spanning vectors a of |⟨w, Q_1^Ta⟩|/(||w||_2||Q_1^Ta||_2) ≤ 1e-10;
    |mean of w in each direction| ≤ 1e-11||w||_∞.
  - R1b: the component of Q_1w orthogonal to Ran d_2 (level-2 gradients) has norm ≤ 1e-9||Q_1w||_2.
  - R1c: direct CG with source w at level 1 and random data B_2, against CG with the level-0 source Q_0^Tw and data
    B_2 - Q_1w/κ_0: max relative deviations of r_0(x) - (r_0(y) - w/κ_0), r_1(x) - r_1(y), f_0(x) - f_0(y),
    f_1(x) - (f_1(y) + d_1w/κ_0), each relative to the max of the corresponding output of x, ≤ 1e-7.
  - Informational: ||Q_1w||_∞/||Q_1j||_∞, ||w||_∞/||j||_∞.
- **R2 (Lemma CR-1; the BCH sign)** su(2) ≅ (R³, ×) with the dot product (an ad-invariant form). Random real Q (12 × 30),
  x_l ∈ (R³)^30, x_{l+1} ∈ (R³)^12, κ = 0.7, r := Qx_l - x_{l+1}. For 50 random u: the commutator row
  -½κ⟨r, [u_{l+1}, Qx_l] + [x_{l+1}, Qu_l]⟩ against ⟨(κ/2)[x_{l+1}, r], Qu_l - u_{l+1}⟩: relative deviation ≤ 1e-12.
  BCH sign: for 20 random pairs of 2 × 2 anti-Hermitian traceless a, b of norm ≤ 1 and ε ∈ {1e-2, 1e-3},
  ||log(e^{-εa}e^{εb}) - ε(b - a) + ½ε²[a, b]|| ≤ 10ε³ (matrix commutator).
- **R3 (Lemma TS)** k = 2, T = 2, κ = (0.5, 2): CG with the residual source s_1 at step 1 and data B_2, against CG with no
  source and data B_2 + s_1/κ_1: the full configuration vectors (both CG runs start at 0) agree to ≤ 1e-9 relative.
- **R4 (Lemma Λ)** (T, k) ∈ {(3, 1), (2, 2)}; configurations: (a) a CG minimiser at random data, (b) Gaussian random
  x_0, (c) a smooth random x_0 (Gaussian random field convolved with a box filter of side 3 twice). Criterion:
  max_{X,μ}|Λ(X, μ) - (Q^{(0→k)}x_0)(X, μ)| ≤ 10·||f_0||_∞. Informational: the ratio to ||f_0||_∞.
- **R5 (Lemma LR-pot)** (T, k) ∈ {(3, 1), (4, 1)}; configurations (a), (b), (c) of R4 (x_1, …, x_{k-1} from x_0 and
  random residuals where needed; for k = 1 there are none). Px computed with the 24 axial orders.
  - R5a: Pλ(c_X) = 0 at every root (|·| ≤ 1e-12·max|Pλ|); P(Px) = Px to 1e-11 relative; Px - x_0 = d(Pλ) to 1e-12.
  - R5b: translation covariance: P(shift by one coarse unit in direction 1 of x_0) = shift(Px) to 1e-11 relative.
  - R5c: ||(Px)^c_0||_∞ ≤ 75||f_0||_∞ + 8·max|Λ| and ||(Px)^c_0||_∞ ≤ 155||f_0||_∞ + 8||B_k||_∞ + 40Σ_i||r^c_i||_∞
    (B_k := the data of (a); for (b), (c) B_k := Q^{(0→k)}x_0 - (residuals), i.e. any random residuals r_i with the data
    defined by the telescoping identity). Informational: the ratios to the bounds.
Resources: each part < 20 min, < 1 GB; numeric lock, nice 10, thread variables 1, python3 without -I, no timeout.
