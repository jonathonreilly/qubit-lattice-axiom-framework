# r55n_w1 criteria — does NORMS Definition N^F-2's vertex norm 𝔑 equal +infinity on the nonabelian Wilson vertex?

Written 2026-10-28T22:27:47Z UTC by the REVIEW55_NORMS reviewer (claude-opus-5-5), BEFORE r55n_w1.py exists.

Object: T := D^3 S_W(1), the cubic Taylor form at the trivial background of the SU(2) Wilson action in the exponential
chart U_b = e^{A_b}, restricted to field configurations supported in one coordinate plane (exact for the d-dim lattice:
a plaquette with >= 2 nonzero links lies in that plane). su(2) is realised as (Q^3, cross product) with the ad-invariant
dot product. Cubic part of S_W = sum_p <X1_p, X2_p>, X1_p = sum_i a_i, X2_p = (1/2) sum_{i<j} [a_i, a_j],
a = (A_b1, A_b2, -A_b3, -A_b4) for U_p = U_b1 U_b2 U_b3^{-1} U_b4^{-1}. T = D^3 of that cubic via exact polarization.
H(Y,W) := sum_p (dY)_p . (dW)_p (Hessian of the quadratic part). lambda-bar_b := lambda_x + lambda_y for b = (x -> y).
Derived (by hand, in the review) Ward identity at the trivial point for U_b -> g_x U_b g_y^{-1}:
  T(d lambda, Y, W) = (1/2)[ H(Y, [lambda-bar, W]) + H(W, [lambda-bar, Y]) ].

Pre-registered gates (exact Fraction/integer arithmetic, python3 -I -B):
- w1-0 CONSTRUCTION: H(d lambda, V) == 0 for all candidates (quadratic gauge invariance). PASS iff all zero.
- w1-1 WARD: the displayed Ward identity holds exactly for every candidate (lambda, Y, W) in the fixed deterministic list
  below. PASS iff all hold. Designed-FAIL control w1-1': the same with the BCH coefficient 1/2 replaced by 1 must fail
  for at least one candidate.
- w1-2 WITNESS (decides 𝔑 = +infinity at k = 0): there is a candidate with T(d lambda, Y, W) != 0. PASS iff at least one.
  Abelian control w1-2': with the bracket set to 0, T(d lambda, Y, W) == 0 for all candidates (must hold; it shows the
  witness is nonabelian).
- w1-3 POSITIVE WITNESS: for lambda, mu fixed below and Z := [lambda-bar, d mu] (linkwise), dZ != 0 and
  T(d lambda, d mu, Z) == (1/2) sum_p |(dZ)_p|^2 > 0. PASS iff both. (Used for the k >= 1 extension argument.)
- w1-4 HARMONIC MODES (informational, no PASS/FAIL attached to the NBG_A claim itself): on a periodic 3x3 planar torus,
  a constant 1-form h (dh = 0, not a pure gauge) has T(h, Y, W) != 0 for some candidate (Y, W). Reported either way; it
  bears only on whether NBG_A's "one-line repair X in S_k" suffices on a torus.
Candidates: lambda supported on sites {(0,0),(1,0),(0,1),(1,1)} with integer vectors from a fixed seed list; Y, W integer
vector fields on the links of the 3x3 square [0,2]^2 from the same fixed list (deterministic, written in the script
before any run; no candidate is added after a result is seen).
