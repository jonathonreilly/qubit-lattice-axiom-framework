# ns55_2 — criteria (written before the script; NSL55.md, Opus 5.5, claude-opus-5-5)

Written (UTC) 2026-10-29, before `ns55_2_bch.py` exists.

## What is checked
NSL55 Lemma B rests on the algebraic structure of the one-link remainder of the nonlinear gauge action,
  F(u, a, β) := log(e^u e^a e^{-u-β}) - a + β,
(x^{e^ξ})(b) = x(b) - dξ(b) + F(ξ(b^-), x(b), dξ(b)) in the convention U(b) -> g(b^-)U(b)g(b^+)^{-1}, g = e^ξ.
Claims: (D1) no terms of degree 0 or 1; (D2) every word contains u or β (F(0, a, 0) = 0); (D3) every word contains at least
two distinct letters (F vanishes when any two arguments vanish); (D4) the degree-2 part is [u,a] - ½[u,β] - ½[a,β];
(D5) every word without u contains both a and β (so h^{-1}F(0, ha, hβ) = O(h)).
These are proved by hand in the text (one line each for D2, D3, D5; D4 by second-order BCH). The check is an independent
exact computation in the free associative algebra, truncated at total degree 4.

## Method
Noncommutative polynomials over Fraction (dict: word tuple -> coefficient) in letters u, a, b (b = β), truncated at degree 4.
exp(X) = Σ_{n≤4} X^n/n!, log(1 + Y) = Σ_{n≤4} (-1)^{n+1} Y^n/n. Plain python, `python3 -I`, exact.

## PASS / FAIL (pre-registered)
- D1-D5 as stated, each tested on every word of degree ≤ 4 with nonzero coefficient. FAIL if any word violates.
- D4 exact: the degree-2 part must equal ua - au - ½(ub - bu) - ½(ab - ba) word by word.
- Control D6 (designed-FAIL): G := log(e^u e^a e^{-u-β}) - a (the +β omitted) must FAIL D1 (it has the degree-1 term -β).
  If G passes D1 the check is broken.
- Control D7 (algebra sanity): log(e^X e^{-X}) must vanish identically to degree 4 for X = u + a (tests exp/log code).
- Overall verdict PASS iff D1-D5 hold for F, D6 fails D1 as designed, and D7 holds.
