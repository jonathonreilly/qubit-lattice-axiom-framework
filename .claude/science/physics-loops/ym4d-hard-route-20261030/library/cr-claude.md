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

`library/crca.md` §2 lists the consumers K2–K4, the four composites and the group-factor clause. Each needs, for every actual pair $(p,X'')$, the regular minimiser and the target radii (R3) of crca, $|\partial U_E-1|\le\vartheta_E\alpha_n\eta^2\ell_n^{-2}$, $|J(U_E)|\le\vartheta_E\alpha_n\ell_n^{-3}L^{(n-p)_+}$. The all-cell bound fails these by the unpaid factor $\alpha_k\ell_p^2/\alpha_n$ at $p=k$ (crca (R4)–(R8)). CR's table implies (R3) under $(\Gamma_1)$–$(\Gamma_3)$ and the level-$k$ provision (RB (12)).

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
| T1 | Theorem 1 (i) existence with the all-cell bounds $\vert \partial U-1\vert <B_3\varepsilon_1\eta^2\ell_{\mathfrak B}^{-2}$, $\vert J(U)\vert <B_3\varepsilon_1\ell_{\mathfrak B}^{-3}$; (ii) uniqueness up to gauge among critical points with $\vert \partial U-1\vert <\varepsilon_0\eta^2\ell_{\mathfrak B}^{-2}$ | CA-I 43113–43160 (`4.12:eq-constrained-minimisers-b`), Balaban CMP 102 Thm 1 | account input |
| AV | (c) normalisation, covariance, locality; (d) $M_{\mathfrak B}(e^{i\eta\mathfrak a}1)=(e^{ib})^u$ with **one** gauge $u$ for all rows and $\vert b(c)\vert \le c_Q\ell(c)\sup_{{\rm carrier}(c)}\vert \mathfrak a\vert $; (e) curvature of averaged data | CA-I 43011–43084; item (v) is stated for every determining set (partition into blocks) on every domain | account inputs |
| P6 | Equal-level rows are anchored: for a row $c$ of level $m$ between two blocks of equal level, $\vert M(e^{i\eta\mathfrak a}1)(c)-1\vert \le C_6\ell_m\sup\vert \mathfrak a\vert $ when $\sup\vert \mathfrak a\vert \le\alpha_1^{(98)}$ (no gauge) | Balaban CMP 98 Prop. 6 with $U_0=1$ (eqs. (158)–(164), p. 43): "$U_k(U_0^k)^{-1}$ is close to 1, the difference ... proportional to $\alpha_1$", with (162)–(163) giving the factor $L^k\eta$; also the outline's Theorem 1a.1.6, $\mathcal M^n(e^{i\eta_kA}U_0)=(e^{i\mathsf a_n}\mathcal M^nU_0)^{v_n}$ with $\vert \mathsf a_n\vert \le2L^n\eta_k\sup\vert A\vert $, $\vert v_n-1\vert \le CL^n\eta_k\sup\vert A\vert $ (SA 7265–7283), which at $U_0=1$ gives the same anchored bound | Balaban literal; the account cites this proposition for (d) but drops the anchoring |
| ROW | The averaging functional of a row depends only on its two blocks and their base points | reading of CA-I 43011–43016 ("the averages of CMP 98 (1.5)"); for equal-level rows it is the definition by iteration | reading |
| COMP | Under a refinement on the same domain, the coarse averages are functions of the fine averages | CA-I 44874 ("Grant the composition property of the averages under refinement"), used in the account's Steps one–two, CA-I 44940–44968 | account's grant |
| R | Response at a real minimiser base: for $U_0=U(\mathfrak B,V_0)$ and real $B$ in the polydisc $\sup\vert B\vert \le r_P$ of CMP 102 (172), $U(\mathfrak B,e^{iB}V_0)=(e^{i\eta\mathcal H}U_0)^g$ for a gauge $g$, and at every point $y$ of layer $m$: $\ell_m\vert \mathcal H(y)\vert ,\ \ell_m^2\vert \nabla^{U_0}\mathcal H(y)\vert ,\ \ell_m^3\vert D^*_{U_0}D_{U_0}\mathcal H(y)\vert \le C_H N_B(y)$, $N_B(y):=\sup_c\vert B(c)\vert e^{-\delta_H d(y,c)}$ | CA-I 10162–10196, `4.4:not-response-bound`, second case ("real minimiser base ... polydisc (172) ... all five members of (190)"); Balaban CMP 102 Prop. 9, (172), (190); used at a general real base in CA-I 16579–16586 | account input |
| CUR | $J(V)(b)=\eta^{-3}\sum_{p\ni b}\pi\,{\rm Im}\,V(\partial_bp)$, and $J(e^{i\eta A}U_0)=J(U_0)+D^*_{U_0}D_{U_0}A+F(U_0,A)$ with $\ell^3\vert F(U_0,A)(b)\vert \le c_F(\mathsf c+\Vert A\Vert )\Vert A\Vert $ when $\vert U_0(\partial p)-1\vert \le\mathsf c\eta^2\ell^{-2}$ on the plaquettes at $b$, $\mathsf c\le1$, $\Vert A\Vert :=\max\{\ell\vert A\vert ,\ell^2\vert \nabla_{U_0}A\vert \}\le1$ | CA-I 10306–10373, `4.4:lem-current-remainder` (proved in the account) | account lemma |
| AX | Axial gauge of a box of edges $\le\Delta$: $U^a=e^{i\eta\mathfrak a}1$, $\vert \mathfrak a\vert \le\frac\pi3(d-1)\Delta\varphi\eta^{-2}$ when $\vert \partial U-1\vert \le\varphi$ and $(d-1)\Delta\varphi/\eta\le1$ | CA-I 43787–43808, `4.12:lem-axial-gauge` (Lie-algebra clause valid for $SU(2)$, RB (1)) | account lemma |
| SEP | Separation of consumer levels: if $c_E(x)=n$ and $c_E\ge m\ge n+2$ on a block $\beta$, then $d(x,\beta)\ge(m-n-1)w$ in the metric of (R) for every $\mathfrak B^{(q)}$, where $w$ is the least width of a region of constant consumer level, in its own units | CA-I 43442–43458, (j), stated "for the consumer geometries inside an admissible box", justified there by the widths of shells and collars in CMP 122a §1, which are not box-specific; finer blocks only lengthen scaled paths | account input, read on $X''$ |
| SRC | $\vert \partial\bar U(\mathfrak p)-1\vert <\alpha_k\eta^2$ on every plaquette of $X''$ | CA-I 43297, (admissible-boxes-a), on the part of $Y_4$ where the healed level is $k$; RB §8 | scope condition; needed for (a) by any route |

**Floors and ceilings.** Besides the account's $(\Phi0)$–$(\Phi2)$ and $(\Gamma_0)$–$(\Gamma_3)$ (CA-I 43559–43627), the proof uses two one-sided floors on $M$, fixed after all constants above and before the couplings:
$$
(\Phi_H)\quad 2L\,e^{-\delta_H w}\le1,\qquad\qquad (\Phi_K)\quad C_\star\le 3L^2B_HK_0M,\quad K_0:=\tfrac\pi3(d-1)c_Qc_d(1+3L^2)\cdot204,
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

**Lemma 3 (axial gauge on two adjacent cubes of consecutive levels).** Let $\Gamma$ be a cube of level $q+1$ and $\gamma$ a cube of level $q$ sharing with $\Gamma$ a face piece in the hyperplane $\{x_\mu=c\}$, $\gamma$ on the $+\mu$ side (the $-\mu$ side is the same with $-e_\mu$). Let $U$ satisfy $|\partial U(\mathfrak p)-1|\le F\eta^2$ on all plaquettes with corners in $\Gamma\cup\gamma$, with $d\,\ell_{q+1}F\eta\le1$. Let $\hat z$ be the minimal corner of $\Gamma$, $\gamma_y$ the lexicographic path in $\Gamma$ from $\hat z$ to $y$, and for $y'\in\gamma$ let $y_0(y')$ be the site of $\Gamma$ with $y'-y_0\in\eta\mathbb N e_\mu$. Put $a(y):=U(\gamma_y)$ on $\Gamma$ and $a(y'):=U(\gamma_{y_0}\cdot[y_0\to y'])$ on $\gamma$, with $[y_0\to y']$ the straight segment. Then $U^a=e^{i\eta\mathfrak a}1$ on the bonds of $\Gamma\cup\gamma$ with $|\mathfrak a|\le\frac\pi3 d\,\ell_{q+1}F$.

*Proof.* On bonds of $\Gamma$ this is AX with $\Delta\le\ell_{q+1}$. On a crossing bond $\langle y_0,y_0+\eta e_\mu\rangle$ and on $\mu$-bonds of $\gamma$, the tree path of the endpoint extends that of the initial point by the bond, so $U^a=1$. For a bond $\langle y',y'+\eta e_\nu\rangle$ of $\gamma$ with $\nu\ne\mu$, write $y'=y_0+j\eta e_\mu$, $1\le j\le\ell_q/\eta$. The holonomy $U^a=U(\text{tree}(y')\cdot e_\nu\cdot\text{tree}(y'+\eta e_\nu)^{-1})$ is the product of a conjugate of the axial loop of the bond $\langle y_0,y_0+\eta e_\nu\rangle$ in $\Gamma$ and a conjugate of the ribbon between the two $\mu$-segments. The first has defect at most $(d-1)(\ell_{q+1}/\eta)F\eta^2$ by AX (CA-I 43811–43865); the ribbon is a product of $j\le\ell_q/\eta$ plaquettes. So $|U^a-1|\le[(d-1)\ell_{q+1}+\ell_q]F\eta\le d\ell_{q+1}F\eta\le1$, and the logarithm bound $|\frac1i\log u|\le\frac\pi3|u-1|$ (CA-I 42746) gives the claim. $\square$

## 5. Rows read in fixed frames

The account's (d) holds only "modulo a gauge $u$". The step below needs data compared in the original endpoint frames. P6 gives this for rows of equal level. For rows between blocks of different levels it follows from (d) itself, because (d) has one gauge $u$ for all rows at once.

**Lemma 4 (anchored rows).** Let $c=\langle z,z'\rangle$ be a row of a determining set, with carrier $K=B(z)\cup B(z')$, and let $|\partial U(\mathfrak p)-1|\le F\eta^2$ on all plaquettes with corners in $K$.

(a) If $c$ joins two blocks of level $m$, let $\hat z$ be the minimal corner of the box $K$, $\gamma_y$ the lexicographic path in $K$ from $\hat z$ to $y$, and $\rho_c:=\gamma_z^{-1}\gamma_{z'}$. If $\frac{2\pi}3(d-1)\ell_mF\le\alpha_1^{(98)}$ and $2(d-1)\ell_mF\eta\le1$, then
$$|M(U)(c)-U(\rho_c)|\le C_a\ell_m^2F,\qquad C_a:=\tfrac{2\pi}3(d-1)C_6 .$$

(b) If $c=\langle z_\Gamma,z_\gamma\rangle$ with $\Gamma,\gamma$ as in Lemma 3, let $w$ be the site of $\Gamma$ on the $\mu$-line through $z_\gamma$ next to the shared face, and $\rho_c:=\gamma_{z_\Gamma}^{-1}\gamma_w[w\to z_\gamma]$ (lexicographic paths of $\Gamma$). If $\frac\pi3d\ell_{q+1}F\le\min(\alpha_1^{(98)},c_{\rm av})$ and $d\ell_{q+1}F\eta\le1$, then
$$|M(U)(c)-U(\rho_c)|\le C_b\ell_{q+1}^2F,\qquad C_b:=\tfrac\pi3d\,(2C_6+3c_Q).$$

*Proof.* (a) AX on $K$ (edges $\le2\ell_m$) gives $a$ with $a(y)=U(\gamma_y)$ and $U^a=e^{i\eta\mathfrak a}1$ on $K$, $|\mathfrak a|\le\frac{2\pi}3(d-1)\ell_mF$. Extend $a$ by $1$ and $\mathfrak a$ by $0$ off $K$. By covariance, $M(U^a)(c)=a(z)M(U)(c)a(z')^{-1}$; by locality $M(U^a)(c)=M(e^{i\eta\mathfrak a}1)(c)$. Hence
$M(U)(c)=U(\gamma_z)^{-1}M(e^{i\eta\mathfrak a}1)(c)U(\gamma_{z'})$, and unitarity gives $|M(U)(c)-U(\rho_c)|=|M(e^{i\eta\mathfrak a}1)(c)-1|\le C_6\ell_m\sup|\mathfrak a|$ by P6.

(b) The same reduction with the gauge of Lemma 3, where $a(z_\Gamma)=U(\gamma_{z_\Gamma})$ and $a(z_\gamma)=U(\gamma_w[w\to z_\gamma])$, gives $|M(U)(c)-U(\rho_c)|=|M(e^{i\eta\mathfrak a'}1)(c)-1|$. Here $\mathfrak a'$ is $\mathfrak a$ on the bonds of $\Gamma\cup\gamma$ and $0$ elsewhere, and $A:=\sup|\mathfrak a'|\le\frac\pi3d\ell_{q+1}F$. By ROW we may compute this datum in any determining set that contains the blocks $\Gamma,\gamma$ with these base points. Fix $\nu\ne\mu$ and put $\Gamma':=\Gamma+\ell_{q+1}e_\nu$ and $\gamma_j:=\gamma+j\ell_qe_\nu$, $0\le j\le L$. If $\gamma$ is the $i$-th level-$q$ cell of the face of $\Gamma$ in the $\nu$-direction ($0\le i\le L-1$), then $\gamma_j$ is a cell of the face of $\Gamma$ if $i+j\le L-1$ and of $\Gamma'$ if $i+j\ge L$. So $\mathfrak B_{\rm loc}:=\{\Gamma,\Gamma',\gamma_0,\dots,\gamma_L\}$, with the given base points for $\Gamma,\gamma$ and any base points for the others, is a determining set on the union of these blocks; meeting blocks differ by one level. Its rows include $\langle\Gamma,\Gamma'\rangle$, $\langle\gamma_j,\gamma_{j+1}\rangle$, $\langle\Gamma',\gamma_L\rangle$ and $c=\langle\Gamma,\gamma_0\rangle$.

Apply (d) to $e^{i\eta\mathfrak a'}1$: $M_{\mathfrak B_{\rm loc}}(e^{i\eta\mathfrak a'}1)=(e^{ib})^u$ with $|b(c')|\le c_Q\ell(c')\sup_{{\rm carrier}(c')}|\mathfrak a'|$. If neither block of $c'$ is $\Gamma$ or $\gamma$, then $\mathfrak a'=0$ on the carrier of $c'$, so $M(e^{i\eta\mathfrak a'}1)(c')=M(1)(c')=1$ by locality and normalisation, and $b(c')=0$. Then $u$ takes one value at the two ends of $c'$. The rows $\langle\gamma_j,\gamma_{j+1}\rangle$ ($1\le j<L$) and $\langle\Gamma',\gamma_L\rangle$ are of this kind. So $u=u_0$ at $z_{\Gamma'}$ and at every $z_{\gamma_j}$, $j\ge1$.

By P6, $X_1:=M(e^{i\eta\mathfrak a'}1)(\langle\Gamma,\Gamma'\rangle)$ and $X_2:=M(e^{i\eta\mathfrak a'}1)(\langle\gamma,\gamma_1\rangle)$ satisfy $|X_1-1|\le C_6\ell_{q+1}A$ and $|X_2-1|\le C_6\ell_qA$. By (d), $X_1=u(z_\Gamma)e^{ib_1}u_0^{-1}$ and $X_2=u(z_\gamma)e^{ib_2}u_0^{-1}$. Hence
$$M(e^{i\eta\mathfrak a'}1)(c)=u(z_\Gamma)e^{ib_c}u(z_\gamma)^{-1}=X_1u_0e^{-ib_1}e^{ib_c}e^{ib_2}u_0^{-1}X_2^{-1}.$$
For unitary factors $|g_1\cdots g_5-1|\le\sum|g_j-1|$, and $|e^{iY}-1|\le|Y|$ for hermitian $Y$. So $|M(e^{i\eta\mathfrak a'}1)(c)-1|\le(2C_6+3c_Q)\ell_{q+1}A$. $\square$

The reduction uses only identity-based configurations on an auxiliary set of blocks, so nothing outside $\Gamma\cup\gamma$ is assumed about $U$. Lemma 4(b) is the anchored form of the account's interface averaging hypothesis. It is derived, not assumed.

## 6. One level of re-blocking: the relative datum

Fix $n\le q<p$ and write $R:=R_{q+1}$. Off $R$ the sets $\mathfrak B^{(q)}$ and $\mathfrak B^{(q+1)}$ coincide, because their levels $\min(q,c_E,t_{X''})$ and $\min(q+1,c_E,t_{X''})$ differ only where $\min(c_E,t_{X''})\ge q+1$. Each level-$(q+1)$ block $\Gamma\subset R$ is the union of $L^d$ level-$q$ blocks of $\mathfrak B^{(q)}$. Let $\mathcal C$ be the set of blocks of $\mathfrak B^{(q+1)}$ adjacent to $R$ and not in $R$, and $N:=R\cup\bigcup\mathcal C$.

*Geometry.* A block of $\mathcal C$ meets a level-$(q+1)$ block and is not of level $q+1$; levels of meeting blocks differ by at most one. So it has level $q$ in both sets. A block of $\mathfrak B^{(q)}$ adjacent to a level-$q$ block $\beta\subset\Gamma\subset R$ lies in $R$ or is a block of $\mathcal C$ (it is adjacent to $\Gamma$ and coincides off $R$ with a block of $\mathfrak B^{(q+1)}$). Hence every row of $\mathfrak B^{(q)}$ that touches $R$ joins two blocks of level $q$ inside $N$. On every site of a block of $N$, $c_E\ge q$: on $R$, $\min(c_E,t)\ge q+1$; on $\mathcal C$, $\min(q+1,c_E,t)=q$.

*Curvature on $N$.* Put $U_1:=U^{(q+1)}$, $U_2:=\bar U$ and $F:=(2B_3L^4+1)\alpha_k=:C_F\alpha_k$. By SRC, $|\partial U_2-1|<\alpha_k\eta^2$. By (e) and SRC, $|\partial D_0^{(q+1)}(P)-1|\le2\alpha_k\ell(P)^2\le2\alpha_k\ell_{q+1}^2$; with $(\Gamma_0)$(i)–(ii), T1(i) applies with $\varepsilon_1=2\alpha_k\ell_{q+1}^2$. For a plaquette with corners in $N$, every block meeting $\mathfrak p^+$ is in $N$ or adjacent to a block of $\mathcal C$, so it has level at least $q-1$ and $\ell_{\mathfrak B^{(q+1)}}(\mathfrak p)\ge\ell_{q-1}$. Hence $|\partial U_1(\mathfrak p)-1|<2B_3\alpha_k\ell_{q+1}^2\eta^2\ell_{q-1}^{-2}=2B_3L^4\alpha_k\eta^2$. Both $U_r$ satisfy the hypothesis of Lemmas 3–4 on $N$ with this $F$. This is where one level at a time matters: on the re-blocked region the coarser minimiser has the sharp bound, because its blocks there have the top level of its own set.

**Lemma 5 (relative datum of one level).** Put $D_W:=M_{\mathfrak B^{(q)}}(U^{(q+1)})$ and $D_0:=D_0^{(q)}$. Under the smallness conditions of Lemma 4 for this $F$, and $C_5\ell_{q+1}^2F\le1$, there are a gauge $v$ on the base points of $\mathfrak B^{(q)}$ and a $\mathfrak g$-valued $B$ on its rows with
$$D_W=(e^{iB}D_0)^v,\qquad B(c)=0\ \text{unless $c$ touches $R$},\qquad |B(c)|\le C_{\rm RD}F\ell_{q+1}^2,$$
where $C_5:=143d^2+4C_a+2C_b$ and $C_{\rm RD}:=\frac\pi3C_5$.

*Proof.* For a base point $z=z_\beta$ of a block $\beta\subset\Gamma\subset R$, let $\pi_z:=\gamma_{z_\beta}^{-1}\gamma_{z_\Gamma}$ (lexicographic paths of $\Gamma$; at most $2d\ell_{q+1}/\eta$ steps). For other base points let $\pi_z$ be the empty path. Put $v(z):=U_1(\pi_z)U_2(\pi_z)^{-1}$ and, for a row $c=\langle z,z'\rangle$,
$$T_r(c):=U_r(\pi_z)^{-1}\,M_{\mathfrak B^{(q)}}(U_r)(c)\,U_r(\pi_{z'}),\qquad B(c):={\rm Ad}_{U_2(\pi_z)}\tfrac1i\log\bigl(T_1(c)T_2(c)^{-1}\bigr).$$
Direct substitution gives $v(z)e^{iB(c)}D_0(c)v(z')^{-1}=U_1(\pi_z)T_1(c)U_1(\pi_{z'})^{-1}=D_W(c)$. Also $|B(c)|\le\frac\pi3|T_1(c)-T_2(c)|$ when the right side is at most $\frac\pi3$, by CA-I 42743; for $SU(2)$ the logarithm is in $\mathfrak g$.

*Rows not touching $R$.* Both blocks lie off $R$, so they are blocks of $\mathfrak B^{(q+1)}$, and the paths are empty. By ROW, $M_{\mathfrak B^{(q)}}(U_r)(c)=M_{\mathfrak B^{(q+1)}}(U_r)(c)$, and $U_1\in C(\mathfrak B^{(q+1)},D_0^{(q+1)})$ makes the two equal. So $T_1=T_2$ and $B(c)=0$.

*Rows touching $R$.* Let $\gamma_c:=\pi_z^{-1}\rho_c\pi_{z'}$, with $\rho_c$ the path of Lemma 4(a) for the level-$q$ row $c$ (at most $4d\ell_q/\eta$ steps). Lemma 4(a) gives $|T_r(c)-U_r(\gamma_c)|\le C_a\ell_q^2F$. It remains to bound $|U_1(\gamma_c)-U_2(\gamma_c)|$. Use $L\ge15$, so $4\ell_q\le\ell_{q+1}$.

- Both blocks in one $\Gamma$: $\gamma_c$ is a closed path in the box $\Gamma$ with at most $5d\ell_{q+1}/\eta$ steps. Lemma 1 gives $|U_r(\gamma_c)-1|\le\frac{25}2d^2\ell_{q+1}^2F$, so the difference is at most $25d^2\ell_{q+1}^2F$.
- Blocks in adjacent $\Gamma\ne\Gamma'$: $\gamma_c$ and the path $\rho_{\Gamma\Gamma'}$ of Lemma 4(a) for the level-$(q+1)$ row $\langle\Gamma,\Gamma'\rangle$ both join $z_\Gamma$ to $z_{\Gamma'}$ in the box $\Gamma\cup\Gamma'$, with at most $9d\ell_{q+1}/\eta$ steps together. Lemma 1 gives $|U_r(\gamma_c)-U_r(\rho_{\Gamma\Gamma'})|\le\frac{81}2d^2\ell_{q+1}^2F$. The coarse data of $U_1,U_2$ on $\langle\Gamma,\Gamma'\rangle$ are equal, so Lemma 4(a) gives $|U_1(\rho_{\Gamma\Gamma'})-U_2(\rho_{\Gamma\Gamma'})|\le2C_a\ell_{q+1}^2F$.
- $\beta\subset\Gamma$ and $\gamma\in\mathcal C$: $\langle\Gamma,\gamma\rangle$ is a row of $\mathfrak B^{(q+1)}$ with equal coarse data. Let $\rho_{\Gamma\gamma}$ be its path from Lemma 4(b). The loop $\gamma_c\rho_{\Gamma\gamma}^{-1}$ is $\pi_{z_\beta}^{-1}\cdot(\rho_c[z_\gamma\to w])\cdot(\gamma_w^{-1}\gamma_{z_\Gamma})$. The site $w$ lies in $\beta$, the level-$q$ cube of $\Gamma$ across the face from $\gamma$; let $\sigma$ be a coordinate path in $\beta$ from $z_\beta$ to $w$ (at most $d\ell_q/\eta$ steps). In the box $\beta\cup\gamma$, Lemma 1 compares $\rho_c[z_\gamma\to w]$ with $\sigma$ (at most $6d\ell_q/\eta$ steps together) at cost $18d^2\ell_q^2F$. The remaining loop $\pi_{z_\beta}^{-1}\sigma\gamma_w^{-1}\gamma_{z_\Gamma}$ lies in the box $\Gamma$ and costs at most $\frac{25}2d^2\ell_{q+1}^2F$. With Lemma 4(b) for $r=1,2$, $|U_1(\gamma_c)-U_2(\gamma_c)|\le(62d^2+2C_b)\ell_{q+1}^2F$.

In all cases $|T_1(c)-T_2(c)|\le C_5\ell_{q+1}^2F$. $\square$

The account's remark (CA-I 44916–44922) found a crossing-bond datum of order $\ell_p^2$ against a needed $\ell_i\ell_p$. Here a crossing defect is $O(\ell_{q+1}^2)=O(L\,\ell_q\ell_{q+1})$: one factor $L$, because each step re-blocks one level only.

## 7. The nesting step and the response step

**Lemma 6 (the coarser minimiser solves the finer problem).** Let $n_P(d,L)$ bound the number of rows of an elementary circuit of $\mathbb L(\mathfrak B^{(q)})$; it is finite because such circuits are local and meeting blocks differ by one level. Put $\varepsilon_1':=(2+n_PC_{\rm RD}C_FL^2)\alpha_k\ell_q^2$ and assume $\varepsilon_1'\le a_1$, $B_3\varepsilon_1'\le\varepsilon_0$. Then $U^{(q+1)}=U(\mathfrak B^{(q)},D_W)^\tau$ for a gauge $\tau$.

*Proof.* This is the account's Steps one–two (CA-I 44940–44968), with $(\mathfrak B_\nu,\mathfrak B)$ replaced by $(\mathfrak B^{(q+1)},\mathfrak B^{(q)})$. $U^{(q+1)}\in C(\mathfrak B^{(q)},D_W)$ by definition. By COMP, every $U\in C(\mathfrak B^{(q)},D_W)$ has $M_{\mathfrak B^{(q+1)}}(U)=M_{\mathfrak B^{(q+1)}}(U^{(q+1)})=D_0^{(q+1)}$. So $C(\mathfrak B^{(q)},D_W)\subset C(\mathfrak B^{(q+1)},D_0^{(q+1)})$, and $U^{(q+1)}$ is critical on the smaller set. The refinement gives $\ell_{\mathfrak B^{(q)}}\le\ell_{\mathfrak B^{(q+1)}}$, so $|\partial U^{(q+1)}-1|<2B_3\alpha_k\ell_{q+1}^2\eta^2\ell_{\mathfrak B^{(q+1)}}^{-2}\le\varepsilon_0\eta^2\ell_{\mathfrak B^{(q)}}^{-2}$ by $(\Gamma_0)$(ii). The datum $D_W$ satisfies the data condition of T1 (CA-I 43116–43119) with $\varepsilon_1'$: by Lemma 5, $\partial D_W(P)$ is conjugate to $\partial(e^{iB}D_0)(P)$, whose distance from $1$ is at most $|\partial D_0(P)-1|+n_P\sup|B|\le2\alpha_k\ell_q^2+n_PC_{\rm RD}F\ell_{q+1}^2$. T1(ii) gives the claim. $\square$

**Lemma 7 (one response step).** Let $\xi\subset X''^{\sim2}$ be a plaquette or bond at $x$, $n:=n_E(\xi)<p$, $n\le q<p$, and let $\sup|B|\le r_P$ (the polydisc of R). Then $U^{(q+1)}$ is gauge equivalent to $e^{i\eta\mathcal H_q}U^{(q)}$, and on the bonds and sites of $\xi^+$
$$|\mathcal H_q|\le\frac{LC_H'}{\ell_n}N_q,\quad |\nabla^{U^{(q)}}\mathcal H_q|\le\frac{L^2C_H'}{\ell_n^2}N_q,\quad |D^*_{U^{(q)}}D_{U^{(q)}}\mathcal H_q|\le\frac{L^3C_H'}{\ell_n^3}N_q,\qquad N_q:=C_{\rm RD}F\ell_{q+1}^2e^{-\delta_H(q-n-1)_+w},$$
with $C_H':=C_He^{\delta_Hc_{\rm st}}$ and $c_{\rm st}$ the largest distance, in the metric of R, between sites at lattice distance at most $3\eta$ (this also absorbs the choice of reference point of a row in $d(y,c)$).

*Proof.* By Lemmas 5 and 6, $U^{(q+1)}\simeq U(\mathfrak B^{(q)},(e^{iB}D_0)^v)$. Covariance of the averages and T1(ii) give $U(\mathfrak B,D^v)\simeq U(\mathfrak B,D)$. Indeed, for an extension $\tilde v$ of $v$, $U(\mathfrak B,D)^{\tilde v}$ is critical and regular in $C(\mathfrak B,D^v)$. R at the real minimiser base $U^{(q)}=U(\mathfrak B^{(q)},D_0)$ then gives $U(\mathfrak B^{(q)},e^{iB}D_0)\simeq e^{i\eta\mathcal H_q}U^{(q)}$, with the three bounds $\le C_HN_B(y)$ times $\ell_m^{-1},\ell_m^{-2},\ell_m^{-3}$ at a point $y$ of layer $m$. On $\xi^+$ every block has level at least $\min(q,n)-1=n-1$ (CA-I 44271–44303), so $\ell_m\ge\ell_n/L$. Let $y^*$ be a site of $\xi$ with $c_E(y^*)=n$. For $y\in\xi^+$, $N_B(y)\le e^{\delta_Hc_{\rm st}}\sup_c|B(c)|e^{-\delta_Hd(y^*,c)}$. By Lemma 5 only rows touching $R$ count. The nearer block of such a row has $c_E\ge q$ on all its sites (§6), so SEP gives $d(y^*,c)\ge(q-n-1)w$ when $q\ge n+2$. With $|B|\le C_{\rm RD}F\ell_{q+1}^2$ this is the claim. $\square$

## 8. The ladder: proof of CR

**Coupling ceilings (8.1).** Besides $(\Gamma_0)$, require, with $F=C_F\alpha_k$ and $\ell\le1$:
$\frac{2\pi}3dF\le\min(\alpha_1^{(98)},c_{\rm av})$ and $dF\le1$ (Lemma 4); $C_5F\le1$ and $C_{\rm RD}F\le r_P$ (Lemma 5, R); $(2+n_PC_{\rm RD}C_FL^2)\alpha_k\le\min(a_1,\varepsilon_0/B_3)$ (Lemma 6); $80L^3C_H'C_{\rm RD}F\le1$, which gives $\eta h_q\le1/16$ in Lemma 2 and $e^{4LC_H'S}\le2$ below; $300L^6C_H'^2C_{\rm RD}^2C_F^2\alpha_k\le1$; $2B_3L^4\alpha_k\le1$; $c_F(2B_3L^4\alpha_k+C_H'C_{\rm RD}F)\le1$ and $C_H'C_{\rm RD}F\le1$ (CUR). Each is an upper bound on $\alpha_k$ by constants fixed before the couplings.

**Theorem 8 (CR).** Let $G=SU(2)$. Assume the inputs of §3, $(\Phi0)$–$(\Phi2)$, $(\Gamma_0)$, $(\Phi_H)$ and (8.1). Let $E$ be a consumer with $X'\cap\mathcal C=\emptyset$; no box is assumed. Let $p$ be a slot level, $X''\subset X'$ a read domain, and assume each level $q\le p$ is a slot level of $E$, so that every $\mathfrak B^{(q)}$ is a consumer determining set on $X''$ with the tower $t_{X''}$. Then:

(a) $U_E(p,X'')$ exists by T1 with $\varepsilon_1=2\alpha_k\ell_p^2$.

(b) Let $\xi\subset X''^{\sim2}$, $n:=n_E(\xi)$. If $n\ge p$, the first line of (b) of the inside proposition holds. If $n<p$, then for a plaquette $\mathfrak p=\xi$ and a bond $\mathfrak b=\xi$ respectively
$$
|\partial U_E(\mathfrak p)-1|\le2\bigl[2B_3L^2+1+10L^4C_H'C_{\rm RD}C_F\,\ell_p\ell_n^{-1}\bigr]\alpha_k\eta^2,\qquad
|J(U_E)(\mathfrak b)|\le\bigl[2B_3L^3\ell_n^{-1}+10L^5C_H'C_{\rm RD}C_F\,\ell_p\ell_n^{-2}\bigr]\alpha_k .
$$
With $C_{\rm curv}:=2(2B_3L+1+10L^4C_H'C_{\rm RD}C_F)$, $C_{\rm curr}:=2B_3L^2+10L^5C_H'C_{\rm RD}C_F$ and $C_\star:=\max(C_{\rm curv},C_{\rm curr}/L)$, the floor $(\Phi_K)$ gives the two below-slot bounds of CR, $3L^2B_HK_b\alpha_k\eta^2\ell_n^{-1}$ and $3L^3B_HK_b\alpha_k\ell_n^{-2}$, with $K_b=K_0M$ as in the statement.

*Proof.* (a) and the case $n\ge p$ are the inside argument of CA-I 44226–44303 verbatim. It uses only SRC on the plaquettes of $X''$, (e), T1 and the two-layer interior, and no box (RB §8).

Let $n<p$. Then $n\le k-1$, so $\ell_n^{-1}\ge L$.

*Base.* $U^{(n)}$ exists by T1 with $\varepsilon_1=2\alpha_k\ell_n^2$. On $\xi^+$ every block of $\mathfrak B^{(n)}$ has level at least $n-1$ (CA-I 44271–44303 with slot $n$). So $\Theta_n:=|\partial U^{(n)}(\mathfrak p)-1|<2B_3L^2\alpha_k\eta^2$ and $J_n:=|J(U^{(n)})(\mathfrak b)|<2B_3L^3\alpha_k\ell_n^{-1}$.

*Steps.* For $q=n,\dots,p-1$, Lemma 7 gives $U^{(q+1)}\simeq e^{i\eta\mathcal H_q}U^{(q)}$ with the stated bounds. Plaquette variables and $|J|$ are gauge invariant (CA-I 42767–42768; J1, CA-I 42794).

*Sum of the step sizes.* Write $j=q-n$ and $J'=p-n-1$. Then $\ell_{q+1}^2=L^{2j+2}\ell_n^2$, and $(\Phi_H)$ gives $e^{-\delta_H(j-1)_+w}\le(2L)^{-(j-1)_+}$. So
$$
S:=\sum_{q=n}^{p-1}N_q\le C_{\rm RD}F\ell_n^2\Bigl[L^2+L^4+\sum_{j=2}^{J'}L^{j+3}2^{1-j}\Bigr]\le5L^{J'+3}C_{\rm RD}F\ell_n^2=5L^2C_{\rm RD}F\,\ell_n\ell_p ,
$$
using $\sum_{j=2}^{J'}L^{j+3}2^{1-j}\le2L^3(L/2)^{J'}(1-2/L)^{-1}\le3L^{J'+3}$ for $L\ge15$, and $L^{J'+3}\ell_n^2=L^2\ell_n\ell_p$.

*Curvature.* Lemma 2 with $V=U^{(q)}$ and $\mathcal H=\mathcal H_q$ gives $\Theta_{q+1}\le(1+4\eta h_q)\Theta_q+2\eta^2|\nabla^{U^{(q)}}\mathcal H_q(x)|+12\eta^2h_q^2$, with $h_q\le LC_H'N_q/\ell_n$ and $|\nabla\mathcal H_q(x)|\le L^2C_H'N_q/\ell_n^2$. Since $\eta\le\ell_n$, iteration gives
$$
\Theta_p\le e^{4LC_H'S}\Bigl[\Theta_n+\frac{2\eta^2L^2C_H'S}{\ell_n^2}+\frac{12\eta^2L^2C_H'^2S^2}{\ell_n^2}\Bigr].
$$
By (8.1), $e^{4LC_H'S}\le2$ and the last term is at most $300L^6C_H'^2C_{\rm RD}^2C_F^2\alpha_k^2\eta^2\le\alpha_k\eta^2$. The middle term is $10L^4C_H'C_{\rm RD}C_F\alpha_k\eta^2\ell_p\ell_n^{-1}$. This is the first bound. For the CR form, $2B_3L^2+1\le(2B_3L+1)\ell_n^{-1}$ and $\ell_p\le1$.

*Current.* Apply CUR with $U_0=U^{(q)}$, $A=\mathcal H_q$, $\xi\to\eta$ and $\ell:=\ell_n/L$. Every site of $\mathfrak p^+$, for a plaquette $\mathfrak p\ni\mathfrak b$, is at most three lattice steps from the site $y^*$ of $\mathfrak b$ with $c_E(y^*)=n$, whose block has level $n$. A lattice step between two blocks crosses a shared face piece, so their levels differ by at most one. Hence every block meeting $\mathfrak p^+$ has side at least $\max(\eta,\ell_{n-3})\ge\ell_n/L^3$. The all-cell bound then gives $|U^{(q)}(\partial\mathfrak p)-1|\le\mathsf c\,\eta^2\ell^{-2}$ with $\mathsf c=2B_3L^4\alpha_k\ell_q^2\le1$. Lemma 7 gives $\|\mathcal H_q\|\le C_H'N_q\le1$ and $\ell^3|D^*D\mathcal H_q(\mathfrak b)|\le C_H'N_q$. Hence $|J_{q+1}-J_q|\le[1+c_F(\mathsf c+C_H'N_q)]C_H'N_q\ell^{-3}\le2L^3C_H'N_q\ell_n^{-3}$. Summing, $J_p\le J_n+2L^3C_H'S\ell_n^{-3}$, which is the second bound. For the CR form, $\ell_n^{-1}\le L^{-1}\ell_n^{-2}$. $\square$

**Corollary 9 (unit-scale form).** If $(\Phi_H)$ is strengthened to $2L^2e^{-\delta_Hw}\le1$, another floor on $M$ of the same kind, the same proof gives $S\le3L^4C_{\rm RD}F\ell_n^2$. Then, for $n<p$,
$$|\partial U_E(\mathfrak p)-1|\le2\bigl[2B_3L^2+1+6L^6C_H'C_{\rm RD}C_F\bigr]\alpha_k\eta^2,\qquad |J(U_E)(\mathfrak b)|\le\bigl[2B_3L^3+6L^7C_H'C_{\rm RD}C_F\bigr]\alpha_k\ell_n^{-1}.$$
These are the unit-scale bounds the inside remark attributes to $\bar U$ (CA-I 44889–44891). They imply CR with a spare factor $\ell_n$ in each bound, and the consumer radii (R3) of `library/crca.md` with ratio at most $C(1+\beta_0)(1+k-n)^{1/2}L^{-(k-n)}/\vartheta_E$.

*Proof.* With $e^{-\delta_Hw}\le(2L^2)^{-1}$, the $j$-th term is at most $\ell_n^2L^42^{1-j}$ for $j\ge2$, so $S\le C_{\rm RD}F\ell_n^2(L^2+2L^4)\le3L^4C_{\rm RD}F\ell_n^2$. Insert this in the last two paragraphs above; the quadratic curvature term is then at most $108L^{10}C_H'^2C_{\rm RD}^2C_F^2\alpha_k^2\eta^2$, which is at most $\alpha_k\eta^2$ under one more ceiling. $\square$

**Remark (if (d) holds only for the fixed determining sets).** Lemma 4(b) applied (d) to an auxiliary partition. If one reads (d) as stated only for the sets $\mathfrak B(p,X)$ fixed by the determining-set hypothesis, run the same argument in $\mathfrak B^{(q+1)}$ itself. It then needs a path in $\mathbb L(\mathfrak B^{(q+1)})$ that avoids $z_\Gamma,z_\gamma$ and joins an equal-level neighbour of $z_\Gamma$ to one of $z_\gamma$. In $d=4$ this holds whenever $R_{q+1}$ and the level-$q$ collar have width at least two blocks along the face; that is a consequence of the widths behind SEP.

## 9. Why this is path-free, and where earlier attacks stopped

- **No data path.** Each step applies R once, at a fixed real minimiser base, to a datum in the polydisc of CMP 102 (172). R asserts the dependence on that polydisc. L16's obstruction concerns data that agree locally but differ globally (a bundle class on a closed torus). Here the two data of a step are close on every row, so it does not arise.
- **No box and no global small gauge.** The relative datum (Lemma 5) is built from transports of length $O(\ell_{q+1})$ to coarse base points. The frames are tied together by the coarse rows (Lemma 4). The flux obstruction to one global small gauge (a constant field on a large disc) concerns one configuration, not the relative datum of two configurations with equal coarse data.
- **No changed boundary row.** All $\mathfrak B^{(q)}$ live on $X''$ with one tower. Rows off $R_{q+1}$ are shared (ROW). This avoids the compatibility that route (ii) of CA-I 45153–45159 leaves unproved.
- **Against RB attack 4 and the account's remark.** There the comparison field was the source's minimiser $U_\nu$, re-blocked from level $p$ to level $i$ in one step. $U_\nu$ is not sharp at fine tower cells (RB (28)), and the crossing datum is $O(\ell_p^2)$ against a needed $O(\ell_i\ell_p)$. One level per step makes the datum of each step live where the coarser minimiser is sharp, and makes the crossing loss one factor $L$.
- **Where the $\ell_n^{-1}$ of CR comes from.** Steps near the slot have data of size $\ell_{q+1}^2\approx\ell_p^2$, damped only by $(2L)^{-(q-n-1)}$ under $(\Phi2)$-type floors. This leaves $\ell_n\ell_p$ in $S$. Corollary 9 removes it with a stronger floor.

## 10. What this does not show, and what to check

1. **Not checked.** Every lemma above is proved by Claude and not yet checked by the other model. The check should read Lemmas 4(b), 5 and 7 first.
2. **Readings to confirm against the source.** (i) R: the derivatives in the five members of CMP 102 (190) are covariant at the base, as in CMP 102 (19); and the account's statement for sets "of the form $\{\Gamma_i\}$ or $\mathbf B_p(X'')\cup\{\Gamma_i\}_{i<p}$" covers the consumer sets $\mathfrak B_E(q,X'')$ that §4.12 says it abstracts (CA-I 43060–43066). (ii) P6 for the account's averages. §4.12 names the CMP 98 (1.5) averages; the OCR of CMP 98 (164) is garbled, and the factor $L^k\eta$ is read from (162)–(163) and from the outline's Theorem 1a.1.6. (iii) ROW and COMP at interface rows. (iv) $n_P<\infty$. (v) SEP in the metric of R, with $w$ growing linearly in $M$.
3. **SEP outside boxes.** The account states (j) for consumer geometries inside admissible boxes. Its justification, the widths of shells and collars from CMP 122a §1, does not use the box. It still has to be read off for each outside class: K4 domains meeting $Z''_k$ and $\Omega_k^{\rm old}$, and old terms on cleaned collars or $B_5$ (CA-I 44993–45003).
4. **SRC is a scope condition.** It is needed for (a) by any route. It holds when $X'\subset Y_4$ lies where the healed level is $k$. That is the case for the account's examples, which lie in $Z\cup\Omega_k^{\rm old}$, provided $X'\subset Y_4$. This is not proved here for every outside consumer.
5. **Constants.** The account's floor $M_*(L)$ is enlarged by $(\Phi_H)$ and $(\Phi_K)$. Both depend only on $L,d$, the input constants and $\delta_H$, so no constant is chosen backward. The ceiling $\gamma_*$ absorbs (8.1).
6. **Scope beyond CR.** Theorem 8 uses no box, so it also gives (a)–(b) for the inside consumers. The real-factor corollary for outside consumers would follow as in CA-I 44828–44845 once (c) of the inside proposition is read with these bounds. That needs the level-$k$ provision and $(\Gamma_1)$–$(\Gamma_3)$; it is not done here.
7. **For the lead.** If the check passes, this is a proof of a statement the account marks "Proof outstanding". Rule 6's five checks apply before anything is offered to them. The tree node and registry rows for CR (`library/t0-tree.md` K2, `library/open-core.md` CR, `library/open-registry.md`) are not edited here.

## Result

**Proof** (an implication; proved by Claude, not yet checked by the other model). For $G=SU(2)$, CA-I `4.12:prop-reblocking-outside` (core statement CR, `library/rb.md` (20)) holds for every outside consumer pair $(p,X'')$: existence at $\varepsilon_1=2\alpha_k\ell_p^2$ and both below-slot bounds, uniformly in depth, domain, diameter and boundary tower (Theorem 8). The premises are:

- the account's own inputs: T1, AV, R (`4.4:not-response-bound`, second case), CUR (`4.4:lem-current-remainder`), AX, its composition grant COMP, and its separation (j) read on $X''$ (SEP);
- Balaban CMP 98 Proposition 6 in its anchored form (P6), and the reading ROW;
- the scope condition SRC.

Two new one-sided floors on $M$, $(\Phi_H)$ and $(\Phi_K)$, and the ceilings (8.1) are added, all in the account's order.

Kind: a proof of a step the account leaves outstanding. It is not a check of their proof and not a correction of their text.

Method: re-block one level at a time on the fixed domain with the consumer's own determining sets (§§6–8). Each step applies Balaban's response at a real minimiser base once, to a relative datum that is supported where the coarser minimiser is sharp. No box, no global small gauge, no changed boundary row and no data path is used, so the L16 obstruction does not arise. Lemma 4(b) derives the anchored interface averages from the account's own (d). Corollary 9 gives the unit-scale bounds $O(\alpha_k\eta^2)$ and $O(\alpha_k\ell_n^{-1})$ under a stronger floor.

Open:
- the other model's line-by-line check, first of Lemmas 4(b), 5 and 7;
- SEP outside admissible boxes and SRC, for each outside consumer class (§10.3–4);
- the readings of §10.2: R's covariant derivatives and its coverage of $\mathfrak B_E(q,X'')$, including admissibility; P6 for the account's averages; ROW and COMP at interface rows; $n_P<\infty$;
- clause (c) (consumer radii) and the real-factor corollary for outside consumers, which are not done here.
