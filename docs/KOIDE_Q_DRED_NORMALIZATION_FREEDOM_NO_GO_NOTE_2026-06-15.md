# Koide Q `D_red = I_2` Normalization-Freedom No-Go

**Date:** 2026-06-15
**Type:** no_go
**Claim type:** no_go
**Status authority:** independent audit lane only. This note does not set,
predict, or apply an audit verdict.
**Primary runner:**
[`scripts/koide_q_dred_normalization_freedom_no_go_2026_06_15.py`](../scripts/koide_q_dred_normalization_freedom_no_go_2026_06_15.py).

## Scope

This note addresses one half of the audit blocker on
`KOIDE_Q_REDUCED_OBSERVABLE_RESTRICTION_THEOREM_2026-04-22.md`:
the imported reduced baseline normalization `D_red = I_2`.

The claim is negative and narrow:

> The reduced two-slot block algebra and split-preserving source family do not
> derive the normalization `D_red = I_2`. For every `c > 0`, the baseline
> `D_red = c I_2` satisfies the same split, additivity, and determinant
> restriction structure after a source-coordinate rescaling. Therefore
> `D_red = I_2` is a normalization bridge or convention until a separate
> physical response-unit theorem fixes `c = 1`.

This does not refute the reduced-observable theorem under its stated admitted
normalization. It proves that the normalization cannot be promoted from the
two-slot algebra alone.

## Finite Algebra

Let the reduced carrier have split projectors

```text
Pi_+ + Pi_perp = I_2,
Pi_+ Pi_perp = 0,
K = k_+ Pi_+ + k_perp Pi_perp.
```

For any positive scalar `c`, take

```text
D_c = c I_2.
```

The reduced determinant generator is then

```text
W_c(K)
  = log det(D_c + K) - log det(D_c)
  = log(1 + k_+/c) + log(1 + k_perp/c).
```

If we define dimensionless source coordinates

```text
u_+ = k_+/c,
u_perp = k_perp/c,
```

then

```text
W_c = log(1+u_+) + log(1+u_perp),
```

which is the same normalized law as the `c = 1` presentation. The algebraic
support theorem therefore fixes the shape of the reduced generator, not the
absolute response-unit normalization.

The derivative at zero source exposes the residual:

```text
dW_c/dk_i |_{K=0} = 1/c.
```

Different `c` values are physically distinguishable if the source coordinate
`k_i` already has an externally fixed unit. The reduced block algebra itself
does not provide that unit.

## Consequence For `koide_q_reduced`

The existing reduced-observable row remains honest as a bounded algebraic
restriction theorem on the admitted normalized carrier. Its algebraic content
does not close the audit-named physical bridge:

- physical charged-lepton carrier/readout identification remains external;
- `D_red = I_2` remains external unless a response-unit theorem fixes `c = 1`;
- the source family `K = diag(k_+, k_perp)` is exact once the reduced carrier
  is supplied, but it does not itself fix the unit of `K`.

The cheapest positive repair is therefore not more determinant algebra. It is
a separate bridge proving that the physical charged-lepton readout supplies the
dimensionless source coordinate in which the reduced baseline is `I_2`, or an
explicit approved premise/convention for that normalization.

## What This Does Not Claim

- It does not say the `c = 1` normalized theorem is algebraically wrong.
- It does not challenge the accepted split-projector, determinant, Legendre
  dual, or unreduced `(1,2)` contrast calculations.
- It does not add an axiom or admission.
- It does not update audit results.
