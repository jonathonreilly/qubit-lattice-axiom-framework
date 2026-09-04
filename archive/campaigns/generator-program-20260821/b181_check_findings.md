# Block 181 adversarial findings — common-differential section solve

All decisions below use exact SymPy integer/rational/symbolic arithmetic. No
floating-point value is used in any rank, equality, sign, definiteness,
spectrum, or conjugacy decision. Shift matrices and quotient shifts were
rebuilt independently from the public Block 128/105 APIs.

## C1 — cover translation orbit and naive average

**Verdict: CONFIRMED.** S1 and S2 survive the independent convention check.

- For origins ordered as `(0,0),(0,1),(1,0),(1,1)`, all four cover
  differentials are `32 x 32`, have exact ranks `(16,16,16,16)`, and have
  exact square zero.
- My shift convention is
  `S_(dt,dx)[cover_index(t+dt,x+dx),cover_index(t,x)] = 1`. Both generators
  are genuine permutation matrices (`S.T*S=I`, one unit entry in each row and
  column). `Ux` has exact order 4 and `Ut` exact order 8; in particular
  `Ux^4=I`, `Ut^8=I`, and `Ut^4 != I`.
- Entrywise and matrixwise conjugacy agree. If
  `p_o(cover_index(t,x))=cover_index(t-dt,x-dx)`, then
  `d_o[i,j]=d00[p_o(i),p_o(j)]`. Twelve independently selected entries per
  nonzero origin all matched. Nonzero seam-sensitive samples include
  `d_(0,1)[4,0]=d00[7,3]=-4*i/5`,
  `d_(1,0)[1,0]=d00[29,28]=3*i/5`, and
  `d_(1,1)[8,4]=d00[7,3]=-4*i/5`.
- The full residual nonzero-entry counts for
  `d_o-S_o*d00*S_o^-1` are `(0,0,0,0)`. Thus the result is not an accidental
  match from comparing only ranks or from using the inverse convention.
- The cocycle closes exactly:
  `S_(1,1)=Ut*Ux=Ux*Ut`; both cocycle residuals and `[Ut,Ux]` have zero
  nonzero entries.
- S3 also closes. The independently assembled graph matrix
  `s=vstack(I,Ux,Ut,Ut*Ux)` has shape `128 x 32` and exact rank 32. With
  `D=diag(d00,d01,d10,d11)`, the residual `D*s-s*d00` has `(nnz,rank)=(0,0)`;
  the four component intertwiner residual counts are `(0,0,0,0)`. Hence the
  graph range is exactly `D`-invariant.
- For `d_avg=(d00+d01+d10+d11)/4`, the exact ranks are
  `rank(d_avg)=32` and `rank(d_avg^2)=32`. Moreover
  `det(d_avg^2)=(3/10)^64`, so S2's full-rank claim has an exact nonzero
  determinant certificate.

The adversarial convention attack therefore fails: the stated plain-shift
orbit is the actual entry-level orbit, while averaging representatives
destroys nilpotence maximally.

## C2 — twisted quotient descent and wrap-sign attacks

**Verdict: CONFIRMED.** S4 is exact, and the exhaustive wrap-sign test shows
that the required twist is temporal only.

I independently built every `16 x 16` quotient shift by moving a source
coordinate and multiplying by the chosen wrap sign once per boundary crossing.
For origins `(0,0),(0,1),(1,0),(1,1)`, the residual data for
`dbar_o-Sbar_o*dbar_00*Sbar_o^-1` are:

| time wrap | space wrap | residual nnz by origin | residual ranks by origin |
|---:|---:|---|---|
| `-1` | `+1` | `(0,0,0,0)` | `(0,0,0,0)` |
| `+1` | `+1` | `(0,0,4,4)` | `(0,0,4,4)` |
| `-1` | `-1` | `(0,4,0,4)` | `(0,4,0,4)` |
| `+1` | `-1` | `(0,4,4,8)` | `(0,4,4,6)` |

Thus the periodic-time attack gives exactly four nonzero entries for the unit
temporal conjugacy (and also four at combined origin `(1,1)`). Making space
antiperiodic instead creates four-entry spatial residuals and does not repair a
periodic temporal wrap. The unique sign pair that closes the whole orbit is
`(time,space)=(-1,+1)`.

The antiperiodic time generator has exact order 8 with `Tap^4=-I` and
`Tap^8=I`; the periodic time generator has order 4. The periodic space
generator has order 4, while the deliberately wrong antiperiodic space
generator has order 8. This independently checks the seam convention rather
than inheriting it from `antiperiodic_quotient`.

All four quotient differentials have exact rank 8 and exact square zero on
dimension 16. For each origin, independently computed image and kernel bases
both have dimension 8 and their concatenation still has rank 8. Hence
`im(dbar_o)=ker(dbar_o)` exactly: the four quotient complexes are acyclic.

## C3 — section Hodge, positivity, and the correctly scoped curvature claim

**Verdict: CONFIRMED-WITH-CORRECTION.** The exact S5 matrix claims hold, and
the requested spectral test establishes non-flatness only under orthogonal
(therefore shift-group) equivalence, not under arbitrary congruence.

With `H_s=(1/4) sum_o S_o.T*H*S_o`, I obtain:

- `H_s.T=H_s` exactly;
- all 32 exact leading principal minors are strictly positive (no numerical
  eigenvalue test was used), so Sylvester's criterion proves positive
  definiteness;
- `nnz(H_s-H)=96` and `nnz(H_s-H_flat)=96`;
- rebuilding the flat reference from `cover_embedding` and
  `shear_hodge(0,1)` gives exactly `H_flat=I_32`;
- the first leading minor is `403993/380800`; the 32nd is the positive exact
  determinant represented below by `product(e_r/a_r)`.

Here is the exact eigenvalue-multiset certificate. Define
`P(a,b,c,d,e)=a*z^4-b*z^3+c*z^2-d*z+e`. SymPy's exact rational factorization
gives

`chi_Hs(z) = product_r P(a_r,b_r,c_r,d_r,e_r)/a_r`,

with each of the eight quartic factors occurring once:

| r | `a_r` | `b_r` | `c_r` | `d_r` | `e_r` |
|---:|---:|---:|---:|---:|---:|
|1|585180463278587904000000|2487167805394675630080000|3938379097216191970406400|2753360772352345988034960|716924930433435257555957|
|2|585180463278587904000000|2487167805394675630080000|3938379097216191970406400|2753360772352345988034960|717156814349137615019957|
|3|518796360417961524068352000|2217015870119768387380838400|3526977366277298684908093440|2475305705241347085590015232|646748774398979904878032151|
|4|2593981802089807620341760000|11085079350598841936904192000|17634886831386493424540467200|12376528526206735427950076160|3232317259296127698257566819|
|5|16543251288838058803200000000|70264352929400969084928000000|111051250338397498712017920000|77391165989081473749591292800|20058665410646090301040352407|
|6|16543251288838058803200000000|70264352929400969084928000000|111051250338397498712017920000|77391165989081473749591292800|20069104695141994123568867407|
|7|19276527266779882878664704000000|82319215631704462209979514880000|130662556308076440897774004838400|91340946171042247130481020407200|23718325770525413420005202503351|
|8|19276527266779882878664704000000|82319215631704462209979514880000|130662556308076440897774004838400|91340946171042247130481020407200|23733293658901445903825624747101|

Thus the exact spectrum is the multiset union of the roots of these eight
quartics. In contrast,
`chi_Hflat(z)=(z-1)^32`. The polynomials already differ at the trace:
`tr(H_s)=927831123589/27222868400 = 32 + 56699334789/27222868400`, whereas
`tr(H_flat)=32`.

Consequently no orthogonal matrix can carry `H_s` to the flat reference, and
in particular no permutation/shift-group element can do so. This supports
“non-flat relative to the fixed flat reference under orthogonal frame
changes.” It does **not** support non-flatness under general congruence:
Sylvester's law makes every real positive-definite form congruent to every
other one. Nor is an entry count by itself a curvature invariant. Any
unqualified “genuinely curved under all frame changes” wording requires this
correction.

## C4 — section-completion covariance and the landed-action scope

**Verdict: CONFIRMED-WITH-CORRECTION.** S6's section identities are exact and
structural, and the actual two landed actions are not isospectral. The prompt's
phrase “four LANDED physical actions (`build_completions()`)” is false for the
bounded runner: that public function returns exactly two, at `(1,0)` and
`(1,1)`.

For every one of the four section origins, the `(nnz,rank)` residuals are
`((0,0),(0,0),(0,0),(0,0))` both on the 32-dimensional cover and after the
16-dimensional antiperiodic quotient with the twisted shifts. This is not a
fortuitous numerical cancellation. With real orthogonal `S` and
`d_k=S*d_0*S.T`,

`Q(S*H*S.T,S*d*S.T) = S*Q(H,d)*S.T`,

because `(S*d*S.T).H=S*d.H*S.T` and `S.T*S=I`. The quotient result follows
with the independently built antiperiodic temporal representation.

The fixed-H contrast needs precise scoping. Relative to the auxiliary `(0,0)`
fixed-H action, cover residual `(nnz,rank)` values are
`((0,0),(256,32),(256,32),(184,32))`; on the quotient they are
`((0,0),(128,16),(128,16),(92,16))`. But the **actual landed pair** is
`(1,0)` versus its spatial translate `(1,1)`, and that residual is exactly
`(256,32)` on the cover (`(128,16)` on the quotient). Thus S6's “256” is
confirmed for the comparison the b128 runner actually lands; it would be
wrong if read as a uniform count for all nonbase origins.

I computed the complete exact degree-16 characteristic polynomials. The two
returned physical actions are not isospectral. They share
the `z^15` coefficient
`-927831123589/190560078800`, but already differ at `z^14`:

| landed origin | exact coefficient of `z^14` | exact constant term |
|---|---:|---:|
| `(1,0)` | `1195620534151694060907411/62608868331486568000000` | `1423734729988975134848782052839707449596193739541851415322710835951753577442866343837/865286896898517871101969556449367884610786432961740800000000000000000000000000000000` |
| `(1,1)` | `8650195819888697214240517/435757723587146513280000` | `7953009607920747471545650105238713815593970342119529377003323269333649139308624711313/2723257770997884904179990099274976608142862937051103232000000000000000000000000000000` |

The full exact monic coefficient tuples (17 coefficients each, with no
floating reconstruction) are emitted by `b181_exact_check.py c4`. SymPy also
leaves each degree-16 polynomial irreducible over the rationals. As an
auxiliary extension—not a claim about what `build_completions()` returns—I
formed the fixed-H actions at all four origins. Their exact `z^14`
coefficients are:

| auxiliary origin | exact coefficient of `z^14` |
|---|---:|
| `(0,0)` | `871148191866791809761041/43575772358714651328000` |
| `(0,1)` | `5084211688537038000338141/265705929016552752000000` |
| `(1,0)` | `1195620534151694060907411/62608868331486568000000` |
| `(1,1)` | `8650195819888697214240517/435757723587146513280000` |

All four auxiliary polynomials are pairwise distinct. Therefore the landed
b128 pair is inequivalent even under arbitrary similarity, strengthening its
matrix-inequality certificate rather than weakening it.

The physical content of the section identity is limited: it says that when
both the differential **and** pairing are transported, the resulting action is
the same object in relabelled coordinates. It does not derive that transported
pairing from the landed fixed-H prescription, make the landed actions
equivalent, produce a shift-invariant action, or complete the common-
differential/OS construction. Relative to the extrapolated four-chart fixed-H
family it is a fifth covariant base object; relative to the runner's actual two
returned completions it is a new third object. Its quotient characteristic
polynomial differs from both landed polynomials.

## C5 — commutator rank, covariance, and the “curvature residual” label

**Verdict: CONFIRMED-WITH-CORRECTION.** S7's ranks and covariance statement are
exact, but the commutator residual itself cannot honestly be identified as
curvature: the same full rank occurs for the exactly flat Hodge.

For section origins `(0,0),(0,1),(1,0),(1,1)`, the physical-action spatial
commutators all have `(nnz,rank)=(160,16)`. After `grassmann_form` and the
doubled periodic spatial shift, all four have `(nnz,rank)=(320,32)`. An
independent recomputation of the landed `(1,0)` control gives
`(nnz,rank)=(304,32)`, agreeing with its stored `commutator_rank=32`.

The exact conjugacy from C4 makes all four section physical-action
characteristic-polynomial coefficient tuples identical. Hence the section
orbit has shift-independent spectrum. Nevertheless, every representative has
a full-rank commutator and is not spatial-shift invariant. Covariance and
invariance are genuinely different here.

The causal label “the residual is curvature” fails an exact control. Replacing
the pairing by the rebuilt flat reference `H_flat=I_32` while retaining `d00`
still gives a Grassmann/spatial-shift commutator of `(nnz,rank)=(96,32)`.
Therefore rank 32 is already generated on the flat reference by the chartwise
staggered differential. Separately, `H_s` itself has `(nnz,rank)=(96,32)`
against both the cover spatial and temporal shifts, so its nonuniform pairing
also contributes to noninvariance.

The honest statement is: the commutator certifies translation noninvariance of
the chosen section representative, while the orbit is translation covariant
and isospectral. C3 independently certifies that `H_s` is not orthogonally
equivalent to the designated flat reference. The commutator rank is not by
itself a curvature invariant or a curvature-only residual. If “covariance, not
invariance” is offered merely as a reframing, it is correct; if offered as a
repair of the missing shift-invariant global action or momentum decomposition,
it hides the original defect and is not a solve.

## C6 — quotient commutant and Jordan type

**Verdict: CONFIRMED.** S8 follows from an independent exact Sylvester-
Kronecker calculation and the direct nilpotent rank sequence.

For the antiperiodic quotient `dbar_00`, the exact data are
`shape=(16,16)`, `rank(d)=8`, `rank(d^2)=0`, `d^2=0`, nullities `(8,16)`,
and `chi_d(z)=z^16`. Multiplying by `-i` first produces an exactly rational
matrix with the same commutant. For column vectorization I built

`L = d_real.T kron I_16 - I_16 kron d_real`,

so `L vec(X)=0` is exactly `X*d_real-d_real*X=0`. The `256 x 256` Sylvester
matrix has exact rank 128 and nullity 128. Therefore the commutant dimension is
128.

Because `d^2=0`, every Jordan block has size at most 2. Each `J_2(0)` block
contributes one to rank, so rank 8 gives exactly eight `J_2(0)` blocks. The
remaining number of `J_1(0)` blocks is `16-2*8=0`. Thus the asserted Jordan
type is exactly `J_2(0)^8`, with no `J_1` summand.

## Overall verdict

**CONFIRMED-WITH-CORRECTION.** The common-differential section is an exact
32-dimensional invariant graph inside the four-chart direct sum, and its
paired-Hodge completion is an exact cover/antiperiodic-quotient covariant
orbit. S1--S4, the algebraic core of S5--S7, and S8 all survive independent
exact arithmetic. The construction does **not** refute the landed b128
nonextension result: the runner lands only two fixed-H actions, those two are
not isospectral, and transporting `H` along with `d` defines a new covariant
object rather than proving the fixed-H objects equivalent or producing a
translation-invariant action.

Three corrections are mandatory. First, the exact Hodge spectrum proves
non-flatness only under orthogonal/shift equivalence, not arbitrary congruence.
Second, `build_completions()` returns two landed actions, not four; “fifth” is
valid only relative to an auxiliary all-four extrapolation. Third, the rank-32
translation residual is not itself curvature: an exact flat-Hodge control also
has rank 32. The strongest defensible outcome is therefore a chart-covariant,
isospectral section orbit with no translation invariance and no completed
common curved OS action.

## Ten-line summary

1. All four cover differentials are nilpotent rank 16 and exact plain-shift conjugates; `Ux`/`Ut` have orders 4/8 and commute.
2. The graph section has rank 32 and satisfies `D*s=s*d00` entry-exactly, while `d_avg^2` has rank 32 and determinant `(3/10)^64`.
3. Quotient descent closes only for temporal antiperiodicity and spatial periodicity; wrong temporal or spatial signs leave exact 4-entry unit-shift residuals.
4. All quotient differentials are nilpotent rank 8 with `im=ker`, hence the 16-dimensional complexes are acyclic.
5. `H_s` is symmetric positive definite with 32 positive leading minors and differs from both raw and flat Hodge matrices at 96 entries.
6. `chi_Hs` is the exact eight-quartic product recorded in C3, whereas `chi_Hflat=(z-1)^32`; only orthogonal/shift non-flatness follows.
7. Section completions are exactly conjugate on cover and quotient by orthogonality, but this is a structural transported-pairing identity with limited physical content.
8. `build_completions()` lands two actions, not four; their exact characteristic polynomials differ, and the actual cover-pair conjugacy residual has 256 nonzero entries.
9. Section and landed Grassmann shift commutators have rank 32, but so does the flat-Hodge control, refuting the label “the residual is curvature.”
10. The quotient commutant has dimension 128, and `rank d=8`, `d^2=0` on dimension 16 gives exactly eight `J_2(0)` blocks and no `J_1` blocks.
