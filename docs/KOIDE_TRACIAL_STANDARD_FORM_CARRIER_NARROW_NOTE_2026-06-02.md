# Koide Tracial Standard-Form Carrier Boundary

**Date:** 2026-06-02
**Updated:** 2026-06-07
**Claim type:** bounded_theorem
**Claim boundary:** supplied-carrier finite algebra. The note proves what a
specified tracial standard-form `R[Z_3]` carrier does and does not determine.
It is not a Tier-A admission, not a framework-axiom revision, and not a
derivation of the physical carrier/scoring rule from Lattice + Quantum +
Record.
**Primary runner:** [`scripts/koide_tracial_standard_form_carrier_2026_06_02.py`](../scripts/koide_tracial_standard_form_carrier_2026_06_02.py)
(SCORECARD PASS=10 FAIL=0).

## Scope

The input analyzed here is explicitly supplied:

```text
R[Z_3] acting on L^2(R[Z_3], tau)
```

with normalized trace `tau`, cyclic vector `Omega=e`, and group-element ONB
`{e,g,g^2}`. The mass coefficient vector is

```text
H = a e + b(g+g^2).
```

The source-side status is therefore bounded support: it proves exact finite
facts about this supplied carrier, while the framework-native physical
selection of the carrier and of its scoring rule remains open.

## Theorem 1: Standard Form Distinguishes The Group-Element Split

In the tracial GNS standard form,

```text
<Omega, pi(g^k) Omega> = tau(g^k),
```

and `{e,g,g^2}` is an orthonormal basis. The cyclic vector is one of those ONB
vectors, so the orthogonal decomposition

```text
L^2 = C Omega  (+)  Omega^perp
    = span{e}  (+)  span{g,g^2}
```

is determined from `(Omega, <.,.>)` without diagonalizing the shift operator.
This is the identity/non-identity group-element split with dimensions `(1,2)`.

The idempotent/Fourier split is also a valid algebraic decomposition, but its
singlet line is the democratic vector

```text
(e+g+g^2)/sqrt(3).
```

Its overlap with `Omega=e` is `1/sqrt(3)`, neither `0` nor `1`. Recovering that
line therefore imports spectral/Fourier structure beyond the cyclic vector.
Thus, on the supplied standard-form carrier, the cyclic vector ranks the
group-element split ahead of the idempotent split.

## Theorem 2: The Hilbert-Schmidt Arithmetic Is Exact

For `J_N` the all-ones matrix and `B_N=J_N-I_N`,

```text
||I_N||^2 = N,        ||B_N||^2 = N(N-1),        <I_N,B_N> = 0.
```

If an additional scoring rule assigns equal energy to the two
cyclic-vector channels, then

```text
N a^2 = N(N-1)b^2,
```

so

```text
r = |b|^2/a^2 = 1/(N-1).
```

At `N=3`, this gives `r=1/2`, and the finite `C_3` Koide coordinate gives

```text
Q = 1/3 + (2/3)r = 2/3.
```

This is a theorem about the supplied carrier plus the supplied channel-count
scoring rule. It is not a derivation of that scoring rule from the baseline
axioms.

## Honest Residual

After the supplied carrier distinguishes the `(1,N-1)` split, one live choice
remains on that split:

| scoring on the split | condition | `r` | `Q` |
|---|---|---:|---:|
| equal energy per channel | `a^2 = 2b^2` | `1/2` | `2/3` |
| equal energy per basis direction | `a^2 = b^2` | `1` | `1` |

The idempotent equal-power option also remains expressible as algebra:

```text
(a+2b)^2 = 2(a-b)^2
```

which gives

```text
r = 17/2 - 6 sqrt(2).
```

The standard form demotes this idempotent route relative to the cyclic-vector
split, but it does not by itself adjudicate channel-counting versus
direction-counting on the cyclic-vector split.

## Relation To Record

The current Record axiom and
`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05` allow finite additive
record coordinates once a readout surface is specified. They do not provide
the generation carrier, the `K`/CPT context, or the scoring rule. The present
theorem is therefore compatible with the approved Record surface but is not
promoted by Record into an unbounded Koide-value derivation.

## What Is Removed

This update removes three overstrong roles from the earlier source:

1. It is not a Tier-A candidate/admission source.
2. It is not an axiom-surface proposal.
3. The Kahler/Dirac/Majorana and signed-readout statements are not used as
   physical predictions or load-bearing support here.

The Kahler identity

```text
a^2 + 4b^2 = 2(a^2+b^2)
```

is retained only as a finite algebraic corroborator that also returns
`r=1/2` under its own supplied scoring functional.

## Bottom Line

The supplied tracial standard-form carrier gives a real algebraic improvement:
`Omega=e` distinguishes the identity/non-identity `(1,2)` split from the
idempotent split. The positive Koide value still needs a separate theorem
selecting channel-count scoring as the physical generation readout. Until that
theorem exists, this row is bounded support, not an unbounded framework
consequence.
