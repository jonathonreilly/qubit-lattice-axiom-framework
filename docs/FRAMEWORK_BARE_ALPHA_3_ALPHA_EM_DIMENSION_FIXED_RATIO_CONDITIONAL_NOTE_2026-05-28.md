# Framework Bare Alpha_3 / Alpha_em Dimension-Fixed Ratio Conditional Note

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; independent audit owns
`claim_type`, `audit_status`, and effective status.
**Primary runner:** [`scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py`](../scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py)

## Purpose

The archived predecessor
`archive_unlanded/framework-bare-alpha-assumed-input-salvage-2026-04-30/FRAMEWORK_BARE_ALPHA_3_ALPHA_EM_DIMENSION_FIXED_RATIO_SUPPORT_NOTE_2026-04-25.md`
failed as a retained-grade support claim because its verifier required an
EW-normalization authority that no longer exists in that form. The exact
algebra was not the problem. This note recovers only the conditional algebraic
content and binds it to the current EW kappa-family boundary.

## Conditional Algebra

Assume the bare bookkeeping inputs

```text
g_3^2 = 1,
g_2^2 = 1/(d + 1),
g_Y^2 = 1/(d + 2),
1/g_em^2 = 1/g_2^2 + 1/g_Y^2.
```

Then

```text
g_em^2 = 1/(2d + 3),
alpha_3(bare) / alpha_em(bare) = 2d + 3.
```

At `d = 3`, this gives

```text
g_em^2 = 1/9,
alpha_3(bare) / alpha_em(bare) = 9,
sin^2(theta_W)(bare) = 4/9.
```

The exact offset from the SU(5) weak-angle value is

```text
4/9 - 3/8 = 5/72.
```

## Current Boundary

The active electroweak surface is the kappa-family/no-go boundary in
[`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md).
That row does not derive the connected-trace specialization
`kappa_EW = 0`; it preserves the family
`K_EW(kappa_EW)` and records what remains open. This note therefore does not
claim a retained EW-normalization theorem or a direct low-energy observable.

## Re-Audit Scope

Audit this as conditional exact algebra plus current-boundary hygiene. The
old support claim should remain archived. The recovered science is useful
because it keeps the dimension-fixed integer fingerprint available without
laundering the missing EW selector into an authority premise.
