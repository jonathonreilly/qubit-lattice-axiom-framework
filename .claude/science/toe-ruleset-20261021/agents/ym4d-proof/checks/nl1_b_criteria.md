# checks/nl1_b_criteria.md — pre-registered criteria for check nl1-b (re-run of nl1-D's clause under a new id)

Written 2026-10-28 after nl1-D was reported as a FAIL, BEFORE `checks/nl1_b_exactness.py` existed. The nl1 criteria,
script and output are untouched. Owner: the (N-loc) worker, session 24. Exact integer arithmetic, no lock.

## Why there is an nl1-b
nl1-D was pre-registered as "every T_α division is exact (zero remainder)". `checks/nl1_division.py`'s helper
`T(p, a)` performs synthetic division of p by (z_α − 1) and returns (quotient, remainder); it does NOT subtract
E_α p first. So its "remainder" is E_α p by construction, and the clause as written tested a property the lemma
never claims. nl1-D is reported as a FAIL. nl2 re-registers the clause the lemma actually asserts.

## What is being checked
Lemma NL-11's proof uses two divisibility facts:
  (E1) (g − E_α g) is divisible by (z_α − 1) with zero remainder, for every polynomial g;
  (E2) T_α(ν_1 g) = g exactly, and T_α(ν_β g) = ν_β T_α(g) exactly for β ≠ α (the two commutation steps of the proof
       of Lemma NL-11 step (1)).

## Verdicts, pre-registered
- **nl1b-A PASS** iff for all 200 random polynomials g (exponents in {0,1,2}, coefficients in [−4,4], d = 4) and every
  α, the synthetic division of (g − E_α g) by (z_α − 1) has zero remainder. Any nonzero remainder is a **FAIL**.
- **nl1b-B PASS** iff for all 200 random g and all α ≠ β: T_α(ν_α g) − g ≡ 0 and T_α(ν_β g) − ν_β T_α(g) ≡ 0 as
  polynomials. Any nonzero difference is a **FAIL**.
- **nl1b-C (designed-FAIL control) PASS** iff, for 200 random g, the synthetic division of g itself (without
  subtracting E_α g) by (z_α − 1) leaves a nonzero remainder in at least 150 cases — i.e. the subtraction in nl1b-A is
  doing real work and nl1b-A is not vacuous.
