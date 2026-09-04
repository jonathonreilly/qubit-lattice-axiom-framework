# Block 184 adversarial check — temporal-link extraction

Method: independent reconstruction from the public APIs in
`admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py`, with
exact SymPy expressions throughout. No floating-point value was used in any
decision, and no supervisor scratch artifact was read.

## C1 — bands: CONFIRMED

For symbolic positive `m`, the exact nonzero-count table of `Q_min` is

`{0: 80, 1: 72, 2: 16, 6: 16, 7: 72}`.

All three asserted non-identities hold. In fact,

- `B_-1 != B_+1^dagger`; the residual has 40 nonzeros, with witness
  `(B_-1-B_+1^dagger)[0,4] = 1121503/714000`.
- `B_-1 != -B_+1^dagger`; the residual has 32 nonzeros, with witness
  `(B_-1+B_+1^dagger)[0,7] = -2*m/15`, nonzero for positive `m`.
- `B_-1 != B_+1^T`; the residual has 40 nonzeros, with witness
  `(B_-1-B_+1^T)[0,4] = 1121503/714000`.

## C2 — cover-link invertibility: CONFIRMED

The exact `(t, rank(L_t), nnz(L_t))` census is

`(0,4,10), (1,4,8), (2,4,10), (3,4,8), (4,4,10), (5,4,8), (6,4,10), (7,4,8)`.

Thus every link is invertible, and the claimed even/odd `10/8` alternation is
exact.

## C3 — parity theorem and convention attack: CONFIRMED

With `d_ref = R*d00*R^-1`, the exact residual

`R*B_+1*R^-1 - band_-1(Q_dual)`

is the zero `32 x 32` matrix (zero nonzeros). Rebuilding the dual action with
the wrong `d00` convention gives an exact residual with **16 nonzero entries**.
For example, its `(0,4)` entry is `-449983/23665200`. The identity is therefore
specific to the reflected differential and is not convention-slack.

## C4 — symbolic temporal link: REFUTED

The `L_1` and odd-`L_0` parts are correct, but the claimed `q`-independence of
the even part is false for the stated symbolic field. Define

`a_t = q_t*v_t/(q_t^2-1)`.

The eight nonzero entries of `L_1` (local row and column indices) are exactly

| `(row,col)` | entry |
| --- | --- |
| `(0,0)` | `-3*a_1/20` |
| `(0,1)` | `m*a_1/4` |
| `(0,2)` | `3*a_1/20` |
| `(1,2)` | `m*a_1/4` |
| `(2,0)` | `3*a_1/20` |
| `(2,2)` | `-3*a_1/20` |
| `(2,3)` | `m*a_1/4` |
| `(3,0)` | `m*a_1/4` |

Every entry is proportional to `q_1`, and direct substitution gives
`L_1|_(q_1=0) = 0` identically.

Under simultaneous `q_t -> -q_t`, the odd part of `L_0` has the same eight
support positions and exactly the preceding entries with `a_1` replaced by
`a_0`. Its only `m`-dependent entries are `(0,1)`, `(1,2)`, `(2,3)`, and
`(3,0)`, each equal to

`m*q_0*v_0/(4*(q_0^2-1))`.

The even part does have four nonzeros, on the diagonal with signs
`(-,+,-,+)`, but their common magnitude is

`E = (1/v_0 + v_1 - v_0/(q_0^2-1) - v_1/(q_1^2-1))/5`.

This is not `q`-independent:

- `dE/dq_0 = 2*q_0*v_0/(5*(q_0^2-1)^2)`,
- `dE/dq_1 = 2*q_1*v_1/(5*(q_1^2-1)^2)`.

Even adding the unstated unit-circle constraints `q_t^2+v_t^2=1` only changes
this to `E = (v_1 + 1/v_1 + 2/v_0)/5`, which contains `1/v_1` and still does
not match the claimed dependence on `v_0, v_1, 1/v_0` only. Hence C4 as a
whole is refuted, while its support, zero-link, odd-part, and mass-location
subclaims survive.

## C5 — slice-determinant pole locus: CONFIRMED

The period-four equalities are exact: `det(D_t)=det(D_(t+4))` for
`t=0,1,2,3`. The four distinct determinants are

```text
det(D_0)=det(D_4)
 = (548228489361365475*m^4
    +304962944720394182*m^2
    +38591511157183400)
   /421311062016000000

det(D_1)=det(D_5)
 = 334383108821
   *(435662650*m^2+157328829)
   *(3310682425*m^2+1188217638)
   /373347535208819834880000000000

det(D_2)=det(D_6)
 = (4101075725308835135000000*m^4
    +2427936620019229248777675*m^2
    +340901205565367100881637)
   /3014584726383820800000000

det(D_3)=det(D_7)
 = 202214717
   *(3900310*m^2+1377693)
   *(14876225*m^2+5457051)
   /9798663030374400000000
```

Each is degree four in `m`, contains only `m^4,m^2,1`, and every displayed
coefficient and denominator is strictly positive. The two asserted positive
quadratic-product factorizations are precisely the `t=1` and `t=3` cases.

The constant terms, checked independently rather than inferred from positive
`m`, are

```text
t=0: 14842888906609/162042716160000
t=1: 111812063464796728010041/667810609930240000000000
t=2: 1023727344040141444089/9052806986137600000000
t=3: 29809387201343374881/192130647654400000000
```

All are strictly positive. Therefore every `det(D_t)>0` for every real `m`,
including `m=0`; there is no real slice pole.

## C6 — antiperiodic quotient: CONFIRMED

The exact quotient band table is

`{0: 40, 1: 36, 2: 16, 3: 36}`.

The four quotient bonds have exact `(rank,nnz)` values
`(4,10), (4,8), (4,10), (4,8)` for bonds `t=0,1,2,3`, respectively.

## C7 — queued twist certificate: CONFIRMED

The fresh measurement gives exact negation:

`Q_quotient[rows slice 0, cols slice 3] = -Q_cover[rows slice 4, cols slice 3]`.

They are not equal. Their eight common nonzero positions are
`(0,0),(0,1),(0,2),(1,2),(2,0),(2,2),(2,3),(3,0)`, and the quotient/cover
entrywise ratio is exactly `-1` at every one. This is the anticipated
antiperiodic seam sign.

## C8 — minimal-frame seam sanity: CONFIRMED

At the landed field `g`, the full exact residual

`R*Q_min[g]*R^-1 - Q_dual[g]`

is the zero `32 x 32` matrix (zero nonzero entries). The b183 seam identity
therefore survives the minimal-frame projection exactly.

## Overall verdict: REFUTED (localized to C4)

Seven checks are confirmed in full: C1, C2, C3, C5, C6, C7, and C8. C4 is
refuted as stated because its four-entry even part retains generic even
`q_0,q_1` dependence. The additional unit-circle specialization does not
fully rescue the wording: it removes `q` but introduces `1/v_1`, omitted from
the claimed volume dependence. No other discrepancy was found.

## Ten-line summary

1. C1 CONFIRMED: the cover band counts are exactly `80,72,16,16,72` on `dt=0,1,2,6,7`, and all three proposed band relations fail.
2. C2 CONFIRMED: all eight links have rank four with exact `10/8` even/odd nonzero alternation.
3. C3 CONFIRMED: the reflected-differential parity residual is zero, while the wrong-`d00` residual has 16 nonzeros.
4. C4 REFUTED: `L_1`, its zero at `q_1=0`, the odd support, and the four mass entries are exact, but the even part generically depends on `q_0,q_1`.
5. C5 CONFIRMED: there are four period-four degree-four even determinants with positive `m^4,m^2,1` coefficients.
6. The four C5 constant terms are strictly positive, proving every slice determinant remains positive at `m=0` and for all real `m`.
7. C6 CONFIRMED: the quotient bands are exactly `{0:40,1:36,2:16,3:36}`, with bond census `10/8/10/8` and rank four throughout.
8. C7 CONFIRMED: the quotient seam is the exact negative of cover link `3->4`, with ratio `-1` on all eight supported entries.
9. C8 CONFIRMED: the full minimal-frame b183 seam residual is the zero `32 x 32` matrix.
10. OVERALL REFUTED: one precise symbolic-dependence clause in C4 fails; every other supervisor claim survives exact adversarial reconstruction.
