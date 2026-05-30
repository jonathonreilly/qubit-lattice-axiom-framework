# Decoherence Exponent Dimensional-Heuristic Boundary Note

**Date:** 2026-04-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_exponent_derivation_scope_repair.py`

## Source Boundary

This row is a bounded boundary note for an old dimensional-scaling heuristic.
It does not prove a dimension-only exponent law, does not assert 5D/6D
predictions, and does not add a new axiom or selector.

## Scope Repair

The earlier note proposed an organizing dimensional scaling story for the
decoherence ceiling exponent in

```text
1 - pur_min ~ C N^alpha.
```

Its load-bearing steps were the asserted effective path-count and mixing-zone
scalings

```text
n_eff ~ M^((d_spatial - 1)/d_spatial),
f_mix ~ (r/L)^d_spatial,
alpha ~ 1/d_spatial.
```

Those steps are not derived from the actual DAG path measure. The matched
2D-vs-4D replay also reports that, after matching the current modular families
and approximate degree, the data do not support a clean dimension-only escape
claim. This repaired row therefore does not claim a dimensional exponent
mechanism.

The binding claim is narrower:

- the old `alpha ~ 1/d_spatial` derivation remains a heuristic route map;
- the matched replay is a counterweight showing the route is not
  isolated from topology/connectivity in the current harness;
- any future positive theorem must either derive the path measure or provide a
  broader matched-dimensional runner that controls topology/connectivity.

No new axiom or fitted selector is introduced.

## Matched-Replay Boundary

The matched-replay dependency
[MATCHED_2D_4D_DECOHERENCE_NOTE.md](MATCHED_2D_4D_DECOHERENCE_NOTE.md)
pins the current comparison:

| N | 2D `pur_min` | 2D `<k>` | 4D `pur_min` | 4D `<k>` | matched 4D `r` |
|---|---:|---:|---:|---:|---:|
| 25 | 0.9341 | 9.76 | 0.9647 | 9.52 | 4.75 |
| 40 | 0.9577 | 9.98 | 0.9559 | 9.69 | 4.75 |
| 60 | 0.9555 | 10.11 | 0.9378 | 9.78 | 4.75 |
| 80 | 0.9667 | 10.24 | 0.9812 | 9.89 | 4.75 |
| 100 | 0.9428 | 10.25 | 0.9991 | 9.89 | 4.75 |

The dependency reports per-seed exponent fits:

```text
2D matched alpha = -0.158 +/- 1.024
4D matched alpha = -2.704 +/- 0.620
delta alpha (4D - 2D) = -2.546
```

This is not evidence for the old "higher dimension makes alpha flatter"
reading in the matched pocket. It is evidence that the current exponent lane is
still topology/connectivity-coupled.

## What This Claims

- The original dimensional-scaling argument is a heuristic and not a
  derivation.
- The current matched 2D/4D replay blocks using this row as a clean
  dimension-only exponent theorem.
- The future repair target is explicit: derive the effective path measure, or
  run a broader matched-dimensional sweep that isolates dimension from
  topology/connectivity.

## What This Does Not Claim

- It does not prove `alpha ~ 1/d_spatial`.
- It does not assert the old 5D/6D exponent predictions as binding results.
- It does not claim dimension alone rescues the decoherence ceiling.
- It does not use unmatched family summaries as proof of a theorem.
- It does not add a new axiom.

## Heuristic Kept For Future Work

The following route remains scientifically useful as a conjectural path, but
not as a closed theorem:

1. define the actual DAG path measure for slit-to-detector amplitudes;
2. derive the effective independent channel count under that measure;
3. derive how slit-overlap/mixing volume scales under a matched family;
4. fit or prove the exponent law only after topology/connectivity are
   controlled.

This is a real future science route. The present row simply prevents the
heuristic from masquerading as a closed mechanism.

## Verification

Run:

```bash
python3 scripts/frontier_exponent_derivation_scope_repair.py
```

Expected:

```text
SUMMARY: PASS=22 FAIL=0
```
