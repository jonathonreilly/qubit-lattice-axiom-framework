# rd55_tens — criteria (written BEFORE rd55_tens.py exists)

Author: Opus 5.5 worker (claude-opus-5-5), ROTDEF.md §8 (scale-separation remark).

## Question
At which tensor rank does an H(4)-invariant symmetric tensor first fail to be O(4)-invariant? Equivalently: the
number of H(4)-invariant vectors in Sym^k(R^4), k = 1..4, compared with the O(4) count (1 for even k, 0 for odd k:
the powers of |x|^2).

## Method (fixed in advance)
Exact integer arithmetic over the 384 signed permutation matrices. For each h, chi_{Sym^k V}(h) is the coefficient of
t^k in prod over cycles c of h of 1/(1 - eps_c t^{len c}), eps_c = product of the signs on the cycle. Multiplicity of
the trivial rep = (1/384) sum_h chi_{Sym^k V}(h). Control: the k = 2 character must equal (tr(h)^2 + tr(h^2))/2 for
every h (FAIL otherwise, script BROKEN).

## Pre-registered PASS/FAIL
- T0 control (k = 2 character identity) holds for all 384 elements. Otherwise BROKEN.
- T1: invariant counts for k = 1, 2, 3, 4 are exactly (0, 1, 0, 2). PASS iff so. (PASS supports: the first
  H(4)-only (cubic) invariant appears at rank 4, sum_i x_i^4; ranks <= 3 carry no anisotropy.)
