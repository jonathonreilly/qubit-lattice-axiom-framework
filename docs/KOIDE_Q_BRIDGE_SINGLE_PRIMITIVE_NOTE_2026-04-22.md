# Koide `Q = 2/3` Bridge — Single-Primitive Narrowing

**Date:** 2026-04-22  
**Claim type:** positive theorem (conditional algebraic theorem)

**Status:** exact support / bridge-target narrowing on the charged-lepton Koide
lane  
**Runner:** `scripts/frontier_koide_q_bridge_single_primitive.py`

**Complete runner stdout:**
[`logs/runner-cache/frontier_koide_q_bridge_single_primitive.txt`](../logs/runner-cache/frontier_koide_q_bridge_single_primitive.txt)

## Question

The current Koide package already has strong executable support for
`Q = 2/3`, but the physical/source-law bridge remains open:

> why must the physical charged-lepton packet extremize the admitted
> block-total Frobenius functional on the accepted framework surface?

This note asks the following finite algebraic question:

> under their stated premises, do the four displayed `Q`-bridge expressions
> evaluate to one common scalar?

## Exact premise ledger

This note proves a conditional algebraic theorem. Its load-bearing domain and
carrier/face inputs are explicit:

1. `r0 > 0` and `r1,r2` are real. Thus `a = r0/3 > 0`; the zero and
   negative-`a` branches are excluded.
2. The stipulated cyclic-carrier normalization is
   `E_+ = r0^2/3`, `E_perp = (r1^2+r2^2)/6`, `a = r0/3`, and
   `|b|^2 = (r1^2+r2^2)/36`.
3. The stipulated Brannen envelope is
   `sqrt(m_k) = v_0(1+c cos(delta+2 pi k/3))`, with the carrier match
   `c = 2|b|/a` and `c > 0`.
4. The dimension face uses the stated mixed-dimension convention
   `dim_C(spinor)=2` and `dim_R(Cl^+(3))=4`.
5. The Yukawa face is explicitly the PDG-normalized doublet convention
   `T=1/2` and `|Y|=1/2`.

Items 2-5 are theorem premises, not claimed first-principles outputs of this
note. In particular, item 5 is a convention-fixed support face, not a claim
that the framework selects a hypercharge convention or physically identifies
the charged-lepton carrier.

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

Under premises 4-5, the runner separately verifies that the three displayed
representation/Yukawa expressions evaluate to the same scalar value:

```text
dim(spinor) / dim(Cl^+(3)) = 1/2,
T(T+1) - Y^2 = 1/2,
(T(T+1) - Y^2) / (T(T+1) + Y^2) = 1/2
```

These numerical coincidences do not derive premises 4-5 and do not identify a
physical source law.

## Exact finite comparison

The theorem compares exactly the following four expressions:

```text
|b|^2/a^2,
dim(spinor)/dim(Cl^+(3)),
T(T+1)-Y^2,
[T(T+1)-Y^2]/[T(T+1)+Y^2].
```

Under premises 1-5, each is `1/2`; premises 1-3 also give the displayed
consequence chain through `Q=2/3`. This is not an exhaustiveness claim about
other arithmetic constructions or physical bridge routes. A theorem selecting
these premises for a physical charged-lepton packet is outside this note and
is neither proved impossible nor assessed here.

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
`c=-sqrt(2)`, not `+sqrt(2)`. Direct summation of the three envelope terms
gives

```text
Q(c) = 1/3 + c^2/6,
```

so `c=sqrt(2)` gives

```text
Q = 2/3
```

independently of `delta`.

### 4. April 22 support faces

Under the explicit face conventions in premises 4-5, three support quantities
hit the same scalar immediately:

```text
dim(spinor) / dim(Cl^+(3)) = 2 / 4 = 1/2,
T(T+1) - Y^2 = 1/2,
(T(T+1) - Y^2) / (T(T+1) + Y^2) = 1/2
```

The runner now asserts all three displayed faces, including the normalized
Casimir ratio omitted by the earlier artifact. Conditional on the stated face
assignments, they coincide with `P_Q = 1/2`. No conclusion about unlisted
support constructions follows.

## What this does not claim

- It does **not** prove that the physical charged-lepton packet must realize
  `P_Q = 1/2`.
- It does **not** derive the cyclic-carrier normalization, Brannen carrier
  match, mixed-dimension convention, or PDG-normalized Yukawa labels listed in
  the premise ledger.
- It does **not** close the Brannen-phase bridge behind `delta = 2/9`.
- It does **not** promote the overall scale `v_0`.

## Bottom line

For the explicitly stipulated algebraic packet, the four listed expressions
share the common scalar value

> `P_Q = |b|^2 / a^2 = 1/2`.

This theorem does not claim that the list is exhaustive or select the premises
physically.
