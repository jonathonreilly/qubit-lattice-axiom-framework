# Conditional per-row bijection census in `S3^3` — Cycle 765

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded conditional finite-arithmetic result

Claim type: bounded_theorem

Runner:

- [`frontier_cycle765_per_row_bijection_s3_cubed_conditional_census_2026_07_28.py`](../scripts/frontier_cycle765_per_row_bijection_s3_cubed_conditional_census_2026_07_28.py)

Input source:

- [`SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md`](SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Exact supplied inputs

The following ordered integer vectors are synthetic supplied inputs inherited
from the linked Cycle-763 conditional arithmetic note:

```text
v0 = (13, 128, 68)
v1 = (97, 1, 232)
v2 = (432, 146, 5)
```

The supplied ternary comparator is

```text
q = (36002393478282646,
     21194155104147802,
     42803451417569552) / 100000000000000000,
```

and the second reference is the exact uniform vector
`u = (1/3, 1/3, 1/3)`.

The supplied per-row bijection is

```text
m = ((1, 2, 0),
     (0, 1, 2),
     (2, 0, 1)).
```

Each tuple uses the convention `feature index -> output index`: the count at
feature coordinate `f` is added to output coordinate `m[f]`. Both this map and
the coordinate order are theorem conditions. They are not derived physical
associations.

These literals carry no asserted provenance from a selector, apparatus,
physical effect or outcome, Record, occurrence process, probability law,
frequency law, convergence argument, or framework derivation. The comparator
is an arithmetic reference and is not selected as a physical law.

## Exact conditional result

Applying the supplied map gives

```text
r0 = (68, 13, 128)
r1 = (97, 1, 232)
r2 = (146, 5, 432)
pooled = (311, 19, 792).
```

For a positive count vector `c`, define `p = c / sum(c)`,
`L1(p,t) = sum_i |p_i-t_i|`, and `TV(p,t) = L1(p,t)/2`. Exact rational
arithmetic gives:

| scope | `TV(p,q)` | `TV(p,u)` | closer to `q`? |
|---|---:|---:|---:|
| `r0` | `240879915857997727/1306250000000000000` | `175/627` | yes |
| `r1` | `56717881451262799/206250000000000000` | `61/165` | yes |
| `r2` | `1140349238972309449/3643750000000000000` | `713/1749` | yes |
| pooled | `29521332868832351/106250000000000000` | `19/51` | yes |

This is an endpoint comparison between supplied vectors. It is not movement
toward the comparator and supplies no statistical or physical interpretation.

## Exact `S3^3` census

The comparison family is the Cartesian product of one coordinate bijection
from `S3` for each of the three rows. It therefore has exactly
`6^3 = 216` members. Exhaustive exact arithmetic finds:

- 122 members have strictly smaller pooled `TV(p,q)` than the supplied map;
- 6 members, including the supplied map, tie at its pooled `TV(p,q)`;
- the supplied map therefore occupies ranks 123–128 of 216;
- 18 members are closer to `q` than to `u` at all three rows and the pooled
  scope; and
- 91 members are closer to `q` than to `u` at the pooled scope.

These counts are properties only of the explicitly supplied finite family and
metric. They are not probabilities assigned to maps and do not establish an
evidential or programmatic bar.

## Boundary

The `216` cases are all and only the three independent row-wise coordinate
bijections in `S3^3`. They are not all deterministic maps. Many-to-one maps,
event-dependent maps, deterministic maps outside the per-row-bijection family,
stochastic kernels, affine calibrations, coarse-grainings, other feature
definitions, other metrics, and other comparators are untested.

No physical mapping, effect/outcome association, apparatus response, selector,
Record, occurrence, probability, frequency, selected weight, convergence,
framework conclusion, no-go, or restriction on future routes is derived here.

## Negative-claim discipline

- **N1:** alternate deterministic, stochastic, calibrated, feature, metric,
  and comparator routes are named above as untested.
- **N2:** the result claims no wall decomposition, route closure, or no-go.
- **N3:** every load-bearing vector, comparator entry, map, coordinate
  convention, metric, and finite family is explicit.
- **N4:** the exhaustive witness matches the residual exactly: all 216 members
  of `S3^3` are enumerated by the runner.
- **N5:** the resolution is three supplied ternary vectors with one supplied
  bijection per row; no broader resolution is claimed.
- **N6:** coordinate order and the map are explicit conventions, while
  normalization, distance arithmetic, and the finite census are the
  propositional content.
- **N7:** broader deterministic, stochastic, calibrated, and physically
  associated maps remain concrete hostile alternatives and are not ruled out.
- **N8:** the note preserves the convention/algebra split and makes no
  cross-cycle or framework-wide extrapolation.

## Verdict

The source result is the exact conditional transformation, endpoint-distance
table, and `S3^3` census above. Independent audit is still required.
