# Decoherence Exponent Dimensional-Heuristic Boundary Note

**Date:** 2026-04-03
**Status:** bounded - bounded or caveated result note
an established theorem.
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The key effective-path-count and mixing-fraction scalings are asserted as heuristic, and the one retained-bounded dependency explicitly reports that the matched 2D-vs-4D replay does not support a clean dimension-only escape claim. Without a"*

with repair: *"missing_bridge_theorem - derive the effective path-count/mixing scaling from the actual DAG path measure, or add a matched multi-dimensional runner that isolates dimension from topology/connectivity."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The empirical tabulation of measured decoherence exponents `α` across spatial dimensions d = 1, 2, 3 from the simulation data, and the qualitative organizing heuristic that `|α| ~ 1/d_spatial` captures the right trend and order of magnitude; this is a descriptive summary of runner output with an approximate scaling ansatz, not a derived theorem.
- **NON-load-bearing (split off / admitted):** The derivation of the effective-path-count scaling `n_eff ~ M^{(d−1)/d}` and mixing-fraction scaling `f_mix ~ (r/L)^d` from the actual DAG path measure — these are acknowledged hand-waving steps (Caveat 1), and the one cited retained-bounded dependency explicitly reports the matched 2D-vs-4D replay does not support a clean dimension-only escape claim; the dimensional scaling law cannot be treated as a retained mechanism until these steps are derived from the actual path measure with topology and connectivity isolated.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

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

Those steps are not derived from the actual DAG path measure. The retained
matched 2D-vs-4D replay also reports that, after matching the current modular
families and approximate degree, the data do not support a clean dimension-only
escape claim. This repaired row therefore does not claim a retained dimensional
exponent mechanism.

The binding claim is narrower:

- the old `alpha ~ 1/d_spatial` derivation remains a heuristic route map;
- the retained matched replay is a counterweight showing the route is not
  isolated from topology/connectivity in the current harness;
- any future positive theorem must either derive the path measure or provide a
  broader matched-dimensional runner that controls topology/connectivity.

No new axiom, fitted selector, or audit verdict is introduced.

## Retained Matched-Replay Boundary

The one-hop retained-bounded dependency
[MATCHED_2D_4D_DECOHERENCE_NOTE.md](MATCHED_2D_4D_DECOHERENCE_NOTE.md)
pins the current comparison:

| N | 2D `pur_min` | 2D `<k>` | 4D `pur_min` | 4D `<k>` | matched 4D `r` |
|---|---:|---:|---:|---:|---:|
| 25 | 0.9341 | 9.76 | 0.9647 | 9.52 | 4.75 |
| 40 | 0.9577 | 9.98 | 0.9559 | 9.69 | 4.75 |
| 60 | 0.9555 | 10.11 | 0.9378 | 9.78 | 4.75 |
| 80 | 0.9667 | 10.24 | 0.9812 | 9.89 | 4.75 |
| 100 | 0.9428 | 10.25 | 0.9991 | 9.89 | 4.75 |

The retained dependency reports per-seed exponent fits:

```text
2D matched alpha = -0.158 +/- 1.024
4D matched alpha = -2.704 +/- 0.620
delta alpha (4D - 2D) = -2.546
```

This is not evidence for the old "higher dimension makes alpha flatter"
reading in the matched pocket. It is evidence that the current exponent lane is
still topology/connectivity-coupled.

## What This Claims

- The original dimensional-scaling argument is a heuristic and not a retained
  derivation.
- The current retained matched 2D/4D replay blocks using this row as a clean
  dimension-only exponent theorem.
- The future repair target is explicit: derive the effective path measure, or
  run a broader matched-dimensional sweep that isolates dimension from
  topology/connectivity.

## What This Does Not Claim

- It does not prove `alpha ~ 1/d_spatial`.
- It does not assert the old 5D/6D exponent predictions as binding results.
- It does not claim dimension alone rescues the decoherence ceiling.
- It does not use unmatched family summaries as proof of a theorem.
- It does not add a new axiom or apply an audit verdict.

## Heuristic Kept For Future Work

The following route remains scientifically useful as a conjectural path, but
not as a closed theorem:

1. define the actual DAG path measure for slit-to-detector amplitudes;
2. derive the effective independent channel count under that measure;
3. derive how slit-overlap/mixing volume scales under a matched family;
4. fit or prove the exponent law only after topology/connectivity are
   controlled.

This is a real future science route. The present row simply prevents the
heuristic from masquerading as a retained mechanism.

## Verification

Run:

```bash
python3 scripts/frontier_exponent_derivation_scope_repair.py
```

Expected:

```text
SUMMARY: PASS=22 FAIL=0
```
