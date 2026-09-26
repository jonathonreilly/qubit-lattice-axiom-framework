# Execution notes

The first complete run finished successfully with 108 groups passed and no
failed group. Exact identities use integer edge arrays and rational/SymPy
matrices. Four explicitly labelled controls use floating-point linear solves,
sparse matrix exponentials and Gaussian quadrature.

SciPy emitted a FutureWarning at construction of the sparse diagonal because
its current default converts the integer diagonal to floating-point storage.
The raw warning is retained at the start of RUN.log. Sparse row-sum checks
involve exactly representable small integers; the other algebraic generator
checks operate directly on integer edge arrays, so no floating approximation
is introduced into those equalities. The sparse matrices used later in the
numerical reward calculation are deliberately converted to floating point.

RESULTS.json is the entire structured suffix of RUN.log. The log also includes
the warning; the two files are therefore not claimed to be byte-identical.
No warning was suppressed and no raw output was discarded.

The analytic invalid routes are documented in REPORT.md: the uncorrected
weighted adjoint is not a reversed Markov generator, stationary Dirichlet
energy can be negative under the growing law, stationary current replacement
requires a new evolving-law proof, and birth noise cannot be omitted.

No primary source, prohibited campaign file, simulation outcome, Git state,
PR, audit status or external message was accessed or changed. All written
files are inside this assigned independent directory.
