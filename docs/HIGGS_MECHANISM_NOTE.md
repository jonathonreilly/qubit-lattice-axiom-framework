# Radial Quartic Global-Minimum Lemma

**Date:** 2026-04-15; exact formal repair 2026-07-16
**Status:** exact theorem about a defined real polynomial on a radial domain.
No physical interpretation is part of the theorem.
**Claim type:** positive_theorem
**Primary runner:** `scripts/frontier_higgs_quartic_mechanism_algebra_repair.py`
**Status authority:** independent audit lane only.

## Exact claim

Let `lambda > 0` and `m2` be formal real parameters. For `r >= 0`, define

```text
V(r) = m2 r^2 / 2 + lambda r^4 / 4.
```

Then `V` has a unique global minimizer on `r >= 0`.

- If `m2 >= 0`, the unique minimizer is `r = 0`, and `V(0) = 0`.
- If `m2 < 0`, set
  `v = sqrt(-m2 / lambda)`. The unique minimizer is `r = v`, with
  `V(v) = -m2^2 / (4 lambda)` and
  `V''(v) = -2 m2 = 2 lambda v^2 > 0`.

The theorem is formal polynomial and order algebra. The stable claim ID and
filename are retained for repository continuity; they do not give the lemma a
physical Higgs interpretation.

## Proof

For every real `m2`, direct factorization gives

```text
V(r) = r^2 (2 m2 + lambda r^2) / 4.
```

### Case `m2 >= 0`

Both factors in the displayed expression are nonnegative on `r >= 0`. If
`r > 0`, then `r^2 > 0` and

```text
2 m2 + lambda r^2 > 0
```

because `m2 >= 0` and `lambda > 0`. Therefore `V(r) > 0` for every
`r > 0`, whereas `V(0) = 0`. Thus `r = 0` is the unique global minimizer.

The boundary case is explicit: when `m2 = 0`,

```text
V(r) = lambda r^4 / 4,
```

so equality still holds only at `r = 0`. This minimum is unique but
degenerate: `V''(0) = 0`.

### Case `m2 < 0`

Define `v > 0` by

```text
v^2 = -m2 / lambda.
```

Substitution and exact completion of the square give

```text
V(r) - V(v) = lambda (r^2 - v^2)^2 / 4.
```

The right-hand side is nonnegative. Equality holds exactly when
`r^2 = v^2`. Over the stated radial domain `r >= 0`, and because `v > 0`,
the only equality point is `r = v`. Hence `v` is the unique global minimizer.
Direct substitution gives

```text
V(v) = -m2^2 / (4 lambda).
```

Finally,

```text
V''(r) = m2 + 3 lambda r^2,
V''(v) = -2 m2 = 2 lambda v^2 > 0.
```

This proves every case, including the equality conditions, the degenerate
`m2 = 0` boundary, and positive curvature when `m2 < 0`.

## Scope firewall

This lemma defines a polynomial and proves its order properties. It does not
claim or supply any of the following:

- a scalar carrier or Higgs field;
- gauge symmetry breaking;
- a Coleman-Weinberg or other physical effective potential;
- framework dynamics or a selected vacuum;
- a derivation of `lambda` or `m2`;
- a physical mass or any observed value.

Any physical interpretation requires a separate supplied bridge and cannot be
inferred from this theorem.

## Verification

The normal exact certificate is

```bash
python3 scripts/frontier_higgs_quartic_mechanism_algebra_repair.py
```

The adversarial certificate adds exact controls for invalid `lambda`, domain,
radius, curvature, perturbation, and physical-inference claims:

```bash
python3 scripts/frontier_higgs_quartic_mechanism_algebra_repair.py --hostile
```

The intentional-failure probe must report one failure and exit nonzero:

```bash
python3 scripts/frontier_higgs_quartic_mechanism_algebra_repair.py --intentional-failure
```
