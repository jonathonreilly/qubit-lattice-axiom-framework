# A^2 Below W2 Source-Literal Arithmetic Boundary

**Date:** 2026-04-25

**Status:** bounded-support / authority-boundary. This note is not a positive
closure claim on the current authority surface.

**Primary runner:**
`scripts/frontier_ckm_a_squared_below_w2_y_quantum_closure.py`

## Purpose

This note preserves the useful source-literal arithmetic behind the older
`A^2 = N_pair/N_color = 2/3` claim while removing the retained-closure
overclaim. The arithmetic is still exact:

```text
Q_L : (2,3)  ->  N_pair = dim_SU2(Q_L) = 2
Q_L : (2,3)  ->  N_color = dim_SU3(Q_L) = 3
A^2 = N_pair / N_color = 2/3
```

The current source surface does not certify this as positive closure because
the source authorities used by the old proof are not all retained-positive
load-bearing authorities. The runner therefore treats non-retained authorities
as explicit boundaries rather than hard failures or hidden retained inputs.

## Source Reading

The arithmetic route reads representation literals from the source notes:

```text
Q_L : (2,3)_{+1/3}
u_R : (1,3)_{+4/3}
d_R : (1,3)_{-2/3}
```

From the left-handed quark literal alone:

```text
N_pair  := dim_SU2(Q_L) = 2
N_color := dim_SU3(Q_L) = 3
A^2     := N_pair / N_color = 2/3
```

The right-handed quark literals remain a color-count cross-check, not a
separate authority promotion.

## Boundary

This note does not assert that the representation-literal source chain is
retained-positive on the current surface. In particular:

- the source-literal arithmetic is useful bounded support;
- the W2 identity `A^2 = N_pair/N_color = 2/3` is a consistency target, not a
  load-bearing positive authority for this below-W2 route;
- the gauge-dimension equality `dim_fund(SU(2))/dim_fund(SU(3)) = 2/3` is
  corroboration only;
- the EW arithmetic `sin^2(theta_W)|_lattice = A^4 = 4/9` is conditional
  corroboration only unless the required EW bare-coupling literals are present
  as retained-positive inputs.

## What Is Preserved

The PR should preserve this bounded result:

```text
A2_BELOW_W2_ARITHMETIC_SUPPORT = True
```

The result is exact arithmetic from extracted source literals. It introduces
no new axiom and uses no observed CKM value, fitted selector, or PDG target as
a derivation input.

## What Is Not Claimed

This note does not:

- close `A^2` below W2 on retained-positive authorities;
- promote decoration, meta, unaudited, support-tier, or no-go authorities;
- promote the EW-CKM trinity arithmetic to positive bridge status;
- change the audit ledger, audit queue, publication matrices, or lane registry.

If later review/audit promotes the required authorities, this note gives the
exact arithmetic route that could be rechecked. Until then, its honest status
is bounded support with exposed authority boundaries.
