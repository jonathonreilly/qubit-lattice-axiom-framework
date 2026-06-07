# Flavor Idempotent U(1) Collapse Boundary

**Date:** 2026-05-30
**Updated:** 2026-06-07
**Claim type:** bounded_theorem
**Claim boundary:** exact finite negative boundary for the idempotent-U(1)
route. The note proves the idempotent U(1) is native and inert, and that the
opposite-charge route leaves the idempotent span. It does not claim a physical
sector-ordering theorem or a framework-native selector for charged-fermion
mass ordering.
**Runner:** `scripts/flavor_idempotent_u1_collapses_2026_05_30.py`
(SCORECARD PASS=7 FAIL=0).

## Scope

The tested route is the continuous idempotent symmetry

```text
U(phi,psi) = exp(i phi) P_s + exp(i psi) P_d,
P_s = J/3,        P_d = I - J/3.
```

This is a polynomial in the `C_3` shift and is distinct from rephasing the
generator. In the Fourier basis it applies the same phase to the two doublet
modes. That is the exact route tested here.

## Exact Collapse

### 1. The Idempotent U(1) Is Native But Inert

The idempotent U(1) commutes with the `C_3` generator:

```text
[U,C] = 0.
```

Therefore it is silent with respect to the generator-rephasing obstruction
and genuinely dodges a blanket "no doublet U(1)" reading. But the same
commutation makes it inert by conjugation on any circulant Hamiltonian:

```text
U H U^dagger = H.
```

So it cannot orient `b`, fix `r`, or select a Koide weight.

### 2. The Nontrivial One-Sided Action Is Not A Hermitian Route

The one-sided operation

```text
H -> H U^dagger
```

is generally non-Hermitian and has complex eigenvalues. It is not the signed
Hermitian Brannen readout used by the Koide value lane. Algebraically, this is
the chiral/asymmetric split that the
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
boundary rules out for the `C_3`-equivariant anticommuting route.

### 3. Opposite Doublet Charge Leaves The Idempotent Span

Let `P_0,P_1,P_2` be the `C_3` spectral projectors. The equal doublet charge

```text
P_1 + P_2
```

is exactly `P_d` and is idempotent-native. The opposite charge

```text
P_1 - P_2
```

is not in `span{P_s,P_d}`. It is the mode-splitting move associated with
generator rephasing, the route handled by
[`KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md`](KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md).

## Ordering Table Demoted To Comparator

The older note also discussed the observed ordering

```text
r_lepton < r_down < r_up.
```

That table is not used as a theorem here. The runner keeps a minimal
non-load-bearing check: the supplied charge and color labels do not monotonely
index the supplied `r` order. This does not prove the absence of every possible
sector selector, and it does not derive charged-fermion ordering from the
framework.

The only retained role is route-pruning:

```text
the idempotent U(1) does not supply the selector.
```

## One-Hop Authorities

- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  supports the native finite `C_3`/idempotent generation algebra context.
- [`KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md`](KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md)
  supplies the generator-rephasing boundary.
- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  supplies the chiral/anticommuting route boundary.

## Bottom Line

The idempotent-U(1) route is a clean finite negative boundary:

```text
native equal-doublet U(1) -> inert;
one-sided action -> non-Hermitian/chiral boundary;
opposite doublet charge -> outside idempotent span / generator-rephasing route.
```

It sharpens the old `C^3=I` wording: the obstruction is not a blanket ban on
all doublet U(1)s. The idempotent U(1) exists, but it selects nothing. The
charged-fermion sector selector remains a separate open bridge.
