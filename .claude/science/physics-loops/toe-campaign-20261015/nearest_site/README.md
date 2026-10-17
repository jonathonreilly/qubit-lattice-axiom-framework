> Review status: the original report below is preserved as an unadopted proof
> candidate. Independent review matched the exact families and equations but
> did not certify exhaustive minimal-prime coverage. Historical exact-proof
> language below is not a current review verdict or adopted no-go.

# Nearest-site staggered block tick: exact decomposition (in progress)

The input is the independent checker's exact unitarity equations for the
spinorial class with nearest-site hops: 11 complex coefficients c0..c10, one
per hop-type orbit, ordered ooo, oo0, ooi, o00, o0i, oi0, oii, 000, 00i, 0ii,
iii (`independent_check_B7/eqs3.txt`). The conjugates cb_i are treated as
independent variables.

Singular `minAssGTZ` (`nn_min.sing` / `nn_min.out`) gives 8 minimal
components: dimensions 4, 4, 2, 2, 2, 2, 4, 4. Imposing reality,
cb = conj(c):

- **Component 1.** Generators set every in-type and mixed coefficient to
  zero, so the walk is purely out-type (shifted-block): flat.
- **Component 2.** Contains c4 cb4 + c5 cb5 and c2 cb2 + c8 cb8. These are
  sums of |c|^2 on real points, so those coefficients vanish; c6, c9, c10 are
  zero; purely out-type: flat.
- **Component 7.** cb3..cb6 are generators, so c3..c6 = 0 on real points;
  purely in-type (block-diagonal): flat.
- **Components 3, 4.** Reality forces c7 conj(c9) real and c6 = -+ i c9.
  Combined with c6 = (c7^2 + 8 c9^2) conj(c6), this forces c9 = 0 and then
  every coefficient except c7: the constant walk.
- **Components 5, 6.** Contain c9 cb9 + c10 cb10, so c9 = c10 = 0, and the
  rest follows: the constant walk.
- **Component 8.** Closed by hand from its generators (B6 note, Theorem 3).
  - Phase alignment of c7..c10.
  - The quartic generator gives r10 = 0 and r8^2 = 2 r9^2, so
    r7^2 + 9 r9^2 = 1.
  - Then c_j = e^{2 i theta} conj(c_j) for j = 3..6, and the cb-only
    generators force c3..c6 = 0.
  - So the walk is purely in-type: flat. `comp8_real.py` agrees numerically:
    the residual scales as 0.48 x delta.

Result: every real nearest-site unitary walk on the spinorial block is flat
(purely in-type, purely out-type, or constant). This is an exact no-go for a
nearest-site Kogut–Susskind-type one-tick walk.
