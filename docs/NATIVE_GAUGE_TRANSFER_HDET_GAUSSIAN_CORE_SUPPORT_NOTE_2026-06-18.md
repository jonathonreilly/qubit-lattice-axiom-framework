# Native Gauge Transfer H_det Gaussian Core Support Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Claim scope:** Gaussian determinant-core support for `H_det(A)`. This note
separates the determinant-level Gaussian core from the scalar Bessel
remainder/tail problem in the native gauge-transfer Weyl-determinant assembly
lane. It does not derive `K_W(A)`, does not prove `H_det(A)` in full, and does
not prove `H_spec`.

**Primary runner:**
[`scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py`](../scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py)

**Runner cache:**
[`logs/runner-cache/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.txt`](../logs/runner-cache/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.txt)

No new axiom, fitted constant, external comparator, target value, or
literature asymptotic is used. Numerical rows below are finite certificates
for the runner's stated support surface; they are not fitted into a
Wilson-to-saddle constant.

## Targeted Blocker

The audited conditional row
`native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_note_2026-06-12`
names two missing ingredients:

```text
H_det(A):
  determinant normalization/tails for the 3x3 Bessel determinant coefficient,
  including c_(0,0) lower normalization and determinant-mode tail domination.

H_spec:
  reduced A2 spectral domination, c_D <= c_J.
```

This note works only the first ingredient, and only its Gaussian determinant
core. The remaining exact-Bessel remainder, determinant tail constants, and
`H_spec` are open after this note.

## One-Hop Inputs

- [`NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md`](NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md)
  supplies the scalar local-CLT expansion for each Bessel atom.
- [`NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md`](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  supplies the saddle diagonal target and geometric `K_geom(A)` side.

The downstream assembly row
`NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md`
names `H_det(A)` and `H_spec`; it consumes this support note but is not a
load-bearing input to it.

## Gaussian Determinant Core

For the exact Wilson coefficient convention, write `t = beta/3`,
`lambda = (p+q,q,0)`, and

```text
c_(p,q)(beta)
  = sum_(n in Z) det[I_(n + lambda_j + i - j)(t)]_(i,j=1..3).
```

The scalar local-CLT note identifies the leading Gaussian entry

```text
g_k(t) = (2 pi t)^(-1/2) exp[-k^2/(2t)].
```

Define the Gaussian determinant core

```text
G_(p,q)(beta)
  = sum_(n in Z) det[g_(n + lambda_j + i - j)(t)]_(i,j=1..3),
R_G(p,q; beta) = G_(p,q)(beta) / G_(0,0)(beta).
```

This is the determinant-level object obtained by applying the scalar leading
term before any scalar `P_1/t` or `R_2/t^2` correction. It is the correct
place to test whether the determinant normalization and the `SU(3)` saddle
shape already align before adding scalar remainders.

The saddle target is

```text
R_sad(p,q; beta) = d_(p,q) exp[-3 C2(p,q)/beta],
d_(p,q) = (p+1)(q+1)(p+q+2)/2,
C2(p,q) = (p^2 + q^2 + p q + 3p + 3q)/3.
```

## Runner Result

The runner checks:

1. `G_(0,0)(beta) > 0` on representative rows, so the Gaussian core has the
   required denominator normalization on the sampled active windows.
2. `R_G(p,q; beta) = R_G(q,p; beta)` on representative rows, checking the
   conjugation symmetry required by the `SU(3)` diagonal.
3. The selected active-window rows approach the saddle diagonal:

```text
beta= 48 (p,q)=( 4, 3) rel=+1.901967e-02
beta= 96 (p,q)=( 6, 5) rel=+1.013147e-02
beta=192 (p,q)=(10, 8) rel=+6.077474e-03
beta=384 (p,q)=(12,10) rel=+2.189001e-03
```

4. The sampled active-window sup certificate decreases:

```text
sqrt(beta) sup_{0<=p,q<=floor(1.25 sqrt(beta))}
  | beta^(-3/2)(R_G - R_sad) |

beta= 48: 1.761683e-02
beta= 96: 1.226940e-02
beta=192: 8.534372e-03
```

5. The exact-Bessel-to-Gaussian correction is also decreasing, but remains a
   separate scalar/remainder wall:

```text
beta= 48: 4.459121e-02
beta= 96: 3.083020e-02
beta=192: 2.172844e-02
```

That last row is the important boundary. The Gaussian determinant core is not
the full exact Wilson determinant. It isolates the determinant-level saddle
shape; the scalar `P_1/t`, scalar remainder, determinant-mode tails, and
`c_(0,0)` lower constants must still be converted into a uniform `K_W(A)`.

## What This Supports

This note provides upstream support for `H_det(A)`:

- the leading scalar Gaussian core, after determinant summation and
  `(0,0)` normalization, already lands on the correct `SU(3)` saddle diagonal
  on the sampled active windows;
- the determinant denominator and conjugation symmetry are checked at the same
  object level as the Weyl determinant, not at scalar-entry level;
- wrong `N_c` and wrong dimension prefactors visibly separate from the
  Gaussian core, so the `SU(3)` color constant and dimension factor are
  load-bearing.

This helps the downstream assembly because it separates the `H_det(A)` wall
into:

```text
H_det_core:
  Gaussian determinant core normalization and saddle alignment.

H_det_remainder:
  scalar P_1/R_2 propagation, determinant-mode tails, c_(0,0) lower constants,
  and a uniform K_W(A) bound.
```

Only `H_det_core` is supported here.

## What Remains Open

- No source-side value of `K_W(A)` is derived.
- No full `H_det(A)` theorem is claimed.
- No true determinant-mode or representation-weight tail constant is derived.
- No reduced A2 spectral comparison `H_spec` or `c_D <= c_J` is proved.
- No half-line gap or beta=6 physical conclusion is claimed.

## Runner

```bash
python3 scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py
```

Expected summary:

```text
TOTAL: PASS=13, FAIL=0
```
