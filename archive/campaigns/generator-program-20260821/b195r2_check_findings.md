# Block 195 round-2 adversarial check: sectored interior reconstruction

Date: 2026-08-25

## Scope and exact target contract

- **Target:** independently reconstruct the interior compressed pair \((K_c,M_{2c})\) from the landed Block-190 width-family construction and test C1--C5 and P1--P3.
- **Domains:** primary \(T=16\), confirmation \(T=20\); fixture \((m,c)=(9/20,5/13)\); non-control point \((1/2,1/3)\).
- **Arithmetic:** exact `Integer`/`Rational`/`QQ` only. `nsimplify` is forbidden and is not used.
- **Authority:** committed Block-190 construction at `e75ad9f499`; in particular its displayed unit-volume Hodge block and wrap-edge sign convention.
- **Completion witness:** exact ranks, exact characteristic polynomials, exact symmetry/congruence residuals, exact principal minors or an exact positive-definiteness certificate, and explicit rational skew-form data.
- **Non-closure:** floating eigenvalues, basis counts in place of invariant ranks, or reproducing target constants without deriving the matrices do not count.

## Running status

Construction extraction, independent exact reconstruction, representative-change attacks, and the rank-two defect analysis are complete. Verdicts default to **REFUTED** if any conjunct fails.

## Independent reconstruction

I rebuilt the Block-190 width family directly from its displayed formulas:

\[
B(c,1)=\operatorname{diag}\!\left(1,
 \frac1{1-c^2}\begin{pmatrix}1&-c\\-c&1\end{pmatrix},1\right),
\qquad Q=mH+HD_s-D_s^T H,
\]

with the wrap-edge temporal sign, the stated grading, the closed-half raising set, and the site reflection \(\theta_s(t)=-t\). I did not call the Block-190 runner. All inverses, ranks, determinants, kernels, and characteristic polynomials were computed over `QQ` using exact fraction-free matrices.

For both widths the column pivots of the full-to-interior Gram map are

```text
(0,1,2,3,4,5,6,7),
```

so the default representative set is the pair core

```text
((2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)).
```

The interior domain has slices `2..4` at \(T=16\) and `2..6` at \(T=20\), exactly as dispatched.

## Claim verdicts

### C1 — **CONFIRMED**

Let \(A=K_{\rm full}[:,D]\) and \(B=M_2\), regarded as maps with the same interior domain. I used the basis-independent obstruction

\[
\operatorname{rank}\!\begin{pmatrix}A\\B\end{pmatrix}-\operatorname{rank}(A),
\]

which is zero exactly when \(\ker A\subseteq\ker B\). The exact results are

| width | `rank(K_full)` | `rank(A)` | `rank(vstack(A,B))` | obstruction rank |
|---:|---:|---:|---:|---:|
| 16 | 8 | 8 | 8 | **0** |
| 20 | 8 | 8 | 8 | **0** |

Thus this is not a basis-count argument: the shifted map descends to the same eight-dimensional quotient at both widths.

### C2 — **CONFIRMED**

At both widths `nnz(Kc-Kc.T)=0`; its eight leading-minor signs are `(+,+,+,+,+,+,+,+)`, so the compressed Gram is positive-definite. The primitive exact factorization is

\[
\chi_{T_2}(z)=
(22569375z^2-233631106z+22569375)^2
\,
(39529825z^2-109432706z+39529825)^2.
\]

The two primitive factor records returned over `QQ` are

```text
((22569375,-233631106,22569375), multiplicity 2)
((39529825,-109432706,39529825), multiplicity 2).
```

### C3 — **CONFIRMED**

For \(P_+=(I+U)/2\), the exact defect ranks are

```text
T=16: rank(P+^T (M2c-M2c^T) P+) = 0
T=20: rank(P+^T (M2c-M2c^T) P+) = 0.
```

In the rational light basis, for \(t=2,3\),

\[
e_{t,0}+e_{t,2},\quad e_{t,1}+e_{t,3},
\]

the restricted form is entrywise symmetric at both widths. Its operator polynomial is exactly

\[
(39529825z^2-109432706z+39529825)^2.
\]

The four exact leading-minor sign certificates for both \(K_+\) and \(M_{2,+}\) are

```text
T=16: K+ (+,+,+,+), M2+ (+,+,+,+)
T=20: K+ (+,+,+,+), M2+ (+,+,+,+).
```

No floating inertia call is used: each sign is the sign of an exact rational determinant. Therefore the light form is positive-definite, and \(T_{2,+}=K_+^{-1}M_{2,+}\) is a positive \(K_+\)-self-adjoint operator on this finite quotient.

### C4 — **CONFIRMED**

The complete compressed defect has rank 2 at both widths. Exact spectral-projector localization gives, in the order \((+,+),(-,-),(+,-),(-,+)\),

```text
T=16: (0,2,0,0)
T=20: (0,2,0,0).
```

The heavy-sector characteristic polynomial is exactly

\[
(22569375z^2-233631106z+22569375)^2.
\]

For both \(K_-\) and the symmetric part \((M_{2,-}+M_{2,-}^T)/2\), the four exact rational leading-minor signs are

```text
T=16: K- (+,+,+,+), Sym(M2-) (+,+,+,+)
T=20: K- (+,+,+,+), Sym(M2-) (+,+,+,+),
```

so the symmetric part is positive-definite at both widths.

### C5 — **CONFIRMED**

Every C1--C4 invariant above is unchanged at \(T=20\): obstruction rank, Gram symmetry, complete and sector characteristic polynomials, defect rank/localization, light symmetry/positivity, and heavy symmetric-part positivity all agree exactly. The forms themselves are width-dependent; the claim is stability of the stated quotient invariants, not entrywise equality of the forms.

## Required probes

### P1 — **CONFIRMED: not a pivot artifact**

I used two alternative quotient sections at each width:

1. the full pair core `t0=3`, i.e. slices `3,4`;
2. a deterministic random full-rank eight-element subset of `D`, deliberately not closed under the displayed permutation `U`.

The random representatives were

```text
T=16: ((2,0),(2,2),(2,3),(3,2),(3,3),(4,0),(4,1),(4,3))
T=20: ((2,1),(3,2),(4,2),(5,0),(5,3),(6,0),(6,1),(6,3)).
```

If \(P\) is the exact change from an alternative quotient section to the pivot section, all four runs give

```text
det(P) != 0
nnz(K_alt - P^T K_pivot P) = 0
nnz(M_alt - P^T M_pivot P) = 0
nnz(T_alt - P^-1 T_pivot P) = 0.
```

For the random sections the induced quotient involution is \(U_{\rm alt}=P^{-1}U_{\rm pivot}P\); it need not be a coordinate permutation, but \(U_{\rm alt}^2=I\) exactly. Every alternative section reproduces light defect rank 0, heavy defect rank 2, both sector polynomials, and the `(+,+,+,+)` positivity certificates. The sector statements are therefore basis-independent congruence/similarity statements.

### P2 — exact skew form and copy interpretation

At \(T=16\), use the heavy basis

```text
(-e_(2,0)+e_(2,2), -e_(2,1)+e_(2,3),
 -e_(3,0)+e_(3,2), -e_(3,1)+e_(3,3)).
```

Then \(D_-=M_{2,-}-M_{2,-}^T=sJ\), exactly, where

\[
s=\frac{15412245266178664398193359375000000}
{12468368115055868578374473995988256597352642542544230293}
\]

and

\[
J=\begin{pmatrix}
0&0&-499791697674660&1588013041094501\\
0&0&12377859914160&-39328790486076\\
499791697674660&-12377859914160&0&0\\
-1588013041094501&39328790486076&0&0
\end{pmatrix}.
\]

This has exact rank 2. A two-direction wedge factorization is

\[
D_- = \gamma(uv^T-vu^T),
\qquad
\gamma=-s,
\]

with

\[
u=(0,0,2034493740,-6464298239)^T,
\qquad
v=(-245659,6084,0,0)^T.
\]

The exact reconstruction residual is zero. The vectors are orthogonal, with

\[
u^Tu=45926316500837688721,
\qquad
v^Tv=60385359337,
\]

and satisfy \(D_-u=-\gamma(u^Tu)v\), \(D_-v=\gamma(v^Tv)u\). Thus they are exact unnormalised rational singular directions, and
\(\operatorname{im}D_-=\operatorname{span}_{\mathbb Q}\{u,v\}\). Normalising them would add irrelevant square roots, so the certificate stays over `QQ`. On the full quotient

```text
nnz(U^T D U-D)=0,   nnz(UD-DU)=0,
```

so the defect is exactly \(U\)-equivariant. The displayed block-off-diagonal shape shows that it pairs one direction in each of the two heavy time-layer planes. Whether that equals a canonical pairing of the two *spectral* copies is treated separately below; it does not follow from rank two alone.

The stronger spectral-copy reading is **not true canonically**. On the heavy sector, with

\[
q(z)=22569375z^2-233631106z+22569375,
\]

the exact residual `nnz(q(T2_minus))` is zero. Its discriminant is

\[
52545986939220736
=2^8\,13\,31\,37\,71\,313^2\,1979,
\]

which is not a rational square. Hence the heavy rational module is two isomorphic copies of the irreducible quadratic module, but a splitting into those two copies is not unique. The landed one-site shift gives an additional exact commuting complex structure \(S_-\):

```text
nnz(S_minus^2 + I) = 0
nnz(S_minus T2_minus - T2_minus S_minus) = 0.
```

This canonically distinguishes the two momentum copies after scalar extension. A defect that *purely paired* those conjugate copies would obey \(S_-^T D_-S_-=D_-\). It does not:

```text
nnz(S_minus^T D_minus S_minus - D_minus) = 8
nnz(S_minus^T D_minus S_minus + D_minus) = 8.
```

Moreover, the `S`-even and `S`-odd pieces

\[
\tfrac12(D_-+S_-^TD_-S_-),\qquad
\tfrac12(D_--S_-^TD_-S_-)
\]

each have exact rank **4**. Thus the rank-two cancellation contains both cross-copy and within-copy components; it is not a pure pairing of the two canonical momentum-degenerate copies. The only basis-free conclusion supported here is: the defect is rank two, entirely heavy, and \(U\)-equivariant. Its off-diagonal time-layer appearance is a coordinate fact, not an additional spectral theorem.

### P3 — **CONFIRMED structurally at the non-control point**

At \((m,c)=(1/2,1/3)\), at both \(T=16\) and \(T=20\), the obstruction rank remains 0, `Kc` remains symmetric, the total defect rank remains 2, and projector ranks remain `(0,2,0,0)`. The light form is symmetric and positive-definite; the heavy symmetric part is positive-definite. The coefficients change, as they should:

\[
\chi_{T_{2,+}}(z)=(233z^2-690z+233)^2,
\qquad
\chi_{T_{2,-}}(z)=(739z^2-7258z+739)^2.
\]

Thus the sectored *structure* persists at the requested non-control point and at both tested widths; the fixture polynomials are not universal.

## Overall verdict

- **C1--C5 survive** the round-2 adversarial check exactly at both requested widths.
- **P1 survives:** the result is a quotient-form statement, not a pivot-section artifact.
- **P2:** the defect is explicitly rank two, entirely heavy, and \(U\)-equivariant. It pairs the two heavy time-layer planes in the displayed pivot coordinates, but the stronger claim that it purely pairs the two canonical momentum-degenerate spectral copies is **refuted**.
- **P3 survives structurally:** light symmetry and heavy rank-two localization persist at \((1/2,1/3)\), with different exact polynomials.

## Reproduction gates

The independent probe is `b195r2_exact_probe.py` in this directory. Final exact runs were:

```text
python3 b195r2_exact_probe.py base     -> TOTAL: PASS=47 FAIL=0
python3 b195r2_exact_probe.py alt      -> TOTAL: PASS=52 FAIL=0
python3 b195r2_exact_probe.py control  -> TOTAL: PASS=27 FAIL=0
```

`python3 -m py_compile b195r2_exact_probe.py` passes. An AST scan reports zero floating literals, and the probe source contains no call to the forbidden simplification routine.
