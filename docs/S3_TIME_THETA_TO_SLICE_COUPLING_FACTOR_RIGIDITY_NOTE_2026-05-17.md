# s3-Time Theta_R -> Lambda_R Coupling: Factor-Rigidity Theorem

**Type:** positive_theorem (narrow scope)
**Status:** scope-bounded positive closure on a structural property of the
existing conditional coupling family.  Does **not** close the parent
`open_gate` row `s3_time_theta_to_slice_coupling_note`.
**Date:** 2026-05-17
**Branch:** `physics-loop/s3-time-theta-to-slice-coupling-block12-2026-05-17`
**Authority role:** records a structural rigidity property of the
conditional `Theta_R -> Lambda_R` coupling family that holds under any
admissible readout in the 1-parameter family `P(rho_E)`.  Names the
upstream readout-triple as the still-open theorem target.
**Status authority:** independent audit lane only.

## Scope and audit boundary

This note proves a **structural rigidity property** of the conditional
coupling family

```text
Xi_P(t ; c) = (P_R c) ⊗ V_R(t),     V_R(t) = exp(-t Lambda_R) u_*
```

introduced by the cited Route-2 time-coupling authority.  It does **not**
derive the unresolved readout-triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4),
```

so it does **not** close the parent open_gate row.  Instead it proves a
strictly weaker positive statement: the unresolved readout ambiguity is
**structurally localized in the spatial prefactor** of the family, and the
time-channel structure is universal across the entire admissible class.

This is a narrow positive theorem.  Its purpose is to sharpen the
structural picture of the row, not to bypass the upstream no-go.

## Cited authorities (one-hop deps; cited but not closed in this note)

- [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_clean`) —
  canonical Route-2 slice backbone authority.  Supplies the exact slice
  generator `Lambda_R`, transfer `T_R = exp(-Lambda_R)`, and seed law
  `V_R(t) = exp(-t Lambda_R) u_*`.  Imported as the slice-backbone
  authority.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  (`claim_type: no_go`, `audit_status: audited_clean`) — canonical
  Route-2 readout-map authority.  Supplies the exact bilinear carrier
  `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`, the restricted
  bright readout class, and the audited-clean no-go on the endpoint
  triple.  Imported as the readout-class authority and as the canonical
  statement of the obstruction this row still inherits.
- [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  (`claim_type: open_gate`) — parent row this note attaches to.  This
  note adds a structural-rigidity addendum; the parent remains open_gate
  because the upstream readout-triple is still not derived.

## Setup

The cited authorities give the following exact ingredients on the live
Route-2 surface:

- exact slice backbone `Lambda_R` (SPD), `T_R = exp(-Lambda_R)`,
  `V_R(t) = exp(-t Lambda_R) u_*`,
- exact restricted carrier `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`,
- exact 1-parameter admissible readout family
  ```text
  P(rho_E) = [[1, 0, rho_E, 0],
              [0, -2, 0, 2]]
  ```
  with `rho_E = beta_E / alpha_E` the irreducible undetermined entry.

## Theorem (factor rigidity)

For every admissible readout `P_R = P(rho_E)` in the 1-parameter family
above, the conditional family `Xi_P(t ; c) = (P_R c) ⊗ V_R(t)` on the
restricted carrier class satisfies the following five structural
properties simultaneously:

- **(F1) Lambda_R is readout-independent.**  `Lambda_R` is constructed
  from the Schur boundary alone; no readout-map data enters its
  definition.  Equivalent reconstruction from the same Schur
  construction agrees to `EXACT_TOL`.
- **(F2) V_R(t) is readout-independent.**  Because `V_R(t)` is built from
  `Lambda_R` and a canonical seed, the entire time-axis trajectory
  `t -> V_R(t)` is independent of the choice of admissible `P_R`.  This
  is the consequence of (F1).
- **(F3) Norm-ratio invariance.**  For every admissible `P_R` and every
  carrier column `c` with `(P_R c) != 0`,
  ```text
  || Xi_P(t1 ; c) || / || Xi_P(t2 ; c) ||  =  || V_R(t1) || / || V_R(t2) ||,
  ```
  i.e. the time-attenuation ratio depends only on `Lambda_R` and is
  therefore universal across the admissible class.  The `P_R`-dependent
  prefactor `||(P_R c)||` cancels.
- **(F4) Semigroup commutation.**  The one-step transfer `T_R` acts
  exclusively on the time-channel:
  ```text
  Xi_P(t ; c) T_R^T  =  Xi_P(t + 1 ; c)
  ```
  (treating `Xi_P` as a `2 x dim` matrix with rows indexed by
  `P_R c`-components and columns by slice indices).  This identity holds
  for every admissible `P_R` and every carrier column `c`, including
  carrier columns on which the readout ambiguity is non-trivial.
- **(F5) Rank-1 ambiguity along time.**  For any two distinct admissible
  readouts `P_a = P(rho_E^a)` and `P_b = P(rho_E^b)`, the difference
  ```text
  Xi_a(t ; c) - Xi_b(t ; c) = ((P_a - P_b) c) ⊗ V_R(t)
  ```
  is a rank-1 outer product whose right factor is the universal
  time-trajectory `V_R(t)`.  The readout ambiguity is therefore
  **structurally localized** in the spatial prefactor; the time-channel
  is shared by every admissible `P_R`.

## Proof sketch

(F1) `Lambda_R` is constructed from the Schur DtN matrix as
`Lambda_R := 1/2 (Lambda + Lambda^T)` with `Lambda` produced by
`schur.schur_dtn_matrix(...)`.  The construction has no readout-map
input.  This is a definitional check; the runner confirms it numerically
by rebuilding `Lambda_R` from the same construction and comparing to
`EXACT_TOL`.

(F2) `V_R(t) = exp(-t Lambda_R) u_*` with `u_*` a canonical seed.  Both
ingredients are defined from `Lambda_R`, which is readout-independent by
(F1).  Hence `V_R(t)` is readout-independent.

(F3) For any `c` with `(P_R c) != 0`,
```text
|| Xi_P(t ; c) ||^2 = || (P_R c) ||^2 || V_R(t) ||^2
```
by the outer-product norm identity.  Dividing two such expressions, the
`|| (P_R c) ||` factor cancels and the ratio is `|| V_R(t1) || / || V_R(t2) ||`,
which is `P_R`-independent by (F2).

(F4) For any 2-by-d matrix `M = a ⊗ v` (with `a` length-2 and `v` length-d),
right-multiplication by `T_R^T` acts only on the second tensor factor:
```text
M T_R^T = a ⊗ (T_R v).
```
For `Xi_P(t; c) = (P_R c) ⊗ V_R(t)`, this gives
```text
Xi_P(t; c) T_R^T = (P_R c) ⊗ (T_R V_R(t)) = (P_R c) ⊗ V_R(t + 1) = Xi_P(t+1; c)
```
where the middle equality uses the semigroup property
`T_R V_R(t) = V_R(t+1)`.

(F5) `Xi_a(t; c) - Xi_b(t; c) = (P_a c) ⊗ V_R(t) - (P_b c) ⊗ V_R(t)
    = ((P_a - P_b) c) ⊗ V_R(t)` by bilinearity of the outer product.
The result is a rank-1 outer product with right factor `V_R(t)`.

## Relation to the parent row and to block 07

This note is strictly downstream of block 07's positive substep on the
parent row:

- Block 07 (PR #1424) closed `Claim A` (background uniqueness `PL S^3 x R`)
  and `Claim B` (Hessian-channel structural no-go) on the open_gate
  parent `S3_ANOMALY_SPACETIME_LIFT_NOTE`.
- This note closes a structural rigidity addendum on a downstream row
  `s3_time_theta_to_slice_coupling_note` whose conditional family lives
  on the same `PL S^3 x R` background.  The rigidity properties (F1)-(F5)
  separate the spatial readout ambiguity from the universal time-channel
  on that background.

(F1)-(F5) are **independent of** and **do not bypass** the upstream
readout-triple no-go from `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE`.  The
ambiguity in the readout triple still blocks a unique exact
`Theta_R -> Lambda_R` coupling.  The parent `open_gate` is **not** closed
by this note; it is, however, structurally sharpened.  The new statement
that can be made on the row is:

> The remaining ambiguity is rank-1 along the time-axis and is localized
> entirely in the spatial readout prefactor.  Any future derivation of
> the readout-triple immediately collapses the conditional family to a
> unique exact coupling.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
```

Current expected result on this branch:

- `frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py`: `PASS=64 FAIL=0`

All five property families pass with residuals at floating-point
precision (typical residual `~1e-16`, worst observed `~9e-16`).  No
property requires the readout-triple to be derived; every check holds for
arbitrary `rho_E` in the admissible 1-parameter family.

## Effect on row state

- Parent row `s3_time_theta_to_slice_coupling_note` remains `open_gate`
  because the upstream readout-triple is still not derived.
- This addendum adds a positive narrow theorem (`positive_theorem`,
  scope-bounded) on a structural property of the conditional family
  that holds for the entire admissible class.
- Next theorem target is unchanged: the missing readout-map endpoint
  triple, which lives on
  [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md),
  not on this row.

## Honest endpoint

- Five-property factor-rigidity theorem on the conditional family
  `Xi_P(t; c) = (P_R c) ⊗ V_R(t)`,
- valid for every admissible readout in the 1-parameter family
  `P(rho_E)`,
- proves the time-channel is universal across the admissible class and
  the readout ambiguity is rank-1 along the time-axis.
- Does **not** derive the readout-triple; does **not** close the parent
  open_gate row.
- Inherited from the cited Route-2 readout-map no-go: the unique exact
  `Theta_R -> Lambda_R` coupling theorem is still **not** closed on
  `main`.
