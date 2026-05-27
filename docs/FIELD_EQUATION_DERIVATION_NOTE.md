# Field Equation Variational Identity For A Stipulated Quadratic Graph Action

**Status:** support - structural or confirmatory support note
**Date:** 2026-04-11
**Primary runner:** scripts/frontier_field_equation_uniqueness.py
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The variation of the chosen action algebraically gives the screened Poisson equation, but the packet does not close the missing bridge that this chosen action is uniquely forced by the framework rather than assumed. The included runner also"*

with repair: *"missing_bridge_theorem: provide a restricted-class uniqueness theorem deriving the local quadratic field action, including why the mass term and source coupling are selected rather than assumed."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** Within the restricted class of local, quadratic, positive-definite graph field actions, the Euler-Lagrange variation of the stated action algebraically and uniquely yields the screened Poisson equation `(L + mu^2 I) Phi = G rho`; this derivation is exact and constitutes the runner-verified content.
- **NON-load-bearing (split off / admitted):** The selection of the local quadratic action form itself — specifically why the mass term and source coupling are chosen and not derived from the framework axioms — is an assumed premise rather than a retained, derived result; this uniqueness-forcing bridge remains an admitted, non-load-bearing input until a retained restricted-class uniqueness theorem for the action is supplied.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Scope Repair

The previous row mixed two claims:

1. a correct algebraic fact: varying the displayed quadratic graph-field
   action gives the screened Poisson equation; and
2. a stronger selection claim: the framework uniquely forces that action and
   therefore uniquely forces the field equation.

The audit accepted the algebraic variational calculation but rejected the
selection claim. The context runner also reports that multiple field operators
pass the tested consistency battery, so the current packet does not supply a
uniqueness theorem.

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
- It does not add a new axiom or apply an audit verdict.

## Relation To Self-Consistency Preference

[SELF_CONSISTENCY_FORCES_POISSON_NOTE.md](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
is retained-bounded as a finite operator-preference result on its tested
surface. It supports why Poisson-type operators are scientifically useful in
the current framework, but it explicitly is not a full uniqueness theorem.

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
