# Supplied cyclic per-row bijection: exact `S3^3` census — Cycle 766

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded conditional finite-arithmetic result

Claim type: bounded_theorem

Runners:

- [`frontier_cycle766_family_winning_mapping_2026_07_28.py`](../scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py)
- [`frontier_cycle766_mapping_independent_check_2026_07_28.py`](../scripts/frontier_cycle766_mapping_independent_check_2026_07_28.py)

Input source:

- [`SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md`](SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, review result, or effective status.

## Exact supplied inputs

The linked Cycle-763 conditional note supplies the synthetic ordered integer
vectors

```text
v0 = (13, 128, 68)
v1 = (97, 1, 232)
v2 = (432, 146, 5)
```

and the exact rational comparator

```text
q = (36002393478282646,
     21194155104147802,
     42803451417569552) / 100000000000000000.
```

The second reference is the exact uniform vector
`u = (1/3, 1/3, 1/3)`. Coordinate order is a supplied condition.

This note additionally supplies the per-row bijection

```text
m = ((0, 1, 2),
     (1, 2, 0),
     (2, 0, 1)).
```

Each tuple maps input coordinate `i` to output coordinate `m[i]`. The map is a
condition of the calculation; no derivation of it is asserted.

## Exact conditional result

Applying the supplied map gives

```text
r0 = (13, 128, 68)
r1 = (232, 97, 1)
r2 = (146, 5, 432)
pooled = (391, 230, 501).
```

For a positive count vector `c`, define `p = c / sum(c)` and
`TV(p,t) = (1/2) sum_i |p_i-t_i|`. Exact rational arithmetic gives:

| scope | `TV(p,q)` | decimal | `TV(p,u)` | comparator closer? |
|---|---:|---:|---:|---:|
| `r0` | `4185210791616554691/10450000000000000000` | `0.400498640346082` | `175/627` | no |
| `r1` | `87657118548737201/206250000000000000` | `0.425004211145392` | `61/165` | no |
| `r2` | `1140349238972309449/3643750000000000000` | `0.312960340026706` | `713/1749` | yes |
| pooled | `21609661557155861/1168750000000000000` | `0.018489549995427` | `24/187` | yes |

These are endpoint comparisons between supplied vectors.

## Exact `S3^3` census

The finite domain is the Cartesian product of one coordinate bijection from
`S3` for each of the three rows. It has exactly `6^3 = 216` members.
Exhaustive exact arithmetic finds:

- the supplied map is the unique pooled-comparator-TV minimum and therefore
  has rank 1 of 216;
- the next distinct pooled comparator TV is
  `823671370658282203/28050000000000000000`
  (`0.029364398240937`);
- 91 members are closer to the comparator than to uniform at the pooled
  scope; and
- 18 members are closer to the comparator than to uniform at all three rows
  and the pooled scope.

The primary runner enumerates the family with forward accumulation. The
checker separately enumerates the bijections with nested loops, applies each
map by inverse indexing, and evaluates direct count-vector distances without
importing the primary runner.

## Boundary

The result quantifies over exactly `S3^3` with the vectors, comparator,
coordinate order, map, metric, and pooling rule all supplied. It does not
quantify over many-to-one maps, maps that vary within a row, stochastic
kernels, affine calibrations, coarse-grainings, other coordinate definitions,
other metrics, or other comparators. No interpretation beyond this finite
conditional arithmetic is asserted.

## Negative-claim discipline

- **N1:** broader deterministic maps, stochastic kernels, calibrations,
  coordinate definitions, metrics, and comparators remain untested.
- **N2:** the result claims no independent wall decomposition or route
  closure; all four endpoint comparisons share the supplied inputs.
- **N3:** every load-bearing vector, comparator entry, coordinate convention,
  map, metric, pooling rule, and finite domain is explicit.
- **N4:** the exhaustive witness matches the finite residual exactly: all 216
  members are enumerated and the two row-level failures remain visible.
- **N5:** the resolution is three supplied ternary rows with one bijection per
  row; no finer or broader resolution is claimed.
- **N6:** coordinate order and the map are explicit conventions, while the
  transformations, distances, ranks, and census counts are the propositional
  content.
- **N7:** broader map classes and alternate comparators remain concrete
  hostile alternatives and are not ruled out.
- **N8:** the claim uses only the linked Cycle-763 conditional source and makes
  no cross-cycle extrapolation.

## Verdict

The source result is the exact conditional transformation, endpoint-distance
table, unique pooled rank, and complete `S3^3` census above. Independent audit
is still required.
