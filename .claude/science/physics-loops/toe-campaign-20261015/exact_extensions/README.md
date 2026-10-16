# Exact extensions in progress (B5)

- `fastR3.py R [GROUP]` is the line-branch certificate at range R. It uses
  Fourier-dictionary arithmetic and lines through every time-reversal-invariant
  momentum: lines whose stabiliser fixes only the line, with a base point
  where g = 0. Signs f = +-1 are branched per point class. At R = 2 it agrees
  with Theorem 4.
  - **R = 3 (`fastR3_3.log`):** 63 unknowns (21 scalars, 42 vectors). Of
    4,405,492 exponent/sign branches only the trivial one is linearly
    consistent (exact recheck of the numerical filter). The trivial branch
    leaves 21 real unknowns, with 122 real quadrics and linear forms
    (`r3_triv.sing`), which is being closed with Singular modStd.
- `tosing_branch.py` converts a branch to Singular, splitting each complex
  equation into real and imaginary parts.
- `spinj_exact.py J` is the exact line-branch test for an irreducible spin-J
  coin under O on the cell. On the axis, C4 has distinct eigenvalues, so U is
  diagonal with unit-monomial entries. On the body diagonal, the 1-dimensional
  C3 eigenspaces give monomials. U(0) = 1 by Schur's lemma.
  - **J = 1/2 (`spinj_1_2.log`):** this validation case reproduces the freeze,
    with a unique branch and U = 1.
  - **J = 3/2:** this is the irreducible 4-dimensional coin, with 19 complex
    parameters. It is running.
