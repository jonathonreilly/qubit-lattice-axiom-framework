# sa55_hm — pre-registered criteria (written before the script; SRCAN55.md §3.2, Lemma SA-TC)

Written 2026-10-29 (UTC, before `sa55_hm.py` exists). Exact rational arithmetic only (`fractions.Fraction`); no floats in
any verdict. Decimal displays are rounded OUTWARD (floor for lower endpoints, ceil for upper endpoints).

## What is checked and why
Lemma SA-TC rests on three elementary facts. A wrong constant in any of them would change the stated rate fraction
ω_hm(r) or the Cauchy prefactor.

- **C1 (polarisation identity).** For p = 1..5, three random symmetric p-linear forms T on Q^p, with integer entries in
  [−9, 9] (fixed seeds): T(e_1, …, e_p) == (2^p p!)^{−1} Σ_{ε∈{±1}^p} (Π_i ε_i) T(v_ε, …, v_ε), v_ε := Σ_i ε_i e_i.
  - PASS iff all 15 equalities hold exactly.
  - **Control C1-ctrl (must FIRE):** the same with the normaliser (2^p)^{−1} (p! omitted) must be unequal for at least one
    form at every p ≥ 2.
- **C2 (the constant ω_hm(1/2) = 1 − (4/π)arctan(1/2)).**
  - Rigorous rational enclosures: arctan by alternating-series brackets; π by Machin, π = 16 arctan(1/5) − 4 arctan(1/239),
    with the brackets combined outward.
  - PASS iff the enclosure of ω_hm(1/2) lies inside [0.4096, 0.4098] and has width < 10^{−6}.
  - **Control C2-ctrl (must FIRE):** the claim "ω_hm(1/2) ≥ 1/2" must be rejected (upper endpoint < 1/2).
  - Informational, no verdict: enclosures of ω_hm(1/4) and ω_hm(1/10).
- **C3 (argument identity and monotonicity).** For r ∈ {1/2, 1/4, 1/10} and rational unit vectors
  (cos θ, sin θ) = ((1 − u²)/(1 + u²), 2u/(1 + u²)), u ∈ {1/7, 1/3, 1/2, 2/3, 1, 3/2, 2, 3, 7}:
  τ := r(cos θ + i sin θ), w := (1 + τ)/(1 − τ).
  - (C3a) Re w = (1 − r²)/|1 − τ|² and Im w = 2r sin θ/|1 − τ|², exactly.
  - (C3b) Re w > 0.
  - (C3c) the maximum of Im w/Re w over the sampled u is attained at u = 1 (θ = π/2) and equals 2r/(1 − r²), which is
    tan(2 arctan r).
  - PASS iff (C3a)-(C3c) hold for all 27 samples.
  - **Control C3-ctrl (must FIRE):** the wrong formula Im w/Re w = 2r sin θ/(1 + r²) must fail on at least one sample.

## Overall verdict
VERDICT: PASS iff C1, C2 and C3 all pass and all three controls fire. Anything else: VERDICT: FAIL, printed with the failing
item. The script writes nothing except its stdout, which is captured to `sa55_hm_out.txt`.

## What this check cannot decide
It does not test the two-constants theorem itself, which is the maximum principle for subharmonic functions; nor Lemma SA-TC's
use of it; nor any Yang–Mills statement. It certifies the polarisation normaliser, the value of ω_hm(1/2), and the closed form
of the harmonic measure's argument on the circle.
