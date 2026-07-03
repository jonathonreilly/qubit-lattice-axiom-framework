# The Route-2 E-Center Lift: the Stack's Own Measured Shell-Response Calibration Matches the 21/4 Target Chain Within Finite-Box Tolerances, and the Pin Reformulates Exactly as One Cross-Channel Covariance — a Sharpening of the Open Gate, Not a Derivation

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py`](../scripts/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.py) (PASS=6 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.txt`](../logs/runner-cache/frontier_quark_route2_e_center_lift_measured_calibration_2026_06_10.txt)

## The pin (engaged at the gate's own stated boundary)

The open gate
[`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md)
reduces the Route-2 readout problem to the triple
`(β_T/α_T, α_T/α_E, β_E/α_E) = (−1, −2, 21/4)`; after granting the two T-side candidates the single
missing entry is `ρ_E = β_E/α_E = 21/4`, equivalently the E-center lift `q_E = 1 + ρ_E/6 = 15/8`. The
naturality no-go
[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
proves the restricted carrier/readout class leaves `ρ_E` **free** (carrier linearity, shell
normalization, T-side data, and low-rational naturality do not select it) and names the missing
structure: *"an additional E-center endpoint ratio, source-domain rule, or stronger readout
primitive"*. Its forbidden-inputs discipline (no observed masses, no fitted targets, no
nearest-rational numerology) is respected throughout this note.

## What this note adds (two narrow facts; no derivation of 21/4 is claimed)

1. **The stack's own measured calibration matches the entire target chain within finite-box tolerances.** The landed
   center-excess row
   ([center-excess runner cache](../logs/runner-cache/frontier_tensor_support_center_excess_law.txt),
   SHA-pinned) contains the exact-arithmetic shell-response endpoint coefficients
   `γ_X(center), γ_X(shell)` for both channels (the `Λ_R` shell response at the 15³ box to the
   canonical source-family endpoints). The measured chain:

   | quantity | measured | target | gap |
   |---|---|---|---|
   | `q_T` | `+0.8333282` | `5/6` | `6.2e-6` |
   | `q_E` | `+1.8762461` | `15/8` | `6.6e-4` |
   | shell `T/E` | `−2.0054` | `−2` | `2.7e-3` |
   | center `T/E` | `−0.8907` | `−8/9` | `2.0e-3` |
   | `ρ_E` (implied) | `+5.2575` | `21/4` | `1.3e-3` |

   So the *"additional E-center endpoint ratio"* the no-go names as the missing structure **is present
   in the stack as a measured calibration of its own exact objects**; what is missing is its **exact
   infinite-volume identification**.
2. **The exact reformulation (exact rational arithmetic).** With the granted T-side values,

   > `ρ_E = 21/4` ⟺ `q_E = 15/8` ⟺ **`q_E = (9/4)·q_T`** ⟺ `c_TE = −8/9`

   — all four directions verified exactly. The pin is therefore a **single cross-channel covariance
   statement** between the two channels' center/shell lifts. (`9/4 = (3/2)²` is recorded as exact
   algebra only; no dimension or multipole reading is claimed — without a stack-native mechanism that
   would be the no-go's forbidden numerology.) The measured covariance `q_E/q_T = 2.251509` agrees
   with `9/4` at the same accuracy class (`6.7e-4`).

## The honest deviation hierarchy (the load-bearing caveat)

`q_T` matches `5/6` about **108× more tightly** than `q_E` matches `15/8` at the same box size
(`6.2e-6` vs `6.6e-4`). The landed cache cannot distinguish (a) slower E-channel finite-size
convergence (plausible — longer-range anisotropy coupling) from (b) an exact infinite-volume `q_E`
that **differs** from `15/8`. The decisive discriminator is a **box-size scan and extrapolation of
`q_E(N)`** — named as the follow-up; it requires parameterizing the `SIZE=15`-pinned module chain of
the landed rows (module-level state; not attempted here).

## What is and is not claimed

- **Is:** the landed calibration values and their gaps to the target chain (C1/C2); the exact
  four-way reformulation (C3); the covariance check (C4); the deviation hierarchy and the named
  box-size discriminator (C5); the relocation statement (C6).
- **Is not:** a derivation of `21/4` (the naturality no-go **stands**: nothing here selects `ρ_E`
  from the restricted class); a retained-status claim for any row; a claim that the infinite-volume
  `q_E` equals `15/8` (explicitly open — the deviation hierarchy is the honest warning it could
  fail); any use of observed quark masses, fitted values, or live-target selection. Adds no axiom, no
  primitive, no fitted value.

## Net (where the pin now sits)

The pin is **relocated**: from *"a free parameter with no stack-native anchor"* to *"the measured
value of a specific stack functional — the `Λ_R` shell-response E-center lift on the canonical
source-family endpoints — whose exact infinite-volume identification with `15/8` is the open theorem"*, with
the equivalent covariance form `q_E = (9/4)·q_T` as the sharpest single statement and the box-size
scan as the named decisive test.

## Load-bearing inputs

- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) — the open gate (the pin's owner row).
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) — the admissibility boundary this note respects and sharpens around.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) — the carrier/readout reduction and endpoint algebra.
- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) — the landed center-excess row whose SHA-pinned cache supplies the measured endpoint coefficients (consumed read-only).

## Forbidden-imports check

No PDG / observed / fitted value is consumed. The only numerical inputs are the landed cache's
exact-arithmetic shell-response endpoints (a stack-internal object, SHA-pinned) and exact rationals;
the target chain values appear only as comparison targets, exactly as the no-go's comparator
discipline prescribes.
