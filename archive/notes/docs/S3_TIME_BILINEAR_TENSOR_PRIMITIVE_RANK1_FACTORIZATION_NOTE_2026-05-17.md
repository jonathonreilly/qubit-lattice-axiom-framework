# Route 2 Bilinear Carrier `K_R` — Rank-1 Outer-Product Factorization (Positive Narrow Theorem)

**Date:** 2026-05-17
**Branch:** `physics-loop/s3-time-bilinear-tensor-primitive-block16-2026-05-17`
**Status:** positive narrow theorem (class A, polynomial-identity
substitution) on the *internal algebraic structure* of the bilinear
carrier symbol `K_R` defined in
[`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md).
**Claim type:** bounded_theorem — positive_theorem, narrow scope.
**Status authority:** independent audit lane only.
**Authority role:** records a class-A structural property of the carrier
symbol under the same named admitted inputs as the parent definition.
Explicitly **does not** close any of the three named open gaps in the
parent note; explicitly **does not** assert retained/bounded promotion.
**Primary runner:**
[`scripts/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.py`](../scripts/frontier_s3_time_bilinear_tensor_primitive_rank1_factorization.py).

## Scope

This is a **positive narrow theorem** on the internal algebraic structure
of the carrier symbol `K_R` defined by
[`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md).
Under the same named admitted inputs (`delta_A1` from the retained-bounded
[`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md);
`(u_E, u_T)` as linear functionals in the adapted basis), the symbol
factors algebraically as a rank-1 outer product, and five structural
properties (R1)-(R5) follow by polynomial identity.

This note **does not** close any of the three named upstream gaps from the
parent definition note (decoupling derivation, aligned-bright identification,
physical-primitive bridge). It does **not** promote the parent row beyond
its current `open_gate` status. It adds a class-A structural addendum that
sharpens the algebraic picture from "definition only" to "definition with
a derived rank-1 outer-product structure".

## Cited authorities (one-hop deps; cited, not closed in this note)

- [`S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
  (`claim_type: open_gate`, `audit_status: audited_renaming`) — the
  source of the symbolic carrier `K_R(q)` and the named admitted-input
  triple `(delta_A1, u_E, u_T)`. This note's R1-R5 are stated *as
  identities of that symbol* under those same admitted inputs.
- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`,
  `audit_status: audited_clean`) — the source of `delta_A1` as a named
  admitted scalar background datum. The runner imports `support_delta`
  from the corresponding `frontier_tensor_support_center_excess_law.py`.

## Independence from named upstream gaps

The parent note names three open theorem targets:

1. retained derivation of the `delta_A1`-decoupling fact;
2. retained derivation of the aligned-bright coordinate identification;
3. retained bridge theorem identifying `K_R` with a physical tensor
   primitive in the GR readout chain.

R1, R2, R3, R5 below are *purely algebraic identities of the symbol*
`K_R` itself and require none of (1), (2), (3). R4 (channel-separation
of partial derivatives) is *stated* using the admitted decoupling fact
from (1) and is *verified* by the runner on the same finite grid that the
parent runner uses; it does not close (1). The class-A scope is preserved.

## Statement of the positive narrow theorem

**Carrier factorization.** Under the named admitted inputs of the parent
note, the symbolic carrier

`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`

factors algebraically as the rank-1 outer product

> `K_R(q) = w(q) v(q)^T`

with

- `w(q) := (1, delta_A1(q))^T`  ("scaling-channel" column)
- `v(q) := (u_E(q), u_T(q))^T`  ("bright-channel" column).

Equivalently, the flattened 4-vector form

`vec K_R(q) = v(q) ⊗ w(q)`

is the Kronecker outer product of the bright-channel column with the
scaling-channel column.

The five structural properties (R1)-(R5) follow by polynomial-identity
arithmetic from the symbol definition.

### (R1) Rank-1 universality

For every `q` on the seven-site star support, the 2x2 matrix `K_R(q)` has
rank at most 1. When the bright channel is non-degenerate (i.e. `u_E(q) != 0`
or `u_T(q) != 0`), the rank is *exactly* 1 regardless of the value of
`delta_A1(q)`. This is a *universal* structural property: it does not
depend on the value of `delta_A1`, on whether `delta_A1` is exactly blind
to non-A1 perturbations, or on whether `(u_E, u_T)` are canonical bright
coordinates.

### (R2) Row proportionality / determinant vanishing

The two rows of `K_R(q)` are proportional: `row_2 = delta_A1(q) * row_1`.
Equivalently the determinant vanishes identically:

`det K_R(q) = u_E(q) (delta_A1(q) u_T(q)) - u_T(q) (delta_A1(q) u_E(q)) = 0`

for every `q`. This is a polynomial identity in `(delta_A1, u_E, u_T)`.

### (R3) Column proportionality

The two columns of `K_R(q)` are proportional whenever the bright channel
is non-degenerate:

- `col_2 / col_1 = u_T(q) / u_E(q)` (when `u_E(q) != 0`)
- `col_1 / col_2 = u_E(q) / u_T(q)` (when `u_T(q) != 0`)

The proportionality ratio is *scale-invariant* in `delta_A1`: it depends
only on the bright channel `(u_E, u_T)`. This is a structural separation
of the bright-channel ratio from the scaling channel `delta_A1`.

### (R4) Channel-separation of partial derivatives (under the named admitted decoupling fact)

Under the named admitted decoupling fact
`delta_A1 ⊥ {E_x, T1x, E_perp, T1y, T1z}` (gap (1) of the parent note),
the partial derivatives of `K_R` along the bright basis vectors split
cleanly:

- `partial_{E_x} K_R(q) = w(q) (1, 0)`
- `partial_{T1x} K_R(q) = w(q) (0, 1)`

where `w(q) = (1, delta_A1(q))^T` is the scaling-channel column.
Equivalently, the bright-direction perturbations modify the *bright*
column `v(q)` only, while the *scaling* column `w(q)` is inherited from
the background `delta_A1(q)`. This is a structural channel-separation of
the carrier under the admitted decoupling fact: bright perturbations act
on `v`, the scaling structure `w` is untouched.

For the auxiliary scaling-channel perturbation (a polynomial perturbation
of `delta_A1` treating it as a free symbol), the formal partial derivative
is

- `partial_{delta} K_R(q) = [[0, 0], [u_E(q), u_T(q)]] = e_2 v(q)^T`

with `e_2 = (0, 1)^T`. The scaling perturbation acts on the *second row*
only, with the bright column `v(q)` unchanged. This is the complementary
structural channel-separation in the scaling direction.

R4 is *stated* using the admitted decoupling fact and is *verified* by
the runner on the same finite grid as the parent runner. The verification
does not promote the decoupling fact above the class-D finite-grid shadow
already recorded by the parent runner; gap (1) remains open.

### (R5) Singular-value collapse

The two singular values of `K_R(q)` are

- `sigma_1(q) = ||w(q)|| * ||v(q)|| = sqrt(1 + delta_A1(q)^2) * sqrt(u_E(q)^2 + u_T(q)^2)`
- `sigma_2(q) = 0`

The single non-zero singular value factors algebraically into a
*pure-scaling contribution* `sqrt(1 + delta_A1(q)^2)` (depending only on
the scalar background datum) and a *pure-bright contribution*
`sqrt(u_E(q)^2 + u_T(q)^2)` (depending only on the bright projections).
This is the singular-value version of the rank-1 outer-product
factorization: the scaling and bright channels are spectrally separated
inside `sigma_1`.

## Proof (polynomial-identity arithmetic)

Each of R1-R5 is a polynomial identity in the symbolic inputs
`(delta_A1, u_E, u_T)`. We give the algebra in each case; the runner
verifies the corresponding numerical identities at machine precision on
the seven-site star support.

**R1, R2, R3 (combined).** Write `K_R(q)` in factored form:

`K_R(q) = [[1], [delta_A1(q)]] [u_E(q), u_T(q)] = w(q) v(q)^T`.

This is the polynomial-identity rank-1 factorization. Any 2x2 matrix of
the form `w v^T` has rank at most 1, with rank exactly 1 iff both `w` and
`v` are non-zero. Here `w(q) = (1, delta_A1(q))^T` is never zero (the
first component is the constant 1). Hence rank-1 iff `v(q) != 0` iff at
least one of `u_E(q), u_T(q)` is non-zero. This gives R1.

The determinant of a rank-1 outer product vanishes identically:
`det(w v^T) = w_1 v_2 w_? v_? - w_2 v_1 w_? v_? = 0` by direct
polynomial expansion. This gives R2.

For R3, observe that the columns of `w v^T` are
`col_j = v_j w`, so `col_2 = (v_2/v_1) col_1 = (u_T/u_E) col_1`
whenever `v_1 = u_E != 0`. The ratio depends only on `v(q)`, not on
`w(q)`. This gives R3.

**R4 (under the admitted decoupling fact).** Under
`delta_A1(q + h E_x) = delta_A1(q)` (admitted) and bilinearity of
`u_E, u_T`:

`K_R(q + h E_x) - K_R(q)`
`= [[u_E(q+hE_x) - u_E(q), u_T(q+hE_x) - u_T(q)],`
`   [delta_A1(q)(u_E(q+hE_x) - u_E(q)), delta_A1(q)(u_T(q+hE_x) - u_T(q))]]`
`= [[h, 0], [h delta_A1(q), 0]]`
`= h [[1, 0], [delta_A1(q), 0]]`
`= h w(q) (1, 0)`

using `u_E(E_x) = <E_x, E_x> = 1` and `u_T(E_x) = <T1x, E_x> = 0`
(orthogonality of the E and T1 sectors of the adapted basis). Dividing
by `h` and taking the formal limit gives `partial_{E_x} K_R = w (1,0)`.
The same calculation with `T1x` and the symmetric inner-product values
gives `partial_{T1x} K_R = w (0, 1)`.

The scaling-channel formal derivative follows from direct symbolic
differentiation of `K_R(q)` treating `delta_A1` as a free symbol:
`partial_{delta} K_R = [[0, 0], [u_E, u_T]] = e_2 v^T`.

**R5.** A rank-1 outer product `w v^T` has the polar decomposition
`w v^T = (||w||) u_w (||v||) u_v^T`, where `u_w = w/||w||`, `u_v = v/||v||`
are unit vectors. The non-zero singular value is `sigma_1 = ||w|| ||v||`
and the second singular value vanishes. Substituting

`||w(q)||^2 = 1 + delta_A1(q)^2`,
`||v(q)||^2 = u_E(q)^2 + u_T(q)^2`

gives the stated factorization. This is a polynomial-identity computation
in `(delta_A1, u_E, u_T)`.

## What is NOT closed by this note

This note explicitly does **not** close:

1. The retained-grade derivation of the `delta_A1`-decoupling fact (gap
   (1) of the parent note). The runner's R4 verification on the finite
   grid is a class-D shadow of the decoupling fact, identical in status
   to the parent runner's existing class-D shadow. The upstream
   certificate remains the open gap.
2. The retained-grade derivation of the aligned-bright coordinate
   identification (gap (2)). R1-R5 refer to `(u_E, u_T)` only as the
   linear functionals already named in the parent note; the
   identification with canonical bright coordinates of any bright/dark
   decomposition is not asserted.
3. The physical tensor-primitive bridge from `K_R` to the GR readout
   chain (gap (3)). R1-R5 are *structural identities of the symbol*
   `K_R` itself, not statements about its identification with any
   physical tensor primitive.

The parent row `s3_time_bilinear_tensor_primitive_note` remains
`open_gate` for all three named upstream theorem targets. The
positive-narrow-theorem addendum supplied here sharpens the carrier's
internal algebraic picture but does not promote the parent row.

## Distinct sub-problem (block-lane independence)

This note is distinct from prior blocks in the s3 lane:

- Block 02 (PR #1407) — AC_phi_lambda C3-foreclosure (different sub-row
  on a different downstream object).
- Block 07 (PR #1424) — background uniqueness `PL S^3 x R` + Hessian
  channel no-go (different scope: kinematics and dynamics bridge channel).
- Block 12 (PR #1440) — time-channel rigidity on the conditional
  coupling family `Xi_P(t; c) = (P_R c) ⊗ V_R(t)` (downstream object: the
  *coupling* of `K_R` to the slice generator, factoring time vs. space).

This block is on the **carrier `K_R` itself**, factoring *within the
carrier* between the scaling channel `w(q) = (1, delta_A1(q))^T` and the
bright channel `v(q) = (u_E(q), u_T(q))^T`. Both factorizations are
outer-product structural statements, but on different objects and in
different sectors.

## Bottom line (scope-bounded)

Under the named admitted inputs of the parent definition note, the
bilinear carrier symbol `K_R(q)` factors algebraically as the rank-1
outer product `w(q) v(q)^T` with `w(q) = (1, delta_A1(q))^T` and
`v(q) = (u_E(q), u_T(q))^T`. The five structural properties (R1)-(R5)
follow by polynomial identity and are verified at machine precision by
the paired runner on the same seven-site star support as the parent
runner.

The three named open theorem targets of the parent note remain upstream
and are explicitly re-cited:

1. retained-grade derivation of the `delta_A1`-decoupling fact;
2. retained-grade derivation of the aligned-bright coordinate
   identification;
3. retained-grade bridge theorem identifying `K_R` with a physical
   tensor primitive in the GR readout chain.

None of these is closed in this note. The contribution is the rank-1
outer-product factorization and the five structural identities only.
