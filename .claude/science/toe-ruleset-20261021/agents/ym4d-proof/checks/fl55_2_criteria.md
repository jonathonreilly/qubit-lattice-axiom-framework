# fl55_2 criteria — value-function (envelope) jets, exact (written before any fl55_2 script)

Owner: FLOW55.md (worker claude-opus-5-5). Script: checks/fl55_2.py, written AFTER this file. Plain python 3 + sympy exact
rationals; no numpy, no floats in any verdict. nice 10. Output: checks/fl55_2_out.txt, checks/fl55_2_err.txt.

## Statement under test (FLOW55 Lemma ENV; FLOW §31 Lemma TOW (5); REVIEW55_NORMS r55n-A1)
Let f(U, V) be a polynomial on R^m × R^d with f(0,0) = 0, ∇f(0,0) = 0, A := f_UU(0,0) positive definite. Let U*(V) be the
critical point of f(·, V) near 0 (power series in V) and W(V) := f(U*(V), V). With ζv := (U*′(0)v, v):
- (E3) D³W(0)[v,v,v] = D³f(0)[ζv, ζv, ζv]  (no second derivative of U* survives);
- (E4) D⁴W(0)[v⁴] = D⁴f(0)[(ζv)⁴] − 3·c(v)ᵀA^{-1}c(v), c(v)_i := ∂_{U_i}(D³f(0)[ζv, ζv, ·]) (the tree exchange through the
  one-step propagator A^{-1}).

## Instances (fixed now)
m = 2, d = 2. f = ½UᵀAU + UᵀBV + ½VᵀCV + (all cubic monomials in (U, V) with coefficients c_3) + (all quartic monomials
with coefficients c_4); A = [[3, 1],[1, 2]]; B, C and every c_3, c_4 pseudo-random rationals (numerators in [−5, 5],
denominators in [1, 4]) from the integer seed 5502 (Python `random.Random(5502)`). U*(V) is computed as a polynomial of
degree 3 in V by Newton/fixed-point iteration on ∇_Uf = 0 with truncation at total degree 3 (exact). W(V) is then
expanded to total degree 4. Test directions v ∈ {(1,0), (0,1), (1,1), (2,−3), (−1,4)}.

## Verdict lines
- **E0 (critical family).** ∇_Uf(U*(V), V) has no terms of total degree ≤ 3 in V. PASS iff exact.
- **E3.** For every test v: the degree-3 homogeneous part of W evaluated at v, times 3! (i.e. D³W(0)[v³]), equals
  D³f(0)[(ζv)³]. PASS iff exact for all five v.
- **E4.** For every test v: D⁴W(0)[v⁴] (4! × the degree-4 part at v) equals D⁴f(0)[(ζv)⁴] − 3c(v)ᵀA^{-1}c(v). PASS iff exact
  for all five v.
- **E3-c (designed FAIL control).** D³f(0)[(0, v)³] (ζ replaced by its V-part only) differs from D³W(0)[v³] for at least one
  test v. Must fire.
- **E4-c (designed FAIL control).** D⁴f(0)[(ζv)⁴] alone (exchange dropped) differs from D⁴W(0)[v⁴] for at least one test v.
  Must fire.

## Overall
PASS iff E0, E3, E4 PASS and both controls fire. A control that does not fire makes the check INVALID. Run once; output
kept unaltered.
