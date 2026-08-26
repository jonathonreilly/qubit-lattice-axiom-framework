# Adversarial scout batch 1 (S1-S4)

Date: 2026-08-26

## Construction and arithmetic contract

- Authority used: landed Block 190 note and its displayed unit-volume Hodge block at `(m,c)=(9/20,5/13)`.
- The carrier is rebuilt from the displayed formulas: staggered antisymmetric kernel, `d_K=P1 K P0+P2 K P1`, site reflection `theta_s(t)=-t`, quarter-weighted four-corner Hodge assembly, closed-half restricted raising set with fixed-slice spatial edges removed, `D_s=A_s-P_s A_s P_s`, `Q=mH+HD_s-D_s^T H`, `G=Q^{-1}`, reflected pairings `L_k`, and `W=K_c^{-1}L_2` with `K_c=L_0`.
- All computations are exact over `QQ` using SymPy `Rational`/`DomainMatrix`. No floating-point conversion and no `nsimplify` call is used for any claimed equality, sign, rank, determinant, polynomial, root count, or bracket endpoint.
- The Block 190 runner's expected-value constants and cached PASS output are not used as computational input. Later notes and earlier scout/check findings are not used as authority for the four results below.

Results are appended below as each independent check completes.

## S1 — `Z_16 x Z_8`: structural package confirmed; new-quartic positivity REFUTED

The carrier was rebuilt with `T=16`, `X=8`, `(m,c)=(9/20,5/13)`, the temporal minus sign on the wrap edge `t=15`, and the same four-corner Hodge block/quarter-weighted cell assembly. Exact results:

- `nnz(d_K^2)=0`.
- `nnz(P_s H P_s-H)=0`.
- `nnz(P_s Q P_s-Q^T)=0`.
- The directed cross block `Q[{1..7}xZ_8,{9..15}xZ_8]` has `0` nonzero entries.
- At `t0=3`, `K_c` is a symmetric rank-16 matrix and all 16 leading principal minors are strictly positive: signs `(+)^16`.
- `nnz([W,U_2])=nnz([W,U_4])=0`, where `U_j` is spatial translation by `j` sites on both time layers of the core.
- The exact `QQ` factorization is

  ```text
  charpoly(W)
   = (22569375 z^2 - 233631106 z + 22569375)^2
     (39529825 z^2 - 109432706 z + 39529825)^2
     (1035991876210625 z^4 - 10651994137075200 z^3
      + 31207521664211586 z^2 - 10651994137075200 z
      + 1035991876210625)^2.
  ```

Thus the `X=4` spectrum does embed verbatim and the only additional irreducible factor is the stated palindromic quartic, with multiplicity two.

The requested positivity claim for that quartic is **false**. Write the quartic as

```text
q(z)=A z^4+B z^3+C z^2+B z+A
```

with

```text
A=1035991876210625,
B=-10651994137075200,
C=31207521664211586.
```

For `u=z+z^{-1}`,

```text
q(z)/z^2 = A u^2+B u+(C-2A).
```

The exact discriminant of this `u`-quadratic is

```text
B^2-4A(C-2A) = -7271743246281426848714247040000 < 0.
```

Because `A>0`, the `u`-quadratic is strictly positive for every real `u`. Therefore `q` has no real roots (positive or negative); its four roots are nonreal and arranged by the real-palindromic symmetries into conjugate/reciprocal pairs. The quartic is palindromic, but it does **not** have real positive reciprocal roots. This refutes only the added positivity sentence, not the factorization or commutant claims above.

## S2 — heavy descended operator: confirmed, with positivity on the whole PD-symmetrizer cone

For `T=16`, `X=4`, and the interior domain `D={2,3,4}`, let `A={1,...,7}` be the full positive span. The exact rectangular reflected Gram `K_AD` has rank `8` and nullity `4`. If `N` is an exact basis matrix for `ker(K_AD)`, the two-step pairing satisfies

```text
rank(M_2,AD N)=0,   nnz(M_2,AD N)=0.
```

Thus the two-step shift descends from this nontrivial interior window. In the deep pair-core section `t0=3`, restrict the descended operator to the `U=-1` basis

```text
(-e_0+e_2, -e_1+e_3, -e_4+e_6, -e_5+e_7).
```

The resulting rational `4 x 4` operator `T_h` has

```text
charpoly(T_h) = (22569375 z^2-233631106 z+22569375)^2.
```

The original OS heavy Gram does not symmetrize it: its self-adjointness defect has exact rank `2`. However, solving the ten-variable linear system

```text
Theta=Theta^T,   Theta T_h=T_h^T Theta
```

over `QQ` gives rank `4` and hence a **six-dimensional** solution space. One exact positive-definite point, scaled to a primitive integer matrix, is

```text
Theta_0 =
[[ 256188293929, -145831898304,   40299876000,             0],
 [-145831898304,  632499095019, -117780540375,             0],
 [  40299876000, -117780540375,  117780540375,             0],
 [             0,             0,             0, 117780540375]].
```

Its leading principal minors are

```text
(256188293929,
 140771921501605873763235,
 13383448550941614697630635533347500,
 1576309802410914094161978485272344882655312500),
```

all strictly positive. Entrywise, `Theta_0 T_h-T_h^T Theta_0=0`, and the leading principal minors of the symmetric product `Theta_0 T_h` are

```text
(206290344745,
 42555706335010949115025,
 13383448550941614697630635533347500,
 1576309802410914094161978485272344882655312500),
```

again all strictly positive.

The product's positivity is **choice-independent on the whole PD part of the symmetrizer space**, not special to `Theta_0`. Indeed, for any `Theta>0` satisfying `Theta T_h=T_h^T Theta`,

```text
A = Theta^(1/2) T_h Theta^(-1/2)
```

is real symmetric and similar to `T_h`. The heavy quadratic has positive discriminant, positive leading/constant coefficients, and `233631106>2*22569375`, so every eigenvalue of `T_h`, hence of `A`, is strictly positive. Therefore `A>0`, and

```text
Theta T_h = Theta^(1/2) A Theta^(1/2) > 0
```

by congruence. Thus every positive-definite `Theta` in the six-dimensional intertwiner space makes `Theta T_h` symmetric positive-definite.

## S3 — `T=24`: confirmed

At `X=4`, `(m,c)=(9/20,5/13)`, unit volume, and the wrap-edge sign at `t=23`, the independently rebuilt exact factorizations are:

```text
t0=3 (deep):
  (22569375 z^2-233631106 z+22569375)^2
  (39529825 z^2-109432706 z+39529825)^2.

t0=1 (near boundary):
  (22569375 z^2-233631106 z+22569375)
  (39529825 z^2-109432706 z+39529825)^2
  (43033320714375 z^2-445467467014578 z+48554286398375).
```

The deep spectrum is therefore width-locked at `T=24`, and the `t0=1` boundary spectrum is exactly the stated heavy-once/light-twice/boundary-quadratic value.

## S4 — positivity edge: endpoint mechanism identified and bracket tightened

For this varying-`c` probe I used the exact unit-volume Hodge law whose `c=5/13` specialization is the Block 190 displayed matrix,

```text
B(c,1) = diag(1, g(c)^(-1), 1),
g(c)^(-1) = (1/(1-c^2)) [[1,-c],[-c,1]].
```

At `T=16`, `X=4`, `t0=3`, and `m=9/20`, the stated endpoint classifications are confirmed.

At the positive endpoint `c=2363/3328`,

```text
charpoly(W)
 = (138122825041956 z^2-132300504979805593 z+138122825041956)^2
   (28700201890091044 z^2-74623855549539593 z+28700201890091044)^2.
```

Both factors are palindromic, both discriminants are strictly positive, and both middle coefficients are negative with magnitude greater than twice the leading coefficient. Hence all roots are real, positive, and reciprocal.

At the failing endpoint `c=365/512`,

```text
charpoly(W)
 = (30557412700 z^2+73498345029689 z+30557412700)^2
   (16000240718500 z^2-41558978418089 z+16000240718500)^2.
```

The discriminants are respectively

```text
5402002987081326057806276721 > 0,
703117874955405695913411921  > 0.
```

Therefore the failed structural leg is **a negative reciprocal pair**: the first factor has `a>0`, constant `a`, positive middle coefficient, and positive discriminant, so both of its roots are real and negative with product one. The second pair remains real, positive, and reciprocal. Squared multiplicity and palindromicity both survive; there is no complex-root failure at this endpoint.

Three exact bisections give:

| probe | exact `c` | result |
| --- | ---: | --- |
| midpoint 1 | `9471/13312` | positive: both squared palindromic factors have real positive reciprocal roots |
| midpoint 2 | `18961/26624` | fails: one squared palindromic factor has a real negative reciprocal pair |
| midpoint 3 | `37903/53248` | positive: both squared palindromic factors have real positive reciprocal roots |

Thus the tightened exact bracket is

```text
(37903/53248, 18961/26624),
```

with the lower endpoint positive and the upper endpoint failing. Its width is one eighth of the supplied bracket's width.

## Batch verdict

| scout | adversarial result |
| --- | --- |
| S1 | Structural package and stated factorization confirmed; **new-quartic positivity refuted** by a negative exact `u`-discriminant. |
| S2 | Confirmed; the symmetric intertwiner space is 6-dimensional, contains an explicit rational PD metric, and `Theta T_h` is PD for **every** PD symmetrizer in that space. |
| S3 | Confirmed exactly at both the deep and `t0=1` boundary cores. |
| S4 | Confirmed; failure at `365/512` is a **real negative reciprocal pair**, with squared palindromicity intact; bracket tightened to `(37903/53248,18961/26624)`. |
