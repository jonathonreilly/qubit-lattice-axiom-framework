# Source-Resolved Geometry-Rule Repair Probe

**Date:** 2026-04-05  
**Status:** author-side finite bounded negative; independent re-audit remains external

## Artifact chain

- [Runner](../scripts/source_resolved_geometry_rule_repair_probe.py)
- [SHA-pinned runner cache](../logs/runner-cache/source_resolved_geometry_rule_repair_probe.txt)
- [Tracked dated output](../logs/2026-04-05-source-resolved-geometry-rule-repair-probe.txt)

## Bounded question

On the declared compact generated-DAG slice, can one additive
geometry-construction change widen detector support enough for the weak-field
sign and mass-scaling read to improve, without changing the field rule?

The finite card is fixed to:

- seeds `0..3`, `16` layers, `24` nodes per non-source layer,
  `connect_radius = 3.2`, and `y/z` range `10`
- baseline control: the generated adjacency augmented by the `k = 3`
  nearest-next-layer rule and a five-edge floor
- repair candidate: preserve that input adjacency in stable order, then union
  the nearest representative in each adaptive `3 x 3` next-layer `y/z`
  sector and nearest-node backfill of the candidate list to floor `9`
- one field rule: the static Green kernel with `mu = 0.08`, `eps = 0.5`, and
  source strengths `[0.001, 0.002, 0.004, 0.008]`
- observables: exact zero-source shift, TOWARD sign count, detector effective
  support `N_eff`, detector support fraction, and the fitted absolute
  centroid-shift exponent `alpha`

The repair is genuinely additive: an input edge is never removed. New edges
come only from the permitted next layer, and repeated candidates are skipped.

## Executable topology gates

The runner checks the construction before reporting field observables:

- every input adjacency is the stable prefix of the repaired adjacency
- all `6916` input edges across the four-seed slice survive
- all `8606` added edges are next-layer sector/floor candidates, distributed
  across `1348` sources
- repaired adjacency lists are duplicate-free
- a discriminating one-source fixture preserves its deliberately noncandidate
  bridge edge and gains `9` sector/floor edges
- a replacement-style mutant using only the new candidate list is rejected for
  dropping that fixture bridge edge

These checks make the former replacement implementation fail before any
numerical interpretation is printed.

## Recomputed finite result

Exact zero-source reduction survives both variants:

- baseline zero-source shift: `0.000e+00`
- additive-repair zero-source shift: `0.000e+00`

Per seed:

| Seed | Baseline TOWARD | Baseline `alpha` | Baseline `N_eff` | Repair TOWARD | Repair `alpha` | Repair `N_eff` |
|---:|---:|---:|---:|---:|---:|---:|
| `0` | `2/4` | `0.822` | `6.60` | `0/4` | `0.397` | `3.21` |
| `1` | `1/4` | `-0.224` | `4.46` | `0/4` | `-0.241` | `3.33` |
| `2` | `4/4` | `-0.612` | `2.93` | `4/4` | `0.013` | `3.38` |
| `3` | `0/4` | `0.246` | `6.25` | `0/4` | `-0.136` | `7.77` |

Aggregated over all `16` source-strength cases:

| Geometry | Zero shift | TOWARD | `alpha` | `N_eff` | Support fraction |
|---|---:|---:|---:|---:|---:|
| Baseline | `0.000e+00` | `7/16` | `0.058` | `5.06` | `0.422` |
| Additive repair | `0.000e+00` | `4/16` | `0.008` | `4.42` | `0.411` |

Thus the corrected repair deltas are:

- `delta_TOWARD = -3`
- `delta_N_eff = -0.64`
- `delta_alpha = -0.050`
- `delta_support_fraction = -0.011`

## Bounded conclusion

On this finite card, the actual additive sector-fan candidate does not widen
aggregate detector support and does not improve either the sign count or the
mass-scaling exponent. It is therefore a bounded negative for this specific
geometry rule on this compact generated family.

This computation does not establish geometry closure, a universal mass law,
or behavior outside the declared four seeds, parameter card, static field
kernel, and observables. Independent audit owns any later ratification.
