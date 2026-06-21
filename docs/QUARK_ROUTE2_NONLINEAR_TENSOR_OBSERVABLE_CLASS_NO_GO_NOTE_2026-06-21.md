# Quark Route-2 Nonlinear Tensor-Observable Class No-Go

**Date:** 2026-06-21
**Status:** exact negative boundary / no-go; no endpoint derivation
**Claim type:** no_go
**Status authority:** branch-local physics-loop packet only. This note does
not set an audit verdict and does not update repo-wide authority surfaces.
**Primary runner:**
[`scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py)
(`PASS=31 FAIL=0`)
**Runner output:**
[`outputs/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.txt`](../outputs/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.txt)

## Scope

This note attacks the remaining Route-2 readout endpoint target

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4)
```

from the nonlinear/tensor-observable side. It proves a narrow negative result:
finite tensor-polynomial observables generated only from the
E-center-blind endpoint columns cannot select

```text
rho_E := beta_E / alpha_E = 21/4.
```

The result does **not** rule out arbitrary future nonlinear observables. It
only prunes a precise class: nonlinear closures that never evaluate the
missing E-center direction and never supply an equivalent source/readout
primitive.

## Minimal premise set

Allowed premises:

1. the exact restricted Route-2 endpoint columns
   ```text
   E-shell  = (1, 0, 0,   0)
   E-center = (1, 0, 1/6, 0)
   T-shell  = (0, 1, 0,   0)
   T-center = (0, 1, 0, 1/6)
   ```
2. the reduced readout family after granting the two T-side endpoint
   candidates,
   ```text
   P(rho_E) =
   [[1, 0, rho_E, 0],
    [0,-2, 0,     2]]
   ```
3. exact rational arithmetic, finite tensor products, polynomial closure, and
   scalar contractions;
4. the Route-2 factor-rigidity observation that the time factor in
   `Xi_P(t; c) = (P_R c) x V_R(t)` is universal across the admissible
   readout family.

Forbidden proof inputs:

1. observed quark masses, fitted Yukawa values, or CKM/`J` objectives;
2. nearest-rational selection from a live endpoint value;
3. a hidden E-center source weight;
4. a source-domain typed rule not already supplied by the current exact
   surface;
5. a nonlinear observable whose coefficients are chosen after seeing
   `rho_E = 21/4`.

## The blind tensor-polynomial class

Let

```text
B_blind = {E-shell, T-shell, T-center}.
```

Define the branch-local class `C_blind^poly` to contain every finite
observable obtained by:

1. applying `P(rho_E)` only to columns in `B_blind`;
2. taking finite tensor powers, mixed tensor words, dot products, determinants,
   norms, and finite polynomial combinations of those generator values;
3. optionally tensoring the resulting left/readout prefactor with the same
   universal time factor `V_R(t)`.

The class explicitly excludes any generator that evaluates `E-center`, any
source-domain rule that fixes the E-center endpoint weight, and any fitted
target comparator.

## Theorem

**Theorem.** Every observable in `C_blind^poly` is independent of `rho_E`.
Therefore no observable in this class can derive or select
`rho_E = 21/4`.

**Proof.** For every `rho_E`,

```text
P(rho_E) E-shell  = (1, 0)
P(rho_E) T-shell  = (0, -2)
P(rho_E) T-center = (0, -5/3).
```

The runner checks this at the generator level by extracting the affine
`rho_E` coefficient of each readout image. All three blind generators have
zero `rho_E` coefficient in both readout channels.

Finite tensor products and scalar contractions are built from products and
sums of those generator coordinates. Since the generator coordinates are
constant in `rho_E`, every finite tensor word, tensor power, contraction, and
polynomial in them is also constant in `rho_E`. Tensoring with the universal
Route-2 time factor does not change this conclusion: the unresolved readout
ambiguity lives only in the left/spatial prefactor.

By contrast,

```text
P(rho_E) E-center = (1 + rho_E/6, 0).
```

The unique varying generator is precisely the missing E-center lift direction

```text
E-center - E-shell = (0, 0, 1/6, 0).
```

So any nonlinear observable that actually selects `rho_E` must contain a
nonblind generator or an equivalent primitive.

## Exact endpoint equivalence

Under the granted T-side data, the target is exactly equivalent to the
E-center lift:

```text
rho_E = 21/4
<=> q_E = gamma_E(center)/gamma_E(shell) = 15/8
<=> gamma_T(center)/gamma_E(center) = -8/9.
```

The runner verifies:

```text
1 + (21/4)/6 = 15/8
(-5/3) / (15/8) = -8/9
```

and conversely solving `q_E = 15/8` gives `rho_E = 21/4`.

## Consequence

This block narrows the nonlinear-observable escape left open by the quadratic
Schur no-go. A future genuinely nonlinear tensor observable remains a valid
positive route, but only if it is not in `C_blind^poly`. In practical terms,
it must supply at least one of:

1. an explicit E-center lift;
2. a source-domain rule that fixes the E-center endpoint weight;
3. a readout-map primitive that evaluates the missing fourth carrier
   direction;
4. a different up-sector scalar-law route outside Route-2 endpoint readout.

Nonlinearity alone is not the missing ingredient. The missing ingredient is
E-center sensitivity.

## Relation to parent rows

The parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
remains an open gate because its unique coupling theorem still depends on the
upstream readout endpoint triple. This note does not close that gate. It
sharpens the no-go memory for one tempting repair family: tensor-polynomial
nonlinear observables that inherit the same E-center blindness.

The factor-rigidity note already localizes the remaining ambiguity in the
spatial readout prefactor. This note adds that finite polynomial/tensor
manipulation of blind prefactors cannot create the missing E-center
coordinate.

## No-go discipline gate

**N1. Alternative routes tested.** The runner separates carrier geometry,
finite tensor powers through degree 6, representative nonlinear polynomial
probes, Route-2 time-factor separation, and parent-surface anchor checks. All
agree that the blind class is invariant under changing `rho_E`.

**N2. Wall independence.** The wall is generator-level: the blind set has no
`rho_E` coefficient. Tensor powers and nonlinear polynomials preserve that
wall because they are algebraic closure operations on constant generators.

**N3. Hidden-wall scan.** The two T-side candidates are explicit conditional
premises. No observed mass, fitted target, live endpoint, nearest-rational
selection, or unregistered E-center source weight is used.

**N4. Residual matching.** The residual is the same one named by the exact
readout map, naturality no-go, E-center blindness no-go, and parent
theta-to-slice row: the missing E-channel endpoint entry
`rho_E = beta_E / alpha_E`.

**N5. Rhetoric audit.** "Cannot derive" means "cannot derive from
`C_blind^poly`." The note does not claim that all future nonlinear observables
or source-domain repairs are impossible.

**N6. Partial-closure path scan.** The positive path is now sharper: construct
a nonlinear observable whose generator set includes the E-center direction or
prove a source/readout primitive that is equivalent to that lift.

**N7. Steelman.** A hostile reviewer should try to exhibit a named nonlinear
observable that secretly evaluates E-center or imports a source-domain
E-center rule. If successful, that observable is outside `C_blind^poly` and
becomes a positive repair candidate rather than a counterexample to this
no-go.

**N8. Cross-cycle echo.** This block is consistent with the April exact readout
map obstruction, the April naturality no-go, the June quadratic Schur no-go,
and the June E-center blindness no-go. Its new content is the explicit
finite tensor-polynomial propagation of the blind-generator invariance.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_tensor_observable_class_no_go_2026_06_21.py
```

Current expected result:

```text
TOTAL: PASS=31, FAIL=0
```

This check is exact rational arithmetic except for no floating-point
calculation at all; it uses the parent notes only as scope anchors.
