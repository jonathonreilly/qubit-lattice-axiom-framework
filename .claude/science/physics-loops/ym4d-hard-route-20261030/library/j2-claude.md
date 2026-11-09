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
This is a further lower bound on \(\kappa\) depending on nothing. The account's theorem holds for every \(\kappa\) above its floors \(\max\{10\log L,\kappa_d,C_\delta(d)/\delta\}\) (CA-II 2826–2828), with all later constants chosen after \(\kappa\); it has no upper bound on \(\kappa\). So (H-\(\kappa\)) is an admissible choice, not an input.

**Data.** A first-passage datum is \((K,\beta)\) with \(\beta=x_0\ge X+B^\sharp\) and \(K=\min\{k:x_k\le X+B^\sharp\}\) for the common flow (LSC §1). Tori are \(\ell=2L^{m_1}\) with \(m_1\ge m_{\mathbb T}(g_-)\), \(g_-=(X+B^\sharp)^{-1/2}\) (LSC §1). Put \(K_J=\max\{k:x_j>X\ \forall j\le k\}\) and \(o:=K_J-K\). (LSC writes \(a\) for this offset; we write \(o\) because \(a\) is the spacing here.) **Case A** is \(K_J\ge m_J\); **Case B** is \(K_J<m_J\). In Case A put, as in LSC (4),
\[
 K'=K_J-m_J=K-b,\quad b=m_J-o\in[0,m_J],\quad N_T=2L^{m_1-o},\quad N=N_TL^{m_J}=2L^{m_1+b}=L^b\ell .          \tag{2.2}
\]
These are admissible correlation-theorem data (LSC (b)). The last lattice \(T^{(K')}\) has spacing \(L^{-b}\) in physical units (LSC (15)).

**Account objects, transported.** In Case A, for a level \(j\le K'\) let \(\pi_j\) be the partition of \(\mathbb T_\ell\) into closed cubes of side \(ML^{j-K}=Ma_{K-j}\). This is the account's \(\pi_j\) (side \(s_j=ML^{j-K'}\) in last-lattice units) after multiplying lengths by \(L^{-b}\). Let \(D_j\) be the finite unions of \(\pi_j\)-cubes connected through common walls (CA-II 60398–60401; CMP 109 §0), \(d_j(X)\) the length of a shortest tree graph in \(X\) meeting all cubes of \(X\), divided by the cube side, and \(Y^{[k]}\) the union of \(Y\) with \(k\) layers of touching cubes of the same partition. A complex function \(W\) on \(\mathbb T_\ell\) gives the account's weight \(v_W(y)=W(L^{-b}y)\) on the last-lattice torus of side \(N\). Write \(e_j(X;W):=e_j(L^bX;v_W)\) and \(\mathcal E(W)=\mathcal E(v_W)\) for the account's terms of CA-II 60698–60708.

### 2.2 Named hypotheses

Each is used only as stated. Their standings are in §6.

- **(H1) Local terms, class reading.** In Case A, at every \(v\in\mathcal W_{K'}\), for every \(j\le K'\) and \(X\in D_j\): (L) \(e_j(X;v)\) is a function of \((v(x_p))_{p\in\operatorname{plaq}(X^{[1]})}\) alone, and vanishes when these values vanish; (A) \(v\mapsto e_j(X;v)\) is holomorphic on \(\mathcal W_{K'}\); (B) \(|e_j(X;v)|\le C_ee^{-(1-\delta)\kappa d_j(X)}\), with \(C_e\) independent of \(K,m_1,o\), the torus, the position and \(v\). This is CA-II 60714–60731 with the domain of 61745–61753 (i); in our register it is P8's H-LOC with H-DOM at \(\mathfrak r=1\) (`port/p8-positivity.md:152–166,200–208`).
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

