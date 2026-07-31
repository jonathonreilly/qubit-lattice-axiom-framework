# Koide `Q = 2/3` Bridge — Conditional-Ratio Narrowing

**Date:** 2026-04-22  
**Claim type:** bounded_theorem

**Status:** bounded conditional algebraic comparison; physical selector open
**Runner:** `scripts/frontier_koide_q_bridge_single_primitive.py`

**Complete runner stdout:**
[`logs/runner-cache/frontier_koide_q_bridge_single_primitive.txt`](../logs/runner-cache/frontier_koide_q_bridge_single_primitive.txt)

## Question

The current Koide package already has strong executable support for
`Q = 2/3`, but the physical/source-law bridge remains open:

> why must the physical charged-lepton packet satisfy the stipulated
> equal-block-power condition on the selected carrier?

This note asks the following finite algebraic question:

> under the stated carrier premises, does equal cyclic block power imply the
> conditional ratio `P_Q=1/2` and hence the Brannen-envelope identity
> `Q=2/3`?

## Exact premise ledger

This note proves a conditional algebraic theorem. Its load-bearing domain and
carrier/face inputs are explicit:

1. `r0 > 0` and `r1,r2` are real. Thus `a = r0/3 > 0`; the zero and
   negative-`a` branches are excluded.
2. The stipulated cyclic-carrier normalization is
   `E_+ = r0^2/3`, `E_perp = (r1^2+r2^2)/6`, `a = r0/3`, and
   `|b|^2 = (r1^2+r2^2)/36`.
3. The stipulated principal-square-root Brannen envelope is
   `sqrt(m_k) = v_0(1+c cos(delta+2 pi k/3))`, with the carrier match
   `c = 2|b|/a`, `c > 0`, `v_0 > 0`, and
   `delta mod (2 pi/3) in [-pi/12,pi/12]`. The endpoint cases allow one
   zero mass; use the open interval if all three masses must be positive.

Items 2-3 are theorem premises, not claimed first-principles outputs of this
note. No dimension-count or hypercharge convention is part of the theorem.

## Main statement

Under premises 1-3, equal cyclic block power implies that the scalar

```text
P_Q := |b|^2 / a^2 = 1/2.
```

On the stated positive, nondegenerate domain, the exact consequence chain is:

```text
equal cyclic block power
<=> real-irrep-block democracy
=> a^2 = 2 |b|^2
=> kappa = a^2 / |b|^2 = 2
=> Brannen c = sqrt(2)
=> Koide Q = 2/3.
```

The trigonometric reduction
`Q(c)=1/3+c^2/6` is an identity for the three signed envelope entries at every
real phase. Its interpretation using principal square roots is asserted only
on the phase/scale domain in premise 3. The theorem does not identify a
physical source law or claim that other arithmetic or physical routes have
been exhausted.

## Proof sketch

### 1. Cyclic projector form

On the canonical cyclic image

```text
H_cyc = (r0/3) B0 + (r1/6) B1 + (r2/6) B2
```

the exact block powers are

```text
E_+ = r0^2 / 3,
E_perp = (r1^2 + r2^2) / 6.
```

Therefore

```text
E_+ = E_perp
<=> 2 r0^2 = r1^2 + r2^2.
```

### 2. Real-irrep-block democracy

Under premise 2

```text
a = r0 / 3,
|b|^2 = (r1^2 + r2^2) / 36,
```

the same equality becomes

```text
3 a^2 = 6 |b|^2
<=> a^2 = 2 |b|^2
<=> |b|^2 / a^2 = 1/2
<=> kappa = a^2 / |b|^2 = 2.
```

### 3. Brannen and Koide

Under premise 3, for the Brannen envelope

```text
sqrt(m_k) = v_0 (1 + c cos(delta + 2 pi k / 3)),
```

the stipulated carrier match is

```text
c = 2 |b| / a.
```

Because `a>0`, `|b|^2 / a^2 = 1/2` forces `c = sqrt(2)`. The sign hypothesis
is load-bearing: the same squared relation with `a<0` would give
`c=-sqrt(2)`, not `+sqrt(2)`. Direct summation of the three signed envelope
terms gives

```text
Q(c) = 1/3 + c^2/6,
```

so `c=sqrt(2)` gives

```text
Q = 2/3
```

independently of `delta` as a signed-amplitude identity. At `c=sqrt(2)`, the
phase domain in premise 3 makes all three entries nonnegative, so the same
calculation is valid for the stated principal square roots.

## What this does not claim

- It does **not** prove that the physical charged-lepton packet must realize
  `P_Q = 1/2`.
- It does **not** derive the cyclic-carrier normalization, equal-power
  selector, Brannen carrier match, or phase-domain selection listed in the
  premise ledger.
- It does **not** close the Brannen-phase bridge behind `delta = 2/9`.
- It does **not** promote the overall scale `v_0`.

## Bottom line

For the explicitly stipulated algebraic packet, equal cyclic block power
implies the conditional ratio

> `P_Q = |b|^2 / a^2 = 1/2`.

and, on the principal-root Brannen domain, `Q=2/3`. This bounded theorem does
not select its premises physically.
