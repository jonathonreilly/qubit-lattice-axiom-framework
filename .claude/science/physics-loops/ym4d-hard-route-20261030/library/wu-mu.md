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

Other passages read (3.38) at other data or domains (§§4.26 and 4.28: CA-I 121185–121522, 123126–123129, 144933; §4.31: CA-I 154420; CA-II 35714), or cite it for a bound on a potential (CA-II 44422, 44454). Section 6.3 says which of these the proof covers.

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

**Theorem.** Fix $d$, $G=SU(N)$, $\beta$, $L$ and the constants that precede the amplitudes in the account's order of choice. Let $\alpha_0,\alpha_1,\alpha_2,\alpha_3$ satisfy the restrictions of CMP 109 Lemma 4, read at the proof radius $2\alpha_3$ (CA-I 34813–34817), and the further ceilings (16) and (17) of §4.9. Each of these is an upper bound fixed by earlier constants alone; none depends on $k$, $j$, $n$, $p$ or a domain. Let the fields be those admitted by Lemma 4: $\mathbf U$ in the space of that lemma, read through the twist polydisc $\mathcal P_U$ of Notation `4.5:not-axial-frame` (CA-I 17433–17460); a fluctuation $\mathbf A$ on $\square_0$ satisfying CMP 109 (3.31); $|\tau|\le1$ and $|B'|<2\alpha_3$; the datum $D=\tau B+B'$, with $B=Q(\eta A)$ as in CMP 109 (3.30). Then:

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

