# Dimension Selection Lower-Bound Finite-k Repair

**Date:** original dimension-selection note; 2026-05-27 lower-bound scope
repair.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
**Cached runner output:** `logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt`
**Source packet verifier:** `scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py`
**Source packet verifier cache:** `logs/runner-cache/dimension_selection_parent_source_packet_manifest_2026_06_05.txt`
**Source packet verifier output:** `outputs/dimension_selection_parent_source_packet_manifest_2026_06_05.json`

## 2026-05-27 Scope Repair

The prior note mixed two statements:

1. a finite runner lower-bound observation: the runner's attraction/mass-law
   criteria fail for `d <= 2` and pass for `d = 3,4,5`;
2. a broader unique-`d = 3` conclusion using separate orbital and atomic
   stability inputs.

Only the first statement is binding in this row. The second statement remains
context for separate upper-bound work and is not a theorem of this packet.
This is finite-runner lower-bound support only, not a unique-dimension
theorem.
This row does not authorize any framework-baseline rewrite.

The finite-k sign bridge
[`DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`](DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md)
supplies the runner-specific lower-bound sign. It differentiates the actual
layer-normalized finite-k propagator used by `scripts/frontier_dimension_selection.py`,
rather than importing WKB/eikonal ray reasoning as the load-bearing sign
argument.

## 2026-06-05 Source Packet Exposure Repair

The current audit blocker is a packet/runner-artifact gap: the parent repair
runner verifies the narrowed prose and finite-k sign replay, but the displayed
`beta` and `I_3` entries come from the original dimension-selection runner, and
the parent runner imports the bridge through a dynamic import. This repair makes
the full packet explicit:

- Parent repair runner: `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
- Parent repair cache: `logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt`
- Original dimension runner: `scripts/frontier_dimension_selection.py`
- Original dimension cache: `logs/runner-cache/frontier_dimension_selection.txt`
- Finite-k bridge note: `docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md`
- Finite-k bridge source: `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
- Finite-k bridge cache: `logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt`
- Finite-k bridge JSON: `outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json`
- Parent source-packet JSON: `outputs/dimension_selection_parent_source_packet_manifest_2026_06_05.json`

The source packet verifier above checks that these paths are linked from this
note, that the bridge and original runner sources are present and complete,
that the original runner cache contains the displayed `beta`/`I_3` lower-bound
table and printed `alpha` values, that the bridge cache reports
`SUMMARY: PASS=56 FAIL=0`, and that all runner caches match the current source
SHA. This does not set an audit verdict; its generated JSON is a disposable
runner output.

The primary parent runner now also imports the original dimension runner, the
finite-k bridge runner, and the source-packet manifest runner directly, then
prints a companion packet check. This makes the audit helper-graph resolver
include the packet sources rather than relying on the older dynamic-import path,
and it pins the original and bridge caches to their current runner SHAs while
exposing the source-packet manifest source for the independent manifest cache
check.

## Answer

No. The current bounded result is narrower:

```text
d <= 2  -> fails the runner's attractive-gravity / beta~1 lower-bound criteria
d >= 3  -> passes those runner criteria for d = 3, 4, 5
```

Thus this row supports a finite-runner lower bound, not a unique-dimension
theorem.

## Runner Surface

For each dimension `d = 1,2,3,4,5`, the original runner:

1. builds a finite lattice or finite propagation model;
2. uses the stated analytic `d`-dimensional potential family
   - `d = 1`: `phi ~ -M r`;
   - `d = 2`: `phi ~ -M log(r)`;
   - `d >= 3`: `phi ~ -M / r^(d-2)`;
3. measures force sign, mass exponent `beta`, distance exponent `alpha`, and
   a linear-propagator Sorkin `I_3` check.

The finite-k bridge supplies the direct runner-specific sign certificate for
the detector-centroid response at the baseline geometry.

## Bounded Result

The runner output reports:

| d | attractive? | beta approx | alpha approx | `I_3` | lower-bound read |
|---|---|---:|---:|---|---|
| 1 | no | 0.18 | 0.42 | `<1e-10` | fails |
| 2 | no | 0.27 | -0.17 | `<1e-10` | fails |
| 3 | yes | 1.01 | 1.32 | `<1e-10` | passes |
| 4 | yes | 1.05 | 3.30 | `<1e-10` | passes |
| 5 | yes | 1.03 | 5.01 | `<1e-10` | passes |

The finite-k derivative bridge independently certifies the same sign
transition for the runner's baseline centroid observable:

```text
d <= 2: negative/away response
d >= 3: positive/toward response
```

This is the bounded claim of this row.

## Non-Claims

This row does not claim:

- that `d = 3` is uniquely selected by the three runner observables;
- that the all-d analytic potential family is derived from the framework
  baseline alone;
- that Bertrand, Tangherlini, Ehrenfest, or atomic-stability upper bounds are
  proved in this row;
- that `Z^3` has been derived from a dimension-free framework baseline;
- that any repo-wide framework-baseline line should be rewritten;
- that observed physical dimension is used as an input.

## Relation To Upper-Bound Work

The separate upper-bound wrapper
`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` combines
this lower-bound route with named external upper-bound mathematics. That
wrapper is not load-bearing for the bounded claim here. Any future attempt to
derive `d <= 3` inside the framework must be reviewed separately.

## What This Closes

- finite-runner lower-bound support for excluding `d <= 2` in the stated
  propagator-plus-Poisson runner surface;
- direct use of the finite-k centroid-sign bridge;
- removal of the unique-`d = 3` overclaim from this parent row.

## What Remains Open

- framework-internal derivation of the all-d potential family;
- uniform control over all runner geometries, `k`, source widths, and positive
  masses;
- framework-internal upper-bound derivation `d <= 3`;
- any framework-baseline dimension rewrite.

## Verification

Run:

```bash
python3 scripts/frontier_dimension_selection_lower_bound_parent_repair.py
python3 scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py
```

Expected summary:

```text
SUMMARY: PASS=27 FAIL=0
SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=... FAIL=0
```
