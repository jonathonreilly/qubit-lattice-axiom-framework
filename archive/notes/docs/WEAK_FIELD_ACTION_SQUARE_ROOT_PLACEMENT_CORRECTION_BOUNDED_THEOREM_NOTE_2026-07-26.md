# Weak-Field Action Square-Root Placement Correction

**Date:** 2026-07-26
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** exact leading-order comparison of two distinct square-root action
forms, a source check identifying which form the original fixed-family probe
executes, and a bounded replay of the misstated form on that same family. No
action-selection mechanism or universal response law is claimed.
**Audit:** unset; the independent audit lane owns `audit_status` and
`effective_status`.
**Primary runner:**
[`scripts/frontier_weak_field_action_square_root_placement_correction_2026_07_26.py`](../scripts/frontier_weak_field_action_square_root_placement_correction_2026_07_26.py)
(5 PASS / 0 FAIL, exit 0).
**Cache:**
[`logs/runner-cache/frontier_weak_field_action_square_root_placement_correction_2026_07_26.txt`](../logs/runner-cache/frontier_weak_field_action_square_root_placement_correction_2026_07_26.txt).

## Question

The bounded G-Newton sharpening note
[`G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md`](G_NEWTON_SELF_CONSISTENCY_BOUNDED_SHARPENING_NOTE_2026-05-10_planckP4.md)
(legacy probe nickname `planckP4`) pairs

```text
S = L sqrt(1 - phi)
```

with the fixed-family response exponent `F proportional to M^0.50`. The
referenced action probe, however, executes a different formula. Which
square-root placement belongs to the measured row?

For this comparison, `f` is the probe's nonnegative weak-field scalar and
`phi=f` is the notation alignment implicit in the source's claimed link to
that probe. If the source intends a different signed field or normalization,
then the quoted `0.50` probe row does not test its formula at all.

## Exact correction

The source function
[`action_value()`](../scripts/action_universality_probe.py) defines its
`valley_sqrt` branch as

```python
return L * (1.0 - np.sqrt(f))
```

Thus the measured `0.50` row belongs to

```text
S_measured = L(1 - sqrt(f)).
```

It does not belong to

```text
S_stated = L sqrt(1 - f).
```

The distinction is exact. Normalize an action as `g(f) = S/L` and define its
valley depth as `Delta(f) = 1 - g(f)`. Then

```text
Delta_measured(f) = sqrt(f),
Delta_stated(f)   = 1 - sqrt(1-f)
                  = f / (1 + sqrt(1-f))
                  = f/2 + f^2/8 + O(f^3).
```

The measured form has leading order `f^(1/2)`. The stated form has leading
order `f`, with coefficient `1/2`. In particular, the stated form and the
valley-linear action `L(1-f)` have the same order of vanishing, although they
are different functions.

The registered
[`action_universality_probe.txt`](../logs/runner-cache/action_universality_probe.txt)
cache reports the finite rows `L(1-sqrt(f)) -> 0.50` and
`L(1-f) -> 1.00`, together with other tested forms. This correction uses those
rows only as finite replay context. The original probe did not include
`L sqrt(1-f)`. The correction runner therefore injects exactly that one formula
into the otherwise unchanged fixed-family harness and obtains
`F proportional to M^0.999998`, `7/7` TOWARD responses, and machine-clean
Born residual. This is a bounded result on the reviewed family, not a
universal selection rule.

## The geometric spent-delay action is a third formula

The retained bounded crossover replay
[`ACTION_CROSSOVER_NOTE.md`](ACTION_CROSSOVER_NOTE.md) defines the geometric
spent-delay action by

```text
S_geo = dl - sqrt(dl^2 - L^2).
```

Writing `dl = L(1+epsilon)` gives

```text
S_geo/L = 1 + epsilon - sqrt(2 epsilon + epsilon^2),
Delta_geo = 1 - S_geo/L
          = sqrt(2 epsilon + epsilon^2) - epsilon
          = sqrt(2 epsilon) + O(epsilon).
```

Its normalized depth therefore has leading order `epsilon^(1/2)`. It shares
that order with `L(1-sqrt(f))`; it is not the same expression as either
`L(1-sqrt(f))` or `L sqrt(1-f)`.

## Consequence for the weak-field comparison

The G-Newton source comparison is not valid as written because it attaches a
measured result to an action the cited probe does not execute. At the narrower
level of leading normalized-depth order, `L(1-f)` and `L sqrt(1-f)` both have
order one. The direct fixed-family replay confirms that the latter gives an
order-one response exponent on the tested family, rather than the attached
`0.50`. Their coefficients, higher-order terms, or other observables can still
separate the two functions.

The measured sublinear comparator is `L(1-sqrt(f))`. This correction does not
derive that action, select it, or change the open status of the weak-field
action-selection problem.

## Claim ledger

| Claim | Direct support | Boundary / falsifier |
|---|---|---|
| The fixed-family probe's `valley_sqrt` branch is `L(1-sqrt(f))`. | The runner imports and evaluates `action_value()` from [`scripts/action_universality_probe.py`](../scripts/action_universality_probe.py). | Falsified if that source branch evaluates to a different function at the reviewed commit. |
| `L sqrt(1-f)` has normalized-depth leading order `f`, coefficient `1/2`. | Exact rationalization `1-sqrt(1-f)=f/(1+sqrt(1-f))` and an independent series/limit check. | Falsified if `Delta(f)/f` does not tend to `1/2` as `f -> 0+`. |
| `L(1-sqrt(f))` has normalized-depth leading order `f^(1/2)`. | Exact identity `Delta(f)=sqrt(f)` and source evaluation. | Falsified if the normalized depth differs from `sqrt(f)`. |
| `L sqrt(1-f)` gives an order-one response exponent on the reviewed fixed family. | The runner reuses the original lattice, detector, field, propagation, and measurement code while replacing only the action formula; it obtains `0.999998`. | Falsified by a deterministic replay on the same source revision and parameters that does not reproduce the stated row within the runner tolerance. |
| The geometric spent-delay depth has leading order `epsilon^(1/2)`. | Exact substitution into the retained bounded crossover formula and an independent limit check. | Falsified if `Delta_geo/sqrt(2 epsilon)` does not tend to `1`. |
| Leading order alone does not separate the two order-one forms. | Both exact limits above are finite and nonzero after division by `f`. | This is only an order-of-vanishing statement; coefficients, higher-order terms, and other observables remain outside its scope. |

## Imports and non-claims

- No measured or fitted value is used to derive either leading order.
- The `0.50` value is quoted only as the output label of the existing
  fixed-family replay.
- The explicit `phi=f` notation alignment is used only to test the source's
  claimed comparison; it is not a field-identification theorem.
- No primitive, axiom, normalization, boundary condition, or external
  literature input is added.
- No audit verdict, lane status, or publication status is changed.
- No universal relation between action order and response exponent is claimed.

## Reproduction

```bash
python3 scripts/frontier_weak_field_action_square_root_placement_correction_2026_07_26.py
```

Expected result: `5 PASS / 0 FAIL`.
