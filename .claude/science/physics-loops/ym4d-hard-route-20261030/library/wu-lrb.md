lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T15:25Z

# A proof of Proposition 4.4:prop-local-real-base (the local real base of a polymer)

Draft for the owner's review. It is not sent anywhere. Research text: it grants no status and makes no public claim.

**Credit.** The proposition, its notation, its setting and the parts of its proof printed at CA-I 8391–8759 are from the complete account of Theorem 0 by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text** (repository `ethanwsussman/Yang--Mills-LLM-experiment`, commit `31a47c543775`; CA-I = `theorem_0_complete_account_raw_I.tex`, CA-II = `..._II.tex`, CA-III = `..._III.tex`). The walk interpolation, the cluster integral and the setting (2.14) are **Tadeusz Bałaban's** (CMP 116, §§1–2; the polydisc bounds are CMP 109 (1.13)–(1.14)). The proof of the parts the account leaves open was written by Codex in `library/lrb.md` (frozen 2026-11-05). Claude checked it line by line in `gates/lrb-gate.md`: first failing step none, eight repairable findings. This write-up applies those eight repairs. It was written by Claude (Opus 5.5, max effort) from those two texts and the account's source; it adds no new mathematical claim.

Source hashes (SHA-256, checked for this write-up): CA-I `4cb5cb5e…6e93`, CA-II `6a1f74b0…b2b8f`, CA-III `7e36523b…352d`, `YM4_sketch_500.tex` `d7f77d4d…4b6f`; they match `library/lrb.md` §1.

## Result

**Kind:** proof of a statement their account leaves outstanding (FINISH, How we work, item 9).

Proposition 4.4:prop-local-real-base holds as stated, under its hypotheses (a)–(d) and in its setting [B-CMP116, (2.14)], with the readings R1–R4 of §4 and the scope limits of §6. Every clause is proved: (1), (2σ), (2U), (2s), (2Γ), (3), (4a), (4b), (4c).

- The account marks the proposition "Proof outstanding" (CA-I 8110, 8373). It prints proofs of (1), (2s), (2Γ) (CA-I 8391–8562) and of (3), (4) (CA-I 8564–8759). The second of these takes six further statements as hypotheses (CA-I 8566–8573).
- This note supplies what those printed parts lack: (2σ); (2U); the kernel and product bounds of the σ-families; the four perturbation estimates of (4a)(i)–(iv); an explicit majorant for the Gaussian vertex integral in (4b); and analyticity of f on a neighbourhood of the closed σ-polydisc in (4c).
- The result is an implication. It does not prove the upstream premises named in §3 and §6, in particular Lemma 4.4:lem-reality-symmetry, whose statement the account does not write out.
- No step uses a computation. Every step is a written inequality.

## 1. The statement as their account prints it (CA-I 8110–8371)

Transcribed from the LaTeX source. The words and symbols are theirs; only the typesetting changes. Displayed labels are theirs.

> **Proposition 4.4:prop-local-real-base** (The local real base of a polymer. Proof outstanding). Assume the following.
>
> (a) The hypotheses of Lemma 4.4:lem-local-coercivity hold, together with those of the lemma on the symmetric part of the localised form, whose application is Corollary 4.4:cor-polymer-base-form. Among them are (W$'$) with its local half, (k1), (k2), (k2$'$) and (k3).
>
> (b) The two inequalities $\theta_K LM\ge 648\,\kappa_1$, $e^{243\kappa_1}\le e^{\theta_K M/64}$ hold. Put $\bar\eta:=e^{-\theta_K M/64}$.
>
> (c) The walk-counting bound holds. Consider cubes of side $LM$ and walks whose step domains have diameter at most $LM/4$; here the diameter is at most $4\ell\le M/12$. A walk $\varpi$ from $b$ to $b'$ that meets $m$ of these cubes satisfies $m\le 81\bigl(2\,d(\varpi;b,b')/(LM)+1\bigr)$, where $d(\varpi;b,b')$ is the length of $\varpi$ between $b$ and $b'$ in the sense of that bound.
>
> (d) The three floors of Definition 4.4:def-base-floors hold.
>
> We work in the setting of [B-CMP116, (2.14)], which we now describe.
> - $Z_0\in\mathbf D_k$.
> - $Z\supset Z_0'$, where $Z_0'$ is the enlargement of $Z_0$ fixed in Corollary 4.4:cor-polymer-base-form, and $Z$ is a closed union of $M_1$-cubes with $Z\subset\Omega_{k+1}$. In the setting $\mathcal S_0$ any $Z$ is admitted.
> - $\sigma_0$ is the family of cubes of side $LM$ of Definition 4.4:def-interpolation-rule, and $\sigma:=(\sigma(\Delta))_{\Delta\in\sigma_0,\ \Delta\subset Z\setminus\operatorname{int}Z_0'}$ is a family of complex numbers with $|\sigma(\Delta)|\le e^{\kappa_1}$.
>
> Let $K$ be one of the three families $\mathsf A$, $C:=\mathsf R^{\mathbb B(Z_0)}(0)$, $\mathsf M:=\mathsf M^Y$. Here $Y$ is the region carrying the family $\mathsf M$, as in Corollary 4.4:cor-polymer-base-form. Each of the three families has the walk expansion $K=\sum_\varpi K_\varpi$ of Lemma 4.4:lem-cell-resolvent(v). For a walk $\varpi$ of it, let $\sigma_0(\varpi)$ be the set of cubes of $\sigma_0$ that meet its footprint $|\varpi|$, and put $m(\varpi):=\#\sigma_0(\varpi)$. For a local datum $\mathsf u$ on $Z$, set, according to the interpolation rule of Definition 4.4:def-interpolation-rule,
> $$K(\sigma;\mathsf u):=\sum_{|\varpi|\subset Z}K_\varpi\bigl(\mathsf u|_{|\varpi|}\bigr)\prod_{\Delta\in\sigma_0(\varpi)}\sigma(\Delta).$$
> Since $W(\emptyset)=Z_0'$, we have $K(0;\mathsf u)=K^{Z_0'}(\mathsf u)$. Put $C(Z_0,\sigma;\mathsf u):=C(\sigma;\mathsf u)$. By Corollary 4.4:cor-localised-covariance, $C(Z_0,0;\mathsf u)^{-1}=\mathsf T_{Z_0'}(\mathsf u)$. Let $\chi_{Z_0}$ and $\chi_{Z_0^c}$ denote multiplication by the indicators of $Z_0$ and of its complement, and set
> $$\Gamma(\sigma;\mathsf u):=\chi_{Z_0}\,\mathsf A(\sigma;\mathsf u)\,\chi_{Z_0^c}\,\mathsf M(\sigma;\mathsf u).$$
> This is the product of the two separately weighted families: the interpolation rule is applied to each operator on its own.
>
> Let $(U|_Z,0)$ be the real local base of the polydiscs $\mathbf P_{\cdot,Z}$ of Definition 4.4:def-regular-backgrounds. Let $\mathsf u=(e^{i\xi A'}U,\mathbf J)\in\mathbf P_{\varsigma,Z}$ with $0<\varsigma\le1+\beta$ and $\rho\ge2\varsigma$. Define the *local real base* by
> $$T_0:=\mathsf T_{Z_0'}(U|_{Z_0'},0),\quad A_0:=\operatorname{sym}\operatorname{Re}T_0,\quad C_0^{\rm cv}:=A_0^{-1},\quad \Gamma_0:=\Gamma(0;U,0),\quad \Gamma_0^{\mathbb R}:=\operatorname{Re}\Gamma_0.\tag{local-real-base-1}$$
> Here $\operatorname{sym}$ denotes the symmetric part: $\operatorname{sym}\operatorname{Re}T_0=\tfrac12\bigl(\operatorname{Re}T_0+(\operatorname{Re}T_0)^{\top}\bigr)$. In (2s), (2Γ) and (4) below, $\mathsf r_s$ and $\eta_{\rm sym}=4\mathsf Be^{-\theta_K\mathsf r_s/2}$ are those of Corollary 4.4:cor-polymer-base-form. Then the following hold.
>
> **(1) Base.** The operators $A_0$ and $C_0^{\rm cv}$ are real symmetric, and
> $$\tfrac58\gamma_*\le A_0\le\mathsf B,\qquad \mathsf B^{-1}\le C_0^{\rm cv}\le\frac{8}{5\gamma_*},\qquad |A_0(b,b')|\le\mathsf Be^{-\delta_{\mathsf A}|b-b'|}.\tag{local-real-base-2}$$
> The operator $\Gamma_0^{\mathbb R}$ is real, and $|\Gamma_0^{\mathbb R}(b,b')|\le|\Gamma_0(b,b')|\le\mathsf BB_{\mathsf M}\mathsf S\,e^{-(\theta/2)|b-b'|}$. Here $\mathsf S:=\sup_b\sum_{b'\in\mathbb B(T)}e^{-(\theta/4)|b-b'|}$ is a number that depends only on $d$, $L$ and the gauge group, and is fixed before $M$.
>
> **(2) Displacement of the true operators from the base, kernelwise with decay.** The following hold at every $\mathsf u\in\mathbf P_{\varsigma,Z}$ and every $\sigma$ with $|\sigma(\Delta)|\le e^{\kappa_1}$.
>
> **(2σ)** This clause holds at every $\mathsf u\in\mathbf P_{\rho,Z}$, the full radius; it is in this form that (2U) and (3) use it. Let $K\in\{\mathsf A,C,\mathsf M\}$. Let $b$ be a row with $\operatorname{dist}_\infty(b_-,Z_0)\le M/4$, where $b_-$ is the initial point of the bond $b$; for $K=C$, let $b$ be any row and $b'$ any column. Then
> $$\sum_{\varpi:\,m(\varpi)\ge1}|K_\varpi(\mathsf u)(b,b')|\,e^{\kappa_1m(\varpi)}\le B_K\,\eta_1\,e^{-(3\theta_K/8)|b-b'|},\tag{local-real-base-3}$$
> where $\eta_1:=e^{81\kappa_1-\theta_KM/8}\le e^{-23\theta_KM/192}\le\bar\eta$. Hence, at such rows, $\bigl|[K(\sigma;\mathsf u)-K^{Z_0'}(\mathsf u)](b,b')\bigr|\le B_K\eta_1e^{-(3\theta_K/8)|b-b'|}$, and
> $$\lvert\!\lvert\!\lvert C(\sigma;\mathsf u)-\mathsf T_{Z_0'}(\mathsf u)^{-1}\rvert\!\rvert\!\rvert_0\le\frac{8S}{\gamma_*}e^{81\kappa_1-\theta_KM/4}\le\frac{8S}{\gamma_*}e^{-47\theta_KM/192}.$$
>
> **(2U)** For $K\in\{\mathsf A,C,\mathsf M\}$,
> $$\bigl|[K^{Z_0'}(\mathsf u)-K^{Z_0'}(U,0)](b,b')\bigr|\le B_Ke^{-\theta_K|b-b'|}\frac{\varsigma}{\rho-\varsigma},\qquad \lvert\!\lvert\!\lvert K^{Z_0'}(\mathsf u)-K^{Z_0'}(U,0)\rvert\!\rvert\!\rvert_0\le B_K\frac{\varsigma}{\rho-\varsigma}.$$
> The same two bounds hold for the σ-families, that is, for $K(\sigma;\mathsf u)-K(\sigma;U,0)$, after a replacement of constants. At all rows, $(B_K,\theta_K)$ is replaced by $(2B_Ke^{81\kappa_1},3\theta_K/8)$. At rows within sup-distance $M/4$ of $Z_0$, it is replaced by $(2B_K,3\theta_K/8)$. These two classes of rows are those of the bounds on the interpolated families, read with the count of (2σ).
>
> **(2s)** The symmetric part is close to the localised form: $|T_0(b,b')-A_0(b,b')|\le4\mathsf Be^{-\delta_{\mathsf A}\max\{\mathsf r_s,|b-b'|\}}\le\eta_{\rm sym}e^{-(\delta_{\mathsf A}/2)|b-b'|}$, and $\lvert\!\lvert\!\lvert T_0-A_0\rvert\!\rvert\!\rvert_0\le\eta_{\rm sym}$. Moreover, $\bigl|[T_0^{-1}-C_0^{\rm cv}](b,b')\bigr|\le C_s\,\eta_{\rm sym}\,e^{-\theta_s|b-b'|}$, with $C_s,\theta_s>0$ depending only on $(\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})$.
>
> **(2Γ)** For $b\in Z_0$,
> $$|\operatorname{Im}\Gamma_0(b,b')|\le\mathsf BB_{\mathsf M}\mathsf S\bigl[4e^{-\theta\mathsf r_s/2}+e^{-\theta M/4}\bigr]e^{-(\theta/4)|b-b'|}\le B_{\mathsf M}\mathsf S(\eta_{\rm sym}+\mathsf B\bar\eta)e^{-(\theta/4)|b-b'|}.$$
>
> **(3) Coercivity on the whole σ-polydisc.** Let $\mathsf u\in\mathbf P_{\rho,Z}$ (full radius) and let $|\sigma(\Delta)|\le e^{\kappa_1}$. Then $C(Z_0,\sigma;\mathsf u)$ is invertible and
> $$\operatorname{Re}C(Z_0,\sigma;\mathsf u)^{-1}\ge\tfrac38\gamma_*.\tag{local-real-base-4}$$
> Of the hypotheses, this clause uses only the two inequalities of (b) together with (k2) and (k3), and none of the three floors of (d).
>
> **(4) Applications.** Put $\hat\varepsilon:=\bar\eta+\frac{\varsigma}{\rho-\varsigma}+\eta_{\rm sym}$. Under the three floors of Definition 4.4:def-base-floors, each of the three summands is at most $\varepsilon_0^{P'}/3$. The quantity $\varepsilon_0^{P'}=\varepsilon_0^{P'}(\mathsf B,\gamma_*,S,\theta_K,\delta_{\mathsf A})$ is the threshold, given by an existence statement, below which two results apply. The first is the perturbation lemma for the Gaussian integral over the base, which holds for perturbation size $\varepsilon\le\varepsilon_0^{P'}$. The second is the estimate of [B-CMP116, (2.23)–(2.26)], where the threshold enters as the smallness of $\alpha_5$. The threshold $\varepsilon_0^{P'}$ is a function of quantities fixed before $M$. Without loss of generality it is shrunk to $\varepsilon_0^{P'}\le\min\{3,\mathsf B\}$ (Corollary 4.4:cor-polymer-base-form, Definition 4.4:def-base-floors). Then the following hold.
>
> **(4a)** The bounds on the σ-interpolated families and on their product hold on the three local families $\mathsf A(\sigma;\mathsf u)$, $C(\sigma;\mathsf u)$ and $\mathsf M(\sigma;\mathsf u)$. Their proofs use only the count in (2σ) and the bound in (2U).
> The perturbation lemma for the Gaussian integral, parts (i)–(iv), holds verbatim with the base $(\Gamma_0^{\mathbb R},C_0^{\rm cv})$ in place of $(\Gamma(0;U,0),C(Z_0,0;U,0))$, with the following changes.
> - The perturbation size $\varepsilon$ is replaced by $C_P\hat\varepsilon$, where $C_P=C_P(\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A})$.
> - The lower bound for the base covariance is replaced by $\tfrac58\gamma_*/\mathsf B^2$. Indeed, by (local-real-base-2), $C_0^{\rm cv}\ge\mathsf B^{-1}\ge\tfrac58\gamma_*/\mathsf B^2$.
> - The lower bound for the reciprocal of the norm of the base covariance is replaced by $\tfrac58\gamma_*$. This satisfies $\tfrac58\gamma_*\le1/\|C_0^{\rm cv}\|$.
> - The decay bound for the inverse base covariance is replaced by $|(C_0^{\rm cv})^{-1}(b,b')|=|A_0(b,b')|\le\mathsf Be^{-\delta_{\mathsf A}|b-b'|}$, which holds by (local-real-base-2). The Combes–Thomas step of part (i) is therefore not needed.
> - The perturbation is $E':=C(Z_0,\sigma;\mathsf u)-C_0^{\rm cv}$, bounded by (2σ), (2U) and (2s).
>
> **(4b)** Two estimates apply: the lemma that establishes [B-CMP116, (2.16)–(2.17)], and the estimate of [B-CMP116, (2.23)–(2.26)]. Their input is that $A_0:=\operatorname{sym}\operatorname{Re}\mathsf T_{Z_0'}(U,0)$ is real symmetric with $A_0\ge\tfrac58\gamma_*$. This input is not assumed: at local data it is proved in (1). In [B-CMP116, (2.24)] the base covariance $C_0^{\rm cv}=A_0^{-1}$ is symmetric. Hence the zeroth-order term cancels exactly, and the integral over $d\mu_0(X)$ in [B-CMP116, (2.25)] converges.
>
> **(4c)** Consider the functional $f(\sigma)$ of [B-CMP116, (2.8)–(2.9)], formed by the interpolation rule of Definition 4.4:def-interpolation-rule with every $K$ replaced by $K(\sigma;\mathsf u)$. It is defined and analytic on the closed polydisc $|\sigma(\Delta)|\le e^{\kappa_1}$, $\Delta\in\sigma_0$, which contains $[0,1]^{\sigma_0}$. This holds at every $\mathsf u\in\mathbf P_{\varsigma,Z}$, $\varsigma\le1+\beta$, that represents a point of the first of the two classes
> $$U^{\Sigma^1}_{k+1}(Z;(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0),\qquad U^{\Sigma^1}_{k+1}(Y';(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0),$$
> with $Z\in\mathbf D_k\supset\mathbf D_{k+1}$. For such $\mathsf u$, the restriction $\mathsf u|_{Y'}$ represents a point of the second class for every $Y'\in\mathbf D_k$ with $Y'\subset Z$. This follows from the restriction theorem for the one-power hereditary class at equal levels, which rests on $\mathfrak T_{k+1}(Y')\subset\mathfrak T_{k+1}(Z)$. These restrictions are the arguments of the potentials $V_k(Y',\cdot)$, $Y'\subset Z_0$, of $F(Z_0,B)$, in the space of [B-CMP116, (1.34)] on $Y'$. All of this holds whether or not $\mathsf u$ extends to a point of $\mathbf P_\varsigma$. In this form the hypothesis of the vertex formula (Lemma 4.4:lem-vertex-formula) is met, and in this form the later uses of $f$ depend on it.

## 2. Its status in the account

- **Outstanding.** The heading says "Proof outstanding" (CA-I 8110). The text "Proof outstanding." stands in place of a proof (8373), followed by a Route (8376–8389). In the account's convention (CA-I 39–41) this means that no complete proof is printed.
- **Printed parts.** Two continued proofs follow the Route.
  - CA-I 8391–8562 proves the second half of (2s) and all of (2Γ). It takes (1) and the first half of (2s) from Corollary 4.4:cor-polymer-base-form.
  - CA-I 8564–8759 proves (3) and (4). It takes six statements as added hypotheses (8566–8573): (1) the walk-count lemma, which is hypothesis (c); (2) the kernel lemma for walk families with its two classes of rows; (3) the product lemma for walk kernels; (4) parts (i)–(iv) of the perturbation lemma for the localised vertex covariance; (5) the positivity lemma for the Gaussian vertex integral, with its bound on [B-CMP116, (2.23)–(2.26)]; (6) the restriction theorem at equal levels, which is Theorem 4.8:thm-restriction-units (CA-I 33276, proved).
- **What is missing.** (2σ) and (2U) have only the Route (8383–8387). Statements (2)–(5) of the list are not printed: the gate searched CA-I, CA-II, CA-III and `YM4_sketch_500.tex` and found neither a label nor a statement for them (gate finding 2). This note proves (2σ), (2U), (2) and (3). It replaces (4) and (5) by explicit estimates (§5.5, §5.6).
- **Use in the account.** Corollary 4.4:cor-localised-independence (CA-I 9615) applies the proposition (9668, 9777). Part III's count of the 27 intermediate statements lists that corollary among the six proved as implications in Part II (CA-III 111054–111061).

## 3. Inputs and their status in the account

"Proved" means that the account prints the statement with a complete proof and no status sentence (CA-I 30–31).

| Input | Where | Status in the account |
|---|---|---|
| Hypotheses (a)–(d); setting [B-CMP116, (2.14)] | CA-I 8112–8143 | hypotheses of the proposition |
| Lemma on walk systems: (a) $\lvert\!\lvert\!\lvert KK'\rvert\!\rvert\!\rvert_\theta\le\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_\theta\lvert\!\lvert\!\lvert K'\rvert\!\rvert\!\rvert_\theta$; (b) $\|K\|\le\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_0$; (c) entry bound and $d(\omega;b,b')\ge\lvert b-b'\rvert$ | CA-I 4908–4984 (no label) | proved |
| Definition 4.4:def-walk-systems: $d(\omega;b,b')$, weighted norm | CA-I 4875–4906 | definition |
| Definition 4.4:def-interpolation-rule: "meets" means $\operatorname{int}\Delta\cap\lvert\varpi\rvert\ne\emptyset$; $K(1_{\sigma'})=K^{W(\sigma')}$ | CA-I 5120–5194 | identity proved |
| Definition 4.4:def-regular-backgrounds: $\mathbf P_\sigma$, $\mathbf P_{\sigma,D}$, no condition on $\partial\mathbf U$ | CA-I 4608–4698 | definition |
| (W$'$) = Definition 4.4:def-form-walk-hypothesis, including datum-free majorants (clause v) | CA-I 5519–5564 | hypothesis, through (a) |
| (k1), (k2), (k2$'$), (k3); $S$, $\theta=\theta_0/4$ (Definition 4.4:def-auxiliary-parameters) | CA-I 6095–6153 | conditions, through (a) |
| Lemma 4.4:lem-cell-resolvent (v): local families of $\mathsf R(x)$, $\mathsf M$ and their bounds | CA-I 6219, 6282–6298 | proved, under the added hypotheses of clause (v) |
| Lemma 4.4:lem-local-coercivity | CA-I 6959 | proved; its hypotheses are in (a) |
| Corollary 4.4:cor-localised-covariance: $C^{(k)}(Z_0)^{W'}=\mathsf T_{W'}^{-1}$, $\operatorname{Re}\mathsf T_{W'}\ge\frac58\gamma_*$ | CA-I 7162–7185 | proved |
| Definition 4.4:not-kernel-symmetrisation (e), (F), (G): $(B_K,\delta_K)$, domain diameters, where the bounds hold | CA-I 7474–7491, 7530–7540 | definition, with the statements it cites |
| Lemma 4.4:lem-reality-symmetry (the symmetry lemma) | CA-I 7629–7630 | "The statement of this lemma is not written out here; parts of its proof are printed below." Not counted as proved. |
| Corollary 4.4:cor-polymer-base-form (i)–(iv): $Z_0'\supseteq Z_0^{+M}$; base bounds (iii); imaginary-part bounds (ii), (iv) | CA-I 7827–7988 | printed with proof; the proof applies clauses (a), (b) of the symmetry lemma, so it stands as an implication from that lemma |
| Definition 4.4:def-base-floors: threshold $\varepsilon_0^{P'}$, which may be decreased; three floors | CA-I 7990–8108 | definition |
| Theorem 4.8:thm-restriction-units, at $i=i'$ | CA-I 33276 | proved |
| Lemma 5.2:lem-complex-fluctuation: the account's reading of [B-CMP116, §2], the term (2.14), the bound on $\sum_Y\lvert\tau(Y)\rvert\lvert V(Y,B)\rvert$ | CA-II 3521–3556 (proof to 3797) | proved, with Bałaban's potentials of form (1.42) and bounds (1.43), (1.36) as hypotheses |
| Lemma 4.4:lem-vertex-formula (reads (4c)) | CA-I 5218 | proved |

## 4. Readings and conventions

- **R1. Parameter cubes.** The cubes on which σ is defined lie in $Z\setminus\operatorname{int}Z_0'$ (setting, CA-I 8141). Only these cubes enter $m(\varpi)$ and the products. $K(0;\mathsf u)=K^{Z_0'}(\mathsf u)$, as the statement says ($W(\emptyset)=Z_0'$). The account says the same at CA-I 8746–8747.
- **R2. Norms.** For a single matrix kernel $N$ (square or rectangular) and $a\ge0$ put $|N|_a:=\max\{\sup_b\sum_{b'}|N(b,b')|e^{a|b-b'|},\ \sup_{b'}\sum_b|N(b,b')|e^{a|b-b'|}\}$. This is $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert_a$ of the one-term walk system. It is submultiplicative and dominates the operator norm (lemma on walk systems, (a), (b)). Transposition does not change it, and $|N|_a\le|N|_{a'}$ for $a\le a'$. Put $\mathcal L(c):=\sup_b\sum_{b'}e^{-c|b-b'|}$ (CA-I 8397–8399). It is finite for $c>0$, uniformly in the torus.
- **R3. The Gaussian $d\mu_C$.** $d\mu_C$ is the normalised Gaussian measure with density proportional to $e^{-\frac12B^{\top}C^{-1}B}$ (CA-I 7313–7314), and $C$ need not be symmetric (Remark 4.4:rem-symmetric-base-need, CA-I 7303–7365). For real $B$, $B^\top C^{-1}B=B^\top H_CB$ with $H_C:=\operatorname{sym}(C^{-1})$. So $d\mu_C(B)=(2\pi)^{-n_B/2}(\det H_C)^{1/2}e^{-\frac12B^\top H_CB}\,dB$ when $\operatorname{Re}H_C>0$, with the root continued from $\det A_0>0$. The normalisation holds at real positive $H_C$ by orthogonal diagonalisation, and then extends by the identity theorem in each symmetric matrix entry (`YM4_sketch_500.tex` 14023–14034). Here $n_B$ is the number of real coordinates of $B$ on $\mathbb B(Z_0)$. So $\det C^{-1}$ is in general not the normalising determinant.
- **R4. The Gaussian $d\mu_0$** (gate finding 1). $d\mu_0$ is the normalised Gaussian measure of unit covariance on the real coordinates of $X$, restricted to $Z$ [B-CMP116, (2.8)]. The account calls it "the measure of $X$" (CA-I 7311) and restricts it to $Z$ (CA-II 3622); it does not define it further, and its own argument at CA-I 8737 assumes the same. If $d\mu_0$ has instead a covariance $\Sigma$ with $\|\Sigma\|\le s_0$, replace $D_X$ by $\Sigma^{1/2}D_X\Sigma^{1/2}$ in §5.6; only early constants change (the gate's repair; not re-proved here).
- **R5. Family bounds.** At every datum of $\mathbf P_{\rho,Z}$, the local $Z$-family of each of the three families satisfies $\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_\theta\le B_K$, with $(B_{\mathsf A},B_C,B_{\mathsf M})=(\mathsf B,\,8S/\gamma_*,\,4S(2/\gamma_*)^{1/2})$; for $\mathsf A$ also $\lvert\!\lvert\!\lvert\mathsf A\rvert\!\rvert\!\rvert_{\delta_{\mathsf A}}\le\mathsf B$ with $\delta_{\mathsf A}\ge8\theta$. Sources: (W$'$) and its local half for $\mathsf A$; Lemma 4.4:lem-cell-resolvent (v) at $x=0$ for $C$, and for $\mathsf M$; Definition 4.4:not-kernel-symmetrisation (e), (G). Every step domain has sup-diameter at most $4\ell\le M/12$ (items (f), (F), and (k3)). A subfamily, such as the $Z_0'$-family, obeys the same bound. These bound absolute sums, not sums with cancellation.
- **R6. Order of constants.** (1) $\mathsf B,\delta_{\mathsf A},\gamma_*,\rho_w$ and the profile $h$. (2) $r'$ by (k1); then $r,\theta_0,\theta,S$. (3) $\ell$ by (k2), (k2$'$). (4) $\varepsilon_0^{P'}$, decreased as CA-I 8016–8017 allows, so that it also meets the finitely many smallness conditions of §§5.5–5.6. Each of these reads only $\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A}$ and lattice sums $\mathcal L(\cdot)$ at these rates. (5) $\kappa_1$ (Stage 4, CA-I 1492–1496; no $M$). (6) $M$ (Stage 6, CA-I 1537), above (k3), the two inequalities of (b), and the two $M$-floors of (d). (7) $\mathcal R_{\mathbf P}$ above its floor in (d); then the radii (CA-I 5822–5909). (8) Bałaban's free parameters $\alpha_4,\gamma_2$ get one more ceiling, (5.21) below, which is an early number; their own later ceilings stay. No early constant reads $M$, $\kappa_1$, $\alpha_4$ or $\gamma_2$, so there is no cycle.

