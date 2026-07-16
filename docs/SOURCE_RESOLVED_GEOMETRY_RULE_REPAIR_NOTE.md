# Source-Resolved Geometry-Rule Repair Probe

**Date:** 2026-04-05  
**Type:** bounded_theorem

## Artifact chain

- [Runner](../scripts/source_resolved_geometry_rule_repair_probe.py)
- [Shared DAG generator and propagator](../scripts/causal_field_gravity.py)
- [SHA-pinned runner cache](../logs/runner-cache/source_resolved_geometry_rule_repair_probe.txt)
- [Tracked dated output](../logs/2026-04-05-source-resolved-geometry-rule-repair-probe.txt)

## Bounded question

On the declared compact generated-DAG slice, can one additive
geometry-construction change widen detector support enough for the weak-field
sign and source-strength response to improve, without changing the field rule?

The finite card is fixed to:

- outer seed labels `0..3`, mapped to generator RNG seeds `7`, `26`, `45`,
  and `64` by `19 * seed + 7`
- `16` layers: one source node at layer zero and `24` nodes in every later
  layer, sampled uniformly in `y,z in [-10,10]`
- generated edges from either of the two preceding layers when Euclidean
  distance is at most `connect_radius = 3.2`
- baseline control: the generated adjacency augmented by the `k = 3`
  nearest-next-layer rule and a five-edge floor
- repair candidate: preserve that input adjacency in stable order, then union
  the nearest representative in each adaptive `3 x 3` next-layer `y/z`
  sector and nearest-node backfill of the candidate list to floor `9`
- four equally weighted source nodes selected from the middle layer around
  `global mean y + 3`, within `|Delta y| <= 2.5` when four are available and
  otherwise by the same nearest-four ranking
- static Green field
  `f_i(s) = g_seed (1/4) sum_m [(s/4) exp(-0.08 rho_im) / rho_im]`,
  `rho_im = r_im + 0.5`, at imposed source strengths
  `[0.001, 0.002, 0.004, 0.008]`; the per-seed gain `g_seed` fixes the maximum
  raw field at strength `0.008` to `0.02`, and the same gain is used for both
  geometries
- propagation wave number `K = 5` with angular envelope
  `exp(-0.8 theta^2) / L`; the edge phase is `exp(i K a)`, with
  `dL = L[1 + (f_i + f_j)/2]` and
  `a = dL - sqrt(max(dL^2 - L^2, 0))`
- exact zero-source shift; TOWARD means positive detector-centroid shift
- detector `N_eff = exp[-sum p_i log p_i]`; support fraction is the fraction
  of positive detector probabilities at least `1%` of the detector peak
- `alpha` is the ordinary-least-squares slope of
  `log |centroid shift|` against `log(source strength)`, not a derived physical
  mass exponent

For this diagnostic, improvement means larger aggregate support, more TOWARD
cases, and `alpha` closer to the linear-response target `1`.

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
- `delta_support_fraction = -0.0104`

## Bounded conclusion

On this finite card, the actual additive sector-fan candidate does not widen
aggregate detector support and does not improve either the sign count or the
source-strength response exponent. It is therefore a finite negative for this
specific geometry rule on this compact generated family.

This computation does not establish geometry closure, a universal mass law,
or behavior outside the declared four seeds, parameter card, static field
kernel, and observables. It does not rule out other sectorizations or fan
constructions. Independent audit owns any later ratification.
