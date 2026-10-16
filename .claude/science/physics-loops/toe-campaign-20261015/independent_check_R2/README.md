# Independent check: O-covariant one-qubit walks on {-2..2}^3 (Theorem 4)

A fresh agent context was given only the problem statement. It had no access to
the note, its runner, or the expected answer. Its verdict is FROZEN, reached by
its own route:

1. A 1-D line lemma on the lines (t,0) and (t,pi) of the k3 = 0, pi slices.
2. An exact D4 classification of the 2-D slices: 100 line cases, each with an
   exact Groebner basis. Singular modStd and minAssGTZ cross-check it and find
   only the points +-I.
3. A 3-D reduction from the slice constraints. Exact Groebner bases in sympy
   and Singular give only V = +-I.

It agrees with the line-branch certificate in
`scripts/cubic_covariant_qubit_walk_line_branch_certificates_2026_10_16.py`.
Run order: `setup.py`, `equations.py`, `slice2d_cases.py`, `reduce3d.py`. The
scripts were written in a scratch directory and use absolute scratch paths for
their pickles; adjust them before rerunning. Limit of independence: the
checker is the same model family in a new context.
