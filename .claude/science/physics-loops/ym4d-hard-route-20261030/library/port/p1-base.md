# P1: base arithmetic, geometry, and finite polymer combinatorics

Provenance: Codex, research-text port begun 2026-11-05 at repository commit bac1fa81fafa298e5a71b37a14224c4d8a8033b9; not an audit and grants no status. Source: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, complete account at 31a47c543775. Written hand arguments only; not yet checked by another model.

## Reading contract and source identities

CA-I means `theorem_0_complete_account_raw_I.tex` at commit `31a47c543775`, read from `/tmp/sa_ca_I.tex`. SA means `YM4_sketch_500.tex` at that commit, read from `/tmp/sa_ym4.tex`. All line numbers below refer to these sources, not this file. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the statements and proof routes. Tadeusz Bałaban supplies the constructions and published formulas identified below. This port supplies only the explicitly marked completions and corrections.

CA-I 27–46 declares an unqualified statement with its following proof to be proved in full. That is a **source declaration**, not an independent check here. Each port below distinguishes that declaration from its hypotheses. Mathematical statements retain the source quantifiers, constants and labels; prose and proofs are rewritten. No numerical computation, enumeration, or test supplies a mathematical premise.

The required GOAL method, FINISH sections, chain-ca §7.2, ca-full README and port map were consulted. `docs/ai_methodology/SCIENCE_WORKFLOW.md` does not exist in this pinned checkout. The output is confined to this file. Outline navigation uses `sa-index/README.md`, the neighbouring rows of chunks 01, 16 and 18, and their obligations; the CA 4.12–4.19 index (chunk 11) and ca-full rows were also consulted. SA 238–294, 1159–1377, 17841–18010 and 19822–19915 give the finite Wilson, polymer and arithmetic antecedents. They do not replace the CA statements below. In particular, the actual RG increment bounds and locality are analytic inputs, not consequences of these finite arguments.

## 1. Wilson definitions and invariance

**Inputs and status.** `1.1:def-lattice`, CA-I 403–445, and `1.1:def-wilson-action`, 447–525: definitions, with the elementary assertions proved immediately afterwards. Normalized Haar probability on SU(N), including existence and uniqueness, is retained as hypothesis **H-Haar**; this note proves the particular invariance consequences it uses. Bałaban CMP 109 supplies the lattice convention, not an additional analytic theorem here.

Fix odd L (Bałaban takes L>11), integers m≥1 and K≥0, and N≥2. The torus is
\(\mathbb T_m=\mathbb R^4/(2L^m\mathbb Z^4)\), with bare sites
\(L^{-K}(\mathbb Z+\tfrac12)^4\) modulo its periods. A bond is an oriented nearest-neighbour pair; reversal is −b. Plaquettes are unoriented elementary squares, with barycentre x(p). In physical units the level-k lattice spacing is \(L^{k-K}\); in level-k units the torus side is \(2L^{m+K-k}\).

A field takes values in SU(N) on bonds, with U(−b)=U(b)⁻¹. Choose one orientation per bond and use product normalized Haar measure dU. The trace is normalized by tr 1=1. For a traversal b₁b₂b₃b₄ of ∂p, put \(U(\partial p)=\prod_{i=1}^4U(b_i)\). Define, exactly as in `1.1:eq-wilson-action-1`–`5`,
\[
a_p(U)=1-\operatorname{Re}\operatorname{tr}U(\partial p)\in[0,2],\quad
A(U)=\sum_p a_p(U),\quad A(c,U)=\sum_p c(x(p))a_p(U),
\]
\[
\mathcal O(f)=A(f,U),\quad \rho_0(U)=e^{-g_0^{-2}A(U)},\quad
\mu_{K,m}=\frac{\rho_0dU}{\int\rho_0dU},\quad
\langle F\rangle_K=\int F\,d\mu_{K,m}.
\]
The weights c may be complex; the f in the source insertion are real Lipschitz functions. Linearity gives
\[
-g_0^{-2}A(U)+\sum_i z_i\mathcal O(f_i)
=-A\left(g_0^{-2}-\sum_i z_if_i,U\right).
\]

**Proof of the assertions in the definition.** A change of starting vertex conjugates the holonomy: moving its first factor V to the end replaces W by V⁻¹WV. Reversing the traversal replaces W by W⁻¹=W*. The trace is invariant under conjugation and tr W* is the conjugate of tr W. Thus aₚ is independent of both choices. Unitary eigenvalues have modulus one, so their normalized average, the trace, has absolute value at most one. This proves the asserted range. Expanding the finite sum defining A(c,U) proves linearity and the source identity term by term. The action is continuous on a finite product of compact groups. The density is continuous and strictly positive, so its compact minimum is positive and its compact maximum is finite. Integrating against the probability dU proves the asserted normalization bounds and existence of every bounded Borel expectation. **(filled) W1.** Explicitly, if P is the number of plaquettes, the same argument gives \(e^{-2g_0^{-2}P}\le\int\rho_0dU\le1\); no uniform continuum estimate is inferred.

For site values λ(x)∈SU(N) and a torus isometry σ preserving bare sites, the source actions (`1.1:eq-invariance-1`,`2`, CA-I 528–537) are
\[
U^\lambda(\langle x,y\rangle)=\lambda(x)U(\langle x,y\rangle)\lambda(y)^{-1},\qquad
(\sigma U)(\langle x,y\rangle)=U(\langle\sigma^{-1}x,\sigma^{-1}y\rangle).
\]
These preserve the reverse-bond constraint. Translations by \(L^{-K}\mathbb Z^4\), coordinate permutations and sign changes, and reflections \(x_\nu\mapsto2c-x_\nu\) with \(2c\in L^{-K}\mathbb Z\) are included. The reflection operator on observables is \(\Theta_{\nu,c}F=\overline{F(r_{\nu,c}U)}\); reflection positivity is not asserted by invariance.

**Statement `1.1:lem-invariance`, CA-I 559–566; proof 568–604. Source status: proved in full.** For every g₀>0, gauge transformation λ, isometry σ of \(\mathbb T_m\) mapping bare sites to bare sites, and bounded Borel F,
\[
\langle F(U^\lambda)\rangle_K=\langle F(\sigma U)\rangle_K=\langle F\rangle_K.
\]

**Proof on the source route.** Around a plaquette based at x₁, the adjacent factors λ(xᵢ)⁻¹λ(xᵢ) cancel. Hence its holonomy becomes λ(x₁)U(∂p)λ(x₁)⁻¹ and its action is unchanged. The isometry permutes plaquettes, possibly reversing traversal or changing the starting vertex. Both operations preserve the real trace, as proved above. Thus A(U^λ)=A(σU)=A(U).

In the independent bond coordinates, the gauge action is multiplication by fixed group elements on both sides of each coordinate. The isometry permutes those coordinates and inverts precisely the coordinates whose orientation changes. **(filled) W2.** From H-Haar, the pushforward of normalized left Haar measure by right multiplication is again normalized left Haar measure, so uniqueness makes it equal to Haar. The pushforward by inversion is normalized right Haar measure: inversion changes left multiplication into right multiplication. By the already established two-sided invariance and uniqueness it too equals Haar. A coordinate permutation preserves the product probability, first on rectangular sets and then on the generated Borel sigma algebra. Each transformation is a continuous bijection, with inverse given by inverse site values or σ⁻¹. Therefore dU and ρ₀dU are invariant. Change variables in the finite integral of F and divide by the same strictly positive normalization. This gives both equalities. No other Wilson theorem is used.

## 2. Coupling definitions and arithmetic

**Definitions and scope.** `1.2:def-couplings`, CA-I 606–629, defines
\[
x_0=g_0^{-2},\qquad x_{k+1}=x_k-\beta_{k+1},\qquad g_k=x_k^{-1/2}\quad(x_k>0).
\]
This is the orientation of Bałaban CMP 109 (0.18),(0.20). His increment is defined in CMP 109 (1.22), identified there with CMP 119 (3.61). Its analytic construction is **H-RG**, not part of an arithmetic definition. In particular neither positivity nor availability of the next step follows merely by writing this recursion.

`1.2:def-flow-constants`, CA-I 631–686, sets
\[
c_0=\frac{11N^2}{12\pi^2}\log L,\qquad c_2>0,\qquad c_5=2c_2,
\quad \lambda_\sharp\ge\underline\lambda=c_0/4,
\quad 0<B_\sharp\le\bar B=C_\beta+1.
\]
c₂ depends only on L,N. Cβ is part of the auxiliary tuple \(\mathfrak p\), chosen after L and before γ. λ♯ and B♯ can depend on L, \(\mathfrak p\), N,γ. Every constant fixed before γ and every ceiling on γ reads these constants only through (c₀/4,c₅,\(\bar B\)). Quantities fixed afterwards can read λ♯,B♯. This is an order-of-choice declaration; the arithmetic below does not prove the one-loop value or the RG construction.

The same definition sets
\[
g_-(g)=(g^{-2}+B_\sharp)^{-1/2},\quad
K(g_0,g)=\min\{k\ge0:x_k\le g^{-2}+B_\sharp\},
\]
\[
R(g')=\min\{L^i:i\in\mathbb Z_{\ge0},\ L^i\ge(\log g'^{-2})^r\},\quad
m_{\mathbb T}(g')=11+m'+\log_LR(g'),\quad M=L^{m'}.
\]
Here r is the integer exponent chosen before L and used in H5 of `2.2:not-hypotheses`; m′ is the exponent of M in \(\mathfrak p\). The reference window is g₋(g)≤g′≤g, equivalently g⁻²≤g′⁻²≤g⁻²+B♯. The first-passage definition alone asserts no finiteness. Bare g₀ lies in (0,g₋(g)] and the declared torus condition is m≥m𝕋(g₋(g)). Those volume and order-of-choice hypotheses are recorded for fidelity, not used by the three arithmetic inequalities. `2.3:rem-thresholds` supplies γ_H and later thresholds in the construction; no conclusion of that remark is consumed here.

### 2.1 Two-sided arithmetic

**Statement `4.19:lem-flow-bounds`, CA-I 56342–56359; proof 56380–56412. Source status: proved in full.** Let n≥1. Let x₀ and \(\beta_l=\beta_l^{\mathfrak A}+\beta_l^{\mathfrak R}\), 1≤l≤n, be real, as are β⁰_l. Put x_l=x_{l−1}−β_l. Let c₀>0, c₂≥0, Cβ≥0 and \(\bar\varsigma\ge0\). Assume, for every 0≤i≤j≤n and every 1≤l≤n,
\[
\sum_{l=i+1}^j\beta_l^0\ge(j-i)c_0-2c_2,\tag{4.19:eq-flow-bounds-1}
\]
\[
|\beta_l^{\mathfrak A}-\beta_l^0|\le c_0/2,\quad
|\beta_l^{\mathfrak A}|\le C_\beta,\quad
|\beta_l^{\mathfrak R}|\le\bar\varsigma\le\min\{c_0/4,1\}.
\tag{4.19:eq-flow-bounds-2}
\]
Set λ♯=c₀/2−\(\bar\varsigma\), B♯=Cβ+\(\bar\varsigma\), c₅=2c₂. Then λ♯≥c₀/4 and
\[
\lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i)
\quad(0\le i\le j\le n).\tag{4.19:eq-flow-bounds-3}
\]

**Inputs.** The displayed assumptions are **H-flow-1**, **H-flow-2**. There is no analytic input to their implication. For the actual RG, CA-I 56361–56378 names `4.2:lem-one-loop` and `4.2:lem-unmarked` as incomplete, and the large-field increment bound and its small-coupling ceiling as additional inputs. They remain H-RG here. The prefix one-loop bound implies H-flow-1 by subtracting \(ic_0+c_2\) from \(jc_0-c_2\), including the empty prefix. No such bound is proved here for the actual RG.

**Proof.** Telescoping cancels each interior x_l and yields \(x_i-x_j=\sum_{l=i+1}^j\beta_l\). Each summand is at most \(|\beta_l^{\mathfrak A}|+|\beta_l^{\mathfrak R}|\le B_\sharp\), giving the upper bound. For the lower bound write
\[
\beta_l=\beta_l^0+(\beta_l^{\mathfrak A}-\beta_l^0)+\beta_l^{\mathfrak R}
\ge\beta_l^0-c_0/2-\bar\varsigma.
\]
Sum and use H-flow-1 to obtain
\((j-i)c_0-2c_2-(j-i)(c_0/2+\bar\varsigma)=\lambda_\sharp(j-i)-c_5\).
Finally \(\bar\varsigma\le c_0/4\) implies λ♯≥c₀/4. **(filled) F1.** When i=j all sums are empty and the assertion is −c₅≤0≤0. The other ceiling gives B♯≤Cβ+1. This lemma does not assert that individual increments are nonnegative, or that B♯>0 for arbitrary abstract data; positivity of B♯ is a separate premise in the next lemma.

### 2.2 First passage

**Statement `4.2:lem-first-passage`, CA-I 3636–3661; proof 3663–3721. Source status: proved in full.** Let λ♯>0, B♯>0, c₅≥0, g>0 and t≥g⁻²+B♯. Let \((x_k)_{0\le k<n_{\max}}\) be real, where \(n_{\max}\in\{1,2,\ldots\}\cup\{\infty\}\), and x₀=t. Assume that for every integer n≥1 for which x₀,…,x_{n−1} are defined and exceed g⁻², x_n is defined and
\[
\lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i)
\quad(0\le i\le j\le n).\tag{4.2:eq-first-passage-1}
\]
Then \(K=\min\{k:x_k\text{ is defined and }x_k\le g^{-2}+B_\sharp\}\) is a well-defined nonnegative integer and:

(a) x_k>g⁻²+B♯ for k<K, and g⁻²<x_K≤g⁻²+B♯. Equivalently, for g_k=x_k⁻¹ᐟ² and g₋(g)=(g⁻²+B♯)⁻¹ᐟ², g_k∈(0,g₋(g)) for k<K, g_K∈[g₋(g),g), and g_k∈(0,g) for k≤K.

(b) `4.2:eq-first-passage-1` holds for 0≤i≤j≤K.

(c)
\[
\frac{t-g^{-2}}{B_\sharp}-1\le K\le
1+\frac{t-g^{-2}-B_\sharp+c_5}{\lambda_\sharp}.
\tag{4.2:eq-first-passage-2}
\]
For any such family indexed by t, K→∞ as t→∞ (with the displayed constants fixed).

**Input.** **H-next** is exactly the extension-and-bound hypothesis above. An abstract sequence need not come from RG. No full construction theorem is invoked.

**Proof.** Choose an integer n₀≥1 strictly greater than \((t-g^{-2}-B_\sharp+c_5)/\lambda_\sharp\). Suppose there is no defined crossing through index n₀. At n=0 the value t is defined and, under this supposition, strictly exceeds g⁻²+B♯. Inductively, if the values through n−1 exist and exceed that threshold, they exceed g⁻². H-next defines x_n; the no-crossing supposition makes it exceed the same threshold. Thus values through n₀ all exist. Apply the lower bound to (0,n₀):
\[
x_{n_0}\le t-\lambda_\sharp n_0+c_5<g^{-2}+B_\sharp,
\]
a contradiction. As the source says (CA-I 3684–3685), the terms are indexed by an initial segment \(k<n_{\max}\) containing \(K\), so \(x_0,\dots,x_K\) all exist; this is used below for \(x_k>g^{-2}+B_\sharp\) at every \(k<K\) and for the extension hypothesis at \(n=K\). The finite set of crossing indices up to n₀ has a least member K. Minimality proves the preterminal assertion.

If K=0, t≥g⁻²+B♯ and the crossing inequality force x_K=g⁻²+B♯>g⁻². If K≥1, H-next applies at n=K, and its upper bound on (K−1,K) gives x_K≥x_{K−1}−B♯>g⁻². The other endpoint is the crossing definition. Every x_k through K is positive; the strictly decreasing function x↦x⁻¹ᐟ² sends the two thresholds to g and g₋(g), giving all coupling assertions.

For K≥1, (b) follows by that same application of H-next. For K=0 it is −c₅≤0≤0. For (c),
\[
t-g^{-2}-B_\sharp\le t-x_K\le B_\sharp K
\]
gives the lower bound after division by B♯. For K≥1,
\[
g^{-2}+B_\sharp<x_{K-1}\le t-\lambda_\sharp(K-1)+c_5.
\]
Rearrangement and division by positive λ♯ give the stated upper bound (in fact strictly). For K=0 its right side is at least one, since t−g⁻²−B♯ and c₅ are nonnegative. The lower bound diverges with t, proving the final assertion. **(filled) F2.** The strict integer choice is justified by the Archimedean property; no infinite sequence is presumed during the contradiction. Each of its finitely many required terms is supplied by H-next. This also handles a potentially finite n_max without an unstated extension.

## 3. Geometric definitions and the conditional gas representation

This section is separate from the numerical activity bounds. Its geometric assertions use the supplied step format; its factorization additionally uses the printed locality hypothesis. Nothing here constructs Bałaban's relative small-field machine.

### 3.1 Definitions and the inputs they carry

`4.6:def-cubes-cells`, CA-I 20288–20345: work in level-k units, in dimension d≥1 (d=4 for T0), on nonwrapping regions. The M-cubes are \(c_n=Mn+[0,M]^d\). The cell scale satisfies \(\check R_k\in L\mathbb N\), \(\check R_k\ge L\); cells have side \(M\check R_k\) and corners on \(M\check R_k\mathbb Z^d\). At level i≤k, \(u_i=L^{-(k-i)}\), M-cubes have side Mu_i and cells side \(a_i=M\check R_i u_i\). Thus a_i∈Mu_iℕ and a_k=M\(\check R_k\). Cubes touch when their closed sets share a point, including corners. For unions of cubes, \(A\sqcap B\) means their common **cubes**, not their common boundary points. Removal, partition, and containment in the combinatorial decompositions below are cube-wise. A core is the closed union of its retained cubes; its touching relation still includes boundary points. N(A) counts cubes. Components are touch-components. A tree graph in the source means **any connected finite union of closed segments**, with length the sum of segment lengths; acyclicity is not required by this definition.

**(filled) G1.** A chain of touching convex cubes gives a polygonal path by joining consecutive contact points within each cube. A finite connected segment union is likewise polygonally connected: subdivide segments at their finitely many intersections and overlap endpoints, and use a finite graph path. It can be chosen without repeated edges. Remove overlapping segment interiors from all but one copy to avoid double counting. These observations justify the connectivity and length uses below, including degenerate point graphs.

`4.6:def-step-datum`, CA-I 20347–20439: fix outer datum
\(\mathcal O=(Z_k;(Y_i,\mathfrak h_i)_{i\le m})\), with support \(|\mathcal O|=Z_k\cup\bigcup_iY_i\). Here m counts second-class components, not the torus exponent. Bałaban's eligible components of the original large-field region are boxes of cells contained in cubes of side \(100M\check R_k\). The remaining large-field region is again called Z_k. Eligible first-class islands X_a are healed, so their histories are summed inside the bracket. Second-class Y_i are thrown back, with variables and histories fixed outside it. An admissible family \(\mathfrak X\) obeys `4.6:eq-step-datum-a`:

- (c1) every X_a is individually an admissible first-class island, with its tests, maturity and construction read inside X_a;
- (c2) distinct X_a share no point;
- (c3) each X_a shares no point with \(|\mathcal O|\).

**H-format / H-geometry.** The existence of these component boxes, their separation and individual admissibility tests is input from Bałaban CMP 119 (2.3), CMP 122a §1 and the relative small-field machine. It is not proved by calling it a definition. The finite port assumes these geometric data and the product island-operation format. Histories internal to each operation are already included there. If history index sets are infinite, existence of the operations and the absolute integrability needed to regroup their history sums is part of H-format.

For completeness, the family conventions in `4.6:def-step-datum` also fix cutoff, attachment and vacuum conventions and the following coupling profile. Fix smooth \(\psi_\varphi:[0,\infty)\to[0,1]\), equal to 1 on [0,1/8] and 0 on [1/4,∞). For level-i cell hull [A]_i of the prepared region A=Z″_i and cells \(D=\prod_\mu D_\mu\),
\[
\varphi_i(x)=\prod_{D\subset[A]_i}\left(1-\prod_{\mu=1}^d
\psi_\varphi(\operatorname{dist}(x_\mu,D_\mu)/a_i)\right),\quad
\frac1{g_k(\cdot)^2}=\frac{\mathbf1_{Z^c}}{g''_k(\cdot)^2}+\frac{\mathbf1_Z}{g_k^2}.
\]
g″_k is the prepared function in Bałaban CMP 122a (1.62). The gas proof does not estimate this profile. Its construction and invariance under removing irrelevant islands remain in H-format and H-locality.

`4.6:def-strips-bracket`, CA-I 20441–20573: set
\(m_\sharp=\lfloor(\check R_k-1)/2\rfloor\), so \(\check R_k-2m_\sharp\ge1\). More generally the strip definition permits any nonnegative integer with that inequality. S♯ consists of S and layers n=1,…,m♯ of M-cubes at sup-distance (n−1)M from S. S⊞ is S with the cells touching it. For a box S=∏[v_j,v′_j] of cells,
\[
S^\sharp=\prod_j[v_j-m_\sharp M,v'_j+m_\sharp M].
\]
Indeed a cube index in coordinate j must satisfy
\(v_j-m_\sharp M\le Mn_j\le v'_j+(m_\sharp-1)M\) if m♯≥1; m♯=0 is immediate. For two disjoint closed cell unions S₁,S₂, every cell-pair distance is a positive multiple of M\(\check R_k\), hence at least that value. Each strip adds at most m♯M of sup-distance on either side. Therefore
\[
\operatorname{dist}_\infty(S_1^\sharp,S_2^\sharp)
\ge(\check R_k-2m_\sharp)M\ge M.\tag{4.6:eq-strips-bracket-b}
\]
Also S♯⊂S⊞: a strip cube outside S lies in an aligned cell whose distance from S is less than M\(\check R_k\). Cell distances are multiples of that number, so this cell touches S. These proofs preserve the source's point separation, stronger than merely having no common cube.

Put \(Z(\mathfrak X)=\bigcup_aX_a\cup\bigcup_iY_i\) and \(Z(\mathfrak X)^\sharp=\bigcup_aX_a^\sharp\cup\bigcup_iY_i^\sharp\). Its strips are pairwise nontouching boxes. The localization class \(\mathbf D_k\) consists of touch-connected cube unions for this port (`4.6:def-geometric-facts`, CA-I 20575–20607, G3). If a broader class is used elsewhere, the source explicitly restricts this interaction family to touch-connected members. Define
\[
\mathcal Y(\mathfrak X)=\{Y\in\mathbf D_k:
Y\sqcap Z(\mathfrak X)^\sharp\text{ is a nonempty union of whole strips},\quad
Y\setminus Z(\mathfrak X)^\sharp\ne\varnothing\}.
\tag{4.6:eq-strips-bracket-a}
\]
G1 of `4.6:def-geometric-facts` is H-geometry above; G2 is the proved strip fact. The external machine that supplies G1 remains a hypothesis.

The island operation \(\mathbf T'_k(X_a)\), Bałaban CMP 122b (1.71), integrates island variables, includes internal histories and the frame average, and leaves functions of other variables alone. Its exponent is
\[
-\tfrac12\langle DH''B,\zeta DH''B\rangle
-A((g'')^{-2}\zeta_1\lceil X_a,U'')
+V(X_a^\sharp,U_k)+E_k(X_a)-E_k(\Lambda\cap X_a),
\]
with the normalization of that published formula. These symbols denote the supplied island operation; no bound or existence of its analytic background is inferred here. The bracket is
\[
\{\cdots\}=\sum_{\mathfrak X\ \text{admissible}}
\left(\prod_{a\in\mathfrak X}\mathbf T'_k(X_a)\right)
\exp\left(\sum_{Y\in\mathcal Y(\mathfrak X)}V(Y)\right).
\tag{4.6:eq-strips-bracket-1}
\]
The history sums act on V(Y) as well. The index family depends on \(\mathfrak X\).

`4.6:def-polymer-expansion`, CA-I 20609–20729: set
\(h_Y=\int_0^1V(Y)e^{t_YV(Y)}dt_Y=e^{V(Y)}-1\). This identity follows by integrating the derivative of e^{tV}; it also holds at V=0. Expand the finite product \(\prod_Y(1+h_Y)\). A datum is \((\mathfrak X,\mathbf D)\), with \(\mathbf D\subset\mathcal Y(\mathfrak X)\), of weight
\[
\left(\prod_{a\in\mathfrak X}\mathbf T'_k(X_a)\right)\prod_{Y\in\mathbf D}h_Y.
\]
Its raw domain is \(X'_0=\bigcup_{Y\in\mathbf D}Y\cup\bigcup_aX_a^\sharp\); its core removes all second-class strips cube-wise. Take the touch-components of this core, and glue two components whenever one Y∈D has core cubes in both. Classes are the equivalence classes generated by these gluings. A class p carries islands \(\mathfrak X_p\), domains \(\mathbf D_p\), and support
\[
X'_p=\bigcup_{Y\in\mathbf D_p}Y\cup\bigcup_{a\in\mathfrak X_p}X_a^\sharp.
\]
Each first-class strip is a connected box disjoint from every second-class strip. It therefore belongs to one core touch-component. Each Y has an off-strip cube, hence a nonempty core, and all its core components are glued by Y. Thus every island and every domain belongs to exactly one class.

A polymer is a support X′ of a class; on the finite torus the set \(\mathcal P\) of possible supports is finite. Define
\[
F(X')=\sum_{\substack{(\mathfrak X,\mathbf D)\text{ one class}\\\text{support }X'}}
\left(\prod_{a\in\mathfrak X}\mathbf T'_k(X_a)\right)\prod_{Y\in\mathbf D}h_Y,
\quad \operatorname{core}(X')=X'\setminus\bigcup_iY_i^\sharp,
\]
\[
X'\,\iota\,X''\iff\operatorname{core}(X')\cap\operatorname{core}(X'')\ne\varnothing.
\tag{4.6:eq-polymer-expansion-b}
\]
The intersection here is of the closed core unions, so touching cores are incompatible. Every cube in a class's core part belongs to one of its islands or domains, hence to X′; the reverse inclusion is immediate from their assignment. Thus the core of X′ is exactly that core part, is nonempty, and depends only on X′. It follows that ι is reflexive and symmetric. A polymer is a **support**, not a support with an extra history label; histories are summed inside F. This distinction is required by the later counting lemma.

### 3.2 Named printed locality hypothesis

**H-locality** is `4.6:rem-interaction-locality`, CA-I 20731–20755, especially `4.6:eq-interaction-locality-a` at 20737–20744. Its source status is **printed without proof**, credited to Bałaban CMP 122b p.379. The account explicitly interprets it to mean:
\[
V(Y)\text{ depends only on }(\mathbf U,\mathbf J)|_Y,
\text{ the fixed variables of }Y_i\subset Y,
\text{ and the integration variables and histories of }X_a\subset Y.
\]
There is no dependence on the remaining islands or their histories. This is a hypothesis here, including consistency of the same local term when irrelevant islands are removed or added. The account invokes it explicitly at **CA-I 20767** in part (a) below. A combinatorial factorization does not prove it.

### 3.3 Polymer-gas representation

**Statement `4.6:lem-polymer-gas`, CA-I 20757–20790; proof 20792–20927. Source status: proved as an implication; part (a) and the gas equality carry H-locality.** Use the strips, data, classes, activities and ι just defined, and call polymers compatible when they are not ι-related.

(a) Assume `4.6:rem-interaction-locality` (printed without proof in Bałaban CMP 122b, cited as printed). Every datum's integrand factors over its classes. The factor belonging to p uses, among island integration variables, only those of \(\mathfrak X_p\).

(b) The map \((\mathfrak X,\mathbf D)\mapsto\{(\mathfrak X_p,\mathbf D_p)\}_p\) is a bijection onto finite families of single-class data with pairwise compatible polymers. Consequently, under (a),
\[
\{\cdots\}=\sum_{r\ge0}\sum_{\substack{\{X'_1,\ldots,X'_r\}\subset\mathcal P\\\text{pairwise compatible}}}
\prod_{p=1}^r F(X'_p).\tag{4.6:eq-polymer-gas-a}
\]

(c) Every polymer is touch-connected and is the cube-wise disjoint union
\[
X'=\operatorname{core}(X')\sqcup
\bigsqcup_{i:Y_i^\sharp\subset X'}Y_i^\sharp.
\tag{4.6:eq-polymer-gas-b}
\]
Every second-class strip in X′ touches its core. Every first-class strip of a datum lies in its core. For every Y∈D, Y is touch-connected and \(Y\setminus Z(\mathfrak X)^\sharp\ne\varnothing\).

**Proof.** (a) H-locality permits an island variable in V(Y) only for X_a⊂Y. The whole-strip condition then implies X_a♯⊂Y. Since X_a♯ consists of core cubes, Y and the island have core cubes in common and belong to the same class. The operation on X_a acts only on those island variables. Thus distinct classes use disjoint integrated coordinates and histories; second-class variables are fixed parameters and may occur in several factors without coupling the integrations. Distribute the finite products and perform the independent operations to get
\[
\prod_p\left[\left(\prod_{a\in\mathfrak X_p}\mathbf T'_k(X_a)\right)
\prod_{Y\in\mathbf D_p}h_Y\right].
\]
**(filled) P1.** This is a product conditional on the outer variables, not an independence claim about a measure on those variables. The interchange of internal integrals or history sums reads the product/integrability part of H-format.

(b) Distinct classes cannot have touching core cubes, since those would already belong to one touch-component. Their polymers are therefore compatible. **(filled) P2.** Restricting to one class leaves a valid datum: its islands retain (c1)–(c3); a domain in that class cannot contain a cube of another class's first-class strip, because that cube would be in both class cores. Removing the other strips therefore changes neither its whole-strip intersection nor its nonempty off-strip cubes. The class relation also remains the same.

Conversely take compatible single-class data and unite their island and domain sets. Conditions (c1) and (c3) hold individually; (c2) holds within each datum and across data because their island strips lie in disjoint cores. For Y in the p-th datum, no cube of Y lies in another datum's first-class strip: such a cube is outside all second-class strips and would belong to both cores. Thus
\[
Y\sqcap Z(\mathfrak X)^\sharp=Y\sqcap Z(\mathfrak X_p)^\sharp.
\]
Its admissibility conditions persist, including its off-strip cubes. The cores of the union share no points across the given data, so touching creates no new cross-class connection. Every chosen domain's core lies in its original class, so gluing creates none either. Inside each datum there remains exactly one class. The two maps are inverse.

**(filled) P3.** The domain sets from distinct data cannot have a repeated Y, since Y has a nonempty core; a repetition would contradict compatibility. The same holds for an island. Hence taking unions loses no multiplicity. Single-class data with the same support also cannot coexist, by reflexivity of ι. They are alternatives summed in F, not repeated compatible polymers. Using (a), the bijection and distributivity therefore gives the stated gas sum with no factorial. The empty datum gives 1.

(c) First-class strips meet no second-class strip. A Y intersects any second-class strip in all its cubes or none, by the whole-strip condition. Their union X′ consequently has the claimed decomposition. First-class strips and all interaction domains are touch-connected. The core touch-components of a class are linked through those domains by its defining equivalence relation; a domain joins all of its own core pieces. Appending each such connected domain joins rather than separates the assembled union. Every cube in X′ is in one of these domains or a first-class strip, so X′ is touch-connected.

For a second-class strip inside X′, choose Y that contains it. Follow a chain of touching cubes in Y from this strip to a cube off Z(\(\mathfrak X\))♯, which exists. The first cube exiting the chosen strip touches it. It cannot belong to another second-class strip, because distinct strips are separated by at least M. It therefore lies in the core of X′ and touches the chosen strip. First-class strips are in the core by their separation from all second-class strips. The final assertions about Y are its definition and G3. This completes (a)–(c).

## 4. Tree geometry and finite counts

### 4.1 Relative lengths

`4.6:def-tree-lengths`, CA-I 20929–21003, uses Bałaban CMP 122b (1.67), with the strip convention. For cube unions Y,Z′, \(d_{k,Z'}(Y)\) is M⁻¹ times the shortest length of a connected finite segment union contained in Y and meeting every cube of Y∖Z′. If no such graph exists the value is +∞. Put
\[
d_\sharp(Y)=d_{k,Z(\mathfrak X)^\sharp}(Y),\quad
d_{\rm out}(X)=d_{k,\cup_iY_i^\sharp}(X).
\]
For polymers or their unions this last graph must meet every core cube. The size d_k(X), credited to CMP 109, is the shortest normalized length meeting every cube of X. Either interpretation of whether that graph must lie in X is permitted by the source. If core(X)=X, the admissible graphs for d_out are the same as, or a subset of, those for d_k, so d_k(X)≤d_out(X).

The source also records
\[
N_a=N(X_a^\sharp)\le(100\check R_k+2m_\sharp)^d\le(101\check R_k)^d.
\]
The box formula for strips and the supplied side bound give the first inequality; 2m♯≤\(\check R_k\) gives the second. For Y in a datum's class p,
\[
d_{k,Z(\mathfrak X)^\sharp}(Y)=d_{k,Z(\mathfrak X_p)^\sharp}(Y).
\]
Indeed §3.3(b) shows that removing other classes removes no strip cubes of Y, so the required hit cubes and admissible contained graphs are identical. These are consequences of H-geometry, not a new RG hypothesis. Domains with d♯=∞ have V(Y)=0 under the standing interaction bound and are dropped.

**(filled) G2.** No unproved attainment theorem is needed for the subsequent estimates: if a shortest graph has not been shown to exist, take graphs with length less than M(d+ε), for every ε>0, and let ε↓0 in the final inequality. When floor(d)=D, first choose ε<D+1−d; this preserves the strict bound (D+1)M needed in the counts. If d=∞, a finite-left-side upper bound by d is automatic. This expands the source's use of a realizing shortest graph without changing any length or constant.

### 4.2 Cubes met by a tree

**Statement `4.6:lem-tree-cubes`, CA-I 21544–21569; proof 21571–21641. Source status: proved in full. Inputs:** `4.6:def-cubes-cells`, `4.6:def-tree-lengths` (and their named geometric hypotheses for the applications).

Let Γ⊂ℝᵈ be a tree graph of length ℓM, ℓ≥0. Then
\[
\#\{n\in\mathbb Z^d:c_n\cap\Gamma\ne\varnothing\}\le5^d(\ell+1).
\tag{4.6:eq-tree-cubes-1}
\]
Consequently:
\[
N(Y\setminus Z(\mathfrak X)^\sharp)\le5^d(d_\sharp(Y)+1)
\quad(Y\in\mathcal Y(\mathfrak X),\ d_\sharp(Y)<\infty),
\]
\[
N(\operatorname{core}(X))\le5^d(d_{\rm out}(X)+1)
\quad\text{for a union of polymers},
\qquad N(X)\le5^d(d_k(X)+1)
\quad\text{for a cube union }X.
\]
The last assertion holds under either reading of d_k.

**Proof.** The finite segment union Γ is bounded, so it meets finitely many grid cubes. Let their index set be \(\mathcal N\). Greedily select a maximal subset \(\mathcal N'\) with pairwise index sup-distance at least 3. Maximality means each n∈N lies at index sup-distance at most 2 from a selected index. Each such index neighbourhood has 5 choices in each coordinate, hence 5ᵈ elements. Thus |N|≤5ᵈ|N′|.

Choose x_n∈c_n∩Γ for each selected cube. Two selected indices differ by at least 3 in some coordinate, so the corresponding closed coordinate intervals are separated by at least (3−1)M=2M. Thus |x_n−x_{n′}|≥2M. Their open radius-M Euclidean balls are disjoint.

If at least two indices were selected, fix n and a different n′. By G1 there is a polygonal simple path in Γ from x_n to x_{n′}. Stop it at its first exit from the open radius-M ball. Continuity puts the endpoint on the sphere. This path portion has length at least the distance M between its endpoints, by the triangle inequality applied to its segments. It has no repeated edge, so its length is at most the length of Γ inside the closed ball. Each nondegenerate segment meets the sphere in at most two points, so replacing the closed ball by the open ball removes no segment length. This proves that Γ has at least length M inside each of the disjoint open balls. Summing these contributions gives ℓM≥|N′|M. **(filled) G3.** The simple-path and first-exit argument makes precise the source's passage from connectedness to a lower bound on graph length; a path with arbitrary retracing would not justify that bound.

If |N′|≤1, it is already at most 1; otherwise it is at most ℓ. Hence |N′|≤max(1,ℓ)≤ℓ+1. The claimed cube estimate follows. Each graph defining one of the three relative lengths meets all cubes counted on that left side. Apply the estimate and minimize, or use G2. No containment condition is needed for the last application beyond the chosen definition of d_k.

### 4.3 Serpentine boxes

**Statement `4.6:lem-serpentine-path`, CA-I 21643–21650; proof 21652–21687. Source status: proved in full. Input:** `4.6:def-cubes-cells`.

For integers d≥1 and n₁,…,n_d≥1, let B be the box of M-cubes with indices
\(\bar n+\prod_{j=1}^d\{0,\ldots,n_j-1\}\). Write N=∏n_j here only. Then B contains a polygonal path through all cube centres, with consecutive cubes sharing a face, of length (N−1)M.

**Proof.** In one dimension use the centres in order. In dimension d, use the induction path P in the first d−1 coordinates. In layer 1 follow P, in layer 2 reverse P, and alternate. The endpoint of a layer and the start of the next have identical first d−1 coordinates and differ by M in the last; their cubes therefore share a face. Each cube is visited exactly once. Writing N′=∏_{j<d}n_j, the within-layer length is n_d(N′−1)M and the n_d−1 interlayer joins add (n_d−1)M. Their sum is (n_dN′−1)M=(N−1)M. Each centre-to-centre segment lies in its two face-adjacent cubes, so the path lies in B. This lemma is ported as the adjacent elementary geometric input; the logarithm's abstract tree bound does not require it.

### 4.4 Connected cube families

**Statement `4.6:lem-connected-families`, CA-I 21689–21693; proof 21695–21729. Source status: proved in full. Input:** `4.6:def-cubes-cells`.

For an M-cube c and integer s≥1, the number of touch-connected families \(\mathcal S\ni c\) of exactly s cubes is at most \(9^{d(s-1)}\).

**Proof.** A cube has Δ=3ᵈ−1 other touching cubes: each index difference is −1,0,1, excluding the zero vector. For each finite connected family choose a spanning tree rooted at c and traverse every edge twice, once outwards and once back. Such a traversal has 2(s−1) steps and visits precisely that family. **(filled) G4.** A spanning tree exists by starting with c and repeatedly adjoining an edge to an unvisited vertex, which connectivity supplies, until all vertices are reached. A recursive traversal visits a child subtree and returns before visiting the next; induction on its vertex count proves that it crosses each edge twice. Fix an order of neighbours and of the finite possible trees to make this a single choice per family. The walk determines its vertex set, so this coding is injective. There are at most Δ^{2(s−1)} walks of that length from c. Since Δ<3ᵈ, this is at most 9^{d(s−1)}. At s=1 the empty walk gives exactly one family. This is a symbolic counting proof, not an enumeration run.

### 4.5 Constants for the counts

`4.6:def-constant-conditions`, CA-I 21421–21465, defines, for 0<β≤1/4,
\[
A_d=5^d[(1+3^d)\log2+2d\log3],\quad C_D=4\cdot3^d e^{2A_d},
\]
\[
c_1(d)=3+5\sqrt d,\quad K_{\rm KP}(d)=4e^{2(A_d+5^d)},\quad
\bar c=\max\{\alpha^{1/3},e^{-p_0(g_k)}\}.
\]
β here is the decay fraction, not a coupling increment. The six source inequalities, with their original labels, are
\[
\tfrac12\beta\kappa\ge A_d+5^d+\log2;\tag{4.6:eq-constant-conditions-a}
\]
\[
\alpha^{1/3}\le\min\{e^{-(1+\beta)\kappa2\sqrt d-\beta\kappa/4},
\beta\kappa/(24\cdot5^dC_D)\};\tag{4.6:eq-constant-conditions-b}
\]
\[
-p_T+c_1(d)\kappa(101\check R_k)^d\le-\tfrac32p_0(g_k);\tag{4.6:eq-constant-conditions-c}
\]
\[
100^d e^{-p_0(g_k)/2}\le\beta\kappa/(16\cdot5^d);\tag{4.6:eq-constant-conditions-d}
\]
\[
3^dK_{\rm KP}(d)e^{(1+\beta/2)\kappa2\sqrt d}\bar c\le1;\tag{4.6:eq-constant-conditions-e}
\]
\[
\beta\kappa(5^{-d}\check R_k^d-1)\ge2\log K_{\rm KP}(d).\tag{4.6:eq-constant-conditions-f}
\]
Here \(p_T=2(1+\beta_0)^{-1}p_0(g_k)-\mathfrak s\), 0≤\(\mathfrak s\)≤1, from `4.6:def-standing-bounds`. These are named assumptions **H-constants**, not parameter values chosen by a run. The proofs below use (a), and later (e). The activity supplier additionally reads (b)–(d). Condition (f) is included for the definition's completeness; it is not needed for the logarithm proposition.

### 4.6 Anchored domains

**Statement `4.6:lem-anchored-domains`, CA-I 21733–21753; proof 21755–21847. Source status: proved in full from the supplied geometric data. Inputs:** `4.6:def-strips-bracket`, `4.6:def-geometric-facts` (H-geometry), `4.6:def-tree-lengths`, `4.6:lem-tree-cubes`, `4.6:lem-connected-families`, and (a) of H-constants only for (γ).

Fix admissible \(\mathfrak X\). An anchor of Y is a pair (c,S) with c a cube of \(Y\setminus Z(\mathfrak X)^\sharp\), S a whole strip contained in Y, and c touching S.

(α) Every Y∈\(\mathcal Y(\mathfrak X)\) with d♯(Y)<∞ has an anchor.

(β) For every cube c and D∈ℕ={0,1,…},
\[
\#\{Y\in\mathcal Y(\mathfrak X):c\text{ is an anchor cube of }Y,
\ \lfloor d_\sharp(Y)\rfloor=D\}\le2e^{A_d(D+2)}.
\]

(γ) Under (a) of H-constants, every cube union W obeys
\[
\sum_{\substack{Y\in\mathcal Y(\mathfrak X),\ Y\subset W\\d_\sharp(Y)<\infty}}
 e^{-\beta\kappa d_\sharp(Y)/2}
\le C_D N(W\setminus Z(\mathfrak X)^\sharp).
\]

**Proof.** Write Z♯ for the strip union. (α) A domain contains some whole strip S and at least one off-strip cube. In a touching chain inside Y from S to that cube, the first cube outside S touches S. It cannot be in another strip, since strips are nontouching. Hence it is off Z♯ and gives an anchor.

(β) Choose a realizing graph, or the approximant in G2, with length less than (D+1)M meeting all off-strip cubes and therefore c. Let \(\mathcal S\) be **all** grid cubes met by this graph, even those met only at boundaries. It is finite, contains c, and is touch-connected. Indeed a separation into two nontouching finite cube families would separate the connected graph into two nonempty disjoint closed sets. The tree-cube lemma gives \(|\mathcal S|\le5^d(D+2)\).

Y is determined by its off-strip cubes and the strips it contains. Its off-strip cubes form a subset of \(\mathcal S\). Every contained strip touches these off-strip cubes by the first-exit argument of (α), now started at that strip. A cube touches or equals at most 3ᵈ cubes, each belonging to at most one strip. Therefore there are at most \(3^d|\mathcal S|\) candidate strips. For s=|S|, the possibilities are bounded by
\(9^{d(s-1)}2^s2^{3^ds}\).
Put q=2·9ᵈ·2^{3ᵈ}≥2 and n=5ᵈ(D+2), an integer. Sum over sizes:
\[
\#\{Y\}\le\sum_{s=1}^{n}q^s
\le q^n\sum_{j=0}^{\infty}q^{-j}
=\frac{q}{q-1}q^n\le2q^n=2e^{A_d(D+2)}.
\]
**(filled) G5.** This is an overcount by codes, not a uniqueness claim for a minimizing graph. For each Y choose one admissible code (S,off-cubes,contained strips). That code reconstructs Y as their union, so distinct Y cannot share it. This justifies counting codes even when a Y has many possible graphs or anchors.

(γ) Each domain in the sum has an anchor cube in W∖Z♯. Overcount it by all such cubes and their at most 3ᵈ touching strips. In bin D=floor(d♯), its weight is at most e^{−βκD/2}. Part (β) gives
\[
\sum_Ye^{-\beta\kappa d_\sharp(Y)/2}
\le N(W\setminus Z^\sharp)\,3^d\,2e^{2A_d}
\sum_{D\ge0}e^{-(\beta\kappa/2-A_d)D}.
\]
By (a), βκ/2−A_d≥5ᵈ+log2≥log2. The geometric series is at most 2. The right side is therefore C_DN(W∖Z♯), with the printed constant unchanged. All rearrangements are of nonnegative terms; for an infinite W the statement is read as an extended nonnegative inequality.

### 4.7 Polymer count

**Statement `4.6:lem-polymer-count`, CA-I 21849–21857; proof 21859–21898. Source status: proved from the geometric part (c) of the polymer-gas lemma. Inputs:** that part of `4.6:lem-polymer-gas`, `4.6:def-tree-lengths`, `4.6:lem-tree-cubes`, `4.6:lem-connected-families`, and the count in `4.6:lem-anchored-domains`(β). H-locality is **not** used by this geometric count.

For a cube c and D∈ℕ,
\[
\#\{X'\in\mathcal P:c\in\operatorname{core}(X'),
\ \lfloor d_{\rm out}(X')\rfloor=D\}\le2e^{A_d(D+2)},
\]
and each counted polymer satisfies \(N(\operatorname{core}(X'))\le5^d(D+2)\).

**Proof.** A graph inside X′ meeting its core cubes, of length less than (D+1)M, meets c. Its cube family S is touch-connected and has at most 5ᵈ(D+2) members, by the arguments just proved. Every core cube lies in S, yielding the second bound. By §3.3(c), X′ is exactly its core plus whole second-class strips, each touching that core. Hence at most 3ᵈ|S| strips can occur. For each s there are at most 9^{d(s−1)} choices for S, at most 2ˢ choices for the core within it, and at most 2^{3ᵈs} choices for those strips. The code reconstructs X′. Summing these bounds over 1≤s≤5ᵈ(D+2) gives the same geometric series as above, namely 2e^{A_d(D+2)}. There is no factor counting island histories, because X′ denotes the support alone.

## 5. Abstract finite polymer combinatorics

### 5.1 Objects and the exponential formula

`4.6:def-abstract-polymers`, CA-I 21900–21955: a finite set \(\mathcal P\), a reflexive symmetric relation ι, and complex activities F define an abstract polymer system. Put ζ(P,Q)=0 for incompatible polymers and 1 otherwise. For a list (P₁,…,P_n), its incompatibility graph G has labelled vertices [n] and edge {i,j} when i≠j and P_iιP_j. Repeated polymers in a list are permitted. Define
\[
\rho^T(P_1,\ldots,P_n)
=\sum_{g\text{ connected on }[n]}\prod_{\{i,j\}\in g}(\zeta(P_i,P_j)-1)
=\sum_{\substack{g\subset E(G)\\([n],g)\text{ connected}}}(-1)^{|g|}.
\]
The equality holds since every edge outside G contributes zero, and each edge inside it contributes −1. For n=1 the empty graph contributes 1. If G is disconnected the sum is empty. Let τ(G) be the number of spanning trees, also 1 for a singleton and 0 for a disconnected graph. Set
\[
\Xi=\sum_{\mathfrak F\subset\mathcal P\text{ compatible}}\prod_{P\in\mathfrak F}F(P),\qquad
\Phi=\sum_{n\ge1}\frac1{n!}\sum_{(P_1,\ldots,P_n)\in\mathcal P^n}
\rho^T(P_1,\ldots,P_n)\prod_{i=1}^nF(P_i).
\]
The empty family contributes 1 to Ξ. This logarithm formula is credited by the account to Bałaban CMP 116 (2.11)–(2.13). Its justification here follows the CA proof, not the outline's alternate tree cancellation.

**Statement `4.6:lem-exponential-formula`, CA-I 21957–21966; proof 21968–22067. Source status: proved in full. Input:** the preceding definition and absolute convergence
\[
\sum_{n\ge1}\frac1{n!}\sum_{\mathcal P^n}\left|\rho^T(P_1,\ldots,P_n)\prod_iF(P_i)\right|<\infty.
\]
Then exp Φ=Ξ.

**Proof.** Replace F by zF and define
\(\Psi_n=\sum_{\mathcal P^n}\rho^T\prod_iF(P_i)\), so
\(\Phi(z)=\sum_{n\ge1}z^n\Psi_n/n!\). The absolute hypothesis makes this series uniformly absolutely convergent on |z|≤1. Thus it is continuous there and analytic on the open disc; Ξ(z) is a polynomial.

For a fixed list expand \(\prod_{i<j}\zeta(P_i,P_j)\) by writing ζ=1+(ζ−1). Every edge set on [n] decomposes uniquely into connected components. Grouping by the partition π of [n] into their vertex sets gives
\[
\prod_{i<j}\zeta(P_i,P_j)=\sum_{\pi\in\operatorname{Part}[n]}
\prod_{B\in\pi}\rho^T((P_i)_{i\in B}).
\]
For n=0 both sides are 1 with the empty partition. The left side kills any repeated or incompatible pair; otherwise it is 1. Therefore summing it times \(\prod_iF(P_i)\) over lists counts every compatible family of size n exactly n! times.

On the right, sums over polymer labels factor over the blocks of π; each block contributes Ψ_|B|. For ordered positive block sizes m₁,…,m_s summing to n, there are \(n!/(m_1!\cdots m_s!)\) ordered partitions, and dividing by s! forgets their order. Nonempty disjoint blocks remain distinct even when their sizes coincide. Hence the coefficient of zⁿ in Ξ(z) is
\[
\sum_{s\ge0}\frac1{s!}\sum_{\substack{m_1,\ldots,m_s\ge1\\\sum m_j=n}}
\prod_{j=1}^s\frac{\Psi_{m_j}}{m_j!},
\]
which is exactly the coefficient in exp Φ(z). Each coefficient calculation is finite. The convergent analytic series therefore agree near zero and throughout |z|<1; radial continuity at z=1 gives exp Φ=Ξ. **(filled) T1.** The only analytic passage is justified by the summable majorant \(\sum|\Psi_n|/n!\). It bounds the tails uniformly up to the boundary, so no zero-free assumption or chosen logarithm branch is used to prove the identity.

### 5.2 Spanning-tree cancellation on the CA route

**Statement `4.6:lem-spanning-tree-bound`, CA-I 22069–22076; proof 22078–22170. Source status: proved in full. Input:** `4.6:def-abstract-polymers`.
\[
|\rho^T(P_1,\ldots,P_n)|\le\tau(G(P_1,\ldots,P_n))
\quad(n\ge1,\ (P_1,\ldots,P_n)\in\mathcal P^n).
\]

**Proof.** For n=1 both sides equal 1. If G is disconnected, both sides equal 0 by the definitions in §5.1. Otherwise root at label 1. For a connected spanning subgraph g⊂E(G), let ℓ_g(v) be its graph distance from 1. Every v≠1 has a neighbour of depth ℓ_g(v)−1 along a shortest path. Choose the smallest-labelled such neighbour p_g(v). The edges {v,p_g(v)} are distinct: a duplicated unoriented edge from two different children would force both depths to be one less than the other. They connect every vertex to 1 by strictly decreasing depth and number n−1, so form a spanning tree T(g). **(filled) T2.** A connected n-vertex graph needs at least n−1 edges, by the vertex-adding construction in G4. If a connected graph with n−1 edges had a cycle, removal of one cycle edge would preserve connectivity and violate that lower bound. This proves the tree assertion without importing an unproved counting formula.

The decreasing-depth parent path in T(g) has length ℓ_g(v); containment T(g)⊂g gives the reverse distance inequality. Thus ℓ_{T(g)}=ℓ_g and its parent is p_g. For a rooted spanning tree T define
\[
E^*(T)=E(T)\cup\{\{u,v\}\in E(G):\ell_T(u)=\ell_T(v)\}
\cup\{\{u,v\}\in E(G):\ell_T(v)=\ell_T(u)+1,\ u>p_T(v)\}.
\]
The last set is understood with endpoints named so v is the deeper vertex.

We prove \(T(g)=T\iff E(T)\subset g\subset E^*(T)\). In the forward direction each g-edge changes graph depth by at most one. An extra edge within a depth is allowed by the second set; an extra edge from v to the previous depth has upper vertex label greater than its chosen least parent, and is allowed by the third. In the reverse direction every allowed edge changes T-depth by at most one. Any g-path from 1 to v therefore needs at least ℓ_T(v) edges. The tree path supplies at most that many, so ℓ_g=ℓ_T. Among the g-neighbours in the preceding depth, p_T(v) is present and all others have larger labels. Hence p_g=p_T and T(g)=T.

The connected spanning subgraphs are consequently partitioned into intervals
\([E(T),E^*(T)]\). Write g=E(T)∪S within an interval. Its contribution to ρᵀ is
\[
(-1)^{n-1}\sum_{S\subset E^*(T)\setminus E(T)}(-1)^{|S|}.
\]
If the optional set is nonempty, pair each subset with its toggle of one fixed optional edge; opposite signs cancel. If it is empty the sum is 1. Therefore ρᵀ is (−1)^{n−1} times the number of surviving tree intervals, at most τ(G). This retains the account's breadth-first parent partition route, rather than substituting the outline's edge-order involution.

### 5.3 Rooted-tree summation

**Statement `4.6:lem-rooted-tree-majorant`, CA-I 22172–22188; proof 22190–22348. Source status: proved in full as a summability implication. Inputs:** `4.6:def-abstract-polymers` and the following hypothesis **H-KP**. Let \(\mathsf w,a:\mathcal P\to[0,\infty)\) satisfy
\[
\sum_{P\,\iota\,Q}\mathsf w(P)e^{a(P)}\le a(Q)\qquad(Q\in\mathcal P).
\tag{4.6:eq-rooted-tree-majorant-a}
\]
Then, for each root Q,
\[
B(Q)=\sum_{n\ge1}\frac1{(n-1)!}
\sum_{(P_2,\ldots,P_n)\in\mathcal P^{n-1}}
\tau(G(Q,P_2,\ldots,P_n))\prod_{j=2}^n\mathsf w(P_j)
\le e^{a(Q)}.
\]
The series converges and its n=1 term is 1.

**Proof.** Let \(\mathcal T_n\) be all trees on [n] rooted at 1. A tree is a spanning tree of G exactly when every edge joins incompatible labels. With P₁=Q put
\[
W_T(Q)=\sum_{P_2,\ldots,P_n}\prod_{\{i,j\}\in E(T)}\mathbf1\{P_i\iota P_j\}
\prod_{j=2}^n\mathsf w(P_j).
\]
Thus \(B(Q)=\sum_{n\ge1}\sum_{T\in\mathcal T_n}W_T(Q)/(n-1)!\). All weights are nonnegative; W_T=1 when n=1. Denote the sum through n=N by B_N, and write \(\mathcal W_m(P)=\sum_{T\in\mathcal T_m}W_T(P)\).

Fix Q. Deleting the root of a tree with n≥2 vertices and root degree j gives j nonempty vertex blocks V_c partitioning {2,…,n}; each has a chosen child r_c as its root and a rooted tree T_c. Conversely such data reconstruct a unique tree by adding edges {1,r_c}. Its weight factors as
\[
W_T(Q)=\prod_{c=1}^j\sum_{P\iota Q}\mathsf w(P)W_{T_c}(P).
\]
On a block of size m, relabel its chosen root as 1 and the other labels arbitrarily. Summing all its tree weights gives \(\mathcal W_m(P)\), independent of the chosen root label. There are m choices of that root. Define \(b_m=\sum_{P\iota Q}\mathsf w(P)\mathcal W_m(P)\).

For ordered sizes m₁,…,m_j≥1 with sum n−1, the blocks can be assigned in \((n-1)!/\prod m_c!\) ways. Divide by j! for their order and multiply by ∏m_c for their child choices. Dividing the full count by (n−1)! leaves
\[
\frac1{(n-1)!}\sum_{T\in\mathcal T_n}W_T(Q)
=\sum_{j\ge1}\frac1{j!}
\sum_{\substack{m_c\ge1\\\sum m_c=n-1}}
\prod_{c=1}^j\frac{b_{m_c}}{(m_c-1)!}.
\]
**(filled) T3.** The factorial shift is \(m_c/m_c!=1/(m_c-1)!\), because a child is counted as the root of its block but is a weighted nonroot vertex of the whole tree. The factor \(\mathsf w(P)\) in b_m supplies exactly this child's weight. No child activity is dropped or counted twice.

Sum this identity over 2≤n≤N and add the singleton n=1, represented by j=0 and an empty product. Then
\[
B_N(Q)=\sum_{j\ge0}\frac1{j!}
\sum_{\substack{m_c\ge1\\\sum m_c\le N-1}}
\prod_{c=1}^j\frac{b_{m_c}}{(m_c-1)!}.
\]
Replacing the sum constraint by the individual constraints m_c≤N−1 adds only nonnegative terms. Thus for N≥2,
\[
B_N(Q)\le\exp\left(\sum_{m=1}^{N-1}\frac{b_m}{(m-1)!}\right)
=\exp\left(\sum_{P\iota Q}\mathsf w(P)B_{N-1}(P)\right).
\]
B₁=1≤eᵃ. If B_{N−1}≤eᵃ, H-KP makes the exponent at most a(Q), proving B_N≤e^{a(Q)} by induction. The partial sums are nondecreasing and bounded, hence converge to B(Q) with the same bound. This is the source's truncation by **number of vertices**, not a replacement by height truncation.

### 5.4 Consequence for finite systems and scope of exhaustion

`4.6:rem-tree-bounds-use`, CA-I 22350–22391, is proved there and is ported here as a consequence of the preceding two lemmas. If |F|≤w and H-KP holds, then
\[
\sum_{n\ge1}\frac1{n!}\sum_{\mathcal P^n}|\rho^T|\prod_i|F(P_i)|
\le\sum_{Q\in\mathcal P}w(Q)B(Q)
\le\sum_{Q\in\mathcal P}w(Q)e^{a(Q)}<\infty.
\]
Indeed the spanning-tree inequality bounds each coefficient. Split off the first vertex and replace 1/n! by 1/(n−1)!, an enlargement of nonnegative terms. The remaining series is B(Q). Finiteness of \(\mathcal P\) proves the last strict inequality, and the exponential formula gives Ξ=exp Φ.

For an infinite but locally finite support set, restrict to polymers contained in increasing bounded boxes. Every finite list occurs eventually; its incompatibility graph and weight do not change. Hence sums of **absolute nonnegative majorants pinned at a root** increase to the full pinned sum and retain any box-independent bound. A signed or complex sum itself need not increase. (correction of scope: the source says "the pinned sums are monotone in R" (CA-I 22370) and carries the exhaustion to \(\mathbb R^d\) (22855–22857); that holds for nonnegative pinned majorants only.) No finite global Φ or partition function in infinite volume follows. The proposition below is used in its finite-torus setting; its final exhaustion paragraph is read only for local and pinned bounds.

## 6. Conditional convergence and decay of the logarithm

### 6.1 Analytic inputs, with their source status

`4.6:not-complex-domain`, CA-I 20187–20286, defines \(\mathfrak U_k(X)\) as the largest domain in the printed nested chain on which **all** required inputs hold. The chain is
\[
U_k^{\rm pr}(X)\supset U_k^{\Sigma^1}(X;a_0,a_1,\gamma_0)
\supset U_k^{\rm ad}(X)\supseteq U_k^{\rm an}(X).
\]
The first is Bałaban's printed multi-scale space, the second his conditions (i)–(iv) in the account's one-power hereditary reading, the third the adopted multi-scale theorem domain, and the fourth the asserted analytic domain of the large-field increment. Shells are \((\Omega_j\setminus\Omega_{j+1})\cap X\), with radii
\(\alpha_{0,j}=g_jC_0(\log g_j^{-2})^{q_0}\) and
\(\alpha_{1,j}=g_jC_1(\log g_j^{-2})^{q_1}\), credited to CMP 119 (2.28), (2.34)–(2.39). The combinatorial theorem reads none of their defining analytic estimates.

**H-domain.** Each activity and the required majorant are defined on this common domain, uniformly in the outer variables, and restriction to X′⊂X maps \(\mathfrak U_k(X)\) into \(\mathfrak U_k(X')\). The supply of these spaces and inclusion maps is not proved here. A supremum bound on a larger set restricts to a smaller set. Composition with a restriction map preserves a supremum bound since its image lies in the target domain; applying this to tails preserves uniform convergence. This proves the domain-transfer assertion that the definition itself uses, without asserting any additional domain inclusion.

`4.6:def-standing-bounds`, CA-I 21314–21368, records the following analytic assumptions, **H-island**, **H-interaction**, **H-analytic**, respectively. For an individually admissible island and a bounded Φ,
\[
|\mathbf T'_k(X,(\mathbf U,\mathbf J))\Phi|
\le e^{\mathfrak s}(\mathbf T'_k(X,(U,0))1)\sup_X|\Phi|,
\quad\mathfrak s=c_\sigma\sup_\omega|\sigma(\omega)|\le1,
\]
\[
\mathbf T'_k(X,(U,0))1\le e^{-2(1+\beta_0)^{-1}p_0(g_k)},\quad
p_T=2(1+\beta_0)^{-1}p_0(g_k)-\mathfrak s.
\]
Here cσ∈{1,3}, and the supremum is over integration variables on the cutoff supports. Substitution gives \(|\mathbf T'_k\Phi|\le e^{-p_T}\sup_X|\Phi|\). For each admissible Y,
\[
|V(Y)|\le\alpha e^{-(1+2\beta)\kappa d_\sharp(Y)}.
\]
These hold uniformly in the indicated histories, integration variables and common complex domains. The operations on analytic Φ and the interactions are analytic there. Their source suppliers are Bałaban CMP 122b (1.73)–(1.75), (1.89), (1.68), (1.65), (1.68)–(1.69); CA-I 21370–21419 explains that positivity, the phase bound and an enlarged-domain bound printed without proof enter those suppliers. They are not proved here. The degree function is \(p_0(g)=A_0(\log g^{-2})^{p_0}\), `1.5:eq-domains-3`, CA-I 1012–1015, also named in `0.2:not-glossary`; its exponent p₀ and function p₀(·) are distinct objects.

**H-activity.** The single-polymer estimate actually read in CA-I 22733–22739 and 22750–22752 is
\[
|F(P)|\le c_1(P)e^{-(1+\beta)\kappa d_{\rm out}(P)}
 e^{-a_vN(\operatorname{core}P)/4},\qquad
 a_v=\frac{\beta\kappa}{4\cdot5^d},
\]
where \(c_1(P)=e^{-p_0(g_k)}\) if \(P\sqcap\bigcup_iY_i^\sharp=\varnothing\), and \(c_1(P)=\alpha^{1/3}\) in the other case; in particular c₁(P)≤\(\bar c\). It is uniform as specified in H-domain. The proof below needs only the weaker estimate obtained by deleting its last factor.

**Source gap retained.** At **CA-I 22393–22395**, `4.6:prop-activity-bound` is a remark saying its proposition's statement is not written out. `4.6:prf-activity-summation`, CA-I 22397–22643, is a conditional proof of a displayed estimate, assuming earlier unnamed claims (i),(ii), a first-step bound and localization. Its assumptions are explicit at 22398–22414; its conclusion is at 22415–22422. This note does not supply those missing pieces. The logarithm proposition's phrase “the remaining hypothesis listed there” has no complete list at the referenced proposition. Therefore **H-activity is carried, not discharged** from H-island and H-interaction. The case assignment above is confirmed in the logarithm proof at 22777–22783; it is not inferred from the names “Case A/B” alone. The missing locality/remaining-hypothesis package is retained as **H-activity-supplier**, with no claim that its full original statement can be recovered here.

### 6.2 Definition of the local logarithm

`4.6:def-polymer-logarithm`, CA-I 21005–21034, uses the same ζ and ρᵀ as §5 and sets
\[
\mathbf R'^{(k)}(X)=\sum_{n\ge1}\frac1{n!}
\sum_{\substack{(P_1,\ldots,P_n)\in\mathcal P^n\\\bigcup_iP_i=X}}
\rho^T(P_1,\ldots,P_n)\prod_{i=1}^nF(P_i).
\]
The boundary group consists of X with \(X\sqcap|\mathcal O|^\boxplus\ne\varnothing\), where
\(|\mathcal O|^\boxplus=Z_k^\boxplus\cup\bigcup_iY_i^\boxplus\); there the source writes \(\mathbf B'^{(k)}(X)=\mathbf R'^{(k)}(X)\). The second group has no common cube with that enlargement. The group split uses the cell enlargement ⊞, not the narrower strip ♯. The identity of the bracket with the exponential of this series is a conclusion, not part of its definition. Credits: CMP 116 (2.13), CMP 122b (1.98) and p.390.

### 6.3 Statement

**`4.6:prop-logarithm-convergence`, CA-I 22645–22680; proof 22686–22858. Source status: an unqualified proved implication, with the activity-supplier gap just recorded.** For the identity \(\{\cdots\}=\exp\sum\mathbf R'(X)\) only, assume also the printed-without-proof locality of interaction terms (Balaban), which the polymer-gas representation needs; the decay bound and absolute convergence do not need it. Assume the hypotheses of `4.6:prop-activity-bound`: the family island-integral bound, strip interaction bound, localization statement and remaining hypothesis listed there; also `4.6:eq-constant-conditions-a`, the ceiling on α¹ᐟ³ and the two coupling conditions of `4.6:def-constant-conditions`. Assume the format statement underlying `4.6:lem-polymer-gas`, and additionally `4.6:eq-constant-conditions-e`. Then, for every union X of M-cubes, the series defining \(\mathbf R'^{(k)}(X)\) converges absolutely, uniformly in outer variables and on \(\mathfrak U_k(X)\), and
\[
|\mathbf R'^{(k)}(X,(\mathbf U,\mathbf J))|
\le K_{\rm KP}(d)c_1(X)e^{-(1+\beta/2)\kappa d_{\rm out}(X)},
\tag{4.6:eq-logarithm-convergence-a}
\]
where
\[
c_1(X)=\begin{cases}
e^{-p_0(g_k)},&X\sqcap\bigcup_iY_i^\sharp=\varnothing,\\
\bar c,&\text{otherwise},
\end{cases}\qquad K_{\rm KP}(d)=4e^{2(A_d+5^d)}.
\]
Moreover, the full connected series
\[
\Phi=\sum_{n\ge1}\frac1{n!}\sum_{\mathcal P^n}\rho^T(P_1,\ldots,P_n)\prod_iF(P_i)
\]
is absolutely convergent, and
\(\{\cdots\}=\exp\sum_X\mathbf R'^{(k)}(X)\).

The full Φ assertion is for the finite polymer system of the step. On ℝᵈ, the account's concluding exhaustion argument supplies uniform local/pinned bounds, as specified in §5.4. No infinite-volume total partition function is asserted in this port.

**Inputs by label.** `4.6:prop-activity-bound` is H-activity/H-activity-supplier, not proved here and not stated in full at its source. `4.6:not-complex-domain` is H-domain. `4.6:def-standing-bounds` gives H-island, H-interaction, H-analytic, all analytic hypotheses. `4.6:def-constant-conditions` supplies H-constants. `4.6:lem-polymer-count`, `4.6:lem-spanning-tree-bound`, `4.6:lem-rooted-tree-majorant`, `4.6:lem-exponential-formula` are proved here. `4.6:lem-polymer-gas` is proved here conditional on H-format, H-geometry and H-locality. The proof first assumes the explicit H-activity estimate; this does not silently replace a missing supplier by a proved proposition.

### 6.4 Proof on the source route

Only lists whose incompatibility graph G is connected contribute, since otherwise ρᵀ=0. If no such list has union X, its local logarithm is zero. Assume there is one. Write
\(t=(1+\beta/2)\kappa\) and \(b=2\sqrt d\) only as abbreviations in this proof.

**Tree extraction.** For a contributing list choose graphs Γ_p⊂P_p meeting all its core cubes, and a spanning tree of G. If {p,q} is an edge of this tree, their cores have touching cubes c,c′ with a common point z. Join a point of Γ_p∩c to z inside c and then to a point of Γ_q∩c′ inside c′. Each segment has length at most √d M. The n−1 joins produce a connected segment union inside X, meeting every cube of \(\bigcup_p\operatorname{core}(P_p)=\operatorname{core}(X)\). Its length is at most \(M\sum_pd_{\rm out}(P_p)+bM(n-1)\). Hence
\[
d_{\rm out}(X)\le\sum_pd_{\rm out}(P_p)+b(n-1).
\tag{4.6:eq-logarithm-convergence-2}
\]
**(filled) G6.** The connected union already meets the source definition of a tree graph. To implement the source's additional spanning-tree sentence literally, first mark a hit point in each required core cube and subdivide every segment at those points and all junctions. A graph spanning tree retains every marked vertex, so still meets all required cubes. If shortest graphs are replaced by ε-approximants, use ε/n in each of the n constituents and let ε↓0 afterwards. No attainment or loss of a cube is hidden in this step.

Define
\(\widetilde w(P)=|F(P)|e^{t(d_{\rm out}(P)+b)}\). The extracted inequality gives
\[
e^{t d_{\rm out}(X)}\prod_p|F(P_p)|
\le e^{-tb}\prod_p\widetilde w(P_p).
\tag{4.6:eq-logarithm-convergence-4}
\]
H-activity, after dropping its volume factor, gives
\[
\widetilde w(P)\le c_1(P)e^{tb}e^{-\beta\kappa d_{\rm out}(P)/2}.
\tag{4.6:eq-logarithm-convergence-5}
\]
A polymer with d_out=∞ has zero activity under H-activity and may be removed; define its majorant as zero before using weighted formulas. No product 0·∞ is needed.

**Summability.** Put a(P)=N(core P). If PιQ, choose a core cube c″ of Q and a touching or equal cube c′ in the core of P. There are at most 3ᵈ choices for c′ for each c″. In bin D=floor(d_out(P)), §4.7 bounds the number of P through c′ by 2e^{A_d(D+2)}, and bounds a(P) by 5ᵈ(D+2). All those d_out(P) are at least D. Therefore
\[
\begin{aligned}
\sum_{P\iota Q}\widetilde w(P)e^{a(P)}
&\le a(Q)3^d\bar c e^{tb}
\sum_{D\ge0}2e^{A_d(D+2)}e^{5^d(D+2)}e^{-\beta\kappa D/2}\\
&=a(Q)3^d\bar c e^{tb}\,2e^{2(A_d+5^d)}
\sum_{D\ge0}e^{-(\beta\kappa/2-A_d-5^d)D}\\
&\le a(Q)3^d\bar c e^{tb}K_{\rm KP}(d)\le a(Q).
\end{aligned}
\]
The penultimate inequality uses (a), giving a geometric ratio at most 1/2; the last is (e). This establishes H-KP for \(\widetilde w,a\), rather than assuming it for these activities.

**(filled) L1.** The pinned estimate mentioned as “the same computation” in the source is as follows. Fix a cube c₀ and restrict to polymers P⊂X with c₀∈core P. There is no sum over c″ or neighbouring c′, and thus no factor a(Q)3ᵈ. Moreover c₁(P)≤c₁(X): if X has no second-class strip cube neither does P, and otherwise c₁(P)≤\(\bar c=c_1(X)\). Hence, explicitly,
\[
\begin{aligned}
\sum_{\substack{P\subset X\\c_0\in\operatorname{core}P}}\widetilde w(P)e^{a(P)}
&\le c_1(X)e^{tb}\,2e^{2(A_d+5^d)}
\sum_{D\ge0}e^{-(\beta\kappa/2-A_d-5^d)D}\\
&\le c_1(X)e^{tb}K_{\rm KP}(d).
\end{aligned}\tag{4.6:eq-logarithm-convergence-6}
\]

**Assembly.** A contributing X has a nonempty core, since every polymer does. Choose one core cube c₀. In every list with union X at least one entry's core contains c₀. Let m(s) be the number of such entries. For each fixed n, multiply the nonnegative tree majorant by m(s)≥1. Symmetry under permutations of the labelled list makes the n choices of the distinguished entry equal. Thus
\[
\begin{aligned}
\sum_{n\ge1}\frac1{n!}\sum_{\cup P_i=X}\tau(G)\prod_i\widetilde w(P_i)
&\le\sum_{n\ge1}\frac1{(n-1)!}
\sum_{\substack{\cup P_i=X\\c_0\in\operatorname{core}P_1}}
\tau(G)\prod_i\widetilde w(P_i)\\
&\le\sum_{\substack{P_1\subset X\\c_0\in\operatorname{core}P_1}}
\widetilde w(P_1)B_{\mathcal P_X}(P_1).
\end{aligned}
\]
Here \(\mathcal P_X=\{P:P\subset X\}\); the second inequality relaxes the exact-union condition to containment for each entry. H-KP still holds after restriction to this subsystem, since its left side becomes smaller. The rooted-tree lemma bounds B_{P_X}(P₁) by e^{a(P₁)}; L1 then bounds the last display by c₁(X)e^{tb}K_KP.

**(filled) L2.** The n-factor above is taken separately at each n before the sum over n; it is n/n!=1/(n−1)!, including n=1. Repetitions cause no change: permuting labelled positions is a bijection of lists even if several positions carry the same polymer. All interchanges can first be made in finite nonnegative truncations and then passed to their increasing suprema.

Apply the spanning-tree bound to |ρᵀ| and the extracted estimate to the product of activities. The **series of absolute values**, not only the absolute value of its sum, is bounded by
\[
e^{-td_{\rm out}(X)}e^{-tb}
 c_1(X)e^{tb}K_{\rm KP}(d)
=K_{\rm KP}(d)c_1(X)e^{-td_{\rm out}(X)}.
\]
This proves absolute convergence and exactly the stated local decay constant.

**Full finite series and identity.** Since d_out≥0 and t,b>0, |F(P)|≤\(\widetilde w(P)\). Rooting at the first vertex as in §5.4 yields
\[
\sum_{n\ge1}\frac1{n!}\sum_{\mathcal P^n}|\rho^T|\prod_i|F(P_i)|
\le\sum_{P\in\mathcal P}\widetilde w(P)B(P)
\le\sum_{P\in\mathcal P}\widetilde w(P)e^{a(P)}<\infty.
\]
The last sum is finite because \(\mathcal P\) is finite. The exponential formula gives Ξ=exp Φ. H-locality and the separately proved gas representation give Ξ=\(\{\cdots\}\). Absolute convergence permits grouping all lists by their union, giving \(\Phi=\sum_X\mathbf R'^{(k)}(X)\). This proves the desired bracket identity.

**(filled) L3: uniformity.** A pointwise bound for the total sum alone would not prove uniform tails. To obtain them, repeat all nonnegative estimates with the field-independent weight
\[
w_*(P)=c_1(P)e^{tb}e^{-\beta\kappa d_{\rm out}(P)/2}
\]
in place of \(\widetilde w\). It dominates \(\widetilde w\) simultaneously on the common domain and for all outer variables covered by H-activity. The very same cube-bin computation proves H-KP for w_*. The rooted-tree sums for w_* are convergent numerical **series defined by a written estimate**, not evaluated by a computer. They dominate every term of the local and finite global absolute series uniformly. Given ε>0, a finite part of this convergent nonnegative majorant has tail below ε; the same tail bound then holds at every parameter value. This is the required uniform convergence. The restriction maps in H-domain make each activity admissible at the field restricted from X. No additional analyticity-domain inclusion is deduced.

For polymers in ℝᵈ, apply the same argument to the finite systems of supports inside boxes. The root estimates and local estimates above do not contain the box side. Increasing boxes therefore gives the corresponding local absolute majorants by monotone limits. It does not make the extensive unrooted sum finite, as explained in §5.4. This finishes the finite proposition and its local exhaustion consequence on the source route.

## Recovery checkpoint

The port is complete as a set of written implications, with the input boundaries recorded above. The two raw files were already present and were reused without a second download. Their SHA-256 identities match the pinned source identities recorded in `library/chain-ca.md` §8:

| Source | SHA-256 |
|---|---|
| CA-I, `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| Outline, `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |

Only bounded source excerpts were returned for mathematical reading. File hashing, anchor location and text editing were bookkeeping, not mathematical evidence. The outline index has no rows bearing the CA-specific tree-cube, serpentine, anchored-domain or polymer-count labels; those were located in ca-full and read at the CA lines cited above. The related outline locality/gas passage is indexed in chunk 16 at 17959–17997 and was read with its neighbours. No conclusion about the absence of a proof elsewhere in the account is drawn from a failed label search.

The next independent reader should check the written port once, retaining H-locality and H-activity. A later analytic lane must supply the actual activity estimate and its missing supplier statement before this logarithm implication can be applied unconditionally to the RG. No alternative proof route was attempted, and no failed route was concealed. No editable prompt file, GOAL, FINISH, skill, ledger or audit file was modified. Platform instructions were not modified.

## Result

This is a **port of the complete account's proofs**, with filled steps. It is research text, not an audit. No retained status or proof of T0 is granted.

The following statements have been ported on the source routes, with definitions, mathematical statements, source lines, source-declared status, full written conditional proofs and explicit inputs:

| Statement | CA-I source | Port |
|---|---:|---|
| `1.1:lem-invariance` | 559–604 | §1, Wilson action and measure invariance |
| `4.2:lem-first-passage` | 3636–3721 | §2.2, including K=0 and finite initial sequence |
| `4.19:lem-flow-bounds` | 56342–56412 | §2.1, summed per-step arithmetic |
| `4.6:lem-polymer-gas` | 20757–20927 | §3.3, separate conditional representation |
| `4.6:lem-tree-cubes` | 21544–21641 | §4.2, retaining 5ᵈ(ℓ+1) |
| `4.6:lem-serpentine-path` | 21643–21687 | §4.3 |
| `4.6:lem-connected-families` | 21689–21729 | §4.4, retaining 9^{d(s−1)} |
| `4.6:lem-anchored-domains` | 21733–21847 | §4.6, all three clauses |
| `4.6:lem-polymer-count` | 21849–21898 | §4.7 |
| `4.6:lem-exponential-formula` | 21957–22067 | §5.1 |
| `4.6:lem-spanning-tree-bound` | 22069–22170 | §5.2, the CA parent-partition proof |
| `4.6:lem-rooted-tree-majorant` | 22172–22348 | §5.3, the CA vertex-count truncation |
| `4.6:rem-tree-bounds-use` | 22350–22391 | §5.4, finite convergence and pinned exhaustion |
| `4.6:prop-logarithm-convergence` | 22645–22858 | §6, conditional on the explicit activity estimate and supplier package |

Every marked completion is listed here:

| Mark | Filled step |
|---|---|
| W1 | Explicit finite normalization bounds. |
| W2 | Right Haar invariance, inversion, coordinate permutations and inverse transformations. |
| F1 | Empty interval and the B♯≤Cβ+1 consequence, without asserting stepwise positivity. |
| F2 | Archimedean integer choice and finite extension induction. |
| G1 | Polygonal paths in touching cubes and finite segment unions; removal of overlap multiplicity. |
| G2 | ε-approximants in place of an unproved minimum-attainment assertion. |
| G3 | A simple first-exit path establishes the length in each disjoint ball. |
| G4 | Spanning-tree construction, the double traversal, and injectivity of the cube-family code. |
| G5 | Reconstruction from counting codes despite nonunique realizing graphs. |
| G6 | Preserving hit points under spanning-tree extraction and the ε/n allocation. |
| P1 | Conditional factorization at fixed outer variables; history/integral regrouping reads H-format. |
| P2 | Restricting a datum to a class preserves interaction-domain admissibility. |
| P3 | No repeated domain or island across compatible class data; no missing factorial. |
| T1 | Uniform scalar power-series majorant and the endpoint z=1. |
| T2 | Connected n-vertex, n−1-edge graphs are trees. |
| T3 | Child-root weights and the factorial shift m/m!=1/(m−1)!. |
| L1 | The pinned cube-bin estimate with c₁(X) and no 3ᵈ factor. |
| L2 | Root marking at each fixed n, including repeated polymer labels. |
| L3 | A parameter-independent termwise majorant proves uniform tails. |

**Corrections.** One correction of scope (the monotonicity of pinned sums, §5.4); no correction to the finite statements or their constants. The source's absent `4.6:prop-activity-bound` statement is a retained gap, not silently repaired. The original reference is **CA-I 22393–22395**. The infinite-volume remark is used for absolute pinned majorants only; finiteness of the total Φ is kept in its finite-system setting. The filled steps are not claims of errors in the source.

**Named hypotheses carried.** H-Haar retains the normalized Haar existence/uniqueness input of `1.1:def-wilson-action`. H-flow-1 and H-flow-2 are precisely `4.19:eq-flow-bounds-1`,`2`; H-next is the extension-and-bound premise of `4.2:lem-first-passage`. H-RG retains actual increment construction and its incomplete one-loop/unmarked suppliers; the arithmetic port does not prove them. H-format and H-geometry retain the step's island-operation, admissibility and component-box supply in `4.6:def-step-datum`, `4.6:def-strips-bracket`, and `4.6:def-geometric-facts`. **H-locality is the printed-without-proof input `4.6:rem-interaction-locality`, explicitly assumed at CA-I 20767.** H-domain retains the common domains and restriction maps of `4.6:not-complex-domain`. H-island, H-interaction and H-analytic are the three clauses of `4.6:def-standing-bounds`. H-constants retains the applicable one-sided conditions in `4.6:def-constant-conditions`. **H-activity and H-activity-supplier retain the explicit single-polymer estimate and its incompletely specified supplier `4.6:prop-activity-bound`.** H-KP remains the abstract tree lemma's hypothesis; §6 proves it for the indicated majorant from the geometric count, H-activity and constants (a),(e). The exponential formula's absolute-convergence premise is likewise proved for that finite application. No analytic premise is discharged merely by deriving H-KP conditionally.

Credit throughout belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and to Tadeusz Bałaban for the source constructions and formulas named above. Codex wrote this port and its filled steps. **This text has not yet been checked by another model.**

## Change log (check, 2026-11-05)

Ported by Codex. Checked line by line by a fresh Claude session ([p1-base-gate](../../gates/p1-base-gate.md)): first failing step none; 3 findings, all repairable; 11 statements ported faithfully, 3 with repairs. Applied by the lead (Claude):

1. `4.2:lem-first-passage`: the source's initial-segment sentence (CA-I 3684–3685) restored.
2. `4.6:prop-logarithm-convergence`: Balaban's printed locality hypothesis named in the statement, for the identity clause only.
3. `4.6:rem-tree-bounds-use`: the monotonicity of pinned sums marked as a correction of scope.

Gap in their text, confirmed: `4.6:prop-activity-bound` is a placeholder remark at CA-I 22393 ("not written out here; parts of its proof are printed below"), cited as a Proposition 14 times (CA-I 22398–23022), absent from CA-II and CA-III. The port keeps it as a named hypothesis.

Status: **checked port.**

