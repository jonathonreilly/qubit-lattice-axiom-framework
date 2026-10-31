# la55_2 — rigorous exact-rational check of the BCH plaquette tail used to certify BA-3's coefficient 9 (criteria first)
Written 2026-10-29 UTC before checks/la55_2_bch.py exists. Plain python, fractions.Fraction only; no floats in any verdict.

Claim to check (derived in LANEA55 §14): for a = (x_1, x_2, -x_3, -x_4), |x_i|_HS <= s, sigma := 4s, P = prod e^{a_i}, Y = P - I,
q_p := log P - sum a_i = Q_2 + R_3 with |Q_2| <= 6 s^2 and |R_3| <= f(sigma), where
  f(sigma) := (e^sigma - 1 - sigma - sigma^2/2) + sigma(e^sigma - 1 - sigma) + (1/2)(e^sigma - 1 - sigma)^2 + u^3/(3(1-u)),  u := e^sigma - 1.
f has nonnegative Taylor coefficients starting at sigma^3, so f(sigma)/sigma^2 is nondecreasing; hence it suffices to check one point.

Rigorous enclosure of e^x for rational 0 < x <= 1/2: E_lo = sum_{m=0}^{20} x^m/m!, E_up = E_lo + 2 x^21/21! (remainder <= x^21/21! * e^x <= 2x^21/21!).
Every term of f is nondecreasing in e^sigma (for u < 1), so f(sigma) <= F_up(sigma) := f evaluated with E_up.

PASS criteria (pre-registered):
- B1: F_up(1/10) <= 3*(1/40)^2, i.e. 6 s^2 + f(4s) <= 9 s^2 at s = 1/40. (Then by monotonicity for all s <= 1/40.)
- B2: u_up(1/10) < 1 (log series convergent in HS norm).
- B3 (sanity of the monotonicity claim, finite check): the Taylor coefficients of f up to degree 12, computed exactly by series
  arithmetic with Fraction coefficients, are all >= 0 and the coefficients of degree 0, 1, 2 are exactly 0.
- B4 (identity of the degree-2 part, exact, symbolic in noncommuting letters): the degree-2 part of log(prod e^{a_i}) equals
  (1/2) sum_{i<j} [a_i, a_j]; checked by expanding with words over 4 noncommuting letters as dicts word->Fraction.
- CONTROL-1 (designed to FAIL): F_lo(1/5) <= 3*(1/20)^2 (s = 1/20) — must FAIL (f too large there), proving B1 can fail.
- CONTROL-2 (designed to FAIL): coefficient 7 instead of 9 at s = 1/40 with a lower bound: 6 s^2 + F_lo(1/10) <= 7 s^2 must FAIL? NO —
  this would only show the *bound* exceeds 7, not the true value; it is reported as information, not as a control of the claim.
Exit non-zero if any of B1-B4 fails or CONTROL-1 does not fail.
