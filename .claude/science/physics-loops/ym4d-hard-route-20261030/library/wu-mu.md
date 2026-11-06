lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T19:07Z

# Uniqueness and locality of the constrained minimizer: a proof of Lemma 4.13 of the complete account

Draft for the owner's review (queue row 350, `wu-mu`). It is not sent anywhere. Research text: no status is granted, and nothing here is a public claim.

**Provenance.** Written by Claude Opus 5.5 (max effort), Mac mini worker, at checkout `d4d149fa2`. It is a write-up of texts that already exist and were checked: the proof `library/mu.md` (Codex, frozen 2026-11-05), its line-by-line check `gates/mu-gate.md` (Claude, first failing step none), the lead's source check of CMP 98 Proposition 4 in `mu.md`, and the carry-over `library/mu-radii.md` (Codex) with its line-by-line check `gates/mur-gate.md` (Claude, one repair). The repairs those checks ask for are applied. This write-up adds no new mathematics. Where it states a step more explicitly than `mu.md`, it says so. The write-up itself has not been checked by the other model.

**Sources.** The complete account of Ethan Sussman and Levent Alpoge at commit `31a47c543775`: CA-I (`theorem_0_complete_account_raw_I.tex`, SHA-256 `4cb5cb5e…6e93`) and CA-III (`…raw_III.tex`, `7e36523b…352d`), fetched by URL for this note; line numbers refer to these files. Tadeusz Bałaban: CMP 98 (1985) 17–51, CMP 102 (1985) 277–309 (cited as CMP 102b, as in the account), CMP 109 (1987) 249–301.

## 1. The statement and its status in the account

The statement, CA-I 45162–45175, reads:

> **Lemma 4.13** (`4.13:lem-minimizer-unique`) [Uniqueness and locality of the constrained minimizer, completing Bałaban's Lemma 4 of [B-CMP109]. Proof outstanding]. Let the constants satisfy the restrictions of [B-CMP109, Lemma 4], and let the fields be those admitted there.
>
> (a) *Uniqueness.* At every field admitted by [B-CMP109, Lemma 4], the constrained variational problem of that lemma has exactly one minimizer, so that the minimizer map of that lemma is well defined.
>
> (b) *Locality.* The minimizer is local, in the sense furnished by the averaging operations of [B-CMP98]. The property required of it is that the nesting identity [B-CMP109, (3.38)] hold when it is read for an arbitrary sub-domain of the domain of [B-CMP109, Lemma 4] in place of that domain.

**Status in the account.** "Proof outstanding." (CA-I 45177). A Route paragraph follows (CA-I 45179–45197). For (a) it asks for three things: (R1) every admitted field satisfies the hypothesis of [B-CMP102b, Theorem 1], with constants that meet the smallness conditions of that theorem; (R2) every minimizer is a critical point in the second space of that theorem, where it asserts uniqueness of the critical orbit; (R3) uniqueness of the orbit gives uniqueness of the minimizer in the form in which Lemma 4 uses it. For (b) it asks for a locality property taken from [B-CMP98] that, with (a), lets (3.38) be read with an arbitrary sub-domain $Z\in\mathcal D_j$ of the domain of Lemma 4. The last sentence (CA-I 45199–45201) says that the lemma enters the one-power hereditary class through (3.38) read on a sub-domain $Z$, and that this reading uses both parts. The account lists the statement again as outstanding at CA-I 166621 and CA-III 111211–111212.

**Where the account uses it.** The label occurs only at its declaration. The content enters through (3.38) on sub-domains:

- the near case, Lemma `4.8:prf-near-case-labels` (CA-I 33602–33827), whose first hypothesis is "the sub-tower conjugation lemma for Bałaban's minimisers" (CA-I 33610–33623), with its proof at CA-I 33654–33698;
- the §4.7 uses (CA-I 29235–29240, 31073–31131, 32422).

Other passages read (3.38) at other data or domains (§§4.26 and 4.28: CA-I 121185–121522, 123126–123129, 144933; §4.31: CA-I 154420; CA-II 35714), or cite it for a bound on a potential (CA-II 44422, 44454). Section 5.3 says which of these the proof covers.

## 2. What the statement means, and the precise form proved

**The minimizer.** Bałaban poses the problem in CMP 102b, pp. 278–279. The action (5) is considered on the space (6), $\mathfrak U_k(\{\Omega_j\},\varepsilon_0)\cap\mathfrak B_k(\Lambda_k,V)$: the regularity conditions (2) and the constraints (3). Both are invariant under the gauge transformations (4), which equal $1$ at the determining sites. Theorem 1 there says: if $V$ satisfies (7) with $\varepsilon_1<a_1$, there is a minimal orbit in the space (8), $\mathfrak U_k(\{\Omega_j\},B_3\varepsilon_1)\cap\mathfrak B_k(\Lambda_k,V)$, and it is the unique critical orbit in (6) if $B_3\varepsilon_1\le\varepsilon_0\le a_0$. CMP 109 (1.1), p. 260, uses this in the form "there exists exactly one regular, critical orbit … and it is a minimal orbit (a set of minima)". So (a) is read as follows. In the regular space (8) there is exactly one minimal orbit. It is the unique critical orbit in the space (6). Exactly one configuration on it is in the axial gauge, and the minimizer map of Lemma 4 takes this configuration. Residual gauge copies on the orbit are not further minimizers. At complex fields the minimizer is Bałaban's analytic continuation (CMP 102b §G, Proposition 9), as the account fixes it in Definitions `4.10:def-minimiser-continuation` and `4.10:def-tower-quantities` (CA-I 38500–38673). No complex-valued action is minimized.

**Locality.** Part (b) itself says what is required: the nesting identity (3.38) read on an arbitrary sub-domain. In the notation of the near case (CA-I 33602–33608), $W=U_j(\square_0,e^{iD})$ is Bałaban's axial minimizer with window tower $(\square_q)_{q\le j}$, $u_j=u_j(D)$ is its gauge, and $\mathcal U=\exp i\xi_j\mathbf H_j(\square_0,D)$ is the $u_j$-copy, so that $W=\mathcal U^{u_j}$. The nesting identity then says that the depth-$n$ minimizer on the tower of a sub-domain $Z$, with the layered averages of $\mathcal U$ as data, is $\mathcal U\restriction Z$ transformed by an explicit gauge. No passage of the account reads a finite-range response property under the name of this lemma. Locality here therefore means this nesting identity, together with the fact that $U_n^{\mathfrak r}(Z;\cdot)$ depends on the set $Z$, the rule and $n$ alone (CA-I (4.8:eq-tower-rules-a)).

**Notation.** As in Definition `4.8:def-tower-rules` (CA-I 32834–32935): $\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}$ are the two tower rules; $\boldsymbol\Omega^{\mathfrak r}(Z)$ is the tower of $Z$ under $\mathfrak r$, truncated at depth $n$, with data sets $\Lambda_q$; $M^{\boldsymbol\cdot}$ is the layered datum; $U_n^{\mathfrak r}(Z;\cdot)$ is the axial minimizer of the depth-$n$ problem; $J_n^{\mathfrak r}$ is its current. We write $\mathcal T$ for the truncated tower when we use the sets $\mathcal A(\mathcal T)$, $\mathcal S(\mathcal T)$ and $\mathcal V(\mathcal T)$ of §4.10 (averages defined, the chart of $G$-valued data, the existence set). The gauge action is that of Definition `4.26:not-gauge-action` (CA-I 129758–129790, as in CMP 109 (1.10)):
$$
U^{h}(b)=h(b_-)\,U(b)\,h(b_+)^{-1},\qquad (U^{a})^{c}=U^{ca}. \tag{1}
$$
Let $\bar u$ be the gauge transformation on $Z$ that is constant on each structure block of the inner tower, with the value of $u_j$ at the root of that block, and equal to $u_j$ on the fine shell $\Lambda_0$. This is Bałaban's $\bar u_j$ of (3.38), "constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $u_j$ at centers of the blocks". Put
$$
g:=\bar u^{-1}u_j . \tag{2}
$$

**Theorem.** Fix $d$, $G=SU(N)$, $\beta$, $L$ and the constants that precede the amplitudes in the account's order of choice. Let $\alpha_0,\alpha_1,\alpha_2,\alpha_3$ satisfy the restrictions of CMP 109 Lemma 4, read at the proof radius $2\alpha_3$ (CA-I 34813–34817), and the further ceilings (A1)–(A3) of §4.9. Each of these is an upper bound fixed by earlier constants alone; none depends on $k$, $j$, $n$, $p$ or a domain. Let the fields be those admitted by Lemma 4: $\mathbf U$ in the space of that lemma, read through the twist polydisc $\mathcal P_U$ of Notation `4.5:not-axial-frame` (CA-I 17433–17460); a fluctuation $\mathbf A$ on $\square_0$ satisfying CMP 109 (3.31); $|\tau|\le1$ and $|B'|<2\alpha_3$; the datum $D=\tau B+B'$, with $B=Q(\eta A)$ as in CMP 109 (3.30). Then:

- **(a)** If $D$ is real, the problem with data $e^{iD}$ on the window tower has exactly one minimal orbit in the space (8), taken at the parameter $\varepsilon_1=C_D\delta$ of §4.4. It is the unique critical orbit in the space (6) at $\varepsilon_0=a_0/2$. Exactly one configuration on it is axial, namely $W=U_j(\square_0,e^{iD})$. If $D$ is complex, $e^{iD}$ lies in the base-one chart of Definition `4.10:def-minimiser-continuation`, so $W$ is the value of the one holomorphic continuation fixed there.
- **(b)** Let $X\in\mathbf D_j$ with $X\subset\tilde\square^{2}$ be the domain of Lemma 4. Let $Z\subset X$ be any sub-domain (this includes every label $(p,Z)\in\mathfrak T_j(X)$), let $\mathfrak r\in\mathfrak R$, and let $1\le n\le j$. Then $\mathcal U\restriction Z$ lies in the existence set $\mathcal V(\mathcal T)$ of the truncated tower, and
$$
U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=(W\restriction Z)^{\bar u^{-1}}=(\mathcal U\restriction Z)^{g}. \tag{3}
$$
Consequently
$$
\partial U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=R(g)\,\partial\mathcal U,\qquad
J_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=(L^n\xi_j)^3R(g)\,\mathcal J . \tag{4}
$$
At real $D$ the restricted field is itself the inner minimizer: $U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(W\restriction Z))=W\restriction Z$.

The consumers' range $1\le n\le p\le j$ is included; the proof does not use $p$. Equation (3) is the printed (3.38) with the acting element written in the order that the action (1) forces; see §6.1.

## 3. Inputs, with their status in the account

| Input | What the proof uses | Status in the account |
|---|---|---|
| Bałaban, CMP 102b Theorem 1, with (2)–(8) | the minimal orbit in (8), the unique critical orbit in (6), the regularity of minimizers, and the seam convention of (7) | published theorem, cited by statement (CA-I 166633); recorded in Definition `4.10:def-minimiser-continuation` (CA-I 38506–38520) |
| CMP 102b §G: (172), (173) with (19)–(21), (181), Proposition 9 | the chart of $G$-valued data, the value bound of the Landau potential, analyticity, agreement with the minimizer at $G$-valued data, the gauge extension | cited by statement (CA-I 166633); Definition `4.10:def-minimiser-continuation` (a)–(d), CA-I 38500–38634: "The proofs are Bałaban's and are not reproduced." Only values and analyticity are used here, not the derivative bounds (189)–(190), which CMP 102b prints without the calculation |
| CMP 98 Proposition 2 | the converse data test: data of a regular field obey (7) with $\varepsilon_1=C_7\varepsilon_0$ | cited by statement (CA-I 166629); $C_7\ge2$ fixed at CA-I 17533 |
| CMP 98 Propositions 4 and 6 | bounds for the auxiliary average $Q$ ((131), (134)–(135)) and for the group average ((159)–(164)) at a flat base | Proposition 6 cited by statement (CA-I 166629); Proposition 4 cited at CA-I 13993. Its (134)–(135) were read from the printed page (journal p. 38), because the OCR there is damaged |
| Lemma `4.6:lem-averaging-locality` (CA-I 24239) | two-block locality of the averages | cited (CMP 98 (58)–(63), (77)–(81), (88)–(92), (124)–(125)) |
| Lemma `4.5:lem-literal-frame` (CA-I 17519–17597; proof 17673–17778) | only (AX1), (AX2-poly) and the first paragraph of (AX3) | proved in the account under its hypotheses (A)–(C); the clauses used here do not use (A), (C) or (AX2-pt) |
| Definition `4.8:def-tower-rules` (CA-I 32834–32935) | the two rules and their separations; that $\mathfrak r_2$ meets CMP 102b (1); the intrinsic dependence (4.8:eq-tower-rules-a) | definition, with the properties it states |
| Lemma `4.10:lem-averaged-data` (CA-I 38430), Theorem `4.10:thm-existence-set` (CA-I 39170) | holomorphy of the averaged data, and of the continued minimizer on the existence set | proved |
| Lemma `9.3:lem-refinement` (CA-III 36939–37000) | the fibre inclusion for a refined tower | proved; it is stated on the torus $T_\eta$, and its proof applies on the window without change |
| Definitions `4.26:not-gauge-action` (CA-I 129758) and `4.26:def-block-axial` (CA-I 130021) | the gauge action (1) and its composition rule; the block-axial tree conditions | definitions; the composition rule is proved there |
| CMP 109 (3.30), (3.31), (3.37), (3.38), Lemma 4, the restrictions of §3 | the datum, and the statement being completed | cited by statement (CA-I 166634) |

## 4. Proof

The proof has two quantitative tasks. First, prove the nesting identity for **every** datum $D$ in one fixed ball, uniformly in the towers, depths and domains (Steps 1–3, 6, 7). Second, put every admitted datum of Lemma 4 in that ball (Step 4). This avoids any appeal to the openness of an existence set, which gives no uniform radius.

### 4.1 Conventions

The averages are Bałaban's group averages $M^q$ of CMP 98, and the auxiliary potential average is his $Q$. The input window is $\square_0=\tilde\square^{5}$, with window tower $(\square_q)_{q\le j}$ and $\square_j\supset\tilde\square^{4}$ (CMP 109 §3; CA-I 33669–33671). The domain is $Z\subset X\subset\tilde\square^{2}$, as in CA-I 33602–33618 and 33654–33676; the claim is about sub-domains of the output domain, not about boundary values at the edge of the window. Empty terminal members of a tower are allowed.

In Steps 1–3, 6 and 7 lengths are in the units of the outer problem: its top block has side $1$, the fine spacing is $\xi_j=L^{-j}$, and a level-$q$ block has side $L^{q-j}$. Step 4 uses the $\eta$-units of CMP 109. The matrix norm is the operator norm. For a datum, $\|D\|_\infty$ is the supremum over **all** its determining bonds, the fine shell included. Logarithms are taken in the fixed identity chart of $G^c$ (Lemma `4.10:lem-principal-logarithm`); every neighbourhood below is small enough to stay in it. The functions $\mathbf H_j(\square_0,\cdot)$ and $u_j(\cdot)$ are those of CMP 102b §G and Proposition 9 at base datum $1$, so $\mathcal U(D)=\exp i\xi_j\mathbf H_j(\square_0,D)$ and $W(D)=\mathcal U(D)^{u_j(D)}$. The constants $a_0,a_1,B_3$ are those of Theorem 1 (they depend on $d$ and $L$ only), and $C_1,B_5$ those of CMP 102b (172)–(173).

### 4.2 Step 1: one chart for every tower, and a bound on the potential

Fix $\varepsilon_*>0$ below the thresholds of Theorem 1 and §G and below the account's $\bar\varepsilon_1$, with $B_3\varepsilon_*<a_0/4$. The datum $1$ satisfies CMP 102b (7) with every positive parameter, on every admissible tower. So §G applies at base $1$ with $\varepsilon_1=\varepsilon_*$. Choose
$$0<r\le\min\{\tfrac14,\ \tfrac14C_1\varepsilon_*\}.$$
If $\|B\|_\infty<r$, then $|e^{iB}-1|\le e^{r}-1<C_1\varepsilon_*$, which is condition (172) at base $1$. Hence, for every admissible tower $\mathcal S$ of every depth and domain, the base-one chart of $\mathcal S$ contains the polydisc $\{\|B\|_\infty<r\}$. On it the Landau potential $\mathbf H_{\mathcal S}(B)$ is holomorphic and satisfies (19)–(21) of CMP 102b with $\varepsilon_2=B_5\varepsilon_*$ (by (173)). Let $\ell_{\mathcal S}(b)$ be the local block side of $\mathcal S$ at $b$. The first inequality of (19) gives
$$N_{\mathcal S}(B):=\sup_b\,\ell_{\mathcal S}(b)\,|\mathbf H_{\mathcal S}(B)(b)|\le B_5\varepsilon_*\qquad(\|B\|_\infty<r). \tag{5}$$
Also $\mathbf H_{\mathcal S}(0)=0$: at datum $1$ the axial minimizer is $1$, its Landau field is $0$, and §G fixes that branch.

Now fix $B$ with $0<\|B\|_\infty<r$, a bond $b$, and a linear functional $\varphi$ of norm one on $\mathfrak g^c$. The function $f(z)=\varphi\bigl(\ell_{\mathcal S}(b)\,\mathbf H_{\mathcal S}(zB/\|B\|_\infty)(b)\bigr)$ is holomorphic on $|z|<r$, with $f(0)=0$ and $|f|\le B_5\varepsilon_*$. The Schwarz lemma gives $|f(z)|\le B_5\varepsilon_*|z|/r$. Put $z=\|B\|_\infty$ and take the supremum over $\varphi$ and $b$:
$$N_{\mathcal S}(B)\le K\|B\|_\infty,\qquad K:=B_5\varepsilon_*/r\qquad(\|B\|_\infty<r). \tag{6}$$
The constant $K$ does not depend on the dimension of the configuration space, on the depth or on the domain. Step 1 uses only the value and analyticity statements of Proposition 9, not the derivative bounds (189)–(190).

### 4.3 Step 2: the averaging estimate and the seam test

Port CMP 98 Proposition 6 at the reference field $U_0=1$, and Proposition 4 for $Q$. There are $a_{98}\in(0,2\log\frac43]$ and $C_A\ge1$, depending on $(d,L)$ only, with the following property. Let $c$ be a level-$q$ output bond of side $s$, let $h$ be the fine spacing, and let $E$ be the two-block carrier of $c$ (Lemma `4.6:lem-averaging-locality`; CA-I 24239–24405). If $F$ is a $\mathfrak g^c$-valued potential with $s\sup_E|F|<a_{98}$, then the group average and the auxiliary average are defined and holomorphic, and
$$\Bigl|\tfrac1i\log M^q(e^{ihF})(c)\Bigr|\le C_A\,s\sup_E|F|,\qquad |Q_q(hF)(c)|\le C_A\,s\sup_E|F|. \tag{7}$$
These are two separate bounds; the two maps are not identified. To read Bałaban's statements in these units, replace the fine spacing by $h/s=L^{-q}$ and the potential by $sF$. At the flat base, hypothesis (52) of CMP 98 holds automatically. For the group average, Proposition 6 with (159)–(164) applies; shrink $a_{98}$ so that the group error is below $\frac12$, and use $|\log(1+E)|\le2|E|$. For $Q$, Proposition 4 gives $Q_k(U_0,\eta A)=Q_k(U_0)A+C_k(U_0,A)$ (134) with $|C_k(U_0,A)|\le C_2|A|^2$ (135), and (131). The linear part is bounded, so a further decrease of $a_{98}$ gives the second bound. Values of $F$ off the carrier play no role. No bound on derivatives of $F$ is needed.

*The seam test.* Let $D$ be real, with $L\|D\|_\infty<a_{98}/2$. Then the test (7) of CMP 102b for the data $e^{iD}$ is at most $C_D\|D\|_\infty$, where
$$C_D:=4C_AL .$$
Indeed $e^{iD(c)}$ is unitary and $|e^{iD(c)}-1|\le|D(c)|$. A plaquette inside one layer has four such factors, and telescoping gives $4\|D\|_\infty$. At a plaquette that meets two levels, one factor is replaced by the one-level finer average, by the convention of CMP 102b p. 278, (7) (CA-I 18616–18620). In the units of that finer lattice, (7) above bounds its logarithm by $C_AL\|D\|_\infty$. All four factors are unitary, so telescoping gives $C_D\|D\|_\infty$. The separation of the tower excludes a seam across more than one level.

### 4.4 Step 3: the ball, and admission of every inner datum

*Carriers.* Let $Z\subset X\subset\tilde\square^{2}$, $\mathfrak r\in\mathfrak R$, $1\le n\le j$, and let $\mathcal T$ be $\boldsymbol\Omega^{\mathfrak r}(Z)$ truncated at depth $n$. Every averaging carrier of a row of $\mathcal T$ lies in $Z$ (CA-I 32966–32973; the support condition of Lemma `4.10:lem-averaged-data`), and so does every gauge tree of an inner structure block. Since $Z\subset\tilde\square^{2}\subset\tilde\square^{4}\subset\square_j$, all of them lie in the outer top region, where the outer local block side is $1$. (Even a carrier that left $Z$ would stay in $\square_j$: in the units of the window construction the two layers between $\tilde\square^{2}$ and $\tilde\square^{4}$ have width $2M$, blocks have side at most $L$, and a two-block carrier has diameter at most $2dL<2M$, since $M\ge2LR_1M_1$ and $R_1\ge4d$.) This holds for every $Z\subset X$, including domains with holes.

*Admission.* By (6) for the window tower, $|\mathbf H_j(\square_0,D)|\le K\|D\|_\infty$ on $\square_j$ whenever $\|D\|_\infty<r$. A level-$q$ inner block has side $s=L^{q-j}\le1$, and the fine spacing is $h=\xi_j$. So, if also $K\|D\|_\infty<a_{98}$, then (7) applies to every row of $\mathcal T$ at once:
$$\|B_{\mathcal T}(D)\|_\infty:=\Bigl\|\tfrac1i\log M^{\boldsymbol\cdot}(\mathcal U(D)\restriction Z)\Bigr\|_\infty\le C_AK\|D\|_\infty . \tag{8}$$
On the fine shell $\Lambda_0$ the datum is $\mathcal U$ itself, and $|\frac1i\log\mathcal U(b)|=\xi_j|\mathbf H_j(b)|\le K\|D\|_\infty$; so (8) holds there too, since $C_A\ge1$.

Choose $\delta>0$ so that
$$\delta<\tfrac r2,\qquad K\delta<\tfrac{a_{98}}2,\qquad C_AK\delta<\tfrac r2,\qquad L\delta<\tfrac{a_{98}}2, \tag{9}$$
and, with $\epsilon_W:=B_3C_D\delta$,
$$C_D\delta<\tfrac{a_1}2,\qquad C_7\epsilon_W<\tfrac{a_1}2,\qquad B_3C_7\epsilon_W<\tfrac{a_0}2,\qquad \epsilon_W<\tfrac{a_0}2 . \tag{10}$$
Conditions (10) pay for the two applications of Theorem 1 in Steps 5–6; both factors $B_3$ are kept. All choices so far depend only on the fixed analytic and geometric constants, never on $k$, $j$, $n$ or $Z$.

On the whole polydisc $\|D\|_\infty<\delta$ we now have: $e^{iD}$ lies in the base-one chart of the window tower; $\mathcal U(D)\restriction Z\in\mathcal A(\mathcal T)$; and $M^{\boldsymbol\cdot}(\mathcal U(D)\restriction Z)=e^{iB_{\mathcal T}(D)}$ with $\|B_{\mathcal T}(D)\|_\infty<r/2$. So the inner datum lies in the base-one chart $\mathcal S(\mathcal T)$ with a margin, and $\mathcal U(D)\restriction Z$ lies in the existence set $\mathcal V(\mathcal T)$ of CA-I (4.10:eq-tower-quantities-2). This holds for every tower at once.

### 4.5 Step 4: every admitted datum lies in the ball

Here a bound on **all** determining rows of the window is needed. The bound (3.32) of CMP 109 on $\tilde\square^{4}$ alone would not suffice.

Units are those of CMP 109: $\eta=L^{-k}$, and a level-$q$ block has side $L^q\eta$. The incoming depth-$(k+1)$ chart of the window is read in its own units $\xi=L^{-1}\eta$, in which its top block has side $1$ and a layer-$n$ block has side $\ell_n=L^{n-k-1}$. The potential $\mathcal A:=L^{-1}\mathbf H_{k+1}(\square_0,\frac1i\log V)$ is the same field in $\eta$-units, and the composite potential of CMP 109 (3.30) is (CA-I 29880–29884)
$$A=\tfrac1{i\eta}\log\bigl(e^{i\eta\mathbf A}\,e^{i\eta\mathcal A}\bigr),\qquad B=Q(\eta A)\ \text{ on }\square_0 .$$

*(i) The incoming datum.* By (AX2-poly) and the first paragraph of (AX3) of Lemma `4.5:lem-literal-frame`, on the whole twist polydisc $\mathcal P_U$ the literal axial datum $V$ satisfies, for every $c\in\mathfrak B(\square_0)$,
$$|V(c)-1|\le C_VM(\alpha_0'''+\alpha_1'''),\qquad \|B_V\|_\infty\le2C_VM(\alpha_0'''+\alpha_1'''),\qquad B_V:=\tfrac1i\log V. \tag{11}$$
The second bound follows from the first by $|\log(1+E)|\le2|E|$ for small $E$. The map $V$ is the literal frame of CA-I 17322–17447. The proofs of these clauses (CA-I 17673–17770) use CMP 98 Proposition 2 at the real field, Proposition 6 about that real field with a complex twist, and explicit finite contour products. They do not use (AX2-pt), the complex-curvature hypothesis (C), the glued background, or the identity being proved. Of the input space, conditions (i)–(ii) supply the real field and its twist; condition (iii) and the output hereditary clause are not used.

By ceiling (A1) of §4.9, $\|B_V\|_\infty<r/2$. So (6), for the window tower at base $1$, gives $\ell_n|\mathbf H_{k+1}(\square_0,B_V)|\le K\|B_V\|_\infty$ on every layer $n$, the collar included. No estimate that rests on (189)–(190) is used.

*(ii) Carriers of the outgoing rows.* Let $q\ge1$. A level-$q$ row of the outgoing depth-$j$ datum, with its two-block carrier, lies in $\square_{q-1}$, also when the row points outward at $\partial\square_q$. By alignment, its second block is inside $\square_q$ or is the adjacent block across one face, so its points are within one level-$q$ block side of $\square_q$. The distance from $\square_q$ to $\square_{q-1}^{c}$ is larger than that side, since $R_1\ge L$ and $\mathfrak M\ge1$. On $\square_{q-1}$ the incoming layer index $n$ is at least $q-1$. The row has side $s_q=L^q\eta$, which is $L^{q-k-1}$ in the units $\xi$, so $s_q|\mathcal A|=L^{q-n}\,\ell_n|\mathbf H_{k+1}|$. Hence
$$s_q\sup_E|\mathcal A|\le LK\|B_V\|_\infty,\qquad s_q\sup_E|\mathbf A|\le L\alpha_2, \tag{12}$$
using $|\mathbf A|<\alpha_2$ on the window (CMP 109 (3.31)) and $s_q\le L^{k+1}\eta=L$ (all indices obey $q\le j\le k+1$). At $q=0$ the same bound follows from the fine-row bound directly.

*(iii) The composite potential.* For matrices $X,Y$ with $t:=|X|+|Y|\le\log\frac43$, submultiplicativity gives $|e^{iX}e^{iY}-1|\le e^t-1$. The logarithm series then gives $|\log(e^{iX}e^{iY})|\le-\log(2-e^t)\le2t$; the last inequality follows by integrating $e^t/(2-e^t)\le2$ from $0$. Apply this with $X=\eta\mathbf A$, $Y=\eta\mathcal A$. Since $\eta\le s_q$, (12) and ceiling (A2) give $t\le L(\alpha_2+K\|B_V\|_\infty)<a_{98}/2\le\log\frac43$. Therefore
$$s_q\sup_E|A|\le2L\bigl(\alpha_2+K\|B_V\|_\infty\bigr)<a_{98}. \tag{13}$$

*(iv) The datum.* By (13), the bound (7) for $Q$ applies to $B=Q(\eta A)$ on each row, with its rows unchanged: $\|B\|_\infty\le2LC_A(\alpha_2+K\|B_V\|_\infty)$. For $|\tau|\le1$ and $|B'|<2\alpha_3$, (11) and ceiling (A3) give
$$\|D\|_\infty\le2LC_A\bigl[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr]+2\alpha_3<\delta . \tag{14}$$
The near case $\mathbf A=0$ is included. This proves chart admission of every admitted datum from the input conditions alone. It does not use the conclusion of Lemma 4 or the near-case membership. (If CMP 109 (3.30) is read with $\tau\log V$ in place of $\log V$, nothing changes for $|\tau|\le1$, since (6) is linear in the norm. If a later Cauchy estimate uses a fixed larger $\tau$-disc, multiply the first term of (14) by its radius before the amplitudes are chosen.)

### 4.6 Step 5: proof of (a)

**Lemma R (one axial configuration on an orbit).** Let $\mathcal S$ be an admissible tower, with the blocks, roots and gauge trees of Notation `4.26:not-gauge-trees`, and let $Y$ be block-axial for $\mathcal S$ (Definition `4.26:def-block-axial`). Let $h$ be a gauge transformation equal to $1$ at every determining site of $\mathcal S$. If $Y^h$ is also block-axial, then $h=1$ at every site, so $Y^h=Y$.

*Proof.* Covariance of the averages gives $M^m(Y^h)=(M^mY)^{h|_{\Lambda_m}}$ (proof of Definition `4.26:not-gauge-action`). On a bond $b$ of a gauge tree $\mathcal T_m(B')$ both averaged values are $1$, so $1=h(b_-)\,h(b_+)^{-1}$: $h$ takes the same value at the two ends of $b$. Each tree spans the level-$m$ sites of its block $B'$ and contains the root of $B'$. The root of each structure block is a determining site, where $h=1$. Going down one level at a time, $h=1$ at every site of every block. The sites of the fine shell are determining sites. $\square$

This is the residual-gauge argument of `mu.md` §5, stated once here and used twice: in (R3) below for the window, and in Step 6 for the inner tower.

**Proof of (a).** Let $D$ be an admitted datum. By (14), $\|D\|_\infty<\delta$.

*(R1) Theorem 1 applies.* Let $D$ be real. By Step 2 and (9), the data $e^{iD}$ satisfy CMP 102b (7) with $\varepsilon_1:=C_D\delta$; the inequality is strict, since the test is at most $C_D\|D\|_\infty$. By (10), $\varepsilon_1<a_1/2$. So Theorem 1 applies to the window problem at depth $j$. It gives a minimal orbit $\mathcal O$ in the space (8), $\mathfrak U_j(\{\square_q\},\epsilon_W)\cap\mathfrak B_j(\cdot\,,e^{iD})$, with $\epsilon_W=B_3\varepsilon_1$. Since $\epsilon_W<a_0/2$, Theorem 1 with $\varepsilon_0=a_0/2$ also gives that $\mathcal O$ is the unique critical orbit in the space (6).

*(R2) Every minimizer is critical in the uniqueness space.* Let $Y$ minimize the action (5) over the space (8). The space (8) is cut out of the constraint set by the strict inequalities (2). So every differentiable curve $Y(t)$ in the constraint set with $Y(0)=Y$ stays in (8) for small $|t|$, on both sides of $0$. The action along it has a minimum at $t=0$, so its derivative there is $0$: $Y$ is critical. Since $\epsilon_W<a_0/2$, $Y$ lies in the space (6) at $\varepsilon_0=a_0/2$. Hence the orbit of $Y$ is $\mathcal O$, and $\mathcal O$ is the only minimal orbit in (8).

*(R3) One minimizer.* The orbits are those of the gauge transformations (4), which equal $1$ at the determining sites. Bałaban's minimal configuration is axial (CMP 102b p. 279; CA-I 38518–38520), so $\mathcal O$ contains the axial configuration $W=U_j(\square_0,e^{iD})$. By Lemma R it contains no other. This is the form in which Lemma 4 uses uniqueness: the map $D\mapsto U_j(\square_0,e^{iD})$ is well defined.

*Complex data.* Let $D$ be complex. By (14), $\|D\|_\infty<\delta<r$. So $e^{iD}=e^{iD}\cdot1$ lies in the base-one chart of the window tower; in the notation of Definition `4.10:def-minimiser-continuation`, $D\in\mathcal B(1)$, and the minimizer map at $D$ is $\Phi_1(D)$. By item (b) of that definition it is the value of one analytic function of the datum, and by item (c) it agrees with the minimizer at real data. Nothing is minimized at complex data; this is the account's convention. This proves (a). $\square$

### 4.7 Step 6: real restriction to a sub-domain

Let $D$ be real with $\|D\|_\infty<\delta$, let $W=U_j(\square_0,e^{iD})$, and let $Z,\mathfrak r,n,\mathcal T$ be as in Step 3. By Step 5, $W$ lies in the regular class $\mathfrak U_j(\{\square_q\},\epsilon_W)$.

*(i) A refined tower on the same window.* Put
$$\widehat\Omega_0=\square_0,\qquad \widehat\Omega_q=\Omega_q^{\mathfrak r}(Z)\quad(1\le q\le n),\qquad \widehat\Omega_q=\varnothing\quad(n<q\le j). \tag{15}$$
This tower is admissible. Its first separation holds because $\operatorname{dist}(\square_0^c,\Omega_1(Z))\ge\operatorname{dist}(Z^c,\Omega_1(Z))$, as $Z\subset\square_0$; its later separations are the inner ones. It is memberwise smaller than the window tower, since $\Omega_q(Z)\subset Z\subset\square_j\subset\square_q$. Rule $\mathfrak r_2$ satisfies CMP 102b (1) with block $\mathfrak M$ and $R=R_\star'\ge R_1$ (CA-I 32975–32981), so both rules can be read at the common gap $R_1$. Empty terminal members change neither the rows nor the action, and are discarded. If $\Omega_1(Z)$ is empty, every inner bond is prescribed and (17) below is immediate.

*(ii) Refinement.* Apply the proof of Lemma `9.3:lem-refinement` (CA-III 36939–37000) to the window tower and (15). The averages of the window tower are compositions of the averages of (15). So the fibre of the refined data $\widehat V:=M_{\widehat{\mathfrak B}}(W)$ is contained in the fibre of the original data, and $W$ is minimal, hence critical, for $(\widehat{\mathfrak B},\widehat V)$. In that proof the refined data obey (7) with parameter $2B_3\varepsilon_1\le C_7\epsilon_W$, as $C_7\ge2$; so its use of Theorem 1 is covered by (10). This imports the fibre inclusion for the actual averages, with their seam rows. It does not claim that a minimizer is insensitive to its boundary data.

*(iii) Change of action domain.* Let $V(t)$ be a differentiable curve of configurations on $Z$ with $V(0)=W\restriction Z$ that keeps the inner data $M^{\boldsymbol\cdot}(W\restriction Z)$ of $\mathcal T$ fixed. Extend it by $W$ outside $Z$, to $\widehat V(t)$ on $\square_0$. The inner level-zero data fix every bond of $Z$ except those that touch $\Omega_1(Z)$. By the first inner separation, every plaquette that contains such a bond lies in $Z$. So every other plaquette term is constant in $t$, and
$$\frac{d}{dt}A_{\square_0}\bigl(\widehat V(t)\bigr)\Big|_{t=0}=\frac{d}{dt}A_Z\bigl(V(t)\bigr)\Big|_{t=0}. \tag{16}$$
The extended curve keeps the refined data fixed: its positive-level rows are the inner rows, because the averages read the field on $Z$ only (CA-I 32966–32973), and every extra level-zero row is fixed. For small $|t|$ it stays in the open regular class of the refined problem, since $W$ lies strictly inside it. By (ii), the left side of (16) is $0$. Hence $W\restriction Z$ is critical for the inner problem. The same-domain refinement lemma alone would not give this; the change of action domain is what (16) adds.

*(iv) Inner uniqueness.* The local block sides of $\mathcal T$ are at most those of the window tower, so the bounds that define the inner regular class are weaker, as in the proof of Lemma `9.3:lem-refinement`. Hence $W\restriction Z$ lies in the inner regular class at parameter $\epsilon_W$. By CMP 98 Proposition 2, the inner data $M^{\boldsymbol\cdot}(W\restriction Z)$ satisfy (7) with parameter $C_7\epsilon_W<a_1/2$, by (10). Theorem 1 for the inner problem gives a minimal orbit, with regularity parameter $B_3C_7\epsilon_W<a_0/2$, and it is the unique critical orbit in the inner space (6) at $\varepsilon_0=a_0/2$. That space contains $W\restriction Z$, since $\epsilon_W<a_0/2$. By (iii), $W\restriction Z$ lies on the inner minimal orbit.

*(v) The axial representative.* The inner block-axial conditions are imposed on the globally aligned trees inside structure blocks of level at most $n\le j$. Those blocks lie in $\square_j$, where $W$ is block-axial for the window tower (CA-I 130021–130052). So the inner conditions are among the outer ones, and $W\restriction Z$ is inner axial. By Lemma R the inner minimal orbit has only one axial configuration. Therefore
$$U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(W\restriction Z)\bigr)=W\restriction Z . \tag{17}$$
Finally, every real minimizer of the inner problem in its regular space (8) is critical and lies in its space (6), by the argument of (R2); so the inner problem, like the window problem, has exactly one minimal orbit there. This says nothing about minima outside Bałaban's regular spaces.

### 4.8 Step 7: complex nesting, and proof of (b)

Let $D$ be real with $\|D\|_\infty<\delta$. Then $\mathcal U=W^{u_j^{-1}}$, so covariance of the averages gives $M^{\boldsymbol\cdot}(\mathcal U\restriction Z)=\bigl(M^{\boldsymbol\cdot}(W\restriction Z)\bigr)^{v}$, where $v$ is the restriction of $u_j^{-1}$ to the sites of the constraint lattices of $\mathcal T$. The fine-lattice gauge $\tilde v$ that CMP 102b (181) attaches to $v$ (Definition `4.10:def-minimiser-continuation` (d)) is constant on each structure block, with the value of $u_j^{-1}$ at its root, and equals $u_j^{-1}$ on the fine shell. That is, $\tilde v=\bar u^{-1}$. By (181), then (17), then (1):
$$U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=\Bigl[U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(W\restriction Z)\bigr)\Bigr]^{\bar u^{-1}}=(W\restriction Z)^{\bar u^{-1}}=\bigl((\mathcal U\restriction Z)^{u_j}\bigr)^{\bar u^{-1}}=(\mathcal U\restriction Z)^{\bar u^{-1}u_j}. \tag{18}$$

Both ends of (18) are holomorphic in $D$ on the whole ball $\|D\|_\infty<\delta$. For the left end: $D\mapsto\mathcal U(D)\restriction Z$ is holomorphic; by Step 3 it maps the ball into $\mathcal A(\mathcal T)$ with data in $\mathcal S(\mathcal T)$; and the averaged data and the continued minimizer are holomorphic there (Lemma `4.10:lem-averaged-data`; Definition `4.10:def-minimiser-continuation` (a)–(b); Theorem `4.10:thm-existence-set`). So the left end is the actual inner continuation, not a continuation assumed outside its domain. For the right end: $\mathcal U(D)$ and $u_j(D)$ are holomorphic (CMP 102b §G, Proposition 9), $\bar u$ is made of root values of $u_j$, and inversion is holomorphic. The two ends agree at the real points of the ball, which form an open subset of the real form $\mathfrak g^{N}$ of $(\mathfrak g^{c})^{N}$, $N$ being the number of determining bonds. By the identity theorem, applied one complex coordinate at a time in a real basis and then extended over the connected ball, (18) holds on the whole ball. With (14), this proves (3) at every admitted datum.

Curvature and current are covariant. By the path formula of (1), $\partial(U^h)(p)=h(x)\,\partial U(p)\,h(x)^{-1}$ at the base point $x$ of $p$, and the current of $U^h$ is $R(h)$ applied to the current of $U$. Writing the inner current in inner top-block units gives the factor $(L^n\xi_j)^3$. This proves (4), which is the account's (4.8:eq-near-case-labels-2) with $g$ in the order (2). The scalar curvature and current bounds that the account derives from (4) (CA-I 33698–33780 and 31085–31131) are proved there and are not repeated. They use only $\|\operatorname{Ad}_g^{\pm1}\|\le|g|\,|g^{-1}|$, and the bounds on $u_j^{\pm1}$ and $\bar u^{\pm1}$ that they use give the same estimate for both orders of the product. This proves (b). $\square$

### 4.9 Order of choice

The new ceilings are (9), (10) and the amplitude ceilings (A1)–(A3) below, with the published chart and averaging thresholds. Their order is:

1. Fix $d$, $G$, $\beta$; then $L$ with the account's floors; then the propagator and averaging constants, the block sizes and the gaps. Keep the account's order $C_1,C_H,\bar\varepsilon_1$. Then choose $\varepsilon_*$, $r$, $K=B_5\varepsilon_*/r$, $a_{98}$ and $C_A$, $C_D=4C_AL$, $C_7$ (CA-I 17533), and $\delta$ by (9)–(10), in this order. None of them depends on $k$, $j$, $n$, $p$ or $Z$.
2. Choose $B^{(109)}$ and $M$ with their existing one-sided floors. This proof imposes no upper bound on $M$.
3. Choose the amplitudes in the order recorded in the account (CA-I 34745–34883): $\alpha_1$ small enough for its existing conditions; $\alpha_0$ small enough for its existing conditions, including those relative to $\alpha_1$; $\alpha_3$ small enough for $4B_3\alpha_3\le\beta L^{-2}\alpha_0$ and $2B_3\alpha_3<\frac12\alpha_1$; then $\alpha_2$ small enough for $c\,\alpha_2\le\alpha_3$. Decrease them further, in the same order, until
$$\text{(A1)}\quad 2C_VM(\alpha_0'''+\alpha_1''')<\tfrac r2,\qquad
\text{(A2)}\quad 2L\bigl(\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr)<a_{98},$$
$$\text{(A3)}\quad 2LC_A\bigl(\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr)+2\alpha_3<\delta ,$$
together with the ceilings of Lemma `4.5:lem-literal-frame` that (AX1) and (AX2-poly) use (among them $\alpha_1'''\le\min\{\alpha_1^{(98)},1\}$, $2C_vM\alpha_1'''\le\frac16$, and the small real-curvature threshold of CMP 98 Proposition 2), and the condition that the bound on $|V-1|$ in (11) lies in the identity logarithm chart.

Every new inequality has a positive right side fixed by earlier constants, and it is preserved when the amplitudes decrease. Every existing coupling among the amplitudes bounds a later amplitude by an earlier one ($\alpha_0$ by $\alpha_1$; $\alpha_3$ by $\alpha_0$ and $\alpha_1$; $\alpha_2$ by $\alpha_3$). So decreasing them in the same order closes without a cycle. This specifies the phrase "sufficiently small and satisfying all the restrictions" of CMP 109 Lemma 4 (p. 280). The specification does not depend on $Z$, on the number of blocks or on the depth. At the account's running radii $\alpha_{\cdot,i}$, (A1)–(A3) are imposed on every running radius; they have the same form, so no new obstruction arises. No current estimate, and no conclusion of another open statement of the account, is used.

## 5. Remarks and scope

### 5.1 The order of the gauge factors

Under the action (1), which is also that of CMP 109 (1.10), the chain of equalities in (3.38) fixes the acting element as $g=\bar u^{-1}u_j$. Pointwise, $g(x)=u_j(y)^{-1}u_j(x)$, where $y$ is the root of the block that contains $x$. The account prints the reversed product $u_j\bar u^{-1}$, or $g(x)=u_j(x)u_j(y)^{-1}$, at CA-I 29236, 31077, 31110, 33615–33616, 33686–33689, 33701–33703 and 121436–121437; this is also the order printed in CMP 109 (3.38), p. 278. It is the product for the mirrored action $U^h(b)=h(b_-)^{-1}U(b)h(b_+)$, which the account discusses at CA-I 130178–130191. Its remark there says that the acting element is "the one fixed by the chain of equalities". The account uses the order (2) at CA-I 121440 and 123129.

The correction is needed for the printed identity to be literally true. It changes no estimate: every consumer uses only $\|\operatorname{Ad}_g^{\pm1}\|\le|g|\,|g^{-1}|$ (CA-I 33698–33735, 31085, 121448–121455), and that bound is the same for both orders. The two products need not act in the same way, and no equality between them is used.

### 5.2 Locality is the nesting identity

No consumer of the account reads a finite-range response property under the name of this lemma. Part (b) is therefore proved in the sense that part (b) itself states: the nesting identity (3) for an arbitrary sub-domain, with the intrinsic dependence of $U_n^{\mathfrak r}(Z;\cdot)$ on $Z$, the rule and $n$. The proof says nothing about how the minimizer responds to changes of its data far away.

### 5.3 Uses of (3.38) outside the statement

The proof covers the near-case consumer `4.8:prf-near-case-labels` and the §4.7 nesting uses (CA-I 32422; 31104–31112 at labels $(p,Z)\in\mathfrak T_{i'}(X)$ with $Z\subset X\subset\tilde\square^{2}$), provided the radius $\alpha^{\sharp}_{3,i'}$ of the latter is at most $2\alpha_3$ at the running radii. Other passages read (3.38) at other data radii and domains. For them the mechanism of Steps 3, 6 and 7 is used in the following general form (`mu-radii.md` §1). Let $W=\mathcal U^{u}$ be an outer axial minimizer whose datum lies in the $\delta$-ball of a base-one chart, and let $\mathcal T$ be any admissible inner tower, with holes or several components allowed, whose carriers and trees lie in the outer top region and whose block sides are at most the outer top side. Then
$$U_{\mathcal T}\bigl(M_{\mathcal T}\,\mathcal U\bigr)=\bigl(W\restriction\mathcal T\bigr)^{\bar u_{\mathcal T}^{-1}}=\bigl(\mathcal U\restriction\mathcal T\bigr)^{\bar u_{\mathcal T}^{-1}u}.$$
The relative gauge $\bar u_{\mathcal T}^{-1}u$ is in general not constant on blocks. At depth zero it is $1$.

With this form, and explicit radius ceilings in the account's order of constants, the following uses are covered: the stage-composite uses of §§4.26 and 4.28, the graded cover included (CA-I 121185–121522, 123126–123129, 144933), and the local-box restriction of the refined minimizer at CA-II 35714. The ceiling for CA-II 35714 uses the constant $C_Q:=\max\{1,K_{\rm loc}/(5.6K_{\rm ax}MC_M^{\rm av})\}$, read from CA-II 35666. For the stage composites, the identity is proved, not the separately assumed sharp bound $\|g\|\,\|g^{-1}\|\le G'_\square$ (CA-I 121440–121455, 123129–123132), which the account keeps as a hypothesis.

Three stronger readings are **not** covered:

1. **§4.31(a) and (c)** (CA-I 154354–154376, 154397–154405, cited at 154420) require the acting gauge to be constant on blocks while the field on the right is the Landau representative. This requirement is false, at arbitrarily small real data, in Bałaban's reading. Take a box with an interior level-one block and a tree bond $b$ of it in direction $1$, and the flat abelian field $\mathcal U_a(x,x+he_1)=e^{ihaT}$, $\mathcal U_a=1$ in the other directions, with $T=\operatorname{diag}(1,-1)$ and $0<|ha|<\pi$. Its curvature is $1$ and its current is $0$; it is the small Landau representative of its data, and the inner axial minimizer equals $1$ on $b$. A gauge $v$ that is constant on the block gives $\mathcal U_a^{v}(b)=v\,e^{ihaT}v^{-1}\ne1$. The account's own §4.7 (CA-I 29234–29239) and Bałaban's (3.38) carry the factor $u_j$ that is not constant on blocks; the quotation at CA-I 154423 has $U_j$ where Bałaban has $u_j$. The consumers (N1)–(N3) of §4.31 read only norm bounds and values of a gauge-invariant function $f$, and the corrected identities give those (`mu-radii.md` (14), (18)–(20)). So their proof does not change.
2. **The bound in §4.31(b)** (CA-I 154378–154395), that the relating gauge has both norms at most exactly $2$ for every allowed gauge, is not established. It is not needed: the consumer at CA-I 156050 needs only equality of values of $f$, which is proved on its full datum range.
3. **CA-II 44422 and 44454** cite (3.38) for a bound on a potential, not for the identity. Step 1 gives a weighted bound of that form with $K$ in place of $B_3$. The anchor bound and the path-integral bounds needed on $X_T$ are proved (`mu-radii.md` §5); an unweighted bound on the whole graded rim is not.

### 5.4 What this does not prove

- Nothing about minima outside Bałaban's regular spaces (6) and (8). At complex data nothing is minimized.
- No finite-range response of the minimizer (§5.2).
- The consumers' scalar curvature and current estimates are the account's; they are not proved again here.
- The derivative bounds (189)–(190) of CMP 102b are neither used nor proved.
- The published inputs, and the cited Lemma `4.6:lem-averaging-locality`, are used as cited and are not proved again.
- The next statement, Lemma `4.13:lem-own-constant` (CA-I 45203), is not addressed.

## 6. Credit

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at commit `31a47c543775`: the statement of Lemma 4.13 and its Route; the tower rules of §4.8; the continuation convention of §4.10; the literal-frame Lemma 4.5; the refinement Lemma 9.3; the gauge-action and block-axial definitions of §4.26; and the consumers, whose estimates are used as they stand. Tadeusz Bałaban for the constrained minimizer and its analytic continuation (CMP 102b), the averaging operations (CMP 98), and Lemma 4 with the nesting identity (3.38) (CMP 109).

The proof written up here is Codex's (`library/mu.md`). It was checked line by line by Claude (`gates/mu-gate.md`), first failing step none, and the check's repairs are applied. CMP 98 Proposition 4 was read from the printed page by the lead (Claude). The carry-over to other radii and domains (§5.3) is Codex's (`library/mu-radii.md`), checked line by line by Claude (`gates/mur-gate.md`), with one repair, which is applied. This write-up is by Claude and has not been checked by the other model.
