# Supplied `3 x 3` Hermitian-Circulant / `P_23` Even-Odd Algebra Lemma

**Claim type:** bounded_theorem

**Date:** 2026-04-15  
**Status:** exact finite-dimensional algebra lemma for the supplied matrix
conventions; no physical-observable identification
**Script:** `scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py`

## Question

For the supplied cyclic shift `S` and exchange matrix `P_23`, what is the exact
real coefficient space of `3 x 3` Hermitian circulant matrices, how does it
split under `P_23`, and what is the displayed entrywise odd polynomial?

## Supplied conventions

Use zero-based matrix indices and

```text
S = [[0,1,0],       P_23 = [[1,0,0],
     [0,0,1],               [0,0,1],
     [1,0,0]],              [0,1,0]].
```

Thus `S^3 = I`, `S^2 = S^dag`, and `P_23 S P_23 = S^2`. Define the real
Hermitian basis

```text
B_0   = I,
B_+   = S + S^2,
B_-   = i(S - S^2).
```

The supplied family is

```text
K(d,c_even,c_odd) = d B_0 + c_even B_+ + c_odd B_-,
```

with `d`, `c_even`, and `c_odd` real. In this exact convention,

```text
K_01 = c_even + i c_odd.
```

The plus sign is part of the supplied `S` and zero-based-index convention.

## Bounded algebra lemma

**Lemma.** The real vector space of `3 x 3` Hermitian matrices commuting with
the supplied `S` is exactly

```text
span_R {B_0, B_+, B_-}.
```

The expansion is unique. With the Hilbert-Schmidt pairing
`<A,B> = Tr(A^dag B)`, its coefficients are

```text
d      = <B_0,K> / 3,
c_even = <B_+,K> / 6,
c_odd  = <B_-,K> / 6.
```

Conjugation by `P_23` acts as

```text
B_0 -> +B_0,
B_+ -> +B_+,
B_- -> -B_-.
```

Therefore the `P_23`-even subspace has real dimension two and the `P_23`-odd
subspace has real dimension one. Equivalently, `c_odd` is the unique
`P_23`-odd coefficient in this supplied Hermitian-circulant algebra.

Finally, direct multiplication of the displayed entry gives the exact
coordinate identity

```text
A_01(K) := Im[(K_01)^2] = 2 c_even c_odd.
```

It follows algebraically that `A_01(P_23 K P_23) = -A_01(K)` on this family.
It is also odd under entrywise complex conjugation. In a convention where
complex conjugation is called the algebraic CP action, `A_01` may therefore be
called an algebraic CP-odd polynomial. That terminology does not make it a
physical CP or leptogenesis observable.

## Basis statement

The coefficient triple and the one-dimensional odd subspace are
basis-covariant: after simultaneous unitary conjugation of `K`, `S`, `P_23`,
and the three basis matrices, the Hilbert-Schmidt extraction returns the same
coefficients and the parity multiplicities remain `(2 even, 1 odd)`.

The coordinate functional `A_01(K) = Im[(K_01)^2]` is different. It refers to
the displayed zero-based `01` entry and is not invariant under an arbitrary basis change.
Any physical use must first supply a readout theorem selecting that coordinate
or replacing it by a justified basis-invariant observable.

## Exact scope firewall

This bounded lemma proves only finite-dimensional supplied-matrix algebra. It
does **not** prove that:

- the supplied `K` is the physical heavy-neutrino or right-Gram carrier;
- framework dynamics generate particular values of `d`, `c_even`, or
  `c_odd`, or require `c_odd != 0`;
- `A_01` is a decay asymmetry, a leptogenesis invariant, or any other
  physical readout;
- a nonzero algebraic polynomial survives normalization, channel summation,
  washout, kinetics, or thermal transport.

The remaining repair class is `missing_bridge_theorem`. Promotion to a
physical statement would require, separately:

1. a **carrier bridge** identifying the supplied matrix and basis with the
   physical right-Gram/heavy-neutrino carrier;
2. a **source/activation bridge** deriving the coefficients, including any
   nonzero odd coefficient, from framework inputs;
3. a **readout bridge** deriving the relevant physical CP/leptogenesis
   observable, its normalization, and its basis/rephasing convention from the
   carrier rather than defining it to be `A_01`;
4. a **transport bridge** carrying that observable through rates, washout,
   kinetics, and thermal evolution to a physical asymmetry.

None of those bridges is supplied here.

## What this closes

This closes the bounded algebra questions:

- the full real Hermitian-circulant parametrization;
- the unique `P_23`-odd coefficient;
- exact Hilbert-Schmidt coefficient extraction;
- the convention-fixed identity
  `Im[(K_01)^2] = 2 c_even c_odd`.

## What this does not close

This note does not identify a physical carrier, source law, observable, or
transport law, and it does not state that any coefficient must be activated.

## Command

```bash
python3 scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py
```
