# Koide First-Order Selector Bounded Localization Certificate

**Date:** 2026-06-18
**Claim type:** bounded_theorem / no-go demarcation
**Status:** source-side bounded-localization certificate; independent audit required.
**Primary runner:** `scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py`
**Runner cache:** `logs/runner-cache/koide_first_order_selector_bounded_localization_certificate_2026_06_18.txt`

## Purpose

This certificate repairs the audit boundary for
`KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md`.
It does not supply the physical `AC_phi_lambda -> M(b) tensor sigma_+`
action bridge and does not derive the physical Koide `r=1/2` selector.

Instead, it isolates the exact finite theorem surface that can be re-audited
without that bridge.

## The Bounded Theorem Surface

Let `C` be the three-cycle on the native generation factor `R^3`, and let

```text
Gamma_chi = (2/3)(I + C + C^2) - I.
```

The bounded surface is exactly:

1. The circulant Koide quotient `Q = sum(lambda_k^2)/(sum lambda_k)^2`
   equals `(1+2r)/3` and is independent of the phase of `b`.
2. The `C3` clock grading has multiplicities `(1,1,1)`, so the formal
   `(singlet,doublet)=(1,1)` block-balance algebra is available while
   respecting `C^3=I`.
3. Within the native circulant generation algebra `span{I,C,C^2}`,
   the only operator that anticommutes with `Gamma_chi` is zero.
4. A separate tensor factor can carry a nonzero anticommuting shape:
   `I_3 tensor sigma_x` commutes with `C tensor I_2` and anticommutes with
   `I_3 tensor sigma_z`.
5. The native circulant mass has `b`-independent Fourier eigenvectors, so it
   remains the Berry-flat/commuting side of the finite comparison.

These five statements are the load-bearing payload. They are finite algebraic
claims checked by the runner.

## What Remains Open

This certificate leaves open:

- the physical `AC_phi_lambda -> M(b) tensor sigma_+` action term;
- the physical first-order/readout weighting rule;
- the derivation of `r=1/2` as a framework-selected charged-lepton branch.

The phrase "L-R coupling gate" is therefore a localization of the remaining
science target, not a claim that the framework already supplies that gate.

## Re-Audit Boundary

The row should be consumed only as bounded algebraic localization and
route-pruning:

```text
native R^3 / C3 / U(1)_b routes do not supply the physical first-order selector;
the only surviving escape requires a separate chiral L-R coupling plus readout.
```

It should not be consumed as a retained physical selector theorem, a retained
Koide `r=1/2` derivation, or a retained `AC_phi_lambda` action/readout bridge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/koide_first_order_selector_bounded_localization_certificate_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=35 FAIL=0
VERDICT: bounded localization certificate passes; physical L-R coupling/readout remains open.
```
