lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T19:07Z

# Uniqueness and locality of the constrained minimizer: a proof of Lemma 4.13 of the complete account

Draft for the owner's review (queue row 350, `wu-mu`). It is not sent anywhere. Research text: no status is granted, and nothing here is a public claim.

**Provenance.** Written by Claude Opus 5.5 (max effort), Mac mini worker, at checkout `d4d149fa2`. It writes up checked texts and adds no new mathematics: the proof `library/mu.md` (Codex, frozen 2026-11-05); its line-by-line check `gates/mu-gate.md` (Claude, first failing step none), whose repairs are applied; the lead's reading of CMP 98 Proposition 4 from the printed page; and, for §5.2 only, `library/mu-radii.md` (Codex) with its line-by-line check `gates/mur-gate.md` (Claude, one repair, applied). Two steps are stated more explicitly than in `mu.md`: Lemma R is its residual-gauge argument, stated once and applied to the window and to the inner tower; and (R2) names the variational space (8) and the uniqueness space (6), as the check asked. This write-up has not been checked by the other model.

**Sources.** The complete account of Ethan Sussman and Levent Alpoge at commit `31a47c543775`: CA-I (SHA-256 `4cb5cb5e…6e93`) and CA-III (`7e36523b…352d`), fetched by URL; line numbers refer to these files. Tadeusz Bałaban: CMP 98 (1985) 17–51; CMP 102 (1985) 277–309, cited as CMP 102b as in the account; CMP 109 (1987) 249–301.

## 1. The statement and its status in the account

The statement, CA-I 45162–45175:

> **Lemma 4.13** (`4.13:lem-minimizer-unique`) [Uniqueness and locality of the constrained minimizer, completing Bałaban's Lemma 4 of [B-CMP109]. Proof outstanding]. Let the constants satisfy the restrictions of [B-CMP109, Lemma 4], and let the fields be those admitted there.
>
> (a) *Uniqueness.* At every field admitted by [B-CMP109, Lemma 4], the constrained variational problem of that lemma has exactly one minimizer, so that the minimizer map of that lemma is well defined.
>
> (b) *Locality.* The minimizer is local, in the sense furnished by the averaging operations of [B-CMP98]. The property required of it is that the nesting identity [B-CMP109, (3.38)] hold when it is read for an arbitrary sub-domain of the domain of [B-CMP109, Lemma 4] in place of that domain.

**Status.** "Proof outstanding." (CA-I 45177), repeated in the status lists at CA-I 166621 and CA-III 111211–111212. The Route (CA-I 45179–45197) asks, for (a): (R1) every admitted field meets the hypothesis of [B-CMP102b, Theorem 1] with constants inside its smallness conditions; (R2) every minimizer is a critical point in the second space of that theorem, where it asserts uniqueness of the critical orbit; (R3) uniqueness of the orbit gives uniqueness of the minimizer in the form Lemma 4 uses. For (b) it asks for a locality property from [B-CMP98] that, with (a), lets (3.38) be read on an arbitrary sub-domain $Z\in\mathcal D_j$. The lemma enters the one-power hereditary class through that reading, which uses both parts (CA-I 45199–45201).

**Uses.** The label occurs only at its declaration. The content enters through (3.38) on sub-domains: in the near case, Lemma `4.8:prf-near-case-labels` (CA-I 33602–33827), whose first hypothesis is "the sub-tower conjugation lemma for Bałaban's minimisers" (CA-I 33610–33623); and in §4.7 (CA-I 29235–29240, 31073–31131, 32422). Other passages read (3.38) at other data or domains, or cite it for a bound on a potential; §5.2 says which of these are covered.

## 2. What the statement means, and the form proved

**The minimizer.** In CMP 102b, pp. 278–279, the action (5) is considered on the space (6), $\mathfrak U_k(\{\Omega_j\},\varepsilon_0)\cap\mathfrak B_k(\Lambda_k,V)$, given by the regularity conditions (2) and the constraints (3), modulo the gauge transformations (4), which equal $1$ at the determining sites. Theorem 1: if $V$ satisfies (7) with $\varepsilon_1<a_1$, there is a minimal orbit in the space (8), $\mathfrak U_k(\{\Omega_j\},B_3\varepsilon_1)\cap\mathfrak B_k(\Lambda_k,V)$, and it is the unique critical orbit in (6) if $B_3\varepsilon_1\le\varepsilon_0\le a_0$. CMP 109 (1.1) uses this as "exactly one regular, critical orbit … and it is a minimal orbit (a set of minima)". So (a) means: exactly one minimal orbit in the regular space (8); it is the unique critical orbit in (6); and exactly one configuration on it is axial, which is the value of the minimizer map. Residual gauge copies are not further minimizers. At complex fields the minimizer is Bałaban's analytic continuation (CMP 102b §G, Proposition 9), as fixed by Definitions `4.10:def-minimiser-continuation` and `4.10:def-tower-quantities` (CA-I 38500–38673). No complex-valued action is minimized.

**Locality.** Part (b) states what is required: the nesting identity read on an arbitrary sub-domain. No passage of the account reads a finite-range response property under this lemma's name. So locality means the identity (3) below, with the fact that $U_n^{\mathfrak r}(Z;\cdot)$ depends on $Z$, the rule and $n$ alone (CA-I (4.8:eq-tower-rules-a)).

**Notation.** As in the near case (CA-I 33602–33608): $W=U_j(\square_0,e^{iD})$ is Bałaban's axial minimizer, with window tower $(\square_q)_{q\le j}$ and gauge $u_j=u_j(D)$; $\mathcal U=\exp i\xi_j\mathbf H_j(\square_0,D)$ is its $u_j$-copy, so $W=\mathcal U^{u_j}$; $\mathcal J$ is the current of $\mathcal U$. As in Definition `4.8:def-tower-rules` (CA-I 32834–32935): $\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}$; $\boldsymbol\Omega^{\mathfrak r}(Z)$ is the tower of $Z$, truncated at depth $n$, with data sets $\Lambda_q$; $M^{\boldsymbol\cdot}$ is the layered datum; $U_n^{\mathfrak r}(Z;\cdot)$ is the axial minimizer of the depth-$n$ problem and $J_n^{\mathfrak r}$ its current. $\mathcal T$ denotes the truncated tower when the sets $\mathcal A(\mathcal T)$, $\mathcal S(\mathcal T)$, $\mathcal V(\mathcal T)$ of §4.10 are used (averages defined; chart of $G$-valued data; existence set). The gauge action is that of Definition `4.26:not-gauge-action` (CA-I 129758–129790), which is CMP 109 (1.10):
$$
U^{h}(b)=h(b_-)\,U(b)\,h(b_+)^{-1},\qquad (U^{a})^{c}=U^{ca}. \tag{1}
$$
Let $\bar u$ be constant on each structure block of the inner tower, with the value of $u_j$ at the root of the block, and equal to $u_j$ on the fine shell $\Lambda_0$. This is Bałaban's $\bar u_j$ of (3.38), "constant on blocks naturally connected with the function $U_n(X,\cdot)$, and equal to $u_j$ at centers of the blocks". Put
$$
g:=\bar u^{-1}u_j . \tag{2}
$$

**Theorem.** Fix $d$, $G=SU(N)$, $\beta$, $L$ and the constants that precede the amplitudes in the account's order of choice. Let $\alpha_0,\alpha_1,\alpha_2,\alpha_3$ satisfy the restrictions of CMP 109 Lemma 4, read at the proof radius $2\alpha_3$ (CA-I 34813–34817), and the ceilings (A1)–(A3) of §4.9. Each is an upper bound fixed by earlier constants; none depends on $k$, $j$, $n$, $p$ or a domain. Let the fields be those admitted by Lemma 4: $\mathbf U$ in its space, read through the twist polydisc $\mathcal P_U$ (CA-I 17433–17460); a fluctuation $\mathbf A$ on $\square_0$ with CMP 109 (3.31); $|\tau|\le1$, $|B'|<2\alpha_3$; and the datum $D=\tau B+B'$, $B=Q(\eta A)$, of CMP 109 (3.30). Then:

- **(a)** If $D$ is real, the problem with data $e^{iD}$ on the window tower has exactly one minimal orbit in the space (8), taken at $\varepsilon_1=C_D\delta$ (§4.4). It is the unique critical orbit in the space (6) at $\varepsilon_0=a_0/2$, and exactly one configuration on it is axial, namely $W$. If $D$ is complex, $e^{iD}$ lies in the base-one chart of Definition `4.10:def-minimiser-continuation`, and $W$ is the value there of the one holomorphic continuation.
- **(b)** Let $X\in\mathbf D_j$, $X\subset\tilde\square^{2}$, be the domain of Lemma 4. Let $Z\subset X$ be a sub-domain on which the tower rules are read (every label $(p,Z)\in\mathfrak T_j(X)$ is one), $\mathfrak r\in\mathfrak R$ and $1\le n\le j$. Then $\mathcal U\restriction Z$ lies in the existence set $\mathcal V(\mathcal T)$, and
$$
U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=(W\restriction Z)^{\bar u^{-1}}=(\mathcal U\restriction Z)^{g}, \tag{3}
$$
$$
\partial U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=R(g)\,\partial\mathcal U,\qquad
J_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=(L^n\xi_j)^3R(g)\,\mathcal J . \tag{4}
$$
At real $D$ the restriction is itself the inner minimizer: $U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(W\restriction Z))=W\restriction Z$.

The consumers' range $1\le n\le p\le j$ is included; the proof does not use $p$. Equation (3) is the printed (3.38) with the acting element in the order that the action (1) forces (§5.1).

## 3. Inputs, with their status in the account

| Input | Used for | Status in the account |
|---|---|---|
| CMP 102b Theorem 1, with (2)–(8) | minimal orbit in (8); unique critical orbit in (6); seam convention of (7) | cited by statement (CA-I 166633; Definition `4.10:def-minimiser-continuation`, 38506–38520) |
| CMP 102b §G: (172), (173) with (19)–(21), (181), Proposition 9 | chart of $G$-valued data; value bound of the Landau potential; analyticity; agreement at $G$-valued data; gauge extension | cited by statement (CA-I 166633; Definition `4.10:def-minimiser-continuation` (a)–(d), 38500–38634: "The proofs are Bałaban's and are not reproduced"). The derivative bounds (189)–(190), printed without the calculation, are not used |
| CMP 98 Proposition 2 | data of a regular field obey (7) with $\varepsilon_1=C_7\varepsilon_0$ | cited by statement (CA-I 166629); $C_7\ge2$ fixed at CA-I 17533 |
| CMP 98 Propositions 4 and 6 | bounds for $Q$ ((131), (134)–(135)) and for the group average ((159)–(164)) at a flat base | Proposition 6 cited by statement (CA-I 166629), Proposition 4 cited at CA-I 13993; (134)–(135) read from the printed page, p. 38, as the OCR is damaged |
| Lemma `4.6:lem-averaging-locality` (CA-I 24239) | two-block locality of the averages | cited (CMP 98) |
| Lemma `4.5:lem-literal-frame` (CA-I 17519–17597; proof 17673–17778) | (AX1), (AX2-poly), first paragraph of (AX3) | proved; these clauses do not use its hypotheses (A), (C) or (AX2-pt) |
| Definition `4.8:def-tower-rules` (CA-I 32834–32981) | the rules and separations; $\mathfrak r_2$ meets CMP 102b (1); (4.8:eq-tower-rules-a) | definition, with the properties proved after it |
| Lemma `4.10:lem-averaged-data` (CA-I 38430), Theorem `4.10:thm-existence-set` (CA-I 39170) | holomorphy of the averaged data and of the continued minimizer on the existence set | proved |
| Lemma `9.3:lem-refinement` (CA-III 36939–37000) | fibre inclusion for a refined tower | proved; stated on the torus $T_\eta$, its proof applies on the window unchanged |
| Definitions `4.26:not-gauge-action`, `4.26:def-block-axial` (CA-I 129758, 130021) | the action (1) and its composition rule; the block-axial tree conditions | definitions; the composition rule is proved there |
| CMP 109 (3.30), (3.31), (3.37), (3.38), Lemma 4, restrictions of §3 | the datum; the statement being completed | cited by statement (CA-I 166634) |

## 4. Proof

There are two quantitative tasks: prove the nesting identity for **every** datum in one fixed ball, uniformly in towers, depths and domains (Steps 1–3, 6, 7); then put every admitted datum in that ball (Step 4). This avoids appealing to openness of an existence set, which gives no uniform radius.

### 4.1 Conventions

The averages are Bałaban's group averages $M^q$ of CMP 98, and the auxiliary potential average is his $Q$. The window is $\square_0=\tilde\square^{5}$, and $\square_j\supset\tilde\square^{4}$ (CMP 109 §3; CA-I 33669–33671). The domain is $Z\subset X\subset\tilde\square^{2}$, as in CA-I 33602–33618 and 33654–33676: a sub-domain of the output domain, not a change of boundary values at the edge of the window. Empty terminal members of a tower are allowed.

In Steps 1–3, 6 and 7 lengths are in outer units: the outer top block has side $1$, the fine spacing is $\xi_j=L^{-j}$, a level-$q$ block has side $L^{q-j}$. Step 4 uses the $\eta$-units of CMP 109. The matrix norm is the operator norm, and $\|D\|_\infty$ is the supremum over **all** determining bonds, the fine shell included. Logarithms are in the identity chart of $G^c$ (Lemma `4.10:lem-principal-logarithm`), and all neighbourhoods below stay in it. $\mathbf H_j(\square_0,\cdot)$ and $u_j(\cdot)$ are the functions of CMP 102b §G and Proposition 9 at base datum $1$. The constants $a_0,a_1,B_3$ of Theorem 1 depend on $(d,L)$ only; $C_1,B_5$ are those of (172)–(173).

### 4.2 Step 1: one chart for every tower, and a bound on the potential

Fix $\varepsilon_*>0$ below the thresholds of Theorem 1 and §G and below the account's $\bar\varepsilon_1$, with $B_3\varepsilon_*<a_0/4$. The datum $1$ satisfies (7) with every positive parameter on every admissible tower, so §G applies at base $1$ with $\varepsilon_1=\varepsilon_*$. Choose $0<r\le\min\{\frac14,\frac14C_1\varepsilon_*\}$. If $\|B\|_\infty<r$, then $|e^{iB}-1|\le e^{r}-1<C_1\varepsilon_*$, which is (172) at base $1$. So for every admissible tower $\mathcal S$, of every depth and domain, the base-one chart contains $\{\|B\|_\infty<r\}$. There the Landau potential $\mathbf H_{\mathcal S}(B)$ is holomorphic and, by (173), satisfies (19)–(21) with $\varepsilon_2=B_5\varepsilon_*$. With $\ell_{\mathcal S}(b)$ the local block side, the first inequality of (19) gives
$$N_{\mathcal S}(B):=\sup_b\,\ell_{\mathcal S}(b)\,|\mathbf H_{\mathcal S}(B)(b)|\le B_5\varepsilon_*\qquad(\|B\|_\infty<r). \tag{5}$$
Also $\mathbf H_{\mathcal S}(0)=0$: at datum $1$ the axial minimizer is $1$, its Landau field is $0$, and §G fixes that branch.

Fix $B$ with $0<\|B\|_\infty<r$, a bond $b$, and a linear functional $\varphi$ of norm one on $\mathfrak g^c$. Then $f(z)=\varphi\bigl(\ell_{\mathcal S}(b)\,\mathbf H_{\mathcal S}(zB/\|B\|_\infty)(b)\bigr)$ is holomorphic on $|z|<r$, $f(0)=0$ and $|f|\le B_5\varepsilon_*$. The Schwarz lemma gives $|f(z)|\le B_5\varepsilon_*|z|/r$. Put $z=\|B\|_\infty$ and take the supremum over $\varphi$ and $b$:
$$N_{\mathcal S}(B)\le K\|B\|_\infty,\qquad K:=B_5\varepsilon_*/r\qquad(\|B\|_\infty<r). \tag{6}$$
$K$ depends neither on the dimension of the configuration space nor on the depth or domain. Only the value and analyticity statements of Proposition 9 are used, not (189)–(190).

### 4.3 Step 2: the averaging estimate and the seam test

Port CMP 98 Proposition 6 at the reference field $U_0=1$, and Proposition 4 for $Q$. There are $a_{98}\in(0,2\log\frac43]$ and $C_A\ge1$, depending on $(d,L)$ only, such that the following holds. Let $c$ be a level-$q$ output bond of side $s$, $h$ the fine spacing, and $E$ the two-block carrier of $c$ (Lemma `4.6:lem-averaging-locality`). If the $\mathfrak g^c$-valued potential $F$ has $s\sup_E|F|<a_{98}$, both averages are defined and holomorphic, and
$$\Bigl|\tfrac1i\log M^q(e^{ihF})(c)\Bigr|\le C_A\,s\sup_E|F|,\qquad |Q_q(hF)(c)|\le C_A\,s\sup_E|F|. \tag{7}$$
These are two bounds; the two maps are not identified. To read Bałaban's statements in these units, replace the fine spacing by $h/s=L^{-q}$ and the potential by $sF$; at the flat base, (52) of CMP 98 holds automatically. The first bound is Proposition 6 with (159)–(164), after shrinking $a_{98}$ so the group error is below $\frac12$ and using $|\log(1+E)|\le2|E|$. The second is Proposition 4: $Q_k(U_0,\eta A)=Q_k(U_0)A+C_k(U_0,A)$ (134), $|C_k(U_0,A)|\le C_2|A|^2$ (135), with (131); the linear part is bounded, and $a_{98}$ is shrunk once more. No bound on derivatives of $F$ is needed.

*The seam test.* Let $D$ be real with $L\|D\|_\infty<a_{98}/2$. Then the test (7) of CMP 102b for $e^{iD}$ is at most $C_D\|D\|_\infty$, with $C_D:=4C_AL$. Indeed each $e^{iD(c)}$ is unitary with $|e^{iD(c)}-1|\le|D(c)|$, and a plaquette inside one layer has four such factors. At a plaquette meeting two levels, one factor is replaced by the one-level finer average (CMP 102b p. 278, (7); CA-I 18616–18620); in the units of that finer lattice, (7) bounds its logarithm by $C_AL\|D\|_\infty$. All four factors are unitary, so telescoping gives $C_D\|D\|_\infty$. The separation of the tower excludes a seam across more than one level.

### 4.4 Step 3: the ball, and admission of every inner datum

*Carriers.* Let $Z\subset X\subset\tilde\square^{2}$, $\mathfrak r\in\mathfrak R$, $1\le n\le j$, and $\mathcal T=\boldsymbol\Omega^{\mathfrak r}(Z)$ truncated at depth $n$. Every averaging carrier of a row of $\mathcal T$ lies in $Z$ (CA-I 32966–32973), and so does every gauge tree of an inner structure block. As $Z\subset\tilde\square^{2}\subset\tilde\square^{4}\subset\square_j$, all of them lie in the outer top region, where the outer local block side is $1$. (A carrier leaving $Z$ would still stay in $\square_j$: the two layers between $\tilde\square^{2}$ and $\tilde\square^{4}$ have width $2M$ in window units, and a two-block carrier has diameter at most $2dL<2M$, as $M\ge2LR_1M_1$, $R_1\ge4d$.) This holds for every $Z\subset X$, holes included.

*Admission.* By (6) for the window tower, $|\mathbf H_j(\square_0,D)|\le K\|D\|_\infty$ on $\square_j$ when $\|D\|_\infty<r$. A level-$q$ inner block has side $s=L^{q-j}\le1$, and $h=\xi_j$. So if also $K\|D\|_\infty<a_{98}$, then (7) applies to every row of $\mathcal T$ at once:
$$\|B_{\mathcal T}(D)\|_\infty:=\Bigl\|\tfrac1i\log M^{\boldsymbol\cdot}(\mathcal U(D)\restriction Z)\Bigr\|_\infty\le C_AK\|D\|_\infty . \tag{8}$$
On the fine shell the datum is $\mathcal U$ itself, with $|\frac1i\log\mathcal U(b)|=\xi_j|\mathbf H_j(b)|\le K\|D\|_\infty$, so (8) holds there too ($C_A\ge1$). Choose $\delta>0$ with
$$\delta<\tfrac r2,\qquad K\delta<\tfrac{a_{98}}2,\qquad C_AK\delta<\tfrac r2,\qquad L\delta<\tfrac{a_{98}}2, \tag{9}$$
and, with $\epsilon_W:=B_3C_D\delta$,
$$C_D\delta<\tfrac{a_1}2,\qquad C_7\epsilon_W<\tfrac{a_1}2,\qquad B_3C_7\epsilon_W<\tfrac{a_0}2,\qquad \epsilon_W<\tfrac{a_0}2 . \tag{10}$$
Conditions (10) pay for the two applications of Theorem 1 (Steps 5 and 6); both factors $B_3$ are kept. So far nothing depends on $k$, $j$, $n$ or $Z$.

Hence, on the whole polydisc $\|D\|_\infty<\delta$: $e^{iD}$ lies in the base-one chart of the window tower; $\mathcal U(D)\restriction Z\in\mathcal A(\mathcal T)$; and $M^{\boldsymbol\cdot}(\mathcal U(D)\restriction Z)=e^{iB_{\mathcal T}(D)}$ with $\|B_{\mathcal T}(D)\|_\infty<r/2$. So the inner datum lies in $\mathcal S(\mathcal T)$ with a margin, and $\mathcal U(D)\restriction Z$ lies in the existence set $\mathcal V(\mathcal T)$ of CA-I (4.10:eq-tower-quantities-2), for every tower at once.

### 4.5 Step 4: every admitted datum lies in the ball

This needs a bound on **all** determining rows of the window; CMP 109 (3.32) on $\tilde\square^{4}$ would not suffice. Units: $\eta=L^{-k}$, and a level-$q$ block has side $L^q\eta$. The incoming depth-$(k+1)$ chart of the window is read in its own units $\xi=L^{-1}\eta$, where its top block has side $1$ and a layer-$n$ block has side $\ell_n=L^{n-k-1}$. In $\eta$-units the same potential is $\mathcal A:=L^{-1}\mathbf H_{k+1}(\square_0,\frac1i\log V)$, and CMP 109 (3.30) reads (CA-I 29880–29884)
$$A=\tfrac1{i\eta}\log\bigl(e^{i\eta\mathbf A}\,e^{i\eta\mathcal A}\bigr),\qquad B=Q(\eta A)\ \text{ on }\square_0 .$$

*(i) The incoming datum.* By (AX2-poly) and the first paragraph of (AX3) of Lemma `4.5:lem-literal-frame`, on the whole twist polydisc $\mathcal P_U$ the literal axial datum $V$ (the frame of CA-I 17322–17447) satisfies, for every $c\in\mathfrak B(\square_0)$,
$$|V(c)-1|\le C_VM(\alpha_0'''+\alpha_1'''),\qquad \|B_V\|_\infty\le2C_VM(\alpha_0'''+\alpha_1'''),\qquad B_V:=\tfrac1i\log V. \tag{11}$$
The proofs of these clauses use CMP 98 Proposition 2 at the real field, Proposition 6 at that field with a complex twist, and finite contour products. They use neither (AX2-pt), nor hypothesis (C), nor the glued background, nor the identity being proved; of the input space they use conditions (i)–(ii) only. By (A1), $\|B_V\|_\infty<r/2$, so (6) for the window tower at base $1$ gives $\ell_n|\mathbf H_{k+1}(\square_0,B_V)|\le K\|B_V\|_\infty$ on every layer $n$, the collar included.

*(ii) Carriers of the outgoing rows.* Let $q\ge1$. A level-$q$ row of the outgoing depth-$j$ datum, with its two-block carrier, lies in $\square_{q-1}$, also when it points outward at $\partial\square_q$. By alignment its second block is inside $\square_q$ or is the adjacent block across one face, so its points are within one level-$q$ block side of $\square_q$; and $\operatorname{dist}(\square_q,\square_{q-1}^c)$ exceeds that side, as $R_1\ge L$ and $\mathfrak M\ge1$. On $\square_{q-1}$ the incoming layer index is $n\ge q-1$. The row has side $s_q=L^q\eta$, which is $L^{q-k-1}$ in units $\xi$, so $s_q|\mathcal A|=L^{q-n}\,\ell_n|\mathbf H_{k+1}|$. With $|\mathbf A|<\alpha_2$ on the window (CMP 109 (3.31)) and $s_q\le L^{k+1}\eta=L$ (as $q\le j\le k+1$),
$$s_q\sup_E|\mathcal A|\le LK\|B_V\|_\infty,\qquad s_q\sup_E|\mathbf A|\le L\alpha_2 . \tag{12}$$
At $q=0$ the same bound follows directly from the fine-row bound.

*(iii) The composite potential.* If $t:=|X|+|Y|\le\log\frac43$, then $|e^{iX}e^{iY}-1|\le e^t-1$, and the logarithm series gives $|\log(e^{iX}e^{iY})|\le-\log(2-e^t)\le2t$ (integrate $e^t/(2-e^t)\le2$ from $0$). Take $X=\eta\mathbf A$, $Y=\eta\mathcal A$. As $\eta\le s_q$, (12) and (A2) give $t\le L(\alpha_2+K\|B_V\|_\infty)<a_{98}/2\le\log\frac43$. Hence
$$s_q\sup_E|A|\le2L\bigl(\alpha_2+K\|B_V\|_\infty\bigr)<a_{98}. \tag{13}$$

*(iv) The datum.* By (13), (7) for $Q$ applies to $B=Q(\eta A)$ on each row: $\|B\|_\infty\le2LC_A(\alpha_2+K\|B_V\|_\infty)$. For $|\tau|\le1$ and $|B'|<2\alpha_3$, (11) and (A3) give
$$\|D\|_\infty\le2LC_A\bigl[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr]+2\alpha_3<\delta . \tag{14}$$
The near case $\mathbf A=0$ is included. This is chart admission from the input conditions alone, without the conclusion of Lemma 4 or the near-case membership. (Reading (3.30) with $\tau\log V$ changes nothing for $|\tau|\le1$, as (6) is linear. A later Cauchy estimate on a fixed larger $\tau$-disc multiplies the first term of (14) by its radius before the amplitudes are chosen.)

### 4.6 Step 5: proof of (a)

**Lemma R (one axial configuration on an orbit).** Let $\mathcal S$ be an admissible tower, with the blocks, roots and gauge trees of Notation `4.26:not-gauge-trees`, and let $Y$ be block-axial for $\mathcal S$ (Definition `4.26:def-block-axial`). Let $h$ equal $1$ at every determining site of $\mathcal S$. If $Y^h$ is block-axial too, then $h=1$, so $Y^h=Y$.

*Proof.* Covariance of the averages gives $M^m(Y^h)=(M^mY)^{h|_{\Lambda_m}}$ (proof of Definition `4.26:not-gauge-action`). On a bond $b$ of a gauge tree $\mathcal T_m(B')$ both averaged values are $1$, so $h(b_-)=h(b_+)$. Each tree spans the level-$m$ sites of its block $B'$ and contains its root. The root of each structure block is a determining site, where $h=1$. Going down one level at a time, $h=1$ at every site of every block; the sites of the fine shell are determining sites. $\square$

**Proof of (a).** Let $D$ be admitted. By (14), $\|D\|_\infty<\delta$.

*(R1)* Let $D$ be real. By Step 2 and (9), $e^{iD}$ satisfies (7) with $\varepsilon_1:=C_D\delta$, strictly, as the test is at most $C_D\|D\|_\infty$; and $\varepsilon_1<a_1/2$ by (10). So Theorem 1 applies to the window problem at depth $j$. It gives a minimal orbit $\mathcal O$ in the space (8), $\mathfrak U_j(\{\square_q\},\epsilon_W)\cap\mathfrak B_j(\cdot\,,e^{iD})$, with $\epsilon_W=B_3\varepsilon_1$. As $\epsilon_W<a_0/2$, Theorem 1 at $\varepsilon_0=a_0/2$ also makes $\mathcal O$ the unique critical orbit in the space (6).

*(R2)* Let $Y$ minimize the action (5) over (8). The space (8) is cut out of the constraint set by the strict inequalities (2). So every differentiable curve $Y(t)$ in the constraint set with $Y(0)=Y$ stays in (8) for small $|t|$, on both sides of $0$; the action along it is minimal at $t=0$, so its derivative there is $0$, and $Y$ is critical. As $\epsilon_W<a_0/2$, $Y$ lies in (6) at $\varepsilon_0=a_0/2$. So the orbit of $Y$ is $\mathcal O$: there is only one minimal orbit in (8).

*(R3)* The orbits are those of the gauges (4), which equal $1$ at the determining sites. The minimal configuration that Bałaban constructs is axial and is denoted $U_k(V)$ (CMP 102b p. 307; CA-I 38518–38520), so $\mathcal O$ contains the axial configuration $W=U_j(\square_0,e^{iD})$; by Lemma R it contains no other. This is the uniqueness Lemma 4 uses: $D\mapsto U_j(\square_0,e^{iD})$ is well defined.

*Complex data.* By (14), $\|D\|_\infty<\delta<r$, so $e^{iD}=e^{iD}\cdot1$ lies in the base-one chart of the window tower: $D\in\mathcal B(1)$ in Definition `4.10:def-minimiser-continuation`, and the minimizer map at $D$ is $\Phi_1(D)$. By item (b) there it is the value of one analytic function of the datum; by item (c) it agrees with the minimizer at real data. This proves (a). $\square$

### 4.7 Step 6: real restriction to a sub-domain

Let $D$ be real with $\|D\|_\infty<\delta$, and let $Z,\mathfrak r,n,\mathcal T$ be as in Step 3. By Step 5, $W$ lies in $\mathfrak U_j(\{\square_q\},\epsilon_W)$.

*(i) A refined tower on the same window.*
$$\widehat\Omega_0=\square_0,\qquad \widehat\Omega_q=\Omega_q^{\mathfrak r}(Z)\quad(1\le q\le n),\qquad \widehat\Omega_q=\varnothing\quad(n<q\le j). \tag{15}$$
It is admissible: $\operatorname{dist}(\square_0^c,\Omega_1(Z))\ge\operatorname{dist}(Z^c,\Omega_1(Z))$ as $Z\subset\square_0$, and the later separations are the inner ones. It is memberwise smaller than the window tower, as $\Omega_q(Z)\subset Z\subset\square_j\subset\square_q$. Rule $\mathfrak r_2$ meets CMP 102b (1) with block $\mathfrak M$ and $R=R_\star'\ge R_1$ (CA-I 32975–32981), so both rules are read at the common gap $R_1$. Empty terminal members change neither rows nor action and are discarded. If $\Omega_1(Z)$ is empty, every inner bond is prescribed and (17) is immediate.

*(ii) Refinement.* Apply the proof of Lemma `9.3:lem-refinement` to the window tower and (15). The window averages are compositions of the averages of (15), so the fibre of the refined data $\widehat V:=M_{\widehat{\mathfrak B}}(W)$ lies in the fibre of the original data, and $W$ is minimal, hence critical, for $(\widehat{\mathfrak B},\widehat V)$. In that proof the refined data obey (7) with parameter $2B_3\varepsilon_1\le C_7\epsilon_W$ ($C_7\ge2$), so its use of Theorem 1 is covered by (10). This imports the fibre inclusion for the actual averages with their seam rows; it does not say a minimizer is insensitive to its boundary data.

*(iii) Change of action domain.* Let $V(t)$ be a differentiable curve on $Z$, $V(0)=W\restriction Z$, that keeps the inner data $M^{\boldsymbol\cdot}(W\restriction Z)$ fixed, and extend it by $W$ to $\widehat V(t)$ on $\square_0$. The inner level-zero data fix every bond of $Z$ except those touching $\Omega_1(Z)$, and by the first inner separation every plaquette containing such a bond lies in $Z$. All other plaquette terms are constant in $t$, so
$$\frac{d}{dt}A_{\square_0}\bigl(\widehat V(t)\bigr)\Big|_{t=0}=\frac{d}{dt}A_Z\bigl(V(t)\bigr)\Big|_{t=0}. \tag{16}$$
The extended curve keeps the refined data fixed: its positive-level rows are the inner rows, since the averages read the field on $Z$ only (CA-I 32966–32973), and every extra level-zero row is fixed. For small $|t|$ it stays in the open regular class of the refined problem, which contains $W$. By (ii) the left side of (16) is $0$, so $W\restriction Z$ is critical for the inner problem. The same-domain refinement lemma alone would not give this.

*(iv) Inner uniqueness.* The local block sides of $\mathcal T$ are at most those of the window tower, so the bounds defining the inner regular class are weaker (as in the proof of Lemma `9.3:lem-refinement`), and $W\restriction Z$ is in that class at parameter $\epsilon_W$. By CMP 98 Proposition 2 the inner data satisfy (7) with parameter $C_7\epsilon_W<a_1/2$. Theorem 1 for the inner problem gives a minimal orbit, of regularity $B_3C_7\epsilon_W<a_0/2$, which is the unique critical orbit in the inner space (6) at $\varepsilon_0=a_0/2$. That space contains $W\restriction Z$, as $\epsilon_W<a_0/2$; by (iii), $W\restriction Z$ is on the inner minimal orbit.

*(v) The axial representative.* The inner block-axial conditions sit on globally aligned trees inside structure blocks of level at most $n\le j$, and these blocks lie in $\square_j$, where $W$ is block-axial for the window tower (CA-I 130021–130052). So the inner conditions are among the outer ones, and $W\restriction Z$ is inner axial. By Lemma R,
$$U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(W\restriction Z)\bigr)=W\restriction Z . \tag{17}$$
By the argument of (R2), the inner problem too has exactly one minimal orbit in its space (8). Nothing is said about minima outside Bałaban's regular spaces.

### 4.8 Step 7: complex nesting, and proof of (b)

Let $D$ be real with $\|D\|_\infty<\delta$. As $\mathcal U=W^{u_j^{-1}}$, covariance gives $M^{\boldsymbol\cdot}(\mathcal U\restriction Z)=(M^{\boldsymbol\cdot}(W\restriction Z))^{v}$, with $v$ the restriction of $u_j^{-1}$ to the sites of the constraint lattices of $\mathcal T$. The fine-lattice gauge $\tilde v$ that (181) attaches to $v$ (Definition `4.10:def-minimiser-continuation` (d)) is constant on each structure block with the value of $u_j^{-1}$ at its root, and equals $u_j^{-1}$ on the fine shell; that is, $\tilde v=\bar u^{-1}$. By (181), (17) and (1),
$$U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U)\bigr)=\Bigl[U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(W\restriction Z)\bigr)\Bigr]^{\bar u^{-1}}=(W\restriction Z)^{\bar u^{-1}}=\bigl((\mathcal U\restriction Z)^{u_j}\bigr)^{\bar u^{-1}}=(\mathcal U\restriction Z)^{\bar u^{-1}u_j}. \tag{18}$$

Both ends of (18) are holomorphic on the whole ball $\|D\|_\infty<\delta$. Left: $D\mapsto\mathcal U(D)\restriction Z$ is holomorphic and, by Step 3, maps the ball into $\mathcal A(\mathcal T)$ with data in $\mathcal S(\mathcal T)$, where the averaged data and the continued minimizer are holomorphic (Lemma `4.10:lem-averaged-data`; Definition `4.10:def-minimiser-continuation` (a)–(b); Theorem `4.10:thm-existence-set`). So the left end is the actual inner continuation, not one assumed outside its domain. Right: $\mathcal U(D)$ and $u_j(D)$ are holomorphic (§G, Proposition 9), $\bar u$ consists of root values of $u_j$, and inversion is holomorphic. The two ends agree on the real points of the ball, an open subset of the real form $\mathfrak g^{N}$ of $(\mathfrak g^{c})^{N}$, $N$ the number of determining bonds. By the identity theorem, one complex coordinate at a time in a real basis and then over the connected ball, (18) holds on the whole ball. With (14), this is (3) at every admitted datum.

By the path formula of (1), $\partial(U^h)(p)=h(x)\,\partial U(p)\,h(x)^{-1}$ at the base point $x$ of $p$, and the current of $U^h$ is $R(h)$ of the current of $U$; inner top-block units give the factor $(L^n\xi_j)^3$. This is (4), the account's (4.8:eq-near-case-labels-2) with $g$ in the order (2). The scalar bounds the account derives from (4) (CA-I 33698–33780, 31085–31131) are proved there and not repeated. They use only $\|\operatorname{Ad}_g^{\pm1}\|\le|g|\,|g^{-1}|$ and bounds on $u_j^{\pm1}$, $\bar u^{\pm1}$, which give the same estimate for both orders of the product. This proves (b). $\square$

### 4.9 Order of choice

1. Fix $d$, $G$, $\beta$; then $L$ with the account's floors; then the propagator and averaging constants, block sizes and gaps, keeping the account's order $C_1,C_H,\bar\varepsilon_1$. Then choose $\varepsilon_*$, $r$, $K=B_5\varepsilon_*/r$, $a_{98}$, $C_A$, $C_D=4C_AL$, $C_7$ (CA-I 17533) and $\delta$ by (9)–(10). None depends on $k$, $j$, $n$, $p$ or $Z$.
2. Choose $B^{(109)}$ and $M$ with their existing one-sided floors. No upper bound on $M$ is imposed.
3. Choose the amplitudes in the order recorded in the account (CA-I 34745–34883): $\alpha_1$ for its existing conditions; $\alpha_0$ for its existing conditions, including those relative to $\alpha_1$; $\alpha_3$ for $4B_3\alpha_3\le\beta L^{-2}\alpha_0$ and $2B_3\alpha_3<\frac12\alpha_1$; $\alpha_2$ for $c\,\alpha_2\le\alpha_3$. Then decrease them, in the same order, until
$$\text{(A1)}\ \ 2C_VM(\alpha_0'''+\alpha_1''')<\tfrac r2,\qquad
\text{(A2)}\ \ 2L\bigl(\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr)<a_{98},\qquad
\text{(A3)}\ \ 2LC_A\bigl(\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr)+2\alpha_3<\delta ,$$
together with the ceilings of Lemma `4.5:lem-literal-frame` that (AX1) and (AX2-poly) use (among them $\alpha_1'''\le\min\{\alpha_1^{(98)},1\}$, $2C_vM\alpha_1'''\le\frac16$ and the real-curvature threshold of CMP 98 Proposition 2), and with the bound on $|V-1|$ in (11) inside the logarithm chart.

Each new inequality has a positive right side fixed by earlier constants and survives decreasing the amplitudes. Each existing coupling bounds a later amplitude by an earlier one ($\alpha_0$ by $\alpha_1$; $\alpha_3$ by $\alpha_0,\alpha_1$; $\alpha_2$ by $\alpha_3$), so decreasing in the same order closes without a cycle. This specifies "sufficiently small and satisfying all the restrictions" in CMP 109 Lemma 4 (p. 280), independently of $Z$, the number of blocks and the depth. At the account's running radii $\alpha_{\cdot,i}$, (A1)–(A3) are imposed on every running radius; they have the same form, so no new obstruction arises. No current estimate and no conclusion of another open statement is used.

## 5. Remarks and scope

### 5.1 The order of the gauge factors

Under the action (1), which is CMP 109 (1.10), the chain of equalities in (3.38) fixes the acting element as $g=\bar u^{-1}u_j$, pointwise $g(x)=u_j(y)^{-1}u_j(x)$ with $y$ the root of the block of $x$. The reversed product $u_j\bar u^{-1}$, or $u_j(x)u_j(y)^{-1}$, is printed at CA-I 29236, 31077, 31110, 33615–33616, 33686–33689, 33701–33703 and 121436–121437, and in CMP 109 (3.38), p. 278. It is the product for the mirrored action $U^h(b)=h(b_-)^{-1}U(b)h(b_+)$, discussed at CA-I 130178–130191, whose remark says the acting element is "the one fixed by the chain of equalities". The account uses the order (2) at CA-I 121440 and 123129. The correction is needed for the printed identity to be literally true, and it changes no estimate: every consumer uses only $\|\operatorname{Ad}_g^{\pm1}\|\le|g|\,|g^{-1}|$ (CA-I 33698–33735, 31085, 121448–121455), which is the same for both orders. The two products need not act alike, and no equality between them is used.

### 5.2 Uses of (3.38) outside the statement

The proof covers the near case and the §4.7 nesting uses (CA-I 32422; 31104–31112 at labels $(p,Z)\in\mathfrak T_{i'}(X)$, $Z\subset X\subset\tilde\square^{2}$), provided the radius $\alpha^{\sharp}_{3,i'}$ of the latter is at most $2\alpha_3$ at the running radii. Other uses need the mechanism of Steps 3, 6 and 7 in a general form: if $W=\mathcal U^{u}$ is an outer axial minimizer with datum in the $\delta$-ball of a base-one chart, and $\mathcal T$ is an admissible inner tower (holes and several components allowed) whose carriers and trees lie in the outer top region and whose blocks are no larger than the outer top block, then
$$U_{\mathcal T}\bigl(M_{\mathcal T}\,\mathcal U\bigr)=\bigl(W\restriction\mathcal T\bigr)^{\bar u_{\mathcal T}^{-1}}=\bigl(\mathcal U\restriction\mathcal T\bigr)^{\bar u_{\mathcal T}^{-1}u},$$
where the relative gauge $\bar u_{\mathcal T}^{-1}u$ is in general not constant on blocks, and is $1$ at depth zero. With explicit radius ceilings in the account's order of constants, this covers the stage-composite uses of §§4.26 and 4.28, the graded cover included (CA-I 121185–121522, 123126–123129, 144933), and the local-box restriction at CA-II 35714, whose ceiling uses $C_Q:=\max\{1,K_{\rm loc}/(5.6K_{\rm ax}MC_M^{\rm av})\}$ from CA-II 35666. For the stage composites the identity is proved, not the sharp bound $\|g\|\,\|g^{-1}\|\le G'_\square$ that the account keeps as a separate hypothesis (CA-I 121440–121455, 123129–123132).

Three stronger readings are **not** covered:

1. **§4.31(a) and (c)** (CA-I 154354–154376, 154397–154405; cited at 154420) ask for a gauge constant on blocks acting on the Landau representative. In Bałaban's reading this is false at arbitrarily small real data. Take a box with an interior level-one block, a tree bond $b$ of it in direction $1$, $T=\operatorname{diag}(1,-1)$, and the flat abelian field $\mathcal U_a(x,x+he_1)=e^{ihaT}$, $\mathcal U_a=1$ in the other directions, $0<|ha|<\pi$. It has curvature $1$ and current $0$, it is the small Landau representative of its data, and the inner axial minimizer is $1$ on $b$; but a block-constant $v$ gives $\mathcal U_a^{v}(b)=v\,e^{ihaT}v^{-1}\ne1$. The account's §4.7 (CA-I 29234–29239) and Bałaban's (3.38) carry the factor $u_j$, which is not block-constant; the quotation at CA-I 154423 has $U_j$ where Bałaban has $u_j$. The consumers (N1)–(N3) of §4.31 read only norm bounds and values of a gauge-invariant function $f$, which the corrected identities give, so their proof does not change.
2. **§4.31(b)** (CA-I 154378–154395): the bound "both norms at most $2$" for every allowed gauge is not established. It is not needed: the consumer at CA-I 156050 needs only equality of values of $f$, which is proved on its full datum range.
3. **CA-II 44422, 44454** cite (3.38) for a bound on a potential. Step 1 gives a weighted bound of that form with $K$ in place of $B_3$; the anchor and path-integral bounds needed on $X_T$ are proved, but an unweighted bound on the whole graded rim is not.

### 5.3 What is not proved

Nothing is claimed about minima outside Bałaban's regular spaces (6) and (8), and nothing is minimized at complex data. Locality is the nesting identity, not a finite-range response of the minimizer to distant changes of its data. The consumers' scalar estimates are the account's and are not proved again. The derivative bounds (189)–(190) of CMP 102b are neither used nor proved. The published inputs and the cited Lemma `4.6:lem-averaging-locality` are used as cited. The next statement, Lemma `4.13:lem-own-constant` (CA-I 45203), is not addressed.

## 6. Credit

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at commit `31a47c543775`: the statement of Lemma 4.13 and its Route; the tower rules of §4.8; the continuation convention of §4.10; the literal-frame Lemma 4.5; the refinement Lemma 9.3; the gauge-action and block-axial definitions of §4.26; and the consumers, whose estimates are used as they stand. Tadeusz Bałaban for the constrained minimizer and its analytic continuation (CMP 102b), the averaging operations (CMP 98), and Lemma 4 with the nesting identity (3.38) (CMP 109).

The proof written up here is Codex's (`library/mu.md`), checked line by line by Claude (`gates/mu-gate.md`), first failing step none. CMP 98 Proposition 4 was read from the printed page by the lead (Claude). The carry-over in §5.2 is Codex's (`library/mu-radii.md`), checked line by line by Claude (`gates/mur-gate.md`), with one repair, applied here. This write-up is Claude's and has not been checked by the other model.
