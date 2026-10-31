# checks/n1_criteria.md — pre-registered criteria for check n1 (exponent bookkeeping)

Written 2026-10-28 12:41 UTC, BEFORE `checks/n1_exponents.py` exists. Exact integer / Fraction arithmetic in plain
python, one process, no BLAS, no numeric lock (brief rule 6: exact symbolic/rational arithmetic does not need the lock).
No constant below is derived in this session: L, d, p_L, and the quoted K_p^♯ / K_ρ^♯ / Z_row / Z_col values are taken
from PROOF.md (c37 D2, c37 E2, REVIEW_S21 P/T) and the weights 2(k-l), (k-l) from RTARGET.md §33.

## What n1 checks
n1 is a bookkeeping check of the SCALING EXPONENTS of the composite (anti-circular) estimate of §N6 and of the per-level
estimate of §N5. It verifies the exponent algebra symbolically (as integers in the exponent of L) and evaluates the three
measured ratios. It is NOT a measurement of any kernel; no kernel is computed.

## Verdicts (pre-registered; a failure is reported as a FAIL and stops the corresponding claim)

- **n1-A (per-level exponent identity).** For general integer d ≥ 2 the per-level recursion exponent of §N5,
  e_per(d, θ_w, θ_A) := d − θ_w − 2 + 2θ_A, evaluated with (θ_w, θ_A) = (2, 1) must give e_per = d − 2 − 2 + 2 = d − 2;
  and the full per-level factor exponent, defined as E_per(d) := (d − 2) + (2 − d) = 0 at d = 4 when the measured
  excess factor L²K̄ is set to 1. Operationally: A_per(d) = c·L^{d−4} with c = (L²K̄)^a, a ∈ {1, 2, 3}.
  PASS iff the script reproduces: exponent d − 4 equals 0 at d = 4, −1 at d = 3, +1 at d = 5.
  FAIL otherwise.

- **n1-B (composite Wilson-term exponent).** With the three ingredient exponents
  (i) ℓ¹ mass of the level-0 curvature response to a level-k delta: (d − 2)k,
  (ii) sup of the level-0 potential response per unit level-k potential: −k,
  (iii) the same for the third leg: −k,
  the total exponent must be (d − 2)k − k − k = (d − 4)k. PASS iff the script gives (d − 4)k, i.e. 0 for d = 4.
  Also required: the two "swapped" orderings (the leg in the differentiated slot exchanged with a leg in an
  undifferentiated slot) must give the SAME total exponent (d − 4)k, from the ingredients
  (i′) ℓ¹ mass of the level-0 potential response to a level-k delta: (d − 1)k, (ii′) sup of the level-0 curvature
  response per unit level-k potential: −2k, (iii′) −k. PASS iff (d − 1)k − 2k − k = (d − 4)k.
  FAIL if the three orderings do not agree.

- **n1-C (composite soft-term exponent and summability).** With n := k − j ≥ 1 and the ingredient exponents
  (i) ℓ¹ mass of the level-j residual response to a level-k delta: d·n − 3(n − 1) = (d − 3)n + 3,
  (ii), (iii) sup of the level-j potential response: −n each,
  the total exponent must be (d − 5)n + 3. PASS iff the script gives (d − 5)n + 3 and iff the per-level ratio
  L^{d−5} is < 1 for d = 4, L ≥ 3 (i.e. the geometric sum over n ≥ 1 converges with ratio 1/L).
  The swapped ordering, with (i′) (d − 1)n, (ii′) −3(n − 1) − ... as in §N6, must give the same exponent (d − 5)n + 3.
  FAIL if the exponents differ or if the ratio is ≥ 1 at d = 4, L = 3.

- **n1-D (weight-invariance control for failure mode N-F2).** For arbitrary rational (θ_w, θ_A) the product
  A(θ_w, θ_A)^k × (the weight mismatch of the level-0 initial condition relative to the canonical weights (2, 1)) must be
  independent of (θ_w, θ_A). PASS iff the script verifies this identity symbolically in the exponent for at least the
  six pairs (θ_w, θ_A) ∈ {0, 1, 2} × {0, 1} and confirms the invariant value L^{(d−4)k}.
  FAIL if any pair breaks the invariance — which would mean the §N5 no-go argument is wrong.

- **n1-E (measured ratios; informational, no verdict).** Print L²K̄ for K̄ ∈ {0.1111…, 0.1138, 0.1154, 0.1202, 0.1236},
  Z_col·Z_row² for (Z_row, Z_col) = (2.849, 156.08), the ratio of the two, and L^d·K̄ and (2/3)K_ρ for
  K_ρ ∈ {2.074, 2.219, 2.614}. No PASS/FAIL attaches to these.

## Not success
A PASS on n1 is a check of the exponent algebra ONLY. It is not evidence for any kernel bound, for (H-K), for the
potential bound of §N3.6, or for the locality hypothesis (N-loc). No claim in NORMS.md may be upgraded on the strength of
n1.
