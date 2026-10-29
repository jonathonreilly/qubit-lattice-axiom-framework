# Minimal proposed source correction

These replacements apply only to UNIFORM_SOFT_MINIMIZER_ASTRA.md. They clarify the tree phase consumed by FC18–FC20 and change no displayed mathematical formula. Source edits remain the coordinator's responsibility; the repaired bytes require affected re-review.

## Opening scope

Replace the first two sentences with:

> Author proof unit for the **u-stripped tree phase** of the supplied SU(N) Wilson / normalized S4′ soft-kernel model. **FC19 follows from the existing linear package with `theta=L^-2`; consequently FC20 gives a depth-uniform neutral quartic jet of the stationary tree value `T_n`.**

## Introduction to US1

Replace “At the trivial field, each real colour has the quadratic energy” with:

> The quadratic part at the trivial field of the normalized tree phase, with the overall factor `u=1/g^2` removed, is, for each real colour,

## Paragraph immediately after US1

Replace the paragraph beginning “These are integrated link variables” with:

> These are integrated link variables in each level's own unit lattice, and all adjoints use ordinary counting inner products. US1 is the quadratic part of the **u-stripped normalized tree phase** `F_tree=sum_p s(U_p)+sum_(j,c) kappa_j phi_(M_c(U_j))(U_(j+1),c)`, where `phi_M(V)=N^-1[max_W Re tr(W^-1 M)-Re tr(V^-1 M)]` and the maximum is over `SU(N)`. Its stationary value is the `T_n` used in FC18–FC20. The quadratic contour-spread term cancels in this phase. The exact finite-u negative logdensity also contains the field-dependent logarithm of a Haar integral, whose quadratic spread contribution is nonzero at finite u; US1 is not its full Hessian divided by u. FC18's fourth-order polar terms refer to `F_tree` and `T_n`.

The scope supplement independently derives the missing finite-u term as `(kappa*u/2)(1-c_N(kappa*u)) average_tau ||z_tau||^2`, with `c_N(t) I=E_t[W]`. This formula need not be added to the already scoped proof note; the explicit distinction above is sufficient for its claim boundary.
