# Block 186 adversarial check: section-frame port and balanced-inertia wall

## Audit boundary and exact method

I read only `scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py` and rebuilt the Block 186 objects from its public APIs `chart_differential_cover`, `cover_embedding`, `cover_index`, `block105.shear_hodge`, and `block105.overlap_field`.  All decisions below use exact SymPy integers/rationals.  Matrix support counts distinguish **ordered matrix entries** from **unordered support-graph edges**, a distinction that matters in C1(iv).

## C1 — port structural theorems

**Verdict: CONFIRMED-WITH-CORRECTION.**

1. `d00` has exactly 32 nonzero ordered entries.  Every one lies within a single even-anchor 2-by-2 cell `(2 floor(t/2),2 floor(x/2))`.  The two directed 4-by-4 strips `t=3 -> 4` and `t=4 -> 3` contain 0 nonzero entries (32 tested entries are exactly zero).
2. The all-flat overlap construction satisfies `H_flat-I_32=0` entrywise (0 residual entries), exactly.
3. With `H=I_32`, `m=9/20`, the stated `D`, and the undressed `P0`, the full 16-by-16 reflected Gram is the zero matrix: rank 0 and 0 nonzero entries.
4. C1(iv) is **refuted as written**.  For the no-glue, period-4 curved field followed by the `x`-minimal average, curved `Q` has **144 ordered inter-cell nonzero entries**, not 96, and its symmetrized support graph has **72 unordered inter-cell edges**, not 96.  Curved `H_min` itself has 48 ordered entries (24 unordered edges) in that support; the other **96 ordered entries** (48 unordered edges) are created by `H D + D^H H`.  Thus 96 is the ordered support increment of `Q` beyond `H`, not the inter-cell entry count of `Q`.  Flat `H=I` has 0 inter-cell edges, so all 72 curved edges are H-induced in the causal sense, but “H-borne” must not be read as “already in the support of H.”

## C2 — flat-seam diagnosis

**Verdict: CONFIRMED.**

For the glued curved/reflected construction with `B_seam=I_4`, the undirected support graph of `Q_glued` has exactly two connected components, each of size 16.  Their time sets are exactly `{0,1,2,3}` and `{4,5,6,7}`.  The site reflection `theta(t)=(-1-t) mod 8` maps each complete component onto the other.  There are 0 directed cross-half nonzero entries.  The dressed 16-by-16 Gram has rank 0 and 0 nonzero entries.

## C3 — self-dual seam space

**Verdict: CONFIRMED-WITH-CORRECTION.**

Let the symmetric upper-triangular coordinates be

`B=[[b0,b1,b2,b3],[b1,b4,b5,b6],[b2,b5,b7,b8],[b3,b6,b8,b9]]`.

For `J=P4 Xi`, the exact residual is

```text
[[ b0-b7, b1+b8,       0, b3+b5],
 [ b1+b8, b4-b9, b3+b5,       0],
 [      0, b3+b5, -b0+b7, b1+b8],
 [ b3+b5,      0, b1+b8, -b4+b9]].
```

The constraint matrix has rank 4 in the 10-dimensional symmetric space, hence the fixed space has dimension 6.  Its off-diagonal-only part has dimension 4.  The diagonal-only part is exactly `diag(a,b,a,b)`.  Equivalently, the independent off-diagonal coordinates may be taken as `b2,b5,b6,b8`, with `b3=-b5` and `b1=-b8`.

For `S(q,v)=shear_hodge(q,v)`, the nonzero residual entries are

```text
R00 =  q^2 v/(q^2-1),       R03=R12=R21=R30 = q v/(q^2-1),
R11 = (-q^2-v^2+1)/(v(q^2-1)),
R22 = -q^2 v/(q^2-1),       R33 = (q^2+v^2-1)/(v(q^2-1)).
```

This verifies the requested `q^2+v^2-1` factor.  On the public API's algebraic domain `v != 0`, `q^2 != 1`, self-duality forces `q=0` and then `v^2=1`.  Therefore both `(q,v)=(0,1)` and `(0,-1)` are exact self-dual members (`I_4` and `-I_4`).  The supervisor's “only flat” statement is true only after adding the conventional but unstated positive-volume restriction `v>0`.

## C4 — `E02` seam construction at `s=1/5`

**Verdict: CONFIRMED.**

With `B_seam=I_4+(E02+E20)/5`, every entry of `Q` is real, and both identities hold entrywise:

```text
Px H_g Px = H_g,
Px Q Px = Q^T.
```

There are exactly 48 ordered cross-half nonzero entries: 24 from the first half to the second and 24 in the reverse direction.  The dressed Gram is exactly Hermitian.  The `P0`-undressed Gram is not Hermitian: its anti-Hermitian defect has rank 16 and 80 nonzero entries.  One exact defect witness is

```text
(K0-K0^H)[0,1]
= -33312574766151728810271091272476210636302272000
  /1284055476497769257284814388230298847972127669509 != 0.
```

## C5 — balanced-inertia wall

**Verdict: CONFIRMED-WITH-CORRECTION.**

I used exact symmetric congruence elimination, not characteristic-polynomial Descartes counting: a nonzero diagonal pivot splits off by a rational Schur complement; a zero remainder contributes its exact nullity.  The following results are exact:

| seam/limit | rank | inertia `(+,−,0)` |
|---|---:|---:|
| `I+(E02+E20)/5` | 12 | `(6,6,4)` |
| `I+(E13+E31)/5` | 12 | `(6,6,4)` |
| `I+((E12+E21)-(E03+E30))/5` (`b5`) | 6 | `(3,3,10)` |
| `I+((E23+E32)-(E01+E10))/5` (`b8`) | 0 | `(0,0,16)`; the Gram is exactly zero |
| equal-coefficient generic mixture defined below | 12 | `(6,6,4)` |
| distinct-coefficient generic mixture defined below | 12 | `(6,6,4)` |
| pure geometry, `G=H_g^-1`, `E02` seam | 8 | `(4,4,8)` |

The exact congruence pivot-sign certificates for three independently requested points are:

```text
E02:          -+-+-+-+-+-+ ; trailing zero block dimension 4
b5:           +--++-       ; trailing zero block dimension 10
pure geometry -+-+-+-+     ; trailing zero block dimension 8
```

At fixed `E02`, `s=1/5`, all five masses give rank 12 and inertia `(6,6,4)`:

```text
m = 1/3, 9/20, 1, 2, 10.
```

The correction is reproducibility scope.  “Generic mixed seam” is not a matrix definition.  To avoid smuggling in supervisor scratch data, I tested two explicit self-dual generic representatives, both with the reported result:

```text
Bgen1 = I + [F02 + F13 + (F12-F03) + (F23-F01)]/5,
Bgen2 = I + [F02 + 2 F13 + 3(F12-F03) + 4(F23-F01)]/5,
Fij   = Eij + Eji.
```

This confirms two generic points, not an undefined universal “generic” assertion.

## C6 — mechanism-exclusion theorem

**Verdict: CONFIRMED.**

For the `E02`, `s=1/5`, `m=9/20` dressed Gram, the exact characteristic polynomial has six nonzero odd-power coefficients, at powers

```text
x^5, x^7, x^9, x^11, x^13, x^15,
```

with coefficient signs `(-,+,+,-,+,-)` in that order.  In particular the `x^15` coefficient is `-tr(K)` and is nonzero (its exact value is given in C7).  Thus the spectrum is not invariant under `lambda -> -lambda`, so no invertible linear similarity can send `K` to `-K`.

The stronger anti-commutant statement also closes exactly.  With `p(x)=charpoly(K)`,

```text
gcd(p(x),p(-x)) = x^4.
```

Hence no nonzero eigenvalue is paired with its negative.  Since Hermitian `K` is diagonalizable, `SK+KS=0` maps the `lambda` eigenspace into the `-lambda` eigenspace.  It must therefore annihilate every nonzero eigenspace and can act only from `ker K` to `ker K`.  Since `nullity(K)=4`, the anti-commutant has exact dimension `4^2=16`; every such `S` is kernel-supported and none is invertible.  Balanced inertia here is therefore not produced by a linear anticommuting symmetry.

## C7 — fresh escape-route tests

**Verdict: CONFIRMED (NO ESCAPE FOUND).**

### C7(i): trace sweep

The trace is **not** identically zero.  Every requested finite-mass value is strictly positive and exactly:

```text
tr K(1/3) =
6400042633297782986875979114566162165938729869072222875747016244932955909213309358385008491541456041736465445860468186827158356445568750955696686741052281557768802498190346784780723617564359856113222547600
/18229579560405248648770289297052202588405843481778732333853293455627450543543529188304504352280458544613757337042261797995258869886739235143955498379222392668792217693159104808472358312524650355290790246835959

tr K(9/20) =
1325050676382935682922367377477599577745794262148917951162503278977525297622870791242866833705369115128330956943458458258005401952376158492943423929459239722488935716886344078135190378509176862992
/3218748283328129756622293961301210624237075212716203020739811740572109643823362085949812051655332792994918710659540011478810491544760272827350849275698690299384853993387376708185825413453778966688757

tr K(1) =
7289565427027461853449408470657385746914193680200548442115953826134281413539498646478217304458270349493919842221123896031679896397836700835156878887109685257126847003878091189193420548372400
/18643294646751297174010963575136193203023844911348684135851261318592925787525294013681852955424655936522531785904022866105195382171002374713711232662501103536274012078484727438620511913584755447

tr K(2) =
10950659865827834274882658200896232341338022350848739446212054504867247448731058252620679584449760800529806632770951387967571609589387637833120919597426361556740397674957934154631453059072390675
/52863469981401171764509898553836652617679451316642298361867627364724623665550101253037729971388712227418075115251450081498712374820806774591847452729067104320808602764700843326661272541550716098682

tr K(10) =
119031143659412758653187352733916499249449097298228528837550337725026938758705489554865604509230813456997989597922586224637165155457460850985686210791144644521269831659510760597245384187791494560615072962517129804500
/3353989140385754377997565580065459123893062844089970549536798703900739614927936020202138888992491069444066550469969870215357829205167676446143893059523542009182859094235602872808479733256011823771708479810080899541398551.
```

### C7(ii): antilinear candidates

Here `K` is real, so `S conjugate(K) S^-1=-K` reduces to the already excluded linear similarity.  Direct candidate residuals `S conjugate(K) S^-1+K` are nevertheless nonzero:

| candidate `S` | residual rank | residual nonzero entries |
|---|---:|---:|
| `xpar` | 16 | 80 |
| `tpar` | 16 | 80 |
| `staggered` | 16 | 64 |
| `deg` | 16 | 64 |
| half reflection `R:t->3-t` | not needed | 208 |
| `R xpar` | not needed | 208 |
| `R tpar` | not needed | 200 |
| `R staggered` | not needed | 200 |
| `R deg` | not needed | 200 |

I interpreted `deg` as local form-degree parity `(-1)^((t mod 2)+(x mod 2))`; on this section it is exactly the staggered diagonal.  A different intended `deg` requires an explicit definition.

### C7(iii): two-sided `Gamma0` dressing

The stated alternative is exactly `K2=xpar K xpar`.  It is Hermitian, differs from `K`, has rank 12, and exact inertia `(6,6,4)`.  Exact congruence gives the same `-+-+-+-+-+-+` nonzero pivot-sign string and a 4-dimensional zero tail.

### C7(iv): positivity alert

No tested C7(ii) candidate supplies the required antilinear negative similarity, and `K2` is indefinite rather than positive or positive-semidefinite.  **No C7 variant breaks the wall.**

## C8 — scope honesty

**Verdict: CONFIRMED.**

The computed wall is explicitly per pairing, per section, and per `x`-minimal frame.  The `b8` zero, the balanced inertia patterns, and the linear mechanism exclusion concern only the Block 186 Gram constructions.  They neither test nor contradict b107-carrier positivity as described in the question, and they are not a no-go theorem for other pairings.

Pairing/frame variants still untested beyond C7 include:

- independent left/right dressings not related by an invertible congruence;
- other section embeddings or choices of `Lambda_+`, including non-time-half sections;
- other reflection maps, site permutations, and non-diagonal dressing matrices;
- complex frames where the antilinear problem does not collapse to a real linear similarity;
- sesquilinear pairings constructed directly from the b107 carrier rather than from `(G Px)^H`;
- non-`x`-minimal frames and other allowed frame averages;
- other seam strengths/shapes coupled to a changed pairing (the present seam sweep alone is not a pairing sweep).

## Overall verdict

**CONFIRMED-WITH-CORRECTIONS.**  The balanced-inertia wall and its linear-mechanism exclusion survive every fully specified exact check.  C1(iv) is numerically false as stated: `Q` has 144 ordered inter-cell entries and 72 unordered edges; 96 counts only the ordered increment beyond `H` support.  C3 needs `v>0` to exclude the exact self-dual point `(0,-1)`, and C5's “generic mixed seam” needs an explicit matrix before it is uniquely reproducible.  None of these corrections produces a positive or positive-semidefinite Gram in the tested pairing/frame.

## Ten-line summary

1. `d00` has 32 nonzeros, all intra-cell, and no `3<->4` entry.
2. Flat overlap gives `I_32`, and the undressed flat-half Gram is exactly zero.
3. Curved no-glue `Q` has 144 ordered inter-cell entries and 72 unordered edges; the claimed 96 is only the ordered support increment beyond `H`.
4. Flat seam gives exactly the two time halves as components and a zero dressed Gram.
5. The symmetric seam fixed space is 6-dimensional, with 4 off-diagonal directions.
6. Shear self-duality gives `(0,±1)` algebraically; only `v>0` selects flat `(0,1)`.
7. The `E02` seam connects the halves with 48 ordered entries and makes only the dressed Gram Hermitian.
8. All specified inertias are balanced; `b8` is zero and pure geometry is `(4,4,8)`.
9. Six odd charpoly terms and `gcd(p(x),p(-x))=x^4` exclude a non-kernel linear anti-symmetry.
10. All traces are nonzero, the tested antilinear candidates fail, and `K2` remains `(6,6,4)`.
