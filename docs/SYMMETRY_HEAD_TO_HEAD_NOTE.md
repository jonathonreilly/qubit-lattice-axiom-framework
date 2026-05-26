# Symmetry Head-To-Head Note

**Date:** 2026-04-03 (scope narrowed 2026-05-26)
**Status:** bounded shared-row comparison only
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:** [`scripts/symmetry_head_to_head.py`](../scripts/symmetry_head_to_head.py)
**Runner cache:** [`logs/runner-cache/symmetry_head_to_head.txt`](../logs/runner-cache/symmetry_head_to_head.txt)

This note freezes a narrow apples-to-apples comparison between the dense mirror
boundary card and the sparse `Z2 x Z2` joint-validation card on the one shared
row that is binding in both cited authorities:

- mirror dense boundary card at `N = 80`, from
  [`MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md)
- `Z2 x Z2` sparse joint-validation card at `N = 80`, from
  [`HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md`](HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md)

The previous `N = 80/100` table and retained-range readout are narrowed here.
`N = 100` and `N = 120` are not binding in this row because the current
retained-bounded `Z2 x Z2` joint-validation authority binds only the sparse
`N = 25, 40, 60, 80` cache. Dense-extension `N = 100/120` values remain
diagnostic context in their own source notes, not part of this comparison
claim.

## Narrowed Claim

On the shared `N = 80` row:

| N | lane | d_TV | purity | gravity | Born | k=0 |
|---|---|---:|---:|---:|---:|---:|
| 80 | mirror dense boundary card | `0.4291` | `0.8182` | `+3.0551` | `<1e-10` | `0.00e+00` |
| 80 | `Z2 x Z2` sparse joint-validation card | `0.540` | `0.782` | `+2.218` | `1.80e-15` | `0.00e+00` |

The bounded comparison read is:

- mirror has the stronger displayed gravity-weighted joint read at this shared
  row
- `Z2 x Z2` has the stronger displayed decoherence-side read at this shared row
  because its purity is lower
- both rows are Born-clean and `k=0` clean on their cited source surfaces

This is a one-row comparison theorem. It is not a retained-range theorem and it
does not rank either lane outside the cited `N = 80` row.

## Non-Binding Context

The mirror boundary-fit authority also contains mirror rows at `N = 40, 60,
100`. The `Z2 x Z2` sources contain additional dense-extension text and a
separate gravity probe. Those facts are useful lane context, but they are not
used to extend this row's binding comparison beyond `N = 80`.

The mirror mutual-information artifact remains a separate supplement named in
plain text: `MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md`. It is not directly
compared to `Z2 x Z2` here because this row has no matched `Z2 x Z2`
mutual-information authority.

## What This File Does Not Claim

- It does not claim `Z2 x Z2` is retained through `N = 120`.
- It does not claim a shared `N = 100` head-to-head theorem.
- It does not claim an asymptotic symmetry-family ranking.
- It does not promote either cited dependency beyond its independent audit
  scope.

## Citation-Graph Note

**Load-bearing dependencies:**

- [`MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md`](MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md) — supplies the mirror dense-boundary `N = 80` row
- [`HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md`](HIGHER_SYMMETRY_JOINT_VALIDATION_NOTE.md) — supplies the sparse `Z2 x Z2` `N = 80` row and explicitly excludes dense `N = 100/120` binding scope

**Plain-text pointer references** (not load-bearing deps):

- `MIRROR_MUTUAL_INFORMATION_CHOKEPOINT_NOTE.md` — separate mirror MI
  supplement, not used for the head-to-head table
