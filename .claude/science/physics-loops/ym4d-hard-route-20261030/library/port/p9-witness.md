# P9 — Witness and volume transfer

Provenance: Research port at repository commit 63e903d537a80091af4ec001b307462954adb53d of Ethan Sussman and Levent Alpoge’s complete account (with Claude and Codex as authors of their text), upstream revision 31a47c543775; Balaban is credited wherever invoked. Port by Codex (GPT-6 family; effort setting not exposed), 2026-11-05. This working text grants no scientific or audit status and has not been independently checked.

## Reading contract

This is a hand-written conditional proof port, not an audit. Source text is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban supplies the published inputs identified below. No computation discharges a mathematical step. Shell/Python operations here only retrieve, locate, hash, and copy text.

The checkout is pinned at `63e903d537a80091af4ec001b307462954adb53d`. The requested `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this checkout. GOAL, FINISH, chain-ca §§2.3, 6, 7.2, port-map, and the supplied local instructions govern this narrow task. Only this output file is edited.

The existing `/tmp/sa_ym4.tex` and `/tmp/sa_ca_{I,II,III}.tex` were reused, not fetched again. Their SHA-256 identities match chain-ca:

| Source | SHA-256 |
|---|---|
| Outline | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| CA-III | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The pinned source URL is `https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/`, followed by `YM4_sketch_500.tex` or `theorem_0_complete_account_raw_II.tex` (and I/III). Source line references below use those files, abbreviated II/I/III. Their remote identity was not re-fetched in this session.

The outline index was consulted first: chunk-24's neighbouring rows for 25974–26091 and its obligations at 25976, 26184, 26832–26846 and 27079–27083. Source excerpts at 25974–25988, 26002–26012, 26054–26062, 26073–26091 show the reference-torus/transfer route. The outline's stronger asymptotics are not replacements for CA's precise hypotheses. CA-I:27–46 defines an unqualified heading as a proof in full, possibly conditional on named statements.

This round ports the C9, C10 and C11 conditional deductions and their transfer assembly. C5 is the next unported statement; see Result for the exact stopping point. The verbatim statement blocks below preserve their labels, constants, hypotheses and non-assertions. LaTeX references inside them retain CA's labels; they are not claims that the referenced inputs have been proved here. Proofs and filled steps follow separately.

## C9 — Torus witness: exact source statement

`8.18:thm-torus-witness`, CA-II:144922–145029. Source standing: unqualified heading, hence a proved implication under the account’s convention. Its antecedents retain their own standing.

```latex
\begin{theorem}[The two-point witness on every torus]\label{8.18:thm-torus-witness}
Let $N$, $L$, $\mathfrak{p}$ be as in clause (iv) of Theorem~0 (Theorem~\ref{3.1:thm-main}). The test
class $\mathfrak{T}(\mathsf{d};\vartheta)$, the numbers $b_0$, $s(\mathsf{d})$, $s_W(g)$, $r(s)$,
$k_W$, $C_W$, $c_{\mathcal{K}}$, $C_{\mathcal{K}}$, the kernel $\mathcal{K}_s$ and the running
shift $\zeta'$ are those of clause (iv) of Theorem~\ref{3.1:thm-main}, unchanged. The volume horizon
$m_V(g)$ and the volume-reading depth floor $s_{\mathrm{vol}}(g,m)$ are those of
Definition~\ref{8.18:def-volume-horizon}, and $\gamma_W^{\mathbb{T}}\le\gamma_W$ is the threshold
fixed in \eqref{8.18:eq-witness-below-horizon-a}. None of $\gamma_W^{\mathbb{T}}$, $C_W$, $k_W$,
$c_{\mathcal{K}}$, $C_{\mathcal{K}}$ depends on $K$, on $g_0$, on the position of the supports of
the test functions, or on $m$.

Assume the hypotheses of Lemma~\ref{8.18:lem-horizon-cases},
Proposition~\ref{8.18:prop-witness-below-horizon} and
Proposition~\ref{8.18:prop-witness-beyond-horizon}, as listed there, together with clause (0) of
Theorem~0, reflection positivity of the lattice measure and the continuum kernel. For the
consequences in part~(d) below, assume in addition clause (ii-$\mathbb{T}$) of Theorem~0.

Consider the following one-sided conditions on $g$, $m$, $\mathsf{d}$ and $K$:
\begin{align}
&g\le\gamma_W^{\mathbb{T}},\label{8.18:eq-torus-witness-1}\\
&\max\{s_W(g),\,s_{\mathrm{vol}}(g,m)\}\le s(\mathsf{d}),\label{8.18:eq-torus-witness-a}\\
&K-s(\mathsf{d})\ge k_W,\label{8.18:eq-torus-witness-2}\\
&m\ge m_{\mathbb{T}}(g_-(g)).\label{8.18:eq-torus-witness-3}
\end{align}
Since $s(\mathsf{d})$ is non-increasing in $\mathsf{d}$, condition \eqref{8.18:eq-torus-witness-a}
is equivalent to
\begin{equation*}
\mathsf{d}\le\mathsf{d}_W^{\mathbb{T}}(g,m):=
\sup\bigl\{\mathsf{d}:\ \max\{s_W(g),\,s_{\mathrm{vol}}(g,m)\}\le s(\mathsf{d})\bigr\}.
\end{equation*}
Since $s_{\mathrm{vol}}(g,m)=0$ for $m\le m_V(g)$ by \eqref{8.18:eq-volume-horizon-d}, on those tori
condition \eqref{8.18:eq-torus-witness-a} coincides with the depth
condition $s_W(g)\le s(\mathsf{d})$ of clause (iv). Condition \eqref{8.18:eq-torus-witness-3} is the
torus clause of hypothesis (H5) (Notation~\ref{2.2:not-hypotheses}), verbatim; nothing more is
required of $m$.

Let $g$ satisfy \eqref{8.18:eq-torus-witness-1}, let $g_0\in\,]0,g_-(g)]$ and $K=K(g_0,g)$, let $m$
satisfy \eqref{8.18:eq-torus-witness-3}, let $\mathsf{d}$ satisfy \eqref{8.18:eq-torus-witness-a}
and \eqref{8.18:eq-torus-witness-2}, put $s:=s(\mathsf{d})$, and let
$(f_1,f_2)\in\mathfrak{T}(\mathsf{d};\vartheta)$. Then the following hold.
\begin{itemize}
\item[(a)] On the torus $\mathbb{T}_m$,
\begin{equation}\label{8.18:eq-torus-witness-4}
S^T_{2;K}(f_1,f_2)=(\zeta'_{K-s})^2\,b_0\,g_{K-s}^4\,\mathcal{K}_s(f_1,f_2)\,
\bigl(1+R_K(f_1,f_2)\bigr),
\end{equation}
where
\begin{equation}\label{8.18:eq-torus-witness-5}
|R_K(f_1,f_2)|\le\tfrac12\ \bigl(\text{indeed }\le\tfrac14\bigr),\qquad
\zeta'_{K-s}\in\bigl[\tfrac23,\tfrac43\bigr],
\end{equation}
and
\begin{equation}\label{8.18:eq-torus-witness-6}
c_{\mathcal{K}}\|f_1\|_\infty\|f_2\|_\infty\le\mathcal{K}_s(f_1,f_2)
\le C_{\mathcal{K}}\|f_1\|_\infty\|f_2\|_\infty .
\end{equation}
\item[(b)] Consequently
\begin{equation}\label{8.18:eq-torus-witness-7}
\tfrac29\,b_0\,g_{K-s}^4\,\mathcal{K}_s(f_1,f_2)\le S^T_{2;K}(f_1,f_2)
\le\tfrac83\,b_0\,g_{K-s}^4\,\mathcal{K}_s(f_1,f_2),
\end{equation}
and, by clause (0) of Theorem~0,
\begin{equation}\label{8.18:eq-torus-witness-8}
\begin{split}
\tfrac29\,b_0\,c_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty
\bigl(g^{-2}+B^{\sharp}(s+1)\bigr)^{-2}
&\le S^T_{2;K}(f_1,f_2)\\
&\le\tfrac83\,b_0\,C_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty
\bigl(g^{-2}+\lambda^{\sharp}s-c_5\bigr)^{-2}.
\end{split}
\end{equation}
\item[(c)] These statements hold uniformly in $K$, $g_0$ and the position of the supports, on every
torus $\mathbb{T}_m$ with $m\ge m_{\mathbb{T}}(g_-(g))$. They hold uniformly also in $m$ on
$\{m_{\mathbb{T}}(g_-(g))\le m\le m_V(g)\}$. For $m>m_V(g)$ the volume enters through
$s_{\mathrm{vol}}(g,m)$ and through nothing else.
\item[(d)] For every torus limit of clause (ii-$\mathbb{T}$-a), (ii-$\mathbb{T}$-b) of Theorem~0, on
every torus of the family:
\begin{itemize}
\item the smeared curvature has strictly positive variance;
\item the limit is not scale invariant under any assignment of a dimension to the curvature;
\item it is reproduced by no free Maxwell field at any charge;
\item the coupling read off the two-point function at separation $\mathsf{d}$ is positive and tends
to $0$ logarithmically as $\mathsf{d}\downarrow0$, at the two-sided rate of
\eqref{8.18:eq-torus-witness-8}.
\end{itemize}
Each of these is a statement at fixed $m$, either at one small $\mathsf{d}$ or as
$\mathsf{d}\downarrow0$.
\end{itemize}

Not asserted: anything about the limits on $\mathbb{R}^4$ of clause (ii-$\mathbb{R}^4$) of
Theorem~0. In particular, it is not asserted that the curvature Hilbert space
$\mathcal{H}^{\mathrm{curv}}$ of those limits has dimension at least two; the bounds above at fixed
$\mathsf{d}$ uniformly in $m$ beyond $m_V(g)$ are not asserted. It
is further not asserted that $\inf_m\mathsf{d}_W^{\mathbb{T}}(g,m)>0$, nor that the floor
$s_{\mathrm{vol}}$ is necessary. Nor is anything asserted that clause (iv) of
Theorem~\ref{3.1:thm-main} lists as not asserted, in particular:
\begin{itemize}
\item that the limit fails to be Gaussian;
\item $O(4)$ invariance;
\item a mass gap;
\item anything for block observables, Wilson loops, or the object denoted $\mathfrak{A}$ in
clause (iv) of Theorem~\ref{3.1:thm-main};
\item anything for one source, for overlapping or signed sources, for separations larger than
$6\mathsf{d}$, or as $\vartheta\to0$;
\item that $\zeta'_{K-s}\to1$, beyond the bound on it in \eqref{8.18:eq-torus-witness-5};
\item the case $N\ge3$.
\end{itemize}
\end{theorem}
```

## C10 — Volume transfer: exact source statement

`8.22:thm-volume-transfer`, CA-II:141540–141583. Source standing: unqualified heading, hence a proved implication under the account’s convention. Its antecedents retain their own standing.

```latex
\begin{theorem}[The volume-transfer bound for connected functions]\label{8.22:thm-volume-transfer}
Work in the setting of Notation~\ref{8.22:not-partition-sources-cells}. In particular $\varrho>0$
is fixed and $\mathfrak{r}\in\{1,2\}$ is fixed there:
$\mathfrak{r}=1$ when \textup{(T1)}--\textup{(T2)} are applied to the complex periodised weight
itself, and $\mathfrak{r}=2$ when they are applied to the real system of four functions formed
from it; $R>0$ is a radius, $\ell$ is the cell side of the per-ball volume-free bound for two
sources of radius $R$, $C_{\mathrm{face}}(R)$ is the face constant of that bound,
$\mathsf{B}=E_+^{\sharp}+C_{\mathrm{low}}$, and
\begin{equation*}
m_{\star}(g)=\max\{m_{\mathbb{T}}(g_-(g)),\,\log_L\ell\}.
\end{equation*}
Assume the following statements:
\begin{itemize}
\item[(a)] reflection positivity of the lattice measure;
\item[(b)] the chessboard lemma, the placement lemma, the periodised-weight lemma, the face
lemma and the Schwarz--Cauchy lemma that accompany the per-ball volume-free bound;
\item[(c)] parts (i) and (ii) of the per-ball volume-free bound, together with its identity
expressing the real part of its counterterm $\mathcal{E}''$ as the cell average of the real part
of the bulk part of the sourced vacuum-energy functional of $\mathbb{T}_{m'}$ at the periodised
weight, plus the real part of the face part of the counterterm;
\item[(d)] properties \textup{(T1)}--\textup{(T5)} of the correlation theorem on
$\mathbb{T}_{m'}$, and its lower stability bound at zero source on $\mathbb{T}_m$ and on
$\mathbb{T}_{m'}$;
\item[(e)] Lemma~\ref{8.22:lem-trace-subadditivity};
\item[(f)] Lemma~\ref{8.22:lem-vacuum-energy-density}.
\end{itemize}
Let $g\le\gamma_J$, $g_0\in\,]0,g_-(g)]$, $K=K(g_0,g)$ and $m\ge m'\ge m_{\star}(g)$; here $m'$
is a second torus exponent, not the exponent $m'$ of $M=L^{m'}$. Let $F_1$
and $F_2$ be real Lipschitz functions on $\mathbb{R}^4$ supported in one ball of radius $R$,
transported to $\mathbb{T}_m$ and to $\mathbb{T}_{m'}$.
No condition is imposed on the signs of $F_1,F_2$, on the number of components of their
supports, or on the overlap or distance of the supports. Then
\begin{equation}\label{8.22:eq-volume-transfer-b}
\begin{gathered}
\bigl|S^T_{2;K,m}(F_1,F_2)-S^T_{2;K,m'}(F_1,F_2)\bigr|
\le C_{\mathrm{VT}}\,\|F_1\|_{\sharp}\|F_2\|_{\sharp},\\
C_{\mathrm{VT}}:=2\log 2\cdot(2Q_{\star}+2)^2\Bigl(\frac{2\mathfrak{r}}{\varrho}\Bigr)^2,
\qquad
Q_{\star}:=\exp\bigl[(\mathsf{B}+\bar{\delta}_{\mathrm{vac}})\ell^4+4C_{\mathrm{face}}(R)\bigr].
\end{gathered}
\end{equation}
The constant $C_{\mathrm{VT}}$ depends only on $(L,\mathfrak{p},g,\varrho;R)$. It does not depend
on $K$, $g_0$, $m$ or $m'$, on the position of the ball, or on the supports of $F_1,F_2$.
\end{theorem}
```

## C11 — Two-point witness: exact source statement

`8.1:thm-two-point-witness`, CA-II:71279–71367. Source standing: unqualified heading, hence a proved implication under the account’s convention. Its antecedents retain their own standing.

```latex
\begin{theorem}[The two-point witness theorem]\label{8.1:thm-two-point-witness}
The gauge group is $\mathrm{SU}(2)$; the formulas
below are written for $\mathrm{SU}(N)$. Work in the quantifier prefix of Theorem~\ref{3.1:thm-main}
(Notation~\ref{2.1:not-prefix}), inside the regime of the correlation theorem, that is, for parameter
values at which that theorem holds, with the coupling threshold $\gamma_J$ that it provides for
those values; the reference coupling is restricted below to $g\le\gamma_W\le\gamma_J$. Fix a
shape constant $\vartheta\in(0,1]$.

Assume that the following statements hold:
\begin{enumerate}
\item[(1)] the correlation theorem, applied below at depth $s=s(\mathsf{d})$ below the cutoff;
\item[(2)] the Gaussian extraction, in each of its three parts;
\item[(3)] the large-field block bound, healed part, for healed regions (those whose large-field
factor has been absorbed back into the small-field format by a later step), and, for regions still
carrying their large-field factor at the level read, the following statements: the corollary on
rarity of young large-field blocks, for young regions; the healed old-region bound, for old regions
healed at a later step; the proposition on never-healed old regions, which bounds at each age the
weight of the old regions not healed by the last lattice of the run, for those regions; and the
additive theorem, which bounds the weight of the event that such regions meet the neighbourhoods of
both supports of Definition~\ref{8.1:def-witness-class} by the smaller of the cell counts of the
two neighbourhoods times the one-cell weight of such regions, so that this weight enters linearly,
adds to this the series over their ages, and so combines the preceding bounds into the bound on the
contribution of such regions used in the proof. Here the \emph{age} at level $k$ of a large-field
region created at step $j$ is $k-j$, the number of steps since the step that created it, and a
region is \emph{young} if its age is at most the level count $\mathfrak{l}$ of the source lemma and
\emph{old} if its age exceeds it;
\item[(4)] the source lemma;
\item[(5)] the continuum kernel;
\item[(6)] the further inputs:
\begin{itemize}
\item clauses (0) and (ii-a) of Theorem~\ref{3.1:thm-main};
\item the envelope \eqref{8.1:eq-coupling-envelope-f} of the running inverse coupling;
\item the operator theorem at free current;
\item the estimate, together with its linearised form, on which, with the operator theorem at
free current, the upper bound in Lemma~\ref{8.1:lem-kernel-bounds} rests;
\item the statement from which the lower bound in Lemma~\ref{8.1:lem-kernel-bounds} is derived,
in the form used in this chapter;
\item the positivity dichotomy of the large-field operations, on which the union bounds over
single cells in the proof rest;
\item the remaining statements of the setting of Theorem~\ref{3.1:thm-main} that the proof uses;
\item the hypotheses of Lemma~\ref{8.1:lem-kernel-bounds} and of
Lemma~\ref{8.1:lem-running-normalisation}.
\end{itemize}
\end{enumerate}

Then there exist constants $C_0$, $r_0$, $C_D$, $k_W$ and $\gamma_W\le\gamma_J$ depending only on
$L$, $M$, $M_1$, the auxiliary parameters $\mathfrak{p}$ (among them $\kappa$), $N$, $\vartheta$,
and the constants of the statements assumed in (1)--(6), among them $\kappa_0$, $E_0$, $B_0$,
$B_3$, $\alpha_0$ and $r$, with the following property; $C_0$, $r_0$, $C_D$ and $k_W$ are the
constants of Definition~\ref{8.1:def-coupling-envelope}, where $C_0$ enters the room function
$C_W(s)$, $r_0$ is the constant depth offset of the witness construction and $k_W$ is the level
floor in the conditions below, and their values are fixed in the proof. Let:
\begin{itemize}
\item $g\in(0,\gamma_W]$;
\item $m$ be any torus exponent admitted by the torus clause of Theorem~\ref{3.1:thm-main},
with no further
condition;
\item $g_0\in(0,g_-(g)]$, and $K=K(g_0,g)$ the first passage;
\item $\mathsf{d}$ satisfy the one-sided conditions $s(\mathsf{d})\ge s_W(g)$ and
$K-s(\mathsf{d})\ge k_W$ and, when $m>m_V(g)$, the one-sided per-torus depth floor
$s(\mathsf{d})\ge s_{\mathrm{vol}}(g,m)$ of Definition~\ref{8.18:def-volume-horizon};
\item $(f_1,f_2)$ be any witness pair in
$\mathfrak{F}^{+}(\mathsf{d},\vartheta)\times\mathfrak{F}^{+}(\mathsf{d},\vartheta)$, in the sense of
Definition~\ref{8.1:def-witness-class}.
\end{itemize}
Here $s_W(g)$ is the $g$-dependent depth floor of Definition~\ref{8.1:def-coupling-envelope}, and
the first two conditions on $\mathsf{d}$ are those displayed in \eqref{8.1:eq-coupling-envelope-d};
$m_V(g)$ denotes the threshold on the torus exponent up to which the per-torus depth floor is not
needed. Write $s:=s(\mathsf{d})$. Then
\begin{equation}\label{8.1:eq-two-point-witness-1}
S^T_{2;K,m}(f_1,f_2)=N_{K-s}^{2}\, b_0\, g_{K-s}^{4}\,
\mathcal{K}_{K,s}(f_1,f_2)\,\bigl(1+R_K\bigr),
\end{equation}
with
\begin{equation}\label{8.1:eq-two-point-witness-2}
|R_K|\le\tfrac12,\qquad\text{indeed}\qquad |R_K|\le\tfrac14 .
\end{equation}
Here $b_0=(N^2-1)/2$, and $\mathcal{K}_{K,s}$ is the two-point kernel of
Definition~\ref{8.1:def-background-kernel}. The normalisation
$N_{K-s}$ of Lemma~\ref{8.1:lem-running-normalisation} (see
\eqref{8.1:eq-running-normalisation-a}) satisfies
\begin{equation}\label{8.1:eq-two-point-witness-3}
N_{K-s}\in\bigl[\,1-\mathfrak{d}_W(\underline{x}_s),\,1+\mathfrak{d}_W(\underline{x}_s)\,\bigr]
\subset\bigl[\tfrac23,\tfrac43\bigr],
\end{equation}
where $\underline{x}_s$ is the lower envelope of Definition~\ref{8.1:def-coupling-envelope}.
The constants $C_0$, $r_0$, $C_D$, $k_W$, $\gamma_W$ are independent of $K$, $m$, the parameter
$N_T$ of the correlation theorem, $g_0$ and of the position of the supports of $f_1$ and $f_2$.
\end{theorem}
```

## Named inputs and their standing

The owner supplies the current standing of [P1](p1-base.md), [P3](p3-free.md) (C1, checked), [P4](p4-operator.md), [P5](p5-induction.md), [P7](p7-torus.md) (checked), and [P6](p6-correlation.md) (ported). P1/P4/P5 are cited as available ports; this note grants no additional check. [lsc](../lsc.md), [mu](../mu.md), [lrb](../lrb.md), [oc](../oc.md), [ui](../ui.md), and [pda](../pda.md) are **refereed**, as specified by the owner. Their older provenance sentences do not override that supplied standing. Their hypotheses and exact scope remain attached. P3 does not supply the unwritten continuum-kernel input. P7 supplies the torus-independence implication, not an unconditional vacuum-density theorem. No claim is made that P5 covers every induction statement: its scope is A5, A6, A12, A13.

The following are hypotheses of this port, individually named, even where CA declares a conditional implication proved. A row preserves the whole source statement, including its domain, constants and further antecedents. An input used below is not discharged by being listed here.

| Hypothesis | Label and source | Standing retained |
|---|---|---|
| H-C2 | `8.4:thm-minimiser-analyticity`, II:85845–85846 | Cited Balaban CMP 102b Theorem 1, Proposition 9, (190); no reproduced proof here. |
| H-C3a | `8.4:prop-small-piece`, II:88192–88193 | Heading explicitly incomplete. |
| H-C3b | `8.5:def-representation-identity`, II:90196–90197 | Heading explicitly outstanding; shifted frozen-run equality is not supplied by analyticity alone. |
| H-C4a | `8.5:lem-radius-tails`, II:90729; qualification II:90834–90843 | Proved implication, with incomplete transfer of 109 (0.29) to its fine-field domain and incomplete profile locality. Part (b) also assumes its remainder-rate hypothesis (iv). |
| H-C4b | `8.5:thm-room-lemma`, II:93196 | Explicitly incomplete. |
| H-C4c | `8.5:prop-remainder-covariance`, II:94225–94261 | Conditional proof; (b) source-carrying unextracted terms have remainder kind, (c) running-coupling comparison, (d) profile locality remain incomplete as declared there. Balaban 119 (2.31), with the specified exponent identification, is another hypothesis. |
| H-C6a | `8.6:lem-prefactor-monotone`, II:102730 | Explicitly incomplete. |
| H-C6b | `8.6:lem-healed-islands-unread`, II:103387 | Explicitly incomplete. |
| H-C6c | `8.6:lem-annealed-removal`, II:104598–104626 | Proved implication from removal domination and H-C6b's two distinct clauses; the final list II:145599 calls it incomplete. Neither description closes H-C6b. |
| H-C7a | `8.7:lem-translation-covariance`, II:107738 | Explicitly incomplete for label histories; bare lattice translation invariance is a different assertion. |
| H-C7b | `8.8:lem-target-independence`, II:109661 | Explicitly incomplete. |
| H-C7c | `8.9:lem-age-lemma`, II:112000–112001 | Explicitly incomplete. |
| H-C7d | `8.12:prop-depth-floor-rarity`, II:126839 | Explicitly incomplete and volume dependent. It is not uniform-old-rarity. |
| H-C8a | `8.21:lem-source`, II:145173–145218 | Explicitly outstanding. Its live-age bound and decomposition are hypotheses, including the stronger use-site forms identified below. |
| H-C8b | `8.21:lem-continuum-kernel`, II:145220–145222 | **Statement and proof unwritten.** Carry the exact consumer form at II:145343–145350 as H-CK: every kernel limit point lies between the displayed positive lower bound and upper bound. This is not proved by C1. |
| H-GX | `8.2:prop-gaussian-extraction`, II:77279–77433 | C5, not ported in this round. Unqualified heading; explicit named antecedents. C11:71370 calls part (b) incomplete; III:110943–110950 describes the second-order deduction conditional on correlation, cluster estimates, Balaban 102b, and **q ≥ 21p0+1**. Retain both declarations and all C3/C4 inputs. |
| H-GX1 | `8.2:lem-extraction-one-point`, II:76772–76774; `8.2:lem-one-step-extraction`, II:76125 | Remark placeholders, not full theorem statements. Do not manufacture their hypotheses from the “lemma” labels. H-GX includes the precise use-site estimates needed below, separately named H-GXa and H-GXb. |
| H-flow | `3.1:thm-main` (0), and `8.1:eq-coupling-envelope-f`, II:68936–68938 | Conditional running-flow result, with positive lower envelope; P1 arithmetic and P6 do not erase its induction assumptions. |
| H-corr | `8.1:prop-correlation-witness-depth`, II:68570; correlation theorem (P6) | Correlation theorem at witness depth, with its actual admitted source domains and torus exponent equal to s. |
| H-kernel | `8.1:lem-kernel-bounds`, II:69925; `8.1:lem-running-normalisation`, II:70501 | Kernel bounds: C1/P3 checked on its stated free-minimiser premises. Running normalization remains conditional on correlation and slope bounds. N = ζ′ is the same quantity, by II:68752–68760. |
| H-healed | `8.6:thm-block-bound-healed`, II:104763; `8.9:prop-healed-old-region`, II:113036 | CA conditional implications; retain H-C6 and H-C7. |
| H-young | `8.8:cor-young-block-rarity`, II:110854 | CA conditional implication, in the precise Case V/young-age uses of the assembly. |
| H-age | `8.18:lem-horizon-cases`, II:143297; `8.18:prop-witness-below-horizon`, II:144388; `8.18:prop-witness-beyond-horizon`, II:144797 | CA proved implications with their full displayed antecedents. C9 assembles these, rather than independently proving their analytic premises. |
| H-closure | `8.18:lem-healed-slices`, II:144214; `8.18:prop-age-antecedent`, II:144336; `8.18:prop-linear-floor`, II:144653 | Conditional age closure, using the prolonged run, terminal reserve, positivity and stability. H-C7 remains attached. |
| H-positive | `4.32:prop-positivity-dichotomy` (I:156837), `6.1:lem-reflection-positivity` (II:60440), `1.1:lem-invariance` (I:559) | Positivity dichotomy remains outstanding. Lattice reflection positivity is a separate CA result; invariance is in P1. |
| H-limit | `3.1:thm-main` (ii-T-a), (ii-T-b), (ii-R4) | Only the actual limit modes and tested correlations in those clauses. Tuned limits retain their uniqueness hypotheses. No clustering or Wightman conclusion is imported. |

H-VT consists of **each** of C10's assumptions (a)–(f), not just a stability slogan. Its labels are `6.2:lem-chessboard-estimate` (II:61205), `6.2:lem-support-placement` (II:61417), `6.2:lem-periodised-weight` (II:61517), `6.2:lem-face-estimate` (II:62293), the Schwarz–Cauchy input (proved directly below), `6.4:thm-per-ball-bound` (II:63964), correlation properties (T1)–(T5), `8.22:lem-trace-subadditivity` (II:140995), and `8.22:lem-vacuum-energy-density` (II:141276). These are CA conditional results retained at that standing. The last density lemma includes its determinant comparison, Balaban 109 (1.7) normalisers, Balaban 119 (2.27)(i)–(iv), (2.29), (2.31)–(2.33) format, and the torus-independent run. P7 and refereed lsc are available inputs on their own domains; no automatic replacement of these hypotheses is asserted.

Additional named use-site inputs: **H-add** is the additive live-slot/age-moment hypothesis explicitly described by `8.12:cor-weak-torus-witness` (II:126663–126670, assumptions (c),(d)) and `8.12:cor-finite-volume-witness` (II:127099–127102, assumption (5)). These passages call it the “additive theorem” without supplying a separate label there; this port does not invent one. Its exact weighted first-/second-moment use is displayed in the C11 proof below. **H-free-torus** is the free Maxwell torus-kernel comparison used at `8.21:cor-consequences-torus` (II:145497–145499), retained as a cited free-field input. **B24** is Balaban CMP 99b p.394 and Corollary 3.8 p.410, explicitly cited in the vacuum-density hypothesis at II:141336–141343; its joined-domain admissibility remains attached. **H-OS-transfer** is the Osterwalder–Seiler Wilson transfer positivity cited in the trace proof at II:141037–141038. None of these citations grants a proof here.

### Published-input hypotheses, individually retained

These are the account's own clause-(iv) list, II:145537–145587. The labels B01–B23 name hypotheses, **not independently checked published proofs**. Balaban receives credit for each. Formula ranges mean every listed formula with its hypotheses, not a proposed substitute.

| Name | Balaban input retained |
|---|---|
| B01 | CMP 95 (1.3), (1.5), (1.16)–(1.19), (1.23)–(1.24), free propagators and step decomposition. |
| B02a, B02b, B02c | CMP 96 Propositions 2.3, 2.6, 2.7, respectively, fluctuation decay. |
| B03 | CMP 98 (19)–(20), averaging. |
| B04 | CMP 99b (3.156), §§C–E, background propagator decay. |
| B05 | CMP 102b Theorem 1, including (6)–(10), minimiser regularity. |
| B06 | CMP 102b Proposition 9, (190), pp.308–309, (172), (182), analyticity. |
| B07 | CMP 109 §2, (2.1), (2.3)–(2.13), (2.16), pp.267–268, small-field step. |
| B08 | CMP 109 Theorem 1, §0, (0.12), (0.14)–(0.26), (0.28)–(0.30), effective action. |
| B09 | CMP 109 §§1–3, (1.3), (1.7), (1.11)–(1.16), (1.18), (1.19), (3.1), (3.2), (3.9), (3.32); §4, (4.4), (4.8), (4.9), (4.14), (4.15), (4.17), (4.18), local terms and constant flux. |
| B10 | CMP 109 Theorem 3, (1.20)–(1.22), (3.61), (5.1)–(5.7), (5.16), coupling renormalisation. |
| B11a, B11b, B11c | CMP 116 Lemma 2 with (1.26), (1.36), (1.41)–(1.43); Lemma 3; and (2.3), (2.5)–(2.6), Appendix C, respectively. |
| B12a, B12b, B12c | CMP 119 Theorem 2; Corollary 3; and (0.1), §2, (2.1)–(2.3), (2.8), (2.10)–(2.37), pp.247,254–256, respectively. |
| B13 | CMP 119 §1, (1.1), (1.5), (1.8), (1.9), (1.11), (1.12), (1.18), (1.19), regularity and cutoffs. |
| B14 | CMP 119 §3, (3.1)–(3.25), small-field step. |
| B15 | CMP 119 (3.40), (3.50), (3.56)–(3.61), (3.65), (6.1), running flow. |
| B16 | CMP 122a §0, (0.3)–(0.5), (1.1), (1.3)–(1.4), (1.98), (1.100)–(1.102), histories. |
| B17 | CMP 122a §1, (1.12)–(1.20), (1.22)–(1.24), (1.27), (1.28), (1.55), (1.75), (1.76), (1.79), (1.82), (1.88), pp.175,177, creation geometry. |
| B18 | CMP 122b §1, (1.2)–(1.10), (1.33)–(1.35), (1.98)–(1.102), pp.355,378,380,383,391, localisation. |
| B19 | CMP 122b (1.70)–(1.73), (1.79)–(1.89), large-field bounds. |
| B20 | **Printed without proof:** CMP 122a pp.178–179, admissibility of prepared data. Refereed pda addresses this input on its stated domain; it is not a blanket proof of every other admission. |
| B21 | **Printed without proof:** CMP 95 §1, flat step quadratic form equals the free one. |
| B22 | **Printed without proof:** CMP 122b §1, positivity and bound for the normalized island operation. |
| B23a, B23b | **Cited as printed:** CMP 122a p.192 (1.70), and CMP 122b p.377 (1.68)–(1.69), respectively, joined-domain convergence and analytic extension. |

The inherited published hypotheses of H-corr, H-kernel and H-VT are retained too, by their labels in P1/P3/P4/P5/P6/P7. This is not a proof of Balaban's cited theorems. Non-Balaban positivity/compactness hypotheses retain their own standing.

## Proof of C10, on the account's route

Source proof: II:141585–141852. All quantities and constants are exactly those in the statement.

**Placement and source.** Put ε = L^(-K). The cell side ℓ is the least power of L above 16(R+1). Since L^m ≥ L^(m′) ≥ ℓ > 2R, the ball does not wrap. H-VT's placement lemma gives one translation in ε Z⁴ placing it at distance at least R+2 from every cell face. Translation preserves both Wilson measures and each sharp norm by `1.1:lem-invariance`; translate both functions by that same vector.

Write a_i = ‖F_i‖♯ and D = {z: |z₁|a₁+|z₂|a₂ < ϱ/𝔯}. Set w_z = z₁F₁+z₂F₂. For a cell-reflection group element η, let ε(η) be its parity and u^(+)=u, u^(−)=conjugate(u). Define

\[
W_z=\sum_{\eta\in\mathfrak G_\ell}(w_z\circ\eta^{-1})^{(\epsilon(\eta))}.
\]

The reflected balls are disjoint. Reindexing η=θη′ for a generating reflection θ gives ε(η)=−ε(η′), η⁻¹θ=η′⁻¹, and W_z∘θ=conjugate(W_z). Every reflected ball retains the R+2 margin. A crossing plaquette's barycentre is within 2ε of a face; R+2>2ε since ε≤1. Thus W_z vanishes there. These are the two mirror-periodicity hypotheses of the trace lemma. The group gives period 2ℓ. Since 2L^(m″)/ℓ is even for m″≥log_Lℓ, W_z descends to both tori. H-VT's periodised-weight lemma gives ‖W_z‖♯≤|z₁|a₁+|z₂|a₂<ϱ/𝔯. For 𝔯=2 retain the four-real-function reading at (z, conjugate z). No holomorphy of W_z itself is claimed.

**Chessboard and transfer.** Only one cell carries w_z. With n_m=(2L^m/ℓ)^4, the chessboard inequality is

\[
|Z_m(w_z)|/Z_m(0)\le [Z_m(W_z)/Z_m(0)]^{1/n_m}.
\]

Let k=L^(m−m′). Apply `8.22:lem-trace-subadditivity` successively in coordinates 1,2,3,4, through the rectangular tori. At each step the partition function is at most the previous one raised to k. Because k is odd, raising real inequalities to k preserves them; induction gives Z_m(W_z)≤Z_(m′)(W_z)^(k⁴). Both endpoint partition functions are nonnegative by their chessboard-value identities. Also n_m=k⁴ n_(m′). Taking nonnegative n_m-th roots gives

\[
|Z_m(w_z)|/Z_m(0)\le Z_{m'}(W_z)^{1/n_{m'}}Z_m(0)^{-1/n_m}. \tag{VT1}
\]

Zero-source denominators are strictly positive: their finite-dimensional integrands are positive on a compact group of positive Haar mass. No nonzero-source lower bound was used.

**Stability and normalization.** On the small torus use

\[
Z_{m'}(W_z)\le \exp\{E_{m'}+\Re\mathcal E_{m'}(W_z)+E_+^\sharp(2L^{m'})^4\}.
\]

On the large torus use only Z_m(0)≥exp{E_m−C_low(2L^m)^4}. Since (2L^(m″))⁴/n_(m″)=ℓ⁴, (VT1) becomes

\[
|Z_m(w_z)|/Z_m(0)
\le \exp\{n_{m'}^{-1}\Re\mathcal E_{m'}(W_z)
 +(\mathsf B+\delta_{\rm vac})\ell^4\},
\quad
\delta_{\rm vac}=|E_m/(2L^m)^4-E_{m'}/(2L^{m'})^4|.
\tag{VT2}
\]

The sign of the vacuum difference is bounded above by its absolute value. H-VT(f) gives δ_vac≤bar δ_vac. It is essential that E_m has that lemma's vacuum-normalized meaning.

**The common counterterm.** Use the per-ball counterterm built entirely on m′:

\[
\mathcal E''(z)=n_{m'}^{-1}\sum_{\eta\in\mathfrak G_\ell(\mathbb T_{m'})}
[\mathcal E^{\rm bulk}_{\eta c}((w_z\circ\eta^{-1})^{(\epsilon(\eta))})]^{(\epsilon(\eta))}
 +\mathcal E^\partial(w_z).
\]

H-VT(c) asserts holomorphy on D, E″(0)=0 and the real-part bulk identity. Subtract that identity from n_(m′)^(-1) Re E_(m′)(W_z). Only n_(m′)^(-1) Re E^∂_(m′)(W_z)−Re E^∂(w_z) remains. The two face bounds make this at most 2C_face(R)≤4C_face(R). Define, using this **same function** E″ for both volumes,

\[
h_v(z)=e^{-\mathcal E''(z)}Z_v(w_z)/Z_v(0),\qquad v=m,m'.
\]

Each h_v is holomorphic on D and h_v(0)=1. Indeed, for fixed finite K,v the linear observable O(w_z) is bounded uniformly in the group variables on each compact z-set. The exponential power series converges uniformly there, allowing termwise integration (filled F10.1). Thus Z_v(w_z) is entire. Equation (VT2), the face cancellation and δ_vac≤bar δ_vac yield |h_m|≤Q_star. The per-ball bound gives |h_(m′)|≤exp{Bℓ⁴+4C_face}≤Q_star, exactly as printed.

**Schwarz–Cauchy, with its constant (filled F10.2).** If either a_i=0, F_i=0 and the claimed mixed derivative vanishes. Otherwise put A=ϱ/𝔯 and Q=Q_star. The function (h_v−1)/(Q+1) has modulus at most one and vanishes at zero. On every complex line through zero, the one-variable Schwarz inequality gives

\[
|h_v(z)-1|\le(Q+1)(|z_1|a_1+|z_2|a_2)/A.
\]

For completeness, the Schwarz inequality here follows by applying the maximum principle to f(t)/t on a disc of radius b<1 and letting b↑1. On the polydisc with radii b_i=A/[2a_i(2Q+2)], the right side is ≤1/2 (first take slightly smaller radii). The convergent series Log(1+u)=Σ_(n≥1)(−1)^(n+1)u^n/n then gives |Log h_v|≤Σ_(n≥1)2^(−n)/n=log 2. The last equality follows by integrating the geometric series on [0,1/2]. Double Cauchy integration and passage to the displayed radii give

\[
|\partial_1\partial_2\operatorname{Log}h_v(0)|
\le \log2\,(2Q+2)^2(2\mathfrak r/\varrho)^2a_1a_2.
\]

Only a neighbourhood of zero needs to be zero-free. There,

\[
\log Z_v(w_z)=\log Z_v(0)+\mathcal E''(z)+\operatorname{Log}h_v(z).
\]

Differentiating twice gives the connected covariance: differentiating Z yields the first and second moments, and ∂₁∂₂ log Z=Z₁₂/Z−Z₁Z₂/Z² (filled F10.3). Subtracting the two volumes cancels ∂₁∂₂E″ exactly. Applying the last bound twice gives C_VT exactly as printed, including its factor 2 log 2.

B, bar δ_vac, ℓ, C_face, 𝔯 and ϱ have precisely the parameter dependence listed in C10. Translation removes the position dependence. The separation-dependent mixed counterterm cancels rather than being bounded. This completes the conditional proof of C10, for signed or overlapping functions as stated. On the large torus the only analytic stability input used was the zero-source lower bound.

## Proof of C9, on the account's route

Source: II:145031–145115; the expanded consequences use `8.21:cor-consequences-torus`, II:145312–145518. H-age, H-flow, H-positive, H-CK and H-limit remain hypotheses.

**The depth condition and its endpoint (correction C9.1).** The exact statement above prints an equivalence with d≤sup{d:s(d)≥n}, where n=max{s_W(g),s_vol(g,m)}. Its argument from monotonicity alone is invalid at the endpoint. In fact, with the account's definition s(d)=min{j≥0:L^j d≥C_W(j)}, for an integer n≥1,

\[
s(d)\ge n\quad\Longleftrightarrow\quad
 d<\min_{0\le j<n}\{C_W(j)L^{-j}\}. \tag{D1}
\]

Proof: s(d)≥n says that no j<n satisfies L^j d≥C_W(j). Negating each of these finitely many non-strict inequalities gives exactly (D1). At their positive minimum at least one j<n meets equality, so s(d)<n. Thus the supremum in C9 is not attained. Replace only the prose equivalence d≤d_W^T by d<d_W^T for n≥1, or retain the actual displayed condition s(d)≥n. If n=0 the condition is automatic. The same correction applies to “largest” in II:144832–144836. No constant or depth condition is changed.

**Part (a).** Every admitted m satisfies exactly one of m≤m_V(g) and m>m_V(g). In the first case the horizon lemma gives K+m≤K_*−1. The volume floor is zero by definition. The below-horizon proposition therefore applies, with the same γ_W^T=min{γ_W,γ_*^†}, witness depth, ultraviolet floor and test pair. It gives the displayed law, |R_K|≤1/4, ζ′∈[2/3,4/3], and both kernel bounds. In the second case the beyond-horizon proposition applies because s≥s_vol(g,m) as well as s≥s_W(g). Its conclusion is the same. The statement |R_K|≤1/2 follows from 1/4≤1/2. This is a case split of conditional propositions; no normalised old-region rarity is substituted for their finite-volume closure.

**Part (b).** The normalization square belongs to [4/9,16/9], and the weaker remainder bound puts 1+R_K in [1/2,3/2]. The remaining factor b₀g_(K−s)^4 K_s is nonnegative and strictly positive for nonzero witness tests. Multiplying yields (4/9)(1/2)=2/9 and (16/9)(3/2)=8/3. H-flow gives

\[
0<\underline x_s=g^{-2}+\lambda^\sharp s-c_5
 \le g_{K-s}^{-2}\le\bar x_s=g^{-2}+B^\sharp(s+1).
\]

Since t↦t^(−2) decreases on the positive half-line, bar x_s^(−2)≤g_(K−s)^4≤underline x_s^(−2). Insert lower with lower and upper with upper in the kernel sandwich. This is exactly C9(b), with no change to 2/9 or 8/3.

**Part (c).** The constants of the two case propositions are independent of K,g₀,m and position. The only additional restriction beyond the admitted torus family is s_vol(g,m), and it is zero below the horizon. Thus the stated uniformity holds. A formula with volume-independent constants does not provide a volume-independent domain of allowed d beyond the horizon.

**Part (d): passage to each torus limit.** Fix g,m,d and a nonzero pair before taking K→∞. Once K−s≥k_W, the bounds of (b) hold with endpoints independent of K. H-limit says the tested connected correlations converge. A real limit of numbers in a fixed closed interval remains in that interval: if the limit were less than the lower endpoint, half their positive difference would contradict convergence, and likewise for the upper endpoint (filled F9.1). This covers each admitted subsequential limit, and each tuned limit only with its own hypotheses.

For the explicit continuum-kernel reading of II:145343–145350, retain H-CK. Passing to a common subsequence for g_(K−s) and the bounded kernel is legitimate: both lie in fixed compact intervals, the first bounded away from zero. Repeated interval bisection produces a convergent subsequence of each; restrict the first subsequence for the second. The connected correlation already has its specified limit, so this does not select a new value of it (filled F9.2). In the notation of the source corollary this yields

\[
\frac29 b_0c_{\mathcal K}\vartheta^2\|f_1\|_\infty\|f_2\|_\infty\bar x_s^{-2}
\le S(f_1,f_2)
\le\frac{800}{3}b_0C_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty\underline x_s^{-2}. \tag{T1}
\]

These are its deliberately weaker continuum bounds, including θ² and 100. The direct closed-interval passage from C9(b) also preserves its stronger stated bounds whenever the limit convention tests exactly the same pair. Nothing here constructs the unwritten H-CK.

**Positive reflected variance.** Choose smooth nonnegative reflected bumps (f,ιf) of the prescribed small shape, supported on opposite sides of a torus mirror. Such bumps exist with some fixed positive shape parameter; choose the coupling/depth thresholds for that parameter. At the lattice level set A=O(f)−E O(f) and Ω=1. Reflection invariance gives E O(ιf)=E O(f). Reflection positivity and this identity give

\[
\langle\Omega,\Omega\rangle=1,\quad
\langle\Omega,A\rangle=0,\quad
\langle A,A\rangle=S^T_{2;K}(\iota f,f).
\]

Pass these three entries to the limit form supplied by H-limit, rather than assuming convergence of an uncentred one-point observable. Equation (T1) gives a strictly positive last entry. Thus A and Ω give two nonzero orthogonal classes. This is positive variance in the reflection-positive form, exactly the account's use of that term; it is not a proof that the Hamiltonian acts nontrivially.

**Logarithmic behaviour (filled F9.3).** Let t=log_L(1/d). Minimality of s(d) gives

\[
t\le s(d)<1+t+\log_L C_W(s(d)-1).
\]

The last term is O(log log(s+2)) for fixed g. For all sufficiently large s it is at most s/2−1, giving s<2t. Also its ratio to s tends to zero; dividing the preceding inequalities by s proves s/t→1. All finite floors at this fixed m are eventually exceeded. For sup-normalized dilates define Q(d)=S(f₁^d,f₂^d)/(‖f₁‖∞‖f₂‖∞). The shape, mass and separation conditions persist under dilation by the change of variables x=du, with integrals multiplied by d⁴ and Lipschitz constants by d⁻¹. Equation (T1) gives positive constants c,C with c/log(1/d)²≤Q(d)≤C/log(1/d)². For any ε>0, writing u=log(1/d), the elementary exponential-series bound e^(εu)≥(εu)^3/3! proves d^(−ε)Q(d)→∞. Thus Q→0 more slowly than every positive power.

Scale invariance with any assigned curvature dimension would give Q(σd)=σ^a Q(d). For a>0 this contradicts the lower logarithmic bound; for a=0 it contradicts Q→0; for a<0 it diverges. This excludes the account's local scaling law on a fixed torus, not an independent classification of all torus symmetries.

**Maxwell comparison (filled F9.4; correction C9.2).** The source at II:145496–145498 says the free Maxwell quotient tends to a strictly positive constant “at any charge.” At zero charge it is zero, so that sentence needs the smallest correction: handle zero charge separately by Q>0. For a nonzero charge, the free-curvature comparison assumed by the source gives the homogeneous off-diagonal curvature kernel of degree −4, with a bounded smooth torus correction. In its quadratic-density covariance, Wick contraction squares that kernel. Under x=du,y=dv, the leading d⁻⁸ cancels dx dy=d⁸du dv; the cross term with the bounded correction is O(d⁴), and its square is O(d⁸). The leading coefficient is positive for a nonzero charge and nonnegative nonzero separated bumps by the squared-kernel positivity in C1. Hence its quotient tends to a positive constant, contrary to Q→0. This uses the stated free torus-kernel comparison as a named published/free input, not the unwritten interacting continuum-kernel lemma as if proved.

Finally define g_eff=(Q/b₀)^(1/4). Equation (T1), with positive quantities, gives exactly

\[
\left(\frac{3}{800C_{\mathcal K}}\right)^{1/2}\underline x_s
\le g_{\rm eff}^{-2}\le
\left(\frac{9}{2c_{\mathcal K}\vartheta^2}\right)^{1/2}\bar x_s.
\]

This proves the positive logarithmically vanishing effective coupling, with two-sided rate only. It neither fixes the sharp one-loop coefficient nor supplies non-Gaussianity. This completes C9's conditional proof, with the endpoint prose corrected.

## Proof of C11, on the account's route

The proof occupies II:71970–73500, split into main term, profile, large-field, local, extraction, irrelevant, and constant-choice parts. The kept-label alternative at II:73057–73213 is not the route used. All proof inputs in the preceding ledger remain attached.

### Precise use-site hypotheses and admission

**H-source-use (outstanding form of H-C8a).** Assume the whole-support decomposition and quantitative bounds actually used at II:72013–72059, 72288–72359, 72531–72640 and 72642–72703. In particular, in the resummed index,

\[
\Phi_i=c_i^0+G_i+\mathfrak L_i,\qquad
G_i=N_{k_0}\mathcal O^{(k_0)}(\tilde f_i)+\mathrm{Irr}_i,
\quad |G_i|\le C_G\mathfrak n_i\varepsilon^2,
\quad\mathfrak L_i=\mathfrak L_i^{\rm near}+\mathfrak F_i,
\]

with the source profile perturbation bound, mixed-derivative spanning decomposition, near/far bounds, age amplification and source-derivative support properties used below. These are the account's named source inputs, not new proved facts. The final `8.21:lem-source` has only clauses (a)–(d), and is outstanding; it does not literally print all the clauses (c)–(e), corollary, and (M4) referenced earlier. Therefore the **use-site forms must remain additional named hypotheses**. In particular one cannot cite its final label as a proof of an unprinted mixed-derivative clause.

**H-GXa (conditional extraction-error form).** `8.1:rem-extraction-errors` (II:71180–71277) and `8.1:prf-extraction-remainder` (II:72821–73002) use the block-law extraction error with its six terms T₁,…,T₆ below. Assume precisely that bound, including the corollary of the source lemma for its observable suprema. This is not identified without proof with C5(a)'s different local joint-moment statement.

**H-GXb (incomplete irrelevant-covariance form).** At II:73004–73054, `8.1:prf-irrelevant-remainder` explicitly takes its “clause (b) of Gaussian extraction” as an incomplete hypothesis. Retain the exact bound 7C_b ρ⁻² p₀(g_(k₀))⁴ times the main term, plus the stated extraction-error terms. Keep H-C4a–c and q≥21p₀+1. C5's heading and the assembly's later status sentence do not silently discharge this use-site form.

**H-depth (admission form).** Besides the displayed s≥s_W(g), the extraction uses r(s)≤s−s_*, s≥m_T(g), and 2B^♯(r(s)+1)≤underline x_s. The definition II:68983–68989 takes the *first* integer satisfying these conditions. Its proof at II:69049–69069 shows eventual satisfaction, but does not establish satisfaction at every integer after that first one. Ceilings in r(s) preclude inferring monotonicity merely from r(s)=O(log log s). Preserve these actual admission conditions as H-depth. A sufficient minimal clarification, if upward closure is not separately proved, is to define s_W by the first **tail** on which all three hold, just as CA defines s_vol and s_T. This is a proposed correction of the threshold definition, not a claim that the printed minimum already has that property. The conditional proof below assumes the three conditions as its named admission input; it does not silently enlarge the printed s_W.

These qualifications explain the sense of “proof” here: a complete deduction from the account's stated and use-site hypotheses. They leave a statement-to-supplier reconciliation open. They are not substitutes for C2–C8 proofs.

### Main term and the exact remainder identity

Set k₀=K−s, x=g_(k₀)^(-2), n_i=𝔫(f_i), ε=g_(k₀)p₀(g_(k₀)), and

\[
\mathfrak S=g_{k_0}^4n_1n_2\rho^{-8},\qquad
\mathfrak M=N_{k_0}^2b_0g_{k_0}^4\mathcal K_{K,s}(f_1,f_2),\qquad
c_M=\frac49b_0c_{\mathcal K}.
\]

H-kernel gives M≥c_M S≥c_M θ²g_(k₀)^4‖f₁‖∞‖f₂‖∞>0. H-flow gives underline x_s≤x≤bar x_s≤bar x(underline x_s), where bar x(y)=(B^♯/λ^♯)(y+c₅)+B^♯. All these are the account's constants.

The positive history decomposition and `8.1:lem-total-covariance` give

\[
S^T_{2;K}=E_{\tilde\nu}\Psi+\operatorname{Cov}_{\tilde\nu}(\Phi_1,\Phi_2).
\tag{W1}
\]

**Filled F11.1.** To see the algebra without suppressing a normalization derivative, let Z(z)=Σ_h∫τ_h(z), Φ_i=∂_i log τ_h|₀, Ψ=∂₁∂₂ log τ_h|₀. Then ∂_iτ_h=τ_hΦ_i and ∂₁∂₂τ_h=τ_h(Ψ+Φ₁Φ₂). Divide by Z(0), subtract the product of first derivatives, and obtain (W1). The positive common-support analytic representation and permitted differentiation are hypotheses of the history decomposition; this algebra does not prove them.

In the resummed index `8.1:rem-healed-summed-out`, every healed label has been summed out. Thus m_i=c_i^0, the deep pieces vanish, and constants have zero covariance. The exact expansion is

\[
\begin{split}
\operatorname{Cov}(\Phi_1,\Phi_2)
={}&\operatorname{Cov}(G_1,G_2)
 +\operatorname{Cov}(\mathfrak L_1,G_2)
 +\operatorname{Cov}(G_1,\mathfrak L_2)
 +\operatorname{Cov}(\mathfrak L_1,\mathfrak L_2),\\
E\Psi={}&R^{\rm loc}+R^{\Psi,\rm live},\\
\operatorname{Cov}(G_1,G_2)
={}&\mathfrak M+R^{\rm prof}+R^{\rm GX}+R^{\rm irr}.
\end{split}
\tag{W2}
\]

The last line uses H-GXa/H-GXb; the previous line uses H-source-use. Let R^L be the three displayed live covariances and R^B′=R^L+R^(Ψ,live). Then

\[
S^T_{2;K}-\mathfrak M
=R^{\rm prof}+R^{\rm GX}+R^{\rm irr}+R^{\rm loc}+R^{\mathcal B'}.
\tag{W3}
\]

The account's sixth slot (sh)′ and its R^(mL) both vanish. Position averaging is a finite average over simultaneous bare-lattice translates, justified by `1.1:lem-invariance`; its absolute value is bounded by the average of the absolute bounds. It does not require the distinct unproved label-translation assertion H-C7a to identify the bare covariance.

**Correction C11.1 (signed remainders versus majorants).** Several printed displays replace signed remainder symbols by nonnegative majorants: II:72563's `R^{Psi,live}:=`, II:72684's definition of R^loc, and the one-sided inequalities for R^L and R^irr. In (W2)–(W3) R means the actual signed contribution. Write B_R for its nonnegative bound and use |R|≤B_R. Also the sentence at II:73229 that every live pairing is in R^(Ψ,live) is corrected to: the live pairings are in R^L **and** R^(Ψ,live). The exact expansion (W2) proves this correction. Neither constants nor estimates change.

### Profile remainder

Source: `8.1:prf-profile-remainder`, II:72182–72286. Write tilde f_i=f_i+δ_i and K=K_(K,s). The profile neighbourhoods stay at separation at least ρ/2 under the printed C₀^prof floor. H-kernel and the profile input give

\[
|\mathcal K(u,v)|\le2^8C_{\mathcal K}\rho^{-8}\mathfrak n(|u|)\mathfrak n(|v|),\quad
\mathcal K(f_1,f_2)\ge c_{\mathcal K}\rho^{-8}n_1n_2,
\]

for (u,v)=(δ₁,f₂),(f₁,δ₂),(δ₁,δ₂), and

\[
\xi_i:=\mathfrak n(|\delta_i|)/n_i
\le\xi:=160\mathfrak d_W(x)C_hM/(\vartheta^2\rho).
\]

Bilinearity yields exactly three error terms. Divide their bounds by M; the factors N²b₀g⁴ρ⁻⁸n₁n₂ cancel, leaving

\[
|R^{\rm prof}|/\mathfrak M
\le2^8(C_{\mathcal K}/c_{\mathcal K})(\xi_1+\xi_2+\xi_1\xi_2).
\]

The printed floors ρ≥160C_hM/θ² and d_W(x)≤1/3 imply ξ≤1/3. Hence 2ξ+ξ²≤3ξ. Keep C_prof≥3·2⁸·160 and

\[
C_0^{\rm prof}=\max\left\{
\frac{32}{3}C_{\rm prof}\frac{C_{\mathcal K}}{c_{\mathcal K}}\frac{C_hM}{\vartheta^2},
\frac{160C_hM}{\vartheta^2}\right\}.
\]

For ρ≥C₀≥C₀^prof this proves |R^prof|≤M/32. Label-supported perturbations remain in L_i, not δ_i. If a zero profile were allowed, its perturbation is zero as well and both sides vanish; actual witness profiles are nonzero.

### Large-field remainder

Source: `8.1:prf-large-field-remainders`, II:72288–72640. Write a_i=s_i^♯ and b_i=f_i for the **bounds** of the near and far pieces in this paragraph only; the original tests are still denoted f_i inside norms. These bounds are

\[
a_i\le 10C_{\rm live}\bar\Theta\,\mathfrak p_{\rm src}(\bar x_s)\rho^8\|f_i\|_\infty/\vartheta,
\qquad
b_i=C_{\rm src}C_{\rm far}\|f_i\|_\infty\rho^8e^{-\varkappa\rho/16}.
\]

Separate O_i, the event of a near live component older than l. Off O_i, the near part is ≤a_i and vanishes outside the young contact event, of mass ≤q_W. The far part is ≤b_i everywhere. Therefore E|L_i|≤a_iq_W+b_i and sup|L_i|≤a_i+b_i on this truncated piece. For bounded variables,

\[
|\operatorname{Cov}(X,Y)|=|E[X(Y-EY)]|\le2\|Y\|_\infty E|X|. \tag{W4}
\]

The two cross covariances with G_i are consequently bounded by

\[
2C_G\varepsilon^2[n_2(a_1q_W+b_1)+n_1(a_2q_W+b_2)].
\]

Let B₁₂ be joint young contact. Its live contribution is bounded by min{n_cells(N₁),n_cells(N₂)} q^lv, not by a square of q^lv: P(B₁∩B₂)≤min{P(B₁),P(B₂)}, and each P(B_i)≤n_cells(N_i)q^lv by a union bound. Include q_× if the use-site geometric exceptional event is retained, and set q₁₂=min{n_cells(N₁),n_cells(N₂)}q^lv. In the resummed route there is no C_LF q_W² term from a healed pair.

Expanding the four near/far covariances, their bounds are

\[
\begin{split}
|\operatorname{Cov}(L_1,L_2)|\le{}&
 a_1a_2(q_{12}+q_\times+q_W^2)
 +2(a_1b_2+b_1a_2)q_W+2b_1b_2.
\end{split}
\tag{W5}
\]

For example, E[near₁near₂] is ≤a₁a₂P(B₁₂), while |E near₁ E near₂|≤a₁a₂q_W²; this is why the single live weight occurs linearly. The mixed near/far terms follow from (W4), and the far/far term from (W4) with E|far|≤b.

The live exponent covariance has the same support rule by `8.1:lem-mixed-derivative-locality` (II:70983) and H-source-use. Its absolute expected value is bounded by

\[
2a_1a_2(q_{12}+q_\times)
 +2(a_1b_2+b_1a_2)q_W+2b_1b_2, \tag{W6}
\]

or the larger printed majorant with 4b(aq_W+b). No independence between the two live components is assumed.

**Filled F11.2 (preserving both profile factors).** The source compresses indexed quantities into their maxima before dividing by ‖f₁‖∞‖f₂‖∞. That compression alone does not justify a bound uniform in their relative amplitudes. Retain the indexed expressions above: every term has one factor linear in f₁ and one in f₂. Equivalently apply the argument first to each profile divided by its nonzero supremum, then use bilinearity to restore their product. Both routes give the printed constants and avoid a spurious max(‖f₁‖∞,‖f₂‖∞)² loss.

On O_i, H-source-use multiplies each near bound by L^(4(a−l)), with a the largest relevant age. H-closure and the account's additive age bound give the one-factor sum

\[
a_i n_{\rm cells}(N_i)\sum_{a>\mathfrak l}L^{4(a-\mathfrak l)}q_{k_0}^{=a}
\]

and the two-factor sum

\[
a_1a_2(n_{\rm cells}(N_1)+n_{\rm cells}(N_2))
\sum_{a>\mathfrak l}L^{8(a-\mathfrak l)}q_{k_0}^{=a}.
\]

These include both the expectation products and joint terms in the additive theorem's majorant. Healed-later slices use H-healed; never-healed slices use the terminal reserve with the stated per-torus floor. These sums are **hypotheses supplied by that conditional age closure**, not estimates derived merely from the word “old.” There is no use of uniform-old-rarity.

Divide (W4)–(W6) and the age shares by c_M θ²x⁻²‖f₁‖∞‖f₂‖∞≤M. Substitution gives the source's two types of bound:

\[
\widehat C_{\rm tot}\bar\Theta^2\mathfrak p_{\rm tot}(\bar x_s)\bar x_s^2
 e^{-c_{\rm src}p_0(g_{k_0})}\vartheta^{-4}, \tag{W7}
\]

\[
\widehat C'_{\rm tot}\bar\Theta\mathfrak p'_{\rm tot}(\bar x_s)\rho^{24}\bar x_s^2
 e^{-\varkappa\rho/16}\vartheta^{-2}. \tag{W8}
\]

Here c_src is replaced by min{c_src,c_lv} when the one-cell live bound is included, exactly as at II:72609–72630. To check the powers, a₁a₂q_W² contributes ρ^(16+8)x²θ⁻⁴e^(−2c′p₀); a₁a₂q_× contributes ρ^(16+4)x²θ⁻⁴e^(−c′p₀); and n₂ε²a₁q_W contributes ρ^(4+8+4)xp₀² times its fixed θ-factor. Every term has one of the two displayed decays. Powers of ρ and p₀ are fixed polynomials in log bar x_s. A far/far term has twice the decay and is bounded by the same far majorant. **Filled F11.3 (normalization and finite budgets).** The hatted constants in (W7)–(W8) are the coefficients *after* division by c_M. Fix the source's unrestricted summary constants C_tot and C′_tot large enough to majorize both the hatted coefficients and c_M times those coefficients, with the polynomial factors including the finite sum of terms. Then the printed source ceiling gives

\[
\widehat C_{\rm tot}\vartheta^{-4}
\sup\mathfrak F_{\rm src}
\le\frac{\widehat C_{\rm tot}c_M}{64C_{\rm tot}}\le1/64,
\]

and the printed far floor gives the identical bound with the primed constants and θ². This spells out the normalization implicit in the source's changing summary constants; it is essential to retain c_M when passing between absolute and relative budgets. It changes none of the numbered numerical constants (32, 64, 448, etc.) and requires no dependence on g,K,m or s. In particular the finite sum is budgeted once, not 1/32 per summand.

The printed γ-src and C₀-src choices pay (W7) and (W8), including the age shares, with their two 1/64 allocations. Thus the total absolute majorant for R^B′ is ≤M/32. The missing age/source inputs retain their standing.

### Spanning local remainder

Source: `8.1:prf-local-remainder`, II:72642–72819. H-source-use bounds the absolute mixed spanning term by the sum, over j≤k₀ and local regions X with X⁺ meeting both supports, of

\[
\sum_T\sup_{\mathcal W_j(X)}|T|\,
4\|f_1\|_\sharp\|f_2\|_\sharp/r^2.
\]

Here r is the **source radius constant** of `8.1:lem-spanning-split`, not the extraction depth r(s). Cauchy's integral on source circles of radii approaching r/(2‖f_i‖♯) gives that factor. Correlation bounds majorize the at most five kinds of local terms by [4(E₀+B₀+C_e+1)+1]e^(−κ″d_j(X)), where κ″=(1−δ)κ≥κ/2; the remainder-family factor g_j^(κ₀)≤1. For ν=k₀−j the spanning geometry gives d_j(X)≥[ρL^ν/(4M)−3]_+, with at most (4LρL^ν/M+3)^4 anchors. The named Balaban 116 (1.26) tree estimate B11a then gives

\[
B_{\rm loc}\le C r^{-2}\|f_1\|_\sharp\|f_2\|_\sharp
\sum_{\nu\ge0}(4L\rho L^\nu/M+3)^4
 e^{-\kappa''[\rho L^\nu/(4M)-3]_+/4}. \tag{W9}
\]

For ρ≥24M, the bracket is at least ρL^ν/(8M), and the anchor factor is at most 5⁴(ρ/M)⁴L^(4+4ν). After extracting e^(−κ″ρ/(32M)), the ν-th ratio is at most

\[
L^{4\nu}e^{-(3/4)\kappa''(L^\nu-1)}
\le\sup_{y\ge3^\nu}y^4e^{-(3/8)\kappa(y-1)}.
\]

**Filled F11.4.** Put a=3κ/8. For y≥max{1,16/a}, the logarithmic derivative of y⁴e^(−ay/2) is 4/y−a/2≤−a/4. Thus y⁴e^(−ay/2) is bounded on [1,∞), and the supremum above is at most C_a e^(−a3^ν/2). Since 3^ν≥ν for ν≥1, this is bounded by a convergent geometric series C_a e^(−aν/2). Its sum depends only on κ. Absorb it in the same C_loc to obtain

\[
B_{\rm loc}\le C_{\rm loc}r^{-2}\|f_1\|_\sharp\|f_2\|_\sharp
(\rho/M)^4L^4e^{-\kappa''\rho/(32M)}. \tag{W10}
\]

**Filled F11.5 (the norm conversion).** In witness-cell units, ‖f‖♯=max{‖f‖∞,40M Lip_(k₀)f}. Since ρ≥C₀≥40M/θ, the witness Lipschitz bound gives 40M Lip_(k₀)f≤‖f‖∞. Therefore ‖f‖♯=‖f‖∞ here. This supplies the step from the sup-norm lower bound for M to the sharp-norm lower bound used in the source; it is not valid for arbitrary profiles at arbitrary radii.

Divide (W10) by M and put C′=C_loc. The relative bound is at most 1/32 if

\[
\kappa''\rho/(32M)\ge
2\log\bar x_s+4\log(\rho/M)+4\log L+
\log\{32C'/ (\vartheta^2r^2c_M)\}. \tag{W11}
\]

The prescribed C₀^loc ensures this at ρ=C_W(s) and C_W(s)≥128M/κ″. The derivative of the left side minus 4log(ρ/M) is κ″/(32M)−4/ρ≥0 above that floor, so (W11) persists for every larger ρ. The existence of a uniform choice is justified with the constant choices below. Thus |R^loc|≤M/32.

### Gaussian-extraction remainder

Use H-GXa, with σ₁=1 as II:71240–71241’s small-window comparison stipulates. The source defines

\[
\begin{split}
D_\square(s)=\max\{&\lceil c_a^{-1}(4p_0\log\log\bar x_s
 +8\log(LC_W(s))+\log C_D)\rceil,\,
\ell+\ell_0r(s)+D_0\},\\
T_1&=\rho^8g_{k_0}^{\sigma_1}\Pi_r,\quad
T_2=\rho^8g_{k_0}^2(1+r),\\
T_3&=\rho^{12}D_\square^4(1+r)p_0(g_{k_0})^4e^{-c_ap_0(g_{k_0})},\\
T_4&=\rho^8p_0(g_{k_0})^4e^{-c_aD_\square},\quad
T_5=L^{-4(r-r_1)},\quad T_6=L^{-8(r-r_1)}p_0(g_{k_0+r})^4.
\end{split}
\]

The hypothesized estimate is

\[
|R^{\rm GX}|\le c_M\mathfrak S\,
\frac{16}{9}\frac{C_a}{c_M}\,4\sum_{j=1}^6T_j. \tag{W12}
\]

The factors 16/9 and 4 are retained: the first bounds N², the second bounds the two perturbed mass ratios together. H-depth ensures k₀+r≤K. The envelope at depths s and s−r, with their lower endpoints ≥e, gives

\[
p_0(g_{k_0})^4,\ p_0(g_{k_0+r})^4
\le A_0^4(\log\bar x_s)^{4p_0},\qquad
p_0(g_{k_0})\ge A_0(\log\underline x_s)^{p_0}.
\]

**Filled F11.6 (ceilings and the one-level shift).** From ρ<LC_W(s),
ceil(log_L(20Lρ))≤ceil(log_L(20LC_W(s)))+1. Hence

\[
r-r_1\ge\lceil(p_0/2+1)\log_L\log\bar x_s\rceil+r_0-1.
\]

Raising L to minus eight times this inequality and multiplying by the displayed p₀⁴ bound gives T₆≤A₀⁴L^(8−8r₀)(log bar x_s)^(−8)≤A₀⁴L^(8−8r₀). Similarly T₅≤L^(4−4r₀). The D_square floor gives e^(−c_aD_square)≤C_D^(-1)(log bar x_s)^(-4p₀)(LC_W)^(-8). Thus T₄≤A₀⁴/C_D since ρ≤LC_W.

The first entry defining D_square is at most

\[
1+c_a^{-1}\{20p_0\log\bar x_s+8\log(LC_0A_0^2)+\log C_D\},
\]

because log(LC_W)=log(LC₀A₀²)+2p₀ log log bar x_s and ceil u≤u+1. Its second entry is O(r(s)), hence also polylogarithmic. None reads K. Each remaining T_j is a polynomial in log bar x_s times, respectively, underline x_s^(−1/2), underline x_s^(−1), or exp{−c_aA₀(log underline x_s)^p₀}. Put y=underline x_s and use bar x_s≤bar x(y). Since y≥e, y⁻¹≤y⁻¹/², and insertion of y² followed by y⁻²≤1 reduces T₃ to the precise second ceiling of the source. Choose r₀,C_D and the tail ceilings so that each of the six terms, including the multiplier (16/9)(C_a/c_M)4, is ≤1/(6·32). Equation (W12) and c_M S≤M give |R^GX|≤M/32.

### Irrelevant remainder

Use H-GXb, retaining its incomplete standing. Its explicit main bound is

\[
|R^{\rm irr}|\le7C_b\rho^{-2}p_0(g_{k_0})^4\mathfrak M+B_{\mathcal E_a}.
\]

Since ρ≥C_W(s)=C₀p₀(bar x_s^(−1/2))² and x≤bar x_s,

\[
\rho^{-2}p_0(g_{k_0})^4
\le C_0^{-2}
\left[p_0(g_{k_0})/p_0(\bar x_s^{-1/2})\right]^4\le C_0^{-2}.
\]

For C₀²≥448C_b the first term is at most M/64. The E_a-type remainder has the same six forms as (W12) by H-GXb. **Filled F11.7:** fix the finite thresholds r₀,C_D and the tail-ceiling polynomials to satisfy both allocations: M/(6·32) for the GX terms and M/(6·64) for these six E_a terms, taking their maximum requirements before fixing γ_W. This specifies the source's phrase “under the same order of constants”; it changes no printed constant, only makes the reserved choice explicit. Summing yields B_Ea≤M/64, so |R^irr|≤M/32. No proof of H-GXb is smuggled into this arithmetic.

### Constant order and final sum

Source: `8.1:prf-constants-ceiling`, II:73214–73489. The following are the exact choice displays; the proof of their feasibility follows.

CA-II:73250–73258:

```latex
\begin{equation}\label{8.1:eq-constants-ceiling-c}
\begin{aligned}
C_0\ge\max\Bigl\{&\frac{40M}{\vartheta},\ 4C_hM,\ 16C_hM,\ \frac{C_hM}{\vartheta},\
\frac{2(C_d+2)}{\vartheta},\
400M\sup_y\frac{\check{R}(y)^4}{p_0(y^{-1/2})^2},\ 3200M,\\
&C_0^{\mathrm{ker}},\ C_0^{\mathrm{loc}},\ C_0^{\mathrm{prof}},\ C_0^{\mathrm{src}},\
(448C_b)^{1/2},\ 24M,\ 2\Bigr\}.
\end{aligned}
\end{equation}
```

CA-II:73275–73289:

```latex
\begin{equation}\label{8.1:eq-constants-ceiling-a}
\begin{aligned}
&(\gamma\text{-}0)\quad X\ge X_0;\\
&(\gamma\text{-}1)\text{--}(\gamma\text{-}3)\quad\text{three ceilings on $g$ of the form
\eqref{8.1:eq-constants-ceiling-3} below,}\\
&\qquad\text{required by the remainder estimates above;}\\
&(\gamma\text{-}4)\quad r(s)\le C\,\frac{p_0(\underline{x}_s^{-1/2})}{\log L}
\quad\text{for every } s;\\
&(\gamma\text{-}5)\quad\text{void};\\
&(\gamma\text{-}6)\quad L^{4\mathfrak{l}(y)}\bigl(M\check{R}(y)\bigr)^4e^{A_0}
\le e^{\frac12 c_q\,p_0(y^{-1/2})}\quad\text{for } y\ge X-c_5;\\
&(\gamma\text{-}7)\quad \mathfrak{d}_W(X-4c_2)\le\tfrac13;\\
&(\gamma\text{-}8)\quad \mu^{\sharp}_Y\le\tfrac12;
\end{aligned}
\end{equation}
```

CA-II:73293–73302:

```latex
\begin{equation}\label{8.1:eq-constants-ceiling-b}
\begin{aligned}
&(\gamma\text{-src})\quad
\sup_{y\ge X-c_5}\mathfrak{F}_{\mathrm{src}}(y)\le\frac{\vartheta^4c_M}{64\,C_{\mathrm{tot}}};\\
&(\gamma\text{-}\varepsilon)\quad
\sup_{y\ge X-c_5}\frac{3\lambda\bigl(\mathfrak{l}(\bar{x}(y))+1\bigr)+2c_2}{y\log 2}
\le 2^{1/p_0}-1;\\
&(C_0\text{-src})\quad C_0\ge C_0^{\mathrm{src}}.
\end{aligned}
\end{equation}
```

CA-II:73329–73333:

```latex
\begin{equation}\label{8.1:eq-constants-ceiling-2}
\mathfrak{F}_{\mathrm{src}}(y):=L^{8(\mathfrak{l}(\bar{x}(y))+1)}\,
\mathfrak{p}_{\mathrm{tot}}\bigl(\bar{x}(y)\bigr)\,\bar{x}(y)^2\,
\exp\bigl(-c_{\mathrm{src}}A_0(\log y)^{p_0}\bigr).
\end{equation}
```

Fix C₀ with every displayed lower bound, then r₀, C_D, k_W, and finally a positive coupling ceiling satisfying all the tail conditions. The normalisation floor X₀ and the constants of H-corr, H-source-use, H-GXa/H-GXb are fixed before these choices. The symbol r_R below is the radius-growth exponent, distinct from both uses of r above.

**Filled F11.8 (existence arguments, not computed thresholds).** Put t=log y≥1. Balaban's radius bound is check R(y)≤C_R t^(r_R)+1, with p₀≥5r_R and p₀>1. For a positive polynomial P and an affine envelope bar x(y), log P(log bar x(y))≤C+D log t and log bar x(y)≤t+C on this domain. Thus every logarithm of an exponential-source majorant is bounded by

\[
A(1+t^{r_R})+B t+D\log t-cA_0t^{p_0}.
\]

The ratios t^(r_R)/t^p₀, t/t^p₀ and log t/t^p₀ tend to zero. Given c>0 choose T so their positive sum is at most (cA₀/2)t^p₀ for all t≥T. The majorant is then ≤exp{−(cA₀/2)t^p₀}, proving a uniform tail bound. Likewise y^(−α)P(log y)=e^(−αt)P(t) tends to zero: each power t^j is bounded against e^(αt/2) by the exponential series, with a strictly higher integer power if needed. This proves the three extraction ceilings and γ-src, including the extra factors bar Θ², y² and all fixed polynomials. It also proves γ-6 and γ-4, whose growing sides have smaller logarithmic powers than p₀.

The profile normalization rate tends to zero by H-kernel's running-normalisation bound; hence γ-7 holds. For γ-ε, the window comparison assumed with the source lemma gives x/x_j≤2 and

\[
\frac{\log x_j}{\log x}
\le1+\frac{3\lambda(\mathfrak l(\bar x(y))+1)+2c_2}{y\log2}
\le2^{1/p_0}.
\]

Consequently (ε_j/ε_(k₀))²=(x/x_j)(log x_j/log x)^(2p₀)≤2·4=8. Its displayed fraction tends to zero by the same logarithmic-over-linear comparison. The window inequality is an input, not a consequence of the last numerical bound. γ-8 belongs only to the unused kept-label alternative and is not needed in the resummed route.

For C₀^loc, divide (W11) at ρ=C₀A₀²t^(2p₀) by t^(2p₀). The terms 2t, log t, and the constants divided by t^(2p₀) are uniformly bounded for t≥1. The remaining dependence is logarithmic in C₀, whereas the left side is linear in C₀. Since log C₀/C₀→0, a single C₀^loc satisfies the inequality and ρ≥128M/κ″ for all t≥1. This also proves the boundedness of sup_y check R(y)^4/p₀(y^(−1/2))² in C₀'s display: its numerator grows at most t^(4r_R), its denominator as t^(2p₀), with 2p₀≥10r_R.

For C₀^src, use ρ≥C₀A₀²t^(2p₀). The log of the prefactor of e^(−varkappaρ/16) is at most A(1+t^(r_R))+Bt+Dlog t+24logρ. At ρ=C_W(s), the final term is 24log C₀+48p₀log t+constant. The same linear-versus-logarithmic choice makes the positive exponent at most varkappaρ/32 and also makes C′_tot e^(−varkappaρ/32)≤θ²c_M/64. For larger ρ, the function ρ²⁴e^(−varkappaρ/32) is decreasing once ρ≥768/varkappa, because its logarithmic derivative is 24/ρ−varkappa/32. Include that lower bound in the *choice* of C₀^src. This fills the uniform-in-ρ step without replacing ρ by C_W inside an increasing polynomial alone.

**Correction C11.2 (monotonicity assertion).** II:73393 asserts eventual monotonic decrease of F_src from growth bounds on check R. A rounded radius function can jump, so those bounds alone do not prove monotonicity. The proof needs only its tail supremum. For every function F→0, sup_(y≥Y)|F(y)|→0 by the definition of limit, and this supremum is non-increasing in Y by inclusion of the indexing sets. Apply this to the explicit majorants just bounded. This keeps exactly the printed supremum ceilings and constants; no monotonicity of the raw rounded function is required. Where “largest” admissible γ is used without endpoint regularity, take any positive γ satisfying all the displayed suprema. The theorem asserts existence of such a ceiling, not maximality. No estimate requires a maximal one.

Thus each actual remainder in (W3) is bounded by M/32, with the large-field terms paid as one group. Including the identically zero shadow slot, the source's final count remains

\[
|S^T_{2;K}-\mathfrak M|\le6\mathfrak M/32
=3\mathfrak M/16<\mathfrak M/4.
\]

Set R_K=(S^T_(2;K)−M)/M, valid because M>0. This proves |R_K|≤1/4≤1/2 and the exact C11 display. H-kernel gives N_(K−s) in [1−d_W(underline x_s),1+d_W(underline x_s)]⊂[2/3,4/3]. Every choice depends only on the printed fixed parameters and antecedent constants, not on K,m,g₀,N_T or positions. The proof is conditional on H-depth and on the use-site suppliers above; it does not close their missing statements.

## Assembly through the reference torus and the limit modes

The two auxiliary statements actually assembled are preserved exactly below. Both have unqualified headings and conditional proofs. Their hypotheses include C9 on the reference torus, C10, H-flow and the stated limit construction.

CA-II:142316–142371:

```latex
\begin{corollary}[The volume-transfer coupling ceiling and depth floor]
\label{8.22:cor-transfer-depth-floor}
Work in the setting of clause~(iv) of Theorem~\ref{3.1:thm-main}: gauge group $\mathrm{SU}(N)$ with $N=2$,
inside the regime of clause~(iii), with $\vartheta$ and the constants $k_W$, $c_{\mathcal{K}}$, $C_{\mathcal{K}}$ of
that clause. Let $\gamma_W^{\mathrm{VT}}$ be the coupling ceiling
of~\eqref{8.22:eq-expansion-consistency-a} and $s_T(g)$ the depth floor
of~\eqref{8.22:eq-expansion-consistency-b} (Definition~\ref{8.22:def-expansion-consistency}). Assume the
following two statements.
\begin{itemize}
\item[(a)] The two-point witness theorem on a single torus below the horizon, that is, for couplings $g$
with $m_{\mathbb{T}}(g_-(g))\le m_V(g)$, where $m_V(g)$ is the horizon exponent of Definition~\ref{8.18:def-volume-horizon},
in the following form. For every $g\le\gamma_W^{\mathbb{T}}$ such that $m':=m_{\mathbb{T}}(g_-(g))$ satisfies
$m'\le m_V(g)$ (here and below $m'$ denotes a torus exponent, as in
Corollary~\ref{8.22:cor-short-distance-volume}), the volume depth $s_{\mathrm{vol}}(g,m')$ of that theorem is
zero, and on the torus $\mathbb{T}_{m'}$, for every $g_0\in\,]0,g_-(g)]$ with $K=K(g_0,g)$, every $\mathsf{d}$
with $s_W(g)\le s(\mathsf{d})=:s$ and $K-s\ge k_W$, and every $(f_1,f_2)\in\mathfrak{T}(\mathsf{d};\vartheta)$ on
$\mathbb{T}_{m'}$,
\begin{equation}\label{8.22:eq-transfer-depth-floor-1}
S^T_{2;K,m'}(f_1,f_2)
=\zeta_{K-s}'^{\,2}\,b_0\,g_{K-s}^4\,\mathcal{K}_s^{(m')}(f_1,f_2)\,(1+R'),\qquad |R'|\le\tfrac14,
\end{equation}
where $\mathcal{K}_s^{(m')}$ is the kernel $\mathcal{K}_s$ read on the bare lattice of $\mathbb{T}_{m'}$,
$\zeta'_{K-s}\in[\frac23,\frac43]$, and
\begin{equation}\label{8.22:eq-transfer-depth-floor-8}
c_{\mathcal{K}}\|f_1\|_\infty\|f_2\|_\infty\le\mathcal{K}_s^{(m')}(f_1,f_2)\le
C_{\mathcal{K}}\|f_1\|_\infty\|f_2\|_\infty .
\end{equation}
\item[(b)] Short-distance volume independence of the two-point function,
Corollary~\ref{8.22:cor-short-distance-volume}.
\end{itemize}
Then for every $g\le\gamma_W^{\mathrm{VT}}$, every $g_0\in\,]0,g_-(g)]$ with $K=K(g_0,g)$, every
$m\ge m_{\mathbb{T}}(g_-(g))$, every $\mathsf{d}$ with $\max\{s_W(g),s_T(g)\}\le s(\mathsf{d})=:s$ and
$K-s\ge k_W$, and every $(f_1,f_2)\in\mathfrak{T}(\mathsf{d};\vartheta)$ on $\mathbb{T}_m$,
\begin{equation}\label{8.22:eq-transfer-depth-floor-a}
S^T_{2;K,m}(f_1,f_2)=\zeta_{K-s}'^{\,2}\,b_0\,g_{K-s}^4\,\mathcal{K}_s^{\star}(f_1,f_2)\,(1+R_K),
\qquad |R_K|\le\tfrac12,
\end{equation}
where $\mathcal{K}_s^{\star}$ is $\mathcal{K}_s$ read on the reference torus $\mathbb{T}_{m_{\star}(g)}$,
$\zeta'_{K-s}\in[\frac23,\frac43]$ as in~(a), and
$\mathcal{K}_s^{\star}$ obeys the kernel bounds~\eqref{8.22:eq-transfer-depth-floor-8} with
$\mathcal{K}_s^{\star}$ in place of $\mathcal{K}_s^{(m')}$. Hence, uniformly in $K$, $g_0$, $m$ and the position,
\begin{equation}\label{8.22:eq-transfer-depth-floor-2}
\tfrac29\,b_0\,g_{K-s}^4\,\mathcal{K}_s^{\star}(f_1,f_2)\le S^T_{2;K,m}(f_1,f_2)
\le\tfrac83\,b_0\,g_{K-s}^4\,\mathcal{K}_s^{\star}(f_1,f_2),
\end{equation}
and the coupling form of the two-point law, the last display of clause~(iv) of
Theorem~\ref{3.1:thm-main}, holds:
\begin{equation}\label{8.22:eq-transfer-depth-floor-3}
\begin{split}
\tfrac29\,b_0\,c_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty\,\bigl(g^{-2}+B^{\sharp}(s+1)\bigr)^{-2}
&\le S^T_{2;K,m}(f_1,f_2)\\
&\le\tfrac83\,b_0\,C_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty\,
\bigl(g^{-2}+\lambda^{\sharp}s-c_5\bigr)^{-2}.
\end{split}
\end{equation}
\end{corollary}
```

CA-II:142607–142632:

```latex
\begin{corollary}[The kernel read on the reference torus]\label{8.22:cor-reference-torus-kernel}
Let $g$, $\vartheta$ and the constants $b_0$, $c_{\mathcal{K}}$, $C_{\mathcal{K}}$, $B^{\sharp}$,
$\lambda^{\sharp}$, $c_5$, $k_W$ be as in Corollary~\ref{8.22:cor-transfer-depth-floor}; in
particular $N=2$ and $g\le\gamma_W^{\mathrm{VT}}$.
Here $s_T(g)$ is the depth floor
of \eqref{8.22:eq-expansion-consistency-b}, and $s_W(g)$ is the depth floor of the two-point
witness theorem. Let $S^T_{n;\infty}$ be any limit in the sense of clause
(ii-$\mathbb{R}^4$) of Theorem~\ref{3.1:thm-main} at the reference coupling $g$, taken along a
sequence $(g_0^{(j)},K_j,m_j)$ with $g_0^{(j)}\in\,]0,g_-(g)]$, $K_j=K(g_0^{(j)},g)$,
$K_j\to\infty$ and $m_j\to\infty$. Let $\mathsf{d}$ satisfy
\begin{equation*}
\max\{s_W(g),s_T(g)\}\le s(\mathsf{d})=:s,
\end{equation*}
that is, let $\mathsf{d}$ lie below the separation ceilings corresponding to these two depth floors.
Then for every pair $(f_1,f_2)$ of $C^1$ functions on $\mathbb{R}^4$ belonging to
$\mathfrak{T}(\mathsf{d};\vartheta)$,
\begin{equation}\label{8.22:eq-reference-torus-kernel-1}
\begin{split}
\tfrac{2}{9}\,b_0\,c_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty
\bigl(g^{-2}+B^{\sharp}(s+1)\bigr)^{-2}
&\le S^T_{2;\infty}(f_1,f_2)\\
&\le \tfrac{8}{3}\,b_0\,C_{\mathcal{K}}\,\|f_1\|_\infty\|f_2\|_\infty
\bigl(g^{-2}+\lambda^{\sharp}s-c_5\bigr)^{-2}.
\end{split}
\end{equation}
\end{corollary}
```

### Signed translates: the account's transfer step, written out

The argument is `8.22:lem-signed-translates`, II:141854–141974, and the two-source part of `8.22:cor-short-distance-volume`, II:141994–142100. It supplies the missing gain between C10's fixed-ball estimate and the witness scale. Let D(F₁,F₂)=S^T_(2;K,m)(F₁,F₂)−S^T_(2;K,m′)(F₁,F₂). Periodise compactly supported profiles when defining D on all of R⁴. Periodisation is linear and commutes with translations; on the balls used below it agrees with transport into either torus. Thus D is a real bilinear form, invariant under simultaneous εZ⁴ translations, with |D(F₁,F₂)|≤C_VT‖F₁‖♯‖F₂‖♯ on a ball of radius R.

Suppose ε≤r≤R/8 and both profiles are supported in B(y,r). Put r′=ε ceil(r/ε), so r≤r′<2r and 4r′Z⁴⊂εZ⁴. Take

\[
\Gamma=\{\tau\in4r'\mathbb Z^4:|\tau|_\infty\le R/4\}.
\]

Its size is (2 floor(R/(16r′))+1)⁴≥(R/(32r))⁴, because 2floor a+1≥a for all a≥0. The translated balls are separated by at least 2r, and lie in B(y,R): |τ|≤2|τ|∞≤R/2 and R/2+r≤R. For signs σ_τ=±1 put F_i^σ=Σ_τ σ_τ f_i(·−τ).

Each f_i vanishes on its ball boundary. Consequently the sup norm of F_i^σ equals that of f_i. For points in different balls, follow the segment between them to its first exit and last entry. The sum of these two within-ball distances is at most the full segment length. The absolute difference of the two values is bounded by Lip(f_i) times this sum. The same estimate holds if one point lies outside all balls; within one ball it is the original Lipschitz inequality. Thus Lip(F_i^σ)≤Lip(f_i), and therefore ‖F_i^σ‖♯≤‖f_i‖♯. This inequality suffices; the source proves equality.

Average algebraically over all sign assignments. Off-diagonal factors σ_τσ_τ′ cancel in pairs by flipping σ_τ, whereas σ_τ²=1. Hence

\[
2^{-|\Gamma|}\sum_\sigma D(F_1^\sigma,F_2^\sigma)
=\sum_\tau D(f_1(\cdot-\tau),f_2(\cdot-\tau))
=|\Gamma|D(f_1,f_2).
\]

This is a hand identity for arbitrary finite Γ, not machine enumeration. Apply C10 to each signed array and divide by |Γ|. With c_Γ=32⁻⁴,

\[
|D(f_1,f_2)|\le C_{\rm VT}c_\Gamma^{-1}(r/R)^4
\|f_1\|_\sharp\|f_2\|_\sharp.
\]

For R=1,r=5d, ε≤d≤1/40 and Lip f_i≤‖f_i‖∞/(θd), each sharp norm is ≤40M‖f_i‖∞/(θd). Thus

\[
|D(f_1,f_2)|\le C_T(g)d^2\|f_1\|_\infty\|f_2\|_\infty,
\qquad C_T(g)=5^4c_\Gamma^{-1}(40M/\vartheta)^2C_{\rm VT}. \tag{V1}
\]

This is the source's exact two-source constant. No three-source theorem is inferred from C10's two-source statement.

### Coupling ceiling, depth floor, and the 1/2 relative bound

The constants are `8.22:def-expansion-consistency`, II:142164–142314. At R=1, ℓ<32L≤L¹¹M since L≥3,M≥1. Hence m_star(g)=m_T(g_−(g)). The reference horizon grows as g⁻²/(3λ), whereas m_star≤12+log_L M+r_pr log_L log(g⁻²+B^♯). Therefore m_star≤m_V for all sufficiently small positive g: divide the latter logarithmic bound by g⁻² and use log t/t→0. This proves existence of a nonempty interval of allowed couplings.

**Endpoint qualification C-V1.** The definition of γ_star^V is a supremum of such intervals. Downward closure alone, the argument printed at II:142221–142226, does not prove membership of its supremum. The implication below keeps the named hypothesis m_star(g)≤m_V(g) at g=γ_star^V; alternatively impose g<γ_star^V. Indeed, for g<sup A there is η∈A with g<η, and then the defining universal inequality applies. This keeps the printed constant and route, and flags the unproved endpoint rather than changing it silently.

The source defines s_T as the least **tail** floor such that for every integer s≥s_T,

\[
LC_W(s)L^{-s}\le1/40,\qquad
C_T(g)L^2C_W(s)^2L^{-2s}\le
\tfrac19b_0c_{\mathcal K}\bar x_s^{-2}. \tag{V2}
\]

For fixed g, C_W is a power of log bar x_s and bar x_s is affine in s. Both left sides, after multiplication by bar x_s² in the second, tend to zero. One hand proof is to take logarithms: their positive terms are O(log(s+2)), their negative terms are −s log L or −2s log L. Their ratio to s tends to −log L or −2log L. They therefore satisfy the inequalities on an entire tail; no monotonicity between adjacent integers is required (filled FV.1). The least tail exists by well-ordering, and its defining quantities are independent of K,g₀,m and position. This is the property needed below; no numerical floor is used.

Now fix the data of `8.22:cor-transfer-depth-floor`, retaining H-depth and the endpoint qualification just stated. Since s_T≥1, minimality of s(d) gives

\[
C_W(s)L^{-s}\le d<LC_W(s)L^{-s}\le1/40.
\]

Also K−s≥k_W≥1 and C_W≥1 imply L⁻ᴷ<d. Choose lifts of the two supporting balls whose centres are at distance at most 8d: points attaining their support distance are within d of the respective centres and at distance ≤6d from each other. Their midpoint ball of radius 5d contains both supports. As 5d<1<L^(m′)/2, it lifts and transports to the reference torus without changing any local test condition. Two lifts differ by 2L^mZ⁴⊂2L^(m′)Z⁴, so the reference pair is unambiguous (filled FV.2).

On m′=m_star≤m_V, C9(a) gives

\[
S^T_{2;K,m'}=\mathfrak M^\star(1+R'),\quad |R'|\le1/4,
\quad\mathfrak M^\star=\zeta_{K-s}'^{\,2}b_0g_{K-s}^4\mathcal K_s^\star.
\]

Its lower bound is (4/9)b₀c_K bar x_s⁻²‖f₁‖∞‖f₂‖∞. Apply (V1), then d<LC_W L⁻ˢ, then (V2). The transfer cost is at most (1/9)b₀c_K bar x_s⁻²‖f₁‖∞‖f₂‖∞≤M_star/4. Thus

\[
R_K=R'+(S^T_{2;K,m}-S^T_{2;K,m'})/\mathfrak M^\star
\]

has |R_K|≤1/4+1/4=1/2. This proves the transferred display with **the reference kernel** K_star. Multiplication by ζ′²∈[4/9,16/9] and 1+R_K∈[1/2,3/2], followed by the positive flow/kernel bounds, proves the corollary's two sandwiches with constants 2/9 and 8/3. Every threshold now depends on g and fixed parameters, not m. This is the account's way to remove s_vol from the all-volume conclusion; dropping that floor directly from C9 would not be valid.

The optional comparison K_s^(m)/K_star≈1 is explicitly unproved at II:142535–142546. It is not used. Equal two-sided kernel bounds alone do not authorize replacing K_star by K_s^(m) in a relative-error display. The coupling sandwich uses only the shared bounds and remains valid as printed. No claim in this port uses the optional kernel replacement.

### Each limit mode, without exchanging limits

For B8 (torus subsequences) fix m and the pair. For B9 (tuned torus family) use only approximating first-passage sequences admitted by that clause, with its uniqueness/tuning inputs retained. For B11 (joint R⁴ limits) fix g,d and a compactly supported C¹ pair before taking its defining sequence (K_j,m_j)→(∞,∞). Eventually m_j≥m_star, K_j−s≥k_W and the growing torus contains the fixed supports without wrapping. The transferred coupling bounds then put every sufficiently late tested covariance in the same closed interval

\[
I=\left[
\tfrac29b_0c_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty\bar x_s^{-2},
\tfrac83b_0C_{\mathcal K}\|f_1\|_\infty\|f_2\|_\infty\underline x_s^{-2}
\right].
\]

The specified limit of that covariance lies in I by F9.1. This is the entire proof of `8.22:cor-reference-torus-kernel`, II:142635–142713. It neither takes a separate limit of g_(K−s) nor assumes a thermodynamic limit at fixed cutoff. Along a subsequence with a reference-torus limit, (V1) also passes to the limit with the same C_T(g)d² bound, exactly `8.22:rem-infinite-volume-law`, II:142760 onward. A further identification of that reference limit as a tuned member uses its separate (v-c)(2) hypothesis.

The limiting sandwich is strictly positive. For reflected test pairs, the limiting reflection-positive form gives a nonzero centred vector orthogonal to the vacuum as in C9(d). Alternatively the account uses its curvature-Hilbert-space dichotomy; that dichotomy would be a separate named input, not a consequence of positivity of one arbitrary unreflected pair. The logarithmic dilation argument F9.3 gives the same slow decrease and effective-coupling conclusions in the admitted limit modes. The Maxwell comparison retains its free-kernel hypothesis and the zero-charge correction. H-CK remains named wherever the account invokes the continuum kernel; its absence has not been cured by the closed-interval argument.

This proves the assembly's conditional consequences. It proves no clustering, uniqueness of the R⁴ limit, vacuum uniqueness, full O(4) invariance, mass gap, non-Gaussianity, or Wightman reconstruction. Those are not corollaries of this two-point sandwich.

## Result

**Kind:** port of the account's conditional proofs, with explicitly filled steps and narrow corrections. Research text only. No T0 closure, audit status or retained status is granted. **This text is not yet checked by another model.**

| Statement | Result in this file |
|---|---|
| C9, `8.18:thm-torus-witness`, II:144922–145115 | Exact statement and full conditional case-split proof, including its four fixed-torus consequences. The separation-supremum prose has the endpoint correction C9.1. |
| C10, `8.22:thm-volume-transfer`, II:141540–141852 | Exact statement and full proof from its (a)–(f), with the original C_VT and Q_star. |
| C11, `8.1:thm-two-point-witness`, II:71279–71367, proof parts through II:73489 | Exact statement and the full resummed-history deduction from the account's use-site hypotheses. H-depth, H-source-use, H-GXa/H-GXb and H-add remain explicit supplier obligations. This does **not** establish that the printed antecedent labels alone supply all these forms. |
| Reference-volume assembly, `8.22:cor-transfer-depth-floor`, II:142316 onward | Exact statement, signed-translate argument and transfer proof with the reference kernel. Endpoint admission C-V1 remains explicit. |
| Limit transfer, `8.22:cor-reference-torus-kernel`, II:142607 onward | Exact statement and fixed-interval proof for joint limits; the same passage is specified for B8/B9 torus modes. |
| C5, `8.2:prop-gaussian-extraction`, II:77279–77433 | **Not ported in this round.** It remains H-GX, including C3/C4 and the q≥21p₀+1 floor. |

Every filled step is indexed here:

- F9.1: closed-interval passage to the tested limit; F9.2: simultaneous kernel/coupling subsequence; F9.3: witness-depth logarithm and slower-than-power bound; F9.4: Maxwell scaling comparison under H-free-torus.
- F10.1: entire finite-volume generating function; F10.2: Schwarz–Cauchy estimate with the exact constant; F10.3: mixed logarithmic derivative equals covariance.
- F11.1: exact total-covariance identity; F11.2: preserve both source amplitudes in the large-field bounds; F11.3: finite majorant budgets with the c_M normalization; F11.4: hand summation of the spanning tail; F11.5: sharp norm equals sup norm under the room floor; F11.6: ceiling/index shift and extraction tails; F11.7: simultaneous 1/32 and 1/64 allocations; F11.8: existence of uniform constants by scalar growth bounds.
- FV.1: existence of a tail depth floor; FV.2: lifting and transporting the witness pair into the reference torus.

Corrections and unresolved qualifications are distinct:

1. **C9.1, correction:** for a positive integer depth floor, the separation threshold is strict. The operative displayed depth condition is unchanged.
2. **C9.2, correction:** zero Maxwell charge gives zero covariance; exclude it by positivity, then use the nonzero-charge scaling argument.
3. **C11.1, correction:** distinguish signed remainders from their positive majorants, and place live pairings in both R^L and R^(Ψ,live) as the exact decomposition requires.
4. **C11.2, correction:** tail suprema, not unproved monotonicity of rounded-radius expressions, justify uniform ceilings. Any admissible positive ceiling suffices for the existential theorem.
5. **H-depth, open supplier issue:** the first-admissible integer was not shown to be a tail floor in the cited proof. Its three admission inequalities are retained explicitly. Replacing the definition by a tail minimum is a proposed repair, not an unnoticed change to s_W.
6. **H-source-use and H-GXa/H-GXb, open supplier issues:** final labels do not literally print all earlier use-site forms. Those forms remain hypotheses with their stated incomplete/outstanding standing.
7. **C-V1, endpoint qualification:** at the supremum coupling require m_star≤m_V explicitly; the proof works without that extra endpoint question for g strictly below the printed supremum. No claim that the endpoint fails has been made.

The carried hypotheses are **all** H-C2, H-C3a/b, H-C4a/b/c, H-C6a/b/c, H-C7a/b/c/d, H-C8a/b, H-GX/GX1/GXa/GXb, H-flow, H-corr, H-kernel, H-healed, H-young, H-age, H-closure, H-positive, H-limit, H-VT(a)–(f), H-source-use, H-depth, H-add, H-CK, H-free-torus, H-OS-transfer, and B01–B24 (including separately named subitems). Each retains its ledger standing and its own domain assumptions. The available P1/P3/P4/P5/P6/P7 and refereed lsc/mu/lrb/oc/ui/pda are cited only with the owner's supplied standing. Uniform-old-rarity and the kept-label flat-shell route are not required by the resummed deduction; C1 is not a replacement for the unwritten continuum kernel.

**Current recovery checkpoint.** The pinned source identities are at the top of this file. C9–C11 and their conditional transfer assembly are saved. C5 statement II:77279–77433 and the beginning of its proof through II:77518 were inspected; the remainder of its proof, II:77519–77859, has not been ported. Before continuing, locate its exact proof endpoint and read that range in bounded pieces. Its one-point and one-step suppliers are unwritten-statement remarks at II:76772 and II:76125, so preserve those use-site hypotheses. The first next task is C5's own transported-covariance proof, not a replacement derivation. Then obtain the still-required other-model check of this note and resolve H-depth and the use-site supplier mappings if the lead wants the exact printed implication without extra admission hypotheses.

Only `library/port/p9-witness.md` was changed. No editable prompt file, GOAL, FINISH, skill, ledger, audit file or platform instruction was changed. Text-location and verbatim-copy checks are bookkeeping only; no program was used to discharge a proof obligation.
