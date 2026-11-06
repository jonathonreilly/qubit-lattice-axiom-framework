lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T02:31Z

# CR (outside re-blocking minimiser bounds): a path-free proof by one-level re-blocking

Started 2026-11-06T14:31Z at commit 54e85c9cd, branch claude/ym4d-hard-route. Research text. Proved by Claude (Opus 5.5, max effort), not yet checked by the other model. No status. No computer-assisted step; no numerics were run.

**Credit.** The statement, the inside proof, the refined-minimiser identity and every input used below are from Ethan Sussman and Levent Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775, cited as CA-I with raw-TeX line numbers. The minimiser, response and averaging theory is Tadeusz Balaban's (CMP 98, 102, 109, 119, 122), cited from the local copies in `~/ym4d-papers`. Prior lanes here: `library/rb.md` (Codex, nine attacks), `library/crca.md`, `library/l16.md`, digest `library/prior/cr-claude.md` (gpt-6.1-sol). Their results are used where named.

## 1. Target, outline check, and what is new

**Target (CR).** CA-I `4.12:prop-reblocking-outside`, CA-I 45085–45106, status **Proof outstanding**. Under the standing hypotheses of `4.12:prop-reblocking-inside` (CA-I 44127–44150), for every consumer $E$ with $X'\cap\mathcal C=\emptyset$, every slot $p$ and every read domain $X''\subset X'$ with $\{c_E<p\}\cap X''\neq\emptyset$, conclusions (a) and (b) of the inside proposition hold, with $K_b=\frac\pi3(d-1)c_Qc_d(1+3L^2)\,204M$. This is equation (20) of `library/rb.md`.

**Outline (lead's rule 10), read here.** CA-I 45108–45159 (route (i) re-block datum lemma; route (ii) tower localisation, with "compatibility ... not proved here"); CA-I 44847–44982, `4.12:rem-refined-minimiser`: the one-step identity $U_E=[e^{i\eta\mathcal H(B_{\rm rb};U_\nu^\tau)}U_\nu^\tau]^\lambda$ is proved there given the composition grant, and the remark states that this route "does not close" because on bonds crossing between adjacent re-blocked blocks the datum is only $O(\ell_p^2)$ times the curvature (CA-I 44899–44932). CA-I 45040–45060: the inside argument stops outside boxes at the axial gauge. So CR is open in the account, and its own proposed one-step route fails at a stated point.

**Prior attacks not repeated.** RB attacks 1–9 (`library/rb.md` §§3–12), MF, ARR, L16 attacks 1–3. All of them either needed one global small gauge, a changed boundary tower, or a path of admitted data. L16 (unchecked) gives a topological obstruction to admitted data paths on a closed torus.

**What is new here.** Re-block **one level at a time on the fixed domain** $X''$, using only the consumer's own determining sets $\mathfrak B^{(q)}:=\mathfrak B_E(q,X'')$, $q=n,\dots,p$. Each step compares two minimisers on the same domain and the same boundary tower. The datum of each step is supported where the coarser minimiser is already sharp, and the crossing-bond defect of the account's remark costs only one factor $L$ per step. No box, no global small gauge, no changed boundary row, and no data path is used. The only "path" is the straight segment inside the analyticity polydisc of Balaban's Proposition 9, which that proposition asserts. A second new point (Lemma 4b) derives the anchored (fixed-frame) form of the interface averages from the account's own hypothesis (d), which has one gauge $u$ for all rows at once.

## 2. Consumer strategy first

`library/crca.md` §2 lists the consumers K2–K4, the four composites and the group-factor clause. Each needs, for every actual pair $(p,X'')$, the regular minimiser and the target radii (R3) of crca, $|\partial U_E-1|\le\vartheta_E\alpha_n\eta^2\ell_n^{-2}$, $|J(U_E)|\le\vartheta_E\alpha_n\ell_n^{-3}L^{(n-p)_+}$. The all-cell bound fails these by the unpaid factor $\alpha_k\ell_p^2/\alpha_n$ at $p=k$ (crca (R4)–(R8)). CR's table implies (R3) (CA-I 44800 and RB (12)).

Decision: prove CR as stated. The proof below gives more: curvature $O(\alpha_k\eta^2)(1+\ell_p\ell_n^{-1})$ and current $O(\alpha_k)(\ell_n^{-1}+\ell_p\ell_n^{-2})$ at every point of $X''^{\sim2}$, with constants fixed before $M$. So no consumer has to change, and the box restriction of the inside proposition is not needed either.

Notation: $\eta=L^{-k}$, $\ell_m=L^{m-k}$, $\alpha_k:=\tilde\alpha_{0,k}$, $G=SU(2)$ (so $\epsilon_G=1$, RB (1)). For $n\le q\le p$ put
$$
\mathfrak B^{(q)}:=\mathfrak B_E(q,X''),\quad D_0^{(q)}:=M_{\mathfrak B^{(q)}}(\bar U),\quad U^{(q)}:=U(\mathfrak B^{(q)},D_0^{(q)}),\quad R_{q+1}:=\bigcup\{\text{level-}(q+1)\text{ blocks of }\mathfrak B^{(q+1)}\}.
$$
So $U^{(p)}=U_E(p,X'')$ is the target, and $U^{(n)}$ is the minimiser at slot $n$.

## 3. Inputs, each with its source and status

Nothing else is used. "Account input" means a statement the account takes by statement or proves; it is cited, not re-derived here.

| Tag | Statement used | Source | Status |
|---|---|---|---|
| T1 | Theorem 1 (i) existence with the all-cell bounds $|\partial U-1|<B_3\varepsilon_1\eta^2\ell_{\mathfrak B}^{-2}$, $|J(U)|<B_3\varepsilon_1\ell_{\mathfrak B}^{-3}$; (ii) uniqueness up to gauge among critical points with $|\partial U-1|<\varepsilon_0\eta^2\ell_{\mathfrak B}^{-2}$ | CA-I 43113–43160 (`4.12:eq-constrained-minimisers-b`), Balaban CMP 102 Thm 1 | account input |
| AV | (c) normalisation, covariance, locality; (d) $M_{\mathfrak B}(e^{i\eta\mathfrak a}1)=(e^{ib})^u$ with **one** gauge $u$ for all rows and $|b(c)|\le c_Q\ell(c)\sup_{{\rm carrier}(c)}|\mathfrak a|$; (e) curvature of averaged data | CA-I 43011–43084; item (v) is stated for every determining set (partition into blocks) on every domain | account inputs |
| P6 | Equal-level rows are anchored: for a row $c$ of level $m$ between two blocks of equal level, $|M(e^{i\eta\mathfrak a}1)(c)-1|\le C_6\ell_m\sup|\mathfrak a|$ when $\sup|\mathfrak a|\le\alpha_1^{(98)}$ (no gauge) | Balaban CMP 98 Prop. 6 with $U_0=1$ (eqs. (158)–(164), p. 43): "$U_k(U_0^k)^{-1}$ is close to 1, the difference ... proportional to $\alpha_1$", with (162)–(163) giving the factor $L^k\eta$; also the outline's Theorem 1a.1.6, $\mathcal M^n(e^{i\eta_kA}U_0)=(e^{i\mathsf a_n}\mathcal M^nU_0)^{v_n}$ with $|\mathsf a_n|\le2L^n\eta_k\sup|A|$, $|v_n-1|\le CL^n\eta_k\sup|A|$ (SA 7265–7283), which at $U_0=1$ gives the same anchored bound | Balaban literal; the account cites this proposition for (d) but drops the anchoring |
| ROW | The averaging functional of a row depends only on its two blocks and their base points | reading of CA-I 43011–43016 ("the averages of CMP 98 (1.5)"); for equal-level rows it is the definition by iteration | reading |
| COMP | Under a refinement on the same domain, the coarse averages are functions of the fine averages | CA-I 44874 ("Grant the composition property of the averages under refinement"), used in the account's Steps one–two, CA-I 44945–44970 | account's grant |
| R | Response at a real minimiser base: for $U_0=U(\mathfrak B,V_0)$ and real $B$ in the polydisc $\sup|B|\le r_P$ of CMP 102 (172), $U(\mathfrak B,e^{iB}V_0)=(e^{i\eta\mathcal H}U_0)^g$ for a gauge $g$, and at every point $y$ of layer $m$: $\ell_m|\mathcal H(y)|,\ \ell_m^2|\nabla^{U_0}\mathcal H(y)|,\ \ell_m^3|D^*_{U_0}D_{U_0}\mathcal H(y)|\le C_H N_B(y)$, $N_B(y):=\sup_c|B(c)|e^{-\delta_H d(y,c)}$ | CA-I 10162–10196, `4.4:not-response-bound`, second case ("real minimiser base ... polydisc (172) ... all five members of (190)"); Balaban CMP 102 Prop. 9, (172), (190); used at a general real base in CA-I 16579–16586 | account input |
| CUR | $J(V)(b)=\eta^{-3}\sum_{p\ni b}\pi\,{\rm Im}\,V(\partial_bp)$, and $J(e^{i\eta A}U_0)=J(U_0)+D^*_{U_0}D_{U_0}A+F(U_0,A)$ with $\ell^3|F(U_0,A)(b)|\le c_F(\mathsf c+\|A\|)\|A\|$ when $|U_0(\partial p)-1|\le\mathsf c\eta^2\ell^{-2}$ on the plaquettes at $b$, $\mathsf c\le1$, $\|A\|:=\max\{\ell|A|,\ell^2|\nabla_{U_0}A|\}\le1$ | CA-I 10306–10373, `4.4:lem-current-remainder` (proved in the account) | account lemma |
| AX | Axial gauge of a box of edges $\le\Delta$: $U^a=e^{i\eta\mathfrak a}1$, $|\mathfrak a|\le\frac\pi3(d-1)\Delta\varphi\eta^{-2}$ when $|\partial U-1|\le\varphi$ and $(d-1)\Delta\varphi/\eta\le1$ | CA-I 43787–43808, `4.12:lem-axial-gauge` (Lie-algebra clause valid for $SU(2)$, RB (1)) | account lemma |
| SEP | Separation of consumer levels: if $c_E(x)=n$ and $c_E\ge m\ge n+2$ on a block $\beta$, then $d(x,\beta)\ge(m-n-1)w$ in the metric of (R) for every $\mathfrak B^{(q)}$, where $w$ is the least width of a region of constant consumer level, in its own units | CA-I 43442–43458, (j), stated "for the consumer geometries inside an admissible box", justified there by the widths of shells and collars in CMP 122a §1, which are not box-specific; finer blocks only lengthen scaled paths | account input, read on $X''$ |
| SRC | $|\partial\bar U(\mathfrak p)-1|<\alpha_k\eta^2$ on every plaquette of $X''$ | CA-I 43297, (admissible-boxes-a), on the part of $Y_4$ where the healed level is $k$; RB §8 | scope condition; needed for (a) by any route |

**Floors and ceilings.** Besides the account's $(\Phi0)$–$(\Phi2)$ and $(\Gamma_0)$–$(\Gamma_3)$ (CA-I 43559–43627), the proof uses two one-sided floors on $M$, fixed after all constants above and before the couplings:
$$
(\Phi_H)\quad 2L\,e^{-\delta_H w}\le1,\qquad\qquad (\Phi_K)\quad C_\star\le \tfrac32L^2B_HK_0M,\quad K_0:=\tfrac\pi3(d-1)c_Qc_d(1+3L^2)\cdot204,
$$
where $w=w(M)$ grows with $M$ (shell width $M$ in own units) and $C_\star$ is the constant of Theorem 8 below, which does not depend on $M$. The coupling ceilings added below are upper bounds on $\alpha_k$ in terms of constants fixed earlier. This keeps the account's order: $L$, then $M_1,\delta,\delta_H$ and the input constants, then $M$, then the couplings.

## 4. Three elementary lemmas

**Lemma 1 (closed paths in a box).** Let $Q$ be a lattice box, $\varphi\ge0$, and $U$ a $G$-valued configuration with $|\partial U(\mathfrak p)-1|\le\varphi$ on every plaquette of $Q$. If $\lambda$ is a closed lattice path of $N$ steps inside $Q$, then $|U(\lambda)-1|\le\frac12N(N-1)\varphi$. If $\lambda_1,\lambda_2$ are paths in $Q$ with the same endpoints and $N_1,N_2$ steps, then $|U(\lambda_1)-U(\lambda_2)|\le\frac12(N_1+N_2)^2\varphi$.

*Proof.* Write $\lambda$ as a word of signed unit steps. Sort it by coordinate index with adjacent transpositions that keep the order of the steps of each coordinate. At most $N(N-1)/2$ transpositions are needed (the number of inversions). After $t$ letters of any intermediate word, the $\mu$-displacement is the sum of the first $r_\mu(t)$ $\mu$-steps of the original word. The original path attains that displacement, so every intermediate path stays in the box $Q$. A transposition of adjacent steps $s,s'$ in different coordinates at a site $y$ replaces $U(s)U(s')$ by $U(s')U(s)$ (transports along the two sides of the plaquette spanned at $y$). By unitarity the transport changes by $|\partial U(\mathfrak p)^{\pm1}-1|\le\varphi$. The sorted word is a concatenation of closed walks on lines. A closed walk on a line has trivial transport, because $U(b)U(\bar b)=1$ and the walk reduces to the empty word by deleting backtracks. This proves the first claim. The second follows from $|U(\lambda_1)-U(\lambda_2)|=|U(\lambda_1\lambda_2^{-1})-1|$. $\square$

**Lemma 2 (plaquette at a perturbed background).** Let $V$ be a configuration, $\mathcal H$ a $\mathfrak g$-valued 1-form, $W:=e^{i\eta\mathcal H}V$, and $\mathfrak p=\mathfrak p(x;\mu,\nu)$. Let $h$ be the largest $|\mathcal H|$ on the four bonds of $\mathfrak p$ and assume $\eta h\le1/16$. Then
$$
|\partial W(\mathfrak p)-1|\le(1+4\eta h)\,|\partial V(\mathfrak p)-1|+2\eta^2|\nabla^V\mathcal H(x)|+12\eta^2h^2 .
$$

*Proof.* Put $V_1=V(x,x+\mu)$, $V_2=V(x+\mu,x+\mu+\nu)$, $V_3=V(x+\nu,x+\mu+\nu)$, $V_4=V(x,x+\nu)$ and $P=\partial V(\mathfrak p)=V_1V_2V_3^{-1}V_4^{-1}$. Moving the exponentials to the left with $Ye^{iX}=e^{i{\rm Ad}_YX}Y$ and $V_1V_2V_3^{-1}=PV_4$ gives
$$
\partial W(\mathfrak p)=e^{i\eta X_1}e^{i\eta X_2}e^{-i\eta X_3}e^{-i\eta X_4}P,\qquad
X_1=\mathcal H_\mu(x),\ X_2={\rm Ad}_{V_1}\mathcal H_\nu(x+\mu),\ X_3={\rm Ad}_P{\rm Ad}_{V_4}\mathcal H_\mu(x+\nu),\ X_4={\rm Ad}_P\mathcal H_\nu(x).
$$
By the definition of $\nabla^V$ (CA-I 42779),
$X_1+X_2-X_3-X_4=\eta[(\nabla^V_\mu\mathcal H_\nu)(x)-(\nabla^V_\nu\mathcal H_\mu)(x)]+(1-{\rm Ad}_P)[\mathcal H_\nu(x)+{\rm Ad}_{V_4}\mathcal H_\mu(x+\nu)]$.
Since $|Y-PYP^{-1}|\le2|P-1||Y|$, this has norm at most $2\eta|\nabla^V\mathcal H(x)|+4h|P-1|$. Each $|X_j|\le h$. Expanding the four exponentials, every term of degree at least two has norm at most $e^{4\eta h}-1-4\eta h\le8\eta^2h^2e^{4\eta h}\le12\eta^2h^2$, as $4\eta h\le1/4$. Hence $|\partial W-P|\le\eta|X_1+X_2-X_3-X_4|+12\eta^2h^2$, and $|\partial W-1|\le|\partial W-P|+|P-1|$. $\square$

**Lemma 3 (axial gauge on two adjacent cubes of consecutive levels).** Let $\Gamma$ be a cube of level $q+1$ and $\gamma$ a cube of level $q$ sharing with $\Gamma$ a face piece in the hyperplane $\{x_\mu=c\}$, $\gamma$ on the $+\mu$ side. Let $U$ satisfy $|\partial U(\mathfrak p)-1|\le F\eta^2$ on all plaquettes with corners in $\Gamma\cup\gamma$, with $d\,\ell_{q+1}F\eta\le1$. Let $\hat z$ be the minimal corner of $\Gamma$, $\gamma_y$ the lexicographic path in $\Gamma$ from $\hat z$ to $y$, and for $y'\in\gamma$ let $y_0(y')$ be the site of $\Gamma$ with $y'-y_0\in\eta\mathbb N e_\mu$. Put $a(y):=U(\gamma_y)$ on $\Gamma$ and $a(y'):=U(\gamma_{y_0}\cdot[y_0\to y'])$ on $\gamma$, with $[y_0\to y']$ the straight segment. Then $U^a=e^{i\eta\mathfrak a}1$ on the bonds of $\Gamma\cup\gamma$ with $|\mathfrak a|\le\frac\pi3 d\,\ell_{q+1}F$.

*Proof.* On bonds of $\Gamma$ this is AX with $\Delta\le\ell_{q+1}$. On a crossing bond $\langle y_0,y_0+\eta e_\mu\rangle$ and on $\mu$-bonds of $\gamma$, the tree path of the endpoint extends that of the initial point by the bond, so $U^a=1$. For a bond $\langle y',y'+\eta e_\nu\rangle$ of $\gamma$ with $\nu\ne\mu$, write $y'=y_0+j\eta e_\mu$, $1\le j\le\ell_q/\eta$. The holonomy $U^a=U(\text{tree}(y')\cdot e_\nu\cdot\text{tree}(y'+\eta e_\nu)^{-1})$ is the product of a conjugate of the axial loop of the bond $\langle y_0,y_0+\eta e_\nu\rangle$ in $\Gamma$ and a conjugate of the ribbon between the two $\mu$-segments. The first has defect at most $(d-1)(\ell_{q+1}/\eta)F\eta^2$ by AX (CA-I 43811–43865); the ribbon is a product of $j\le\ell_q/\eta$ plaquettes. So $|U^a-1|\le[(d-1)\ell_{q+1}+\ell_q]F\eta\le d\ell_{q+1}F\eta\le1$, and the logarithm bound $|\frac1i\log u|\le\frac\pi3|u-1|$ (CA-I 42746) gives the claim. $\square$
