# ROUGH numerical criteria — no experiment executed

Prerequisites: exclusive numeric lock; successful nice priority at least 10;
BLAS/OMP/MKL/NumExpr/Accelerate threads all one; no pools; RSS below 1 GB;
load below 8; at least 30 percent memory available. Inspect RSS using
resource.getrusage or psutil, never RLIMIT_AS. Stop before mathematical work
if any prerequisite fails. The priority preflight already failed in this
sandbox, so the checks below are NOT RUN and no executable experiment is
launched here.

If execution becomes possible in a later authorized run, predeclared checks:

1. On finite SU(2) paired-contour fields, compare the explicit mean-deficit
   and coarse-curvature quantities with the ribbon incidence bounds. Require
   the analytic inequalities within absolute roundoff 1e-10, without changing
   their coefficients after looking at the result.
2. On finite nonnegative incidence arrays, compare forward substitution and
   reverse propagation of regulator demands. Require coefficient equality
   within 1e-12. An intentional omitted shared-reader contribution must fail.
3. Enumerate distinct subsets of four source labels in a finite positive
   integral. Check quotient jets including denominator derivatives against
   direct differentiation through total field order six; require relative
   error 1e-8 where the expected value is nonzero and absolute error 1e-10
   otherwise. An omitted denominator derivative must fail.

These finite diagnostics would check implementations, not prove uniform
inherited-law moment estimates. No runner, result, PASS count or mutation
success is asserted in this packet.
