# Finite Lattice-Symmetry Proxy Census — Bounded Theorem

**Date:** 2026-04-03
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note states an
author-side computational boundary; it neither assigns nor predicts an audit
outcome.

**Primary runner:**
[`scripts/audit_companion_lattice_symmetry_unification_decision_certificate.py`](../scripts/audit_companion_lattice_symmetry_unification_decision_certificate.py)

Supporting artifacts:

- [`logs/runner-cache/audit_companion_lattice_symmetry_unification_decision_certificate.txt`](../logs/runner-cache/audit_companion_lattice_symmetry_unification_decision_certificate.txt)
- [`scripts/lattice_symmetry_unification_decision.py`](../scripts/lattice_symmetry_unification_decision.py)
- [`logs/2026-04-03-lattice-symmetry-unification-decision.txt`](../logs/2026-04-03-lattice-symmetry-unification-decision.txt)

## Bounded claim

For the fully supplied finite algorithm below, the exact Cartesian census has
36 tradeoff keys:

```text
max_dy in {3,4,5,6}
aperture in {narrow_center, wide_center, wide_outer}
mass offset in {-1,0,+1}.
```

Every one of those 36 keys has a nonpositive final-detector centroid-shift
proxy. The largest value is strictly negative:

```text
-4.744643220520 at (max_dy=4, narrow_center, offset=-1).
```

The canonical barrier aperture also has 44 explicitly enumerated
distance-sweep points — 11 distances for each of the four `max_dy` values —
and every point has a nonpositive centroid-shift proxy. The literal supplied
selection predicate accepts `0/36` rows.

This is an exact finite software-output theorem. The words `centroid-shift
proxy`, `three-slit residual`, `mutual-information proxy`, and `purity-deficit
proxy` below are definitions internal to the supplied algorithm. No retained
bridge identifies them with physical gravity, Born probability, decoherence,
or a framework-wide architecture. No physical incompatibility or no-go is
claimed.

## Supplied finite and model contract

Nothing in this contract is presented as framework-derived. The complete
load-bearing choice inventory is:

1. a directed two-dimensional layer graph with 40 layers, integer transverse
   sites `y=-20,...,+20`, open transverse boundary, and edges from layer `x`
   only to layer `x+1` with `|delta y| <= max_dy`;
2. source `(x,y)=(0,0)`, barrier layer `40//3`, field-source layer
   `2*40//3`, and detector equal to the complete final layer;
3. aperture row sets `narrow_center=[4]`, `wide_center=[3,4,5]`, and
   `wide_outer=[4,5,6]`, with their reflected lower rows;
4. mass-source offsets `-1,0,+1` relative to the upper aperture edge, plus the
   canonical choice `wide_center` with offset `+1`;
5. distance grid `[2,3,4,5,6,7,8,10,13,16,19]`;
6. radial field profile `0.1/(r+0.1)` — supplied strength `0.1` and softener
   `0.1`;
7. the directed propagation rule in `lattice_mirror_hybrid.py`, including
   `BETA=0.8`, `K=5.0`, its `dl-ret` phase/action, angular weight, `1/L`
   factor, and no layer normalization;
8. eight transverse bins, equal branch prior, `LAM=10.0`, and the supplied
   intermediate-depth amplitude construction used for the mutual-information
   and purity-deficit proxies;
9. a separate zero-field three-slit cancellation card used only as a numerical
   residual check; it is not the same two-aperture card used for the other
   proxies; and
10. selection thresholds `three-slit residual <= 1e-12`,
    `|k=0 shift| <= 1e-9`, mutual information `>=0.10`, purity deficit
    `>=0.03`, positive centroid shift, and an absolute no-barrier tail with
    negative exponent and `R^2 >=0.80`.

The compact companion checks the imported constants, graph geometry,
boundaries, source, detector, field profile, exact key set, and exact point
counts against this literal contract before it can emit a final decision. Its
cache identity also binds the complete source of the primary computation and
the propagation helper, so any implementation change makes the cache stale.

## Certificate contents

The cache contains:

- four canonical rows;
- four 11-point barrier-distance curves;
- four no-barrier tail fits;
- all 36 tradeoff rows;
- literal primary and second implementations of the selection predicate;
- raw sign/count checks; and
- the final finite-census decision.

Cancellation-scale three-slit residuals vary across supported numerical
runtimes while remaining many orders of magnitude below `1e-12`. The
certificate therefore serializes any finite residual at or below that declared
tolerance as `0.000e+00`; the raw value is still used for every check. This
makes the cached transcript deterministic without promoting roundoff digits to
scientific evidence.

## Canonical rows

| `max_dy` | mutual-information proxy | `d_TV` proxy | purity deficit | centroid-shift proxy | three-slit residual | `k=0` shift |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | `0.339254` | `0.590490` | `0.045665` | `-7.953602553235` | `<=1e-12` | `0` |
| 4 | `0.516908` | `0.735462` | `0.124308` | `-7.417059464459` | `<=1e-12` | `0` |
| 5 | `0.653173` | `0.834544` | `0.084635` | `-6.538914581062` | `<=1e-12` | `0` |
| 6 | `0.379595` | `0.574232` | `0.041402` | `-5.467299144690` | `<=1e-12` | `0` |

The no-barrier absolute-tail fits are:

| `max_dy` | peak distance | exponent | `R^2` |
|---:|---:|---:|---:|
| 3 | 7 | `-0.97888097` | `0.93427055` |
| 4 | 10 | `-1.68275825` | `0.91671263` |
| 5 | 8 | `-3.37113503` | `0.75355673` |
| 6 | 4 | `-1.55334003` | `0.88827889` |

## Proof boundary

The proof is exhaustive finite evaluation under the supplied contract:

1. construct the four exact directed graphs;
2. evaluate the four canonical rows and 44 barrier-distance points;
3. evaluate the Cartesian product of four `max_dy` values, three apertures,
   and three offsets;
4. verify exact key coverage, finiteness, signs, predicate agreement, and the
   strict maximum; and
5. exit nonzero if a contract, coverage, arithmetic, or decision check fails.

This closes only the enumerated software-output claim. It does not quantify
over other strengths, field profiles, boundary conditions, propagation laws,
topologies, aperture continua, binning rules, observables, or physical
interpretations. Those are alternative supplied models, not routes excluded
by this theorem.

## No-go boundary

No No-Go Discipline `PASS` is authored here. The branch does not establish
five independent attack routes, route exhaustion, a physical semantic bridge,
or a family-wide impossibility. The exact nonpositive census can falsify the
specific supplied selection attempt, but it cannot foreclose another model or
another physical bridge.

For a later strength-modified sibling computation, see the non-load-bearing
cross-reference `docs/LATTICE_FIELD_STRENGTH_UNIFICATION_NOTE.md`. That sibling
is not an authority for this finite claim and is intentionally not a citation
graph dependency.
