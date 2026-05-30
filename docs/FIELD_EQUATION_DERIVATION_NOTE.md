# Field Equation Variational Identity For A Stipulated Quadratic Graph Action

**Date:** 2026-04-11; scope repair 2026-05-27
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_field_equation_variational_scope_repair.py`

## Source Boundary

This row proves only that the displayed finite graph action has the stated
Euler-Lagrange equation. It does not derive or uniquely select that action,
mass term, or source coupling from the framework axioms.

## Scope Repair

The previous row mixed two claims:

1. a correct algebraic fact: varying the displayed quadratic graph-field
   action gives the screened Poisson equation; and
2. a stronger selection claim: the framework uniquely forces that action and
   therefore uniquely forces the field equation.

The algebraic variational calculation is correct, but the selection claim is
not supplied here. The context runner also reports that multiple field
operators pass the tested consistency battery, so the current packet does not
supply a uniqueness theorem.

This repaired row keeps only the exact variational identity.

## Stipulated Action

Let `G = (V,E,w)` be a finite undirected weighted graph and let `L` be its
weighted graph Laplacian:

```text
(L Phi)_i = sum_j w_ij (Phi_i - Phi_j).
```

For real field values `Phi_i`, source density `rho_i`, coupling `G_c`, and
screening parameter `mu^2 >= 0`, define the action

```text
S[Phi]
  = 1/2 sum_(i,j in E) w_ij (Phi_i - Phi_j)^2
    + (mu^2/2) sum_i Phi_i^2
    - G_c sum_i rho_i Phi_i.
```

Equivalently, with the standard `1/2 Phi^T L Phi` graph-gradient convention,

```text
S[Phi] = 1/2 Phi^T (L + mu^2 I) Phi - G_c rho^T Phi.
```

## Theorem

For the stipulated action above,

```text
grad_Phi S = (L + mu^2 I) Phi - G_c rho.
```

Therefore every stationary point satisfies

```text
(L + mu^2 I) Phi = G_c rho.
```

If `mu^2 > 0`, then `L + mu^2 I` is strictly positive definite on every finite
graph, so the stationary point is unique. If `mu^2 = 0`, the equation is the
unscreened Poisson equation on the charge-neutral / gauge-fixed subspace; the
constant mode remains the usual Laplacian kernel.

## Proof

The weighted graph-gradient term is

```text
1/2 sum_(i,j in E) w_ij (Phi_i - Phi_j)^2 = 1/2 Phi^T L Phi.
```

Because `L` is symmetric,

```text
d/dPhi [1/2 Phi^T L Phi] = L Phi.
```

The mass term contributes

```text
d/dPhi [(mu^2/2) Phi^T Phi] = mu^2 Phi.
```

The source term contributes

```text
d/dPhi [-G_c rho^T Phi] = -G_c rho.
```

Adding the three derivatives gives

```text
grad_Phi S = (L + mu^2 I) Phi - G_c rho.
```

Stationarity `grad_Phi S = 0` gives the screened Poisson equation. This proves
the bounded variational identity for the stipulated action.

## What This Claims

- Exact finite-graph Euler-Lagrange algebra for the displayed action.
- Positive-definite uniqueness of the stationary solution when `mu^2 > 0`.
- The unscreened `mu^2 = 0` boundary has the expected constant-mode gauge
  freedom.

## What This Does Not Claim

- It does not derive the quadratic action from axioms.
- It does not prove that the mass term is selected rather than supplied.
- It does not prove that the source coupling is selected rather than supplied.
- It does not prove uniqueness among all local, nonlocal, higher-derivative,
  heat-kernel, or self-consistent field operators.
- It does not derive Einstein's equation or a full relativistic field law.
- It does not add a new axiom.

## Relation To Self-Consistency Preference

[SELF_CONSISTENCY_FORCES_POISSON_NOTE.md](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
is a bounded finite operator-preference result on its tested surface. It
supports why Poisson-type operators are scientifically useful in the current
framework, but it explicitly is not a full uniqueness theorem.

This row is therefore a companion bounded identity: if the displayed action is
the action under review, then the screened Poisson equation follows exactly.
Selecting that action remains a separate science target.

## Verification

Run:

```bash
python3 scripts/frontier_field_equation_variational_scope_repair.py
```

Expected:

```text
SUMMARY: PASS=21 FAIL=0
```
