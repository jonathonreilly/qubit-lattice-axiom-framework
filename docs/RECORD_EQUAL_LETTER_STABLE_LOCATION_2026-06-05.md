# Record Equal-Letter Stable Location

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
apply audit verdicts, does not edit audit data, and does not assert package
promotion.
**Primary runner:**
[`scripts/frontier_record_equal_letter_stable_location_2026_06_05.py`](../scripts/frontier_record_equal_letter_stable_location_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_equal_letter_stable_location_2026_06_05.txt`](../logs/runner-cache/frontier_record_equal_letter_stable_location_2026_06_05.txt)
(`PASS=26 FAIL=0`).

**Depends on:**

- [`RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md`](RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05.md)
- [`RECORD_SELECTOR_AUDIT_SIDECAR_2026-06-05.md`](RECORD_SELECTOR_AUDIT_SIDECAR_2026-06-05.md)

---

## Result

The equal-letter point is a stable location on the Record-prior dial.

For the two-record alphabet, let

```text
u = (1/2, 1/2).
```

For `0 < alpha < 1`, define the post-record atom-symmetric reset/thermalizing
map

```text
Phi_alpha(p) = (1 - alpha) p + alpha u.
```

Then `u` is stationary and linearly attracting:

```text
Phi_alpha(p) - u = (1 - alpha)(p - u).
```

The record-letter imbalance contracts by the same factor:

```text
(p_0' - p_1') = (1 - alpha)(p_0 - p_1).
```

Therefore the equal-letter point is a stable post-record location. On the
generation dial this is exactly

```text
s = 0,      r = 1/2,      Q = 2/3
```

under the supplied Koide algebra map.

## What this does not say

This is not a physical dial-selection theorem.

The same reset construction works for every dial prior

```text
pi_s = (1/(1 + 2^s), 2^s/(1 + 2^s)).
```

For each fixed `s`,

```text
Phi_{s,alpha}(p) = (1 - alpha) p + alpha pi_s
```

has `pi_s` as its stable fixed point. Thus stability itself does not choose
`s`. The equal-letter point is stable when the post-record atom-symmetric
surface is the surface being studied. The framework still has not selected the
physical dial position.

## Proof

The Markov matrix for the equal-letter reset map is

```text
P_alpha =
[[1 - alpha/2, alpha/2],
 [alpha/2,     1 - alpha/2]].
```

It is row-stochastic. It is invariant under the swap of the two record atoms.
It satisfies detailed balance with `u`:

```text
u_i P_alpha(i,j) = u_j P_alpha(j,i).
```

Its eigenvalues are

```text
1, 1 - alpha.
```

The eigenvector for eigenvalue `1` is the uniform line; the transverse
imbalance mode contracts by `1 - alpha`. For `0 < alpha < 1`, this gives a
strictly attracting stable location.

The dial identification follows from

```text
pi_s = (1/(1 + 2^s), 2^s/(1 + 2^s)).
```

Solving `pi_s = (1/2, 1/2)` gives `s=0`. The generation-weight relation
`r(s)=2^(s-1)` gives `r=1/2`, and the supplied Koide algebra relation
`Q(s)=1/3+(2/3)r(s)` gives `Q=2/3`.

Finally, replacing `u` by arbitrary `pi_s` gives the same contraction law:

```text
Phi_{s,alpha}(p) - pi_s = (1 - alpha)(p - pi_s).
```

So the theorem certifies stability of a location, not selection of the dial.

## Relation to the sidecar rows

The sidecar identified three rows as `equal_letter_stable_location` support:

| Claim id | How to read it after this theorem |
|---|---|
| `flavor_missing_axiom_carrier_measure_note_2026-05-30` | generator-channel HS measure can support the `s=0` stable location when read as a post-record channel surface |
| `koide_kappa_block_total_frobenius_algebraic_narrow_theorem_note_2026-05-10` | equal-weight Frobenius algebra supports the same stable location, not a physical selector |
| `koide_tracial_standard_form_carrier_narrow_note_2026-06-02` | tracial-standard carrier/channel-count reading supports the stable location, not endpoint closure |

These rows should not be promoted by this note. They can cite it only for the
weaker statement:

```text
s=0 is a stable equal-letter location on the post-record atom/channel surface.
```

They still cannot claim:

```text
the physical dial point is chosen.
```

## Boundary

- Does not force Koide.
- Does not fix the dial.
- Does not choose the physical value of `s`.
- Does not apply audit verdicts.
- Does not derive record-production dynamics.
- Does not derive a unique physical arrow among all possible `pi_s` targets.

## Runner summary

The runner verifies:

- the three sidecar rows are exactly the `equal_letter_stable_location` rows;
- the equal-letter reset chain is row-stochastic, swap-symmetric, stationary,
  detailed-balanced, and attracting;
- the imbalance and quadratic Lyapunov functions contract exactly;
- `s=0` maps to `r=1/2` and `Q=2/3`;
- `s=1` and arbitrary `pi_s` have their own stable reset maps;
- the sidecar entries do not use forced endpoint or audit-clean labels.

Scorecard: `PASS=26 FAIL=0`.
