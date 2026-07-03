# Conditional Order Separation for Gravity-Sign LV Corrections

**Date:** 2026-06-08
**Type:** bounded conditional order-counting theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.py`](../scripts/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.py)
**Runner cache:** [`logs/runner-cache/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.txt`](../logs/runner-cache/gravity_sign_bottom_leading_order_decouples_from_lv_2026_06_08.txt)

## Statement

Assume a supplied effective TT kernel has a nonzero leading two-derivative
coefficient `c2` and a cubic-anisotropy correction that first enters at the
next even order:

```text
omega^2(k) = c2 |k|^2 (1 + alpha A4(khat) |k|^2).
```

For any finite `alpha`, the strict `k -> 0` sign of
`omega^2(k)/|k|^2` is `sign(c2)`. The `alpha A4 |k|^2` term is subleading in
that limit and cannot, by itself, change the sign of the supplied leading
coefficient.

This is a useful order-separation lemma. It says that a genuinely `O(k^4)`
cubic-anisotropy correction is not the same datum as a supplied `O(k^2)`
kinetic-sign coefficient. It does not derive `c2`, its sign, leading isotropy,
the physical TT kernel, or the emergent dynamical metric.

## Runner-Verified Result

The runner checks four finite algebraic/numerical facts:

- **B1:** for sampled finite `alpha`, `omega^2/|k|^2 -> c2` as `|k| -> 0`
  when `c2` is supplied.
- **B2:** the relative LV contribution scales as `|k|^2`, so the correction to
  `omega^2` is `O(k^4)` on this model.
- **B3:** changing the sign of the supplied `c2` changes the strict leading
  sign; the runner therefore depends on `c2` being supplied by other physics.
- **B4:** the source note contains the guardrails that the broad wall-relocation
  claim is not landed.

`TOTAL: PASS=4 FAIL=0`.

## What This Establishes

Under the explicit model assumptions above, a finite higher-derivative
cubic-anisotropy coefficient does not alter the strict leading sign. This can
be used as a local algebraic support fact in later gravity-sign work if that
work independently supplies:

- a physical TT kernel;
- a nonzero positive `O(k^2)` coefficient;
- leading isotropy of that coefficient;
- the reflection-positivity/sign bridge being invoked;
- the dynamical metric or edge-length degree of freedom on which the effective
  action is meant to live.

## What This Does Not Establish

This note does **not** prove:

- `G > 0`;
- that the framework already has the needed leading `SO(3)` or Lorentz
  structure for gravity;
- that reflection positivity fixes the gravity sign on the target physical
  kernel;
- that the catch-22 or Lorentz-naturalness gap is irrelevant to the gravity
  program;
- that all Lorentz-violating terms begin at `O(k^4)`;
- that mixing, nonlocality, relevant/marginal LV operators, gauge constraints,
  source/action normalization, or an emergent dynamical metric are supplied;
- that the bare lattice, Record axiom, scale-reference primitive, or kinetic
  isotropy primitive supplies the missing dynamical metric.

## No-Go Discipline Gate

The submitted PR claimed a broad bottom relocation: the gravity sign does not
need IR-exact Lorentz and the remaining bottom is only the emergent dynamical
metric. That broad claim is **not landed**.

- **N1 alternative routes:** at least five routes remain open: derive `c2>0`;
  derive the physical TT kernel; prove all lower-order LV terms are absent;
  control constrained/gauge mixing; supply the dynamical metric. The runner
  tests none of these.
- **N2 wall independence:** `c2` sign, leading isotropy, RP-to-gravity-sign,
  LV spectrum, and dynamical metric are independent walls; none follows from
  the toy order-counting lemma.
- **N3 hidden-wall scan:** phrases like "framework has" and "RP fixes" were
  hidden admissions in the submitted text. They are now explicit assumptions.
- **N4 residual matching:** the naturalness-gap witness concerns LV correction
  size. This note only separates a modeled `O(k^4)` correction from a supplied
  `O(k^2)` coefficient.
- **N5 rhetoric audit:** "cannot flip the sign" is narrowed to "cannot change
  the strict `k -> 0` sign of a supplied nonzero `c2` in this model."
- **N6 partial-closure scan:** approved axioms and primitives do not supply the
  dynamical metric, source/action normalization, or gravity-sign bridge.
- **N7 steelman:** a lower-order LV operator, constrained-mode mixing, or a
  wrong supplied `c2` sign would break the broad claim while leaving this toy
  order-counting result intact.
- **N8 cross-cycle echo:** prior Lorentz/naturalness walls are not retired by
  this lemma; they are only separated from one specific modeled leading-sign
  question.

Result: the no-go/bottom-relocation claim fails the gate and is demoted to this
conditional bounded theorem.
