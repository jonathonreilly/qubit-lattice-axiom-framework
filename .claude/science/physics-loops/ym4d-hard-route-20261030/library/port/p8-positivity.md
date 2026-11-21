# P8: Positivity and compactness — port of complete-account tranche 7

Provenance: Codex (GPT-6 family), 2026-11-05, checkout `0dfd1df554229fb5bbcae22e26e6490ce8b89075`. Research text, not an audit; grants no status. This port has not yet been checked by another model. All arguments are by hand; source retrieval and text navigation are not proof steps.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at commit `31a47c543775`; Tadeusz Balaban for the lattice gauge theory and renormalisation constructions they use. The route below is theirs. Added details are marked **(filled)** and changes to a printed claim are marked **(correction)**.

Source convention: `I:L` and `II:L` mean lines of `theorem_0_complete_account_raw_I.tex` and `theorem_0_complete_account_raw_II.tex` at that commit. `SA:L` means `YM4_sketch_500.tex`. All three pinned raw files were fetched once in this session; they matched the cached text used for the excerpts. A source heading's “proved” standing describes the account, not an independent check here. Every unproved antecedent remains a named hypothesis.

Round 1 completes B5, B7 and B8 below. The concluding Result records the exact stopping point and retained hypotheses.

## 1. Scope, sources, and standing of inputs

This round ports chain-ca §7.2 tranche 7, starting with B5, B7 and B8. The prescribed route is the complete account. The outline is a navigation and comparison source. In particular, its all-periodic-state results are not silently substituted for the finite-torus statements below.

The outline index was searched for reflection positivity, chessboard estimates, support placement, periodisation, ultraviolet bounds and compactness. Relevant neighbouring entries are in `sa-index/chunk-01.md` (SA:473–563), `chunk-03.md` (SA:2773–2942), and `chunk-22.md` (SA:23621–24364 and 24541–24718). Their obligations are collected in `sa-index/obligations.md`. They distinguish finite positivity and conditional compactness from the source estimates they need. The complete-account index `sa-index/ca-full/index.tsv` locates the numbered statements below. Their status is read again at each source heading. Under I:27–46, an unqualified proof heading means proved there, possibly as an implication.

The following inputs retain their supplied repository standing:

* **P1**, `p1-base.md`; **P3**, `p3-free.md`; **P4**, `p4-operator.md`; **P5**, `p5-induction.md`; **P7**, `p7-torus.md`: checked ports, each conditional on its own named inputs. P1 supplies finite Wilson conventions and first-passage arithmetic. P7 ports A14, including its seven hypotheses; its title does not close those hypotheses.
* **P6**, `p6-correlation.md`: ported, not yet checked. We use its conditional correlation theorem B3, `5.1:thm-correlation-theorem`, II:2791–2966, only through the explicit interfaces below. Its unproved source/weight inputs remain attached.
* **LSC**, `../lsc.md`: frozen. It supplies `6.3:lem-last-scale-constants` in the vacuum-normalized convention, with its flow, representation, real-background and sourced-majorant hypotheses. The account's own statement is unwritten at II:63365–63367; it is not independently a proved source lemma.
* `../mu.md`, `../lrb.md`, `../oc.md`, `../ui.md`, `../pda.md`: refereed inputs available to this lane. Their conclusions are not assumed to be identical to a CA statement merely because they treat related objects. The portion completed below does not need to invoke them.

No inherited RG implication is proved anew here. No result below establishes the full target T0. In particular, an off-diagonal limit does not itself supply full O(4), clustering, or Wightman reconstruction.

## 2. B5: finite-lattice reflection positivity

### 2.1 Exact statement and conventions

**`6.1:lem-reflection-positivity`, II:60440–60465; proof II:60467–60624. Source status: proved, with no incomplete/outstanding qualifier.** Work in last-lattice units. The torus is \(\mathbb T=\mathbb R^4/N\mathbb Z^4\), the bare spacing is \(\varepsilon=L^{-K'}\), and sites lie in \(\varepsilon(\mathbb Z+\tfrac12)^4\). For \(c\in\varepsilon\mathbb Z\) and a coordinate \(\mu\), set
\[
 \Pi=\{x_\mu=c\}\cup\{x_\mu=c+N/2\},\qquad
 \theta x=(x_1,\ldots,2c-x_\mu,\ldots,x_4).
\]
Here the Chapter 6 units have \(N=2L^{m+b}\), with \(m,b\ge0\) integers and \(L>1\) an integer. Thus \(N/2\in\mathbb Z\subset\varepsilon\mathbb Z\). Let \(H_\pm\) be the open components of \(\mathbb T\setminus\Pi\). Neither plane contains a site, because integer and half-integer mesh coordinates are distinct. On bonds in \(H_+\), \(\theta\cdot U\) reads the reflected bond variable, with inversion if the reflection reverses its positive orientation. For every bounded measurable complex function \(F\) of the bonds in \(H_+\),
\[
 \langle F(\theta\cdot U)\rangle=\langle F(U)\rangle,
 \qquad
 \langle\overline{F(\theta\cdot U)}F(U)\rangle\ge0.
 \tag{P8.1}
\]
In fact the Wilson measure is invariant under every torus isometry preserving the bare lattice. These are precisely clauses (i) and (ii) of the source statement.

Here \(G=SU(N_{\rm col})\), the trace has \(\operatorname{tr}1=1\),
\[
 a_p(U)=1-\operatorname{Re}\operatorname{tr}U(\partial p),\quad
 A(U)=\sum_pa_p(U),\quad
 d\mu=Z_{\rm bare}^{-1}e^{-x_0A(U)}dU,\quad x_0>0.
\]
The bonds are oriented lattice edges, including their periodic edge labels. Haar measure on each bond is normalized. Each diagonal entry of a unitary matrix has modulus at most one, so its normalized real trace lies in \([-1,1]\). Thus \(0\le a_p\le2\), and the finite integral \(Z_{\rm bare}\) is positive.

### 2.2 Proof on the account's crossing-kernel route

An isometry permutes bonds and may invert their variables. Product Haar measure is invariant under both operations. It permutes plaquettes. Cyclic changes of a loop preserve its trace, and reversing a loop conjugates its trace. Thus it preserves \(A\), proving the first assertion.

Split the bonds into the two open halves and the crossing links. Each crossing link \(\ell_x\) is oriented from \(H_-\) to \(H_+\). A plaquette either lies in one open half or has two crossing links in one of the two planes. Write its two parallel tangential links as \(b^+_{x,\nu}\), \(b^-_{x,\nu}\), with the same orientation, for \(\nu\ne\mu\). Its holonomy is
\[
 W_{x,\nu}=U(\ell_x)U(b^+_{x,\nu})
 U(\ell_{x+\varepsilon e_\nu})^{-1}U(b^-_{x,\nu})^{-1}.
\]
Consequently
\[
 A=A_+(U_+)+A_-(U_-)+A_\times(U),\qquad
 A_-(U_-)=A_+(\theta\cdot U_-).
 \tag{P8.2}
\]
The source expands \(\varphi(W)=\exp(x_0\operatorname{Re}\operatorname{tr}W)\) into positive character coefficients. We give an explicit expansion of the same type, so that its convergence needs no unproved Fourier-decay assertion.

**(filled: positive character series and convergence.)** Let \(V\) be the defining unitary representation of dimension \(d=N_{\rm col}\), and let \(R=V\oplus\overline V\). Then
\[
 \operatorname{Re}\operatorname{tr}W=\frac{\chi_R(W)}{2d},\qquad
 \varphi(W)=\sum_{q=0}^\infty a_q\chi_{R^{\otimes q}}(W),\qquad
 a_q=\frac{x_0^q}{q!(2d)^q}\ge0.
 \tag{P8.3}
\]
The term \(q=0\) is the trivial representation. The identity follows by the exponential series and the trace identity for tensor products. Put \(d_q=(2d)^q\). For each fixed integer \(k\ge1\),
\[
 \sum_{q\ge0}a_qd_q^k
 =\sum_{q\ge0}\frac{[x_0(2d)^{k-1}]^q}{q!}<\infty.
\]
The ratio of consecutive summands eventually is at most \(1/2\), which proves convergence by a geometric tail. In particular (P8.3) converges uniformly, since \(|\chi_{R^{\otimes q}}|\le d_q\). Every matrix-index expansion below has at most a fixed power of \(d_q\) indices per plaquette. There are finitely many plaquettes. The displayed bound therefore proves absolute uniform convergence of every expanded integral. Reducible unitary representations work in the source's factorization exactly as irreducible ones do.

For a unitary representation \(D\), direct matrix multiplication gives
\[
 \chi_D(\sigma_1\sigma_2\sigma_3^{-1}\sigma_4^{-1})
 =\sum_{i,j,k,l}D_{ij}(\sigma_1)D_{jk}(\sigma_2)
 \overline{D_{lk}(\sigma_3)}\,\overline{D_{il}(\sigma_4)}.
 \tag{P8.4}
\]
Expand each crossing plaquette by (P8.3)–(P8.4). Since \(F\) reads no crossing link, integrate those links first. For fixed representation labels the integral at \(\ell_x\) is
\[
 I_x(i,l;j,k)=\int d\sigma\prod_{\nu\ne\mu}
 D^{q_{x,\nu}}_{i_{x,\nu}j_{x,\nu}}(\sigma)
 \overline{D^{q_{x-\varepsilon e_\nu,\nu}}_{l_{x-\varepsilon e_\nu,\nu}k_{x-\varepsilon e_\nu,\nu}}(\sigma)}.
\]
Haar invariance permits replacing \(\sigma\) by \(\sigma'\sigma''^{-1}\), integrated in both variables. Expand each matrix product. With intermediate indices \(m,m'\), define
\[
 u_x^{m,m'}(i,l)=\int d\sigma\prod_{\nu\ne\mu}
 D^{q_{x,\nu}}_{i_{x,\nu}m_\nu}(\sigma)
 \overline{D^{q_{x-\varepsilon e_\nu,\nu}}_{l_{x-\varepsilon e_\nu,\nu}m'_\nu}(\sigma)}.
\]
The \(\sigma'\) integral is this expression. The \(\sigma''\) integral is its complex conjugate with \((j,k)\) in place of \((i,l)\). Thus
\[
 I_x(i,l;j,k)=\sum_{m,m'}u_x^{m,m'}(i,l)
                           \overline{u_x^{m,m'}(j,k)}.
 \tag{P8.5}
\]
Put \(\alpha=(q(\cdot),m(\cdot),m'(\cdot))\),
\[
 c_\alpha=\prod_{x,\nu}a_{q_{x,\nu}}\ge0,\qquad
 G_\alpha(U_+)=\sum_{j,k}\prod_x\overline{u_x^{m,m'}(j,k)}
             \prod_{x,\nu}D^{q_{x,\nu}}_{j_{x,\nu}k_{x,\nu}}(U(b^+_{x,\nu})).
\]
After summing \((i,l)\), (P8.5) proves
\[
 \int\prod_xdU(\ell_x)\prod_{x,\nu}\varphi(W_{x,\nu})
 =\sum_\alpha c_\alpha G_\alpha(U_+)
                       \overline{G_\alpha(\theta\cdot U_-)}.
 \tag{P8.6}
\]
Here reflection carries each tangential plus link to the minus link with the same orientation. The two planes give independent crossing-link integrals. Their positive sums multiply and have the same form (P8.6).

**(correction: endpoint of the geometry assertion.)** II:60604 uses \(N/2\ge1>\varepsilon\). At \(K'=0\), the second inequality can be equality. What the proof needs is disjoint sets of crossing edge labels and crossing plaquettes at the two planes. They remain disjoint when \(N/2=\varepsilon\): the two periodic links joining the two layers have different edge labels, and each crossing plaquette uses only one plane's links. Thus the argument includes this endpoint; it does not rely on the printed strict inequality.

If \(P_\times\) counts crossing plaquettes, (P8.2) and (P8.6) give
\[
 \int\overline{F(\theta\cdot U)}F(U)e^{-x_0A(U)}dU
 =e^{-x_0P_\times}\sum_\alpha c_\alpha
 \left|\int F(U_+)G_\alpha(U_+)e^{-x_0A_+(U_+)}dU_+\right|^2\ge0.
\]
The change \(U_-\mapsto\theta\cdot U_-\) preserves product Haar measure. The convergence just proved justifies every integration and sum, even for bounded measurable \(F\). Divide by \(Z_{\rm bare}>0\). This proves (P8.1).

### 2.3 Reflection form

**`6.1:cor-reflection-form`, II:60634–60690. Source status: proved.** For bounded half-algebra functions,
\[
 (F,G)_\theta=\langle\overline{F(\theta\cdot U)}G(U)\rangle
\]
is a Hermitian positive semidefinite sesquilinear form, and
\[
 |(F,G)_\theta|^2\le(F,F)_\theta(G,G)_\theta.
 \tag{P8.7}
\]
The same positivity holds in the other open half. Indeed sesquilinearity is immediate from the integral. Invariance and \(\theta^2=1\) give Hermitian symmetry. Positivity was proved above. **(filled)** If \((F,F)>0\), apply positivity to \(G-tF\) with \(t=(F,G)/(F,F)\). Expanding gives \(0\le(G,G)-|(F,G)|^2/(F,F)\). If \((F,F)=0\), the same expansion is \((G,G)-2\operatorname{Re}(\bar t(F,G))\); choosing \(t=s(F,G)\) and letting \(s\to+\infty\) forces \((F,G)=0\). Both cases give (P8.7). Finally reflect a function from the minus half into the plus half and apply (P8.1).

## 3. B7 inputs and finite chessboard lemmas

### 3.1 Named hypotheses, with normalization fixed before estimates

**H0 (ordinary analysis and compact-group integration).** We use the real and complex number fields with completeness, ordinary compactness and countable choice, normalized Haar measure on compact groups with its left/right/inversion invariance, integration of absolutely convergent series, and the finite-dimensional Cauchy integral formula and maximum principle. These foundational results are not re-proved here. All representation identities used in §2 were written out. No machine certificate is an input.

**H-LOC (the correlation theorem's local-energy interface).** This is `6.2:def-localised-terms`, II:60692–60821, read from B3 rather than supplied by positivity. Write \(s_j=ML^{j-K'}\). Let \(D_j\) consist of wall-connected unions of scale-\(j\) cubes of side \(s_j\). Let \(X^+\) add one touching-cube layer, and let \(d_j(X)\) be the minimal length of a tree meeting all cubes of \(X\), in units of \(s_j\). A plaquette belongs to \(\operatorname{plaq}(X^+)\) when it intersects \(X^+\). Set
\[
 e_j(X;v)=e^{(j)}(X;v)-e^{(j)}(X;0),\qquad
 \mathcal E(v)=\sum_{j=0}^{K'}\sum_{X\in D_j}e_j(X;v).
\]
Retain these exact clauses:

* **(L)** \(e_j(X;v)\) reads only the values \(v(x_p)\) for \(p\in\operatorname{plaq}(X^+)\). It is zero when those values are zero.
* **(A)** The terms are holomorphic in the admitted source variables.
* **(B)** \(|e_j(X;v)|\le C_e\exp[-(1-\delta)\kappa d_j(X)]\).
* **Representation independence:** the production formula defines a function of the weight, independent of the list of sources representing that weight.

The constants and domains are those of B3, including its named inputs and its outstanding window-data statement, II:2810–2812. P6 is ported but not yet checked. These four clauses remain hypotheses here.

**H-STAB/LSC (upper bound and floor in one convention).** Write
\[
 \widehat Z(v)=e^{-E_{\rm vac}}Z_{\rm bare}(v),\qquad
 \widetilde Z(v)=e^{-\mathcal E(v)}\widehat Z(v).
\]
Use the frozen LSC clauses (5a)–(5b):
\[
 |\widetilde Z(v)|\le e^{E_+^\sharp N^4},\quad
 \widetilde Z(0)=\widehat Z(0)\ge e^{-C_{\rm low}N^4},\quad
 0\le t:=E_+^\sharp+C_{\rm low}\le E_*.
 \tag{P8.8}
\]
The first two inequalities are used at each finite datum; the last, uniform inequality is used only in §5.4. Its scope and inherited hypotheses are LSC §1(b), §3, and the freeze record at lines 720–724. These include equality at zero source of the sourced and source-free one-step energies, the representation and vacuum-energy inputs, Balaban's real-background theorem, and the eight sourced upper-bound inputs retained in LSC §3. P8 proves none of them.

**(correction: inherited vacuum convention.)** The source's \(Z\) in all formulas below is read as \(\widehat Z\). This is the normalization repair already proved and frozen in LSC. We do not assert a uniform lower bound on the unnormalized bare mass. Since \(E_{\rm vac}\) is real and source-independent,
\[
 \frac{\widehat Z(v)}{\widehat Z(0)}
 =\frac{Z_{\rm bare}(v)}{Z_{\rm bare}(0)}
 =\langle e^{A(v,U)}\rangle,
 \qquad \partial_1\cdots\partial_n\log\widehat Z
 =\partial_1\cdots\partial_n\log Z_{\rm bare}.
 \tag{P8.9}
\]
The cancellation occurs before the chessboard root. A common change of vacuum constant shifts the two exponents oppositely; it preserves their sum. It does not establish either estimate by itself.

**H-TREE (Balaban's anchored sum).** Retain CMP 116, (1.26), in the precise form used at II:62045–62061. There are \(c_\kappa>0\) and \(C_{(1.26)}<\infty\), independent of scale, cube and volume, with
\[
 \kappa_{\rm adm}=(1-\delta)\kappa-c_\kappa,\qquad
 \sum_{X\in D_j:\,X\supset\square}e^{-\kappa_{\rm adm}d_j(X)}
 \le C_{(1.26)}.
 \tag{P8.10}
\]
This cited Balaban input is not re-proved in this port. The margin \(c_\kappa>0\) is part of the hypothesis, not inferred merely from convergence at the larger rate.

Let \(\lambda_*=(40M)^{-1}\), \(\|f\|_\sharp=\max(\|f\|_\infty,\operatorname{Lip}(f)/\lambda_*)\),
\[
 w_z=\sum_{i=1}^nz_if_i,\quad
 \rho(z)=r^{-1}\sum_i|z_i|\|f_i\|_\sharp,\quad
 \mathbb D_{\mathfrak r}=\{\rho<1/\mathfrak r\}.
\]
The sources are real Lipschitz functions, each in a radius-\(R\) ball, with pairwise support distance at least \(d>0\); \(n\ge2\). The source uses the word “polydisc” for this weighted \(\ell^1\) ball. Cauchy's formula below uses actual product polydiscs contained in it.

**H-DOM (two source readings).** For \(\mathfrak r=1\), retain (A), (B) and (P8.8) on the full weight class \(\mathcal W_{K'}\), including weights with \(\sup|v|<r\) and \(\operatorname{Lip}v<r\lambda_*\). This is the class reading. For \(\mathfrak r=2\), retain them for every finite list of real Lipschitz functions on its ball \(\sum_l|\zeta_l|\|h_l\|_\sharp<r\), with the same constants and the same production formulas. This literal reading alone suffices below. The account separates these readings at II:60744–60762 and II:61762–61872. In either reading, ordinary transported lists have the full radius; only the periodised list can lose a factor two.

### 3.2 Cells and copies

Definitions are `6.2:def-cell-reflections`, II:60823–61117. Choose a power \(\ell\) of \(L\) dividing \(N/2\). Put \(n_c=N/\ell\), an even integer, and
\[
 c_k=\ell k+[0,\ell]^4,\quad k\in(\mathbb Z/n_c\mathbb Z)^4,\qquad
 J=|\mathcal C|=n_c^4=N^4/\ell^4.
\]
The algebra \(\mathfrak A_c\) consists of bounded measurable functions of bonds wholly in \(c^\circ\). Crossing bonds belong to no cell algebra. Faces are link planes because \(\ell/\varepsilon\) is integral.

Let \(\theta_{\mu,a}\) reflect \(x_\mu\) to \(2a\ell-x_\mu\), and let \(\mathfrak G_\ell\) be the group they generate. Its action on the \(\mu\)-th cell index is \(k\mapsto2a-1-k\). The composition of two such maps is translation by an even number of cells. In one direction the elements are the \(n_c/2\) translations by \(2a\ell\), and the \(n_c/2\) reflections \(x\mapsto2a\ell-x\). A reference cell maps exactly once to each even or odd cell, respectively. In four directions the actions commute. Thus \(\mathfrak G_\ell\) acts simply transitively on cells, with \(J\) elements.

Write \(\epsilon(g)\in\{+1,-1\}\) for the product of the four reflection signs. It is a homomorphism. It equals \((-1)^{\sum_\mu(k'_\mu-k_\mu)}\) when \(g c_k=c_{k'}\). A single face reflection pairs the two parity classes, so both have \(J/2\) elements. This proves the group assertions used below, including for \(n_c=2\).

For a lattice isometry \(g\), set \(T_gF(U)=F(U\circ g)\), where orientation-reversed bonds are inverted. Direct substitution of a bond gives \(T_gT_h=T_{gh}\). It follows that \(T_g\) preserves products, sup norms and Haar-Wilson expectations, commutes with conjugation, and maps \(\mathfrak A_c\) to \(\mathfrak A_{gc}\). Define
\[
 \Theta_\theta F=\overline{T_\theta F},\qquad
 F^{[c']}=(T_{g_{c\to c'}}F)^{(\epsilon(g_{c\to c'}))},
 \quad \xi^{(+)}=\xi,\quad \xi^{(-)}=\bar\xi.
\]
The composition and parity laws give
\[
 \Theta_\theta(F^{[c']})=F^{[\theta c']},\quad
 (F^{[c']})^{[c'']}=F^{[c'']},\quad
 (FG)^{[c']}=F^{[c']}G^{[c']},\quad
 (\lambda F)^{[c']}=\lambda^{(\epsilon(g_{c\to c'}))}F^{[c']}.
 \tag{P8.11}
\]
For example, the first identity applies one more conjugation and replaces the transporting element by \(\theta g\); its parity changes sign. The second uses \(g_{c'\to c''}g_{c\to c'}=g_{c\to c''}\), which follows from simple transitivity. These checks also prove that copying is independent of the sequence of reflections.

### 3.3 Chessboard value and estimate

**`6.2:lem-chessboard-value`, II:61119–61203. Source status: proved.** For \(F\in\mathfrak A_c\),
\[
 \mathsf c(F)=\left\langle\prod_{c'}F^{[c']}\right\rangle\ge0,\qquad
 \|F\|_{\rm ch}=\mathsf c(F)^{1/J}.
\]
The norm is unchanged by copying or complex conjugation, is absolutely homogeneous, and has \(\|1\|_{\rm ch}=1\).

To prove positivity, split the cells at any pair of opposite faces. Their interiors lie in the two open halves. The product \(G\) on one half is bounded and reads only that half. By (P8.11), the product on the other half is \(\Theta G\). Thus \(\mathsf c(F)=\langle\Theta G\,G\rangle\ge0\) by B5. Copying again gives the same product, proving copy invariance. Conjugating conjugates its expectation, which is real. Multiplying \(F\) by \(\lambda\) multiplies its product by \(\lambda^{J/2}\bar\lambda^{J/2}=|\lambda|^J\). The constant assertion uses \(\langle1\rangle=1\).

**`6.2:lem-chessboard-estimate`, II:61205–61415. Source status: proved.** For every family \(F_c\in\mathfrak A_c\),
\[
 \left|\left\langle\prod_cF_c\right\rangle\right|
 \le\prod_c\|F_c\|_{\rm ch}.
 \tag{P8.12}
\]
In particular, \(|\langle F\rangle|\le\|F\|_{\rm ch}\).

Here is the complete finite spreading proof. For an array \(Y\), write \(a(Y)=\langle\prod_cY_c\rangle\). Let \(Y^{\theta,+}\) retain the plus half and reflect it into the minus half; define \(Y^{\theta,-}\) conversely. The half products \(G_\pm\) satisfy
\[
 a(Y)=(\Theta G_-,G_+)_\theta,\qquad
 |a(Y)|^2\le a(Y^{\theta,+})a(Y^{\theta,-}),
 \tag{P8.13}
\]
where both factors on the right are nonnegative. This is precisely (P8.7); multiplicativity of \(\Theta\) identifies the two diagonal terms.

Starting from any chosen cell carrying \(F\), spread its copies in direction 1, then 2, then 3, then 4. In one direction, suppose a cyclic interval of \(s\) parallel blocks carries copies, starting at index \(b\). If \(s\le n_c/2\), retain the half starting at \(b\) and reflect at its boundary. The interval and its reflected interval are disjoint and adjacent, giving \(2s\) blocks. If \(n_c/2<s<n_c\), retain the half of length \(n_c/2\) inside that interval and reflect it; the whole cycle is filled. Each step increases \(s\). After finitely many steps that coordinate is filled. Reflections in the next coordinate preserve the copies in all already filled coordinates. After four coordinates the array is \((F^{[c]})_c\). This works for every even \(n_c\), not only powers of two.

If \(\|F_{c_0}\|_{\rm ch}=0\), run this sequence from \(F_{c_0}\). Put \(B=\max(1,\max_c\|F_c\|_\infty)^J\). All followed and unchosen branches have \(|a|\le B\), since transports and conjugation preserve sup norms. Iterating (P8.13) through \(T\) steps gives
\[
 |a(Y^0)|^{2^T}\le B^{2^T-1}a(Y^T)
 =B^{2^T-1}\mathsf c(F_{c_0})=0.
\]
This proves (P8.12) when a norm vanishes.

Otherwise keep labels on every copy of every original \(F_c\). There are only finitely many labelled fillings. For each filling set
\[
 R(Y)=\frac{|a(Y)|}{\prod_c\|Y_c\|_{\rm ch}}.
\]
The denominator is positive. Its two reflected versions multiply to its square, so (P8.13) gives
\(R(Y)^2\le R(Y^{\theta,+})R(Y^{\theta,-})\).
A constant copied filling has \(R=1\); hence the finite maximum \(R_{\max}\) is positive. If \(Y\) maximizes \(R\), both reflected fillings also maximize it, since neither exceeds \(R_{\max}\). Spread any label in a maximizing filling as above. Every step is still a maximizer. The final copied filling has \(R=1\), so \(R_{\max}=1\). The original filling satisfies (P8.12). Setting all but one factor to 1 gives the last assertion. The account credits Fröhlich, Israel, Lieb and Simon for the chessboard method; the finite proof is included here.

### 3.4 Support placement

**`6.2:lem-support-placement`, II:61417–61505. Source status: proved.** If \(\ell\ge8n(R+1)\), there is \(a\in\varepsilon\mathbb Z^4\) such that each \(B_i+a\) is in an open cell, at distance at least \(R+2\) from every face plane. With \(\tau_af=f(\cdot-a)\), for every complex \(z\),
\[
 Z\left(\sum_i z_i\tau_af_i\right)=Z\left(\sum_i z_if_i\right),\qquad
 S_n^T(\tau_a\vec f)=S_n^T(\vec f).
 \tag{P8.14}
\]

For each coordinate, a translation modulo \(\ell\) fails for the \(i\)-th ball only in an open arc of length \(4R+4\): its centre comes within \(2R+2\) of a face. The union of \(n\) such arcs leaves length at least \(4n(R+1)\). Its complement has at most \(n\) closed components, unless it is the whole circle, which is easier. One component has length at least \(4(R+1)>\varepsilon\). Because \(\ell/\varepsilon\) is integral, that component contains a grid point modulo \(\ell\). Choose one in each coordinate. Each centre is then at distance at least \(2R+2\) from faces, and its entire radius-\(R\) ball has the required margin.

For the identity, relabel plaquettes by \(p\mapsto p+a\). Their barycentres translate by \(a\); their action factors are those of the translated configuration. The Wilson density and Haar measure are invariant under this lattice translation. The source-independent vacuum factor stays fixed. This gives the equality of entire partition functions. Their local logarithms at zero have equal mixed derivatives, proving (P8.14).

From now on make this placement. Set \(I_c=\{i:B_i\subset c^\circ\}\). The nonempty \(I_c\) partition \(\{1,\ldots,n\}\), and their number \(q\) satisfies \(q\le n\).

### 3.5 Periodised weights and the factor-two domain

**`6.2:lem-periodised-weight`, II:61517–61744; domain explanation II:61746–61872. Source status: proved, conditional on the admitted weight domains for its membership clause.** Put
\[
 w_{c,z}=\sum_{i\in I_c}z_if_i,\quad F_{c,z}=e^{A(w_{c,z},U)},\quad
 u_{c,g,z}=w_{c,z}\circ g^{-1},
\]
\[
 w^{\rm ch}_{c,z}=\sum_{g\in\mathfrak G_\ell}u_{c,g,z}^{(\epsilon(g))},\qquad
 h^\pm_{c,i}=\sum_{\epsilon(g)=\pm1}f_i\circ g^{-1}.
 \tag{P8.15}
\]
Its clauses are:

(a) \(F_{c,z}\in\mathfrak A_c\), bounded at finite cutoff; set it to 1 on empty cells. Then \(\prod_cF_{c,z}=e^{A(w_z,U)}\) and \(Z(w_z)/Z(0)=\langle\prod_cF_{c,z}\rangle\).

(b) \(F_{c,z}^{[gc]}=e^{A(u_{c,g,z}^{(\epsilon(g))},U)}\). The copies have disjoint supports between distinct cells, and
\[
 w^{\rm ch}_{c,z}=\sum_{i\in I_c}(z_ih^+_{c,i}+\bar z_i h^-_{c,i}),\quad
 \|h^\pm_{c,i}\|_\sharp=\|f_i\|_\sharp,\quad
 \|F_{c,z}\|_{\rm ch}^{J}=\frac{Z(w^{\rm ch}_{c,z})}{Z(0)}\in[0,\infty).
 \tag{P8.16}
\]
(c) For \(z\in\mathbb D_1\), \(w^{\rm ch}_{c,z}\in\mathcal W_{K'}\) in the class reading. For \(z\in\mathbb D_2\), \(((z_i),(\bar z_i))\) is in the full source ball of the real list \((h^+_{c,i},h^-_{c,i})\). Each \(u_{c,g,z}\) is in the full source ball of its transported list for \(z\in\mathbb D_1\).

For (a), a plaquette whose source value is nonzero has barycentre in a placed ball. Every point of it is within \(2\varepsilon\) of that barycentre. Since \(R+2>2\varepsilon\), all its bonds lie in the open cell. Also
\(|A(w_{c,z},U)|\le2\|w_{c,z}\|_\infty\#\operatorname{plaq}(\mathbb T)\),
so its exponential is bounded. Linearity of \(A\) proves the product identity; (P8.9) proves the quotient identity.

For (b), relabeling plaquettes proves
\(T_ge^{A(v,U)}=e^{A(v\circ g^{-1},U)}\).
The plaquette action is real, so conjugation replaces \(v\) by \(\bar v\). This proves the copy formula and (P8.15). Each transported source is confined to \((gc)^\circ\), hence different \(g\)'s give disjoint cell supports. Grouping by parity yields (P8.16)'s first identity. Its last identity follows by multiplying copies, then by the positivity proved in §3.3.

For the norms and (c), set \(\Lambda=\sum_{i\in I_c}|z_i|\operatorname{Lip}f_i\). On each cell the periodised weight is one transported copy of \(w_{c,z}\), possibly conjugated. Its Lipschitz constant is at most \(\Lambda\); it vanishes on all cell faces. **(filled: global gluing.)** Subdivide a shortest torus geodesic at its finitely many cell-face intersections. On each segment the endpoint difference is bounded by \(\Lambda\) times its length. Add these inequalities. If a segment is in a face, both values are zero; limits handle geodesics lying along grid intersections. This proves the global bound, without multiplying by the number of cells. Disjoint supports also give
\[
 \|w^{\rm ch}_{c,z}\|_\infty\le\sum_{i\in I_c}|z_i|\|f_i\|_\infty,\qquad
 \operatorname{Lip}w^{\rm ch}_{c,z}\le\Lambda.
\]
For \(\rho(z)<1\), these are \(<r\) and \(<r\lambda_*\), so H-DOM gives class membership. Apply the same gluing argument to \(h^\pm_{c,i}\) and to the extension of \(f_i|_c\) by zero. Restriction to one cell of the specified parity gives the reverse norm inequalities. Hence both the sup norms and Lipschitz constants equal those of \(f_i\), proving the norm assertion.

Finally
\[
 \sum_{i\in I_c}\left(|z_i|\|h^+_{c,i}\|_\sharp+
                      |\bar z_i|\|h^-_{c,i}\|_\sharp\right)
 =2\sum_{i\in I_c}|z_i|\|f_i\|_\sharp<r
\]
when \(\rho(z)<1/2\). For a single transported list there is no doubling. H-DOM and representation independence supply exactly the terms and estimates needed at these weights. We do not treat \(z\mapsto w^{\rm ch}_{c,z}\) as a holomorphic map: its odd copies involve \(\bar z\).

## 4. B7 geometric and analytic estimates

### 4.1 Diameter and locality across cell faces

**`6.2:lem-domain-diameter`, II:61874–62028. Source status: proved.** For \(X\in D_j\) and \(x_1,x_2\in X^+\),
\[
 |x_1-x_2|_{\mathbb T}\le s_j(d_j(X)+8)\le4s_j(d_j(X)+3).
 \tag{P8.17}
\]
Its four consequences are:

(a) If two weights are nonzero at barycentres of plaquettes meeting \(X^+\), and their nonzero barycentre sets are at distance at least \(D>0\), then
\[
 d_j(X)\ge\frac{D-4\varepsilon}{4s_j}-3
          \ge\frac{DL^{K'-j}}{4M}-4.
 \tag{P8.18}
\]
(b) If \(X^+\) meets a face and a source confined at distance at least \(R+2\) from all faces, then it contains points at distance at least \(R+2-2\varepsilon\ge R\), and
\[
 d_j(X)\ge\frac{RL^{K'-j}}{4M}-3.
 \tag{P8.19}
\]
(c) At each scale define
\[
 \mathcal X_{c',j}=\{X\in D_j:X^+\subset(c')^\circ\},\qquad
 \mathcal X_{\partial,j}=D_j\setminus\bigsqcup_{c'}\mathcal X_{c',j}.
\]
The union is disjoint, and every member of \(\mathcal X_{\partial,j}\) has \(X^+\) meeting a face.

(d) If \(v=\sum_{c'}v_{c'}\), with each \(v_{c'}\) supported in a subset of \(c'\) at distance at least \(R+2\) from all faces, then
\[
 X\in\mathcal X_{gc,j}\quad\Longrightarrow\quad e_j(X;v)=e_j(X;v_{gc}).
 \tag{P8.20}
\]
This last clause uses H-LOC.

For (P8.17), each \(x_i\) lies in a cube touching a cube of \(X\). Choose \(t_i\) where a shortest tree meets the latter cube. Two touching cubes of side \(s_j\) have union of diameter at most \(4s_j\) in four dimensions. The path in the tree between \(t_1,t_2\) has length at most \(s_jd_j(X)\). The triangle inequality gives \(8s_j+s_jd_j(X)\). If a minimizing tree is represented only by an infimum, take a tree within \(\eta>0\) of that length and then let \(\eta\downarrow0\). This is a **(filled)** endpoint of the same argument.

For (a), move each barycentre to a point of its plaquette in \(X^+\), at cost at most \(2\varepsilon\). Apply (P8.17). Since \(\varepsilon/s_j=1/(ML^j)\le1\), (P8.18) follows. For (b), move the one barycentre to \(X^+\) at cost \(2\varepsilon\); its distance from a face was at least \(R+2\). Apply (P8.17) again.

For (c), \(X^+\) is connected: \(X\) is wall-connected, and each added cube touches it. The connected components of the complement of all face planes are precisely the open cells. A connected set avoiding every face therefore lies in one open cell. This proves (c), without an alignment assumption between the scale cubes and the cell grid.

For (d), any barycentre of a plaquette meeting \(X^+\subset(gc)^\circ\) is within \(2\varepsilon\) of that cell. A source in another cell is separated from it by a face and a margin \(R+2\). Thus that other source vanishes at the barycentre, since \(R+2-2\varepsilon\ge R>0\). The two weights agree at every barycentre read by \(e_j\). H-LOC(L) proves (P8.20).

### 4.2 Anchors and the retained tree sum

**`6.2:lem-tree-sum`, II:62030–62125. Source status: proved as an implication from Balaban 116 (1.26).** At scale \(j\), at most
\[
 \mathfrak a(R,K'-j)=\left(\frac{2(R+2)L^{K'-j}}{M}+6\right)^4
 \tag{P8.21}
\]
cubes are adjacent to a cube meeting a given radius-\(R+2\) ball. If a plaquette meeting \(X^+\) has barycentre in a radius-\(R\) ball, then \(X\) contains one of these cubes. If a family \(\mathcal Y\subset D_j\) has such anchors and \(d_j(X)\ge D\ge0\) for every member, then
\[
 \sum_{X\in\mathcal Y}C_e e^{-(1-\delta)\kappa d_j(X)}
 \le C_e C_{(1.26)}\mathfrak a(R,K'-j)e^{-c_\kappa D}.
 \tag{P8.22}
\]

Lift the ball centre to \(\mathbb R^4\). A cube meeting that ball lies in the coordinate box of radius \(R+2+s_j\). An adjacent cube lies in the box of radius \(\eta=R+2+2s_j\). In one coordinate, a grid interval \([ks_j,(k+1)s_j]\) meeting \([t-\eta,t+\eta]\) has
\((t-\eta)/s_j-1\le k\le(t+\eta)/s_j\).
There are at most \(2\eta/s_j+2\) choices. Multiply the four counts to obtain (P8.21). Periodic identifications can only reduce this upper bound: choose one lift for each torus cube, and distinct torus cubes have distinct chosen lifts. A plaquette's diameter is at most \(2\varepsilon\le2\); hence the cube of \(X^+\) it meets intersects the enlarged ball. That cube touches a cube of \(X\), proving the anchor assertion.

For (P8.22), split the exponential as
\[
 e^{-(1-\delta)\kappa d_j(X)}
 \le e^{-c_\kappa D}e^{-\kappa_{\rm adm}d_j(X)}.
\]
Sum over all possible anchors, then over all domains containing that anchor. Overcounting increases the nonnegative sum. H-TREE bounds each anchored sum by \(C_{(1.26)}\), proving (P8.22).

### 4.3 Ultraviolet estimate, including convergence of its series

**`6.2:lem-ultraviolet-bound`, II:62127–62291. Source status: proved, conditional on H-LOC and H-TREE.** For real Lipschitz \(h_1,\ldots,h_n\), \(n\ge2\), in radius-\(R\) balls with pairwise support distance at least \(d>0\), and arbitrary subfamilies \(\mathcal Y_j\subset D_j\), put
\[
 \Phi(\zeta)=\sum_{j=0}^{K'}\sum_{X\in\mathcal Y_j}
 e_j\left(X;\sum_{l=1}^n\zeta_lh_l\right),\qquad
 \mathbb D_h=\left\{\sum_l|\zeta_l|\|h_l\|_\sharp<r\right\}.
\]
Then \(\Phi\) is holomorphic on \(\mathbb D_h\), \(\Phi(0)=0\), and
\[
 |\partial_1\cdots\partial_n\Phi(0)|
 \le C_{\rm UV}(d;R)(n/r)^n\prod_l\|h_l\|_\sharp,
 \tag{P8.23}
\]
\[
 C_{\rm UV}(d;R)=C_eC_{(1.26)}\sum_{i\ge0}
 \mathfrak a(R,i)e^{-c_\kappa[dL^i/(4M)-4]_+}<\infty.
 \tag{P8.24}
\]
This constant is independent of cutoff, bare coupling, torus size and support positions, and is non-increasing in \(d\).

Finite sums and H-LOC(A) give holomorphy, and (L) gives the value at zero. If a local term does not read any nonzero barycentre of one source, it is independent of that source variable; its full mixed derivative is zero. A contributing domain therefore reads every source. In particular it reads sources 1 and 2, so (P8.18) gives
\[
 d_j(X)\ge\Delta_j=[dL^{K'-j}/(4M)-4]_+.
\]
It also has an anchor near the ball of source 1. If a source is zero the whole derivative vanishes, so suppose all norms are positive.

For \(0<\eta<1\), use Cauchy's formula on the product circles
\(|\zeta_l|=(1-\eta)r/(n\|h_l\|_\sharp)\).
Their closed polydisc is inside \(\mathbb D_h\). H-LOC(B) and the formula give
\[
 \left|\partial_1\cdots\partial_n e_j\left(X;\sum_l\zeta_lh_l\right)\bigg|_0\right|
 \le C_e e^{-(1-\delta)\kappa d_j(X)}
      \left(\frac{n}{(1-\eta)r}\right)^n\prod_l\|h_l\|_\sharp.
\]
Let \(\eta\downarrow0\), and sum (P8.22) with threshold \(\Delta_j\). Finally substitute \(i=K'-j\); the finite sum is bounded by the full nonnegative series (P8.24). This proves (P8.23).

**(filled: a hand-checkable tail.)** Set \(A_R=(2(R+2)/M+6)^4\). Since \(L^i\ge1\), \(\mathfrak a(R,i)\le A_R L^{4i}\), and
\[
 \mathfrak a(R,i)e^{-c_\kappa[dL^i/(4M)-4]_+}
 \le A_Re^{4c_\kappa}L^{4i}e^{-\alpha L^i},\qquad
 \alpha=c_\kappa d/(4M)>0.
\]
The ratio of consecutive terms in the last majorant is
\(L^4e^{-\alpha(L-1)L^i}\).
Choose an integer \(i_0\) with
\(L^{i_0}\ge(4\log L+\log2)/(\alpha(L-1))\).
Such an integer exists because \(L>1\). Every later ratio is at most \(1/2\). The finite prefix and geometric tail prove convergence, with no computed value. The defining series contains only the stated fixed constants. Each summand decreases with \(d\), proving monotonicity.

### 4.4 Face estimate

**`6.2:lem-face-estimate`, II:62293–62396. Source status: proved, conditional on H-LOC and H-TREE.** Suppose \(v=\sum_{\iota\in\mathsf K}v_\iota\), a finite sum of weights supported at barycentres in radius-\(R\) ball copies, each at distance at least \(R+2\) from faces, and (B) holds at \(v\). Then
\[
 \sum_{j=0}^{K'}\sum_{X\in\mathcal X_{\partial,j}}|e_j(X;v)|
 \le |\mathsf K| C_{\rm face}(R),
\]
\[
 C_{\rm face}(R)=C_eC_{(1.26)}\sum_{i\ge0}
 \mathfrak a(R,i)e^{-c_\kappa[RL^i/(4M)-3]_+}<\infty.
 \tag{P8.25}
\]
The constant is independent of cutoff, bare coupling, torus size, cell side and ball positions.

A nonzero term reads some nonzero source barycentre, by (L). At least one \(v_\iota\) is nonzero there. Group that domain with every such \(\iota\); this only increases the sum. Its enlargement also meets a face by §4.1(c). Thus (P8.19) gives threshold \([RL^{K'-j}/(4M)-3]_+\), and §4.2 gives an anchor near that ball. Apply (P8.22) once per \(\iota\), then sum in \(j\) and extend to all \(i=K'-j\ge0\). This proves (P8.25). For convergence, the previous tail proof applies with \(\alpha=c_\kappa R/(4M)>0\) and prefactor \(e^{3c_\kappa}\). This writes out why \(R>0\) is required.

### 4.5 Bounded holomorphic functions and their logarithms

**`6.2:lem-bounded-logarithm`, II:62398–62495. Source status: proved.** Let \(h\) be holomorphic on \(\mathbb D_{\mathfrak r}\), with \(h(0)=1\), \(|h|\le Q\), \(Q\ge1\). Then
\[
 |h(z)-1|\le(Q+1)\mathfrak r\rho(z).
 \tag{P8.26}
\]
On \(\rho\le[2\mathfrak r(Q+1)]^{-1}\), its principal logarithm is holomorphic on a containing open set and has modulus at most \(\log2\). Moreover
\[
 |\partial_1\cdots\partial_n\operatorname{Log}h(0)|
 \le(\log2)(2Q+2)^n\mathfrak r^n(n/r)^n\prod_i\|f_i\|_\sharp.
 \tag{P8.27}
\]

For \(\rho(z)>0\), the function
\(\psi(\lambda)=[h(\lambda z/(\mathfrak r\rho(z)))-1]/(Q+1)\)
is holomorphic on the unit disc, bounded by 1, and zero at zero. **(filled)** The quotient \(\psi(\lambda)/\lambda\) has a removable singularity at zero. On the circle of radius \(s<1\) its modulus is at most \(1/s\). The maximum principle gives this bound inside that circle; let \(s\uparrow1\). Thus \(|\psi(\lambda)|\le|\lambda|\). Evaluate at \(\lambda=\mathfrak r\rho(z)\) to get (P8.26).

**(filled: zero norms.)** If \(\|f_i\|_\sharp=0\), the domain imposes no bound on the \(i\)-th variable. For fixed other variables, Cauchy's estimate on an arbitrarily large circle bounds its derivative by \(Q/A\). Let \(A\to\infty\); \(h\) is independent of that variable. Remove all such coordinates. This also treats \(\rho(z)=0\) and gives zero for the full mixed derivative when needed.

On \((Q+1)\mathfrak r\rho<1\), (P8.26) puts \(h\) in the open right half-plane. The convergent series
\(\operatorname{Log}(1+u)=\sum_{k\ge1}(-1)^{k+1}u^k/k\)
defines its local branch, and on \(|u|\le1/2\) its absolute value is at most
\(\sum_{k\ge1}2^{-k}/k=\log2\).
For nonzero norms apply the iterated Cauchy integral formula on the circles
\[
 |z_i|=\frac{r}{2\mathfrak r(Q+1)n\|f_i\|_\sharp}.
\]
Their product lies in the smaller closed source ball and within the open logarithm domain. Each circle contributes the inverse of its radius. This gives (P8.27), with no assertion of zero-freeness on the original source ball.

### 4.6 Chessboard inequality with bulk and face terms

**`6.2:lem-chessboard-inequality`, II:62497–62643. Source status: proved as an implication from the preceding interfaces.** Define
\[
 \mathcal E^{\rm bulk}_{c'}(v)=\sum_j\sum_{X\in\mathcal X_{c',j}}e_j(X;v),\quad
 \mathcal E^{\rm bulk}=\sum_{c'}\mathcal E^{\rm bulk}_{c'},\quad
 \mathcal E^\partial(v)=\sum_j\sum_{X\in\mathcal X_{\partial,j}}e_j(X;v).
\]
Thus \(\mathcal E=\mathcal E^{\rm bulk}+\mathcal E^\partial\). For placed sources and \(z\in\mathbb D_{\mathfrak r}\),
\[
 \left|\frac{\widetilde Z(w_z)}{\widetilde Z(0)}\right|
 \le\exp\left\{\sum_{c\ {\rm occ}}J^{-1}\operatorname{Re}\mathcal E(w^{\rm ch}_{c,z})
 -\operatorname{Re}\mathcal E(w_z)+qt\ell^4\right\}.
 \tag{P8.28}
\]
The exponent is at most
\[
 \begin{split}
 &\sum_{c\ {\rm occ}}\left\{
 J^{-1}\sum_{g\in\mathfrak G_\ell}
 \operatorname{Re}\mathcal E^{\rm bulk}_{gc}(u_{c,g,z}^{(\epsilon(g))})
 -\operatorname{Re}\mathcal E^{\rm bulk}_c(w_{c,z})\right\}\\
 &\hspace{12mm}+(\sum_c|I_c|+n)C_{\rm face}(R)+qt\ell^4.
 \end{split}
 \tag{P8.29}
\]

Indeed (P8.16), (P8.8) and (P8.9) give
\[
 \|F_{c,z}\|_{\rm ch}^J
 =\frac{Z(w^{\rm ch}_{c,z})}{Z(0)}
 \le \exp\{\operatorname{Re}\mathcal E(w^{\rm ch}_{c,z})+tN^4\}.
\]
The ratio on the left is nonnegative, so it equals its modulus. Taking a nonnegative root is valid even when it is zero. Since \(N^4/J=\ell^4\), multiplication over occupied cells and (P8.12) give (P8.28) after multiplication by \(e^{-\operatorname{Re}\mathcal E(w_z)}\).

For each interior domain, (P8.20) discards every other cell's source. Hence
\[
 \mathcal E^{\rm bulk}_{gc}(w^{\rm ch}_{c,z})
 =\mathcal E^{\rm bulk}_{gc}(u_{c,g,z}^{(\epsilon(g))}),\qquad
 \mathcal E^{\rm bulk}_{c}(w_z)=\mathcal E^{\rm bulk}_{c}(w_{c,z}).
 \tag{P8.30}
\]
Empty cells give zero. There are \(n\) original ball pieces and \(J|I_c|\) pieces in the periodised weight for cell \(c\). Apply (P8.25):
\[
 |\mathcal E^\partial(w_z)|\le nC_{\rm face}(R),\qquad
 J^{-1}|\mathcal E^\partial(w^{\rm ch}_{c,z})|\le |I_c|C_{\rm face}(R).
 \tag{P8.31}
\]
Split the energies in (P8.28), use (P8.30), and bound the real parts of the face terms by their absolute values. This gives (P8.29). No covariance of local RG energies between different cells was assumed.

## 5. B7: the per-ball theorem

### 5.1 Statement

**`6.4:thm-per-ball-bound`, II:63964–64000. Source status: proved as an implication from B3, B5, B6 and Balaban 116 (1.26).** Its proof of (i) is II:64004–64068. The remaining proof is `6.4:prf-recentred-quotient`, II:64070–64283. The row's shorter range is therefore not the end of the proof.

Here is the theorem with the source's quantifiers and constants. Let \(n\ge2\), \(R,d>0\), and let \(\ell=\ell(n,R)\) be the least power of \(L\) with \(\ell\ge8n(R+1)\). Let
\[
 m\ge\max\{m_{\mathbb T}(g_-(g)),\log_L\ell\},\qquad
 K'\text{ arbitrary},\qquad g\le\gamma_J(L,\mathfrak p,r),
\]
where \(r\) is fixed first. Retain the standing correlation-theorem data of Chapter 6. Let \(f_1,\ldots,f_n\) be its radius-\(R\) ball sources with separation \(d\), placed as in §3.4. Use the bulk and face energies of §4.6, and define, for \(z\in\mathbb D_{\mathfrak r}\),
\[
 \mathcal E''(z)=\sum_{c\ {\rm occupied}}J^{-1}
 \sum_{g\in\mathfrak G_\ell}
 \left[\mathcal E^{\rm bulk}_{gc}
       (u_{c,g,z}^{(\epsilon(g))})\right]^{(\epsilon(g))}
 +\mathcal E^\partial(w_z),\qquad
 h''(z)=e^{-\mathcal E''(z)}\frac{Z(w_z)}{Z(0)}.
 \tag{P8.32}
\]
Then (i) \(\mathcal E''\) is holomorphic on \(\mathbb D_{\mathfrak r}\), vanishes at zero, and obeys the first bound below; (ii) \(h''\) is holomorphic there, \(h''(0)=1\), and obeys the second bound; (iii) the third bound follows:
\[
 \begin{gathered}
 |\partial_1\cdots\partial_n\mathcal E''(0)|
 \le2C_{\rm UV}(d;R)(n/r)^n\prod_i\|f_i\|_\sharp,\\
 |h''(z)|\le Q_\infty^n\quad(z\in\mathbb D_{\mathfrak r}),\\
 |S_n^T(\vec f)|\le C_n^\infty(d;R)\prod_i\|f_i\|_\sharp,\\
 Q_\infty=\exp[(E_+^\sharp+C_{\rm low})\ell^4+2C_{\rm face}(R)],\\
 C_n^\infty(d;R)=
 \left[2C_{\rm UV}(d;R)+(\log2)\mathfrak r^n(2Q_\infty^n+2)^n\right](n/r)^n.
 \end{gathered}
 \tag{P8.33}
\]
The source concludes that the constant is independent of \(K,g_0,m,N\) and support positions, and is non-increasing in \(d\). In this port that uniformity is supplied by frozen LSC, in the convention (P8.8)–(P8.9). Its admission conditions remain attached, including \(0<g\le\min\{\gamma_H,\gamma_J,\gamma_D\}\) and the level identifications in §5.4. Before using LSC, (P8.33) is proved with the numerical parameter \(t=E_+^\sharp+C_{\rm low}\) left visible. It does not by itself assert that \(t\) is uniform on other data.

### 5.2 Holomorphy and the mixed derivative

Every sum in (P8.32) is finite at fixed cutoff. For even \(g\), the bulk term is a holomorphic function of the complex-linear source \(\sum_{i\in I_c}z_i(f_i\circ g^{-1})\), on its full ball. For odd \(g\), write it as
\[
 \overline{\Phi_g(\bar z)},\qquad
 \Phi_g(\zeta)=\mathcal E^{\rm bulk}_{gc}
       \left(\sum_{i\in I_c}\zeta_i(f_i\circ g^{-1})\right).
\]
This is holomorphic too. **(filled)** Around any \(z_0\), expand \(\Phi_g\) in a convergent power series around \(\bar z_0\). Conjugating its values at \(\bar z\) conjugates its coefficients and produces powers of \(z-z_0\). Thus the argument is local and requires no unproved global Taylor-series claim. At zero it also gives
\[
 \partial^\alpha\overline{\Phi_g(\bar z)}\big|_0
 =\overline{\partial^\alpha\Phi_g(0)}.
 \tag{P8.34}
\]
The face energy is a holomorphic sum on the original source ball. By (L) every summand vanishes at zero. This proves holomorphy and \(\mathcal E''(0)=0\).

If at least two cells are occupied, each \(I_c\) is a proper subset of the source indices. Every bulk summand is independent of at least one variable, and its full mixed derivative vanishes. If only one cell is occupied, all sources occur in its transported list. Isometries preserve support radii, support distances and sharp norms. Apply (P8.23) with \(\mathcal Y_j=\mathcal X_{gc,j}\). It bounds each even term by
\(C_{\rm UV}(d;R)(n/r)^n\prod_i\|f_i\|_\sharp\);
(P8.34) gives the same bound for odd terms. The factor \(J^{-1}\) averages exactly \(J\) such terms. In either case apply (P8.23) once to \(\mathcal Y_j=\mathcal X_{\partial,j}\) for the face term. Their sum is the first line of (P8.33).

### 5.3 Bulk cancellation, normalized quotient, and cumulant

The finite Wilson integral \(Z(w_z)\) is entire. On any compact set of \(z\)'s, its integrand and each derivative are bounded by a fixed exponential times a product of bounded plaquette sums. H0 justifies differentiation under the finite Haar integral. Also \(Z(0)>0\). Consequently \(h''\) is holomorphic on \(\mathbb D_{\mathfrak r}\), and its value at zero is 1.

Outer conjugation preserves the real part. By (P8.30) and the bijection \(g\mapsto gc\),
\[
 \operatorname{Re}\mathcal E''(z)=
 \sum_{c\ {\rm occupied}}J^{-1}\operatorname{Re}\mathcal E^{\rm bulk}
                          (w^{\rm ch}_{c,z})
 +\operatorname{Re}\mathcal E^\partial(w_z).
 \tag{P8.35}
\]
This equality compares the same local terms evaluated at the same weights. It needs no equality of local energies produced on different cells.

The per-cell inequality used in §4.6 is
\[
 \|F_{c,z}\|_{\rm ch}\le
 \exp\{J^{-1}\operatorname{Re}\mathcal E^{\rm bulk}(w^{\rm ch}_{c,z})
       +J^{-1}\operatorname{Re}\mathcal E^\partial(w^{\rm ch}_{c,z})+t\ell^4\}.
\]
Use (P8.12), multiply over occupied cells, and multiply by
\(e^{-\operatorname{Re}\mathcal E''(z)}\). Equation (P8.35) cancels every bulk term. What remains is
\[
 |h''(z)|\le\exp\left\{
 \sum_{c\ {\rm occupied}}J^{-1}\operatorname{Re}\mathcal E^\partial(w^{\rm ch}_{c,z})
 -\operatorname{Re}\mathcal E^\partial(w_z)+qt\ell^4\right\}.
\]
Use (P8.31), \(\sum_c|I_c|=n\), \(q\le n\), and \(t\ge0\) from (P8.8). The exponent is at most
\(2nC_{\rm face}(R)+nt\ell^4\), proving \(|h''|\le Q_\infty^n\).

Now \(Q_\infty^n\ge1\). Apply (P8.27) with \(Q=Q_\infty^n\). In the resulting neighbourhood of zero, define the logarithm of \(Z\) by
\[
 \log Z(w_z)=\log Z(0)+\mathcal E''(z)+\operatorname{Log}h''(z).
\]
Its exponential equals \(Z\), and it has the prescribed value \(\log Z(0)\) at zero. Thus it is the branch used for the cumulant. Differentiating once in each source variable gives
\[
 S_n^T(\vec f)=\partial_1\cdots\partial_n\mathcal E''(0)
              +\partial_1\cdots\partial_n\operatorname{Log}h''(0).
\]
The two bounds already proved give the last line of (P8.33). If any source is zero, both sides' mixed derivatives vanish, and the inequality follows without any radius division. Since only \(C_{\rm UV}(d;R)\) depends on \(d\), its monotonicity proves the theorem's monotonicity assertion.

This also proves the small zero-free source region in `6.4:rem-complex-sources`, II:64285–64344:
\[
 \rho(z)\le\frac{1}{2\mathfrak r(Q_\infty^n+1)}
 \quad\Longrightarrow\quad |h''(z)-1|\le\tfrac12.
\]
It follows from the bound and normalization, not from reflection positivity alone. Complex sources were used throughout; replacing them by real sources was never a step.

### 5.4 LSC closes the constant dependence in the stated convention

This is the account's final constant step, II:64268–64282, with the frozen replacement for its unwritten B6. No part of §5.2–§5.3 used a per-ball uniformity conclusion to prove LSC. We use only LSC §1(a),(b),(d),(e) as supplied; its §1(c) is a consumer of the same algebra just proved.

Let \(m_1\) be the physical torus exponent, and \(m_J=m^J_{\mathbb T}(g)\) the fixed withheld exponent of LSC. Its bounded offset is \(a=K_J-K\in\mathcal A\), and
\[
 b=m_J-a\in\mathcal B(g)\subset\{0,\ldots,m_J\},\quad
 K'=K_J-m_J=K-b,\quad N_T=2L^{m_1-a},\quad N=2L^{m_1+b}.
\]
In Case A, \(K_J\ge m_J\), LSC supplies admissible data and \(t\le E_*\), uniformly in the physical torus exponent, cutoff, bare coupling and offset. Every coefficient in (P8.33) is nonnegative, and that formula is non-decreasing in \(t\). Therefore replacing \(t\) by \(E_*\) gives a constant with the required uniformity.

For clarity, port also the account's change of units, `6.4:rem-unit-conversion`, II:64494–64568. If last-lattice and reference units agree, nothing changes. Otherwise put \(f^{(b)}(y)=f(L^{-b}y)\). Barycentre relabelling gives the identical observable, with no Jacobian or volume factor: it is a plaquette sum, not an integral of \(f\). Its support radius and separation become \(RL^b\), \(dL^b\), while
\[
 \|f^{(b)}\|_\infty=\|f\|_\infty,\qquad
 \operatorname{Lip}f^{(b)}=L^{-b}\operatorname{Lip}f,\qquad
 \|f^{(b)}\|_\sharp\le\|f\|_\sharp.
\]
Consequently the reference-unit constant is
\[
 C_n^*(d;R)=\max_{b\in\mathcal B(g)}
 \left[2C_{\rm UV}(dL^b;RL^b)
 +(\log2)\mathfrak r^n
 \left(2e^{n[E_*\ell(n,RL^b)^4+2C_{\rm face}(RL^b)]}+2\right)^n\right](n/r)^n.
 \tag{P8.36}
\]
This is a finite maximum, hence finite. It is independent of cutoff, bare coupling, physical volume and support positions, and non-increasing in \(d\).

The cell-side hypothesis must also be transported. Since
\[
 8n(RL^b+1)\le L^b8n(R+1)\le L^b\ell(n,R),
\]
and the last expression is a power of \(L\), minimality gives
\(\ell(n,RL^b)\le L^b\ell(n,R)\le L^{m_J}\ell(n,R)\).
Thus the sufficient common floor \(L^{m_1}\ge L^{m_J}\ell(n,R)\), together with the correlation-theorem floor, admits every value of \(b\). No assertion is made using an unscaled cell-size condition when the units differ.

In Case B, \(K_J<m_J\), retain the frozen local plaquette bound LSC §1(d), equation (8):
\[
 |S_n^T(\vec f)|\le C_n^B(R)\prod_i\|f_i\|_\infty,\quad
 C_n^B(R)=c_n[12(2R+3)^4]^nL^{4nm_J},\quad
 c_n=\sum_{\pi\in\operatorname{Part}(n)}(|\pi|-1)!.
\]
It is a local count, independent of the physical volume. The maximum of this constant and (P8.36) covers both cases under the common floor. LSC §6.4 separately covers the remaining tori under the original floor of clause (iii-b); we retain that frozen implication with its hypotheses. Its proof is not replaced by a bare normalization assertion here.

Thus B7 and all its support, chessboard, periodisation, ultraviolet, face, and logarithm steps are ported, as conditional implications. H-TREE and the sourced construction are still inputs. The source's alternative `6.2:prop-cell-covariance` is not needed: its extra covariance hypothesis is avoided by the account's own counterterm (P8.32).

## 6. B8: fixed-torus subsequences and closed positivity

### 6.1 Exact subsequence statement and its inputs

**`5.12:prop-subsequential-limits`, II:59926–60087. Source status: proved as an implication from its four displayed assumptions.** Fix \((g,m,N_T)\), where \(N_T\) is a positive integer and
\(N_{\rm side}=N_TL^m\) is the site count per side at level \(K'=K-m\). Here \(m\) counts withheld steps; it is not the physical torus exponent used in §5.4. The physical torus has side one. Its bare spacing is \(L^{-K}N_T^{-1}\). For \(C^1\) tests on that torus put
\[
 \mathcal O(f)=\sum_p f(x(p))[1-\operatorname{Re}\operatorname{tr}U(\partial p)],\qquad
 S^T_{n;K,m}(\vec f)=\partial_{z_1}\cdots\partial_{z_n}\log Z(\textstyle\sum_i z_if_i)\big|_0
 =\langle\mathcal O(f_1);\ldots;\mathcal O(f_n)\rangle_K^{\rm conn}.
 \tag{P8.37}
\]
At fixed \(N_T\), (P8.37) is independent of \(m\). Let \(g_0^{(i)}\) be a sequence of bare couplings, with first-passage levels \(K_i=K(g_0^{(i)},g)\) and \(x_0^{(i)}=(g_0^{(i)})^{-2}\). Retain precisely these assumptions:

1. **H-TORUS-BOUND:** the correlation theorem's fixed-\((g,m,N_T)\) torus bound, uniform in \(K\) on pairwise separated supports.
2. **H-COMPACT:** for \(n\ge2\), and closed pairwise separated sets \(B_1,\ldots,B_n\), a sequence of multilinear functionals on \(C^1_{B_1}\times\cdots\times C^1_{B_n}\) which is equicontinuous on sharp-norm bounded sets and converges on a countable sharp-norm dense subset converges everywhere to a multilinear limit. If defined on all separated tuples, with these properties on every such product, its limits are restrictions of one finite-order distribution on
\[
 \Omega_n=\{(x_1,\ldots,x_n)\in(\mathbb T^4)^n:x_i\ne x_j\ (i\ne j)\}.
 \tag{P8.38}
\]
3. **H-FIRST-PASSAGE:** \(K_i\to\infty\).
4. **H-TORUS-FLOOR:** the compatibility condition of `5.1:def-torus-floor`, II:679–748, with \(C_{\mathbb T}=L^{11}M\):
\[
 L^m\ge N_{\mathbb T}(g,m),\quad
 N_{\mathbb T}(g,m)=L^{11}M\sup_{u\in\mathbb Z_{\ge0}}L^{-u}
 R_J(g^{-2}+b_++4c_2+3\lambda(m+u)),
 \tag{P8.39}
\]
where \(R_J(x)\) is the least nonnegative integer power of \(L\) at least \((\log x)^{r_{\rm pr}}\). The flow constants and first-passage convention are those of B3 and P1.

Then a single subsequence \((K_{i_l})\) gives convergence of (P8.37) for every \(n\ge2\) and every tuple with pairwise disjoint supports. The limit \(S^T_{n;m}\), which may depend on that subsequence, is multilinear on its admissible support domains and is the restriction of a finite-order distribution on \(\Omega_n\). It is symmetric and covariant under lattice symmetries common to the entire subsequence. There is no assertion for \(n=1\) or coincidences.

**Standing and non-circular use.** H-TORUS-BOUND is B3(iv)'s finite-cutoff estimate, II:2940–2951, carried by P6 (ported, not yet checked), with the vacuum convention supplied by frozen LSC. We do not use B3(iv)'s subsequent claim of limit existence to prove B8. H-COMPACT is an explicit assumption in the source, II:59953–59964. The elementary dense-set convergence part is filled below. Its distributional extension clause, denoted **H-KERNEL**, remains a named assumption, not an application of an unnamed kernel theorem. H-FIRST-PASSAGE and H-TORUS-FLOOR are retained at their displayed scope; LSC and P1 give their specified applications, with their own hypotheses.

The norm in this side-one convention is
\[
 \|f\|_{\sharp,N_{\rm side}}=
 \max\{\|f\|_\infty,40M\operatorname{Lip}f/N_{\rm side}\},
 \tag{P8.40}
\]
as at II:737–748. We abbreviate it by \(\|f\|_\sharp\) within §6. It is fixed while \(K\) varies. It is not a norm whose derivative coefficient shrinks with the bare spacing.

### 6.2 Proof of the subsequence proposition

At fixed \(K,N_T\), the bare lattice has
\(N_{\rm side}L^{K'}=N_TL^mL^{K-m}=N_TL^K\) sites per side. The bare observable and normalized generating function therefore do not refer to the withheld exponent. A source-independent vacuum factor contributes only a constant to \(\log Z\). This proves (P8.37)'s independence assertion and its identification as a cumulant.

Discard the finite prefix with \(K_i<m\). For each remaining datum, H-TORUS-FLOOR admits H-TORUS-BOUND. Thus for tests separated by \(d>0\),
\[
 |S^T_{n;K_i,m}(\vec f)|\le C_n(d)\prod_j\|f_j\|_\sharp,
 \tag{P8.41}
\]
with \(C_n(d)\) independent of \(i\). The finite integral makes cumulants multilinear. **(filled: complexification.)** If the supplied bound is stated only for real tests, expand each complex test as \(\operatorname{Re}f+i\operatorname{Im}f\). Both parts retain its support and have sharp norm at most its norm. Summing the \(2^n\) multilinear terms gives (P8.41) with \(2^nC_n(d)\). No new cutoff dependence occurs. We absorb this fixed factor into \(C_n\) when complex tests are used.

Fix closed sets \(B_j\) at pairwise distance at least \(d\), and \(f_j,f'_j\in C^1_{B_j}\). Multilinearity gives
\[
 S_i(\vec f)-S_i(\vec f')
 =\sum_{j=1}^nS_i(f'_1,\ldots,f'_{j-1},f_j-f'_j,f_{j+1},\ldots,f_n).
\]
Every tuple on the right stays in the same separated support product. Therefore
\[
 |S_i(\vec f)-S_i(\vec f')|
 \le C_n(d)\sum_{j=1}^n\|f_j-f'_j\|_\sharp
                \prod_{r\ne j}\max(\|f_r\|_\sharp,\|f'_r\|_\sharp).
 \tag{P8.42}
\]
This proves equicontinuity on every norm-bounded subset.

Every separated compact support tuple lies in a product of finite unions of closed balls with rational centres and rational radii, whose closures are still separated. Here are the margins. Take \(d>0\) such that the original supports have mutual distance at least \(3d\). Around each point choose a rational-centred ball, with centre within \(d/4\) and radius strictly between \(d/4\) and \(d/2\), containing that point in its interior. It lies within distance \(3d/4<d\) of that point. Compactness gives finite subcovers. The resulting unions \(B_j\) have pairwise distance at least \(d\). There are countably many such support products, over all \(n\ge2\).

**(filled: separability in the supported spaces.)** Continuous functions on a compact coordinate torus are separable in the uniform norm: on a uniform rational grid, multilinearly interpolate rational complex values, consistently at periodic faces. Uniform continuity bounds the interpolation error by the oscillation within one grid cube plus the error in its vertex values. Let the mesh and these errors tend to zero. These interpolants form a countable dense set. Thus \(C(\mathbb T^4)^5\) is separable. The map
\(f\mapsto(f,\partial_1f,\ldots,\partial_4f)\)
embeds \(C^1\), with its usual norm, into this metric space. A subspace of a separable metric space is separable: take a countable base of balls and choose one subspace point from each ball meeting it. The chosen points are dense. Apply this to each \(C^1_{B_j}\) and then to finite products. The sharp norm (P8.40) is bounded by a fixed multiple of the \(C^1\) norm, so these spaces have countable sharp-norm dense subsets too. This argument does not require approximants to leak outside \(B_j\).

Enumerate the union of all these dense tuple sets, over all support products and all \(n\ge2\). It is countable. Each coordinate value is bounded by (P8.41). A bounded complex sequence has a convergent subsequence: enclose it in a square, keep a closed quarter-square containing infinitely many terms, repeat, and choose increasing indices in the nested squares. Their diameters tend to zero, so completeness gives a limit. Apply this selection successively to the countably many tuple coordinates. At step \(r\), retain an infinite subsequence of step \(r-1\). Choose its diagonal indices increasingly. For any fixed coordinate the diagonal tail lies in its selected convergent subsequence. Thus all dense tuple values converge on one subsequence.

**(filled: extension without another extraction.)** For a fixed arbitrary tuple in one support product and \(\eta>0\), choose a dense tuple \(\vec h\) so close that the right side of (P8.42) is less than \(\eta/3\), uniformly in the cutoff. The approximants' norms can be bounded by one plus those of the original tuple. On the chosen subsequence, the values at \(\vec h\) differ by less than \(\eta/3\) for two sufficiently late indices. The triangle inequality through \(\vec h\) then bounds the original two values by \(\eta\). They are Cauchy and converge. The result is independent of the product or dense approximants, since it is the limit of the same original numerical sequence. This establishes the convergence part of H-COMPACT directly.

The same argument works on every separated support product, since every tuple now converges there. Multilinearity passes to the limit whenever the alternative supports in one slot remain separated from all other slots; enlarge that slot's support set to their finite union. Equation (P8.42) and (P8.41) pass with their constants by taking limits. Apply **H-KERNEL**, the remaining clause of assumption (2), to obtain one finite-order distribution on \(\Omega_n\). Its local support products cover \(\Omega_n\): choose small disjoint rational balls around any distinct coordinates. This use retains the source's distribution hypothesis explicitly; a diagonal sequence alone is not claimed to prove it.

Finally, the finite generating function is entire and nonzero near zero. Its local logarithm has commuting partial derivatives, so the cumulants are symmetric. For any common lattice isometry \(\iota\), the change of variables \(U\mapsto\iota_*U\) preserves Haar measure and Wilson action, and gives
\[
 \mathcal O(f)(\iota_*U)=\mathcal O(f\circ\iota)(U).
\]
Hence \(S_i(f_1\circ\iota,\ldots,f_n\circ\iota)=S_i(\vec f)\) at every cutoff in the subsequence. Passing to the limit proves the claimed covariance. It gives only the common symmetries asserted in this proposition; no continuum rotation group is inferred here.

### 6.3 Exact positivity statement

**`5.12:lem-limit-positivity`, II:60089–60178. Source status: proved, conditional on the lattice positivity hypothesis and the preceding subsequential limits.** Retain **H-TORUS-RP**: the finite Wilson expectations are invariant and reflection positive for \(\theta:x^0\mapsto-x^0\), with the half-algebra in the cited lattice lemma. On the even centred lattices of B5 this input is supplied by §2 after rescaling; for other lattice conventions the source's cited lattice-positivity hypothesis remains an input. It is not inferred from convergence.

Write \(S_n^K=S^T_{n;K,m}\) and \(S_n=S^T_{n;m}\) along the subsequence of §6.1. Let \(I\) be finite. Let the \(C^1\) tests \(f_i\), \(i\in I\), have pairwise disjoint supports in \(0<x^0<1/2\), and let \(c_\alpha\in\mathbb C\) for subsets \(\alpha\subset I\). Put
\[
 F_K=\sum_{\alpha\subset I}c_\alpha
 \prod_{i\in\alpha}\bigl(\mathcal O(f_i)-\langle\mathcal O(f_i)\rangle_K\bigr).
 \tag{P8.43}
\]
Then \(\langle\overline{\theta(F_K)}F_K\rangle_K\ge0\) for each admitted cutoff. It is a polynomial \(P_K(F)\) in \(S_n^K\), \(n\ge2\), evaluated only at pairwise disjoint supports. Its coefficients depend on \((c_\alpha,f_i)\), with no separately occurring centering constants. Along the same subsequence it converges to the polynomial \(P(F)\) formed with \(S_n\), and
\[
 P(F)=\lim_{l\to\infty}\langle\overline{\theta(F_{K_{i_l}})}F_{K_{i_l}}\rangle_{K_{i_l}}\ge0.
 \tag{P8.44}
\]
Nothing is asserted about one-point functions or coinciding insertions. The notation \(F_K\) makes explicit the cutoff dependence already present in the source's \(F\).

### 6.4 Proof, including the centering polynomial

**(filled: admission to the link half-algebra.)** On the even centred lattices, both time boundaries of the slab are link planes. A spatial plaquette has constant time equal to its barycentre time. A time-space plaquette has barycentre time \(a\) on the integer mesh, and its time coordinates range over \([a-\varepsilon/2,a+\varepsilon/2]\). If its barycentre is strictly between two boundary times on that mesh, it is at least one mesh step from each. The whole interval is therefore in the open slab. A crossing plaquette has barycentre exactly on a boundary, where every test in (P8.43) vanishes. Thus every plaquette with a nonzero source value reads only half-space bonds, even at the coarsest admitted spacing. This is also the argument printed at II:65290–65302 in `7.2:prop-torus-reflection`; it supplies the omitted detail at II:60121–60125. For any different geometry, the corresponding half-algebra admission is retained with H-TORUS-RP.

Each \(\mathcal O(f_i)\), its centering constant, and the finite polynomial \(F_K\) is bounded at a fixed cutoff. H-TORUS-RP applies and gives the finite nonnegative form. Plaquette relabelling and the reality of \(a_p\) give
\[
 \theta\mathcal O(f)=\mathcal O(\theta f),\quad
 \overline{\mathcal O(f)}=\mathcal O(\bar f),\quad
 \langle\mathcal O(\theta f)\rangle_K=\langle\mathcal O(f)\rangle_K.
\]
Consequently
\[
 \overline{\theta F_K}=
 \sum_\alpha\bar c_\alpha\prod_{i\in\alpha}
 \bigl(\mathcal O(\theta\bar f_i)-\langle\mathcal O(\theta\bar f_i)\rangle_K\bigr).
 \tag{P8.45}
\]
The centering is compatible with reflection even when the tests are complex.

**(filled: the finite moment–cumulant identity.)** For bounded random variables \(X_j\), \(j\in J\), let
\(M(t)=\langle\exp(\sum_jt_jX_j)\rangle\), and \(W(t)=\log M(t)\) near zero. The coefficient of the square-free monomial \(\prod_{j\in J}t_j\) in \(M\) is \(\langle\prod_jX_j\rangle\). The corresponding coefficient of \(W\) for a nonempty subset \(B\) is its joint cumulant \(\kappa(X_j:j\in B)\). In \(M=\sum_{k\ge0}W^k/k!\), a square-free coefficient is formed from ordered disjoint nonempty blocks partitioning \(J\). There are \(k!\) orders for every partition into \(k\) blocks. They cancel \(1/k!\). Therefore
\[
 \left\langle\prod_{j\in J}X_j\right\rangle
 =\sum_{\pi\in\operatorname{Part}(J)}\prod_{B\in\pi}\kappa(X_j:j\in B).
 \tag{P8.46}
\]
Subtracting deterministic constants subtracts only a linear polynomial from \(W\). For centred variables its singleton cumulants vanish and all cumulants of order at least two are unchanged. This proves, rather than assumes, the two centering rules used here.

For each \((\alpha,\beta)\), take a disjoint copy \(\alpha'=\{i':i\in\alpha\}\), and let
\(h_{i'}=\theta\bar f_i\), \(h_j=f_j\) for \(j\in\beta\). Expanding (P8.43) and (P8.45), then applying (P8.46), yields exactly the source's polynomial:
\[
 P_K(F)=\sum_{\alpha,\beta}\bar c_\alpha c_\beta
 \sum_{\pi\in\Pi_{\ge2}(\alpha'\sqcup\beta)}
 \prod_{B\in\pi}S_{|B|}^K((h_j)_{j\in B}).
 \tag{P8.47}
\]
Here \(\Pi_{\ge2}\) contains partitions with no singleton block. On the empty set it contains the empty partition, whose product is 1. On a singleton it is empty, whose sum is zero. These conventions include the constant terms of \(F_K\), as required.

Each test occurs at most once in each half because \(\alpha,\beta\) are subsets. The original tests in the positive half have disjoint supports; their reflected conjugates have disjoint supports in the negative half. The two families lie in disjoint open slabs. Since their supports are compact, every distance relevant to the finite tuple is positive. Thus each cumulant in (P8.47) lies in the domain of §6.1 and has its limit on the single chosen subsequence. Even if an index occurs in both \(\alpha\) and \(\beta\), it labels two different tests on opposite halves, not a coinciding insertion.

There are finitely many subsets, partitions and factors in (P8.47). Hence the limit passes through all products and sums. Its value is exactly the same polynomial with \(S_n\) in place of \(S_n^K\). Every finite-cutoff value is a nonnegative real number; their limit is nonnegative, proving (P8.44). No limit of \(\langle\mathcal O(f_i)\rangle_K\) was taken or needed. The result is positivity of this centered moment polynomial; it does not say that higher connected cumulants separately form positive kernels.

## Result

**What was ported.** B5, `6.1:lem-reflection-positivity`, and its reflection-form corollary are proved here on the account's character-kernel route. B7, `6.4:thm-per-ball-bound`, is ported through the end of its proof at II:64283. The port includes the cell/copy geometry, chessboard value and estimate, support placement, periodisation, enlarged-domain diameter, anchored sum, ultraviolet bound, face bound, bounded-logarithm lemma, and bulk/face chessboard inequality. It uses frozen LSC for the final uniform constants, in the vacuum-normalized convention. B8, `5.12:prop-subsequential-limits` and `5.12:lem-limit-positivity`, is ported in full as the source's conditional fixed-torus statements, including the exact centered positivity polynomial.

**Filled steps.** The additions marked in the text are: an explicit positive tensor-character expansion with absolute convergence; the null-vector case of reflection Cauchy–Schwarz; global Lipschitz gluing of copied sources; the infimum endpoint for a shortest tree; an explicit geometric tail for the ultraviolet and face series; the Schwarz-lemma argument and zero-norm coordinates in the logarithm bound; local power-series holomorphy after double conjugation; complexification, support-preserving separability and dense-set extension on one subsequence; plaquette admission to the open link half-algebra; and the square-free coefficient proof of the moment–cumulant and centering identities. None is computer-assisted.

**Corrections.** The strict comparison \(1>\varepsilon\) at II:60604 is not valid when \(K'=0\); §2.2 supplies the edge-label argument needed at equality. The substantial normalization correction is inherited from frozen LSC: the upper bound and floor use the same \(e^{-E_{\rm vac}}\) normalization, with cancellation before forming the quotient or taking its chessboard root. No uniform bare floor is claimed. The B7 proof extends beyond the chain row's displayed II:64068 endpoint; this port includes II:64070–64283 as well.

**Named hypotheses retained.** H0 names ordinary analysis and compact-group integration. H-LOC and H-DOM retain B3's local production formulas, locality, holomorphy, bounds and admitted source domains, at P6's ported-but-not-yet-checked standing. Their transitive source/weight inputs remain, including `5.6:prop-polydisc-holomorphy` (outstanding, II:46167) and the preparatory window-data statement (outstanding, II:2810–2812). H-STAB/LSC retains the frozen LSC implication and its flow, representation, real-background, vacuum-energy, source-free/sourced matching and sourced-majorant hypotheses. H-TREE is Balaban CMP 116 (1.26), retained as a cited input. B8 retains H-TORUS-BOUND, H-FIRST-PASSAGE, H-TORUS-FLOOR, and H-KERNEL, the distributional part of its displayed compactness assumption. H-TORUS-RP is proved by B5 for the even centred link-reflection geometry; any other geometry covered only by the original citation remains conditional on that input. The elementary dense-set convergence part of H-COMPACT is proved here.

**Stopping point.** This round stops after B8. B10 has not been ported: resume with `7.4:lem-torus-transport` (II:65661–65767), `7.4:lem-lattice-symmetries` (65844–65927), `7.4:lem-half-space` (65929–66046), `7.4:lem-translation-modulus` (66048–66144), and `7.4:lem-linearity` (66209–66332), then B11–B13 in the chain's order. Their later limit, invariance and reconstruction conclusions are not claimed by this round.

This is a port of Ethan Sussman and Levent Alpoge's proof route, with Claude and Codex credited as authors of their text and Balaban credited for its underlying construction. It is research text, not an audit, and grants no status. **This text is not yet checked by another model.** Text-format and source-location checks establish no mathematical conclusion. No ledger, frozen input, or other research file was edited.
