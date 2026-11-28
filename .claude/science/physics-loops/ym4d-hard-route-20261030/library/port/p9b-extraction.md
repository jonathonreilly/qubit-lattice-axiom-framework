# P9b — Gaussian extraction: port of C5

Provenance: Repository base `90d9eccdfbd0bb6f1e9a9f35a1cb8c738195cdcf`; source account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, revision `31a47c543775`. Port by Codex, 2026-11-05; reasoning setting not independently recorded. This is a research-text port, grants no status, and is not yet checked by another model.

## Scope, source standing, and recovery record

This ports C5 of `chain-ca.md` §7.2 on the complete account's route. It does not redo P9's witness. The source is [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex), statement 77279–77433, proof 77435–77859. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; credit Balaban for the minimiser, fluctuation covariances and conditional-mean identification cited below.

The heading at II:77279 has no qualification. Under CA-I:27–46 this declares a proof in full from named hypotheses. Preserve two other declarations: II:71370 calls the witness's Gaussian-extraction part (b) incomplete; III:110943–110950 calls the second-order part an implication, with the additional floor `q ≥ 21 p_0 + 1`. These are source declarations, not independent verification.

The two extraction lemmas named by C5 are explicitly unwritten-statement remarks, II:76125–76127 and 76772–76774. Therefore this port distinguishes algebraic deductions from their analytic use-site hypotheses. A displayed bound is not proved merely by referring to an unwritten “corresponding display.” In particular the two P9 use-site forms H-GXa and H-GXb remain separately named until their supplier mapping is established.

Only this file is edited. The requested `docs/ai_methodology/SCIENCE_WORKFLOW.md` and repository skill files are absent from this checkout; no search outside the authorized folders was made to replace them. No audit, status change, computation-assisted proof, or other-model check is performed.

## Exact statement

`8.2:prop-gaussian-extraction`, CA-II:77279–77433. Source status: unqualified heading; declared proved implication. The following is an exact transcription, including its unresolved internal references. Their presence does not supply the missing statements.

```latex
\begin{proposition}[The Gaussian extraction]\label{8.2:prop-gaussian-extraction}
Assume the following.
\begin{itemize}
\item The hypotheses of Lemma~\ref{8.2:lem-extraction-one-point} (Gaussian extraction for one local
observable). Among them are the localisation of the sourced step and the condition on the range
of~$r$.
\item For the second form of the bound on the remainder in~(b): the equivariance hypothesis, under
which the corresponding display of Lemma~\ref{8.2:lem-extraction-one-point} holds with $\sigma_1=2$ and the members linear in the
curvature size of the remainder bounds of the one-step
extraction lemma, Lemma~\ref{8.2:lem-one-step-extraction}, acquire the factor
$\kappa_{\mathfrak{B}}$.
\item For the value in~(c): the flat-background hypothesis.
\end{itemize}

Let $G_a\in\mathfrak{G}_{k_0}(p_a;\ell,M,\varrho)$, $a=1,2$, have both supports in one box
$\mathfrak{B}_D$ as in Definition~\ref{8.2:def-two-densities}. Let
$h\in\mathcal{C}_{p_1,p_2}(D)$ be a history that is clean for $p_1$ and for $p_2$ with this one box,
and let $W$ lie in the level-$(k_0+r)$ window. Write $\mathrm{bg}_r(W)$ for the depth-$s$ image of
the $r$-step minimiser, restricted to $\mathfrak{B}_\ell(p_1)\cup\mathfrak{B}_\ell(p_2)$, as in
Definition~\ref{8.2:def-transported-laws} for $p=p_1$ and for $p=p_2$; the function $G_a$ and its
differentials read its restriction to $\mathfrak{B}_\ell(p_a)$. Write $\kappa_{W,a}$ for $\kappa_W$
of that definition taken at $p=p_a$.

For $0\le i<r$ let $\Gamma^{12}_i(W)$ be the joint centred Gaussian law on
$\mathfrak{g}^{\mathfrak{B}_\ell(p_1)\cup\mathfrak{B}_\ell(p_2)}$ of
$\mathfrak{L}^{(i)}_W(iCB_i)$ restricted to both supports, with $B_i$, $C$ and
$\mathfrak{L}^{(i)}_W$ as in Definition~\ref{8.2:def-transported-laws}. Its two marginals are the
laws $\Gamma_i(W)$ of that definition for $p=p_1$ and for $p=p_2$. Its cross-covariance between the
two supports carries the covariance line joining $p_1$ and $p_2$.

For a centred Gaussian law $\Gamma$ on this space we put
\begin{equation*}
\langle DG_1(\mathrm{bg}_r),\Gamma\,DG_2(\mathrm{bg}_r)\rangle
:=E_{\xi\sim\Gamma}\bigl[DG_1(\mathrm{bg}_r)[\xi]\cdot DG_2(\mathrm{bg}_r)[\xi]\bigr].
\end{equation*}
For two such laws $\Gamma,\Gamma'$ and the Hessians $H_a=\operatorname{Hess}_{\mathrm{bg}_r}G_a$
we put
\begin{equation*}
(H_1\otimes H_2)[\Gamma,\Gamma']:=E\bigl[H_1[\xi,\xi']\,H_2[\xi,\xi']\bigr],
\end{equation*}
where $\xi\sim\Gamma$ and $\xi'\sim\Gamma'$ are independent. This is the full contraction in which
one argument of $H_1$ is paired with one argument of $H_2$ through the cross-covariance of $\Gamma$,
and the remaining two arguments are paired through the cross-covariance of $\Gamma'$. Since $H_1$ and
$H_2$ are symmetric, $(H_1\otimes H_2)[\Gamma,\Gamma']=(H_1\otimes H_2)[\Gamma',\Gamma]$. Finally,
$n=\dim\mathfrak{g}$. The letters $C_1$, $C_\eta$ and $C_{\mathrm{ext},2}$ below denote positive
constants not depending on $W$, $h$, $k_0$, $r$ or $D$. Then the following hold.
\begin{enumerate}
\item[(a)] (Joint moment.) The product $G_1G_2$ lies in
$\mathfrak{G}_{k_0}(\cdot\,;\ell+6C_W,M^2,\varrho)$. The quantity $(G_1G_2)^{\langle h\rangle}(W)$
is given by Lemma~\ref{8.2:lem-extraction-one-point} applied to $G_1G_2$, that is, by
the corresponding display with the corresponding bound, with
jets up to fourth order. Its main term is the sum of two pieces: the Gaussian functional with the
structure displayed in~(b), and the product of the main terms of
the corresponding display of Lemma~\ref{8.2:lem-extraction-one-point} for $G_1$ and for $G_2$.
\item[(b)] (Truncated moment.) The carried conditional covariance
\begin{equation*}
\mathcal{T}^{(r)}(W):=(G_1G_2)^{\langle h\rangle}(W)-G_1^{\langle h\rangle}(W)\,
G_2^{\langle h\rangle}(W)
\end{equation*}
satisfies
\begin{equation}\label{8.2:eq-gaussian-extraction-a}
\begin{split}
\mathcal{T}^{(r)}(W)={}&\sum_{i<r}g_{k_0+i}^2\,
\bigl\langle DG_1(\mathrm{bg}_r),\Gamma^{12}_i(W)\,DG_2(\mathrm{bg}_r)\bigr\rangle\\
&+\frac12\sum_{i,i'<r}g_{k_0+i}^2g_{k_0+i'}^2
\bigl(\operatorname{Hess}_{\mathrm{bg}_r}G_1\otimes\operatorname{Hess}_{\mathrm{bg}_r}G_2\bigr)
\bigl[\Gamma^{12}_i,\Gamma^{12}_{i'}\bigr]
+\mathcal{E}_{2,r}(W).
\end{split}
\end{equation}
The first sum, the one-line term, consists of a single transported covariance line between the two
gradients. It vanishes at flat $W$, and it always satisfies
\begin{equation}\label{8.2:eq-gaussian-extraction-1}
\Bigl|\sum_{i<r}g_{k_0+i}^2\,
\bigl\langle DG_1(\mathrm{bg}_r),\Gamma^{12}_i(W)\,DG_2(\mathrm{bg}_r)\bigr\rangle\Bigr|
\le C_1\sum_{i<r}g_{k_0+i}^2L^{-4i}\,C_{\mathrm{ax}}^2\mu_2^2\,\kappa_{W,1}\kappa_{W,2},
\end{equation}
where $C_{\mathrm{ax}}$ and $\mu_2=2M\varrho^{-2}$ are as in
Lemma~\ref{8.2:lem-one-step-extraction}.

The second sum, the two-line term, consists of two transported covariance lines. Take
$G_a=O_{s,p_a}$, where $O_{s,p}(U):=1-\operatorname{Re}\operatorname{tr}U(\partial p)$ is the action
density of the plaquette $p$ at depth $s$, and take $W$ flat.
Then the two-line term equals
\begin{equation}\label{8.2:eq-gaussian-extraction-2}
\frac n2\Bigl(\sum_{i<r}g_{k_0+i}^2\,\mathfrak{g}^{\mathrm{step}}_{12,i}\Bigr)^2,
\end{equation}
where, for $i<r$, $\mathfrak{g}^{\mathrm{step}}_{12,i}$ is the flat-background covariance per colour
of the fluxes through $p_1$ and through $p_2$ of the $i$-th transported step fluctuation:
\begin{equation*}
\mathfrak{g}^{\mathrm{step}}_{12,i}:=n^{-1}E_{\xi\sim\Gamma^{12}_i(W)}
\bigl[\langle\ell_{p_1}(\xi),\ell_{p_2}(\xi)\rangle\bigr]\quad\text{at flat }W,
\end{equation*}
with $\ell_p(\xi)\in\mathfrak{g}$ the linearised flux of $\xi$ through the plaquette $p$.

The remainder satisfies
\begin{equation}\label{8.2:eq-gaussian-extraction-3}
\begin{split}
|\mathcal{E}_{2,r}(W)|\le{}&C_{\mathrm{ext},2}M^2\Bigl[g_{k_0}^6\Pi_2
+g_{k_0}^4\Pi_2'\bigl(\kappa_{W,1}+\kappa_{W,2}+g_{k_0}p_0(g_{k_0})\bigr)
+g_{k_0}^4\Pi_2''\kappa_{W,1}\kappa_{W,2}\Bigr]\\
&+M^2\bigl(e^{-c_{\mathrm{loc}}D}+e^{-c_{\mathrm{w}}p_0(g_{k_0})^2}\bigr).
\end{split}
\end{equation}
Relative to $g_{k_0}^4$, this is of order $g_{k_0}p_0(g_{k_0})$ and $\kappa_{W,a}$ times the
prefactors. Under the equivariance hypothesis the bound improves to
\begin{equation}\label{8.2:eq-gaussian-extraction-4}
\begin{split}
|\mathcal{E}_{2,r}(W)|\le{}&C_{\mathrm{ext},2}M^2\Bigl[g_{k_0}^6\Pi_2
+g_{k_0}^4\Pi_2'\bigl((\kappa_{W,1}+\kappa_{W,2})\kappa^{\mathfrak{B}}_W
+g_{k_0}^2p_0(g_{k_0})^2\bigr)
+g_{k_0}^4\Pi_2''\kappa_{W,1}\kappa_{W,2}\Bigr]\\
&+M^2\bigl(e^{-c_{\mathrm{loc}}D}+e^{-c_{\mathrm{w}}p_0(g_{k_0})^2}\bigr).
\end{split}
\end{equation}
Relative to $g_{k_0}^4$, this is of order $g_{k_0}^2$ and
$\kappa_{W,a}\kappa^{\mathfrak{B}}_W$ times the prefactors, plus the exponential terms.

In both bounds $c_{\mathrm{loc}}$ and $c_{\mathrm{w}}$ are the constants of
the corresponding display of Lemma~\ref{8.2:lem-extraction-one-point}. The prefactors $\Pi_2,\Pi_2',\Pi_2''$ are polynomials in
$D$, $r$, $\log x_{k_0}$ and $C_W$, and none of them contains a factor $L^{4r}$.
\item[(c)] (Two-point tower.) Let $G_a=O_{s,p_a}$. Let $\mathcal{A}$ be the free lattice field and
$\mathcal{G}_i:=\sigma(Q^{(i)}\mathcal{A})$ its nested conditionings. Extend
$\mathfrak{g}^{\mathrm{step}}_{12,i}$ to all $i\ge0$ as the per-colour covariance of the fluxes
through $p_1$ and through $p_2$ of the $i$-th fluctuation of $\mathcal{A}$,
\begin{equation*}
\begin{split}
\mathfrak{g}^{\mathrm{step}}_{12,i}&:=n^{-1}E\bigl[\langle\Delta_i\ell_{p_1},
\Delta_i\ell_{p_2}\rangle\bigr],\\
\Delta_i\ell_p&:=E\bigl[\ell_p(\mathcal{A})\,\big|\,\mathcal{G}_i\bigr]
-E\bigl[\ell_p(\mathcal{A})\,\big|\,\mathcal{G}_{i+1}\bigr].
\end{split}
\end{equation*}
By the flat-background hypothesis, for $i<r$ this agrees with the definition of
$\mathfrak{g}^{\mathrm{step}}_{12,i}$ in~(b). Then
\begin{equation}\label{8.2:eq-gaussian-extraction-5}
\begin{split}
&\sum_{i\ge0}\mathfrak{g}^{\mathrm{step}}_{12,i}=\mathfrak{g}_{12}
:=n^{-1}E\bigl[\langle\ell_{p_1}(\mathcal{A}),\ell_{p_2}(\mathcal{A})\rangle\bigr],\\
&\Bigl|\sum_{i\ge r}\mathfrak{g}^{\mathrm{step}}_{12,i}\Bigr|\le C_\eta L^{-4r}.
\end{split}
\end{equation}
Here $\mathfrak{g}_{12}$ is the per-colour covariance of the fluxes through $p_1$ and $p_2$ of the
free lattice field $\mathcal{A}$. The identity is the law of total covariance for $\mathcal{A}$ along
its nested conditionings $\sigma(Q^{(i)}\mathcal{A})$.

Now take the smeared densities $X^{(k_0)}(f_a)$ of Definition~\ref{8.2:def-two-densities} in place
of $G_a$, with $\mathcal{K}_s$ and $G^{(s)}_K$ as in that definition. The same identity, applied term
by term, gives the structure $b_0\mathcal{K}_s(f_1,f_2)$ of clause~(iii)(c) of
Theorem~\ref{3.1:thm-main}, with $G^{(s)}_K$ replaced by its truncation to the $r$ levels
$k_0,\dots,k_0+r-1$. The levels $k_0+i$ with $i\ge r$, coarser than those retained, contribute for
each pair of plaquettes the tail $\sum_{i\ge r}\mathfrak{g}^{\mathrm{step}}_{12,i}$ bounded in
\eqref{8.2:eq-gaussian-extraction-5}.
\end{enumerate}
\end{proposition}
```

## Inputs, with their source standing

The name in the first column is local to this port. It is not a new CA label.
An input includes its stated domain and all its antecedents. No row is discharged by this table.

| Name | CA label and locus | Standing and exact use |
|---|---|---|
| H-C2 | `8.4:thm-minimiser-analyticity`, II:85845–85885 | **Cited**, Balaban CMP 102b Theorem 1, Proposition 9, (190), pp.308–309. Real regular base data, admissible determining set, small multiplier and the specified gauge are required. Supplies background regularity, analyticity and derivative decay; no proof of Balaban's theorem is ported here. |
| H-C3a | `8.4:prop-small-piece`, II:88192–88259 | **Incomplete at (*)**, as its heading states. Supplies the small box-gradient/Hessian budget for far members. Its spent-pocket cap remains; the growth of the current-scale radius alone does not remove that cap. |
| H-C3b | `8.5:def-representation-identity`, II:90196–90197, 90212–90226 | **Outstanding**, despite being called a definition. Identity of the shifted frozen representation and its running marginal coefficient is a hypothesis, distinct from analyticity. |
| H-C4a | `8.5:lem-radius-tails`, II:90729–90832; qualification 90834–90843 | Unqualified lemma, **proved implication** from (i)–(iii), and (iv) for the remainder class. The fine-field-domain version of Balaban 109 (0.29) and profile locality are explicitly incomplete. Keep the animal count 109 (0.26), decay floor, and remainder-rate/mass hypothesis (iv). The final list II:145593 calls the supplier incomplete. |
| H-C4b | `8.5:thm-room-lemma`, II:93196–93217 | **Incomplete**. Its (*) is the frozen sourced family's zero block mean, `8.5:prop-zero-block-mean`. The source-profile defect, covariance difference and separated-range bounds, all room floors, and actual geometry remain hypotheses. |
| H-C4c | `8.5:prop-remainder-covariance`, II:94225–94318 | Unqualified **conditional implication**. Hypotheses (b) source-carrying unextracted terms have remainder type, (c) running-coupling comparison, and (d) profile locality are explicitly incomplete. Keep Balaban 119 (2.31) with the stipulated identification of its exponent with `κ₀≥7`, the remainder radius-tail condition and every room floor. The final list II:145595–145596 calls this supplier incomplete. |
| H-q | III:110943–110950, assembly of `3.1:thm-main` (iv) | **Additional numerical hypothesis** `q ≥ 21 p_0 + 1`. Here `q` is the exponent of Balaban CMP 119 (2.28); `p_0` is the fixed exponent, not the degree function `p_0(g)`. It accompanies the second-order extraction, even though C5's own heading omits it. |
| H-corr | `5.1:thm-correlation-theorem`, II:2791–2811; `8.1:prop-correlation-witness-depth`, II:68570–68590; `3.1:thm-main` (0), (iii); III:110943–110950 | **Conditional** flow/correlation inputs. Read at their admitted domains. [P6](p6-correlation.md) is a port, not a proof of every antecedent. |
| H-loc | `8.3:thm-sourced-step-localisation`, II:82711 onward; `8.2:def-clean-step-localisation`, II:75071; C5 II:77282–77284 | **Conditional** localisation with placement, positivity, window, quadratic-form, exterior-field and interaction hypotheses. H-C2/H-C3 remain attached. Merely being in a common box is insufficient. |
| H-OP | `8.2:lem-extraction-one-point`, II:76772–76774; proof continuations `8.2:prf-carried-step`, 76776–76926, and `8.2:prf-remainder-recursion`, 76928–77129 | **Statement unwritten; proof parts printed.** Assume the one-insertion estimates actually invoked below, including closure of the class under the carrying operations, segregation, and uniformity for every shortened segment. |
| H-step | `8.2:lem-one-step-extraction`, II:76125–76127; use at 77601–77633 | **Statement unwritten; proof parts printed.** In particular assume its part (v) covariance expansion and the stated one-step error forms. The complete part (v) cannot be recovered from the remark heading. |
| H-alg | `8.2:lem-flat-background`, II:74201–74233 | Unqualified **proved** lemma: zero gradient at a locally pure-gauge background; `‖DG‖≤C_ax μ₂ η`; plaquette Hessian equal to the flux inner product. Retain its axial small-curvature domain and norm convention. |
| H-tr | `8.2:lem-curvature-contraction`, II:75214–75342; `8.2:def-transported-laws`, II:76684–76770 | **Conditional** transport estimates with (I)–(IV), including Balaban 102b regularity, holomorphy, composed-minimiser identification and the linear curl response. Covariance transport is the derivative of the actual minimiser, not a substitute free model. |
| H-pos | `8.2:lem-fluctuation-positivity`, II:75164–75212 | **Proved implication** from `Q(U,0)≥γ₀/2`. The real covariance and uniform box moment bounds used here require that antecedent and the appropriate readout norms. |
| H-flow | `8.2:lem-coupling-comparison`, II:75635–75701 | **Proved implication** from the running-flow bounds and `2B♯(r+1)≤x_(k₀)`. In particular `g_(k₀+i)²≤2g_(k₀)²`. |
| H-eq | C5 II:77285–77288; `8.2:prf-carried-step`, II:76869–76873; `8.2:prf-remainder-recursion`, II:77059–77071 | **Named equivariance hypothesis** for the improved bound only: every relevant curvature-linear remainder acquires the box-curvature factor and the one-point exponent becomes `σ₁=2`. The finite-link-set “equivariance theorem” is referenced by name in these passages; no exact theorem label is supplied there. Do not invent one. |
| H-flat | `8.2:rem-gaussian-exact`, II:77131–77161; `8.2:prf-two-point-tower`, II:77776–77802 | **Printed-without-proof identification**, expressly cited as printed at II:77159–77161: the transported flat Balaban step is the conditional increment of the free field. The tower proof credits Balaban CMP 95 (1.23)–(1.24), II:77831–77833. |
| H-free, H-tail | `8.2:prf-two-point-tower`, II:77787–77800; `8.2:eq-gaussian-exact-1`, II:77153–77157 | **Explicit hypotheses**: free Gaussian field with nested linear block conditionings, and the one-point conditional-mean variance bound `C_η L^(-4I)` at each plaquette. The two-point tower proof names these by description, not a theorem label. Do not identify them with an unrelated tower lemma merely because its title matches. |
| H-geom | `8.2:def-local-observables`, II:74118–74158; `8.2:def-clean-event`, II:75491–75540; `8.2:def-two-densities`, II:77201–77268 | **Definitions and admission hypotheses**, including one common clean box, all support margins, `s_*≤s−r`, `r≥1`, `s≤K−1`, `2B♯(r+1)≤x_(k₀)`, and the support enclosure discussed below. |

The assembly's “cluster-expansion lemma, which is proved” (III:110944–110945) is retained as **H-cluster**, in precisely the instance used by the analytic extraction suppliers. That sentence supplies no label. This port does not silently choose a polymer lemma or claim its hypotheses hold. It is an upstream input, not an extra step of the covariance algebra below.

### Quantitative use-site hypotheses that the placeholders leave open

Write `g=g_(k₀)`, `P=p_0(g)`, `κ_a=κ_(W,a)`, and `κ_B=κ_W^B`. These abbreviations do not change constants. A prefactor is a polynomial in `D,r,log x_(k₀),C_W` with fixed coefficients. Fixed inverse tube radii and jet constants may enter those coefficients. Define

\[
\begin{split}
 B_3(W)&=C_{\rm ext,2}M^2\{g^6\Pi_2+
 g^4\Pi'_2(\kappa_1+\kappa_2+gP)+g^4\Pi''_2\kappa_1\kappa_2\},\\
 B_4(W)&=C_{\rm ext,2}M^2\{g^6\Pi_2+
 g^4\Pi'_2[(\kappa_1+\kappa_2)\kappa_B+g^2P^2]
 +g^4\Pi''_2\kappa_1\kappa_2\},\\
 T(W)&=M^2(e^{-c_{\rm loc}D}+e^{-c_{\rm w}P^2}).
\end{split} \tag{P9b.1}
\]

Here `B_3(W),B_4(W)` are only names for error budgets. They are not Balaban's constant `B₃`; their subscripts refer to C5's error displays, not C3 and C4 in chain-ca.

The following are **open analytic uses of H-OP/H-step**, not conclusions proved by naming them:

* **H-jet.** Their holomorphic jet/transport estimates apply to both carried main parts and to `Φ_i,Ψ_i`, with uniform Cauchy margins. They control the derivative corrections and the nonflat Hessian terms isolated in §Proof below by the polynomial portions of (P9b.1), after summation. The equivariant version requires the corresponding `κ_B` improvement. The source's “of order g⁴ multiplied by further factors” at II:77621–77623 and 77741–77743 is not a quantitative bound specifying those factors.
* **H-tail-sum.** The localisation and window errors, including errors already in carried remainders, sum to at most the **printed** `T(W)` with the **printed** rates. II:77756–77759 collects them without displaying that estimate. No change of `c_loc,c_w` or insertion of a polynomial in front of `T` is made here. Raw per-step exponential bounds do not imply this form without such a summation allocation.
* **H-support.** The product's support is contained in a ball `B_(ℓ+6C_W)(p_*)` and its subsequent read sets meet H-OP's common-box margins. This is the precise geometric use at II:77439–77443. The general local-observable statement must include this enclosure if “as in Definition 8.2:def-two-densities” is not already read to include it. A bound on minimum distance between two sets alone does not prove that enclosure.

H-GXa and H-GXb remain the separately stated P9 hypotheses. Their exact consumption and the missing mappings appear at the end.

## Proof on the account's route

The deductions below are by hand. Each `(filled)` expands an omitted algebraic or limiting step. A named hypothesis remains an input. In particular, the final analytic error estimate is conditional on H-jet and H-tail-sum as well as the source's named suppliers. This qualification is essential to the meaning of this port.

### 1. The product and its jets — clause (a)

Source: II:77435–77452. By H-support, both functions can be read on the product's stated support ball. Restriction from that ball to either smaller support maps its radius-`ϱ` tube into the original tube. The product is holomorphic, gauge invariant and bounded by `M²`. It therefore belongs to the stated class with support parameter `ℓ+6C_W`, on that geometric admission hypothesis.

**F1 (filled).** For tangent vectors `v_1,…,v_j`, the repeated product rule gives

\[
 D^j(G_1G_2)[v_1,\ldots,v_j]
 =\sum_{A\subset\{1,\ldots,j\}}
 D^{|A|}G_1[v_A]\,D^{j-|A|}G_2[v_{A^c}]. \tag{P9b.2}
\]

For one direction repeated `j` times, this has the binomial coefficients `binom(j,a)`. On the common tube, the one-variable Cauchy formula applied to the product gives the sharper direct bound `j!M²ϱ^(−j)`. Thus its jets through order four exist in exactly the class required by H-OP; no product of derivative estimates changes the supremum constant `M²`.

Apply H-OP to the product, with its fourth-order version as C5(a) expressly requires. The printed continuation of H-OP at II:77041–77049 only displays its second-order main part. The existence and estimate for the higher-order version used here remain part of H-OP, not a new deduction from that continuation.

For the claimed splitting, set `G_a^r=m_a+e_a` and `T^r=t+e_T`, with `m_a,t` their respective main parts. The defining covariance identity gives

\[
 (G_1G_2)^r=t+m_1m_2+
 e_T+m_1e_2+m_2e_1+e_1e_2. \tag{P9b.3}
\]

This is the exact split of main terms claimed in (a). It also specifies every product error that H-OP's bound must cover. Clause (b) now computes `t`; no joint moment is inferred by multiplying conditional means alone.

**C1 (correction: geometric inference, if read literally for arbitrary local observables).** The proof at II:77439–77443 infers the enclosure from a distance bound between supports. Minimum support distance does not imply it for arbitrary `ℓ`. The smallest route-preserving clarification is H-support above, with the same `ℓ+6C_W` and `D`, rather than a changed radius. This is an admission condition, not a proved consequence of the printed minimum-distance condition. For example, the intervals `[-ℓ,ℓ]` and `[ℓ+6C_W,3ℓ+6C_W]` have minimum distance `6C_W`. Their union has diameter `4ℓ+6C_W`, which exceeds the diameter `2ℓ+12C_W` of a radius-`ℓ+6C_W` ball when `ℓ>3C_W`. This disproves the geometric inference from minimum distance alone. For the particular witness supports, their actual enclosure must be supplied by the witness geometry.

### 2. Exact conditional covariance recursion — clause (b)

Source: II:77454–77504. Let `E_i` denote the positive, normalized step expectation at level `k₀+i`, conditioning on the next field. H-OP's segregation hypothesis says that the carried functions use these very expectations. Put

\[
 G_a^{(i+1)}=E_iG_a^{(i)},\qquad
 U^{(i+1)}=E_iU^{(i)},\qquad
 U^{(0)}=G_1G_2,\quad T^{(i)}=U^{(i)}-G_1^{(i)}G_2^{(i)}.
\]

Insert `U^(i)=T^(i)+G_1^(i)G_2^(i)` to obtain exactly

\[
 T^{(i+1)}=E_iT^{(i)}+
 \operatorname{Cov}_i(G_1^{(i)},G_2^{(i)}). \tag{P9b.4}
\]

**F2 (filled).** At `j=1` this is the desired sum because `T^(0)=0`. If

\[
 T^{(j)}=\sum_{i<j}E_{j-1}\cdots E_{i+1}
 \operatorname{Cov}_i(G_1^{(i)},G_2^{(i)}),
\]

then applying `E_j` and adding the `j`th covariance gives the same formula at `j+1`. The new term has an empty composition, hence coefficient one. Consequently, with `𝐄_i=E_(r−1)⋯E_(i+1)`,

\[
 T^{(r)}=\sum_{i<r}\mathbf E_i
 \operatorname{Cov}_i(G_1^{(i)},G_2^{(i)}). \tag{P9b.5}
\]

This is `8.2:eq-gaussian-extraction-6`. For every bounded real or complex `F`, positivity gives `|E_iF|≤E_i|F|≤‖F‖∞`; iteration proves the same for `𝐄_i`. This explains exactly why remainders can be carried in supremum norm. It does not assert positivity for a complex tilted law outside the real conditioning window.

### 3. Separate carried remainders

Source: II:77506–77600. Write `G_a^(i)=M_(a,i)+J_(a,i)`. For clarity, `j_(a,i)` denotes a nonnegative bound for `|J_(a,i)|`; it is the source's capital `J_(a,i)`. Expanding the covariance gives a main-main term and

\[
 R_i=\operatorname{Cov}_i(M_{1,i},J_{2,i})+
 \operatorname{Cov}_i(J_{1,i},M_{2,i})+
 \operatorname{Cov}_i(J_{1,i},J_{2,i}).
\]

**F3 (filled).** Since `E_i(M−E_iM)=0`,

\[
 |\operatorname{Cov}_i(M,J)|
 =|E_i[(M-E_iM)J]|
 \le j\,E_i|M-E_iM|,
\quad
 |\operatorname{Cov}_i(J_1,J_2)|\le2j_1j_2. \tag{P9b.6}
\]

H-OP's bulk remainder estimates used at II:77530–77535 are

\[
 j_{a,i}\le Cg^3\Pi M,\qquad
 E_i|M_{b,i}-E_iM_{b,i}|\le C(g\kappa+g^2)M. \tag{P9b.7}
\]

The exponential parts of these bounds are kept separately under H-tail-sum; they cannot be dropped from a total remainder bound. Multiplication in (P9b.6) produces

\[
 CM^2(g^4\kappa\Pi+g^5\Pi+g^6\Pi^2). \tag{P9b.8}
\]

At all intermediate stages `i<r−1`, the admitted window estimate is `κ≤4gP`; thus the first term is at most `4CM²g⁵PΠ`. At the last stage the local curvature has the transported scale of `κ_1` or `κ_2`, under H-tr/H-OP. The first term then enters `g⁴Π'_2(κ_1+κ_2)`. For `P≥1`, `g⁵Π≤g⁵PΠ`. This weak-coupling admission is explicit: with `P=A₀(log x)^(p₀)`, `A₀,p₀>0`, it suffices that `x≥exp(A₀^(−1/p₀))`, in addition to `g≤1`. The proof below is on that small-coupling domain. The exact intermediate bound `4gP` is retained as the H-OP window estimate used at II:76978–76985; it is not derived here merely from comparability of couplings. The `g⁶` term enters `g⁶Π_2`. Summing `r` terms multiplies a prefactor by `r` and introduces no `L^(4r)`.

For the improved estimate, H-eq gives

\[
 j_{a,i}\le CM(g^4\Pi+g^2\bar\kappa\bar\kappa_B\Pi'), \tag{P9b.9}
\]

where barred curvatures refer to steps producing the remainder, strictly before step `i`. At `i=0`, the remainder is zero. At `i≥1`, these production indices obey `j≤i−1≤r−2`; **both** barred curvatures therefore satisfy the intermediate window bound `4gP`.

**F4 (filled).** Multiplication by `CM(gκ+g²)` gives exactly the four monomials

\[
 CM^2\{g^6\Pi+g^5\kappa\Pi+
 g^4\bar\kappa\bar\kappa_B\Pi'+
 g^3\kappa\bar\kappa\bar\kappa_B\Pi'\}. \tag{P9b.10}
\]

The third is bounded by `16CM²g⁶P²Π'`. For the fourth, use both barred bounds to obtain `16CM²g⁵κP²Π'`. If `i<r−1`, this is at most `64CM²g⁶P³Π'`, an allowed `g⁶` term. At `i=r−1`, use `κ_a≤Cκ_B`, which follows from the containment in `8.2:eq-transported-laws-8` and `L^(−2r)≤1`, and

\[
 g\kappa_a\le\tfrac12(g^2+\kappa_a^2)
 \le\tfrac12g^2+C\kappa_a\kappa_B.
\]

The last monomial is then at most an allowed sum of `g⁶` and `g⁴κ_aκ_B` terms, with `P²` inside the polynomial. The second monomial in (P9b.10) obeys the same inequality at the last step. At an intermediate step it is at most `4g⁶PΠ`, and

\[
 4g^6P\Pi\le2g^6\Pi+2g^6P^2\Pi
\]

is the source's precise split. This fills the index distinction behind II:77559–77568; it does not identify curvatures at two different levels.

The product of the two bounds (P9b.9) has terms proportional to

\[
 g^8\Pi^2,\quad g^6\bar\kappa\bar\kappa_B\Pi\Pi',\quad
 g^4(\bar\kappa\bar\kappa_B)^2(\Pi')^2.
\]

For `g≤1`, their bounds are respectively `g⁶Π²`, `16g⁸P²ΠΠ'≤16g⁶P²ΠΠ'`, and `256g⁸P⁴(Π')²≤256g⁶P⁴(Π')²`. Different barred maxima for the two observables are handled by the same common window bounds. All lie in the `g⁶Π_2` member. Thus the carried-remainder products have exactly the claimed polynomial forms in both versions, conditional on (P9b.7)/(P9b.9).

### 4. One-step covariance and the derivative corrections

Source: II:77601–77633. H-step(v), at `V'=V_(k₀+i+1)`, gives

\[
 \operatorname{Cov}_i(M_{1,i},M_{2,i})=\Phi_i+\Psi_i+\mathcal E_i^{(2)},
\]

where

\[
 \Phi_i=g_i^2\langle DM_{1,i},C_iDM_{2,i}\rangle,\qquad
 \Psi_i=\tfrac14g_i^4\operatorname{Cov}_{\gamma_i}
       (D^2M_{1,i}[\mathrm iCB,\mathrm iCB],
        D^2M_{2,i}[\mathrm iCB,\mathrm iCB]). \tag{P9b.11}
\]

Here only in this proof `g_i=g_(k₀+i)`, and `C_i` denotes the covariance with its source readout convention. The map `C` in `iCB` and the covariance `C^(k₀+i)` remain distinct. The imaginary unit `i` is not the level index.

The main part printed at II:76782–76786 is

\[
 M_{a,i}=G_a\circ\mathfrak B^{(i)}+Q_{a,i},\qquad
 Q_{a,i}=\tfrac12\sum_{j<i}g_j^2
 \operatorname{Tr}_{\Gamma_j^{(i)}}D^2G_a(\mathfrak B^{(i)}). \tag{P9b.12}
\]

**F5 (filled).** Define `u_a=D(G_a∘B^(i))` and `v_a=DQ_(a,i)`. Then the correction suppressed in the source's rewrite of `Φ_i` is exactly

\[
 \mathcal E_i^\Phi=g_i^2\{
 \langle u_1,C_iv_2\rangle+
 \langle v_1,C_iu_2\rangle+
 \langle v_1,C_iv_2\rangle\}. \tag{P9b.13}
\]

Under the uniform jet bounds in H-jet, `v_a=O(g²ΠM)` and `u_a=O(ΠMκ_a)` at the transported background, so the three terms are bounded by `CM²[g⁴Π(κ_1+κ_2)+g⁶Π]`. In the equivariant use, `Q_(a,i)` is itself a gauge-invariant holomorphic scalar; applying H-alg on its admitted box tube gives `v_a=O(g²ΠMκ_B)`. The same multiplication then gives `CM²[g⁴Π(κ_1+κ_2)κ_B+g⁶Π]`, using the uniform curvature ceiling for the last product. These estimates show which **quantitative jet inputs** the phrase “further factors” must mean. Their uniform tube bounds are not proved by that phrase.

For the Hessian replacement in `Ψ_i`, the chain rule gives, exactly,

\[
 D^2M_{a,i}[z,z']
 =H_a[D\mathfrak B^{(i)}z,D\mathfrak B^{(i)}z']
 +DG_a[D^2\mathfrak B^{(i)}[z,z']]
 +D^2Q_{a,i}[z,z']. \tag{P9b.14}
\]

The last two terms must also be included in the error. The non-equivariant jet bounds give their contributions of orders `g⁴κ_a`, `g⁴κ_1κ_2`, and `g⁶`, after the covariance contraction. The equivariant assertion requires the contracted terms linear in `DG_a` to acquire `κ_B`, exactly as stipulated in H-eq/H-jet. No estimate for a tensor norm alone proves that extra factor. This records, rather than silently omits, the analytic obligation in replacing the Hessians.

### 5. Carry the two-line term and compute its coefficient

Source: II:77635–77668. Apply H-OP at starting level `k₀+i+1` for `r−i−1` steps. At `i=r−1`, this is the identity and its error is zero. Its value term transports `Ψ_i` to `B_(i+1,r)(W)`; the carrying error has order `g²·g⁴=g⁶` with its polynomial prefactor, or the improved error specified in the source. Retain the Hessian-replacement errors (P9b.14).

Let `K_i` be the covariance matrix of the joint law `Γ_i^12(W)`. The retained value is

\[
 \tfrac14 g_i^4\operatorname{Cov}
       (H_1[\xi,\xi],H_2[\xi,\xi]),\qquad \xi\sim\Gamma_i^{12}.
\]

**F6 (filled).** In real coordinates the Gaussian moment-generating function is `exp(tᵀK_it/2)`. Four derivatives at zero give

\[
 E\xi_\alpha\xi_\beta\xi_\gamma\xi_\delta
 =(K_i)_{\alpha\beta}(K_i)_{\gamma\delta}
 +(K_i)_{\alpha\gamma}(K_i)_{\beta\delta}
 +(K_i)_{\alpha\delta}(K_i)_{\beta\gamma}.
\]

This formula also holds for a degenerate covariance, by writing the vector as a linear image of independent real Gaussians. Subtraction of the two means cancels the first pairing. Symmetry of each Hessian makes the other two equal. For an independent copy `ξ'`,

\[
 \operatorname{Cov}(H_1[\xi,\xi],H_2[\xi,\xi])
 =2E(H_1[\xi,\xi']H_2[\xi,\xi'])
 =2(H_1\otimes H_2)[\Gamma_i^{12},\Gamma_i^{12}]. \tag{P9b.15}
\]

Multiplying by `g_i⁴/4` gives the diagonal coefficient `g_i⁴/2` in C5(b). All sums here are finite coordinate sums; no computation is used to establish the pairing count.

### 6. Carry the one-line term and recover all cross-level pairs

Source: II:77670–77706. H-OP applied to `Φ_i` gives its value at the transported background and

\[
 \tfrac12\sum_{i<j<r}g_j^2\operatorname{Tr}_{\Gamma_j^{12}}D^2\Phi_i,
\]

plus the printed carrying error `O(g²·g³Π)` in the crude case. In the equivariant case the source uses

\[
 CM^2g^2\{g^4\Pi+g^2\Pi'(\kappa_1+\kappa_2)\kappa_B\}. \tag{P9b.16}
\]

The value term, after (P9b.13), is exactly
`g_i²〈DG_1(bg_r),Γ_i^12 DG_2(bg_r)〉`.

**F7 (filled).** For each support, H-alg bounds the gradient by `C_ax μ₂κ_a`; the transport/moment instance of H-tr/H-pos supplies its `L^(−2i)` factor in `L²(Γ_i)`. Cauchy–Schwarz for the two linear readouts gives

\[
 |E(DG_1[\xi]DG_2[\xi])|
 \le(E|DG_1[\xi]|^2E|DG_2[\xi]|^2)^{1/2}
 \le C_1 L^{-4i}C_{\rm ax}^2\mu_2^2\kappa_1\kappa_2.
\]

Multiplication by `g_i²` and the triangle inequality give exactly `8.2:eq-gaussian-extraction-1`. At a locally pure-gauge flat background both gradients vanish. Gauge invariance does **not** set this term to zero at arbitrary nonflat `W`.

At flat background write the retained part as `F_i(Z)=g_i² u_1(Z)ᵀC_i(Z)u_2(Z)`, where `u_a(0)=0`. The first derivatives of `u_a` are the transported Hessians of `G_a`.

**F8 (filled).** The degree-two Taylor term is

\[
 F_i(Z)=g_i^2\langle H_1[\mathfrak L^{(i+1)}Z,\mathfrak L^{(i)}\cdot],
 C_iH_2[\mathfrak L^{(i+1)}Z,\mathfrak L^{(i)}\cdot]\rangle+O(Z^3).
\]

Each derivative hitting `C_i` or a transport coefficient leaves at least one undifferentiated `u_a(0)=0`; hence it does not contribute at degree two. Differentiating the quadratic term twice gives a factor two. Its trace against the later law, multiplied by `g_j²/2`, therefore equals

\[
 g_i^2g_j^2(H_1\otimes H_2)[\Gamma_i^{12},\Gamma_j^{12}],\qquad i<j.
\]

This explains both the coefficient and the strict inequality between the indices. Each unordered pair `{i,j}` occurs at its smaller index exactly once. Because the contraction is symmetric, this equals the sum of the two ordered terms `(i,j)` and `(j,i)`, each with coefficient `1/2`. Together with §5's diagonal terms, it gives the full double sum in `8.2:eq-gaussian-extraction-a`.

**F9 (filled: nonflat terms that must be estimated).** The flat calculation alone does not prove that double-sum formula at general `W`. For one direction `z`, the full second derivative is

\[
\begin{split}
 g_i^{-2}D^2F_i[z,z]={}&
 2(Du_1[z])^TC_iDu_2[z]
 +(D^2u_1[z,z])^TC_iu_2+u_1^TC_iD^2u_2[z,z]\\
 &+2(Du_1[z])^T(DC_i[z])u_2
 +2u_1^T(DC_i[z])Du_2[z]
 +u_1^T(D^2C_i[z,z])u_2.
\end{split} \tag{P9b.17}
\]

Also `Du_a` contains `DG_a·D²B` as well as `H_a·DB·DB`. Retain the latter in the two-line main term. Every other term has at least one background gradient and, under H-jet, contributes a term of order `g_i²g_j²` times `κ_1+κ_2` or `κ_1κ_2`, with an allowed prefactor. Its equivariant version requires the extra box-curvature factor for the curvature-linear contractions. This is the missing nonflat estimate behind the source's flat Hessian computation. H-jet explicitly retains it; this note does not claim the flat Taylor identity proves it. The route and coefficients remain unchanged.

### 7. Plaquette colour factor

Source: II:77708–77731. For a plaquette observable, H-alg and polarization give

\[
 H_a[Z,Z']=\langle\ell_{p_a}(Z),\ell_{p_a}(Z')\rangle.
\]

At the admitted flat background the colour covariance is diagonal, as the source assumes. In an orthonormal colour basis, put `c_i=g^step_(12,i)`. Then
`E[ℓ_(p₁)(ξ_i)^αℓ_(p₂)(ξ_i)^β]=δ_(αβ)c_i`.

**F10 (filled).** For two independent fields of laws `Γ_i,Γ_j`, expand both inner products. Independence between the fields gives

\[
 (H_1\otimes H_2)[\Gamma_i,\Gamma_j]
 =\sum_{\alpha,\beta}(\delta_{\alpha\beta}c_i)
                         (\delta_{\alpha\beta}c_j)=nc_ic_j.
\]

The definition `n^(−1)E〈ℓ_(p₁),ℓ_(p₂)〉` indeed equals `c_i`. Hence the diagonal and unordered off-diagonal contributions are

\[
 \frac n2\sum_i g_i^4c_i^2+n\sum_{i<j}g_i^2g_j^2c_ic_j
 =\frac n2\left(\sum_i g_i^2c_i\right)^2. \tag{P9b.18}
\]

This is exactly `8.2:eq-gaussian-extraction-2`. The cross-covariances `c_i` may be signed; the square expansion does not assume that each is positive. The number `n/2=(N²−1)/2` agrees with `b₀` in `8.2:def-two-densities`.

### 8. Collect the errors without changing their constants

Source: II:77733–77769. There are the source's four error classes: one-step errors, differential-replacement errors, carrying errors, and the covariances containing carried remainders. The additional terms displayed in (P9b.14) and (P9b.17) belong to the differential-replacement class; omitting them would not be an exact identity.

**F11 (filled).** The one-step polynomial terms have forms

\[
 CM^2\{g^6\Pi+g^4\kappa\Pi'+g^4\kappa_{\mathrm{bg},1}
 \kappa_{\mathrm{bg},2}\Pi''\}.
\]

At `i<r−1`, substitution of `κ,κ_(bg,a)≤4gP` gives respectively `g⁶Π`, `4g⁵PΠ'`, and `16g⁶P²Π''`. At the last step the local curvature instances are `κ_a`, with their transported factors supplied by H-tr/H-step. They give `g⁴Π'(κ_1+κ_2)` and `g⁴Π''κ_1κ_2`.

Under H-eq the intermediate curvature-linear term becomes `g⁴κκ_BΠ'≤16g⁶P²Π'`; its last-step form is `g⁴Π'(κ_1+κ_2)κ_B`. This proves the stated allocation into `B_3` or `B_4`, without interchanging the top curvature with an earlier curvature.

The crude carrying errors are `g⁶ΠM²` for `Ψ_i` and `g⁵ΠM²` for `Φ_i`. The latter is in `g⁵PΠ'_2M²` on the admitted weak-coupling range `P≥1`. The improved `Φ_i` error is (P9b.16), already of the form of `B_4`; its `Ψ_i` companion has one additional `g²≤1` and is bounded by the same forms. Sections 3 and 4 account for every remainder-product and derivative-correction monomial, conditional on their stated analytic inputs.

A finite sum of such prefactors is still a polynomial. More explicitly, for `0≤i<r` and `0≤j<r`, a monomial `D^a i^b j^c(log x)^d C_W^e` is at most `D^a r^(b+c)(log x)^d C_W^e`. Summing at most `r²` terms adds at most two to the power of `r`. The geometric transport sums obey

\[
 \sum_{i=0}^{r-1}L^{-4i}\le\frac1{1-L^{-4}},\qquad L>1.
\]

These operations introduce no positive exponential in `r`. The finite constants and coefficients can be included in the unspecified source polynomials and the positive constant named `C_ext,2`; no displayed numerical coefficient or decay rate is changed.

**C2 (correction: equality versus retained term).** At II:77652–77657 the carried value of `Ψ_i` is identified with its transported `G_a`-Hessian expression. Read literally as an equality of full functions, this omits (P9b.14). The smallest correction is to write “equals that expression **plus the Hessian-replacement error**,” and include that error in the already present error collection. The source route, main coefficients and claimed bounds are unchanged. The estimate for this error remains H-jet where the source does not supply it. Likewise, at general `W`, the flat computation of `D²Φ_i` must be supplemented by (P9b.17); F9 records that requirement explicitly.

**F12 (filled: the exact tail obligation).** A sum of `r` bounds `Ce^(−cD)` is only `rCe^(−cD)`. It is not bounded by `e^(−cD)` with the same rate and coefficient for arbitrary `r`. Likewise `e^(−c(D−ℓ_i))` is not `e^(−cD)`. The printed remainder recursion II:77020–77036 retains `r` and the support loss before its final summary. Thus H-tail-sum is needed for the **particular constants** in C5. It must allocate the stronger input rates/margins to the final bound, or supply the final bound directly. This port does not fix this by decreasing `c_loc` or `c_w`, which the task forbids. This is an open supplier estimate, not a proved absorption.

With that input, the total exponential error is exactly bounded by `T(W)`. Define `E_(2,r)` to be the sum of all actual errors in (P9b.5). The estimates above give `|E_(2,r)|≤B_3+T` and, with H-eq, `|E_(2,r)|≤B_4+T`. Inserting the value terms, diagonal contractions and cross-level contractions in (P9b.5) proves the printed equation `8.2:eq-gaussian-extraction-a` and its two remainder bounds **on these named analytic hypotheses**. It does not discharge them.

### 9. Two-point tower — clause (c)

Source: `8.2:prf-two-point-tower`, II:77775–77859. This part is a complete deduction from the three explicit tower hypotheses H-free, H-flat and H-tail. It does not need the nonflat error estimates of §§4–8.

Use the source's per-colour convention throughout:

\[
 \operatorname{cov}_n(U,V)=n^{-1}E\langle U-EU,V-EV\rangle,
 \qquad \operatorname{var}_n(U)=\operatorname{cov}_n(U,U).
\]

The scalar notation `Cov(X_i,Y_i)` in the source's tower proof is read in this convention, or colour by colour and then averaged. Without that convention its first display would miss the factor `1/n` from the proposition's definition.

Let `X_i=E[ℓ_(p₁)(A)|G_i]`, `Y_i=E[ℓ_(p₂)(A)|G_i]`, where `G_(i+1)⊂G_i` and `G_0` reads the full free field. Tower conditioning gives `E[X_i|G_(i+1)]=X_(i+1)` and likewise for `Y`. Put `δX_i=X_i−X_(i+1)`, `δY_i=Y_i−Y_(i+1)`.

**F13 (filled).** Because the increments have conditional mean zero, each mixed inner product with a `G_(i+1)`-measurable variable has zero expectation. For example,

\[
 E\langle\delta X_i,Y_{i+1}-EY_{i+1}\rangle
 =E\langle E[\delta X_i\mid\mathcal G_{i+1}],Y_{i+1}-EY_{i+1}\rangle=0.
\]

Expanding the inner product in the covariance therefore yields

\[
 \operatorname{cov}_n(X_i,Y_i)
 =n^{-1}E\langle\delta X_i,\delta Y_i\rangle
 +\operatorname{cov}_n(X_{i+1},Y_{i+1}). \tag{P9b.19}
\]

This is the law of total covariance in the source. For a jointly Gaussian vector and linear conditioning, the conditional mean is its orthogonal linear projection onto the conditioning subspace. To see determinism of the conditional covariance, subtract that projection. The residual is orthogonal to each conditioning coordinate. The joint Gaussian moment-generating function then factors, since its mixed quadratic covariance is zero. Hence residual and conditioning coordinates are independent. The residual covariance is constant, even if the covariance has null directions. This justifies the source's removal of its conditional expectation around the covariance.

H-flat identifies `n^(−1)E〈δX_i,δY_i〉` with `g^step_(12,i)` for the Balaban transported increment, at flat background. This identification is **not** a consequence of the abstract law of total covariance. It is the cited Balaban input.

**F14 (filled).** Summing (P9b.19) over `i=0,…,I−1` cancels each intermediate covariance once with a plus sign and once with a minus sign:

\[
 \mathfrak g_{12}=\sum_{i<I}\mathfrak g^{\rm step}_{12,i}
                 +\operatorname{cov}_n(X_I,Y_I). \tag{P9b.20}
\]

Cauchy–Schwarz in the real Hilbert space of square-integrable colour vectors gives

\[
 |\operatorname{cov}_n(X_I,Y_I)|
 \le\operatorname{var}_n(X_I)^{1/2}\operatorname{var}_n(Y_I)^{1/2}
 \le C_\eta L^{-4I}. \tag{P9b.21}
\]

Both one-point variance bounds are H-tail with the source's same constant. Since `L>1`, the last expression tends to zero. Thus the partial sums in (P9b.20) converge to `g_12`. Setting `I=r` gives exactly

\[
 \sum_{i\ge r}\mathfrak g^{\rm step}_{12,i}
 =\operatorname{cov}_n(X_r,Y_r),\qquad
 \left|\sum_{i\ge r}\mathfrak g^{\rm step}_{12,i}\right|
 \le C_\eta L^{-4r}.
\]

There is no illicit interchange of an infinite series and a nonlinear function. The statement follows first for finite partial sums and then by their displayed remainder estimate. In fact absolute convergence follows too: orthogonal increments imply
`var_n(δX_i)≤var_n(X_i)≤C_ηL^(−4i)` and the corresponding bound for `δY_i`; Cauchy–Schwarz bounds the absolute value of each summand by `C_ηL^(−4i)`.

**F15 (filled: smearing and the running weights).** At a fixed cutoff each smeared density is a finite sum of plaquette densities. Covariance is bilinear, so the plaquette formula (P9b.18) gives the Gaussian term

\[
 b_0\sum_{p,q}f_1(x(p))f_2(x(q))
   \left[\sum_{i<r}g_i^2\mathfrak g^{\rm step}_{pq,i}\right]^2. \tag{P9b.22}
\]

For the unit-coupling kernel put `G_r(p,q)=Σ_(i<r)g^step_(pq,i)` and `t_r=G_∞−G_r`. Clause (c) bounds `|t_r|≤C_ηL^(−4r)` for each pair. The difference of the two squared kernels is exactly

\[
 G_\infty^2-G_r^2=2G_rt_r+t_r^2,\qquad
 |G_\infty^2-G_r^2|\le2|G_r|C_\eta L^{-4r}+C_\eta^2L^{-8r}. \tag{P9b.23}
\]

Multiplying this by `|f_1(x(p))f_2(x(q))|` and summing is valid for signed test functions too. This gives the asserted **structure** `b₀K_s` with the kernel truncated to the retained levels. It does not discard the running couplings in (P9b.22).

For clarity, removing those weights requires H-flow. Define `d_i=g_i²/g²−1`, so `|d_i|≤(2B♯i+c₅)g²`, and `e_r=Σ_(i<r)d_i g^step_(pq,i)`. Then

\[
 \sum_{i<r}g_i^2\mathfrak g^{\rm step}_{pq,i}=g^2(G_r+e_r),\qquad
 |e_r|\le g^2\sum_{i<r}(2B^\sharp i+c_5)
                         |\mathfrak g^{\rm step}_{pq,i}|.
\]

The square differs from `g⁴G_r²` by `g⁴(2G_re_r+e_r²)`. Bounds for this term and for the smeared tail are required for P9's relative-error form. An unweighted tower identity alone cannot yield that relative-error bound or replace `g_i²` by `g²` exactly.

## What each clause supplies to the existing P9 witness

The consumer is [p9-witness.md](p9-witness.md), especially “Precise use-site hypotheses and admission,” “Gaussian-extraction remainder,” and “Irrelevant remainder.” That committed file is left unchanged.

| C5 clause | H-GXa: extraction-error consumer | H-GXb: irrelevant-covariance consumer |
|---|---|---|
| (a), joint moment | Supplies the local product-observable extraction, provided the fourth-order H-OP and product support admission hold. It is one ingredient in comparing a joint moment and two means. It does **not** state P9's block-law six-term estimate. | No direct supply. Product extraction can be applied to admitted irrelevant insertions, but their smallness and source normalization are additional inputs. |
| (b), one-line term and bound `8.2:eq-gaussian-extraction-1` | Supplies the conditional gradient-covariance term, its zero value at flat background, and its nonflat curvature bound. Its top-field average still needs the source's window/background control. | No `7C_bρ^(−2)p_0(g)^4` room estimate follows from this bound alone. |
| (b), two-line term and `8.2:eq-gaussian-extraction-2` | Supplies the actual transported Gaussian main term and the coefficient `n/2=b₀`. The errors `8.2:eq-gaussian-extraction-3/4` supply local conditional error forms. P9 uses the crude `σ₁=1` form at II:71240–71241. | Supplies the quadratic-covariance **form** to which the C4 room/remainder inputs apply. The specific irrelevant-covariance bound is not a clause of this final printed proposition. H-C3b and H-C4a–c remain required. |
| (c), tower identity and tail | Supplies the per-plaquette unit-coupling tower and its `C_ηL^(−4r)` tail. With kernel, support and scale conversions it is the source of P9's `L^(−4(r−r₁))` member. The squared-tail identity (P9b.23) explains why one must also control quadratic tail/background terms. | No direct supply of the irrelevant mass, zero-block-mean cancellation or room factor. |

**F16 (filled: conditional versus averaged covariance).** Let `Z` denote the conditioning history and top field, with conditional means `m_a(Z)`. Expanding the two means gives

\[
 \operatorname{Cov}(G_1,G_2)
 =E[\operatorname{Cov}(G_1,G_2\mid Z)]
  +\operatorname{Cov}(m_1(Z),m_2(Z)). \tag{P9b.24}
\]

C5 controls the first term on the joint clean event. It does not bound the second term, the complement of that event, or every normalization in passing to P9's block law. This is why a port of C5(b) does not itself discharge H-GXa.

For an exact comparison, H-GXa is the error bound recalled in `8.1:rem-extraction-errors`, II:71180–71277:

\[
\begin{split}
 |\mathcal E_a|\le C_ag^4\mathfrak n(\tilde f_1)\mathfrak n(\tilde f_2)
 \bigg\{&g^{\sigma_1}\Pi_r+g^2(1+r)
 +D_\square^4(1+r)\rho^4P^4e^{-c_aP}+P^4e^{-c_aD_\square}\\
 &+\rho^{-8}\big[L^{-4(r-r_1)}
       +L^{-8(r-r_1)}p_0(g_{k_0+r})^4\big]\bigg\},
 \qquad \Pi_r=rD_\square^4L^4P^2. \tag{P9b.25}
\end{split}
\]

The source lists the suppliers: position averaging and source admission; the clean-complement weight with its age/depth hypotheses; coupling variation; the covariance-tower tail; the top window bound (Balaban CMP 119 (2.17)); small-window Gaussian comparison; the source lemma's observable suprema using Balaban 102b Theorem 1; and locality. C5 supplies local pieces of this list. It gives no explicit polynomial identifying its `Π_2,Π'_2,Π''_2` with the **specific** `Π_r` in (P9b.25). Nor does it give the clean-complement probability or the source suprema. Those remain **H-GXa**, including P9's H-source-use and H-depth. There is no new proof of the witness in this port.

H-GXb is the use-site at `8.1:prf-irrelevant-remainder`, II:73004–73054. It assumes its “clause (b) of Gaussian extraction” as incomplete and uses the coefficient **7** in

\[
 R^{\rm irr}\le7C_b\rho^{-2}P^4\mathfrak M+
       (\hbox{terms of the type of }\mathcal E_a). \tag{P9b.26}
\]

P9 retains an absolute-value version of this as its hypothesis. The displayed use-site inequality is one-sided; an absolute bound still needs a supplier for both signs. C5 has absolute bounds for its own `E_(2,r)`, but those do not automatically supply an absolute bound for a different irrelevant remainder. This is part of the open H-GXb mapping, not a change to the committed witness.

Thus neither the label collision “clause (b)” nor III's later assembly sentence closes H-GXb. The room and remainder-covariance statements C4, the shifted-representation identity C3b, and their actual source-profile domains must supply it. The source marks those inputs incomplete or outstanding; they remain so here.

### The exponent floor stays attached

H-q remains `q≥21p_0+1`, exactly as III:110946 states. The outline index directs the reader to ET3–ET4, outline 26729–26764. That passage explains a sufficient power count on the same route; it is not a replacement for CA's missing analytic inputs.

**F17 (filled: the floor's arithmetic, under ET3's own hypotheses).** Write `t=log x≥1`, `p=p_0`, `A=t^(3p−q)+x^(−a)`, and let `n_i=‖f_i‖∞`. ET3 assumes

\[
 \|O_i\|_\infty\le Cx^{-1}r^4t^{2p}n_i,
 \quad\|I_i\|_\infty\le Cx^{-1}r^4 A n_i,
 \quad r\le C_rt^{2p},\quad a>0.
\]

Using `|Cov(U,V)|≤2‖U‖∞‖V‖∞`, the two mixed terms are bounded by a constant times

\[
 x^{-2}r^8t^{2p}A n_1n_2
 \le C'x^{-2}[t^{21p-q}+t^{18p}x^{-a}]n_1n_2.
\]

For large `x`, `A≤1`; thus the `I,I` term, bounded by `Cx^(−2)r⁸A²n_1n_2`, is no larger than the same expression, since `A²≤A` and `t^(2p)≥1`. The stated integer floor implies `21p−q≤−1`, so the first term tends to zero. For the second, choose an integer `m>18p`. The series for `e^(at)` gives `e^(at)≥(at)^m/m!`, whence `t^(18p)e^(−at)≤m!a^(−m)t^(18p−m)→0`. This is a hand proof of the arithmetic step. It proves neither ET3's insertion bounds nor H-GXb's precise coefficient `7C_b`; those stay hypotheses.

## Source record and recovery checkpoint

Files already present in `/tmp` were reused, with no repeated download. Their hashes match the pinned source identities recorded by P9:

| File | SHA-256 |
|---|---|
| `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `/tmp/sa_ca_II.tex` | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| `/tmp/sa_ca_III.tex` | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

Index consultation: `sa-index/README.md`; `ca-full/README.md` and neighbouring statement rows for C5/C2/C3/C4; chunk-24's neighbouring extraction, tower and ET3 rows; `obligations.md` entries for 26184, 26461–26482, 26668–26681 and 26729–26742. Direct outline excerpts read: 26162–26168, 26618–26639, 26729–26764. They give a sketched extraction strategy, conditional weighted Gaussian construction, and proved covariance bookkeeping conditional on the displayed sup-norm inputs. They do not supply the missing complete-account lemma statements.

The complete C5 statement and both proof blocks II:77279–77859 were read. Its one-point suppliers were followed through their proof continuations II:76776–77129; its local-observable/flat-background definitions, transport definitions, admission conditions and required open-input declarations were inspected in bounded excerpts. No complete CA file or complete outline was read. File retrieval, hashes, searches and literal statement copying are bookkeeping only; no run discharges a proof step.

Current checkpoint: C5(a)–(c) and their route are saved here. The outstanding work is analytic supplier completion and the H-GXa/H-GXb mapping, not another derivation of the Gaussian pairing or tower identity. In particular, retain H-jet's nonflat and contracted equivariant estimates, H-tail-sum's exact rates, the fourth-order H-OP use, and actual product support admission. The unresolved source declarations are preserved; do not convert this note into an unconditional C5 or T0 proof.

## Result

**Ported statement:** `8.2:prop-gaussian-extraction`, CA-II:77279–77433, clauses (a), (b), (c), with its exact statement and its proof route through II:77859. The conditional-covariance recursion, Gaussian contractions, index count, colour factor and two-point tower deduction are written out. The analytic extraction estimates remain conditional on the named source and use-site inputs. This is a port of their route with explicit supplier obligations, not an independent proof of all printed antecedents.

**Filled steps:** F1 product jets and main/error split; F2 covariance recursion and empty composition; F3 covariance remainder products; F4 equivariant monomials and production indices; F5 derivative and Hessian replacements; F6 fourth Gaussian moment and diagonal factor; F7 one-line estimate and its flat vanishing; F8 cross-level coefficient and ordered-pair count; F9 complete nonflat derivative terms; F10 plaquette colour contraction; F11 all polynomial error allocations and absence of `L^(4r)`; F12 exact tail-summation obligation; F13 tower orthogonality and Gaussian conditional covariance; F14 telescoping and tail limit; F15 smearing, squared tails and running weights; F16 conditional-to-averaged covariance distinction; F17 the exponent-floor arithmetic. F9 and F12 expose the estimates still required; they do not claim to prove those analytic estimates.

**Corrections:** C1 states the product's actual support enclosure as an admission condition where the printed minimum-distance argument is insufficient; it keeps `ℓ+6C_W`. C2 includes the omitted Hessian-replacement error in the carried `Ψ_i` value and retains the nonflat derivative errors; it keeps the source's main coefficients. No source constants or routes have been changed. The corrections do not prove their analytic suppliers.

**Named hypotheses carried:** H-C2; H-C3a/b; H-C4a/b/c with every incomplete antecedent; H-q (`q≥21p_0+1`); H-corr and H-cluster; H-loc; H-OP and H-step (unwritten statements); H-alg, H-tr, H-pos and H-flow on their own domains; H-eq; H-flat, H-free and H-tail; H-geom/H-support; H-jet and H-tail-sum. For consumption by P9, **H-GXa and H-GXb remain open use-site hypotheses**, including H-source-use and H-depth. The clause table identifies what C5 supplies and what it does not.

This text credits Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Balaban at the cited uses. It grants no research-retention or audit status. **This text is not yet checked by another model.** Only `library/port/p9b-extraction.md` changed; no editable prompt file or platform instruction was modified.
