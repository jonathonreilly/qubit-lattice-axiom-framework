# DM Full Closure -- 64:1 Channel-Weight Bridge

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Review boundary:** source-note candidate. Later independent review sets the
ledger state; this note does not set or predict it.
**Primary runner:** [`scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py`](../scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py)
**Cached runner output:** [`logs/runner-cache/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.txt`](../logs/runner-cache/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.txt)

## Purpose

This companion supplies a self-contained algebraic channel-weight bridge for
the downstream same-surface DM thermal-bounding lane. It proves the SU(3)
singlet/octet weight identity behind the visible-channel formula

```text
s_vis(alpha_s) = (8 s_1(alpha_s) + s_8(alpha_s)) / 9.
```

The repair is only item (i) of the parent bridge gap: the 64:1 same-surface
channel-weight calculation. It does not address observational constants,
packet-completeness, endpoint selection, or physical-color identification, and
it does not edit the downstream parent note or change any generated parent
state.

## Load-Bearing Inputs

Load-bearing links are restricted to the algebraic carrier and bounded
Sommerfeld-normalization notation:

- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  supplies the `3 x 3bar = 1 + 8` multiplicity fraction used as the
  algebraic carrier split.
- [`DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
  supplies the thermal-average and Sommerfeld algebra for `s_1` and `s_8`.

The downstream parent note is a consumer of this bridge, not a load-bearing
input to it. The verifier therefore proves the folding identity directly on
the SU(3) carrier and exact rational coefficients instead of importing parent
helper modules.

This companion adds no axiom, primitive, Tier-A input, convention, fitted value,
or observed-data input.

## 1. Parent Formula

For `N_c = 3`, the parent helper defines

```text
alpha_1 = C_F alpha_s,          C_F = (N_c^2 - 1)/(2 N_c),
alpha_8 = (1/(2 N_c)) alpha_s,
s_1 = <S_+(alpha_1; v)>_T,
s_8 = <S_-(alpha_8; v)>_T,
s_vis = (8 s_1 + s_8)/9.
```

The bridge below explains the `8:1` folded coefficient in `s_vis` from the raw
`64:1` squared-coupling ratio plus the `1 + 8` channel multiplicities.

## 2. The Narrow Bridge

With SU(3) generators normalized by `Tr(T^a T^b) = delta_ab/2`,

```text
C_F = (N_c^2 - 1)/(2 N_c) = 4/3.
```

The t-channel quark-antiquark color operator has channel scalars

```text
singlet:  -C_F = -4/3,
octet:    +1/(2 N_c) = +1/6.
```

Therefore the raw squared-coupling ratio is

```text
(C_F)^2 / (1/(2 N_c))^2
  = (4/3)^2 / (1/6)^2
  = 64.
```

The multiplicities of `3 x 3bar = 1 + 8` are `1` and `8`, so the folded weights
are

```text
w_1 = (1/9) * (4/3)^2 = 16/81,
w_8 = (8/9) * (1/6)^2 = 2/81,
w_1 / w_8 = 8.
```

The multiplicity-folded average is then

```text
(w_1 s_1 + w_8 s_8)/(w_1 + w_8)
  = (16 s_1 + 2 s_8)/18
  = (8 s_1 + s_8)/9.
```

This matches the parent helper formula exactly.

## 3. Verification

The runner verifies the bridge with two independent routes:

- explicit Gell-Mann generators `T^a = lambda^a/2`, including the trace
  normalization and `sum_a T^a T^a = (4/3) I_3`;
- explicit singlet and octet projectors on `3 x 3bar`, including projector
  idempotency, traces `1` and `8`, and channel scalars `-4/3` and `+1/6`;
- exact rational arithmetic for the raw `64:1` ratio and folded `8:1` ratio;
- exact equality of the folded formula
  `(w_1 s_1 + w_8 s_8)/(w_1+w_8) = (8 s_1+s_8)/9` for arbitrary channel
  values.

## 4. Boundaries

This companion closes only the algebraic channel-weight bridge. The following
remain outside this note:

- **Item (ii):** observational constants and live-DM plaquette inputs, including
  the live-DM plaquette / eta-omega observational constants named by the parent
  repair target;
- **Item (iii):** packet-completeness and endpoint-selector premises;
- identification of the algebraic carrier split with physical SM color;
- any parent-row status change.

The color automorphism source note carries its own physical-color deferral; this
companion preserves that deferral. The result is an algebraic same-surface
channel-weight identity on the carrier used by the parent helper, not an
independent physical-color derivation.

## 5. Command

```bash
python3 scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py
```

Expected summary: all checks pass and no failures.
