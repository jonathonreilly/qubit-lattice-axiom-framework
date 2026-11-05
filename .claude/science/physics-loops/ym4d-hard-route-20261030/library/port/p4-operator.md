# P4 — Operator and localised-independence ports

Provenance: Port of the complete account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, source revision 31a47c543775; Balaban is credited at each imported theorem. Repository baseline requested: 11083d13b. Research text only; no audit or retained status; not yet checked by another model.

## Scope and source conventions

CA-I means `theorem_0_complete_account_raw_I.tex` at `31a47c543775`, fetched as `/tmp/sa_ca_I.tex`. Line references below refer to that revision. SA means `YM4_sketch_500.tex` at the same revision. All mathematical constructions and the proof routes below are credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Published inputs are credited to Tadeusz Balaban. This port does not rebuild them.

The source convention at CA-I:27–56 gives an unmarked heading the status “proved in full”; this includes implications from named statements. All three requested headings are unmarked. Their antecedents retain their separate standing below. “Proved in CA” reports the source's declaration, not an independent verification here. Exact statement blocks retain the source's LaTeX labels and cross-references. A cross-reference is not a discharge of its hypothesis.

Only this file is edited. The repository is at `11083d13b2b23ff21f7e24c9b7750f38a43aefc2`. `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent at this revision. The task-specific GOAL and FINISH rules apply. P1, P3 and the frozen minimizer note are not redone.

## Current checkpoint

Port text complete for the three conditional implications, with the A4-C3 exactness-scope correction; see Result for the filled steps, corrections and retained hypotheses. Source identities and outstanding application obligations are recorded in Source navigation and recovery. No numerical or computer-assisted proof step is used. Independent check remains pending.

## A4 — Operator bounds at free current

Source: CA-I:19578–19743. Status: unmarked statement, declared proved in CA; conditional on the inputs recorded below.

### Exact source statement

```latex
\begin{theorem}[Operator bounds at free current]\label{4.5:thm-operator-bounds}
Work in the setting of this section, with the reading conventions and with the constants chosen in the order of
Remark~\ref{4.5:rem-constants-order}. Assume the following statements:
\begin{itemize}
\item the bounds and the generalised random-walk expansion of the constrained covariance
inverse $\mathsf{q}_0=(QG_0Q^{*})^{-1}$ (Remark~\ref{4.5:rem-covariance-inverse-walks}),
which is stated in \cite[\S3]{B-CMP99b} without proof;
\item the analyticity and uniformity of the derivative bounds for the averaging maps
(Remark~\ref{4.5:rem-averaging-analyticity}), which is stated in \cite[p.~43]{B-CMP98}
without proof;
\item the corollary that furnishes the constant $C_H$ of
Remark~\ref{4.5:rem-constants-order}, together with the two auxiliary statements
accompanying it;
\item the regularity theorem for the glued window background $\mathbf{U}^{\mathrm{gl}}$;
\item the identity $U_j(\square_0,M^{\cdot}U_{k+1})=U_{k+1}$ at level $j$, the level-$j$
counterpart of Lemma~\ref{4.5:lem-window-minimiser};
\item the bound on the Baker--Campbell--Hausdorff remainder that controls the gauge maps
$g$ and $g'$ of the frames, whose statement also stands among the displays
\eqref{4.5:eq-literal-frame-b};
\end{itemize}
and, for the literal-frame variant of \textup{(N-b)} only, the small curvature of block
averages at near-unitary complex data (Remark~\ref{4.5:rem-block-curvature-complex}), which
is stated in \cite[(3.26)]{B-CMP109} without proof. Then the following hold.

\smallskip
\noindent\textup{(O)} \emph{Operators at free current.} Let $(\mathbf{U},\mathbf{J})$
satisfy the conditions (i)--(iii) of \cite{B-CMP109} at any constants
$\alpha_0',\alpha_1'$ under the ceilings for which the pairs with (i)--(iii) lie in the class
$\mathfrak{S}$ of \eqref{4.5:eq-admissible-pairs-a} (in \cite{B-CMP109} these are constants
that are sufficiently small but much larger than $\alpha_0,\alpha_1$). Then the operators
\begin{equation*}
G,\quad G_1,\quad H,\quad H_1,\quad H_0,\quad \tilde G,\quad (QGQ^{*})^{-1},\quad
(QG_1Q^{*})^{-1},\quad \Delta^{(2)},
\end{equation*}
with $J_{k+1}$ replaced by $\mathbf{J}$ in all propagators and operators, exist as the
operators at free current of Lemma~\ref{4.5:lem-free-current-operators}, are analytic,
obey the bounds of \cite[Theorem~3.3]{B-CMP99b} listed in
\eqref{4.5:eq-free-current-operators-a} (those with sup-norm data and those involving
$\nabla^{*}$, but not the bound involving the Laplacian, which is kept for $G_0$, $H_0$ only)
and the bounds \cite[(3.132), (3.133), (3.137)]{B-CMP99b}, have the generalised random-walk
expansions of \eqref{4.5:eq-free-current-operators-a}, and their versions localised in the
decoupling parameters $s$ as in clause (K10) of Theorem~\ref{4.5:thm-chart-existence} obey
\cite[(1.11)]{B-CMP116} in these norms.

\smallskip
\noindent\textup{(F)} \emph{Far terms.} Let $X\in\mathbf{D}_j$ meet the complement of
$\tilde\square^{2}$, and let $(\mathbf{U},\mathbf{J})\in\mathcal{U}_X$, where
$\mathcal{U}_X$ denotes the set \cite[(3.16)]{B-CMP109},
\begin{equation*}
\begin{split}
\mathcal{U}_X:=U^{c}_{j}\bigl(X,\tfrac12\alpha_0,\tfrac12\alpha_1,\alpha_0\bigr)
\cap\bigl\{(\mathbf{U},\mathbf{J}):\ &\mathbf{U},\mathbf{J}\text{ satisfy (i)--(iii) for }
j=k+1\\
&\text{with the constants }(1+\beta)\alpha_0,\ (1+\beta)\alpha_1,\ \alpha_0\bigr\}.
\end{split}
\end{equation*}
Membership in $\mathcal{U}_X$ is understood representative-wise, in the sense of
the corresponding display: one representative modulo $G$-valued gauge maps
satisfies both members of the intersection, and the orbit is recovered by \textup{(F4)}
below. Put $J:=\mathfrak{s}\mathbf{J}$ with $\mathfrak{s}=(L^{j-1}\eta)^{3}\le L^{-3}$.
Take the chart of Theorem~\ref{4.5:thm-chart-existence} at level $j$, in units of $\xi$ and
with the trivial sequence of domains, and let $B(t)$ and $v:=\partial_{t_\square}B(t)$ be
as in \cite[(3.6)--(3.8)]{B-CMP109}, taken as functions of $H_k:=\mathcal{H}^{J}$ at level
$k$. Replace the functional of \cite[(3.13)]{B-CMP109} by
\begin{equation*}
\Phi^{\mathbb{K}}:=\mathbf{E}^{(j)}\bigl(X,\ e^{i\xi A(t_\square)}\mathbf{U},\
J+\mathfrak{J}(B(t),t_\square)\bigr),
\end{equation*}
where $A(t_\square)$ is the field of \cite[(3.13)]{B-CMP109}, now formed from
$\mathcal{H}^{J}$, and $\mathfrak{J}(B(t),t_\square)$ is the current correction
$\mathfrak{J}$ of the chart formed in the same way;
replace the conditions of \cite[(3.14)]{B-CMP109} by
$|A|,|P_1A|,|\nabla_{\mathbf{U}}A|,|\mathfrak{J}|<\alpha_2$ on $X$, and define the radius
$r$ by
\begin{equation*}
r\cdot\max\bigl\{|\delta\mathcal{H}[v]|_X,\ |P_1\delta\mathcal{H}[v]|_X,\
|\nabla\delta\mathcal{H}[v]|_X,\ |\delta\mathfrak{J}[v]|_X\bigr\}=\tfrac13\alpha_2 ,
\end{equation*}
where $\delta\mathcal{H}[v]$, $\delta\mathfrak{J}[v]$ are the first variations of clause (K4)
of Theorem~\ref{4.5:thm-chart-existence}, displayed in
\eqref{4.5:eq-chart-variation-decay-a}.
If $\varepsilon_1$ is sufficiently small, then:
\begin{itemize}
\item[(F1)] $\Phi^{\mathbb{K}}$ is analytic on $\mathcal{U}_X\times\{|t_\square|\le r\}$,
and $|\Phi^{\mathbb{K}}|\le E_0e^{-\kappa d_j(X)}$.
\item[(F2)] (The counterpart of \cite[(3.9)]{B-CMP109}.) On $X$ each of the four quantities
in the definition of $r$ is bounded by
\begin{equation*}
C L^{j}\eta\, e^{-c_{*}\delta_0\operatorname{dist}^{(\xi)}(X,\operatorname{supp}\zeta_\square)}
\,|\zeta_\square H_k(B')| ,
\end{equation*}
whence \cite[(3.17)]{B-CMP109} holds at the rate $c_{*}\delta_0$.
\item[(F3)] At $(\mathbf{U},\mathbf{J})=(U_{k+1},J_{k+1})$ one has
$\Phi^{\mathbb{K}}=\mathbf{E}^{(j)}(X,e^{i\xi A(t_\square)}U_{k+1})$, which is the composite
function of \cite[(3.7)]{B-CMP109}.
\item[(F4)] (The invariance \cite[(1.19)]{B-CMP109}.) $\Phi^{\mathbb{K}}$ is invariant under
$(\mathbf{U},\mathbf{J},B)\mapsto(\mathbf{U}^{u},R(u)\mathbf{J},R(\bar u)B)$ for every
$G$-valued $u$ and for every $u=u'u_G$ with $u_G$ $G$-valued and
$\|\mathrm{Ad}_{u'}^{\pm1}\|\le\mathfrak{K}$, as in clause (K5) of
Theorem~\ref{4.5:thm-chart-existence}. This is the scope of the restriction statement for
complexified gauge maps near $G$-valued ones (maps $v=v'v_G$ with $|v'-1|$ small), and it is
the scope used in \cite[(3.29)]{B-CMP109}, namely $G^{c}$-valued transformations in a
sufficiently small neighbourhood of $G$-valued transformations. The invariance is used
only within this scope. The
statements that use \textup{(F)} --- \cite[(3.17)]{B-CMP109}, the inclusion of analyticity
spaces of \cite{B-CMP116}, and the real integrals of the step --- use representatives.
\item[(F5)] The same statements hold for the functions localised in the decoupling
parameters, with constants multiplied by $e^{c_{\mathbb{K}}\kappa_1}$.
\item[(F6)] The same statements hold for the two further far terms that \cite{B-CMP109}
treats in exactly the same way --- the second term of \cite[(3.21)]{B-CMP109} and the
bracket removed after \cite[(3.22)]{B-CMP109} --- for $X\subset\tilde\square^{2}$ with
$\operatorname{dist}^{(\xi)}(X,\operatorname{supp}(1-\tilde\zeta_\square))\ge
M(L^{j}\eta)^{-1}$; for these terms the chart is the window chart $H_j(\square_0,\cdot)$ on
the tower $\{\Omega_n\}:=\{\square_n\}_{n\le j}$.
\end{itemize}

\smallskip
\noindent\textup{(N)} \emph{Near terms.} Let $(\mathbf{U},\mathbf{J})\in\mathfrak{U}$, the
space of Proposition~\ref{4.5:prop-glued-window}.
\begin{itemize}
\item[(N-a)] $H_k(B')$ at the background $(\mathbf{U}^{\mathrm{gl}},\mathbf{J})$ is defined
and analytic in $(\mathbf{U},\mathbf{J},B')$ for $|B'|<c_9/8$, with
$N_\beta(H_k(B'))\le 16C^{K}_{9}|B'|$; \cite[(1.21)]{B-CMP116} holds for its version
localised in the decoupling parameters, with the factor $e^{c_{\mathbb{K}}\kappa_1}$; and it
depends on $(\mathbf{U},\mathbf{J})$ only through their restrictions to
$Y_0\cup\square_0$.
\item[(N-b)] There is a map $\mathfrak{w}=\mathfrak{w}[\mathbf{U}{\upharpoonright}\square_0^{+}]$
on the sites of $\square_0^{+}$, an explicitly given analytic function of the restriction of
$\mathbf{U}$ to $\square_0^{+}$, with $\|\mathrm{Ad}_{\mathfrak{w}}^{\pm1}\|\le2$, such that
on the bonds of $\square_0$ the background is $(\mathbf{U}^{\mathrm{gl}})^{\mathfrak{w}}
=e^{i\eta\mathcal{A}}$. Here $\mathfrak{w}:=w'$ is the frame map of
Lemma~\ref{4.5:lem-fine-axial-frame} and $\mathfrak{b}:=B_b^{f}(1+2\beta)$; in the
literal-frame variant, $\mathfrak{w}:=w=g^{-1}\circ\tilde v$ is the frame map of
Lemma~\ref{4.5:lem-literal-frame}, which is $u_{k+1}^{-1}v^{-1}$ in the notation of
\cite[(3.26)--(3.27)]{B-CMP109}, and $\mathfrak{b}:=B_b(1+2\beta)$. The data of the window
in this frame are $e^{iB}$ with $\sup|B|\le\frac12C_1\bar\varepsilon_1$ at base one. Put
\begin{equation*}
\mathbf{A}:=(t\tilde\zeta_\square+t_\square\zeta_\square)\cdot R(\mathfrak{w})H_k(B'),
\qquad
\hat{\mathbf{A}}:=\frac{1}{i\eta}\log\bigl(e^{i\eta\mathbf{A}}e^{i\eta\mathcal{A}}\bigr);
\end{equation*}
$\mathbf{A}$ is the field $(t\tilde\zeta_\square+t_\square\zeta_\square)\mathbf{H}_k(B')$
of \cite[(3.28)]{B-CMP109} in which the variables $\mathbf{J}$, $B$ are replaced by
$R(u_{k+1}^{-1})R(v^{-1})\mathbf{J}$, $R(u_{k+1}^{-1})R(v^{-1})B$, and $\hat{\mathbf{A}}$ is
the logarithm of \cite[(3.30)]{B-CMP109}. Then
\begin{equation}\label{4.5:eq-operator-bounds-a}
\begin{gathered}
|\mathcal{A}|,\ |\nabla^{\eta}\mathcal{A}|,\ \|\mathcal{A}\|_{1,\beta}\le
\mathfrak{b}M\alpha_0\quad\text{on }\tilde\square^{4},\\
|\mathbf{A}|,\ |\nabla^{\eta}\mathbf{A}|,\ \|\mathbf{A}\|_{1,\beta}<\alpha_2
\quad\text{on }\square_0,\\
|\hat{\mathbf{A}}|,\ |\nabla^{\eta}\hat{\mathbf{A}}|,\ \|\hat{\mathbf{A}}\|_{1,\beta}
<2(\alpha_2+\mathfrak{b}M\alpha_0)\quad\text{on }\tilde\square^{4}.
\end{gathered}
\end{equation}
The first line, the counterpart of \cite[(3.27)]{B-CMP109}, involves $\alpha_0$ alone (not
$\alpha_1$) and the first power of $M$. The second line, the counterpart of
\cite[(3.31)]{B-CMP109}, is stated with the plain lattice derivative $\nabla^{\eta}$ and holds
for $|t|\le1$, $|t_\square|\le r_\square(B')$ under $3C_N^{s}\varepsilon_1'\le\alpha_2$, both
at $s\equiv1$ and for the localised chart $H_k(s(Y_0),B')$ of \cite{B-CMP116}. The third
line is the counterpart of \cite[(3.32)]{B-CMP109}.
\item[(N$'$)] At $(\mathbf{U},\mathbf{J})=(U_{k+1},J_{k+1})$ one has
$\mathbf{U}^{\mathrm{gl}}=U_{k+1}$, and $H_k(B')$ is the function $\mathcal{H}(B')$ of
\cite{B-CMP102b}.
\end{itemize}
\end{theorem}
```

### Inputs and their standing

The source proof is CA-I:19744–19867. The statement is an implication in the setting of §4.5, not a theorem from geometry alone.

| Input | Source locus | Standing retained |
|---|---|---|
| `4.5:rem-covariance-inverse-walks` | 13142–13173; CMP 99b §3 before (3.132) | Printed without proof; named hypothesis for the bounds and intrinsic walk expansion of \(\mathsf q_0\). |
| `4.5:rem-averaging-analyticity` | 13175–13197; CMP 98 §E p.43 after (164) | Printed without proof; named hypothesis for the extension of derivative bounds (156)–(157). |
| Corollary furnishing \(C_H\) and its two auxiliary statements | 19588–19590; 19376–19420; concrete frame uses 17550–17555, 18494–18507 | Explicit named hypotheses of A4; the heading supplies no label. Keep the background derivative bound and Landau-to-axial bound as hypotheses. The cited analytic background inputs are CMP 102b Theorem 1 and Proposition 9. |
| Glued-window regularity theorem | 19591; hypothesis (R) at 17015–17055 and following | Named hypothesis, including analyticity and the gauge \(h\). |
| Level-\(j\) window identity | 19592–19593 | Explicit hypothesis. `4.5:lem-window-minimiser`, 19267–19374, gives the displayed level-\(k+1\) counterpart with a proof in CA. Its use here retains real-data, tower and axial-gauge conditions. |
| Frame BCH remainder bound | 19594–19596; `4.5:lem-literal-frame` (AX3), 17519 onward | Explicit named hypothesis, including the bounds on \(g,g'\); not silently replaced by a formal BCH series. |
| `4.5:rem-block-curvature-complex` | 13198–13249; CMP 109 p.263 and (3.26), p.275; extension at p.277 | Printed without proof. Used only for the literal-frame variant here. |
| `4.5:lem-free-current-operators` | 13680 onward; formula 13727–13743 | Proved conditional implication in CA; imports the first two printed inputs and the cited propagator theorems. |
| `4.5:thm-chart-existence` | 14496–14553 | Proved conditional implication in CA, assuming free-current operators and `4.5:lem-nonlinear-correction`. The clauses used below retain their own inputs. |
| K3, K4/K8, K5, K6, K10 | `4.5:prf-chart-linear-bounds` 14711; `4.5:prf-chart-variation-decay` 14803; `4.5:prf-chart-covariance` 14992; `4.5:prf-diagonal-exactness` 15669; `4.5:prf-chart-walk-localisation` 15265 | Proved conditional implications in CA. In particular K3 retains the inverse-covariance sentence; the far-current bound retains CMP 99b (3.49), (3.69), chain-ca P10. |
| `4.5:lem-uniform-increment` | 16019–16151; use 19783 and 19828 | “Stated; proof incomplete” in CA. [ui.md](../ui.md) supplies a completion on the account's inherited analytic inputs, **not yet checked**. Assume that completion here with its original statement and constants. Its weaker-rate repair belongs to that input, not a new A4 decay rate. |
| `4.5:prop-glued-window` | 16992 onward | Proved implication from its explicit rim-regularity input and ceilings. |
| `4.5:lem-fine-axial-frame`, `4.5:lem-literal-frame` | 18477–18767; 17519 onward; summaries `4.5:eq-fine-axial-frame-b`, `4.5:eq-literal-frame-b` | Proved conditional implications in CA. Retain the background corollary, gauge-map bound and all displayed ceilings; the literal version additionally retains the printed complex-curvature input. |
| Activity domain, bound and diagonal identification | CMP 109 (1.9), (1.11)–(1.18), (3.6)–(3.14); CA-I:19628–19661, 19788–19799 | Named inputs concerning the actual \(\mathbf E^{(j)}\). The complex-pair inclusion (1.17), chain-ca P05, remains printed without proof. |
| Constant order | `4.5:rem-constants-order`, 19375–19576 | The printed order and inequalities, with the reference correction below. No numerical value is substituted. |

**A4-C1 (correction, reference only).** CA-I:19386–19388 and 19459–19475 refer to fine-frame conditions `(cf4)` and `(cf5)`. The actual display `4.5:eq-fine-axial-frame-a`, CA-I:18518–18530, labels its conditions `(cf1)`, `(cf2)`, `(cf3)`. Read `(cf4)` as `(cf3)` and `(cf5)` as `(cf2)` in the constant-order remark. The former has the identified member \(b'/L\le\alpha_1^{(98)}\); the latter contains the mixed \(\alpha_0'''+C_{14}\alpha_1'''\) bounds. All displayed inequalities, constants and order of choice are retained. In particular use the whole actual fine-frame display, not nonexistent clauses.

### Proof on the account's route

**(O).** Apply `4.5:lem-free-current-operators` with independent current \(\mathbf J\) in every propagator. Its defining formulas, not an on-shell identity, give the nine listed operators, analyticity, the specified norm bounds and the intrinsic walk expansions. The hypotheses of (O) place the pair in \(\mathfrak S\). K10 supplies their decoupling versions and CMP 116 (1.11) in exactly those norms. The Laplacian estimate stays confined to \(G_0,H_0\).

**(F1).** Use one representative satisfying both members of \(\mathcal U_X\), as the source requires. After current rescaling,
\[
 |J|_{(-3)}=\mathfrak s|\mathbf J|\le L^{-3}\alpha_0<a_\gamma.
\]
Together with the other ceilings this places the pair in \(\mathfrak S\) for the level-\(j\) and level-\(k\) charts. K3 bounds the base chart by \(\alpha_2/3\) in each required quantity once the final fluctuation radius is small enough.

**A4-F1 (filled): all four bounds and the Taylor term.** This application includes the \(P_1\mathcal H\) member `4.5:eq-chart-linear-bounds-3`, not only the value and gradient. Write \(q\) for the maximum in the definition of \(r\). For \(q>0\), \(r=\alpha_2/(3q)\); hence each first-order contribution has norm at most \(\alpha_2/3\). The affine field \(A(t_\square)\) therefore has value, gradient and \(P_1\)-image bounded by \(2\alpha_2/3\). For the current correction the only remaining nonlinear term is the remainder of \(F\) in the chart's definition. Taylor's formula along the segment is
\[
 F(H+tD)-F(H)-tF'(H)D
 =t^2\int_0^1(1-u)F''(H+utD)[D,D]\,du,
 \qquad D=\delta\mathcal H[v].
\]
The chart's second-derivative bound, in the norms and admitted segment of K4, gives the source's bound \(C_F'\alpha_2^2\). Thus
\[
 |\mathfrak J(B,t_\square)|\le \tfrac23\alpha_2+C_F'\alpha_2^2
 \le (\tfrac23+\tfrac14)\alpha_2=\tfrac{11}{12}\alpha_2<\alpha_2.
\]
Here \(\alpha_2\le1/(4C_F')\) is exactly the printed ceiling. The strict margin ensures that the composite is analytic on a neighborhood of each point of its stated closed parameter disc, within the admitted background domain.

**A4-C2 (correction, degenerate-radius convention).** The printed equation \(rq=\alpha_2/3\) has no finite solution when \(q=0\). In that case read the disc condition as \(|t_\square|q\le\alpha_2/3\), with no finite radius restriction from this equation. On \(X\), \(D\), \(P_1D\), \(\nabla D\) and \(\delta\mathfrak J[v]\) then vanish. The affine field is constant there, and so is the local current remainder (its finite stencil is covered by the value/gradient norms in the chart). The same proof applies for every finite parameter disc on which the defining local expressions are read. This is the continuous zero-direction interpretation of the source's Cauchy-radius prescription; no positive-radius case or constant changes.

Apply the uniform-increment input to \(A(t_\square)\) on the same maximal tower carried by the first member of \(\mathcal U_X\). It supplies conditions (i), (ii), (iii)'s curvature half and both halves of (iv), now at \(\alpha_0,\alpha_1\). The current half follows separately:
\[
 |J+\mathfrak J|<L^{-3}\alpha_0+\alpha_2<\alpha_0.
\]
**A4-F2 (filled): the last strict inequality.** The increment lemma has \(C_{IV}\ge4C_{14}\), \(C_{14}=9(2d+2)\), and \(\alpha_2\le\alpha_0/C_{IV}\). Since \(L\ge27\), \(L^{-3}<1/2\) and \(1/C_{IV}<1/2\). Their sum is strictly less than one. The pair therefore belongs to \(U_j^c(X,\alpha_0,\alpha_1)\). The named activity bound on that space gives
\(|\Phi^{\mathbb K}|\le E_0e^{-\kappa d_j(X)}\).
Joint analyticity follows by composing this activity with K1. The notation involving \(r\) is read fibrewise in the background and fluctuation datum, since \(r\) itself depends on that datum.

**(F2).** The actual averaged direction obeys
\(|v|\le c_QL^j\eta|\zeta_\square H_k(B')|\), with support in the specified one-block enlargement. Use K4/K8 at level \(j\) in \(\xi\)-units. Its source measure \(\ell_{j'}^d\) cancels the kernel's \(\ell_{j'}^{-d}\), so no count of fine bonds or levels appears. For each of the value, gradient and current readouts the result is the printed
\[
 C L^j\eta e^{-c_*\delta_0\operatorname{dist}^{(\xi)}(X,\operatorname{supp}\zeta_\square)}
 |\zeta_\square H_k(B')|.
\]
**A4-F3 (filled): the \(P_1\) member and radius.** K4's weighted kernel calculus includes \(P_1\in\mathcal K_{-2}\); composing in that calculus gives the same force-norm estimate. The fraction \(c_*\) was fixed after paying those finitely many convolution losses in K10. It is not reduced again here. Put \(D_X=\operatorname{dist}^{(\xi)}(X,\operatorname{supp}\zeta_\square)\). If the denominator is nonzero, the definition of \(r\) now gives
\[
 r\ge\frac{\alpha_2 e^{c_*\delta_0D_X}}
 {3CL^j\eta|\zeta_\square H_k(B')|}.
\]
This is the CMP 109 (3.17) estimate at the stated rate. The zero case is handled by A4-C2.

**(F3).** At a true pair, K6(c) identifies
\(J+\mathfrak J(B,t_\square)\) with the physical current of \(e^{i\xi A(t_\square)}U_{k+1}\). CMP 109 (1.9) identifies the two-argument activity on this graph with its configuration-only activity. Substitution gives exactly (F3).

**(F4).** K5 transports \(\mathcal H\), its variations and \(\mathfrak J\) by \(R(u)\) when the datum is transported by \(R(\bar u)\). Thus the produced pair transforms by the same gauge map. The activity's named gauge invariance then gives equality of \(\Phi^{\mathbb K}\). This is applied only where the two charts are defined, with the factorization and adjoint bound printed in (F4). It does not assert invariance on an unrestricted complex gauge orbit.

**(F5).** K10 supplies the localized chart with the same four norm controls and the prescribed multiplier \(e^{c_{\mathbb K}\kappa_1}\). Use the final \(\varepsilon_1\) ceiling, which already reads this factor, to make the base contributions \(\le\alpha_2/3\). Repeat the affine and Taylor estimates of (F1) with those localized bounds; apply the same uniform increment and activity bound. Repeat the weighted variation estimate of (F2), now with the supplied multiplied constants. K5 supplies gauge covariance at these localized data. K6 is different: K10 expressly asserts the diagonal exactness identities only at \(s\equiv1\) (CA-I:15338–15340). Thus the analytic bounds and gauge conclusion pass as above, but the proof does not supply an arbitrary-\(s\) physical-current identity.

**A4-C3 (correction, exactness scope).** Read the “same statements” in (F5) with (F3) restricted to \(s\equiv1\). The source proof at 19820–19824 says to apply the proofs of (F1)–(F4), but (F3)'s proof uses K6(c), which the actual K10 input explicitly withholds at general decoupling parameters. The smallest correction is to propagate (F1), (F2), (F4) and the stated bounds to general admissible \(s\), and retain (F3) at \(s\equiv1\). This changes no constant or proof route. It corrects the scope warranted by the printed proof; it is not a counterexample to every conceivable further exactness statement. An assertion of (F3) at arbitrary \(s\) would need a separate named input, not the supplied K10. The exact source statement above is left unchanged so this difference is visible.

**A4-F4 (filled): (F6) and the tower read.** For either additional far term, replace its active cut-off support by the support of \(1-\tilde\zeta_\square\) and its chart by the window chart. The assumed separation is \(M(L^j\eta)^{-1}\). The window restriction lies in \(\mathfrak S\); K1–K10 are uniform over the admissible sequence. The increment lemma is applied to the maximal tower of \(X\), supplied by the first member of \(\mathcal U_X\). If it is instead read on the window tower, condition (iv) must be established for that tower, exactly as the source says at 19828–19831. No transfer of (iv) between unrelated towers is inferred. The same bounds give (F1), the support replacement gives (F2), the assumed level-\(j\) window identity gives (F3), and K5/K10 give (F4)/(F5), with the exactness scope of A4-C3. Thus both further far terms satisfy the assertions in that corrected scope.

**(N-a).** The glued-window proposition produces the admitted representative \((S^h,\operatorname{Ad}_h\mathbf J)\), with \(\|\operatorname{Ad}_h^{\pm1}\|\le2\). Covariance gives
\[
 H_k(B';\mathbf U^{\rm gl},\mathbf J)
 =R(h^{-1})H_k(R(\bar h)B';S^h,\operatorname{Ad}_h\mathbf J).
\]
**A4-F5 (filled): radius and norm accounting.** The transformed datum has size at most \(2|B'|<c_9/4\) when \(|B'|<c_9/8\), within the orbit radius. The output gauge costs at most two. The source uses the allowed chart norm allowance four, so
\[
 N_\beta(H_k(B'))\le 2\,C_9^K\,(2|B'|)\,4=16C_9^K|B'|.
\]
K10 gives the localized bound with its stated factor. The local term reads its walk domains \(Y_0\), while construction of the glued field reads \(\square_0\); the composite reads only their union. Analyticity follows from the named regularity theorem and K1.

**(N-b).** Apply the fine-frame lemma with \(\mathfrak w=w'\), \(\mathfrak b=B_b^f(1+2\beta)\). Its explicit path products make \(w'\) analytic on the stated restriction and bound its adjoint norm by two. Its (AXF4) supplies the base-one representation and datum bound. Its (AXF5) gives the plain-derivative and Hölder bounds for \(\mathbf A\), for the printed \(t,t_\square\) range and \(3C_N^s\varepsilon_1'\le\alpha_2\), including the localized chart. Its (AXF6) gives the BCH logarithm bound. Indeed its \(b'=B_b^fM\alpha_0'''\) equals \(\mathfrak bM\alpha_0\). The already imposed ceiling \(\alpha_2+b'\le1/(4C_{\rm BCH})\) is the one required there. All three lines of `4.5:eq-operator-bounds-a` follow without changing their constants. For the literal variant use \(w=g^{-1}\tilde v\), \(b=B_bM\alpha_0'''\), and (AX3)–(AX6) of the literal-frame lemma, retaining its additional printed complex-curvature hypothesis.

**(N′).** The window-minimizer identity gives \(\mathbf U^{\rm gl}[U_{k+1}]=U_{k+1}\). This is a true pair with its own current. K6(a) identifies its response chart with Balaban's \(\mathcal H\). This proves (N′). The frozen [mu.md](../mu.md), `4.13:lem-minimizer-unique`, is not reproved or promoted here; in particular it does not by itself replace the separately assumed window identity at every use radius.


## A3 — Localised independence

Source: CA-I:9615–9670. Status: unmarked statement, declared proved in CA; conditional on the inputs recorded below.

### Exact source statement

```latex
\begin{corollary}[Independence of the localised terms from the small-field region]
\label{4.4:cor-localised-independence}
Let $\mathcal{S}$ denote the setting in which the $(k+1)$-st renormalisation step is performed
with small-field region
$\Lambda_{k+1}$, let $\mathcal{S}_0$ denote the whole-lattice setting, and let
$\mathcal{R}$ be the walk-expansion rule, with $\mathbb{L}$ the family of operators it expands and
$K^{W'}$ the $W'$-indexed term of $K\in\mathbb{L}$. In this corollary and its proof the letters
$\mathcal{R}$, $\rho$, $s$ and $t$ have the following meanings: $\mathcal{R}$ is the rule just
named, $\rho$ is the index of the local class $\mathbf{P}_{\rho,X}$ of
Definition~\ref{4.4:def-local-data-classes}, $s$ denotes the interpolation parameters of
$\mathcal{R}$, and $t$ is the remaining argument of the terms of \cite[(3.47)]{B-CMP119}.
Assume the following.
\begin{enumerate}
\item[(i)] For every closed union $W$ of $M_1$-cubes, every $W$-indexed quantity of
\cite[\S\S1--2]{B-CMP116} and of
\cite[(3.44)--(3.47)]{B-CMP119} is a finite sum of products of walk factors all of whose steps
have their domains (the grains of the walk) contained in $W$,
local densities on $W$, characteristic functions of bonds of $W$, interpolation integrals, and
universal coefficients.
\item[(ii)] For $W\subset\Lambda_{k+1}$ the local densities, the characteristic functions and the
interpolation integrals are the same in $\mathcal{S}$ and in $\mathcal{S}_0$.
\item[(iii)] The terms $\mathbf{E}_0^{(k+1)}(\Lambda_{k+1},X,b)$ are finite sums of the products
in (i), and a product all of whose ingredients agree in $\mathcal{S}$ and $\mathcal{S}_0$ agrees in
$\mathcal{S}$ and $\mathcal{S}_0$.
\item[(iv)] The conclusions of Theorem~\ref{4.4:thm-uniform-agreement} (locality of the rule and
agreement on uniform regions), of Lemma~\ref{4.4:lem-interior-sufficiency} (interior sufficiency
of the whole-lattice setting) and of Lemma~\ref{4.4:lem-vertex-formula} (the vertex formula)
hold, and conditions (f1) and (f4) of the one-family hypothesis, as it appears among the
hypotheses of Lemma~\ref{4.4:lem-interior-sufficiency}, hold for the operator families expanded
by $\mathcal{R}$.
\item[(v)] For a representative of the one-power hereditary class at $(k+1,X;\cdot)$ and every
$Y'\in\mathbf{D}_k$ with $Y'\subset X$, the restriction to $Y'$ is a representative at
$(k+1,Y';\cdot)$ (the restriction statement for the one-power hereditary class, in the case
where its two levels coincide).
\end{enumerate}
Then for every $X\in\mathbf{D}_{k+1}$ with $X\subset\Lambda_{k+1}$ and every bond $b$ of $X$
(respectively every point $z$ of $X$, for the terms of \cite[(3.47)]{B-CMP119} indexed by points),
the term $\mathbf{E}_0^{(k+1)}(\Lambda_{k+1},X,b)$ (respectively
$\mathbf{E}_0^{(k+1)}(\Lambda_{k+1},X,z)$) of \cite[(3.47)]{B-CMP119}, for
each of the three parts of \cite[(3.37)]{B-CMP119}, computed in $\mathcal{S}$ under
$\mathcal{R}$, equals the term with the same $(X,b)$ (respectively $(X,z)$) computed in
$\mathcal{S}_0$, as a function of $((\mathbf{U},\mathbf{J})|_X;t)$, with $t$ the remaining
argument of the terms in \cite[(3.47)]{B-CMP119}. The equality holds
\begin{itemize}
\item for the first part, on the local class $\mathbf{P}_{\rho,X}$
(Definition~\ref{4.4:def-local-data-classes});
\item for the second and third parts, on the representatives of the one-power hereditary class
$U^{\Sigma^1}_{k+1}(X;(1+\beta)\alpha_0,(1+\beta)\alpha_1,\alpha_0)$, the
class on which these parts are evaluated.
\end{itemize}
These representatives lie in the local class $\mathbf{P}_{1+\beta,X}$
(Definition~\ref{4.4:def-local-data-classes}), where the vertex functionals formed from these
terms are
defined (Lemma~\ref{4.4:lem-local-coercivity}, Proposition~\ref{4.4:prop-local-real-base} and a
standing hypothesis of this chapter).
\end{corollary}
```

### Inputs and their standing

The source proof is CA-I:9681–9791. Keep these inputs separately.

| Input | Locus | Standing in this port |
|---|---|---|
| `4.4:def-local-data-classes` and its local polydiscs | 4427–4503; 4608–4702 | Definitions and domain inclusions; retain their radius ceilings. |
| Hypotheses (i)–(iii), including the assembly proposition | 9625–9638; 9677–9679 | Named hypotheses about the actual Balaban CMP 116 §§1–2 and CMP 119 (3.44)–(3.47) representation. Not inferred from abstract locality. |
| `4.4:thm-uniform-agreement`, especially (a)–(c) | 9355–9474 | Proved conditional implication in CA. Its form-walk, one-family, whole-lattice positivity, walk-covering and rim-touching hypotheses remain attached. Its part (d) in the large-field setting is not used. |
| `4.4:lem-interior-sufficiency` | 9476–9582 | Proved conditional implication in CA. It assumes the local form of the form-walk and one-family hypotheses, whole-lattice positivity, and primed-radius ceilings. |
| `4.4:lem-vertex-formula` | 5218–5274; its application 5276–5291 | Finite evaluation identity, proved in CA; the application uses the specified interpolation rule. |
| One-family conditions (f1), (f4) | `4.4:def-one-family-hypothesis`, 5580–5700; explicitly required at 9642–9643 and used at 9765–9766 | Named hypotheses on local analyticity and the CMP 116 norms, not a seam-bound theorem. |
| `4.4:lem-cell-resolvent` (i), (ii), (iv), (v) | 6219–6302 | Proved conditional implication in CA. Keep (W′), coercivity condition (γ), (k1), (k2), and the local-form positivity, inclusion and regularity hypotheses. |
| `4.4:prop-rule-properties`, walk norm and (c2) | 8912 onward; invoked at 9748 and 9761 | Proved conditional implication in CA; its convergence and product-norm conclusions are inputs here. |
| `4.4:lem-local-coercivity` | 6959–6984 | Proved conditional implication in CA; retain cell coercivity, the cell-cover condition and `4.4:eq-local-coercivity-2`. Its bound is \(5\gamma_*/8\). |
| A2 = `4.4:prop-local-real-base` | 8110–8373 | Heading: “Proof outstanding.” [lrb.md](../lrb.md) supplies a conditional proof, being refereed according to the owner. It is a named input here, not checked or reproved in this port. |
| Hereditary domain inclusion and equal-level restriction (v) | 9644–9647; 9661–9669; 9774–9789 | Named hypotheses. The standing hypothesis applying A2 to these representatives is retained; A2's existence alone is not that application. |
| Determinant normalization and actual potentials | 9718–9721; Balaban CMP 119 (3.37), (3.44)–(3.47), CMP 116 (1.34), (2.1)–(2.13) | Named representation/normalization inputs. The determinant sign is (-1/2). |

The transfer from CMP 109 §3 to the CMP 119 cover, printed without proof at CMP 119 p.276 (CA-I:9413–9417; chain-ca P02), is not discharged here. If used to supply the one-family norm input, it remains a named hypothesis. The comparison of interiors does not require proving all seam norms in \(\mathcal S\).

### Proof on the account's route

**1. Reduce to the walk factors.** Fix \(X\subset\Lambda_{k+1}\) and the local datum in the stated class. Hypothesis (i) lists five kinds of ingredients. Hypothesis (ii) identifies the densities, bond indicators and interpolation integrals in the two settings. The universal coefficients agree by definition. Hypothesis (iii) therefore reduces equality of assembled terms to equality of their walk ingredients.

**A3-F1 (filled): the interpolation evaluation.** For a cube coordinate \(\Delta\), write \(E_\Delta^i\) for evaluation at \(s(\Delta)=i\). The fundamental theorem of calculus gives \(\int_0^1\partial_{s(\Delta)}=E_\Delta^1-E_\Delta^0\). Evaluations in distinct coordinates commute. Thus
\[
 f_\sigma=\prod_{\Delta\in\sigma}(E_\Delta^1-E_\Delta^0)
             \prod_{\Delta\notin\sigma}E_\Delta^0 f
 =\sum_{\sigma'\subset\sigma}(-1)^{|\sigma\setminus\sigma'|}f(1_{\sigma'}).
\]
Summing over \(\sigma\) replaces each factor by \((E^1-E^0)+E^0=E^1\), so the sum is \(f(1)\). This uses iterated integrated derivatives, as defined in CA, not an unstated joint differentiability assertion. The prescribed interpolation rule replaces an operator at a vertex by its restricted walk sum \(K^{W'}\). In a \(W\)-indexed term these sets satisfy \(W'\subset W\).

Uniform agreement (c) identifies both the walk indices and their values whenever \(W'\subset W\subset\Lambda_{k+1}\). Interior sufficiency says these absolutely convergent sums are functions of the local datum itself. It uses whole-lattice majorants, not a whole-lattice extension of that datum. Therefore every vertex value, its finite alternating sum, and each product in (iii) agree.

**2. First part: retain the determinant sign.** For \(a,\lambda_0>0\), direct subtraction gives
\[
 (\lambda+\lambda_0)^{-1}-(\lambda+a)^{-1}
 =(a-\lambda_0)(\lambda+\lambda_0)^{-1}(\lambda+a)^{-1}.
\]
**A3-F2 (filled): evaluate the integral and specify its branch.** Its integral from zero to \(R\) is
\(\log(R+\lambda_0)-\log\lambda_0-\log(R+a)+\log a\).
The first and third terms have difference tending to zero. This gives the source's equation `4.4:eq-localised-independence-1`.

For complex \(a\) in the right half-plane the same antiderivative uses the branch real on positive reals. On compact subsets the integrand and all its fixed derivatives have integrable majorants. The identity is holomorphic there. For a finite accretive matrix \(A=\mathsf A^Y\), apply the scalar identity on each Jordan block: substitute the finite Taylor expansion in its nilpotent part, integrating each derivative. All eigenvalues have positive real part, since an eigenvector \(v\) obeys \(\operatorname{Re}\lambda\,|v|^2=\operatorname{Re}\langle v,Av\rangle>0\). This proves the matrix identity without assuming diagonalizability. Its trace is the analytic logarithm of the determinant, normalized at a real positive matrix. Consequently
\[
 -\tfrac12\log\det\mathsf A^Y
 =-\tfrac12\dim(\ell^2(Y;\mathfrak g^c))\log\lambda_0
 -\tfrac12\int_0^\infty\frac{\operatorname{Tr}[(\mathsf A^Y-\lambda_0 I)
                    \mathsf R^Y(\lambda)]}{\lambda+\lambda_0}\,d\lambda .
\]
This is exactly the source's configuration-independent constant and sign. Compression and the determinant convention are the named inputs above. At a merely local datum, the following term formula defines the localized expression directly; no global matrix extension is required.

Expand \(\mathsf A=\sum_\omega\mathsf A_\omega\) and \(\mathsf R^Y(\lambda)=\sum_\varpi\mathsf R^Y_\varpi(\lambda)\). For a fixed bond \(b\), the diagonal trace is the sum of
\(\operatorname{tr}(\mathsf A_\omega\mathsf R^Y_\varpi)(b,b)\) and
\(-\lambda_0\operatorname{tr}\mathsf R^Y_\varpi(b,b)\).
Collect the first terms when \(\operatorname{hull}_{k+1}(|\omega|\cup|\varpi|)=X\), and the second when \(\operatorname{hull}_{k+1}(|\varpi|)=X\).

**A3-F3 (filled): absolute interchange.** Put \(c=\gamma_*/2>0\). The cell-resolvent input bounds its walk norm by \(4S/(\lambda+c)\). The product rule for that norm bounds the product by a fixed multiple of the product of the two norms. Thus the absolute majorant for the integral, before collecting any \(X\)-subsum, is a fixed finite multiple of
\[
 \frac{\|\mathsf A\|_{\rm walk}+\lambda_0\|I\|_{\rm walk}}
      {(\lambda+\lambda_0)(\lambda+c)}.
\]
On \([0,1]\) the last denominator is at least \(\lambda_0c\). On \([1,\infty)\) it is at least \(\lambda^2\). Both integrals are finite. The same estimate holds on local families by the local clause (v). Absolute convergence justifies products, regrouping by hull and integration in either order. Finite dimensional traces introduce no convergence issue; this argument does not claim their total trace is volume-free.

Every factor contributing to a fixed \(X\)-term has footprint inside \(X\). Uniform agreement identifies it, including its compression data. The scalar weights, \(\lambda_0\), sign and normalization are common. Hence the first localized part agrees as a function on \(\mathbf P_{\rho,X}\).

**3. Second and third parts.** Keep the actual formulas of CMP 116 (2.1)–(2.13) and CMP 119 (3.44)–(3.47). Their operator arguments are \(\mathsf A(s)\), \(\mathsf M^Y(s)\) and \(C^{(k)}(Z_0,s)\). The potential \(V_k(Y',\cdot)\) also reads the named subfamily \(\mathbb L_1\). Hypotheses (f1), (f4) provide these operators at independent current in the required norms. Step 1 identifies all their vertex arguments whose footprints lie inside \(X\).

**A3-F4 (filled): domain and assembly.** Take a representative in exactly the one-power hereditary class printed in the statement. Its domain inclusion places it in \(\mathbf P_{1+\beta,X}\). Local coercivity supplies positivity on the stipulated local polydisc. A2, with its retained standing application hypothesis, supplies the defined analytic vertex functional on that datum. Hypothesis (v) supplies the admissible restriction for every \(Y'\subset X\) entering \(V_k\). Thus both settings evaluate the same functional at the same local arguments; they do not merely have equal formal operator expressions outside their domains. Each vertex value agrees, each alternating sum agrees, and hypotheses (i)–(iii) give equality of the assembled bond-indexed or point-indexed term. This proves all three parts on precisely their printed domains. No change to the source statement or constants is made.


## A9 — Operator theorem at free current

Source: CA-I:46035–46156. Status: unmarked statement, declared proved in CA; conditional on the inputs recorded below.

### Exact source statement

```latex
\begin{theorem}[The operator theorem at free current]\label{4.14:thm-operator-theorem}
Use the levels, territories, covers, bond sets, the cores $\mathsf{Z}_0$, the form $\mathsf{Q}$ at
free current, the operators $\mathsf{A}$, $\mathsf{C}$, $\mathsf{J}$, the balls $\mathcal{U}(1)$ and
$\mathcal{U}(\varepsilon_1)$ and
the constants $\gamma_0$, $\gamma_1$, $\gamma_{+}$, $\gamma_{-}$, $\varepsilon_1$, $m_1$, $\delta_0$,
$B_0$, $B_{\mathsf{J}}$, $B_{\mathsf{Q}}$, $\delta_{\mathsf{Q}}$, $\rho_{\mathsf{Q}}$
and $\ell=M/12d$ of Definition~\ref{4.14:not-free-current-notation}, and the class
$\mathcal{U}_{\mathbb{R}}$ of real backgrounds of Definition~\ref{4.14:def-real-backgrounds}.
Assume the following.
\begin{itemize}
\item The nest $\{\Omega_j\}_{j\le k}$ and $\Omega_t$ satisfy conditions (A1) and (A2) of
\eqref{4.14:eq-prepared-data-admissible-a}.
\item The floors on $M_1$, on $M_1^{\sharp}$, on $M$ and on $L$ of
\eqref{4.14:eq-block-size-conditions-a} hold
(Definition~\ref{4.14:def-block-size-conditions}).
\item The ceilings of \eqref{4.14:eq-block-size-conditions-b} hold
(Definition~\ref{4.14:def-block-size-conditions}).
\end{itemize}
Let $\mathbb{B}\subset\mathbb{B}^{+}$ be arbitrary, let $\mathbb{B}'=\mathbb{B}^{+}\setminus\mathbb{B}$,
$\mathsf{A}=\mathsf{Q}_{\mathbb{B}\mathbb{B}}$, $\mathsf{J}=\mathsf{Q}_{\mathbb{B}\mathbb{B}'}$ and,
where it exists, $\mathsf{C}=\mathsf{A}^{-1}$. Then the following hold; no clause is lettered (J),
so that clause letters are not confused with the operator $\mathsf{J}$.
\begin{enumerate}
\item[(A)] \emph{Objects.} The series defining $\mathsf{Q}$ in
Definition~\ref{4.14:not-free-current-notation} converge, and $\mathsf{Q}$ is analytic on
$\mathcal{U}(1)$; on $\mathcal{U}(\varepsilon_1)$ the inverse $\mathsf{C}=\mathsf{A}^{-1}$ exists;
the operators $\mathsf{Q}$, $\mathsf{A}$, $\mathsf{C}$, $\mathsf{J}$ are analytic, and $\mathsf{Q}$,
$\mathsf{A}$, $\mathsf{C}$ are complex symmetric; $\mathsf{A}\mathsf{C}=1$ on all of
$\mathcal{U}(\varepsilon_1)$. On $\mathfrak{G}\cap\mathcal{U}(\varepsilon_1)$, where
$\mathfrak{G}=\{J=J(\mathbf{U})\}$, let $A_k\in\mathfrak{g}^{\mathbb{B}^{+}}$ be the field of the
fluctuation integral of Ba{\l}aban's construction, written $A_k=\varphi\oplus A'$ with $\varphi$
supported on $\mathbb{B}$ and $A'$ on $\mathbb{B}'$; then the quadratic form in $A_k$ of that
integral is
\begin{equation}\label{4.14:eq-operator-theorem-a}
\tfrac12\langle \varphi,\mathsf{A}\varphi\rangle+\langle \varphi,\mathsf{J}A'\rangle
+\tfrac12\langle A',\mathsf{Q}_{\mathbb{B}'\mathbb{B}'}A'\rangle ,
\end{equation}
so that $\mathsf{C}$ and $\mathsf{J}$ are the covariance and the source operator of the
conditional integral over $A_k|_{\mathbb{B}}$. At $\mathbb{B}=\mathbb{B}^{\ast}$ these are the
operators of \cite[(3.23), (3.25)]{B-CMP119}; at $\mathbb{B}=\mathbb{B}^{K1}$ they are the
covariance and source operator of the conditional integral over $A_k|_{\mathbb{B}^{K1}}$.
\item[(B)] \emph{Bounds at every base point.} At every point $(U,0)$ with
$U\in\mathcal{U}_{\mathbb{R}}$, $\mathsf{Q}$ is real symmetric with
$\gamma_0/2\le\mathsf{Q}\le\gamma_1$, and $\mathsf{C}$ is real symmetric with
$\gamma_{-}\le\mathsf{C}\le\gamma_{+}$. At every real point of $\mathcal{U}(\varepsilon_1)$,
$\gamma_0/4\le\mathsf{Q}\le\gamma_1$ and $\gamma_{-}\le\mathsf{C}\le2\gamma_{+}$. On
$\mathcal{U}(\varepsilon_1)$, $\operatorname{Re}\mathsf{Q}\ge\gamma_0/4$.
\item[(C)] \emph{The source operator.} $\mathsf{J}$ is real at real points,
$\mathsf{J}^{T}=\mathsf{Q}_{\mathbb{B}'\mathbb{B}}$, and $\|\mathsf{J}\|\le\gamma_1$ on
$\mathcal{U}(1)$.
\item[(D)] \emph{Sheets.} In the sheet format of the unit frame,
$\mathsf{Q}\in\mathcal{S}_{u}[\rho_{\mathsf{Q}};B_{\mathsf{Q}},\delta_{\mathsf{Q}};1]$, and for every
$x\ge0$
\begin{equation*}
(x+\mathsf{A})^{-1}\in\mathcal{S}_{u}\Bigl[\frac{M}{4};\,\frac{B_0m_1}{m_1+2x},\,\delta_0;\,
\varepsilon_1\Bigr],
\end{equation*}
with walks and domains independent of $x$.
\item[(E)] \emph{Expansion properties of $\mathsf{C}$.} $\mathsf{C}$ obeys the walk-expansion properties
$(\mathrm{W}1)$, $(\mathrm{W}2)$, $(\mathrm{W}3)'$, $(\mathrm{W}5)^{\mathrm{cov}}$,
$(\mathrm{W}6)^{\mathrm{geo}}$ with the constants $(B_0,\delta_0,\varepsilon_1)$. Here
$(\mathrm{W}1)$--$(\mathrm{W}6)$ are the properties of the walk-expansion format fixed with the
operator theorem at free current with the hulls $\widehat{\square}$, the statement whose domain
lists of the one-box terms carry the hulls $\widehat{\square}$ where the domain lists of the
present theorem carry the reading hulls $\square^{\mathsf{r}}$
(clause (B) above is the property $(\mathrm{W}4)$ for
$\mathsf{Q}$ and $\mathsf{C}$), and $(\mathrm{W}3)'$, $(\mathrm{W}5)^{\mathrm{cov}}$,
$(\mathrm{W}6)^{\mathrm{geo}}$ are the variants of $(\mathrm{W}3)$, $(\mathrm{W}5)$,
$(\mathrm{W}6)$ fixed with that format. Further,
$(\mathrm{W}6)^{\mathrm{geo}}$ is asserted for labels coinciding on an open neighbourhood of
$[\nu]$, the list $[\nu]$ consisting of the reading hulls $\square^{\mathsf{r}}$ of its boxes.
\item[(F)] \emph{The source operator's expansion.} $\mathsf{J}$ satisfies clause (F) of the
operator theorem at free current with the hulls $\widehat{\square}$, read with the enlarged domain
lists described after the present theorem.
\item[(G)] \emph{Resolvents.} Clause (G) of the operator theorem at free current with the hulls
$\widehat{\square}$ holds, read with the same enlarged domain lists.
\item[(H)] \emph{Local balls.} Let $U\in\mathcal{U}_{\mathbb{R}}$ be given globally, and let
$(A',J)$ be given only on
\begin{equation*}
[\nu]^{\approx}=\{x:\ \tau(\{x\},[\nu])<M/2L\},
\end{equation*}
a subset of the one-cube collar $[\nu]^{\sim}$ by the localisation lemma with cut-off distance
$M/2L$ (so that data given on $[\nu]^{\sim}$ suffice a
fortiori), with each of the quantities entering the norm $\|(A',J)\|_{\star}$ less than
$\varepsilon_1/2$ there. Then, for each operator $T$ of (E)--(G), the term $T_\nu$ is defined and
analytic, and the properties $(\mathrm{W}3)'$, $(\mathrm{W}5)^{\mathrm{cov}}$,
$(\mathrm{W}6)^{\mathrm{geo}}$ of (E)--(G) hold for it at the radius $\tfrac12\varepsilon_1$.
\item[(I)] \emph{Uniformity.} The constants $B_0$, $B_{\mathsf{J}}$, $\delta_0$, $\delta_{\mathsf{Q}}$,
$\gamma_0$, $\gamma_1$, $\varepsilon_1$ and the radii $a_1^{\oplus}$, $a_0^{\oplus}$ of
Definition~\ref{4.14:def-block-size-conditions} depend on $d$ and $L$ only;
they are independent of $M$, $k$, $K$, the nest, $\mathbb{B}$, $\Lambda_t$, $\mathsf{Z}_0$, the
volume and $g$.
\item[(K)] \emph{The instance $\mathbb{B}=\mathbb{B}^{K1}$.} The three statements of clause (K)
of the operator theorem at free current with the hulls $\widehat{\square}$ hold, read with the
enlarged domain lists described after the present theorem.
\end{enumerate}
Moreover:

\emph{The covariance statement.}\ For every lattice symmetry $r$ of the group $\mathfrak{r}$ (the $2^d$ reflections
and the $d!$ permutations preserving the partitions) the index sets transport by
$\nu\mapsto r\nu$, and
\begin{equation*}
T_{r\nu}[r\cdot\mathrm{data}](r\cdot\mathsf{u})
=\mathcal{R}_r\,T_\nu[\mathrm{data}](\mathsf{u})\,\mathcal{R}_r^{-1}
\end{equation*}
for $T\in\{\mathsf{C},\mathsf{J},(x+\mathsf{A})^{-1},\mathcal{K}\}$, where
$\mathsf{u}=(\mathbf{U},J)$, $\mathcal{K}$ is the Schur complement defined below, $\mathrm{data}$
stands for the geometric data on which the operators depend, and $r\cdot$ denotes transport by
$r$.

\emph{Dependence on $\Lambda_t$.}\ Write $\mathsf{C}^{K1}$ for $\mathsf{C}$ at $\mathbb{B}=\mathbb{B}^{K1}$. Every term of
the walk expansion of $\mathsf{C}^{K1}$ that depends on $\Lambda_t$ has a domain containing a
point of $\Lambda_t^{c}$ together with its $\ell/3$-collar.

\emph{The Schur complement.}\ Let $B_{\mathcal{K}}$ be the constant of the corollary on the Schur complement.
The Schur complement
$\mathcal{K}=\mathsf{Q}_{\mathbb{B}'\mathbb{B}'}-\mathsf{J}^{T}\mathsf{C}\mathsf{J}$ satisfies
\begin{equation*}
\mathcal{K}\in\mathcal{S}_{u}[M/4;\,B_{\mathcal{K}},\,\delta_0/2;\,\varepsilon_1],
\end{equation*}
and $\gamma_0/2\le\mathcal{K}\le\gamma_1$ at every $(U,0)$ with $U\in\mathcal{U}_{\mathbb{R}}$.
\end{theorem}
```

### Hypotheses, definitions and source standing

The full proof of this implication is CA-I:47253–48140, after its four preparatory lemmas. It does not end at the statement's line 46156.

**Prepared data.** Keep `4.14:prop-prepared-data-admissible`, CA-I:45557–45624, as hypothesis **P4-H-prepared**: printed without proof in Balaban CMP 122a pp.178–179; cited as printed. Its precise last sentence asserts (A1) for the prepared nest. It does **not** supply (A2). CA-I:45612–45615 expressly assumes (A1) and (A2) together in the operator theorem. In level-\(k\) units, \(\ell_j=L^{j-k}\), they require
\[
 \Omega_0\supset\cdots\supset\Omega_k,\qquad
 \ell_j^{-1}\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})\ge M
 \quad(1\le j<k),
\]
compatible closed \(M\)-cube partitions at their respective levels and the stated Dirichlet hull, and separately
\[
 \Omega_t\subset\Omega_k,\qquad
 \operatorname{dist}_\infty(\Omega_t,\Omega_k^c)\ge6M,
 \qquad\Omega_t\text{ is a union of level-}k\text{ closed }LM\text{-cubes}.
\]
Neither is discharged by this port.

**Background and sizes.** `4.14:not-free-current-notation`, CA-I:45236–45439, fixes the operators, bilinear transposes, two covers, frame norms and distances. `4.14:def-real-backgrounds`, CA-I:45439 onward, imposes (u1), (reg), (reg)\(^{\sharp}\). `4.14:def-block-size-conditions`, CA-I:45636–45822, imposes every displayed floor and ceiling. Keep all of them, including the two additional rate floors in its item (c)(ii). The quantities \(\mathsf F\) and \(\mathsf F^P\) are the account's named inversion and positivity floor conditions, not newly evaluated constants.

The following are the actual proof inputs. A label in the first column is a CA label when one is printed. Prefix **P4-H** supplies a local name when CA instead cites a result by its descriptive name. Such an input is retained as a named hypothesis; the use locus is given rather than an invented theorem label or a claim that its proof has been checked.

| Input | CA-I locus | Standing and use |
|---|---|---|
| `4.14:lem-reading-hulls` | 46173–46509 | Unmarked, proof follows in CA. Assume its (i)–(v), including first-cover reading sets and diameter bounds. |
| `4.14:lem-symmetry-covariance` | 46511–46798 | Unmarked, proof follows; conditional on the stated covariance of the averaging letters (46587–46596). Keep that scheme as a hypothesis. |
| `4.14:lem-local-balls` | 46800–46944 | Unmarked, proof follows, using (A1), aligned cubes and \(M>2L\). Its cutoff and Leibniz estimates are expanded below. |
| `4.14:lem-unit-lattice-operators` | 46952–47251 | Unmarked, proof follows, importing CMP 98 bounds and the named averaging/localisation inputs. Keep its actual supports, pivot inverse, radius and coefficients. |
| P4-H-elementary: elementary-sheet lemma | 47294–47324 | Named input, norm clauses (n1)–(n3), rooted in CMP 99b Theorems 3.4, 3.7, 3.9, 3.10, at (u1), (3.35). These are cited, not rebuilt. |
| P4-H-local: locality/complex-localisation/projection chain | 47326–47379 | Named inputs giving local sheets and the \(\Delta^{(2)}\) bound. CMP 98 (139), (142), (147)–(148), (159)–(163) remain cited inputs. |
| P4-H-singular: singular-word lemma | 47389–47394 | Named input for orders (1,0,1) and smooth junctions of the displayed word. |
| P4-H-sheet: product, summation, flattening (F1)–(F3), connection, inversion and walk-sheet lemmas | 47396–47426; 47513–47531; 47555–47584; 47865–47886 | Named analytic-sheet calculus inputs, with exactly the stated norms, floors, radii and shift factors. Not reproved in this port. |
| P4-H-positive: flat and real-background positivity, sector lemma and IMS/tail estimates | 47428–47511; 47753–47785; 47853–47863 | Named inputs. The flat bound uses CMP 96 Proposition 2.7 on the extended domains; the summation bound uses CMP 96 Lemma 2.1. |
| P4-H-assembly: five-stage word assembly and small-current admission | 47533–47584 | Named input, including both branching operations and the smallness conditions for \(a_0^\oplus\). The proof at 47583 refers to four conditions “displayed” in `4.14:eq-block-size-conditions-d`; the displayed formula at 45803–45814 gives the \(a_1^\oplus\) minimum and order, and does not itself print those four \(a_0^\oplus\) inequalities. Retain the assembly-admission assertion as a hypothesis; do not claim that this display proves it. |
| P4-H-form: form symmetry, graph identification and unit-lattice coercivity proposition (b) | 47587–47629; 47927–47933 | Named inputs; graph identities use CMP 99b (3.117′), (3.126), (3.129), CMP 109 and CMP 116 conventions. Coercivity reads (A1),(A2), the displayed floors, identity-background regularity and criticality. |
| P4-H-core: core regrouping and original-hull walk format | 46084–46125; 47991–48047 | Named inputs defining/proving W1, W2, W3′, W5\(^{\rm cov}\), W6\(^{\rm geo}\), and the referenced clauses F,G,K of the original-hull version. Keep that format, including its resolvent convention. |
| P4-H-K1: unit-lattice block identities and dependence lemma | 48098–48115 | Named inputs for the nonzero \(-a\) cross block, zero \(\mathsf G\) cross block, and \(\Lambda_t^c\) collar in each dependent word. |
| P4-H-Schur: Schur-complement sheet corollary | 48117–48119 | Named input for the constant \(B_{\mathcal K}\), radius \(M/4\), and rate \(\delta_0/2\). The spectral bounds are proved below. |

The three intermediate lemmas `4.14:prf-form-walk-expansion` (47253), `4.14:prf-positivity-inversion` (47686), and `4.14:prf-block-identities` (47895) have unmarked headings and proofs in CA. The proof below ports their successive deductions, keeping their named inputs above. In particular a generic sheet algebra is not used to invent missing source constants or formats.

### Proof, part 1: construct the form in the stated sheet class

Use the source's seven inputs in their original order, CA-I:47287–47683.

**(i) Elementary sheets.** P4-H-elementary gives sheets for \(G',G_0,T'\) and
\((DG'),(G'D^*),(D^*G_0),(G_0D)\). It reads CMP 99b (3.43) at \(\beta=1/2\) and (3.44) at \(\varepsilon=1/2\); the additional \(M_1^{-|\omega|/2}\le1\) only improves their bounds. Use exactly
\[
 \widehat X=\bigcup_{\square\subset X}\square^{\max\{5,2L\}},
 \quad\rho_0=c_X(d)L^2M_1.
\]
The reading-hulls lemma gives geometric locality on these lists. The weight stays on \(X_0\), so its constants \(B_{\rm el},\delta_{\rm el}\) do not change. The diameter changes to \(\rho_0\); the many-scale distance condition (τ1) preserves the decay bound.

**(ii) Local operators.** Use the symmetric endpoint weights \(w_z\) from the exact definition. The symmetry lemma changes the local constant by
\[
 \nu e^{\delta c_N}\longmapsto n_w\nu e^{\delta(c_N+dL)},
 \quad c_N\longmapsto c_N+dL,
 \quad n_N\longmapsto n_Nn_w,
 \quad n_w\le3(2dL+1)^d.
\]
It preserves all five sheet properties. Apply P4-H-local to \(Q',Q'^T,\mathfrak S,a,M_{\mathsf f},Q,Q^T\). For \(\Delta^{(2)}[\mathsf f]\), follow the printed chain: the complex (139) bound; the complex localisation proposition with \(L\ge8\); its Cauchy corollary giving complex (148); that corollary's (iii′) with complex averaging; then complex projection (iv). The result is
\[
 \|\chi_y\Delta^{(2)}[\mathsf f]\|
 \le C_2\ell_y^{-2}\sup_b\ell_b^3|\mathsf f(b)|.
\]
Keep \(\theta_k=6C'_1\alpha_0+\kappa\alpha_1\), \(\kappa=4(3c'''+2c^{\natural}/L)\), in the averaging input. This \(\kappa\) is not the glossary's parameter. Nothing here replaces the required complex extension by a bound at real data alone.

**(iii) Unit-lattice operators.** The unit-lattice lemma supplies \(P_\Lambda,C_\flat,C_\flat^T,\mathsf G,\mathcal J[\mathsf f]\) on the admitted complex ball. The \(r_\flat\) ceilings and the last three entries of
\[
 a_1^\oplus=\min\left\{\varepsilon_Ta_1^{\rm el},
 \frac{r_\flat}{2\mathsf o_2},
 \frac{r_\flat^2}{16L^{d+1}\mathsf o_2},
 \frac{\log2}{4dL\mathsf o_2}\right\}
\]
are precisely its inputs. In particular \(\|\pi_c^{-1}\|\le4\) and the source-vertex bound are retained, not inferred from a formal inverse at the identity.

**(iv) Singular word.** Apply P4-H-singular to
\[
 \mathfrak b=(DG')(D^*G_0D)(G'D^*).
\]
Its three orders are (1,0,1); use its smooth junctions. This isolates the singular composition before the ordinary product calculus.

**(v) Constrained inverse.** First form \(T=QG_0Q^T\). Product and flattening (F1) put it in the many-scale frame. That frame has \(c_\tau=2L\), and its summation bound uses CMP 96 Lemma 2.1 under the stated floor. The second cover has
\[
 N_d=2\cdot5^d,\quad\lambda^\sharp=C_dL^2/M_1^\sharp,
 \quad w^\sharp=M_1^\sharp/(2L),\quad\rho_T=8dL^2M_1^\sharp.
\]
The floor \(M_1^\sharp>2L\rho_0\) verifies its width condition at the actual elementary radius. List \(\square^{\mathsf r}=\square^{2L+1}\) in each word domain. The reading-hulls lemma preserves Sh1–Sh4 and supplies Sh5 on the enlarged lists.

Use the positivity input at the identity to obtain \(\widetilde T(1)\ge m^{\rm flat}\). The real-background proof is its seven-step comparison: IMS error \(\le m^{\rm flat}/6\); local tail \(\le m^{\rm flat}/12\); (reg)\(^{\sharp}\) gauge; cutoff \(\varphi_\square=1\) on \(\square^3\); complex path
\[
 \mathsf u_z=(e^{iz\eta\varphi_\square A},0),
 \quad |z|<r^\sharp=a_1^{\rm el}/(2a^\sharp);
\]
gauge covariance and reading identify its value at one with the gauged local walk sum; Schwarz compares it to the identity; finally sum the local inequalities. The path's admission and the IMS/tail bounds are those of P4-H-positive in the scale-weighted norms, with the ceiling's stated \(L^2\) allowance.

**A9-F1 (filled): Schwarz and the error shares.** Write \(K_T=eB_TS_{ms}(\delta_T)\). For unit vectors the difference of path matrix elements is analytic, vanishes at zero and is bounded by \(2K_T\). Scaling the disc and applying Schwarz bounds its value at one by \(2K_T/r^\sharp\). The printed ceiling implies
\(r^\sharp\ge12K_T/m^{\rm flat}\), hence this loss is at most \(m^{\rm flat}/6\). Local positivity at the identity, comparison and addition of the tail therefore leave
\[
 m^{\rm flat}-m^{\rm flat}/12-m^{\rm flat}/6-m^{\rm flat}/12
 =2m^{\rm flat}/3.
\]
Gauge transport is unitary at real backgrounds. Summing with \(\sum h_\square^2=1\), then subtracting the IMS error, leaves \(m^{\rm flat}/2=m_0\). This fills the source's final assembly of the seven steps.

The sector input gives \(\operatorname{Re}\widetilde T\ge m^{\rm flat}/4\) for \(\|A'\|<\varepsilon_Ta_1^{\rm el}\), where
\(\varepsilon_T=m_0/(4eB_TS_{ms}(\delta_T))\). The first entry of the \(a_1^\oplus\) minimum admits all of \(\mathcal U(1)\). Apply the inversion input at coercivity \(m^{\rm flat}/4\) and the exact floor \(\mathsf F_{ms}(B_T,\delta_T,m^{\rm flat}/4;N_d,\lambda^\sharp,w^\sharp)\). It yields
\[
 \widetilde T^{-1}\in\mathcal S_{ms}[\rho_T;48N_d/m^{\rm flat},\mu_T/4;1].
\]
Flattening (F2) then gives \(T^{-1}\in\mathcal O^{-2}[\rho_T;B_{T^{-1}},\delta_{T^{-1}};1]\). No Balaban inverse theorem is rebuilt here.

**(vi) Five-stage assembly.** Combine the preceding letters in the alphabet \(\mathfrak L\), with its common radius \(\rho_T\), bound and rate. Its vertices are \(M_J\), with \(\nu_J=2c_{\mathfrak g}a_0^\oplus\), \(\Delta^{(2)}\), and \(\mathcal J\). The actual word tails lie in \([-5,5]\subset[-(8+d),8+d]\). Use \(\mathfrak S/2\) in the second symmetrizing term: the symmetry lemma identifies its polarized form with the original one, without increasing weights. Apply the named assembly in this order: construct \(G_\pi,T_\pi^{-1}\) and the associated current; insert that current \(\mathfrak j_0\) in \(\Delta^{(2)}\) by branching; construct \(G_1,T_1^{-1}\) and its associated current; branch \(\mathcal J[\mathfrak j]\); then form
\[
 \mathsf Q=C_\flat^T
 (P_\Lambda T_1^{-1}P_\Lambda-a+\mathcal J[\mathfrak j]+\mathsf G)C_\flat.
\]
Summation, product and flattening (F3) give exactly
\[
 \mathsf Q\in\mathcal S_u[\rho_{\mathsf Q};B_{\mathsf Q},\delta_{\mathsf Q};1],
 \qquad\rho_{\mathsf Q}=\rho_T,\quad\delta_{\mathsf Q}=\delta_{\mathfrak L}/32.
\]
The source's small-current assembly hypothesis gives absolute convergence of (q1),(q2) and the identities
\(G_\pi=(G_0^{-1}+W_\pi)^{-1}\), \(G_1=(G_0^{-1}+W_1)^{-1}\).

**A9-F2 (filled): limits and symmetry.** The named sheet bounds majorize the series uniformly on each smaller analytic ball, so Cauchy's integral formula passes through the sums and gives analytic limits. Symmetry is supplied by the symmetric defining forms, not by the false general rule that a product of symmetric matrices is symmetric. Taking transposes of their convergent sums preserves those identities. Reality and covariance pass in the same way. Every constituent reads the specified enlarged list; a product reads its union, and equal local constituents give equal sums. Thus Sh5 also passes. The sheet Schur estimate gives \(\|\mathsf Q\|\le eB_{\mathsf Q}S_u(\delta_{\mathsf Q})=\gamma_1\).

**(vii) Identity base.** At \((1,0)\) the physical current is zero. P4-H-form identifies \(\mathsf Q(1,0)\) with the unit-lattice form \(\mathcal B\) on the displayed data \((\Omega_t^{(k)},(\Omega_j)_{j\le k},1,M_1,hC^{(2)})\). Coercivity proposition (b) gives \(\mathcal B\ge\gamma_0^X/c_\Phi^2=\gamma_0\). Its four conditions are (A1),(A2); identity-background regularity; the remaining data condition supplied by (fl-99) and (fl-M)′(i)–(ii); and criticality at the identity. The latter follows directly because the first derivative of each identity plaquette action is zero. The cited positivity input remains CMP 96 Proposition 2.7. The account's alternative Jensen/Poincaré route is not used.

### Proof, part 2: positivity and inversion

This is `4.14:prf-positivity-inversion`, CA-I:47686–47898. Keep
\[
 m_1=\gamma_0/4,\quad\varepsilon_1=\gamma_0/(8\gamma_1),\quad B_0=12\cdot2^d/m_1,
\]
\[
 \mu_1=\min\{\delta_{\mathsf Q}/4,
 m_1/(8eB_{\mathsf Q}S_u(\delta_{\mathsf Q}/2))\},\quad\delta_0=\mu_1/4.
\]
Part 1 evaluated on a unit vector at the identity gives \(\gamma_0\le\gamma_1\).

**Real backgrounds.** Use the unit boxes of side \(\ell=M/(12d)\), centered on \(\ell\mathbb Z^d\), with product cutoffs and \(\sum h_{\mathsf b}^2=1\). Their overlap, Lipschitz constant, width and hull diameter are
\[
 2^d,\qquad 3d/\ell=36d^2/M,\qquad\ell/4=M/(48d),\qquad3d\ell=M/4.
\]
The printed floor \(M\ge144d\rho_{\mathsf Q}\) says \(\rho_{\mathsf Q}\le\ell/12\). The remaining floors give \(\ell\ge6\) and \(M>2L\). The side \(\ell\) is a real number; it need not be an integer. The identity \(M/\ell=12d\) gives the alignment used here.

**A9-F3 (filled): room for the local gauge.** A selected box has a bond of \(\mathbb B^+\) in its prescribed inner enlargement. Its twice-collared hull has side \(5\ell\le M\), and is within distance \(5\ell+1\) of \(\Omega_t\). Since \(d=4\) and \(\ell\ge6\), \(5\ell+1<6M\). Choose a containing side-\(M\) cube through that hull; its possible extra displacement is at most \(M\), still below the \(6M\) margin. Thus it lies inside \(\Omega_k\), and the (reg) hypothesis applies. This uses (A2), not the printed prepared-data sentence alone.

Put \(\mathsf D=\tfrac12\sum[h_{\mathsf b},[h_{\mathsf b},\mathsf Q]]\). Expanding each commutator gives
\[
 \tfrac12[h,[h,Q]]=\tfrac12(h^2Q+Qh^2)-hQh,
 \quad \mathsf Q=\sum h_{\mathsf b}\mathsf Qh_{\mathsf b}+\mathsf D.
\]
Use the named IMS estimate and the floor \(\mathsf F_u^P(B_{\mathsf Q},\delta_{\mathsf Q},\gamma_0;2^d,36d^2/M,M/(48d))\). They give \(\|\mathsf D\|\le\gamma_0/6\), with the source's estimate at CA-I:47771–47775. For the local partial walk sum \(\mathsf Q^{\mathsf b}\), the tail input gives
\[
 \|\mathsf E_{\mathsf b}\|
 \le eB_{\mathsf Q}e^{-\delta_{\mathsf Q}\ell/8}S_u(\delta_{\mathsf Q}/2)
 \le\gamma_0/12.
\]
These are the exact uses of the positivity floor; no machine evaluation or altered decay constant is inserted.

On the containing cube take the (reg) gauge, \(U^u=e^{i\eta A}\), with \(|A|,|\nabla A|<a_Q\). Extend the gauge by the identity outside that cube. Let \(\chi=1\) on the local reading hull, vanish outside its \(\ell\)-collar, and have Lipschitz constant \(1/\ell\). The discrete product rule bounds the gradient of \(\chi A\) by \(a_Q(1+1/\ell)<2a_Q\), and its value by \(a_Q\). Hence
\[
 \mathsf u_z=(e^{iz\eta\chi A},0)\in\mathcal U(1),
 \quad |z|<r_{\rm reg}=a_1^\oplus/(2a_Q).
\]
Gauge covariance and the reading property give
\(\mathsf Q^{\mathsf b}(U,0)=\Gamma(u)^{-1}\mathsf Q^{\mathsf b}(\mathsf u_1)\Gamma(u)\).
The gauge is real, so \(\Gamma(u)\) is unitary. The ceiling yields
\(r_{\rm reg}\ge12\gamma_1/\gamma_0\ge12\).
For unit vectors the analytic difference of path matrix elements has modulus at most \(2\gamma_1\) and vanishes at zero. Schwarz gives an operator-norm difference at one of at most
\[
 2\gamma_1/r_{\rm reg}=4a_Q\gamma_1/a_1^\oplus\le\gamma_0/6.
\]
The two tails and this comparison leave \(2\gamma_0/3\) on each cutoff range. Sum those forms with \(\sum h_{\mathsf b}^2=1\) and allow the IMS error \(\gamma_0/6\). This proves \(\mathsf Q(U,0)\ge\gamma_0/2\).

**A9-F4 (filled): complex sector and invertibility.** On a fibre based at \((U,0)\), a datum of normalized size \(s<\varepsilon_1\) lies at parameter \(s\) on a unit-radius analytic line through that base. For each unit vector the difference of the matrix element from its base value is bounded on that line by \(2\gamma_1\). Schwarz bounds it at parameter \(s\) by \(2\gamma_1s<\gamma_0/4\). Thus the Hermitian real part satisfies
\(\operatorname{Re}\mathsf Q\ge\gamma_0/4=m_1\).
The source's entrywise sector-lemma proof gives the same radius. Compression to any \(\mathbb B\) preserves this inequality. If \((x+\mathsf A)v=0\) for \(x\ge0\), then
\(0=\operatorname{Re}\langle v,(x+\mathsf A)v\rangle\ge(x+m_1)|v|^2\), so \(v=0\). Finite dimensionality then gives an inverse. This proves existence, but the sheet bound still uses the next named input.

Apply P4-H-sheet's unit-frame inversion lemma with the arbitrary index set \(\mathbb B\), the same box constants and the floor \(\mathsf F_u\) from the statement. Its output is
\[
 (x+\mathsf A)^{-1}\in\mathcal S_u
 \left[\max\{\rho_{\mathsf Q},M/4\};\frac{12\cdot2^d}{m_1+2x},\frac{\mu_1}{4};\varepsilon_1\right].
\]
Since \(\rho_{\mathsf Q}\le M/(144d)\le M/4\), its radius is \(M/4\). Substituting \(B_0m_1=12\cdot2^d\) and \(\delta_0=\mu_1/4\) gives exactly clause (D). The inversion lemma's indices and domains do not depend on \(x\). Nothing requires a regular shape for \(\mathbb B\). At \(x=0\), it gives \(\mathsf C=\mathsf A^{-1}\).

### Proof, part 3: block identities and every remaining clause

This is `4.14:prf-block-identities`, CA-I:47895–48140.

**(A).** The convergent form series is analytic and complex symmetric. Its coordinate blocks are analytic, and \(\mathsf A^T=\mathsf A\). The inverse exists throughout \(\mathcal U(\varepsilon_1)\). **A9-F5 (filled):** the cofactor formula divides analytic entries by the nowhere-zero analytic determinant, so \(\mathsf C\) is analytic. Transposing \(\mathsf A\mathsf C=I\) yields \(\mathsf C^T\mathsf A=I\); uniqueness of the inverse gives \(\mathsf C^T=\mathsf C\). These facts use bilinear transpose; they do not confuse complex symmetry with Hermitian symmetry.

On the physical graph, P4-H-form identifies \(\mathsf Q\) with Balaban's \(C^*\Delta^{(k)}C\). Here Balaban's \(C\) is distinct from \(\mathsf C\). Write \(A_k=\varphi\oplus A'\). The two half cross terms agree because \(\mathsf Q_{\mathbb B'\mathbb B}=\mathsf J^T\), giving the exact displayed quadratic form in (A). Completing the square gives
\[
 \tfrac12\langle A_k,\mathsf QA_k\rangle
 =\tfrac12\langle\varphi+\mathsf C\mathsf JA',
       \mathsf A(\varphi+\mathsf C\mathsf JA')\rangle
  +\tfrac12\langle A',\mathcal KA'\rangle,
 \quad\mathcal K=\mathsf Q_{\mathbb B'\mathbb B'}-\mathsf J^T\mathsf C\mathsf J.
\]
**A9-F6 (filled):** the mixed term is \(\langle\varphi,\mathsf A\mathsf C\mathsf JA'\rangle=\langle\varphi,\mathsf JA'\rangle\), and the extra square term is \(\tfrac12\langle A',\mathsf J^T\mathsf C\mathsf JA'\rangle\), precisely canceled by \(\mathcal K\). At real positive data this is the conditional Gaussian precision/covariance identification; its algebraic continuation holds throughout the complex ball. The identification with the actual fluctuation integral is asserted only on the physical graph. Choosing \(\mathbb B^*\) gives CMP 119 (3.23),(3.25); choosing \(\mathbb B^{K1}\) gives the indicated conditional integral.

**(B).** At a base point the quadratic-form bounds on \(\mathsf Q\) restrict to \(\mathsf A\), so all its eigenvalues lie between \(\gamma_0/2\) and \(\gamma_1\). Diagonalizing this real symmetric positive matrix and taking reciprocals gives
\[
 \gamma_- I=\gamma_1^{-1}I\le\mathsf C\le(2/\gamma_0)I=\gamma_+ I.
\]
At every real point in the small ball the same argument uses \(\gamma_0/4\), giving \(\gamma_-\le\mathsf C\le4/\gamma_0=2\gamma_+\). The complex real-part bound is part 2.

**(C).** A block of a real matrix is real. Transpose symmetry gives the asserted transpose identity. Coordinate projections have norm at most one, so \(\|\mathsf J\|\le\|\mathsf Q\|\le\gamma_1\) on \(\mathcal U(1)\).

**(E), (F), (G).** Apply P4-H-core to a unit sheet of radius at most \(M/4\). Its aligned-core requirement is supplied by (A2); in particular the cubes within \(3M\) of a core in \(\mathsf Z_0^\sim\) are in the single level-\(k\) partition. At \(x=0\), (D) is the sheet \(\mathcal S_u[M/4;B_0,\delta_0;\varepsilon_1]\), so the core lemma gives all the properties in (E). Its W2 is an absolute regrouping of the same series at different cores, not a new equality obtained by choosing unrelated expansions.

For (F), take the off-diagonal block of the form sheet. It has \(B_{\mathsf J}=B_{\mathsf Q}\), radius \(\rho_{\mathsf Q}\le M/4\), rate \(\delta_{\mathsf Q}\), and analytic radius one. Since \(\delta_0\le\delta_{\mathsf Q}\) and \(\varepsilon_1\le1/8\), the same bounds hold at the stated weaker rate and smaller ball. The core input supplies the precise source-operator clause F of the original-hull format.

For (G), use (D) at each \(x\ge0\). Retain the inversion input's factor for a word with \(n\) steps,
\[
 (1+2x/m_1)^{-(n+1)}.
\]
There is one inverse factor for each of the \(n+1\) visited positions; the index starts at \(n=0\). This explains the source's shift exponent, with no index shift to \(n\). For complex shifts the cited resolvent convention uses \(\operatorname{Re}x\) in its allowed half-plane; the inequality \(|1+2x/m_1|\ge1+2\operatorname{Re}x/m_1\) preserves that majorant. Do not assert resolvent control across its singularities.

**A9-F7 (filled): enlarged reading lists and decay.** Each many-scale word carries \(\square^{\mathsf r}\); each elementary word carries the stated \(\widehat X\). Agreement of labels on a neighborhood of the union identifies each constituent. Products and sums therefore agree termwise. This is Sh5 passed to W6\(^{\rm geo}\), with exactly that neighborhood condition. Enlarging a domain gives additional allowed connecting choices, so its infimum tree distance cannot increase. Therefore if \(d_{\rm new}\le d_{\rm old}\), then \(e^{-\delta d_{\rm old}}\le e^{-\delta d_{\rm new}}\). Every upper decay estimate persists. The separate diameter estimate from the reading-hulls lemma remains \(\rho_{\mathsf Q}\le M/4\); it is this estimate that permits the core packing input. Gauge covariance is Sh4 passed termwise. No lower distance bound for the old lists is silently transferred to the enlarged lists.

**(H).** Use the local-ball lemma at \(r=\varepsilon_1\) for covariance/resolvents and at \(r=1\) for the source operator. Write
\[
 \chi(x)=\max\{0,1-(2L/M)\tau(\{x\},[\nu])\}.
\]
**A9-F8 (filled): collar and cutoff.** A path of weighted length \(<M/(2L)\) cannot cross a full layer, which costs at least \(M\) by (A1). Starting in a level-\(n\) cube, it stays in either layers \(\{n,n+1\}\) or \(\{n-1,n\}\). In the former its Euclidean length is \(<M\ell_n/2\); in the latter it is \(<M\ell_{n-1}/2\). On the common grid of mesh \(M\ell_{\min\{m,n\}}\), a cube of the destination level \(m\) is either touching the starting cube or separated from it by at least one mesh. The strict half-mesh bound forces touching. Hence \([\nu]^\approx\subset[\nu]^\sim\).

The value/current components do not grow on multiplication by \(\chi\). One step in layer \(m\) changes \(\chi\) by at most \(2L/M\); the discrete product rule gives
\[
 \ell_m^2|\nabla(\chi A')|
 \le\ell_m^2|\nabla A'|+(2L/M)\ell_m|A'|.
\]
Thus local components less than \(r/2\) extend, by cutoff and zero, to components strictly below \((1+2L/M)r/2<r\). At the cutoff boundary the same difference formula uses the nonzero-side value and the Lipschitz bound for \(\chi\), so no values outside its support are required. The global real background \(U\) is already given. On \([\nu]\), \(\chi=1\); the reading property therefore makes the term independent of extension. The extension map is linear and the original term analytic, giving local analyticity. The same reading/covariance properties are inherited. Since \(\varepsilon_1\le1/8\), the data of radius \(\varepsilon_1/2\) required for (H) also satisfy the source operator's radius \(1/2\).

**(I).** Keep the printed order, expanded at CA-I:48069–48080:
\[
 d,L\to M_1\to(B_{\rm el},\delta_{\rm el},a_1^{\rm el},\rho_0,B_T,\delta_T,m^{\rm flat},r_\flat)
 \to M_1^\sharp
\]
\[
 \to(\varepsilon_T,\mu_T,B_{T^{-1}},\delta_{T^{-1}},\rho_T,B_{\mathfrak L},\delta_{\mathfrak L},
 x,a_1^\oplus,a_0^\oplus,B_{\mathsf Q},\delta_{\mathsf Q},\gamma_0,\gamma_1,
 \varepsilon_1,m_1,\mu_1,\delta_0,B_0,\mathsf c_1)
 \to\kappa_1\to M\to\text{layer couplings}\to\text{radii}\to g.
\]
The source includes an unqualified \(x\) in this order list. In the resolvent clause, \(x\) remains arbitrary; part 2 displays all dependence of its bound on that shift, and none of the constants in (I) is chosen from it. **A9-F9 (filled):** choose \(M_1\) once as a function of \((d,L)\) satisfying its floor; choose \(M_1^\sharp\) once satisfying the subsequent floor. Substitute these choices into every later constant. A function of these two fixed choices is a function of \((d,L)\). Only afterwards choose \(M\). The occurrences of \(\ell=M/(12d)\) enter the floor tests, not the output constants. This proves the precise list of independences in (I), conditional on the named input uniformities. It does not show that arbitrary independent choices of \(M_1,M_1^\sharp\) have identical constants.

**(K).** Set \(\mathbb B=\mathbb B^{K1}\). P4-H-K1 gives three statements in the source's original format: pivot rows of \(C_\flat\) have entries on both sides, with the asserted nonzero \(\mathbb B\mathbb B'\) block of \(C_\flat^T(-a)C_\flat\); the unit-lattice identity makes the corresponding block of \(C_\flat^T\mathsf GC_\flat\) vanish; and the constants are independent of \(\Lambda_t\). The last assertion follows also from (I). These are properties of the actual pivot construction. No generic inference that every crossed matrix product is nonzero is used.

**Lattice symmetry.** The symmetry lemma supplies the bijection \(\nu\mapsto r\nu\) of all constituent indices. Endpoint weights satisfy \(w_{rz}(r\iota)=w_z(\iota)\). The half-symmetrizing convention and the reversal parities make both trilinear words orientation independent. By the retained averaging-covariance hypothesis, each elementary factor conjugates by \(\mathcal R_r\). **A9-F10 (filled):** adjacent conjugating factors cancel in a product, \((RTR^{-1})(RSR^{-1})=RTSR^{-1}\); transported sums use the index bijection. The same identity holds for inverses by multiplying the conjugated inverse. It therefore passes through branching, inversion, core regrouping and the Schur product, giving exactly the theorem's termwise covariance identity.

**Dependence on \(\Lambda_t\).** Apply P4-H-K1's dependence lemma to each word of \(\mathsf C^{K1}\). Every word depending on \(\Lambda_t\) has the required point of \(\Lambda_t^c\) with its \(\ell/3\)-collar in its listed domain. Symmetric cell weights only reweight local factors; they do not change the projection \(1''\) on which that dependence lemma reads the split. Enlarged lists contain the original lists, so this inclusion persists. No inference from decay alone would give it.

**Schur complement.** P4-H-Schur and the product/sum calculus give
\[
 \mathcal K\in\mathcal S_u[M/4;B_{\mathcal K},\delta_0/2;\varepsilon_1].
\]
Keep that corollary's constant and rate. **A9-F11 (filled):** at a real base point, completing the square above shows
\[
 \langle A',\mathcal KA'\rangle
 =\min_\varphi\langle\varphi\oplus A',\mathsf Q(\varphi\oplus A')\rangle,
\]
with minimizer \(-\mathsf C\mathsf JA'\). The lower bound on \(\mathsf Q\) gives at least \((\gamma_0/2)(|\varphi|^2+|A'|^2)\), hence at least \((\gamma_0/2)|A'|^2\) at that minimizer. Evaluating instead at \(\varphi=0\) bounds the minimum by \(\gamma_1|A'|^2\). Thus \(\gamma_0/2\le\mathcal K\le\gamma_1\), exactly as stated.

This completes the account's implication, with every named premise above retained. Its application to a prepared history additionally needs the background-space and drop-out supply conditions of `4.14:rem-supply-scope`, CA-I:49495–49546 (and its continuation). In particular CMP 122a p.191's printed drop-out-space sentence is not proved by (A)–(K). No claim that every RG history supplies these hypotheses is made.



## Retained Balaban frontier

These are the named input families of `chain-ca.md` §§6.1–6.2 at the pinned repository revision. They are preserved here to prevent any published or printed sentence from disappearing behind an intermediate lemma. The precise use loci for P4 are in the proof tables above. Rows used only by later tranches remain a **carried frontier**, not extra hypotheses artificially required for this local implication. None is rebuilt or discharged here.

Each P-number below is a distinct named hypothesis bundle. “Printed” reports the complete account's attribution to Balaban. It is not an independent reading of the original paper. In particular P01's source statement supplies prepared (A1), while A9 separately assumes (A2).

| # | Sentence bundle | CA standing/use lines | Reach |
|---|---|---|---|
| P01 | Prepared large-field data admitted; 122a pp.178–179 | I:45557; I:166579–166580; II:145579–145580; III:75801 | J |
| P02 | Transfer 109 §3, Lemmas 5–6, to 119's cube cover; 119 p.276 | I:166581–166583,166638–166640 | J |
| P03 | Two lowest tower regularity classes; 99b p.396, (3.35),(3.37) | I:166584–166585; III:111073–111079 says a conditional proof is supplied | J; replacement/supplier reconciliation needed |
| P04 | Locality of interaction terms; 122b p.379 | I:166586–166587 | J |
| P05 | Complex-pair inclusion; 109 (1.17) | I:166588–166589 | J |
| P06 | Block-averaged curvature estimates extended to near data; 109 p.277, (3.26)–(3.28) | I:166590–166592 | J |
| P07 | Inverse constrained covariance bounds and walks; 99b §3 before (3.132) | I:166593–166594; `4.5:prf-chart-linear-bounds`, I:14711 | J |
| P08 | Further operator walk expansions; 99b after Theorem 3.9 | I:166595–166596 | J |
| P09 | Analytic derivative bounds of averaging maps; 98 §E p.43 | I:166597–166598 | J |
| P10 | Second far-family current inequality; 99b (3.49),(3.69) | I:166599–166600 | J |
| P11 | Polymer-gas representation of bracket; 122b (1.90) | I:166601–166602 | J |
| P12 | Large-field bounds under remaining modifications; 122b p.386 | I:166603–166604 | J |
| P13 | Layerwise gauge clauses; 122a (1.64)–(1.69), pp.190–191 | I:166605–166606 | J |
| P14 | Layerwise ceiling as a small-coupling condition; 122a p.192 | I:166607–166608 | J |
| P15 | Bounds for old terms beside a new region; 122b p.375 | I:166609–166610; II:60275–60276; III:111308–111310 | J/S; also common order of choice, III:110863–110866 |
| P16 | Joined-domain convergence and analytic extension; 122a p.192 (1.70), 122b p.377 (1.68)–(1.69) | I:166611–166613; II:145585–145587; III:111358–111361 | J/W/U |
| P17 | Absolute boundary bound and gauge invariance; 122b (1.11),(1.23)–(1.48), p.369 | I:166641–166642 | J |
| P18 | Analytic solution of large-field equation; 122b p.367 (1.40)–(1.41) | I:166643–166644 | J |
| P19 | Small sum of localised remainders; 122b p.368 after (1.46)–(1.48) | II:60277–60280; III:111351–111353 | S |
| P20 | Flat step quadratic form equals free field's; 95 §1 | II:145581–145582 | W |
| P21 | Normalised island operation positivity and bound; 122b §1 | II:145583–145584 | W |
| P22 | Passage between response bounds (189),(190); 102b p.308 | `9.3:prop-second-variation`, III:35577; III:75781 | U |

Each published item below is likewise a named hypothesis at its stated Balaban theorem/formula locus, with **cited, not reproved here** standing. Within a grouped entry, each theorem, proposition, lemma or corollary keeps its own number and all its stated hypotheses. The rightmost CA loci are the account's input lists; this port does not turn that list into a verification of the papers. The common (0)/(i) list was also read at CA-I:166552–166648. Other clause lists are carried from chain-ca, not independently reread for this tranche.

| Part of chain | Published theorem/definition frontier in CA |
|---|---|
| Joint (0)/(i) | 95 (1.118), 96 p.229 (2.36), Lemmas 2.1,2.4 and Propositions 2.6–2.7; 98 Propositions 1–7; 99a Lemma 1, Theorems 2,4, Proposition 6; 99b Theorems 3.1–3.4,3.7,3.9–3.15 and Corollaries 3.5,3.6,3.8; 102b Theorem 1 and Propositions 3,9; 109 Theorems 1,3 and Lemmas 4–6; 116 Lemmas 1–3; 122a Proposition 1; 122b Theorem 1 and Proposition 1. Exact CA entries I:166565–166578. Additional (i) entries: 99a (1.19), 109 (3.37)–(3.50), 119 Theorems 1,2 and Corollary 3, I:166628–166637. |
| (iii-a,c,d) | 98 Proposition 2 and displayed averaging identities; 99a (1.3)–(1.6); 99b Theorems 3.1–3.11,3.15 and listed propagator formulas; 102b Theorem 1, Proposition 9, §§F–G; 109 Lemma 4 and §§2–5; 116 Lemmas 1–3, localised-term and cluster formulas; 119 Theorem 1, Lemma 4, Corollary 3 and induction bounds; 122a cube and stage conditions; 122b localisation and large-field bounds and Theorem 1. Exact formula lists II:60239–60274. |
| (iii-b) | 109 (0.24)–(0.26); 116 (1.26); 119 (2.49),(2.50); 122b p.355 and (0.1), II:64593–64601. The p.355 dependence is part of the last-scale-constants assumption, not an independent proof of it. |
| (ii) | 109 (0.1),(0.2), II:68339–68344. No further Balaban theorem is cited by statement in either torus branch, II:68346–68347. Lattice positivity and analytic compactness inputs are still present. |
| (iv) | 95 free-propagator formulas; 96 Propositions 2.3,2.6,2.7; 98 (19),(20); 99b decay formulas; 102b Theorem 1, Proposition 9 and analytic-response formulas; 109 small-field step, effective action and coupling theorem; 116 Lemmas 2–3 and cluster bounds; 119 Theorem 2, Corollary 3, regularity, step and running-coupling formulas; 122a history/creation formulas; 122b localisation and region bounds. Exact enumeration II:145537–145578. |
| (v) and (ii-T-a) | 102b Theorem 1 and Propositions 3,5,6,9; 116 Lemma 3; 99b Theorems 3.1,3.4,3.12,3.13 and regularity/propagator formulas; 109 Lemma 4 and (3.15); 98 Propositions 1,2,4,5; 99a Lemma 1 and Propositions 3,5; 96 Lemma 2.1 and (2.60)–(2.61); 122a and 122b stage, remainder and localisation formulas; 119 induction bounds. Exact enumeration III:75776–75823. |

The non-Balaban input lists remain unchanged: Combes–Thomas, Osterwalder–Seiler and Osterwalder–Schrader are outside this operator port. In particular no continuum reconstruction or mass-gap claim follows from the positive constrained matrices here.

## Source navigation and recovery

The initial navigation used `sa-index/README.md`, `ca-full/README.md`, `ca-4.12-4.19/README.md`, and chain-ca §§2.1, 6.1, 6.2, 7.2. Searches of the outline index included operator bounds, localised independence, uniform increment, local real base, uniform agreement, interior sufficiency, vertex formula, coercivity, covariance and averaging. Their CA labels are not the outline's labels. The relevant neighboring outline rows are chunk-04's A1–A4 obligations and chunk-10's propagator/response rows; obligations.md:105–116 and 731–746 retain their open scope. Bounded outline source reads included SA:3810–3907 and 10307–10352. The complete-account index and source, not those outline summaries, govern this port.

Primary proof ranges read: CA-I:19578–19867, 9615–9791, 46035–46171, 47253–48140. Necessary statement/definition reads include the local-data, vertex, resolvent, coercivity, agreement and interior-sufficiency passages in the A3 table; the printed inputs, chart clauses, increment, frames, glued-window and constant order passages in the A4 table; and the notation, prepared-data, background, block-size, reading-hull, symmetry, local-ball and unit-lattice passages in the A9 table. Inputs named only descriptively in the source remain P4-H hypotheses at their use loci.

Recovery decision: the three target implications are written below their exact statements. Before an outward use, check this text once with another model, check the current standing of ui.md and lrb.md, and supply the particular application’s retained hypotheses. Do not restart Balaban derivations as part of this port. No alternative proof route was attempted. The source's alternate Jensen/Poincaré proof was deliberately not substituted.

Source identities (SHA-256; bookkeeping only):

| File | SHA-256 |
|---|---|
| `sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `ui.md` | `c002a622c52db33f3db6e21819d575923671ed8a8fffdd0664eac5e3815e34c8` |
| `lrb.md` | `b69c630d51e0aece29c255803b99e62376170f2523258e88b46d81992597e57a` |
| `mu.md` | `2f3643c41fa8655a01ae8a6f7afa16c45f459bf41512c585acbeae63504a323b` |
| `chain-ca.md` | `5c3653be968613911d0afe5c40dfec070f39a205e5257acd38805d39a6642f79` |

## Result

**Statements ported:** `4.5:thm-operator-bounds` (A4), `4.4:cor-localised-independence` (A3), and `4.14:thm-operator-theorem` (A9), with their exact source statements and proofs of their implications on the account's route, with A4's localized exactness read in the corrected scope A4-C3. This is a conditional research port. It closes no cited Balaban input and establishes no status for T0.

**Filled steps:** A4-F1, all four chart norms and the current Taylor remainder; A4-F2, the strict current ceiling; A4-F3, the P1 norm and radius estimate; A4-F4, the two far terms and their tower read; A4-F5, the near-chart radius and factor 16. A3-F1, vertex evaluations; A3-F2, scalar/matrix logarithm and branch; A3-F3, absolute convergence and regrouping; A3-F4, domain admission and assembly. A9-F1, Schwarz/IMS error shares; A9-F2, analytic limits and symmetry; A9-F3, room for the gauge cube; A9-F4, sector bound and finite-dimensional invertibility; A9-F5, analytic symmetric inverse; A9-F6, the square completion; A9-F7, enlarged-list decay/locality; A9-F8, the local collar and cutoff; A9-F9, constant dependencies; A9-F10, transport through products and inverses; A9-F11, the Schur spectral bounds.

**Corrections:** A4-C1 repairs stale `(cf4)/(cf5)` references by the actual `(cf3)/(cf2)` displayed conditions. A4-C2 supplies the degenerate-radius interpretation when the printed maximum is zero. A4-C3 restricts the (F3) exactness inherited by (F5) to \(s\equiv1\), as required by K10; the unqualified all-\(s\) reading is not proved. None changes a positive-radius bound or any source constant. No mathematical correction to A3 or A9 is asserted. The unprinted four-condition assembly reference in A9 is recorded as the named P4-H-assembly hypothesis, not silently repaired or declared proved.

**Named hypotheses carried:** every row of the three input tables, including the actual activity/representation, one-family, positivity, domain, restriction, chart, frame, sheet-calculus, covariance and supply inputs; P4-H-prepared and separate (A2); all cited Balaban theorem instances and printed-sentence bundles at the loci in the frontier table. `ui.md` is a completion not yet checked; `lrb.md` is a proof being refereed, used with its retained premises. `mu.md` is frozen and was not redone. This text does not certify that a prepared history meets any of these hypotheses.

Written by hand by Codex. Shell/Python use was restricted to reading, source extraction, file editing and identity bookkeeping. No run discharges a proof step. **Not yet checked by another model.** Only `library/port/p4-operator.md` was edited; no prompt file, platform instruction, audit, ledger or frozen proof was changed.

## Change log (check, 2026-11-05)

Ported by Codex. Checked line by line by a fresh Claude session ([p4-operator-gate](../../gates/p4-operator-gate.md)): first failing step A4-F1 (L232), a naming repair with no route change; all three statements byte-identical to the source. Repairs recorded by the lead (Claude):

1. **A4-F1.** No second-derivative chart bound is printed: K4 says "No second derivative of a response is taken" (CA-I 14838), and the curvature-remainder lemma (14083–14096) prints a first-derivative bound only (their text has the same looseness at 19773). Repair: the lemma's term-by-term series argument (14128–14130) also gives a second-derivative constant; choose \(C_{F'}\) at least that large where it is fixed (19411). The printed ceiling \(\alpha_2\le1/(4C_{F'})\) then gives the 11/12 line.
2. A4 (F1): the increment lemma supplies "(i), (ii), the first member of (1.14), and (iv) in uniform form" (CA-I 19781–19786), as the source says.
3. A4-F5: the extra factor 4 is slack; \(16C^K_9|B'|\) holds.
4. A4-C1, A4-C2 correct; the stale labels (cf4)/(cf5) also occur at CA-I 19967–20082.
5. **A4-C3 correct and exposes no downstream gap**: every consumer of (F5) found (29354, 29409–29506, 30575–30600, remark 20132–20149) uses bounds only; the cluster expansion needs bounds and analyticity at \(s\), separation at \(s=0\), and the value at \(s\equiv1\).
6. A3: cite the coercivity lemma (CA-I 5950) for accretivity; add P\('_X\) membership of the hereditary representatives to the domain-inclusion hypothesis (needed for the L1 operators, 9488). A3's input A2 is "Proof outstanding" in their text; it stays a named input.
7. A9: the "four-condition assembly reference" (CA-I 47580–47584) points to no printed display in any of the four source files; it is likely the smallness of \(\nu_J=2c_{\mathfrak g}a_0^\oplus\) at the four J-vertex stages, unprinted. The "operator theorem with the hulls \(\widehat\square\)" cited in A9 (E)–(G), (K) is not printed either. Both stay named hypotheses (P4-H-assembly, P4-H-core). Display d's coarse order disagrees with the expanded order at 48066–48075; the port follows the expanded one.

Status: **checked port.** A4 faithful with repairs; A3 faithful; A9 faithful.
