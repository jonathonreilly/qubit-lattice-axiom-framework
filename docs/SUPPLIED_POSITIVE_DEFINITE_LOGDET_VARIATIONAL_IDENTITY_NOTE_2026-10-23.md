# Supplied positive-definite logdet variational identity

**Date:** 2026-10-23
**Status:** bounded - conditional matrix theorem; independent confirmation pending.
**Type:** bounded_theorem
**Script:** `scripts/supplied_positive_definite_logdet_variational_identity_2026_10_23.py`
**Claim scope:** finite-dimensional complex Hermitian positive-definite matrices only; no physical generator, source selection or transport conclusion.
**Status authority:** independent audit lane only.

## Hypotheses and statement

Supply an integer n>=1 and a complex Hermitian matrix Y>0. Optimize over
Hermitian K with I+K>0. Logs are natural logs of positive real determinants.
Then

    sup_K {log det(I+K) - Tr(KY)} = Tr(Y) - log det(Y) - n,
    K_star = Y^{-1} - I.

The supremum is attained uniquely at K_star. Y is held fixed: this theorem
optimizes K, not Y. All positivity assumptions are substantive.

## Complete proof

Let A=I+K>0 and Z=Y^(1/2) A Y^(1/2)>0, where the square root is the unique
positive Hermitian square root. Congruence is a bijection between positive A
and positive Z. Determinant multiplicativity and trace cyclicity give

    log det A - Tr((A-I)Y)
      = log det Z - Tr Z + Tr Y - log det Y.

By the spectral theorem the first two terms equal sum_j(log z_j-z_j), with
real z_j>0. The scalar inequality log z<=z-1 follows, for example, by
integrating 1-1/z away from its minimum at z=1; equality holds only at 1.
Consequently the sum is at most -n, uniquely when every z_j=1. Hermiticity
then implies Z=I, hence A=Y^{-1} and K=K_star. This K is feasible because
Y^{-1}>0. This proves global attainment and uniqueness, including
noncommuting complex matrices; directional sampling is unnecessary.
The exact nonnegative gap is Tr Z-log det Z-n.

For supplied H_seed>0 and H_e>0, put
Y=H_seed^(-1/2) H_e H_seed^(-1/2). Similarity and trace cyclicity rewrite the
value as Tr(H_seed^{-1} H_e)-log det(H_seed^{-1} H_e)-n. The generally
non-Hermitian product is similar to positive Y, so its determinant is positive;
this corollary does not assert positivity merely from its determinant.

## Hypothesis boundaries

If Hermitian Y is singular positive semidefinite, choose a null eigenvector
and let A have eigenvalue t in that direction, 1 elsewhere. The objective
contains log t and is unbounded above. If Y has a negative eigenvalue lambda,
the same choice contributes log t-lambda(t-1), again unbounded above.
In particular Y=diag(-1,-1) has determinant +1 and still fails the hypothesis.
The scalar Y=0 and Y=-1 checks illustrate these routes; the argument above,
not a finite t sample, establishes unboundedness. Without I+K>0, the real
logdet objective used here is not the stated optimization problem.

## Evidence and limits

The primary exercises scalar, diagonal and noncommuting complex supplied
fixtures, the optimizer, exact gap formula and seed normalization; it rejects
singular, indefinite, non-Hermitian and infeasible inputs. Numerical tolerances
are 1e-12 for fixture identities and 1e-10 for matrix validation. They do not
replace exact hypotheses or prove the theorem. A finite monotonicity check on
the boundary examples is only a control on the displayed divergent routes.

This algebra was present within PR9847's observable-relative-action Part 0.
It is extracted as its own executable owner without importing that runner's
transport initialization or optimization campaign. The historical selector
runner, its unconditional authority assertions, and the sister stationarity
runner's failed residual are not certified or repaired here. No framework
origin of a logdet generator, physical minimization rule, PMNS selector, eta
closure, uniqueness of a constrained source, or physical primitive follows.
All inherited numerical and negative evidence remains untouched.

## Command

`python3 scripts/supplied_positive_definite_logdet_variational_identity_2026_10_23.py`
