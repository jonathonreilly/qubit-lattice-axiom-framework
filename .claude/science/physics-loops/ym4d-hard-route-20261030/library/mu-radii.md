# MUR: minimizer uniqueness at the remaining data radii and domains

Provenance: Research text against checkout ec845e49b and the Sussman–Alpoge sources at 31a47c543775. Source authors: Ethan Sussman and Levent Alpoge, with Claude and Codex. This note checks carry-over from the frozen library/mu.md; it grants no audit or retained status. No computation discharges a proof obligation.

## Source checkpoint

The checkout is `ec845e49b92c8eec949f70f3d5165ec5d1ba2bb5`. The outline and CA-I were fetched once. Existing CA-II/III copies were reused after their SHA-256 values matched the frozen `mu.md` manifest. The exact-label and literal `(3.38)` search is saved at `/tmp/mur-ec845e49b/use-hits.txt`. These operations are source navigation only.

The index was read before the relevant source excerpts: `sa-index/README.md`, chunk 09 and its neighbouring rows, `obligations.md` at 9776/9842/9913, the CA 4.12–4.19 README and chunk 02, and the complete-account statement index. The outline's restriction argument at 9776–9781 and 9913 is a sketch. This note uses the frozen proof in `mu.md`, not that sketch as an additional theorem.

The literal lemma label occurs only at CA-I 45163. Its `(3.38)` citations outside §§4.7–4.8 are:

| CA location | What the citation does |
|---|---|
| I 10607 | Names the floor on the cube-gauge constant for the already treated one-power class. |
| I 45172, 45195, 45200 | States the target, its proposed route and its consumer; no additional domain. |
| I 121193, 121226, 121389, 121436, 121440, 121467, 121522 | Stage near pairs, their full datum, and composite-entry comparison. |
| I 123126, 123129 | The same comparison on the graded cover. |
| I 129545, 130188 | Root geometry and gauge-action conventions; no new data radius. |
| I 144933 | The lifted-point version in §4.28. |
| I 154420 | The local form (a) of §4.31's nesting assertions; the adjacent global assertions require separate attention. |
| II 35714 | Local-box restriction of the refined minimizer in §5.5(a4). |
| II 44422, 44454 | A bound on the potential value, rather than the nesting identity. |

The other literal hits cite **CMP 99b**, not CMP 109: CA-I 12969, 25069, 25219, 25290, 28131, 131692; CA-III 36360, 75788. There is no new CMP 109 nesting use among those hits. The excluded §4.7–§4.8 hits are I 29235, 29237, 31073–31074, 31122, 32422, 33684, 33765.

The broader spelling search also finds the status lists at I 166621 and III 111211–111212. They repeat that the proof is outstanding in the account and introduce no new application. The labels (N1)–(N3) below are the three forms in §4.31, not additional occurrences of the literal lemma label.

The main radius checks are proved below, with their existing hypotheses retained. The literal block-constant formula in §4.31, the separate numerical bound in its form (b), and the stronger whole-rim reading of the last potential estimate must be distinguished from the weaker assertions actually used. The Result records those limits. Balaban's cited theorems and gauge construction are credited to Tadeusz Bałaban; the account's constructions and parameter families are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex.

## 1. Uniform restriction lemma and its exact gauge

Use the constants of `mu.md` §§4–5. In particular, \(r,K,a_{98},C_A,C_D,C_7,
\delta>0\) are fixed before the running amplitudes. Make the fixed
enlargement of \(C_A\) specified in §4.2 before selecting \(\delta\).
Decrease \(\delta\) once, if necessary, to keep every inequality below
strict. This does not change the
frozen file. Write \(s_b\) for a row's block side and \(\ell(b)\) for the
local block side of a tower. Its base-one chart satisfies
\[
 \sup_b\ell(b)|H(D)(b)|\le K\|D\|_\infty,\qquad \|D\|_\infty<r.       \tag{1}
\]
Both actual group averaging and the auxiliary potential average obey
\[
 |\log M^q(e^{ihF})(c)|, |Q_q(hF)(c)|
 \le C_A s_c\sup_{E_c}|F|,\qquad s_c\sup_{E_c}|F|<a_{98}.             \tag{2}
\]
The factor \(1/i\) does not change the norm. These are the proved statements of
`mu.md` (4.2)–(4.3), including its printed-page source check. They are not
interchanged definitions of \(M\) and \(Q\).

Let \(W(D)=\mathcal U(D)^{u(D)}\) be the axial outer minimizer, with
\(\mathcal U(D)=e^{ihH(D)}\). Let \(\mathcal T\) be an admissible inner
tower. Require its averaging carriers and axial trees to lie in the outer
top region, and its block sides to be no larger than the outer top side.
The outer top side is one in this paragraph. The inner tower may have
holes or several components. Its level-zero shell and seam rows retain
the actual Balaban convention. Then, for \(\|D\|<\delta\),
\[
 U_{\mathcal T}\bigl(M_{\mathcal T}\mathcal U(D)\bigr)
 =\bigl(W(D)|_{\mathcal T}\bigr)^{\bar u_{\mathcal T}^{-1}}
 =\bigl(\mathcal U(D)|_{\mathcal T}\bigr)^{g_{\mathcal T}},
 \qquad g_{\mathcal T}=\bar u_{\mathcal T}^{-1}u.                    \tag{3}
\]
Here \(\bar u_{\mathcal T}\) is constant on each inner structure block,
with value \(u\) at its root, and equals \(u\) on the prescribed shell.
**The relative gauge \(g_{\mathcal T}\) is generally not block-constant.**

Here is the proof, including the facts used when the domains change.
Equation (1), the carrier assumption and (2) give
\(\|\log M_{\mathcal T}\mathcal U\|\le C_AK\|D\|<r/2\).
Thus the inner chart exists on the whole outer \(\delta\)-ball.
For real \(D\), the outer field has regularity
\(\epsilon_W\le B_3C_D\|D\|\). Refine the outer tower by the inner
positive-level members and keep the original outer first member. The
additional level-zero rows fix the exterior. Composition of the actual
averages gives inclusion of the refined fibre in the original fibre.
This is precisely CA-III 36939–37007, not a locality assertion about
arbitrary boundary values. A curve on the inner fibre extends by the
fixed outer field. Every varying bond touches the inner first variable
region. The first separation puts every affected plaquette inside the
inner action domain. The two action derivatives are therefore equal;
the outer derivative is zero. Local block sizes only decrease, so the
restricted real field stays in the regular uniqueness space. Its data
tests are at most \(C_7\epsilon_W\). The inequalities (5.2) of `mu.md`
make both applications of the real uniqueness theorem valid.

The inherited inner trees are a subset of the outer aligned trees.
Hence the restricted outer axial field is already inner axial. A
residual transformation fixing the roots and preserving all tree bonds
is one, successively down every tree. This identifies the representative,
not only its orbit. Covariance of the actual averages now gives (3) at
real \(D\). Both sides are holomorphic on the whole \(\delta\)-ball by
the chart inclusion just proved. The identity theorem on the real slice,
one coordinate at a time, proves (3) throughout that ball. The curvature
and current identities follow by gauge covariance; the current gains
\(s_n^3\) when written in inner top-block units. This is `mu.md` §6 with
its corrected left-action order. No minimization of a complex-valued
action is involved.

At depth zero the determining rows are the fine bonds themselves.
There are no inner tree edges or variable bonds to minimize over;
\(U_0(X,M^0\mathcal U)=\mathcal U|_X\) and
\(\bar u_{\mathcal T}=u|_X\), so \(g_{\mathcal T}=1\).
Thus the same formula includes this endpoint without a limiting argument.

The same real restriction argument also applies to a real regular outer
minimizer which is not in a base-one chart. In that case one must supply
complex admission about its induced **real** datum. Small curvature alone
does not put its literal group-valued data near one. Section 4 below pays
for that distinction where it occurs.

## 2. Stage near pairs: §§4.26 and 4.28

### 2.1 The actual parameters and domains

The datum is
\[
 D_P=\varsigma B(t,\tau)+B'
     =\varsigma Q+\varsigma Q'(t,\tau)+B',\quad
 \varsigma,t\in[0,1],\quad
 |\tau|\le {\mathsf w_0\over K^{\rm nr}\vartheta(\square)},\quad
 \|B'\|<\alpha_3(T).                                               \tag{4}
\]
These are CA-I 117396–117451 and 121226–121232. In particular, \(\tau\)
is not bounded by one. It multiplies the stage layer, not the whole datum
\(Q\). The third radius (I 117206–117225) satisfies
\[
 \alpha_3(T)\le
 \min\{\operatorname{room}_T\alpha_{\cdot,\ell}/(12B_3),
       \beta L^{-2}\alpha_{0,\cdot}/(2B_3),
       \alpha_{1,\cdot}/(3B_3)\}.                                  \tag{5}
\]
The inner triples have \(p'\le\ell=\ell_T\) and
\(X'\subseteq X_T\subset\tilde\square^2\); the outer box is
\(\square_0=\tilde\square^5\). The source structure on that box has
levels at least \(\ell\). Its shell levels take at most two adjacent
values. These are I 120581–120653 and 121175–121232. The graded-cover
use at I 123126–123132 has the same domains and datum.

At lifted points the source structure is
\(\mathfrak B^{\mathfrak c}|_{\square_0}\). The levels of
\(\mathfrak c\) again take at most two adjacent values and are all at
least \(\ell_T\). The box and its carriers are supplied by
\([\square_0]_\sharp\subset Y\). The radius (5) uses
\(\operatorname{room}^{\dagger}_T=\beta/2\). See I 144305–144430,
144671–144748 and 144933. Thus lifted depth is not an extra factor in
(4). The conversion in I 144379–144409 absorbs its weight into the
cutting-level radius before the box calculation.

### 2.2 Admission on every row

Here is an explicit extension of `mu.md` §7. Put
\[
  a=\max\left\{\sup_m\max\{\alpha_{0,m},\alpha_{1,m}\},
                  \bar\gamma_0(t_\gamma)\right\}.
\]
All radii appearing in this maximum are the running radii of the fixed
family, including birth radii when a piece is frozen; \(\alpha_{\cdot,m}\)
stands for one of the two radii (I 116590–116592). The second member is
the run-free majorant of \(\gamma_0^{(k)}\), I 116606–116630. It pays
also for the ambient clauses and their frozen weights. Let \(E\ge1\) be
a fixed conversion constant for the following operations: conversion
between the two adjacent shell units, the input factors \(1+2\beta\),
and the fixed local norms of the near-pair dictionary. One can use the
maximum of the constants in I 120504–120653 and 144305–144430,
multiplied by \(4L^3\). It depends on the fixed constants, not on a level,
a weight or a box. Increase it once to cover the two bounded changes of
frame below. Its choice does not read (a).

In units of the coarser of the two shell levels, the whole box input has
real curvature and complex twist sizes at most \(Ea\). This statement
uses the input clauses on the **whole** box, not just the smaller
\(\tilde\square^4\) used to define \(\mathfrak a_0,\mathfrak a_1\).
For the lifted case these are (h4) and (H) of I 144700–144748. For the
ordinary case these are the inherited-domain input and shell geometry
of I 120920–120944 and 120581–120653. More explicitly, the domain is the
intersection at I 119705–119710: on the run it supplies the lettered
clauses, and off the run it supplies the unweighted direct clauses
(B)–(C) of I 119476–119479. The ordinary box excludes the lifted points;
the at-most-two adjacent shell levels cost only the fixed powers of
\(L\) in \(E\). On a lifted box use the conversion on the entire box
at I 144379–144409; its factor \(0.381^g\le1\) removes the possibly
large frozen weight before taking the supremum. No supremum of that
weight is absorbed into \(E\). These inputs remain hypotheses of the
respective consumer theorems. The ambient extension in
I 119464–119479 supplies (A)–(C) on \(Y^+\), and
I 116606–116610 bounds the potentially weighted (A) amplitude by
\(\gamma_0^{(k)}\le a\). Thus a carrier at the box boundary does not
require extending the sharper interior radii without a hypothesis.
For the ordinary two-level box the source top level differs from its
cover level by at most one. Since \(M\) is a power of \(L\), its
coarse blocks are aligned with the box. The global averages used for
the upper contour legs are available on those blocks, and the
prescribed outer rows use the ambient extension. For lifted boxes the
stated containment \([\square_0]_\sharp\subset Y\) supplies these
same carriers. The fixed one-level conversion is included in \(E\).

Apply the literal-frame construction to its actual determining rows.
The argument of I 17322–17447, 17673–17778 also covers a restriction of
the two-level structure: each such row is the corresponding global
\(q\)-average. Extend the definition of its frame on missing upper
contour legs by those global averages, exactly as at I 17385–17405.
The top contour has at most \(C_dM\) bonds with \(C_d=12dL\):
the box has eleven cover cubes per side and the two scales differ by
at most one. Each descending leg has at most \(dL\) bonds, and its twist bound has a factor \(L^{q-p_\square}\).
Consequently its total twist length is bounded by
\[
 Ea\left(C_dM+dL\sum_{q<p_\square}L^{q-p_\square}\right)
 \le Ea(C_dM+2d).
\]
The real contour estimate and the comparison with its complex twist
are exactly AX2-poly, whose proof needs only those contours and the
real curvature bound. It reads every row, including the shell rows.
Thus, enlarging \(E\) if necessary but still before (a),
\[
 \|B_V\|\le 2C_VM E a.                                           \tag{6}
\]
The logarithm is justified by \(C_VM Ea<1/4\). The complex part of the
frame has norm and inverse norm at most two once its displayed contour
sum is small. The Landau-to-axial frame of its small incoming chart
also has such a bound by its tree product. These account for the fixed
frame enlargement in \(E\); no input hereditary-composite bound is used
to prove (6).

The stage layer remains small on its large \(\tau\)-disc. Before entry
conversion, I 117732–117744 gives the bounds
\[
 N(\tau\zeta_\square\mathbb H^w)
 \le {\mathsf w_0\rho_m\alpha_{\cdot,m}\over3K_{\rm cv}},\qquad
 N(t\zeta'_\square\mathbb H^w)
 \le {\mathsf w_0\rho_m\alpha_{\cdot,m}\over18K_{\rm cv}}.          \tag{7}
\]
The schedule factor \(\rho_m\) is at most a fixed constant, already
included in \(E\). For example the stage-increment identity
\(\iota_l^1=(2/3)\mathsf w_0\rho_m\) and its schedule ceiling
\(\iota_l^1\le\beta\) give \(\rho_m\le3\beta/(2\mathsf w_0)\).
This is not the possibly infinite empty-infimum \(\operatorname{room}_T\).
Their sum, converted to the common box unit and to the incoming
Landau frame, is therefore at most \(Ea\). Notice the cancellation of
\(\vartheta(\square)\) in the first bound. Replacing \(|\tau|\) by a
fixed number would not prove admission on this disc.

Choose \(2C_VMEa<r/2\). Equation (1) bounds the incoming box potential
on every layer by \(K\|B_V\|\) in that layer's unit. An outgoing row
of level \(q\le\ell\) has its carrier in the preceding outer layer.
Its block side is at most \(L\) times that layer's side. This includes
outward rows: the neighbour across the face is still in the preceding
layer by separation. The positive-level structure in the box has
levels at least \(\ell\), and the maximal boundary towers are nested.
Thus the carrier comparison used in `mu.md` (7.2) holds here too.

For a carrier \(E_c\), the composed potential \(F\) therefore satisfies
\[
 s_c\sup_{E_c}|F|\le2L(Ea+K\|B_V\|).
\]
This follows by applying
\(|\log(e^{iX}e^{iY})|\le2(|X|+|Y|)\) in the fixed small matrix ball;
its power-series proof is in `mu.md` §7. It is valid on the shell as
well as the top region. Apply the auxiliary \(Q\) bound (2). Since
\(|\varsigma|\le1\), (5)–(6) give
\[
 \boxed{\quad
 \|D_P\|\le
 2LC_A\bigl(E+2KC_VME\bigr)a+{a\over3B_3}<\delta .\quad}           \tag{8}
\]
One may replace the last term by \(2a/(3B_3)\) to provide a doubled
\(B'\)-proof radius. Also impose
\(2L(E+2KC_VME)a<a_{98}/2\) and the fixed logarithm ceiling. These are
finitely many upper bounds on (a) by positive fixed numbers.

Every carrier and tree of the inner \(X'\)-tower lies in the outer
level-\(\ell\) top region. Indeed \(X'\subset\tilde\square^2\), while
that region contains \(\tilde\square^4\). The largest inner block has
level at most \(\ell\le i\); a layer of the box has side \(ML^i\)
in common lattice units. The two layers dominate a two-block carrier
and its tree under the already imposed \(M\) floor. Holes in \(X'\)
only add prescribed inner shell rows. This is exactly the geometry
required in §1. The source's conflicting prose about the sign of
\(\square_0^{\sim2}\) is unnecessary here: the explicit nested boxes
\(\tilde\square^2\subset\tilde\square^4\subset\tilde\square^5\)
are the sets used in the proof.

Apply (3). This proves the nesting identity for every ordinary,
graded-cover and lifted-point member (4), on every own triple.
It applies to the Landau representative on which the entries are
actually read (I 120980–121026), and by covariance to the axial one.
The relative factor is \(\bar u_\ell^{-1}u_\ell\), as already written
at I 121440 and 123129.

### 2.3 Constants and scope of the conclusion

The stage running radii have the form
\(C e^{-t/2}t^q\), \(t\ge t_\gamma\), at I 124430–124470.
For \(t\ge4q\), its logarithmic derivative is at most \(-1/4\).
It decreases to zero. Hence its supremum on this tail tends to zero
as \(\gamma\downarrow0\). The ambient majorant is also a fixed multiple of
\(e^{-t/2}t^{r+q}\), I 116615–116630. Its logarithmic derivative is
\(-1/2+(r+q)/t\), hence at most \(-1/4\) for \(t\ge4(r+q)\).
It too tends to zero, so the enlarged \(a\) has the required limit.
The fixed ratios of the remaining radii are included in \(E\). Choose all geometric constants, then \(E\),
then impose (8) by decreasing \(\gamma\). This is the account's
order (I 124467–124473). Nothing asks \(M\), a decay rate or a stage
constant to depend on \(\gamma\). Birth radii obey the same supremum
bound, irrespective of the age when they are read.

Classification: **carry-over after these radius ceilings**, with the
geometry verification above. The assertion at I 10607 merely names
the one-power-class floor already present in `mu.md`; it adds no
radius and is covered unchanged. The root and convention citations
I 129545 and 130188 also add no radius.

This proves the identity, not the separately assumed sharp bound
\(\|g\|\|g^{-1}\|\le G'_\square\). The account expressly separates
that hypothesis at I 121440–121455 and 123129–123132. Nor does (3)
assert that either product configuration in I 117470–117478 is itself
a minimizer. Their extra factors are general own-level layers.
The (3.38) use concerns their baseline \(P\); the entry moves of the
two remainders use the separate perturbation estimate, as at
I 121605–121665 and the explicit hypothesis (h10), I 144728–144730.
Small amplitude alone cannot replace the criticality requirement.

## 3. CA-II 35714: a refined minimizer on a local box

The field is the first box pair
\[
 \mathfrak b'_j=(U,J)(\mathfrak B_j^*,M^\cdot\mathfrak b),\qquad
 \mathfrak b=e^{i\eta\mathbf A}\mathbb W,
\]
with \(\mathbf A=(t\zeta'_\square+\mathsf t\zeta_\square)\mathbb H^w\).
Its definition is II 34176–34221. The parameters are the filed box
disc \(\mathsf t\in\mathbb D_\square\), \(t\in[0,1]\), and
\(|\sigma|\le e^{\kappa_1}\), not a new freely chosen data ball.
The use at II 35710–35714 concerns
\[
 j\le p,\quad \square'_0\subset Q^{\sim-2},\quad
 Q^{(1)}\subset\tilde\square^3,
\]
where \(Q\) has at most nine \(\pi_p\)-cubes per side and every cell
meeting \(Q^{(1)}\) has level at least \(p\). Its inner datum is
\(\mathsf V'=M^\cdot\mathfrak b'_j|_{\mathfrak B_j(\square'_0)}\).
The assertion is **modulo gauge**, as in II 35315–35319.

Set \(t_p=L^{j-p}\le1\) and
\(a_Q=K_{\rm loc}w_Q\alpha_Q\). Retain the account's majorant
comparison in II 35662–35667, in the conservative form
\[
 w_Q\alpha_Q\le C_Q\mathsf A_w(\gamma),\qquad
 C_Q=\max\{1,K_{\rm loc}/(5.6K_hK_{ax}MC_M^{av})\}.
\]
Indeed the last scalar inequality in that display bounds
\(5.6K_hK_{ax}MC_M^{av}w_Q\alpha_Q\) by
\(K_{\rm loc}\mathsf A_w\); division gives the assertion. This
comparison concerns the input weights, not the restriction identity.
Its constants are chosen before \(\gamma\), and
\(\mathsf A_w(\gamma)\downarrow0\), II 34664–34728 and 34831–34849.
No equality between the product of two separate maxima and the maximum
of their product is presumed.

There is an apparent ordering trap in the printed proof: the uniform
inner-chart radius is not proved by simply saying “identity theorem”
at II 35655. The required bound can be obtained *before* making that
argument. Use parts (a1)–(a3), the constraints defining \(\mathfrak b'_j\),
and the averaging and comb calculation at II 35716–35747. On a top row,
\(M^j\mathfrak b'_j=M^j\mathfrak b\) is a constraint, not a consequence
of the desired restriction identity. On a rim row one instead averages
\(\mathfrak b'_j\) at level \(i<j\). Part (a2) and the complex averaging
bound used in the account give
\[
 8C_M^{av}w_Q\alpha_Q t_p^2 L^{2(i-j)}
 \le c_1a_Qt_p^2 .                                                \tag{9}
\]
The last inequality uses \(K_{\rm loc}\ge8C_M^{av}\), \(c_1\ge1\)
and \(L^{2(i-j)}\le1\). Part (a3) gives the same top-row estimate.
The account's comb construction therefore gives on **all** inner rows
\[
 \|D'_{ax}(b)\|
 \le2d(1+|b-y|)c_1a_Qt_p^2.                                      \tag{10}
\]
This ports that construction, with its complex averaging/distortion
hypothesis, not a new deduction from curvature alone. Neither the
top constraint nor the rim calculation uses the equality at 35712.
Thus using (9)–(10) for chart admission does not assume that equality.

In level-\(j\) units a box inside \(Q\) has side at most \(9M/t_p\).
Using the largest of the coordinate and path distances,
\(1+|b-y|\le10dM/t_p\). It follows that
\[
 \boxed{\quad
 \|D'_{ax}\|\le20d^2Mc_1K_{\rm loc}C_Q\mathsf A_w(\gamma)t_p
 \le20d^2Mc_1K_{\rm loc}C_Q\mathsf A_w(\gamma)<\delta/2 .\quad}         \tag{11}
\]
The potentially long box costs \(t_p^{-1}\); its datum gains \(t_p^2\).
There is no depth-dependent ceiling. Equation (11) also provides
margin at the boundary of the filed source discs. It is stronger
than the single smallness inequality printed at II 34847, and is
permitted by exactly the same order of choice.

For real data \(\mathfrak b'_j\) is the regular constrained minimizer
specified in its definition. Near \(\square'_0\), \(\mathfrak B_j^*\)
has level exactly \(j\): the refinement caps all levels there at \(j\).
Refine by the maximal \(j\)-tower of \(\square'_0\), leaving the
outer field fixed. Every new row is finer than, or equal to, the old
row it replaces. The fixed shell and composition of averages preserve
the old constraints. Separation again puts all varying plaquettes
inside \(\square'_0\). Therefore restriction preserves criticality,
with the same proof of equality of action derivatives as in §1.
The real restriction is in the regular uniqueness space, since its
local block sides only decrease. By (11) its induced datum in the
comb frame is admitted to the inner chart. The real uniqueness theorem
identifies the two regular critical orbits.

For complex parameters use the source's analytic minimizer family
and the holomorphic comb frame. Include all the complex source slots
in this continuation: holding an already complex source fixed and
varying only \(t,\mathsf t\) would not give a real slice. In each
source chart the reference is real, and making its field, fluctuation
and auxiliary coordinates real gives the real family just considered.
The source minimizer's regular variational-space membership, including
the fourth-entry bound explicitly invoked at II 35710, is retained;
curvature (a2) alone is not a substitute for it. The needed new inner map is now
holomorphic on the entire parameter domain by (11), not merely in a
neighbourhood of a real point. Fixing an axial representative uses
finite products of the actual averaged tree bonds, which are also
holomorphic. The equality of these representatives holds on the real
slice, so it holds on the connected polydiscs by the identity theorem.
Gauge covariance then removes the chosen comb frame. This proves
\[
 \mathfrak b'_j|_{\square'_0}
   =(U_j,J_j)(\square'_0,\mathsf V')\quad\text{modulo gauge}.         \tag{12}
\]
The same argument also justifies the preceding restriction of
\(\mathbb W\) to \(Q\) at II 35641–35655: its comb datum has size at
most \(K_{\rm loc}\mathsf A_w(\gamma)\), II 35662–35667. The extra
condition (11) covers it after taking the maximum of these two fixed
coefficients.

Classification: **carry-over after a radius ceiling and the stated
local refinement**, not an application requiring the *global* datum
of \(\mathfrak b'_j\) to be near one. The already assumed source
minimizer, complex averaging bounds and source-family analyticity
remain inputs of this implication. No claim about another branch of
complex critical points, or about arbitrary changed boundary data,
is made.

## 4. The §4.31 citation and the adjacent global assertions

### 4.1 Local radius: the carry-over is uniform

CA-I 154420 explicitly identifies **(a)** of I 154338–154405 with
(3.38). Its datum satisfies \(\|D\|\le\beta\le\beta_W\), and its
domains satisfy \(X^{\sim5}\subset\square_0\). The claimed identities
are read on \(X^{\sim-2}\). The local background
\(\mathbf U[D]=e^{i\xi H_j(D)}\) is the Landau field, not its axial
copy in the Balaban interpretation of this citation. I 154193–154224
displays a bare exponential, and CMP 102b §G, (173) and Proposition 9
specify that the corresponding \(H\) is the Landau potential. A change
to a different normalization would require an explicit identification.
The needed estimate below can also be proved directly from the local
background assumptions of §4.31: its exponent is bounded on
\(\square_0^{\sim-2}\supset X^{\sim3}\) by \(2C_{19}B_0\beta\),
and at real data it represents the same minimal orbit. Use
\(K_W:=\max\{K,2C_{19}B_0\}\) instead of \(K\) in the carrier and
tree estimates of this subsection, and choose
\(\beta_W<\min\{\delta/2,a_{98}/(2K_W),r/(2C_AK_W)\}\).
Then real refinement followed by inner axialization and continuation
proves the same relative-gauge statement, without inferring an axial
normalization merely from the word “minimiser”.

Choose
\[
             \beta_W\le\delta/2.                                \tag{13}
\]
The five-layer margin puts every inner carrier and tree in the outer
top region, just as in §1. Formula (3) therefore holds on every such
\(X\), for every \(n\) allowed in the cited (1.16). The fact that the
aligned outer cube may have many cubes per side adds no factor:
(1) is a supremum bound independent of its size, and the paths used
here stay within individual structure blocks.

There is also a uniform bound for the **relative** gauge in (3).
At a tree edge of averaging level \(m<n\), (2) bounds its logarithm
by \(C_AK_W\beta s_m\). A descending path has at most \(dL\) such edges
at each level. The sum of their physical lengths is bounded by
\[
 dL\sum_{m<n}s_m
 \le {dL\over L-1}s_n\le {dL\over L-1}.
\]
The tree-product identity, CA-I 130055–130176, contains no uncontrolled
conjugations. Multiplying the exponential bounds for each factor and
its inverse gives
\[
 \|g_X^{\pm1}\|\le e^{C_tK_W\beta},\qquad C_t={dLC_A\over L-1}.
\]
For \(C_tK_W\beta\le1/2\), the power series gives
\(e^{C_tK_W\beta}\le1+2C_tK_W\beta\). Choose \(c_u\ge2C_tK_W\), and decrease
\(\beta_W\) further so that this bound holds. Then
\[
 U_n(X,M^n\mathbf U[D])=\mathbf U[D]^{g_X},\quad
 \|g_X^{\pm1}\|\le1+c_u\beta.                                    \tag{14}
\]
The corresponding current identity has the factor \((L^n\xi)^3\).
These choices are made from the universal chart constants before
\(\beta_W,w_s,r_s\). They do not determine a geometric constant from
a running radius.

The later use of this assertion, called (N1), is I 156008–156038.
There \(D\) is replaced by \(\tau D\), and
\[
 |\tau|N'<
 \min\{\alpha'/(12B_0C_{19}),\beta_W,1/(10c_u)\}.
\]
With (13), this whole path is in the required ball. Equation (14)
gives \(\|g_X\|\|g_X^{-1}\|\le1.1^2=1.21\), exactly the factor
that consumer uses. Its curvature and current estimates therefore
carry over after (13), with no changed age, volume or path radius
beyond the displayed minimum.

### 4.2 The global-to-local and wrapping domains

Although the literal citation at 154420 refers only to (a), the adjacent
(b) and (c) are part of the same nesting input, later called (N2)–(N3).
Their data are genuinely different. They start from
\[
 W_{V_0}(B)=e^{i\eta H(B;U_0)}U_0,\qquad U_0=U_k(V_0),
 \quad V_0\in\mathcal V_s(w_s),\quad \|B\|<4r_s,
 \quad \rho_s=2B_3w_s+8B_0r_s.                                   \tag{15}
\]
Here \(V_0\) is real and regular; it need not be near one. The bounds
\(\|H\|\le C_{19}\rho_s\) and real-minimizer identification are
source inputs, I 154153–154182. Case (c) allows every connected \(X\),
including large and wrapping sets. Thus the **base-one admission step
of `mu.md` does not apply unchanged**. Reducing \(r_s\) cannot make an
arbitrary fixed \(V_0\) close to one.

There is a real-base version of the same argument. Fix a positive
regularity parameter \(\epsilon_*\) smaller than the real uniqueness
and continuation thresholds and the real-background threshold of
CMP 98 Proposition 6. Enlarge \(C_A\) once, if needed, to cover that
proposition's general real-base form as well as (2). At any real minimal base whose data tests
are at most \(\epsilon_*/2\), CMP 102b (172) supplies the same positive
perturbation radius \(r_g\), independent of the domain and the base.
For example, decrease \(r_g\) below \(C_1\epsilon_*/4\) and the fixed
logarithm radius. This is the same positive-parameter device used at
base one in `mu.md` §4.1. The account records it for general real bases
at I 38511–38555. No differentiability-decay estimate is used.

For an \(X\)-tower let \(V_{X,0}=M_X(U_0|_X)\). The real refinement
and action-domain proof in §1 apply to the whole-torus outer problem:
there is no outer boundary to cross. They give its regular minimal
orbit on \(X\), with the inherited axial representative. The real
data tests are at most \(C_R B_3w_s\), where \(C_R\) is the fixed
converse-test constant, enlarged to cover the curvature and current
normalizations and the real-background tests of that proposition. Choose
\[
 C_RB_3w_s<\epsilon_*/2
\]
and the real uniqueness ceilings of `mu.md` (5.2), with the same
fixed constants. This covers disconnected intermediate layers and
wrapping \(X\) alike: refinement only decreases local scales, and the
inner fixed shell still contains every change of action domain.

On every determining row, Proposition 6's averaged-twist estimate
about the real field \(U_0\) gives
\[
 \left\|{1\over i}\log\bigl(M_XW(B)\,V_{X,0}^{-1}\bigr)\right\|
       \le C_AC_{19}\rho_s.                                     \tag{16}
\]
Indeed its output block side is at most the global top side one;
the twist in (15) has supremum \(C_{19}\rho_s\). A fine shell row
has the still smaller factor \(\eta\). Every carrier is in the
whole-torus top region. Impose
\[
 C_{19}\rho_s<a_{98}/2,\qquad C_AC_{19}\rho_s<r_g/2.                \tag{17}
\]
The entire \(4r_s\)-ball is now in each *real-base* inner chart.
Both the global field and the inner chart are holomorphic on that
ball. Axialize the global restriction by its actual tree products,
fixing the inner determining roots. For real \(B\) the real uniqueness
argument identifies this axial field with the inner minimizer. The
identity theorem identifies them for complex \(B\) as well.

The axializing gauge is uniformly controlled. The real base \(U_0\)
is axial on every inherited inner tree. Thus its averaged tree-bond
values are one. The perturbed values have logarithm bounded by
\(C_As_m C_{19}\rho_s\). The geometric series of tree lengths used
above gives
\[
 \|h_X^{\pm1}\|\le e^{C_tC_{19}\rho_s}
 \le1+c_u(B_3w_s+C_{19}\rho_s),                                  \tag{18}
\]
after increasing \(c_u\) once and imposing
\(C_tC_{19}\rho_s\le1/2\). Consequently the correct global identity is
\[
 U_n(X,M^nW)=W^{h_X},\qquad
 J_n(X,M^nW)=(L^n\xi)^3\operatorname{Ad}(h_X)J^\xi(W).             \tag{19}
\]
The gauge \(h_X\), like \(g_X\), need not be block-constant.
This proves the radius and domain extension needed for the global
curvature/current comparison. Its actual (N3) consumer is
I 155387–155429, for every \(j=k-t\), every connected \(X\), and
every allowed \(n\le j\). Keep the strengthened (S1) condition
\(c_u(B_3w_s+C_{19}\rho_s)\le1/10\). The gauge in (18) then has
both norms at most \(1.1\), so its adjoint norm is at most \(1.21\).
The consumer's curvature estimate gains exactly this factor. The
current gains it and \((L^n\xi)^3\le(L^n\xi)^2\), since
\(n\le j\) and \(\xi=L^{-j}\). These are the only two uses of
nesting in that paragraph; block-constancy is unused. This argument
retains the supplied global background construction and its direct
curvature/current bounds.

For (b), the consumer actually needs equality of gauge-invariant local
functions. Let \(g\) be its chosen gauge and suppose its actual
terrace datum
\(D=-i\log M^\cdot(W^g|_{\square_0})\) is in (13). Apply the
real-base restriction just proved on \(\square_0\), then use gauge
covariance of the axial minimizer. Its orbit is the same as that of
\(W^g\). Since \(D\) also lies in the base-one chart, the one-function
property of the minimizer (I 38550 onward) identifies this chart with
that orbit. Thus on the common local-function domain
\[
 f(W^g,\operatorname{Ad}(g)J(W))=f(\mathbf U[D],J(\mathbf U[D])).    \tag{20}
\]
All \(G^{\mathbb C}\) gauges are allowed for these (f), I 153964–153980.
No particular bound on the gauge relating the two representatives is
needed for (20).

The actual gauge used at I 156050 has a datum bound on the **whole**
\(4r_s\)-ball, not just at the evaluation point. I 155895–155956 proves
\[
 \|D\|\le c_{\rm av}N_0\le2c_{\rm av}C_gMh_s,\qquad
 h_s=8(B_3M'w_s+C_{19}\rho_s).
\]
Replace (S4) by the stronger ceiling
\(2c_{\rm av}C_gMh_s<\beta_W\), with (13). This proves the precise
(N2) use through (20). It does not claim the extra numerical assertion
\(\|\bar u_1^{\pm1}\|\le2\) for every arbitrary gauge allowed in the
standalone version of (b). That assertion is stronger than the
consumer's gauge-invariant equality.

All additional conditions (13), (17), (18) and the real-base ceilings
are compatible with I 154950–155038. After the fixed constants,
\(w_s,r_s\) are free positive radii. Every new expression on their
left is a linear form with nonnegative fixed coefficients. Decreasing
both radii meets all finitely many conditions, independently of \(K\).
Neither \(r_g\) nor \(c_u\) depends on the radii then chosen.

### 4.3 An exact failure: the block-constant gauge in (a) and (c)

Radius changes alone do **not** prove the literal formulas at
I 154354–154376 and 154397–154405. Those lines require the acting gauge
to be constant on each block. The missing factor is the Landau-to-axial
gauge \(u\) in (3). Omitting it is different from reversing the order
of two factors. It cannot be repaired by shrinking a positive radius.

Here is a hand counterexample in the same axial convention. Choose a
box with an interior level-one block and one of its tree bonds (b)
parallel to the first coordinate. Work in the diagonal \(SU(2)\)
subgroup, with \(T=\operatorname{diag}(1,-1)\). At fine spacing \(h\)
put, for a real number \(a\ne0\),
\[
 \mathcal U_a(x,x+he_1)=e^{ihaT},\qquad
 \mathcal U_a(x,x+he_\mu)=1\quad(\mu\ne1).                         \tag{21}
\]
Take (a) sufficiently small that \(0<|ha|<\pi\). Every plaquette is
one and the current is zero. Every path between fixed endpoints has
the same abelian parallel transport. Therefore the actual group
averages give the same constant connection at the appropriate block
side: an output bond of side \(s\) has value \(e^{isaT}\) in direction
one. These are averages of the *Landau field*; one must not silently identify
them with the raw datum of its axial copy. Use the normalized inverse
Landau-to-axial map of CMP 102b Proposition 2 and §G (printed pp. 281
and 307). Its hypotheses can be checked before invoking it: on this
fixed finite box the constant potential satisfies the size condition
(19) for small enough \(|a|\), its first and second differences vanish,
and its divergence vanishes in (21). Take the constraint value in (20)
to be \(Q_j(1,hA)\), including the fixed fine shell; these values tend
to zero with \(a\). The current is zero, so the constrained critical
condition holds. The map therefore axializes the field by the
hierarchical trees with the prescribed block-root normalization.
In this commuting example all its phases are scalar
exponentials, equal to one at \(a=0\), and analytic for small \(a\).
On the fixed fine shell use the prescribed normalization. Call the
result \(W_a\), and set the raw outer datum to
\(D_a=-i\log M_{\rm outer}W_a\). Every operation is a finite product,
inverse or identity-chart average, and \(W_0=1\). Thus \(D_a\to0\)
as \(a\to0\), on all determining rows including the shell. For this
fixed finite box it lies in every proposed positive data ball for
sufficiently small nonzero \(a\). No uniform-in-volume estimate is
needed for a counterexample.

The constant potential has zero lattice divergence on the variable
region, hence satisfies the Landau condition \(RD^*A=0\) there.
Its axial copy has the prescribed averages by the definition of
\(D_a\). Its Wilson current is zero, so it solves the constrained
critical equations. The root phases were fixed by the same chart
normalization, not by imposing a second incompatible gauge condition.
It is within the small chart ball. Uniqueness of the normalized small
Landau solution in CMP 102b §G therefore makes (21) the local
\(\mathbf U[D]\). Equivalently, the abelian flat field has zero
Wilson action and its small Landau representative is the constant
potential. The fixed fine shell is part of the datum, so there is no
unstated boundary condition on that potential.

The inner \(U_1(X,M\mathcal U_a)\) is axial. Its value on (b) is
one; the condition is I 130021–130052 and I 38515–38527. If a gauge
\(v\) is constant on that block, then
\[
       \mathcal U_a^v(b)=v\,e^{ihaT}v^{-1}\ne1.                   \tag{22}
\]
The last inequality follows by multiplying an asserted equality by
\(v^{-1}\) and \(v\), since \(e^{ihaT}\ne1\). Thus no block-constant
gauge can give the printed equality. This example works at arbitrarily
small real data and for either sign convention of the gauge action.
It is neither a numerical example nor a residual-gauge counting issue.

For (c), take the same constant abelian connection on the torus,
\(V_0=1\), with a sufficiently small constant real top perturbation
\(B\). It is a flat constrained critical configuration with constant
Landau potential. An interior tree bond of an allowed \(X\) gives the
same contradiction for the Balaban Landau representative. If a different
normalization is intended in §4.31, its identification is an additional
obligation; the representative-independent conclusion established here
is the relative-gauge identity (19). No wrapping geometry is needed to refute the
block-constant requirement; allowing wrapping does not cure it.

The weakest statement needed by the actual (N1) consumer is the pair
of curvature/current bounds obtained from a gauge with
\(\|g^{\pm1}\|\le1.1\). Constancy on blocks is unused in the
inequalities at I 156017–156038. Equations (14) and (19) prove the
stronger corrected identities and the required bounds. For (N2) the
needed statement is exactly (20). Thus the radius issue is repairable,
but a literal “Proof at every use” would conceal a false extra
representative condition in this part of the account.

## 5. The two potential-value citations: CA-II 44422 and 44454

These lines do not use a second nesting identity. They read a bound on
the source's \(H_{\rm src}=H_j(\mathfrak r_v,B^0_u)\), at the
*working* loop datum on the own box. In the bounds below put
\(H=\ell_j^{-1}H_{\rm src}\), the physical one-form. In
level-\(j\) coordinates the fine spacing is \(\xi=\eta/\ell_j\),
so \(e^{i\xi H_{\rm src}}=e^{i\eta H}\); the exponent and path
integral are unchanged by this conversion. Here the domain has level-\(j\) blocks and a graded rim of
levels below \(j\), as specified in II 42806–42810. The bounds actually
read at II 44418–44426 and 44451–44465 are
\[
 \|B^0_u\|_\infty\le {1.2\alpha_{3,j}\over L},\qquad
 \|B^0_u\|_\infty\le1.2\cdot6dMc_1a_{Q_v}t_p,\qquad
 a_{Q_v}\le2K_{\rm loc}\mathsf A_w(\gamma),\quad t_p\le1.          \tag{23}
\]
The actual data are correlated loop data; they are not an arbitrary
ball of radius independent of \(j\). The proof also reads the entire
majorant polydisc \(|B(b)|<|B^{ax}(b)|_\star\), whose supremum is
less than \(\alpha_{3,j}\), at II 44357–44363 and 44473–44483.

### 5.1 Radius and the constant in the value bound

Impose \(\sup_j\alpha_{3,j}<r/2\). Then the entire majorant polydisc,
and the Schwarz disc \(|z|<L/1.2\) at \(zB^0_u\), lie in the chart
of §1. Equation (1) gives
\[
 \ell_{\mathfrak B_j(\mathfrak r_v)}(b)|H(B)(b)|
        \le K\|B\|_\infty .                                    \tag{24}
\]
On a level-\(j\) block this is the required
\(\ell_j\sup|H|\le K\|B\|_\infty\). On a rim block of level
\(i<j\), its left side is instead \(\ell_i|H|\). Replacing
\(\ell_i\) by \(\ell_j\) there would lose \(L^{j-i}\).

The frozen proof does not establish \(K\le B_3\). In particular a
smaller datum radius cannot by itself change its derivative at zero
and make that comparison true. Use \(K_*:=\max\{K,B_3\}\) in the
*new smallness ceilings*, without changing the meaning of the
account's earlier constant \(B_3\):
\[
 \begin{split}
 100C_VK_*\sup_j\alpha_{3,j}&\le1,\\
 220d^2M^2K_*c_1K_{\rm loc}\mathsf A_w(\gamma)&\le1.              \tag{25}
 \end{split}
\]
These strengthen precisely II 43080–43083. All constants precede
\(\gamma\); both suprema tend to zero in the account's order
(II 43061–43071). This is a radius change with no new lower bound
or circular dependence. It proves the needed numerical consequences
with \(K\), without claiming the printed coefficient \(B_3\).

For II 44422 it suffices to apply the stated regauging estimate to the
level-\(j\) block containing the anchor \(y\). By (23)–(25),
\[
 |u_B(y)-1|\le C_VK\|B^0_u\|\le0.012/L<0.002.                  \tag{26}
\]
Thus \(n(u_B(y))\le1.002/(1-0.002)<1.01\), where
\(n(v)=\|v\|\|v^{-1}\|\). This is the only use of the first
citation: the comb gauge and the restriction gauge equal one at
\(y\), giving \(n(g_v(y))=n(u_B(y))\). A bound on the regauging at
every rim point is unnecessary for this step.

### 5.2 The path integral and its actual read domain

The weakest consequence needed at the second citation is
\[
 n(g_v(x))\le2
 \quad\text{at the vertices read by the clauses on }X=X_T.       \tag{27}
\]
The proof of Step 3 (II 44489–44528) reads only this set and the local
stencils in it; its bump containment hypothesis is expressly
\(B(x)\subset X\). It does not read a gauge bound at the artificial
outer boundary of \(\mathfrak r_v\).

Here is the geometry needed for (27), rather than an unweighted
estimate on the entire graded box. The own box surrounds \(X\) by
the margin prescribed in II 34310–34316: \(5/2\) cubes for short
singles and one cube for cores. Here is a direct check of its top
region, using the maximal tower convention I 12713–12728. Put
\(\ell_q=L^q\eta\). At step \(q\), the strict gap removes at most
\(R_1\mathfrak M\ell_{q-1}\), and rounding to the aligned
\(\mathfrak M\ell_q\)-grid can be paid by two further grid sides.
Removing that much gives an admissible smaller rectangle, hence the
maximal member contains it. The total collar is therefore smaller than
\[
 \sum_{q=1}^j(R_1+2L)\mathfrak M\ell_{q-1}
 <{(R_1+2L)M_1\over L-1}\ell_j
 \le{3R_1M_1\over L-1}\ell_j <{M\over2}\ell_j.
\]
The last inequalities use \(\mathfrak M\le M_1\), \(R_1\ge L\),
\(L\ge8\) and the inherited floor \(M\ge2LR_1M_1\) of `mu.md`.
This is a verification of the collar bound, not an assumption that
every admissible tower is maximal. Hence \(X\), the anchor, and the
coordinate hull of \(X\) lie inside the top region of this box.
For a rectangular box, a coordinate-ordered path between two points
of that smaller rectangle stays in it: each coordinate remains
between its two endpoint values. The same statement applies to the
vertices of every stencil required on \(X\). Thus the comb paths
needed here may be chosen in the level-\(j\) region. The side bound
\(2M/t_p\) of II 42826 gives
\(\operatorname{len}_j(\gamma_x)\le2dM/t_p\).
This is also the length used explicitly at II 44438–44439.

On these paths (24) is an unweighted bound in level-\(j\) units.
Multiplying it by their length and using (23) gives
\[
 \int_{\gamma_x}|H|
 \le {2dM\over t_p}K\,(1.2\cdot6dMc_1a_{Q_v}t_p)
 \le28.8d^2M^2Kc_1K_{\rm loc}\mathsf A_w(\gamma)
 <{29\over220}<0.14.                                            \tag{28}
\]
The long-path factor \(t_p^{-1}\) cancels. The units matter:
\(\ell_j|H|\) is multiplied by length divided by \(\ell_j\).
The near-unitary transport bound supplied as hypothesis (a) of the
corollary gives \(n(W(\gamma_x))\le1.45\). The already established
identity \(W^{g_v}=e^{i\eta H}\), read along a path, now yields
\[
 n(g_v(x))\le e^{2\int_{\gamma_x}|H|}\,1.01\,1.45<2.             \tag{29}
\]
For an entirely hand verification of the last scalar inequality,
\(e^t\le1+t+t^2/[2(1-t)]\) for \(0\le t<1\), by bounding each
\(m!\) below by \(2\) for \(m\ge2\). At \(t=7/25\) the right
side is \(1201/900\), and
\((1201/900)(101/100)(29/20)=3517729/1800000<2\).
This proves (27) and therefore the gauge-cost consequence of the
second citation.

There are two literal limits. First, neither citation proves its
particular coefficient \(B_3\) from `mu.md`; (25) pays for the
proved coefficient. Second, II 44438 says “for every \(x\in\mathfrak
r_v\)” while putting its path in \(\mathfrak r_v^\flat\), and
II 44454–44457 writes an unweighted bound on \(H\). Equation (24)
does **not** justify extending that unweighted bound into the graded
rim. No such extension has been proved here. It would require a
further boundary-weighted response estimate, or a separate uniform
bound on the corresponding weighted path integrals. Shrinking a
positive, depth-independent radius does not remove the factor
\(L^{j-i}\). The actual consumer (27) avoids that extension by the
checked interior geometry. Classification: the two **needed scalar
uses carry over after (25)**; the stronger printed whole-rim reading
is not covered by the frozen value proof.

## 6. Source identities, hypotheses retained, and verification limits

The source version is [31a47c543775 of the Sussman–Alpoge project](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775). The files read were the [outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex) and [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex). Line numbers in this note refer to those exact files, not to the outline's numbering. The outline was used for indexed navigation and identification of conventions, not to replace a proof by its sketch.

| Source | SHA-256 |
|---|---|
| Outline | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |
| Frozen [mu.md](mu.md) | `12132e460fb51d0453b62c21f317b49550ce6c524cf8314975cc919e9bd67bee` |
| [mu-gate.md](../gates/mu-gate.md) | `de8219fbe964ceda039cb808e725432453307459ef1f5ccbf003c41b18525237` |

The source navigation packet is `/tmp/mur-ec845e49b/`. It includes the complete literal-hit list and the broader spelling search. The durable mathematical argument and the source identities are here; a search hit or index status is not mathematical evidence. Source passages were read in bounded ranges. Where a source describes a statement as an input, it remains an input here. In particular:

- §2 retains the account's direct input bounds, stage-layer size estimate, and its separately stated sharp composite-conjugator hypothesis. It proves admission and nesting on the full stage parameter range, not that extra hypothesis or the unrelated remainder membership theorem.
- §3 retains the source minimizer's regularity, reality and holomorphy, the complex averaging/comb estimates used at II 35657–35667 and 35716–35747, and the stated weight majorant. It supplies the previously unchecked *uniform inner chart* and the change of action domain. It does not turn a curvature bound alone into a theorem about arbitrary complex fields.
- §4 retains the supplied global background and its real-minimizer identification. General real-base charts and the one-function orbit extension are the published CMP 102b §G/Proposition 9 inputs, recorded explicitly at CA-I 38511–38645. The value of the local function uses the account's invariance under all complex gauges.
- §5 retains the thin-layer corollary's explicit transport and chart hypotheses (II 44335–44364). It proves precisely the value-bound consequences needed there, including their units and read domain. It does not prove every other hypothesis of that corollary.

All new estimates above are hand arguments. Fetching, searches, hashes and text editing served navigation and bookkeeping only; no run, numerical output or symbolic calculation discharges a step. This is one research-text check, not an independent audit or an assertion of retained status. Only `library/mu-radii.md` was created; no editable prompt, frozen proof, gate, account source, ledger or platform instruction was modified.

## Result

The stage-composite uses in **§4.26 and §4.28**, including the graded cover, and **CA-II 35714** are covered after the explicit radius ceilings (8) and (11), in the account's order of constants. Their domains, all determining rows, real uniqueness, fixed-shell restriction and full complex continuation have been checked. The descriptive and status-only citations introduce no further radii.

A literal claim that every printed use is proved would overstate the result. The following stronger readings are **not covered**:

1. **CA-I 154420 and §4.31(a), I 154354–154376:** the acting gauge is required to be block-constant even though the field on the right is the Landau representative. The missing factor is the nonconstant Landau-to-axial factor, not a radius loss. The flat commuting example (21)–(22) refutes this requirement at arbitrarily small data in the Balaban reading. The weakest needed curvature/current comparison, and the stronger corrected relative-gauge identity, are proved in §4.1 on the entire (N1) path.
2. **The adjacent §4.31(c), I 154397–154405, used at I 155387–155429:** the same representative defect remains, including on a nonwrapping box. The corrected identity (19) and the exact numerical cost used by (N3) hold on every permitted domain, including wrapping domains, after (17)–(18). A different intended normalization would need to be specified and identified.
3. **The extra bound in §4.31(b), I 154378–154395:** the assertion that the relating gauge has both norms at most exactly two for *every* allowed gauge is not established by this carry-over. Covariance and a small extra gauge factor give a product bound, without the strict margin that would imply that particular number. The consumer at I 156050 needs only equality of gauge-invariant local functions; (20) proves that equality on its full admitted datum range. This is an adjacent stronger assertion, not another literal (3.38) citation.
4. **The strengthened literal readings of CA-II 44422/44454:** `mu.md` proves a weighted value estimate with constant \(K\), not the particular coefficient \(B_3\) nor an unweighted estimate on the entire graded rim. Equation (24) identifies the exact lost scale factor. After (25), the anchor bound and every path-integral bound actually needed on \(X_T\) are proved by (26)–(29). Extending those bounds to all rim points would require another estimate and is not asserted.

Thus all the identified **needed nesting or scalar consequences** have the carry-over proved above, with the listed representative corrections and the consumer's existing hypotheses. The literal stronger statements in this list must not be reported as proved by a radius change. No scientific status is granted.
