# P5 — Complete-account induction port

Provenance: Port of the complete account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; source revision 31a47c543775. Repository baseline c86830eb5. Research text only; no status conferred. Not yet checked by another model.

## Scope and source convention

This ports only chain-ca §7.2 tranche 5 rows A5, A6, A12 and A13. All six headings are unmarked in CA-I. Under CA-I:27–46, that means the account declares their proofs complete, as implications from their hypotheses. It does not mean those hypotheses are proved here. Source file throughout: `theorem_0_complete_account_raw_I.tex` at `31a47c543775` (abbreviated CA-I). Exact statement blocks preserve its LaTeX and labels. Proofs below follow its route.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Tadeusz Bałaban for the constructions and cited results individually identified below. Codex supplies the marked filled steps and corrections. No computation discharges any mathematical step.

Repository inputs have the standing specified by the owner at this revision: [p1-base.md](p1-base.md) is a checked port; [p3-free.md](p3-free.md) and [p4-operator.md](p4-operator.md) are ports; [mu.md](../mu.md) and [lrb.md](../lrb.md) are proved and refereed; [ui.md](../ui.md) is completed and checked; [oc.md](../oc.md) is being refereed. Older status sentences inside p4 do not override this current standing. Their hypotheses remain attached. P3 concerns free-field algebra and does not supply the interacting one-loop or unmarked-increment inputs below.

## Current checkpoint

All six conditional implications are ported below, with exact source statements, written proofs, marked filled steps, the A6-C1 reference correction, and named antecedents. The Result and recovery section record the remaining supplier obligations. This file is the current checkpoint. Only this repository file was edited.

## A5 — Large-field representation and bound

Source statement: CA-I:22860–22908. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{proposition}[Representation and bound of the large-field terms]\label{4.6:prop-large-field-bound}
Let $k$ be the level of the step, and let the family of configurations and the spaces
$\mathfrak{U}_k(X)$ be those of Convention~\ref{4.6:not-complex-domain}. Let $Z_k$ be the
large-field region and $Y_i$, $i$ in a finite index set, the regions of the outer datum of the
step, as in Definition~\ref{4.6:def-polymer-expansion}. Assume the
following.
\begin{itemize}
\item The hypotheses of Proposition~\ref{4.6:prop-logarithm-convergence}, that is, those of
Proposition~\ref{4.6:prop-activity-bound} together with the further one-sided condition on
$\bar{c}$ assumed in Proposition~\ref{4.6:prop-logarithm-convergence}.
\item The analyticity statement \eqref{4.6:eq-standing-bounds-c} of
Definition~\ref{4.6:def-standing-bounds}.
\item The following statements, on the family of Convention~\ref{4.6:not-complex-domain}: the
format statement, the statement on the prepared sequences of large-field regions, and the
positivity dichotomy of the large-field operations.
\item The one-sided condition \eqref{4.6:eq-constant-conditions-f}.
\end{itemize}
Let $\mathbf{R}'^{(k)}(X)$ be the logarithm terms of
Definition~\ref{4.6:def-polymer-logarithm}, and let $c_1(X)$ and
$K_{\mathrm{KP}}(d)=4e^{2(A_d+5^d)}$ be as in Proposition~\ref{4.6:prop-logarithm-convergence}.
Then the following hold.
\begin{enumerate}
\item[(a)] For every union $X$ of $M$-cubes and all $(\mathbf{U},\mathbf{J})\in\mathfrak{U}_k(X)$,
\begin{equation}\label{4.6:eq-large-field-bound-1}
\bigl|\mathbf{R}'^{(k)}(X,(\mathbf{U},\mathbf{J}))\bigr|
\le K_{\mathrm{KP}}(d)\,c_1(X)\,
\exp\Bigl(-\bigl(1+\tfrac12\beta\bigr)\kappa\, d_{k,\cup_i Y_i^{\sharp}}(X)\Bigr).
\end{equation}
\item[(b)] For every $X$ in the second group of Definition~\ref{4.6:def-polymer-logarithm},
that is, with
$X\sqcap\bigl(Z_k\cup\bigcup_i Y_i\bigr)^{\boxplus}=\emptyset$, and for all
$(\mathbf{U},\mathbf{J})\in\mathfrak{U}_k(X)$,
\begin{equation}\label{4.6:eq-large-field-bound-a}
\bigl|\mathbf{R}'^{(k)}(X,(\mathbf{U},\mathbf{J}))\bigr|
\le \exp\bigl(-p_0(g_k)\bigr)\exp\bigl(-\kappa\, d_k(X)\bigr).
\end{equation}
\item[(c)] Let $X$ be in the second group. The real unit point $(U,J)=(1,0)$ lies in
$\mathfrak{U}_k(X)$; write $\mathbf{R}'^{(k)}(X,1)$ for the value of
$\mathbf{R}'^{(k)}(X,\cdot)$ there. Then $|\mathbf{R}'^{(k)}(X,1)|$ obeys
\eqref{4.6:eq-large-field-bound-a}, and the shifted member
$\mathbf{R}'^{(k)}(X,\cdot)-\mathbf{R}'^{(k)}(X,1)$ obeys
\eqref{4.6:eq-large-field-bound-a} with an extra factor $2$ on the right-hand side. If
condition \eqref{4.6:eq-constant-conditions-f} holds with $2K_{\mathrm{KP}}(d)$ in place of
$K_{\mathrm{KP}}(d)$, the shifted member obeys \eqref{4.6:eq-large-field-bound-a} itself.
\item[(d)] For every union $X$ of $M$-cubes the function $\mathbf{R}'^{(k)}(X,\cdot)$ depends
only on the variables on $X$, and it is an
analytic function of $(\mathbf{U},\mathbf{J})$ on $\mathfrak{U}_k(X)$.
\end{enumerate}
\end{proposition}
```

### Inputs and proof

Proof locus: CA-I:22920–23036. The source's comparison with Balaban CMP 122b (1.99), (1.100), p.390 is at 22910–22917. The relative length here uses the strips \(Y_i^\sharp\), exactly as printed; it is not silently replaced by the unthickened \(Y_i\).

**Named inputs.**

| Name / CA label | Locus | Standing and exact use |
|---|---|---|
| P5-H-log, `4.6:prop-logarithm-convergence` | CA-I:22645–22858; p1 §6 | Checked conditional port. Absolute and uniform convergence and the displayed bound, with all p1 hypotheses retained. The bracket identity is finite-volume; no infinite-volume total logarithm is asserted. |
| P5-H-domain, `4.6:not-complex-domain` | CA-I:20187–20286 | Common analytic domain and restriction maps, assumed as supplied. Use only the largest member on which all inputs hold. |
| P5-H-activity, `4.6:prop-activity-bound` | CA-I:22393–22395; conditional fragment `4.6:prf-activity-summation`, 22397–22643 | The proposition's statement is explicitly not written out. Retain p1's H-activity estimate and H-activity-supplier (localization, first-step bound, geometric claims (i),(ii), remaining supplier hypotheses). No closure is inferred from its label. |
| P5-H-standing, `4.6:def-standing-bounds` (a),(b),(c) | CA-I:21314–21419 | Island bound, interaction bound, analyticity. Assumed; retain p1's H-island, H-interaction, H-analytic. |
| P5-H-format, P5-H-prepared, P5-H-positive | CA-I:22871–22875; format through `4.6:def-step-datum`, `4.6:def-polymer-expansion` (20609 onward) | The format, prepared large-field sequences, positivity dichotomy are explicit hypotheses. The dichotomy is listed proof outstanding at 166624. Their application to every relevant domain remains an input. |
| P5-H-real-slice | CA-I:22980–22984 | The real-slice assertion for the chosen class puts \((1,0)\) in its domain. Retained as the explicitly invoked input; analyticity alone does not put a centre in a domain. |
| P5-H-geometry, `4.6:def-strips-bracket`, `4.6:def-tree-lengths`, `4.6:def-geometric-facts` | p1 §§3–4; CA-I:20441–20607, 20929–21003; use 22931–22958 | Strip inclusion, cell content of an island, core and relative-tree conventions. Their supplied geometry is retained. |
| `4.6:lem-tree-cubes` | CA-I:21544–21641; p1 §4.2 | Checked port: a tree of length \(M\ell\) meets at most \(5^d(\ell+1)\) cubes. |
| P5-H-constants, `4.6:def-constant-conditions` | p1 §4.5; CA-I:21421–21465; exact condition (f) at 21462–21464 | All conditions of P5-H-log, plus \(\beta\kappa(5^{-d}\check R_k^d-1)\ge2\log K_{\rm KP}(d)\). For the last part of (c), replace only \(K_{\rm KP}\) here by \(2K_{\rm KP}\), as the source requires. |
| P5-H-locality, `4.6:rem-interaction-locality` | CA-I:20731–20755; assumed at 20767 | Balaban CMP 122b p.379, printed without proof; local dependence of the interaction on its named domain. Required for the representation and the locality part of (d); carried from checked p1, not discharged by it. |

**Proof (a).** P5-H-log gives, uniformly on the stated domain,
\[
|\mathbf R'^{(k)}(X)|\le K_{\rm KP}(d)c_1(X)
 e^{-(1+\beta/2)\kappa d_{\rm out}(X)}.
\]
The definition of relative length is \(d_{\rm out}(X)=d_{k,\cup_iY_i^\sharp}(X)\). Substituting proves (a).

**Proof (b).** The second-group condition excludes all cubes touching \(Z_k\cup\bigcup_iY_i\). Since \(Y_i^\sharp\subset Y_i^\boxplus\subset(Z_k\cup\bigcup_jY_j)^\boxplus\), it excludes every outer strip. Thus \(c_1(X)=e^{-p_0(g_k)}\), \(\operatorname{core}X=X\), and \(d_{\rm out}(X)\ge d_k(X)\), by the supplied geometry. The last inequality compares the relative connecting problem with the ordinary tree visiting these core cubes; it is not an assertion for arbitrary relative metrics.

If the defining series has no polymer tuple with union \(X\), it is zero. Otherwise choose one polymer \(P\) in such a tuple. It also avoids every outer strip. The second case of P5-H-activity's geometric supplier gives an island \(X_a\) with \(X_a\subset X_a^\sharp\subset P\subset X\). An island contains a level-\(k\) cell, hence \(\check R_k^d\) distinct \(M\)-cubes. A tree visiting the cubes of \(X\), of length \(Md_k(X)\), meets these cubes. The tree-cube lemma yields
\[
\check R_k^d\le5^d(d_k(X)+1),\qquad d_k(X)\ge5^{-d}\check R_k^d-1.
\]
**A5-F1 (filled).** If the tree length is defined as an infimum, apply the lemma to lengths \(M(d_k(X)+\epsilon)\), then let \(\epsilon\downarrow0\). No minimizer or machine search is needed. Condition (f) now gives
\[
\log K_{\rm KP}(d)\le \tfrac12\beta\kappa d_k(X).
\]
Substitute in (a):
\[
|\mathbf R'^{(k)}(X)|\le e^{-p_0(g_k)}e^{-\kappa d_k(X)}
 \left[K_{\rm KP}(d)e^{-(\beta/2)\kappa d_k(X)}\right]
\le e^{-p_0(g_k)}e^{-\kappa d_k(X)}.
\]
The same argument covers all outer variables and every point of the common domain, since each input is uniform there.

**Proof (c).** P5-H-real-slice supplies the point \((1,0)\). Apply (b) there and at the variable pair. The triangle inequality gives the factor 2. With strengthened (f), repeat the preceding absorption with \(\log(2K_{\rm KP})\). Then
\[
|\mathbf R'(X,u)-\mathbf R'(X,1)|
\le e^{-p_0(g_k)}e^{-\kappa d_k(X)}
 [2K_{\rm KP}e^{-(\beta/2)\kappa d_k(X)}]
\le e^{-p_0(g_k)}e^{-\kappa d_k(X)}.
\]
**A5-F2 (filled).** The shift is of each union-filed logarithm member. On a finite system absolute convergence allows evaluating and subtracting the centre term by term. Thus \(\sum_X R'(X,u)=\sum_X R'(X,1)+\sum_X[R'(X,u)-R'(X,1)]\). The first sum supplies the vacuum constant. This does not subtract partition functions before taking a logarithm.

**Proof (d).** Each activity is a finite sum of products of interactions and island operations, with integrals in interpolation parameters \(t\in[0,1]\). P5-H-standing(c) supplies holomorphy of the island operation applied to an analytic integrand. Every interaction depends on its own \(Y\subset P\). Every island operation depends on its island strip and collar, contained in \(P\). These locality inputs put the entire activity on \(P\).

**A5-F3 (filled).** Integration preserves the asserted holomorphy: on a compact coordinate polydisc in the common domain the integrands are locally uniformly bounded and continuous in \(t\), under the standing analytic/operation hypothesis. Apply their Cauchy formula on a smaller polydisc and interchange its compact contour integral with the \(t\)-integral. The integrated function has the same Cauchy formula and is holomorphic. The actual island integrals are covered by the analytic-operation hypothesis, rather than by an unsupported assertion about moving cutoff supports.

A term in the union-filed series is a finite product of activities on \(P_\nu\subset X\), pulled back by the supplied restriction maps. It is therefore holomorphic on \(\mathfrak U_k(X)\) and depends only on the pair on \(X\). P5-H-log bounds the absolute tail uniformly. On a compact polydisc, pass to the limit in the Cauchy formula for partial sums. This proves holomorphy of the sum, including in the independent-current coordinates. If two ambient pairs agree on \(X\), all partial sums agree and so do their limits. This proves locality. The argument is in each finite-dimensional local chart; it does not require convexity of the whole domain. All four clauses follow. \(\square\)


## A6.1 — Cauchy extraction of the beta coefficient

Source statement: CA-I:32226–32289. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{proposition}[The large-field part of the beta coefficient by Cauchy extraction]
\label{4.7:prop-beta-extraction}
Fix $k$ such that the induction hypothesis $\mathfrak{i}(k)$ holds and
$x_0,\dots,x_k\ge\gamma^{-2}$, where $\gamma\le 1$. Assume the hypotheses of
Corollary~\ref{4.7:cor-kernel-power-bound}, the conditions $(\Gamma0)$--$(\Gamma6)$ of
Definition~\ref{4.7:def-smallness-conditions}, and $\kappa_0\ge 17$. Put
$\kappa_1=\kappa_0-5$ and $C_{\mathfrak{R}}:=2K_{CE}$. Assume further the following
statements.
\begin{itemize}
\item[(A1)] The power bound for large-field-descended kernels at every level, that is, the
bound $(E)$ of Corollary~\ref{4.7:cor-kernel-power-bound}, display
\eqref{4.7:eq-kernel-power-bound-a}. At $i=k+1$, $g_{k+1}$ is replaced, in the bound and in
the radii, by the stand-in $\tilde{g}=g_k$.
\item[(A2)] True pairs lie in the regularity class, as stated in
Definition~\ref{4.7:not-true-pairs}.
Here a true pair is a pair consisting of a configuration and its current. The constant
$c_T$ and the radius $r_j$ of the polydisc norm $N_j$ are those of display
\eqref{4.7:eq-true-pairs-a}.
\item[(A3)] The decay bound \cite[Proposition~9, (190)]{B-CMP102b}, taken at the real
background $1$, together with the remark in \cite{B-CMP109} that the same estimate holds
for the derivative $H_j=D\mathbf{H}_j(0)$ of the nonlinear potential function
$\mathbf{H}_j$ of that paper and for the second-order operators applied to
$\mathbf{H}_j$: for every bond $b$ and every $X$,
\begin{equation}\label{4.7:eq-beta-extraction-3}
N_j(H_j\delta_b\lceil X)\le C_{\mathsf{h}}e^{-\delta_0\operatorname{dist}(b,X)},
\end{equation}
where $\delta_b$ is the unit element at the bond $b$ and $\lceil X$ denotes restriction
to $X$.
\item[(A4)] The second-moment bound for whole-lattice sums, which evaluates the coefficient
of \cite[(5.42)]{B-CMP109} (see also \cite[(3.62)]{B-CMP119}). Let $C_A$ be a constant with
\begin{equation*}
\sum_X\bigl(Md_j(X)+c\bigr)^2e^{-\kappa d_j(X)}\le C_A ,
\end{equation*}
where $c$ is the constant of that second-moment formula. There is a constant $C_{\Pi}$,
containing the factor $4C_{\mathsf{h}}^2C_A$, such that
the following holds. If a whole-lattice sum $\Pi(b,b')=\sum_X\Pi_X(b,b')$ at level $j$ has,
for some $S_j>0$ and for all $X$, $b$, $b'$, summands bounded by
\begin{equation*}
|\Pi_X(b,b')|\le\frac{4C_{\mathsf{h}}^2S_j}{(c_Tr_j)^2}\,
e^{-\kappa d_j(X)-\delta_0[\operatorname{dist}(b,X)+\operatorname{dist}(b',X)]},
\end{equation*}
then the coefficient $\beta$ that \cite[(5.42)]{B-CMP109} assigns to $\Pi$ satisfies
$|\beta|\le C_{\Pi}S_j(c_Tr_j)^{-2}$.
\end{itemize}
Let $C'$ be the constant defined in \eqref{4.7:eq-beta-extraction-a} below, and let
$\bar{\varsigma}:=C'\gamma^{\kappa_0-8}$ be the ceiling for $|\beta^{\mathfrak{R}}|$
used in the induction along the coupling flow.

Then for every $j\le k$
\begin{equation}\label{4.7:eq-beta-extraction-1}
|\beta^{\mathfrak{R}}_j|\le C'g_j^{\kappa_1-2}=C'g_j^{\kappa_0-7},
\end{equation}
and at $j=k+1$ the bound \eqref{4.7:eq-beta-extraction-1} holds with $g_{k+1}$ replaced by
the stand-in $\tilde{g}=g_k$.
This bound is free of $k$, $K$, $m$, of position and of the site. At $j=k+1$, with
$C_{\Pi}$ the constant of (A4), which contains the factor $4C_{\mathsf{h}}^2C_A$,
\begin{equation}\label{4.7:eq-beta-extraction-a}
\begin{gathered}
C':=\frac{2C_{\Pi}K_{CE}}{(c_T\min\{C_0,C_1\})^2},\\
|\beta^{\mathfrak{R}}_{k+1}|\le C'g_k^{\kappa_0-7}\le C'\gamma^{\kappa_0-7}
\le C'\gamma^{\kappa_0-8}=\bar{\varsigma}.
\end{gathered}
\end{equation}
\end{proposition}
```

### Inputs and proof

Proof locus: CA-I:32291–32410. This is a Cauchy-extraction implication, not a derivation of Balaban's response estimate or of the tensor's second-moment formula.

**Named inputs.** P5-H-induction is the already reached level hypothesis \(\mathfrak i(k)\), with \(x_0,\ldots,x_k\ge\gamma^{-2}\). P5-H-smallness is `4.7:def-smallness-conditions`, CA-I:31784–31999, including its complete displayed ceilings, floors and prose supplements. Its constant order fixes \(K_{CE},C_\Pi,c_T,C_0,C_1\) before the last coupling ceiling. The following hypotheses are separate.

| Name / label | Source and standing |
|---|---|
| P5-H-E, `4.7:cor-kernel-power-bound` | CA-I:32000–32224. Unmarked conditional proof. Its statement at 32000–32049 assumes the marked cluster bound \(K_{CE}=4b^{\rm adm}/\nu_{CL}\), `4.7:lem-potential-splitting` (30329 onward), marked-family theorem (a), own-coefficient rule, the coupling-power-sum lemma (b), earlier-level volume cancellation, localized independence, class restrictions, and CMP 116 Lemma 1 (1.34) on \(U^{\Sigma^1}\). These are carried inputs; this port does not prove the corollary's supplier package. The actual bound is \(S_j=2K_{CE}g_j^{\kappa_0-5}\). |
| P5-H-true, `4.7:not-true-pairs` = (A2) | CA-I:29522–29614. Conditional membership statement and proof, despite the heading “definition.” It assumes the small-field exponential lemma, hereditary membership and Balaban CMP 109 (1.17), cited as printed also at each label with cube side \(M/L\). |
| P5-H-decay = (A3) | CA-I:32241–32253. Balaban CMP 102b Proposition 9 (190), at background 1, plus the derivative/second-order extension attributed to CMP 109. Retain exactly the stated \(C_{\mathsf h},\delta_0\) estimate. ui's checked weaker-rate repair does not itself supply this separate estimate at the printed rate. |
| P5-H-moment = (A4) | CA-I:32254–32268. The displayed \(C_A\) summation and the \(C_\Pi\) second-moment implication, using CMP 109 (5.42), CMP 119 (3.62). Cited/assumed; not proved by the Cauchy step. The whole-lattice summation and coefficient convention must be the same at every use. |
| P5-H-compose | CA-I:32302–32308; Balaban CMP 109 (4.2) | Identification of the constrained background with \(\exp(i\xi\mathbf H_j)\), in the same chart and at its own current. Cited input. |
| P5-H-stationary | CA-I:32319–32322; Balaban CMP 109 (4.14) | Vanishing of the first variation of each kernel at 1. Cited input. It is needed for the chain-rule cancellation, independently of the bound on the kernel. |
| `4.7:not-kernel-families`, `4.7:not-running-couplings` | CA-I:30112–30186, 29060–29105 | Definitions/standing conventions. \(r_j=c_*g_j(\log g_j^{-2})^q\), \(c_*:=\min\{C_0,C_1\}\); at the new level every radius and bound uses \(g_k\). The own-coefficient marking is retained. |

The inherited P4 uses of [mu](../mu.md), [lrb](../lrb.md), [ui](../ui.md), and [oc](../oc.md) retain the current standing recorded above. None replaces P5-H-moment or P5-H-decay. In (A4), the displayed \(\sum_X\) has no anchor printed beside it. Its summation convention is an unresolved part of P5-H-moment. If it meant all translates without an anchor or spatial weight on \(\mathbb Z^4\), the displayed \(C_A\) bound would diverge: infinitely many translates of one fixed polymer have the same positive summand. This port assumes (A4) exactly as stated for the coefficient construction; it neither proves that unrooted bound nor silently replaces it by an anchored theorem.

**Proof.** For each union \(X\), set
\[
\mathcal F_X(Z)=E^{(j),\mathfrak R}(X;e^{i\xi Z},J(e^{i\xi Z})),\qquad
H_j=D\mathbf H_j(0).
\]
The coefficient is extracted from
\[
\Pi^{(j),\mathfrak R}(b,b')=\sum_X
 \partial_{B(b)}\partial_{B(b')} E^{(j),\mathfrak R}(X,U_j(e^{iB}))\big|_{B=0}.
\]
By P5-H-compose the summand is the second derivative of \(\mathcal F_X\circ\mathbf H_j\). The chain rule gives
\[
D^2\mathcal F_X(0)[H_j\delta_b,H_j\delta_{b'}]
+D\mathcal F_X(0)[D^2\mathbf H_j(0)[\delta_b,\delta_{b'}]].
\]
P5-H-stationary kills exactly the second term. This is why a kernel bound alone would not suffice.

For complex \(s,t\), define \(f(s,t)=\mathcal F_X(sH_j\delta_b+tH_j\delta_{b'})\), and set
\[
\rho_b=\frac{c_Tr_j e^{\delta_0\operatorname{dist}(b,X)}}{2C_{\mathsf h}},\qquad
\rho_{b'}=\frac{c_Tr_j e^{\delta_0\operatorname{dist}(b',X)}}{2C_{\mathsf h}}.
\]
On these radii, P5-H-decay and the triangle inequality give the restricted norm bound
\[
N_j((sH_j\delta_b+tH_j\delta_{b'})|_X)
\le |s|C_{\mathsf h}e^{-\delta_0\operatorname{dist}(b,X)}
 +|t|C_{\mathsf h}e^{-\delta_0\operatorname{dist}(b',X)}\le c_Tr_j.
\]
Locality, the prescribed local norm (including its required collar), and P5-H-true put these true pairs in the class. Thus \(|f|\le S_j e^{-\kappa d_j(X)}\), with \(S_j=C_{\mathfrak R}g_j^{\kappa_1}\).

**A6-F1 (filled).** To avoid assuming holomorphy beyond a closed domain boundary, first integrate on radii \((u\rho_b,u\rho_{b'})\), \(0<u<1\). The two-variable Cauchy formula is
\[
\partial_s\partial_t f(0,0)=\frac1{(2\pi i)^2}
 \int_{|s|=u\rho_b}\int_{|t|=u\rho_{b'}}\frac{f(s,t)}{s^2t^2}\,dt\,ds.
\]
Taking absolute values cancels the contour lengths against one denominator power. Letting \(u\uparrow1\) gives
\[
|\Pi_X(b,b')|\le\frac{4C_{\mathsf h}^2 S_j}{(c_Tr_j)^2}
 e^{-\kappa d_j(X)-\delta_0[\operatorname{dist}(b,X)+\operatorname{dist}(b',X)]}.
\]
If \(b=b'\), the two-variable formula still computes \(D^2\mathcal F_X(0)[H_j\delta_b,H_j\delta_b]\); there is no extra factorial. Both parameter directions were budgeted separately.

This is precisely (A4)'s premise. Therefore
\[
|\beta_j^{\mathfrak R}|\le C_\Pi S_j(c_Tr_j)^{-2}.
\]
All summation and passage to the whole-lattice coefficient here belong to P5-H-moment. They are not justified by interchanging a conditionally convergent infinite sum. The identical calculation for any other family obeying the same first-variation cancellation and true-pair bound \(S_je^{-\kappa d_j(X)}\) yields the source's `4.7:eq-beta-extraction-6`.

**A6-C1 (correction: wrong smallness-condition reference).** CA-I:32383–32389 attributes \((\log g_j^{-2})^q\ge1\) to \((\Gamma4f)\). The actual (f), at 31823, is a ratio bound, not that logarithmic floor. For the standing integer exponent \(q\ge1\), use (e), \(\gamma\le e^{-q}\): then \(\log g_j^{-2}\ge2q\ge1\). More generally the account's standing ceiling \(\gamma\le1/2\) at CA-I:1724–1727 gives the same floor for every \(q>0\). Indeed \(e=\sum_{n\ge0}1/n!\le3<4\), since \(n!\ge2^{n-1}\) for \(n\ge1\); hence \(\log4>1\). If the proposition is detached from both these standing choices and permits \(0<q<1/2\), explicitly retain \(\gamma\le e^{-1/2}\) as the needed logarithmic-floor hypothesis. No value of \(C'\) or exponent changes.

**A6-F2 (filled).** With the applicable logarithmic floor,
\[
(c_Tr_j)^{-2}=(c_Tc_*)^{-2}g_j^{-2}(\log g_j^{-2})^{-2q}
\le(c_Tc_*)^{-2}g_j^{-2}.
\]
Insert \(C_{\mathfrak R}=2K_{CE}\), \(\kappa_1=\kappa_0-5\). This gives exactly
\[
|\beta_j^{\mathfrak R}|\le
 \frac{2C_\Pi K_{CE}}{(c_Tc_*)^2}g_j^{\kappa_1-2}
 =C'g_j^{\kappa_0-7}.
\]
At \(j=k+1\), the same proof uses \(g_k\) for the bound and for \(r_{k+1}\); it does not assume \(g_{k+1}\) exists or is small. Since \(g_k\le\gamma\le1\) and \(\kappa_0-7>0\),
\[
|\beta_{k+1}^{\mathfrak R}|\le C'g_k^{\kappa_0-7}
\le C'\gamma^{\kappa_0-7}\le C'\gamma^{\kappa_0-8}=\bar\varsigma.
\]
**A6-F3 (filled).** Because \(C'>0\) is fixed before \(\gamma\) and \(\kappa_0-8\ge9>0\), the last ceiling follows by taking
\(\gamma\le[\min\{c_0/4,1\}/C']^{1/(\kappa_0-8)}\), intersected with all earlier ceilings. This changes no earlier constant. Uniformity in level, site, position, \(m,K\) is inherited from the explicitly uniform five constants defining \(C'\). \(\square\)


## A6.2 — Large-field coupling increment

Source statement: CA-I:32412–32458. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{proposition}[The large-field part of the coupling increment]\label{4.7:prop-coupling-increment}
Fix a level $k$ in the induction over levels that constructs the coupling flow (called below the level induction), and assume the following.
\begin{itemize}
\item The induction hypothesis $\mathfrak{i}(k)$ of the level induction holds, together with its hypotheses $(\gamma_k)$, taken with domain the one-power hereditary class $U^{\Sigma^1}$, and its flow hypothesis $(\beta_k)$. Moreover $x_0,\dots,x_k\ge\gamma^{-2}$, and $\gamma$ lies below the ceilings of the level induction.
\item The conditions $(\Gamma0)$--$(\Gamma6)$ and $(\varphi1)$--$(\varphi6)$ of \eqref{4.7:eq-smallness-conditions-a} hold, condition $(\Gamma6)$ being taken with its member (vi), which carries the factor $86d$, as fixed in Definition~\ref{4.7:def-smallness-conditions}. The floor $(\varphi B)$ of that display is adopted, as in Corollary~\ref{4.7:cor-kernel-power-bound}, but is not used below. Moreover $\gamma\le1$ and $\kappa_0\ge17$, and hypothesis (A3) of Proposition~\ref{4.7:prop-beta-extraction} holds.
\item Clauses (N) and (F) of the operator bounds at free current hold. So do the following clauses of the frame lemma, which those two clauses use beyond their own statement: part (a) of its first clause and part (ii) of its fourth clause, which carry the cost of the adjoint action of the frame map; its second clause, the bound on the global supremum of the window data by a multiple of $M\alpha_0$; its third clause, which accompanies that bound; and its fifth clause, the linear clause. So does the corollary supplying the operator bounds at free current, applied layer by layer.
\item The one-power hereditary class $U^{\Sigma^1}$ is the class of the induction. The hypotheses $(\gamma_k)$ and $(H_{\cdot})$, the condition \cite[(3.16)]{B-CMP109}, the hypothesis space $\mathfrak{U}$ of \cite[Lemma~4]{B-CMP109}, and the bound (E) of \eqref{4.7:eq-kernel-power-bound-a} are taken with domain $U^{\Sigma^1}$. Condition \cite[(1.12)]{B-CMP109} is taken in the form fixed in \eqref{4.7:eq-class-restrictions-a}. Collars are the cut $Z^{\wr p}$ of the class at every label, not the collar made of Ba{\l}aban's own cubes.
\item The restrictions \eqref{4.7:eq-class-restrictions-a} of the regularity class with its cube gauge condition (Definition~\ref{4.7:not-class-restrictions}) hold, and so does the proposition on membership in that class with its near, far and true-pair clauses. These rest on three inputs:
\begin{itemize}
\item the lemma on admissible towers accompanying the operator bounds at free current, at scale $M/L$;
\item the nesting lemma for \cite[(3.38)]{B-CMP109}, taken with the single factorisation $U:=1$ used in \cite{B-CMP109};
\item \cite[(1.17)]{B-CMP109}, cited as printed.
\end{itemize}
\item The following further statements are available:
\begin{itemize}
\item the corollary furnishing the constant $K_{CE}$ of \eqref{4.7:eq-kernel-power-bound-a};
\item clauses (a) and (d) of the theorem on the marked and unmarked kernel families, together with the convention extending the kernels to the whole lattice;
\item the statement that true pairs lie in the regularity class (Definition~\ref{4.7:not-true-pairs}), called below the true-pair statement;
\item the independence of the localised terms from the small-field region (Corollary~\ref{4.4:cor-localised-independence});
\item the lemma giving existence of the whole-lattice tensor and site-freeness of the coefficient (the tensor lemma), at all indices $\le k$.
\end{itemize}
\end{itemize}
Then the following hold.
\begin{itemize}
\item[(a)] The coefficient splits as
\begin{equation*}
\beta_{k+1}=\beta^{\mathfrak{A}}_{k+1}+\beta^{\mathfrak{R}}_{k+1}.
\end{equation*}
Each summand is the coefficient \cite[(5.42)]{B-CMP109} of the whole-lattice tensor of its own sub-family: the regular sub-family for $\beta^{\mathfrak{A}}_{k+1}$, the large-field-descended one for $\beta^{\mathfrak{R}}_{k+1}$. Two things are not asserted here: the existence of the $\mathbb{Z}^4$ tensor at every admissible site, and the site-freeness of $\beta_{k+1}$. Both are conclusions of the tensor lemma.
\item[(b)] The large-field part is bounded by
\begin{equation*}
|\beta^{\mathfrak{R}}_{k+1}|\le C'g_k^{\kappa_0-7}\le\bar{\varsigma},
\end{equation*}
with $C'$ and $\bar{\varsigma}$ as in \eqref{4.7:eq-beta-extraction-a}.
\item[(c)] The bound (E) of \eqref{4.7:eq-kernel-power-bound-a}, with $C_{\mathfrak{R}}$ and $\kappa_1=\kappa_0-5$ as there, holds for every $i\le k+1$, every localisation domain $X\in\mathbf{D}_i$ and every pin $z$, for two families of kernels: the unpinned kernels of \cite[(2.13)]{B-CMP116}, and the kernels $E^{(i),\mathfrak{R}}_{\mathfrak{s}}(X;\cdot,z)$ pointed at $z$ of \cite[(3.44)--(3.47)]{B-CMP119}. It holds at every admissible site $\mathfrak{s}\in\mathcal{S}_i^{\flat}$ on $U^{\Sigma^1}_i(X;\alpha_{0,i},\alpha_{1,i})$, where these kernels are analytic and $G^c$-gauge invariant. Hence (E) holds on the polydisc
\begin{equation}\label{4.7:eq-coupling-increment-1}
\bigl\{\mathbf{U}=\exp(\sqrt{-1}\,A)\ :\ \sup_X|A|<a^{\mathfrak{R}}_i,\ \ \sup_X|\mathbf{J}|<a^{\mathfrak{R}}_i\bigr\},
\end{equation}
with
\begin{equation}\label{4.7:eq-coupling-increment-a}
a^{\mathfrak{R}}_i:=\frac{\xi_i^{3}\,c_T\,r_i}{8d}>0,\qquad E^{\mathfrak{R}}_i:=C_{\mathfrak{R}}\,g_i^{\kappa_1},
\end{equation}
where $\xi_i=L^{-i}$ is the spacing at which the lattice differences in the proof below are taken, $c_T$ is the constant of \eqref{4.7:eq-true-pairs-a}, and $r_i$ is the radius with which the true-pair statement is formulated in Definition~\ref{4.7:not-true-pairs}; the quantities $a^{\mathfrak{R}}_i$ and $E^{\mathfrak{R}}_i$ are free of $\mathfrak{s}$, $X$ and $z$.

At $i=k+1$ the coupling $g_{k+1}$ is replaced by the stand-in $\tilde{g}=g_k$. There clause (c), with $\tilde{g}$ in the bound and in the radii, is the hypothesis $(H_{k+1})$(d) of the tensor lemma for the large-field-descended sub-family, namely its bound at the stand-in $\tilde{g}:=g_{j-1}$, taken at $j=k+1$. For $i\le k$ the bound, at the true couplings, re-proves what the hypothesis $(H_i)$(d) received from this proposition at induction index $i-1$.
\end{itemize}
\end{proposition}
```

### Inputs and proof

Proof locus: CA-I:32460–32496. The kernel-bound and domain clauses are proved first below; the coefficient then uses the extraction just ported. This is the same source argument, with its dependency order made explicit.

**Named inputs and inherited standing.**

| Name | Label / locus | Standing and role |
|---|---|---|
| P5-H-induction | \(\mathfrak i(k),(\gamma_k),(\beta_k),(H_i)\); CA-I:32413–32418, 32431 | Earlier levels only; assumed with the one-power domains and true earlier couplings. |
| P5-H-smallness | `4.7:eq-smallness-conditions-a`, CA-I:31809–31862 | All Γ0–Γ6, φ1–φ6; φB adopted but unused in this proof. Γ6(vi) is the printed condition with coefficient \(172d\), carrying the stated \(86d\) cost with its margin; do not replace it by a weaker ceiling. |
| P5-H-operator | `4.5:thm-operator-bounds`, CA-I:19578–19743, clauses (N),(F) | Conditional port in p4, with its Balaban, analytic-domain and chart hypotheses. ui supplies the completed, checked increment input. |
| P5-H-frame / P5-H-hereditary-operator | CA-I:32416; frame `4.5:lem-literal-frame`, 17519 onward; layerwise corollary used at 32416 | Precisely first clause (a), second and third clauses, fourth clause (ii), fifth clause; adjoint-frame costs retained. Layerwise operator supply is a separate assumed input, not an automatic consequence of a single-domain estimate. |
| P5-H-restriction / P5-H-membership | `4.7:not-class-restrictions`, CA-I:30188–30327; use 32417–32424 | Restriction statements and near/far/true-pair membership with their actual collars \(Z^{\wr p}\). The near statement is not fully printed at `4.8:prop-near-case`, 33598; its descriptive input remains named. `4.8:prop-far-case` (33839 onward), `4.8:prop-small-pairs` (34058–34189), `4.8:prop-class-reproduction` (34241 onward) are conditional implications, not unconditional domain supply. |
| P5-H-towers / P5-H-nesting | CA-I:32420–32423 | Admissible towers at \(M/L\), and nesting for CMP 109 (3.38) with the single factorization \(U:=1\). mu supplies `4.13:lem-minimizer-unique` at its proved and refereed scope, retaining its published inputs and the unconfirmed CMP 98 Proposition 4 (134) OCR noted in mu. No claim about later stage radii follows. |
| P5-H-109-1.17 | CA-I:32424, 32485; `4.8:prop-small-pairs` hypothesis at 34067–34072 | Balaban CMP 109 (1.17), printed without proof, applied at complex pairs at every label, both tower rules, with \(M/L,LB^{109}\). This stronger application is assumed explicitly. Neither mu nor oc discharges it. |
| P5-H-marking / P5-H-extension | CA-I:32427–32428; notation `4.7:not-kernel-families`, 30112–30186 | Marked/unmarked theorem (a),(d), own coefficients, whole-lattice extension. Named supplied statements; their full proofs are not ported here. |
| P5-H-E, P5-H-true, P5-H-decay, P5-H-moment | Above; CA-I:32000–32049, 29522–29614, 32241–32268 | Conditional kernel bound and true-pair inclusion; cited decay and second-moment inputs. Carry all extraction premises, including P5-H-compose and P5-H-stationary, at the new level. The moment input is used when the proof invokes beta extraction, even though the coupling proposition singles out only (A3) in its second bullet. |
| P5-H-localised | `4.4:cor-localised-independence`, CA-I:9615–9791 | Conditional port in p4; lrb is proved and refereed under its own (a)–(d) and CMP 116 (2.14) setting. |
| P5-H-tensor | “tensor lemma,” CA-I:32431; level hypothesis at 58219–58275 of `4.38:thm-torus-independence` | Earlier-index tensor existence and site-freeness. Do not assume the new-level conclusion to obtain its own analytic bound. |

P5-H-E already uses the extraction bound for earlier coefficients through `4.7:lem-potential-splitting`, CA-I:30561–30573. **A6-F4 (filled)** makes the order explicit: previous-level bounds and the cluster statement give new-level (E); (E), true-pair admission and (A3)–(A4) give new-level extraction. Any supplier of the corollary that requires the new coefficient in advance would not satisfy this level ordering. No whole-theorem circular invocation is allowed.

**(a), family splitting.** By P5-H-marking, the effective family is the sum of its regular and large-field-descended families, with the prescribed whole-lattice convention. Differentiation is linear on each finite partial sum. At an admissible coefficient construction, the tensor and moment sums supplied by P5-H-tensor/P5-H-moment preserve this equality. CMP 109 (5.42) is a linear functional of the tensor, so
\(\beta_{k+1}=\beta^{\mathfrak A}_{k+1}+\beta^{\mathfrak R}_{k+1}\).
This is a decomposition of the coefficient once constructed. Like the source, it does not establish existence of an infinite-volume tensor at every new site, or site-freeness. Those conclusions belong to the tensor/torus step.

**(c), the bound on the class.** Invoke P5-H-E at every \(i\le k+1\). It supplies both pinned and unpinned kernels, their analyticity and gauge invariance, at every admissible site:
\[
|E^{(i),\mathfrak R}(X,\cdot)|,\ |E^{(i),\mathfrak R}(X,\cdot,z)|
\le C_{\mathfrak R}g_i^{\kappa_1}e^{-\kappa d_i(X)}.
\]
For \(i\le k\) all quantities use the true \(g_i\); at \(k+1\) all use \(g_k\).

To get the claimed polydisc, put \(h=\xi_i=L^{-i}\), \(a=h^3c_Tr_i/(8d)\), and suppose \(\|A\|_{\infty,X},\|\mathbf J\|_{\infty,X}<a\). Extend \(A\) by zero, and put \(Z=A/h\). This extension never increases the supremum, including for a domain with holes.

**A6-F5 (filled: units and finite differences).** In `4.7:not-true-pairs`, the letter fixing the reference spacing is a dummy reference index. Choose that reference to be \(i+1\). Then \(\eta=L^{-i}=h\), \(\ell_i=1\), and \(e^{i\eta Z}=e^{iA}\), as required here. On this mesh a first difference has size at most \(2h^{-1}\|Z\|_\infty\). A second difference in one direction has size at most \(4h^{-2}\|Z\|_\infty\). Therefore
\[
\|\Delta Z\|_\infty\le4d h^{-2}\|Z\|_\infty,
\qquad\|\partial^*\partial Z\|_\infty\le8(d-1)h^{-2}\|Z\|_\infty.
\]
For the latter estimate, each component is a sum over the other \(d-1\) directions of two second-difference terms, each with at most four signed translates. This remains true across the zero-extension boundary. With \(h\le1\), the norm defined at CA-I:29525–29528 obeys
\[
N_i(Z)\le\max\{h^{-1},2h^{-2},4dh^{-3},8(d-1)h^{-3}\}\|A\|_\infty
\le8dh^{-3}\|A\|_\infty<c_Tr_i.
\]
These are the coordinate lattice differences of that small-field norm; no uncontrolled change to a nonunitary frame is being made.

P5-H-true now gives the true pair \((e^{iA},J(e^{iA}))\) in the regular class. The definition of that class, CMP 109 (1.10)–(1.16) in its stipulated reading, splits its conditions. Conditions (i),(ii),(iv), and the first inequality of (1.14), depend on \(\mathbf U\) alone. The membership input supplies (iv) at every label \((p,Z)\), for both towers, with exactly the one-power radius. Its proof uses the separately retained P5-H-109-1.17 at \(M/L\); a true pair at the top label alone would not give all hereditary clauses.

**A6-F6 (filled: independent current).** Since \(C_0\le C_1\) and \(q_0=q_1=q\), `4.7:eq-running-couplings-2` gives \(r_i=\alpha_{0,i}\). The definition of \(c_T\) gives \(c_T\le1/8\). Hence
\[
a=\frac{h^3c_Tr_i}{8d}\le\frac{r_i}{64d}\le\alpha_{0,i}.
\]
Replace the true current by the independent \(\mathbf J\). Every configuration-only clause just obtained remains valid, with the same factorization and gauges. The sole remaining current inequality, the second inequality of CMP 109 (1.14), holds because \(\|\mathbf J\|_\infty<a\le\alpha_{0,i}\). Thus the whole independent-pair polydisc lies in \(U^{\Sigma^1}_i(X;\alpha_{0,i},\alpha_{1,i})\). Restrict (E) to it. This proves (c), with the source's exact \(a_i^{\mathfrak R},E_i^{\mathfrak R}\), both positive where required and independent of site, \(X,z\).

At \(i=k+1\) this is precisely the analytic-polydisc bound needed as \((H_{k+1})(d)\) for the large-field family, at its stand-in coupling. At earlier indices it reproduces the bounds previously supplied by the step of index \(i-1\). The small radius is deliberate: a sup bound without mesh powers need not control a plaquette divided by \(h^2\). The tensor construction needs a positive radius, not a radius uniform in \(i\).

**(b), coefficient bound.** Apply the preceding extraction to the newly established (E), with all its named premises and the same radii. It gives
\[
|\beta_{k+1}^{\mathfrak R}|\le C'g_k^{\kappa_0-7}
\le C'\gamma^{\kappa_0-7}\le C'\gamma^{\kappa_0-8}=\bar\varsigma.
\]
This calculation uses only the earlier coupling \(g_k\). Thus it is available before the new inverse coupling is defined. All three conclusions follow at the standing of the named inputs. \(\square\)


## A12 — Clause (0)

Source statement: CA-I:56419–56460. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{proposition}[Clause (0) concluded]\label{4.19:prop-clause-zero}
Assume (H1)--(H6) of Notation~\ref{2.2:not-hypotheses}. Let $(x_k)$, $x_k=g_k^{-2}$, be the running
inverse couplings of Definition~\ref{1.2:def-couplings}, started at $g_0\in(0,g_-(g)]$. Assume
further the following statements:
\begin{enumerate}
\item[(a)] Ba{\l}aban's one-step renormalization theorem, \cite[Theorem~3]{B-CMP109};
\item[(a$'$)] the widened form of condition \cite[(1.12)]{B-CMP109}, on cubes smaller than those
of that condition, and the statement that the step of the construction reproduces this widened
form;
\item[(b)] the finite part of the one-loop law, Lemma~\ref{4.2:lem-one-loop}, and the bounds on
the unmarked part of the increment, Lemma~\ref{4.2:lem-unmarked}, each stated with its proof
incomplete at the step marked $(\ast)$ there;
\item[(c)] the bound on the large-field part of the coupling increment;
\item[(d)] the independence of the localised terms from the small-field region,
Corollary~\ref{4.4:cor-localised-independence};
\item[(e)] the operator bounds at free current;
\item[(f)] the representation and bound of the large-field terms;
\item[(g)] the one-power hereditary class;
\item[(h)] the torus-independence of the terms localised in non-wrapping domains.
\end{enumerate}
Assume these jointly with the conclusion of Theorem~\ref{4.20:thm-representation}, the inductive
representation of the effective densities, at the scales already reached: for every $n\ge1$ with
$x_i\ge\gamma^{-2}$ for all $i<n$, that conclusion holds at every level $k<n$. Then
$K=K(g_0,g)$ of Definition~\ref{1.2:def-flow-constants} is a well-defined non-negative integer
satisfying
\begin{equation}\label{4.19:eq-clause-zero-1}
\frac{g_0^{-2}-g^{-2}}{B_\sharp}-1\;\le\;K\;\le\;
1+\frac{g_0^{-2}-g^{-2}-B_\sharp+c_5}{\lambda_\sharp}.
\end{equation}
Consequently $K\to\infty$ as $g_0\downarrow0$, and the set of realised cutoffs is unbounded.
Moreover:
\begin{itemize}
\item $g_k\in(0,g)\subset(0,\gamma_H]$ for every $k\le K$;
\item $g_K\in[g_-(g),g)$;
\item for $0\le i\le j\le K$,
\begin{equation}\label{4.19:eq-clause-zero-2}
\lambda_\sharp(j-i)-c_5\;\le\;x_i-x_j\;\le\;B_\sharp(j-i);
\end{equation}
\item the $K$ renormalization steps on $\mathbb{T}_m$ at lattice spacing $L^{-K}$ produce exactly
the couplings $g_0,\dots,g_K$.
\end{itemize}
\end{proposition}
```

### Inputs and proof

Proof locus: CA-I:56462–56524. The proof is the coupling part of the **joint induction on the level** with the effective-density representation. It is not an invocation of two globally completed theorems in a cycle.

### Every hypothesis (a)–(h), and the prefix representation

| Source item / local name | CA label and locus | Standing carried in this repository |
|---|---|---|
| P5-H-H1–H6 | `2.2:not-hypotheses`, CA-I:1126–1181 | Standing model and constant-choice conditions: pure Wilson SU(N), d=4; odd large L; ordered auxiliary parameters, then γ, then γ_H; \(\gamma_H\le(\gamma^{-2}+c_5+1)^{-1/2}\); \(0<g\le\gamma_H\); \(m\ge11+m'+\log_LR(g_-(g))\); \(0<g_0\le g_-(g)\). The present SU(2) lane imports no unproved SU(N>2) extension. The other one-sided floors and ceilings of H3 remain attached. |
| (a), P5-H-step | CA-I:56424; Balaban CMP 109 Theorem 3 | Published theorem cited as an input. Its actual one-step construction and stated hypotheses are carried, not rebuilt by this arithmetic. |
| (a′), P5-H-wide-gauge | CA-I:56425–56427; CMP 109 (1.12) | Widened smaller-cube condition and its reproduction by the step. [oc](../oc.md), `4.13:lem-own-constant`, CA-I:45203–45234, supplies the own-constant one-step proof, **being refereed**. Keep its inputs and exact scope; it is not a proof of every other hereditary clause. |
| (b1), P5-H-loop | `4.2:lem-one-loop`, CA-I:3901–4030; use 56361–56368 and 56428–56430 | Source status discrepancy preserved: its heading cites CMP 109 (1.22), Theorem 3 and CMP 116 (2.41); CA-I:3930–3945 says used as stated. Its determinant comparison and lattice coefficient are asserted at 3967–3988. A12 describes the lemma as proof incomplete at (*). This port neither resolves that discrepancy nor calls the interacting one-loop law proved here. Its finite sum bound remains a named cited/open input. P3's free-field algebra is not this law. |
| (b2), P5-H-unmarked | `4.2:lem-unmarked`, CA-I:4031–4075; bound `4.2:eq-unmarked-1` | Explicit “Stated; proof incomplete at the step marked (*)”. Earlier representation, actual one-step bound and CMP 116 (2.41) remainder estimate are its hypotheses. Still an open supplier here. |
| (c) | `4.7:prop-coupling-increment`, CA-I:32412–32496 | A6 port above, with every named hypothesis. The ceiling is \(\bar\varsigma=C'\gamma^{\kappa_0-8}\le\min\{c_0/4,1\}\). |
| (d) | `4.4:cor-localised-independence`, CA-I:9615–9791 | Port in p4. The needed `4.4:prop-local-real-base` is proved and refereed in lrb, on its inherited hypotheses. |
| (e) | `4.5:thm-operator-bounds`, CA-I:19578–19743 | Port in p4, with its full named frontier. `4.5:lem-uniform-increment` is completed and checked in ui. `4.14:thm-operator-theorem`, CA-I:46035–46156, is also ported in p4; no new stage-admission conclusion is inferred. |
| (f) | `4.6:prop-large-field-bound`, CA-I:22860–23036 | A5 above and checked p1 logarithm port, still conditional on activity, format, prepared sequence, positivity, common-domain, locality and real-slice inputs. |
| (g), P5-H-class | `4.8:def-one-power-class`, CA-I:33113 onward; `4.8:prop-class-reproduction`, 34241 onward; use 56436 | Hereditary class and its reproduction on the actual prescribed towers. Conditional, with restriction/membership, nesting and printed CMP 109 (1.17) inputs retained. mu supplies the minimizer/nesting result at its proved and refereed scope. It does not itself supply complex stage admission. |
| (h), P5-H-torus | `4.38:thm-torus-independence`, CA-I:58187–58411 | Conditional implication, not ported in this lane. Its seven hypotheses at 58188–58216 and level hypothesis at 58219–58275 remain attached: localised/interior independence; local walk and single-cell statements; walk and one-family covariance; operator bounds; A6; A5 with format, rounding, exterior-island and joined-domain extensions; local label and free-bond rules. The latter analytic extension is the printed input CMP 122a p.192 (1.70), CMP 122b p.377 (1.68)–(1.69). |
| P5-H-prefix-representation | `4.20:thm-representation`, statement CA-I:61095–61206; assumed at 56439–56441 | For every n with \(x_i\ge\gamma^{-2}\) for i<n, the whole inductive conclusion holds at k<n. This is an earlier-level input, not the new-level conclusion. The source assigns its proof to the following induction at 61208 onward. Its open representation/history/stage frontier remains attached. |
| P5-H-cell-comparison | CA-I:56516–56521, expanded at 57117–57135 | The two cell-multiplier bounds are **taken by statement** at 57122–57127. Keep \(\check R_K\le R(g_-(g))\) and \(\check R_i\le L^{K-i}\check R_K\) as named geometry inputs where required. The latter is not proved by monotonicity alone; CA-I:50674–50677 explicitly distinguishes that fact. |

Definitions: `1.2:def-couplings` (CA-I:606–629) fixes \(x_0=g_0^{-2}\), \(x_l=x_{l-1}-\beta_l\). `1.2:def-flow-constants` (631–684) fixes
\[
c_5=2c_2,\quad \lambda_\sharp=c_0/2-\bar\varsigma\ge c_0/4>0,
\quad B_\sharp=C_\beta+\bar\varsigma>0,
\quad g_-(g)=(g^{-2}+B_\sharp)^{-1/2}.
\]
Here \(c_0=11N^2\log L/(12\pi^2)\), as printed, and the existence of the actual coefficient with this one-loop normalization belongs to P5-H-loop. `4.2:def-increment` (3764–3866) identifies the coefficient of the complete regular part: Gaussian normalizer plus fluctuation logarithm with the inherited marked remainders. No Gaussian-only coefficient is substituted for it.

### Proof on the source route

**Step 1: construct the next coefficient from a prefix.** Fix \(n\ge1\) with \(x_i\ge\gamma^{-2}\) for all \(i<n\). The prefix representation supplies the regular input and the actual bounds at each earlier level. Hypotheses (a),(a′),(g) supply the one-step construction in its reproduced class. Hypotheses (d),(e) supply localised identification and the operator estimates used in that construction. A5 and A6 supply the large-field terms and their descendant kernels under their hypotheses. Their new-level bounds use \(g_{n-1}\), never an as-yet undefined \(g_n\).

The small-field family and its tensor are then read through `4.2:def-increment` and (h). In that theorem, \((H_n)(a)\)–(c+) concern only levels below n; (d) is the new-level analyticity and positive polydisc radius, supplied for the marked part by A6(c), with the regular part supplied by the small-field input. Consequently the complete coefficient \(\beta_n\) is defined, is real for the real inputs, and uses only \(g_0,\ldots,g_{n-1}\). Its independence of the torus is supplied by (h). These are exactly the source's formation inputs at CA-I:56463–56484. Their analytic supply is carried as a hypothesis, not proved by the scalar recursion.

**A12-F1 (filled: induction order).** At n=1 the earlier coefficient list is empty and the representation at level 0 is the assumed base case. At n>1 use already established bounds for indices below n. Only after forming and estimating \(\beta_n\) define \(x_n=x_{n-1}-\beta_n\). The simultaneous representation induction may then supply the next prefix. Thus the order is prefix representation → new families at stand-in radii → tensor/coefficient → new inverse coupling → next representation. A hypothesis about all earlier prefixes is a strong-induction hypothesis; it does not assert the new representation before its step.

**Step 2: establish the two-sided bound through n.** P5-H-loop gives, for every \(i\le j\le n\),
\[
\sum_{l=i+1}^j\beta_l^0
=\sum_{l=1}^j\beta_l^0-\sum_{l=1}^i\beta_l^0
\ge (jc_0-c_2)-(ic_0+c_2)=(j-i)c_0-c_5.
\]
P5-H-unmarked and the ordered ceiling \(\varepsilon_1^I\le c_0/(2C_{\rm rem})\) give
\(|\beta_l^{\mathfrak A}-\beta_l^0|\le c_0/2\), \(|\beta_l^{\mathfrak A}|\le C_\beta\).
A6 gives \(|\beta_l^{\mathfrak R}|\le\bar\varsigma\). Use the earlier estimates for l<n and the just-formed estimate for l=n. The source's `4.19:lem-flow-bounds`, checked in p1, applies. Explicitly,
\[
x_i-x_j=\sum_{l=i+1}^j\beta_l
\le(C_\beta+\bar\varsigma)(j-i)=B_\sharp(j-i),
\]
\[
x_i-x_j\ge(j-i)c_0-c_5-(j-i)(c_0/2+\bar\varsigma)
=\lambda_\sharp(j-i)-c_5.
\]
The empty sum at i=j gives \(-c_5\le0\le0\). No individual sign of \(\beta_l\) was used. These slopes are exactly the fixed ones; no later constant was substituted.

**Step 3: apply the first-passage arithmetic.** Put \(h=g^{-2}\), \(t=g_0^{-2}\), \(B=B_\sharp\), \(\lambda=\lambda_\sharp\). By H3,H4,
\[
h\ge\gamma_H^{-2}\ge\gamma^{-2}+c_5+1>\gamma^{-2}.
\]
By H6, \(t\ge h+B\). Whenever all previous entries exceed h+B, Step 1 supplies the next entry and Step 2 supplies the interval bounds through it. This is precisely `4.2:lem-first-passage`, CA-I:3636–3721, checked in p1.

**A12-F2 (filled: all endpoint cases).** Here is its use with no omitted stopping argument. If \(t=h+B\), K=0. Otherwise, if passage never occurred, recursive extension would give every n and
\(x_n\le t-\lambda n+c_5\). Choose an integer \(n>(t-h-B+c_5)/\lambda\); the Archimedean property supplies one. Then \(x_n<h+B\), a contradiction. Hence
\(K=\min\{k:x_k\le h+B\}\) is finite. For K>0, \(x_{K-1}>h+B\) and \(x_{K-1}-x_K\le B\), so \(x_K>h\). Every earlier entry exceeds h+B. For K=0, \(x_0=h+B>h\) since B>0. Thus all \(x_k>h>0\), and all \(g_k=x_k^{-1/2}\) exist for k≤K, lie in (0,g), and
\(g_K\in[(h+B)^{-1/2},g)=[g_-(g),g)\).

Since \(x_K\le h+B\) and \(t-x_K\le BK\),
\[
K\ge(t-h-B)/B=(t-h)/B-1.
\]
If K>0, apply the lower drift to K−1 and use \(x_{K-1}>h+B\):
\[
\lambda(K-1)-c_5\le t-x_{K-1}<t-h-B.
\]
This gives the stated weak upper bound
\(K\le1+(t-h-B+c_5)/\lambda\).
If K=0 its right side is \(1+c_5/\lambda\ge1\), so the same inequality holds. These are exactly `4.19:eq-clause-zero-1`. Step 2 at n=K gives the claimed interval bounds if K>0; the previously checked empty-sum case gives them if K=0. Since B is fixed independently of the bare coupling, the lower cutoff bound tends to infinity as \(g_0\downarrow0\). Thus realised cutoffs are unbounded; this does not assert that every integer cutoff is realised.

**Step 4: identify the run on the declared lattice.** This is the last source paragraph, CA-I:56513–56523. Use `4.38:def-admissible-sites`, CA-I:57027–57165. In level-i units a site (m,K′) has half-side \(L^{m+K'-i}\). Admissibility through j requires \(K'\ge j\) and
\[
L^{m+K'-i}\ge L^{11}M\check R_i\quad(0\le i\le j).
\]
Before forming the next cell size, the weaker set \(\mathcal S_j^\flat\) requires only the inequalities through j−1. Its half-side at level j is at least \(L^{10}M\check R_{j-1}\). This shows why the next coefficient can be read before the next cell multiplier is known.

**A12-F3 (filled: H5 at every scale).** By H5, \(L^m\ge L^{11}MR(g_-(g))\). The first cell comparison follows also directly from the definitions: \(\check x_K=\min_{i\le K}x_i\le x_K\le h+B=g_-(g)^{-2}\); taking the increasing logarithmic function and then its least dominating power of L gives \(\check R_K\le R(g_-(g))\). The second comparison, \(\check R_i\le L^{K-i}\check R_K\), remains the separately named cell-multiplier input taken by statement in the source, not a consequence of monotonicity. For each \(0\le i\le j\le K\),
\[
L^{m+K-i}\ge L^{11}ML^{K-i}R(g_-(g))
\ge L^{11}ML^{K-i}\check R_K\ge L^{11}M\check R_i.
\]
Thus (m,K) is admissible at every j≤K, with the exact power 11 unchanged. No claim that bare cube-fitting alone establishes the analytic hypotheses is made.

**A12-F4 (filled: equality of the two sequences).** Start the lattice construction with the same \(x_0=t\). Suppose its entries agree through j−1. The prefix-only rule and (h) give the same \(\beta_j\) on this admissible lattice as on the abstract run. Subtraction gives the same \(x_j\), and positivity gives the same \(g_j=x_j^{-1/2}\). Finite induction proves agreement through K. For K=0 there is no step to perform. Hence declaring the lattice after determining K is consistent. This proves the last clause, and completes the conditional proposition. \(\square\)


## A13.1 — Containment

Source statement: CA-I:56530–56547. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{proposition}[Containment: Ba{\l}aban's one coupling hypothesis holds along the flow]
\label{4.19:prop-containment}
Assume hypothesis (H4) of Notation~\ref{2.2:not-hypotheses}, clause (0) of Theorem~\ref{3.1:thm-main}
in the form of Proposition~\ref{4.19:prop-clause-zero}, and the terminal ceiling
$\gamma_H\le(\gamma^{-2}+c_5+1)^{-1/2}$ of hypothesis (H3) (see
Remark~\ref{2.3:rem-thresholds}). Then for all $k\le K$
\begin{equation}\label{4.19:eq-containment-1}
x_k>g^{-2}\ge\gamma_H^{-2}\ge\gamma^{-2}+c_5+1,
\end{equation}
so $0<g_k<\gamma$. In particular:
\begin{itemize}
\item every lower bound $x_k\ge x_*$ of the construction with $x_*\le\gamma^{-2}+c_5+1$ holds
at every level $k\le K$;
\item the one hypothesis of Ba{\l}aban's ultraviolet stability theorem
(\cite[Theorem~1]{B-CMP122b}), namely that all
effective couplings lie in $(0,\gamma]$, is satisfied.
\end{itemize}
\end{proposition}
```

### Inputs and proof

Proof locus: CA-I:56549–56566. Inputs are `4.19:prop-clause-zero` (A12 above, conditional), H4 of `2.2:not-hypotheses` (CA-I:1168), and the H3 terminal ceiling `2.2:eq-hypotheses-1` (1160–1162), reiterated in `2.3:rem-thresholds` (1721–1732). The stability theorem, **P5-H-stability = Balaban CMP 122b Theorem 1, pp.355–356**, remains a named cited theorem. Only its stated effective-coupling hypothesis is verified here; its conclusion is not reproved or granted status.

**Proof.** A12 gives \(0<g_k<g\) for every k≤K. For positive a<b, multiplying by the positive number \(a^{-2}b^{-2}\) shows \(b^{-2}<a^{-2}\); thus inverse squares reverse the inequality. Hence \(x_k=g_k^{-2}>g^{-2}\). H4 gives \(g^{-2}\ge\gamma_H^{-2}\). The terminal ceiling, with both sides positive, gives \(\gamma_H^{-2}\ge\gamma^{-2}+c_5+1\). Therefore
\[
x_k>g^{-2}\ge\gamma_H^{-2}\ge\gamma^{-2}+c_5+1>\gamma^{-2}.
\]
The last inequality uses \(c_5\ge0\). Taking inverse square roots gives \(0<g_k<\gamma\). For any construction floor \(x_*\le\gamma^{-2}+c_5+1\), the same chain gives \(x_k>x_*\), hence \(x_k\ge x_*\). It also places all effective couplings in \((0,\gamma]\), as needed by P5-H-stability. This proves every clause. \(\square\)

**A13-F1 (filled).** The proof uses A12's strict upper bound on every coupling, not stepwise monotonicity of the run. K=0 is included, since A12 gives \(g_0=g_-(g)<g\) in that case. No additional small-coupling theorem is invoked to prove containment.


## A13.2 — Fixed-depth windows

Source statement: CA-I:56568–56582. Source status: unmarked, declared proved as an implication.

### Exact source statement

```latex
\begin{corollary}[Coupling windows at fixed depth and subsequential limit couplings]
\label{4.19:cor-windows}
Assume clause~(0) of Theorem~\ref{3.1:thm-main} (Proposition~\ref{4.19:prop-clause-zero}). Let
$g_0^{(i)}\downarrow 0$ be a sequence of bare couplings, and put $K_i:=K(g_0^{(i)},g)$. Then, for
every $s\ge 0$ and every $i$ with $K_i\ge s$,
\begin{equation}\label{4.19:eq-windows-1}
x_{K_i-s}\in\bigl(g^{-2}+\max\{0,\lambda_\sharp s-c_5\},\ g^{-2}+B_\sharp(s+1)\bigr].
\end{equation}
Along a subsequence, $g_{K_i-s}\to g_{\infty,s}$ for every $s\ge 0$, where the limits
$g_{\infty,s}$ satisfy
\begin{equation}\label{4.19:eq-windows-2}
g_{\infty,s}^{-2}\in\bigl[g^{-2}+\max\{0,\lambda_\sharp s-c_5\},\ g^{-2}+B_\sharp(s+1)\bigr];
\end{equation}
in particular $g_{\infty,0}\in[g_-(g),g]$.
\end{corollary}
```

### Inputs and proof

Proof locus: CA-I:56584–56630. The sole research input is A12, with all its antecedents. \(c_5\ge0\), \(B_\sharp>0\), \(\lambda_\sharp>0\), and \(g_-(g)\) retain their definitions. There is no new Balaban input. The following hand proof supplies the compactness and diagonal details omitted in the source.

**A13-F2 (filled: depth and run indices).** Depth s is a non-negative **integer**, as required for \(K_i-s\) to be a level; the source's notation “s≥0” has this implicit meaning. Write \(x_k^{[i]}\) and \(g_k^{[i]}\) for the run starting at \(g_0^{(i)}\), to distinguish the run index from the level. The exact source statement suppresses these superscripts.

Fix s and a run with \(K_i\ge s\). The two-sided interval bound, with endpoints \(K_i-s,K_i\), gives
\[
\lambda_\sharp s-c_5\le x_{K_i-s}^{[i]}-x_{K_i}^{[i]}\le B_\sharp s.
\]
The terminal window gives \(g^{-2}<x_{K_i}^{[i]}\le g^{-2}+B_\sharp\). Add these inequalities:
\[
g^{-2}+\lambda_\sharp s-c_5<x_{K_i-s}^{[i]}
\le g^{-2}+B_\sharp(s+1).
\]
Also A12 gives \(x_{K_i-s}^{[i]}>g^{-2}\). Combining the two strict lower bounds gives exactly
\[
x_{K_i-s}^{[i]}\in
\bigl(g^{-2}+\max\{0,\lambda_\sharp s-c_5\},\ g^{-2}+B_\sharp(s+1)\bigr].
\]
This proves `4.19:eq-windows-1`, including s=0 and the case \(\lambda_\sharp s-c_5\le0\).

The lower bound on \(K_i\) tends to infinity as \(g_0^{(i)}\downarrow0\). Thus, for each fixed s, deleting finitely many runs makes all these entries defined. They lie in the closed bounded interval
\[
I_s=[g^{-2}+\max\{0,\lambda_\sharp s-c_5\},\ g^{-2}+B_\sharp(s+1)]\subset(0,\infty).
\]
Its left endpoint is at least \(g^{-2}>0\). It is nonempty because it contains the entries of the remaining runs.

**A13-F3 (filled: compactness without a black box).** For any sequence in a closed bounded interval [a,b], bisect the interval. At least one closed half contains infinitely many terms. Choose such a half, and repeat within it. The chosen closed intervals are nested and their lengths tend to zero. If \(a_n,b_n\) are their endpoints, completeness of the real numbers gives \(y=\sup_n a_n\); nesting implies \(a_n\le y\le b_n\) for every n. Choose one term in the nth interval with index larger than the preceding chosen index, possible because it contains infinitely many terms. Its distance from y is at most \((b-a)2^{-n}\), hence tends to zero. This gives a convergent subsequence with limit in [a,b]. This is a written existence argument, not machine enumeration.

Apply that argument to depth 0 to choose an increasing infinite index sequence \(J_0\). At depth s≥1, discard the finitely many indices of \(J_{s-1}\) with \(K_i<s\), and choose a further infinite subsequence \(J_s\) convergent at depth s. All earlier depths remain convergent, since every subsequence of a convergent sequence has the same limit: its tail eventually lies in any prescribed neighbourhood containing the parent tail.

**A13-F4 (filled: the common diagonal).** Enumerate each \(J_s\) increasingly, starting at position 1, and set \(i_n=J_n(n)\) for n≥1. Since \(J_{n+1}\) is a subsequence of \(J_n\),
\(J_{n+1}(n+1)\ge J_n(n+1)>J_n(n)\); thus \((i_n)\) is strictly increasing. For fixed s and n≥max{s,1}, \(i_n\in J_n\subset J_s\). Its increasing tail is therefore a subsequence of \(J_s\), so depth s converges on this one diagonal. Call its inverse-coupling limit \(y_s\). The closed-interval construction gives \(y_s\in I_s\).

For positive x,y,
\[
|x^{-1/2}-y^{-1/2}|=
\frac{|x-y|}{\sqrt{x}\sqrt{y}(\sqrt{x}+\sqrt{y})}.
\]
On \(I_s\) the denominator is at least \(2(g^{-2})^{3/2}>0\). Hence convergence of inverse couplings implies convergence of the couplings to \(g_{\infty,s}=y_s^{-1/2}>0\), and \(g_{\infty,s}^{-2}=y_s\in I_s\). This proves `4.19:eq-windows-2`. For s=0, \(c_5\ge0\) makes \(I_0=[g^{-2},g^{-2}+B_\sharp]\). Inverse square roots give
\(g_{\infty,0}\in[(g^{-2}+B_\sharp)^{-1/2},g]=[g_-(g),g]\). The endpoint g is permitted in the limit even though every finite terminal coupling is strictly smaller. \(\square\)

The corollary proves only simultaneous subsequential convergence at integer depths. It proves neither tuning to a prescribed cutoff, whole-sequence convergence, monotonicity of the increments, nor uniqueness of these limit couplings; compare `4.19:rem-not-asserted`, CA-I:56632–56647.


## Balaban hypotheses retained by name and locus

Every item below retains its original hypotheses. “Cited” and “printed” report the account's attribution. No original Balaban paper is independently verified by this port. The direct inputs above are used in the six implications. The joint-induction frontier below remains attached through the prefix representation and P4; listing it does not make every entry a new direct premise of A13's arithmetic.

### Direct formula and theorem inputs

| Hypothesis name | Balaban locus | CA-I use / standing |
|---|---|---|
| P5-B-step | CMP 109 Theorem 3, (1.22); CMP 116 (2.41) | 56424, 3901–3945; cited step and one-loop inputs, with the one-loop source-status discrepancy recorded above. |
| P5-B-decay | CMP 102b Proposition 9 (190) | 32241–32253; cited at background 1, exactly the A3 bound. |
| P5-B-derivative-extension | CMP 109 remark on the derivative of its nonlinear potential and its second-order operators | 32243–32245; no more precise CMP 109 locus is given there. Named hypothesis, not an invented theorem number. |
| P5-B-coefficient | CMP 109 (5.42), CMP 119 (3.62) | 32254–32268, 32364–32380; assumed second-moment implication. |
| P5-B-background-composition | CMP 109 (4.2) | 32302–32308; cited identification. |
| P5-B-first-variation | CMP 109 (4.14) | 32319–32322; cited stationarity. |
| P5-B-regularity | CMP 109 (1.10)–(1.16), (3.16), Lemma 4, (3.38) | 30188–30327, 32417–32424, 32483–32490; class definition, widened cube convention, and nesting/membership inputs. mu proves its stated minimizer/nesting result, not every use-radius application. |
| P5-B-family | CMP 116 (2.13); CMP 119 (2.27)–(2.29), (2.31), (3.44)–(3.47) | 30112–30186, 32445–32456; kernel definitions and standing analytic/covariant family bounds. |
| P5-B-cluster | CMP 116 Lemma 1 (1.34), and marked cluster estimate with \(K_{CE}=4b^{\rm adm}/\nu_{CL}\) | 32000–32028; supplied on the hereditary class. The pinned and unpinned estimates retain their common constant. |
| P5-B-island | CMP 122b (1.71), (1.73)–(1.75), (1.89) | 20615, 21314–21419; assumed island-operation and mass/phase bounds. The phase-smallness statement at 21382–21387 is a separate supplier, retained as **P5-H-phase**. |
| P5-B-interaction | CMP 122b (1.65), (1.68)–(1.69) | 21314–21419; analytic operation and strip-interaction bounds. |
| P5-B-enlarged-interaction | CMP 122b p.379 | 21394–21398; bound on the enlarged island with a different constant, explicitly printed without proof. |
| P5-B-large-field-comparison | CMP 122b (1.99), (1.100), p.390 | 22910–22917, 22939–22943, 23032–23035; the source bounds/locality to which A5 compares. The present conditional proof supplies its own stated strip-length version; these comparisons are not additional discharges. |
| P5-B-stage | CMP 122a (1.60)–(1.70) | `4.18:thm-preparatory-boundary`, 54985–55003, explicitly assumes the stage theorem and the profile-class extension. Retained behind the representation. |
| P5-B-stability | CMP 122b Theorem 1, pp.355–356 | 56543–56545, 56564–56565; cited theorem. A13 verifies its named coupling hypothesis only. |

### Printed-sentence frontier of the joint induction

These names preserve the distinct sentence bundles of `chain-ca.md` §6.1 and P4. They are **printed without proof, carried hypotheses** in CA's own input list, not proofs acquired by porting. The notation `P5-Pxx` is local to this file.

| Name | Balaban locus and content | CA-I locus |
|---|---|---|
| P5-P01 | 122a pp.178–179, prepared-data admission | 166579–166580 |
| P5-P02 | 119 p.276, transfer of 109 §3 and Lemmas 5–6 to the 119 cover | 166581–166583; 166638–166640 |
| P5-P03 | 99b p.396 (3.35),(3.37), lowest two tower regularity classes | 166584–166585; retained with P4's supplier-reconciliation qualification |
| P5-P04 | 122b p.379, interaction locality | 166586–166587; direct `4.6:rem-interaction-locality`, 20731–20755 |
| P5-P05 | 109 (1.17), complex-pair inclusion | 166588–166589; direct use 29558–29598 and 34067–34072 at every label |
| P5-P06 | 109 p.277 (3.26)–(3.28), extension of block-averaged curvature bounds to near data | 166590–166592 |
| P5-P07 | 99b §3 before (3.132), constrained-covariance inverse bounds and walks | 166593–166594 |
| P5-P08 | 99b §3 after Theorem 3.9, further operator walks | 166595–166596 |
| P5-P09 | 98 §E p.43, analytic averaging-derivative bounds | 166597–166598 |
| P5-P10 | 99b (3.49),(3.69), second far-current inequality | 166599–166600 |
| P5-P11 | 122b (1.90), bracket's polymer-gas representation | 166601–166602; p1 ports the conditional combinatorics, retaining locality and format |
| P5-P12 | 122b p.386, large-field bounds under remaining modifications | 166603–166604 |
| P5-P13 | 122a (1.64)–(1.69), pp.190–191, layerwise gauge clauses | 166605–166606 |
| P5-P14 | 122a p.192, layerwise small-coupling ceiling | 166607–166608 |
| P5-P15 | 122b p.375, old-term bounds beside a new region | 166609–166610; 166645–166646 |
| P5-P16 | 122a p.192 (1.70); 122b p.377 (1.68)–(1.69), joined-domain analytic extension and bounds | 166611–166613; direct torus hypothesis 58207–58212 |
| P5-P17 | 122b (1.11),(1.23)–(1.48), p.369, boundary absolute bounds and gauge invariance | 166641–166642 |
| P5-P18 | 122b p.367 (1.40)–(1.41), analytic solution of the large-field equation | 166643–166644 |
| P5-P19 | 122a p.191, generalizing spaces on components whose integrations stop | `4.14:rem-supply-scope`, 49531–49546; later-domain application obligation, not a consequence of the operator implication |

P5-B-enlarged-interaction is a further printed bound, separate from P5-P04's locality. The gauge cube choice C=1, or C∈{1,2} with 1 allowed, and actual-background admission at all levels remain application hypotheses of `4.14:rem-supply-scope`, CA-I:49495–49546. They are not supplied by labelling a domain analytic.

### Cited theorem frontier inherited through P4 and representation

Each semicolon-separated item names a **separate hypothesis** with its numbered locus. Prefix B means Balaban; suffix T, L, P, C or Eq means theorem, lemma, proposition, corollary or formula. Every entry has standing **cited, not reproved by P5**. CA-I:166565–166578 supplies the common (0)/(i) list; 166628–166637 supplies the additional representation list. The existing ports retain their own stated scope and exceptions.

| Names and original loci | CA-I list locus |
|---|---|
| B95-Eq1.118; B96-Eq2.36 (p.229) | 166565–166566 |
| B96-L2.1; B96-L2.4; B96-P2.6; B96-P2.7 | 166567 |
| B98-P1; B98-P2; B98-P3; B98-P4; B98-P5; B98-P6; B98-P7 | 166568 |
| B99a-L1; B99a-T2; B99a-T4; B99a-P6 (pp.98–99) | 166569–166570 |
| B99b-T3.1; B99b-T3.2; B99b-T3.3; B99b-T3.4; B99b-T3.7; B99b-T3.9; B99b-T3.10; B99b-T3.11; B99b-T3.12; B99b-T3.13; B99b-T3.14; B99b-T3.15; B99b-C3.5; B99b-C3.6; B99b-C3.8 | 166571–166572 |
| B102b-T1, (7)–(9), p.279; B102b-P3; B102b-P9 | 166573 |
| B109-T1; B109-T3; B109-L4; B109-L5; B109-L6 | 166574–166575 |
| B116-L1; B116-L2; B116-L3 | 166576 |
| B122a-P1 | 166577 |
| B122b-T1 (pp.355–356); B122b-P1 | 166578 |
| B99a-Eq1.19 (p.79); B109-Eq3.37–3.50 (each numbered formula retained); B119-T1; B119-T2; B119-C3 | 166630–166636 |

The constant-order use of B99b-T3.1 p.397 and B102b (162)–(163), p.304, is explicitly retained at CA-I:166706–166709. The stage theorem and all direct formula inputs named in the preceding table remain additional hypotheses; this theorem list does not subsume the printed sentences.

## Open inputs behind the prefix representation

The direct analytic gaps have already been named: P5-H-activity and its unwritten supplier; P5-H-positive; the near-membership statement; P5-H-moment and its summation convention; the cited decay/composition/first-variation inputs; P5-H-loop and P5-H-unmarked; the hereditary, torus and cell-comparison supply. The source's **inherited joint-induction frontier** below prevents the earlier-level representation from hiding its open work. It is a source-status inventory, not an independent audit or an assertion that all these leaves enter each local clause directly.

Repository standing for the following carried inputs is **unresolved in this port; no completion is invoked**, except for the four explicitly updated rows. This says what P5 assumes; it does not reclassify unrelated repository work. Source labels/loci are those in pinned `chain-ca.md` §3. The account's own declarations were read at CA-I:166615–166624 and 166650–166692. The label map is retained from chain-ca; the long downstream proofs are not reread here.

| Name | CA label | CA locus | Source standing recorded in chain-ca | Repository standing used by P5 |
|---|---|---|---|---|
| F01 | `2.4:prop-m-freeness` | I:2239 | incomplete, I:2239 | Carried unresolved input; no completion invoked here. |
| F02 | `4.2:lem-unmarked` | I:4031 | incomplete, I:4031 | Carried unresolved input; no completion invoked here. |
| F03 | `4.4:prop-local-real-base` | I:8110 | outstanding, I:8110 | lrb: proved and refereed, with its inherited inputs. |
| F04 | `4.5:lem-uniform-increment` | I:16019 | incomplete, I:16019 | ui: completed and checked, with its inherited inputs. |
| F05 | `4.12:prop-reblocking-inside` | I:44127 | incomplete, I:44128 | Carried unresolved input; no completion invoked here. |
| F06 | `4.12:prop-reblocking-outside` | I:45085 | outstanding, I:45085 | Carried unresolved input; no completion invoked here. |
| F07 | `4.13:lem-minimizer-unique` | I:45162 | outstanding, I:45163 | mu: proved and refereed, at its stated/use scope. |
| F08 | `4.13:lem-own-constant` | I:45203 | outstanding, I:45204 | oc: proof being refereed; inherited gauge inputs retained. |
| F09 | `4.21:prop-relative-machine` | I:61212 | outstanding, I:61325 | Carried unresolved input; no completion invoked here. |
| F10 | `4.22:not-live-region-geometry` | I:85575 | outstanding, I:85575 | Carried unresolved input; no completion invoked here. |
| F11 | `4.22:prop-stage-totals` | I:87328 | incomplete, I:87329 | Carried unresolved input; no completion invoked here. |
| F12 | `4.24:prop-norm-conversion` | I:106533 | outstanding, I:106533 | Carried unresolved input; no completion invoked here. |
| F13 | `4.24:prf-field-dependence` | I:106589 | incomplete, I:106589 | Carried unresolved input; no completion invoked here. |
| F14 | `4.24:prop-holonomy-bound` | I:107073 | outstanding, I:107073 | Carried unresolved input; no completion invoked here. |
| F15 | `4.25:lem-gaussian-pieces` | I:110806 | incomplete, I:110806 | Carried unresolved input; no completion invoked here. |
| F16 | `4.25:lem-piece-oscillation` | I:111188 | incomplete, I:111188 | Carried unresolved input; no completion invoked here. |
| F17 | `4.25:lem-non-deep-pieces` | I:114658 | incomplete, I:114658 | Carried unresolved input; no completion invoked here. |
| F18 | `4.25:prop-dissolution` | I:115062 | incomplete, I:115062 | Carried unresolved input; no completion invoked here. |
| F19 | `4.27:lem-t-step-layer` | I:131633 | incomplete, I:131633 | Carried unresolved input; no completion invoked here. |
| F20 | `4.27:lem-weights-heredity` | I:132878 | incomplete, I:132878 | Carried unresolved input; no completion invoked here. |
| F21 | `4.27:prf-stage-move-cubes` | I:134184 | incomplete, I:134184 | Carried unresolved input; no completion invoked here. |
| F22 | `4.27:prf-density-increase` | I:135143 | incomplete, I:135143 | Carried unresolved input; no completion invoked here. |
| F23 | `4.27:prf-unheld-raw-points` | I:135466 | incomplete, I:135467 | Carried unresolved input; no completion invoked here. |
| F24 | `4.27:prf-index-zero-margin` | I:136192 | incomplete, I:136192 | Carried unresolved input; no completion invoked here. |
| F25 | `4.27:prf-ambient-inclusion` | I:136490 | incomplete, I:136490 | Carried unresolved input; no completion invoked here. |
| F26 | `4.27:lem-real-minimiser` | I:136809 | incomplete, I:136809 | Carried unresolved input; no completion invoked here. |
| F27 | `4.27:thm-arrest-theorem` | I:137628 | incomplete, I:137628 | Carried unresolved input; no completion invoked here. |
| F28 | `4.27:prf-newborn-continuation` | I:138485 | incomplete, I:138486 | Carried unresolved input; no completion invoked here. |
| F29 | `4.27:prop-live-piece-bounds` | I:138933 | incomplete, I:138933 | Carried unresolved input; no completion invoked here. |
| F30 | `4.27:rem-raw-current-radius` | I:140297 | incomplete, I:140297 | Carried unresolved input; no completion invoked here. |
| F31 | `4.27:rem-index-zero-members` | I:140692 | incomplete, I:140692 | Carried unresolved input; no completion invoked here. |
| F32 | `4.28:lem-near-pair-sums` | I:145837 | incomplete, I:145837 | Carried unresolved input; no completion invoked here. |
| F33 | `4.30:lem-no-two-sided-point` | I:152408 | incomplete, I:152408 | Carried unresolved input; no completion invoked here. |
| F34 | `4.30:prop-cell-counting` | I:152723 | unwritten / incomplete, I:152724 | Carried unresolved input; no completion invoked here. |
| F35 | `4.32:prop-positivity-dichotomy` | I:156837 | outstanding, I:156837 | Carried unresolved input; no completion invoked here. |

The source list also uses descriptive names without a label at that use site. Retain these as separate named inputs: **P5-O-real-slots**, real-factor slot bounds inside admissible boxes (I:166619, incomplete); **P5-O-volume-counts**, **P5-O-two-data-bounds**, and **P5-O-kernel-difference**, the relative-machine hypotheses (166652–166657, outstanding); **P5-O-kept-functional** (166660–166661, outstanding); **P5-O-probe-summand** (166662, outstanding); **P5-O-foreign-operation** (166664, outstanding); **P5-O-covariance-decay** (166665, outstanding); **P5-O-one-point-current** (166675, incomplete); **P5-O-core-freezing** (166686, incomplete). Their use-site loci, not invented theorem numbers, identify them here. Downstream named instances remain as in chain-ca. The final SU(N≥3) stability item (166690–166692) is not used for this SU(2) port.

## Source navigation and recovery

The checkout was `c86830eb5a7d96960a21636d6f8168d434783ead`. The first write created this file with its title and Provenance line. The task's GOAL method, FINISH sections, chain-ca §7.2 and ca-full README governed the port. `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent at this pinned checkout; no replacement workflow was fabricated.

Navigation used `sa-index/README.md`, the relevant rows and neighbouring rows of chunks 13, 17 and 19, `obligations.md`, and `ca-4.12-4.19/README.md` and chunk 11. The ca-full index supplied label locations, whose target statements were then read in CA-I. The bounded outline comparison used SA:14659–14685 (local logarithm), 19410–19448 (class/step order), 20181–20226 (Hessian extraction), and 20719–20821 (formation, first passage and depth windows). These outline passages do not replace the complete-account proofs.

| Source | SHA-256 of bytes read |
|---|---|
| `/tmp/sa_ym4.tex`, 32,992 lines | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `/tmp/sa_ca_I.tex`, 166,711 lines | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |

These agree with the pinned identities in chain-ca. Only missing files were eligible for the requested raw-URL fetches. Source reading used bounded ranges. Hashing, exact-statement comparison and file bookkeeping are not proof steps.

The full written section drafts were saved while working in `/tmp/p5-a5.txt`, `/tmp/p5-beta.txt`, `/tmp/p5-increment.txt`, `/tmp/p5-clause.txt`, `/tmp/p5-containment.txt`, and `/tmp/p5-windows.txt`. This repository file supersedes those scratch drafts after locus corrections. Recovery should start here. No alternative derivation was substituted. The next decision is an independent reading of this port; upstream completion work must address the actual named supplier, not rerun the arithmetic to suggest closure. In particular, resolve the activity placeholder, the exact second-moment convention, the near-membership supplier, the unmarked and one-loop inputs, and the retained representation/domain inputs at their own loci. Do not infer their closure from the checked standing of p1, mu, lrb or ui.

## Result

**Statements ported, all conditional research implications:**

| Row | Exact CA label | Statement | Proof |
|---|---|---|---|
| A5 | `4.6:prop-large-field-bound` | CA-I:22860–22908 | CA-I:22920–23036 |
| A6 | `4.7:prop-beta-extraction` | CA-I:32226–32289 | CA-I:32291–32410 |
| A6 | `4.7:prop-coupling-increment` | CA-I:32412–32458 | CA-I:32460–32496 |
| A12 | `4.19:prop-clause-zero` | CA-I:56419–56460 | CA-I:56462–56524 |
| A13 | `4.19:prop-containment` | CA-I:56530–56547 | CA-I:56549–56566 |
| A13 | `4.19:cor-windows` | CA-I:56568–56582 | CA-I:56584–56630 |

**Every marked filled step:** A5-F1, infimum version of the tree-length bound; A5-F2, subtracting the centre after union filing and exponentiation; A5-F3, analytic interpolation integrals, restriction, local uniform limits and locality. A6-F1, interior bidiscs, the two-variable Cauchy formula and repeated-direction case; A6-F2, the exact radius loss; A6-F3, the final ordered ceiling; A6-F4, previous-level versus new-level extraction order; A6-F5, the reference-index choice and mesh-difference bound with exactly 8d; A6-F6, replacing the true current by the independent current within its stated radius. A12-F1, strong-induction order; A12-F2, finite passage, K=0, strict terminal endpoint and both cutoff bounds; A12-F3, the H5 inequality at each scale, retaining the second cell comparison; A12-F4, induction identifying the abstract and lattice runs. A13-F1, containment including K=0 without stepwise monotonicity; A13-F2, integer depth and distinct run indices; A13-F3, interval subsequence extraction by a written completeness argument; A13-F4, the common increasing diagonal and continuous inverse-square-root passage.

**Correction:** A6-C1 replaces the erroneous Γ4(f) citation for the logarithmic floor by the actual standing floor, with the detached-statement qualification written explicitly. The route, constants, exponents, strip lengths, polydisc radius and displayed conclusions are preserved. The one-loop source-status discrepancy and the unspecified/unrooted reading of (A4)'s sum are recorded as unresolved input issues, not silently repaired theorems.

**Named hypotheses carried:** every row of the A5, A6 and A12 input tables; in particular the complete A12 list (a),(a′),(b)–(h), the earlier-level representation, H1–H6, and the cell comparison. The Cauchy proof retains (A1)–(A4), composition and vanishing first variation. The coupling application explicitly carries that whole extraction package, including (A4). The common-domain, real-slice, activity, locality, format, prepared-sequence and positivity inputs of A5 remain attached. All direct Balaban inputs, the P5-P01–P5-P19 printed bundles, the named cited-theorem frontier and the inherited open representation frontier remain hypotheses at their recorded loci and standing. The available inputs are credited at their current standing: p1 checked; p3 and p4 ports; mu and lrb proved and refereed; ui completed and checked; oc being refereed.

This is a port of the account's deductions, with filled steps and the marked reference correction. It does not prove the open antecedents or T0 and grants no scientific status. Credit belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and to Balaban at the cited loci. Codex wrote this port by hand. No numerical calculation, search, enumeration, solver or other computer-assisted proof was used. Only `library/port/p5-induction.md` changed; no editable prompt, ledger, audit file or platform instruction changed. **This text is not yet checked by another model.**
