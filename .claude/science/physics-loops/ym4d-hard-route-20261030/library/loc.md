# Proof lane LOC: localization of curved admitted data

Provenance: Research text at checkout `1fe9e114b5cf4265d2631d839b43c62a8530c2c1`, prepared by Codex for the LOC-flat task on 2026-11-05; no audit or retained status is asserted. Source material from the Yang–Mills outline and complete account is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, at upstream revision `31a47c543775`. The pre-existing local `loc.md` is preserved at `/tmp/ym4d-loc-1fe9e114b/loc-before.md`.

## Scope and source record

The target is DOM Lemma 12, with the right-trivialized path norm of DOM Lemma 11. The output must preserve the same determining system and the exact local rows. A new boundary problem alone does not meet that target. The quantitative complex requirement is DOM Lemma 14, when used by ST1 FC7. This note changes no frozen consumer or status file.

The previous file at this path concerned locality of formed slots through later steps, a different LOC interface. Its content remains recoverable from this path at commit `1fe9e114b`, as well as from the saved copy. Replacing the requested output file makes no scientific disposition of that earlier note.

Sources are pinned at the revisions in the provenance line. The outline was fetched once to `/tmp/sa_ym4.tex` (32,992 lines; SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`). The complete account was fetched once to `/tmp/sa_ca_I.tex` (166,711 lines; SHA-256 `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`). Retrieval and hashes supply source identity only.

The index was consulted before the source excerpts. The relevant entries are outline chunks 09 and 16 and their rows in `sa-index/obligations.md`; the complete-account index is `sa-index/ca-4.12-4.19/`. Bounded source checks:

* SA 9660–9695 states the regular critical orbit, the two axial conventions, the cube gauge, and the raw-datum continuation. The local gauge at 9684 requires an enlarged cube and small side times regularity.
* SA 9776–9789 defines localization using a **joined sequence**. Its collars lie in single layers. The comparison allows a collar-length-dependent constant. SA 9913 sketches alignment using the defect of lifts. This is a different interface from a local datum on the unchanged global system.
* SA 17575–17585 gives the quiet-box geometry. At 17585 the stage references are localized, while the separate prepared-box extension has the stated `CM^2` curvature loss. That extension sketch supplies neither the present relative path nor the quantitative holomorphic section.
* DOM was read in full. Its pure-gauge extension/path is retained. Its three curved-data failures are the starting point, not three new attacks in this note.
* CP12 §4, PR-lay Q and Lemma 6, GEOH's class/preparation/Lift specifications, ST1's LOC/ST-test, CV, F6 and FC7, and IN1's rows 1–10 with Amendment 1 fix the working interfaces. Their named imports remain imports.

CA-I 49495–49515 and 49531–49547 separate gauge supply from the operator implication. CA-I 54986–55010 explicitly assumes the stage theorem. These were checked after reading the neighbouring index entries in chunks 06 and 10. The outline's joined-sequence comparison is **sketched** at SA 9913. The stage construction at SA 17585 uses references “formed with backgrounds localised in $X$”; it does not give the rule requested here. This note attempts a step of our DOM interface, not a correction of their text.

The local literature check also read Bałaban's CMP 99 (1985), 389–434, supplied OCR lines 420–455. Its (3.35) assumes local witnessing gauges. The OCR is not used to discharge a formula. The explicit working statements are PR-lay Q and CP12 (8), (12)–(14).

## The exact path question

Fix an actual stage geometry and its determining row set \(\Gamma\). Let \(E\) be the rows supplied by \(D_+|_{X^\sharp}\). Let \(P\subset E\) be all rows within distance \(R_\sharp/2\) of the full stage carriers. Inclusion of the complete protected reads in \(E\) is required. A row is an oriented group variable, not a Lie-algebra coordinate fixed along a long path.

Write \(\mathcal A_{\rm in}\) for the admitted real input class of DOM Lemma 12, with the actual (56), (58) tests. Write \(\mathcal A_{\rm path}\) for the real class admitted in DOM Lemma 11: the **same determining system**, with S, the derivative estimate, regular uniqueness and consistent CV readout throughout. Keep every condition belonging to that class. We do not add (58) along the path merely because it is required at its endpoints. If the specified path class also imposes those tests, they remain imposed.

The path norm is
\[
 v(D_s)=\max_{c\in\Gamma}
       \left\|i^{-1}\dot D_s(c)D_s(c)^{-1}\right\|.
 \tag{L1}
\]
A bound on the derivative of a principal logarithm is not a substitute for (L1).

**Necessary consequence of LOC-flat.** If its local rule and paths exist with bound \(C_{\rm path}\), then any two members of \(\mathcal A_{\rm in}\) agreeing on \(E\) can be joined inside \(\mathcal A_{\rm path}\), fixed on \(P\), with speed at most \(2C_{\rm path}\).

*Proof.* Locality gives the same endpoint \(D^\sharp\) for both inputs. Follow the first path to that endpoint, then reverse the second. Allocate half of \([0,1]\) to each path. Reversal preserves speed and this reparametrization multiplies it by two. Both pieces have the same values on \(P\). Their concatenation is piecewise \(C^1\) and admitted. No logarithm across the junction is needed. \(\square\)

This is a necessary condition, not an equivalence. It does not construct a holomorphic section of restriction to \(E\).

## Attack 1: a massive collar gauge with the cell scale retained

This attempt strengthens the earlier clamping attempt by keeping its diameter factors and testing the final coupling ceiling. It also checks the nonlinear cutoff directly.

Put \(\ell=\log\theta_t\). On a single layer suppose a supplied enlarged cube has side
\[
 S\le C_{\rm box}MR_t,\qquad
 R_t\le L\ell^r,\qquad
 \epsilon_t\le C_\epsilon e^{-\ell/2}\ell^p.
 \tag{L2}
\]
Here \(p\) and the displayed constants are fixed; \(C_\epsilon\) may include the later test amplitude. For any fixed integer \(a\ge0\),
\[
 S^a\epsilon_t
 \le (C_{\rm box}LM)^a C_\epsilon
                 e^{-\ell/2}\ell^{p+ar}\longrightarrow0.
 \tag{L3}
\]
The convergence is uniform for \(\ell\ge\log X_0\) as \(X_0\to\infty\).

*Proof.* Choose an integer \(n>p+ar\). The exponential series gives
\(e^{\ell/4}\ge(\ell/4)^n/n!\). The right side of (L3) is bounded by a fixed multiple of \(e^{-\ell/4}\ell^{p+ar-n}\), which tends to zero. \(\square\)

Thus a polynomial loss in the cell side alone is not a reason to abandon this route. IN1 permits the final ceiling to depend on \(M\). It does not permit an early returned constant to grow with \(M\), or a ceiling to depend on the torus volume.

**What the massive gauge supplies.** If PR-lay Q applies on this whole enlarged cube, it gives an initial gauge with
\[
       |A_1|,\ |\nabla A_1|\le C S\epsilon_t
 \tag{L4}
\]
in the layer's units. The curvature and current bounds of CP12 (8) must also hold there. Take \(\xi=1\) in CP12, and \(a=C'S\epsilon_t\). Equation (L3) puts \(a\) below its fixed contraction threshold. Its fixed-point map is
\[
 \lambda=(-\Delta_\eta+1)^{-1}1_{Q'}
 \left[-\Psi_1(\lambda)^{-1}
       \{\Psi_2(\lambda)\operatorname{div}A_1+S(\lambda)\}\right].
 \tag{L5}
\]
The resolvent has norm bounded independently of the mesh in the value/first-difference norm used there. On a ball of radius \(Ka\), its forcing is bounded by \(C(a+(K+1)^2a^2)\), and its Lipschitz constant by \(C(a+Ka)\). Choosing \(K\) first and then \(a\) gives a contraction. Consequently the gauge correction and the resulting potential have size at most \(C''S\epsilon_t\). No iteration through the number of fine sites occurs.

For a holomorphic input \(A_1\) on a complex ball where these same estimates hold, the iteration is holomorphic. Its iterates converge uniformly with a geometric error bound. Applying the one-variable Cauchy integral on each coordinate line to that uniform limit proves holomorphy of the limit. This only proves holomorphy **after an analytic initial gauge and its ball have been supplied**.

**The cutoff estimate, by hand.** Work in any one supplied real gauge, with \(U(b)=e^{i\eta A(b)}\), \(\eta\le1\), \(|A|\le a\), and
\(\eta^{-2}|\partial U-I|\le\epsilon\). For a scalar cutoff \(0\le\chi\le1\), suppose \(|D^+\chi|\le K/w\). For sufficiently small fixed \(a\),
\[
 \eta^{-2}|\partial(e^{i\eta\chi A})-I|
       \le C\bigl(\epsilon+a/w+a^2\bigr).
 \tag{L6}
\]
All four links and their difference stencils must be supplied.

To prove (L6), expand the four exponentials on a plaquette. The linear term is \(i\eta^2 dA\). The sum of terms of degree at least two is bounded by \(C\eta^2a^2\). This follows by majorizing the product series by \(e^{4\eta a}-1-4\eta a\). Thus \(|dA|\le\epsilon+Ca^2\). The exact forward product rule gives
\[
 (d(\chi A))_{\mu\nu}(x)
 =\chi(x)(dA)_{\mu\nu}(x)
  +(D^+_\mu\chi)(x)A_\nu(x+\eta e_\mu)
  -(D^+_\nu\chi)(x)A_\mu(x+\eta e_\nu).
\]
Its norm is at most \(\epsilon+Ca^2+2Ka/w\). Apply the same exponential-product estimate to \(\chi A\). This proves (L6), with constants independent of \(\eta,S,M\). It also proves it for \((1-s+s\chi)A\), uniformly in \(s\in[0,1]\).

In that fixed gauge the latter path has exact right-trivialized bond velocity
\[
 i^{-1}\partial_s e^{i\eta(1-s+s\chi)A}
                 e^{-i\eta(1-s+s\chi)A}
       =\eta(\chi-1)A.
 \tag{L7}
\]
Undoing a fixed real gauge preserves its norm. With \(a\le CS\epsilon_t\) and \(w\ge cS\), (L6) is bounded by
\(C'(\epsilon_t+S^2\epsilon_t^2)\). Equation (L3) makes this at most a fixed multiple of \(\epsilon_t\). Equation (L7) is also uniformly small. These are useful local estimates for curved fields.

**Attempted repairs and exact failure.** Four distinctions prevent these estimates from proving LOC-flat.

1. The hypotheses concern one supplied cube and one initial gauge. CP12 starts from that gauge. A cell-sized annulus can surround the missing core or cross several layers. The gauges recorded on complete small cubes do not supply (L4) on a containing cube through that core. Filling the missing cube to invoke Q would assume the extension being sought.
2. Applying (L5) to \(U_+=\Phi(D_+)\) does not make it a local datum rule. The restriction of \(U_+\) to the collar is itself a function of global data. The outline's joined problem is a possible local replacement, but it changes the determining sequence. Its defect-of-lifts comparison does not identify a new datum on the original system with exact agreement on every row of \(E\).
3. A bound \(C'\epsilon_t\) does not preserve an unchanged threshold \(T\) from an input only known to satisfy \(<T\). Shrinking the coupling shrinks both sides by the same factor. For example, \(u=3T/4\), \(v=3T/2\) satisfy \(u<T\) and \(v\le2u\), but \(v>T\) for every \(T>0\). This route needs verified slack or a threshold-preserving extension, with the actual loop indices. None was obtained.
4. Even with all collar inputs supplied, (L7) describes a path on that gauge box. It is a global path from \(D_+\) only if the exterior has already been put in a compatible global chart. A small collar does not do this. Applying the same construction on successively larger exterior boxes replaces \(S\) by an unrestricted volume length; (L3) no longer supplies a common coupling ceiling.

There is also no uniform raw-datum chart from ordinary holomorphy alone. A gauge built by a path product can contain
\(q_n(z)=(e^{iz\sigma_3})^n=e^{inz\sigma_3}\). Its derivative at zero has norm \(n\), and \(\|q_n(iy)\|=e^{n|y|}\). Each factor and product is holomorphic. This disproves a uniform bound for this product construction, not for every possible localized rule.

The cell-scale smallness estimate succeeds. The local-to-global admitted deformation does not.

## Attack 2: deform through the actual CV representative

This attempt uses CV itself, rather than a global tree gauge. It first tests whether its gauge homotopy changes the datum at all.

For a node-fixing residual gauge \(g\), covariance of the actual average gives
\[
 M_{\mathbf B}(U^g)(c)
   =g(c_-)M_{\mathbf B}(U)(c)g(c_+)^{-1}
   =M_{\mathbf B}(U)(c).
 \tag{L8}
\]
CV constructs precisely such a residual gauge. Its recursion fixes the nodes and changes only the nonnodes. A path of residual gauges therefore gives a **constant datum path**. It cannot remove any remote curved datum.

Allowing arbitrary node gauges does not fix this. Along
\(D_s(c)=q_s(c_-)D(c)q_s(c_+)^{-1}\), every closed datum-loop product is conjugated at its base. Its trace is fixed. On a remote single-layer patch put a small link \(e^{i\alpha\sigma_3}\), and set neighbouring links to the identity. A neighbouring plaquette has trace \(2\cos\alpha\). Replacing \(\alpha\) by \(2\alpha\) changes that trace. Choose \(0<\alpha<\pi/4\) smaller than half every affected admission threshold. Both assignments have arbitrarily small, nonzero local curvature and can agree with the same datum near \(E\). Gauge motions alone cannot send both to one endpoint. This is an obstruction to the gauge-only construction, not to general admitted paths.

**A physical interpolation after CV.** The next attempt was to scale link logarithms in the selected representative. Even a flat input defeats preservation of arbitrarily small curvature by this rule. Set
\[
 X=i\alpha\sigma_1,\qquad Y=i\alpha\sigma_2,\qquad
 Z=\Log(e^Xe^Y),\qquad 0<\alpha<1/10.
\]
The four oriented links \(e^X,e^Y,I,e^{-Z}\) have plaquette product \(I\). They can be assigned by vertex values on this square and extended as an exactly pure-gauge field. All displayed logarithms use their branches near the identity.

Scaling all four logarithms by \(1/2\) produces
\[
                  e^{X/2}e^{Y/2}e^{-Z/2}\ne I.             \tag{L9}
\]
For an exact check, put \(a=e^{X/2}\), \(b=e^{Y/2}\). Equality in (L9) would give \((ab)^2=e^Z=a^2b^2\). Cancellation on the left by \(a\) and on the right by \(b\) gives \(ba=ab\). But
\[
 ab-ba=-\sin^2(\alpha/2)[\sigma_1,\sigma_2]
       =-2i\sin^2(\alpha/2)\sigma_3\ne0.
\]
Thus (L9) has a fixed positive defect. The original flat field passes every positive curvature threshold, including one smaller than this defect. The interpolation does not.

This example does not invalidate DOM's pure-gauge path. That path moves vertex values and stays exactly flat. It invalidates the proposed interpolation of bond logarithms. CV does not remove arbitrary node holonomies, so its residual normalization does not supply the missing global small chart. No datum-changing admitted homotopy was obtained by this attack.

## Attack 3: patchwise Lie-algebra interpolation and gauge synchronization

Cover the collar by enlarged cubes with bounded overlap. On cube \(Q_\alpha\), choose a gauge \(g_\alpha\) and write
\(U^{g_\alpha}=e^{i\eta A_\alpha}\). This attempt uses the available small cube gauges, then tries to patch the deformations. It does not assume a common gauge at the start.

The transition matrices are
\[
 h_{\alpha\beta}(x)=g_\alpha(x)g_\beta(x)^{-1},\qquad
 h_{\alpha\beta}h_{\beta\gamma}=h_{\alpha\gamma}.
 \tag{L10}
\]
On an overlap they obey the exact bond identity
\[
 e^{i\eta A_\alpha(b)}
 =h_{\alpha\beta}(b_-)
        e^{i\eta A_\beta(b)}h_{\alpha\beta}(b_+)^{-1}.
 \tag{L11}
\]
These are endpoint-dependent changes of frame. They are not conjugation of each potential by one constant matrix.

**Direct averaging fails to respect the original field.** Take the original field to be \(I\) on a two-dimensional patch, embedded in four dimensions. Use gauges
\(g_1(x)=e^{iax_1\sigma_1}\) and \(g_2(x)=e^{iax_2\sigma_2}\), with fixed small \(a>0\). Their exact potentials are
\[
 (A_1)_1=-a\sigma_1,\quad (A_1)_2=0,
 \qquad (A_2)_1=0,\quad (A_2)_2=-a\sigma_2.
\]
Each describes a flat field. A half-half partition of unity gives links
\(u=e^{-i\eta a\sigma_1/2}\), \(v=e^{-i\eta a\sigma_2/2}\).
Their plaquette is \(uvu^{-1}v^{-1}\ne I\). Indeed
\(uv-vu=-2i\sin^2(\eta a/2)\sigma_3\ne0\), as long as \(0<\eta a<1\).
Thus even constant weights can create curvature from two flat descriptions of the same field. Varying weights also create the first-difference term in (L6).

This does not say that good gauges cannot be chosen. Choosing both gauges equal to the identity removes this example. It says that an estimate on each gauge separately is not a gluing theorem.

**First repair: transport every patch into one frame.** On an overlap, (L11) transports the unmodified fields exactly. But the proposed contracted patches
\(U_{\alpha,s}=e^{i\eta(1-s)A_\alpha}\) do not satisfy (L11) with the original transitions. At \(s=1\), its two sides would be
\[
                 I\quad\hbox{and}\quad
                 h_{\alpha\beta}(b_-)h_{\alpha\beta}(b_+)^{-1}.
 \tag{L12}
\]
They coincide only when that transition is constant along the bond. One must therefore deform the transitions too, preserving their cocycle identities and the protected datum. The original compatible gauges do not provide that deformation.

**Second repair: pin transitions and use the massive gauge on the cover.** Suppose \(|A_\alpha|,|A_\beta|\le a\) on an overlap. From (L11), for \(b=(x,y)\),
\[
 h_{\alpha\beta}(y)
 =e^{-i\eta A_\alpha(b)}h_{\alpha\beta}(x)e^{i\eta A_\beta(b)}.
\]
Unitarity and \(\|e^{iH}-I\|\le\|H\|\) for Hermitian \(H\) imply
\[
 \|h_{\alpha\beta}(y)-h_{\alpha\beta}(x)\|\le2\eta a.
 \tag{L13}
\]
Along an overlap path of physical length \(d\), telescoping gives \(2ad\). Thus a transition can be made near the identity on a *bounded* overlap by removing its value at one chosen point. This is a useful local estimate.

Pinning these constants along a tree of patches gives a sum of such errors along the tree. The elementary bound after \(n\) transitions is proportional to \(n\), not to the overlap multiplicity. On a fixed cell collar this may still be paid by (L3). On the whole exterior, \(n\) is unrestricted by the local stage geometry. A fixed coupling ceiling cannot make \(na\) small for all torus sizes.

Replacing this tree estimate by a massive inverse is not yet a repair. The CP12 map (L5) takes a single small potential on its supplied enlarged cube as input. Here the objects to be solved for are the transitions and their time-dependent compatibility equations (L10)–(L12). An inverse bound for a site operator neither solves those equations nor identifies a global logarithmic chart. No such solution was constructed in this attack.

**Exact failure.** Patch contraction is not compatible on overlaps; compatible patch contraction is precisely an additional deformation problem. The real size bounds and the massive scalar inverse do not resolve it. Even if this compatibility were proved on the cell collar, a path from each arbitrary exterior completion to the same localized endpoint would still have to be constructed. We obtained no estimate for that global path. The argument does not show that every possible patching scheme fails.

## A fourth attempt: a curved extension with no gauge choice

There is a useful positive result on one uniform lattice. It removes the initial-gauge problem for that special geometry.

**Folding extension.** Let
\[
 Q=\prod_{i=1}^4\{0,\ldots,n_i\},\qquad
 T=\prod_{i=1}^4\mathbb Z/N_i\mathbb Z,\qquad N_i\ge2n_i+2.
\]
Let \(D\) assign \(SU(2)\) matrices to the edges of \(Q\), with reversed edges assigned inverses. There is a rule \(\mathsf F(D)\) on \(T\) with these properties:

* it uses only those edge values and agrees on every edge of \(Q\);
* every output plaquette is either the identity or a conjugate of an input plaquette or its inverse;
* it is real and holomorphic as a map of the complexified edge variables;
* its map in raw coordinates at any real input has norm at most one, on a fixed small raw ball independent of all side lengths.

In particular it preserves a **common** plaquette threshold exactly, also for curved input. It is not asserted to preserve a heterogeneous collection of layer-indexed tests.

*Proof.* For representatives \(x\in\{0,\ldots,N_i-1\}\), set
\[
 r_i(x)=
 \begin{cases}
 x,&0\le x\le n_i,\\
 2n_i-x,&n_i\le x\le2n_i,\\
 0,&2n_i\le x<N_i.
 \end{cases}
 \qquad r(x)=(r_1(x_1),\ldots,r_4(x_4)).                 \tag{L14}
\]
Adjacent vertices map to equal or adjacent vertices. Define the output on \((x,y)\) to be \(I\) when \(r(x)=r(y)\), and otherwise \(D(r(x),r(y))\). On \(Q\) this is the input.

On a plaquette in directions \(i,j\), the \(i\)-increment of \(r\) depends only on \(x_i\), and the \(j\)-increment only on \(x_j\). If either increment is zero, opposite surviving edges cancel. Otherwise the four images are the four corners of a unit plaquette in \(Q\), traversed once. Reversing orientation inverts the plaquette product; moving its base conjugates it. In \(SU(2)\) these operations preserve \(\|P-I\|\). This proves the first two claims.

Each output edge is either \(I\), one input edge, or its inverse. Matrix inversion is holomorphic on \(SL(2,\mathbb C)\). To check the uniform raw bound, write an input edge as \(D(c)=e^{iB(c)}D^0(c)\), with \(D^0(c)\) real. On a copied edge the output raw coordinate is \(B(c)\). On an inversely copied edge it is exactly
\[
                 -\operatorname{Ad}(D^0(c)^{-1})B(c).     \tag{L15}
\]
To verify (L15), multiply \(D(c)^{-1}\) by \(D^0(c)\) on the right, then take the logarithm near the identity. Conjugation by the fixed unitary \(D^0(c)\) preserves the operator norm, also for complex \(B\). Collapsed edges have coordinate zero. For example, \(\|B\|<1/4\) lies on the required common logarithm branches. Thus the output raw norm is at most \(\|B\|\). \(\square\)

This is a genuine curved-data endpoint construction, with no long path products. In the single-layer loop-regular datum class, the admitted-background conclusion follows if the A1 import is applied at that same threshold. The construction itself proves only the displayed edge, plaquette and chart statements.

**Why it does not close LOC.** First, a mixed determining system does not supply all fine edges on a rectangular \(Q\). A row of one level can fold into a region where that level is not a determining row. Its seam loop may use a nonlinear average of finer rows. Formula (L14) supplies neither those missing rows nor an identity commuting with that average. The actual geometry cannot be replaced by the complete cuboid without proof.

Second, this extension supplies no path from the original exterior data. A proposed path obtained by deforming the underlying map from the identity to \(r\) already fails on a uniform torus. On a coordinate circle the identity map has winding number one. The periodic piecewise-linear extension of \(r_i\) in (L14) has winding number zero: it goes forward, then back, then stays fixed. Winding number is constant under a continuous homotopy. One way to check this is to lift the circle map to the real line; its increment after one period is an integer multiple of the period. Along a homotopy this integer is continuous, hence constant. Thus this particular pullback-homotopy construction cannot join the two maps. This is not a nonexistence proof for paths of gauge data, which need not be pullbacks by maps of the torus.

The fourth attempt therefore supplies an endpoint on a useful special class, but does not supply the necessary relative path.

## The sector issue is not discharged by an old verdict

A repository search found the same danger in an earlier route: `relative-density-bound.md`, item (r), and `sector-values.md` §0. The cited review is `gates/theorem-z-3b7fd4e57.md`, D4. It proposes a remote lattice instanton to obstruct a small-curvature path. Crucially, its last paragraph at line 119 says that its four-dimensional admissibility argument was not re-proved on this lattice. That report is evidence of a failed earlier path argument. Its verdict is not a substitute for the hand proof required here.

The elementary logical test is exact. Suppose a function \(Q\) on \(\mathcal A_{\rm path}\) is constant on every admitted path fixed on \(P\). If two members of \(\mathcal A_{\rm in}\) agree on \(E\) but have different \(Q\), LOC-flat is false. This follows from the concatenation argument after (L1), without any speed estimate.

To turn the proposed instanton into this counterexample, one must define the invariant on the **actual mixed determining data and the whole allowed path class**, and give two admitted curved inputs with identical restrictions to \(E\). The path class may be larger than the endpoint test class. Its admissibility radius, its missing/inward rows, the fixed protected shell, and every seam test must be included. A topological invariant of fine fields is not automatically an invariant of these determining data. A charge calculation in a uniform fine lattice does not make this identification.

The two-dimensional abelian flux example also does not settle this problem. A path of \(SU(2)\) data can leave its diagonal \(U(1)\) subgroup. No abelian flux conservation law may be applied to that path without proving its extension to the nonabelian class. No numerical test or old PASS label is used here.

Consequently the possibility of disconnected relative fibres remains a reason to test the path requirement itself. It is not treated as a proved counterexample, and it must not be silently excluded by selecting a topological sector as new input.

## Recovery and verification limits

The current checkpoint is this file. The endpoint problem and the path problem are distinct. The hand deductions are (L3), the conditional cutoff and speed estimates (L6)–(L7), the exact failures (L8)–(L13) of the specified interpolation methods, and the single-layer folding extension (L14)–(L15). The CP12 contraction is used with its initial-gauge hypothesis explicit. None of these results proves the missing path for the actual stage class.

All returned LOC/path/chart constants must be chosen at IN1 rows 3–4, before \(\kappa\), independently of \(M,\bar\kappa\), history depth and volume. The later choice of \(M\) and the final ceiling on \(\gamma\) can enforce (L3). They cannot absorb a factor in an unrestricted torus diameter, repair an unchanged threshold ratio, or supply a bounded raw chart from mere holomorphy. IN1 Amendment 1 changes only the stated floors on \(L\) and \(\kappa\).

No scientific computation was run. Source retrieval, searching, hashes and file checks are bookkeeping. The displayed arguments are by Codex and have not been checked by another provider. Only `library/loc.md` is edited. The prior version is retained at the recovery path in the provenance line. No editable prompt file, frozen consumer, audit file or ledger was changed.

## Result

**Open lemma**

**Uniform protected-fibre path lemma (statement to prove or refute).** In the actual stage geometries and admission classes defined above, there is a constant \(C_{\rm rel}<\infty\), chosen before \(\kappa\) independently of \(M,\bar\kappa\), depth and volume, such that, after one permitted final coupling ceiling, the following holds. For every
\[
 D^0,D^1\in\mathcal A_{\rm in},\qquad D^0|_E=D^1|_E,
\]
there is a piecewise \(C^1\) path \(D_s\in\mathcal A_{\rm path}\), \(0\le s\le1\), with
\[
 D_0=D^0,\quad D_1=D^1,\quad
 D_s|_P=D^0|_P,\qquad
 \sup_{s,c}\|i^{-1}\dot D_s(c)D_s(c)^{-1}\|\le C_{\rm rel}.
 \tag{L16}
\]

LOC-flat implies this lemma with \(C_{\rm rel}=2C_{\rm path}\). Even qualitative connectivity in (L16) is unresolved here. Its failure would refute the requested local endpoint/path rule. Its proof alone would not construct the holomorphic local section, so this is an explicit necessary subproblem, not a claimed equivalent reduction or the sole sufficient missing input.

The three new attacks failed at distinct points: the massive gauge gives a controlled collar formula only after a common local gauge and its carrier are supplied; CV gauge motions preserve the datum, and subsequent logarithmic contraction can create curvature from a flat input; patch interpolation lacks a compatible deformation of its transition functions, with no uniform global repair. The additional folding construction proves a curved single-layer endpoint but provides neither mixed-row compatibility nor an admitted relative path.

Thus LOC-flat for curved stage data is **not proved or refuted by this note**. DOM Lemma 11 remains a valid conditional route from an admitted path to decay; this work does not discharge its path premise or ST-test's quantitative holomorphic requirement.
