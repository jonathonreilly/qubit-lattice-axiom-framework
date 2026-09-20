# Independent finite-rate bound: initial derivation

Derived 2026-09-20 before reading any new primary campaign calculations.
This file records the analytical result before computational checks.

Let `Q` be an irreducible reversible row generator on at least two states,
with invariant probability `pi` and spectral gap `lambda>0` for `L=-Q` on
the mean-zero subspace of `L2(pi)`. Let `0<b_min<=B<=b_max`,
`mu=E_pi B`, `sigma_B^2=Var_pi(B)`, and `f=alpha/pi` for an arbitrary
entrance probability `alpha`. All norms below are in `L2(pi)` unless noted.
Write `nu_0=pi B/mu` for the rare-birth event law.

The proposed bound is

```
TV(nu_epsilon,nu_0)
 <= min{1, epsilon sqrt(mu*b_max)/(2(lambda+epsilon*b_min))
                 * ||f-B/mu||_2}.
```

In particular, it is at most the same prefactor times
`sqrt(chi^2(alpha||pi)) + sigma_B/mu`. For stationary entrance this becomes

```
TV(nu_epsilon,nu_0)
 <= min{1, epsilon sigma_B sqrt(b_max/mu)
                 /(2(lambda+epsilon*b_min))}.
```

It vanishes for stationary entrance and constant hazard. The stronger exact
statement is that `alpha=nu_0` gives `nu_epsilon=nu_0` for every epsilon.

## Derivation

Reversibility converts the row occupation resolvent to a self-adjoint
function equation. Put

```
r = epsilon (epsilon B + L)^(-1) f,
h = r-1/mu,
g = f-B/mu.
```

Here `B` also denotes multiplication by the hazard. Then
`nu_epsilon(s)=pi(s)B(s)r(s)`, `(L+epsilon B)h=epsilon g`, and
`E_pi g=E_pi(Bh)=0`.

Let `P` be projection onto mean-zero functions, put `u=Ph`, and define
`b=B-mu`. The weighted-mean condition gives
`h=u-E_pi(Bu)/mu`. Projecting the equation gives the exact identity

```
(L + epsilon T) u = epsilon g,
T = P B P - (b tensor b)/mu
```

on the mean-zero subspace. For any such `u`,

```
<u,Tu> = E_pi(Bu^2) - (E_pi Bu)^2/mu
        = min_c E_pi[B(u-c)^2].
```

Consequently `b_min ||u||^2 <= <u,Tu> <= b_max ||u||^2`:
the lower bound follows by first replacing B by b_min and minimizing over
c, while the upper bound follows by choosing c=0. Thus

```
||u|| <= epsilon ||g||/(lambda+epsilon*b_min).
```

Finally,

```
TV = (1/2) E_pi[B |h|]
   <= (1/2) sqrt(mu E_pi[B h^2])
    = (1/2) sqrt(mu <u,Tu>)
   <= (1/2) sqrt(mu*b_max) ||u||.
```

This proves the proposed bound without assuming that L and T commute.
The entrance/hazard statistic can also be written exactly as

```
||g||^2 = chi^2(alpha||pi) + sigma_B^2/mu^2
          - 2 Cov_pi(f,B)/mu.
```

The triangle inequality gives the separated entrance/hazard bound above.

## An alternative exact clock representation

The row generator `R=diag(B)^(-1)Q` is reversible with invariant law
`nu_0=pi B/mu`. Factoring the original resolvent shows exactly

```
nu_epsilon = epsilon alpha(epsilon I-R)^(-1).
```

If `gamma` is the spectral gap of `-R` in `L2(nu_0)`, the spectral theorem
therefore yields

```
TV(nu_epsilon,nu_0)
 <= epsilon/[2(epsilon+gamma)] * sqrt(chi^2(alpha||nu_0)).
```

The Dirichlet-form comparison gives `gamma>=lambda/b_max`, since
`E_R=E_Q/mu` and `Var_nu0(v)<=b_max Var_pi(v)/mu`. Also
`chi^2(alpha||nu_0)=mu E_pi[g^2/B]`. This supplies a second bound stated
entirely using the original motion gap and known hazard/entrance quantities.
It need not dominate the first bound; both are valid.

For a singleton motion class the event law is the only point mass for every
epsilon, so the TV error is zero without introducing a spectral gap.
The displayed bounds hold for fixed finite Q, B and alpha. Dependence on
the spectral gap and entrance density remains explicit; no bound uniform
over growing graphs is asserted.
