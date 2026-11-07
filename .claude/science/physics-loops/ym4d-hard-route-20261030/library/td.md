# TD: distance rates, composition, and natural-scale convergence

Provenance: Codex, pass 2 of Claude's `td-draft.md`, read in full at checkout `413f26e3cfff32fab4ed0a60c1aa3877b5c465e8`; research text, not an audit, no status granted. Source text credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as its authors, revision `31a47c543775`. Not yet refereed.

The main result is Theorem 10. It gives a conditional response, composition and gas theorem. It does **not** establish the draft's counterexample to ordinary-distance TD, or its filing of the new gas into the existing boundary class. The latter obstruction occurs in Theorem 9, at the attempted conclusion of draft Theorem 10.2. All proofs below are written arguments.

## Definitions and hypotheses

Fix a finite main-step history, its input structure \(\sigma\), its gas region \(\Lambda\), and its open complex input fibre \(\mathcal O_\sigma(U)\). The real factor \(U\) and near stored variables are fixed. Here \(\mathcal O_\sigma\) has precisely the chain-domain, working-core and ceiling requirements of `ci-form-draft.md`, Definition 1.1, under NL1-L's radius design \((Tq0)\). No theorem below constructs this domain or the actual response on it.

Fine cubes have side \(M\) at level \(i-1\); coarse cubes have side \(LM\). Their graph adjacency is contact along any face, including a corner. The fine graph has degree at most \(80\). Write \(d\) for its graph distance, \(\operatorname{St}(A)\) for the least edge count of a tree containing a nonempty set \(A\), and \(\operatorname{MST}(A)\) for the minimum spanning-tree weight on \(A\), with edge weights \(d\). Distances on a torus are periodic. All sets and sums before the cluster logarithm are finite.

Let \(I\) be the free bonds assigned to gas cubes. A complex fluctuation \(\zeta\) has coordinates \(\zeta_{b,a}\), \(b\in I\); put \(|\zeta|_c=\max_{b\text{ assigned to }c,a}|\zeta_{b,a}|\), with value zero on an empty cube. The mask \(\zeta\mathbf1_A\) retains exactly the coordinates assigned to cubes in \(A\). All graph lengths below are in the specified cube units; transferring a different source length convention requires its fixed comparison factor in the early geometric constants.

For a nonempty read set \(X\), let
\[
 m_X(W)=\operatorname{MST}(W\cup\{*\};\ w(c,c')=d(c,c'),\ w(c,*)=d(c,X)).                 \tag{1}
\]
These are the specified edge weights; we do not assume their triangle inequality after collapsing \(X\). For a function of cube variables, define its Boolean difference
\[
 D_WF(\zeta)=\sum_{A\subset W}(-1)^{|W\setminus A|}F(\zeta\mathbf1_A),\qquad W\ne\varnothing.       \tag{2}
\]
It is local in the variables \(\zeta\). This definition makes no assertion about locality in the external pair.

**R — response and completed source.** Import the following strengthened form of ST1's DR, uniformly on \(\mathcal O_\sigma(U)\). It uses `(DR-ζ)`, `(DR-loc)` of `nl1-L-draft.md` 259–267, with the explicit row-space and stencil clauses below; it is not a conclusion of frozen P82.

* A shift \(h(s;P,S)\) is jointly holomorphic for \(|s_c|<e^{\bar\kappa}\), \(\|S\|_{\rm src}<s_D=\epsilon_D e^{-c_D\bar\kappa}\), vanishes at \(S=0\), and satisfies
  \[
  n_b(h)\le C_D E_{\bar\kappa}\|S\|_{\rm src}e^{-\mu_R d_+(b,\operatorname{supp}S)}.                \tag{3}
  \]
  Here \(n_b(H,K)=\max\{l|H|,l^2|\nabla^UH|,l^3|K|\}\) is a seminorm at fixed \(U\). Its stencil lies in a connected set \(B_b\) of at most 16 fine cubes containing the initial-site cube \(\Delta_b\). The source domain is the full ball in the product of assigned row spaces, invariant under row masks and independent complex scalings within that ball. Its norm is the maximum of row norms; sources on disjoint cube rows therefore have maximum norm. The metric \(d_+\) is ST1's input layer metric, distinct from \(d\).
* On each face-connected component of \(\operatorname{supp}s\), the response reads only the source rows and switch values of that component. In particular, when \(B_b\subset\operatorname{supp}s\), its stencil reads only components meeting \(B_b\). Reality, restriction and the physical identification at \(s=1\) are separate parts of this import.
* The main-step source is \(S(v)\), with \(v=v_0+u(s\odot\zeta)\), \(u\) linear and cube-local, \(\|u(\zeta)\|_\infty\le c_Tg\|\zeta\|_\infty\). It is holomorphic on \(\|v\|_\infty<c_{\rm ch}L^{-9}\), has Lipschitz constant \(C_A\), and \(\|S(v_0)\|_{\rm src}\le C_A\delta_{\rm src}\). Each source row reads only its cube and its first graph-neighbour layer, by \(M\ge R_\sigma+3\). All these sources are supported in a fixed set \(\mathcal S\).

Put \(\ell=\log\theta_{i-1}\), \(g=e^{-\ell/2}\), \(\mathfrak b=A_1\ell^{p_0}\), \(R=\ell^q\), \(q>p_0>0\), and \(\delta_{\rm src}=A_1g\ell^{p_0}\). Assume \(C_A\delta_{\rm src}<s_D/2\) and \(\|v_0\|_\infty<c_{\rm ch}L^{-9}/2\). Define
\[
\begin{split}
 D&=e^{\bar\kappa}-1,\quad Q=6400/D\le\tfrac12,\quad a=\tfrac12\log(D/6400),\quad \delta=(8e)^{-1},\\
 \varrho&=\frac{\min\{s_D/2,C_Ac_{\rm ch}L^{-9}/2\}}{c_TC_Ae^{\bar\kappa}g},\\
 h_0(P)&=h(\mathbf1;P,S(v_0)),\\
 G(s,\zeta)&=h(s;P,S(v_0+u(s\odot\zeta)))-h(s;P,S(v_0)),\\
 A_R&=4C_DE_{\bar\kappa}s_DD^{15},\qquad
 A_V=C_DE_{\bar\kappa}C_A(3\delta_{\rm src}+c_Tge^{\bar\kappa}R),\\
 K_1&=\max\{1,4A_R/A_V\},\qquad
 \beta_c(\zeta)=2K_1|\zeta|_c/\varrho,\qquad
 \vartheta=4K_1\mathfrak b/(\delta\varrho).
\end{split}                                                                        \tag{4}
\]
The notation \(a\) here is a response rate. The gas amplitude below is \(\mathfrak a\).

**A — admission and amplitudes.** For each old exempt term \(f\), specify a nonempty set of complete reads \(\mathcal B_f\), \(X(f)=\{\Delta_b:b\in\mathcal B_f\}\), and a presentation set \(X_f\supset X(f)\). On
\[
 \mathcal A_f(P)=\{h:n_b(h)<A_b:=A_Ve^{-\mu_Rd_+(b,\mathcal S)}\ (b\in\mathcal B_f)\}
\]
the map \(\Phi_f(P,h)=f(\rho_X^{\rm res}(P\dotplus h^\delta);\mathfrak q_X)\) must be jointly holomorphic and have its declared bound. For two-sided terms use \(|\Phi_f|\le b_f\); for kept forms use pair oscillation \(\le\omega_f\). For an island use \(\operatorname{Re}\Phi_f\le A_f\) and the **additional uniform hypothesis**
\[
 A_f-\operatorname{Re}\Phi_f(P,h_0(P))\le B_f\quad(P\in\mathcal O_\sigma(U)).              \tag{5}
\]
Set \(\widetilde\omega_f=2b_f,\omega_f,2B_f\), respectively.

Admission is the arbitrary-shift reading of NL1-L, Theorem V′, Steps 3–7. Those steps apply when all endpoint pillars, their read sets and pin stencils are included: (3) forces levelling, ST1 Lemma 4 bounds the pinned shift, and its half-gap inclusion puts every read in the target domain. They use the shift bound, not its response equation. This justifies A **conditional on those complete reads, V1–V6, and the ST1/ST3 admission hypotheses**. It does not create the missing response or activity domains.

**Outstanding — complex island amplitude.** NL1-L 487 establishes a real base value only at a real input pair. At complex \(P\), \(h_0(P)\) and \(\Phi_f(P,h_0(P))\) need not be real. PAN's quadratic estimate is also stated for real pairs. Neither supplies (5) uniformly on the complex fibre. A one-sided bound alone is insufficient: \(-N(1+z/2)/(1-z/2)\) has negative real part on \(|z|<2\), yet changes by \(-2N\) between zero and one. All island conclusions below therefore require (5), with the polynomial bound in X below.

**X — carriers and sizes.** Each exempt term has a number \(d_f^{\rm old}\ge0\) and amplitude \(\widehat\omega_f\) such that
\[
 \widetilde\omega_f\le\widehat\omega_f e^{-\kappa d_f^{\rm old}},\qquad
 \sup_c\sum_{f:X(f)\ni c}\widehat\omega_f e^{-(\kappa/2)d_f^{\rm old}}
 \le N_{\rm ex}\le C_{\rm ex}(M)\ell^{t_{\rm ex}}.                       \tag{6}
\]
Boundary and kept-form lengths are their supplied SA relative lengths; island lengths are zero; ordinary remainders keep their full lengths. This imports PAN's per-cube `(N-B)`, `(N-K)` and the other kind bounds, **uniformly in the complex pair**, with (5) for islands. Their derivation for the actual construction is not proved here.

**G — separated hubs and projection.** Let \(H\) be the standing-island hulls and \(\widetilde H=N_2(H)\). Distinct hubs are at distance at least \(s_0=\check R_i-4\), each lies in a box of side \(D_H=C_0L\check R_i+6\), and gas cubes have distance at least \(G_0=10L\check R_i-2\) from every hub and the live set. These are PAN's `(G-gap)`, `(G-isl)`, `(G-sep)`, retained as LF1 geometry imports.

The graph \(\Gamma^\natural\) contracts **each entire hub** to one vertex. Cube edges remain; a cube outside the hubs is adjacent to a hub when its distance from it is one. Write \(\pi\) for contraction and
\[
 \ell^\natural(W)=\operatorname{St}_{\Gamma^\natural}(\pi W),\qquad
 r_H=\lfloor(s_0-3)/2\rfloor.
\]
Require
\[
 r_H\ge257L,\quad 4\log(D_H+3)\le r_H,\quad
 8\log(D_H+3)\le s_0-2,\quad G_0-1\ge s_0-2,                          \tag{7}
\]
and the carrier hypotheses
\[
 \operatorname{St}_{\Gamma^\natural}(\pi X_f)\le C_{\rm pr}(1+d_f^{\rm old}),
 \qquad X_f\text{ meets a hub or the live set}.                         \tag{8}
\]
Here \(C_{\rm pr}\ge1\) is uniform in \(L,M,\kappa,\bar\kappa\). The graph length \(\ell^\natural\) is a new definition, **not** SA's relative-tree length. Projecting a supplied covering tree and then contracting its covered islands proves (8) if all read enlargements fit its fixed collar. The asserted containment and the uniform projection constant remain a carrier-geometry import; the sentence defining SA's relative length alone does not prove them.

## Response and composition

**Lemma 1 (tree bounds and cost shares).** The following bounds hold on the fine cube graph.

1. Rooted connected sets of \(n\) cubes number at most \(6400^{n-1}\). Also \(\operatorname{St}(A)\le\operatorname{MST}(A)\le2\operatorname{St}(A)\), and, for \(t\ge6\),
   \[
   \sup_x\sum_y e^{-td(x,y)}\le2,\qquad
   \sum_{|A|=n}e^{-t\operatorname{MST}(A\cup\{x\})}\le2(2e)^n.          \tag{9}
   \]
2. A minimum spanning tree of any finite nonnegatively weighted complete graph, rooted at \(*\), assigns each nonroot vertex the weight \(l_c\) of its parent edge. Then
   \[
   \sum_cl_c=\operatorname{MST},\qquad
   \sum_{c\in A}l_c\le\operatorname{MST}(A\cup\{*\}).                 \tag{10}
   \]
   This is Bird's allocation. In particular for (1), the latter weight is at most \(\operatorname{MST}(A\cup\{x\})\), for every \(x\in X\).
3. \(m_X(W)\ge d(c,X)\) for \(c\in W\). There is a fine subgraph with at most \(m_X(W)\) edges joining each cube of \(W\) to some cube of \(X\).

*Proof.* A rooted spanning tree has a depth-first walk of \(2(n-1)\) steps, each with at most 80 choices; a canonical choice gives an injection from sets to walks. Realizing MST edges as geodesics proves the first tree comparison. Doubling a Steiner tree and listing terminals by first visit proves the second. Since \(2n+1\le3^n\) for \(n\ge1\), the distance sum is bounded by \(1+\sum_{n\ge1}(81e^{-6})^n<2\). Here \(e>8/3\), by its first five Taylor terms, proves \(e^6>162\) without a numerical evaluation. For \(n\) ordered vertices distinct from \(x\), sum over rooted labelled trees and then over their leaves' positions. There are at most \(n^n\) parent maps, each positional sum costs at most \(2^n\), and division by \(n!\), using \(n^n/n!\le e^n\), gives \((2e)^n\). Sets containing \(x\) contribute at most \((2e)^{n-1}\).

For (10), deleting the parent edge of \(c\) gives its descendant cut. Every edge crossing this cut has weight at least \(l_c\), or replacing the parent edge would lower the tree weight. Fix a threshold \(u\). Each \(c\in A\) with \(l_c>u\) lies in a distinct nonroot component of the threshold graph on \(A\cup\{*\}\): its component cannot cross its descendant cut, and two such components equal would put each vertex below the other. The count is thus at most the number of threshold components minus one. In any minimum tree that number equals the number of tree edges of weight \(>u\), by the same cut argument. Integrate these step functions in \(u\). This proves (10). Replacing a root \(x\in X\) by \(*\) decreases edge weights; if \(x\in A\), retain it and add its zero root edge.

Finally, the path to \(*\) in a tree for (1) has weight at least \(d(c,X)\). Realize its ordinary edges as geodesics and each root edge by a path to a nearest point of \(X\). Their union has the asserted edge count. ∎

**Lemma 2 (DR-row).** Under R, for sources \(S_c\) on distinct cube rows, \(\|S_c\|_{\rm src}<s_D/2\), \(S_W=\sum_{c\in W}S_c\), and \(\varnothing\ne W\),
\[
 n_b\!\left(\sum_{A\subset W}(-1)^{|W\setminus A|}h(\mathbf1;P,\sum_{c\in A}S_c)\right)
 \le C_DE_{\bar\kappa}s_DD^{15}e^{-\mu_Rd_+(b,\operatorname{supp}S_W)}
       Q^{\operatorname{St}(W\cup\{\Delta_b\})}
       \prod_{c\in W}\frac{4\|S_c\|_{\rm src}}{s_D}.                 \tag{11}
\]
For \(\|\zeta\|_\infty<\varrho\), the main-step increment in (4), \(G_W=D_WG(\mathbf1,\cdot)\), satisfies
\[
 n_b(G_W(\zeta))\le A_Re^{-\mu_Rd_+(b,\mathcal S)}
       Q^{\operatorname{St}(W\cup\{\Delta_b\})}
       \prod_{c\in W}\frac{2|\zeta|_c}{\varrho}.                    \tag{12}
\]

*Proof.* Hold switches on \(B_b\) at one. Repeated fundamental theorem of calculus expands the response into coefficients indexed by \(Y\supset B_b\), with one integrated switch derivative for each cube of \(Y\setminus B_b\). The response bound on \(|\tau_c|<s_D/(2\|S_c\|)\) is \((C_DE_{\bar\kappa}s_D/2)e^{-\mu_Rd_+}\). Cauchy circles about \([0,1]\), with radii increasing to \(D\), bound the \(Y\)-coefficient by this number times \(D^{-|Y\setminus B_b|}\). Component locality makes its stencil zero unless \(Y\) is graph-connected, and makes it independent of source variables outside \(Y\). Its \(W\)-difference consequently vanishes unless \(W\subset Y\). That difference is bounded by \(2^{|W|}\) times the coefficient bound and vanishes on every source coordinate hyperplane. Repeated one-variable Schwarz supplies \(\prod_c(2\|S_c\|/s_D)\). This argument for a seminorm follows by applying scalar linear functionals to its finite-dimensional readout.

Set \(n_0=\operatorname{St}(W\cup\{\Delta_b\})+1\). Lemma 1 gives
\[
 \sum_YD^{-|Y\setminus B_b|}
 \le\sum_{n\ge n_0}6400^{n-1}D^{16-n}
 \le2D^{15}Q^{n_0-1}.
\]
This proves (11), including the zero-source cases by cancellation.

For (12), apply the same proof to \(G(s,\zeta)\), using independent coordinate radii \(\varrho/|\zeta|_c\). Formula (4) keeps both completed sources in their source balls and the datum in its chart. Their difference has seminorm at most \(2C_DE_{\bar\kappa}s_De^{-\mu_Rd_+}\). The source on a switch component reads only that component's first neighbour layer. After masking, cubes outside \(Y\) vanish. A distinct graph component of \(Y\) cannot be in that neighbour layer. Thus both independence outside \(Y\) and the connectedness cancellation still hold. Schwarz and the last displayed sum prove (12). ∎

**Lemma 3 (composition).** Let \(\Phi\) be holomorphic on
\(h_0+\{v:n_b(v)<A_b/4\ (b\in\mathcal B)\}\), with
\(|\Phi-\Phi(h_0)|\le\omega\). Put \(X=\{\Delta_b:b\in\mathcal B\}\).
Suppose \(a\ge12\), \(0<\beta_c<\delta\), and fixed shifts satisfy
\[
 n_b(g_A)\le(A_b/4)\prod_{c\in A}\beta_c\,
              e^{-a\operatorname{MST}(A\cup\{\Delta_b\})}.
\]
For \(t^A=\prod_{c\in A}t_c\) and \(F(t)=\Phi(h_0+\sum_{A\ne\varnothing}t^Ag_A)\),
\[
 |D_WF(\mathbf1)|\le\omega\prod_{c\in W}(2\beta_c/\delta)
                  e^{-(a-6)m_X(W)}.                                 \tag{13}
\]
There is no factor counting the reads.

*Proof.* Use the parent costs \(l_c\) for (1), and radii
\(r_c=(\delta/\beta_c)e^{(a-6)l_c}>1\). On this polydisc, (10) bounds each shift term by
\((A_b/4)\delta^{|A|}e^{-6\operatorname{MST}(A\cup\{\Delta_b\})}\).
Its sum is at most \((A_b/4)2\sum_{n\ge1}(2e\delta)^n=(A_b/4)(2/3)\), by (9). Thus \(F\) is admitted at every read. The function
\(\sum_{A\subset W}(-1)^{|W\setminus A|}[F(t\mathbf1_A)-\Phi(h_0)]\)
vanishes on all coordinate hyperplanes and is bounded by \(2^{|W|}\omega\). Repeated Schwarz at \(t=\mathbf1\) gives \(2^{|W|}\omega\prod r_c^{-1}\). Now use \(\sum l_c=m_X(W)\). The hull-product device is the one used for individual strings in YM3-I 52582–52589. ∎

**Lemma 4 (one-term bound, TD′).** Under R and A, if \(a\ge12\) and \(\beta_c(\zeta)<\delta\), then
\[
 |D_W[\Phi_f(P,h_0+G(\mathbf1,\cdot))](\zeta)|
 \le\widetilde\omega_f\prod_{c\in W}(2\beta_c(\zeta)/\delta)
                   e^{-(a-6)m_{X(f)}(W)}.                              \tag{14}
\]

*Proof.* From (3)–(4), \(n_b(h_0)\le A_b/3\), so the radius-\(A_b/4\) ball about \(h_0\), even doubled radially, lies in \(\mathcal A_f\). Two-sided and oscillation bounds give the required difference bound immediately. For an island, put \(\psi(z)=\Phi_f(P,h_0+zv)-\Phi_f(P,h_0)\), \(|z|<2\). Then \(\psi(0)=0\), \(\operatorname{Re}\psi\le B_f\). If \(B_f=0\), the harmonic maximum principle gives \(\psi=0\). Otherwise \(\psi(2z)/(2B_f-\psi(2z))\) maps the unit disc to the closed unit disc and vanishes at zero. Schwarz at \(1/2\) gives \(|\psi(1)|\le2B_f\). This proves the required Borel–Carathéodory bound without assuming the base value is real.

By Lemmas 1–2 and (4), \(n_b(G_A)\le(A_b/4)\prod_{c\in A}\beta_c\,e^{-a\operatorname{MST}(A\cup\{\Delta_b\})}\). Boolean inversion gives \(G(\mathbf1,\zeta\mathbf1_B)=\sum_{\varnothing\ne A\subset B}G_A(\zeta)\). Apply Lemma 3. A zero cube coordinate gives zero by cancellation, or by the limit from positive \(\beta_c\). ∎

**Theorem 5 (TD-natural, conditional).** Assume R, A, X, G and
\[
 \lambda_V\le\kappa/(4C_{\rm pr}),\quad a-6\ge\lambda_V+12,
 \qquad \vartheta<1.                                                  \tag{15}
\]
Define \(f_W\) by (14) and \(V^{\rm ex}(W)=\sum_ff_W\). Then, on the real box \(|B(b)|<\mathfrak b\), uniformly in \(P\),
\[
 \begin{split}
 |V^{\rm ex}(W;P,B)|&\le\mathfrak a_{\rm ex}e^{-\lambda_V\ell^\natural(W)},\\
 \mathfrak a_{\rm ex}&=2e^{\kappa/4}N_{\rm ex}\vartheta
       e^{-\nu(G_0-1-C_{\rm pr})},\qquad
 \nu=\min\{\kappa/(8C_{\rm pr}),(a-6-\lambda_V)/2\}.
 \end{split}                                                          \tag{16}
\]
Moreover \(\sum_WV^{\rm ex}(W)=\sum_f[\Phi_f(P,h_0+G(\mathbf1,B))-\Phi_f(P,h_0)]\) exactly. The terms are holomorphic in \(P\), real at real data, and local in \(B\) on \(W\). They need not be local in \(P\) on \(W\). Under RUN's radius growth below, \(\mathfrak a_{\rm ex}\to0\) as the coupling ceiling tends to zero.

*Proof.* Write \(m_f=m_{X(f)}(W)\), \(d_f=d_f^{\rm old}\). Join the graph of Lemma 1(3) to a tree covering \(\pi X_f\). This proves
\[
 \ell^\natural(W)\le m_f+C_{\rm pr}(1+d_f).
\]
The same connected union joins a gas cube to a hub or the live set. Until its first such contact it is an ordinary cube path, so it has at least \(G_0-1\) edges. Therefore \(m_f+C_{\rm pr}d_f\ge G_0-1-C_{\rm pr}\). Multiplying (14) by \(e^{\lambda_V\ell^\natural(W)}\) and using (15) gives
\[
 e^{\lambda_V\ell^\natural(W)}|f_W|
 \le e^{\kappa/4}\vartheta\,\widehat\omega_f e^{-(\kappa/2)d_f}
 e^{-\nu(G_0-1-C_{\rm pr})}e^{-(a-6-\lambda_V)m_f/2}.
\]
Fix \(c\in W\) and assign \(f\) to a nearest cube of \(X(f)\). Lemma 1(3), (6), and (9) sum the last two \(f\)-dependent factors to at most \(2N_{\rm ex}\). This proves (16). Finite Boolean inversion gives exactness; finite composition gives the remaining analytic assertions.

With all earlier parameters fixed, \(\varrho=c(\bar\kappa)/g\) and \(A_V\ge c'(\bar\kappa)g\ell^q\). Consequently
\(\vartheta\le C(\bar\kappa)(g\ell^{p_0}+\ell^{p_0-q})\to0\).
The uniform lower bound \(\check R_i\ge(\ell-1)^r\), \(r\ge2\), is the running-minimum/frame bound used in PAN, and is an additional part of RUN. Thus the exponential in (16) dominates the polynomial (6). For example \(e^x\ge x^n/n!\), with a fixed integer \(n\) large enough, proves the limit. Hence \(\mathfrak a_{\rm ex}\to0\). ∎

## The linked gas

**J — actual gas input.** The ordinary potential types have connected fine supports and decay length \(\ell_t(Y)=\operatorname{St}(Y)\). The exempt type has \(\ell_{\rm ex}=\ell^\natural\). Combine origins within each of a fixed number of types. Assume, uniformly in \(P\),
\[
 |V_t(Y;P,B)|\le\mathfrak a_t e^{-\lambda_V\ell_t(Y)}
       \left(1+M^{-4}\sum_{b\subset Y}|B(b)|^2\right),\qquad
 \mathfrak a=\sum_t\mathfrak a_t.                                     \tag{17}
\]
Theorem 5 supplies the exempt bound without the quadratic allowance. For ordinary terms, (17) imports `ci-form-draft.md`, Proposition 5.3 and Lemma 5.4, including `(Size)` and `(W-in′)`. An optional inserted type requires its own such bound and connected collar; no insertion is needed for CI at zero source.

Write \(Y^\sharp\) for the coarse cubes meeting the first fine neighbour layer of \(Y\). A selected tagged family \(\mathbf D\) and distinct failed bonds \(P_0\) define
\[
 F_\iota=(-1)^{|P_0|}\chi_{Y_0}\prod_{b\in P_0}(1-\chi_b)
                 \prod_{Y\in\mathbf D}(e^{V(Y)}-1),                  \tag{18}
\]
where \(Y_0\) comprises the box-required free bonds, \(P_0\cap Y_0=\varnothing\), and \(\chi_b=\mathbf1_{\{|B(b)|<\mathfrak b\}}\). Set this integrand to zero outside \(\chi_{Y_0}=1\). Let \(Z_0\) include **all** selected supports and failed bonds. For every coarse set \(Z\supset Z_0^\sharp\), define
\[
 T(Z,\iota)=\int_{[0,1]^{Z\setminus Z_0^\sharp}}
       \partial_{s_{Z\setminus Z_0^\sharp}}\mathcal J(Z_0;s_Z;P)[F_\iota]\,ds,             \tag{19}
\]
with \(s_Z=1\) on \(Z_0^\sharp\) and zero off \(Z\).

Import the matrix, Gaussian-comparison and structural parts of H-M of frozen `in1.md` 97–108 for these **assigned** functionals and supports. Do not import its UM counting or logarithm conclusion. Explicitly, uniformly on independent coarse switch discs of radius \(e^{\bar\kappa}\), require joint holomorphy, perturbation \(\varepsilon\le\varepsilon_0(K_0)\), local dimension \(m\le c_m(LM)^4\#Z\), and
\[
 |\mathcal J[F]|\le F_*\exp\{A_{K_0}(\varepsilon+\rho+\gamma_{\rm tilt}/2)m
                   -\gamma_{\rm tilt}\mathfrak b^2|P_0|/2\}
\]
for the actual integrands bounded by \(F_*e^{\rho|B|^2}\), including their distinct failed tests, whenever \(\rho+\gamma_{\rm tilt}/2\le\rho_0(K_0)\). IN1 Lemma 3's choices must give \(C_0^{\rm UM}\le1\), with an early \(W_0>0\). Also require normalization \(\mathcal J[1]=1\), the finite interpolation identity, and factorization of (19) when both supports and selections split into coarse sets with no contact. Physical completeness is required only to identify the gas with the physical integral. These structural identities are assumptions independently of its numerical bounds. Reality at real data, gauge covariance and Borel dependence of the potentials and functionals must be supplied by the assigned construction.

**Outstanding — actual Gaussian identification.** CI Proposition 4.2 and PR-lay Corollary B.6 cite the superseded IN1 draft. Frozen IN1's H-M and Lemma 2 explicitly separate its auxiliary path-weighted matrix from the actual hereditary carriers. `gates/carrier-check.md` supplies an envelope for the specified replacement series; it does not make every other carrier assignment hereditary. Thus J is retained as an actual-construction import, not inferred from the precision estimate alone.

**Lemma 6 (hub counts).** Under G, choose a fixed collar constant \(C_h\ge1\), also covering failed-bond collars. Then
\[
 \#W^\sharp\le2C_h(1+\ell^\natural(W)/L),\qquad
 S^\natural_\xi:=\sup_{x\in\Lambda}\sum_{W\ni x}e^{-\xi\ell^\natural(W)}\le4
 \quad\bigl(\xi\ge\kappa_f^\natural:=\log(4\cdot82^2e)\bigr).           \tag{20}
\]
Also \(\sup_{x\in\Lambda}\sum_{y\in\Lambda}e^{-t d_{\Gamma^\natural}(x,y)}\le2\) for \(t\ge\log(162e)\).

*Proof.* Prune a minimum tree for \(W\) so all leaves are in \(W\), and let its length be \(n\). Removing its hub vertices leaves cube components \(C\). If \(C\) attaches to \(k\ge2\) hubs, their attachment cubes are pairwise at least \(s_0-2\) apart. The disjoint radius-\(r_H\) balls about them each contain at least \(r_H\) edges of \(C\). If \(k=1\), that component contains a gas leaf and at least \(G_0-1\ge r_H\) edges. Consequently
\[
 \sum_{\text{hubs }v}\deg(v)\le n/r_H,\qquad
 \#\{C\}\le1+n/r_H.                                                  \tag{21}
\]
A fine tree of \(e_C\) edges has collar size at most \(C_h(1+e_C/L)\): split its doubled walk into segments of at most \(L\) steps; each segment and its fixed fine collar meet a bounded number of coarse cubes. Sum over \(C\) and use \(r_H\ge L\) to prove the first bound of (20).

For rooted \(W\), encode a chosen minimum tree by its \(2n\)-step depth-first walk and flags indicating its vertices in \(W\). Cube vertices have at most 82 next instructions, including a return. A hub has at most \((D_H+3)^4\); its departures total at most \(n/r_H\). The count is at most \(2^{n+1}82^{2n}e^n\), by (7). At the stated \(\xi\), its sum is \(2\sum_{n\ge0}2^{-n}=4\). This corrects the draft's \(4^{-n}\) arithmetic, without changing its final bound.

A geodesic of length \(n\) between gas cubes meets at most \(2n/(s_0-2)\) hubs, using the initial gap and the separation of successive hubs. Cube departures have at most 81 choices and hub departures at most \((D_H+2)^4\). Thus its possible endpoints number at most \((81e)^n\), by (7). The last assertion follows by a geometric series. ∎

For a connected ordinary domain of \(n\) cubes, \(\operatorname{St}(Y)=n-1\). Lemma 1's animal count therefore gives rooted entropy at most \((1-6400e^{-\xi})^{-1}\le2\) for \(\xi\ge\log12800\). Define \(S_\xi^{\rm all}\) to be the sum of these bounds over **all tagged ordinary types**, plus (20) for the exempt type. Fix \(\lambda_0,\sigma_1>\max\{\kappa_f,\kappa_f^\natural\}\), with \(\kappa_f\ge\log12800\). Charging to a fine cube gives
\[
 \sum_{Y:Y^\sharp\subset Z}e^{-\xi\ell_t(Y)}
 \le c_fL^4 S_\xi^{\rm all}\#Z.                                     \tag{22}
\]
This uses the sum of type entropies; the maximum used in draft §9.4 is insufficient unless already defined to include every tag.

A coarse set and a selection \((Z,\iota)\) are **linked** if the graph of the contact-components of \(Z\), joined whenever one selected domain's collar meets both, is connected. Define
\[
 H^\natural(Z)=\sum_{\iota\ne\varnothing:\ Z_0^\sharp\subset Z,\ (Z,\iota)\ {m linked}}T(Z,\iota).
\]
Compatibility means no cubes touch or coincide. This is a declared adjacency convention; equality of this convention with every use of “wall” in SA is unnecessary. J explicitly requires factorization for separated sets in this convention.

The gas partition function is \(\Xi=\sum_{\mathcal F\ {m compatible}}\prod_{Z\in\mathcal F}H^\natural(Z)\), with empty product one. Define the initially formal union-filed series
\[
 E(X)=\sum_{n\ge1}\frac1{n!}\sum_{\bigcup_{j=1}^n Z_j=X}
       \phi(Z_1,\ldots,Z_n)\prod_{j=1}^nH^\natural(Z_j).
\]
Here \(\phi\) is the sum of \((-1)^{|E|}\) over connected spanning subgraphs of the incompatibility graph of the labelled list; \(\phi(Z)=1\). Repeated polymers are allowed and are self-incompatible. Theorem 8 proves convergence and \(\Xi=\exp(\sum_XE(X))\).

Let \(\Lambda^\natural(Z)\) be the least sum of \(\ell^\natural(W)\) over families of exempt domains, with collars in \(Z\), linking its contact-components; it is zero for connected \(Z\), and infinity if no family exists. Coarse hubs \(H^c\) consist of coarse cubes meeting the uninflated hulls \(H\). Let \(d^{\natural c}\) be Steiner length after contracting those coarse hubs, and put \(\mathcal L(X)=d^{\natural c}(X)+5\).

**Lemma 7 (coarse geometry and linked entropy).** For \(N=\#Z\),
\[
 d^{\natural c}(Z)\le c_1N+c_2\Lambda^\natural(Z)/L,\qquad
 c_1=257+2C_h,\quad c_2=513+2C_h.                                    \tag{23}
\]
With \(\alpha_0=\log12800+2592L^4\), \(\beta_0=13\),
\[
 \sup_q\sum_{Z\ni q:\Lambda^\natural(Z)<\infty}
       e^{-\alpha_0\#Z-\beta_0\Lambda^\natural(Z)}\le1.                \tag{24}
\]

*Proof.* A linking family can be reduced to at most one fewer domains than the number of components, by retaining only domains joining different current groups. Its cost does not increase. A minimum fine contracted tree of length \(n_W\) has cube components with total edge count at most \(n_W\) and component count at most \(1+n_W/r_H\). Splitting doubled cube walks into segments of length at most \(L\), each meeting at most \(4^4=256\) coarse cubes, gives at most \(512n_W/L+256(1+n_W/r_H)\) projected edges. Each hub attachment costs at most one further coarse edge: its fine cube is within three of the uninflated hull and \(L\ge4\). By (21) and \(r_H\ge257L\), the total is at most \(513n_W/L+256\). At most \(2C_h(1+n_W/L)\) collar attachments join this tree to the components of \(Z\). Add component spanning trees, of total length at most \(N\), and sum over at most \(N\) selected linking domains. This is (23).

For (24), each linking domain gives a spanning tree between witness gas cubes at cost at most twice its Steiner length. Retain a tree joining the coarse components. Its link distances \(t_e\) sum to at most \(2\Lambda^\natural(Z)\). Thus its weight is bounded by the product of component weights \(e^{-\alpha_0|A|}\) and link weights \(e^{-(\beta_0/2)t_e}\). Root at the component containing \(q\). For each child, an attachment from \(A\) has at most \(81L^4|A|\) first gas witnesses, total second-witness weight at most 2 by Lemma 6, and at most 16 coarse roots at the second witness. Here \(\beta_0/2\ge\log(162e)\); for instance \(e^{11/2}>(8/3)^5(3/2)>162\).

Let \(W_d\) bound rooted structures of depth at most \(d\), allowing overlaps. The unordered-child exponential overcounts each valid structure: distinct child components have all their permutations, cancelling the factorial denominator. If \(W_d\le1\),
\[
 W_{d+1}\le\sum_{n\ge1}6400^{n-1}
        e^{-(\alpha_0-2592L^4)n}\le\sum_{n\ge1}2^{-n}\le1.
\]
The same bound initializes \(W_0\). Every finite linked set has such an encoding, whose total link weight dominates its weight in (24). Monotone summation in depth proves (24). ∎

Choose an output rate \(\mu_o\ge\kappa\), and set
\[
\begin{split}
 C_h^\natural&=2C_h,&K_*&=3+(c_1+5)\mu_o+\log81+\alpha_0,\\
 \sigma_2&=c_2\mu_o/L+\beta_0,&\Theta^\natural&=2C_h(1+K_*),\\
 \lambda_V-\lambda_0&\ge\sigma_1+\sigma_2+\Theta^\natural/L,&\log D&\ge\Theta^\natural,\\
 A_{\mathfrak a}&=2c_fL^4S_{\sigma_1}^{\rm all}/W_0,&
 \tau&=e^{\Theta^\natural}(A_{\mathfrak a}\mathfrak a+p_*),\\
 \mathfrak a&\le\min\{W_0/2,(4e^{\Theta^\natural}A_{\mathfrak a})^{-1}\},&
 p_*&=N_{\rm bond} e^{-\gamma_{\rm tilt}\mathfrak b^2/2}\le(4e^{\Theta^\natural})^{-1}.
\end{split}                                                                         \tag{25}
\]
Here \(N_{\rm bond}=c_b(LM)^4\) bounds the number of failed bonds per coarse cube, with fixed geometric \(c_b\); \(\gamma_{\rm tilt}\) is IN1's post-\(M\) Gaussian tilt, **not** the coupling ceiling. In particular \(\tau\le1/2\).

**Theorem 8 (UM-natural).** Assume G, J and (25). Then the finite gas factors into compatible linked polymers, and
\[
 |H^\natural(Z;P)|\le\tau e^{-(K_*-2)\#Z}e^{-\sigma_2\Lambda^\natural(Z)}.                \tag{26}
\]
For \(w_Z=\sup_P|H^\natural(Z;P)|e^{\mu_o\mathcal L(Z)}\),
\[
 \sup_q\sum_{Z\ni q}w_Ze^{\#Z}\le\tau/81,\qquad
 \sum_{Z'\not\sim Z}w_{Z'}e^{\#Z'}\le\tau\#Z\le\#Z/2.              \tag{27}
\]
The union-filed connected-cluster terms satisfy
\[
 |E(X;P)|\le(\tau/81)e^{-\mu_o\mathcal L(X)}.                         \tag{28}
\]
They converge locally normally and are holomorphic on the supplied common input fibre, real at real data. If a coordinate polydisc of radii \(r_j\), centred at \(P_0\), lies in that fibre, then
\( |\partial^\alpha E(X;P_0)|\le\alpha!\,r^{-\alpha}(\tau/81)e^{-\mu_o\mathcal L(X)}\).
All conclusions are uniform in any additional external parameters on which J and (17) hold uniformly, including an ordinary source box if supplied. No enlarged domain for a history operation is inferred.

*Proof.* In the finite Mayer/interpolation identity, partition \((Z,\iota)\) by the connected components of its link graph. Each selected support belongs to one group; distinct groups have no cube contact. J factors \(T\) over them. A group with empty selection contributes zero, since its term differentiates \(\mathcal J[1]=1\). Conversely compatible linked selections reconstruct exactly one original selection. This proves the gas factorization.

Give each selected potential a coupling disc of radius
\((W_0/\mathfrak a)e^{(\lambda_V-\lambda_0)\ell_t(Y)}\).
Equations (17), (22) bound their summed exponents by
\(P W_0L^4N+P W_0M^{-4}|B|^2\), where \(P\) includes all type entropies. Gaussian comparison and the distinct failed tests bound the Mayer integral by \(2^{|\mathbf D|}e^{C_0^{\rm UM}N}p^{|P_0|}\), \(p=e^{-\gamma_{\rm tilt}\mathfrak b^2/2}\). It vanishes when any selected coupling is zero. Repeated Schwarz, then coarse Cauchy with radius increasing to \(D\), give
\[
 |T(Z,\iota)|\le e^N(2\mathfrak a/W_0)^{|\mathbf D|}
 e^{-(\lambda_V-\lambda_0)\sum_Y\ell_t(Y)}p^{|P_0|}D^{-h},\quad
 h=\#(Z\setminus Z_0^\sharp).                                        \tag{29}
\]
The zero-amplitude case uses only failed tests. Joint holomorphy and the Gaussian dominating function justify the Cauchy operations; no cutoff argument is complexified.

The collar count gives
\(N\le2C_h[|\mathbf D|+L^{-1}\sum_Y\ell_t(Y)+|P_0|+h]\).
Pay \(e^{(1+K_*)N}\) from (29) using (25), leaving
\(e^{-K_*N}\prod_Y[(2\mathfrak a/W_0)e^{\Theta^\natural}e^{-(\sigma_1+\sigma_2)\ell_t(Y)}]
\prod_{P_0}pe^{\Theta^\natural}\).
Only exempt domains can join different components, so a linked selection pays at least \(\sigma_2\Lambda^\natural(Z)\). Drop selection restrictions after keeping that gain. By (22), the nonempty selection sum is at most \(e^{\tau N}-1\le\tau e^{2N}\). This proves (26).

Equations (23), (25) imply
\[
 w_Ze^{N}\le\tau\,81^{-N}e^{-\alpha_0N-\beta_0\Lambda^\natural(Z)}.
\]
Use \(81^{-N}\le1/81\) and (24). An incompatible polymer contains one of at most \(81N\) neighbouring cubes, proving (27).

For completeness, the hard-core tree bound used next has a finite combinatorial proof. For a fixed incompatibility graph, assign each connected subgraph its breadth-first tree from vertex 1, using a fixed vertex order to choose the first parent. The subgraphs with a given tree form an interval: optional edges join equal levels, or adjacent levels without replacing a chosen first parent. Their alternating sum is \((-1)^{n-1}(1-1)^r\). Hence the absolute connected coefficient is at most the number of allowed spanning trees. The rooted tree sums, truncated by depth, obey
\(F_Z^{(0)}=1\), \(F_Z^{(d+1)}=\exp(\sum_{Y\not\sim Z}w_YF_Y^{(d)})\).
Equation (27) gives \(F_Z^{(d)}\le e^{\#Z}\) inductively. Taking increasing depth bounds the full rooted series.

For an incompatibility-connected list, joining covering trees costs at most one graph edge per join. Thus
\(\mathcal L(\bigcup Z_j)\le\sum_j\mathcal L(Z_j)\).
In the union-filed cluster formula, mark a polymer containing a fixed \(q\in X\). This changes \(1/n!\) to \(1/(n-1)!\) and only enlarges the absolute sum. The preceding rooted estimate and (27) give (28). It also dominates the series uniformly in the external parameters. Expanding the pairwise compatibility indicators on labelled lists and separating graph components gives \(\Xi=\exp(\sum_XE(X))\) coefficient by coefficient. The convergent identity therefore holds near zero activities; scaling activities within (27) and taking the dominated limit continues it to the stated gas. Normal convergence proves holomorphy; coordinate Cauchy gives the derivative bound. All locality in external fields remains that supplied by J and the potential carriers. ∎

**Theorem 9 (CI at an exempt main step: exact remaining condition).** Assume `(CI-old)`—the holomorphic, Borel, reality, covariance and stored-slot bounds for every older formed activity on its declared chain domain—the admission hypotheses of ST1 Theorem 14 and ST3 Theorem 14′ used in A, and R, A, X, G, J, (15), (25). The regular-gas logarithms satisfy (28) and the holomorphic, Borel and reality parts of CI on the common fibre. To conclude CI **as carried local activities in the existing IN1 class**, also require a filing map with the following properties:

* each output has its actual external-pair and stored-variable carrier and a declared chain domain containing all later reads;
* filing is an exact regrouping on these carriers, with summable multiplicities, hereditary restriction and the required covariance;
* the regrouped regular and boundary terms obey their respective IN1 class lengths and amplitudes, including the full-island containment condition for every claimed exemption.

Under that additional input, NL1-L's CI induction applies with `(i′)` requiring the actual composition and (12), and with output bounds furnished by the filing input. On **raw unions** its bound is exactly \(b_E(X)=(\tau/81)e^{-\mu_o\mathcal L(X)}\).

*Proof.* CI-old supplies the bounds for the old factors. Admission A and Lemma 2 supply the strengthened composition premise. Theorem 5 gives the exempt potential estimate; the ordinary estimates and J give the other inputs of Theorem 8. Its normal convergence and the imported Borel/covariance properties give the corresponding CI properties at \(\sigma\). The extra filing input is precisely what makes these functions activities on their asserted local domains, with the required class bounds. Induction then uses older, already formed activities only. ∎

**Outstanding — draft Theorem 10.2 and `(File♮)`.** The draft does not prove this filing input. Two distinct failures occur.

First, Boolean localization of \(B\) is not localization of \(P\). For example \(F(p,B)=\epsilon p_zB_c\), with \(z\) in a remote read carrier, has \(D_{\{c\}}F=\epsilon p_zB_c\). A small \(\epsilon\) can meet a response-size bound, but the external read at \(z\) has not disappeared. The response's stored-source base \(h_0(P)\) has the same issue. A uniform bound on \(\mathcal O_\sigma\) does not construct a hereditary activity on the core of \(\{c\}\).

Second, SA 6191–6197 permits exemption only of whole hulls contained in the output support. A raw union \(X\) of gas cubes contains none of the remote hubs used by its contracted tree. For two gas cubes on opposite sides of a large island, \(d^{\natural c}(X)\) omits the island crossing, whereas the source's relative length cannot exempt that island inside \(X\). Hence the draft's inequality \(d_i^\natural(\mathcal S';X)\le d^{\natural c}(X)\) is false. Enlarging \(X\) to include the hub and connecting carriers still requires a new length comparison and a multiplicity sum; it is not a proof of the displayed inequality. Nor does equality of contracted and ordinary lengths force a raw union to be contact-connected. The asserted filing, and therefore the full existing-class conclusion of draft Theorem 10.2, remain **Outstanding**. The island-formation bounds `(Size-isl)`, `(Loc-isl)` also remain LF1 inputs; this gas argument does not prove them.

## Parameter order and main statement

**RUN.** Use frozen IN1's constant order, frozen TP1's running-minimum radii and the finite-history frame bounds imported by PAN: uniformly above the final cutoff threshold, \(\check R_i\ge(\ell-1)^r\), \(r\ge2\). Require every non-exempt base amplitude in (17) to tend to zero as the final coupling ceiling \(\gamma\downarrow0\), with all preceding parameters fixed. An optional insertion instead occupies at most half the final potential budget. This is a hypothesis about the ordinary/inserted inputs, not a conclusion about unspecified potentials.

**Lemma 9.1 (the window and frozen IN1 Amendment 1).** Put \(b=1+4\beta_s\), \(\mu_o=b\kappa\), and
\[
\begin{split}
 A_\natural&=b[c_2+2C_h(c_1+5)],&
 B_\natural(L)&=\lambda_0+\sigma_1+\beta_0+2C_h(4+\log81+\alpha_0)/L,\\
 u&=\min\{(2C_h^{\rm WF})^{-1},(4C_{\rm pr})^{-1},1\}.
\end{split}                                                        \tag{30}
\]
Assume \(C_h^{\rm WF},C_{\rm pr}\ge1\). The natural lower endpoint in (25) is exactly \(A_\natural\kappa/L+B_\natural(L)\). The floor in Amendment 1,
\[
 L>\max\{4C_h^{\rm WF},8C_{\rm pr}\}A_\natural,                     \tag{31}
\]
is sufficient for this window to fit below all three endpoints
\(\kappa/(2C_h^{\rm WF})-\varepsilon_{\rm rate},\ \kappa/(4C_{\rm pr}),\ \kappa-1\)
once \(\kappa\ge2[B_\natural(L)+\varepsilon_{\rm rate}+1]/[u-A_\natural/L]\).

To retain frozen IN1's displayed original window (24) **simultaneously**, define
\[
\begin{split}
 A_{\rm old}&=bC_h^{\rm UM}c_\ell,&
 B_{\rm old}(L)&=\lambda_0+\sigma_0+C_h^{\rm UM}(3+c_\ell g_*)/L,\\
 A_*&=\max\{A_\natural,A_{\rm old}\},&B_*(L)&=\max\{B_\natural(L),B_{\rm old}(L)\}.
\end{split}
\]
One explicit common choice is
\[
 \begin{gathered}
 L>\max\{4C_h^{\rm WF},8C_{\rm pr}\}A_*,\qquad
 \kappa\ge\frac{2[B_*(L)+\varepsilon_{\rm rate}+1]}{u-A_*/L},\\
 \lambda_V=A_*\kappa/L+B_*(L).
 \end{gathered}                                                      \tag{32}
\]
All original IN1 floors are retained as well.

*Proof.* Since \(u\le1/4\), (31) says \(A_\natural/L<u/2\). The three upper endpoints are at least \(u\kappa-\varepsilon_{\rm rate}-1\). The stated \(\kappa\)-floor makes this strictly greater than the lower endpoint. The same proof with \(A_*,B_*\) proves (32), which dominates both lower endpoints. Although \(B_\natural(L)\) grows as \(L^3\), it is fixed before \(\kappa\); the latter absorbs it. No later \(M\) or \(\bar\kappa\) occurs. ∎

Thus Amendment 1 has the right **natural-window slope floor** and creates no cycle, conditional on the uniform geometric \(C_{\rm pr}\) in (8). Its phrase about the gap between slopes must mean \((u-A_\natural/L)\kappa\), not the slope difference alone. It does not, by itself, replace IN1's still-displayed (24). To require both windows one must use (32), or first normalize the early constants so that \(A_{\rm old}\le A_\natural\), and absorb both intercepts in the later \(\kappa\)-floor. The affected IN1 choices are rows **2 and 4**, as Amendment 1 correctly says; draft §11's “row 7” is wrong. This manuscript changes no frozen file.

**Theorem 10 (conditional TD and remaining CI reduction).** For each finite main-step history, assume R, A, X, G, J, RUN, and the named admission inputs in A. If the hypotheses hold uniformly in histories and their common complex fibres, the conclusions are uniform there. Make the following choices in order, interleaving other IN1/ST1 choices without reversing their dependencies.

1. Fix the powers \(r,p_0,q\), margins, number of potential types, geometric constants \(C_h,C_{\rm pr},c_f,c_b,c_1,c_2,\kappa_f,\kappa_f^\natural,\beta_0\), old-window constants, and \(\lambda_0,\sigma_1>\max\{\kappa_f,\kappa_f^\natural\}\). The projection and hull constants used to choose \(L\) must be uniform in \(L\). Choose odd \(L\) by (32) and the earlier floors. Then \(\alpha_0\) and the tagged count \(P\) are fixed.
2. Before \(\kappa\), independently of \(M,\bar\kappa\), fix the ST1 base response/chart/admission constants, including \(C_D,\mu_R,C_A,c_T,c_D,\epsilon_D,c_{\rm ch},R_\sigma\), and J's early \(K_0,H_0,b_{\rm mat},d_{\rm mat},C_\tau,A_{K_0},\varepsilon_0,\rho_0,c_m\). Here \(b_{\rm mat},d_{\rm mat}\) are the matrix-envelope constants, distinct from \(b\) in (30). Choose \(W_0\) by frozen IN1 (22), using \(P\) which includes **all** types.
3. Choose \(\kappa\) by (32) and the imported floors; set \(\mu_o=b\kappa\), \(\lambda_V\) by (32), and then \(K_*,\sigma_2,\Theta^\natural,A_{\mathfrak a}\) by (25). Choose \(\bar\kappa\) after these, with
   \[
   \log(e^{\bar\kappa}-1)\ge\max\{\Theta^\natural,\Theta_{\rm old},
                2\lambda_V+36+\log6400,\log12800\},\qquad
   \bar\kappa\ge\lambda_V+2,                                        \tag{33}
   \]
   and all existing response/bracket floors. Here \(\Theta_{\rm old}\) is frozen IN1 (24). The draft's stronger \(\log12801\) is harmless. Now fix \(s_D,E_{\bar\kappa},D,a,A_R\) and the post-\(\bar\kappa\) response parameters.
4. Choose \(M\), a power of \(L\), meeting \(M\ge\max\{4,R_\sigma+3\}\), IN1 (23), and all imported separation floors. Choose the later absolute radii, \(\gamma_{\rm tilt}\), \(A_1\), island geometry and amplitude prefactors \(C_0,C_{\rm ex}(M)\), and the remaining IN1 constants in their prescribed order. Finally decrease \(\gamma\) to enforce R's source/chart ceilings, (7), \(\vartheta<1\), the ordinary input ceilings and (25). The quantities \(\varrho,A_V,K_1,\beta,\vartheta\) in (4) are **running functions of \(g,\ell\)**; only their prefactors are fixed before this last step.

Then Lemma 2 gives DR-row, Lemma 3 gives composition, Theorem 5 gives the exact TD-natural decomposition with \(\mathfrak a_{\rm ex}\to0\), and Theorem 8 gives the raw-union logarithm and Cauchy bounds (26)–(28). With `(CI-old)` and the actual carrier/filing input in Theorem 9, the remaining CI induction follows. Without that input, this theorem asserts no CI closure in the existing class and no ordinary-distance TD conclusion.

*Proof.* Lemma 9.1 ensures (15)'s first inequality and (25)'s rate inequality. Equation (33) implies \(Q\le1/2\), \(a\ge\lambda_V+18\), hence the remaining rate hypotheses. All amplitudes in R become admissible as \(g\ell^q\to0\). Theorem 5 proves \(\vartheta,\mathfrak a_{\rm ex}\to0\). RUN makes the remaining base amplitudes small. Since \(\gamma_{\rm tilt}>0\) is fixed after \(M\), \(p_*\to0\). Also \(\check R_i\to\infty\), so (7) holds: logarithms grow more slowly than its linear right sides. These limits are uniform by the stated imports. Thus every last requirement is a ceiling on \(\gamma\), not a redefinition of an early constant. Apply the numbered results in order. The optional insertion uses the reserved half-budget. ∎

## Source check and the claimed obstruction

**Proposition 11 (draft Proposition 7.1 is not a counterexample to the cited inputs).** With SA's literal relative-tree definition, the draft's estimate
\(d^\natural(X_f)\le2G+(m-1)s+2\) for a chain of \(m\) islands of diameter \(D\) is unjustified. It does not establish a gap in SA's (UM1).

*Proof.* SA 6191–6197 minimizes the length of a **tree** meeting every unexcused cube and each chosen hull; chosen hulls must be contained in \(X_f\). It does not assign zero cost to edges inside hulls. A tree meeting the two outside endpoint cubes contains a path between them, so its length is at least their separation (up to the fixed endpoint convention). In the draft's chain this includes \(mD\), the term omitted from its proposed upper bound. Meeting each hull once can avoid filling its interior, but cannot disconnect this endpoint path. CA-III 3519–3524 gives the same distinction explicitly: a tree contained in the domain intersects every unexcused cube; CA-II 16026–16029 and CA-III 12287–12288 agree. Consequently the exponential comparison used to force \(\lambda_T(s+D)\le\kappa s\) has not been obtained. The construction instead describes a **contracted** length, as newly defined here. ∎

There are two further defects in that proposed proof. The adjacent rounded radii need not have ratio tending to one: SA 17334 supplies \(\check R_{i-1}\le L\check R_i\), and power-of-\(L\) rounding permits jumps. Also failure of the displayed Boolean decomposition alone would not refute an existential claim about **every possible** local decomposition without a coefficient/entropy argument. Neither defect is needed for Proposition 11.

The exact answer about SA is therefore: **(UM1), as written at 14304–14313, does not have the claimed island-contraction gap.** It is an explicit hypothesis on the *actual local potentials*. Its ordinary tree length is defined at 14293–14303. SA has not derived it there from R23 alone. The downstream conditional implication remains conditional on this hypothesis and on actual carriers. The checked dependency chain is:

| Source lines | Use of UM1 and qualification |
|---|---|
| SA 14314–14412 | Declared complex boxes, exact integrand/supports, enlarged Gaussian bounds and **separate actual heredity/factorization hypotheses**. |
| SA 14416–14481 | Ordinary covering-tree collar and entropy counts UM7–UM11. Contracting islands changes these counts; Lemmas 6–7 prove replacements. |
| SA 14483–14657 | UM12 coupling discs use UM1; Gaussian integration/Schwarz give UM16; UM19 pays collars; selection summation gives UM24. No R23-to-UM1 deduction occurs. |
| SA 14659–14773 | UM25–UM30 use local-core suprema, hereditary restrictions, tree weights and union filing. These hypotheses preclude inferring local carriers from a bound at one global input. |
| SA 14775–14811 | Parameter conditions and an insertion slot are sufficient conditions; actual enlarged matrix control is explicitly required. |
| SA 14817–15110 | SI1–SI11 use the unmarked potential-ball majorant for a finite insertion and Cauchy estimates. They retain the ordinary local Gaussian/polymer hypotheses and distinguish physical pairs from independent complex cores. |
| SA 3908–3936; 14206–14216 | Requirement B1 and the matrix-interface discussion feed this same conditional chain; B1 explicitly leaves verification on actual interacting matrices/cores to be done. |

The other quoted source passages were checked against the pinned raw files, after consulting the index and neighbouring rows:

| Passage | Finding |
|---|---|
| SA 1273–1347 | The rooted criterion and logarithm result are conditional. Theorem 8 gives the needed finite tree/cancellation proof. |
| SA 6185–6207 | Boundary origins and R23 are quoted accurately; their interpretation as free hull contractions is not. |
| SA 17550–17564 | Kept-form carriage states a pair-oscillation bound in relative hull length. It is an input here, not a response construction. |
| SA 17903–17938 | Walk switches, brackets and Schwarz give the displayed finite re-expansion and amplitudes. These lines do not prove the summed multipoint or external-carrier assertions used in this draft. |
| SA 17985–18010 | Healing includes refiling existing boundary terms; it supplies no proof of `(File♮)` for the new raw unions. |
| YM3-I 52582–52589 | Products are attached to individual coefficient/string hulls. This supports the device in Lemma 3, not an automatic localization of a black-box composite. |
| CA-II 79915–80015 | The quoted main-step fluctuation formula and outside factors occur in the Balaban discussion. Identification with the ST3 main-step chart remains a named construction input. |
| CA-I 900–990, 1008–1049; CA-II 15870–15899, 16013–16045; CA-III 15965–16035 | Relative lengths and localization domains retain their stated tree/domain hypotheses. None defines SA 6191's length by contracting whole islands. |

SA, CA-I/II/III and YM3-I here mean the files at [revision 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775), by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The RG and large-field constructions underlying the quoted account are credited there to Tadeusz Balaban. No four-dimensional theorem is imported merely from a three-dimensional formula.

## Definitions supplied

The distillation supplies or makes explicit: (i) the finite contact graph, scalar cube read norm, collapsed **edge weights** (1), and Boolean localization separately from external locality; (ii) the row-maximum source norm, full completed-source domain, stencil locality and masked one-layer source dependence in R; (iii) arbitrary-shift admission with complete endpoint reads and the complex island deficit (5); (iv) the new hub-contracted graph, projection premise and rooted counts, distinguished from SA relative length; (v) tagged type sums, linked selections, linkage cost and raw-union length; (vi) the actual Gaussian integrand/support/cutoff interface and the missing carrier/filing condition; (vii) RUN, the common rate window and running quantities in the parameter order. All strengthening beyond a cited source is an explicit hypothesis, not a claim that the source proves it.

## Result

This text proves the hand implications DR-row → composition → TD-natural → linked-gas convergence and the raw logarithm bound, under R, A, X, G, J and RUN. Actual DR, complete admission, complex island deficit, per-cube amplitude sums, hub geometry/projection, actual Gaussian/hereditary structure, and ordinary-potential bounds are imports. Existing-class CI additionally needs the carrier/filing construction in Theorem 9; ordinary-distance TD remains **Outstanding**, neither proved nor disproved here.

Corrections to the pass-1 draft and its proposed changes to other notes:

* **ST1/NL1-L/P82:** the DR-row and arbitrary-shift arguments are valid with the strengthened inputs stated here. A row-maximum source norm, arbitrary complex sources and source-row locality are not consequences of frozen P82's real all-weight inverse. Keep ST1's actual DR construction open; the interface strengthening is not automatically supplied by CI-old.
* **PAN/NL1-L:** correct the complex base-value argument using \(A-\operatorname{Re}f_0\); PAN's real quadratic estimate does not supply its required uniform complex bound. `(Proj)` is a carrier premise, not a consequence of the single relative-length definition. The finite source range and zero-coordinate cases are explicit in Lemma 2.
* **CI/SA:** withdraw Proposition 7.1 and its claimed SA gap. The new gas is a valid conditional construction, but the proposed correction replacing ordinary TD by TD-natural does not by itself close CI. Withdraw `(File♮)` and the unsupported assertion that the other raw unions are connected; separate fluctuation locality from external-pair locality. Keep the actual Gaussian assignment and island-formation inputs open.
* **Numerical constants and counts:** fix the entropy-series ratio to \(1/2\), replace the erroneous KP equality by \(81^{-N}\le1/81\), and sum tagged type entropies. Prove smallness with \(g\ell^{p_0}+\ell^{p_0-q}\), rather than treating running radii as fixed constants. The adjacent rounded-radius ratio used in Proposition 7.1 is also unjustified.
* **Frozen IN1:** verify its Amendment 1 for the intended natural window, make the \(\kappa\)-floor explicit, retain both windows by (32), and correct the row locator. No cycle is created under the stated early uniformity. No frozen note was edited. The UM7 citation is expanded to SA 14416–14433; the draft's 14422–14437 clipped the premises.

Only `library/td.md` is changed. Retrieval, searches and source-identity bookkeeping discharge no mathematical step. The text is **not yet refereed**, is not an audit and grants no scientific status.
