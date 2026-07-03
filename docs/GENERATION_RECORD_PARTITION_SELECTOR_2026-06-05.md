# Generation Record Partition Selector

**Date:** 2026-06-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note does not set, predict, or propose an
audit outcome.
**Primary runner:** [`scripts/generation_record_partition_selector_2026_06_05.py`](../scripts/generation_record_partition_selector_2026_06_05.py)
(sympy exact algebra; **SCORECARD 25 PASS / 0 FAIL**).
**Cached log:** [`logs/runner-cache/generation_record_partition_selector_2026_06_05.txt`](../logs/runner-cache/generation_record_partition_selector_2026_06_05.txt).

## Scope and honesty

This note sharpens the partition half of the generation dynamics gate.

Given the supplied generation readout context:

- the hw=1 generation carrier carries the regular representation of `C3`;
- the readout context has a fixed `K`/CPT conjugation;
- the Record axiom names realized outcomes by `K`/CPT orbit of central sectors.

Then the native Record-compatible central partition is uniquely

```text
singlet P0  |  faithful doublet P1.
```

Equivalently: the three complex character sectors are not three native Record
letters. The two faithful character projectors are exchanged by `K`/CPT, so
Record sees their orbit as one doublet record sector. Splitting that doublet
requires the K-odd orientation operator `i(C-C^2)`, or an equivalent extra
complex basis/orientation choice inside the doublet.

This does **not** select weights, probabilities, a Born measure, a time arrow,
or a Koide value. It selects the partition only. The remaining gates are the
measure/arrow gates inside this two-sector partition.

## Relation to the existing row

[`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)
already proves that the `K`/CPT orbit count is two: a one-dimensional singlet
and a two-dimensional doublet.

This note adds the selector form needed for dynamics:

1. it enumerates all real/K-stable central idempotents;
2. it proves that the only nonzero proper ones are `P0` and `P1`;
3. it proves the faithful doublet has no finer K-stable central sub-idempotent;
4. it identifies the exact import needed to split it: the K-odd operator
   `J=i(C-C^2)`.

So the partition gate is sharpened from "two sectors exist" to "the native
Record-compatible central partition is uniquely `P0 | P1`, unless an extra
K-breaking orientation is imported."

## Setup

Let `C` be the order-3 generation cycle on the supplied carrier:

```text
C^3 = I.
```

Over `C`, the central primitive character projectors are

```text
P0 = (I + C + C^2)/3
P+ = (I + omega^2 C + omega C^2)/3
P- = (I + omega C + omega^2 C^2)/3
```

with `omega^3=1` and `1+omega+omega^2=0`.

They are orthogonal idempotents and resolve the identity:

```text
P0 + P+ + P- = I.
```

Each has complex rank `1`.

## Theorem

Under the fixed `K`/CPT conjugation of the supplied readout context:

```text
K(P0) = P0,
K(P+) = P-,
K(P-) = P+.
```

Therefore the `K`/CPT orbit sectors are:

```text
{P0}        dimension 1
{P+, P-}    dimension 2
```

Define

```text
P1 = P+ + P- = I - P0.
```

Then `P1` is a real K-fixed central idempotent of rank `2`, and the Record
alphabet has exactly two native letters:

```text
P0 | P1.
```

## Idempotent enumeration

The runner enumerates all real central idempotents of the form

```text
X = a I + b C + c C^2,       a,b,c in R,
```

by solving

```text
X^2 = X.
```

The exact solutions are only:

```text
0,
I,
P0 = (I+C+C^2)/3,
P1 = (2I-C-C^2)/3.
```

Thus `P0` and `P1` are the only nonzero proper real central idempotents. There
is no nonzero proper K-stable central sub-idempotent inside the doublet `P1`.

Equivalently, K-stable unions of the three complex character sectors are
exactly the unions of K-orbits:

```text
empty,
{P0},
{P+,P-},
{P0,P+,P-}.
```

So the full nontrivial K-stable central decomposition of identity is uniquely

```text
P0 | P1.
```

## Observable selector

A K-real C3-invariant Hermitian readout observable has the form

```text
A = alpha I + beta(C+C^2),       alpha,beta in R.
```

It acts as:

```text
A P0 = (alpha+2 beta) P0,
A P1 = (alpha-beta) P1.
```

The two faithful character projectors `P+` and `P-` always have the same
eigenvalue under any such K-real central observable. Therefore a K-real Record
readout can distinguish the singlet from the doublet, but cannot split the
doublet into the two complex characters.

The exact operator that does split the faithful pair is

```text
J = i(C-C^2).
```

It is Hermitian and C3-invariant, but

```text
K(J) = -J.
```

Its characteristic polynomial is

```text
lambda(lambda^2-3),
```

and it assigns opposite eigenvalues to the faithful character sectors. Hence
splitting the doublet requires a K-odd orientation import, not just the Record
readout context.

## Dynamics consequence

This closes the partition half of the dynamics question **within the supplied
C3 + K/CPT readout context**:

```text
Record-compatible generation partition = singlet | doublet.
```

That is exactly the partition on which the two-sector entropy setting
`s=0`, `r=1/2`, `Q=2/3` lives.

The note does not choose the arrow or measure. The next gate remains:

```text
Why should the physical charged-lepton record dynamics use the two-sector
entropy/block-counting arrow rather than Born/dimension weighting, sharpening,
or transit?
```

## Runner coverage

The runner verifies:

- `C^3=I` and exact cube-root identities;
- complex character projectors `P0,P+,P-` are orthogonal central idempotents;
- `K` fixes `P0` and swaps `P+ <-> P-`;
- `P1=P++P-` is real, K-fixed, central, and rank `2`;
- exact real central idempotent enumeration gives only `0,I,P0,P1`;
- K-stable complex-sector unions are exactly K-orbit unions;
- K-real C3-invariant observables have one singlet eigenvalue and one doublet
  eigenvalue;
- `J=i(C-C^2)` is the K-odd doublet-splitting orientation operator;
- the selector does not determine weights or dynamics.

## Net

The partition selector is a real positive result. After Record, the native
generation record partition is not an arbitrary choice among three complex
letters. It is the K/CPT-orbit partition `P0 | P1`. What remains open is not
the partition, but the physical arrow/measure on that partition.
