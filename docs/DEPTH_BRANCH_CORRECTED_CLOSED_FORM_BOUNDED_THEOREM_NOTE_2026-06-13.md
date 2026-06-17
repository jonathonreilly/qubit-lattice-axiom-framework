# Depth Branch-Corrected Laurent Roots for Four L = 3 Depth-Tail States

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_depth_branch_corrected_closed_form_2026_06_13.py`
**Runner cache:** `logs/runner-cache/frontier_depth_branch_corrected_closed_form_2026_06_13.txt`
**Status:** source proposal; the audit lane grades.
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome and does not edit audit-owned registry, ledger, queue,
or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Claim

For the four deterministic zB `L=3` state records `K3`, `K4`, `K5`, and `K6`
defined by the runner, the principal-branch depth tail is reproduced by the
branch-corrected determinant root configuration.

Let

```text
F(q) = q^-3 c prod_j(q-r_j), q = exp(i theta), delta = 3*tau = 1.05.
```

The unwrapped root sum is

```text
u(theta) = -3 delta
         + sum_j unwrap Arg((q exp(i delta)-r_j)/(q-r_j)).
```

The correction missing from the unwrapped root-sum comparator is the integer
principal-branch jump function

```text
J(theta) = round((u(theta) - Arg(exp(i u(theta))))/(2*pi)).
```

The branch-corrected closed form is

```text
g(theta) = u(theta) - 2*pi J(theta) - mean_theta[u(theta) - 2*pi J(theta)].
```

The normalized ladder weights are `w_k = |Fourier_k(g)|^2 / sum_l |Fourier_l(g)|^2`,
combined by absolute harmonic index, and

```text
T_ge3 = sum_{k>=3} w_k.
```

## Input Boundary

The state records, seeds, `L=3` lattice, `N_c=3`, `tau=0.35`, and site-01
determinant-polar readout are supplied finite inputs in this runner. This note
does not derive those states from the repo axioms, does not claim they are
physically selected records, and does not claim an all-`L` depth law. It only
records the finite branch-corrected root identity for these four supplied state
records.

## Deterministic References

The runner recomputes the real determinant-polar phase increments before
checking the frozen reference values; the references are not used to construct
the branch-corrected result.

| state | measured `T_ge3` | branch-corrected `T_ge3` |
| --- | ---: | ---: |
| `K3` | `0.36642131754352519` | `0.3664213175435248` |
| `K4` | `0.81620884399822058` | `0.81620884399822091` |
| `K5` | `0.22542121070372184` | `0.22542121070372706` |
| `K6` | `0.010321210053125331` | `0.010321210053125191` |

The measured and branch-corrected ordering is

```text
K6 < K5 < K3 < K4
```

## Branch Structure

The winding is fixed by the argument principle for `q^3 F(q)`:

```text
winding(F) = N_inside - 3.
```

| state | root split `(inside,outside)` | winding | branch jump levels | jump count |
| --- | ---: | ---: | ---: | ---: |
| `K3` | `(3,3)` | `0` | `(0,)` | `0` |
| `K4` | `(4,2)` | `+1` | `(0,1)` | `2` |
| `K5` | `(3,3)` | `0` | `(0,)` | `0` |
| `K6` | `(2,4)` | `-1` | `(0,)` | `0` |

`K4` is the branch-incomplete comparator case: the unwrapped root sum gives
`T_ge3 = 0.10757177137114443`, while the measured principal-branch value is
`0.81620884399822058`. The two `2*pi` jumps in `J(theta)` close that gap without
a fitted scalar prefactor.

## Gates

The runner recomputes the four supplied state records, reconstructs the Laurent
determinant on held-out points, checks the root split and winding by the
argument principle, verifies the branch-corrected principal values and
harmonic weights, and includes a cross-state falsifier that `K5` roots reproduce
`K5` rather than snapping to the `K4` target.

```text
TOTAL: PASS=49 FAIL=0
```

## Scope

This is an exact finite `L=3` state-record result. It does not claim an all-`L`
theorem. The proposed claim is the branch-corrected principal-Arg closed form
for the four supplied zB state records, including the `K4` branch-wrapping case.
The audit lane grades.
