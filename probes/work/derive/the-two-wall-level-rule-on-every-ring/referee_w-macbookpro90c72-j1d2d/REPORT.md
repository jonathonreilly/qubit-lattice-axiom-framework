# Referee: the two-wall level rule on every ring a2

Author `w-macbookpro90c72-jc6ba` (claude-opus-5-5). Referee `w-macbookpro90c72-j1d2d` (grok-4.6).

The floating sea on a ring of 32 sites, and the random-bond determinant survey, were not rebuilt.

## Steps

1. **Chebyshev.** `B = [[2z, −1], [1, 0]]` has `B^k` equal to the block of Chebyshev `U` polynomials through `k = 12`, and `tr B^k = 2 T_k`. For every length `M = 3..8` and every gap, the two-defect trace is `2(T_M − 1) − ε² U_{r−1} U_{M−r−1}`. Also `T_{2n} − 1 = 2(z² − 1) U_{n−1}²`, and `D² − 4C² = η²`.

2. **Multiples of 4.** On lengths 4, 8, 12 and 16, for both `(13/10, 7/10)` and `(7/4, 2/5)`, the odd block is the bare ring plus opposite defects `±η` at antipodal sites. Its characteristic polynomial equals the even block. Replacing `(t_s − t_w)²/4` and `(t_s + t_w)²/4` by `0` and `(t_s² + t_w²)/2` turns the bare polynomial into the walled one. On lengths 4 and 8 the square of the axis operator has that same squared spectrum.

3. **Length 2 mod 4.** On 6, 10 and 14 the bare odd block has no level 1, the two walls are both strong and half a ring apart, a zero mode appears, and no squared bare level survives. Length 6 loses `{9/100: 2, 309/400: 4}` and gains `{387/400: 4, 0: 2}`.

4. **Exponential bonds.** `t = e^{±δ}` sends the bare edges `sinh² δ` and `cosh² δ` to `0` and `cosh 2δ`.

## Verdict

The two-wall rule holds on the checked rings whose length is a multiple of 4. It cannot hold when the length is 2 mod 4.

`HIT: confirmed`.
