# Current-Form Tensorized Action / Carrier Variational-Disconnection No-Go

**Date:** 2026-04-14 (original construction); 2026-07-11 (current-form
variational-disconnection theorem)
**Claim type:** no_go
**Status:** exact negative boundary for the displayed action/carrier pair;
independent audit is required before any retained-grade use
**Primary runner:**
[`scripts/frontier_s3_time_bilinear_tensor_action.py`](../scripts/frontier_s3_time_bilinear_tensor_action.py)
**Runner cache:**
[`logs/runner-cache/frontier_s3_time_bilinear_tensor_action.txt`](../logs/runner-cache/frontier_s3_time_bilinear_tensor_action.txt)

## Question

The old note put two formulas beside one another:

```text
I_TB(f,a;j,q) = I_R(f;j) + 1/2 ||a - vec K_R(q)||^2,
Xi_TB(t;q)    = vec K_R(q) tensor exp(-t Lambda_R) u_*.
```

The formulas are finite and algebraically consistent.  The missing question is
whether the first formula generates the second one.  It does not.  This note
proves that narrow statement directly.  The result is an obstruction to the
current form, not a no-go against every possible tensor action or every
possible Einstein/Regge bridge.

## Minimal premise set

Let the slice space be `R^n`, with `n >= 2`.  Let `Lambda_R` be a symmetric
positive-definite `n x n` matrix, let `u_*` be nonzero, and abbreviate

```text
k(q) := vec K_R(q) in R^4.
```

No physical interpretation of `k`, no special endpoint values, and no
particular construction of `Lambda_R` are needed.  The theorem holds for every
nonzero `k`, every nonzero `u_*`, and every symmetric-positive
`Lambda_R`.  The scalar functional `I_R(f;j)` may be any differentiable
functional on `R^n`; its detailed origin is also irrelevant.

These generic premises deliberately remove the old upstream-certificate
problem from the proof.  The obstruction is a property of the displayed
formulas themselves.

## Theorem: the displayed action does not generate the displayed carrier

For fixed `q` and `j`, the first variation is

```text
delta I_TB
  = <grad_f I_R(f;j), delta f>
    + <a - k(q), delta a>.
```

Therefore the current Euler--Lagrange equations are exactly

```text
grad_f I_R(f;j) = 0,
a = k(q).
```

The tensor-sector Hessian is `I_4`, and the mixed `f`--`a` Hessian is zero.
Neither equation contains `t`, `u_*`, `Lambda_R` acting on a tensor field, or
the `4n`-dimensional field in which `Xi_TB` lives.

By contrast, the displayed carrier obeys

```text
partial_t Xi_TB(t;q)
  = -(I_4 tensor Lambda_R) Xi_TB(t;q),
Xi_TB(0;q) = k(q) tensor u_*.
```

Because `Lambda_R` is positive definite, `Lambda_R u_*` is nonzero.  Hence
for nonzero `k(q)`,

```text
partial_t Xi_TB(0;q) = -k(q) tensor Lambda_R u_* != 0.
```

The action's tensor equation gives the static algebraic value `a=k(q)`.  The
carrier equation gives a nonstationary flow in `R^4 tensor R^n`.  The latter
cannot be obtained as an Euler--Lagrange equation, or as the Euclidean gradient
flow of the displayed `1/2 ||a-k||^2` term, because its field variable and its
generator are absent from `I_TB`.

This is not a parameter mismatch.  It is a structural mismatch:

- the action varies four tensor coordinates `a in R^4`;
- the carrier has `4n` coordinates;
- the action's tensor Hessian is `I_4`;
- the carrier generator is `I_4 tensor Lambda_R`;
- the action is separable between `f` and `a`, so eliminating either block
  cannot create the missing mixed tensor/slice generator.

For `n >= 2`, even an invertible re-labeling of the current variables cannot
identify the `n+4` dimensional action domain with the `4n` dimensional carrier
space.  More importantly, re-labeling cannot insert a time derivative or the
absent generator.

## Completion control: the extra structure that would generate the carrier

The obstruction has a sharp falsifier.  Introduce a new tensor field
`A in R^4 tensor R^n` and define

```text
G := I_4 tensor Lambda_R,
S_gen(A) := 1/2 <A, G A>.
```

Its Euclidean gradient flow is

```text
partial_t A = -G A.
```

With `A(0)=k(q) tensor u_*`, the unique solution is exactly

```text
A(t) = k(q) tensor exp(-t Lambda_R)u_* = Xi_TB(t;q).
```

Thus the semigroup is not the problem.  A generator-bearing field action can
produce it.  But `S_gen` is a new action on a new field space; it is not the
displayed `I_TB`, and the framework has not derived a physical identification
of `S_gen` with Einstein/Regge dynamics.  This control isolates the one
remaining wall without turning it into a new axiom or silently importing it.

## Bilinear-carrier rank lemma

For the named bilinear expression

```text
K_R(q) = [[u_E, u_T], [delta u_E, delta u_T]]
       = [1, delta]^T [u_E, u_T],
```

`det K_R(q)=0` and `rank K_R(q) <= 1` identically.  Likewise, when reshaped as
a `4 x n` matrix,

```text
Xi_TB(t;q) = k(q) [exp(-t Lambda_R)u_*]^T
```

has rank at most one for every `t`.  This lemma is not the headline no-go:
rank-one carriers can be useful on restricted sectors.  It does show that the
word "tensor" does not by itself supply independent tensor-channel dynamics.

## Exact claim boundary

This note proves only:

> The displayed current-form `I_TB` does not generate the displayed
> `Xi_TB` semigroup by its Euler--Lagrange equations or by Euclidean gradient
> flow of its tensor penalty.  A generator-bearing tensor-field action is an
> additional mathematical input.

It does **not** prove:

- that no enlarged tensor action can generate `Xi_TB`;
- that the completion control `S_gen` is physically selected;
- that gradient flow is Einstein/Regge dynamics;
- that no non-variational bridge can be declared;
- that the scalar Schur action or bilinear carrier lacks value on its stated
  restricted surfaces;
- a no-go against Einstein/Regge dynamics in general.

The old positive identification target therefore closes negatively for the
displayed formulas: juxtaposing `I_TB` and `Xi_TB` is not a derivation of one
from the other.  Any future positive route must add and derive the missing
tensor-field variable, generator-bearing action, and physical bridge.

## Runner verification

The companion runner uses an exact rational witness matrix and an independent
matrix-exponential calculation to check:

1. the action Hessian is `diag(Lambda_R, I_4)` with zero mixed block;
2. the action stationary equations are the scalar equation plus `a=k`;
3. the carrier satisfies the nontrivial `I_4 tensor Lambda_R` semigroup;
4. the current tensor penalty's gradient flow is static at `a=k`;
5. the completion-control action generates the carrier exactly;
6. the bilinear carrier and spacetime carrier have rank at most one; and
7. the dimension and generator mismatches persist for `n >= 2`.

The manual first-variation calculation above is the independent check on the
runner's matrix implementation.
