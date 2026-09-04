# The Route-2 q_E Box-Size Scan: 15/8 Is a Fixed-N=15 Coincidence, Not a Bulk Limit — Closing the Infinite-Volume Escape Hatch (the Naturality No-Go Stands Unchanged)

**Date:** 2026-06-10
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py`](../scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py) (PASS=7 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_qe_box_size_scan_2026_06_10.txt`](../logs/runner-cache/frontier_quark_route2_qe_box_size_scan_2026_06_10.txt)

## The discriminator

The relocation note
[`QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION...`](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md)
observed that the landed stack reproduces the Route-2 readout target chain at the single box N=15
(`q_T` vs `5/6` at `6.2e-6`, `q_E` vs `15/8` at `6.6e-4`) but with a **108× deviation hierarchy** between
the two channels, and **floated — while explicitly flagging it could fail —** the hope that `q_E`
identifies with `15/8` in the stack's own boundary-removal (`N→∞`) limit; it named the box-size scan as
the decisive discriminator. This note runs that scan. **Discipline (the naturality no-go's):** no
observed quark masses, no fitted targets, no nearest-rational selection — only the stack's own exact
objects at varying `N`, with `5/6, 15/8, −2, −8/9` as comparison targets.

## Result

The reconstruction reuses the landed `adm_metric` / `ricci_and_einstein` / `max_tensorial_components` /
`reduced_data` / `build_adapted_basis` verbatim and parameterizes the box size `N`; the only landed
object bypassed is the 15-pinned scalar Schur action, which feeds the unused `[1]` slot, not the
`e_spatial_tf` slot `q_X` reads. **Anchor:** at `N=15` the four reconstructed `γ` reproduce the landed
cache to `~1e-13` (S1) — the reconstruction is the landed observable.

1. **The mechanism — an isolated one-box numerator excursion (S3).** The shell normalization `a_aniso`
   is **identical** at the center (`e0`) and shell (`s/√6`) endpoints (`a_center/a_shell = 1` to `1.6e-15`),
   so it **cancels exactly** in `q_X = γ_X(center)/γ_X(shell) = β_X(center)/β_X(shell)`. The bare
   finite-difference `β_E(shell)` is **positive at every box** (`N=13,17,19,21,25,29 ≈ +1e-5`) **except
   N=15**, where it makes an **isolated one-box downward excursion** to `−1.6e-5` — *not* a smooth
   zero-crossing (the `N13/N17` interpolant at `N15` is positive `+1.2e-5`). So `q_E=15/8` at `N=15` is
   set by that single-box numerator excursion. The base observable `eta_floor(e0/s)` is smooth and
   monotone-decreasing (S2), so this is a property of the delicate differenced coefficient, not a broken
   potential — and it is robust to the finite-difference step `EPS ∈ {0.0025,0.005,0.01}` and the Ricci
   step (S5).
2. **No infinite-volume limit recovers 15/8 (S4, S5b).** Under the **fixed-radius** boundary-removal
   limit, `q_T(N)` sign-flips (`+0.83` at N=15 → `−0.20, −0.81, −1.32, −2.09`) and `q_E(N)` runs
   large-negative (`→ ~ −11`). Under a **box-proportional** probe radius (a different, also-well-defined
   infinite-volume observable), `q_E` and `q_T` **converge — but to `(1, 1)`, not `(15/8, 5/6)`**. So
   `15/8` fails under **both** limits. (The fixed-radius limit is *a* faithful boundary-removal limit,
   not *the* unique one; neither yields `15/8`.)

## Verdict (two-part — the honest framing)

1. **`15/8` is a fixed-`N=15` exact-readout coincidence.** This scan **negatively resolves the
   self-posed infinite-volume discriminator** the relocation note floated: within the landed functional,
   *no* infinite-volume limit identifies `q_E` with `15/8`. This **closes the "maybe it converges to
   15/8 in the bulk" escape hatch** and **vindicates the relocation note's explicitly-flagged caution**.
2. **It does NOT sharpen the standing naturality no-go**
   ([`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO...`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)),
   which was always a fixed-carrier **structural-selection** gap with **no convergence claim** and
   **stands unchanged**. `15/8` was never claimed by the readout's native framing to *be* the
   infinite-volume value. The `21/4` pin (`ρ_E = β_E/α_E` free) remains exactly where the naturality
   no-go left it; this scan supplies **no** selecting primitive — it only rules out the bulk-limit
   promotion of the `N=15` coincidence.

## What is and is not claimed

- **Is:** the `N=15` anchor (`~1e-13`); the exact `a_aniso` cancellation reducing `q_X` to a bare `β`
  ratio; the isolated one-box downward excursion of `β_E(shell)` at `N=15` (robust); the
  non-convergence under the fixed-radius limit and the convergence-to-`(1,1)` under the box-proportional
  limit — hence `15/8` fails under both; the two-part verdict (closes the bulk-limit hatch; naturality
  no-go unchanged).
- **Is not:** does **not** claim `15/8` was ever the readout's infinite-volume value (the rider on
  "excludes"); does **not** sharpen or weaken the naturality no-go; does **not** supply a selecting
  primitive for `ρ_E`; does **not** derive `q_E`; does **not** assert the fixed-radius limit is the
  unique boundary-removal limit; adds no axiom, no primitive, no fitted value, no observed/fitted input.

## Boundaries (honest)

- **Two limits tested, both miss `15/8`;** other observable definitions that *break* the
  `a_center = a_shell` cancellation would be **different functionals, not limits of this one**, and are
  out of scope (a new construction, not a rescue).
- The `N=15` numerator excursion's independent significance (beyond being the pinning box) is unexplored.
- The 15-pin in the scalar-Schur channel is benign for `q_X` (it `IndexError`s only on grids *smaller*
  than 15 and is correctly bypassed); the anchor confirms the bypass is exact.
- The framing is deliberately two-part: the scan closes the bulk-limit hatch for this functional, but it
  does not sharpen or weaken the standing naturality no-go.

## Load-bearing inputs

- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) — the open gate (the pin's owner row).
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) — the standing naturality no-go (unchanged; the convergence question this scan closes was never part of it).
- [`QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md) — the relocation note that floated and flagged the bulk-limit hope this scan resolves.
- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) — the landed producer of the `γ` coefficients (reconstructed and anchored here at `N=15`).

## Forbidden-imports check

No PDG / observed / fitted value is consumed. The only numerical inputs are the stack's own exact
objects (the `N`-box Green's function, the fixed-radius tensor probe, the shell anchor) and exact
rationals; `5/6, 15/8, −2, −8/9, 1` appear only as comparison targets, exactly as the naturality
no-go's comparator discipline prescribes.
