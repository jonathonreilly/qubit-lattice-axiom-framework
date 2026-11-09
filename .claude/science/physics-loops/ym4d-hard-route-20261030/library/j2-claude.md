lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-09T13:53Z

# J2: the rooted ordinary source package (queue row 359, `j2-claude`)

Provenance: Claude Opus 5.5 (max effort), Mac mini worker, 2026-11-09, on branch `claude/ym4d-hard-route` at `ab92cf371`. Research text, not an audit; it grants no status. Proved by Claude, not yet checked by the other model. No computer-assisted step: every step below is a written hand argument, and no run was made.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account (CA-I/II/III) and the outline (SA) at `31a47c543775`. The local-term properties, their two domain readings and the torus-bound proof used here are theirs. Tadeusz Balaban for the renormalization-group construction and the localization domains (CMP 109, §0; CMP 119; CMP 122). Codex wrote the frozen inputs LSC, P6, P8 and P10 used below.

Sources: CA-I/II/III and SA fetched once into a private scratch folder from `raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/`. CA-I sha256 begins `4cb5cb5e`, SA begins `d7f77d4d`; both equal the hashes recorded in `ro1-vs-ca.md`. Line numbers are TeX lines of those files. Balaban CMP 109 is read from the owner's copy in `~/ym4d-papers/`.

## 0. Repo search and prior work

- `library/prior/j2-claude.md` (digest, rule 0b): "partly covered". Not covered: the common-data all-scale representation, repeated and mirror lists, the actual rooted geometry, and a named register of open suppliers. This note attacks exactly those four items.
- `library/t0-joins.md:254–306` states the J2 contract (J2.1)–(J2.3) and a supplier table, with no proof. `library/ro1-vs-ca.md:42–48,148` says the missing step is "derive RO1's H-U from CA's correlation theorem". `library/t0-tree.md:147,156,265` list B04, B13 and J2 as **OPEN**.
- `library/open-registry.md:31,923,932` registers J2, B04 and B13 to `j2-claude` only. `open-core.md` and `l17c.md` have no J2 entry. So there is no duplicate attack (rule 0a).
- Ported suppliers read: P6 B3 (`port/p6-correlation.md:460–642`, the theorem; `:2645–2671`, the register; `:3431–3743`, the torus-bound proof); P8 H-LOC, H-DOM, H-TREE (`port/p8-positivity.md:152–198`); frozen LSC (`lsc.md:27–128,146–305,308–380,625–724`); P10 A20 (`port/p10-stability.md:1362–1440,1591–1680`).
- `library/prior/repo-search-2026-11-08.md` has no hit on UV1, H-U or the rooted source package.

## 1. Where the account treats the object (rule 9)

The account has no statement in the form of SR1 (4)–(6). It has the four ingredients, as one definition with a written argument:

- **CA-II 60692–60821, `6.2:def-localised-terms`.** For \(j\le K'\) and \(X\in D_j\) it defines \(e_j(X;v)=e^{(j)}(X;v)-e^{(j)}(X;0)\), \(\mathcal E(v)=\sum_{j\le K'}\sum_{X\in D_j}e_j(X;v)\) and \(\widetilde Z=e^{-\mathcal E}Z\). It states (L) locality on \(\operatorname{plaq}(X^+)\), (A) analyticity, (B) \(|e_j(X;v)|\le C_ee^{-(1-\delta)\kappa d_j(X)}\), (S) \(|\widetilde Z(v)|\le e^{E_+^\sharp N^4}\) and (F) \(\widetilde Z(0)\ge e^{-C_{\rm low}N^4}\). Its proof says: "each is read off from the correlation theorem."
- **CA-II 61745–61872, `6.2:rem-transported-weights`.** Class reading, part (i): (A), (B), (S) "hold for every weight \(v\in\mathcal W_{K'}\), and not only at the weights \(v=w_z\)". Literal reading, part (ii): for every finite system of real Lipschitz functions and every coefficient point of its polydisc. Quote (II:61811): "None of these five ingredients uses the presentation \(v=\sum_iz_if_i\)." And (II:61863–61864): the production formula "belongs to the construction written directly in terms of the weight".
- **CA-II 2722–2790, `5.1:def-weight-classes`.** \(\mathcal W_j(X)\) is defined by \(|w(p)|<r_j\) and \(\operatorname{Lip}_jw<\mathfrak l_j\). These conditions read only the plaquette function, not a list.
- **CA-II 25012–25241, `5.2:def-induction-format`**, clauses (a), (c), (d), (f): per-weight analyticity, locality on \(X^+\) and Balaban's bounds "uniformly on \(\mathcal W_j(X)\)".
- **CA-II 60350–60438, `6.1:not-units-sources`**, items (b)–(d): last-lattice units, \(s_j=ML^{j-K'}\), \(D_j\) the wall-connected unions of \(\pi_j\)-cubes, \(d_j(X)\) the shortest tree length divided by \(s_j\), \(X^+\) one layer of cubes, \(\operatorname{plaq}(Y)\) the bare plaquettes that meet \(Y\).
- **Balaban CMP 109, §0** (owner's copy, text layer lines 445–465): a localization domain is a union of a finite family of \(\pi_j\)-cubes connected through common walls, "their intersection is a \(d-1\)-dimensional cube"; \(d_j(X)\) is the length of a shortest tree graph in \(X\) meeting all its cubes, divided by \(M\), "graphs in the continuous space".

Classification. The per-weight properties (L), (A), (B), (S), (F) are **proved as an implication** in the account, from the correlation theorem and its proof; their standing is the correlation theorem's (P6 B3 register, §6 below). The account does **not** state: the size \(m(X)\) of SR1 or a rooted count in it; physical units on the torus of side \(2L^{m_1}\); the small-cutoff branch; one common normalization with uniform constants. The last two are frozen LSC. So this note is a **proof of a step they do not state**, the J2 join, from their statements and our frozen ports. It also contains one **check of their argument**: Lemma 3 reads the torus-bound proof for the list-independence claim.

## 2. Statement

### 2.1 Setting

Use SR1's conventions (`sr1.md:9–65`) and the dictionary of `t0-joins.md` J1 §1. The group is \(SU(2)\) with normalized Haar measure. On the torus \(\mathbb T_\ell=\mathbb R^4/\ell\mathbb Z^4\), \(\ell=2L^{m_1}\), the bare spacing is \(a=L^{-K}\) and the bare sites are \(a(\mathbb Z+\frac12)^4\). (The J1 translation by \(-\delta_a\) moves sites, tests and domains together, so every statement below transfers to SR1's \(a\mathbb Z^4\) verbatim.) Put \(a_p=1-\frac12\operatorname{Re}\operatorname{Tr}U(\partial p)\), \(\mathcal O_K(f)=\sum_pf(x(p))a_p\), and
\[
 Z_{K,\ell}(W)=\int e^{-\beta\sum_pa_p+\mathcal O_K(W)}\,dU ,\qquad
 t_f=\max\{\|f\|_\infty,\,40M\operatorname{Lip}f\}.               \tag{2.1}
\]
So \(Z_{K,\ell}(W)/Z_{K,\ell}(0)=\langle e^{\mathcal O_K(W)}\rangle\), and \(c_M:=40M\) in SR1's notation. Scales are \(a_s=L^{-s}\), \(0\le s\le K\).

**Parameters.** Take the account's order of choice for the correlation theorem (CA-II 2791–2868, ported in P6 B3) and LSC's additions (`lsc.md:27–76`, §7). In particular: odd \(L\); the margin \(\delta\in(0,\delta_J(L)]\), so \(1-\delta>\frac9{10}\); the decay parameter \(\kappa\); then \(\kappa_1\), \(M_1\) and \(M=L^{m'}\); the source radius, written \(\varrho\) as in LSC; the ceilings \(\gamma_J,\gamma_H,\gamma_D\); then the target \(g\le\min\{\gamma_H,\gamma_J,\gamma_D\}\), \(X=g^{-2}\). LSC (1)–(3) then fix the common flow \((x_k)\), \(m_J=m_J(g)\), the finite set \(\mathcal A\) and \(a^\natural=\max\mathcal A\). One extra choice is made, at the point where the account chooses \(\kappa\):
\[
 \kappa\ \ge\ \kappa^\natural:=4096 .                               \tag{H-\(\kappa\)}
\]
This is a further lower bound on \(\kappa\) depending on nothing. The account's theorem holds for every \(\kappa\) above its floors \(\max\{10\log L,\kappa_d,C_\delta(d)/\delta\}\) (CA-II 2823–2825), with all later constants chosen after \(\kappa\); it has no upper bound on \(\kappa\). So (H-\(\kappa\)) is an admissible choice, not an input.

**Data.** A first-passage datum is \((K,\beta)\) with \(\beta=x_0\ge X+B^\sharp\) and \(K=\min\{k:x_k\le X+B^\sharp\}\) for the common flow (LSC §1). Tori are \(\ell=2L^{m_1}\) with \(m_1\ge m_{\mathbb T}(g_-)\), \(g_-=(X+B^\sharp)^{-1/2}\) (LSC §1). Put \(K_J=\max\{k:x_j>X\ \forall j\le k\}\) and \(o:=K_J-K\). (LSC writes \(a\) for this offset; we write \(o\) because \(a\) is the spacing here.) **Case A** is \(K_J\ge m_J\); **Case B** is \(K_J<m_J\). In Case A put, as in LSC (4),
\[
 K'=K_J-m_J=K-b,\quad b=m_J-o\in[0,m_J],\quad N_T=2L^{m_1-o},\quad N=N_TL^{m_J}=2L^{m_1+b}=L^b\ell .          \tag{2.2}
\]
These are admissible correlation-theorem data (LSC (b)). The last lattice \(T^{(K')}\) has spacing \(L^{-b}\) in physical units (LSC (15)).

**Account objects, transported.** In Case A, for a level \(j\le K'\) let \(\pi_j\) be the partition of \(\mathbb T_\ell\) into closed cubes of side \(ML^{j-K}=Ma_{K-j}\). This is the account's \(\pi_j\) (side \(s_j=ML^{j-K'}\) in last-lattice units) after multiplying lengths by \(L^{-b}\). Let \(D_j\) be the finite unions of \(\pi_j\)-cubes connected through common walls (CA-II 60380–60382; CMP 109 §0), \(d_j(X)\) the length of a shortest tree graph in \(X\) meeting all cubes of \(X\), divided by the cube side, and \(Y^{[k]}\) the union of \(Y\) with \(k\) layers of touching cubes of the same partition. A complex function \(W\) on \(\mathbb T_\ell\) gives the account's weight \(v_W(y)=W(L^{-b}y)\) on the last-lattice torus of side \(N\). Write \(e_j(X;W):=e_j(L^bX;v_W)\) and \(\mathcal E(W)=\mathcal E(v_W)\) for the account's terms of CA-II 60698–60708.

### 2.2 Named hypotheses

Each is used only as stated. Their standings are in §6.

- **(H1) Local terms, class reading.** In Case A, at every \(v\in\mathcal W_{K'}\), for every \(j\le K'\) and \(X\in D_j\): (L) \(e_j(X;v)\) is a function of \((v(x_p))_{p\in\operatorname{plaq}(X^{[1]})}\) alone, and vanishes when these values vanish (the account's \(X^+\), one layer of cubes, lies in \(X^{[1]}\), so its (L) implies this); (A) \(v\mapsto e_j(X;v)\) is holomorphic on \(\mathcal W_{K'}\); (B) \(|e_j(X;v)|\le C_ee^{-(1-\delta)\kappa d_j(X)}\), with \(C_e\) independent of \(K,m_1,o\), the torus, the position and \(v\). This is CA-II 60714–60731 with the domain of 61745–61753 (i); in our register it is P8's H-LOC with H-DOM at \(\mathfrak r=1\) (`port/p8-positivity.md:152–166,200–208`).
- **(H2) Normalized stability and floor (LSC).** In Case A, at every \(v\in\mathcal W_{K'}\),
  \[
  \bigl|e^{-E_{\rm vac}-\mathcal E(v)}Z_{\rm bare}(v)\bigr|\le e^{C_+^*N^4},\qquad
  e^{-E_{\rm vac}}Z_{\rm bare}(0)\ge e^{-C^*_{\rm low}N^4},                \tag{2.3}
  \]
  with \(E_{\rm vac}\) real and source-independent, and \(C^*_+,C^*_{\rm low}\) uniform in \(K,g_0,m_1,o,N_T\) and positions. This is LSC's Result (`lsc.md:690–694`) and (5a)–(5b). Lemma 3 below records why the upper half holds at every such \(v\), not only at \(v=w_z\), once LSC's eight sourced hypotheses hold at \(v\).
- **(H3) Common data (J1).** SR1's and RO1's first-passage data, their block size \(M\) and constant \(c_M\) are the ones above: the common flow is the account's (LSC §3 "Flow", II:63072–63081), \(M\) is the account's \(M\), and \(c_M=40M\). This is part of J1 (J1-CA, J1-ID, J1-ORDER item 2); J2 does not prove it.

Lemma 3 also names the inputs behind (H2) at a general weight; §6 lists every upstream input with its standing.

### 2.3 Theorem J2

**Theorem J2 (implication).** Assume (H1)–(H3) and (H-\(\kappa\)). Set
\[
 \begin{gathered}
 r_{\rm src}=\varrho/2,\quad \kappa_{\rm src}=\frac{(1-\delta)\kappa}{162},\quad
 \kappa_D=22\log2,\quad A_{\rm src}=C_e\,e^{(1-\delta)\kappa},\quad C_{\rm dep}=12M,\\
 C_+=\max\{C^*_+,\,24r_{\rm src},\,1\}\,L^{4m_J},\qquad
 C_-=\max\{C^*_{\rm low},\,1\}\,L^{4m_J}.
 \end{gathered}                                                    \tag{2.4}
\]
These are fixed once \(g\) is fixed. They do not depend on \(K,\beta,m_1\), the list, its coefficients, or positions. Then \(\kappa_{\rm src}-\kappa_D\ge 7\), and for every first-passage datum, every \(m_1\ge m_{\mathbb T}(g_-)\), every finite family \((f_i)\) of real Lipschitz functions on \(\mathbb T_\ell\) (repetitions and overlapping supports allowed), and every complex \(z\) with \(\sum_i|z_i|t_{f_i}<2r_{\rm src}\), the source \(W=\sum_iz_if_i\) satisfies SR1 (4)–(6) as follows.

1. **(J2.1)** \(|Z_{K,\ell}(W)|\le\exp\{V+\operatorname{Re}[U(W)+\sum_{s=0}^K\sum_Xe_{s,X}(W)]+C_+\ell^4\}\) and \(Z_{K,\ell}(0)\ge e^{V-C_-\ell^4}\), with real \(V\) and \(U\equiv0\).
2. **(J2.2)** The domain terms are indexed by pairs \((s,X)\), \(X\) a nonempty finite union of closed cubes of side \(Ma_s\) in \(\mathbb T_\ell\). Each \(e_{s,X}\) is a function of the restriction of \(W\) to \(X^+:=X^{[2]}\) (in fact of its values at the barycentres there), independent of the list representing \(W\). It is holomorphic in the coefficients on the source ball, vanishes when \(W|_{X^+}=0\), and obeys
   \[
   |e_{s,X}(W)|\le A_{\rm src}e^{-\kappa_{\rm src}m(X)},\qquad
   \operatorname{diam}X^+\le C_{\rm dep}a_s(m(X)+1),                 \tag{2.5}
   \]
   with \(m(X)\) the least number of edges of a connected subgraph of the cube 1-skeleton meeting every cube of \(X\). Each \((s,X)\) carries one term, so there is no extra type multiplicity, and \(\kappa_{\rm src}>\kappa_D\), a valid rooted entropy rate for this indexing (Lemma 2). The sums are finite at fixed \((K,\ell)\), hence converge normally.
3. **(J2.3)** For every ball \(B(R)\) of radius \(R\ge0\), placed anywhere, and every \(t\ge0\),
   \[
   \sum_{X:\,X^+\cap B(R)\ne\varnothing,\ m(X)\ge t}e^{-\kappa_{\rm src}m(X)}
   \le C_6(R+1)^4a_s^{-4}e^{-7t},\qquad C_6=10^4\cdot2^{21},             \tag{2.6}
   \]
   uniformly in the scale, the torus and the position.

The source class contains the global mirror-periodized profiles of SR1 Lemma 3 and RO1 Lemma 2, with independent even and odd coefficient lists, because these are finite families of real Lipschitz functions on \(\mathbb T_\ell\) with arbitrary complex coefficients. Dividing (J2.1) by its floor gives RO1 (H.U) with \(C_{\rm st}=C_++C_-\) (Corollary 4).

## 3. Geometry: Balaban's tree length against SR1's edge-tree size

Fix one partition and write \(c\) for its cube side. The torus is \(\mathbb R^4/(nc\mathbb Z)^4\) with \(n\ge2\) cubes per side; for \(\pi_j\) on \(\mathbb T_\ell\), \(n=\ell/(Ma_{K-j})\ge2L^{11}\) by the torus floor (LSC §1, \(m_1\ge m_{\mathbb T}(g_-)\ge m'+11\)). Distances are torus distances. An *edge tree* is a connected subgraph of the grid 1-skeleton; \(m(X)\) is the least number of edges of one that meets every cube of \(X\). For a nonempty union \(X\) of closed grid cubes, \(|X|\) is its number of cubes.

**Lemma 1.**

- (a) *Corner.* If an edge tree \(G\) meets a closed grid cube \(Q\), then some vertex of \(G\) is a corner of \(Q\).
- (b) *Cover.* Let \(T\) be a tree graph (a finite connected acyclic union of straight segments) of length \(\lambda\), where length is measured in a norm \(|\cdot|_*\) with \(|\cdot|_*\ge|\cdot|_\infty\). (The Euclidean norm qualifies, and so does every \(\ell^p\) norm.) Then at most \(81(\lceil2\lambda/c\rceil+1)\) closed grid cubes meet \(T\).
- (c) *Size.* If \(X\in D\), that is, its cubes are connected through common walls, then
  \[
  m(X)\le|X|-1\le162\,d(X)+161,\qquad\text{so}\qquad d(X)\ge\frac{m(X)-161}{162}.   \tag{3.1}
  \]
- (d) *Enlargement.* If a point \(y\) has distance less than \(c\) from a union \(Y\) of grid cubes, then \(y\in Y^{[1]}\). Hence the barycentre of a bare plaquette of side \(\varepsilon\le c/3\) that meets \(X^{[1]}\) lies in \(X^{[2]}\).
- (e) *Diameter.* \(\operatorname{diam}X^{[k]}\le c\,(m(X)+4(k+1))\) for every \(k\ge0\). In particular \(\operatorname{diam}X^{[2]}\le12c\,(m(X)+1)\).

*Proof.* (a) Work in a lift where \(Q=[0,c]^4\). A vertex of \(G\) lying in \(Q\) is a grid point in \([0,c]^4\), hence a corner. Otherwise \(G\) meets \(Q\) in an edge \(\{u+te_i:0\le t\le c\}\), \(u\in c\mathbb Z^4\), at some \(t\). For \(k\ne i\), \(u_k\in[0,c]\cap c\mathbb Z=\{0,c\}\). Also \(u_i+t\in[0,c]\) forces \(u_i\in\{-c,0,c\}\). If \(u_i\in\{0,c\}\) then \(u\) is a corner of \(Q\). If \(u_i=-c\) then \(t=c\), and the other endpoint \(u+ce_i\) is a corner of \(Q\). Both endpoints are vertices of \(G\).

(b) If \(\lambda=0\), \(T\) is one point; each coordinate of a point lies in at most two closed grid intervals, so at most \(2^4=16\) cubes contain it. Let \(\lambda>0\). Double every edge of \(T\). The doubled multigraph is connected and every degree is even, so it has a closed Euler walk that traverses each edge of \(T\) exactly twice. Parametrize this walk by \(|\cdot|_*\)-arc length: \(\gamma:[0,2\lambda]\to T\) is onto and \(|\gamma(t)-\gamma(t')|_\infty\le|t-t'|\). Put \(n_0=\lceil2\lambda/c\rceil\) and \(p_k=\gamma(\min\{kc,2\lambda\})\), \(0\le k\le n_0\). Each \(t\in[0,2\lambda]\) is within \(c/2\) of some \(\min\{kc,2\lambda\}\). So \(T\) is covered by the closed sup-norm balls \(B_\infty(p_k,c/2)\). Each such ball projects on each coordinate circle to an arc of length \(c\); that arc meets at most three closed grid intervals of length \(c\) (the integers \(q\) with \(qc\le u+c\) and \((q+1)c\ge u\) lie in an interval of length two). So each ball meets at most \(3^4=81\) closed grid cubes. A cube that meets \(T\) meets one of the balls. This gives the bound.

(c) Let \(\eta>0\) and take a tree graph \(T\subset X\) meeting all cubes of \(X\) with length \(\lambda\le c(d(X)+\eta)\). Every cube of \(X\) meets \(T\), so by (b) \(|X|\le81(\lceil2\lambda/c\rceil+1)\le81(2\lambda/c+2)\le162(d(X)+\eta+1)\); for \(\lambda=0\) the bound \(16\) is smaller. Let \(\eta\downarrow0\): \(|X|\le162(d(X)+1)\). For the other inequality, give each cube \(Q\), the image of \(y+[0,c]^4\) with \(y\in c\mathbb Z^4\), its lower corner \(\underline Q\), the image of \(y\). If two cubes of \(X\) share a wall, their index vectors differ in exactly one coordinate by \(\pm1\), so their lower corners are joined by one grid edge. The wall-adjacency graph of \(X\) is connected (CMP 109 §0). Its spanning tree has \(|X|-1\) edges. The corresponding grid edges form a connected subgraph containing \(\underline Q\in Q\) for every cube \(Q\) of \(X\). A spanning tree of that subgraph has at most \(|X|-1\) edges and the same vertices, so it meets every cube of \(X\). Hence \(m(X)\le|X|-1\le162d(X)+161\).

(d) Let \(\operatorname{dist}(y,Q)<c\) for a cube \(Q\) of \(Y\), lifted to \(\underline q+[0,c]^4\). Then each coordinate obeys \(\underline q_i-c<y_i<\underline q_i+2c\). So \(y_i\) lies in one of the grid intervals \([\underline q_i-c,\underline q_i]\), \([\underline q_i,\underline q_i+c]\), \([\underline q_i+c,\underline q_i+2c]\), each of which meets \([\underline q_i,\underline q_i+c]\). The product cube contains \(y\) and touches \(Q\). For the plaquette statement: a point of a bare plaquette is within \(\varepsilon/\sqrt2<c\) of its barycentre, so the barycentre is within distance less than \(c\) of \(X^{[1]}\), hence in \(X^{[2]}\).

(e) Let \(G\) be an edge tree with \(m(X)\) edges meeting every cube of \(X\). A point \(x\in X^{[k]}\) lies in a cube \(Q_k\) joined to a cube \(Q_0\) of \(X\) by a chain \(Q_k,\dots,Q_0\) of touching cubes. So \(\operatorname{dist}(x,Q_0)\le\sum_{i=1}^k\operatorname{diam}Q_i=2kc\), since a side-\(c\) cube in four dimensions has diameter \(2c\). By (a), \(Q_0\) contains a vertex \(u\) of \(G\), so \(\operatorname{dist}(x,u)\le2(k+1)c\). Two vertices of \(G\) are joined inside \(G\) by at most \(m(X)\) edges of length \(c\). Hence \(\operatorname{diam}X^{[k]}\le4(k+1)c+m(X)c\). For \(k=2\), \(m+12\le12(m+1)\). \(\square\)

*Remark.* Balaban notes that shortest trees may be taken along cube edges (CMP 109 §0). Lemma 1 does not use this. With Euclidean length that remark would need care: along the diagonal staircase of cubes \([q,q+1]^4\), a continuum tree pays \(2\) per step and an edge tree pays \(4\). Lemma 1(c) only needs some fixed constant.

## 4. Rooted count and the ST6 bound

**Lemma 2.** At one scale, with cubes of side \(c=Ma_s\) on \(\mathbb T_\ell\):

- (a) For every cube \(Q\) and every \(m\ge0\), \(\#\{X:\,Q\subset X,\ m(X)=m\}\le16\cdot8^{2m}\cdot2^{16(m+1)}=2^{20}\,2^{22m}\). Here \(X\) runs over all nonempty finite unions of cubes. So \(\kappa_D=22\log2\) is a valid rooted entropy rate, with prefactor \(2^{20}\).
- (b) If \(\kappa_{\rm src}-\kappa_D\ge7\), then (2.6) holds with \(X^+=X^{[2]}\), and \(\sum_Xe^{-\kappa_{\rm src}m(X)}\le2^{21}\ell^4a_s^{-4}\).

*Proof.* (a) This is SR1 Lemma 5, (19), and RO1 (2.4), with the corner step made explicit by Lemma 1(a). Take an edge tree \(G\) with \(m\) edges meeting every cube of \(X\). By Lemma 1(a) it has a vertex at a corner of \(Q\): at most \(16\) choices. A depth-first closed walk from that vertex traverses each edge twice. It has length \(2m\) and at most \(8\) choices per step, and it determines \(G\). Every cube of \(X\) meets \(G\), so by Lemma 1(a) it contains one of the \(m+1\) vertices of \(G\). Each vertex is a corner of at most \(16\) cubes. So \(X\) is a subset of at most \(16(m+1)\) cubes. Multiply the three counts. The torus changes nothing: a step still has at most \(8\) choices, and a vertex is still a corner of at most \(16\) cubes.

(b) Write \(\gamma=\kappa_{\rm src}-\kappa_D\ge7\). By (a), for a fixed root cube,
\[
\sum_{X\supset Q,\ m(X)\ge t}e^{-\kappa_{\rm src}m(X)}\le2^{20}\sum_{m\ge\lceil t\rceil}e^{-\gamma m}
\le\frac{2^{20}e^{-\gamma t}}{1-e^{-7}}\le2^{21}e^{-7t}.
\]
If \(X^{[2]}\) meets \(B(R)\), the argument of Lemma 1(e) gives a cube \(Q\) of \(X\) within distance \(4c\) of \(B(R)\), so \(Q\) meets the concentric ball of radius \(R+4c\). On each coordinate circle the projection of that ball is an arc of length \(2(R+4c)\), which meets at most \(2(R+4c)/c+2\) closed grid intervals. So at most \((2R/c+10)^4\le10^4(R/c+1)^4\le10^4(R+1)^4a_s^{-4}\) cubes can serve as \(Q\); the last step uses \(c=Ma_s\ge a_s\) and \(a_s\le1\). Multiply. For the global sum, the torus has \((\ell/c)^4\le\ell^4a_s^{-4}\) cubes, and each has rooted sum at most \(2^{21}\) at \(t=0\). \(\square\)

**The margin.** Under (H-\(\kappa\)), \(1-\delta>\frac9{10}\) and \(162\cdot22.75=3685.5<3686.4=\frac9{10}\cdot4096\), so \(\kappa_{\rm src}>22.75\). Also \(\log2<0.7\), so \(\kappa_D<15.4\). Hence \(\kappa_{\rm src}-\kappa_D>7.35\ge7\). This is the only place (H-\(\kappa\)) is used.

## 5. Stability at a general weight: a reading of the account's proof

**Lemma 3.** Work in Case A. Let \(v\in\mathcal W_{K'}\). Assume at \(v\): the sourced mass identity \(\int\rho^v_{K'}dV_{K'}=\int\rho^v_0\,dU\) (P10 A20, CA-I 157263–157283, with its premises H-SOURCE-IND, H-COMPLEX-MOVES, H-GAUGE-SECTOR, H-SOURCE-REFERENCE, H-FORWARD-REVERSE); the induction format with sources at every level \(k\le K'\) (CA-II 25012–25241); and LSC's eight retained sourced upper-bound hypotheses (`lsc.md:233`, the nine of CA-II 59647–59680 less the floor). Then the upper half of (2.3) holds at \(v\), with LSC's constant \(C^*_+\).

*Proof (reading, checked line by line against the source).* LSC proves the upper bound (13), (13a) and its Result from these inputs at one weight \(w\) (`lsc.md:233–301`). The representation is \(\widehat Z(w)=\int\rho^w_{K'}dV_{K'}\) with \(E=E_{\rm vac}\) (`lsc.md:199`, (N6), and the sourced integral identity). The bound then uses LSC's items 1–4 (`lsc.md:239–242`), which port CA-II 59718–59813. I read CA-II 59645–59822 in full, in the verbatim port `port/p6-correlation.md:3436–3613`, and against the fetched source. In that range the source enters only through the weight \(w\): through its local terms \(e^{(j)}(X;w)\) and their bound (3), through the history expansion of \(\rho^w_{K'}\), and through the sourced budget, complex-weight, zone-cell, modification, gas, count and label hypotheses at \(w\). The list \(w=\sum_iz_if_i\) is named at II:59685–59687 only to place \(w\) in the admissible ball. Its other uses are the independence of \(e_j(X;\cdot)\) from \(z_i\) when \(X^+\) misses \(\operatorname{supp}f_i\), and the separation \(\mathsf d\) and the order \(n\); all three are used only in the derivative estimates (\(\alpha\))–(\(\beta\)), II:59823–59924, which Lemma 3 does not use. The weight-class lemma (CA-II 2722–2790) puts every \(w_z\), \(z\in\mathbb D\), in \(\mathcal W_{K'}\), and only membership in \(\mathcal W_{K'}\) is used afterwards. So the deduction applies verbatim at every \(v\in\mathcal W_{K'}\) at which its inputs hold. \(\square\)

This is the account's own remark, CA-II 61745–61815 part (i) (proof of (i) at 61781–61815), at its standing. The check here is of that deduction only. It does not show that the inputs hold at a general weight; the account asserts them for every weight in \(\mathcal W_k\) (CA-II 61784–61808), and they stay named (§6). The floor half of (2.3) is source-free and needs no such reading.

## 6. Proof of Theorem J2

Fix a datum \((K,\beta)\), \(m_1\ge m_{\mathbb T}(g_-)\), a finite real Lipschitz family \((f_i)\) on \(\mathbb T_\ell\), and \(z\) with \(\sum_i|z_i|t_{f_i}<2r_{\rm src}=\varrho\). Put \(W=\sum_iz_if_i\). By LSC (a), \(K\le K_J\) and \(o=K_J-K\in\mathcal A\).

**Step 1 (Case A: the source is admissible).** Put \(\tilde f_i(y)=f_i(L^{-b}y)\) on the last-lattice torus of side \(N=L^b\ell\). Then \(v_W=\sum_iz_i\tilde f_i\). By LSC (16), \(\|\tilde f_i\|_\sharp=\max\{\|f_i\|_\infty,40ML^{-b}\operatorname{Lip}f_i\}\le t_{f_i}\). So \(\sum_i|z_i|\|\tilde f_i\|_\sharp<\varrho\): \(z\) lies in the account's polydisc of the family \((\tilde f_i)\). By the last claim of `5.1:def-weight-classes` (CA-II 2752–2753, proof 2776–2789), \(v_W\in\mathcal W_{K'}\). Nothing here uses separation, the number of functions, or distinctness: repeated and overlapping members are allowed, since only the sum \(v_W\) and the triangle inequality enter.

**Step 2 (Case A: the identity).** Dilation by \(L^b\) maps the bare sites \(a(\mathbb Z+\frac12)^4\) of \(\mathbb T_\ell\) onto \(\varepsilon(\mathbb Z+\frac12)^4\), \(\varepsilon=L^ba=L^{-K'}\). It maps bonds, plaquettes and barycentres to bonds, plaquettes and barycentres, preserves the Haar product and the Wilson weight, and gives \(v_W(L^bx_p)=W(x_p)\). Hence \(Z_{K,\ell}(W)=Z_{\rm bare}(v_W)\) (LSC (15)–(16) and the display after (16)).

**Step 3 (Case A: the decomposition and (J2.1)).** Put \(V=E_{\rm vac}\), \(U\equiv0\), and for \(0\le s\le K\) and \(X\) a nonempty union of side-\(Ma_s\) cubes,
\[
 e_{s,X}(W)=\begin{cases}e_{K-s}(L^bX;v_W),& s\ge b\ \text{and}\ L^bX\in D_{K-s},\\ 0,&\text{otherwise.}\end{cases}   \tag{6.1}
\]
The map \(X\mapsto L^bX\) is a bijection from unions of side-\(Ma_s\) cubes of \(\mathbb T_\ell\) onto unions of \(\pi_j\)-cubes of the last-lattice torus, \(j=K-s\). Indeed \(L^bMa_s=ML^{b-s}=ML^{j-K'}=s_j\). Since \(j\le K'\) exactly when \(s\ge b\),
\[
 \sum_{s=0}^K\sum_Xe_{s,X}(W)=\sum_{j\le K'}\sum_{X'\in D_j}e_j(X';v_W)=\mathcal E(v_W).
\]
By (H2) at \(v_W\) and Step 2,
\[
 |Z_{K,\ell}(W)|=e^{E_{\rm vac}}\,e^{\operatorname{Re}\mathcal E(v_W)}\,
 \bigl|e^{-E_{\rm vac}-\mathcal E(v_W)}Z_{\rm bare}(v_W)\bigr|
 \le e^{V+\operatorname{Re}\sum_{s,X}e_{s,X}(W)+C^*_+N^4}.
\]
Here \(N^4=L^{4b}\ell^4\le L^{4m_J}\ell^4\). If \(C^*_+\ge0\), then \(C^*_+N^4\le C_+\ell^4\). If \(C^*_+<0\), then \(C^*_+N^4<0<C_+\ell^4\). The floor half of (H2) gives \(Z_{K,\ell}(0)\ge e^{V-C^*_{\rm low}N^4}\ge e^{V-C_-\ell^4}\) in the same way. This is (J2.1) in Case A.

**Step 4 (Case B: (J2.1)).** Here \(K\le K_J\le m_J-1\). Put \(V=\log Z_{K,\ell}(0)\), which is real because \(Z_{K,\ell}(0)>0\), \(U\equiv0\), and every \(e_{s,X}\equiv0\). The floor holds since \(C_->0\). The torus has \((\ell/a)^4\) sites and \(6(\ell/a)^4\) plaquettes, and \(0\le a_p\le2\). With \(\sup|W|\le\sum_i|z_i|\|f_i\|_\infty<2r_{\rm src}\),
\[
 |\mathcal O_K(W)|\le\sum_p|W(x_p)|a_p<24r_{\rm src}(\ell/a)^4
 =24r_{\rm src}L^{4K}\ell^4\le24r_{\rm src}L^{4m_J}\ell^4\le C_+\ell^4 .
\]
So \(|Z_{K,\ell}(W)|\le\int e^{-\beta\sum_pa_p}e^{\operatorname{Re}\mathcal O_K(W)}dU\le Z_{K,\ell}(0)e^{C_+\ell^4}=e^{V+C_+\ell^4}\). All other clauses hold trivially for zero terms. The diameter clause is a property of \(X\) alone and holds by Lemma 1(e).

**Step 5 (Case A: (J2.2)).** Fix \((s,X)\) with \(s\ge b\), \(X'=L^bX\in D_j\), \(j=K-s\).

- *Dependence region and list independence.* By (H1)(L), \(e_j(X';v)\) is a function of \(v(x_p)\), \(p\in\operatorname{plaq}(X'^{[1]})\). The cube side is \(s_j=ML^j\varepsilon\ge M\varepsilon\ge9\varepsilon\), since the account takes \(M\ge3L\ge9\) (CA-II 2844). Lemma 1(d) puts all these barycentres in \(X'^{[2]}\). After dilation, \(e_{s,X}(W)\) is a function of the values of \(W\) at the barycentres in \(X^{[2]}=X^+\). It is a function of \(W\), hence of no list. If \(W|_{X^+}=0\), these values vanish, and (L) gives \(e_{s,X}(W)=0\).
- *Holomorphy.* \(\mathcal W_{K'}\) is open in the finite-dimensional space of plaquette functions: it is cut out by strict inequalities on finitely many continuous functions. The map \(z\mapsto v_{W_z}\) is affine and sends the source ball into \(\mathcal W_{K'}\) (Step 1). By (H1)(A), \(z\mapsto e_{s,X}(W_z)\) is holomorphic on the ball, for any list, including lists with independent even and odd coefficients.
- *Bound.* The ratio \(d_j\) and the edge count \(m\) are invariant under dilation, because lengths and the cube side scale together. By (H1)(B) and Lemma 1(c),
  \[
  |e_{s,X}(W)|\le C_ee^{-(1-\delta)\kappa d(X)}\le C_ee^{-(1-\delta)\kappa(m(X)-161)/162}
  \le C_ee^{(1-\delta)\kappa}e^{-\kappa_{\rm src}m(X)}=A_{\rm src}e^{-\kappa_{\rm src}m(X)} .
  \]
- *Diameter.* Lemma 1(e) with \(c=Ma_s\) gives \(\operatorname{diam}X^+\le12Ma_s(m(X)+1)=C_{\rm dep}a_s(m(X)+1)\).
- *Entropy and multiplicity.* Each pair \((s,X)\) carries exactly one term. By Lemma 2(a) and §4, \(\kappa_{\rm src}>\kappa_D+7\).
- *Convergence.* At fixed \((K,\ell)\) the pairs \((s,X)\) are finitely many and each term is bounded by \(A_{\rm src}\) on the ball. So the sums converge normally on the ball.

**Step 6 ((J2.3)).** This is Lemma 2(b), using \(\kappa_{\rm src}-\kappa_D\ge7\).

**Step 7 (uniformity).** By (2.4), the constants depend on the account's construction constants \(C_e,\delta,\kappa,M\), on \(\varrho\), and on \(g\) through \(m_J(g)\), \(C^*_+\) and \(C^*_{\rm low}\). LSC makes the last two uniform in \(K,g_0,m_1,o,N_T\) and positions. Nothing depends on the list, its coefficients or the datum. \(\square\)

**Corollary 4 (RO1 H-U).** In the setting of Theorem J2,
\[
 \frac{|Z_{K,\ell}(W)|}{Z_{K,\ell}(0)}\le
 \exp\Bigl\{\operatorname{Re}\sum_{s,X}e_{s,X}(W)+(C_++C_-)\ell^4\Bigr\},              \tag{6.2}
\]
which is (H.U) with \(U_\ell\equiv0\) and \(C_{\rm st}=C_++C_-\). For RO1's mirror-periodized source \(W=\sum_iz_iH^+_i+\sum_iz'_iH^-_i\), with independent \(z,z'\), apply Theorem J2 to the family \((H^+_i,H^-_i)\). Its members are real Lipschitz on \(\mathbb T_\ell\) with \(t_{H^\pm_i}\le t_{f_i}\): CA-II 61719–61728 proves \(\operatorname{Lip}h^\pm_{c,i}=\operatorname{Lip}f_i\), and SR1 Lemma 3 states the same bound. So (6.2) holds when \(\sum_i(|z_i|+|z'_i|)t_{f_i}<2r_{\rm src}\), jointly holomorphically in \((z,z')\). Conjugate evaluation \(z'=\bar z\) comes afterwards.

*Proof.* Divide the upper bound of (J2.1) by its floor; \(V\) cancels. \(\square\)

**What the consumers read, checked against their text.** SR1 Lemma 3 (`sr1.md:164–197`) and RO1 Lemma 2 (`ro1.md:161–191`) retain the terms whose dependence region lies in one open cell. They conjugate the odd-cell terms and count the discarded terms by (5)–(6) and the rooted sum. SR1 Lemma 5 (`sr1.md:218–258`) uses (17), which Lemma 2(b) gives, and the diameter clause. A term in an odd cell reads only \(\sum_iz'_iH^-_i\), because \(H^+_i\) vanishes off even cells (CA-II 61719–61720). So it is a holomorphic function of \(z'\), and its conjugate at \(z'=\bar z\) is holomorphic in \(z\). The scales \(s<b\) carry zero terms. The consumers' scale sums therefore include every \(0\le s\le K\), as SR1 (4) and RO1 (2.6) require, and those scales cost nothing beyond the bulk term \(C_\pm\ell^4\). The cell normalizers built from (6.1) are locally bounded in \(\ell\) at fixed \(K\): a cell of side \(l\) holds at most \(C(l/a_s)^4\) retained domains per scale, each bounded by \(A_{\rm src}\). This is what SR1 Lemma 3's compactness step uses.

## 7. Order of constants

The J2 constants split in two groups.

- **Fixed before the coupling.** \(c_M=40M\), \(r_{\rm src}=\varrho/2\), \(\kappa_{\rm src}\), \(\kappa_D\), \(A_{\rm src}=C_ee^{(1-\delta)\kappa}\), \(C_{\rm dep}=12M\) and \(C_6\) read only \(L,\delta,\kappa,M,\varrho\) and the construction constant \(C_e\). The account fixes all of these before its ceiling \(\gamma_J\) (CA-II 2791–2868). (H-\(\kappa\)) is imposed when \(\kappa\) is chosen, so it changes no earlier choice.
- **Fixed after the coupling.** \(C_\pm\) read \(g\) through \(m_J(g)\), \(C^*_+\) and \(C^*_{\rm low}\). LSC's exponents depend on \(L,\mathfrak p,g,\varrho\), and are uniform only once \(g\) is fixed (`lsc.md:128`, §7).

So the package does not fit IN1's row 8 literally. SR1's order table (`sr1.md:101`) and RO1's order paragraph (`ro1.md:88`) ask for the source constants before \(X_0\) and \(g\). I checked every use of \(C_\pm\), \(C_{\rm st}\), \(A_{\rm src}\) and \(r_{\rm src}\) in SR1 and RO1: `sr1.md:172,189–190,207,234,251–255,283`; `ro1.md:90,175,183,195,200`. Each use builds a later constant (\(B_C,Q_{n,R},Q_0,p,C_B,B_0,C_I\)) that precedes only the test data, positions, states and cutoffs. None feeds a coupling ceiling; RO1 states "RO1 adds no ceiling on the coupling" (`ro1.md:88`). Therefore SR1 Theorem 1 and RO1 Theorem 9 hold with the J2 constants fixed after \(g\), at fixed \(g\). The factorial exponent \(k=\lceil p\rceil+5\) does not depend on \(g\): \(p\) comes from the middle row of SR1 (20), which reads \(A_{\rm src}\) only. The literal placement in IN1's row 8 is a J1-ORDER question for the IN1 construction, not for this package. **Forward to the lead:** J1-ORDER item 4 should record that the account's \(C_\pm\) are \(g\)-dependent last-scale constants.

## 8. Register of named inputs and their standing

Theorem J2 is an implication from (H1)–(H3). Behind them are the following inputs, unchanged from their ports. No input is closed here.

| Input | Where it enters | Standing carried |
|---|---|---|
| CA correlation theorem (iii): induction format with sources at every level \(k\le K'\), uniformly on \(\mathcal W_j(X)\) (CA-II 2921–2936, 25012–25241) | (H1) (L), (A), (B); Lemma 3 | P6 B3 **ported, not yet checked**. Its register (`port/p6-correlation.md:2647–2670`): C-admitted; C-boundary (assumed); **C-preparation, window data "proof outstanding"** (II:2810–2812); **C-B1 polydisc holomorphy, "Proof outstanding"** (II:46131–46167), needed for (A) on actual terms; C-slots; C-frozen, whole-disc bound on \(Q_\zeta\); C-sites, eight step hypotheses; C-reference; C-one-loop, cited Balaban CMP 109 (1.22), Thm 3 and CMP 116 (2.41); **C-Mfree incomplete at (\*)**; **C-sixth not written out**. |
| CA 6.2 (L), (A), (B) in the class reading (CA-II 60714–60731, 61745–61815) | (H1) | The account's deduction from (iii). Its domain claim (i) is the reading checked in Lemma 3. In our register this is P8 H-LOC with H-DOM at \(\mathfrak r=1\), a hypothesis of P8. |
| LSC's eight retained sourced upper-bound hypotheses, at every \(v\in\mathcal W_{K'}\) (CA-II 59647–59680 less the floor) | (H2) upper half; Lemma 3 | C-last, at CA standing. The account asserts them for every weight in \(\mathcal W_k\) (CA-II 61784–61808). |
| LSC (a), (b), (5), (5a)–(5b) and Result | (H2); Steps 1–4 | **Frozen**: checked line by line by Claude, first failing step none (`gates/lsc2-gate.md`). Inputs retained there: the flow and coefficient identification (II:63072–63081); the zero-source format and vacuum theorem (CA-I 4.36); equality at zero source of sourced and source-free one-step energies (assumed by the authors too, II:140916–140926); Balaban CMP 102b Theorem 1 (real background); positivity and representation hypotheses of the density theorem. |
| P10 A20, exact sourced mass (CA-I 157263–157283) | Lemma 3 (representation of \(\widehat Z(v)\)) | **Ported, not yet checked**; premises H-SOURCE-IND, H-COMPLEX-MOVES, H-GAUGE-SECTOR, H-SOURCE-REFERENCE (Balaban CMP 122a pp. 176–177), H-FORWARD-REVERSE (CMP 122b). |
| J1: common flow, block size \(M\), \(c_M=40M\), order | (H3); §7 | **OPEN** (J1-CA, J1-ID, J1-ORDER). For the account's package this note fixes the J1-ORDER item 2 geometry: SR1's cubes are the account's \(\pi_j\) cubes, and SR1's \(m(X)\) and rooted rate are related to the account's \(d_j\) by Lemmas 1–2. |
| Choice (H-\(\kappa\)) | §4 margin | A choice inside the account's order. Not an input. |

Not used: P8 H-TREE (Balaban CMP 116 (1.26)), which Lemmas 1–2 replace by a hand count; C-compact, C-positive, C-rank; C-uniform-last, which LSC removes by fixing \(m=m_J(g)\); P8's chessboard estimates, which belong to the consumer side.

## 9. What this does not show

- It does not prove any input in §8. J2 now stands exactly where the account's correlation theorem and LSC stand, plus J1. It stands no better than those.
- It gives no global nonvanishing of \(Z(W)\) and no global logarithm.
- It gives the torus statement only. All-state transfer, one-point comparison, graded moments and insertion density remain SR1 Lemmas 2–10 and RO1 Lemmas 1–3. Those are frozen implications from (4)–(6) and H-U; they now read Theorem J2.
- It does not give J3 (state-uniform TU10), J4, J5, or the IN1 cross-construction identity J1-ID.
- The small-cutoff branch (Case B) uses a crude bound with \(L^{4m_J}\). This suffices for J2 because \(m_J\) depends only on \(g\).

## Result

**Proof**

Theorem J2 holds as an implication. Under (H1) (the account's local-term properties, class reading), (H2) (frozen LSC's normalized stability and floor) and (H3) (J1's common data), and with the admissible choice \(\kappa\ge4096\), SR1 (4)–(6) and RO1 (H.U) hold in their full scope. The scope is: every first-passage datum, both the Case A and the small-cutoff Case B; every sufficiently large torus \(\ell=2L^{m_1}\), \(m_1\ge m_{\mathbb T}(g_-)\); every finite real Lipschitz list, with repetitions and overlaps; mirror-periodized profiles with independent even and odd coefficient lists before conjugate evaluation; and all scales \(0\le s\le K\). The data are \(U\equiv0\), \(V=E_{\rm vac}\) in Case A and \(V=\log Z(0)\) in Case B, and the account's localized vacuum-energy differences transported to physical units in (6.1). They come with the actual rooted geometry: dependence region \(X^{[2]}\), \(m(X)\le162\,d_j(X)+161\) (Lemma 1), the rooted rate \(\kappa_D=22\log2\) with no extra type multiplicity, the margin \(\kappa_{\rm src}-\kappa_D>7\), and ST6 with explicit constants (Lemma 2). The constants are (2.4); \(C_\pm\) depend on \(g\), which SR1 and RO1 accept (§7).

Kind (rule 9): a proof of a join the account does not state, plus one check of their argument. The account's claim that its stability bound holds at every weight, independently of the list presentation, was read against the proof of the torus bound, CA-II 59645–59822: first failing step none (Lemma 3).

Proved by Claude, not yet checked by the other model.

**What stays open:** the inputs of §8. These are the correlation theorem's register: the preparatory window data and the polydisc holomorphy (both "proof outstanding"), the incomplete M-freeness, the unwritten sixth family, and the eight sourced upper-bound hypotheses. Also LSC's source-free inputs, P10 A20's premises, and J1. H-TREE is no longer needed for J2. Suggested node update for the lead: B04, B13 and J2 move from **OPEN** to **proved conditional (Claude, unchecked)** on the §8 inputs. They are then OPEN only through P6/LSC/P10 and J1.
