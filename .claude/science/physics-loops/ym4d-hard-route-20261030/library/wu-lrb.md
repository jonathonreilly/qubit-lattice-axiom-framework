lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T15:25Z

# A proof of Proposition 4.4:prop-local-real-base (the local real base of a polymer)

Draft for the owner's review. It is not sent anywhere. Research text: it grants no status and makes no public claim.

**Credit.** The proposition, its notation, its setting and the parts of its proof printed at CA-I 8391–8759 are from the complete account of Theorem 0 by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text** (repository `ethanwsussman/Yang--Mills-LLM-experiment`, commit `31a47c543775`; CA-I = `theorem_0_complete_account_raw_I.tex`, CA-II = `..._II.tex`, CA-III = `..._III.tex`). The walk interpolation, the cluster integral and the setting (2.14) are **Tadeusz Bałaban's** (CMP 116, §§1–2; the polydisc bounds are CMP 109 (1.13)–(1.14)). The proof of the parts the account leaves open was written by Codex in `library/lrb.md` (frozen 2026-11-05). Claude checked it line by line in `gates/lrb-gate.md`: first failing step none, eight repairable findings. This write-up applies those eight repairs. It was written by Claude (Opus 5.5, max effort) from those two texts and the account's source. It adds no new result; the two supporting sentences it adds are named in the last section.

Source hashes (SHA-256, checked for this write-up): CA-I `4cb5cb5e…6e93`, CA-II `6a1f74b0…b2b8f`, CA-III `7e36523b…352d`, `YM4_sketch_500.tex` `d7f77d4d…4b6f`; they match `library/lrb.md` §1.

## Result

**Kind:** proof of a statement their account leaves outstanding (FINISH, How we work, item 9).

Proposition 4.4:prop-local-real-base holds as stated, under its hypotheses (a)–(d) and in its setting [B-CMP116, (2.14)], with the readings R1–R4 of §4 and the scope limits of §6. Every clause is proved: (1), (2σ), (2U), (2s), (2Γ), (3), (4a), (4b), (4c).

- The account marks the proposition "Proof outstanding" (CA-I 8110, 8373). It prints a proof of the second half of (2s) and of (2Γ) (CA-I 8391–8562), taking the bounds on $A_0$ in (1) and the first half of (2s) from Corollary 4.4:cor-polymer-base-form. It prints a proof of (3) and (4) (CA-I 8564–8759) that takes six further statements as hypotheses (CA-I 8566–8573).
- This note supplies what those printed parts lack: the bound on $\Gamma_0$ in (1); (2σ); (2U); the kernel and product bounds of the σ-families; the four perturbation estimates of (4a)(i)–(iv); an explicit majorant for the Gaussian vertex integral in (4b); and analyticity of f on a neighbourhood of the closed σ-polydisc in (4c).
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
  - CA-I 8391–8562 proves the second half of (2s) and all of (2Γ). It takes the bounds on $A_0$ and $C_0^{\rm cv}$ in (1), and the first half of (2s), from Corollary 4.4:cor-polymer-base-form. The bound on $\Gamma_0$ in (1) appears only in the statement (CA-I 8204).
  - CA-I 8564–8759 proves (3) and (4). It takes six statements as added hypotheses (8566–8573): [L1] the walk-count lemma, which is hypothesis (c); [L2] the kernel lemma for walk families with its two classes of rows; [L3] the product lemma for walk kernels; [L4] parts (i)–(iv) of the perturbation lemma for the localised vertex covariance; [L5] the positivity lemma for the Gaussian vertex integral, with its bound on [B-CMP116, (2.23)–(2.26)]; [L6] the restriction theorem at equal levels, which is Theorem 4.8:thm-restriction-units (CA-I 33276, proved).
- **What is missing.** The bound on $\Gamma_0$ in (1) has no printed proof. (2σ) and (2U) have only the Route (8383–8387). Statements [L2]–[L5] are not printed: the gate searched CA-I, CA-II, CA-III and `YM4_sketch_500.tex` and found neither a label nor a statement for them (gate finding 2). This note proves the $\Gamma_0$ bound, (2σ), (2U), [L2] and [L3]. It replaces [L4] and [L5] by explicit estimates (§5.5, §5.6).
- **Use in the account.** Corollary 4.4:cor-localised-independence (CA-I 9615) applies the proposition (9668, 9777). Part III's count of the 27 intermediate statements lists that corollary among the six proved as implications in Part II (CA-III 111054–111061).

## 3. Inputs and their status in the account

"Proved" means that the account prints the statement with a complete proof and no status sentence (CA-I 30–31).

| Input | Where | Status in the account |
|---|---|---|
| Hypotheses (a)–(d) and the setting [B-CMP116, (2.14)]; within (a): (W$'$) = Definition 4.4:def-form-walk-hypothesis (5519–5564, with datum-free majorants in clause v) and (k1)–(k3) of Definition 4.4:def-auxiliary-parameters (6095–6153) | CA-I 8112–8143 | hypotheses of the proposition |
| Definitions read: 4.4:def-regular-backgrounds ($\mathbf P_\sigma$, no condition on $\partial\mathbf U$; 4608–4698), 4.4:def-walk-systems ($d(\omega;b,b')$, weighted norm; 4875–4906), 4.4:not-kernel-symmetrisation (e), (F), (G) ($(B_K,\delta_K)$, domain diameters, where the bounds hold; 7474–7491, 7530–7540), 4.4:def-base-floors (threshold, three floors; 7990–8108) | CA-I | definitions |
| Lemma on walk systems: (a) $\lvert\!\lvert\!\lvert KK'\rvert\!\rvert\!\rvert_\theta\le\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_\theta\lvert\!\lvert\!\lvert K'\rvert\!\rvert\!\rvert_\theta$; (b) $\lVert K\rVert\le\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_0$; (c) entry bound and $d(\omega;b,b')\ge\lvert b-b'\rvert$ | CA-I 4908–4984 (no label) | proved |
| Definition 4.4:def-interpolation-rule: "meets" means $\operatorname{int}\Delta\cap\lvert\varpi\rvert\ne\emptyset$; $K(1_{\sigma'})=K^{W(\sigma')}$ | CA-I 5120–5194 | identity proved |
| Lemma 4.4:lem-cell-resolvent (v): local families of $\mathsf R(x)$, $\mathsf M$ and their bounds | CA-I 6219, 6282–6298 | proved, under the added hypotheses of clause (v) |
| Lemma 4.4:lem-local-coercivity | CA-I 6959 | proved; its hypotheses are in (a) |
| Corollary 4.4:cor-localised-covariance: $C^{(k)}(Z_0)^{W'}=\mathsf T_{W'}^{-1}$, $\operatorname{Re}\mathsf T_{W'}\ge\frac58\gamma_*$ | CA-I 7162–7185 | proved |
| Lemma 4.4:lem-reality-symmetry (the symmetry lemma) | CA-I 7629–7630 | "The statement of this lemma is not written out here; parts of its proof are printed below." Not counted as proved. |
| Corollary 4.4:cor-polymer-base-form (i)–(iv): $Z_0'\supseteq Z_0^{+M}$; base bounds (iii); imaginary-part bounds (ii), (iv) | CA-I 7827–7988 | printed with proof; the proof applies clauses (a), (b) of the symmetry lemma, so it stands as an implication from that lemma |
| Theorem 4.8:thm-restriction-units, at $i=i'$ | CA-I 33276 | proved |
| Lemma 5.2:lem-complex-fluctuation: the account's reading of [B-CMP116, §2], the term (2.14), the bound on $\sum_Y\lvert\tau(Y)\rvert\lvert V(Y,B)\rvert$ | CA-II 3521–3556 (proof to 3797) | proved, with Bałaban's potentials of form (1.42) and bounds (1.43), (1.36) as hypotheses |
| Lemma 4.4:lem-vertex-formula (reads (4c)) | CA-I 5218 | proved |

## 4. Readings and conventions

- **R1. Parameter cubes** (gate finding 8). In this proposition $\sigma_0$ consists of the $LM$-cubes $\Delta\subset Z\setminus\operatorname{int}Z_0'$, on which σ is defined (setting, CA-I 8141). This is forced by $W(\emptyset)=Z_0'$ (CA-I 8159), and the account says it at CA-I 8746–8747. So $m(\varpi)$ counts only these cubes, and $K(0;\mathsf u)=K^{Z_0'}(\mathsf u)$.
- **R2. Norms.** For a single matrix kernel $N$ (square or rectangular) and $a\ge0$ put $|N|_a:=\max\{\sup_b\sum_{b'}|N(b,b')|e^{a|b-b'|},\ \sup_{b'}\sum_b|N(b,b')|e^{a|b-b'|}\}$. It is submultiplicative, by $|b-b''|\le|b-b'|+|b'-b''|$ as in the proof of the lemma on walk systems (a), and it dominates the operator norm by the Schur test, as in (b). Transposition does not change it, and $|N|_a\le|N|_{a'}$ for $a\le a'$. Applied to a single kernel, such as a difference of two families, the statement's $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert_0$ is read as $|\cdot|_0$, as the account reads it in its proof of (3) (CA-I 8585). Put $\mathcal L(c):=\sup_b\sum_{b'}e^{-c|b-b'|}$ (CA-I 8397–8399). It is finite for $c>0$, uniformly in the torus.
- **R3. The Gaussian $d\mu_C$.** $d\mu_C$ is the normalised Gaussian measure with density proportional to $e^{-\frac12B^{\top}C^{-1}B}$ (CA-I 7313–7314), and $C$ need not be symmetric (Remark 4.4:rem-symmetric-base-need, CA-I 7303–7365). For real $B$, $B^\top C^{-1}B=B^\top H_CB$ with $H_C:=\operatorname{sym}(C^{-1})$. So $d\mu_C(B)=(2\pi)^{-n_B/2}(\det H_C)^{1/2}e^{-\frac12B^\top H_CB}\,dB$ when $\operatorname{Re}H_C>0$, with the root fixed from $\det A_0>0$ by (5.14). The normalisation holds at real positive $H_C$ by orthogonal diagonalisation, and then extends by the identity theorem in each symmetric matrix entry (`YM4_sketch_500.tex` 14023–14034). Here $n_B$ is the number of real coordinates of $B$ on $\mathbb B(Z_0)$. So $\det C^{-1}$ is in general not the normalising determinant.
- **R4. The Gaussian $d\mu_0$** (gate finding 1). $d\mu_0$ is the normalised Gaussian measure of unit covariance on the real coordinates of $X$, restricted to $Z$ [B-CMP116, (2.8)]. The account calls it "the measure of $X$" (CA-I 7311) and restricts it to $Z$ (CA-II 3622); it does not define it further, and its own argument at CA-I 8737 assumes the same. If $d\mu_0$ has instead a covariance $\Sigma$ with $\|\Sigma\|\le s_0$, replace $D_X$ by $\Sigma^{1/2}D_X\Sigma^{1/2}$ in §5.6; only early constants change (the gate's repair; not re-proved here).
- **R5. Family bounds.** At every datum of $\mathbf P_{\rho,Z}$, the local $Z$-family of each of the three families satisfies $\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_\theta\le B_K$, with $(B_{\mathsf A},B_C,B_{\mathsf M})=(\mathsf B,\,8S/\gamma_*,\,4S(2/\gamma_*)^{1/2})$; for $\mathsf A$ also $\lvert\!\lvert\!\lvert\mathsf A\rvert\!\rvert\!\rvert_{\delta_{\mathsf A}}\le\mathsf B$ with $\delta_{\mathsf A}\ge8\theta$. Sources: (W$'$) and its local half for $\mathsf A$; Lemma 4.4:lem-cell-resolvent (v) at $x=0$ for $C$, and for $\mathsf M$; Definition 4.4:not-kernel-symmetrisation (e), (G). Every step domain has sup-diameter at most $4\ell\le M/12$ (items (f), (F), and (k3)). A subfamily, such as the $Z_0'$-family, obeys the same bound. These bound absolute sums, not sums with cancellation.
- **R6. Order of constants.** (1) $\mathsf B,\delta_{\mathsf A},\gamma_*,\rho_w$ and the profile $h$. (2) $r'$ by (k1); then $r,\theta_0,\theta,S$. (3) $\ell$ by (k2), (k2$'$). (4) $\varepsilon_0^{P'}$, decreased as CA-I 8016–8017 allows, so that it also meets the finitely many smallness conditions of §§5.5–5.6. Each of these reads only $\mathsf B,\gamma_*,S,\theta,\delta_{\mathsf A}$ and lattice sums $\mathcal L(\cdot)$ at these rates. (5) $\kappa_1$ (Stage 4, CA-I 1492–1496; no $M$). (6) $M$ (Stage 6, CA-I 1537), above (k3), the two inequalities of (b), and the two $M$-floors of (d). (7) $\mathcal R_{\mathbf P}$ above its floor in (d); then the radii (CA-I 5822–5909). (8) Bałaban's free parameters $\alpha_4,\gamma_2$ get one more ceiling, (5.24) below, which is an early number; their own later ceilings stay. No early constant reads $M$, $\kappa_1$, $\alpha_4$ or $\gamma_2$, so there is no cycle.

## 5. Proof

We write $\theta:=\theta_K=\theta_0/4$, as the account does. Constants called *early* depend only on the data of R6 (1)–(3); they never depend on $M$, $\kappa_1$, $\alpha_4$, $\gamma_2$, the volume or the level.

### 5.1 Clause (2σ), and the kernel bounds of the σ-families

Fix $\mathsf u\in\mathbf P_{\rho,Z}$, $K\in\{\mathsf A,C,\mathsf M\}$, a row $b$ and a column $b'$. Write $d_\varpi:=d(\varpi;b,b')$, the length of a shortest tree that contains $b_-$ and $b'_-$ and meets every domain of $\varpi$ (CA-I 4890–4891).

*Geometry.* Let $m(\varpi)\ge1$. Some $\Delta\in\sigma_0$ meets $|\varpi|$, so there is a point $x\in\operatorname{int}\Delta\cap|\varpi|$ (CA-I 5132–5133). By R1, $\Delta\subset Z\setminus\operatorname{int}Z_0'$, so $x\notin\operatorname{int}Z_0'$. Corollary 4.4:cor-polymer-base-form gives $Z_0'\supseteq Z_0^{+M}$ (CA-I 7836–7838), so $\operatorname{int}Z_0'$ contains every point at sup-distance less than $M$ from $Z_0$. Hence $\operatorname{dist}_\infty(x,Z_0)\ge M$. The point $x$ lies in a step domain of $\varpi$, of sup-diameter at most $4\ell\le M/12$ (R5). A shortest tree for $d_\varpi$ contains $b_-$ and meets that domain, and its $\ell^1$ length is at least the sup-distance between any two of its points. So, if $\operatorname{dist}_\infty(b_-,Z_0)\le M/4$,
$$d_\varpi\ \ge\ M-\tfrac M{12}-\tfrac M4\ =\ \tfrac{2M}3\ \ge\ \tfrac M3 .\tag{5.1}$$
For $K=C$, every row and every column lies in $\mathbb B(Z_0)$, so $\operatorname{dist}_\infty(b_-,Z_0)\le1\le M/4$ (by (k2), (k3): $M\ge48\ell$ and $\ell\ge2r+4$). So (5.1) holds at every entry of $C$. For every walk, $d_\varpi\ge|b-b'|$ (lemma on walk systems, (c)).

*Count.* By (c) and the first inequality of (b),
$$\kappa_1m(\varpi)\le81\kappa_1+\frac{162\kappa_1}{LM}\,d_\varpi\le81\kappa_1+\frac\theta4\,d_\varpi .\tag{5.2}$$

*The sum.* At the rows of (2σ), for $m(\varpi)\ge1$, (5.1) and (5.2) give
$$\kappa_1m(\varpi)-\theta d_\varpi\le81\kappa_1-\tfrac{3\theta}8d_\varpi-\tfrac{3\theta}8d_\varpi\le\Bigl(81\kappa_1-\frac{\theta M}8\Bigr)-\frac{3\theta}8|b-b'| .\tag{5.3}$$
Multiply by $|K_\varpi(\mathsf u)(b,b')|e^{\theta d_\varpi}$ and sum over $\varpi$. By R5, $\sum_\varpi|K_\varpi(\mathsf u)(b,b')|e^{\theta d_\varpi}\le\lvert\!\lvert\!\lvert K\rvert\!\rvert\!\rvert_\theta\le B_K$. This is (local-real-base-3), with exactly $\eta_1=e^{81\kappa_1-\theta M/8}$.

*The differences.* The walks with $m(\varpi)=0$ carry the empty product $1$ and sum to $K(0;\mathsf u)=K^{Z_0'}(\mathsf u)$ (R1). So $K(\sigma;\mathsf u)-K^{Z_0'}(\mathsf u)=\sum_{m(\varpi)\ge1}K_\varpi(\mathsf u)\prod_{\Delta\in\sigma_0(\varpi)}\sigma(\Delta)$, and each product has modulus at most $e^{\kappa_1m(\varpi)}$. The entry bound of (2σ) follows, with no factor two. For $C$, spend all of $\frac{3\theta}4d_\varpi$ on (5.1): $\kappa_1m(\varpi)-\theta d_\varpi\le81\kappa_1-\theta M/4$. Sum over $(\varpi,b')$ at fixed $b$, or over $(\varpi,b)$ at fixed $b'$. Since $C(0;\mathsf u)=\mathsf T_{Z_0'}(\mathsf u)^{-1}$ (Corollary 4.4:cor-localised-covariance, as the statement says), this gives the Schur bound of (2σ) with $(8S/\gamma_*)e^{81\kappa_1-\theta M/4}$.

*Constants.* The second inequality of (b) is $243\kappa_1\le\theta M/64$, so $81\kappa_1\le\theta M/192$. Hence $\eta_1\le e^{-23\theta M/192}\le e^{-\theta M/64}=\bar\eta$ and $e^{81\kappa_1-\theta M/4}\le e^{-47\theta M/192}$. This proves (2σ) at every $\mathsf u\in\mathbf P_{\rho,Z}$ and $|\sigma(\Delta)|\le e^{\kappa_1}$.

*Kernel bounds on the σ-families* ([L2], the kernel lemma; first sentence of (4a)). By (5.2) alone, at every row, $\sum_\varpi|K_\varpi(\mathsf u)(b,b')|\,e^{\kappa_1m(\varpi)}e^{\frac{3\theta}4d_\varpi}\le e^{81\kappa_1}\sum_\varpi|K_\varpi(\mathsf u)(b,b')|e^{\theta d_\varpi}$. So the σ-weighted family has weighted norm at most $B_Ke^{81\kappa_1}$ at rate $3\theta/4$ (*all rows*). At rows with $\operatorname{dist}_\infty(b_-,Z_0)\le M/4$, the walks with $m(\varpi)=0$ give at most $B_K$ at rate $\theta$. By (5.3), $\kappa_1m+\frac{3\theta}8d_\varpi-\theta d_\varpi\le\log\eta_1$, so the walks with $m(\varpi)\ge1$ give at most $\eta_1B_K$ at rate $3\theta/8$. The total is at most $2B_K$ at rate $3\theta/8$ (*controlled rows*; for $C$ these are all rows). Both bounds hold for the row sums at the retained rows, for the column sums over them, and entrywise (lemma on walk systems, (c)).

### 5.2 Clause (2U)

Fix the real local $U$ and $\mathsf u=(e^{i\xi A'}U,\mathbf J)\in\mathbf P_{\varsigma,Z}$. For $z\in\mathbb C$ put $\mathsf u_z:=(e^{iz\xi A'}U,z\mathbf J)$, so $\mathsf u_1=\mathsf u$ and $\mathsf u_0=(U,0)$. The conditions that define $\mathbf P_{s,Z}$ are [B-CMP109, (1.13)] for $A'$ at radius $s\alpha_1$ and [B-CMP109, (1.14)] for $\mathbf J$ at $s$ times its radius. Both are bounds homogeneous of degree one in $(A',\mathbf J)$, and no condition on $\partial\mathbf U$ enters (CA-I 4624–4637). Hence $\mathsf u_z\in\mathbf P_{\rho,Z}$ for $|z|<\rho/\varsigma$, and $\rho/\varsigma\ge2$. Only $U|_Z$ enters; nothing is extended beyond $Z$.

Let $\Phi(z)$ be one of the following: the entry $e^{\theta|b-b'|}K^{Z_0'}(\mathsf u_z)(b,b')$; the finite matrix $K^{Z_0'}(\mathsf u_z)$ with the norm $|\cdot|_0$; or the same two objects for $K(\sigma;\mathsf u_z)$ at fixed σ, with the weights and row classes of §5.1. Let $D$ bound $\Phi$ on the disc $|z|<\rho/\varsigma$. For $K^{Z_0'}$, $D=B_K$ by R5 and $d_\varpi\ge|b-b'|$; for the σ-families, $D$ is the constant of §5.1. $\Phi$ is analytic. Each walk term is analytic in the datum ((W$'$) (iii), (v); Lemma 4.4:lem-cell-resolvent (v)), and $z\mapsto\mathsf u_z$ is entire. The partial sums over finitely many walks are bounded by $D$ on the disc, so Cauchy's integral formula passes to the limit by dominated convergence. For $R<\rho/\varsigma$, Cauchy's estimate bounds the Taylor coefficients at $0$ by $\|\Phi_n\|\le DR^{-n}$. Sum over $n\ge1$ at $z=1$ and let $R\uparrow\rho/\varsigma$:
$$\|\Phi(1)-\Phi(0)\|\le D\sum_{n\ge1}(\varsigma/\rho)^n=D\,\frac{\varsigma}{\rho-\varsigma}.\tag{5.4}$$
For $K^{Z_0'}$ this is the entry bound and the Schur bound of (2U). For the σ-families it gives $(B_Ke^{81\kappa_1},3\theta/4)$ at all rows, which implies the printed $(2B_Ke^{81\kappa_1},3\theta/8)$, and $(2B_K,3\theta/8)$ at controlled rows. This proves (2U).

### 5.3 Clauses (1), (2s), (2Γ)

The account proves everything in these clauses except the bound on $\Gamma_0$ in (1), which `lrb.md` (13) proves. The gate checked all of it line by line (gate, §6).

*(1).* $A_0=\operatorname{sym}\operatorname{Re}T_0$ is real symmetric by definition. The bounds $\frac58\gamma_*\le A_0\le\mathsf B$ and $|A_0(b,b')|\le\mathsf Be^{-\delta_{\mathsf A}|b-b'|}$ are Corollary 4.4:cor-polymer-base-form (iii) as printed. Inverting the eigenvalues gives a real symmetric $C_0^{\rm cv}$ with $\mathsf B^{-1}\le C_0^{\rm cv}\le8/(5\gamma_*)$. At the datum $(U,0)$, $\Gamma_0(b,b')=\sum_{b_1\notin Z_0}\mathsf A^{Z_0'}(b,b_1)\mathsf M^{Z_0'}(b_1,b')$. By R5 and the lemma on walk systems (c), $|\mathsf A^{Z_0'}(b,b_1)|\le\mathsf Be^{-\theta|b-b_1|}$ (as $\delta_{\mathsf A}\ge\theta$) and $|\mathsf M^{Z_0'}(b_1,b')|\le B_{\mathsf M}e^{-\theta|b_1-b'|}$. For $x+y\ge|b-b'|$, $e^{-\theta x-\theta y}\le e^{-(\theta/2)|b-b'|}e^{-(\theta/2)x}$. Extend the sum to all $b_1$; then $|\Gamma_0(b,b')|\le\mathsf BB_{\mathsf M}\mathcal L(\theta/2)e^{-(\theta/2)|b-b'|}\le\mathsf BB_{\mathsf M}\mathsf S\,e^{-(\theta/2)|b-b'|}$. A real part has modulus at most that of the number.

*(2s) and (2Γ).* The first half of (2s) is Corollary 4.4:cor-polymer-base-form (iii) as printed. The second half of (2s) and all of (2Γ) are proved in full in the account (CA-I 8402–8483 and 8485–8561), and we cite them. Their inputs are R5, Corollary 4.4:cor-localised-covariance (for $T_0^{-1}=C^{Z_0'}(U,0)$) and Corollary 4.4:cor-polymer-base-form (ii)–(iv). The imaginary-part bounds of (ii) and (iv) are clause (a) of the symmetry lemma, read through the corollary. The constants are $S'':=\sup_b\sum_{b''}|b-b''|e^{-(\delta_{\mathsf A}/2)|b-b''|}$, $\delta_{\rm CT}:=\min\{\delta_{\mathsf A}/2,\ 5\gamma_*/(16\mathsf BS'')\}$, $a:=\min\{\theta,\delta_{\rm CT}\}$, $C_s=\frac{8S}{\gamma_*}\cdot\frac{16}{5\gamma_*}\mathcal L(a/2)\mathcal L(a/4)$ and $\theta_s=a/4$. The Combes–Thomas bound $|A_0^{-1}(b,b')|\le\frac{16}{5\gamma_*}e^{-\delta_{\rm CT}|b-b'|}$ of that proof is used again in §5.5.

### 5.4 Clause (3)

This is the account's printed argument (CA-I 8582–8632). Its one open input, (2σ), is proved in §5.1. Let $\mathsf u\in\mathbf P_{\rho,Z}$ and $|\sigma(\Delta)|\le e^{\kappa_1}$. Put $\mathsf T_{\mathsf u}:=\mathsf T_{Z_0'}(\mathsf u)$ and $\mathsf E_\sigma:=C(Z_0,\sigma;\mathsf u)-\mathsf T_{\mathsf u}^{-1}$. Corollary 4.4:cor-localised-covariance gives $\operatorname{Re}\mathsf T_{\mathsf u}\ge\frac58\gamma_*$. R5 and the lemma on walk systems (b) give $\|\mathsf T_{\mathsf u}\|\le\mathsf B$. The Schur bound of (2σ) gives $\|\mathsf E_\sigma\|\le(8S/\gamma_*)e^{-47\theta M/192}$.

Put $\mathsf t:=\gamma_*/(4\mathsf BS)$. Then $\mathsf t\le2/5$, because $S\ge1$ (the term $b'=b$) and $\frac58\gamma_*\le\|\mathsf T_{\mathsf u}\|\le\mathsf B$. (The account writes $\mathsf t\le\frac14$ from $\gamma_*\le\mathsf B$, CA-I 8591; $\mathsf t\le\frac25$ suffices below: gate finding 3.) Condition (k2) says exactly $e^{-\theta_0\ell/8}\le\mathsf t$. By (k3) and $\theta=\theta_0/4$, $\theta M\ge12\theta_0\ell$, so $e^{-\theta M}\le\mathsf t^{96}$. Since $\mathsf B\cdot8S/\gamma_*=2/\mathsf t$,
$$\mathsf B\|\mathsf E_\sigma\|\le2\mathsf t^{45/2}\le\tfrac12,\qquad \mathsf B^2\|\mathsf E_\sigma\|\le\frac{\gamma_*\mathsf t^{43/2}}{2S}\le\frac{\gamma_*}{16}.\tag{5.5}$$
So $C(Z_0,\sigma;\mathsf u)=\mathsf T_{\mathsf u}^{-1}(I+\mathsf T_{\mathsf u}\mathsf E_\sigma)$ is invertible, $C^{-1}=(I+\mathsf T_{\mathsf u}\mathsf E_\sigma)^{-1}\mathsf T_{\mathsf u}$, and $\|C^{-1}-\mathsf T_{\mathsf u}\|\le\mathsf B^2\|\mathsf E_\sigma\|/(1-\mathsf B\|\mathsf E_\sigma\|)\le\gamma_*/8$. Hence $\operatorname{Re}C(Z_0,\sigma;\mathsf u)^{-1}\ge\frac12\gamma_*\ge\frac38\gamma_*$.

The proof uses (b), (k2), (k3), and, through (2σ), hypotheses (a) and (c). It uses no floor of (d), which is what the printed sentence on hypotheses asserts (gate finding 4).

### 5.5 Clause (4a): products and the four perturbation estimates

Write $q_\varsigma:=\varsigma/(\rho-\varsigma)$, so $\hat\varepsilon=\bar\eta+q_\varsigma+\eta_{\rm sym}$.

*Products* ([L3], the product lemma). Take a product of $p\le3$ of the σ-families, with coordinate projections (such as $\chi_{Z_0^c}$) between the factors. Expand it over the intermediate bonds $b_1,\dots,b_{p-1}$ and over separate walks $\varpi_1,\dots,\varpi_p$. Put $D:=\sum_jd(\varpi_j;b_{j-1},b_j)$, $N:=\sum_jm(\varpi_j)$ and $B_\Pi:=\prod_jB_{K_j}$. The rule is applied to each factor on its own, so a term carries $N$ factors $\sigma(\Delta)$, counted with multiplicity, and modulus at most $e^{\kappa_1N}$. Then (5.2) for each walk gives
$$\kappa_1N\le81p\kappa_1+\theta D/4.\tag{5.6}$$
The absolute family sums with weight $e^{\theta D}$ have both Schur sums at most $B_\Pi$: sum the last walk and endpoint first for a row, the first ones for a column, as in the lemma on walk systems (a). A projection only removes terms.

Let the initial row satisfy $\operatorname{dist}_\infty(b_{0,-},Z_0)\le M/4$, and let $N\ge1$. Join shortest trees of the $p$ walks at their common points $b_{j,-}$. The union is connected, contains $b_{0,-}$, meets a step domain that contains a point outside $\operatorname{int}Z_0'$, and has length at most $D$. The geometry of §5.1 gives $D\ge M/3$, and $D\ge|b_0-b_p|$. With (5.6), $p\le3$ and $243\kappa_1\le\theta M/64$ from (b),
$$e^{\kappa_1N-\theta D}\le e^{81p\kappa_1-\theta M/8}e^{-(3\theta/8)|b_0-b_p|}\le\bar\eta\,e^{-(3\theta/8)|b_0-b_p|};\tag{5.7}$$
in fact the first factor is at most $e^{-7\theta M/64}$. The product at $\sigma=0$ keeps exactly the terms with $N=0$. So the change from $0$ to σ consists of the terms of (5.7), with no subtraction loss. On rows within $M/4$ of $Z_0$ it has $|\cdot|_{3\theta/8}\le B_\Pi\bar\eta$, the product at $0$ has $|\cdot|_\theta\le B_\Pi$, and so the product at σ has $|\cdot|_{3\theta/8}\le2B_\Pi$. At all rows, (5.6) gives $B_\Pi e^{81p\kappa_1}$ at rate $3\theta/4$. Transposition gives the same for a column near $Z_0$. For the change in the datum, apply (5.4) to the whole product, not factor by factor: in the controlled-row norm it is at most $2B_\Pi q_\varsigma$.

For $\Gamma$ ($p=2$, rows in $\mathbb B(Z_0)$, $B_\Pi=\mathsf BB_{\mathsf M}$), split $\Gamma(\sigma;\mathsf u)-\Gamma_0=[\Gamma(\sigma;\mathsf u)-\Gamma(\sigma;U,0)]+[\Gamma(\sigma;U,0)-\Gamma(0;U,0)]$. Then
$$|\Gamma(\sigma;\mathsf u)-\Gamma_0|_{3\theta/8}\le\mathsf BB_{\mathsf M}(\bar\eta+2q_\varsigma),\tag{5.8}$$
for the rectangular kernel with rows in $\mathbb B(Z_0)$; both Schur sums are controlled. The rate is better than the $\theta/32$ the account uses at CA-I 8679.

*The four estimates* ([L4], in the form the account's proof reads it at CA-I 8646–8693). Fix, before $M$, the early rate $a_P:=\frac12\min\{\theta_s,\theta/32\}>0$. As the account does (CA-I 8653–8654), split $E'=C(Z_0,\sigma;\mathsf u)-C_0^{\rm cv}$ and $\Gamma-\Gamma_0^{\mathbb R}$:
$$E'=[C(\sigma;\mathsf u)-\mathsf T_{Z_0'}(\mathsf u)^{-1}]+[\mathsf T_{Z_0'}(\mathsf u)^{-1}-T_0^{-1}]+[T_0^{-1}-C_0^{\rm cv}],\qquad \Gamma-\Gamma_0^{\mathbb R}=(\Gamma-\Gamma_0)+i\operatorname{Im}\Gamma_0.\tag{5.9}$$
The bounds used are (2σ) at rate $3\theta/8$; (2U) for $K=C$, whose $Z_0'$-family is $\mathsf T_{Z_0'}(\cdot)^{-1}$, at rate $\theta$; (2s) at rate $\theta_s$; (5.8); and (2Γ) at rate $\theta/4$. Every rate exceeds $a_P$, so the weight $e^{a_P|b-b'|}$ costs only early lattice sums. Hence, for an early $D_0$,
$$|E'|_{a_P}+|\Gamma(\sigma;\mathsf u)-\Gamma_0^{\mathbb R}|_{a_P}\le D_0\hat\varepsilon.\tag{5.10}$$
Let $Q\ge1$ be an early bound for $|A_0|_{a_P}$, $|C_0^{\rm cv}|_{a_P}$, $|\Gamma_0^{\mathbb R}|_{a_P}$ and $D_0$. It exists by (1) and the Combes–Thomas bound of §5.3, since $a_P<\delta_{\rm CT}$.

(i) *Inverse.* Let $QD_0\hat\varepsilon\le\frac12$. In the algebra $(|\cdot|_{a_P})$ of R2, $C=A_0^{-1}(I+A_0E')$ and $|(I+A_0E')^{-1}|_{a_P}\le2$. So $C^{-1}=(I+A_0E')^{-1}A_0$, and
$$C^{-1}=A_0-A_0E'A_0+R_2,\qquad |C^{-1}-A_0|_{a_P}\le2Q^2D_0\hat\varepsilon,\qquad |R_2|_{a_P}\le2Q^3D_0^2\hat\varepsilon^2,\tag{5.11}$$
with $R_2=(A_0E')^2(I+A_0E')^{-1}A_0$. The base inputs are $C_0^{\rm cv}\ge\mathsf B^{-1}\ge\frac58\gamma_*/\mathsf B^2$, $1/\|C_0^{\rm cv}\|\ge\frac58\gamma_*$ and $(C_0^{\rm cv})^{-1}=A_0$ with the decay of (1). No further Combes–Thomas step is needed.

(ii) *Real part of the vertex kernel.* $R_3:=\operatorname{Re}\Gamma(\sigma;\mathsf u)-\Gamma_0^{\mathbb R}=\operatorname{Re}[\Gamma(\sigma;\mathsf u)-\Gamma_0]$ entrywise. It obeys (5.10), since $|\operatorname{Re}w-\operatorname{Re}w_0|\le|w-w_0|$. No reality of $\Gamma_0$ is used.

(iii) *Form.* With the bilinear transpose, which the analytic prefactor requires,
$$\Gamma^{\top}C\Gamma-(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}\Gamma_0^{\mathbb R}=(\Gamma-\Gamma_0^{\mathbb R})^{\top}C\Gamma+(\Gamma_0^{\mathbb R})^{\top}(C-C_0^{\rm cv})\Gamma+(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}(\Gamma-\Gamma_0^{\mathbb R}).\tag{5.12}$$
Decrease the threshold so that $D_0\hat\varepsilon\le1$. Then $|C|_{a_P},|\Gamma|_{a_P}\le Q+1$, and (5.12) has $|\cdot|_{a_P}\le3(Q+1)^2D_0\hat\varepsilon$. Transposition does not change $|\cdot|_{a_P}$, also for rectangular kernels. The form is read on real $X$.

(iv) *Determinants.* Put $E_1:=C^{-1}-A_0$ and $E_2:=\operatorname{Re}_{\rm ent}E_1$ (entrywise real part). Then
$$\det C^{-1}=\det A_0\cdot\det(I+C_0^{\rm cv}E_1),\qquad \det(\operatorname{Re}_{\rm ent}C^{-1})=\det A_0\cdot\det(I+C_0^{\rm cv}E_2).\tag{5.13}$$
If an $n\times n$ matrix $N$ has $\|N\|\le u\le\frac12$, the series for $\log(I+N)$ gives
$$|\log\det(I+N)|\le n\sum_{j\ge1}u^j/j\le2nu .\tag{5.14}$$
The determinant does not vanish on this ball, so (5.14) also fixes the branch. By (5.11), $\|C_0^{\rm cv}E_i\|\le\frac8{5\gamma_*}\,2Q^2D_0\hat\varepsilon$. So the quotients and their inverses are at most $e^{c\,\hat\varepsilon\,n_B}$, with $c$ early. The same holds with $\operatorname{sym}E_1$ or $\operatorname{sym}\operatorname{Re}_{\rm ent}E_1$ in place of $E_1$, since $\operatorname{sym}$ and $\operatorname{Re}_{\rm ent}$ do not increase the operator norm. These give the determinants of the actual densities (R3).

So the four estimates hold with smallness parameter $C_P\hat\varepsilon$, $C_P$ early: enlarge $C_P$ to cover the constants of (5.10)–(5.14). Decrease $\varepsilon_0^{P'}$ so that $QD_0\hat\varepsilon\le\frac12$, $D_0\hat\varepsilon\le1$ and $\frac{16}{5\gamma_*}Q^2D_0\hat\varepsilon\le\frac12$ hold whenever $\hat\varepsilon\le\varepsilon_0^{P'}$. This is the decrease that CA-I 8016–8017 allows, made before $M$. Together with §5.1 (kernel bounds) and the product bounds above, this proves (4a), in the form stated in §6, S2.

### 5.6 Clause (4b): the Gaussian vertex integral

Write the vertex integral as the account does (CA-I 7305–7314; at $s=1$, CA-II 3606–3620):
$$\mathcal J(F):=\int d\mu_0(X)\,e^{-\frac12X^{\top}\Gamma^{\top}C\Gamma X}\int d\mu_C(B)\,e^{-B^{\top}\Gamma X}F(B),\tag{5.15}$$
with $\Gamma=\Gamma(\sigma;\mathsf u)$ and $C=C(Z_0,\sigma;\mathsf u)$. Let $n_B$ and $n_X$ be the real dimensions of $B$ and $X$. All bounds below are uniform in both, and the cost is proportional to $n_B$ only.

*Constants.* Put $\mathsf K:=1+\mathsf B+\frac8{5\gamma_*}+\mathsf BB_{\mathsf M}\mathsf S^2$. It bounds $\|A_0\|$, $\|C_0^{\rm cv}\|$ and $\|\Gamma_0^{\mathbb R}\|\le|\Gamma_0^{\mathbb R}|_0\le\mathsf BB_{\mathsf M}\mathsf S\mathcal L(\theta/2)\le\mathsf BB_{\mathsf M}\mathsf S^2$, and $A_0\ge\frac58\gamma_*\ge\mathsf K^{-1}$. By (5.10), after an early enlargement of $C_P$,
$$\|C-C_0^{\rm cv}\|+\|\Gamma-\Gamma_0^{\mathbb R}\|\le\varepsilon_P:=C_P\hat\varepsilon .\tag{5.16}$$
Let $|F(B)|\le F_*e^{\lambda|B|^2}$ with $\lambda\ge0$, and let $\varepsilon_P\le1/(2\mathsf K)$. As in (5.11), $\|C^{-1}-A_0\|\le2\mathsf K^2\varepsilon_P$, and $\|C\|,\|\Gamma\|\le2\mathsf K$. Put $C^{\rm sym}:=\operatorname{sym}C$ and
$$R_B:=\operatorname{Re}_{\rm ent}H_C,\quad J:=\operatorname{Re}_{\rm ent}\Gamma,\quad P_X:=\operatorname{Re}_{\rm ent}(\Gamma^{\top}C^{\rm sym}\Gamma),\quad D_B:=R_B-2\lambda I,\quad h_B:=2\mathsf K^2\varepsilon_P+2\lambda .$$
$R_B$, $P_X$ and $D_B$ are real symmetric, and $J$ is real. Entrywise real part, $\operatorname{sym}$ and transposition do not increase operator norms. Since $\|D_B-A_0\|\le h_B$ and $A_0\ge\mathsf K^{-1}$: if $\mathsf Kh_B\le\frac12$, then
$$D_B\ge(2\mathsf K)^{-1},\qquad \|D_B^{-1}-C_0^{\rm cv}\|\le2\mathsf K^2h_B .\tag{5.17}$$

*Bound.* For real $(B,X)$, $|e^{-\frac12X^{\top}\Gamma^{\top}C\Gamma X}|=e^{-\frac12X^{\top}P_XX}$, the density of $d\mu_C$ (R3) has modulus $(2\pi)^{-n_B/2}|\det H_C|^{1/2}e^{-\frac12B^{\top}R_BB}$, and $|e^{-B^{\top}\Gamma X}|=e^{-B^{\top}JX}$. Take moduli in (5.15) and do the real $B$-integral:
$$\iint\bigl|\text{integrand of (5.15)}\bigr|\le F_*\,\frac{|\det H_C|^{1/2}}{(\det D_B)^{1/2}}\int d\mu_0(X)\,e^{\frac12X^{\top}D_XX},\qquad D_X:=J^{\top}D_B^{-1}J-P_X .\tag{5.18}$$
No contour is moved and no cutoff is crossed.

*Zeroth order.* At $\varepsilon_P=\lambda=0$: $J=\Gamma_0^{\mathbb R}$, $D_B=A_0$, $P_X=(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}\Gamma_0^{\mathbb R}$, so $D_X=0$. Equivalently, $\int d\mu_{C_0^{\rm cv}}(B)e^{-B^{\top}\Gamma_0^{\mathbb R}X}=e^{\frac12X^{\top}(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}\Gamma_0^{\mathbb R}X}$ cancels the base prefactor exactly. This is the zeroth-order cancellation in [B-CMP116, (2.23)–(2.24)] (CA-I 8700–8706), and it holds because $C_0^{\rm cv}$ is symmetric.

*Remainder.* Expand $J=\Gamma_0^{\mathbb R}+(J-\Gamma_0^{\mathbb R})$, with $\|J-\Gamma_0^{\mathbb R}\|\le\varepsilon_P$ and $\|J\|\le2\mathsf K$, and use (5.17): $\|J^{\top}D_B^{-1}J-(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}\Gamma_0^{\mathbb R}\|\le4\mathsf K^2\varepsilon_P+2\mathsf K^2\varepsilon_P+2\mathsf K^4h_B\le10\mathsf K^6\varepsilon_P+4\mathsf K^4\lambda$. The telescope (5.12) with $C^{\rm sym}$ in place of $C$, in operator norm and with entrywise real parts, gives $\|P_X-(\Gamma_0^{\mathbb R})^{\top}C_0^{\rm cv}\Gamma_0^{\mathbb R}\|\le7\mathsf K^2\varepsilon_P$. Hence
$$\|D_X\|\le v:=17\mathsf K^6\varepsilon_P+4\mathsf K^4\lambda .\tag{5.19}$$
If $v\le\frac12$, the $X$-integral in (5.18) converges absolutely and equals $\det(I-D_X)^{-1/2}$ (R4).

*Volume cost.* $J^{\top}D_B^{-1}J$ has rank at most $n_B$. Write $\Gamma=\Gamma_1+i\Gamma_2$ and $C^{\rm sym}=C_1+iC_2$ with $\Gamma_j$, $C_j$ real. Then
$$P_X=\begin{pmatrix}\Gamma_1\\\Gamma_2\end{pmatrix}^{\!\top}\begin{pmatrix}C_1&-C_2\\-C_2&-C_1\end{pmatrix}\begin{pmatrix}\Gamma_1\\\Gamma_2\end{pmatrix}$$
has rank at most $2n_B$, so $\operatorname{rank}D_X\le3n_B$. $D_X$ is real symmetric with eigenvalues $\mu$ of modulus at most $v\le\frac12$, and $-\log(1-\mu)\le2|\mu|$ there, so
$$\det(I-D_X)^{-1/2}\le e^{3n_Bv}.\tag{5.20}$$
Also $\|C_0^{\rm cv}(H_C-A_0)\|\le2\mathsf K^3\varepsilon_P=:a_1$ and $\|C_0^{\rm cv}(D_B-A_0)\|\le\mathsf Kh_B=:a_2$. Every eigenvalue of either matrix has modulus at most its norm, and those of the second are real (it is similar to a real symmetric matrix). So for $a_2\le\frac12$, $|\det H_C|^{1/2}(\det D_B)^{-1/2}\le(1+a_1)^{n_B/2}(1-a_2)^{-n_B/2}\le e^{n_B(3\mathsf K^3\varepsilon_P+2\mathsf K\lambda)}$. With (5.18)–(5.20),
$$\iint\bigl|\text{integrand of (5.15)}\bigr|\le F_*\,e^{68\mathsf K^6(\varepsilon_P+\lambda)\,n_B}.\tag{5.21}$$
The conditions used ($\varepsilon_P\le1/(2\mathsf K)$, $\mathsf Kh_B\le\frac12$, $v\le\frac12$) all follow from $\varepsilon_P\le(68\mathsf K^6)^{-1}$ and $\lambda\le(16\mathsf K^4)^{-1}$: then $\mathsf Kh_B\le\frac1{34\mathsf K^3}+\frac1{8\mathsf K^3}<\frac12$ and $v\le\frac14+\frac14$.

*The integrand $F$ is the account's.* By CA-II 3606–3620, the remaining integrand of the term (2.14) is
$$F(B)=(-1)^{|P|}\chi_{Y_0}\chi^c_P\exp\Bigl[\sum_{Y\in D}\tau(Y)V(Y,B)\Bigr].\tag{5.22}$$
In the setting (2.14) the potentials have the form [B-CMP116, (1.42)] and the bounds (1.43), (1.36). On the τ-circles of [B-CMP116, (2.18)–(2.20)] the account proves (CA-II 3710–3719)
$$\sum_{Y\in D}|\tau(Y)|\,|V(Y,B)|\le c_V\alpha_4|B|^2+c_V\alpha_4M^{-4}|Y_0|,\tag{5.23}$$
with $c_V$ the larger of its two $O(1)$ constants, an early number. On the support of $\chi^c_P$ every bond $b\in P$ has $|B(b)|\ge T$, so $\chi^c_P\le e^{-\gamma_2T^2|P|/2}e^{\frac{\gamma_2}2\sum_{b\in P}|B(b)|^2}$. So $|F(B)|\le F_*e^{\lambda|B|^2}$ with
$$F_*=\exp\bigl(c_V\alpha_4M^{-4}|Y_0|-\gamma_2T^2|P|/2\bigr),\qquad \lambda=c_V\alpha_4+\gamma_2/2 .$$
This keeps the failed-test factor of [B-CMP116, (2.26)]. With the determinant bounds of §5.5 (iv), (5.21) gives the Gaussian estimates the account reads at [B-CMP116, (2.16)–(2.17), (2.23)–(2.26)], with $\alpha_5=O(\hat\varepsilon)+O(\alpha_4)+\gamma_2$ as at CA-I 8698.

*Order.* Decrease $\varepsilon_0^{P'}$ to at most $(68\mathsf K^6C_P)^{-1}$, with the conditions of §5.5. Give $\alpha_4,\gamma_2$ the early ceiling
$$c_V\alpha_4+\gamma_2/2\le(16\mathsf K^4)^{-1},\tag{5.24}$$
and keep their own later ceilings. The three floors of (d) give $\bar\eta,q_\varsigma,\eta_{\rm sym}\le\varepsilon_0^{P'}/3$. The first is (eq-base-floors-2). The second is consequence (a) of Definition 4.4:def-base-floors, because $\varsigma/(\rho-\varsigma)$ increases with $\varsigma\le1+\beta$. The third is Corollary 4.4:cor-polymer-base-form (i): $4\mathsf Be^{-\theta\mathsf r_s/2}\le4\mathsf Be^{-\theta\mathsf r^*/2}=\varepsilon_0^{P'}/3$. So $\varepsilon_P\le(68\mathsf K^6)^{-1}$, and (4b) is proved.

### 5.7 Clause (4c): admission and analyticity

*Potentials and cutoffs.* The potentials $V(Y,\cdot)$ in (5.22), $Y\subset Z_0$, are evaluated at the local datum on $Y$. The σ-interpolation acts only on the three Gaussian operators; it puts no σ-dependent background into the potentials (CA-II 3599–3620). The real cutoffs stay fixed. Where a potential is defined only for $|B|<T$ on its support, evaluate it there and set the integrand to zero outside. The integrand is then Borel, with the majorant (5.23); no analyticity of a sharp cutoff is needed.

*Admission.* Apply Theorem 4.8:thm-restriction-units with $i=i'=k+1$ (so $\mu=1$), $Y=Z$ and $X=Y'$, both in $\mathbf D_k$, $Y'\subset Z$. If $\mathsf u$ is a $\Sigma^1$-representative at $(k+1,Z;(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0)$ with decomposition $\mathbf U=U'U$, then $\mathsf u|_{Y'}$ is one at $(k+1,Y';(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0)$, with decomposition $(U'|_{Y'})(U|_{Y'})$. The theorem imposes no condition on $M$ or on the position or shape of $Y'$. It uses no extension beyond $Z$ and no simple connectivity. For $Y'\subset Z_0$ this is the admission of the arguments of $V_k(Y',\cdot)$ in [B-CMP116, (1.34)].

*Polynomial in σ.* The torus is finite, so $\sigma_0$ is finite, and each walk multiplier $\prod_{\Delta\in\sigma_0(\varpi)}\sigma(\Delta)$ is a square-free monomial. By §5.1, $\sum_\varpi|K_\varpi(\mathsf u)(b,b')|e^{\kappa_1m(\varpi)}<\infty$, so the walks may be grouped by their set $\sigma_0(\varpi)$. Hence, for fixed $\mathsf u$, $K(\sigma;\mathsf u)=\sum_{S\subset\sigma_0}c_S(\mathsf u)\prod_{\Delta\in S}\sigma(\Delta)$ is a polynomial in σ.

*Margins.* The bounds of (3), §5.5 and §5.6 hold at every point of the closed polydisc $|\sigma(\Delta)|\le e^{\kappa_1}$ with strict margins, and they are continuous in σ. By compactness they hold, with a uniform positive margin, on an open neighbourhood $\mathcal N$ of the closed polydisc. So on $\mathcal N$, $C$ is invertible, the root of $\det H_C$ is fixed by (5.14), and both integrals converge.

*Majorant.* In the exponent of (5.18), put $\tilde B:=B+D_B^{-1}JX$. The joint real form $\frac12B^{\top}D_BB+B^{\top}JX+\frac12X^{\top}P_XX+\frac12|X|^2$ (the last term from $d\mu_0$, R4) equals $\frac12\tilde B^{\top}D_B\tilde B+\frac12X^{\top}(I-D_X)X\ge(4\mathsf K)^{-1}|\tilde B|^2+\frac14|X|^2$. The map $(\tilde B,X)\mapsto(B,X)$ has norm at most $1+\|D_B^{-1}J\|\le1+4\mathsf K^2$. So the joint form is at least $c(|B|^2+|X|^2)$ with $c:=\min\{(4\mathsf K)^{-1},\frac14\}(1+4\mathsf K^2)^{-2}>0$, an early number. (The growth $e^{\lambda|B|^2}$ of $F$ is already in $D_B$.) By the margins, at least $c/2$ remains on $\mathcal N$. So the integrand of (5.15) has a σ-independent integrable Gaussian majorant on $\mathcal N$.

*Analyticity.* For fixed $(B,X)$ and fixed admissible $\mathsf u$, the integrand is analytic in σ on $\mathcal N$: the entries of $C$ and $\Gamma$ are polynomials, $C^{-1}$ and $(\det H_C)^{1/2}$ are analytic where $C$ is invertible and the root is fixed, and $F$ does not depend on σ. With the uniform majorant, Fubini, dominated convergence and Morera's theorem in each $\sigma(\Delta)$ give a continuous function that is analytic in each variable, hence analytic on $\mathcal N$ (Osgood's lemma). The functional $f(\sigma)$ is a finite combination of such terms, integrated over the $t(Y)$ and the τ-circles of the term (2.14), which are compact sets. The bound (5.23) holds uniformly on those circles, so analyticity passes through these integrals in the same way (gate finding 5).

*Vertex.* At $\sigma=1_{\sigma'}$, the identity of Definition 4.4:def-interpolation-rule gives $K(1_{\sigma'};\mathsf u)=K^{W(\sigma')}(\mathsf u)$ for each family. So the integral is the specified vertex functional, with its original $F$. Analyticity on $\mathcal N$ gives the $C^1$ hypothesis on the real cube $[0,1]^{\sigma_0}$ that Lemma 4.4:lem-vertex-formula needs. Every coefficient, potential argument and cutoff uses only $\mathsf u|_Z$, and $\mathsf u$ need not extend to a point of $\mathbf P_\varsigma$. This proves (4c), and with it the proposition.

## 6. Scope limits

These are the limits the gate records (`gates/lrb-gate.md`, Verdict and findings 1–8). Each one stays with the result.

- **S1. Implication.** The proof assumes (a)–(d) and the setting (2.14). It does not prove the upstream premises: Lemma 4.4:lem-reality-symmetry, whose statement the account does not write out and which enters only through Corollary 4.4:cor-polymer-base-form; (W$'$); the added hypotheses of Lemma 4.4:lem-cell-resolvent (v) and of Lemma 4.4:lem-local-coercivity; and Bałaban's potential bounds [B-CMP116, (1.36), (1.42), (1.43)] with the τ-radii (2.18)–(2.20), as read at CA-II 3535–3537 and 3706–3722. CMP 116 is not in our local paper folder, so those readings were checked against the account's text only. The CMP 109 bounds (1.13)–(1.14) were checked in the OCR.
- **S2. Unprinted lemmas** (gate finding 2). (4a) and (4b) are proved in the form of the explicit estimates (5.10)–(5.14) and (5.15)–(5.24). These replace the account's "perturbation lemma for the localised vertex covariance, parts (i)–(iv)", "positivity lemma for the Gaussian vertex integral" and "lemma that establishes (2.16)–(2.17)". None of these is printed. So "holds verbatim" in (4a), and "hold as stated" at CA-I 9256, cannot be compared with a text. What is proved is what the account's continued proof reads from them (CA-I 8646–8739).
- **S3. The measure $d\mu_0$** (gate finding 1) is read as the unit Gaussian; see R4.
- **S4. Volume cost.** (5.21) bounds each term by $F_*e^{68\mathsf K^6(\varepsilon_P+\lambda)n_B}$, with $n_B$ the number of real coordinates on $\mathbb B(Z_0)$. It converts to the account's volume $|Z_0|$ by the fixed bond and colour multiplicity, or by one factor $(LM)^4$ per $LM$-cube where $|Z_0|$ counts cubes. Whether this cost is summable in the cluster expansion is a later step of Bałaban's expansion, under its own ceilings. It is not claimed here, and convergence of (5.15) alone is not read as a resummation.
- **S5. Local form of (4c), and what the consumers read.** Analyticity holds on a neighbourhood of the closed σ-polydisc, at local hereditary representatives on $Z$, without a global extension. The label occurs only in CA-I, and its three consumers read exactly this. Remark 4.4:rem-cluster-lemmas-base (CA-I 8760–8837) reads the real pair $(\Gamma_0^{\mathbb R},C_0^{\rm cv})$ with $C_0^{\rm cv}$ symmetric, smallness $C_P\hat\varepsilon$ and same-level admission. Remark 4.4:rem-cluster-lemmas-local (9208–9353) reads the bounds of (1), items (i)–(iv) with the printed substitutions, (3) and (4c). Corollary 4.4:cor-localised-independence (9615–9784) reads the vertex functional at representatives in $\mathbf P_{1+\beta,X}$. The proof keeps the preassigned walk families: it does not replace the resolvent interpolation by the inverse of an interpolated precision, it does not assume that partial sums are real symmetric, and it does not extend a local datum globally.
- **S6. The sentence on hypotheses in (3)** (gate finding 4). The printed clause says it "uses only the two inequalities of (b) together with (k2) and (k3)". The proof also uses (a) and (c), through (2σ). It uses no floor of (d), and that part of the sentence holds.
- **S7. A dangling label in a consumer** (gate finding 7). Remark 4.4:rem-cluster-lemmas-local cites "hypothesis (R9)" of this proposition, "its lower bound (R9) on $M$" (CA-I 9217, 9278, 9339). The proposition has hypotheses (a)–(d) and no (R9). Read as (b), the consumer's use is served: (3) holds from (b), (c), (k2), (k3), and the product bounds of §5.5 hold with constants $B_\Pi$ and rate $\theta$.

## Checks and provenance

- Statement, labels and line numbers were read in the account's source at `31a47c543775`, with the hashes above. A few line numbers in `library/lrb.md` and the gate are 6–20 lines off the source (for example CA-I 8726–8727 for 8746–8747, the Combes–Thomas step 8411–8471 for 8423–8483, and CA-II 3610–3616 for 3622). This note uses the source's numbers. For the lead: this affects citations only, not any step.
- The proof is `library/lrb.md` (Codex, frozen 2026-11-05), checked line by line by Claude in `gates/lrb-gate.md`: first failing step none. All eight findings of that check are applied above: finding 1 (R4, S3), 2 (S2), 3 (§5.4), 4 (S6), 5 (§5.7), 6 (§2: Part III's count line is cited as a count, not as a use by clause (0)), 7 (S7) and 8 (R1, §5.1).
- In writing this note, Claude redid each displayed inequality of §5 by hand against `lrb.md` and the account. No step needed a change of substance. Four small additions are not in `lrb.md` or the gate, and the other model has not checked them: the analyticity of the walk sums in §5.2 (dominated convergence in Cauchy's formula); the explicit constant $c$ of the majorant in §5.7; the reading of $\lvert\!\lvert\!\lvert\cdot\rvert\!\rvert\!\rvert_0$ on a single kernel in R2; and the observation that the $\Gamma_0$ bound of (1) has no printed proof in the account (a search of CA-I finds it only in the statement, line 8204).
- No computation, numerical run or machine search is used. This note proves nothing beyond `lrb.md` and its gate. It is a draft for the owner; it is not sent anywhere.

