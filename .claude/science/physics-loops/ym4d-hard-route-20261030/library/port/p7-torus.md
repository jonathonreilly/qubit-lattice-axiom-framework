# P7: Torus independence of the running coupling

Provenance: Codex (GPT-6 family; reasoning effort not exposed), 2026-11-05; checkout `1eec566345588742f2577288c15d6ba7c819c206`. Research text, not an audit; grants no status. Port of Ethan Sussman and Levent Alpoge's complete account at `31a47c543775`, with Claude and Codex as authors of their text. Credit also belongs to Tadeusz Balaban for the underlying renormalisation construction and cited inputs. This port is not yet checked by another model.

## Source and scope

This lane ports A14, `4.38:thm-torus-independence`, in
`theorem_0_complete_account_raw_I.tex:58187–58411` (hereafter CA-I).
It supplies hypothesis (h) of `4.19:prop-clause-zero`.
Every unproved input remains a named hypothesis.
All proof steps below are written mathematical arguments; no run discharges a step.

The requested workflow file `docs/ai_methodology/SCIENCE_WORKFLOW.md`
is absent from this pinned checkout. Its copy on the already available
`origin/main` was read through git, following the planning-branch entry point.
The lane follows the owner's narrower GOAL.md and FINISH.md instructions,
chain-ca.md A14 and §7.2, and the source indexes.
Existing `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex` are used for bounded excerpts.

## Exact source statement and declared standing

CA-I:58187 has no status qualification. CA-I:27–46 says that an unmarked
heading declares a proof in full, with named hypotheses retained.
CA-I:58413–58414 places the proof in the remainder of the section.
Thus the source standing is **proved implication**, not unconditional supply
of its premises. The following is the exact statement, including its label,
CA-I:58187–58411. The referenced definitions are unpacked below.

```latex
\begin{theorem}[Torus-independence of the localized terms]\label{4.38:thm-torus-independence}
Assume the following statements of this book:
\begin{itemize}
\item[(1)] independence of the localized terms from the small-field region
(Corollary~\ref{4.4:cor-localised-independence}), together with the interior sufficiency of the
whole-lattice setting (Lemma~\ref{4.4:lem-interior-sufficiency});
\item[(2)] the lemma on the walk expansion of the averaged Laplacian $\mathsf{A}$ on the base
class of data, with its statement that this expansion is determined by local data given on
the footprint of each walk, and with the accompanying lemma on single cells;
\item[(3)] the reflection and permutation covariance of the walk expansion of
$\mathsf{A}$, and, for the operators of $\mathbb{L}_1$ other than $\mathsf{A}$, the covariance
clause of the hypothesis of Definition~\ref{4.4:def-one-family-hypothesis};
\item[(4)] the operator bounds at free current;
\item[(5)] the large-field part of the coupling increment;
\item[(6)] the representation and bound of the large-field terms, together with the statements
used with it: the six-clause format of that representation; the description of the new
large-field region
in \cite[p.~390]{B-CMP122b}; the clause on points of the small-field region near an island
that lies outside the domain considered, an island being a first-class component of the
large-field region (Definition~\ref{4.38:def-non-wrapping}); the statement on the rounding of the
prepared large-field sequence up to cells; a lemma on the format of that representation, used
together with it; and those clauses of a further statement on that representation which concern
its format, the remaining clauses of that statement not being used. We assume also the
convergence and analytic extension of the expansions on the joined localization domains, used
here as stated in \cite[p.~192, (1.70)]{B-CMP122a} and
\cite[p.~377, (1.68)--(1.69)]{B-CMP122b}; the locality of the pieces of the renormalisation
operation is derived in the proof from the definitions of \cite[\S\S A, C]{B-CMP99b} and the
statements of this list;
\item[(7)] the locality of the rules that make or change a label and the clause on the
integrand at free bonds in the interior, both of Definition~\ref{4.38:def-standing-data}.
\end{itemize}

Let $j\ge1$, and assume the following hypothesis $(\mathrm{H}_j)$, which is the form in which the
induction on the level enters (it is not to be confused with the hypotheses (H1)--(H7) of
Theorem~0, Notation~\ref{2.2:not-hypotheses}).
\begin{itemize}
\item[(a)] The numbers $(g_i,\check R_i)_{0\le i<j}$ and $(\beta_i)_{1\le i<j}$ are defined
and site-free, that is, the same at every site $\mathfrak{s}=(m,K')$, and $x_i\ge\gamma^{-2}$
for these $i$.
\item[(b)] The renormalisation steps $1,\dots,j-1$ have been performed with these numbers at
every site $\mathfrak{s}\in\mathcal{S}_{j-1}$
(Definition~\ref{4.38:def-admissible-sites}), with two clauses of the clause set
$\mathfrak{i}(j-1)$ of the induction at level $j-1$: the flow clause $x_{j-1}>0$, and the clause
that the
step is taken at every site of $\mathcal{S}_{j-1}$ with the constant $E$ of
Definition~\ref{4.38:def-admissible-sites} set to $0$.
\item[(c$^{+}$)] Clauses (i), (ii)(a) and (iii) below hold at every level $i<j$ in place of $j$.
Moreover $f^{\mathfrak{A}}:=(f_i^{\mathfrak{A}},\beta_i^{\mathfrak{A}})_{i<j}$, where
$f_i^{\mathfrak{A}}$ is the family $\{E_{\mathfrak{s}}^{(i),\mathfrak{A}}(X;\cdot)\}$ of
$\mathfrak{A}$-marked localized terms at level $i$, belongs to the
class $\mathfrak{F}_{j-1}$ of volume-consistent families; in particular the bound
\cite[(2.29)]{B-CMP119} holds for the $\mathfrak{A}$-terms at every site, this property being
hereditary along the steps. For $\natural\in\{\cdot,\Re\}$ the clause asserted at the sites is
the last sentence of clause (ii)(a) at level $i$, the Euclidean clause.
\item[(d)] At every $\mathfrak{s}\in\mathcal{S}_j^{\flat}$ the whole-lattice step $j$
converges on the domain of \cite[(2.27)(ii)]{B-CMP119}. This step is the last logarithm in
\cite[(3.28)]{B-CMP119}, taken in the case in which the localization domains $\Omega_j$ and
$\Lambda_j$ are both the whole lattice torus, pointed as in
\cite[(3.37)--(3.42)]{B-CMP119} and expanded as in \cite[(3.44)--(3.47)]{B-CMP119} under the
walk-resummation rule $\mathcal{R}$. The radii are absolute, that is, not evaluated at any
coupling, for the $\mathfrak{A}$-terms; for the $\Re$-terms that domain is read as the tube at
the stand-in coupling $\tilde g:=g_{j-1}$ fixed in the induction on the level. Its terms
$E_{\mathfrak{s}}^{(j),\natural}(X;\cdot,z)$,
$X\in D_j(\mathfrak{s})$, $z$ a unit-lattice point of $X$, split, by the marking of the terms
that defines the two parts $\beta_j^{\mathfrak{A}}$ and $\beta_j^{\Re}$ of the coupling increment
(Definition~\ref{4.2:def-increment}),
into the two sub-families $\natural\in\{\mathfrak{A},\Re\}$, are analytic there. They are real
at real $(\mathbf{U},\mathbf{J})$. They are invariant under the
complexified gauge group $G^{c}$, in the sense of \cite[(1.19)]{B-CMP119}, which is
\cite[(2.27)(iii)]{B-CMP119}. Finally, on the polydisc
\begin{equation*}
\bigl\{\mathbf{U}=e^{iA}:\ \sup_X|A|<a^{\natural},\ \sup_X|\mathbf{J}|<a^{\natural}\bigr\}
\end{equation*}
about $(\mathbf{U},\mathbf{J})=(1,0)$, where $A$ denotes a $\mathfrak{g}^{\mathbb{C}}$-valued
lattice field on $X$ and is not the action functional, they
obey
\begin{equation*}
\bigl|E_{\mathfrak{s}}^{(j),\natural}(X;\cdot,z)\bigr|\le E_0^{\natural}e^{-\kappa d_j(X)},
\end{equation*}
with $E_0^{\natural}>0$, $a^{\natural}>0$ and $\kappa\ge2\kappa(d)$ independent of
$\mathfrak{s}$, $X$ and $z$.
\end{itemize}
For $j=1$, hypothesis $(\mathrm{H}_1)$ consists of: $g_0\in(0,\gamma]$; the cell-size
multiplier $\check R_0$ is given and site-free; and (d), with \cite[\S3]{B-CMP119} read at
$k=0$, where, by the lemma of this book
identifying the zeroth step of that analysis, it coincides with \cite[\S1]{B-CMP119}.

Then the following hold.
\begin{itemize}
\item[(i)] Let $\mathfrak{s}\in\mathcal{S}_j^{\flat}$, and let $X\in D_j(\mathfrak{s})$ be
non-wrapping (Definition~\ref{4.38:def-non-wrapping}) with lift $\hat X$. Then the function
$E_{\mathfrak{s}}^{(j)}(X;\cdot,z)$, read on $\hat X$, is intrinsic
(Definition~\ref{4.38:def-intrinsic-trace}) as an analytic function on the domain of (d): it
depends neither on $\mathfrak{s}$ nor on the lift. No operator, minimiser, partition function
or scalar of $\mathbb{T}_j(\mathfrak{s})$ occurs in it; the periodised objects occur only in
its argument. The functions $E^{(j)}(\hat X;\Phi,\hat z)$, $\hat X\in D_j^{\infty}$, so
defined satisfy
\begin{equation*}
E^{(j)}(\hat X+t;\tau_t\Phi,\hat z+t)=E^{(j)}(\hat X;\Phi,\hat z),\qquad t\in M\mathbb{Z}^4.
\end{equation*}
The same holds for $E^{(j),\mathfrak{A}}$ and for $E^{(j),\Re}$.
\item[(ii)] (a) Let $\mathsf{h}_{\mathfrak{s}}$ be the linearised minimiser-and-current map at
the site $\mathfrak{s}$, and let $\mathsf{h}_\infty$ be its walk-expansion limit. For points
$x,y,z$ of the unit lattice of $\mathbb{R}^4$ (read on $\mathbb{T}_j(\mathfrak{s})$ through
$p_{\mathfrak{s}}$ where the torus tensors are concerned), the series
\begin{equation}\label{4.38:eq-torus-independence-a}
\begin{split}
&\Pi_\infty^{(j)}(x,y,z)\\
&\quad:=\sum_{\hat X\in D_j^{\infty},\ \hat X\ni z}
\bigl\langle\partial^2E^{(j)}(\hat X;(1,0),z);\ \mathsf{h}_\infty\delta_x,\
\mathsf{h}_\infty\delta_y\bigr\rangle
\end{split}
\end{equation}
converges absolutely and decays exponentially in $|x-z|+|y-z|$.
Here $\delta_x$ denotes the function on the unit lattice equal to $1$ at $x$ and to $0$ elsewhere.

It is the pointwise limit, as $s_j(\mathfrak{s})\to\infty$ in $\mathcal{S}_j^{\flat}$, of the
torus tensors $\Pi_{\mathfrak{s}}^{(j)}(x,y,z)$. These are the tensors of
\cite[(3.50)]{B-CMP119}, with $E^{(j)}(X,U_j,z)$ replaced by the total
$E_{\mathfrak{s}}^{(j)}(U_j,z)$.

The two-point tensors $\sum_z\Pi_{\mathfrak{s}}^{(j)}(x,y,z)$ of \cite[(1.20)]{B-CMP109}
converge to
\begin{equation*}
\sum_z\Pi_\infty^{(j)}(x,y,z)=:\Pi_\infty^{(j)}(x-y),
\end{equation*}
which satisfies \cite[(5.10)]{B-CMP109}; it is the limit of the
expression \cite[(5.1)]{B-CMP109}.

For every Euclidean transformation $r$ of the unit lattice of $\mathbb{R}^4$,
\begin{equation*}
\Pi_\infty^{(j)}(rx,ry,rz)=(r\otimes r)\,\Pi_\infty^{(j)}(x,y,z);
\end{equation*}
in particular $\Pi_\infty^{(j)}$ is translation invariant.

All of this holds for $\mathfrak{A}$ and for $\Re$ separately. No rate of convergence is part
of the statement.

At each site $\mathfrak{s}$, let $\mathcal{E}^{\natural}_{\mathfrak{s}}(V,z)$ denote the total
of the terms of the sub-family $\natural$ at $\mathfrak{s}$ pointed at $z$ (all terms for
$\natural=\cdot$), evaluated at the minimiser determined by a regular configuration $V$ (a real
regular background, Definition~\ref{4.4:def-regular-backgrounds}). Then for every Euclidean
transformation $r$ of the unit lattice of $\mathbb{T}_j(\mathfrak{s})$,
\begin{equation*}
\mathcal{E}^{\natural}_{\mathfrak{s}}(rV,rz)=\mathcal{E}^{\natural}_{\mathfrak{s}}(V,z),\qquad
\natural\in\{\cdot,\mathfrak{A},\Re\}.
\end{equation*}
This is the Euclidean clause of a volume-consistent family at level $j$.

(b) The number $\beta_j$, defined as the coefficient \cite[(3.61)]{B-CMP119}, that is
\cite[(1.22)]{B-CMP109}, of $\Pi_\infty^{(j)}$, is well defined and real. It equals
$\beta_j^{\mathfrak{A}}+\beta_j^{\Re}$, and it is a function of $(g_0,\dots,g_{j-1})$ and of
the fixed parameters of the construction alone. Hence $x_j$ is site-free. Given $x_j>0$, which
is the flow
clause of the induction at level $j$, the numbers $g_j$, $\check R_j$, $\varepsilon_j$,
$\delta_j$, $k_1(j)$ of Definition~\ref{4.38:def-standing-data} and the class $\mathcal{S}_j$
are also site-free: they are the same at every site, and free of $m$ and $K'$.
\item[(iii)] Assume moreover that $x_j\ge\gamma^{-2}$ and that step $j$ has been completed at
every $\mathfrak{s}\in\mathcal{S}_j$. Then every term or operation of the representation
\cite[(2.18)]{B-CMP119} of $\rho_j$ that is localized in a non-wrapping $W$ is intrinsic
(Definition~\ref{4.38:def-intrinsic-trace}).

This includes the members carrying the coupling profile, namely
\begin{equation*}
-A(x_j(\cdot),\mathbf{U})\restriction W
\quad\text{and}\quad
-\beta_iA(h_z\varphi_i,\mathbf{U})\ \ (z\ \text{with}\ \operatorname{supp}h_z\subset W),
\end{equation*}
of \cite[(2.23)--(2.25)]{B-CMP119} and \cite[(3.65)]{B-CMP119}. Here
$x_j(\cdot):=1/g_j^2(\cdot)$ is the position-dependent inverse coupling of
\cite[(2.24)]{B-CMP119}, $h_z$ is the cut-off function attached to $z$ in these members,
and $\varphi_i$ is the coupling profile of the
label $\ell$
carried by the term. By
Lemma~\ref{4.38:lem-coupling-profile}, for $x$ the barycentre of a plaquette of $W$,
$\varphi_i(x)$ reads only the cells of
$[\Lambda_i(\ell)^c]_i$ within $\tfrac14a_i$ of $x$, and these lie in
$[x]_i^{+1}\subset W^{+1}$. In particular:
\begin{itemize}
\item[(a)] the terms $E^{(j)}(X;\cdot,z)$, $X\subset\Lambda_j$, $z\in\Lambda_j^0$, of every
label at $\mathfrak{s}$ are the functions of clause (i); here $\Lambda_j^0$ is the range of
$z$ in \cite[(2.26)]{B-CMP119};
\item[(b)] let $\ell$ be any label at $\mathfrak{s}$, and let $X\in\mathbf{D}_j$ be any
non-wrapping union of $M$-cubes, unions of cells included, with lift $\hat X$ and with
$X\subset\Lambda_j(\ell)^{\sim-1}$ (the union of the cells of $\Lambda_j(\ell)$ that touch no
cell of $\Lambda_j(\ell)^c$), the range of localization domains of
\cite[(2.30), p.~260]{B-CMP119}. Let $R^{(j)}(X;\cdot)$ be the term of
\cite[(2.30)]{B-CMP119} with localization domain $X$; it is the sum of
$R'^{(j),\ell}(X;\cdot)$, the term with localization domain $X$ in the logarithm of the
polymer expansion \cite[(1.90)]{B-CMP122b} at the label $\ell$, written as the series
\cite[(2.13)]{B-CMP116}, and of the remaining part
$R''^{(j)}(X;\cdot)$. Then
\begin{equation}\label{4.38:eq-torus-independence-b}
\begin{gathered}
R^{(j)}(X;\cdot)=R''^{(j)}(X;\cdot)+R'^{(j),\ell}(X;\cdot)=\mathfrak{r}^{(j)}(\hat X;\cdot),\\
\mathfrak{r}^{(j)}(\hat X;\cdot):=R''^{(j)}(\hat X;\cdot)+\mathfrak{r}'^{(j)}(\hat X;\cdot),\\
B'_{\mathrm{ann}}(X):=R'^{(j),\ell}(X)-\mathfrak{r}'^{(j)}(\hat X),
\end{gathered}
\end{equation}
where $\mathfrak{r}'^{(j)}$ is the series of $R'^{(j)}$ taken over the catalogue of the empty
trace, as in \eqref{4.38:eq-label-remainder-b}, read on the lift in the last line. The functions
$\mathfrak{r}^{(j)}(\hat X;\cdot)$ form one family, independent of $\mathfrak{s}$, of the lift
and of the label, and covariant under $\tau_t$ for
$t\in M\check R_j\mathbb{Z}^4$. The difference $B'_{\mathrm{ann}}(X)$ vanishes whenever the
trace of $\ell$ on $X^{+1}=[X]\cup(\text{the cells touching }[X])$ is empty, that is,
whenever $X$ belongs to the class $\mathcal{X}_j(\ell)$ of domains with empty trace of
\eqref{4.38:eq-label-remainder-b}. Since $\mathcal{X}_j(\ell)$ is exactly the range of
\cite[(2.30)]{B-CMP119}, as is shown later in this section, $B'_{\mathrm{ann}}(X)$ vanishes on the
whole range;
\item[(c)] the objects
\begin{equation*}
B^{(j)}(X;\cdot),\quad \mathbf{B}'^{(j)}(X;\cdot),\quad \mathbf{T}^{(j-1)}(\cdot\cap X)
\quad\text{with}\ W:=X,
\end{equation*}
and $\mathbf{T}'_j(X)$ with $W:=X^{\sharp}$ depend on $(\mathfrak{s},\text{label})$ only
through the trace of the label on $W^{+1}$; here $B^{(j)}(X;\cdot)$ is the term of
\cite[(2.42)]{B-CMP119}, and $X^{\sharp}$ is the strip of $X$
(Definition~\ref{4.38:def-standing-data}) on which the potential term of
\cite[(1.91)]{B-CMP122b} with domain $X^{\sharp}$, contained in $\mathbf{T}'_j(X)$, lives.
\end{itemize}
Consequently, under the additional hypotheses of this clause, and with the flow clause at
level $j$ and the step statement for volume-consistent
families at level $j-1$, parts (a)--(c$^{+}$) of hypothesis $(\mathrm{H}_{j+1})$ hold.
\end{itemize}
\end{theorem}
```

## Inputs, standing, and proof order

The theorem's seven assumptions and its separate level hypothesis are retained.
The following names expand them; they do not assert additional completed work.
An input cited here is assumed on **every** datum and domain where it is used.
Statements about common local data include admission on those data.

| Name | Content and source | Standing used here |
|---|---|---|
| P7-H1 | A3, `4.4:cor-localised-independence`, CA-I:9615–9791, and `4.4:lem-interior-sufficiency`, 9476–9582. Includes the local data classes, primed-radius membership, uniform agreement, hereditary restrictions, and the local positivity/coercivity hypotheses. | Checked [P4](p4-operator.md), A3, with the check-log additions. Its A2 input is supplied by refereed [lrb](../lrb.md), on lrb's premises. |
| P7-H2 | The form-walk hypothesis and single-cell statements in theorem assumption (2), CA-I:58193–58195; the one walk family (f1)–(f4), 5580–5700; the cell-resolvent clauses, 6219–6302; uniform agreement, 9355–9474. All local inverses, near/far selectors, and walks read their full footprints. | Named analytic hypotheses inherited through P4. In particular lrb retains the symmetry lemma, W′, cell resolvent/coercivity inputs, and CMP 116 bounds. |
| P7-H3 | Reflection/permutation covariance in (3), CA-I:58196–58198, including (f3). Also the closed-total covariance lemma and its hypotheses as listed at 58747–58756 and applied at 58915–58958; the closed-total identity for the unmarked subfamily at 58949–58956. | Named covariance/representation inputs. These concern totals on regular minimisers, not arbitrary local extensions. |
| P7-H4 | A4, `4.5:thm-operator-bounds`, CA-I:19578–19867, with all its hypotheses. | Checked P4, A4, including its repairs; [ui](../ui.md) is completed and checked. P4's cited and printed Balaban frontier remains attached. |
| P7-H5 | A6, `4.7:prop-beta-extraction`, 32226–32410, and `4.7:prop-coupling-increment`, 32412–32496. | Checked [P5](p5-induction.md), A6. Retain its kernel-power, composition, membership, vanishing-variation, and moment assumptions. In particular its recorded unrooted (A4) summation issue is not resolved by this port. |
| P7-H6a | A5 representation/bound and six-clause format; completion of missing action terms as whole-lattice members, including their vacuum convention; locality of V and island integrals; new region Z_j ∪ ⋃Y_b; assignment of foreign-island terms; prepared-sequence rounding; hereditary format clauses. CA-I:58201–58214, 59101–59114, 59339–59347, 59813–59835, 60111–60133. | Checked P5, A5, with checked [P1](p1-base.md). Its activity supplier, positivity dichotomy, widened-support statement, hereditary/domain and printed-locality hypotheses stay attached. The extra format and completion clauses named at these use sites remain hypotheses; C3 below uses completion as an identity of the entire local action member. |
| P7-H6b | Convergence and analytic extension on joined localisation domains, CA-I:58210–58212: Balaban CMP 122a p.192 (1.70), CMP 122b p.377 (1.68)–(1.69). | Assumed exactly as the source says; not supplied by abstract convergence of a different polymer gas. |
| P7-H6c | Strip and vacuum conventions; component separation, confinement of island/stage data, and the R'' localisation corollary. CA-I:56877–56930, 59345–59351, 59836–59855. Local terms and integrals are those of CMP 119 (2.18)–(2.42), CMP 122a (1.60)–(1.100), CMP 122b (1.14)–(1.48), (1.68)–(1.100). | Named construction/representation inputs. The elementary strip, profile, catalogue and gluing deductions used here are proved below. |
| P7-H7 | (L0)–(L5), `4.38:def-standing-data`, CA-I:56691–56965: the prescribed scheme, natural cut-offs, local label rules, exact walk rule, and only the stated characteristic function on free interior bonds. Includes the actual growth recursion (r1)–(r3), 57673–57689, and small-field separation used at 59108–59117. | Standing hypotheses of the construction. Locality of an arbitrarily chosen rule is not inferred from its name. |
| P7-Hnum | Odd L, powers-of-L partitions and multipliers, Ř_i ≤ L^(j−i)Ř_j, Ř_i ≥ L, and the clock inequality used at 58572–58587. Every scalar depends only on fixed parameters and already generated couplings. | Source standing numerical/geometry hypotheses, CA-I:56691–56755, 57027–57161. No future coupling is an input. |
| P7-Hwalk | At U=1, Balaban CMP 99b Theorems 3.10, 3.12 and (3.108), with uniform absolute walk tails, exponential response decay, and the finite-range current linearisation. CA-I:58734–58743, 58838–58860. | Cited operator input. Equality of its finite-footprint terms follows from P7-H2, not from decay alone. |
| P7-Hsum | The rooted-domain counting bound of CMP 109 (0.26), used at CA-I:58878–58879; the pointed-polarisation-sums lemma supplying the particular CMP 109 (5.10) estimate with its δ₁, used at 58985–58987. | Named bounds. P1 supplies checked polymer combinatorics within its scope. The particular δ₁ estimate is retained, not replaced by a newly chosen rate. |
| P7-Hextract | The exact coefficient normalisation and algebra identifying CMP 119 (3.57), (3.61) with CMP 109 (1.22), through CMP 119 (3.62)–(3.64). CA-I:59000–59005. | Named published algebraic identification, assumption (3) of `4.38:prf-increment-site-free`. Absolute convergence, reality, linearity and site independence are proved here. |
| P7-Hmin | Existence, analytic representatives, regular-orbit uniqueness, and covariance of the minimiser/current and the composite block map. The use site cites Balaban CMP 102b Theorem 1, CA-I:58930–58934. | [mu](../mu.md) and [oc](../oc.md) are proved and refereed, with their exact scopes and inherited Balaban inputs. They do not supply a new existence theorem beyond those inputs. |
| P7-Hnorm | The actual localisation/pointing formula, cancellation of the normalising partition function, and exact sum-preservation of walk, vacuum and strip normalisations. CA-I:58443–58449, 58601–58614, 59075–59082. | The A3 assembly inputs and named normalisation identities. The cancellation mechanism and preservation of each local comparison are written below. |
| P7-Hfamily | For the final propagation assertion: the step statement on volume-consistent families at the preceding level. Its detailed suppliers are the layer-bookkeeping corollary, the two family-propagation lemmas, and the covariance lemma, CA-I:60672–60680. | Explicit extra hypothesis of the theorem's final sentence. No next whole-lattice convergence clause is produced for free. |
| P7-Hlevel | Exactly (H_j)(a),(b),(c⁺),(d), CA-I:58219–58268; at j=1, its special base form at 58269–58272. | Earlier-level induction data, current whole-lattice convergence and uniform analytic bounds. These are assumed, not conclusions of A14. |

For prepared geometry, [pda](../pda.md) is completed and refereed: it proves
(A1) for one R-operation under the old-label (A1) and rule (C).
Its (A2), T-step/old-label supply and analytic conditions remain inputs.
P4's prepared-data uses have exactly this scope. P3 is a **checked port**
of free-field algebra, with its H-BG, H-TOWER, H1-MIN, H2-FLUX and H3-CONT inputs.
[P3](p3-free.md) is not used to replace the interacting response or extraction.
Thus all nine supplied notes have their owner-specified current standing;
older “not yet checked” sentences inside those notes are superseded by their check logs.

The source proof route is:
`prf-proof-non-wrapping` (58416–58730), `prf-polarisation-limit`
(58732–58988), `prf-increment-site-free` (58990–59086),
`prf-label-inherited` (59088–59318), `prf-label-remainder`
(59320–59615), `lem-range-empty-trace` (59617–59774),
`prf-label-activities` (59793–60101), `prf-label-boundary`
(60103–60234), then `cor-volume-families` (60672–60716)
and the step-order explanation (60718–60808).
All these headings are unqualified at their source lines. Their named premises
remain at the standing above. Sections below follow that route, preceded by
its elementary geometry and profile lemmas.

## Geometry, traces and profiles used by the proof

### Sites and common lifts

Use level-j units. A site is s=(m,K′), with K′≥j, and
\[
 s_j(s)=2L^{m+K'-j},\qquad
 \mathbb T_j(s)=\mathbb R^4/s_j(s)\mathbb Z^4.
\]
The admissible sets are exactly
\[
 \mathcal S_j=\{(m,K'):K'\ge j,
 L^{m+K'-i}\ge L^{11}M\check R_i\ (0\le i\le j)\},\qquad
 \mathcal S_j^\flat=\mathcal S_{j-1}\cap\{K'\ge j\}.
\]
They are cofinal: for fixed K′ there are only finitely many inequalities,
and increasing m eventually satisfies each one. Also
\(s_j/2\ge L^{10}M\check R_{j-1}\) on \(\mathcal S_j^\flat\).
Thus this class needs no \(\check R_j\), which is fixed only after extraction.
The additive vacuum constant E is zero during the induction, as in the source.

A domain is non-wrapping when it fits in a cube of side at most s_j/4.
A collar of width r≤s_j/16 then fits in a cube of side
\(s_j/4+2r\le3s_j/8<s_j/2\).
Within such a cube no coordinate difference can be shortened by adding a
nonzero period. Projection is an isometry and is injective.
It preserves grids, marks, bonds and all incidences, including corner contacts.
Two lifts differ by a deck translation. Fixing a lift of one point fixes the
lift of the domain: after aligning that point, their coordinate ranges lie
in intervals of length less than s_j, on which projection is injective.
Deck translations preserve the grids, since their sides divide s_j.
Subdomains remain non-wrapping at lower levels because both their diameters
and the torus side multiply by the same factor \(L^{j-i}\).
This proves the lift properties used from CA-I:57291–57371.

For tree lengths intrinsic to X, lifting and projection give inverse,
length-preserving correspondences between trees in X and its lift.
For the *unrestricted* tree lengths used by a walk's near/far selector,
use the source's `4.38:lem-tree-lengths`, CA-I:57552–57650, as follows.
If all target sets lift into \(Q=c+[0,a]^4\), \(a\le s/2\), define the
s-periodic map
\[
 f(u)=u\ (0\le u\le a),\quad f(u)=a\ (a\le u\le s-a),\quad
 f(u)=s-u\ (s-a\le u\le s),\qquad F(x)_\mu=c_\mu+f(x_\mu-c_\mu).
\]
Each piece has slope of modulus at most one, and the endpoint values agree.
Thus F contracts ℓ¹ length, fixes Q and maps every periodic copy of a target
set back to that target. Lift a torus tree, apply F, subdivide its finitely
many polygonal intersections, and remove cycle edges while retaining the
meeting points as vertices. This gives a tree in Q of no greater length.
Conversely project a Euclidean tree and perform the same cycle removal.
Taking infima proves equality of all three tree-length infima. In particular
the selector \(d(\omega)\le r'\) agrees on a common footprint; it cannot
silently select a different local resolvent on another torus.

**P7-F1 (filled): wrapping tails without assuming a minimizing tree.**
For a tree in X of length at most \(Md_j(X)+\epsilon\), lift the tree.
Each coordinate range has length at most that number. Each M-cube of X meets
the tree, so X fits in the projected cube enlarged by M on each side.
Let \(\epsilon\downarrow0\). If necessary choose a convergent subsequence of
cube centres in the compact torus; containment of the finite closed domain
passes to the limit. Therefore
\[
 X\text{ wrapping}\quad\Longrightarrow\quad
 d_j(X)>s_j/(4M)-2.                                      \tag{P7.1}
\]
This supplies the source's shortest-tree argument also when d_j is defined
as an infimum. It also shows that domains of bounded d_j containing a fixed
point fit in a fixed bounded cube. There are only finitely many such domains.

### One-cell traces

Cells at level i have side \(a_i=M\check R_iL^{-(j-i)}\).
P7-Hnum makes \(a_j/a_i\) an integer power of L. All partitions are compatible.
For a union W of fine cubes, [W]_i consists of the cells holding one of its
fine cubes; \([W]_i^{+1}\) adds all touching cells. Sharing and containment
are cube-wise. Merely meeting a boundary does not share a cube.
The trace records each label member's own cubes, the bond set I, and the marks.
It is not just an indicator of the large-field region.

Here is the source's rounding lemma, CA-I:57162–57289, with its proof.
For cells of side a indexed by n,n′,
\[
 \operatorname{dist}_\infty(Q_n,Q_{n'})
 =a\max\{|n-n'|_\infty-1,0\}.                         \tag{P7.2}
\]
Indeed the distance of two coordinate intervals is
\(a\max\{|n_\mu-n'_\mu|-1,0\}\), and the distance of products is their maximum.
A fine cube has one coarse parent, by coordinate division of its index.
Consequently W shares a fine cube with a union of coarse cells precisely
when [W] shares a coarse cell with it. Symmetry of touching then gives
\[
 W\cap Z^\sim=\varnothing\text{ cube-wise}
 \quad\Longleftrightarrow\quad
 [W]^{+1}\cap Z=\varnothing\text{ cell-wise}.           \tag{P7.3}
\]
A cell at distance <a from a fine cube of W has distance <a from its coarse
parent. Equation (P7.2) makes that distance zero, so it belongs to W⁺¹.
If W′⊂W and i≤j, a level-i cell touching [W′]_i has a level-j parent
that touches [W]_j. Hence
\[
 [W']_i^{+1}\subset[W]_j^{+1}.                         \tag{P7.4}
\]
Every point of W⁺¹ is within 2a_j of W: one cell for rounding and one for
touching. A cell outside W⁺¹ has index distance at least two from every
parent of a cube of W. Thus if W⁺¹ shares no cell with Z, every x∈W has
\(\operatorname{dist}_\infty(x,Z)\ge a_j\).
Translations by \(a_j\mathbb Z^4\) preserve all these operations.

Every member of a retained label lies in \(\Lambda_j^c\): nesting puts
\(\Omega_i^c,\Lambda_i^c,S_i\) there; P7-H7 puts tested/rejected data there;
P7-H6a confines retained histories to their regions Y_b there.
Conversely \(\Lambda_j^c\) is itself a member. Therefore the trace on W⁺¹
is empty precisely when W⁺¹ shares no cell with \([\Lambda_j^c]_j\).
For the converse with bonds on cell boundaries, use the trace convention:
a contributing bond has an interior point relative to W⁺¹. A small open
neighbourhood of that point meets the interior of a large-field cell within
W⁺¹. Distinct cell interiors are disjoint, so that cell is shared.
This is the argument of CA-I:57458–57528; boundary-only contacts are excluded
by the specified trace, not by assuming that closed cells are disjoint.

An intrinsic function uses only local fields, local grids and axes, the
fixed parameters, available scalar numbers, and this trace. Its construction
uses the natural rules in P7-H7. Relabelling all those data by a common lift
or a partition-preserving translation gives the same formula and the same
integration domains. This is the precise transport meant by “intrinsic”.

### Strips, product profiles, and gluing

Put \(m_\sharp=\lfloor(\check R_j-1)/2\rfloor\).
Since \(\check R_j\ge L\ge3\), \(m_\sharp\ge1\),
\(m_\sharp M<a_j/2\), and \(2m_\sharp\le\check R_j-1\).
An m_♯-layer strip lies within m_♯M of its core. Thus two cores separated
by a_j have strips separated by at least
\((\check R_j-2m_\sharp)M\ge M\).
The source's component/box assertion remains in P7-H6c; these inequalities
prove the separation consequence used here. Also
\((X^\sharp)^{+1}\) lies within \(2a_j+m_\sharp M<3a_j\) of X.
On \(\mathcal S_j\), \(s_j/16\ge L^{11}a_j/8\ge3a_j\), so its collar lifts.
First-class islands, with their collars, fit in cubes of side at most
106a_j<s_j/4. The last strict inequality follows from
\(L^{11}/2>106\) for odd L≥3.

Use exactly the profile of CA-I:56764–56774:
\[
 \eta_D(x)=1-\prod_{\mu=1}^4
 \psi_\varphi(\operatorname{dist}(x_\mu,D_\mu)/a_i),\qquad
 \varphi_i(x)=\prod_{D\subset[\Lambda_i^c]_i}\eta_D(x). \tag{P7.5}
\]
Here ψ is smooth, equals one on [0,1/8], and zero on [1/4,∞).
The composite with interval distance is smooth at the interval endpoints
because ψ is constant near zero. A factor differs from one only within a_i/4
of its cell. Near a fixed point, only its cell and touching cells can
contribute. The product is locally finite, smooth, and valued in [0,1].
It vanishes within a_i/8 of any bad cell and equals one beyond all a_i/4
neighbourhoods. Equation (P7.4) puts every cell it reads on W inside W⁺¹.
On the one-cell interior the distance to bad cells is at least a_i, so φ_i=1
even after an enlargement by 3a_i/4. The tent h_z has radius L^(−(j−i));
this is ≤3a_i/4, and hence h_zφ_i=h_z for interior z.

A grid-preserving motion permutes the factors and the coordinate distances,
so φ is natural. A disjoint union of cell lists splits the product exactly.
This gives the retained-label factor times the separate island factors,
including stage and prepared profiles. Round-ups of an island's finer-scale
sets stay within that island by grid compatibility.

**P7-F2 (filled): the ramp stays in the strip at the smallest allowed size.**
If a closed M-cube c contains a point at distance <a_j/4 from a cell-union S,
then \(n=\operatorname{dist}_\infty(c,S)/M\) is a nonnegative integer
with n<Ř_j/4. For odd Ř_j≥5,
\(n\le(\check R_j-1)/4\le(\check R_j-3)/2=m_\sharp-1\).
For Ř_j=3, n<3/4 gives n=0=m_♯−1. Thus c lies in S or its strip.
For a level-i set inside an island, a_i≤a_j gives the same conclusion.
This proves the profile/strip property at all allowed levels without a
finite enumeration. It is the case split in CA-I:58010–58032.

Finally \(x_{i-1}(x)=x_i(x)+\beta_i\varphi_i(x)\), so finite telescoping gives
\[
 x_j(x)+\sum_{i=1}^j\beta_i\varphi_i(x)=x_0,\qquad
 -A(x_j(\cdot),U)-\sum_{i=1}^j\beta_iA(\varphi_i,U)=-x_0A(U). \tag{P7.6}
\]
The same cancellation on an island collar is
\(-\beta A(h_z(1-\varphi),U)-\beta A(h_z\varphi,U)+\beta A(h_z,U)=0\).
Linearity in the plaquette weight proves both identities. Together with the
retained exact representation identities, they change no total. They do not
make individual island activities independent of ψ. This is precisely the
profile argument of CA-I:58047–58183.

For later catalogue gluing, port `4.38:lem-growth-factorise`,
CA-I:57669–57777. The assumed rule is
\[
 Z_{n+1}=\mathsf M(Z_n\cup\mathsf R_{n+1}^{\sim}),\qquad
 \mathsf R_{n+1}=\mathsf R_n\cup\mathsf T_n.
\]
Here M repeatedly replaces components by containing boxes, and tests read
within varpi<c_K of the current component, with c_K>1.
Consider two runs ending in non-touching regions Z¹,Z². At stage n their
regions lie in their final regions, separated by at least c_K.
No test neighbourhood or unit bond reaches both. The boundary tests, and
removal of previously tested sets, therefore split. Their answers and failed
sets split, so R_(n+1) splits. Enlargement commutes with union. Every box
created within either run remains within its final region, so boxes from the
two runs cannot merge. Induction gives exact union of the runs, including
when one has stopped. Products over tests and the sums defining their
exponents factor accordingly. For restriction to a final component, every
intermediate connected box stays in that component; the same induction gives
the restricted run. Thus gluing and restriction follow from the stated rule,
not from an assumption that arbitrary histories factor.

## Proof of (i): the non-wrapping whole-lattice family

This ports CA-I:58416–58730. Fix j, put k=j−1, and assume P7-Hlevel.
Form the whole-lattice step on each site in S_j^♭. No new coupling is used.
Localise and point each of the three CMP 119 (3.37) contributions as in
(3.41), using P7-Hnorm. For interpolation coordinates Δ the fundamental
theorem of calculus gives
\[
 \prod_{\Delta\in\sigma}(E_\Delta^1-E_\Delta^0)
 \prod_{\Delta\notin\sigma}E_\Delta^0 f
 =\sum_{\sigma'\subset\sigma}(-1)^{|\sigma\setminus\sigma'|}f(1_{\sigma'}).
                                                               \tag{P7.7}
\]
The evaluation operators commute, being in different coordinates.
At such a vertex an operator becomes
\[
 K^{W'}=\sum_{|\omega|\subset W'}K_\omega,\qquad W'\subset X.       \tag{P7.8}
\]
This is the actual rule in H2, not restriction of a global torus inverse.
The resulting convergent series with index X is the source's Ψ_X.
Its indices and scalar coefficients are incidences, Ursell/Mayer
coefficients, footprint hull assignments, and tents. Its ingredients are:

1. The restricted walks (P7.8), including propagators, minimiser operators,
   the averaged Laplacian, compressions, resolvents and square roots.
2. Local plaquette densities with weight x_k; monomials of P^(k); inherited
   \(E^{(i)}(X')-E^{(i)}(X';1)-\beta_iA(h_{z'},\cdot)\);
   and \(R^{(i)}(X')-R^{(i)}(X';1)\) for i≤k₁(k), all with X′⊂X.
3. The prescribed bond indicators at δ_k/g_k and unit Gaussian measures.
4. The t(Y), τ integrations and the one-bond surface insertion ∂_tχ_t.

In the whole-lattice setting every Λ_i is the whole torus, so (P7.5) is an
empty product and φ_i=1. Hence its action weight is the common number x_k.
For item 1, the walk words use fixed cut-offs, block-local maps and Dirichlet
inverses on the local determining cubes. P7-H2 identifies these words on
common lifted data. For the averaged Laplacian the coefficients are local
on their footprints. Cell resolvents use exactly those near walk terms
whose footprints lie in q^♯; the tree-length argument above identifies the
near/far choice as well. Products, sums, inverse-series words and branchings
are then identical. Their norm convergence is part of H2/H4.
This covers the source's full operator list:
\(G',(Q'G'^2Q'^*)^{-1},P,R,G_0,G\);
\((QGQ^*)^{-1},H,H_0,\widetilde G,G_1,H_1,\Delta^{(2)},\Delta^{(k)},\mathsf A\);
and \(C^{(k)}(Z_0),C^{(k)}(\Lambda),(C^{(k)})^{1/2},(u+\mathsf A)^{-1}\).
The small solutions H_k(B′), D,A₀ use the same component equations and
local data; local uniqueness/admission is in H1/H2/H4/Hmin.
Local minimisers use their determining domain as Ω₀. The block algebra
Q,C,h,D̃,b₀(c),z^(k)(c) and fixed profiles use the same local coordinates.

For item 2, (H_j)(a) identifies the scalar numbers. Each X′⊂X lifts at its
own level. By (H_j)(c⁺), its older E and R terms are intrinsic. At the empty
label each older R is exactly its empty-trace family r^(i). This uses only
i<j. Items 3 and 4 read identical bonds, thresholds and fixed integration
parameters. Gaussian variables outside the participating domain integrate
to one. The same is true of every universal incidence coefficient.

**P7-F3 (filled): cancellation is at fixed cluster support.**
The pointed quotient has the source form
\[
 N/D=\sum_{Z_0\ni b}H'(Z_0)
 \exp\{\log\Xi(Z_0^{\hat c})-\log\Xi(\mathbb T)\}.              \tag{P7.9}
\]
Expand each logarithm into its absolutely convergent connected-cluster
series, as supplied by Hnorm and Hlevel(d). A cluster all of whose polymers
are permitted in Z₀^ĉ has exactly the same coefficient and weight in both
logarithms. It cancels. Every remaining cluster meets the exclusion of Z₀.
Expanding the exponential therefore leaves only clusters attached to the
rooted object. Filing by the union of complete footprints gives the X-term.
Thus no scalar log Ξ(𝕋) survives in a fixed Ψ_X. One may first truncate the
absolutely convergent sums, cancel equal indexed terms, and take the limit;
the norm of any regrouping error is at most the omitted absolute tail.
This supplies the passage from (P7.9) to local ingredients, using the actual
quotient and compatibility convention in P7-Hnorm.

**P7-F4 (filled): exact reassembly of the infinite-lattice subtractions.**
The CMP 109/119 quadratic rewriting starts with a finite local expression
\[
 T_\square=\sum_{X''\subset\square^{\sim2}}
 E^{(i,2)}(X'')[H_i(\square_0)\cdot,H_i(\square_0)\cdot]
 -\beta_i\langle\partial H_i(\square_0)\cdot,
                \zeta_\square\partial H_i(\square_0)\cdot\rangle.
                                                               \tag{P7.10}
\]
It inserts the infinite-volume form and its complement, and writes
H_loc=H_∞+(H_loc−H_∞). Bilinearity produces exactly four terms; the three
containing H_loc−H_∞ are all retained. Splitting a domain sum into inside
and outside, and a point sum into its core and tail, is an identity.
Restoring those complements recovers (P7.10), including the counterterm.
The interpolation functional (P7.7) is linear, so this cancellation also
holds at each fixed interpolation index. Thus the infinite-volume objects
used in that rewriting do not add a nonlocal ingredient to Ψ_X. None of
the tails in CA-I:58622–58637 is discarded.

**P7-F5 (filled): equality on the full stated domain.**
Fix a common lifted datum in the domain of (H_j)(d). H1 and H6b ensure that
every local vertex and joined-domain expansion used above is defined there.
Match the series by its footprint, contents and interpolation indices.
Each matched term is equal, as are the parameter measures. The two sums are
therefore equal: for any ε>0 retain a finite collection with both omitted
absolute tails <ε, compare the finite sums, and let ε decrease to zero.
This applies at every datum of the stated domain. Where local compact
uniformity is used to differentiate, Cauchy bounds on a smaller compact
polydisc give the same tail argument. No extension of a local datum to a
global regular configuration, or uniqueness of an unspecified analytic
continuation, has been assumed. The source's analytic extension is H6b.

Define E^(j)(X̂;Φ,ẑ) by this common value. Every bounded lifted domain fits
on a sufficiently large site, by cofinality. Equality on common lifts makes
the definition independent of the chosen site.

For t∈Mℤ⁴ in level-j units, its level-k displacement lies in LMℤ⁴.
It preserves the M₁, m₄, L, M and LM partitions of the operator construction.
For inherited R terms at i≤k₁(k), P7-Hnum gives
\(M\check R_i\le L^{j-i}\). In particular Ř_i≤L^(j−i);
as both are powers of L, Ř_i divides L^(j−i). Thus the level-i displacement
\(ML^{j-i}\mathbb Z^4\) preserves its \(M\check R_i\) cell grid.
All other inherited E terms have their M-grid covariance from (H_j)(c⁺).
Transport each indexed ingredient and each integration variable.
This proves
\[
 E^{(j)}(\hat X+t;\tau_t\Phi,\hat z+t)=E^{(j)}(\hat X;\Phi,\hat z).
\]
It includes deck translations, hence independence of the lift.
Marking reads levels only, so the same matching proves the assertion for
𝔄 and ℜ separately. The global minimiser and the linear response h_s remain
arguments of these functions. In particular compressing a periodised
operator to X would not prove this conclusion: its nonzero image terms need
not vanish. The proof used its footprint-restricted walks instead. This
completes (i).

## Proof of (ii)(a): polarisation limit and Euclidean totals

This ports CA-I:58732–58988. Fix a marking ν∈{·,𝔄,ℜ}.
Let F_X(A,J)=E_s^(j),ν(X;(exp(iA),J),z). Work in these analytic coordinates;
addition below is in (A,J), not addition of group elements.
For the total ν=·, set a^·=min{a^𝔄,a^ℜ} and E₀^·=E₀^𝔄+E₀^ℜ.
The triangle inequality on that common polydisc supplies its bound from
the two bounds in (H_j)(d). The group here is SU(N), in particular SU(2)
for T0; its complexified Lie algebra is sl_N(ℂ).

**P7-F6 (filled): first variations and gauge representatives.**
Global constant gauge transformations fix (1,0). Their invariance makes
DF_X(0) an invariant linear functional on a direct sum of copies of
sl_N(ℂ), for the independent A and J slots. Such a functional is zero:
using the trace pairing, its coefficient commutes with every traceless
matrix, hence is scalar; its traceless component is zero. One can see the
commutant assertion directly by commuting with diagonal matrices, which
kills off-diagonal entries, then with matrix units, which equates the
diagonal entries. This holds for every copy separately. Thus DF_X(0)=0.
Differentiate the infinitesimal gauge identity
DF_X(q)v_λ(q)=0 in direction w at q=0. The term with DF_X(0) vanishes,
leaving D²F_X(0)[w,(dλ,0)]=0. The chain rule for evaluation at the minimal
orbit therefore reads only its linearisation: the second derivative of
its representative is multiplied by DF_X(0). Changes of analytic gauge
representative add an infinitesimal gauge direction, which the Hessian
annihilates. This proves the source's representative independence.
Consequently
\[
 \Pi_s^{(j),\nu}(x,y,z)=\sum_{X\ni z}
 D^2F_X(0)[\mathsf h_s\delta_x,\mathsf h_s\delta_y].              \tag{P7.11}
\]
Analytic representatives and convergence of the differentiated total are
read on Hlevel(d), Hmin and the bounds proved next.

At the identity the linearisation is
\(\mathsf h_s=(H_s,\mathsf D H_s)\), with D finite-range and
translation invariant. P7-Hwalk gives, uniformly in s,
\[
 |\mathsf h_s\delta_x(b)|\le C_h(j)e^{-\delta_0\operatorname{dist}(x,b)}. \tag{P7.12}
\]
The finite range of D preserves this form: if its range is r_D and its
absolute row sum is C_D, use
\(\operatorname{dist}(x,b')\ge\operatorname{dist}(x,b)-r_D\)
for its finitely many b′. The current bound is at most
C_D exp(δ₀r_D) times the H bound.

**P7-F7 (filled): the common walk limit.**
Fix finitely many output bonds and a lifted input x̂. Given ε>0, the uniform
absolute-tail estimate in Hwalk chooses a footprint cutoff so that all
walks escaping that cutoff contribute <ε at those bonds, on every site.
Choose both torus sides large enough to lift this cutoff cube. H2 matches
all walks inside it, with equal values. Their sums on the two tori differ
by at most 2ε. The local values are Cauchy. Summing the same finite walks
on ℝ⁴ and taking the tail limit identifies their limit as h_∞δ_x̂.
The bound (P7.12) passes to that limit, since torus distances to the fixed
bonds eventually equal lifted distances. This argument uses a uniform
absolute tail, not bare pointwise convergence of a walk series.

Put d=d_j(X), d_x=dist(x,X), d_y=dist(y,X), a=a^ν and E₀=E₀^ν.
The bounds in (H_j)(d) and (P7.12) give
\[
 |D^2F_X(0)[\mathsf h_s\delta_x,\mathsf h_s\delta_y]|
 \le C_\nu e^{-\kappa d-\delta_0(d_x+d_y)},\qquad
 C_\nu=4E_0a^{-2}C_h^2.                                      \tag{P7.13}
\]
**P7-F8 (filled): the factor four and open radii.**
For directions u,v of norms U,V on X, use the bidisc
\(|s|<(1-ε)a/(2U)\), \(|t|<(1-ε)a/(2V)\) in
F_X(su+tv). Its image lies inside the given radius. The two Cauchy integrals
bound the st coefficient by 4E₀UV/((1−ε)²a²) times exp(−κd).
Let ε↓0. If U or V is zero the bilinear expression is zero. Insert (P7.12).
This also treats repeated directions, with no missing factorial.

For z∈X the tree geometry gives
\(|x-z|\le d_x+Md+2c_dM\), and the same inequality for y.
The additive cube diameter is needed even for d=0.
With \(\delta'=\frac14\min\{\delta_0,\kappa/M\}\),
\[
 \delta'(|x-z|+|y-z|)
 \le\delta_0(d_x+d_y)+\tfrac12\kappa d+4c_dM\delta'.
\]
P7-Hsum gives \(\sum_{X\ni z}e^{-\kappa d_j(X)/2}\le K_0\).
Summing (P7.13) therefore yields, on every torus and on ℝ⁴,
\[
 |\Pi_s^{(j),\nu}(x,y,z)|\le
 C_\nu K_0e^{4c_dM\delta'}e^{-\delta'(|x-z|+|y-z|)}.             \tag{P7.14}
\]
In particular all the displayed series are absolutely convergent.

Fix lifted x̂,ŷ,ẑ. On a non-wrapping X, (i) identifies its Hessian with
the fixed finite-dimensional Hessian on X̂. Its two arguments converge
by F7, so its summand converges. The absolute bound is
C_ν exp(−κd_j(X̂)), summable independently of the site.
Lifting through ẑ bijects the non-wrapping domains with lifted domains
containing ẑ and fitting in a cube of side s_j/4. Every fixed bounded
domain belongs to that class eventually. By (P7.1), the wrapping contribution
has the explicit bound
\[
 C_\nu K_0\exp\{-\tfrac12\kappa(s_j/(4M)-2)\}\longrightarrow0. \tag{P7.15}
\]
**P7-F9 (filled): passage between changing index sets.**
Choose a finite subset of lifted domains with omitted majorant sum <ε.
For all sufficiently large sites it fits, and its finite sum converges.
The omitted non-wrapping terms are bounded by ε; the wrapping sum tends to
zero by (P7.15). Applying the same ε bound to the omitted infinite series
proves the asserted pointwise limit, independently of the cofinal exhaustion.
The same argument and (P7.14) prove the exponential bound for Π_∞.
No rate for the full convergence has been asserted.

For Euclidean covariance use *totals on regular minimal configurations*.
The exact re-summation in Hnorm/H3 identifies
\(\Phi_s^\nu(V,z)=\sum_{X\ni z}E_s^{(j),\nu}(X;(U_j,J_j)(V),z)\)
with the closed CMP 119 (3.37),(3.41) expression. H3's covariance lemma
applies with the scheme/attachment conditions, earlier bounds (2.29),(2.32),
and the reflection norm clause (f3). The marked 𝔄 total has the corresponding
closed expression and the bound supplied by \(f^{\mathfrak A}\in\mathfrak F_{j-1}\).
The ℜ identity follows by subtraction from the full total.

For completeness, the minimiser-orbit part of that application is as follows.
P1's checked Wilson invariance gives A(rU)=A(U). The assumed composite
block map commutes with r. Hence r maps a regular minimiser over V to a
regular minimiser over rV; regular-orbit uniqueness identifies that orbit.
Gauge invariance removes the choice of representative. Changing integration
variables and permuting the sums in the closed expression, with H3, gives
\(\Phi_s^\nu(rV,rz)=\Phi_s^\nu(V,z)\).
Each unit-lattice Euclidean motion has signed-permutation linear part, so
it normalises s_jℤ⁴ and descends to the torus. Differentiating the identity
twice yields
\[
 \Pi_s^{(j),\nu}(rx,ry,rz)=(r\otimes r)\Pi_s^{(j),\nu}(x,y,z).
\]
Here r⊗r denotes its linear action on the tensor indices. Taking the
pointwise limit proves the same identity for Π_∞, including unit translations.
This argument does not claim unit-translation covariance for each off-minimal
local extension; (i) asserts only the M-grid covariance for that extension.

Finally write w=y−z and choose the representatives
\(-s_j/2<w_\mu\le s_j/2\). Translation covariance gives
\[
 \sum_z\Pi_s^{(j),\nu}(x,y,z)
 =\sum_w\Pi_s^{(j),\nu}(x-y+w,w,0).                            \tag{P7.16}
\]
Each summand is bounded by Ce^(−δ′|w|). This is summable on ℤ⁴:
the shell |w|_∞≤n has at most (2n+1)⁴ points, and a fixed polynomial times
e^(−δ′n) is summable. For example e^(δ′n/2)≥(δ′n/2)^6/6!
bounds its tail by a constant times e^(−δ′n/2). Extend each finite torus sum
by zero outside its representative box. A finite-box/tail argument exactly
as in F9 passes its limit through the w sum. Translation invariance then
converts that limit to \(\sum_{\hat z}\Pi_\infty(x̂,ŷ,ẑ)\), a function of x̂−ŷ.
P7-Hsum's pointed-sum lemma supplies the *particular* CMP 109 (5.10) bound
with its δ₁; it is explicitly retained. Independently, (P7.14) already gives
exponential decay of this sum, since
\[
 e^{-\delta'(|x-z|+|y-z|)}
 \le e^{-\delta'|x-y|/2}e^{-\delta'|x-z|/2}.
\]
This finishes every assertion of (ii)(a), including its site Euclidean clause.

## Proof of (ii)(b): extracting the common increment

This ports `4.38:prf-increment-site-free`, CA-I:58990–59086.
The coefficient is **the same functional** of Π_∞ used in CMP 119 (3.61),
equivalently CMP 109 (1.22). Its equality with that normalisation is
P7-Hextract. We do not select a different scalar coefficient.

**P7-C1 (correction): the source of translation invariance.**
CA-I:59018–59019 attributes translation invariance to (H_j)(d). That clause
states convergence, analyticity, gauge invariance, reality and bounds;
it does not state Euclidean covariance. Use the just-proved (ii)(a),
specifically `prf-polarisation-limit` (d), instead. The theorem's H3 input
and the preceding-level Euclidean clause supplied that proof. This repairs
the reference without adding a new symmetry premise.

The pointed second-moment tensor is independent of its pointing z:
translate every summation variable by −z and use (ii)(a).
Reflections and permutations, transversality from F6, and the pointed-sum
identity (P7.16) are precisely the hypotheses of the reduction in Hextract.
All second moments are finite by (P7.14). Indeed their absolute sums are
bounded by products of sums of a degree-two polynomial times an exponential;
the shell argument following (P7.16) applies after increasing the polynomial
degree. Thus every rearrangement required by the coefficient identity is
legitimate. Its coefficient β_j is well defined.

**P7-F10 (filled): reality, splitting and absence of a future input.**
On real coordinate directions F_X is real, so its second derivatives are
real. The response at real data is real. Equations (P7.11) and its absolute
limit give real Π_∞, and the real moment functional of Hextract gives real
β_j. Differentiation, summation and the coefficient functional are linear.
Since E=E^𝔄+E^ℜ with separately convergent sums,
\(\beta_j=\beta_j^{\mathfrak A}+\beta_j^{\Re}\).
Its only arguments are D_j^∞, the intrinsic E^(j), and h_∞.
Their scalars are \((g_i,\beta_i,\check R_i)_{i<j}\) and fixed parameters.
Replace \(\beta_i\) by \(g_{i-1}^{-2}-g_i^{-2}\) and each Ř_i by its
prescribed function of the prefix. This gives dependence on
\((g_0,\ldots,g_{j-1})\) and fixed parameters alone. Neither the side,
the cutoff K′, g_j nor Ř_j enters.

It follows that \(x_j=x_{j-1}-\beta_j\) is common to every site.
If x_j>0, define \(g_j=x_j^{-1/2}\) using the positive root. Hnum then
fixes Ř_j, ε_j, δ_j and k₁(j) from the same common prefix.
The displayed inequalities defining S_j are consequently common as well.
No positivity assertion is inferred from site independence.

The source also explains why exact normalisations do not change this scalar.
Under Hnorm the pointed torus tensor is the second variation of an unchanged
total. Its large-volume limit and coefficient therefore agree. The profile
cancellation (P7.6) proves the same fact for profile changes. The 𝔄 part
has no island profile; the ℜ part is the difference from the full total.
Thus this reasoning preserves the split too. It does not identify individual
activities produced by different profiles.

## Proof of (iii): local terms and operations at every label

Now assume the theorem's additional hypotheses: x_j≥γ⁻² and completion
of step j at every s∈S_j. All scalar and cell choices of level j are already
fixed. We first treat T-produced objects, then the R-operation.

### The profile members, the interior terms, and inherited domains

This follows `prf-label-inherited`, CA-I:59088–59318.
For a plaquette p⊂W, (P7.5) reads only bad cells within a_i/4 of its
barycentre. By (P7.4) those cells lie in W⁺¹. Telescoping gives
\[
 -A(x_j(\cdot),U)|_W=-x_0A(U)|_W+
                    \sum_{i\le j}\beta_iA(\varphi_i,U)|_W.
                                                               \tag{P7.17}
\]
Each term therefore reads fields on W and the label trace on W⁺¹.
For −β_iA(h_zφ_i,U), the hypothesis supp h_z⊂W is essential.
It puts every contributing plaquette in W, and its profile reads the
same enlargement. This proves the profile-members clause of (iii).

For non-wrapping X⊂Λ_j, H1 compares the actual interior series with the
whole-lattice series. Interior sufficiency admits the local data directly.
Thus domains encircling a hole require no whole-lattice label with the same
trace. If X meets an island healed by R, H6a's completion rule inserts
exactly the missing whole-lattice term, with the prescribed vacuum value.
Both cases give the E terms of (i).

The inherited R vertices in a term retained from the T-produced action
need their one-cell domain condition. First let X⊂Λ_j^T. For i<j and
X′⊂X we prove
\[
 [X']_i^{+1}\subset[X]_j^{+1}\subset\Lambda_i(\ell).             \tag{P7.18}
\]
The first inclusion is (P7.4). For a T-produced label the second is the chain
\[
 [X]_j^{+1}\subset(\Lambda_j^{T})^\sim
 \subset\Omega_j^{T}\subset\Lambda_{j-1}^{T}\subset\Lambda_i^{T}.
                                                               \tag{P7.19}
\]
The first step uses X⊂Λ_j^T, a union of cells. The second uses the
small-field rule \((\Omega_j^c)^{\sim2}\subset\Lambda_j^c\) in H7:
one of the two spare layers suffices. The third follows from
\(\Omega_j^T\subset((Z'_{j-1})^{\sim5})^c\), since
\(Z'_{j-1}\supset Z_{j-1}=\Lambda_{j-1}^c\).
The last is the retained nesting in H6a.

**P7-F11 (filled): inherited versus completed terms after healing.**
Healing enlarges each Λ_i, by H6a's construction and nesting statements.
For X⊂Λ_j^T, (P7.19) still puts [X]_j⁺¹ inside Λ_i^T⊂Λ_i(ℓ).
Thus (P7.18) holds for every term retained from that action.
Every level-i cell of [X′]_i⁺¹ is then contained in Λ_i.
It contains no bad fine cube. Hence X′ has empty trace at level i and
lies in that level's one-cell interior. By (H_j)(c⁺),
\(R^{(i)}(X')=\mathfrak r^{(i)}(\hat X')\).
This applies to the older R terms inside E, i≤k₁(k), and the additional
vertices inside R'', k₁(k)<i≤k=j−1. Both ranges are strictly below j.
H6c's localisation corollary therefore identifies R''^(j)(X) with the
whole-lattice member when X⊂Λ_j^T.

**P7-C3 (correction): completion replaces the post-healing cell assumption.**
CA-I:59279–59301 writes Λ_j as the old small-field region plus whole healed
islands, and uses [X]_j⊂Λ_j for X⊂Λ_j. The cell argument applies if those
added pieces are whole cell-components. The declared retained geometry
also permits residual regions Y_b and sets that are only unions of M-cubes;
this is explicit at CA-I:59619–59642. Nesting and the
cell partitions alone do not establish [X]_j⊂Λ_j in that case.
We do not assert that stronger intermediate chain for every post-R domain.

The completion premise already assumed in H6a, CA-I:59101–59108 and
59196–59203, gives the needed conclusion directly. Here are the two cases.
If X⊂Λ_j^T, use F11. Otherwise X⊂Λ_j(ℓ) contains a newly admitted fine
cube. The new-region description puts that cube inside an island of the
R-operation. The action member with this domain is consequently one of
the missing members supplied by completion. H6a identifies the **entire**
member, with its vacuum convention, with the whole-lattice member.
In its formula the older R vertices are the empty-label members used in
the whole-lattice construction of (i); their admission is Hlevel, and
their identity is (H_j)(c⁺). There is no substitution of an actual-label
R vertex from an unproved one-cell interior. This argument applies to the
completed E and R'' members alike. It also covers a domain crossing the
boundary between the old small-field region and a partially healed island.

These cases exhaust X⊂Λ_j(ℓ), and prove the E identification and the
label-free R'' identification needed by the theorem. In other occurrences
of older terms (island activities and boundary operations) we need their
trace-locality, not empty trace; that is the already available clause (iii)
at i<j. Thus the stronger general chain in `prf-label-inherited` (c) is
unneeded. This repair retains the source's completion input in full; it
does not deduce completion from a bound or from geometric nesting.

**P7-F12 (filled): current-level T terms precede current-level R terms.**
Before the R-operation, the T-produced boundary term has the source form
\(B^{(j)}(X,(U,J),A,\{S_i\cap X\})\), CMP 119 (2.42).
Its local fields and S_i∩X are fixed by the trace. Each older member of
its defining list has domain X″⊂X and reads [X″]_i⁺¹⊂X⁺¹ by (P7.4).
Its walk factors, profiles, cut-offs, counting factors and reference
measures are those already handled, with their definitions in H6a/H7.
Thus B produced by T is intrinsic before any R′^(j) activity is used.
Likewise CMP 119 (2.19)–(2.21) factorise the inherited T-operation over
its components. Its restriction to X uses those same local ingredients
and the older-level hypothesis. This establishes the current-level T
input of `prf-label-activities` (f), CA-I:59863–59869, in the order
specified at CA-I:60756–60765. It does not assume the result for the
current R-operation in order to prove that result.

### The catalogue and the logarithmic series R′

Port `prf-label-remainder`, CA-I:59320–59615. H6a identifies R′ as
\[
 R'^{(j),\ell}(X)=\sum_{n\ge1}\frac1{n!}
 \sum_{\substack{X'_q\in\mathcal C_j(X;\ell)\\\bigcup_qX'_q=X}}
 \rho^T(X'_1,\ldots,X'_n)\prod_{q=1}^nF_\ell(X'_q).             \tag{P7.20}
\]
P1/P5 supply the checked logarithm deduction on the assumed activity bounds.
The series is the actual CMP 122b (1.90) gas, written as CMP 116 (2.13);
it is not an abstract gas chosen to have the desired locality.
The coefficient ρ^T depends only on incidence.
A catalogue element is a polymer X′⊂X with island/history contents
\(\{(X_a,\mathfrak h_a)\}\) and a finite family of interaction domains Y.
Its exact tests are:

- (c1) Each island/history is first-class in its own right, with the source's
  size and domain conditions, and its own growth run.
- (c2) Distinct islands do not touch, and every X_a^♯⊂X′.
- (c3) No island touches a bad cell of the retained label, with cells read
  by the prescribed round-up when necessary.
- (c4) Each Y∈D_j lies in X′ and meets Z^♯ in a union of whole components,
  at least one, where \(Z=\bigcup_aX_a\cup\bigcup_bY_b(\ell)\).
- (c5) Vacuum values are attached to the strips X_a^♯ and Y_b^♯ as in H6c.

Necessity is the first-class, strip, compatibility and vacuum format of H6a.
For sufficiency, the growth gluing/restriction proof above says that (c1)–(c3)
are exactly the admissibility of the combined pre-R label with these
first-class components. The cross-component seed restrictions add nothing:
a seed within six layers of an old coarse region would lie within its
new ten-layer enlargement, since the rule adds 4+1+1+2+1+1=10 layers.
Nesting would place it in Λ_j(ℓ)^c, contradicting (c3).
The remaining format conditions are precisely (c4)–(c5) by H6a/H6c.
The label sum ranges over arbitrary allowed unions; it contains each
resulting admissible contents. Hence this is the actual catalogue.

**P7-F13 (filled): no unseen component enters the catalogue.**
Condition (c3) reads cells touching an island inside [X], all in X⁺¹.
If the strip of a labelled cell meets an M-cube of Y⊂X, their distance is
at most m_♯M<a_j. Equation (P7.2) puts that cell in X⁺¹, even if it does
not touch X itself. Thus every labelled strip that can meet Y is seen.
To decide whether a seen component is wholly contained, take its class K₀
of marked touching cells in X⁺¹. If K₀^♯⊂Y, then K₀⊂X⊂[X]. Every cell
adjacent to K₀ is therefore in X⁺¹. Were the global marked component
strictly larger, a finite touching path from K₀ to its complement would
have a first adjacent marked cell outside K₀. That cell is seen, contradicting
maximality of the trace class. Hence K₀ is the whole component.
If a seen class that meets Y fails this containment test, the global
component cannot satisfy (c4). These two cases decide (c4) from the trace.
The vacuum attachments in (c5) use exactly the same contained components.
Conditions (c1)–(c2) concern the contents themselves, not unseen label data.
Thus equal traces on X⁺¹ give equal catalogues, including their marks.

The source sentence at CA-I:59573 uses “contained” as a transitive verb:
its intended inclusion is \(K_0\subsetneq Y_b\). F13 makes that inclusion
explicit. This is a filled step, not a correction to that sentence.

Define \(\mathcal X_j(\ell)\) by empty trace on X⁺¹, and define
\(\mathfrak r'^{(j)}(X)\) by (P7.20) with the empty-label catalogue.
For X∈𝒳_j(ℓ), equal traces imply
\(\mathcal C_j(X;\ell)=\mathcal C_j(X;\emptyset)\).
This proves index equality. Equality of activities is proved separately below.

### The second-group range is exactly the empty-trace range

This ports `4.38:lem-range-empty-trace`, CA-I:59617–59774.
Put \(Z=[\Lambda_j(\ell)^c]_j\).
By definition \(\Lambda_j^{\sim-1}\) is the union of cells outside Z^∼.
A fine cube of X lies in this interior exactly when its parent does.
By symmetry of touching, (P7.3) gives
\[
 X\subset\Lambda_j(\ell)^{\sim-1}
 \ \Longleftrightarrow\ X^{+1}\text{ shares no cell with }Z
 \ \Longleftrightarrow\ X\in\mathcal X_j(\ell).                 \tag{P7.21}
\]
The second-group condition in CMP 122b p.390 is the same condition:
H6a gives \(\Lambda_j^c=Z_j\cup\bigcup_bY_b\).
Both rounding and adjoining touching cells commute with unions, so
\[
 ([\Lambda_j^c]_j)^\sim=([Z_j]_j)^\sim\cup\bigcup_b([Y_b]_j)^\sim.
\]
Sharing no M-cube with its right side is exactly the first condition in
(P7.21). The convention is cube-wise disjointness; point-wise disjointness
of closed sets would erroneously remove another boundary layer.
In cell indices, (P7.21) says distance at least two, not at least three.
Every point of X is then at distance at least a_j from Λ_j^c, by (P7.2).

**P7-F14 (filled): all lower-level data are absent as well.**
Empty trace gives X⁺¹⊂Λ_j. Nesting gives
\(X^{+1}\subset\Lambda_j\subset\Omega_j\subset\Lambda_i\subset\Omega_i\)
for i<j. A level-i cell lying in X⁺¹ contains no bad fine cube of either
level-i region. The tested and historical members are also absent by the
trace argument already proved. Thus comparison with the empty label does
not discard an older datum while keeping only current-level emptiness.

### Activities, prepared profiles and termwise equality

This ports `prf-label-activities`, CA-I:59793–60101.
By H6a, F(X′) is the actual CMP 122b (1.91) integral operation built from
island operations T′_j(X_a) and interaction terms V(Y), with X_a^♯,Y⊂X′.
We identify every ingredient's reading set before taking the logarithm.

1. Integration variables lie in their islands. The domains, measures and
   cut-offs are fixed by that island's own history and the retained trace.
2. Operators use the footprint rule with footprints inside Y.
   Their Dirichlet pieces use the local determining sequence on the
   stated cover cube; its complete footprint is part of Y. H2 and H6a
   identify them on matching data.
3. The prepared, stage, pre-R and retained coupling profiles all use (P7.5).
   The source's prepared coupling is g''_k=g_k^(N), with k=j here;
   its new retained coupling is the function of CMP 122b p.365.
   The action-difference terms
   \(A((g_k^{(n+1)})^{-2}-(g_k^{(n)})^{-2},\cdot)\)
   from CMP 122a (1.62) are retained in B''_k, not dropped.
   Factor each profile into its non-island part and island parts by (P7.5).
   The non-island part reads [Y]_i⁺¹⊂[Y]_j⁺¹. Its extra prepared/stage
   factors from \([Z''_i\cap Y_b]_i\) differ from one only in Y_b^♯.
   An island part, including any prepared/stage part, differs from one
   only in X_a^♯, by F2. Since distinct strips are separate components,
   (c4) forces every such strip that meets Y to be wholly contained in Y.
   Hence exactly those islands contained in Y can affect V(Y).
4. Older terms with X″⊂Y read [X″]_i⁺¹, inside [Y]_j⁺¹ by (P7.4).
   For i<j this is (H_j)(c⁺). For current-level T terms it is F12 and
   the R'' result above. No current R′ output is used as an input.
5. Counting coefficients N^(i) use the common fixed numbers and the
   contained local domains.
6. The source's averaged trees are built with the fixed axes and the
   hyperoctahedral average. Transport permutes the finite average, so
   it is intrinsic with the same contents.
7. H6c attaches only vacuum values of terms whose domains are contained
   in Y. Their own hypotheses and the preceding items identify those
   values; no external-volume vacuum normaliser is inserted.

All label reading sets are contained in [Y]_j⁺¹⊂X⁺¹. In particular
when T′_j(X_a) occurs here, X_a^♯⊂X′⊂X implies
\((X_a^\sharp)^{+1}\subset X^{+1}\).
Matching the histories, fields and local integration variables identifies
activities for equal traces. H6b/Hlevel supply convergence and analyticity
on the joined domain. The finite-sum/absolute-tail argument of F5 therefore
identifies (P7.20) as analytic functions, not only as formal expressions.
Thus R′^(j),ℓ(X) is intrinsic with reading set X⁺¹.

**P7-C2 (correction): round-ups require the rounded target.**
CA-I:60035–60042 argues that cells of \([\Lambda_i(\ell)^c]_i\)
lie in \(\Lambda_j(\ell)^c\). The latter need not be a union of level-j
cells after R. The sufficient, always valid inclusion is
\[
 [\Lambda_i(\ell)^c]_i\subset[\Lambda_j(\ell)^c]_j.             \tag{P7.22}
\]
Indeed each cell on the left holds a bad fine cube. Nesting puts that cube
in Λ_j^c, and compatibility puts its level-i parent inside its level-j
parent, which belongs to the right side. The same parent argument applies
to stage sets inside Y_b. This replaces the overstrong inclusion only;
it leaves the empty-trace conclusion and its range unchanged.

Now take X∈𝒳_j(ℓ). By F14, or directly (P7.22), none of the non-island
profile cells are read on X⁺¹. All non-island factors are one on X,
as under the empty label. Island factors are identical because the paired
catalogue element has identical island contents and histories. The small-field
cut-offs agree: no Y_b meets X, since Y_b⊂Λ_j^c and X⁺¹ has empty trace.
The remaining six types of ingredients agree by their just-proved locality.
Virtual islands in the catalogue are still present; empty *retained* trace
does not erase them. Thus activities agree term by term, and
\[
 R'^{(j),\ell}(X)=\mathfrak r'^{(j)}(\hat X),\qquad
 B'_{\rm ann}(X)=0,\qquad
 R^{(j)}(X)=R''^{(j)}(\hat X)+\mathfrak r'^{(j)}(\hat X)
          =\mathfrak r^{(j)}(\hat X).                          \tag{P7.23}
\]
Equation (P7.21) shows that this is the **whole** range of CMP 119 (2.30),
including unions of M-cubes that are not cell-unions.

The empty-trace construction reads at most the collar
2a_j+m_♯M<3a_j, which lifts at every admissible site.
Every term, its catalogue and its measure transports on that lift.
Cofinality defines one family on every bounded lifted domain; common-lift
agreement makes it independent of the site and the lift.
For t∈M Ř_jℤ⁴, a_j/a_i being an integer implies that translation preserves
all older cell partitions, as well as their subdivisions and cut-offs.
It therefore gives the covariance in (iii)(b), with exactly this translation
group. The empty-label remainder keeps the A5 bound
\(|\mathfrak r'^{(j)}(X)|\le e^{-p_0(g_j)}e^{-\kappa d_j(X)}\)
at the standing of H5/H6a; it is the same series, not a newly estimated one.

### Boundary objects and the next induction hypothesis

Port `prf-label-boundary`, CA-I:60103–60234.
The same seven ingredient types give each boundary statement, with the
following precise domains.

| Object | Domain W | Why its label reading is confined to W⁺¹ |
|---|---|---|
| B^(j)(X) | X | Its S_i∩X data are local; F12 treats its T part, and the carried older/profile/completion pieces have the same reading sets. |
| T^(j−1)(·∩X) | X | Its component factorisation from CMP 119 (2.19)–(2.21), inherited terms and reference measures are local there. |
| B′^(j)(X) | X | Off 𝒳_j it is exactly (P7.20); on 𝒳_j the boundary difference is zero by (P7.23). Membership in this range is itself trace-determined by (P7.21). |
| T′_j(X) | X^♯ | It includes V(X^♯). Each older domain X″⊂X^♯ reads [X″]_i⁺¹⊂(X^♯)⁺¹. The profiles, history integration, counts, trees and vacuum attachments obey the same inclusion. |

For the last row inside a larger polymer, the required strip inclusion
X_a^♯⊂X′⊂X puts this read set inside X⁺¹, as used above.
The foreign-island assignments and prepared rounding in H6a are essential
here. Geometric completion from refereed pda alone would not supply their
analytic representation or enlarge its stated one-operation scope.

**P7-F15 (filled): locality reaches do not accumulate.**
At every substitution the actual smaller domain X″ is contained in the
current domain W. Its older reading set is [X″]_i⁺¹, and (P7.4) puts that
set directly inside [W]_j⁺¹. We never enlarge an already enlarged set to
form the next reading set. The six uses of older locality in the source
are: empty-label inherited R inside Ψ_X; R vertices inside E; R vertices
inside R''; historical terms inside island activities; older terms inside
B′; and older terms inside V(X^♯). Each has exactly this inclusion.
Thus a single coarsest-level cell layer suffices for all levels. Profiles
read only a quarter of their own cell, and their reaches satisfy the same
inclusion. This proves (iii)(c) and the general intrinsic-object assertion.

There is no change of the sum when the second-group terms are identified.
Absolute convergence and (P7.23) give
\[
 \sum_XR'^{(j),\ell}(X)=
 \sum_{X\in\mathcal X_j(\ell)}\mathfrak r'^{(j)}(\hat X)
 +\sum_{X\notin\mathcal X_j(\ell)}\mathbf B'^{(j)}(X).          \tag{P7.24}
\]
This is an equality for the **same label** and its same representation.
No equality of individual densities at different labels is needed or
claimed. The “unchanged split” remark, CA-I:60376–60493, contains a broader claim;
only its exact regrouping identity is used here. The coefficient in (ii)
was already fixed by the whole-lattice total.

**P7-F16 (filled): the last sentence propagates only (a)–(c⁺).**
The common numbers through j have been constructed in (ii)(b).
The additional assumption x_j≥γ⁻² supplies the next (a).
The completed step on every S_j, with E=0, supplies the next (b).
The proved (i), (ii)(a), (iii) join their earlier-level versions in (c⁺).
For its remaining 𝔄-family membership use exactly P7-Hfamily.
Here is the source's propagation deduction, CA-I:60672–60716.
Write at each site
\[
 E^{(k+1)}=[\log Z^{(k)}-\log Z^{(k)}(1)]
              +\mathsf S_{k+1}(g'^{-2},\mathbf E_f),\quad
 f\in\mathfrak F_k,\quad g'\in(0,\gamma].                    \tag{P7.25}
\]
The two named step lemmas carry all the family clauses except volume
consistency: the CMP 109 (1.7),(1.18),(1.19) properties, the stated analytic
domain and constants, reality, and the Euclidean total clause, with H3.
Whenever they extend an older sum to the infinite lattice, the already
available volume consistency identifies those older local terms, and
β[f_i]=β_i identifies their subtractions. This reads levels i≤k only.
For volume consistency of the new term, the proof of (i) applies to its
unpointed series as well: the same local operator words and intrinsic
older densities are used, and the layer-bookkeeping premise of Hfamily
supplies the log Z−log Z(1) part. Thus the new family has every clause,
with the same constants. Its coefficient is the well-defined β[f_(k+1)]
of (ii), so appending this pair places it in F_(k+1) by definition.
Applied to the unmarked step at k=j−1, this supplies
\(f^{\mathfrak A}\in\mathfrak F_j\).

For j=1 the older-term arguments are vacuous; the source's base H₁ supplies
g₀, Ř₀ and convergence of the identified zeroth step. At no j have we
proved the next clause (d) from locality. That convergence/domain input
must be supplied when the joint induction performs its next whole-lattice
step. The allowed order is therefore
\[
 \text{earlier prefix and current (d)}\ \longrightarrow\ E^{(j)},\Pi_\infty^{(j)},\beta_j
 \ \longrightarrow\ x_j,\check R_j,\mathcal S_j
 \ \longrightarrow\ T\text{-terms}\ \longrightarrow\ R\text{-terms}
 \ \longrightarrow\ (H_{j+1})(a),(b),(c^+).
\]
The flow inequalities, step existence and family propagation remain their
named inputs. This completes the port of A14 as a conditional implication. ∎

## Source navigation and recovery

The entry points were GOAL.md, its “Method: port the complete account”
section, FINISH.md's “Build on published work”, “Working efficiently” and
“Rules”, [chain-ca](../chain-ca.md) A14 and §7.2, and
[the complete-account index README](../sa-index/ca-full/README.md).
Source lookup began in [the outline index](../sa-index/README.md), its
neighbouring chunk rows and [obligations](../sa-index/obligations.md), then
in the complete-account index. The relevant outline rows are in chunk 20;
the common-companion passage is `/tmp/sa_ym4.tex:21454–21535`.
That outline passage requires the interacting compatibility. The account's
A14 supplies the conditional proof route ported here; the outline's
requirement itself was not used as a proof.

The main CA index rows are `ca-full/index.tsv:223–238`. Its `PROVED` tags
were checked against the corresponding unqualified source headings and
the declaration convention, CA-I:27–46. Only bounded source excerpts were
read. The theorem statement is transcribed above without altering even
the source's references; corrections belong to the subsequent proof.
The clause-(0) connection is the (h) row in the change log of checked
[P5](p5-induction.md), with source `4.19:prop-clause-zero`,
CA-I:56419–56460. This file does not edit that table or grant its row status.

Both requested source files already existed. Their SHA-256 identities
agree with the pinned sources in chain-ca:

| Local source | SHA-256 |
|---|---|
| `/tmp/sa_ym4.tex` | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `/tmp/sa_ca_I.tex` | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |

They are Sussman and Alpoge's files at upstream commit `31a47c543775`,
`YM4_sketch_500.tex` and `theorem_0_complete_account_raw_I.tex`, respectively.
No duplicate download was needed. Source searches, hashes, transcription
comparison and file bookkeeping discharge no mathematical obligation.
Recovery should start from this saved file and its named inputs.

## Result

**Ported:** A14, `4.38:thm-torus-independence`, exactly stated at
CA-I:58187–58411, with its source standing **proved implication with named
hypotheses** confirmed at the heading and declaration convention.
The proof above follows the account's non-wrapping local series, walk limit,
polarisation, coefficient extraction, label catalogue, activity and boundary
route, through the final family-propagation deduction.

| Theorem conclusion | What the port establishes conditionally |
|---|---|
| (i) | One intrinsic analytic whole-lattice family on non-wrapping lifts, with M-grid covariance and separate 𝔄/ℜ marking. |
| (ii)(a) | The common response limit, absolutely convergent pointed tensor, vanishing wrapping contribution, pointwise and two-point limits, exponential bounds, and covariance of totals on regular minimisers. The particular CMP 109 (5.10) estimate keeps its named supplier. |
| (ii)(b) | The real, site-free β_j=β_j^𝔄+β_j^ℜ with dependence only on the earlier coupling prefix and fixed parameters; the subsequent scalars are common when the stated positivity premise holds. |
| (iii)(a)–(c) | The profile and interior terms, empty-trace remainder and exact second-group range, and the prescribed one-cell reading sets for boundary terms and island operations. |
| Final sentence | Only (H_(j+1))(a),(b),(c⁺), with the additional step, flow and family-propagation inputs. The next whole-lattice convergence clause (d) is not a conclusion. |

**Filled steps:** F1 handles infimal tree lengths and wrapping tails; F2
proves strip containment including the smallest allowed multiplier; F3
cancels the normaliser at fixed cluster support; F4 reassembles all
quadratic complements; F5 identifies convergent analytic series on their
actual domains; F6 proves stationarity and gauge-representative independence;
F7 gives the common walk-tail limit; F8 supplies the bidisc estimate, its
open-radius limit and repeated-direction case; F9 handles changing domain
index sets; F10 proves reality, additivity and prefix-only dependence;
F11 separates inherited and completed members; F12 orders current T and
R operations without a circular locality premise; F13 proves that the
trace detects every relevant complete component; F14 removes all older
label data on the empty-trace range; F15 proves that one-cell reaches do
not accumulate; F16 spells out the restricted induction propagation.

**Corrections:** C1 replaces the erroneous reference to (H_j)(d) for
translation covariance by the already proved polarisation covariance.
C2 replaces an unjustified inclusion into the unrounded large-field set
by the sufficient inclusion into its level-j round-up. C3 uses the
source's full completion premise for partially healed regions, instead of
assuming the post-R small-field region is a cell-union; the stronger
intermediate inherited-domain chain is not asserted there. The catalogue
sentence about a component that “contained” K₀ needs no correction.
Only the same-label regrouping identity is used from the unchanged-split
remark, not its broader assertion about densities at different labels.
These choices preserve the theorem's stated conclusions and retain all
supplier hypotheses.

**Named hypotheses:** P7-H1–H5, P7-H6a–H6c, P7-H7, P7-Hnum,
P7-Hwalk, P7-Hsum, P7-Hextract, P7-Hmin, P7-Hnorm, P7-Hfamily and
P7-Hlevel, with their exact use domains and inherited premises in the
input table. In particular, local analytic admission, the full completion
and representation format, joined-domain analytic extension, closed-total
covariance, the published response and counting bounds, coefficient
normalisation and the inductive convergence bound have not been proved
from scratch here. The checks of P1, P3, P4 and P5 and the completed or
proved, refereed standing of mu, lrb, oc, ui and pda are credited within
their stated scopes; none closes an input outside its scope.

Credit belongs to **Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text**, and to **Tadeusz Balaban** at the cited
construction and theorem loci. This is research text and a conditional
port, not an audit, a proof of T0, or a grant of scientific status.
No numerical calculation, enumeration, solver or other computer-assisted
step was used as mathematical evidence. Only `library/port/p7-torus.md`
was written in this checkout. **This text is not yet checked by another model.**

## Change log (check, 2026-11-05)

Ported by Codex. Checked line by line by a fresh Claude session ([p7-torus-gate](../../gates/p7-torus-gate.md)): statement byte-identical to CA-I 58187–58411; first failing step L1076–1077, removable, no conclusion changes; verdict faithful with repairs. Applied by the lead (Claude):

1. **L1076–1077** (activities, item 3): the sentence that the prepared/stage factors from \([Z''_i\cap Y_b]_i\) "differ from one only in \(Y_b^\sharp\)" copies CA-I 59953, which assumes the round-up lies in \(Y_b\) (not shown; \(Y_b\) is only a union of \(M\)-cubes). Replace it by the radius fact: by lem-coupling-profile (e) and (P7.4), the factor reads only cells inside \([Y]_j^{+1}\subset X^{+1}\). Nothing depends on the removed sentence.
2. **Errors in their text, confirmed:** C1 (CA-I 59018–59019 cites (H_j)(d) for translation invariance; (H_j)(d) at 58241–58267 has no covariance clause; the source is part (d) of prf-polarisation-limit); C2 (CA-I 60035–60037, 60041–60042 put level-\(i\) round-ups inside the unrounded \(\Lambda_j(\ell)^c\) or \(Y_b\), valid only for unions of level-\(j\) cells); C3 (step 5, CA-I 59279–59301, needs \(\Lambda_j(\ell)\) a union of cells, which their range lemma does not grant; routed through the completion clause).
3. **Unprinted input:** the "lemma on pointed polarisation sums" cited for CMP 109 (5.10) at CA-I 58985–58987 has no statement or label in CA-I, CA-II or CA-III. It stays a named input (Hsum), and is really needed: the port's own rate \(\tfrac18\min\{\delta_0,\kappa/M\}\) is weaker than (5.10)'s \(\tfrac12\min\{\delta_0,\kappa/M\}\).
4. F2 and most of F13 are their own arguments (CA-I 58010–58032), not filled steps. F16 uses the large-field \(\beta_j\) bound H5 (hypothesis (3) of prf-label-boundary).

Status: **checked port.** Clause (0) hypothesis (h) is a checked port, on its named inputs.
