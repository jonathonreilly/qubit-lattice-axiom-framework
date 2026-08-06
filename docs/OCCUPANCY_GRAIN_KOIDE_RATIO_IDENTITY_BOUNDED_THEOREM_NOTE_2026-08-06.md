# Occupancy-Grain / Koide-Ratio Coordinate Identity (Bounded Theorem)

**Date:** 2026-08-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_occupancy_grain_koide_ratio_identity_2026_08_06.py`](../scripts/frontier_occupancy_grain_koide_ratio_identity_2026_08_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_occupancy_grain_koide_ratio_identity_2026_08_06.txt`](../logs/runner-cache/frontier_occupancy_grain_koide_ratio_identity_2026_08_06.txt)

## Claim

Parameterise a real 3-vector in the cube-root-of-unity eigenbasis,

```text
x_k = a + b w^k + conj(b) conj(w)^k ,     k = 0,1,2 ,
```

with `a` real, `b = p + q w` complex, and `w` a primitive cube root of unity.
This is a complete real parameterisation carrying exactly `1 + 2` real degrees
of freedom. Write

```text
r = |b|^2 / a^2 ,        Q = (sum_k x_k^2) / (sum_k x_k)^2 .
```

Then, identically:

```text
sum_k x_k   = 3 a
sum_k x_k^2 = 3 a^2 + 6 |b|^2

        Q = (1 + 2 r) / 3
```

and therefore, as an exact equivalence in both directions,

```text
        r = 1/2   <==>   Q = 2/3 .
```

Equivalently: splitting `x = a(1,1,1) + u` with `sum u = 0`, the longitudinal
and transverse norms are `3a^2` and `6|b|^2`, so `r = 1/2` is exactly
longitudinal/transverse **equipartition**.

## Proof

Working in `Z[w]` with `w^2 = -1 - w`, the components and the Eisenstein norm
are rational functions of `(a, p, q)`:

```text
x_0 = a + (2p - q) ,   x_1 = a - (p + q) ,   x_2 = a + (2q - p) ,
|b|^2 = p^2 - p q + q^2 .
```

Writing `u_k = x_k - a`, one has `u_0 + u_1 + u_2 = 0` and

```text
sum u_k^2 = (2p-q)^2 + (p+q)^2 + (2q-p)^2 = 6(p^2 - pq + q^2) = 6|b|^2 .
```

Hence `sum x_k = 3a` and `sum x_k^2 = 3a^2 + 2a·0 + 6|b|^2`. Dividing,

```text
Q = (3a^2 + 6|b|^2)/(9a^2) = (a^2 + 2|b|^2)/(3a^2) = (1 + 2r)/3 .
```

The map `r -> (1+2r)/3` is strictly increasing, so the equivalence
`r = 1/2 <=> Q = 2/3` is a bijection and no other `r` gives `2/3`. ∎

The runner checks the parameterisation's reality and invertibility, both sum
rules, the identity, the equivalence, and the equipartition restatement on
seven rational sample points, entirely in `Fraction` arithmetic.

## What this is for

`Q` is the Koide ratio when `x_k = sqrt(m_k)`. `r` is the block-power ratio
`|b|^2 / a^2` used on the charged-lepton occupancy surface, whose interior
stationary value is the subject of
[`ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md`](ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md)
(unaudited at the time of writing; status authority is the audit lane). That
note's declared supplied context uses the same `a` / `b`-`bbar` decomposition,
in the form `||a I||^2 = ||b C + bbar C^2||^2`.

The identity above says those two quantities are **the same quantity in
different coordinates**. Consequently, *under the identification described in
the next section*, a theorem fixing `r` is a theorem fixing `Q`, and vice
versa. That is the whole content of this note.

## The identification this depends on, stated as an open premise

This note does **not** prove that the charged-lepton `K`/CPT 2-sector partition
is the `(a ; b, bbar)` decomposition of a rank-3 spectral element. That
identification is the **supplied context** of the universality note
(`charged_lepton_k_cpt_2_sector_occupancy_context`), declared there and not
derived there either. It remains open.

What changes is only that the payoff of proving it is now explicit and
computable rather than diffuse: proving that identification converts an
already-landed `r`-theorem into a statement about `Q`. Nothing here discharges
any part of it.

## Non-claims

- This note **derives neither** `Q` nor `r`. It is a coordinate identity
  relating them, valid for every `(a, p, q)` with `a != 0`.
- It **does not close** the charged-lepton mass lane, does not assert Koide,
  does not select a grain horn, and supplies no part of a closing theorem for
  the AC orbit-occupancy statistical-grain derivation obligation.
- It does not assert that a realized state registers `r = 1/2`; under the
  realized-state primitive that remains registered data.
- It says nothing about the phase `arg(b)` (the Koide `delta`). Only the
  modulus enters `r`, and `delta` is untouched and open.
- The `K`/CPT partition, its identification with the charged-lepton occupancy
  surface, and the rank-3 spectral reading are **not** derived here.
- PDG masses appear only as a disclosed **comparator**, never as a derivation
  step. No numerical agreement is claimed as evidence for any framework
  proposition.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted.

## Scope boundary

Real 3-vectors, `a != 0`, exact rational arithmetic. The claim is an algebraic
identity between two scalar functions of the same object; it carries no
physical content on its own and acquires physical meaning only through the
identification named above, which is open.

## Reproduce

```bash
python3 scripts/frontier_occupancy_grain_koide_ratio_identity_2026_08_06.py
```

Standard library only. No floating point in any load-bearing check (the
comparator block is float and is labelled as such), no randomness, no external
dependencies.
