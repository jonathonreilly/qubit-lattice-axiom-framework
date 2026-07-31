# Conditional finite-vector comparator distances and coordinate permutations — Cycle 763

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded conditional finite-arithmetic result

Claim type: bounded_theorem

Runner:

- [`frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py`](../scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py)

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, effective status, or framework claim.

## Exact supplied inputs

This note treats the following ordered integer vectors as synthetic supplied
inputs:

```text
q0 counts = (13, 128, 68)
q1 counts = (97, 1, 232)
q2 counts = (432, 146, 5)
```

The supplied ternary comparator is the exact rational vector

```text
b = (36002393478282646,
     21194155104147802,
     42803451417569552) / 100000000000000000,
```

whose entries are positive and sum exactly to one. The second reference is
the exact uniform vector `u = (1/3, 1/3, 1/3)`. Coordinate order is part of
the supplied theorem condition; it is not a derived physical association.

These literals carry no asserted provenance from a selector, apparatus,
physical outcome, Record, occurrence process, probability law, frequency
law, or framework derivation.

## Result

For each count vector `c`, define `q = c / sum(c)`,
`L1(q,t) = sum_i |q_i-t_i|`, and `TV(q,t) = L1(q,t)/2`.
Exact rational arithmetic gives:

| row | exact normalized vector | `L1(q,b)` | `L1(q,u)` | endpoint closer to `b`? |
|---|---|---:|---:|---:|
| `q0` | `(13/209, 128/209, 68/209)` | `0.800997280692164` | `0.558213716108453` | no |
| `q1` | `(97/330, 1/330, 116/165)` | `0.549991577709215` | `0.739393939393939` | yes |
| `q2` | `(432/583, 146/583, 5/583)` | `0.838916369689298` | `0.815323041738136` | no |

Thus `q1` is closer to the supplied comparator than to uniform in the
supplied identity order. This is an endpoint comparison, not movement toward
the comparator.

The runner also exhausts the six elements of `S3`, applying the same global
coordinate permutation to all three vectors:

| permutation | `q0` closer to `b`? | `q1` closer to `b`? | `q2` closer to `b`? |
|---|---:|---:|---:|
| `(0,1,2)` | no | yes | no |
| `(0,2,1)` | no | no | yes |
| `(1,0,2)` | yes | yes | no |
| `(1,2,0)` | no | no | yes |
| `(2,0,1)` | yes | no | no |
| `(2,1,0)` | no | yes | yes |

Therefore no one of these six global coordinate permutations makes all three
supplied vectors closer to `b` than to `u`.

## Boundary

The finite negative statement quantifies only over the six explicitly
enumerated global coordinate permutations. It does not address other fixed
maps, many-to-one maps, stochastic channels, affine calibrations, independent
per-row relabelings, other metrics, sampled data, asymptotics, or any physical
effect/outcome association. No physical mapping or route is foreclosed.

No Record, occurrence, probability, frequency, selected weight, apparatus
sensitivity, or framework conclusion is derived here. The comparator is a
supplied arithmetic reference, not a selected physical law.

## Negative-claim discipline

- **N1:** alternate map and metric classes are named above as untested and
  outside this finite theorem.
- **N2:** the result claims no wall decomposition or closure relation.
- **N3:** every load-bearing vector, comparator entry, order, metric, and map
  domain is explicit.
- **N4:** the witness matches the residual exactly: all six members of `S3`
  are enumerated by the runner.
- **N5:** the resolution is three supplied ternary vectors under one shared
  coordinate permutation; no broader resolution is claimed.
- **N6:** coordinate order is an explicit convention, while normalization and
  distance arithmetic are the propositional content.
- **N7:** broader deterministic, stochastic, or calibrated maps remain a
  concrete hostile alternative and are not ruled out.
- **N8:** the note preserves the convention/algebra split and makes no
  cross-cycle or framework-wide extrapolation.

## Verdict

The source result is the exact conditional normalization, distance table, and
six-case permutation exhaustion above. Independent audit is still required.
