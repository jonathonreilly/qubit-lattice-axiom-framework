# Koide Selected-Eigenline Ambient-Eta Repair Target

**Date:** 2026-06-07
**Claim type:** open_gate
**Type:** open_gate / audit-bound repair target
**Status authority:** independent audit lane only. This companion note does not
modify the retained Tier-A witness
[`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`](KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md).
**Primary runner:** [`scripts/frontier_koide_selected_eigenline_ambient_eta_repair_target_2026_06_07.py`](../scripts/frontier_koide_selected_eigenline_ambient_eta_repair_target_2026_06_07.py)
**Cached runner output:** [`logs/runner-cache/frontier_koide_selected_eigenline_ambient_eta_repair_target_2026_06_07.txt`](../logs/runner-cache/frontier_koide_selected_eigenline_ambient_eta_repair_target_2026_06_07.txt)

## Scope

This note captures the science salvage from rejected PR #3066 without changing
the already-audited Koide selected-eigenline witness.

The retained no-go scope is the selected-eigenline obstruction:

- the relevant Wilson zero-mode character sector has rank two;
- a `CP^1` family of rank-one lines shares the same Wilson zero-mode and `Z3`
  character data;
- the endpoint lift/basepoint remains free;
- closure of the selected endpoint still requires a selected rank-one line and
  an endpoint-lift theorem.

The ambient finite Wilson eta proxy is diagnostic-only. It is not a substitute
for the selected-eigenline obstruction and should not be treated as a
load-bearing residual.

## Current repair target

On current main, the retained witness is audit-ratified and therefore cannot be
edited by review-loop without independent re-audit. Its note/runner still carry
ambient-mismatch wording. The companion runner computes the current finite
Wilson diagnostic directly from the witness helper functions and finds that the
frozen `r = 1.0` convention gives

```text
|eta| / fixed_site = 2/9.
```

So the repair target is narrow:

```text
remove ambient eta mismatch as a residual;
keep rank_two_zero_mode_character_sector_not_canonically_split;
keep wilson_eigenline_endpoint_lift_not_fixed.
```

That direct witness edit is audit-bound because the witness is a Tier-A
dependency. The present companion records the target and leaves the audit lane
to decide whether and how to re-ratify the edited witness.

## Runner checks

The runner verifies:

- the current finite Wilson eta diagnostic at `r = 1.0` equals `2/9`;
- the selected/spectator residual is independent of an ambient eta proxy
  variable;
- closure still requires `alpha = 0` and endpoint offset `c = 0`;
- the live witness still contains the ambient-residual wording, so this
  companion is tracking an actual repair target rather than inventing a new
  route.

## Dependencies

- [`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`](KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md)
- [`KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md`](KOIDE_DIMENSIONLESS_NOTE_2026-04-24.md)

**No-promotion statement:** this note does not change the audit status or
effective status of the Koide witness. It is an audit-bound repair target and
companion diagnostic only.

This note does not modify the audited Tier-A witness.
