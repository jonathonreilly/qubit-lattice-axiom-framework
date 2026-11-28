## Repo search

**GUIDE.** FINISH row 1246, source checkout `4df5fc707`. The target-specific prior file is absent. The lead's November 8 search covered main and PRs 10114, 10133, 10134 and 10141. I read the relevant source passages at the fetched heads. PR 10114 (`f76f6c649c`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149) gives a positive one-step plaquette correlation at finite coupling and a contraction in the small Wilson-parameter interval through $1/32$. Grok's PR 10133 (`89faef229f`, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 77–86) leaves the crossover and source transport open. PR 10134 (`1e70c7211a`, `mass-gap-interface.md`, I1–I5) distinguishes a nonempty excited space, a gap and identification. PR 10141 (`a2f6a430e2`, `fp1.md`, lines 299–315) controls a classical block minimizer. Main (`8b11ae2bb9`, `research/mass-gap/library/gap-phys-seed.md`, lines 305–329) gives the conditional finite-size propagation theorem.

**GUIDE.** The outline and CA-I are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, at `31a47c543775`. Index chunks 01 and 29 and the corresponding obligations point to outline lines 581–599 and 31858–31882. Those passages distinguish the cyclic action-density theory from the full algebra and exhibit a decaying correlation with spectral support down to zero. CA-I lines 2704–2712 and 3213–3222 leave even vacuum uniqueness and the mass gap open. Their ultraviolet bounds and the physical infrared estimate have separate hypotheses. [Outline at the cited revision](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712) · [Outline index](sa-index/README.md)

**GUIDE.** Row 1218, `prior/gap-onebound-read-sol.md`, locates three relevant proposals. Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy give a conditional ascent from a full thermal bound on a range of shapes. The first four authors also study cube heat-bath relaxation. Zeng Chunping formulates a common decay rate for local observables. I use the repository comparison to identify the questions. None of these estimates is assumed for the tuned four-dimensional Wilson law. Row 1236, `gap-solve27-astra62.md`, leaves the neutral physical spectrum open after its static-pair comparison. Its estimates are author research awaiting a check. The closest observability results are rows 1171 and 1178 on equal-time short Wilson loops. Row 1161 already supplies the neutral state count used in (20). [Lead’s repository search](prior/repo-search-2026-11-08.md) · [Row 1218](prior/gap-onebound-read-sol.md) · [Row 1171](gap-solve14-astra62.md) · [Row 1178](gap-solve18-astra62.md) · [Row 1161](gap-solve9-astra62.md)

**OPEN.** Construct the nontrivial four-dimensional SU(2) Yang–Mills vacuum theory and find a common positive energy threshold for its orthogonal complement. The first proof attempt below concerns how to control the neutral physical spectrum of the actual Wilson transfer. No scientific status is assigned by this note.

## Which neutral states do the plaquettes see?

**GUIDE.** At fixed lattice spacing, “cyclic” means that functions of successive plaquette readings prepare a dense set of states from the vacuum. The finite-cube result is (4), with the spatial-only version established by (8)–(11). The bounded correlation (6) then measures the true slowest neutral relaxation rate. Its spectral weight at bounded physical energies can nevertheless vanish by (15). The remaining strict physical-time inequality is (27).

**GUIDE.** I will try to recover the local Wilson observable algebra from measurements of individual spatial and temporal plaquettes. A uniform decay estimate on a total family would detect the physical spectral edge. The finite-cutoff question comes first since inserting a normalized trace can lose colour information. Row 1236 computes the temporal marked multiplier on one link. Row 1207 (`gap-agy-solve2-argon.md`, Theorem 4.2, by Gemini Argon) computes the electric double commutator for a sum of magnetic terms. Neither passage identifies the cyclic space of plaquette histories. I found no owner for that question in the registry. Their lattice source samples distinct plaquette barycentres. Isolating an individual plaquette uses a cutoff-dependent test, as explained below.

**GUIDE.** The transfer construction is due to Osterwalder and Seiler and to Lüscher. I use GL3 and GL8 in the Sussman–Alpoge outline, lines 2197–2224 and 2315–2335. I will first extract the electric representation projectors from the marked kernel. Then I will test whether plaquette products and those projectors can produce general closed-loop readings, and whether the cost permits a continuum conclusion.

### Selecting the representation on one spatial link

**PROVED.** Fix a finite periodic spatial cube of side $n\ge4$ and $\beta>0$. Use normalized Haar measure. Write $w(q)=\operatorname{tr}(q)/2$ and identify SU(2) with the unit quaternions. On the vertex-gauge-invariant space use the time transfer $T=DCD$, where $D$ is the spatial magnetic half weight and $C$ is the product of the normalized electric convolutions. Positive scalar normalizations of $T$ do not matter here. Vertex averaging at each temporal cut gives this restriction. The top vector $\psi$ can be chosen strictly positive. Indeed the unprojected continuous kernel is strictly positive on a compact space. Maximizing its Rayleigh quotient, taking the modulus and applying the kernel gives a positive eigenfunction. Equality in the modulus inequality forces each top eigenfunction to have constant phase. This gives simplicity and invariance under the symmetries of $T$.

**PROVED.** Let $\mathcal A$ be the von Neumann algebra generated by $T$, multiplication by each spatial elementary $w_p$, and the transfer $T_e$ with the temporal plaquette at spatial edge $e$ marked once by its half-trace. These are self-adjoint bounded operators. Finite words in them acting on $\psi$ describe linear combinations of finite plaquette histories, allowing products on a spatial slice. A spatial polynomial is a bounded observable at this cutoff. Strong closure gives the same closed cyclic subspace as the words, since the orthogonal projection onto their closed span commutes with every generator. All the operators commute with the three spatial centre flips.

**PROVED.** Both $D$ and $D^{-1}$ belong to $\mathcal A$, by bounded continuous functional calculus of the finitely many spatial plaquette multipliers. Thus $\mathcal A$ contains $C=D^{-1}TD^{-1}$ and $C^{[e]}=D^{-1}T_eD^{-1}$. They commute. On the tensor product of edge representations of dimensions $d_b=1,2,\ldots$, their joint eigenvalue pair is
\[
    (s,s\,v_{d_e}),\qquad
    s=\prod_b c_{d_b}>0,\qquad
    c_d=I_d(\beta)/I_1(\beta),\qquad
    v_d=p_\beta+\partial_\beta\log c_d,\qquad
    p_\beta=I_2(\beta)/I_1(\beta).
\tag{1}
\]
The marked coefficient follows by differentiating the normalized one-link density, whose derivative is $(w-p_\beta)$ times that density. This calculation and the ordering of the marked ratios appear in row 1236, equations (6)–(10). For clarity, $I_{d+1}/I_d$ is the mean of $t$ in a law proportional to $e^{\beta t}(1-t^2)^{d-1/2}$ on $[-1,1]$. This follows by differentiation of the integral for $\beta^{-d}I_d(\beta)$, or by expanding the exponential and integrating its even powers. The mean is positive for $\beta>0$ and its derivative is the strictly positive variance. Hence $v_{d+1}-v_d=\partial_\beta\log(I_{d+1}/I_d)>0$.

**PROVED.** In the joint spectral calculus select the Borel set $\{(s,t): s>0,\ t=s v_d\}$. Equation (1) gives exactly the projection onto dimension $d$ on edge $e$, restricted to invariant states. The zero eigenprojection of $C$ vanishes by its strictly positive multipliers and completeness of Peter–Weyl. This argument needs neither a bounded inverse for $C$ nor a generic choice of $\beta$. In particular $\mathcal A$ contains $S_{e,h}=\exp(h\Delta_e)$ for every $h>0$, since $-\Delta_e$ has eigenvalue $d^2-1$ in this normalization. Here $\Delta_e$ is the sum of squares of the three unit-imaginary-quaternion left derivatives on $e$.

**PROVED.** Suppose multiplication by two real smooth gauge invariants $f,g$ belongs to $\mathcal A$. Then so does multiplication by $\Gamma_e(f,g)=\sum_a(\partial_{e,a}f)(\partial_{e,a}g)$. Indeed $h^{-1}[[S_{e,h},M_f],M_g]$ has strong limit $2M_{\Gamma_e(f,g)}$. On smooth vectors the limit follows from the product rule. For a uniform norm bound, the heat kernel on this one link is a probability kernel and its mean squared quaternion chord from its starting link is $2(1-e^{-3h})\le6h$. This is the action of $S_{e,h}$ on the four fundamental matrix coordinates. Positivity and conservation of the heat semigroup also follow from the maximum principle on the unit sphere. The double-commutator kernel multiplies the heat kernel by $(f(Y)-f(X))(g(Y)-g(X))$. Each difference is bounded by a constant times the chord on the compact sphere, uniformly in the other links. The row and column integral bounds give a uniform operator norm after division by $h$. Density of the smooth vectors gives the asserted strong limit. The sign here uses the nonpositive $\Delta_e$.

### Recovering the configuration in an open spatial box

**PROVED.** For a finite connected spatial subgraph $H$, vertex gauge transformations identify its configurations with tuples of based chord holonomies up to simultaneous conjugation. To obtain the tuple, set the links on a rooted spanning tree equal to $1$, by successive transformations from the root. The remaining transformation is common conjugation at the root. Under product Haar measure the chord holonomies are independent Haar variables after conditioning on the original tree links. Statements below about functions on $H$ act by pullback on the full slice.

**PROVED.** At one vertex of a unit cube, take the three incident faces in the $xy,yz,zx$ planes. Orient their based holonomies $A,B,C$ in that cyclic order. For example $A$ starts on the positive $x$-edge and ends on the inverse $y$-edge, and $B$ starts on the $y$-edge. Their three half-traces are generators. For words $P,Q$ with $P$ ending on $b^{-1}$ and $Q$ starting on $b$, each using $b$ just once, differentiation on the left of $b$ gives
\[
       \Gamma_b(w(P),w(Q))=-\operatorname{Im}P\cdot\operatorname{Im}Q,
       \qquad w(PQ)=w(P)w(Q)+\Gamma_b(w(P),w(Q)).
\tag{2}
\]
The imaginary parts are in the common frame at the base vertex. Indeed the varied words are $P e^{-ta}$ and $e^{ta}Q$, respectively. Possible other shared edges are held fixed. Applying (2) gives $w(AB),w(BC),w(CA)$. After cancelling the common $y$-edge in $AB$, that word ends on the inverse $z$-edge. Another application gives $w(ABC)$.

**PROVED.** These seven real numbers determine the gauge orbit on this corner graph. The three based face words are independent free generators, as seen from the tree consisting of the three root edges and one further edge to each of the three face corners. The pair traces determine the three mutual dot products of the imaginary parts. Their lengths follow from the unit norms. The triple trace also gives the oriented volume of the three imaginary parts, since
\[
 w(ABC)=abc-c\,u\cdot v-a\,v\cdot z-b\,u\cdot z-(u\times v)\cdot z
\]
for $A=a+u,B=b+v,C=c+z$. A Gram matrix and signed volume determine three vectors up to a proper rotation. In the degenerate case an isometry on their span extends to a proper rotation by choosing the action on its orthogonal complement. Every proper rotation comes from quaternion conjugation. The continuous map from the compact orbit space to its seven trace values is therefore a homeomorphism onto its image. Bounded Borel functional calculus and Haar completion give all bounded gauge-invariant multipliers on the corner.

**PROVED.** Here is the extension step. Suppose all invariant multipliers on $H$ have been obtained. An elementary face has one arc in $H$ and closes by a path whose internal vertices and edges are new. Choose an edge $b=(x,y)$ on the old arc such that $H-b$ is connected and has at least two independent cycles. Orient and cyclically start the face so that its word is $bR$, traversing $b$ just once. Choose a route $D_0$ from $y$ to $x$ in $H-b$ and two based fundamental cycles $L_1,L_2$ there at $x$. Put
\[
    D_i\in\{D_0,\ D_0L_1,\ D_0L_2,\ D_0L_1L_2\},\qquad H_i=bD_i .
\]
All $w(H_i)$ are smooth invariant multipliers on $H$. On a set of full Haar measure $1,L_1,L_2,L_1L_2$ form a real basis of the quaternions. Indeed the first two imaginary vectors are almost surely nonparallel, and their cross product is the component of $\operatorname{Im}(L_1L_2)$ perpendicular to their span. The Haar assertion follows in tree gauge since the two chord variables are independent. Left multiplication by $bD_0$ preserves linear independence.

**PROVED.** The algebra contains the following four scalar readings. The right-hand side is the quaternion dot product.
\[
 w(H_i)w(bR)+\Gamma_b(w(H_i),w(bR))
                    = H_i\cdot (bR).
\tag{3}
\]
Both words start with $b$, so their derivatives are minus the components of their respective imaginary parts. Compare two configurations having the same old orbit and the same four new readings. Align the old configurations by a gauge transformation. Their four $H_i$ now agree in a common frame. Equation (3) gives the entire quaternion $bR$ by linear inversion. It fixes the product along the new arc with its endpoints in the old frames. On the interior of that arc the remaining links can be aligned by successive gauges, with consistency at the last endpoint given by the product. This proves recovery of the enlarged orbit. It also proves measurability. For example, in tree gauge use the first imaginary cycle direction and the component of the second perpendicular to it as the first two axes. Their cross product fixes the third. In this measurable frame the inverse of the four-by-four Gram system is an ordinary Borel function where its determinant is nonzero. The exceptional set and all its pullbacks have Haar measure zero. Thus all bounded gauge-invariant multipliers on the enlarged graph belong to $\mathcal A$. Adding a single tree edge to a fresh vertex also preserves the assertion, since its link can be gauged to $1$.

**PROVED.** This step fills an open rectangular three-dimensional grid, with at least one unit cell in each direction. In the starting cube, add an opposite face through the missing eighth vertex. It adds a two-edge arc between two old face corners. Add the last edge by one more face. In each case the chosen old edge lies on a cycle, and the graph already has cycle rank at least three. To adjoin a layer to a completed box, first add one outward edge at a root of its outer face. Traverse a spanning tree of that face, parents before children. For an old face-tree edge $uv$, once the outward copy $u'$ is present, the square $u,v,v',u'$ adjoins the path through the fresh vertex $v'$. Finally add the outer copies of each non-tree edge by its square. In every square choose $uv$ in the completed old box as $b$. It lies on a cycle there, and deleting it leaves a connected graph of cycle rank at least two. Repetition in each coordinate proves the assertion. In particular (3) applies to arbitrary invariant multipliers on any such open box embedded in a larger periodic slice.

### Closing the three periodic seams

**PROVED.** On the periodic spatial cube, the preceding open box contains every vertex. It omits the links crossing one end of each coordinate interval. Fix one seam direction and write $A_i$ for the link from the last face to the first at transverse position $i$. Use only neighbours $i,j$ of the open transverse square grid. Let $b_{ij}$ be the known edge from $i$ to $j$ on the first face, and $c_{ij}$ the corresponding edge on the last face. The Wilson plaquette reads
\[
         w(A_i b_{ij} A_j^{-1}c_{ij}^{-1}).
\]
After aligning the old box, (3) determines the open transporter $B_{ij}=A_i b_{ij}A_j^{-1}$ in those frames. To see the orientation explicitly, write the inverse plaquette starting with $c_{ij}$, obtaining $c_{ij} B_{ij}^{-1}$. Use four old paths avoiding $c_{ij}$ as in (3). Every such edge lies on a cycle in the box, and deleting it leaves the required rank. The reconstruction only uses previously known scalar readings and this plaquette and its four link derivatives paired with old readings. No other crossing edge enters the tests used to supply the four old paths.

**PROVED.** At a root $i_0$ on the first face choose two independent based grid cycles $\gamma_1,\gamma_2$. Their products $b_{\gamma_1},b_{\gamma_2}$ almost surely do not commute. This follows by the same tree and independent-Haar argument on that face. The recovered products on the last face satisfy $B_\gamma=A_{i_0} b_\gamma A_{i_0}^{-1}$. A unit quaternion commuting with both noncommuting quaternions has imaginary part parallel to both imaginary axes and must be $1$ or $-1$. Thus $A_{i_0}$ is determined up to sign. The relation $A_j=B_{ij}^{-1}A_i b_{ij}$ propagates the same sign along the connected grid. Equivalently the two conjugacies determine a rotation in SO(3), with two lifts in SU(2). Choosing a Borel lift on a finite collection of coordinate patches makes the reconstruction measurable. This completes one seam up to its global centre flip. The three reconstructions use only the open box and plaquettes crossing their own seam. They determine the configuration up to vertex gauges and the three independent seam flips. All their exceptional sets form a finite union of null sets at fixed $n$.

**PROVED (finite-cutoff cyclicity).** Let $\mathcal H_+$ be the space of square-integrable functions of a spatial slice invariant under vertex gauges and the three spatial centre flips. For every $n\ge4$ and $\beta>0$,
\[
       \overline{\operatorname{span}}\{ A\psi:\ A\text{ a finite word in }
          T,\ M_{w_p},\ T_e\}=\mathcal H_+ .
\tag{4}
\]
In fact the algebra contains multiplication by every bounded invariant function on the quotient. Its measurable coordinates were constructed above on a conull set. Multiplication by such functions on the strictly positive $\psi$ has dense range of vectors in $\mathcal H_+$. Truncate $u/\psi$ in absolute value and use dominated convergence in $L^2$ to recover any $u\in\mathcal H_+$. Conversely every generator and the vacuum respect each symmetry defining $\mathcal H_+$. The same argument with the completed open box gives the full gauge-invariant cyclic space there when the spatial box has open boundary and carries its elementary plaquettes. No limit of lattice spacings enters (4).

### Removing the marks on individual temporal links

**GUIDE.** Row 1171, [gap-solve14-astra62.md](gap-solve14-astra62.md), already reconstructs an equal-time connection modulo gauges and flat centre flips from contractible Wilson traces of length at most 18. It uses traces joining two vertex frames across a link. The trace-coordinate argument on a general graph also appears in [gap-channel-astra.md](gap-channel-astra.md). I use the centre-cochain conclusion of row 1171 below. The new question is whether the readings can themselves be obtained from spatial elementary plaquettes and an unmarked time step. The two-face derivative identity is Lemma F2 of [gap-target-max.md](gap-target-max.md). It is important in this question that two distinct incident faces share just one edge.

**PROVED.** There is a countable set $\mathcal E\subset(0,\infty)$, independent of the size of the finite graph, such that for $\beta\notin\mathcal E$ the unmarked electric convolution $C$ generates $\exp(h\sum_e\Delta_e)$ by bounded Borel functional calculus, for every $h>0$. For any finite list of positive integers $\mathbf d$ put $s_{\mathbf d}(\beta)=\prod_i c_{d_i}(\beta)$ and $k_{\mathbf d}=\sum_i(d_i^2-1)$. At fixed $d$,
\[
                c_d(\beta)=1-\frac{d^2-1}{2\beta}+o(\beta^{-1}).
\tag{5}
\]
Indeed $c_d$ is the mean of $\sin(d\theta)/(d\sin\theta)$ in the one-link probability with angle density proportional to $\sin^2\theta\,e^{-\beta(1-\cos\theta)}$. The character ratio is $1-(d^2-1)\theta^2/6+O_d(\theta^4)$ near zero. Rescale $\sqrt\beta\,\theta$ and dominate the rescaled moments with the Gaussian bound from $1-\cos\theta\ge2\theta^2/\pi^2$. The limiting second moment is $3$, by integration by parts in the radial Gaussian integral. This proves (5). If $k_{\mathbf d}\ne k_{\mathbf d'}$, the two real-analytic $s$ functions differ near infinity. Their positive-axis coincidence points are isolated. Take the union over the countably many pairs of finite lists. Off this union, $s_{\mathbf d}$ specifies $k_{\mathbf d}$. Assign the bounded value $e^{-hk_{\mathbf d}}$ at each distinct eigenvalue, and zero elsewhere. This gives the asserted heat operator on every finite graph. The marked proof of (4) holds also at exceptional couplings.

**PROVED.** For any $\beta>0$ one can alternatively supply the common heat operator using only the *sum* of the temporal plaquette traces at a cut as an extra reading, allowing arbitrary bounded functions of that sum on the finite lattice. An exponential of the sum changes that cut's common electric coupling to any $\gamma>0$, with the one-link normalizers fixed by a scalar. Removing the two spatial half weights as before gives $C(\gamma)$. On each finite tensor of spins, $C(\gamma)^{\lfloor2h\gamma\rfloor}$ tends to $e^{-hk_{\mathbf d}}$ by (5). The powers are contractions, so the limit holds strongly. This statement does not identify that spatially global reading with a fixed continuum source.

**PROVED.** Suppose the common spatial heat semigroup is available along with the individual spatial plaquette multipliers. Its double commutator gives multiplication by $\Gamma(f,g)=\sum_e\Gamma_e(f,g)$. The proof above applies to a product of finitely many heat kernels. The expected sum of squared link chords is at most $6h$ times the number of links, which suffices at fixed volume. Fix a vertex $x$. For two perpendicular oriented rays $i,j$ out of $x$, let $Q_{ij}$ be the based elementary face starting on $i$ and returning on $j^{-1}$. Thus $Q_{ji}=Q_{ij}^{-1}$. Fix cyclic orders $1\to2$, $2\to3$, $3\to1$ of the unsigned axes, at all choices of ray signs. Write $v_{ij}=\operatorname{Im}Q_{ij}$ in these orders.

**PROVED.** The following information at $x$ follows from spatial plaquettes and at most two applications of $\Gamma$.

* The real parts and lengths of all twelve imaginary vectors are known.
* The dot product between any two distinct face vectors sharing a ray is known. Their elementary plaquettes share one edge, so the total $\Gamma$ has only that contribution. Invert a based word as necessary and use (2). Using the opposite orientation of the stored edge changes left to right derivatives and preserves the contracted dot product.
* For each choice of one ray in each axis, the ordered triple of face vectors is known up to a proper rotation. To see its orientation, use the trihedral $A,B,C$ above. The only common edges of $AB$ (after cancellation) and $C$ are the first and last root edges. At both, the contribution is $w(ABC)-w(AB)w(C)$. Thus $w(ABC)=w(AB)w(C)+\Gamma(w(AB),w(C))/2$. The triple-trace formula recovers the signed volume.

**PROVED.** These data place all twelve vectors in a single proper frame, almost surely. Here are the details of the relative rotation, which is needed for the conclusion. Two octants differing by one ray have a common face vector $b$. Write the old triple as $(a,b,c)$ and the new one as $(d,b,e)$, choosing the two remaining names so that $a,d$ share one unchanged ray and $c,e$ share the other. The internal Gram and signed-volume data give a realization of each triple. Align the two copies of the nonzero $b$. The remaining proper rotation of the new triple is a rotation by an angle $\theta$ in $b^\perp$. The observed $a\cdot d$ and $c\cdot e$, after subtracting the components along $b$, give two linear equations for $(\cos\theta,\sin\theta)$. A row of the coefficient matrix is $(u\cdot v,u\cdot Jv)$, where $u,v$ are the corresponding old and new projections and $J$ is a quarter turn in the oriented plane. The matrix is nonsingular almost surely. In product Haar measure the twelve $Q_{ij}$ are independent Haar at this vertex. Each has a private non-root edge in no other incident face, and conditioning on the other edges leaves independent Haar on one such edge per face. Conditional on $a,b,c,d$ with nonzero projections, the planar angle of $e$ has a continuous uniform law. Thus proportionality of the two rows has probability zero. This test can use the actual realization to check nonsingularity since changing the initial alignment merely rotates the two coefficient columns. Degenerate triples are null by the same independent-variable argument. The finitely many adjacent pairs of octants are good simultaneously. Following a spanning tree of the eight octants aligns them all. Every inversion here is Borel on its nonsingular set. The finite Wilson marginal is absolutely continuous with respect to slice Haar.

**PROVED.** After aligning the frames of two configurations with the same data at every vertex, their $Q_{ij}$ agree there. The four face holonomies around a given link can also be based at its other endpoint by conjugating with that link, with the known orientation reversal when necessary. At least two have nonparallel imaginary vectors almost surely. Consequently the two links implement the same conjugation up to a central sign. Equal nonzero plaquette traces make these signs a closed $\mathbb Z_2$ cochain. On the cubical universal cover its product along a path depends only on the endpoints: elementary square moves commute coordinate steps and immediate reverse steps cancel. Products around the three periods give the three seam signs, after which the cochain descends as a vertex gauge. This is the final step of row 1171. The information used here consists of elementary loops, boundaries of two incident faces after cancellation, and the six-edge contour of a trihedral corner. The longest needed word on a spatial slice has length six after cancellation. Unlike the length-18 frame measurements, these multipliers are all obtained from the *common* heat operator by the two displayed derivative operations.

**PROVED.** It follows that for $\beta\notin\mathcal E$, the right side of (4) is already the closed cyclic space generated by $T$ and the spatial elementary plaquette multipliers alone. For every $\beta>0$ the equal-time length-four and length-six readings just listed generate the bounded invariant multiplication algebra modulo Haar-null sets. These conclusions also apply to the stationary vacuum slice, whose density is $\psi^2$. A global temporal-sum mark as above suffices at every $\beta$ if only elementary spatial plaquettes are measured. The exceptional set in the spatial-only operator proof is a limitation of spectral identification by (5). No physical tuning is assumed to avoid it.

### A bounded statistic for the bottom neutral energy

**GUIDE.** A closer predecessor to the octant argument is row 1178, [gap-solve18-astra62.md](gap-solve18-astra62.md), lines 124–140. It reconstructs each vertex list from *all* based products of two and three incident plaquettes, of length up to 12. Its two-face calibration then fixes each adjoint link. I use that calibration and its null-set argument. The smaller selection above uses only faces sharing an edge and trihedral triples. This selection is what permits generation by spatial plaquette histories. Row 1178 also proves that individual spatial plaquette traces at a single time lose part of the neutral space.

**PROVED.** At a fixed cutoff the original scalar source can address a single face if its test function is allowed to depend on the cutoff. In the convention of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, the weight is sampled at the barycentre (outline lines 326–337 and 1688–1693, CA-I lines 423–431 and 448–466). The two half-integral coordinates identify the orientation, and the other coordinates identify the square. A smooth bump about one barycentre of radius less than $a/4$ can isolate its $1-w_p$. Extracting those tests from a limit for fixed smooth functions is a separate convergence question.

**PROVED.** The following real, bounded statistic uses only the ordinary stationary Wilson law on a finite cylinder with infinite time. Write $U=T/\|T\|$, and let $r_+$ be its largest eigenvalue on $\mathcal H_+\ominus\mathbb C\psi$. It lies strictly between zero and one by positivity, injectivity, simplicity and compactness. In the slab of $m$ steps ending at time zero read the list $X_m$ of all spatial and temporal elementary half-traces there, including both boundary slices. Read the reflected list $Y_m$ in the slab starting at time $t$ in reverse order so corresponding entries are mirror partners. Let $Y_m'$ be an independent copy with the same marginal. Fix any $\sigma_m>0$ with no dependence on $t$ and set
\[
 \begin{split}
 k_m(x,y)&=\exp[-\sigma_m^2\|x-y\|^2/2],\\
 D(t)&=\sum_{m=1}^{\infty}2^{-m}
       \big\{\mathbb E k_m(X_m,Y_m)-\mathbb E k_m(X_m,Y_m')\big\}.
 \end{split}
\tag{6}
\]
Then for integer $t\ge1$,
\[
              0<D(t)\le r_+^t,\qquad
              \lim_{t\to\infty}D(t)^{1/t}=r_+ .
\tag{7}
\]
The weights and bandwidths of (6) do not use an eigenfunction.

**PROVED.** For the vector $s$ of independent real $N(0,\sigma_m^2)$ source coefficients, its characteristic function gives $k_m(x,y)=\int e^{-is\cdot x}e^{is\cdot y}\,dG_m(s)$. Write $v_{m,s}$ for the past-slab Wilson vector of $e^{is\cdot X_m}$ with the vacuum component subtracted. The transfer Markov property and reflection give the $m$-summand before weighting as
\[
                  \int\langle v_{m,s},U^t v_{m,s}\rangle\,dG_m(s).
\]
In the Doob representation the slab vector is the conditional mean given the end slice, times $\psi$. Its norm before centering is at most one. Equivalently one can integrate the positive transfer path with unit-modulus insertion. The independent term in (6) subtracts exactly the vacuum component. This proves nonnegativity and the upper bound. If a vector in the top excited eigenspace had zero scalar products with all the centered slab vectors, Fourier uniqueness on each finite cube of possible trace readings would give zero scalar products with vectors from *every* bounded function of those readings. The function of $s$ in such a scalar product is continuous, so vanishing for $G_m$-almost every $s$ already suffices. Every word in (4) is a slab insertion up to its scalar vacuum normalization, with unused steps at the far end allowed. Hence a nonzero top excited vector has nonzero integrated squared overlap for some finite $m$. Keeping that one positive spectral contribution gives $D(t)\ge c_{n,\beta}r_+^t$ with $c_{n,\beta}>0$. This proves (7). The same proof works with spatial plaquettes alone off $\mathcal E$.

**OPEN.** One possible sufficient infrared estimate is an upper bound on the exponential rate in (7), of at most $e^{-a_j m_{\rm phys}}$ with a common $m_{\rm phys}>0$ on arbitrarily large spatial cubes at every sufficiently fine cutoff, in a volume and cutoff construction matching the full local observable theory. Constants multiplying $e^{-a_jm_{\rm phys} t}$ in (6) may depend on the finite cube and cutoff if the $t\to\infty$ limit is taken first. This estimates a spectral edge. The one-cube *thermal* route would additionally have to control multiplicities. Neither estimate has been inserted as a premise of (4) or (7).

### Spatial plaquettes alone at every positive bare coupling

**PROVED.** The exceptional set in (5) can in fact be removed. Work at one fixed finite spatial cube and fixed $\beta>0$. Write $\mathcal A_s$ for the algebra generated by $T$ and the spatial elementary plaquette multipliers. As before it contains $C$. Its positive operator $B=-\log C$, defined by spectral calculus, has the additive expression
\[
       B=\sum_b h_\beta\big(\sqrt{1-\Delta_b}\big),\qquad
       h_\beta(d)=-\log c_d=d\log d+O_\beta(d).
\tag{8}
\]
For the estimate, the positive series of $I_d(\beta)$ lies between $(\beta/2)^d/d!$ and this quantity times $e^{\beta^2/4}$. Bound $\log(d!)$ between the adjacent integral sums for $\log x$. The bound in (8) follows also at $d=1$ by increasing its constant. We use the Bessel coefficients from GL3.

**PROVED.** If $f$ is real smooth, invariant and $M_f\in\mathcal A_s$, then this algebra contains multiplication by
\[
                          G_f(X)=\sum_b|\nabla_b f(X)|.
\tag{9}
\]
Here the norm on each link is the round three-sphere norm. This follows from conjugating $B$ with the bounded phases $e^{ikf}$. The proof below treats the unbounded logarithm by its resolvent.

**PROVED.** On one edge put $Q_{k,b}=k^{-2} e^{-ikf}(-\Delta_b)e^{ikf}$ for integers $k\ge2$ and $A_b=|\nabla_b f|^2$. For a smooth test $v$,
\[
 Q_{k,b}v=A_b v-\frac{i}{k}\big((\Delta_b f)v+2\nabla_b f\cdot\nabla_b v\big)
                              -\frac{1}{k^2}\Delta_b v .
\tag{10}
\]
Consequently $Q_{k,b}v\to A_bv$ and $\sup_k\|Q_{k,b}^2v\|<\infty$, by differentiating the smooth coefficients on the compact space. The resolvents $(1+Q_{k,b})^{-1}$ converge strongly to multiplication by $(1+A_b)^{-1}$. On a test $(1+A_b)v$ the difference from $v$ is $(1+Q_{k,b})^{-1}(A_b-Q_{k,b})v$. These tests are dense and the resolvents are contractions. Polynomials in $(1+x)^{-1}$ approximate continuous functions vanishing at infinity on $[0,\infty)$ by compactifying that half-line. Thus compactly supported continuous functions also pass to this strong limit.

**PROVED.** On the spectrum of $Q_{k,b}$ put $H_k(x)=h_\beta(\sqrt{1+k^2x})/(k\log k)$, extending $h_\beta$ continuously by linear interpolation between integers for this argument. Equation (8) gives uniform convergence to $\sqrt{x}$ on each bounded interval. Indeed $y=\sqrt{x+k^{-2}}$ gives the main expression $y+y\log y/\log k$, and $y\log y$ is bounded there. Interpolation preserves (8) with an enlarged constant. On the entire half-line $|H_k(x)|\le C_\beta(1+x)$, using $y|\log y|\le C(1+y^2)$ and $k\ge2$. For a fixed smooth $v$, the squared spectral tail of $(1+x)$ on $x>R\ge1$ is bounded by $4\|Q_{k,b}^2v\|^2/R^2$. After truncation at $R$, the preceding strong convergence applies. Sending $R$ to infinity proves
\[
 \frac{e^{-ikf} h_\beta(\sqrt{1-\Delta_b})e^{ikf}}{k\log k}\,v
                           \longrightarrow |\nabla_b f|\,v .
\]
This calculation takes place on the ordinary product Haar space and restricts to invariant vectors. It uses no individual edge operator as an observable.

**PROVED.** Sum over the finite edge set and write $B_k=e^{-ikf}Be^{ikf}/(k\log k)$. Each $(1+B_k)^{-1}$ belongs to $\mathcal A_s$. On smooth $v$ we just proved $B_kv\to G_fv$. Testing its resolvent on $(1+G_f)v$ gives strong convergence to $(1+G_f)^{-1}$ by the same contraction argument. These inputs are dense since $G_f$ is bounded. Inverting the bounded-away-from-zero limit gives (9) inside the algebra.

**PROVED.** For the loops needed at a vertex, (9) recovers their common-link dot product explicitly. Let $f=w(P),g=w(Q)$ be two simple contours of lengths $p,q$ with $l$ common edges. In the pairs used above the gradient dot product is the same number $d$ on each common edge. For incident faces there is just one. For $P=AB$ and $Q=C$ the two contributions agree by the endpoint computation following (5). A half-trace on a simple contour has gradient length $a=\sqrt{1-f^2}$ on each of its edges, by left or right quaternion differentiation. Write $b=\sqrt{1-g^2}$. Therefore
\[
       d=\tfrac12\left[
          \left(\frac{G_{f+g}-(p-l)a-(q-l)b}{l}\right)^2-a^2-b^2
       \right].
\tag{11}
\]
Opposite orientations on a common edge give the fused half-trace by (2). Thus (9)–(11) yield every adjacent-face dot product and oriented octant triple constructed above. The octant alignment and centre recovery then apply verbatim. This proves (4) with **only $T$ and individual spatial elementary $M_{w_p}$ at every $\beta>0$**. In particular (6)–(7) hold if both slabs read only their spatial plaquette half-traces. At no stage is the number of layers needed for strong approximation bounded uniformly in $n$ or $\beta$.

### Testing the decay rate in the weak-coupling Wilson law

**GUIDE.** I now use only the spatial readings in (6). To avoid making the statistic small merely by letting the bare plaquette approach one, fix $s>0$ and take $\sigma_m^2=s\beta^2/d_m$, where $d_m=3n^3(m+1)$ counts the spatial plaquettes on the $m+1$ slices. This gives a statistic normalized to the fluctuations of a bare plaquette. Its exact exponential rate is still (7).

**PROVED, conditional on the finite-window Wilson estimates of row 1231.** Let $n$ be even, $\beta\to\infty$, $\beta\le B_0\log n$ and take the infinite-time vacuum at each finite cube. Put $k_n(t)=P_{\rm cyl}(p,p+te_0)$ and $v_n=k_n(0)$ for one spatial face $p$. Here $P_{\rm cyl}$ is the one-colour projection onto exact two-forms on the free lattice cylinder. For any $0<\eta<1/24$, uniformly for integer $t\ge0$,
\[
 \begin{split}
 D(t)={}&e^{-3s v_n^2/2}\sum_{m\ge1}2^{-m}
     \left[\exp\!\left\{\frac{3s}{2(m+1)}
                  \sum_{l=0}^m k_n(t+2l)^2\right\}-1\right]\\
       &\hspace{18mm}+O_{s,B_0,\eta}(\beta^{-\eta}+n^{-3}).
 \end{split}
\tag{12}
\]
The inputs are [gap-solve26-astra62.md](gap-solve26-astra62.md), equations (2)–(5), including the uniformity in offsets of the radius comparison, and the half-tilt moment used there. Row 1231 credits Sourav Chatterjee for the open-box free-energy method. The free projection and its symbol are due here to the account of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (outline lines 1670–1693 and 1733–1762). The outline's free comparison alone supplies no interacting estimate.

**PROVED under those inputs.** Set $\xi_p=\beta(1-w_p)$. Compare at most four such readings to $|Z_p|^2/2$, where $Z$ has three independent Gaussian colours of covariance $P_{\rm cyl}$. Expectations of polynomials of fixed total degree at most four differ by $O_\eta(\beta^{-\eta})$ for bounded coefficients, uniformly in all offsets. For detail, clip each squared radius at $A\log\beta$. In row 1231 (2) the sup norm and Lipschitz constant of the clipped test are bounded by a fixed power of $\log\beta$. Choose its box exponent $\gamma$ between $2\eta$ and $1/12$. The resulting logarithms are absorbed by $\beta^{\gamma/2-\eta}$. Uniform exponential moments of each $\xi_p$ and of its Gaussian comparison bound the unclipping error by $C e^{-c A\log\beta}$ using Hölder, also with repeated locations. Choose $A$ large last. Independent Wilson copies follow by expanding mixed moments into products. The bounds pass to the vacuum cylinder before using any $n$ limit as in row 1231 (3).

**PROVED under those inputs.** Write $S=d_m^{-1}\sum_\alpha(\xi_\alpha-\xi'_\alpha)^2$ for a pair of slabs. Its Gaussian mean is $3v_n^2$ for independent slabs and
\[
          3v_n^2-\frac{3}{m+1}\sum_{l=0}^m k_n(t+2l)^2
\]
for the reflected pair. The factor follows from $\operatorname{Cov}(|Z_p|^2/2,|Z_q|^2/2)=3P_{\rm cyl}(p,q)^2/2$. In either experiment the Gaussian variance of $S$ is at most $C/n^3$ uniformly in $t,m$. In fact in the covariance of two individual squared differences, each surviving Gaussian pairing joins the two lists at least twice. The monomials on each list have even total degree. All entries have magnitude at most one. With both times and orientations fixed, the sum over the spatial displacement of the absolute product of two crossing entries is at most one by Cauchy–Schwarz. The squared entries in a row of an orthogonal projection sum to its diagonal, at most one. Independent-copy entries obey the same bound or vanish. There are boundedly many pairings. Summing the two time and orientation indices and dividing by $d_m^2$ leaves $C/n^3$. The comparison of four readings above gives the Wilson mean within $O_\eta(\beta^{-\eta})$ and the variance within that same error. Each term in the double average uses at most four readings, so this comparison is also uniform in $m$. Taylor's formula for $e^{-s S/2}$ about $\mathbb E S$ has expectation error at most $(s^2/8)\operatorname{Var}S$ since $S\ge0$. This proves (12) for the positive summable slab weights.

**PROVED under those inputs.** On the infinite-time cylinder $k_n(t)\ge0$ and $k_n(t)\le C(1+t)^{-4}$ uniformly in $n$. Indeed row 1231 (4) gives a spatial Fourier sum with nonzero modes, bounded by $Cn^{-3}\sum_{q\ne0}|q|e^{-c t|q|}$. Counting unit shells for $nq/(2\pi)$ bounds this by $C n^{-4}\sum_{l\ge1}l^3e^{-ct l/n}$ for $t\ge1$, hence by $C t^{-4}$ both for $t\le n$ and $t>n$. The value at zero is bounded by one. Also $v_n\to1/2$ by the bounded projection-symbol integral and four-axis symmetry. The sum of its six diagonal entries is three at every nonzero frequency. In particular the normalized statistic has $\liminf D(0)>0$, by just the $m=1$ term in (12). At separated times it obeys
\[
      0<D(t)\le C_s(1+t)^{-8}
                    +C_{s,B_0,\eta}(\beta^{-\eta}+n^{-3}).
\tag{13}
\]
For $t=\lfloor\beta^\delta\rfloor$ with $0<\delta<1/192$, row 1231 (5) gives $t^4k_n(t+2l)\to1/\pi^2$ for each fixed $l$. The uniform bound just proved dominates the summable mixture. Taking $8\delta<\eta<1/24$ in (12) yields the relative asymptotic
\[
                 t^8 D(t)\longrightarrow
                           e^{-3s/8}\frac{3s}{2\pi^4}.
\tag{14}
\]
It agrees with the free two-curvature threshold seen by a single bare plaquette. Here the statistic at each cutoff also sees *every* excited neutral eigenspace with positive weight.

**PROVED under those inputs.** Let $\nu_{n,\beta}$ be the positive energy measure of (6), using $E=-\log U$ in lattice units. At a fixed physical side $L=na$ and for fixed $A<\infty$, (13) implies
\[
 \nu_{n,\beta}([0,aA])\le e^{A L}D(n)
                 \le C_{s,B_0,\eta,A,L}(\beta^{-\eta}+n^{-3}).
\tag{15}
\]
The first inequality follows by keeping just this interval in the positive Laplace integral. Thus a nonvanishing total weight and finite-cutoff sensitivity to the entire neutral spectrum coexist with vanishing weight on *every* bounded physical energy interval. Taking a small fixed-lag covariance as evidence for the gap would lose precisely the late-time rate in (7). To determine that rate, one would need, for instance a strict upper bound on $D(t+\lceil h/a\rceil)/D(t)$ as $t\to\infty$ at fixed cutoff, with a common physical $h>0$ and uniform margin on the required cubes. This ratio is nondecreasing in $t$ by positive spectral reweighting, and its limit is $r_+^{\lceil h/a\rceil}$. The additive remainder in (12) is insufficient for such a bound.

### A direct estimate on blocks of physical time transfer

**GUIDE.** To bound the ratio after (15), one could try to contract the positive neutral transfer at each block of $u$ time steps by uniformly comparing its endpoint kernels. Row 1151, [gap-solve5-astra62.md](gap-solve5-astra62.md), exhibits a large *one-step* cross ratio between a flat field and a central field with maximally frustrated plaquettes. Here I test a growing block length and require both fields to have vanishing scaled elementary plaquette action.

**PROVED.** Let $n$ be even, $V=n^3$, $\beta\to\infty$ with $\beta\le B_0\log n$. For every integer sequence $1\le u=o(\beta^{1/4})$ there are two deterministic spatial fields $X,Y$ such that
\[
 \max_{p,\ Z=X,Y}\beta(1-w_p(Z))\longrightarrow0,\qquad
 \frac{K_u^+(X,Y)}{\sqrt{K_u^+(X,X)K_u^+(Y,Y)}}
                         \le e^{-c u V}
\tag{16}
\]
for all sufficiently large $\beta$, with an absolute $c>0$. Here $K_u^+$ is the actual positive $u$-step Wilson kernel averaged over vertex gauges and spatial centre flips, with any common scalar normalization. This is a statement about the kernel at specified endpoints.

**PROVED.** Fix a small constant $\kappa>0$ to be chosen below and put $b=\lfloor\kappa\sqrt\beta/u\rfloor$. Thus $b\to\infty$, $b\ll n$ and $\beta/b^4\to0$. Take $X_e=1$. In $Y$ put $Y_e=\exp(i\alpha_{x_1})$ on edges in direction 2, with a fixed unit imaginary quaternion $i$, and put the other edges equal to $1$. In successive full strips of width $4b$, increase $\alpha$ from zero by $1/b^2$ per step for $2b$ steps, then decrease by that amount for $2b$ steps. Keep it zero in the remainder of the circle. All elementary plaquette angles are at most $1/b^2$. At least $c_0V$ translated $b$-by-$b$ squares in the $12$ plane fit in a rising portion. Each has boundary holonomy of angle exactly one. An edge occurs on the boundaries of at most $2b$ such squares, since it lies on one of two parallel sides with at most $b$ possible beginnings.

**PROVED.** Suppress the separate endpoint magnetic half weights, which cancel out of the quotient (16). In temporal gauge integrate the $u-1$ internal spatial slices with product Haar, set $X_0=X$, and let $X_u$ be the gauge transform of a centre flip of $Y$. Integrate the final vertex gauges with probability Haar and average the eight flips. This formula follows by commuting both symmetry projections through each transfer and leaving them at the last cut. Let $\theta_{s,e}$ be the round distance from $X_{s,e}$ to $X_{s+1,e}$. Along each of the specified squares,
\[
           1\le \sum_{s=0}^{u-1}\sum_{e\in\partial R}\theta_{s,e}.
\]
Indeed the final holonomy has angle one, invariant under all the final gauges and flat flips. The bi-invariant triangle inequality telescopes the product first around its boundary and then through time. Cauchy–Schwarz on $4bu$ terms, $1-\cos\theta\ge2\theta^2/\pi^2$, and the multiplicity $2b$ give
\[
                   \sum_{s,e}(1-\cos\theta_{s,e})\ge c_1 V/(b^2u).
\tag{17}
\]
Keep half of this temporal cost and discard the nonnegative internal magnetic action. In the remaining half-coupling integral keep only a spanning tree of edges at the last step. Integrating the vertex gauges from its leaves gives $z_{\beta/2}^{V-1}$, with $z_\gamma=\int e^{-\gamma(1-w)}\,dq$. Integrating the internal slices in reverse order costs $z_{\beta/2}^{3V(u-1)}$. This bounds the numerator, without the endpoint weights, by $e^{-c_1\beta V/(2b^2u)}z_{\beta/2}^{N_*-1}$, $N_*=3V(u-1)+V$.

**PROVED.** For either diagonal entry, keep the trivial flip. Restrict every internal link to a ball of angular radius $\beta^{-1/2}$ about its specified endpoint link. Restrict each final site gauge to the same radius about $1$. This uses $N_*$ independent Haar variables. Every temporal angle is at most $3/\sqrt\beta$. Each internal plaquette angle is at most $4/\sqrt\beta+1/b^2$. The resulting lower bound, suppressing endpoint factors, is
\[
       \tfrac18(c_2\beta^{-3/2})^{N_*}
                          e^{-C u V(1+\beta/b^4)} .
\]
The cap volume lower bound and $z_{\beta/2}\le C_2\beta^{-3/2}$ follow by integrating $\sin^2\theta$ in the Haar angle density. Combining the bounds gives a logarithm at most
\[
       -c_1\beta V/(2b^2u)+C_3uV(1+\beta/b^4)+\tfrac32\log\beta+\log8.
\]
Choose $\kappa$ so that $c_1/(2\kappa^2)>3C_3+2$, then take the specified limit. This proves (16).

**PROVED.** Even on these endpoint pairs, comparison of $K_u^+$ to a product of positive endpoint factors requires a ratio of upper to lower constants at least $e^{cuV}$. The obstruction also applies to one-block contraction in the oscillation of the logarithm of a density ratio. On the two displayed endpoints, row and column scalings reduce the kernel to diagonal entries $1$ and off-diagonal entries $z\le e^{-cuV}$. The log output ratio for input weights in ratio $e^\epsilon$ has derivative $(1-z)/(1+z)$ at $\epsilon=0$. Positive narrow bumps about the two fields give the same limiting two-row calculation for the continuous kernel, by continuity, adding an arbitrarily small common positive background if required. Thus this uniform method can have contraction coefficient arbitrarily close to one already inside the vanishing-action band. Equation (16) concerns $u=o(\beta^{1/4})$ and extreme endpoints. It supplies no lower bound on the stationary probability of those endpoints, and no conclusion about contraction at $u$ of order $1/a$.

### A fixed number of time slices suffices with one temporal average per cut

**PROVED.** There is an integer \(m_*\), independent of the spatial side \(n\ge4\) and of \(\beta>0\), with the following property. All bounded functions of the individual spatial plaquette traces on \(m_*+1\) consecutive slices and of the single mean temporal plaquette trace on each intervening cut prepare a norm-dense linear subspace of \(\mathcal H_+\) from the Wilson vacuum. All three temporal orientations enter the same mean. The traces here and below are half-traces.

**PROVED.** Write \(\mathcal L_d\) for the weak-operator closed linear span of the \(d\)-step transfer kernels with arbitrary bounded complex functions of these readings inserted. At depth zero this means multiplication by functions of the spatial readings. The half spatial weights at adjacent endpoints give exactly the full weight at an interior slice. Concatenating two insertions gives an allowed insertion on the combined slab. Taking weak limits in the two factors successively gives \(\mathcal L_i\mathcal L_j\subset\mathcal L_{i+j}\). On a finite cube we can remove the two endpoint factors \(D\) and multiply the cut by \(\exp((\gamma-\beta)\sum_{p\ {\rm temporal}}w_p)\) times its normalization. This realizes the independently normalized product electric convolution \(C_\gamma\) on one step for every \(\gamma>0\). Gauge projection gives its restriction to physical functions. Since \(C_\gamma\to I\) strongly, \(I\in\mathcal L_1\) and \(\mathcal L_d\subset\mathcal L_{d+1}\).

**PROVED.** If all bounded functions of a real smooth \(F\) occur as multiplication operators in \(\mathcal L_d\), then
\[
 M_{\exp[-\Gamma(F,F)/2]}
   ={\rm s}\!-\!\lim_{\gamma\to\infty}
 M_{\exp(-i\sqrt\gamma F)}\,C_\gamma\,M_{\exp(i\sqrt\gamma F)}
 \ \in\mathcal L_{2d+1},\qquad
 \Gamma(F,F)=\sum_e|\nabla_e F|^2 .                                      \tag{18}
\]
Indeed write an independent left increment at each link as \(\exp(\xi_e/\sqrt\gamma)\), using unit imaginary quaternions as orthonormal directions. Its radial density in the scaled coordinate is proportional to \(\exp[-\gamma(1-\cos(r/\sqrt\gamma))]\gamma\sin^2(r/\sqrt\gamma)\) on \(0\le r\le\pi\sqrt\gamma\). Pointwise convergence, \(1-\cos x\ge2x^2/\pi^2\) and dominated convergence give the three-dimensional standard Gaussian limit and uniform second moments for large \(\gamma\). At fixed \(n\), Taylor expansion of \(F\) on the compact product group gives the linear form \(\sum_e \xi_e\cdot\nabla_e F\) with an error tending to zero in expectation, uniformly in the base point. This follows first on bounded increment sets, then by the second-moment tail bound. A continuous test vector evaluated at the incremented point converges uniformly in mean to its value at the base point. Gaussian characteristic functions prove (18) on continuous vectors, and contraction gives strong convergence on \(L^2\). Fixed \(n\) throughout this limit is sufficient for the depth assertion.

**PROVED.** Let \(f_i\) be finitely many simple spatial loop half-traces of lengths \(p_i\). Suppose all bounded Borel functions of their joint values are available in \(\mathcal L_d\). Join indices if their loops share a link, and let \(\Delta\) be the maximum degree of this graph. Applying (18) to \(F=\sum_i a_i f_i\) and multiplying by the known diagonal correction \(\exp[\tfrac12\sum_i a_i^2p_i(1-f_i^2)]\) places
\[
 M_{\exp[-\sum_{i<j}a_i a_j\Gamma(f_i,f_j)]}\ \in\mathcal L_{3d+1}.
\]
Here \(\Gamma(f_i,f_i)=p_i(1-f_i^2)\) by invariance of the metric and simplicity of each loop. The graph edges split into \(S\le2(\Delta+1)\Delta+1\) induced matchings. Indeed color two edges differently whenever endpoints coincide or are joined by a graph edge. Each edge conflicts with at most \(2(\Delta+1)\Delta\) others, so sequential greedy coloring suffices. For one matching and arbitrary real weights \(h_{ij}\) take \(a_i=1,a_j=-h_{ij}\) at its paired ends, zero elsewhere. All unwanted off-diagonal terms vanish. Multiplying over the matchings and then by \(\exp(\sum b_i f_i)\) shows that every real exponential of a linear form in the joint tuple \((f_i,\Gamma(f_i,f_j))\) occurs in the common space \(\mathcal L_{d'}\), where
\[
                    d'=d+S(3d+1).                                         \tag{19}
\]
Their linear span is a unital algebra of functions separating points on the compact range of that tuple. Uniform approximation by Stone–Weierstrass and bounded monotone approximation in the spectral measure give every bounded Borel multiplier of the tuple in the same space. Only this function algebra is multiplied at the approximation step. Closure of \(\mathcal L_{d'}\) under arbitrary operator products is unnecessary.

**PROVED.** Start with the elementary spatial faces and \(d=0\). A face meets at most twelve other faces along links. The first application of (19) supplies all two-face fused simple loop traces used in the vertex reconstruction, jointly with the original faces. Apply (19) again to the faces and these loops. At most four faces contain a specified link, and each has at most twelve face neighbors, hence at most \(4+4\cdot12=52\) members of this family use a link, counting a fused unoriented loop once per face pair. Each loop has length at most six, giving a maximum degree at most \(312\). The contractions of a fused trace with the third face give the triple data at each octant by the two-shared-link computation above. Thus the measurable reconstruction places the entire centre-neutral invariant multiplication algebra in \(\mathcal L_{m_*}\), with \(m_*\) bounded by the two iterations of (19) at degrees 12 and 312. Applied to the strictly positive vacuum, all its bounded multipliers span a dense subspace. Application to the vacuum is weak-operator to weak-vector continuous, and a linear subspace has the same weak and norm closure. This proves the fixed-depth assertion.

**PROVED.** The faithful correlation test can consequently use just this single slab. Take the spatial Gaussian factor at \(m=m_*\) in (12), and multiply the kernel by
\[
 \exp\!\left[-\frac{n^{-3}}{2m_*}
      \sum_{i=1}^{m_*}(\bar w_i(X)-\bar w_i(Y))^2\right] ,
\]
where \(\bar w_i\in[-1,1]\) is the cut mean. Call the resulting connected difference \(D_*(t)\). The Gaussian Fourier measure has full support in every reading, including every temporal mean, at each finite \(n\). The density result just proved and the spectral argument for (7) give \(D_*(t)>0\), \(\lim_{t\to\infty}D_*(t)^{1/t}=r_+\) and \(\lim_{t\to\infty}D_*(t+\ell)/D_*(t)=r_+^\ell\) for each integer \(\ell\ge1\). The temporal factor changes the difference by at most \(4n^{-3}\). Under the inputs of (12)–(15) their estimates therefore apply with the single \(m_*\) term in place of the weighted sum. In particular this detector also loses all weight on bounded physical energies in that limit. Its observation slab has physical width \(m_*a\to0\).

**PROVED.** The cut reweighting in this construction has a quantitative cost. Before gauge projection the single-link essential supremum of the new normalized kinetic density relative to the old one is \(z_\beta/z_\gamma\) for \(\gamma\ge\beta\), attained at zero angle by continuity. The radial integral and the two quadratic bounds on \(1-\cos r\), using a small cap for the lower bound, give \(z_b\asymp b^{-3/2}\) for \(b\ge1\). On \(3n^3\) independent reference increments the supremum is exactly \((z_\beta/z_\gamma)^{3n^3}\). Thus the proof gives a uniform number of slices together with preparations whose norms need not be bounded uniformly. This cost pertains to the particular reweighting in (18).

### Testing a physical-time endpoint comparison in the thermodynamic limit

**GUIDE.** The count needed for this test is already in row 1161. Its equation (19) uses products of bounded oscillating plaquette angles on disjoint supports and the inverse-transfer form. Row 1153, equation (13), had obtained a count with a threshold depending on the coupling. Row 1204 resolves an axial momentum in the oscillating-plaquette estimate. Here the application is to worst-case normalized endpoint kernels. [Row 1161](gap-solve9-astra62.md) · [Its check, row 1162](gap-solve9-check-opus.md) · [Row 1153](gap-solve6-astra62.md) · [Row 1204](gap-solve21-astra62.md)

**PROVED, using row 1161 (19).** For the periodic cubes of the count, take \(4\mid n\), \(\beta\ge1\), \(M\ge c_0 n^3\) disjoint selected locations and \(1\le l\le M\). With absolute \(C,c_0>0\), its statement in lattice units is
\[
       \#\{i:0<E_i\le Cl\}\ \ge\ \tfrac12{M\choose l}
                         \quad\text{on }\mathcal H_+ .                      \tag{20}
\]
For integer \(u\ge1\), keeping these terms in the neutral trace gives
\[
 \operatorname{Tr}_{+} U^u-1\ \ge\ {M\choose l}\Lambda^{-lu},
                              \qquad \Lambda=2e^C .                        \tag{21}
\]
This uses one value of \(l\) at a time and permits repeated levels between different counts.

**PROVED.** In particular, writing \(z_u=\inf_{X,Y}K_u^+(X,Y)/\sqrt{K_u^+(X,X)K_u^+(Y,Y)}\), we have
\[
 z_u\le(\operatorname{Tr}_{+}U^u)^{-1}
       \le (M+1)(1+\Lambda^{-u})^{-M}.                                    \tag{22}
\]
For the first inequality normalize the kernel by \(\lambda^u\), which leaves \(z_u\) unchanged. Its diagonal square root \(g\) has \(\|g\|^2=\operatorname{Tr}_{+}U^u\). To see this, take increasingly fine nested finite Haar partitions on the link space and compress the normalized continuous kernel to the cell-constant functions. The trace of each compression is the sum over cells of the double integral on the cell square divided by its measure. By uniform continuity this tends to the integral of the diagonal. The cell projections converge strongly to the identity, so summing in an eigenbasis of the positive trace-class operator gives the same limit as its trace. Trace class also follows from the one-link Bessel decay and bounded spatial weights. The inequality \(K/\lambda^u\ge z_u\,g\otimes g\) is pointwise. Testing the true kernel on the positive \(g\), whose Rayleigh quotient is at most one, gives the assertion. For the second inequality sum the binomial terms including \(l=0\) and bound that sum by \(M+1\) times their largest term in (21). At every fixed spacing and any finite physical block time \(h>0\), set \(u=\lceil h/a\rceil\) and let the spatial side go to infinity. The infimum then tends to zero exponentially in the spatial volume. Thus a volume-independent endpoint comparison fails even at this physical block time. The proof of (16) additionally locates bad pairs in a vanishing-action band at the shorter times specified there. The threshold in (20) is in lattice units and gives no positive lower bound on the first physical energy.

### Localizing the plaquette preparations on a large spatial torus

**PROVED.** Put \(\lambda=\|T\|\), normalize \(\|\psi\|=1\), and set \(\chi=D\psi>0\). Then \(\lambda\chi=D^2 C\chi\) on the full link space. For any subset \(J\) of spatial links write \(C_J\) for the normalized electric convolution on them only. There is an absolute \(c>0\) such that
\[
                          C_J\chi\ge c^{|J|}\chi \qquad(\beta\ge1).          \tag{23}
\]
Indeed vary those links along \(X_e(s)=\exp(sv_e)X_e\). The log of the magnetic weight \(D^2\) has second derivative at least \(-16\beta\sum_{e\in J}|v_e|^2\). The absolute second derivative of a face trace is bounded by \((\sum_{e\in p\cap J}|v_e|)^2\), each face has four edges and a link occurs in four spatial faces. Each electric log kernel has second derivative at least \(-\beta\sum|v_e|^2\). For the log of its integral against positive \(\chi\), differentiation gives the mean second derivative plus a variance, preserving this lower bound. Compactness at each finite lattice justifies differentiation. Thus the same path in \(\log\chi\) has second derivative bounded below by \(-17\beta\sum|v_e|^2\). Integrate twice and pair the independent kinetic increments \(v\) and \(-v\). Their first-order exponents average to a hyperbolic cosine at least one. This bounds the convolution ratio below by \(\mathbb E\exp[-(17\beta/2)\sum|v_e|^2]\). Each increment has probability bounded below by an absolute positive constant of lying at angle at most \(1/\sqrt\beta\), by the cap and normalization estimates above. Independence proves (21).

**GUIDE.** The temporal mean in (18) extends over an entire finite cube. For a local physical correlation one needs preparations that can be confined spatially when that cube grows. The local convolution estimate (23) gives such preparations and controls their error on low-energy input states.

**PROVED.** Let \(B\) be a finite open cubical box embedded with room for its one-cell collar in the spatial torus. Let \(J\) contain all links of all elementary plaquettes incident to the vertices of \(B\). Use just these spatial plaquettes on observed slices and the mean temporal plaquette on the links of \(J\) on each intervening cut. Define
\[
 R=\lambda^{-1} D(I_J\otimes C_{\bar J})D,\qquad
                      U\le R,\qquad 0\le R\le L_J I,\quad
                 L_J=c^{-|J|},\quad \beta\ge1 .                            \tag{24}
\]
For the first order inequality use \(0\le C_J\le I\). For the second, (23) gives \(R\psi\le L_J\psi\) pointwise. The weighted Schur bound for the symmetric nonnegative kernel of \(R\), including its identity kernel on \(J\), gives the norm bound. Explicitly, apply \(2|v(X)v(Y)|\le |v(X)|^2\psi(Y)/\psi(X)+|v(Y)|^2\psi(X)/\psi(Y)\) to its symmetric kernel measure. Also \(R\) commutes with every multiplication depending only on \(J\).

**PROVED.** With \(\mathcal L_j(J)\) the weakly closed space of the indicated *local* \(j\)-step insertions, normalized by \(\lambda^j\), every bounded gauge-invariant function \(f\) of the links in \(B\) satisfies
\[
                            M_f R^{m_*}\in\mathcal L_{m_*}(J).               \tag{25}
\]
Here the same fixed integer as in (19) can be used. Changing the coupling on the links of \(J\) alone gives \(V_\gamma=\lambda^{-1}D(C_{\gamma,J}\otimes C_{\bar J})D\) in one step, with no spatial reweighting. Its strong limit is \(R\) at fixed cube. For \(F\) supported on \(J\), the phase calculation (18) instead has strong limit \(M_{\exp[-\Gamma_J(F,F)/2]}R\). Indeed the phases commute with \(D\) and the complement convolution, so the small-increment calculation is entirely on \(J\). If the preceding stage supplies \(M_g R^d\) for all bounded \(g\) of its readings, surround \(V_\gamma\) with the two phases times \(R^d\). Their outer \(R^d\)'s commute with the phases, giving the limiting damping times \(R^{2d+1}\). Multiplication by a known diagonal correction times \(R^d\) and multiplication over matchings work with the powers of \(R\) adding at every step. This proves the local version of (19) with \(R^{d'}\) multiplying every output. Extra steps, when needed to use the common upper bound on the degree, simply multiply by \(R\). The uniform and bounded monotone limits still hold after multiplication by this fixed bounded power.

**PROVED.** Perform the octant reconstruction at every vertex of \(B\), using its collar. It fixes each link in the box up to vertex gauges and central signs. Equal elementary plaquette data on the box make the signs closed. Square moves in this rectangular box make the signs a vertex coboundary without any periods. Hence every bounded gauge invariant \(f\) there is measurable in the reconstructed data up to a Haar-null set. A Borel frame and tree gauge as before give the multipliers in (25). No orbit determination is required in the exterior of the collar.

**PROVED.** Let \(P_\tau=1_{[\tau,1]}(U)\), \(0<\tau\le1\), and take an integer \(b\ge1\). There is a sum \(A_{f,b}\) of weak limits of local slabs of at most \(m_* b\) steps such that
\[
 \|(M_f-A_{f,b})P_\tau\|
          \le m_*\|f\|_\infty\sqrt{L_J/[\tau(2b+1)]}.                      \tag{26}
\]
In fact use \(A_{f,b}=M_f[1-(1-R/L_J)^b]^{m_*}\). This polynomial has a zero of order \(m_*\) at the origin. Equations (24)–(25) and concatenation realize each monomial \(M_fR^j\) at its own depth \(j\). The order bound \(R\ge \tau P_\tau\) gives \(\|R^{-1/2}P_\tau\|\le\tau^{-1/2}\), by the variational formula for the inverse form and Cauchy–Schwarz against the compressed component. For \(0\le x\le L_J\), the error of the polynomial is at most \(m_*(1-x/L_J)^b\) and \(x(1-x/L_J)^{2b}\le L_J/(2b+1)\) by single-variable maximization. Applying these bounds and then \(R^{-1/2}P_\tau\) proves (26).

**PROVED.** At finite cube \(P_\tau\) has finite rank, so the weak limits in (26) can be replaced to any further operator-norm precision *on this input space* by finite linear combinations of actual local slab insertions. Indeed apply the weak convergence to a basis of \(P_\tau\) as one vector in a finite direct sum of Hilbert spaces. The weak closure of a linear space of such tuples equals its norm closure. For preparation from the vacuum, shorter terms can be padded on their past side by ordinary \(U\) to reach the same depth, since \(U\psi=\psi\). Both the depth and the spatial collar in (26) are independent of the size of the ambient torus. The tolerable norm of a raw insertion is unrestricted.

**PROVED.** For example fix \(0<\alpha<\delta<1\) and let \(a\downarrow0\) in fixed reference length units. Boxes may grow in lattice units subject to \(L_J\le a^{-\alpha}\). For \(b=\lceil a^{-\delta}\rceil\), uniformly bounded \(f\), and \(P_\tau\) carrying physical energies at most a fixed \(A\), take \(\tau=e^{-aA}\). Both the bound in (26) and the physical slab width \(a m_* b\) tend to zero. This admits collars with a sufficiently small positive multiple of \(\log(1/a)\) links. For a box of fixed positive physical side the link count instead grows as \(a^{-3}\). Estimate (26) does not give a vanishing physical width there, or bound the amplitudes of the sources used to prepare a renormalized continuum field.

### The physical long-time estimate

**PROVED.** At fixed cutoff the slab result also identifies every neutral operator in weak closure using \(2m_*+1\) steps and the global temporal means of (18). On the neutral configuration quotient the ordinary one-step kernel is strictly positive and continuous, since averaging the positive continuous Wilson kernel over the compact symmetry group preserves these properties. Multiply that central step on the left and right by arbitrary bounded quotient multipliers obtained at depth \(m_*\). The resulting kernels have the form \(f(X)K(X,Y)g(Y)\). Finite sums of separated bounded functions are dense in \(L^2\) of the product quotient measure, by approximation by rectangle functions. Dividing a rank-one kernel by the bounded-away-from-zero \(K\) shows that every bounded-vector rank-one map is a Hilbert–Schmidt limit of these sums. Finite-rank strong approximation of the identity then gives the full algebra of bounded operators in weak closure. In particular, lack of finite-cutoff observables is resolved on this sector. The construction uses unrestricted norms for the slab insertions.

**OPEN.** Let \(a_j\downarrow0\) be a tuning that gives the required continuum theory, let \(\beta_j\) be its Wilson parameters and take \(b_j=\lceil h/a_j\rceil\). A sufficient estimate for the mass gap on that route is the existence of \(h>0,\ 0<q<1\) and \(j_0\) such that for all \(j\ge j_0\),
\[
 \limsup_{\substack{n\to\infty\\4\mid n}}\
 \lim_{t\to\infty}
 \frac{D_{*,n,\beta_j}(t+b_j)}{D_{*,n,\beta_j}(t)}
            \ \le q .                                                       \tag{27}
\]
The innermost limit is the actual neutral transfer eigenvalue \(r_{+,n,\beta_j}^{b_j}\). The statistic uses ordinary Wilson expectations with the same positive bandwidth in every time shift at the given cutoff. The clause of (27) still to be proved is the strict uniform inequality.

**PROVED, conditional on (27) and continuum matching.** Assume the infinite-volume limits at each cutoff and their subsequent continuum limits match the time translates of a total family of local Osterwalder–Schrader states, including their vacuum subtractions, and yield the nontrivial Yang–Mills theory in the question. A gauge-invariant source supported in a bounded spatial box is neutral on sufficiently large tori. The three centre seams can be moved off that box by vertex centre gauges. For a centered prepared finite-cube vector \(v_{n,j}\), the transfer spectrum gives
\[
 \langle v_{n,j},U^{s+\ell b_j}v_{n,j}\rangle
       \le (r_{+,n,\beta_j}^{b_j})^\ell
                     \langle v_{n,j},U^s v_{n,j}\rangle
 \qquad(s,\ell\in\mathbb N).
\]
Take the thermodynamic limit first, then the continuum limit with \(a_js\to\epsilon>0\), keeping \(\ell\) fixed. By the matching hypothesis the continuum centered vector \(v\) obeys
\[
 \langle v,e^{-(\epsilon+\ell h)H}v\rangle
          \le q^\ell\langle v,e^{-\epsilon H}v\rangle .
\]
If its spectral measure had positive weight on \([0,A]\) for \(A<-\log q/h\), its left side would be at least that weight times \(e^{-(\epsilon+\ell h)A}\), contradicting the bound as \(\ell\to\infty\). Totality makes the corresponding spectral projection vanish on the vacuum orthogonal complement. This formulation allows the state norms at zero padding to depend on the cutoff.

**OPEN.** The absolute error in (12) can exceed the entire low-energy contribution in (15). Endpoint comparison at physical block time fails in the order of volumes required in (27), by (22). The local approximation (26) reconstructs measurements but gives no bound on the normalized time-translate ratio for their centered states. I do not obtain (27), another lower bound on the physical spectral edge, or the continuum construction and full-field identification required by Jaffe and Witten. PROVED in this note denotes an author’s hand argument with its stated hypotheses. The new arguments have no independent review.

RESULT — OPEN for the Jaffe–Witten mass gap. Spatial plaquette histories are cyclic for the finite-cutoff centre-neutral sector. One fixed-depth slab with a temporal mean on each cut detects its exact spectral edge. The uniform physical decay inequality (27) and full continuum matching remain open.
