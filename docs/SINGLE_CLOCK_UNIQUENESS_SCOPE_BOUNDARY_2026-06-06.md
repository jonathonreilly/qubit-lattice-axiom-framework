# Single-Clock Uniqueness Scope Boundary

**Date:** 2026-06-06
**Claim type:** no-go / scope-repair boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_single_clock_uniqueness_scope_boundary_2026_06_06.py`](../scripts/frontier_single_clock_uniqueness_scope_boundary_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_single_clock_uniqueness_scope_boundary_2026_06_06.txt`](../logs/runner-cache/frontier_single_clock_uniqueness_scope_boundary_2026_06_06.txt).

## Targeted Review Gate

This block targets the active review item
`2026-05-20-single-clock-uniqueness-negative-gate` in
[`docs/repo/ACTIVE_REVIEW_QUEUE.md`](repo/ACTIVE_REVIEW_QUEUE.md).

The review finding is that a broad no-spatial-reflection-positivity /
no-second-clock uniqueness proof was not landed because it was a broad negative
claim with unaudited dependencies and no no-go-discipline checklist.

## Result

The already-narrow finite-dimensional Stone theorem has a clean valid scope:

```text
given one positive Hermitian transfer T and a fixed positive scale tau,
H = -(1/tau) log(T) is unique.
```

This does **not** by itself prove:

- the time scale `tau` is fixed by `T`;
- no other positive transfer matrix exists;
- no other reflection-positive axis exists;
- no independent commuting one-parameter group exists on a tensor factor;
- the framework has a framework-wide one-clock exclusion theorem.

Therefore the safe repair is:

```text
Stone uniqueness is transfer-relative and tau-relative.
No-second-clock requires a separate axis/transfer uniqueness premise.
```

## Exact Boundary

The runner verifies three facts exactly.

### 1. Fixed `T,tau` gives a unique generator

For a positive diagonal transfer

```text
T = diag(1/2, 1/3)
```

and fixed `tau=1`, the generator

```text
H_1 = -log(T)
```

reconstructs `T`, and `U(t)=exp(-itH_1)` is a one-parameter unitary group with
generator `H_1`.

### 2. `T` alone does not fix the clock unit

The same `T` is also reconstructed with `tau=2` and

```text
H_2 = -(1/2) log(T) = H_1/2.
```

Thus `T` fixes the product `tau H`, not a physical clock normalization by
itself. A time-unit or blocked-time-spacing bridge is an extra premise.

### 3. Multiple supplied transfers are compatible with finite Stone theory

On a tensor product, two positive transfers

```text
T_A = diag(1/2,1/3),      T_B = diag(1/5,1/7)
```

lift to commuting positive transfers `T_A ⊗ I` and `I ⊗ T_B`, with commuting
generators. Their product has the summed generator for a chosen common `tau`,
but Stone uniqueness for that product does not erase the factor groups. It only
says that the product transfer has a unique generator once the product transfer
and `tau` are supplied.

## No-Go Discipline Checklist

Any future no-second-clock claim must state and check at least:

- **N1:** the exact supplied transfer matrix or transfer family;
- **N2:** the physical time step / block spacing `tau`;
- **N3:** positivity and trivial-kernel domain for the transfer;
- **N4:** uniqueness of the reflection-positive axis or transfer construction;
- **N5:** exclusion of independent commuting transfer factors if the claim says
  no second clock;
- **N6:** whether tensor-product factor clocks are gauge, redundant, or
  physically excluded;
- **N7:** which dependencies are current-surface authority and which are
  branch-local support;
- **N8:** the narrow status: transfer-relative Stone uniqueness versus broad
  framework no-second-clock.

This block supplies a no-go for skipping N2/N4/N5.

## Boundaries

- Does not reject the narrow finite-dimensional Stone theorem.
- Does not derive or disprove reflection positivity.
- Does not prove a second physical clock exists in the framework.
- Does not prove a framework-wide one-clock exclusion theorem.
- Does not update repo-wide review or authority surfaces.

## Runner Summary

Expected scorecard:

```text
PASS=19 FAIL=0
```
