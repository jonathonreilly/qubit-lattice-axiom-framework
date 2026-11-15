# p3 criteria (lane E, session 3; written 2026-10-28 ~00:26 UTC, AFTER the §15.1-§15.5 derivations in PLD.md and BEFORE
checks/p3_pld.py exists)

Order disclosure: the statements tested here were derived first (PLD.md §15.1-§15.5); these criteria are fixed before
any script is written or run. No criterion is to be edited after the run; any change is disclosed in p3_time.txt.

Scope: elementary statements of session 3 only. Nothing here tests an SU(N) lattice measure, (SG), (SF), N5, (INF).

## A. Lemma TL (su(N)-valued logarithm), N = 2, 3, 4
Construct TL by the eigenvalue-shift recipe of Lemma TL's proof (principal log when ||1 - U||_op < 2 sin(π/N)).
Samples: 2000 Haar-random U per N (QR of complex Ginibre, phase-fixed, det normalised); all central elements ω·1
(ω^N = 1); for N = 2 the element -1; 200 near-central samples ω·exp(εH), H random traceless Hermitian, ε = 1e-6.
PASS iff for every sample:
- A1 ||exp(TL(U)) - U||_op ≤ 1e-10;
- A2 |tr TL(U)| ≤ 1e-10;
- A3 ||1 - U||_HS ≤ |TL(U)|_HS·(1 + 1e-12) + 1e-14, and ||1 - U||_op ≤ ||1 - U||_HS + 1e-14;
- A4 ||TL(U)||_op ≤ 3π + 1e-10;
- A5 on samples with ||1 - U||_op < 2 sin(π/N): TL(U) equals the principal log to 1e-10.
Negative control (must hold, else FAIL): A6 at every non-trivial central element the principal log has
|tr log U| ≥ 1 (it is 2π|m|), i.e. the unfixed definition is not su(N)-valued.

## B. Lemma HS-net and Proposition PLD-SG (i) against exact probabilities in a model satisfying the hypothesis
Model: X_p iid centred Gaussian on su(2) ≅ R³ with covariance σ²g²·1 (HS-orthonormal coordinates); it satisfies the
hypothesis of Lemma HS-net with m = 0 and any t_1. Exact P(|X_p| ≥ τ ∀p ∈ A) = (chi-3 survival at τ/(σg))^{|A|}.
Grid: σ ∈ {1, 2}, g ∈ {0.05, 0.1, 0.2}, τ/(σg) ∈ {0.5, 1, 2, 3, 5, 8}, |A| ∈ {1, 3, 10}.
- B1 PASS iff the HS-net bound (first form, δ = 1/2, m = 0: (5³e^{-(49/128)τ²/(σ²g²)})^{|A|}) ≥ exact in every case.
- B2 PASS iff the Gaussian-ξ Lemma HS bound ((2√2)³e^{-τ²/(4σ²g²)})^{|A|} ≥ exact in every case.
- B3 (net) PASS iff a greedy δ-separated set on S² (δ = 1/2) built from 20000 random points has ≤ 125 points and every
  one of 10⁵ fresh random unit vectors v has max_u⟨u, v⟩ ≥ 1 - δ²/2 = 0.875 for some net point (covering checked
  only to the sampling resolution; informational if the greedy set misses a covering by < 1e-3, disclosed).
- B4 Negative control (must FAIL the inequality somewhere, else the check is not discriminating): the bound
  (e^{-τ²/(2σ²g²)})^{|A|} (prefactor 1, the Gaussian one-dimensional exponent) is < exact for some case of the grid.
- B5 Remark G-IR (1) arithmetic: for a Gaussian with per-plaquette aligned variance v, log E e^{t⟨e,X⟩} = ½t²v|A| is
  verified by Monte Carlo (10⁵ samples, |A| = 5, equicorrelated covariance) to within 3 standard errors; and the
  threshold v* = σ²g² + 2mσ²g³/ε_1 is the exact crossing of ½t²v vs ½σ²g²t² + mgt at t = ε_1/(σ²g²) (algebraic, to 1e-12).

## C. Arithmetic used in §15 and in fix F-9
- C1 F-9: smallest N with 11N²/(6π²(N - 1)) > log(24·3⁴)/log 3 is N = 37 (PASS iff the computed value is 37).
- C2 F-9: report the smallest N with α t²β_1 > 6.8928 for α ∈ {1/(2N), 1/(2(N - 1))} at t = 1/2 and at t = 2/117
  (informational; PASS iff the t = 1/2 values lie in [550, 650] and the t = 2/117 values in [4·10⁵, 6·10⁵]).
- C3 F-1: sup_{x>0} x^{p/2}e^{-(a - a')x} = (p/(2e(a - a')))^{p/2}: numeric maximisation agrees to 1e-9 relative for
  p ∈ {3, 24, 192}, a - a' ∈ {0.01, 0.1, 1}.
- C4 INH: for L ∈ {3, 5}, c_1 = 1/(2(L² + 5.5·(3/2)L(L - 1))), every ε_1 on a 200-point grid of (0, 0.517] and every ε on
  a 200-point grid of [1.001L²c_1ε_1, ε_1): θ = 2arcsin(ε/2) < π/6 and 2 sin(θ/(2L²)) > c_1ε_1. PASS iff all hold.
- C5 Descent depth (informational): the least m with (L²/(2C_I))^m c_1 ≥ 2C_I/L² for C_I ∈ {1, 1.5, 2}, L = 3.
- C6 F-6: (2n_c + 1)⁴a > 3κε_♮ at n_c = 10¹³ for a down to 1e-40, κ ≤ 10, ε_♮ ≤ 0.007 (PASS iff it holds).

## Resources
Numeric lock (mkdir loop), nice 10, OPENBLAS/OMP/MKL/VECLIB threads 1, no `timeout`, python3 without -I; abort if
load ≥ 8 or free memory < 25%. Expected: < 60 s, < 300 MB.
