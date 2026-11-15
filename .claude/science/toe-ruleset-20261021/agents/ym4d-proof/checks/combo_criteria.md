# COMBO check criteria — registered before implementation

2026-10-30 UTC (2026-10-29 local). These are finite exact algebra checks
of the written comparator examples, not measurements of Yang–Mills.
No scientific script has yet been written or run for COMBO.

1. With four independent mean symbols and six independent off-diagonal
   covariance symbols, Gaussian raw moments must have identically zero
   fourth joint cumulant, using the full partition formula.
2. A common independent amplitude taking values 1 and 2 with probabilities
   1/2 and 1/2, multiplying a centred Gaussian family, must give covariance
   `(5/2) Cij` and fourth cumulant
   `(9/4)(C12 C34 + C13 C24 + C14 C23)`.
3. A common independent shift taking values -1 and 1 with equal probability,
   added to that Gaussian family, must give covariance `Cij+1` and fourth
   cumulant `-2` for four unit-integral tests.
4. For the point-labelled product of two independent centred Gaussian
   families with identical covariance H, raw subset moments are squares
   of Gaussian subset moments. The second moment must be `Hij^2`, the
   third cumulant zero, and the fourth cumulant
   `2(AB+AC+BC)`, where `A=H12 H34`, `B=H13 H24`, `C=H14 H23`.
   This is a kernel identity before separate smearing of the four slots.
5. Applied to the product family in item 4, each deterministic affine map
   `e -> a e+b`, for `(a,b)=(-3/2,7/3),(2/3,-5/2)`, must multiply
   the covariance by `a^2` and the fourth cumulant by `a^4`. The ratio
   invariance must hold by cross multiplication, without division at zero.
6. Controls must be detected: omitting a Gaussian pair subtraction;
   substituting `E[A^4]` for `Var(A^2)` in item 2; replacing the coefficient
   2 by 1 in item 4; dropping the mean-variance term in item 3. Each must
   give a nonzero difference from the independently computed result.

All identities use exact integers/rationals and formal polynomials, with
zero tolerance. No quadrature, fitted coefficients, AF extrapolation or
interacting-source checks are planned. A failed identity remains a failed
identity; later probes must be identified as post-hoc.

Execution is serial, without pools, under an exclusive `combo_numeric.lock`.
Require nice >=10, OPENBLAS/OMP/MKL/VECLIB/NUMEXPR threads all equal to one,
load1 <8 and native macOS free memory >=30%, checked before/during/after.
A watchdog enforces combined runner/child RSS <800 MiB and time <60 s.
Record resource readings and result hashes. Failure of nice or any guard
is a failed run, not permission to weaken it. Disable bytecode writes.
