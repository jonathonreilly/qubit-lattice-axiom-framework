# Repo search

At the pinned checkout `0bdd62338c0b16241714e7de6001172ef6c99153`, the prior file named for this target did not exist. The supplied `library/prior/repo-search-2026-11-08.md` is a search digest for older, unrelated obligations (PI-ADMIT, TPI, M3, GEOH, and others), and contains no hit for the mixed-only corner. Its closest mass-gap entries concern a nontriviality witness and free-field support, not a gauge model on a product of two graphs. The task row supplies no file-level “Repo prior work” hits.

I checked the current lane’s `library/open-registry.md`, the relevant FINISH rows, and existing prior gap-reading notes. There is no registry owner for this literature question. The adjacent `gap-face-alt-read-luna.md` already searched plane-dependent gap theorems, generic anisotropy, 2D models, and strong-coupling ranges, but explicitly records that it did **not** search the route-F4 mixed-only corner. I reuse its general literature results rather than repeat them. `gap-face-exercise-fable.md` identifies the open F4-KP activity/entropy estimate and says the corner was not found in the lane folder; I read its C15/F4 definition and open statement. Thus this target is not covered elsewhere or owned by another registry row.

The lead’s supplied repo-first instruction says main and open YM4D PR branches were searched before queuing; however, this row contains no target-specific hit paths or “Repo prior work” list to inspect. The available November 8 digest is not that search. The closest item-level prior is the Fable exercise’s F4 formulation (reused below), not a proof or a published-model identification. This report records that limitation rather than treating the old digest as evidence of a negative search on main/PRs.

## Provenance and scope

Written by gpt-6-luna high, literature reading for route F4, at pinned checkout `0bdd62338c0b16241714e7de6001172ef6c99153`. Research text only; no proof, audit, or status is granted. No numerical or computer-assisted step is used as proof. No paper was added to the checkout.

The task’s two Sussman–Alpoge source files were fetched once each into the new empty directory `/tmp/sa-gap-mixed-corner-read-luna.xAsar9/`: the 32,992-line outline and 166,711-line CA-I account. I did not read either whole. The indexed outline’s nearby polymer rows (library/sa-index/chunk-01.md: 1153–1174, 1267–1269, 1349–1373) describe a generic finite polymer model: the connected-log theorem is combinatorial, while activity summability and gauge-field application are separate inputs. Its source lines 1120–1373 give the explicit proof of the connected identity, tree cancellation, rooted estimate and K-P condition. Nearby CA-I index chunks 1–11 (indexed items 4.12–4.19) contain no hit on mixed-only surfaces, product-of-graphs homology, or route F4. The CA-I index README’s described scope is multiscale operator reproduction, not a theorem on this corner. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their outline/account text, for this indexed material.

## 1. Mixed-only SU(2) corner in the literature

**Model to identify.** The exercise’s corner is the four-dimensional cubic cell complex with coordinates split into two square-lattice graphs, $A=\mathbb Z^2_{12}$ and $B=\mathbb Z^2_{34}$, and Wilson plaquette terms only on the four mixed orientations $13,14,23,24$. The $12$ and $34$ plaquette couplings are zero; in its notation $(\beta_L,\beta_M,\beta_T)=(0,\beta,0)$. This is a well-defined anisotropic Wilson gauge action on the product cell complex $A\times B$, but not the usual “transverse lattice” Hamiltonian limit: that term normally describes a continuous/quantized longitudinal direction with a transverse spatial lattice and a limiting electric-plus-magnetic Hamiltonian. “Mixed action” is also ambiguous in the literature (often fundamental-plus-adjoint, thin-plus-smeared, or plaquette-plus-rectangle terms), so the phrase alone does not identify this model.

I searched the exact coupling corner and variants of “mixed plaquettes only,” product cell complexes/graphs, omitted plaquette orientations, and transverse-lattice zero-coupling formulations. I found no paper naming this four-dimensional SU(2) probability measure as a studied model and no exact solution or clustering theorem stated for this precise action. General strong-coupling expansions are expected to specialize to zero couplings on two orientations when all remaining plaquette activities are sufficiently small; that is a natural specialization of a local cluster expansion, but I did not find or verify a published theorem with the anisotropic hypotheses and constants written for this corner. It would say nothing about the route-F4 window values. This is a bounded search finding, not proof that no such paper exists. The adjacent gap-face literature note likewise found no rigorous gap/bridge for an anisotropic face, but did not cover this particular four-mixed-orientation corner.

There is a useful contrast, not a result for F4: K. Osterwalder and E. Seiler’s 1978 paper proves strong-coupling infinite-volume analyticity and Wilson confinement for lattice Yang–Mills, and the later open paper of Shen, Zhu and Zhu gives an explicit small-coupling SU(N) region. Both concern the ordinary all-orientation isotropic model, not the four-orientation corner. For the latter paper, in its convention the SU(N) condition is \(|\beta|<1/[16(d-1)]\); for $(d,N)=(4,2)$ this is $1/48$. This does not transfer to β near 2.3–2.6 in the corner. Its proof is written for SU(2), but not for the anisotropic product-cell action. The full Osterwalder–Seiler paper was not accessible as an open copy in this pass; I rely only on its publisher abstract and the authors’ account in Shen–Zhu–Zhu’s introduction, and assign it no numerical endpoint.

## 2. Closed mixed surfaces and the Künneth form

There is a direct standard cellular statement for the product of two graphs. Give each graph its 1-dimensional CW structure. The product CW chain complex has

\[
C_2(A\times B)=C_1(A)\otimes C_1(B),\quad
C_1(A\times B)=(C_1(A)\otimes C_0(B))\oplus(C_0(A)\otimes C_1(B)),
\]

with $\partial(e\otimes f)=\partial e\otimes f-e\otimes\partial f$. There are no 3-cells, so 2-cycles are precisely $H_2(A\times B)$ at the chain level. The integral Künneth theorem (the graph chain groups are free, hence the Tor terms vanish) gives

\[
H_2(A\times B;\mathbb Z)\cong H_1(A;\mathbb Z)\otimes H_1(B;\mathbb Z),
\]

because each graph has $H_2=0$. For finite-support chains on the infinite square-lattice graphs, take the algebraic direct-limit version; the formula remains valid. Over $\mathbb F_2$, signs disappear and the same statement holds.

For $A=B$ equal to the square grid viewed as a graph (with no square 2-cells in either factor), finite 1-cycles in each factor have the unit-square boundaries as a basis. Hence the mixed 2-cycle group has basis \(\partial P\otimes\partial Q\), indexed by pairs of unit squares, and each finite mod-2 closed mixed surface has a unique finite subset of these generators. Each generator is the 16-plaquette hypercube shell from the F4 complex. This is the homological meaning of the C15 statement already in the exercise note; I am reusing that result, not claiming it as a newly checked proof. The formula is about the cellular 2-cycle space. By itself it supplies no bound on the number or activity of larger labeled surfaces, and no convergence or clustering result.

A relevant open treatment is Oliver Knill, “The Künneth formula for graphs,” which uses a particular Cartesian product graph and discrete cohomology. The safest match for F4 is the ordinary product CW complex and its cellular chain tensor product above; graph-theoretic products can mean other constructions. The formula is exact in that CW setting, but its proof is general algebraic topology and is not a gauge-theory proof.

## 3. Kotecký–Preiss and the clustering implication

### Criterion

For a finite or countable abstract polymer system $(\mathcal P,\not\sim,z)$, assume incompatibility is symmetric and reflexive (each polymer is incompatible with itself), and define

\[
Z=\sum_{\mathcal F\text{ compatible}}\prod_{X\in\mathcal F}z_X.
\]

A clean sufficient Kotecký–Preiss condition is: there is a nonnegative function $a_X$ such that

\[
\sum_{Y:Y\not\sim X}|z_Y|e^{a_Y}\le a_X\qquad (X\in\mathcal P).
\]

Then the connected Mayer/Ursell series for \(\log Z\) converges absolutely; for a finite system it defines the branch with \(\log Z(0)=0\), and $Z\ne0$. The rooted absolute connected-cluster sum at root $X$, with the root activity omitted and the usual (1/(n-1)!) labeling factor, is at most $e^{a_X}$. For countable systems the same rooted estimate holds under the criterion; an infinite-volume total partition function or total unrooted logarithm need not be finite. A weighted form replaces $a_Y$ by $a_Y+b_Y$ in the exponential and yields rooted cluster bounds weighted by $e^{\sum b_Y}$.

Hand proof outline: expand $\log Z$ formally into connected incompatibility graphs; an edge-ordering sign-reversing involution cancels all connected edge sets except spanning trees; root each tree at $X$; the tree sum is bounded by the increasing recursion $T_X^{(0)}=1$, $T_X^{(h+1)}=\exp(\sum_{Y\not\sim X}|z_Y|T_Y^{(h)})$. Induction using K-P gives $T_X^{(h)}\le e^{a_X}$. Monotone convergence bounds the full rooted tree series, hence the connected series. Scaling activities by $t\in[0,1]$, exponentiating the series near zero, and using the identity theorem proves $Z=e^{\log Z}\ne0$ on the full activity segment. These are the proof steps the local outline spells out at lines 1150–1348 (credited above); it is an abstract polymer proof and does not construct F4 activities.

For F4, if polymer supports are plaquettes and two polymers are incompatible when their supports intersect, the row’s proposed bound

\[
\sup_p\sum_{\gamma\ni p}|w(\gamma)|e^{a|\gamma|}\le a
\]

implies the standard criterion with $a_\gamma=a|\gamma|$: an incompatible γ′ must contain at least one plaquette of γ, so sum over its at most |γ| plaquettes and apply the displayed rooted bound. This implication requires the proposed polymers and incompatibility relation to be the actual polymer representation of the partition function. It does not prove that this activity bound holds.

### From convergent polymers to exponential clustering

The precise conditional statement is: suppose the finite-volume expectation of each local observable is represented by a local insertion/marked-polymer expansion with a common, volume-independent absolute majorant; the unmarked polymers satisfy a weighted K-P condition; and every term contributing to the truncated two-observable correlation is a connected incompatibility cluster meeting both supports. If a cluster connecting supports at lattice distance $r$ has total weighted geometric cost at least $\mu r$ (for example, use $b_\gamma=\mu\,\mathrm{diam}(\operatorname{supp}\gamma)$ in the weighted criterion), then the rooted cluster bound gives

\[
|\langle FG\rangle-\langle F\rangle\langle G\rangle|\le C(F,G)e^{-\mu r},
\]

where $C(F,G)$ is the product/combination of the two local insertion majorants and the K-P rooted constants; it is independent of volume. Locality of supports, a connected cluster representation, and differentiability/majorants for the inserted observables are hypotheses. K-P convergence of the partition-function logarithm alone does not furnish those observable representations or their constants. In a lattice gauge expansion one must also show the character/intertwiner expansion has the required polymer form, account for gauge constraints and Haar integrations, and verify the weighted activity and marked-observable bounds for the chosen boundaries. The SU(2) result of Shen–Zhu–Zhu shows a rigorous exponential covariance estimate for the isotropic strong-coupling model by a different stochastic-curvature/Poincaré method; it does not prove this implication for F4.

## Sources and access

- K. Kotecký and D. Preiss, “Cluster Expansion for Abstract Polymer Models,” *Commun. Math. Phys.* 103 (1986), 491–498. The original text is openly readable at [the UCLA-hosted PDF](https://www.math.ucla.edu/~biskup/290k.1.24w/PDFs/Kotecky-Preiss.pdf). Its Theorem (pp. 492–493) gives nonvanishing, the connected logarithm, and the weighted rooted estimate; its following proposition treats correlation decay from weighted cluster sums. This is the criterion source, not a gauge-model application.
- Salvador Miracle-Solé, “A Lecture on Cluster Expansions,” [arXiv:1206.3642](https://arxiv.org/abs/1206.3642), 9 pages, complete proofs for an abstract polymer system. It is a readable short proof reference but is not by David Brydges.
- H. Shen, R. Zhu and X. Zhu, “A stochastic analysis approach to lattice Yang–Mills at strong coupling,” [arXiv:2204.12737](https://arxiv.org/abs/2204.12737), 43-page open PDF read from the arXiv source. For SU(N), their Assumption 1.1 is \(|\beta|<1/[16(d-1)]\); Corollary 1.6 gives exponential covariance decay for disjointly supported smooth cylinder functions, with constants depending on support sizes and a positive curvature/contractivity constant. It explicitly includes SU(2) and $d=4$. The proof proceeds through Langevin dynamics, uniform-in-volume functional inequalities, and a locality estimate for the semigroup, not the proposed F4 contour sum.
- K. Osterwalder and E. Seiler, “Gauge Field Theories on a Lattice,” *Ann. Phys.* 110 (1978), 440–471, [publisher record](https://doi.org/10.1016/0003-4916(78)90039-8). The publisher abstract says strong-coupling infinite-volume existence/analyticity and Wilson’s confinement bound; direct PDF retrieval returned 403, so full paper and exact constants were not read.
- Erhard Seiler, *Gauge Theories as a Problem of Constructive Quantum Field Theory and Statistical Mechanics*, LNP 159 (1982), [Springer record](https://doi.org/10.1007/3-540-11559-5). The record identifies the lattice-gauge chapter (pp. 3–98), but marks the book as subscription content; no full chapter was read.
- David Brydges, “A Short Course on Cluster Expansions,” in *Critical Phenomena, Random Systems, Gauge Theories* (Les Houches 1984), pp. 129–183 (1986). I found bibliographic records and a third-party viewer, but did not rely on or download that copy as a verified open source. The accessible Miracle-Solé paper and the complete proof in the Sussman–Alpoge outline provide the hand-rebuildable generic argument here.
- Oliver Knill, “The Künneth formula for graphs,” [arXiv:1505.07518](https://arxiv.org/abs/1505.07518), for a discrete graph-cohomology product. The product convention differs from the product CW cell complex stated above, so I use it only as related terminology.

All downloaded papers were kept in new empty scratch directories under `/tmp`; no sign-in or paywall bypass was used. Shell retrieval of the UCLA K-P URL returned 404 during this pass, although the source is readable through the linked PDF viewer; the arXiv PDFs for Brydges-adjacent Miracle-Solé and Shen–Zhu–Zhu were downloaded into `/tmp/sa-gap-mixed-corner-sources.DYfIQl/`. Osterwalder–Seiler and Seiler full texts could not be read. No route-F4 literature hit was found for the special mixed-only action.

Credits: Kotecký and Preiss; Osterwalder and Seiler; Erhard Seiler; David Brydges; Hao Shen, Rongchan Zhu and Xiangchan Zhu; Oliver Knill; and Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their outline/account text.

RESULT: No published result for the four-mixed-orientation SU(2) corner was found in this bounded search. Its 2-cycles are the Künneth tensor products of the factors’ 1-cycles; this explains the C15 hypercube-shell basis but does not bound labeled-surface entropy. K-P supplies a hand-rebuildable, volume-independent rooted cluster criterion, and exponential clustering follows when local observable insertions and distance-weighted connected-cluster bounds are also verified. The generic criterion is not an F4 activity proof; F4-KP remains open, and no proof status is granted.
