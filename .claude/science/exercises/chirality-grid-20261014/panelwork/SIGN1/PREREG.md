# SIGN-1 pre-registration (written 2026-10-14 ~21:40Z, before any SIGN-1 script was run)

Item: TESTS.md "SIGN-1. Is the X2 corner-package Hamiltonian sign-free for QMC?" (packet branch
origin/claude/chirality-grid-exercise-20261014, TESTS.md:97-103). Readings there are FIXED and copied here
unchanged: **SIGN-FREE** (an explicit criterion proved to hold for the faithful model or a stated faithful
reduction, decomposition written out); **SIGN-PROBLEM** (proof that the known criteria fail for every
decomposition considered, or explicit negative/complex weights on a small cluster in a natural decomposition,
decompositions tried listed); **OPEN** otherwise. Memory cap 0.2 GB per run, one process, OMP_NUM_THREADS=2.

## Model (X2, COMBO_REPORT.md:55-70)
H = sum_a psi^dag sigma_a sin p_a psi + W sum_x Q(psi_S(x)), psi_S = F psi, F = f(p) x 1_2 x 1_16, f real and even
(f_NN or f_F1). Q = lambda1 sum_a B^a^dag B^a + lambda2 sum_a (B^a B^a + h.c.), B^a = psi_S^T (i sigma_y x N^a) psi_S,
N^a the symmetric 16x16 Spin(10) "C Gamma^a" (built here as N^a = Gamma^a_9 real symmetric for a <= 9, N^10 = i 1).
(lambda1, lambda2) are not fixed by X2; I scan the whole circle. lambda2 != 0 is required by X2 (U(1)_F must be
broken to Z4, COMBO_REPORT.md:80).

## Criteria and the necessary condition I test
Sufficient sign-free criteria (to be cited precisely after reading): Wu-Zhang Kramers positivity (number-conserving
decoupling, antiunitary T^2 = -1); Li-Jiang-Yao 2016 two fundamental classes: Majorana class {T1+, T2-} and Kramers
class {T1-, T2-}, anticommuting Majorana time reversals (MTRs); Wei-Wu-Li-Zhang-Xiang 2016 Majorana Kramers
positivity (S with T = SC, T^2 = -1, plus P) and Majorana reflection positivity (antilinear theta, theta^2 = 1, plus a
semidefinite cross kernel). Every one of these requires that every HS-decoupled H[phi] respect at least one fixed MTR
(a T- for all but MRP; a T+ for MRP). So the **necessary condition** tested is: an MTR Theta, the same for all
configurations, with each HS channel O_k Theta-even if its coefficient in H is attractive (real field) and Theta-odd if
repulsive (imaginary field).

## P1 (proof + check): which MTRs are possible at all
Claim to prove: (a) the filter (zero at hw1, nonzero at hw0, hw2, hw3) has both even- and odd-offset parts, so any
site-local Theta compatible with the filtered vertices is uniform in x; (b) a uniform MTR leaving the walker invariant
is number-conserving, Theta = (i sigma_y x V) K with V unitary, V^T = +V (T-) or -V (T+); (c) Theta-invariance of Q
forces V to implement an O(10) reflection with k odd flipped directions; T- iff k in {1,5,9}, T+ iff k in {3,7}.
Check: solve numerically for all real orthogonal O (64x64) anticommuting with the walker's flavour matrices.
**Expectation (mine):** (a)-(c) hold.

## P2 (LP over all on-site decompositions)
For each class k in {1, 3, 5} (k = 9, 7 equal k = 1, 3 under lambda2 -> -lambda2, covered by the scan), average over the
compact group H_k = SU(2)_spin x Spin(k) x Spin(10-k) x <Z4, Theta> that preserves Q and the parity classes. A feasible
decomposition exists iff an H_k-invariant one exists (convexity; to be proved in the report). If Lambda^2(R^64) is
multiplicity-free under H_k (checked numerically via Casimirs), the problem is an LP in one coefficient g_rho per irrep:
-(1/4) sum_rho g_rho Alt(P_rho) = q_Q, g_rho <= 0 on Theta-even irreps, >= 0 on Theta-odd irreps.
Equalities are imposed on a random sample of 4-index components; infeasibility on a subset is rigorous for the full
problem; any feasible solution is re-verified on many more components. Grid: 72 angles of (lambda1, lambda2).
Save Farkas certificates for infeasible cases (check y^T q < 0 and sign conditions numerically).
- **Reading P2-NONE:** infeasible for every k and every angle with lambda2 != 0.
- **Reading P2-SOME:** feasible for some (k, angle) with lambda2 != 0; then test the full sufficient condition (second
  anticommuting MTR / P / MRP semidefiniteness) for that decomposition.
**Expectation (mine):** P2-NONE (16 of Spin(10) is complex; the reflection splits the 10 into odd + odd parts).

## P3 (any Spin(10)-invariant Q)
Same LP with Spin(10) x SU(2) invariance imposed as linear constraints; ask whether any element of the cone has a
nonzero Delta F = 4 part. **Reading:** NONE-ANY (no Spin(10)-invariant Z4 quartic is sign-free by these criteria)
or SOME (name it).

## P4 (small-cluster weights, natural decomposition)
Cluster 4x1x1 torus (sin p_y = sin p_z = 0), f_NN restricted, 4 x 64 = 256 Majoranas. Natural decomposition: the
10-channel X^a = Re B^a, Y^a = Im B^a with real fields for attractive and imaginary fields for repulsive channels,
including the exact bilinear remainder. Weight w = +- sqrt(det(1 + prod_l e^{B_l})); for complex det the weight is
non-real; for real det the sign is fixed by analytic continuation along a complex path from phi = 0 (w(0) > 0).
Angles: lambda2/lambda1 in at least 3 regimes (both repulsive, mixed, both attractive). 40 random configurations each.
Control: Wu-Zhang density channel with the same walker and filter; expected all w > 0 to numerical precision.
- **Reading P4-NEG:** in some regime with lambda2 != 0, at least 10% of configurations have |Im w|/|w| > 1e-6 or w < 0
  (|w| above 1e-10 relative), with the control passing.
- **Reading P4-POS:** all weights real positive within 1e-8 relative in every regime.

## P5 (faithful reductions, only if P2-NONE)
(a) lambda2 = 0 (U(1)_F kept); (b) Spin(10) -> Spin(9) or Spin(5)^2 channel-reweighted quartics that are
Theta-compatible; (c) Spin(6)/SU(4) toy. For each: is it sign-free (full criterion), and what does it lose
(U(1)_F anomaly, G_SM invariance, mirror gapping).

## Decision rule for the FIXED readings
- SIGN-PROBLEM if P1 holds and P2-NONE (proof for every on-site decomposition with every site-local MTR), stated with the
  decompositions considered; P4-NEG adds the explicit cluster weights.
- SIGN-FREE only if a faithful model or stated faithful reduction passes a full sufficient criterion with the
  decomposition written out.
- OPEN otherwise (e.g. P2-SOME without a full criterion; P4-POS while P2-NONE).
Scope stated in advance: not covered are cross-vertex (non-on-site) HS channels, non-site-local Theta, and non-DQMC
methods (fermion bag, CT-INT, meron, Majorana-bag); the result is about the known criteria, not every algorithm.

## Follow-up A (dated 2026-10-14 21:50Z, after p1_p2_p3_lp.py ran; written before any pair-stage script)
Outcome so far: P1 as expected. P2 came out **P2-SOME** (single-MTR LP feasible at every angle for k = 1, 5 and 3),
contrary to my expectation. Reason to be stated in the report: a single MTR is only a necessary condition, and for
T+ it is vacuous (the even-minus-odd Casimir-type identity has zero quartic part). Also a measurement breach: that
run peaked at 615 MB RSS (261 MB footprint), above the 0.2 GB cap; it ran 60 s, single process, nothing else running.
Later runs use fewer samples and batching and are checked against the cap.

Per the P2-SOME branch I now test the full sufficient conditions, i.e. **pairs** of anticommuting MTRs
(LJY 2016 Kramers class {T-,T-}, Majorana class {T+,T-}). With T2 = Theta_1 (k = 1), every walker-compatible partner
is T1 = (1 x u) T2 with u in Z4 x Spin(10), u* = -u; up to the Spin(9) centraliser, u = i Gamma^A with |A| in
{0,1,2,3,4}. The channels must then commute with P = T1 T2 (a unitary on the 16), with T2-parity matched to sign.
- |A| = 0 (u = i, P = U(1)_F): Kramers class needs F-conserving channels; infeasible for lambda2 != 0 (proof in report).
- |A| = 1 (u = i Gamma^9, P generates the (9,10)-plane U(1)_c of Spin(10)): Kramers class. Test now by an explicit
  symmetry-adapted SDP (channels = U(1)_c-neutral bilinears, organised under SU(2) x Spin(8); four s/c doubled
  families get 2x2 blocks). 36 angles. Readings: **PAIR-FEASIBLE** (relative residual < 1e-7 at some angle with
  lambda2 != 0; then build the decomposition and check cluster weights are real >= 0 with Kramers pairing) or
  **PAIR-INFEASIBLE** (> 1e-4 at every angle with lambda2 != 0); else unclear.
- |A| = 2, 3, 4 and pairs built on T2 = Theta_5: tested if time allows; otherwise listed as not tested.
Decision rule unchanged: SIGN-FREE needs a full criterion with the decomposition written out; SIGN-PROBLEM needs every
considered decomposition/criterion to fail (or the TESTS.md cluster-weight clause, which I will report but, per my
decision rule above, not use alone to override an untested full-criterion class); otherwise OPEN.
