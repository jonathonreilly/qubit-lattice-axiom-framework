# B_Z: geometry of the first exterior read

Codex; research base `b0f28659cacceb6a7a5439c8b485c965022b480a`.
FINISH row 517. Research text, not an audit. This grants no status.
This lane writes only this file. No computer-assisted proof is used.

**Result:** stop (c) at BZ-TRACE after the three routes below.
The quoted CMP 119 construction has a bare graded edge.
Its identification with the actual B_Z entry remains open.

## 1. Scope and sources

`library/prior/bz-geom.md` is absent at this commit.
The registry lists PI-ADMIT under `pi-admit`.
Row 517 authorizes this narrower continuation of its C0-ETA supplier.
The existing proofs in `c0-sup.md` and `out-pi.md` are inputs here.
Their failed routes are not repeated as new work.
The U22/U24 entries in layer-pkg.md (1220–1222) and adm-pl.md (763–765)
also retain this localized certificate as an input. They do not close it.

Write **I** for the complete account and **SA** for the outline,
both at `31a47c543775`.
Write **N** for `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
The three requested scratch files already existed. They were not downloaded again.
Source reads are bounded excerpts, located through the supplied indices and source anchors.
The specified Balaban paper folder is absent. No paper was downloaded.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every definition and port below.
Credit Tadeusz Balaban for the localization, graded boundary and local-gauge methods.
References to his papers below mean quotations in the account, unless stated otherwise.

The target is the actual localized pair on its prescribed parameter domain.
A different extension, a smaller domain, or a replacement determining set would not prove it.
The operator is PI's compressed whole-action Hessian with its touching field bonds.

## 2. What can already be used

| Input | Source | What is available |
|---|---|---|
| PI reads only the first exterior spacing | `c0-sup.md`, Proposition 3.1 and Lemma 3.2 | Includes local matrices and reference norms on PI's tower class. |
| Bare boundary filling | `c0-sup.md`, Proposition 4.1 | Conditional on a bare first gap and the actual pair bounds. |
| Gauge per real reference is sufficient | `gates/c0-sup-check.md`, finding 6 | A gauge need not be fixed across different real references. |
| Localized layer at B_Z | I 131568, 131725–131746 | An input, including its ambient domain and layer bound. |
| Geometry of that localized layer | I 137565–137583 | Outside the geometry of the layer theorem's input spaces; the localized assertion is used with proof incomplete. |
| CMP 119 localization display | I 92517–92533 | Parent blocks survive in the interior; a graded set replaces blocks near the cut. |
| Localization provisos at two other sets | I 94755–94812 | Verified for B^0 and B^C, not stated for B_Z. |
| Raw index-zero tests | I 134745–134826 | Tests and heredity on the specified ambient determining domain. |

Put $X=\Omega_0(\mathfrak B_Z)$ and $X_\eta=\{x:d_\infty(x,X)\le\eta\}$.
Only actual coefficient reads in $X_\eta$ need a boundary certificate.
There is no second exterior collar to supply.
Interior admission and the other layer inputs remain separate premises.

## 3. Route 1: identify the cut from the printed localization

### 3.1 The collar is graded, not uniformly of level j

This distinction matters for finding 15.
The subscript in $\mathbf B_j(Z)$ gives its maximum level.
It does not give the level of every boundary block.

Port the following construction from Sussman and Alpoge, I 32861–32894 and 147407–147427.
Balaban's CMP 119 rule starts with $D_0=Z$.
For $1\le n\le j$, it takes maximal unions of $M_1\ell_n$-cubes with

$$
D_n\subset D_{n-1},\qquad
d_\infty(D_n,D_{n-1}^c)\ge M_1\ell_n,\qquad \ell_n=L^n\eta.
\tag{1}
$$

Its level is $n$ on $D_n\setminus D_{n+1}$.
In particular, its outer rim has level zero.
The account proves its interior inclusion and describes its staircase at I 147765–147805.
That proof is already theirs. It is not a missing lemma.

I 93580–93588 gives the splice for $\mathfrak B^C$ explicitly:
keep the parent partition on $C^{\sim-2}$ and the minimal partition on the remaining rim.
I 92517–92533 quotes the same CMP 119 rule in another application.
Neither display describes a constant-level partition on the rim.

Here is the exact boundary consequence.
It applies to that construction, without identifying it with $\mathfrak B_Z$.

**Lemma 3.1.** Let $C\subset Z$ be the retained core, with
$d_\infty(C,Z^c)\ge h>0$.
Consider a valid splice whose retained parent blocks lie in $C$.
On $Z\setminus C$, use the levels of the partition in (1).
Then its positive-level region satisfies

$$
d_\infty(\Omega_1^{\mathrm{loc}},Z^c)
\ge \min\{h,M_1L\eta\}\quad(j\ge1).
\tag{2}
$$

For $j=0$ the lower bound is $h$.
The assertion includes an empty positive-level region.

**Proof.** A positive-level point in $C$ has distance at least $h$ from $Z^c$.
A positive-level point outside $C$ belongs to $D_1$.
Equation (1) gives its distance at least $M_1L\eta$.
For $j=0$, the partition outside $C$ has only level zero.
Taking the infimum proves the claim. $\square$

Under the two-layer convention, $h=2M_1\ell_j$.
This convention and its units are explicit at I 147765–147805.
Thus positive-level parent blocks cannot reach the outer edge of this splice.
Retain PI's other gaps and suppose the bound in (2) exceeds $2L(r_N+2)\eta$.
A level-one patch then stays inside $Z$, since its radius is $r_NL\eta$.
Every higher-level patch stays inside its preceding region by the retained gaps.
Thus a crossing patch has a bare anchor.
Its anchor lies within $r_N\eta$ of the boundary.
Its patch and one-spacing reads lie within $2(r_N+2)\eta$ of it.
They therefore miss $\Omega_1^{\mathrm{loc}}$.
This proves the boundary-model assertion. Equation (2) does not prove all of (T).

This resolves the proposed inference from CMP 119:
a coarse parent stratum does **not** imply a coarse localized outer edge.
It does not resolve which partition item 10 actually uses.

### 3.2 What the single-stratum proviso would buy

Suppose $Z\subset X_{\mathfrak a}$ and
$d_\infty(\partial Z,X_{\mathfrak a}^c)>\eta$.
Then

$$
Z_\eta\subset X_{\mathfrak a}.
\tag{3}
$$

To prove this, take $z\in Z_\eta\setminus Z$.
A nearest-point segment to $Z$ meets its boundary within distance $\eta$ of $z$.
If $z\notin X_{\mathfrak a}$, this contradicts the displayed boundary distance.
The lattice version uses the corresponding closed geometric unions.
Points already in $Z$ belong to $X_{\mathfrak a}$ by hypothesis.

For a parent tower, $\partial Z\subset\Omega_j^{\mathrm{par}}$ with $j\ge1$
would give this distance from its first gap, if that gap exceeds $\eta$.
For a parent raw stratum, the distance must be supplied separately.
The R-stage level alone does not locate $\partial Z$ in a parent stratum.

The account verifies the CMP 119 provisos for $\mathfrak B^0,\mathfrak B^C$ at I 94780–94812.
It uses the specific separation
$d_k(\Lambda_C^{\sim},C^c)\ge9\check R_k$.
It then places $\partial C$ in the level-$k$ parent stratum.
Those are the two sets of that lemma, with their own component $C$.
The proof does not quantify over every localization domain of an interrupted stage.

**Failure of route 1.** No read source identifies item 10's $Z$ with that $C$,
or gives its counterpart of this separation inequality.
I 131725 cites CMP 122b (2.14); it does not print the localization rule.
I 137565–137583 invokes the exceptional localized theorem rather than proving that identification.
The splice above is a valid candidate construction.
Choosing it would not establish that it is the account's $\mathfrak B_Z$.
Thus (2) is a conditional bare-edge proof, not an actual-entry certificate.

## 4. The single remaining supplier

Call the following statement **BZ-TRACE**.
It concerns the literal entry of I 131725–131746, including later sources and images.
It is a supplier within C0-ETA, not a new registry task.

For each such entry, retain its prescribed parameter and switch domain $\mathcal D$.
For each crossing PI patch, let $E$ be its required bonds in $X_\eta$.
Include the reference-norm reads as well as the coefficient reads.
Then:

1. The actual localized tower has PI's bare first gap at $X$.
   Its required boundary reads $E$ lie in $X_{\mathfrak a}$.
2. Those reads carry the same real reference and twist as the ambient member of item 10.
   This holds at every point of $\mathcal D$ and uses that member's own continuation.
3. One admitted tested cube, or one admitted hull gauge, covers $E$.
   Its gauge is on the entire required trace.
   In the fine-link convention $U_r^u=e^{i\eta A}$, its supplied bounds obey

$$
\eta|A|\le\epsilon_r,\qquad \eta|a|<\epsilon_c
\quad\hbox{on }E,\qquad
\epsilon_r=\tfrac14L^2a_0^*,\quad \epsilon_c=\tfrac14a_1^*.
\tag{4}
$$

The last clause is a quantitative test-transfer requirement.
It must follow from the original radii, not from shrinking $\mathcal D$.
The cube may depend on the geometry.
The unitary gauge may depend on the real reference, as finding 6 permits.

**Conditional conclusion.** BZ-TRACE supplies C0-ETA on precisely PI's boundary reads.
Use the same reference and twist from clause 2 in the gauge from clause 3.
Equation (4) is the reduced boundary certificate.
Clause 1 permits the bare filling of c0-sup.md, Proposition 4.1.
That proposition and its check supply PI's boundary estimates.
All interior and additional consumer premises remain attached.
This uses no second collar and changes no actual coefficient.

## 5. Route 2: build the boundary certificate from the actual tests

This route uses item 10's own families, rather than an ordinary-step corridor.
Its three families are listed at I 131730–131737:
the positive-level cubes, the raw index-zero members, and the gauge member on $Y'$.
The raw family is described at I 134749–134755.
Its cubes have side at most $2ML\eta$.
Its twist clause is the index-zero instance of (3.37).
These are ports from Sussman and Alpoge, not new estimates.

### 5.1 Crossing a grid face is repairable

A patch need not fit in one partition cube.
The account already handles this issue.
I 48263–48271 gives a containing cube for a small box inside a union of aligned cubes.
I 48329–48335 permits that containing cube to slide off the partition.
The relevant printed gauge families allow this.

For a second-cover hull, I 48337–48370 gives

$$
H=\square^4\subset Q\subset
\widehat\Omega_m\setminus\widehat\Omega_{m+2},
\qquad Q\cap\widehat\Omega_{m+1}^c\ne\varnothing.
\tag{5}
$$

I 48479–48518 identifies the printed family containing $Q$.
I 49120–49234 then restricts its single gauge to $H$.
The last result does not join two independently supplied gauges.
Its local version only gives a gauge on $H\cap Y_{\mathrm{loc}}$.

Thus the patch may cross several partition cubes.
It still needs containment in one admitted gauge trace.
The hull theorem assumes the second-cover geometry, including its index at least two.
It does not identify an arbitrary localized boundary patch with such a hull.
At raw points one must use the stated index-zero family instead.

### 5.2 The exact radius transfer

Keep the fine-link normalization $U_r^u=e^{i\eta A}$.
Suppose $E$ lies in one such hull trace.
The ported hull estimate is

$$
\ell_n|A|<\mathfrak a(\square),\qquad
\mathfrak a(\square)=L^2\mathsf c_1BM R_m\alpha_{0,m},
\qquad n\in\{m-1,m,m+1\},
\tag{6}
$$

where $\mathsf c_1=1+c(\beta_0)L(L+1)$ and
$c(\beta_0)=\sup_{t\ge1}3^{-t}t^{\beta_0}$.
These constants and the bound are from I 49131–49144 and 49162–49212.
If the actual twist has its supplied bound $\ell_n|a|<t_n$, then
c0-sup.md (9) gives, on $E$,

$$
\eta|A|<\max_{n\ {\rm met}}L^{-n}\mathfrak a(\square),\qquad
\eta|a|<\max_{n\ {\rm met}}L^{-n}t_n.
\tag{7}
$$

In particular, the first maximum is at most $L^{1-m}\mathfrak a(\square)$.
Matching these two maxima to $\epsilon_r,\epsilon_c$ gives (4).
For an index-zero cube, the two factors are simply one.
The transfer is valid on the original parameter image.
It gives no control at a parameter absent from the supplying space.

No first-difference estimate has to be transported for this bare-boundary use.
Proposition 4.1 derives those estimates after filling unused links.
There is also no need to make the gauge holomorphic.
Fix a real reference, prove inversion on its whole complex domain, then use the actual matrix entries.
This is finding 6's weaker consumer.

### 5.3 Trace and pair are still missing

I 49503–49518 expressly restricts the supplied gauges to $Q\cap\Omega_0$.
Equation (6) keeps that restriction.
Consequently a larger hull does not create a gauge outside the supplying domain.
This is an exact restriction in the theorem, not a loss in its constant.

There is a separate point about the pair.
I 119603–119612 preserves the unitary part through a stage.
I 119615–119650 uses one global pair and its own continuation.
It also keeps that pair unchanged off the support of the stage cutoff.
These facts prevent arbitrary replacement of exterior values.
They do not identify the localized determining set with a member of that stage geometry.

Raw heredity does not make that identification either.
Its relation is between two dates with no level lowered,
as stated at I 134758–134826 and proved at I 134826–134861.
A graded localization through a positive parent stratum creates lower grades near the cut.
It is then not one of those chronological moves.
Applying raw heredity to that new grade would reverse its hypothesis.
If the parent is already raw, restriction can preserve existing tests.
It still needs the required exterior reads inside their original domain.

**Failure of route 2.** The test route proves (4) once $E$ has the actual covering trace and pair.
The hull and raw-stratum theorems do not supply that trace at $\mathfrak B_Z$.
Using a new local extension would lose clause 2 of BZ-TRACE.
Using the localized layer theorem to certify the pair would use the conclusion being supplied.
This route reaches the same BZ-TRACE statement by test inheritance, rather than by identifying the cut.

## 6. Route 3: rebuild the localized member with the newer tower comparison

The newer account supplies a further possible route.
Its cut comparison constructs and compares actual constrained continuations.
Thus it could, in principle, replace exact inheritance with a quantitative boundary estimate.
Port its results with their stated domains; do not re-prove them.

N 37070–37119 intersects an ambient tower with the second-rule erosion of a localization domain.
It proves separation and the needed agreement near a protected inset.
N 35857–35908 proves the corresponding protected-stencil geometry.
These are positive results of Sussman and Alpoge.
They concern the rebuilt tower and its protected interior.

The output definition is decisive.
At N 36707–36753, the input field is on the inner bonds of $Z$.
Input differences have their whole read in $Z$.
Outputs are inner plaquettes and bonds whose six incident plaquettes are inner.
A base point is called settled when

$$
\lambda'(x)=\min\{\lambda^\flat(x),p\}.
\tag{8}
$$

N 36859–36877 gives the ambient estimate at these settled outputs.
N 37390–37460 compares two cuts only on unchanged free pillars.
Their complete reads must be settled in both towers.
Every changed datum carrier must also be at physical distance at least $D\ge2$.

These conditions exclude the missing boundary read in two independent ways.

First, consider a cut through a positive parent level.
At its new bare rim, the erosion has $\lambda'(x)=0$.
The parent has $\lambda^\flat(x)\ge1$, and $p\ge1$.
Thus

$$
0=\lambda'(x)<\min\{\lambda^\flat(x),p\}.
\tag{9}
$$

The rim is not settled.
It is precisely where the grades have changed.
No positive separation from the changed boundary carriers is supplied there.
The cut comparison cannot be evaluated there.

Second, even a settled raw rim has protruding whole-action plaquettes.
Such a plaquette is not an inner output of this theorem on $Z$.
Its exterior links are not among that theorem's inner inputs.
An estimate for all its permitted outputs therefore still omits PI coefficients.
This is the first-collar issue, not a demand for the unused second collar.

Enlarging the rebuilt domain would require supplying the same missing field trace on the enlargement.
It would also change the constrained problem.
Agreement of its averages is insufficient for equality of the fine pair.
The exact-fibre obstruction in c0-sup.md, section 7, already establishes that fact.
It need not be repeated.

**Failure of route 3.** The newer theorem controls protected outputs after changing a cut.
It supplies neither the uncovered exterior inputs nor the changed boundary outputs of BZ-TRACE.
This failure follows from its explicit output and distance conditions, not from a missing proof of that theorem.
The original prescribed domain has not been replaced by a smaller one.

## 7. The non-bare alternative

No source read here proves that the actual $\mathfrak B_Z$ has a non-bare edge.
The CMP 119 display cannot be used as that counterexample: section 3 proves why.
Nor does the display identify the actual edge as bare.
That identification remains part of BZ-TRACE.

If a literal construction instead leaves level-$j$ rows at the edge, Proposition 4.1 is unavailable.
Its replacement would have to control the **complete** boundary-model read:
the protruding plaquettes, outward averaging rows, full endpoint blocks, and difference stencils.
The row reads may then extend by $\ell_j$, beyond $X_\eta$.
The gap that kept those positive-level carriers inside $X$ has been lost.
Thus the one-spacing reduction itself must be checked again in this different class.

The required replacement of Proposition 4.1 would say this:
scale-weighted gauge and twist bounds on those complete reads give PI's local inverse bounds,
uniformly in $\ell_j/\eta$, for the literal rows and compressed whole-action Hessian.
Its proof would need a flat boundary inverse on that class, followed by coefficient comparison.
The existing bare inverse cannot supply its first step.
SA 10505 explicitly distinguishes these two boundary problems.

The original zero filling does not prove this replacement.
Let $s=\ell_j$, let $H$ be Hermitian with $|H|=1$, and retain the constant potential
$A=\alpha H/s$ up to a filling seam.
Put zero on the next parallel bond, one fine step away.
Then

$$
s|A|=\alpha,\qquad
s^2|\nabla A|=\alpha\,s/\eta.
\tag{10}
$$

The same calculation holds for a twist at identity reference.
The second quantity has no bound by a depth-independent multiple of $\alpha$.
A smooth filling would require room on scale $s$ outside every fixed actual read.
No such room is supplied for the hypothetical non-bare entry.

Equation (10) rejects this proof method.
It is not a counterexample to every possible boundary inverse.
It is also not a counterexample at a reached $\mathfrak B_Z$.
This branch therefore supplies neither stop (a) nor stop (b).

## 8. Outcome

This is stop **(c)** at **BZ-TRACE**, section 4.
The three routes are:

| Route | What it establishes | Where it fails to supply BZ-TRACE |
|---|---|---|
| Literal CMP 119 splice, section 3 | A graded splice has a bare rim; a buffered cut gives its first exterior spacing inside the parent. | The actual B_Z cut is not identified with this splice or with the buffered component of I 94780–94812. |
| Item 10 tests and hull gauges, section 5 | One admitted covering gauge gives the exact smallness transfer (7). | Hulls preserve their domain trace. Chronological raw heredity does not cover a localization that lowers grades. |
| Newer geometric-cut comparison, section 6 | Protected interior continuations can be compared on complete admitted stencils. | The new rim is not settled in a positive parent stratum; protruding plaquettes are outside the theorem's outputs in every case. |

There is no complete proof of C0-ETA at the literal localized entry.
There is also no reached-entry counterexample.
The account's localized layer bound remains its declared input.
Invoking it would not prove this boundary supplier.

The useful refinement is the boundary diagnosis.
The quoted CMP 119 rule has a bare staircase edge, even when the parent cut has positive level.
The unresolved task is to identify and cover the actual read at B_Z.
It is not to glue arbitrary gauges or estimate an unused second collar.

The conditional arguments and the filling obstruction above are hand arguments.
They have not been checked by another model.
No numerical run, search over fields, or machine enumeration supplies any mathematical conclusion.

## 9. Status table

| Statement | Status in this note | Scope |
|---|---|---|
| PI's first-spacing read reduction and bare filling | Existing proved inputs, checked in c0-sup-check.md | PI tower class and supplied pair bounds. |
| CMP 119 minimal tower and localization splice | Ported from Sussman–Alpoge, I 32861–32894, 93580–93588, 147407–147427 | Their stated construction; not identified with item 10's B_Z. |
| A coarse parent cut need not give a coarse localized edge | Proved conditionally, Lemma 3.1 | The printed graded splice; boundary gap given by (2). |
| First exterior spacing lies in the ambient domain | Proved conditionally, (3) | Requires the actual cut and its boundary buffer. |
| Test/hull radius transfer | Ported bounds and conditional consequence (7) | One admitted trace, the same fine-link convention, and the original parameter image. |
| Newer cut comparison | Ported with its output conditions | Does not cover the required new boundary read. |
| Value-only zero filling at a non-bare edge | This method fails by (10) | No claim that the actual edge is non-bare. |
| BZ-TRACE implies boundary C0-ETA | Conditional implication, section 4 | Retains interior admission and all other consumer hypotheses. |
| BZ-TRACE for the literal B_Z | Open after three routes | No actual cut/trace/pair certificate has been established. |

**First open input: BZ-TRACE.**
Identify the literal localized tower and supply its admitted boundary trace with the actual pair,
on the full prescribed parameter and switch domain, before using the localized layer theorem.
