# Exact finite comparator arithmetic for a supplied three-label target-apportionment fixture

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_supplied_three_label_target_apportionment_comparator_2026_07_30.py`](../scripts/frontier_supplied_three_label_target_apportionment_comparator_2026_07_30.py)

Independent checker:

- [`frontier_supplied_three_label_target_apportionment_independent_check_2026_07_30.py`](../scripts/frontier_supplied_three_label_target_apportionment_independent_check_2026_07_30.py)

Constitutional effect: none. This package changes no axiom, foundation,
primitive, registry, policy, audit result, or audit status. Its authority is
`none`; the bounded theorem remains unaudited until the independent audit lane
evaluates it.

## Supplied fixture

Adopt the exact rational target

```text
q = (
  36002393478282646,
  21194155104147802,
  42803451417569552
) / 100000000000000000.
```

The three numerators are nonnegative and sum to the denominator, so `q` is an
exact rational simplex. Adopt the four sizes and tolerance ladder

```text
M = (8, 32, 128, 512),
epsilon = (3/50, 1/50, 1/500, 1/1000).
```

For each `M`, the supplied count vector was authored by Hamilton
largest-remainder apportionment of `M q`:

| `M` | supplied count vector |
|---:|---:|
| 8 | `(3, 2, 3)` |
| 32 | `(11, 7, 14)` |
| 128 | `(46, 27, 55)` |
| 512 | `(184, 109, 219)` |

This constructional relation is a premise, not evidence recovered from
independently generated data. The sizes, tolerances, target, and counts are
authored test inputs. They are not sampled observations, realized outcomes,
framework Records, fitted data, or empirical calibration.

## Conditional result

For a supplied count vector `n` of size `M`, define

```text
f_i = n_i / M,
r_i = f_i - q_i,
d_epsilon = number of slots i for which |r_i| > epsilon.
```

Exact rational arithmetic gives:

| `M` | `d_(3/50)` | `d_(1/50)` | `d_(1/500)` | `d_(1/1000)` |
|---:|---:|---:|---:|---:|
| 8 | 0 | 2 | 3 | 3 |
| 32 | 0 | 0 | 3 | 3 |
| 128 | 0 | 0 | 0 | 2 |
| 512 | 0 | 0 | 0 | 0 |

Each count vector is exhaustive and nonnegative, hence every `f` is an exact
simplex. Each row also equals the declared largest-remainder construction.
These are finite identities for the four supplied fixtures. They are not a
sampling theorem, concentration bound, finite-to-limit theorem, or asymptotic
convergence result.

For the hostile software-control fixture `n=(M,0,0)`, all three slots disagree
with `q` at every supplied tolerance for every supplied size. This demonstrates
only that the comparator rejects that declared counterexample; it does not
make the positive fixtures independent evidence.

## Proof-obligation graph

```text
supplied rational target q with sum_i q_i = 1
  + supplied sizes, tolerances, and count vectors
      -> exact largest-remainder recount
      -> exact simplexes f_i = n_i/M
      -> exact residuals r_i = f_i-q_i
      -> finite disagreement census

supplied first-slot-only control
      -> finite hostile-control disagreement census
```

Every item on the left is an explicit fixture premise. The result closes only
the arithmetic on the right.

## Independent reconstruction

The primary runner uses `fractions.Fraction`. The independent checker imports
neither the primary runner nor any physics module. It recomputes apportionment
with integer quotient/remainder arithmetic, compares residuals by integer
cross-multiplication, then executes the primary as a clean black-box
subprocess. A mutation control changes one target numerator and confirms that
the production runner fails closed when exact target normalization is broken.

## Claim boundary

This package does not claim or test selection of a Born law. It supplies no
occurrence generator, framework Record-formation bridge, probability law,
independence or exchangeability premise, physical trace-functional selection,
empirical data, or limit theorem. Those questions are outside this finite
software fixture and are not compressed into one named obstruction.

The rational target is a supplied comparator convention. Agreement with
count vectors constructed from that same target has no independent physical
or statistical evidentiary force.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_supplied_three_label_target_apportionment_comparator_2026_07_30.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 scripts/frontier_supplied_three_label_target_apportionment_independent_check_2026_07_30.py
```

The runners print reproducibility payloads. No claim-status receipt or cached
PASS log is part of this source package.
