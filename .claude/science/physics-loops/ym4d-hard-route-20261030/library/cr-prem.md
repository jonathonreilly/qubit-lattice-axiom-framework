# CR: source premises of outside re-blocking

Written 2026-11-06 by Codex gpt-6-astra on the laptop. Checkout
`3d38c3c3e4d23b352d6738581d1ed9bbd28ff1a9`. Research text, not an audit.
This note grants no status. No computation discharges a proof step.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, and Tadeusz Bałaban for the averaging and variational constructions.
The conditional ladder proof is Claude's `cr-claude.md`, as repaired in
`cr-r2.md` and the two Codex checks. The arguments below concern its additional
premises. They do not repeat its conditional ladder estimates.

Sources read: `GOAL.md`; the requested parts of `FINISH.md`; all of
`library/prior/cr-claude.md`, `gates/cr-r2-gate.md`, and `library/cr-r2.md`;
the README and relevant neighbouring rows in `library/sa-index/`, including
its obligations and the CA-I 4.12–4.19 index; `library/open-registry.md`,
`library/lit-balaban.md`, and the relevant sections of `library/b98.md`
and `library/b98-iterate.md`. `library/prior/cr-prem.md` and the generic science-workflow
file are absent. The registry's CR row still names `cr-r2`; FINISH row 408
expressly assigns this follow-up on that same result. No separate target is
taken over. Source quotations below give the exact ranges actually read.

`I` denotes `/Users/jonreilly/ym4d-lead/sa/theorem_0_complete_account_raw_I.tex`.
`SA` denotes `YM4_sketch_500.tex` in that directory. Their supplied revision is
`31a47c543775`. That directory has no Git repository, so this revision is
provenance supplied by the owner. The files themselves are the evidence.
Bałaban's papers are unavailable in the permitted scope. Only the account and
the repository's quotations are used. The outline's symmetrised average and
the account's cited CMP 98 average are distinguished below.
The source SHA-256 identities are
`d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` (SA)
and `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` (I).
Hashing records source identity; it verifies no mathematical claim.

The target is I:45085–45106, **“Proof outstanding.”** It assumes an actual
consumer, an outside domain, and a read pair with a point below the slot.
It exports only (a) and (b) of I:44167–44185. T1, AV, R, CUR and AX retain
their stated hypotheses. An additional convention is not a consequence of
those inputs merely because it is convenient.

## 1. (EC): a source test is not necessarily a graph word

I:42981–42984 says **“an elementary closed circuit”** and defines its value
as an ordered product. It does not define “elementary”. I:43113–43127 imports
T1 using those products. In contrast, SA:9623 says:

> “\(\mathcal M(V_{j-1})\) is used on those bonds of \(p'\) that lie in the finer layer.”

These are two different descriptions of the tests. SA:9607 and 9610 specify
the native rows: selected bonds of the level lattices, with
\(M_{\mathbf B}(U)=(\mathcal M^jU|_{\Gamma_j})_j\). A four-sided test in that
description need not be a four-factor word in the independent native data.
The replacement factor is itself an average.

Here is an exact check of the distinction. Use commuting SU(2) data
\(\exp(itH)\), with \(H=\operatorname{diag}(1,-1)\). Work inside the common
logarithm chart. In one averaged edge, select a fine bond crossing the face
between its two endpoint blocks. Choose its transverse coordinate off the
central straight path. Set that bond to \(\exp(itH)\) and all other bonds to
1. The internal contour legs do not cross this face. Of the \(L^d\) translated
straight segments, exactly \(L\) cross the chosen bond: the starting normal
coordinate is free and all transverse coordinates are prescribed. The central
reference path misses it. Thus the formula SA:7065–7071, and the fixed-contour
formula (5) of `b98.md`, give exactly

\[
             \mathcal M(V)(c)=\exp(i t L^{1-d}H).
\tag{1}
\]

For small \(t\), every logarithm here is its displayed commuting logarithm.
An ordered word in independent datum bonds, with this bond as its only
nonidentity input, instead equals \(\exp(intH)\) for an integer \(n\).
Its derivative at zero cannot equal (1), since \(0<L^{1-d}<1\).
This is a counterexample to replacing the native averaged factor by a word
in the native datum bonds. It is **not** a counterexample to CR or a proof that
the undefined graph plaquettes violate (EC). Adding specially defined
interface variables could change the comparison; their constraints would
then need to be specified.

The corrected sufficient input is test stability, rather than a common
intersection point:

\[
 \|T_P(e^{iB}D)-T_P(D)\|\le C_T\|B\|_\infty,
 \qquad C_T=C_T(L,d),
\tag{EC'}
\]

for every **actual** T1 test and the data used by the ladder. This replaces
\(16\) by \(C_T\) in its data-admission estimate.

For a fixed finite source test on a fixed smaller chart, (EC') has a short
proof. Write each exponential and logarithm as its convergent matrix series.
On a closed ball strictly inside the chart, the series for their first
derivatives converge uniformly. Hence each derivative has a finite bound.
There are finitely many paths and operations in a one-step test, depending
only on \(L,d\). The chain rule gives a bound \(C_T\) for its derivative in
the maximum norm. Integrating along \(s\mapsto e^{isB}D\), \(0\le s\le1\),
gives (EC'). Endpoint gauge factors conjugate a closed test and preserve its
norm. The needed common chart and the identification of the ladder variables
with the native variables do not follow from this argument.

Three routes to the literal (EC) identification fail at distinct points.
Geometric dual faces would define a possible set of elementary circuits, but
I:42981–42984 does not choose that cell structure. Expanding the native tests
as words fails by (1). Using AV(e) only bounds tests on fields in the image of
the averaging map; it does not specify the tests or their response to arbitrary
independent datum twists. Thus neither (EC) nor (EC') on the fixed graph
ladders is discharged. The remaining identification is part of the single
actual-system lemma stated in the Result.

## 2. (BP): fixed hierarchy points, and the limit of that match

I:24244–24246 defines **“\(B^j(x)\) ... with centre \(x\)”** on a fixed block
hierarchy. I:24373–24374 says that higher operations are compositions
**“through the block centres”** and **“refer to no sequence of domains.”**
For these native rows, a common block has a common centre. This proves (BP)
for two restrictions of that hierarchy: the centre is a function of the cube,
not of the restriction. The centred lattices are nested by the oddness argument
at I:794–799. No new geometric lemma is needed.

The abstract hypothesis is weaker. I:43055–43059 fixes a determining set
**“with base points ... once and for all”** for each domain, level function and
slot. It does not equate choices at different slots. Its explicit requirement
at I:42999 is just \(z_B\in B\).

Here is a counterexample to deriving (BP) from that requirement. Take two
partitions sharing a block \(B\) containing distinct fine sites \(a,b\).
Assign \(z_B=a\) in one and \(z_B=b\) in the other. Keep both choices fixed.
Every requirement on block levels and tower distances remains unchanged.
Both base-point requirements hold, while (BP) fails. This is a counterexample
to the abstract implication, not an assertion about the native centre choice.

Changing base points is not harmless for the literal common-row equality.
For the flat field \(U(x,y)=g(x)g(y)^{-1}\), covariance and normalization give
the averaged row \(g(z_B)g(z_C)^{-1}\). Set \(g(a)=1\),
\(g(b)=\exp(itH)\ne1\), and \(g(z_C)=1\). The two rows are 1 and
\(\exp(itH)\), respectively. The fine curvature is zero. Thus the proof may
use either the common centre convention or an explicit transport between
endpoint frames. It may not drop both. In the latter version, that transport
must enter the datum identity and its support statement.

For the source hierarchy (BP) is matched. For the abstract graph it requires
the same identification as (R-form); notation alone does not establish it.

## 3. (R-form): the literal row identification fails at a flat interface

I:10175–10178 makes admissibility a **“standing hypothesis”** and restricts R
to \(\{\Gamma_i\}\) or \(\mathbf B_p(X'')\cup\{\Gamma_i\}_{i<p}\).
I:9833–9837 assigns these symbols their meanings in CMP 119, §2. The supplied
quotation of CMP 119 (2.14), at I:92521–92530, is a splicing formula:

\[
 \mathbf B\cup\mathbf B_j(\Omega)
 = (\mathbf B\cap\Omega^{\sim-2})
   \cup[\mathbf B_j(\Omega)\cap(\Omega\setminus\Omega^{\sim-2})].
\tag{2}
\]

I:94792–94796 spells out its provisos: the boundary meets one parent stratum,
the domain is a union of the specified cubes, and the boundary is at least
\(2\mathfrak M\) from the other strata. Formula (2) does not itself define an
average for every pair of face-adjacent unequal blocks.

Compare the actual row definitions. I:42969–42970 puts **“one bond for each
pair of adjacent blocks”** in the graph. SA:9607 instead selects bonds of the
homogeneous level lattice. At a flat interface, take a coarse block of side
\(Ls\) and a complete face covered by blocks of side \(s\). The graph has
\(L^{d-1}\) distinct rows from this coarse block through that face. A native
outward row from its top in that normal direction is one bond of the lattice
of spacing \(Ls\). Its endpoint is the corresponding level-lattice site in
the finer region. These are not the \(L^{d-1}\) adjacent small-block centres.
For \(d=4,L>1\), the row sets differ.

This example can be embedded in arbitrarily thick aligned strata. Enlarge
each constant-level region by any required number of cubes away from this
face. The local row discrepancy remains. Thus admissibility, wide collars
and common centres do not prove the literal (R-form) identity. Adding the
inward-bond variant does not establish that identity either: SA:9625 gives
it additional seam nodes and pinch tests, with a rate specific to that case.
It does not identify those nodes with the graph's single coarse vertex.

The corrected requirement is an **equivalence of constrained problems**, or
a response theorem directly for the graph problem. An equivalence must give
maps between the two data spaces which preserve the constraint fibres, the
Wilson action on the same domain, and the real regular orbit. It must also
give uniform bounds for the data twists and preserve their distance from the
readout, up to fixed losses. Equality of the partitions is insufficient.

This is the main unresolved lemma, not a newly named substitute for a proof.
The three concrete attacks are recorded here.

1. **Identify the rows without changing coordinates.** The flat-interface
   count above refutes that identification.
2. **Compress the extra graph rows by endpoint transports.** A flat field
   allows such transports. At nonzero curvature, two routes differ by the
   enclosed plaquette product. Put \(\exp(itH)\) on one edge of a square and
   1 on its other edges. The two transports differ for every small nonzero
   \(t\). Declaring the extra rows redundant therefore needs an exact
   constraint-fibre identity, not an estimate that they are close.
3. **Apply R merely to the minimum of the level functions.** The minimum
   describes a partition but supplies no equality of row functionals. Also,
   (2) requires a single-stratum boundary. A rectangle whose boundary crosses
   a flat level interface does not satisfy that proviso. The broader first
   case of R can cover an admissible native sequence, but still needs the
   missing constraint-fibre equivalence to cover the graph problem.

These attacks do not refute a possible equivalence or a direct graph response
estimate. They do refute the two shortcuts just tested. No source-matched
application of R to every fixed graph ladder results from them.

## 4. P6: a written anchored bound for the named equal-level average

I:43013–43016 says **“These data are the averages of”** CMP 98 (1.5),
**“composed at interfaces between blocks”** as in CMP 119 (2.14).
Thus its named equal-level prescription is the CMP 98 average.
I:16546–16552 quotes its logarithmic factor and accumulated endpoint factor.
The scale sum in the latter display is
\(\sum_{r<m}L^{r+1}\eta\), not a depth-independent constant before scaling.
SA:7268–7270 states the corresponding anchored factors for the symmetric
average. We do not use either estimate as an unproved lemma here.

For the CMP 98 map, use its fixed-contour formula reproduced in `b98.md` (5):

\[
 \mathcal M(U)(c)=
 \exp\!\left(\sum_{x\in B(y)}L^{-d}
       \log[U(\Gamma_{y,x})U([x,x'])U(\Gamma_{y',x'})^{-1}U[c]^{-1}]
       \right)U[c],\qquad c=(y,y').
\tag{3}
\]

This is the small-chart source prescription being matched. The source's
endpoint normalization is also explicit in I:24276–24289. The proof below
uses (3), not the conclusion of CMP 98 Proposition 6. It does not transfer
that proposition to a different average by citation.

**Lemma.** For the iterates of (3), with their fixed hierarchy endpoints,
there are \(a_*>0,C_6<\infty\), depending only on \(L,d\), such that

\[
 \|\mathcal M^m(e^{i\eta a})(c)-1\|
       \le C_6\ell_m\|a\|_\infty,
 \qquad \ell_m=L^m\eta\le1,\quad\|a\|_\infty\le a_* .
\tag{4}
\]

All fields and endpoint factors in this lemma are real SU(2) fields. We use
the operator norm. Fixed finite-dimensional norm equivalence only changes
the constants if the account's norm is used.

*Proof.* First work at one level, with dimensionless bond potentials \(A\).
Define

\[
 m_y(A)=\exp\!\left(\sum_xL^{-d}\log U(\Gamma_{y,x})\right),
 \qquad U=e^{iA},
 \qquad S(A)(c)=m_y(A)^{-1}\mathcal M(e^{iA})(c)m_{y'}(A).
\]

All paths have a length bounded in terms of \(L,d\). The estimate
\(\|\prod U_b-1\|\le\sum\|U_b-1\|\le\sum\|A_b\|\) follows by
telescoping the product of unitary factors. Choose a fixed \(r>0\) so that
every logarithm in this finite formula lies in its power-series chart for
\(\|A\|_\infty\le2r\). The exponential series and
\(\log(1+Z)=\sum_{n\ge1}(-1)^{n+1}Z^n/n\) converge there with their first
two derivatives on the smaller ball. Thus \(H(A)=i^{-1}\log S(A)\) has
bounded second derivative on \(\|A\|_\infty\le r\), and \(m\) has bounded
first derivative there. These constants involve only the finite one-step
formula. Compactness of that closed ball, or the convergent series
majorants, supplies their finite bounds.

Differentiate at zero. A path product has derivative the signed sum of its
bond potentials. Put \(\sigma_y(A)=\sum_xL^{-d}\sum_{b\in\Gamma_{y,x}}\pm A_b\).
The derivative of the logarithm of (3) is

\[
 \sigma_y(A)+\sum_xL^{-d}\sum_{b\in[x,x']}A_b-\sigma_{y'}(A).
\]

The two factors \(m_y^{-1},m_{y'}\) cancel the two \(\sigma\)-terms.
Each straight segment contains \(L\) bonds. Consequently

\[
 \|DH(0)A\|_\infty\le L\|A\|_\infty,\qquad
 \|H(A)\|_\infty\le L\|A\|_\infty+K\|A\|_\infty^2,\qquad
 \|m(A)-1\|_\infty\le K'\|A\|_\infty .
\tag{5}
\]

The quadratic inequality follows by integrating the second derivative with
weight \(1-t\). Choose \(K,K'\ge1\). This derives the needed special case
of I:24349–24369; no derivative bound is imported from that citation.

For real SU(2) inputs, the small logarithms are traceless skew-Hermitian:
their two eigenvalues are opposite imaginary angles. Thus every \(m\) and
\(S\) above is unitary. Covariance of (3) follows because each relative loop
is conjugated at \(y\), while \(U[c]\) transforms at its two endpoints.
The power series commute with conjugation.

Write the actual iterate as
\(\mathcal M^r(e^{i\eta a})=(e^{iA_r})^{g_r}\), starting with
\(A_0=\eta a,g_0=1\). Covariance and the definition of \(S\) give

\[
 A_{r+1}=H(A_r),\qquad
 g_{r+1}=(g_r|_{\text{next sites}})m(A_r).
\tag{6}
\]

Let \(a=\|a\|_\infty\), \(a_r=\|A_r\|_\infty\) and
\(t_r=a_r/(\eta L^r)\). Equation (5) gives

\[
 t_{r+1}\le t_r+(K/L)\eta L^r t_r^2,\qquad
 \sum_{r<m}\eta L^r={\ell_m-\eta\over L-1}\le{1\over L-1}.
\]

Choose
\(a_*\le\min\{r/4,L(L-1)/(8K)\}\).
If the preceding \(t_r\)'s are at most \(2a\), summing the recurrence gives
\(t_s\le a+4Ka^2/[L(L-1)]\le3a/2\) for the next \(s\le m\).
Also \(a_s\le2a\le r/2\), so (5) remains applicable. Induction proves
\(a_s\le2a\ell_s\) at every step. For the unitary endpoint product in (6),
telescoping now gives

\[
 \|g_m-1\|_\infty
 \le K'\sum_{r<m}a_r
 \le {2K'\over L-1}a\ell_m .
\]

Finally
\(g_m(y)e^{iA_m(c)}g_m(y')^{-1}-1\) has norm at most
\(\|g_m(y)-1\|+\|A_m(c)\|+\|g_m(y')-1\|\).
This proves (4), with \(C_6=2+4K'/(L-1)\). The case \(m=0\) follows
directly from \(\|e^{i\eta a}-1\|\le\eta\|a\|\).

Every recursively read path lies in the two endpoint blocks of the iterate.
Indeed a one-step path lies in its two blocks, and replacing a coarse bond
by its child computation stays in the corresponding parent blocks.
Induction proves the assertion. Extend a local potential by zero if needed.
This gives the same bound on a complete equal-level carrier. \(\square\)

Thus P6 is proved for the equal-level CMP 98 prescription actually named in
I:43015, with its own hierarchy endpoints. Identifying additional graph
endpoint conventions is the issue in §2. This proof supplies no assertion
about an unspecified mixed-level row.

## 5. COMP and COMP(=): prove the composition which the source defines

I:44874 says **“Grant the composition property”**. I:44949–44953 repeats
**“which we grant”**, including **“trivially where the two sets coincide.”**
Neither sentence is a proof of composition for the graph extension.

There is an exact native composition theorem. SA:7127 defines
\(\mathcal M^{q+1}U=\mathcal M(\mathcal M^qU)\). I:24373–24374 specifies
compositions on the fixed hierarchy. Here is the needed precise form.

**Composition lemma.** Regard a retained row as a finite evaluation tree of
one-step averages. Suppose every terminal row in a coarser retained row's
evaluation tree is a finer retained row, with the same endpoints, contour
rule and branch. Then a function \(F\) of the finer data satisfies
\(M_{\rm coarse}=F\circ M_{\rm fine}\). On any common row with the same
evaluation tree, the two functions are equal.

*Proof.* At a terminal vertex, substitute its finer datum. At an internal
vertex, apply its prescribed finite one-step function to the values of its
children. Induct on the finite tree's height. The value after substitution
equals the value from the original configuration at every vertex, hence at
the root. This proves factorisation. A common row has identical leaves and
identical operations, so the same induction proves equality. Nonassociativity
of a group mean is irrelevant: the trees have not been reassociated.
Finally, if \(M_{\rm fine}U=M_{\rm fine}W\), factorisation gives
\(M_{\rm coarse}U=M_{\rm coarse}W\). Every differentiable curve with the
finer datum fixed therefore has the coarser datum fixed. The first variation
of the same action vanishes along that curve whenever it vanishes on the
coarser constraint fibre. This is exactly the restricted-criticality step
at I:44959–44962. \(\square\)

For a native one-level ladder this terminal-row condition has a concrete
sufficient geometry. Every newly retained level-\((q+1)\) row reads a double
block of that level. If the finer ladder is entirely level \(q\) on that
double block, it retains every row needed by the last one-step average.
Old lower-level rows retain their original evaluation trees. Therefore COMP
and COMP(=) hold. A gap greater than \(2\ell_{q+1}\) from the new top region
to the finer ladder's levels below \(q\) and to its exterior is a sufficient,
conservative way to ensure this double-block coverage. The bound follows
because a point of either block of that carrier lies within
\(2\ell_{q+1}\) in sup-distance of its top endpoint's block.

This proves the source mechanism, including its boundary requirement. It
does not assert that the graph's interface formula is this tree. In
particular, spatial locality alone does not imply COMP(=). Two functions
may read the same carrier and differ. For example, the direct transport from
one corner of a square to the next and the transport along its other three
sides have the same endpoints, are normalized and gauge covariant, and read
the same square. Put \(\exp(itH)\) on an edge used only by the second route.
Their values are 1 and \(\exp(\pm itH)\). Hence identical carriers do not
identify their functions, even arbitrarily close to the identity.

The correction needed by CR is equality of the actual row functions on
common rows and terminal-row closure for every changed row. Source
composition proves these once that identification is made. The proof does
not justify taking the account's COMP grant as one of T1, AV, R, CUR or AX.

## 6. (G-c): widths do not supply the required cube grid

I:43520–43524 says, in its inside-box argument, **“Each region of constant
intermediate level is at least one layer of cubes of side \(M\ell\) wide.”**
I:53641–53660 defines the compatible, origin-based partitions and the cells
of side \(MR_i\ell_i\). I:53779–53785 is more specific:

> “For \(i\in I_M\) the member \(Z''_i\) is a union of level-\(i\) \(M\)-cubes”;
> the members are “separated by one layer”.

Here \(I_M=\{k_0+1,\ldots,k\}\). The same passage defines the lower members
using old domains, and keeps \(Z_i\) unchanged for \(i\le h\).
I:53836–53837 explicitly says of the older members' cell-union hypothesis
(G): **“Hypothesis (G) is not assumed ... unless this is said.”**
Thus the prepared sequence supplies genuine geometric information. Its
upper-range statement is not a statement about every older member.

Two elementary facts give the part of (G-c) which this information supports.
If a set is a union of cubes of side \(M\ell_i\), and \(M/M_1\) is an integer,
each cube subdivides into \((M/M_1)^d\) origin-aligned cubes of side
\(M_1\ell_i\). Its complement is a union of the same grid cubes, with the
usual lattice convention assigning boundary sites to blocks. Restricting
either set to a read domain preserves a global extension: use the original
set. Also, restricting both sets in a distance infimum can only increase
their separation. These assertions follow directly by subdividing each
coordinate interval, and by taking infima over subsets. They require no
response estimate. The power-of-\(L\) size convention allows the later
choice of \(M\) to be a multiple of \(M_1\).

These facts apply whenever the consumer superlevel sets are the restrictions
of those particular prepared sets or their complements. They do not identify
the sets for us. The class formulas I:43359–43367 give the exact reduction:

| Class | Superlevel set which must be matched |
|---|---|
| K1, \(c_E=j\), \(p\le j\) | No read pair satisfies \(\{c_E<p\}\ne\varnothing\). CR has no such case. |
| K2, \(c_E=\min(o,j)\) | For \(i\le j\), exactly \(\{o\ge i\}\cap X''\); for \(i>j\), empty. |
| K3, \(c_E=o\) | Exactly \(\{o\ge i\}\cap X''\). |
| K4, \(c_E=\mathsf b\) | Exactly \(\{\mathsf b\ge i\}\cap X''\). |
| K5 | The preceding sets for each constituent read, on that read's full domain. |

Truncation at \(j\) cannot create a narrower nonempty width. Indeed, for
\(i<j\), both sets defining \(W_i(\min(o,j))\) equal those for \(o\);
for \(i\ge j\) the upper set is empty. Thus a global old-level extension and
its widths would settle K2 and K3 together. K4 needs the prepared-level
extension, including its lower range. The table is a set identity, not an
assumption of that extension.

There is a simple counterexample to deriving the cube clause from width
alone. Take a large periodic lattice, with no boundary tower to consider.
Put \(c=2\) on a thick slab whose boundary coordinate is
\((NM_1+1)\ell_2\). Put \(c=1\) in thick adjacent slabs, of width \(w\)
an integer multiple of \(\ell_2\), and \(c=0\) elsewhere. Choose all slabs
and the period much larger than \(w\), and \(w\ge M\ell_1+2\ell_2\).
Assign boundary sites by half-open blocks. Each constant-level region is
a union of its own level blocks. Neighboring levels differ by one.
The only nonvacuous intermediate width is \(W_1(c)\), and it is at least
\(w-\ell_2\ge M\ell_1\). But \(\{c\ge2\}\) cuts through an
\(M_1\ell_2\)-cube, for \(M_1>1\). No extension can repair this internal cut
when the read domain is the whole torus. This refutes the inference from
wide level strata to the aligned-extension clause. It does not describe
an actual generated history.

The corrected geometric statement must identify the old and prepared
superlevel sets on each full read domain with a specified global nest on the
response theorem's cube grid. It must retain the gaps of that nest.
Three attempted ways to obtain this universal statement stop at different
places. The width sentence cannot supply alignment, by the slab example.
The prepared-sequence statement supplies upper members, but its own lower
range is different. Finally, an inheritance proof needs the weaker
aligned-cube property at its initial stage and after every preceding
operation. The displayed upper prepared sequence does not supply that
induction. Substituting the stronger cell-union hypothesis (G) would assume
information the source explicitly withholds. Its absence does not disprove
the weaker (G-c). The outside restriction could also remove the lower members,
but that requires an exact identity for its superlevel sets. The local
matches above do not establish that identity for every K2–K5 outside read.

## 7. (G-t): the native tower margin is sufficient; the abstract rule is not

I:32840–32851 distinguishes the two block sizes:

\[
 M_1=R_\star'\mathfrak M,\qquad R_\star'\ge R_1,\qquad R_1\ge L.
\tag{7}
\]

Here \(\mathfrak M\) is the propagator block size and \(M_1\) is the
CMP 119 block size. I:32871–32883 quotes the two native rules. In physical
units they are

\[
\begin{array}{ll}
\mathfrak r_1:&
 \Omega_i\text{ is a union of }\mathfrak M\ell_i\text{-cubes},\quad
 d(\Omega_i^c,\Omega_{i+1})>R_1\mathfrak M\ell_i;\\
\mathfrak r_2:&
 \Omega_i\text{ is a union of }M_1\ell_i\text{-cubes},\quad
 d(\Omega_i^c,\Omega_{i+1})\ge M_1\ell_{i+1}.
\end{array}
\tag{8}
\]

For the tower function defined by these superlevel sets, extended by \(-1\)
off \(X''=\Omega_0\), the sets in its width are exactly
\(\{t\le i-1\}=\Omega_i^c\) and \(\{t\ge i+1\}=\Omega_{i+1}\).
Thus \(\mathfrak r_2\) gives

\[
                       W_i(t)\ge LM_1\ell_i.
\tag{9}
\]

This includes \(i=0\), hence includes the exterior boundary. No claim about
only an interior contour is being substituted for it.

The comparison with the propagator condition has a direct proof. Subdivide
each \(M_1\ell_i\)-cube into \(\mathfrak M\ell_i\)-cubes, using (7).
For consecutive tower sets, (8) gives

\[
 d(\Omega_i^c,\Omega_{i+1})
 \ge LM_1\ell_i
 =LR_\star'\mathfrak M\ell_i
 >R_1\mathfrak M\ell_i.
\tag{10}
\]

The last inequality uses \(L>1\) and \(R_\star'\ge R_1>0\).
This proves the native early margin. It does not rely on later enlargement
of \(M\), and it avoids confusing two block sizes both called \(M_1\) in
different papers. Rule \(\mathfrak r_1\) already states the required native
propagator gap, but need not satisfy the stronger numerical form (9).

Use one metric throughout (8)–(10). I:32835–32837 calls it lattice distance;
SA:9596 uses sup-distance for the admissible sequences. If the former is
the ambient shortest bond-path distance, then
\(d_\infty(x,y)\le d_1(x,y)\le d\,d_\infty(x,y)\).
The upper bound follows by summing at most \(d\) coordinate differences.
Taking infima preserves these inequalities. Hence a lower \(d_1\)-gap
only gives that gap divided by \(d\) in sup-distance. When those conventions
are mixed, the sufficient early choice is
\(LR_\star'>dR_1\), rather than the bare \(LR_\star'>R_1\).
The source's large-\(L\) choice \(L\ge15\) at I:43575 and \(d=4\), together
with (7), supplies this stronger inequality. This settles the margin for
the native \(\mathfrak r_2\) tower in either convention. For a differently
stated response gap, its numerical threshold must be substituted explicitly.

The abstract tower at I:43001–43005 instead gives the implication

\[
 d(x,(X'')^c)\ge2M_1\ell_m\quad\Longrightarrow\quad t_{X''}(x)\ge m.
\tag{11}
\]

It is an interior lower bound on \(t\). It is not an upper bound near the
boundary. Here is a counterexample to obtaining (9) from (11). Let \(X''\)
be one level-\(k\) cube, put \(t=k\) and \(c=k\) everywhere on it, and use
the uniform level-\(p\) partition for each slot \(p\le k\). All these cubes
are aligned and every adjacent level difference is zero. Implication (11)
holds wherever its antecedent holds. But \(t_{\ge1}=X''\), while
\(t_{\le-1}=(X'')^c\). Their distance is one fine spacing under the lattice
convention, or zero for closed geometric cubes. It is smaller than
\(LM_1\eta\). Thus (G-t) does not follow from the abstract determining-set
hypothesis.

For CR the correction is to identify \(t_{X''}\) with the actual native
tower rule, and to use that rule's cube size and admissibility distance.
If it is \(\mathfrak r_2\), the proof above supplies the requested margin.
Three other routes fail: reversing (11) fails by the cube example;
enlarging the consumer size \(M\) leaves this boundary gap unchanged; and
calling both constructions a tower supplies no equality of their
superlevel sets. No cited line identifies all fixed ladders of §4.12 with
the native towers of (8). That identification remains part of the
actual-system lemma.

## 8. (S): source control on the whole read, not only at its output

I:43223–43225 says **“The healed level \(\mathsf n(x)\) equals \(k\) on
\(Z\cup\Omega_k^{\mathrm{old}}\).”** I:43295–43299 gives the source clause:

> “on the part of \(Y_4\) where \(\mathsf n=k\)”,
> \(\left|\partial\bar U(\mathfrak p)-1\right|
> <\tilde\alpha_{0,k}\eta^2\).

These two lines prove the source bound on every full plaquette in
\(Y_4\cap(Z\cup\Omega_k^{\mathrm{old}})\). The minimal replacement for (S)
is that the same bound holds on every plaquette of the full action domain
\(X''\). It suffices that

\[
 X''\subset Y_4,\qquad \mathsf n=k\text{ on all of }X''.
\tag{S'}
\]

The union condition in (S) is one sufficient way to prove (S'). The quoted
definition asserts the value of \(\mathsf n\) on that union. It does not
assert the converse needed to deduce the union condition from (S').
A bound only on
\(X''^{\sim2}\), the output region, does not suffice. AV and T1 read the
whole domain in this argument.

There is a concrete source match beyond the small admissible box.
I:93534–93536 defines \(C^\sharp\) by adding
\[
 m_\sharp=\lfloor(\check R_k-1)/2\rfloor
\]
layers of \(M\)-cubes to a component \(C\). I:93601–93604 says the new
determining set is **“of level \(k\) on all of \(C^\sharp\)”**, and permits
restriction to every \(Y_4\subset C^\sharp\).
I:96084–96086 specifies the filing domains \(Y_4\subset C^\sharp\).
Here \(C\) is a component of \(\Lambda_k^c\); the letter \(Z\) in that
section denotes a class of components, rather than the single component
called \(Z\) in §4.12.

For completeness, the geometric containment used here has a direct proof.
The cells have side \(a=M\check R_k\); see I:20443–20448.
Two different touching-components have no touching pair of cells.
For two cells with indices \(v,w\in\mathbb Z^d\), failure to touch implies
\(|v_\mu-w_\mu|\ge2\) for some coordinate. Every point of one cell is then
at sup-distance at least \(a\) from every point of the other in that
coordinate. Taking the minimum over the finitely many cells gives
distance at least \(a\) between different components. Adding \(m_\sharp\)
layers of \(M\)-cubes moves any point by at most \(m_\sharp M<a\) from
the original set. This follows coordinate by coordinate, one layer at a
time. Therefore \(C^\sharp\) meets no other component of \(\Lambda_k^c\).
It follows that

\[
                  C^\sharp\setminus C\subset\Lambda_k
                       \subset\Omega_k^{\mathrm{old}}.
\tag{12}
\]

The last inclusion is the old label nesting printed at I:53758–53760.
Consequently every full read contained in \(Y_4\subset C^\sharp\) satisfies
(S), after identifying this \(C\) with the component under treatment.
This rebuilds the separation step used in I:96110–96115; its citation is
not the proof. The direct source-tube statement also supplies (S') on
these domains.

The same full-domain argument applies to a read in \(B_5\), or in a cleaned
collar inside \(Z\), provided its source filing domain is \(Y_4\).
For example, I:53807–53810 defines the collar
\(R_n=Z_{j+1}\setminus Z''_{j+1}\) **“inside \(Z\)”**.
If \(X''\subset R_n\cap Y_4\), then every point of \(X''\) is in \(Z\cap Y_4\);
the two quoted source lines prove SRC on it. The proof is valid for K2
and K3 old-level reads and for K4 prepared-level reads whenever that full
containment holds. K1 has no below-slot case. K5 inherits the conclusion
for each of its full constituent reads.

This argument does not turn a localization statement about a term into a
statement about all data it reads. I:43347–43351 explicitly quantifies over
**“every sub-domain \(X''\subset X'\) of its class of domains”**.
I:93595–93606 likewise defines a source tube separately for each filing
domain; it does not say that all filings lie in one \(C^\sharp\).
As a warning against an incorrect substitution of domains, I:77033–77038
places the full reads of its pieces in an enlarged \(Y_4^+\). A containment
in such an enlargement is not a containment in the original \(Y_4\).
This is not an identification of that section's pieces with all the
consumers of CR.

Three attempted extensions to every outside read fail. First, knowing that
a domain meets a healed collar does not place its other points there:
adjoin a path and a cube outside the collar to obtain an explicit
counterexample to that set implication. Second, (12) settles a single
collared-component source domain, but does not place every filing domain
in it. Third, source curvature on a smaller box cannot be extended by
locality. Put \(\exp(itH)\) on one bond of a plaquette outside that box and
1 on every other bond, with the bond far enough away that no plaquette
of the box uses it. All source plaquettes in the box are flat, while the
outside plaquette has nonzero curvature. These are counterexamples to the
two proposed extensions of local information. Neither is asserted to be
an admissible source datum on a larger filing domain.

Thus (S) is proved on the full source domains just matched, including
\(C^\sharp\), and no all-consumer extension has been proved. The missing
assertion is full-read coverage for the actual outside consumers, not a
pointwise estimate on their output locations.

## Result

**Open actual-system lemma.** CR (a) and (b) are **not proved here from the
account's own T1, AV, R, CUR, AX and determining-set hypothesis**.
The obstacle is the application to the account's actual systems, not the
conditional ladder estimate.

The precise remaining assertion is as follows. For every outside K2–K4
read pair of I:45085, and every intermediate ladder level, the fixed
constraint system of §4.12 must have a native representation to which R
applies, or a directly proved response theorem of the same strength.
The representation must preserve the action, constraint fibres and regular
real orbit, identify the actual T1 tests, and give the twist and support
bounds used by the ladder. Common rows must have identical endpoint frames
and identical averaging functions. Its level nests and full source reads
must satisfy the native gaps and source bound on the entire action domain.
K5 requires this assertion for each constituent read. K1 contributes no
below-slot case.

Three distinct attacks on the load-bearing constraint-system part failed
in §3: literal row identification fails at a coarse/fine face; compression
by endpoint transports is obstructed by nonzero loop holonomy unless an
exact fibre identity is supplied; and applying R just to a minimum level
function supplies no such identity and can violate the boundary proviso
of the splicing formula. This is the stopping lemma. No impossibility
theorem for it is claimed.

The written positive results are narrower and explicit. Equation (4)
proves P6 for the named equal-level CMP 98 map at its hierarchy endpoints.
The evaluation-tree proof gives native COMP and COMP(=) whenever the
finer retained data close the coarser computation. Equations (7)–(10)
settle the native CMP 119 tower's early response margin. Equation (12)
settles source coverage for every full read in the collared-component
source domain. The counterexamples forbid replacing these matches by
the weaker abstract statements. They do not refute CR.

No new unconditional CR implication follows by assembling only those
positive results. In particular, the quantified representation and
full-read assertion above has not been discharged. This note is a
partial premise result with an explicit stopping lemma, not a completed
proof of the requested proposition.

## 9. Clause (c) and the real-factor conclusion

I:43402–43405 defines the two target radii. At \(n=k\) they reduce to
\(\vartheta_E\alpha_k\eta^2\) and
\(\vartheta_E\alpha_k\ell_p^{-1}\).
I:44172–44175 gives the corresponding upper bounds in (b):
\(2L^2B_3\alpha_k\eta^2\) and
\(2L^3B_3\alpha_k\ell_p^{-1}\).
Since \(\alpha_k>0\), comparison of these bounds with strict target
inequalities requires, respectively,

\[
                 \vartheta_E>2L^2B_3,\qquad
                 \vartheta_E>2L^3B_3.
\tag{13}
\]

Decreasing the coupling does not repair this comparison: its factor
\(\alpha_k\) cancels. If only positivity of the coefficient is supplied,
the proposed numerical implication has a counterexample. Choose that
coefficient smaller than the corresponding constant and a nonnegative
scalar equal to the upper bound. The scalar satisfies (b)'s inequality
and fails the target inequality. This is not a counterexample realized
by a minimiser or an identified consumer coefficient.

I:43425–43434 supplies a coefficient floor for \(n<k\), and at \(n=k\)
for K4 in \(B_5\). I:43437–43440 restricts the assertion that all level-\(k\)
points lie in \(B_5\) to
**“\(\mathfrak Q\subset Z''_k\cup B_5\)”**.
Those lines cannot supply (13) for an arbitrary outside read.
Thus three routes to extending the inside comparison fail: small coupling
cancels out; the below-\(k\) floor omits \(k\); and the inside-box
classification has a hypothesis which an outside domain need not satisfy.
A sharper estimate at those level-\(k\) points, or an actual consumer
coefficient bound there, is still required. The statement of CR at
I:45085–45106 itself exports only (a) and (b).

I:44803–44843 states the real-factor corollary **inside admissible boxes**.
It expressly assumes both the slot conclusion and equality of each
composite's real factor with \(\bar U\) off the core. The exact transfer
under those hypotheses is elementary. Fix one consumer and one full read.
If its real factor equals \(\bar U\) throughout that read, locality gives
identical data for that same determining map. The two minimisers are the
same T1 orbit. Gauge covariance preserves the plaquette and current norms,
so the established slot bounds transfer. Apply this argument to each of
the four factors and every read. It uses equality on the full read and
the same determining map; equality of fields only at an output point
would not suffice.

This proves the transfer implication. It does not supply the missing
outside slot conclusion or the required actual-domain identifications.
No outside real-factor corollary is obtained here.

RESULT: CR (a) and (b) remain unproved from the stated account inputs; the note proves the specified native premises and stops at the actual-system lemma after three failed attacks. Clause (c) and the outside real-factor conclusion remain open.
