# Check x4: criteria (written 2026-10-27, before checks/x4_soft_noise.py exists)

Purpose: test the session-5 claims of EXISTENCE §14.1-14.2 on the free Gaussian soft chain (layer 1's Setting SC as a
measure): B_{i+1} = Q_root B_i + xi_i, xi_i white noise of variance sigma_i^2 per link, d = 4, L = 3, one real
component. All quantities exact (finite sums or exact linear algebra); no sampling. s := L^n.

Claims under test (derived in §14.2 before this check is run):
- (GS-1) Q_root - Q_str = -d h exactly, hence d Q_root = d Q_str (one step).
- (GS-2) after n straight blocking steps of unit white noise: block-link variance (2 s^-2 + s^-4)/3; block-plaquette
  variance (4/3)(2 s^-2 + s^-4); link-covariance symbol <= s^-2 at every coarse momentum; curvature-covariance symbol
  (max eigenvalue of the 6x6 plaquette-component matrix) <= 16 s^-2.
- (GS) the chain sum at fixed resolution m converges as K -> infinity.

**A (must hold; PASS criterion).** Fine torus (Z/9)^4, coarse (Z/3)^4. Implement the linearised S4' root map Q_root
literally (24 coordinate orders, 81 offsets, complete-axial contours, straight leg of L steps), the straight average
Q_str and the slice functional h. For 3 random fields A (seeded): max |Q_root A - (Q_str A - d h A)| <= 1e-12 and
max |d Q_root A - d Q_str A| <= 1e-12. A2 (informational, diagnostic for the gauge-variant (Q2)): the exact value of
Var(h xi)(X)/sigma^2 = ||c||^2 (c the coefficient vector of h at one site).

**B (must hold; PASS criterion).** Block-plaquette and block-link variance of Q_str^n applied to unit white noise:
(B1) position space, by iterating the one-step adjoint of Q_str on the dual vector of one coarse plaquette (resp. link),
n = 1, 2, coarse torus side 3 (fine sides 9, 27); (B2) exact finite Fourier alias sums, n = 1..8, coarse torus side 4.
PASS iff every value equals the closed form to relative error <= 1e-10. If B fails, §14.2's closed form is wrong and
must be corrected before any verdict.

**C (must hold; PASS criterion).** On the coarse momentum grid of side 16 (all 16^4 points) and n = 0..6: sup of the
link-covariance symbol <= s^-2 (1 + 1e-12), and sup of the max eigenvalue of the curvature-covariance symbol
<= 16 s^-2 (1 + 1e-12). Report s^2 * sup for both (informational: how sharp the bounds are).

**D (decides the test numerically; interpretation fixed now).** L = 3, kappa = 1. Two coupling sequences indexed by
resolution r = K - i: (D1) constant sigma^2 = 1; (D2) an (F)-type sequence 1/g_r^2 = 1/g^2 + b r log L with g^2 = 1,
b = 22/(48 pi^2) (any b > 0 would do), sigma_r^2 = g_r^2. For m in {0, 2, 5} and K = m+1..m+60, the noise part of the
block-plaquette variance N_K(m) = (4/3) sum_{n=0}^{K-m-1} sigma^2_{m+1+n} (2 L^-2n + L^-4n), computed (i) by this
formula and (ii) independently as sum_n sigma^2 * (B2 value for n) for n <= 8 plus the formula's tail; and the crude
operator-norm bound 16 sum_n sigma^2_{m+1+n} of session 4.
- **CONVERGES** iff N_K(m) is nondecreasing in K and N_{m+60}(m) - N_{m+30}(m) <= 1e-12 N_{m+60}(m) in every case.
- **DIVERGES** iff N_{m+60}(m) - N_{m+30}(m) > 1e-6 N_{m+60}(m) in some case; then T11 is FAIL at the free level.
- Report the crude bound's growth (expected: linear in K for D1, ~ log K for D2) to show what the session-4 recursion
  would have concluded.

Resources: one process, nice 10, OPENBLAS/OMP/MKL/VECLIB threads = 1, peak < 1 GB, numeric lock held, `uptime` load
< 8 and >= 25% memory free before starting. Output checks/x4_out.txt, record checks/x4_time.txt.
