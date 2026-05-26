# Koide Q = 2/3 Frobenius-Extremum Algebraic Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Source status:** repair candidate for independent audit. This note does
not apply an audit verdict and does not promote any downstream Koide row.
**Primary runner:** `scripts/koide_q_two_thirds_frobenius_extremum_runner.py`

## 0. Review-Loop Boundary

This note salvages the exact algebraic core of the submitted
Frobenius-extremum bridge. Review-loop narrows the source to the retained
`C_3` theorem surfaces available on current main and removes the broad
claim that this closes the physical charged-lepton Koide lane.

The claim is only:

```text
retained C_3 circulant eigenvalue algebra
+ scoped equal-weight Frobenius extremum a^2 = 2 |b|^2
=> Q_alg(lambda) = 2/3.
```

The equal-weight Frobenius extremum is not newly derived here. It is the
scoped algebraic extremum already isolated in the retained kappa narrow
theorem. That theorem also records the open question of which Frobenius
weighting is canonical for the physical charged-lepton lane; this bridge
inherits that scoped input and does not settle it.

## 1. The Narrowed Claim

> **Theorem (signed algebraic Q at the Frobenius extremum).**
> Assume the retained circulant/character surface
> [`KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md):
>
> ```text
> H = a I + b C + bbar C^2,
> lambda_k = a + b omega^k + bbar omega^(-k),  k = 0,1,2.
> ```
>
> Assume the retained kappa Frobenius algebraic surface
> [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md):
>
> ```text
> E_+ = 3 a^2,
> E_perp = 6 |b|^2,
> equal-weight log extremum: E_+ = E_perp,
> equivalently a^2 = 2 |b|^2.
> ```
>
> Define the signed algebraic ratio
>
> ```text
> Q_alg(lambda) := (lambda_0^2 + lambda_1^2 + lambda_2^2)
>                  / (lambda_0 + lambda_1 + lambda_2)^2,
> ```
>
> when the denominator is nonzero. Then at the scoped equal-weight
> Frobenius extremum,
>
> ```text
> Q_alg(lambda) = 2 / 3.
> ```

On any chamber where all three `lambda_k` are positive, this same ratio is
the positive-vector Koide invariant used by the retained cone algebraic
equivalence theorem
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md).
Outside a positive chamber, this row asserts only the signed algebraic
identity above.

## 2. Exact Proof

The retained circulant/character bridge gives the Fourier sums:

```text
lambda_0 + lambda_1 + lambda_2 = 3 a,
lambda_0^2 + lambda_1^2 + lambda_2^2 = 3 a^2 + 6 |b|^2.
```

At the scoped equal-weight Frobenius extremum,

```text
a^2 = 2 |b|^2,
```

so:

```text
lambda_0^2 + lambda_1^2 + lambda_2^2
  = 3 a^2 + 6 |b|^2
  = 3 a^2 + 3 a^2
  = 6 a^2,
```

while:

```text
(lambda_0 + lambda_1 + lambda_2)^2 = (3 a)^2 = 9 a^2.
```

Therefore:

```text
Q_alg(lambda) = 6 a^2 / 9 a^2 = 2 / 3.
```

The proof is exact rational arithmetic after the retained Fourier and
Frobenius identities are imported.

## 3. Positive-Chamber Boundary

At `a^2 = 2 |b|^2`, the eigenvalues can be written

```text
lambda_k = a + 2 |b| cos(delta + 2 pi k / 3).
```

This vector is not positive for every phase `delta`; for example, one
phase chamber can send one cosine to `-1`, giving a negative eigenvalue.
The positive-vector Koide-cone reading is therefore chamber-limited. The
signed algebraic identity `Q_alg(lambda) = 2/3` remains exact, but a
physical charged-lepton reading needs a separate positive-spectrum/readout
bridge.

## 4. What Is Not Claimed

This bridge intentionally does not claim:

- that the framework selects the equal-weight Frobenius log-functional as
  the canonical physical extremal principle;
- that `lambda_k = sqrt(m_k)` for charged-lepton masses;
- that the eigenvalue vector is positive for every phase;
- that `delta = 2/9` or any Brannen phase is derived;
- that the parent `CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md` is promoted or
  closed;
- that any PDG mass value, fitted observational value, or radian primitive
  is used.

## 5. Dependency Boundary

The load-bearing dependencies are the three retained narrow theorem surfaces
linked in Section 1:

- the `C_3` circulant/character bridge for the eigenvalue Fourier algebra;
- the kappa Frobenius algebraic narrow theorem for the scoped
  equal-weight extremum `a^2 = 2 |b|^2`;
- the cone algebraic equivalence only for the positive-chamber
  interpretation of the signed ratio.

The older broad Koide parent notes and radian-bridge no-go notes are reader
context only. They are not load-bearing dependencies for this bounded
algebraic bridge.

## 6. Runner Slice

The primary runner is
`scripts/koide_q_two_thirds_frobenius_extremum_runner.py`. It checks:

- the exact ratio formula
  `(3 a^2 + 6 |b|^2) / (3 a)^2 = 2/3` under `a^2 = 2 |b|^2`;
- a non-extremal control where the ratio is not `2/3`;
- a positive-chamber example;
- a non-positive phase example, to keep the physical Koide reading out of
  the global claim.

The runner does not inspect audit-ledger status, audit queues, effective
status, or dependency closure. Those are generated by the audit pipeline
after the source row is parsed.

## 7. Audit Boundary

Audit status is set only by the independent audit lane. The intended
source-side claim type is `bounded_theorem`: assuming the retained
circulant/character algebra and the scoped equal-weight Frobenius extremum,
exact algebra gives `Q_alg(lambda) = 2/3`. This row does not derive the
physical charged-lepton Koide relation and does not promote downstream
Koide claims.
