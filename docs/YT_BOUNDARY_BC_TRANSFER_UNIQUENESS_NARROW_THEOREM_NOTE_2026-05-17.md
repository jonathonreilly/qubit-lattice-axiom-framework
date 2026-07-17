# Universal Scalar Yukawa Boundary-Transfer Uniqueness Theorem

**Original date:** 2026-05-17
**Exact-theorem pivot:** 2026-07-17
**Claim type:** positive_theorem
**Type:** positive_theorem
**Status:** exact support theorem; independent review and independent audit are
required before any proposed-retained or effective-retained status.
**Claim scope:** the universal exact transfer theorem for positive solutions of
`y' = a(t)y + b y^3` on a finite interval with continuous real `a` and
`b > 0`: its closed form, exact endpoint domain, range `(0,infinity)`, strict
monotonicity, and exact inverse. The one-loop Yukawa specialization below is
conditional symbolic context only and is excluded from this claim scope.

**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/frontier_yt_boundary_bc_transfer_uniqueness.py`](../scripts/frontier_yt_boundary_bc_transfer_uniqueness.py)
**Cache:**
[`logs/runner-cache/frontier_yt_boundary_bc_transfer_uniqueness.txt`](../logs/runner-cache/frontier_yt_boundary_bc_transfer_uniqueness.txt)

The historical path is preserved so the same audited row can be re-audited.
The former row was a sampled coupled-flow diagnostic conditional on five
implementation inputs. This pivot does not rename those inputs or promote
them. It removes them from the theorem.

## The question

Suppose a positive scalar coupling obeys

```text
dy/dt = a(t)y + b y^3.
```

If its value `X` is specified at one end of a finite interval, is its value at
the other end a one-to-one function of `X`? For continuous `a` and positive
`b`, the answer is exact. No grid or root finder is needed.

## The theorem

Let `t0 < T`, let `a` be a continuous real function on `[t0,T]`, and let
`b > 0`. Define

```text
A(t) = integral from t0 to t of a(s) ds,
J(t) = integral from t0 to t of exp(2 A(s)) ds.
```

For initial data `y(t0) = X > 0`, set

```text
D(t;X) = 1 - 2 b X^2 J(t).
```

Then:

1. On every subinterval where `D(t;X) > 0`, the unique positive solution is

   ```text
   y(t;X) = X exp(A(t)) / sqrt(D(t;X)).                 (1)
   ```

2. Because `J` is continuous and strictly increasing, the solution has a
   finite endpoint at `T` exactly for

   ```text
   0 < X < X_crit,
   X_crit = 1 / sqrt(2 b J(T)).                         (2)
   ```

3. On that exact domain the endpoint transfer map

   ```text
   Phi_T(X) = y(T;X)
   ```

   is a strictly increasing bijection from `(0,X_crit)` onto
   `(0,infinity)`. Its derivative is

   ```text
   d Phi_T/dX
     = exp(A(T)) / (1 - 2 b J(T) X^2)^(3/2) > 0.       (3)
   ```

4. Every positive endpoint target `Y` therefore has exactly one preimage,

   ```text
   X*(Y)
     = Y / sqrt(exp(2 A(T)) + 2 b J(T) Y^2).            (4)
   ```

Equations (1)-(4), including the exact domain and range, are the whole
load-bearing claim.

## Proof

The positive solution cannot cross zero. Set

```text
z(t) = y(t)^(-2).
```

Direct differentiation gives the linear equation

```text
z' + 2 a(t) z = -2 b.                                  (5)
```

Multiplying by the integrating factor `exp(2 A(t))` and using
`z(t0) = X^(-2)` gives

```text
z(t) = exp(-2 A(t)) [X^(-2) - 2 b J(t)].               (6)
```

Taking the positive inverse square root of (6) gives (1). Conversely,
differentiating (1), using `A' = a` and `J' = exp(2A)`, reproduces the
original differential equation and the initial value. This proves the
solution formula without importing an ODE trajectory.

Since `exp(2A)` is positive and continuous, `J(t0)=0` and `J` is strictly
increasing. Thus `D(t;X)` stays positive through `T` exactly under (2). At
`X=X_crit`, `D` reaches zero at `T`; for `X>X_crit`, it reaches zero once at
an earlier time. Hence (2) is the exact finite-endpoint domain, not a sampled
bound.

At `T`, differentiating (1) with respect to `X` gives (3). Also,

```text
lim X -> 0+       Phi_T(X) = 0,
lim X -> X_crit-  Phi_T(X) = infinity.
```

Strict monotonicity and these endpoint limits prove bijectivity. Solving
`Phi_T(X)=Y` for `X` gives (4), and

```text
2 b J(T) X*(Y)^2 < 1
```

for every `Y>0`, so the inverse always lies in the exact domain. QED.

## Sharp domain boundary

The assumptions matter.

- `X=0` is the separate zero solution and is outside the positive-domain
  bijection.
- At `X=X_crit`, the endpoint is not finite.
- For `X>X_crit`, the positive solution has a denominator zero before `T`.
- The condition `b>0` is part of the theorem. With `b<0`, the transfer remains
  order-preserving on positive inputs but its range need not be all positive
  targets, so the stated bijection and inverse-domain conclusion would be a
  different theorem.

These are domain statements about the displayed scalar equation. They are not
claims about a fixed physical trajectory.

## Conditional symbolic one-loop Yukawa corollary

For any continuous real gauge-history triple `(g1(t),g2(t),g3(t))`, with
`g1` written in the SU(5)-normalized hypercharge convention, define

```text
a_g(t) = -(17 g1(t)^2/20 + 9 g2(t)^2/4 + 8 g3(t)^2)/(16 pi^2),
b_y    = 9/(32 pi^2).
```

Then the one-loop Yukawa-shaped scalar equation

```text
y' = a_g(t)y + b_y y^3
```

has the theorem's exact transfer map. This corollary is conditional and
symbolic only. It quantifies over the gauge histories and the positive endpoint
target; it selects neither. It does not assert that a particular physical
flow, scale interval, matching prescription, or boundary value is supplied by
the framework.

## Import firewall

The former implementation inputs `I1`-`I5` have no load-bearing role:

| former input | role in this theorem |
|---|---|
| canonical lattice constants | none |
| a fixed boundary target | none; `Y>0` is universally quantified |
| coupled multi-loop coefficients and procedure | none |
| fixed threshold scales | none |
| an electroweak initial-condition surface | none |

No numerical value from those inputs appears in the theorem, proof, runner, or
cache. They are not converted into definitions, benchmark choices, or hidden
fixtures.

This theorem supplies no Planck-scale, Ward-target, Standard-Model, or
parent-lane closure. In particular, it does not close the parent YT boundary
theorem, prove a coupled multi-loop transfer, or select a physical endpoint
target.

## Runner evidence

The companion runner provides four separately invocable layers:

1. exact symbolic derivation and source-firewall checks;
2. an independently coded numerical oracle on synthetic coefficient histories
   only;
3. hostile domain, formula, source, and API mutation rejection;
4. intentional-failure fixtures that must exit nonzero.

The numerical oracle is a cross-check, not the proof. The proof-bearing checks
are the exact `z=y^(-2)` reduction, closed-form substitution, endpoint
derivative, limits, and two-sided inverse identities.

## Source graph boundary

The theorem is self-contained and has no scientific source-note dependency.
The runner and cache links above are implementation evidence. Any later
physical use must cite and independently close its own gauge-history,
matching, target, scale, and observable bridges.
