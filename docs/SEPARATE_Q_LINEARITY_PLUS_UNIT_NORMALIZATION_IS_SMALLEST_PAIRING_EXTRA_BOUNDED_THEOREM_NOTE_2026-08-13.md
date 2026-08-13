# Separate Q-linearity plus unit normalization is the smallest complete pairing extra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Status:** bounded
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/separate_q_linearity_plus_unit_normalization_is_smallest_pairing_extra_2026_08_13.py`](../scripts/separate_q_linearity_plus_unit_normalization_is_smallest_pairing_extra_2026_08_13.py)

Parents on `origin/main`:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — Record
  names the one-argument additive readout `I`.
- [`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) — product-law
  non-claim only. That note already lists the physical product law
  `M_source M_test` among the statements it does not prove. This row does
  not import its kernel algebra.

No unmerged pull request is a source. The product map below is reconstructed
here from the displayed matching.

## Result

On the value group `Q`, a map `B:Q×Q→Q` that is separately Q-linear and
unit-normalized is exactly the product. The matching “separately Q-linear
and `B(1,1)=1`” is extra to Record. Any extra object that factors a two-body
number through `(I(S),I(T))` and satisfies that matching is exactly
`π(S,T)=I(S)I(T)`. The `{0,1}` unit table alone does not assign values to
`(3,4)`, so the matching is a smallest complete extra on `Q`.

The product map is displayed. It is not installed as axiom content. The
axioms do not select bilinearity.

## Algebra

The value group is `Q`. A map `B:Q×Q→Q` is separately Q-linear when, for all
`x,x',y,y',q∈Q`,

```text
B(x+x',y)=B(x,y)+B(x',y),
B(x,y+y')=B(x,y)+B(x,y'),
B(q x,y)=q B(x,y)=B(x, q y).
```

It is unit-normalized when `B(1,1)=1`.

## Theorem 1

If `B` is separately Q-linear and `B(1,1)=1`, then `B(p,q)=p q` for all
`p,q∈Q`.

Proof. Separate Q-linearity scales each slot against the unit:

```text
B(p,q)=B(p·1, q·1)=p q B(1,1)=p q.
```

Witnesses reconstructed from that identity:

```text
B(3,4)=12,
B(3/2,1/2)=3/4,
B(2,0)=0.
```

## Theorem 2

The same conclusion follows from separate additivity on `Q`, with no extra
real-line continuity hypothesis. Additive maps `Q→Q` are Q-linear.

Proof. Let `f:Q→Q` satisfy `f(x+y)=f(x)+f(y)`. Then `f(0)=0` because
`f(0)=f(0)+f(0)`, and `f(-x)=-f(x)`. Integer scaling is repeated addition:
`f(n x)=n f(x)` for `n∈Z`. For a positive integer `n`,
`f(x)=f(n·(x/n))=n f(x/n)`, so `f(x/n)=(1/n) f(x)`. Therefore
`f((p/q) x)=(p/q) f(x)` for all `p/q∈Q`. Applying this in each slot of a
separately additive `B` yields separate Q-linearity, and Theorem 1 applies
once `B(1,1)=1`.

## Theorem 3

Record, quoted from the axiom memo, names a one-argument additive readout:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

`I` is a one-argument additive readout. It does not name a two-argument `B`.
The matching “separately Q-linear and `B(1,1)=1`” is extra.

## Theorem 4 (smallest complete)

Any extra object that (i) factors a two-body number through `(I(S),I(T))` and
(ii) is separately Q-linear and unit-normalized is exactly
`π(S,T)=I(S)I(T)`.

A strictly smaller object, for example the unit table alone on `{0,1}×{0,1}`
without extension, does not assign values to `(3,4)`. The matching is
therefore a smallest complete extra on `Q`: it is the smallest extra that
assigns a two-body number at every pair in `Q×Q` while remaining separately
Q-linear and unit-normalized.

## Theorem 5

Display `B`; do not install it. No gravitational coupling constant is
installed. The axioms do not select bilinearity. This result is not the
already-used contrast between a disjoint-union readout and a two-argument
product.

## Non-claims

- Record does not name a two-argument pairing.
- The four axioms do not select bilinearity.
- The displayed matching is extra, not axiom content.
- The Newton parent is used only for its product-law non-claim. This row
  does not prove a physical two-body force law.

## Verification

```bash
python3 scripts/separate_q_linearity_plus_unit_normalization_is_smallest_pairing_extra_2026_08_13.py
```

Expected closeout: `TOTAL: PASS>=10 FAIL=0`.
