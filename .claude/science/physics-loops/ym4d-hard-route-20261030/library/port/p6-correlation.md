# P6: correlation, weights, and the one-loop law

Provenance: Port of the complete account by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, pinned upstream at 31a47c543775; repository source revision e5d4b95fe. Balaban is credited at each borrowed input below. Research text only; no audit or scientific status is conferred. Not yet checked by another model.

## Scope, source identity, and standing

This ports tranche 6 of `chain-ca.md` §7.2, rows B2–B4 of §2.2. It is a port of implications, not a proof of their open antecedents. CA-II means `theorem_0_complete_account_raw_II.tex` at upstream revision `31a47c543775`; CA-I has the corresponding Part I filename. The source convention is CA-I:27–46: an unqualified heading denotes a proved implication, with named inputs retained. The structural index is not a status authority.

The exact statements below preserve the source's TeX labels, quantifiers, constants, caveats, and displayed hypotheses. Proofs and dependency annotations follow them. The two weight lemmas are different: §5.5 controls windowed fields and near-unit data; §5.6 turns a separately assumed decoupling polydisc bound into summable pieces. Neither proves that the other's hypotheses hold. In particular, §5.5 is not a substitute for B1.

### Existing repository inputs

Use [pointed irrelevance](../port-pi.md), `5.2:lem-pointed-irrelevance`, only on its admitted E-family domain. It is already ported; its background and membership hypotheses remain attached. The owner supplies the following standings: [P1](p1-base.md), [P3](p3-free.md), and [P4](p4-operator.md): checked; [P5](p5-induction.md): ported; [mu](../mu.md), [lrb](../lrb.md), and [oc](../oc.md): their 4.13, 4.4, and own-constant implications proved and refereed; [ui](../ui.md): their 4.5 implication checked. These standings are used as supplied, not granted by this note. None closes unrelated named hypotheses in those notes.

B1 is `5.6:prop-polydisc-holomorphy`, CA-II:46131–46165, explicitly **Proof outstanding** at 46167. The owner assigns its attack to `library/ph.md`; that file is absent from this pinned checkout. B1 remains a named hypothesis throughout this port.

## Exact source statements

### B2a: 5.6:lem-weight

CA-II:45154–45299. Status at source: unqualified heading, followed by a proof; conditional on the displayed inputs. For B2, the assembly nevertheless counts the weight machinery as incomplete (`chain-ca.md` §4); this port does not promote that machinery.

```latex
\begin{lemma}[The weight lemma]\label{5.6:lem-weight}
Let $t$ be a term with exempt set $Y_1(t)$, set of decoupling variables $\mathcal{V}=\mathcal{V}(t)$,
composite $F_t(\sigma;\mathfrak{d})=t\circ\mathsf{R}(\sigma;\mathfrak{d})$ and set $\mathcal{D}_b$ of data of
size at most $b$, as in Definition~\ref{5.6:def-decoupling-variables}, and put
\begin{equation*}
r(\kappa_1)=e^{\kappa_1}\bigl(e^{\kappa_1}-1\bigr)^{-2}.
\end{equation*}
Assume hypothesis $(\mathrm{H}_{\circ})$:
\begin{equation}\label{5.6:eq-weight-a}
\begin{gathered}
\kappa_1\ge 1,\quad\text{and for every }\mathfrak{d}\in\mathcal{D}_b\text{ the function }
\sigma\mapsto F_t(\sigma;\mathfrak{d})\\
\text{is holomorphic on the open polydisc }P_{\mathcal{V}}(e^{\kappa_1}),\\
\text{with }|F_t(\sigma;\mathfrak{d})|\le\mathfrak{b}\text{ for all }\sigma\in P_{\mathcal{V}}(e^{\kappa_1}).
\end{gathered}
\end{equation}
Here holomorphic means, as in Definition~\ref{5.6:def-decoupling-variables}, continuous and separately
holomorphic in each variable. Holomorphy is required in $\sigma$ for each $\mathfrak{d}$ separately;
nothing (no measurability, continuity or analyticity) is assumed of the dependence on
$\mathfrak{d}$. If $F_t(\cdot;\mathfrak{d})$ is holomorphic on a neighbourhood of the closed polydisc
$\mathbb{D}_{\mathcal{V}}(e^{\kappa_1})$ with $|F_t|\le\mathfrak{b}$ on
$\mathbb{D}_{\mathcal{V}}(e^{\kappa_1})$, then $(\mathrm{H}_{\circ})$ holds by restriction. Since
$\partial^W$ annihilates every function of $\mathfrak{d}$ alone when $W\neq\emptyset$, replacing $F_t$
by $F_t-c(\mathfrak{d})$, for any function $c$ of the datum, changes no piece with variable set
$W\neq\emptyset$; for such pieces $(\mathrm{H}_{\circ})$ may therefore be read with $\mathfrak{b}$ the
supremum of $|F_t-c|$ over $\sigma\in P_{\mathcal{V}}(e^{\kappa_1})$ and $\mathfrak{d}\in\mathcal{D}_b$.

Pieces, final domains $Y$, the sets $\mathcal{P}(t;Y)$, the numbers $n=n(t;Y)$ of cells of
$Y\setminus Y_1(t)$, the number $\lambda$ of links of the chain, and the counting readings
$(\pi 1)\text{--}(\pi 3)$ are those of Definition~\ref{5.6:def-pieces} and \eqref{5.6:eq-pieces-b}.
Then the following hold.
\begin{enumerate}
\item[(a)] (Per-piece factor.) Every piece $p$ of $t$ with variable set $W$, $|W|=m$, obeys
\begin{equation}\label{5.6:eq-weight-b}
\sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|\le\mathfrak{b}\,r(\kappa_1)^m
\le\mathfrak{b}\,e^{-(\kappa_1-1)m}.
\end{equation}
\item[(b)] (Count at a fixed final domain.) Assume $(\pi 1)$ and $(\pi 2)$ of \eqref{5.6:eq-pieces-b}.
Then for every final domain $Y$, with $n=n(t;Y)$,
\begin{equation}\label{5.6:eq-weight-c}
\sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|
\le\mathfrak{b}\,\bigl(\lambda\,r(\kappa_1)\bigr)^n
\le\mathfrak{b}\,\bigl(\lambda e^{-(\kappa_1-1)}\bigr)^n .
\end{equation}
In particular the left side is at most $\mathfrak{b}$ when $n=0$ (the exceptional term of
\cite[text following (1.66)]{B-CMP122b}, in which $Y=Y_1(t)$ and the contribution is that of the term
itself); for $n\ge 1$ it is at
most $\mathfrak{b}$ when $\kappa_1\ge 1+\log\lambda$, and at most $\mathfrak{b}\,2^{-n}$ when
$\kappa_1\ge 1+\log(2\lambda)$. In the chain form of \cite[(1.61)--(1.63)]{B-CMP122b}, where
$\lambda=3$, this reads: at most $\mathfrak{b}$ for $\kappa_1\ge 1+\log 3$, and at most
$\mathfrak{b}\,2^{-n}$ for $\kappa_1\ge 1+\log 6$.
\item[(c)] (Decay transfer to the final domain.) Assume $(\pi 1)\text{--}(\pi 3)$ of
\eqref{5.6:eq-pieces-b}, and let $\ell$ be a linear size on cell sets obeying $(\mathrm{TL})_{c'}$,
\eqref{5.6:eq-linear-sizes-a}. Suppose $\mathfrak{b}\le\mathfrak{b}_0e^{-a\ell(Y_1(t))}$ with
$a\ge 0$ (the inductive factor extracted from the exponential of \cite[(1.66)]{B-CMP122b} decays at
the rate $a=(1+3\beta)\kappa$). Then for
every final domain $Y$ with $\mathcal{P}(t;Y)\neq\emptyset$,
\begin{equation}\label{5.6:eq-weight-d}
\sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|
\le\mathfrak{b}_0e^{-a\ell(Y)}\bigl(\lambda e^{-(\kappa_1-1-c'a)}\bigr)^n
\le\mathfrak{b}_0e^{-a\ell(Y)},
\end{equation}
the second inequality under the one-sided floor $(\mathrm{F}\text{-}\kappa_1)^{P}$,
\begin{equation}\label{5.6:eq-weight-e}
\kappa_1\ge 1+\log\lambda+c'a,
\end{equation}
imposed on $\kappa_1$ after $\kappa$ has been chosen. At $n=0$ no floor is needed, since then
$Y=Y_1(t)$. With $\lambda=3$, $a\le 2\kappa$ and $c'=d=4$ (free tree length), the floor
\eqref{5.6:eq-weight-e} is implied by $\kappa_1\ge 1+\log 3+8\kappa$; with $c'=1$ (contained tree
length, face adjacency) it is implied by $\kappa_1\ge 1+\log 3+2\kappa$. The lower bound
$\kappa_1\ge 16\kappa+1$ of Definition~\ref{5.1:def-admitted-inputs} implies both as soon as
$8\kappa\ge\log 3$, that is $\kappa\ge(\log 3)/8$, for instance whenever $\kappa\ge 1$; where it would
not, the lower bound on $\kappa_1$ is raised to \eqref{5.6:eq-weight-e}, and raising this lower bound
is admissible. No value is assigned to $\kappa_1$.
\item[(d)] (All final domains.) Assume $(\pi 1)\text{--}(\pi 3)$ of \eqref{5.6:eq-pieces-b}. For
$n\ge 0$ let $N_t(n)$ be the number of final domains $Y$ with $\mathcal{P}(t;Y)\neq\emptyset$ and
$n(t;Y)=n$. Then
\begin{equation}\label{5.6:eq-weight-f}
\begin{gathered}
N_t(0)\le 1,\qquad N_t(n)\le 2^{D_d\cdot\#Y_1(t)}\,(8D_d)^n\quad(n\ge 1),\\
\sum_{Y}\sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|
\le 2^{D_d\cdot\#Y_1(t)}\,\mathfrak{b}\sum_{n\ge 0}\bigl(8\lambda D_d\,r(\kappa_1)\bigr)^n\\
\qquad\le 2\cdot 2^{D_d\cdot\#Y_1(t)}\,\mathfrak{b},
\end{gathered}
\end{equation}
the last inequality for $\kappa_1\ge 1+\log(16\lambda D_d)$; for $\lambda=3$ the condition reads
$\kappa_1\ge 1+\log(48D_d)$. If the minimal tree length of $Y_1(t)$ is finite (for
$d_k^{\subset}$, for instance, when $Y_1(t)$ is face-connected; for $d_k^{\mathrm{fr}}$ always), then,
by the count of the cells of a cell set in terms of its tree length,
\begin{equation*}
\#Y_1(t)\le 3^d\bigl(2d_k^{\mathrm{fr}}(Y_1(t))+1\bigr)\le 3^d\bigl(2d_k^{\subset}(Y_1(t))+1\bigr),
\end{equation*}
so that, with $c''_d=3^dD_d\log 2$ and for $\ell\in\{d_k^{\mathrm{fr}},d_k^{\subset}\}$,
\begin{equation*}
2^{D_d\cdot\#Y_1(t)}\le e^{c''_d}\,e^{2c''_d\,\ell(Y_1(t))}.
\end{equation*}
Hence, if $\mathfrak{b}\le\mathfrak{b}_0e^{-a\ell(Y_1(t))}$, the final bound
$2\cdot 2^{D_d\cdot\#Y_1(t)}\,\mathfrak{b}$ of \eqref{5.6:eq-weight-f} satisfies
\begin{equation*}
2\cdot 2^{D_d\cdot\#Y_1(t)}\,\mathfrak{b}
\le 2e^{c''_d}\,\mathfrak{b}_0\,e^{-(a-2c''_d)\ell(Y_1(t))}
\le 2e^{c''_d}\,\mathfrak{b}_0\,e^{-(1-\varepsilon)a\ell(Y_1(t))},
\end{equation*}
the last inequality under the one-sided floor $(\mathrm{F}\text{-}\kappa)^{(d)}$, depending only on
$d$, $\beta$ and $\varepsilon$,
\begin{equation}\label{5.6:eq-weight-g}
\varepsilon a\ge 2c''_d,\quad\text{which for }a=(1+3\beta)\kappa\text{ reads}\quad
\kappa\ge\frac{2\cdot 3^dD_d\log 2}{\varepsilon(1+3\beta)},
\end{equation}
for any fixed $\varepsilon\in\,]0,1[$. Otherwise the prefactor $2^{D_d\cdot\#Y_1(t)}$ is kept
displayed. In either case no bound with a constant uniform in the term $t$ is asserted unless either
the floor \eqref{5.6:eq-weight-g} holds or the prefactor $2^{D_d\cdot\#Y_1(t)}$ is carried explicitly.
Clause (d) is not
needed for the order of summation of \cite[text following (1.66)]{B-CMP122b}, in which the final
domain is fixed first, nor for the per-final-domain bound of the correlation theorem.
\item[(e)] (Subset form.) Let $\mathcal{N}$ be a finite set of cells and let $F$ satisfy
$(\mathrm{H}_{\circ})$ with $\mathcal{V}$ replaced by $\mathcal{N}$ and $\mathfrak{b}$ denoted
$\mathfrak{N}(F)$, or with $\mathfrak{N}(F)$ the supremum of
$|F(\sigma;\mathfrak{d})-F(\mathbb{1};\mathfrak{d})|$ over $\sigma\in P_{\mathcal{N}}(e^{\kappa_1})$
and $\mathfrak{d}\in\mathcal{D}_b$, in the sense of the remark following \eqref{5.6:eq-weight-a},
where $\mathbb{1}$ is the point with all coordinates equal to $1$. Let $F_{\mathsf{y}}$ be the
subset-form pieces of \eqref{5.6:eq-pieces-c}. Then the bound in the first line of the following
display holds for every $\mathsf{y}\subset\mathcal{N}$, $\mathsf{y}\neq\emptyset$, and the
telescoping identity in its second line holds for every $\mathfrak{d}\in\mathcal{D}_b$:
\begin{equation}\label{5.6:eq-weight-h}
\begin{gathered}
\sup_{\mathfrak{d}\in\mathcal{D}_b}|F_{\mathsf{y}}(\mathfrak{d})|
\le\mathfrak{N}(F)\,r(\kappa_1)^{|\mathsf{y}|}\le\mathfrak{N}(F)\,e^{-(\kappa_1-1)|\mathsf{y}|},\\
F(\mathbb{1};\mathfrak{d})-F(0;\mathfrak{d})
=\sum_{\mathsf{y}\subset\mathcal{N},\ \mathsf{y}\neq\emptyset}F_{\mathsf{y}}(\mathfrak{d}).
\end{gathered}
\end{equation}
No disc in any variable other than the decoupling variables enters.
\item[(f)] (Dependence of the constants.) The constants in (a)--(e) are the numbers $r(\kappa_1)$,
$\lambda^n$, $2$, $4$, $8$, $16$, and numbers depending only on $d$ and the adjacency $\sim$, namely
\begin{equation}\label{5.6:eq-weight-i}
c'\in\{1,d\},\qquad D_d\in\{2d,\;3^d-1\},\qquad 3^d,\qquad c''_d=3^dD_d\log 2 .
\end{equation}
The conditions are one-sided lower bounds on $\kappa_1$ and, only where the absorption in (d) is wanted,
on $\kappa$. None of them depends on $K$, $k$, $N$, an age, a nesting depth, a position, the volume,
the size of a large-field region, the number of terms, or the coupling. The blocking factor $L$ enters
nowhere, and no power of $L$ is written or used; $M$ enters only through the definition of the lengths,
where it cancels, the increments in $(\mathrm{TL})_{c'}$ being $c'\cdot M/M$. No property of the group
$SU(N)$ is used.
\end{enumerate}
\end{lemma}
```

### B2b: 5.5:lem-weight

CA-II:35258–35538. Status at source: unqualified heading, followed by a proof; conditional on the displayed inputs. For B2, the assembly nevertheless counts the weight machinery as incomplete (`chain-ca.md` §4); this port does not promote that machinery.

```latex
\begin{lemma}[The weight lemma]\label{5.5:lem-weight}
Work in the setting of Definition~\ref{5.5:def-windowed-source}, with the letters, levels and
weights of Notation~\ref{5.5:not-weight-notation}, the near units, their three classes and
their filed discs as in Definition~\ref{5.5:def-near-unit-classes}, the data factor of
Definition~\ref{5.5:def-data-factor}, and the constants of
Definition~\ref{5.5:def-weight-constants}. Assume the floors and the one-sided
ceilings on $\gamma$ listed in Definition~\ref{5.5:def-weight-constants}, among them
\eqref{5.5:eq-weight-constants-d}. Assume moreover the following statements:
\begin{itemize}
\item the membership statement for own-read near units (Definition~\ref{5.5:def-weight-inputs});
\item the remainder statement for box-read near units (Definition~\ref{5.5:def-weight-inputs});
\item the closure statements for the pair system $\mathcal{K}^{rd}$
(Definition~\ref{5.5:def-weight-inputs}): its closure under
the read moves $\mathsf{M}2$, $\mathsf{M}3$, $\mathsf{M}4$, under the paired-chart move
$\mathsf{M}5$, under the restriction move $\mathsf{M}6$ and under the response-dilation move
$\mathsf{M}1$, and its closure under the comb-dilated remainder move $\mathsf{M}8$;
\item the remainder statement for the third class (size, block sum and filing of the
remainders of the near Wilson and counterterm pieces);
\item the two-run statement for the third class off the chart, namely the bound on the
two-machine differences of the third-class pieces, in the format of the size and block-sum
bounds of the remainder statement for the third class with $\mathsf{s}_v\mathsf{v}_v$ replaced
by $C^{\perp}\mathsf{S}^{\perp}_v$, at every third-class unit, the letters being those of
part~(e);
\item the per-cell row bounds of the near-unit table at unit weight, and the statement that
the own-level family of each own-read unit takes values in the tube $\mathfrak{U}_T$ of that
unit, on which the membership statement rests.
\end{itemize}
The two-run statement for the third class and the closure under $\mathsf{M}8$ enter only
part~(e), at the third class off the chart, that is, at the pieces at which the weighted
scaffold majorants of Definition~\ref{5.5:def-windowed-source}, on which the paired charts
rest, are not available. Then at every stage of every $\mathbf{R}_k$,
for every block $\square$, every $t\in[0,1]$ and every $\sigma$ with
$|\sigma|\le e^{\kappa_1}$ --- with $\mathsf{t}\in\mathbb{D}_{\square}$ in~(a) and in the rows
read on the box pair, $|\tau|\le\rho_A(v)$ in the own-read rows, and
$|\mathsf{t}|\le r^{rem}_{\square}$ in the remainder rows --- the following hold.
\begin{enumerate}
\item[(a)] \textup{(a1)} $|\partial\mathbb{W}(x)-1|<1.4\,\theta_2(x)$ for every cell $x$
meeting $\tilde{\square}^3$.

\textup{(a2)} For every cell $x$ meeting $\tilde{\square}^3$ and every $j\le k$,
\begin{equation}\label{5.5:eq-weight-a}
|\partial\mathfrak{b}'_j(x)-1|\le 4\,\theta_2(x).
\end{equation}

\textup{(a3)} Let $Q$ be a box of at most $9$ cubes of $\pi_p$ a side; write $Q^{(1)}$ for the
enlargement of $Q$ by one layer of $\pi_p$-cubes and $Q^{\sim-1}$, $Q^{\sim-2}$ for $Q$ shrunk
by one and by two such layers. Assume
$Q^{(1)}\subset\tilde{\square}^3$ and every cell meeting $Q^{(1)}$ of level at least $p$; let
$w_Q$ and $\alpha_Q$ be the largest values of $w(\Delta)$ and of $\alpha_{0,\ell(\Delta)}$
over those cells. In one gauge of the complexified gauge group $G^{\mathbb{C}}$ on
$Q^{\sim-1}$ one has $\mathfrak{b}=e^{i\eta A}$ with a potential $A$ satisfying, for
$0\le\beta\le\beta_0$ ($\beta_0$ the H\"older ceiling, $\|\cdot\|_{\beta}$ the H\"older
seminorm of exponent $\beta$, $\ell_p=L^p\eta$ the length of level $p$),
\begin{equation}\label{5.5:eq-weight-b}
\max\bigl\{\ell_p|A|,\ \ell_p^2|\nabla A|,\ \ell_p^{2+\beta}\|\nabla A\|_{\beta}\bigr\}
\le\mathsf{a}_Q:=K_{loc}\,w_Q\,\alpha_Q .
\end{equation}

\textup{(a4)} Let $j\le p$ and let $\square_0'\subset Q^{\sim-2}$ be a box of
$\pi_j$-cubes. Then $\mathfrak{b}'_j$ restricted to $\square_0'$ equals
$(U_j,J_j)(\square_0',\mathsf{V}')$ modulo gauge, where $\mathsf{V}'$ is
$M^{\cdot}(\mathfrak{b}'_j)$ restricted to $\mathfrak{B}_j(\square_0')$. Put $t_p:=L^{j-p}$.
In the comb gauge centred at any $y\in\square_0'$, one has
$|\partial\mathsf{V}'-1|\le c_1\mathsf{a}_Qt_p^2$ and, on all bonds $b$,
$|B^{ax}(b)|\le 2d(1+|b-y|)\,c_1\mathsf{a}_Qt_p^2$; moreover
\begin{equation}\label{5.5:eq-weight-c}
\begin{gathered}
B^{ax}_{\mu}(x)=\sum_{\iota<\mu}(x-y)_{\iota}F_{\iota\mu}(y)+\mathfrak{e}_{\mu}(x),
\qquad |F|\le c_1\mathsf{a}_Qt_p^2,\\
|\mathfrak{e}_{\mu}(x)|\le c_1(1+|x-y|)^2\mathsf{a}_Qt_p^{2+\beta}
\quad\text{on the level-}j\text{ bonds},\\
|\mathfrak{e}_{\mu}(b)|\le 4d(1+|b-y|)\,c_1\mathsf{a}_Qt_p^2
\quad\text{on the graded-rim bonds (levels }i<j).
\end{gathered}
\end{equation}

\item[(b)] Let $v$ be a near unit with anchor $y$, and let $n$, $j$, $\nu$ and the scale ratio
$t=L^{j-n}$ be its letters as in Definition~\ref{5.5:def-windowed-source} (see also
Notation~\ref{5.5:not-weight-notation} for the homonym $t$); this $t$ is the scale
ratio, not the interpolation parameter $t\in[0,1]$ of the preamble. Put
$\Theta:=c_Ww^{\vee}(y)$ and $z:=\Theta\rho_{n,j}$. On the filed discs the
near units satisfy the following bounds, which form the table $\mathfrak{N}^P(v;\Theta)$.
\begin{itemize}
\item A box-read core, taken whole together with its counterterm piece on the same box
pair: its term $\mathfrak{i}_y$ at the anchor $y$ satisfies
\begin{equation*}
|\mathfrak{i}_y|\le C_I'\,\mathfrak{n}\,\nu^3z^2(1+z)\,t^{4+\hat{\alpha}}.
\end{equation*}
\item A box-read short single: at most $2\mathfrak{n}_v(S^{\star}_v)^{-2}$.
\item An own-read unit: at most $2\mathfrak{n}_v$ each, by the membership statement.
\item The near constituents ($X\ni y$, $X\subset\tilde{\square}^2$) of a straddling core,
that is, of a core with $y\in\tilde{\square}^2$ and
$\mathfrak{r}_v=\square_y^{\sim\nu+1}\not\subset\tilde{\square}^2$, where $\square_y\in\pi_j$
is the cube of $y$, so that $v$ itself is not a near unit; this holds at every $\nu$. They are
own-read units on $\mathcal{W}_T$, each at most $2\mathfrak{n}_ve^{-\kappa d_j(X)}$ at the
prefactor $24K''\vartheta(\square)\eta_p$, with $\eta_p\le t^5$. For $\nu\ge2$ one has
$X\cap\tilde{\square}=\emptyset$, because $2\nu+3<L^{\nu-1}$ for $\nu\ge2$ (at $\nu=2$:
$7<8\le L$), and then $\eta_p\le e^{-\frac14\delta wL^{n_0-j}}\le t^5$. The first inequality,
which by the definition of $\eta_p$ amounts to $d_{\ell}(X_T,\square^{\zeta})\ge wL^{n_0-j}$,
follows from $X\cap\tilde{\square}=\emptyset$ by the distance bound for the own-level family;
the second follows from the level floor among the floors of
Definition~\ref{5.5:def-weight-constants}. Here $w=M/M_1$ is the side of the own-scale cube in
units of $M_1$ (Notation~\ref{5.5:not-weight-notation}), not a weight. At
$\nu=1$ one has $n=j$, so $t=1$, and $\eta_p\le t^5$ holds because $\eta_p\le1$; nothing is
claimed of $\mathfrak{r}_v\cap\tilde{\square}$.
For two machines each is at most $2\mathsf{S}e^{-\kappa d_j(X)}$. These bounds have
degree $0$ in $\Theta$. Their per-cell sums --- $t^5$ times the number of anchors of such
constituents per unit $n$-cell, a number proportional to $(\nu+2)t^{-3}$ --- are summable in
$\nu$ inside $\kappa_R$, by the per-cell row bounds at unit weight, and inside
$\kappa_R^{\times}$ as well: in the set where the normalised row sums are at most one, a
level-$j$ size is at most $K_r/c^{(r)}_{n,j}$, with the row constants $K_r$ and
$c^{(r)}_{n,j}$ of Definition~\ref{5.5:def-weight-constants}; this quotient is proportional
to $t^{-\hat{\alpha}}$, and $(\nu+2)t^{2-\hat{\alpha}}$ remains summable in $\nu$.
\item An own-read unit which is a read core ($S^{\star}_v\le1$, so that by
\eqref{5.5:eq-near-unit-classes-a} $C_MDt^2z\ge1>\frac12$): its constituents, taken singly,
together with its counterterm companion of the third class, are bounded inside
$C_I'\,\mathfrak{n}\,\nu^3z^2(1+z)t^{4+\hat{\alpha}}$.
\item At $\nu\le2$, where the units are own-read by the filing at every value of
$S^{\star}_v$: the constituents ($2\mathfrak{n}_v$ each) and the counterterm companion (at
most $C'\mathfrak{n}z^2t^4$, with the constant $C'$ of
Definition~\ref{5.5:def-weight-constants}) are separate units of the table.
\item The Wilson piece of the block (third class): at most $\Theta^2\mathfrak{N}_W(v)$.
\item The remainders of the box-pair-read pieces (slot $\flat$): at most
$(K_A+28K^{rem})\vartheta(\square)\mathfrak{n}_ve^{-\frac18\delta D_v}$, free of weights,
with block sum by the remainder statement for box-read near units; the remainders of the
third class by the remainder statement for the third class.
\end{itemize}
Every entry of the table $\mathfrak{N}^P(v;\Theta)$ is non-decreasing and of degree at most
$3$ in $\Theta$, so that
\begin{equation}\label{5.5:eq-weight-d}
\mathfrak{N}^P\bigl(v;c_Ww^{\vee}(y)\bigr)\le c_W^3\,w^{\vee}(y)^3\,\mathfrak{N}^P(v;1).
\end{equation}
The far pieces read no datum; the pieces of the fourth kind in the total of
Definition~\ref{5.5:def-data-factor} sit at blocks meeting
$R_{\mathsf{n}}$, which by~(c) read no cell of $\mathcal{W}$.

\item[(c)] If $\Delta\in\mathcal{W}$, $y\in\tilde{\square}^2$ and
$\operatorname{dist}_n(\Delta,y)<1$, with $n=\min\{\ell(y),n_0\}$ as in
Definition~\ref{5.5:def-windowed-source}, then, writing $t(\Delta)$ for the step of the arrest
that raised $\Delta$ (Notation~\ref{5.5:not-weight-notation}),
\begin{equation}\label{5.5:eq-weight-e}
t(\Delta)\ge\ell(y),\qquad t(\Delta)\ge n_0-1,\qquad \square\in\mathfrak{O}^+ .
\end{equation}
If $\tilde{\square}^2$ holds a point of level at most $n_0-2$, then
$\tilde{\square}^2\subset X_{\mathfrak{c}}$ crosses the thin strata of the sequence of block
partitions $\mathbb{B}$ of exactly one
preparation $\mathfrak{c}$ ($X_{\mathfrak{c}}$ the region of $\mathfrak{c}$), of step
$t_{\mathfrak{c}}\ge n_0$ ($t_{\mathfrak{c}}:=k_{\mathfrak{c}}$
for an arrest, $t_{\mathfrak{c}}:=k$ for the running or a sibling preparation of this
$\mathbf{R}_k$), with $k_0(\mathfrak{c})\le n_0-2$ for the level $k_0(\mathfrak{c})$ attached
to $\mathfrak{c}$; every cell inside $\tilde{\square}^2$ has
level in $[k_0(\mathfrak{c}),n_0+1]$, and every weighted cell within one own unit of
$\tilde{\square}^2$ belongs to $\mathfrak{c}$. No window block, the exceptional ones
included, reads a cell of $\mathcal{W}$ through $\mathfrak{R}(\square)$; the set
$\tilde{\square}^5$ of an exceptional block may nevertheless meet $\mathcal{W}$, and this case
is treated in~(c$'$).

\item[(c$'$)] \textup{(Count times weight.)} Let $\tilde{\square}^5$ meet $\mathcal{W}$, so
that $\square\in\mathfrak{O}^+$ or $\square$ is exceptional, and $\varrho=\varrho(\square)\ge
\check{R}_k-4$; let $\mathfrak{K}(\square)$ be the sum of
\eqref{5.5:eq-weight-constants-b}. In case \textup{(i)}, where $\tilde{\square}^2$ holds no
point of level at most $n_0-2$, the first line of \eqref{5.5:eq-weight-f} holds; in case
\textup{(ii)}, where it holds such a point, with $t:=t_{\mathfrak{c}}\ge n_0$ as
in~(c) ($t=k$ at an exceptional block), the second line holds (recall
$L_{\circ}=\mathsf{L}_0$, Notation~\ref{5.5:not-weight-notation}):
\begin{equation}\label{5.5:eq-weight-f}
\begin{aligned}
&\text{(i)}\quad \mathfrak{K}(\square)\le 2(7L)^d
\max\bigl\{L_{\circ}^{6s(\square)},\,C^{\mathtt{a}}_{\mathrm{pr}}e^{\varrho-2}\bigr\},\\
&\text{(ii)}\quad \mathfrak{K}(\square)\le 3\cdot7^d\mathsf{L}_0^6L^{dN_0(t)}
\le C^{tile}e^{\varrho-1}.
\end{aligned}
\end{equation}
The majorant $\mathfrak{K}^{\sharp}(\square)$ denotes the right-most member of the applicable
case.

\item[(d)] At every block, the near-unit total at $\square$ (the total whose excess over
$L_{\circ}^{6s(\square)}\mathfrak{N}_0(\square)$ defines $\mathfrak{d}(\square)$ in
Definition~\ref{5.5:def-data-factor}) is at most
$\kappa_Rc_W^3\mathfrak{K}(\square)\mathfrak{N}_0(\square)\le
\mathsf{l}^2(\square)\mathfrak{N}_0(\square)$. Hence, where $\mathfrak{d}$ is not $1$ by
definition,
\begin{equation}\label{5.5:eq-weight-g}
\begin{gathered}
L_{\circ}^{6s(\square)}\mathfrak{d}(\square)\le\mathsf{l}^2(\square)
\le L_{\circ}^{6s(\square)}\mathfrak{d}^{\sharp}(\square),\quad\text{that is,}\\
\mathfrak{d}(\square)\le\mathfrak{d}^{\sharp}(\square)
\le 1+C^{\mathtt{a}}e^{\frac18\delta_Pd^{\wedge}(\square,R_{\mathsf{n}})}
\qquad(\mathfrak{d}^{\sharp}\ge1);
\end{gathered}
\end{equation}
elsewhere $\mathfrak{d}=1$. Thus \eqref{5.5:eq-data-factor-a} holds at every block in its
one-machine form, with degree $0$ in $\Theta$, and $C^{\mathtt{a}}\ge C^{\mathtt{a}}_{\mathrm{pr}}$.

\item[(e)] Let $\mathsf{A}$, $\mathsf{B}$ be two machines on one scaffold, and let
$\mathcal{K}:=\mathcal{K}^{rd}$ be their pair system, on which the four closure properties
(closure under restriction, closure under the response dilation, closure under the read
moves, closure under the paired charts) hold by the closure statements assumed above, as
does the closure under $\mathsf{M}8$, by the same assumed closure statements. For a pair
$\mathsf{p}$ of $\mathcal{K}^{rd}$ with components $P^{\mathsf{A}}$ and $P^{\mathsf{B}}$ put
$\delta f(\mathsf{p}):=f^{\mathsf{B}}(P^{\mathsf{B}})-f^{\mathsf{A}}(P^{\mathsf{A}})$,
$\mathsf{S}:=\mathsf{S}^{rd}$ and $\mathsf{a}:=\mathsf{S}^{rd}[\hat{A}]$, where $\hat{A}$ is
the slot letter of the Wilson and counterterm plaquette functional. Let
$\mathsf{R}^{\times}_{\mathsf{p}}$ be the pair of the move $\mathsf{M}2$ at the pieces read
on the box pair and the pair of the move $\mathsf{M}3$ at own-read units. Then for every near
unit $v$ and every $\mathsf{p}\in\mathcal{K}^{rd}(k;\mathsf{n}+1,\hat{X})$ (the pairs of stage
$\mathsf{n}+1$ over the region $\hat{X}$ of the source, at level $k$), on the filed disc,
\begin{multline}\label{5.5:eq-weight-h}
\bigl|\delta(f_v\circ\mathsf{R}^{\times}_{\mathsf{p}})-\delta f_v(\mathbb{1})\bigr|\\
\le w^{\vee}(y)^3\,\mathfrak{N}^P(v;c_W)
\Big|_{\mathfrak{n}\mapsto\mathsf{S}+\mathfrak{n}\mathsf{a},\;C_I'\mapsto C_I'',\;
\mathsf{s}_v\mathsf{v}_v\mapsto C^{\perp}\mathsf{S}^{\perp}_v}.
\end{multline}
The last substitution is made at the row of (b) for the remainders of the third class:
$\mathsf{s}_v$, $\mathsf{v}_v$ are the letters of the bound
$\mathfrak{N}^W_v=K^W\mathsf{s}_v\mathsf{v}_ve^{-\frac14\delta D_v}\alpha_{\cdot,j}$ of the
remainder statement for the third class, with $K^W$ the constant of that bound and
$\alpha_{\cdot,j}$ the level-$j$ radius of Definition~\ref{5.5:def-weight-constants};
$\mathsf{S}^{\perp}_v$ is the $\delta$-size in the slot $\circ$ of the third-class cell-unit
$v$, bounded a priori by $2\max\{\mathfrak{n}^{\perp}_v,\mathfrak{n}_{\hat{A}}\}$ in the
two-run statement for the third class, $\mathfrak{n}^{\perp}_v$ being the size bound of $v$ in
the slot $\circ$ and $\mathfrak{n}_{\hat{A}}$ being the largest bound on
the Wilson and counterterm functional over the moves that land in the slot $\circ$;
$C^{\perp}:=720L^2$. At the third class (the Wilson pieces of the block and the counterterm
companions of the cores, with their remainders), \eqref{5.5:eq-weight-h} holds on the chart
as written wherever the weighted scaffold majorants of
Definition~\ref{5.5:def-windowed-source} exist on the unit's own box (the read cores); off the
chart --- the
Wilson pieces of the block at every $\nu$, the remainder rows of the companions at every
$\nu$, and the second member of the two-run bound of the third-class remainder statement ---
it holds by the two-run statement for the third class together with the closure under
$\mathsf{M}8$. For the item $\mathfrak{n}\mathsf{a}$ of the counterterm companions at
$\nu\le2$, where the radius of the chart in the slot $\hat{A}$ would exceed one, the value is
supplied by the closure under the move $\mathsf{M}2$ in the slot $\circ$, while the table
factor requires the low-order variation bound at the second cube size, which is not a
hypothesis of this lemma; for that item no claim is made. The two-cutoff response statement
at zeroth order and the flat energy-difference bound are not hypotheses of this lemma.

Consequently the two-machine differences of the pieces entering the one-machine form of the
data-factor bound of Definition~\ref{5.5:def-data-factor}, at the one-block set
$\{\square\}$, satisfy that bound in its two-machine form, with the bound
\begin{equation*}
\mathsf{l}^2(\square)\cdot\mathfrak{n}_0\big|_{E_0+1\mapsto\mathsf{l}^J}\cdot
\bigl(\vartheta(\square)+\mathfrak{p}_{\mathsf{j}}\mathbb{1}[\square\ \text{meets}\
R_{\mathsf{n}}]\bigr),
\end{equation*}
where $E_0$ and $\mathfrak{n}_0$ are as in Definition~\ref{5.5:def-data-factor}; the factor
$\mathsf{l}^2(\square)$ is the same as in~(d), and the ratio $C_I''/C_I'$ is absorbed into
$\mathfrak{n}_0$; the cost of this transport is carried by the size-free member
$\kappa_R^{\times}$ of $\kappa_R$ in \eqref{5.5:eq-weight-constants-a}. Here
\begin{equation*}
\begin{split}
\mathsf{l}^J:=\max\Bigl\{&\max_{j\le k,\,\mathcal{F}}\max\bigl\{\mathsf{S}_j[\mathcal{F}],\
\mathsf{a}_j,\
\mathsf{S}_j[\mathcal{F}]+\mathfrak{n}_{\mathcal{F}}\mathsf{a}_j,\
\mathsf{b}_j+b_+\mathsf{a}_j\bigr\},\
\sup_v\mathsf{S}^{\perp}_v,\\
&\sup_{n\le k}C\sum_{j\le n}\bar{\rho}^{\,2}_{n,j}\,\mathsf{S}_j[R^{(j)}]\Bigr\},
\end{split}
\end{equation*}
the constant $C$ being that of the third per-cell row, and
the supremum over $v$ running over the third-class cell-units. In the letters of the
definition of the two-machine data functional, $\mathsf{S}_j[\mathcal{F}]$ is the level-$j$
$\delta$-size of the family $\mathcal{F}$ and $\mathfrak{n}_{\mathcal{F}}$ its size bound,
$\mathsf{a}_j$ is the level-$j$ $\delta$-size in the slot $\hat{A}$, $\mathsf{b}_j$ and $b_+$
are the further $\delta$-size and coefficient of that definition, $\bar{\rho}_{n,j}$ is its
radius ratio of the levels $n$ and $j$, and $R^{(j)}$ is the level-$j$ family of the third
row. Described in the notation of
this section, $\mathsf{l}^J$ is
the maximum of the per-cell row sums of the near-unit table at the $\delta$-sizes, summed
over $j$ (the third row being the last member of the display), and of
$\mathsf{S}$, $\mathsf{a}$, $\mathsf{S}+\mathfrak{n}\mathsf{a}$,
$\mathsf{b}_j+b_+\mathsf{a}$ and $\sup_v\mathsf{S}^{\perp}_v$. It is read on
$\mathcal{K}^{rd}\subset\mathrm{cl}^{pr}_J$, the production class, so that the same
functional formed on
$\mathrm{cl}^{pr}_J$ dominates it; it is a function of the $\delta$-sizes, and it is one of
the members of the data functional $\mathsf{l}_{\mathsf{n}+1}$ of stage $\mathsf{n}+1$. Only
the definition of $\mathsf{l}^J$ enters
this lemma; bounds on $\mathsf{l}^J$ are not used in it.
\end{enumerate}
\end{lemma}
```

### B3: 5.1:thm-correlation-theorem

CA-II:2791–2966. Status at source: unqualified heading, followed by a proof; conditional on the displayed inputs. For B2, the assembly nevertheless counts the weight machinery as incomplete (`chain-ca.md` §4); this port does not promote that machinery.

```latex
\begin{theorem}[The correlation theorem]\label{5.1:thm-correlation-theorem}
Assume the admitted inputs of Definition~\ref{5.1:def-admitted-inputs}, namely:
\begin{enumerate}
\item[(a)] Ba{\l}aban's renormalisation-group construction at zero source,
\cite[Theorem~1]{B-CMP122b}, of which Definition~\ref{5.1:def-admitted-inputs} admits the
identities and the source-free statements, every estimate on terms being re-proved;
\item[(b)] the source-free statements of Ba{\l}aban about configuration maps, domains and
operators that are admitted there by statement: the configuration statements on a
localisation domain's own box, together with the supplementary clause admitted with them,
and the random-walk statement and the
far-field statement of \eqref{5.1:eq-admitted-inputs-a};
\item[(c)] the statements listed there as inputs: the lower bound and the kernel bound for
the quadratic form $\mathcal{A}$ and the identities and source-free estimates taken from
\cite[(2.1)--(2.13), (2.27)--(2.41)]{B-CMP116}, all displayed in
\eqref{5.1:eq-admitted-inputs-a}, together with the
further statements listed in Definition~\ref{5.1:def-admitted-inputs}.
\end{enumerate}
Assume further the statement on the summation of boundary terms at finer zones.
Assume also the source-free statement on the resummation geometry at the preparatory site,
which Definition~\ref{5.1:def-admitted-inputs} admits as a further source-free hypothesis,
and the statement on the window data of the blocks at the preparatory site, on which the
relative bound for the boundary-type terms depends and whose proof is outstanding.

Fix $L$. Then fix Ba{\l}aban's auxiliary number $\mathsf{L}_0$ of \cite[(1.24)]{B-CMP122a}
(a number distinct from the constant $L_0$ of Theorem~0) subject to
\begin{equation*}
3\le\mathsf{L}_0<\tfrac12 L,\qquad \mathsf{L}_0^2\le L/3 ;
\end{equation*}
then the margin parameter $\delta$ of \cite[(1.32)]{B-CMP116} subject to
\begin{equation*}
\delta\in\,]0,\delta_J(L)],\qquad \delta_J(L):=\tfrac{1}{10}\bigl(1-4/L\bigr);
\end{equation*}
then $\kappa$ subject to $\kappa\ge\max\{10\log L,\ \kappa_d,\ C_\delta(d)/\delta\}$, the
member $10\log L$ being Ba{\l}aban's own floor of \cite{B-CMP119}, where
$\kappa_d$ and $C_\delta(d)$ are numbers depending on $d$ only; then $\kappa_1$ subject to
\begin{equation*}
\begin{split}
\kappa_1\ge\kappa_1^J(L,\kappa):=\max\bigl\{&16\kappa+1,\ 4L\kappa+1,\
1+c_l(2\kappa+4)+\lambda_\ast(d,L),\\
&2+a_k+3^dc_\flat+\log\bigl(2e^2\hat b_t^{\,2}N^\flat\bigr),\
4+c_\ast+\mathsf{c}_{\mathrm{an}}+2c_\flat\bigr\}
\end{split}
\end{equation*}
and to Ba{\l}aban's own floor $\tfrac12(\kappa_1-1)\ge 2L\kappa$ of \cite{B-CMP116}. Here
$c_l:=1+234d$; $\lambda_\ast(d,L)$ is an animal-counting constant depending on $d$ and $L$
only, always written with its arguments and distinct from $\lambda_*=(40M)^{-1}$ of
Definition~\ref{5.1:def-torus-floor}; $a_k:=(1+3\beta_{\mathrm{pr}})\kappa$ with
$\beta_{\mathrm{pr}}:=1/5$;
$\hat b_t:=(L+2)^d+3^d$; $N^\flat:=(10L+2)^d$; and $c_\flat$, $c_\ast$,
$\mathsf{c}_{\mathrm{an}}$ are numbers depending on $d$, $L$ and $\kappa$ only, not on $M$.
Then fix the block sizes, which are powers of $L$: $M_1$ with $M_1\ge M_E(d,L)$ and
$L^3M_1\ge R_E(d,L)$, and $M$ with $M>M_2:=L^2M_1$ (so that $M\ge L^3M_1$), subject to
\begin{equation*}
M\ge\max\{3L,2L^2\},\qquad
\delta_1M/M_1\ge 2,\qquad \delta_1M\ge\kappa_1,
\end{equation*}
where $\delta_1:=\min\{\mu_0/2,\delta_W/2\}$ with $\mu_0$, $\delta_W$ the $(d,L)$-numbers of
the order of choice; subject to the floor that $\tfrac14\delta_P$ times the weight per
stratum of the scaled distance $d^{\wedge}$ is at least $110d(a_k+1)$, where $\delta_P$ is
the rate of the exponential weights $e^{-\delta_P d^{\wedge}}$ built on $d^{\wedge}$;
and subject to the further one-sided lower bounds on $M_1$, on $M$ and on
$M/M_1$ (the last through the same weight per stratum), each imposed after $\kappa_1$ has
been fixed, that are
displayed in the subsections of this chapter where the rim and the localised remainder
corollary at the preparatory site are constructed. Fix $\kappa_0\ge 7$ and the exponents
subject to
\eqref{5.1:eq-analyticity-spaces-a}, the remaining parameters being as in hypothesis~(a).
The analysis constants and the $(d,L)$-numbers and functions of the rim construction
are chosen in the order of choice \eqref{5.1:eq-admitted-inputs-b}, which begins with the
absolute number $\theta_S\in[\tfrac12,\tfrac89]$, in which $L$, $\delta$, $\kappa$,
$\kappa_1$, $M_1$, $M$ are followed by $\mathsf{a}:=A_0/A_1$, $C_{\mathrm{far}}$ and the
remaining constants, and in which $\gamma$, the ceiling on the coupling, comes last.
The number $r$ is fixed before $\gamma$: fix $r>0$.

Then there is $\gamma_J=\gamma_J(L,\delta,M,M_1,\kappa,\kappa_1,\kappa_0,\dots,r)>0$ with
\begin{equation*}
\gamma_J\le\gamma^\circ:=(8c_2+4)^{-1/2}
\end{equation*}
such that for every $g\le\gamma_J$, every $x_0>g^{-2}$, with $K=K(x_0,g)$ the first-passage
index of Definition~\ref{5.1:def-reference-recursion}, every integer $m$ with
$m_{\mathbb{T}}(g)\le m\le K$ (the lower bound being the torus floor
$L^m\ge N_{\mathbb{T}}(g,m)$ of \eqref{5.1:eq-torus-floor-a}) and every integer
$N_T\ge 1$, with $N:=N_TL^m$ and $K':=K-m$, the following hold.
\begin{enumerate}
\item[(i)] The reference recursion of Definition~\ref{5.1:def-reference-recursion} is
defined; the first line of the display below holds for $0\le i<j\le K$, the chain of
inequalities at the beginning of its second line holds for every $k$ with $0\le k\le K$,
and $x_K$ lies in the interval stated there:
\begin{equation}\label{5.1:eq-correlation-theorem-a}
\begin{gathered}
\lambda(j-i)-2c_2\le x_i-x_j\le 3\lambda(j-i)+2c_2,\\
|b_{k+1}(0)-\beta^0_{k+1}|\le C_\beta\mathrm{e}_k+v_k\le\lambda,\qquad
x_K\in\,]X,X+b_+],\quad b_+:=3\lambda+2c_2 .
\end{gathered}
\end{equation}
\item[(ii)] (The running-shift statement.) For $k<K$ the coefficient $b_{k+1}$ and the
running shift $\zeta_{k+1}$ are analytic functions of the bare shift $\zeta$ on
$D(0,2r)$, real for real $\zeta$; the function $f_{k+1}$ of the variables
$(\xi_0,\dots,\xi_k)$ is holomorphic on the polydisc
$\mathfrak{P}_k:=\prod_{j\le k}D(0,\sigma_{\mathrm{rad}}x_j)$, with $\sigma_{\mathrm{rad}}$
the radius constant of Definition~\ref{5.1:def-reference-recursion}, and the term
$\beta\bigl[\mathsf{P}^{(k+1)}-L^{(k+1)}\bigr]$ below is its value at $\xi_j=\zeta_j$,
$j\le k$; here $\mathsf{P}^{(k+1)}$ and $Q^{(k+1)}$ are formed from the three families at
scale $k+1$ of Definition~\ref{5.2:def-three-families}, and $\beta[\cdot]$,
$L^{(k+1)}$, $\beta^0_{k+1}$ and $\|\cdot\|^\flat$ are as in
\eqref{5.1:eq-analyticity-spaces-c}; and
\begin{equation}\label{5.1:eq-correlation-theorem-b}
\begin{aligned}
&\zeta_{k+1}=\zeta_k+b_{k+1}(\zeta)-b_{k+1}(0),\\
&b_{k+1}=\beta^0_{k+1}+\beta\bigl[\mathsf{P}^{(k+1)}-L^{(k+1)}\bigr]
+\beta\bigl[Q^{(k+1)}\bigr],\\
&\beta\bigl[\mathsf{P}^{(k+1)}-L^{(k+1)}\bigr]=f_{k+1}(\zeta_0,\dots,\zeta_k),
\qquad |f_{k+1}|\le C_\beta\mathrm{e}_k,\\
&\sup_{\frac12\mathfrak{P}_k}\ \sum_{j\le k}\sigma_{\mathrm{rad}}x_j
\Bigl|\frac{\partial f_{k+1}}{\partial\xi_j}\Bigr|\le\frac43\,C_\beta\mathrm{e}_k,\\
&\sup_{\zeta\in D(0,2r)}\bigl|\beta[Q^{(k+1)}_\zeta]\bigr|\le v_k,\qquad
\|Q^{(k+1)}_\zeta\|^\flat\le\mathfrak{m}_k,\\
&|b_{k+1}(\zeta)-b_{k+1}(0)|\le d_k(\varrho)|\zeta|\ \text{ on }D(0,\varrho)
\qquad\text{for every }\varrho\in[r,2r],\\
&\sum_{k<K}d_k(\varrho)\le C_{\mathfrak{D}}\Bigl[\lambda^{-1}g(\log g^{-2})^{p_0}
+\frac{g^{\kappa_0-6}}{\lambda\varrho}\Bigr]\le\frac13
\qquad\text{for every }\varrho\in[r,2r],\\
&|\zeta_k-\zeta|\le\tfrac13|\zeta|,\qquad
\sum_k\operatorname{Lip}_{\bar D(0,r)}b_{k+1}\le\tfrac23,\\
&N_K:=\frac{d\zeta_K}{d\zeta}(0)\in\bigl[\tfrac23,\tfrac43\bigr].
\end{aligned}
\end{equation}
Here $C_{\mathfrak{D}}$ is a constant.
All dependence on $\zeta$ --- through every earlier slot factor, every older term and
every remnant --- is contained in these statements.
\item[(iii)] For $k\le K'$ and $w\in\mathcal{W}_k$, the density $\rho^w_k$ defined by the
first member of the display below, in which $T^w$ and $R^\flat$ are the two operations
whose composite $R^\flat T^w$ is one step of the induction on the level, has the induction
format with sources of Definition~\ref{5.2:def-induction-format} at level $k$;
its terms are analytic in $w$, a term localised in a domain $X$ depends on $w$ only
through its restriction to $X^+$
(Definition~\ref{5.1:def-weight-classes}), and the terms satisfy the bounds of
Ba{\l}aban's construction with the enlarged activity constants of
\eqref{5.1:eq-admitted-inputs-c}. Moreover the
second and the third relation of the display hold, the third for every plaquette $p$,
where $\zeta_k(p)$ is the running shift at level $k$ at the plaquette $p$ for the
source $w$:
\begin{equation}\label{5.1:eq-correlation-theorem-c}
\rho^w_k:=(R^\flat T^w)^k\rho_0^w,\qquad
\int\rho^w_k\,dV_k=\int\rho_0^w\,dU,\qquad |\zeta_k(p)|\le\tfrac43\sup|w|.
\end{equation}
\item[(iv)] (The torus bound.) For $n\ge 2$ and test functions $f_1,\dots,f_n$ whose
supports are pairwise at distance at least $\mathsf{d}>0$, with $Z(z)$ the integral of
\eqref{5.1:eq-torus-floor-b} at the source $w=\sum_i z_if_i$,
\begin{equation}\label{5.1:eq-correlation-theorem-d}
\begin{gathered}
\Bigl|\partial_{z_1}\cdots\partial_{z_n}\log Z(z)\big|_{z=0}\Bigr|
\le\bigl[C_{UV}(\mathsf{d})+\log 2\cdot(2\mathsf{Q}+2)^n\bigr]
\Bigl(\frac nr\Bigr)^n\prod_{i=1}^n\|f_i\|_\sharp,\\
\mathsf{Q}=e^{(E_+^\sharp+C_{\mathrm{low}})N^4},\qquad
C_{UV}(\mathsf{d})\le C\mathsf{d}^{-4}\bigl(1+\log^+\mathsf{d}^{-1}\bigr),
\end{gathered}
\end{equation}
with a constant $C$, where $E_+^\sharp$ and $C_{\mathrm{low}}$ are constants fixed in the
treatment of the last lattice. Hence, the bound not depending on $K$, the derivatives
$\partial_{z_1}\cdots\partial_{z_n}\log Z(z)|_{z=0}$ have subsequential limits as
$K\to\infty$ at fixed $m$ and $N_T$, and these limits are connected Schwinger functions
of the smeared action density $\operatorname{tr}F\cdot F$ off the diagonals; they are
symmetric, lattice-covariant and reflection positive
(Proposition~\ref{5.12:prop-subsequential-limits} and
Lemma~\ref{5.12:lem-limit-positivity}).
\end{enumerate}
None of the constants depends on $K$, $k$, $m$, the torus or the position; $N$ enters only
through $\|\cdot\|_\sharp$, through $\mathsf{Q}$ and, through $m$, through the torus floor
\eqref{5.1:eq-torus-floor-a}. The frozen whole-lattice objects --- $b_j$, $\zeta_j$, and
the families $\mathsf{P}_\xi$, $E_\zeta$, $P^\flat_\zeta$, $Q_\zeta=E_\zeta-P^\flat_\zeta$
and $R_\zeta$ constructed in the induction on the level, the reference sequence
$x_j$ and $K$ --- are numbers and families that do not depend on the torus; for the levels
$K'<k\le K+1$, at which the physical torus is too small, they are constructed on the
auxiliary tori of Definition~\ref{5.2:def-auxiliary-torus}, whose side is a power of $L$.
\end{theorem}
```

### B4a: 5.3:lem-driven-flow

CA-II:26201–26231. Status at source: unqualified heading, followed by a proof; conditional on the displayed inputs. For B2, the assembly nevertheless counts the weight machinery as incomplete (`chain-ca.md` §4); this port does not promote that machinery.

```latex
\begin{lemma}[The driven flow of the running shift]\label{5.3:lem-driven-flow}
For $c\in\mathbb{C}$ and $R>0$ let $D(c,R)$ denote the open disc of radius $R$ about $c$. Let $K\ge 1$
and $\mathfrak{d}_0,\dots,\mathfrak{d}_{K-1}>0$. For $0\le k\le K-1$ put
\begin{equation*}
\mathfrak{P}_k:=\prod_{j\le k}D(0,\mathfrak{d}_j)\subset\mathbb{C}^{k+1},
\qquad
\mathfrak{d}_*(k):=\min_{j\le k}\mathfrak{d}_j .
\end{equation*}
For each $k<K$ let $f_{k+1}$ be holomorphic on $\mathfrak{P}_k$ with $|f_{k+1}|\le\omega_k$. Let
$\varrho>0$ satisfy $\tfrac83\varrho\le\mathfrak{d}_*(K-1)$. Suppose that, for each $k<K$, whenever
$\zeta_0,\zeta_1,\dots,\zeta_k$ are holomorphic functions on $D(0,\varrho)$, with $\zeta_0(\zeta):=\zeta$ and
$|\zeta_j(\zeta)-\zeta|\le\tfrac13|\zeta|$ for $j\le k$ and $\zeta\in D(0,\varrho)$, a function
$\mathsf{q}_{k+1}$ holomorphic on $D(0,\varrho)$ with $|\mathsf{q}_{k+1}|\le v_k$ is given; define then
$\zeta_{k+1}$ on $D(0,\varrho)$ by
\begin{equation}\label{5.3:eq-driven-flow-1}
\zeta_{k+1}(\zeta):=\zeta_k(\zeta)
+\bigl[f_{k+1}(\zeta_0(\zeta),\dots,\zeta_k(\zeta))-f_{k+1}(0)\bigr]
+\bigl[\mathsf{q}_{k+1}(\zeta)-\mathsf{q}_{k+1}(0)\bigr].
\end{equation}
Put
\begin{equation}\label{5.3:eq-driven-flow-2}
d_k:=\frac{16}{9}\,\frac{\omega_k}{\mathfrak{d}_*(k)}+\frac{2v_k}{\varrho}\qquad(0\le k<K).
\end{equation}
If $\sum_{k<K}d_k\le\tfrac13$, then for all $k<K$ the flow \eqref{5.3:eq-driven-flow-1} is defined,
and on $D(0,\varrho)$
\begin{equation}\label{5.3:eq-driven-flow-3}
|\zeta_{k+1}-\zeta_k|\le d_k|\zeta|,
\qquad
|\zeta_{k+1}-\zeta|\le\tfrac13|\zeta| .
\end{equation}
\end{lemma}
```

### B4b: 5.14:thm-one-loop-law

CA-II:27042–27082. Status at source: unqualified heading, followed by a proof; conditional on the displayed inputs. For B2, the assembly nevertheless counts the weight machinery as incomplete (`chain-ca.md` §4); this port does not promote that machinery.

```latex
\begin{theorem}[Exact one-loop law of the construction's running coupling]\label{5.14:thm-one-loop-law}
Let $N\ge 2$, let the blocking factor $L$, Ba{\l}aban's auxiliary parameters $\mathfrak{p}$ and the
remaining constants be chosen as in the prefix of Theorem~0, and let hypothesis (H7) of Theorem~0 be
in force, so that the reference coupling satisfies $g\le\gamma_J$. The letters are those of
Notation~\ref{5.14:not-flow-notation}, and $\mathfrak{e}_u$, $C_v$, $\Delta$ are the majorants of
Definition~\ref{5.14:def-defect-majorants}. Assume:
\begin{enumerate}
\item[(a)] the flow statement of the correlation theorem, that is, the bounds
\eqref{5.14:eq-flow-notation-d}: for $N=2$ as part of Theorem~\ref{5.1:thm-correlation-theorem}, and
for $N\ge 3$ as part of Proposition~\ref{5.13:prop-sun-correlation};
\item[(b)] the one-loop lemma, in the form \eqref{5.14:eq-flow-notation-b} recorded in
Notation~\ref{5.14:not-flow-notation}.
\end{enumerate}
Then for every $g\le\gamma_J$, every $g_0\in\left]0,g_{-}(g)\right]$ with $K=K(g_0,g)$, every $m$ of
the family of tori, and all $0\le i<j\le K$,
\begin{equation}\label{5.14:eq-one-loop-law-a}
\bigl|x_i-x_j-(j-i)\,c_0\bigr|\le 2c_2+\sum_{k=i}^{j-1}\bigl[C_\beta\,e(g_k)+v_k\bigr].
\end{equation}
In particular, for every $0\le s\le K$,
\begin{align}
\bigl|x_{K-s}-x_K-s\,c_0\bigr|
&\le 2c_2+\sum_{u=1}^{s}\bigl[C_\beta\,e(g_{K-u})+v_{K-u}\bigr]\notag\\
&\le \Delta(s)=2c_2+C_v+C_\beta\sum_{u=1}^{s}\mathfrak{e}_u,
\label{5.14:eq-one-loop-law-b}
\end{align}
and $\Delta(s)/s\to 0$ as $s\to\infty$. Here
\begin{equation}\label{5.14:eq-one-loop-law-1}
c_0=\frac{11N^2}{12\pi^2}\,\log L .
\end{equation}
The majorant $\Delta$ depends on $(L,N,\mathfrak{p})$ only; the convergence $\Delta(s)/s\to 0$ is
therefore uniform in $K\ge s$, in $g\le\gamma_J$, in $g_0$, in $m$ and in the position of the
sources, on which no constant of the correlation theorem depends. Consequently, along every
subsequence of the corollary to clause~(0) of
Theorem~0, that is, for $g_0^{(i)}\downarrow 0$ with $K_i:=K(g_0^{(i)},g)\ge s$ and
$g_{K_i-s}\to g_{\infty,s}$, one has
\begin{equation}\label{5.14:eq-one-loop-law-c}
g_{\infty,s}^{-2}\in\bigl[\,g^{-2}+s\,c_0-\Delta(s),\;g^{-2}+B^{\sharp}+s\,c_0+\Delta(s)\,\bigr],
\end{equation}
so that $g_{\infty,s}^{-2}/(s\,c_0)\to 1$ as $s\to\infty$, and $(x_{K-s}-x_K)/s\to c_0$ as
$s\to\infty$, uniformly in $K\ge s$.
\end{theorem}
```

## Proof-port convention

The complete source proof passages follow in their original TeX, preserving every constant and invocation. Numbered **(filled)** annotations supply implicit algebra, limits and admission steps. **(correction)** annotations override only the identified printed step. Invoking another result retains it as a named hypothesis here unless its full proof is included or its precise repository standing is given. A source sentence saying a supplier “gives” an estimate does not establish that supplier. This is a port of the account's own route, with no computer-assisted proof.

## B2a: decoupling-weight proof and inputs

| Name | Label and locus | Standing |
|---|---|---|
| W6-H | 5.6:eq-weight-a, II:45161–45176 | Holomorphy and bound for each fixed datum assumed. Its actual-term supplier B1, 5.6:prop-polydisc-holomorphy, II:46131–46167, is outstanding. |
| W6-piece | 5.6:def-decoupling-variables, II:44707–44790; 5.6:def-pieces, II:44792–44878 | Finite-variable definitions and probability-measure representation of pieces. |
| W6-chain | 5.6:eq-pieces-b, II:44829–44854 | (π1)–(π3) explicitly assumed, abstracted from Balaban CMP 122b (1.61)–(1.66). Chain injectivity is not a holomorphy consequence. |
| W6-length | 5.6:def-linear-sizes, II:44602 onward; 5.6:lem-tree-length-adjunction, II:45479–45581 | General adjunction property assumed. CA proves the free-length and contained-length instances with \(c'=d\) and \(c'=1\), respectively. Named inputs here. |
| W6-Cauchy | 5.6:lem-cauchy-factor, II:44941–45006; 5.6:lem-cauchy-estimates, II:45008–45152 | Elementary CA implications; their needed argument appears below. |
| W6-count | 5.6:lem-rooted-sets, II:45645–45701; 5.6:lem-tree-cells, II:45703–45772 | CA combinatorial implications retained as named inputs, with their encoding explained below. |
| W6-decay | II:45206–45209, 45629–45642 | Decay on the exempt set assumed. Balaban CMP 122b (1.66), and its relative length (1.67), are named published inputs. Smaller-set decay needs a separate comparison. |

### (a): per-piece Cauchy estimate

CA-II:45301–45366. Complete original passage by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; annotations following it are part of this port.

```latex
\begin{proof}[Proof of (a)]
Fix $\mathfrak{d}\in\mathcal{D}_b$ and a piece $p$ with data $(W,\mu)$, $|W|=m$; by
Definition~\ref{5.6:def-pieces},
\begin{equation*}
p(\mathfrak{d})=\int_{[0,1]^{\mathcal{V}}}\mu(d\sigma)\,(\partial^WF_t)(\sigma;\mathfrak{d}),
\end{equation*}
with $\mu$ a Borel probability measure on $[0,1]^{\mathcal{V}}$. Since
$\kappa_1\ge 1$ by $(\mathrm{H}_{\circ})$, $e^{\kappa_1}\ge e>1$.

For $s\in[0,1]^{\mathcal{V}\setminus W}$ define the slice
\begin{equation*}
G_s(\sigma_W)=F_t(\sigma_W,s;\mathfrak{d}),\qquad\sigma_W\in P_W(e^{\kappa_1}),
\end{equation*}
where $(\sigma_W,s)$ is the point of $\mathbb{C}^{\mathcal{V}}$ with $W$-coordinates $\sigma_W$ and
$(\mathcal{V}\setminus W)$-coordinates $s$. Every coordinate of $s$ has modulus at most
$1<e^{\kappa_1}$, so
$[0,1]^{\mathcal{V}\setminus W}\times P_W(e^{\kappa_1})\subset P_{\mathcal{V}}(e^{\kappa_1})$. By
$(\mathrm{H}_{\circ})$, $F_t(\cdot;\mathfrak{d})$ is continuous and separately holomorphic on
$P_{\mathcal{V}}(e^{\kappa_1})$ and bounded there by $\mathfrak{b}$; restricting to the set just
described, $G_s$ is continuous and separately holomorphic on $P_W(e^{\kappa_1})$ with
$|G_s|\le\mathfrak{b}$. Since
$\partial^W$ differentiates in the $W$-coordinates only,
\begin{equation*}
\partial^WF_t(\sigma;\mathfrak{d})=\partial^WG_{\sigma_{\mathcal{V}\setminus W}}(\sigma_W)
\qquad\text{for }\sigma\in[0,1]^{\mathcal{V}}.
\end{equation*}
Lemma~\ref{5.6:lem-cauchy-estimates}, applied to $G=G_{\sigma_{\mathcal{V}\setminus W}}$ with
radius $e^{\kappa_1}$ and bound $\mathfrak{b}$ in place of the lemma's $R$ and $B$, gives by
\eqref{5.6:eq-cauchy-estimates-a}, at the point
$\sigma_W\in[0,1]^W$ where $|\sigma_w|\le 1$ for each $w\in W$,
\begin{align*}
|\partial^WF_t(\sigma;\mathfrak{d})|
&\le\mathfrak{b}\prod_{w\in W}e^{\kappa_1}\bigl(e^{\kappa_1}-|\sigma_w|\bigr)^{-2}\\
&\le\mathfrak{b}\,\bigl[e^{\kappa_1}(e^{\kappa_1}-1)^{-2}\bigr]^m=\mathfrak{b}\,r(\kappa_1)^m
\qquad\text{for every }\sigma\in[0,1]^{\mathcal{V}}.
\end{align*}
(For $m=0$ one has $\partial^{\emptyset}F_t=F_t$, and the bound by $\mathfrak{b}=\mathfrak{b}\,r(\kappa_1)^0$
is $(\mathrm{H}_{\circ})$ itself, since $[0,1]^{\mathcal{V}}\subset P_{\mathcal{V}}(e^{\kappa_1})$.)

Lemma~\ref{5.6:lem-cauchy-estimates}, applied to $F_t(\cdot;\mathfrak{d})$ on
$P_{\mathcal{V}}(e^{\kappa_1})$ (the finite set there being $\mathcal{V}$, the radius $e^{\kappa_1}$
and the bound $\mathfrak{b}$), shows that $F_t(\cdot;\mathfrak{d})$
is $C^\infty$ on $P_{\mathcal{V}}(e^{\kappa_1})$. Hence $\partial^WF_t(\cdot;\mathfrak{d})$ is
continuous on the
compact cube $[0,1]^{\mathcal{V}}$, in particular Borel measurable and bounded, and the integral
defining $p(\mathfrak{d})$ exists. Since $\mu$ is a probability measure,
\begin{equation*}
|p(\mathfrak{d})|\le\int_{[0,1]^{\mathcal{V}}}\mu(d\sigma)\,|\partial^WF_t(\sigma;\mathfrak{d})|
\le\mathfrak{b}\,r(\kappa_1)^m .
\end{equation*}
This holds for each $\mathfrak{d}\in\mathcal{D}_b$ separately, with a right side independent of
$\mathfrak{d}$; taking the supremum over $\mathfrak{d}\in\mathcal{D}_b$ gives the first inequality of
\eqref{5.6:eq-weight-b}, and no property of the dependence on $\mathfrak{d}$ is needed. Finally, by
Lemma~\ref{5.6:lem-cauchy-factor}, $0\le r(\kappa_1)\le e^{-(\kappa_1-1)}$ for $\kappa_1\ge 1$; raising
to the power $m\ge 0$ gives $r(\kappa_1)^m\le e^{-(\kappa_1-1)m}$, the second inequality of
\eqref{5.6:eq-weight-b}.

Thus each differentiated variable costs the factor
\begin{equation*}
e^{\kappa_1}\bigl(e^{\kappa_1}-|\sigma_w|\bigr)^{-2}\le e^{\kappa_1}\bigl(e^{\kappa_1}-1\bigr)^{-2}
=r(\kappa_1),
\end{equation*}
the undifferentiated variables being held at their
real values in $[0,1]$, inside the polydisc where the bound $|F_t|\le\mathfrak{b}$ still holds, and
the averages over $[0,1]$ cost the factor $1$.
\end{proof}
```

**W6-F1 (filled: Cauchy limits and empty cases).** Fix the datum first. For differentiated coordinates choose circles \(|\sigma_w|<r_w<R=e^{\kappa_1}\), keeping other coordinates fixed in \([0,1]\). Iterated Cauchy yields
\[
|\partial^WF_t|\le\mathfrak b\prod_{w\in W}\frac{r_w}{(r_w-|\sigma_w|)^2}.
\]
Continuity and separate holomorphy suffice on these finite compact products. Let \(r_w\uparrow R\). On the real cube the derivatives are continuous, hence integrable against the specified probability measure of mass one. Take the datum supremum last. For \(W=\varnothing\) use W6-H directly. A datum-only constant has zero mixed derivative for nonempty \(W\), without any datum measurability assumption.

The scalar inequality retains the account's factor: for \(x\ge e\), \(x/(x-1)^2\le e/x\). At the smallest \(x=e\) it is equivalent to \(e^2-3e+1\ge0\); indeed \(e>8/3>21/8>(3+\sqrt5)/2\), since \(81/16>5\). Thus \(r(\kappa_1)\le e^{-(\kappa_1-1)}\le1\). This is the account's Cauchy-factor route, not its subsequent sharper product-difference route.

### (b): fixed final domain

CA-II:45425–45477. Complete original passage by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; annotations following it are part of this port.

```latex
\begin{proof}[Proof of the count of pieces at a fixed final domain]
\label{5.6:prf-fixed-domain-count}
We prove clause \eqref{5.6:eq-weight-c} of the weight lemma (Lemma~\ref{5.6:lem-weight}). Its
hypotheses are \eqref{5.6:eq-weight-a}, that is, $(\mathrm{H}_{\circ})$, which includes
$\kappa_1\ge 1$, and the first two counting readings $(\pi 1)$--$(\pi 2)$ of
\eqref{5.6:eq-pieces-b} for the pieces of Definition~\ref{5.6:def-pieces}.

Fix a final domain $Y$. Let $\mathcal{N}'(t;Y)$ be the set of cells of $Y\setminus Y_1(t)$, and
let $n=n(t;Y)$ be their number. By $(\pi 1)$, every $p\in\mathcal{P}(t;Y)$ has $|W(p)|\ge n$. By
$(\pi 2)$, the map $p\mapsto(Y'_i)_{i\in I}$ from $\mathcal{P}(t;Y)$ to the ordered
$\lambda$-partitions of $\mathcal{N}'(t;Y)$ is injective, so
$\#\mathcal{P}(t;Y)\le\lambda^n$. The reason for this count is as follows. Each of the $n$ cells
of $Y\setminus Y_1(t)$ enters the chain of domains at exactly one of the $\lambda$ links. Sending
each cell to the index $i\in I$ of the increment $Y'_i$ that contains it identifies an ordered
$\lambda$-partition $(Y'_i)_{i\in I}$ with a map $\mathcal{N}'(t;Y)\to I$, that is, with a choice
function assigning to each cell its link. There are $\lambda^n$ such maps, and admissibility of a
partition only removes some of them.

Since $\kappa_1\ge 1$, the elementary inequality for the Cauchy factor
(Lemma~\ref{5.6:lem-cauchy-factor}) gives
\[
0<r(\kappa_1)\le e^{-(\kappa_1-1)}\le 1 .
\]
By clause \eqref{5.6:eq-weight-b}, each $p\in\mathcal{P}(t;Y)$ obeys
$\sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|\le\mathfrak{b}\,r(\kappa_1)^{|W(p)|}$.
Because $r(\kappa_1)\le 1$ and $|W(p)|\ge n$, this is at most $\mathfrak{b}\,r(\kappa_1)^n$.
Summing over the at most $\lambda^n$ pieces and applying the bound on $r(\kappa_1)$ once more, we
obtain
\begin{equation}\label{5.6:eq-fixed-domain-count-1}
\sum_{p\in\mathcal{P}(t;Y)}\ \sup_{\mathfrak{d}\in\mathcal{D}_b}|p(\mathfrak{d})|
\le\lambda^n\,\mathfrak{b}\,r(\kappa_1)^n
\le\mathfrak{b}\,\bigl(\lambda e^{-(\kappa_1-1)}\bigr)^n .
\end{equation}

If $n=0$, the right-hand side of \eqref{5.6:eq-fixed-domain-count-1} equals $\mathfrak{b}$.

Now let $n\ge 1$. Taking logarithms,
\[
\lambda e^{-(\kappa_1-1)}\le 1
\iff \log\lambda-(\kappa_1-1)\le 0
\iff \kappa_1\ge 1+\log\lambda .
\]
Under this condition, \eqref{5.6:eq-fixed-domain-count-1} is at most $\mathfrak{b}$. In the same
way,
\[
\lambda e^{-(\kappa_1-1)}\le\tfrac12
\iff \log(2\lambda)-(\kappa_1-1)\le 0
\iff \kappa_1\ge 1+\log 2\lambda .
\]
Under this condition, \eqref{5.6:eq-fixed-domain-count-1} is at most $\mathfrak{b}\,2^{-n}$.
These are the two clauses. For $\lambda=3$ the two conditions read $\kappa_1\ge 1+\log 3$ and
$\kappa_1\ge 1+\log 6$, where $1+\log 6=1+\log(2\cdot 3)$.
\end{proof}
```

### (c): decay transfer

CA-II:45583–45643. Complete original passage by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; annotations following it are part of this port.

```latex
\begin{proof}[Proof of part (c) of the weight lemma: transfer of the decay to the final domain]
\label{5.6:prf-decay-transfer}
We argue from three hypotheses: the holomorphy hypothesis $(\mathrm{H}_{\circ})$, \eqref{5.6:eq-weight-a}; the
counting forms $(\pi 1)\text{--}(\pi 3)$ of the pieces, \eqref{5.6:eq-pieces-b}; and the adjunction property
$(\mathrm{TL})_{c'}$ of the linear size $\ell$, \eqref{5.6:eq-linear-sizes-a}. We also use parts (a) and (b)
of the weight lemma (Lemma~\ref{5.6:lem-weight}), \eqref{5.6:eq-weight-b} and \eqref{5.6:eq-weight-c}.
Let $a \ge 0$, and assume $\mathfrak{b} \le \mathfrak{b}_0 e^{-a\ell(Y_1(t))}$.

Let $Y$ be a final domain with $\mathcal{P}(t;Y) \neq \emptyset$, and put $n = n(t;Y) = \#(Y \setminus Y_1(t))$.
By $(\pi 3)$, $Y \supseteq Y_1(t)$ and every $\sim$-component of $Y$ meets $Y_1(t)$. These are exactly the
hypotheses of $(\mathrm{TL})_{c'}$ with $Y_1 = Y_1(t)$, so
\begin{equation}\label{5.6:eq-decay-transfer-1}
\ell(Y) \le \ell(Y_1(t)) + c' n .
\end{equation}
Suppose first that $\ell(Y_1(t)) = \infty$. Then the assumption on $\mathfrak{b}$ forces $\mathfrak{b} = 0$, and
by (a) all pieces vanish, so there is nothing to prove. Suppose now that $\ell(Y_1(t)) < \infty$. Then
$\ell(Y) < \infty$ by \eqref{5.6:eq-decay-transfer-1}. Multiplying \eqref{5.6:eq-decay-transfer-1} by
$a \ge 0$ and exponentiating gives
\begin{equation*}
e^{-a\ell(Y_1(t))} \le e^{-a\ell(Y)}\, e^{a c' n}.
\end{equation*}

The bound (b), combined with $\mathfrak{b} \le \mathfrak{b}_0 e^{-a\ell(Y_1(t))}$ and then with the last
inequality, gives
\begin{align*}
\sum_{p \in \mathcal{P}(t;Y)} \sup |p|
 &\le \mathfrak{b}_0\, e^{-a\ell(Y_1(t))} \bigl(\lambda e^{-(\kappa_1 - 1)}\bigr)^{n}
 \le \mathfrak{b}_0\, e^{-a\ell(Y)} \bigl(\lambda e^{-(\kappa_1 - 1) + c' a}\bigr)^{n} \\
 &= \mathfrak{b}_0\, e^{-a\ell(Y)} \bigl(\lambda e^{-(\kappa_1 - 1 - c' a)}\bigr)^{n}.
\end{align*}
This is the first inequality of \eqref{5.6:eq-weight-d}. Taking logarithms, we have
$\lambda e^{-(\kappa_1 - 1 - c'a)} \le 1$ if and only if $\kappa_1 \ge 1 + \log\lambda + c'a$. This is the
one-sided floor $(\mathrm{F}\text{-}\kappa_1)^{P}$, \eqref{5.6:eq-weight-e}. Under it the $n$-th power is at
most $1$, which gives the second inequality of \eqref{5.6:eq-weight-d}. For $n = 0$ the power equals $1$,
and no floor is used.

We now read off the size of $c'a$. By the lemma on tree lengths under adjunction of cells
(Lemma~\ref{5.6:lem-tree-length-adjunction}), property $(\mathrm{TL})_{c'}$ holds in two cases:
\begin{itemize}
\item with $c' = d$ for the free tree length $d_k^{\mathrm{fr}}$;
\item with $c' = 1$ for the contained tree length $d_k^{\subset}$ under face adjacency.
\end{itemize}
The decay rate of Ba{\l}aban's inductive factor is $a = (1+3\beta)\kappa$, and $a \le 2\kappa$ for
$\beta \le \tfrac13$. Hence at $d = 4$ and $c' = d$ we have $c'a \le d \cdot 2\kappa = 8\kappa$, and at
$c' = 1$ we have $c'a \le 2\kappa$. The number of links of the chain is $\lambda = 3$. Thus
$(\mathrm{F}\text{-}\kappa_1)^{P}$ holds as soon as $\kappa_1 \ge 1 + \log 3 + 8\kappa$ in the first case,
and as soon as $\kappa_1 \ge 1 + \log 3 + 2\kappa$ in the second.

Finally, compare this with the one-sided condition $\kappa_1 \ge 16\kappa + 1$ on the auxiliary parameters.
We have
\begin{equation*}
16\kappa + 1 \ge 1 + \log 3 + 8\kappa
\iff 8\kappa \ge \log 3 .
\end{equation*}

The transfer proved here is in the plain linear size $\ell$. Ba{\l}aban's own extraction, from the exponential
of \cite[(1.66)]{B-CMP122b}, is made in a linear size relative to the large-field region, defined in
\cite[(1.67)]{B-CMP122b}; the argument above does not use it. Suppose the decay available where the bound is used
sits on a set $Y_0$ with $Y_0 \subsetneq Y_1(t)$. Then the comparison of $\ell(Y_1(t))$ with $\ell(Y_0)$ is
not supplied by part (c), and has to be made at the place of use.
\end{proof}
```

**W6-C1 (correction: zero decay rate).** II:45597–45599 infers that infinite \(\ell(Y_1)\) forces \(\mathfrak b=0\), but this requires \(a>0\). When \(a=0\), read the zero-rate weight as one and use (b) directly. When \(a>0\), W6-H does annihilate the pieces. This repairs the \(0\cdot\infty\) boundary case without changing a constant. At \(n=0\) no floor is needed.

### (d): all final domains

CA-II:45774–45882. Complete original passage by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; annotations following it are part of this port.

```latex
\begin{proof}[Proof of part (d) of Lemma~\ref{5.6:lem-weight}: sum over all final domains with prefactor]
\label{5.6:prf-all-final-domains}
Assume hypothesis $(\mathrm{H}_{\circ})$ of \eqref{5.6:eq-weight-a} and the counting forms
$(\pi 1)\text{--}(\pi 3)$ of \eqref{5.6:eq-pieces-b}. Write $Y_1:=Y_1(t)$, and recall that
$\lambda$ is the number of links of the chain and that
\begin{equation*}
N_t(n)=\#\{Y:\ \mathcal{P}(t;Y)\neq\emptyset,\ n(t;Y)=n\}.
\end{equation*}
The argument has three steps: a count of the final domains, a summation over them, and the
treatment of the prefactor.

\emph{Count.} Fix $n\ge 1$ and a finite set of cells $Y$ with $\mathcal{P}(t;Y)\neq\emptyset$ and
$n(t;Y)=n$. By $(\pi 3)$, $Y\supseteq Y_1$ and every $\sim$-component of $Y$ meets $Y_1$; that
is, every cell of $Y$ is joined to a cell of $Y_1$ by a $\sim$-path of cells of $Y$. Put
$A:=Y\setminus Y_1$, so that $\#A=n$, and let $C_1,\dots,C_q$ be the $\sim$-components of $A$,
that is, the components of the $\sim$-graph of $A$ itself.

Each $C_i$ is $\sim$-adjacent to $Y_1$. Indeed, take $\Delta\in C_i$ and a $\sim$-path of cells
of $Y$ from $\Delta$ to a cell of $Y_1$. The path starts in $C_i$ and ends in $Y_1$, which is
disjoint from $A\supseteq C_i$, so it has a first cell outside $C_i$. That cell is
$\sim$-adjacent to its predecessor on the path, which lies in $C_i$. It cannot lie in
$A\setminus C_i$, for then it would be joined to $C_i$ in the $\sim$-graph of $A$ and would
belong to $C_i$. Hence it lies in $Y_1$.

Fix once and for all a total order on the cells. Root $C_i$ at its least cell among those
$\sim$-adjacent to $Y_1$. Since $C_i\cap Y_1=\emptyset$, these are exactly the cells of
$C_i\cap\partial^{+}Y_1$, a set which is non-empty by the preceding paragraph. The components are
pairwise disjoint, so distinct components have distinct roots. Let $S\subset\partial^{+}Y_1$ be
the set of roots, so that $\#S=q$. For $s\in S$ let $m_s$ be the number of cells of the component
rooted at $s$. Assign to $Y$ the code
\begin{equation*}
\Bigl(S,\ (m_s)_{s\in S},\ \text{the components, as connected cell sets containing their roots}
\Bigr).
\end{equation*}
The map $Y\mapsto$ code is injective, because $Y=Y_1\cup\bigcup_i C_i$ and $Y_1$ depends on $t$
only.

We count the codes in three stages.
\begin{itemize}
\item The set $S$ is a non-empty subset of $\partial^{+}Y_1$. Each cell has $D_d$ neighbours,
so $\#\partial^{+}Y_1\le D_d\,\#Y_1$. This leaves at most
$2^{\#\partial^{+}Y_1}\le 2^{D_d\#Y_1}$ choices for $S$.
\item Given $S$ with $\#S=q\in[1,n]$, the sizes $(m_s)_{s\in S}$ satisfy $m_s\ge1$ and
$\sum_s m_s=n$. There are $\binom{n-1}{q-1}\le 2^{n-1}$ such choices.
\item Given $S$ and the sizes, the component rooted at $s$ is a $\sim$-connected set of $m_s$
cells containing $s$. Every cell has $D_d\ge1$ neighbours. The rooted-sets lemma
(Lemma~\ref{5.6:lem-rooted-sets}) therefore applies with $D=D_d$. It bounds the number of
choices for the components by
\begin{equation*}
\prod_{s\in S}a(m_s)\le\prod_{s\in S}(4D_d)^{m_s-1}\le(4D_d)^{n}.
\end{equation*}
\end{itemize}
Multiplying the three counts,
\begin{equation}\label{5.6:eq-all-final-domains-1}
N_t(n)\le 2^{D_d\#Y_1}\,2^{n-1}\,(4D_d)^n\le 2^{D_d\#Y_1}(8D_d)^n\qquad(n\ge1).
\end{equation}
Moreover $N_t(0)\le1$, since $n(t;Y)=0$ forces $A=\emptyset$, that is, $Y=Y_1$.

\emph{Sum.} By (b) of the weight lemma, \eqref{5.6:eq-weight-c}, for each $Y$ with
$n(t;Y)=n$,
\begin{equation*}
\sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathcal{D}_b}|p|\le\mathfrak{b}\,(\lambda\,r(\kappa_1))^{n}.
\end{equation*}
Here $\sup_{\mathcal{D}_b}|p|$ is the supremum of $|p|$ over data of size at most $b$, as in (b).
All terms are non-negative, so the sum over all final domains may be regrouped by the value of
$n(t;Y)$. Using $N_t(0)\le1$, \eqref{5.6:eq-all-final-domains-1} and
$1\le 2^{D_d\#Y_1}$, we obtain
\begin{equation}\label{5.6:eq-all-final-domains-2}
\begin{split}
\sum_{Y}\sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathcal{D}_b}|p|
&=\sum_{n\ge0}\ \sum_{Y:\,n(t;Y)=n}\ \sum_{p\in\mathcal{P}(t;Y)}\sup_{\mathcal{D}_b}|p|\\
&\le\mathfrak{b}\Bigl[1+\sum_{n\ge1}2^{D_d\#Y_1}(8D_d)^n(\lambda\,r(\kappa_1))^n\Bigr]\\
&\le 2^{D_d\#Y_1}\,\mathfrak{b}\sum_{n\ge0}\bigl(8\lambda D_d\,r(\kappa_1)\bigr)^n.
\end{split}
\end{equation}
By $(\mathrm{H}_{\circ})$ we have $\kappa_1\ge1$. Lemma~\ref{5.6:lem-cauchy-factor} then gives
$r(\kappa_1)\le e^{-(\kappa_1-1)}$. Consequently $8\lambda D_d\,r(\kappa_1)\le\tfrac12$ as soon
as $8\lambda D_d\,e^{-(\kappa_1-1)}\le\tfrac12$, and
\begin{equation*}
8\lambda D_d\,e^{-(\kappa_1-1)}\le\tfrac12
\quad\Longleftrightarrow\quad
\kappa_1\ge1+\log(16\lambda D_d).
\end{equation*}
Under this condition the geometric series in \eqref{5.6:eq-all-final-domains-2} is at most $2$.
The right side of \eqref{5.6:eq-all-final-domains-2} is then at most
$2\cdot2^{D_d\#Y_1}\,\mathfrak{b}$.

\emph{Prefactor.} Let $\ell\in\{d_k^{\mathrm{fr}},d_k^{\subset}\}$, and suppose
$d_k^{\mathrm{fr}}(Y_1)<\infty$, which is the hypothesis of the lemma on cells met by a tree
graph (Lemma~\ref{5.6:lem-tree-cells}). That lemma gives
$\#Y_1\le 3^d(2\ell(Y_1)+1)$ for both choices of $\ell$. Multiplying by $D_d\log 2$ and recalling
$c''_d=3^dD_d\log2$,
\begin{equation*}
D_d\,\#Y_1\log2\le D_d\,3^d\bigl(2\ell(Y_1)+1\bigr)\log2=c''_d\bigl(2\ell(Y_1)+1\bigr).
\end{equation*}
Hence $2^{D_d\#Y_1}\le e^{c''_d}\,e^{2c''_d\ell(Y_1)}$. This yields the absorption arithmetic
displayed in (d), \eqref{5.6:eq-weight-f}, with $a=(1+3\beta)\kappa$:
\begin{equation*}
e^{2c''_d\ell(Y_1)}\,e^{-a\ell(Y_1)}=e^{-(a-2c''_d)\ell(Y_1)}.
\end{equation*}
When $\ell(Y_1)>0$, the right side satisfies
\begin{equation*}
e^{-(a-2c''_d)\ell(Y_1)}\le e^{-(1-\varepsilon)a\ell(Y_1)}
\quad\Longleftrightarrow\quad
\varepsilon a\ge 2c''_d.
\end{equation*}
When $\ell(Y_1)=0$, both sides equal $1$. The condition $\varepsilon a\ge2c''_d$ is the one-sided
floor $(\mathrm{F}\text{-}\kappa)^{(d)}$ of \eqref{5.6:eq-weight-g}.
\end{proof}
```

**W6-F2 (filled: combinatorial factors).** Every component of \(Y\setminus Y_1\) touches \(Y_1\): follow a path in \(Y\); an exit to another added cell would join the components. Its least touching cell roots it in \(\partial^+Y_1\). There are at most \(2^{D_d\#Y_1}\) root sets and \(2^{n-1}\) positive compositions of \(n\). A rooted connected set of \(m\) cells has a depth-first tree-walk encoding with \(2(m-1)\) up/down symbols and \(m-1\) neighbour ranks, giving \((4D_d)^{m-1}\) possibilities. This accounts for \(8D_d\) without numerical enumeration. The empty added domain contributes separately. Traversing a witnessing tree twice and posting every \(M\) steps gives at most \(2\ell+1\) posts and \(3^d\) cells per post; \(M\) cancels because lengths are in units of \(M\). The printed \(c''_d=3^dD_d\log2\) and its decay expenditure follow. This never supplies a missing decaying prefactor.

### (e) and (f): telescoping and constants

CA-II:46020–46129. Complete original passage by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; annotations following it are part of this port.

```latex
\begin{proof}[Proof of clauses (e) and (f) of Lemma~\ref{5.6:lem-weight}]
\label{5.6:prf-telescoping-identity}
\emph{Proof of (e): the bound.} Let $\mathsf{y}\subset\mathcal{N}$ with $\mathsf{y}\neq\emptyset$.
By \eqref{5.6:eq-pieces-c}, $F_{\mathsf{y}}$ is a piece of the model form with variable set
$W=\mathsf{y}$ and base point $0$ on $\mathcal{N}\setminus\mathsf{y}$. Clause (a) of the weight lemma,
\eqref{5.6:eq-weight-b}, therefore applies to it with the bound $\mathfrak{b}$ of $(\mathrm{H}_{\circ})$,
which dominates $\sup|F|$ and equals $\mathfrak{N}(F)$ with the first choice of $\mathfrak{N}(F)$.

With the second choice of $\mathfrak{N}(F)$ we apply (a) to $F-F(\mathbb{1})$ instead. For fixed
$\mathfrak{d}$, the function $\sigma\mapsto F(\sigma;\mathfrak{d})-F(\mathbb{1};\mathfrak{d})$ is
holomorphic on $P_{\mathcal{N}}(e^{\kappa_1})$ and bounded there by $\mathfrak{N}(F)$. Since
$\mathsf{y}\neq\emptyset$, the operator $\partial^{\mathsf{y}}$ annihilates the constant
$F(\mathbb{1};\mathfrak{d})$. Hence $F-F(\mathbb{1})$ has the same piece $F_{\mathsf{y}}$.

In both cases, (a) gives the first inequality below. Lemma~\ref{5.6:lem-cauchy-factor} gives
$r(\kappa_1)\le e^{-(\kappa_1-1)}$ for $\kappa_1\ge 1$, and raising this to the power $|\mathsf{y}|$
gives the second:
\begin{equation*}
\sup_{\mathfrak{d}\in\mathcal{D}_b}|F_{\mathsf{y}}(\mathfrak{d})|
\le\mathfrak{N}(F)\,r(\kappa_1)^{|\mathsf{y}|}
\le\mathfrak{N}(F)\,e^{-(\kappa_1-1)|\mathsf{y}|}.
\end{equation*}
This is the bound in \eqref{5.6:eq-weight-h}.

\emph{Proof of (e): the telescoping identity.} Fix $\mathfrak{d}\in\mathcal{D}_b$ and write
$F(\sigma)$ for $F(\sigma;\mathfrak{d})$. By $(\mathrm{H}_{\circ})$, $F$ is continuous, separately
holomorphic and bounded on $P_{\mathcal{N}}(e^{\kappa_1})$, and $e^{\kappa_1}>1$ because
$\kappa_1\ge 1$. The Cauchy estimates (Lemma~\ref{5.6:lem-cauchy-estimates}) therefore show that $F$
is $C^\infty$ on $P_{\mathcal{N}}(e^{\kappa_1})$. Hence its restriction to the real points, an open
neighbourhood of $[0,1]^{\mathcal{N}}$ in $\mathbb{R}^{\mathcal{N}}$, is $C^\infty$ in the real
variables.

Let $\mathcal{C}=C^\infty([0,1]^{\mathcal{N}})$ be the space of functions $H$ on
$[0,1]^{\mathcal{N}}$ with continuous partial derivatives of all orders on the closed cube. By the
preceding paragraph, the restriction of $F$ to $[0,1]^{\mathcal{N}}$ lies in $\mathcal{C}$.
For $\Delta\in\mathcal{N}$,
$c\in\{0,1\}$ and $H\in\mathcal{C}$ set
\begin{gather*}
(E_\Delta^{c}H)(\sigma):=H(\sigma\text{ with }\sigma(\Delta):=c),\\
(I_\Delta H)(\sigma):=\int_0^1(\partial_{\sigma(\Delta)}H)(\sigma\text{ with }\sigma(\Delta):=u)\,du .
\end{gather*}
Both operators map $\mathcal{C}$ into itself; for $I_\Delta$ this is differentiation under the integral
sign, the integrand having continuous derivatives on the compact cube. The fundamental theorem of
calculus in the variable $\sigma(\Delta)$ gives
\begin{equation}\label{5.6:eq-telescoping-identity-1}
E_\Delta^{1}H=E_\Delta^{0}H+I_\Delta H\qquad(H\in\mathcal{C}).
\end{equation}

Operators attached to distinct cells $\Delta\neq\Delta'$ commute on $\mathcal{C}$.
\begin{itemize}
\item Two evaluations fix two different coordinates, so they commute.
\item $E_\Delta^{c}$ and $I_{\Delta'}$ commute, because fixing $\sigma(\Delta)$ commutes with
differentiating in $\sigma(\Delta')$ and integrating over $\sigma(\Delta')$.
\item For $I_\Delta$ and $I_{\Delta'}$, differentiation under the integral sign gives
$I_\Delta I_{\Delta'}H$ as the integral over $[0,1]^2$ of
$\partial_{\sigma(\Delta)}\partial_{\sigma(\Delta')}H$, evaluated at
$(\sigma(\Delta),\sigma(\Delta'))=(u,u')$. The same computation gives $I_{\Delta'}I_\Delta H$ as the
integral of $\partial_{\sigma(\Delta')}\partial_{\sigma(\Delta)}H$ taken in the other order. These
agree by Clairaut's theorem, since $H$ is $C^2$, and by Fubini's theorem on $[0,1]^2$.
\end{itemize}

Let $\prod$ denote composition of operators in any order; by the commutation just shown, the order is
immaterial. Apply \eqref{5.6:eq-telescoping-identity-1} once for each cell. Distributing the
composition of the $|\mathcal{N}|$ sums, and reordering each resulting term by commutativity, we
obtain, at every $\sigma$,
\begin{align*}
F(\mathbb{1})
&=\Bigl(\prod_{\Delta\in\mathcal{N}}E_\Delta^{1}\Bigr)F
=\Bigl(\prod_{\Delta\in\mathcal{N}}\bigl(E_\Delta^{0}+I_\Delta\bigr)\Bigr)F\\
&=\sum_{\mathsf{y}\subset\mathcal{N}}
\Bigl(\prod_{\Delta\in\mathsf{y}}I_\Delta\prod_{\Delta\notin\mathsf{y}}E_\Delta^{0}\Bigr)F .
\end{align*}

To evaluate the $\mathsf{y}$-summand, first apply the $E_\Delta^{0}$ with $\Delta\notin\mathsf{y}$;
they set the coordinates off $\mathsf{y}$ equal to $0$. Then apply the $I_\Delta$ with
$\Delta\in\mathsf{y}$ one after another, and use Fubini's theorem on $[0,1]^{\mathsf{y}}$. Writing
$u_{\mathsf{y}}\in[0,1]^{\mathsf{y}}$ for the integration variable, the summand equals
\begin{equation*}
\int_{[0,1]^{\mathsf{y}}}\partial^{\mathsf{y}}F(u_{\mathsf{y}},0_{\mathcal{N}\setminus\mathsf{y}})\,
du_{\mathsf{y}}
=F_{\mathsf{y}}
\end{equation*}
by \eqref{5.6:eq-pieces-c}. For $\mathsf{y}=\emptyset$ it is $F(0)=F_\emptyset$. Subtracting $F(0)$
from both sides gives
\begin{equation*}
F(\mathbb{1};\mathfrak{d})-F(0;\mathfrak{d})
=\sum_{\mathsf{y}\subset\mathcal{N},\ \mathsf{y}\neq\emptyset}F_{\mathsf{y}}(\mathfrak{d}),
\end{equation*}
which is the telescoping identity of \eqref{5.6:eq-weight-h}.

\emph{Proof of (f).} Clause (f), \eqref{5.6:eq-weight-i}, asserts that the constants and conditions in
(a)--(e) depend on no parameter beyond those listed below. Consider the constants and conditions in
clauses (a)--(e), and in the lemmas on which these clauses rest:
Lemma~\ref{5.6:lem-cauchy-factor}, Lemma~\ref{5.6:lem-cauchy-estimates},
Lemma~\ref{5.6:lem-tree-length-adjunction}, Lemma~\ref{5.6:lem-rooted-sets} and
Lemma~\ref{5.6:lem-tree-cells}. They involve the following parameters and no others:
\begin{itemize}
\item $\kappa_1$, through the factor $r(\kappa_1)$ and through the one-sided floors imposed on
$\kappa_1$;
\item the number $\lambda$ of links of the chain;
\item the dimension $d$ and the adjacency $\sim$, through the constants $c'$, $D_d$ and $3^d$;
\item in clause (c), and in the optional absorption of clause (d) only, the decay rate
$a=(1+3\beta)\kappa$ of the statement to which the weight lemma is applied (hence $\kappa$ and
$\beta$), together with $\varepsilon$.
\end{itemize}
None of these is $K$, $k$, $N$, $L$, the volume, a position, the number of terms or the coupling.
The cube side $M$ enters only through the definitions of the tree lengths $d_k^{\mathrm{fr}}$ and
$d_k^{\subset}$, which are measured in units of $M$; there it cancels, so that no constant or
condition depends on $M$. This is the assertion of (f).
\end{proof}
```

**W6-F3 (filled: finite product identity).** Evaluation and integration satisfy \(E_i^1=E_i^0+I_i\), with \(I_iF=\int_0^1\partial_iF\,ds_i\). Operators in different coordinates commute on the compact cube. Expand \(\prod_i(E_i^0+I_i)F\) and subtract the empty subset \(F(0)\). For an empty variable set both sides are zero. Subtracting \(F(\mathbf1;\mathfrak d)\) changes no nonempty piece.

## B2b: window-weight proof and inputs

| Name | Label/locus | Standing retained |
|---|---|---|
| W5-setting | 5.5:not-weight-notation, II:34020–34137; 5.5:def-windowed-source, II:34158–34337 | Definitions with source class, scaffold, frozen pieces, stored supports, levels, weights and minimiser domains assumed. |
| W5-filing | 5.5:def-near-unit-classes, II:34389–34547 | Three classes and three discs, with their own suppliers. Box reading of rows 1–3 requires \(\nu\ge3\) and \(S_v^\star>1\). Third-class pieces have a separate entire read. |
| W5-data | 5.5:def-data-factor, II:34549–34662; 5.5:def-weight-constants, II:34664–35005 | Exact data functionals, floors, ceilings, row bounds and geometry retained. The factor 24 of the own-read disc stays inside \(\kappa_R,C_R\). |
| W5-membership | 5.5:def-weight-inputs (i), II:35030–35071 | Own-level tube containment, holomorphy, jet identity, size, filing and paired read assumed. |
| W5-box-rem | Same definition (ii), II:35073–35122 | Tube admission of both pairs and interpolation segment, holomorphy, size, block sum and paired difference assumed. |
| W5-pair | Same definition (iii), II:35124–35205 | Joint holomorphy/containment and closure under M1–M6 and M8; M7 supplies rim reads. Paired-chart majorants retained. |
| W5-third-rem | Same definition (iv), II:35207–35218 | Entire third-class remainders, their \(\mathsf s_v\mathsf v_v\) sizes and per-cell sums assumed. |
| W5-third-pair | Same definition (v), II:35220–35235 | Off-chart difference bound with \(C^\perp=720L^2\), \(\mathsf S_v^\perp\), and its ceiling assumed. Does not supply W5-low. |
| W5-rows | II:34871–34881, 35237–35255 | Unit-weight per-cell sums, single-term analyticity, no-inherited-cell tile bound and supplier rows of \(\mathsf l^J\) assumed. Its definition is used; its bound is not proved here. |
| W5-local | Invocations II:35559–35597, 35628–35744 | Window perturbation and parameter corollary, local constrained minimiser, complex averaging extension, source-fluctuation bound and bump regularity: named suppliers at these loci. |
| W5-cover | II:35065–35069, 35761–35777 | Balaban CMP 119 p.276: transfer of CMP 109 §3 analysis to the cover, **printed without proof**. Own-box (c1)–(c3), short-single, core, Wilson, counterterm and column estimates retained. |
| W5-geometry | 5.5:prf-weighted-cells, II:36037–36249; data-factor (f),(h) | Level/zone, separation, nesting, arrest, collar, raised-layer, residual-cell, anchor and comparison-region assertions assumed. |
| W5-depth | II:36260–36390 | Raise/depth bounds and \(k_0(t)=t-N_0(t)\), on the same scaffold, assumed. |
| W5-resum | II:36401–36484, 36740–36797 | Positive linear resummation on filed discs, with exactly W5-data's row constants, assumed. |
| W5-low | II:35500–35506, 36706–36721, 36785–36790 | Excluded low-order variation factor at the second cube size. Not an input of this lemma. Carry separately for its unrestricted total. 5.9:thm-low-order-variation is a distinct supplier, not proved by this port. |
| W5-sixth | Complex extension invoked II:34693; 5.11:lem-sixth-family, II:59618–59620 | **Statement and proof not written out**. The required complex-extension use is an open input. |

Use [port-pi](../port-pi.md), 5.2:lem-pointed-irrelevance, for E-family cancellation only on its admitted domain. Use [mu](../mu.md), their 4.13, with the owner's **proved and refereed** standing, for its regular real/continued complex minimiser identity. Its note leaves the extra data radii of the CA-II:35714 use unchecked; that extension remains W5-local admission. [oc](../oc.md) has the same **proved and refereed** standing for its own-constant one-step scope. [lrb](../lrb.md), **proved and refereed**, and [ui](../ui.md), **checked**, support their respective 4.4 and 4.5 operator inputs. These results do not supply every window hypothesis.

The table's source-locus names are deliberate when the invocation itself has no label. They retain a specific hypothesis rather than inventing a theorem number.

### (a1)–(a2): regularity and windowed minimiser

CA-II:35543–35626. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of \textup{(a1)} and \textup{(a2)}]
\emph{(a1).} This clause is one of the defining conditions of the source class; no estimate
is involved. Since $\hat{X}\supseteq\hat{\mathsf{K}}_{\square}\supseteq\square_0$, the
triple $(k,\square_0,\mathfrak{B}^+)$ is one of the triples of the source over $\hat{X}$ at
which the conditions defining the admissible source class $\mathfrak{K}_P$ are imposed: the
definition of that class imposes its second and fourth entries for every triple
$(p,X',\mathfrak{s})$ among the current one and all its predecessors, and on the pieces
frozen by a live arrest $\mathfrak{a}$ it imposes them in the form attached to
$\mathfrak{a}$. By the definition of $\mathbb{W}=U(\mathfrak{B}^+(\square_0),M^{\cdot}(\mathbb{U}))$
in Definition~\ref{5.5:def-windowed-source}, the second entry of this triple at a cell $x$
is $|\partial\mathbb{W}(x)-1|$. In the reading with weights and arrest factor in which the
source class is taken (Definition~\ref{5.5:def-windowed-source}), the condition on this entry
states that the second entry at $x$ is less than
$F^{(k')}(x)\,w(x)\,r_2(\ell(x))$, taken at the levels and weights
$(\ell^+,w^+)$ of $\mathfrak{B}^+$; here $F^{(k')}$ is the arrest factor, $k'$ being the step
index it carries in that condition (the letter $F^{(k')}$ is used only in this paragraph). The
arrest factor satisfies $F^{(k')}(x)\le1+2\beta$, by
the bound on the arrest factor, where $\beta=\frac15$ is the parameter of that bound (not the
H\"older exponent of (a3)); thus $F^{(k')}(x)\le1.4$. At the data of $\mathfrak{B}^+$ one has
$w^+(x)r_2(\ell^+(x))\le\theta_2(x)$, by the comparison of the refined levels and weights with
the current ones. Hence
\begin{equation*}
|\partial\mathbb{W}(x)-1|<F^{(k')}(x)\,w^+(x)\,r_2(\ell^+(x))\le1.4\,\theta_2(x).
\end{equation*}
The condition is imposed on the set $X'^{\flat}$ attached to the triple, and
$X'^{\flat}\supset\tilde{\square}^3$; this gives (a1) for every cell $x$ meeting
$\tilde{\square}^3$. The window is read in the same way in \cite[(3.40)]{B-CMP109},
where the condition numbered (iv) of \cite[p.~278]{B-CMP109} is stated there to be a
consequence of its condition (iii).

\emph{(a2).} By Definition~\ref{5.5:def-windowed-source}, $\mathfrak{B}^*_j$ refines
$\mathfrak{B}^+(\square_0)$. The configuration $\mathbb{W}$ is minimal under the data of
$\mathfrak{B}^+(\square_0)$, and these data are averages of the data of $\mathfrak{B}^*_j$;
so $\mathbb{W}$ is critical under its own $\mathfrak{B}^*_j$-data, and
\begin{equation*}
W':=U(\mathfrak{B}^*_j,M^{\cdot}(\mathbb{W}))=\mathbb{W}^g
\end{equation*}
for a gauge transformation $g$, by \cite[(3.39)]{B-CMP109}; for complex $\mathbb{U}$ the
identity persists by the analytic continuation furnished in the setting of the perturbation
lemma for the windowed minimiser. The reason is that, by \cite[Theorem~1]{B-CMP102b}, the
minimal
orbit is an orbit of the group of gauge transformations which fix the constraints; these
transformations are the identity at the base points of the blocks, so $g=1$ there, and the
gauge factor is local to each block. For $x$ in the block with base point $y_0$, let
$\Gamma$ be the contour from $y_0$ to $x$; then
$g(x)=W'(\Gamma)^{-1}\mathbb{W}(\Gamma)$. Write $n(\cdot)$ for the size function on complex
group elements used in the defining condition of the admissible source class $\mathfrak{K}_P$
that controls the configuration along contours, $a_{\flat}$ for the radius in that condition,
$\mathcal{H}(B_0)$ for the field variable on the base cube $B_0$ of the block that enters the
contour bound of the perturbation lemma, and $\ell$
for the length scale entering the bound on it (not the level $\ell(x)$ of a cell). That
defining condition gives
$n(\mathbb{W}(\Gamma))\le e^{2da_{\flat}}$, and the bound on $W'$ along contours in the
setting of the perturbation lemma gives
$n(W'(\Gamma))\le2^{1/2}e^{2d\ell\sup|\mathcal{H}(B_0)|}$. These two bounds give
$n(g)\le2$ under the smallness condition of the perturbation lemma among the ceilings of
Definition~\ref{5.5:def-weight-constants}, since $a_{\flat}\le5\mathsf{A}_w(\gamma)$.
Combining $n(g)\le2$ with (a1), the second entry
$E_2^{\mathfrak{B}^*_j}(\mathbb{W})(x)$ of $\mathbb{W}$ relative to the data of
$\mathfrak{B}^*_j$ satisfies
\begin{equation*}
E_2^{\mathfrak{B}^*_j}(\mathbb{W})(x)\le2\cdot1.4\,\theta_2(x)=2.8\,\theta_2(x).
\end{equation*}

The perturbation lemma for the windowed minimiser holds in every frame. Apply it in the frame
$(\square_0,\mathfrak{B},\mathfrak{B}^*_j)$, with $\mathbb{W}$ as its configuration and
$\mathbf{A}$ in the slot of its fluctuation. Its hypotheses hold. Its defining condition on
the source holds because $(\mathbb{W},\mathbb{J})\in\mathfrak{K}_P$. Its two regularity
conditions and its smallness condition hold by the second clause of the corollary on the
parameters of the perturbation lemma, applied at the parameter value one half. That clause
bounds the first parameter of the perturbation lemma by one quarter of a radius which is
itself at most one, hence by one quarter, and it bounds the second parameter by the first.
With the first parameter at most $\frac14$, the perturbation lemma multiplies the entry bound
$2.8\,\theta_2(x)$ by at most $\frac54$ and adds at most $\frac14r_2(\ell(x))$; it thus gives
\begin{equation*}
|\partial\mathfrak{b}'_j(x)-1|\le2.8\,\theta_2(x)\cdot\tfrac54+\tfrac14r_2(\ell(x))
\le3.75\,\theta_2(x)\le4\,\theta_2(x),
\end{equation*}
where $2.8\cdot\frac54=3.5$ and $\frac14r_2(\ell(x))\le\frac14\theta_2(x)$, the weight
$w(x)$ being at least one by Notation~\ref{5.5:not-weight-notation}. The bound holds
pointwise in
$(t,\mathsf{t})\in[0,1]\times\mathbb{D}_{\square}$, which proves \eqref{5.5:eq-weight-a};
it is the entry bound used for the pieces of the third class in~(b).
\end{proof}
```

### (a3)–(a4): box and comb fields

CA-II:35628–35744. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of parts (a3) and (a4) of Lemma~\ref{5.5:lem-weight}: small-field regularity on a local box]\label{5.5:prf-box-regularity}
We work in the setting of the weight lemma (Lemma~\ref{5.5:lem-weight}). Its parts (a1) and (a2), the latter displayed in \eqref{5.5:eq-weight-a}, are used as inputs. The constants $K_{ax}$, $C_M^{av}\ge 2$, $K_h$, $c_1$, $c_{\cdot}$ and $K_{loc}$ are those of Definition~\ref{5.5:def-weight-constants}. In particular
\begin{equation*}
K_{loc} = 4\bigl(c_{\cdot}+3K_hK_{ax}MC_M^{av}\bigr),
\end{equation*}
see \eqref{5.5:eq-weight-constants-c}, and $K_h,\ K_{ax}M,\ c_1\ge 1$. The ceiling on $\gamma$ is \eqref{5.5:eq-weight-constants-d}, namely $K_{loc}\,\mathsf{A}_w(\gamma)\le c_h$, where $c_h$ is half the least of the absolute smallness constants of four published statements, each taken for the quantity it bounds: \cite[Proposition~2]{B-CMP98}, \cite[Theorem~1]{B-CMP102b}, \cite[Proposition~9]{B-CMP102b}, and the Baker--Campbell--Hausdorff step \cite[(3.30)--(3.32)]{B-CMP109}.

Let $Q$ be a box as in (a3). Thus $Q$ has at most $9$ cubes of $\pi_p$ a side, $Q^{(1)}\subset\tilde{\square}^3$, and every cell meeting $Q^{(1)}$ is of level at least $p$. Further, $w_Q$ and $\alpha_Q$ are the largest values of $w(\Delta)$ and of $\alpha_{0,\ell(\Delta)}$ over those cells. Sizes said to be taken \emph{in level-$p$ units} carry the powers of $\ell_p$ of \eqref{5.5:eq-weight-b}.

\emph{Part} (a3). \emph{The minimiser of $Q$.} Let $\mathfrak{B}_p(Q)$ be the maximal sequence of block partitions on $Q$ in the sense of \cite{B-CMP109}. Put
\begin{equation*}
\mathsf{V}_Q := M^{\cdot}(\mathbb{W})|_{\mathfrak{B}_p(Q)},
\end{equation*}
the family of averages of $\mathbb{W}$ over the blocks of $\mathfrak{B}_p(Q)$. We apply the locality part of the lemma on the constrained minimiser in a local box to $(\mathbb{W},Q,p)$, with $Q$ as its box and $\mathfrak{B}_p(Q)$ as its sequence. It yields two facts.

First: for any configuration $U$, every level-$p$ average $M^p(U,c)$ of $U$ is a function of the values of $U$ off the box and of the averages $M^{\cdot}(U)|_{\mathfrak{B}_p(Q)}$. Consequently the same holds for those data of the sequence $\mathfrak{B}^+(\square_0)$ whose blocks meet $Q$; all of these are of level at least $p$.

Second: let a variation of $\mathbb{W}$ be supported inside $Q$ and keep $\mathsf{V}_Q$ fixed. By the first fact it keeps those data of $\mathfrak{B}^+(\square_0)$ fixed, and it vanishes on the outer layer of $Q$. Now $\mathbb{W}$ is minimal under the data of $\mathfrak{B}^+(\square_0)$. Hence $\mathbb{W}|_Q$ is critical under the constraint $\mathsf{V}_Q$ in the smaller class of configurations on $Q$.

The critical point is unique by \cite[Theorem~1]{B-CMP102b}. The smallness that theorem requires is here
\begin{equation*}
1.4\,w(\Delta)\,\tilde{\alpha}_{0,\ell(\Delta)}\le 2.8\,\mathsf{A}_w(\gamma),
\end{equation*}
where $\tilde{\alpha}_{0,\ell(\Delta)}$ is the enlarged radius at level $\ell(\Delta)$, which satisfies $\tilde{\alpha}_{0,\ell(\Delta)}\le 2\alpha_{0,\ell(\Delta)}$, and $2.8\,\mathsf{A}_w(\gamma)$ is paid by the ceiling, as shown at the end of this part. Therefore
\begin{equation}\label{5.5:eq-box-regularity-1}
\mathbb{W}|_Q = U_p(Q,\mathsf{V}_Q)\quad\text{modulo gauge.}
\end{equation}
At complex data, \eqref{5.5:eq-box-regularity-1} follows from the real case by the identity theorem for holomorphic functions. The argument is the one used in the lemma on the constrained minimiser in a local box.

\emph{The data.} We apply \cite[Proposition~2]{B-CMP98} at complex data, in its extension to complex data given by the complex form of the averaging bound of this chapter, and feed it the bound (a1). For levels $\ell\ge p$, using $\tilde{\alpha}\le 2\alpha$, this gives in level-$p$ units
\begin{equation}\label{5.5:eq-box-regularity-2}
|\partial\mathsf{V}_Q-1|
\le 1.4\,C_M^{av}\,w_Q\,\tilde{\alpha}_{0,\ell}\,(\ell_p/\ell_\ell)^2
\le 2.8\,C_M^{av}\,w_Q\,\alpha_Q .
\end{equation}

\emph{The axial gauge on $Q$.} In the axial gauge of \cite[(3.26)]{B-CMP109} on a box of at most $9$ cubes a side, each bond variable is a product of at most $K_{ax}M$ conjugated plaquette variables of the box, with distortion at most $2$. Write $\mathsf{V}_Q^{v}$ for the data $\mathsf{V}_Q$ in this gauge. By \eqref{5.5:eq-box-regularity-2}, $\mathsf{V}_Q^{v}=e^{iB}$ with
\begin{equation}\label{5.5:eq-box-regularity-3}
|B|\le 5.6\,K_{ax}MC_M^{av}\,w_Q\,\alpha_Q\le K_{loc}\,\mathsf{A}_w(\gamma).
\end{equation}

\emph{Representation.} We apply \cite[Proposition~9]{B-CMP102b} at the identity configuration $\mathbb{1}$. The representation parts of the lemma on the constrained minimiser in a local box read the data through $B$ alone. They give
\begin{equation*}
U_p(Q,e^{iB}) = \bigl(e^{i\eta\mathcal{H}(B)}\bigr)^{u}
\end{equation*}
for a field $\mathcal{H}(B)$ on $Q$, determined by $B$, and a gauge transformation $u$. On $Q^{\sim-1}$, moreover,
\begin{equation*}
\max\bigl\{\ell_p|\mathcal{H}|,\ \ell_p^2|\nabla\mathcal{H}|,\
\ell_p^{2+\beta}\|\nabla\mathcal{H}\|_\beta\bigr\}\le K_h\sup|B| .
\end{equation*}
Combine this with \eqref{5.5:eq-box-regularity-1} and \eqref{5.5:eq-box-regularity-3}. There is a gauge $g$ on $Q^{\sim-1}$ in which $\mathbb{W}=e^{i\eta H}$, with
\begin{equation}\label{5.5:eq-box-regularity-4}
\max\bigl\{\ell_p|H|,\ \ell_p^2|\nabla H|,\ \ell_p^{2+\beta}\|\nabla H\|_\beta\bigr\}
\le 5.6\,K_hK_{ax}MC_M^{av}\,w_Q\,\alpha_Q .
\end{equation}
This is \cite[(3.27)]{B-CMP109}, with $Q$ in place of $\square_0$ and $w_Q\alpha_Q$ in place of the single $\alpha_0$.

\emph{The layer.} In the gauge $g$ we have $\mathfrak{b}^g=e^{i\eta\operatorname{Ad}_g\mathbf{A}}\,e^{i\eta H}$. By the bound on the source fluctuation of this chapter, on $\mathbb{D}_\square$
\begin{equation*}
N^{\Delta}_x(\mathbf{A})\le\alpha_{\cdot,\ell(x)},
\end{equation*}
where $N^{\Delta}_x$ is the local norm at $x$ on the cell $\Delta$; its H\"older member is included, and no gap between levels enters. This bound does not involve the weight. In level-$p$ units it is at most $c_{\cdot}\alpha_Q$, by the definition $c_{\cdot}=\sup_n\alpha_{\cdot,n}/\alpha_{0,n}$. The conjugation $\operatorname{Ad}_g$ costs a factor $2$. Put
\begin{equation*}
A:=\frac{1}{i\eta}\log\bigl(e^{i\eta\operatorname{Ad}_g\mathbf{A}}\,e^{i\eta H}\bigr).
\end{equation*}
The Baker--Campbell--Hausdorff bounds \cite[(3.30)--(3.32)]{B-CMP109} are local. With \eqref{5.5:eq-box-regularity-4} they give
\begin{equation*}
\begin{aligned}
\max\bigl\{\ell_p|A|,\ \ell_p^2|\nabla A|,\ \ell_p^{2+\beta}\|\nabla A\|_\beta\bigr\}
&\le 2\bigl(2c_{\cdot}\alpha_Q+5.6\,K_hK_{ax}MC_M^{av}\,w_Q\,\alpha_Q\bigr)\\
&\le K_{loc}\,w_Q\,\alpha_Q=\mathsf{a}_Q .
\end{aligned}
\end{equation*}
The last inequality uses $11.2\le 12$ against the definition of $K_{loc}$. This is \eqref{5.5:eq-weight-b}.

\emph{The smallness spends.} The ceiling \eqref{5.5:eq-weight-constants-d} is one-sided, and it pays all four smallness requirements used above.
\begin{itemize}
\item The quantity $2.8\,\mathsf{A}_w(\gamma)$ is used for \cite[Theorem~1]{B-CMP102b} and for \cite[Proposition~2]{B-CMP98}. Since $K_{loc}\ge 12C_M^{av}\ge 24$, it is at most $K_{loc}\mathsf{A}_w(\gamma)\le c_h$.
\item The quantity $K_{loc}\mathsf{A}_w(\gamma)$ is used for \cite[Proposition~9]{B-CMP102b}; it is at most $c_h$.
\item The quantity $2K_{loc}\mathsf{A}_w(\gamma)$ is used for the Baker--Campbell--Hausdorff step. It is at most $2c_h$, the least of the four smallness constants.
\end{itemize}

\emph{Part} (a4). \emph{The identity.} Let $j\le p$, and let $\square_0'\subset Q^{\sim-2}$ be a box of $\pi_j$-cubes. The configuration $\mathfrak{b}'_j$ is minimal under the data of $\mathfrak{B}^*_j$. Near $\square_0'$ these data are of level exactly $j$: the levels there are at least $p\ge j$, and the refinement $\mathfrak{B}^*_j$ caps them at $j$. We run the argument of the first paragraph of part (a3) at $(\mathfrak{b}'_j,\square_0',j)$ in place of $(\mathbb{W},Q,p)$. The regularity it needs is supplied by (a2) and by the bound on the fourth regularity entry of the admissible triple in the lemma on the bump construction of this chapter. It gives
\begin{equation*}
\mathfrak{b}'_j|_{\square_0'}=(U_j,J_j)(\square_0',\mathsf{V}')\quad\text{modulo gauge},
\end{equation*}
which is the identity \cite[(3.38)]{B-CMP109}.

\emph{The part of level $j$.} Block averages are covariant under gauge transformations, so
\begin{equation*}
\mathsf{V}'=M^j(\mathfrak{b})=M^j\bigl(e^{i\eta A}\bigr)^{g}.
\end{equation*}
We apply the averaging part of the lemma on the constrained minimiser in a local box, with $H$ replaced by $A$. This is legitimate because \cite[(4.16)--(4.18)]{B-CMP109} read the field only through the bounds \cite[(3.32)]{B-CMP109}, and part (a3) supplies these for $A$ with size $\mathsf{a}_Q$. With $t_p=L^{j-p}$ the result is
\begin{equation*}
|\partial\mathsf{V}'-1|\le c_1\mathsf{a}_Q t_p^2 .
\end{equation*}
It also gives the comb-gauge representation \eqref{5.5:eq-weight-c}, with $|F|\le c_1\mathsf{a}_Q t_p^2$ and, on the bonds of level $j$,
\begin{equation*}
|\mathfrak{e}_\mu(x)|\le c_1(1+|x-y|)^2\,\mathsf{a}_Q\,t_p^{2+\beta}.
\end{equation*}

\emph{The graded rim.} Near $\partial\square_0'$ there are levels $i<j$, and there $\mathsf{V}'=M^i(\mathfrak{b}'_j)$. Only supremum bounds are used at these levels. Part (a2), combined with \cite[Proposition~2]{B-CMP98}, bounds the deviation of a rim plaquette of level $i$ by
\begin{equation*}
4C_M^{av}\,w(x)\,\tilde{\alpha}_{0,\ell(x)}\,(\ell_i/\ell_{\ell(x)})^2
\le 8C_M^{av}\,w_Q\,\alpha_Q\,t_p^2\,L^{2(i-j)}
\le c_1\mathsf{a}_Q t_p^2 .
\end{equation*}
The last inequality holds because $L^{2(i-j)}\le 1$ for $i<j$, $K_{loc}\ge 8C_M^{av}$ and $c_1\ge 1$. Every plaquette deviation, of level $j$ or on the rim, is therefore at most $c_1\mathsf{a}_Qt_p^2$. Hence, on all bonds,
\begin{equation*}
|B^{ax}(b)|\le 2d(1+|b-y|)\,c_1\mathsf{a}_Q t_p^2 .
\end{equation*}
On the graded-rim bonds, $\mathfrak{e}^{rim}$ is $B^{ax}$ minus the linear term $\sum_{\kappa<\mu}(x-y)_\kappa F_{\kappa\mu}(y)$ of \eqref{5.5:eq-weight-c}. The bound on $|F|$ then gives
\begin{equation*}
|\mathfrak{e}^{rim}(b)|\le|B^{ax}(b)|+d\,|b-y|\,|F|\le 4d(1+|b-y|)\,c_1\mathsf{a}_Q t_p^2 .
\end{equation*}
Here we used $d|b-y|\le 2d(1+|b-y|)$. This completes the proof of (a4).
```

**W5-F1 (filled: continuation and level restriction).** Extend the real minimiser identity by the one-variable identity theorem successively in a real coordinate basis, then by continuation in the common connected admitted chart. Both sides must already be holomorphic there; a size bound alone does not supply admission. This is why W5-local retains the larger-radius use. The \(\nu\ge3\) restriction stays: own-read low-order units and the separately entire third class use their prescribed reads. No low-order box chart is inferred.

### (b): complete near-unit table argument

CA-II:35748–36034. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of Lemma~\ref{5.5:lem-weight}, part (b): the rows of the near-unit table]
\label{5.5:prf-near-unit-rows}
Throughout, $v$ is a near unit with anchor $y$ and $X_v\subset\tilde{\square}^2$. As in the setting
of Lemma~\ref{5.5:lem-weight}, $n=\min\{\ell(y),n_0\}$, $\nu=1+n-j$, $t=L^{j-n}$ and
$\Theta=c_W w^{\vee}(y)\ge 1$, and we put $z:=\Theta\rho_{n,j}$ as in the table
\eqref{5.5:eq-weight-d}. The weighted scaffold majorants $|B^{ax}|_*$, $|F|_*$,
$|\mathfrak{e}_\mu|_*$ and $|\mathfrak{e}^{rim}|_*$ are those of \eqref{5.5:eq-windowed-source-b}.
The radius $S^{\star}_v$ and the inequality it is to satisfy are those of
\eqref{5.5:eq-near-unit-classes-a}, and the filed discs are those of
\eqref{5.5:eq-near-unit-classes-b}. The filing into read, box-read, own-read and third-class units
is that of Definition~\ref{5.5:def-near-unit-classes}.

The analysis of the near units on the cover of blocks rests on the transfer of the analysis of
\cite[\S3]{B-CMP109} to that cover, printed without proof in \cite[p.~276]{B-CMP119}; cited as
printed. From the lemmas of that analysis, as they are stated in this book, we use the following
statements:
\begin{itemize}
\item its box conditions (c1), (c2) and (c3) on a box pair;
\item its short-single lemma;
\item its core lemma, which bounds the core term $\mathfrak{i}_y$ at the anchor $y$;
\item its bound for the Wilson pieces, clause (b);
\item its counterterm projection bound.
\end{itemize}
From the column bounds at the localisation site we use:
\begin{itemize}
\item the step-by-step bounds in the proof of the core lemma;
\item the field-free column bound.
\end{itemize}

\smallskip\noindent\emph{(i) Boxes; the weighted majorants.}
Let $v$ be a read unit, so that $\nu\ge 3$, and put $p:=n-1$. Let $Q_v$ be the union of the cubes of
$\pi_{n-1}$ meeting $\mathfrak{r}_v$, together with two further layers of cubes of $\pi_{n-1}$
around it. For a box $Q$ made of cubes of $\pi_{n-1}$ we write $Q^{(1)}$ for $Q$ enlarged by one
layer of such cubes, and $Q^{\sim-2}$ for $Q$ with its two outer layers removed.

Since $n-1-j=\nu-2$, a level-$j$ unit has length $L^{-(\nu-2)}$ in units of $\pi_{n-1}$. Hence,
measured in cubes of $\pi_{n-1}$, the sides of $\mathfrak{r}_v$ are at most
\begin{equation*}
\max\bigl\{(2\nu+3)L^{-(\nu-2)},\;1+5L^{-(\nu-2)}\bigr\}\le \tfrac{13}{8}<2 .
\end{equation*}
Indeed, $(2\nu+3)L^{-(\nu-2)}$ decreases in $\nu$ and equals $9/L\le 9/8$ at $\nu=3$. Likewise
$1+5L^{-(\nu-2)}\le 1+5/L\le 13/8$ for $\nu\ge 3$ and $L\ge 8$.

A segment of length less than $2$ meets at most $3$ unit intervals. So the union of the cubes of
$\pi_{n-1}$ meeting $\mathfrak{r}_v$ has at most $3$ cubes a side. Consequently $Q_v$ has at most
$7$ cubes a side and $Q_v^{(1)}$ at most $9$. Every point of $Q_v^{(1)}$ lies within $6$ cubes of
$\pi_{n-1}$ of $y$, that is within $6/L<1$ level-$n$ unit of $y$.

As $y\in\tilde{\square}^2$ and $n\le n_0$, this gives $Q_v^{(1)}\subset\tilde{\square}^3$. The cells
of $Q_v^{(1)}$ have level at least $n-1$, by the level bound for the cells meeting
$\tilde{\square}^3$. Since every cell meeting $Q_v$ is at level-$n$ distance at most $6/L<1$ from
$y$, the
definition of $w^{\vee}(y)$ gives $w_{Q_v}\le w^{\vee}(y)$. Further,
$\alpha_{Q_v}\le 2\alpha_{0,n}$ by the bound on the scaffold radii near an arrest, and
$\mathfrak{r}_v\subset Q_v^{\sim-2}$ by construction.

On $Q_v$ we read the small-field regularity on a local box, established in the part of the proof
of Lemma~\ref{5.5:lem-weight} under that heading. We apply the comb-gauge display
\eqref{5.5:eq-weight-c} at
$(Q,p,\square_0'):=(Q_v,n-1,\mathfrak{r}_v)$, for each of the two machines $\mathsf{A}$,
$\mathsf{B}$ by the per-machine hypothesis of the pair system $\mathcal{K}$, with the H\"older
exponent of \eqref{5.5:eq-weight-c} taken to be $\hat{\alpha}$, the exponent of condition (c3),
and with $t_p=L^{j-(n-1)}=Lt$. The definition of $c_W$ in
\eqref{5.5:eq-weight-constants-c} gives $\Theta\ge 2c_1K_{loc}L^3\alpha_{0,n}w^{\vee}(y)/\mathfrak{a}_n$.
Using also $\hat{\alpha}\le 1$, this yields
\begin{align*}
c_1K_{loc}\,w^{\vee}(y)\cdot 2\alpha_{0,n}L^2t^2
 &\le \Theta\,\mathfrak{a}_n t^2/L,\\
c_1K_{loc}\,w^{\vee}(y)\cdot 2\alpha_{0,n}L^{2+\hat{\alpha}}t^{2+\hat{\alpha}}
 &\le \Theta\,\mathfrak{a}_n t^{2+\hat{\alpha}} .
\end{align*}

The factor $L^{-1}$ in the first line is the one reserved in the power $L^3$ of $c_W$; it is the
spare factor used by the remainder hypothesis for box-read units of Lemma~\ref{5.5:lem-weight}. It
follows that conditions (c1) and (c3) hold for the box pair $\mathfrak{b}'_j$ on $\mathfrak{r}_v$ with
$(\mathfrak{a}_n,t)$ replaced by $(\Theta\mathfrak{a}_n,t)$. It also follows that the weighted
majorants dominate pointwise:
\begin{equation}\label{5.5:eq-near-unit-rows-1}
\begin{gathered}
|B^{ax}(b)|\le L^{-1}|B^{ax}|_*(b),\qquad |F|\le |F|_*,\\
|\mathfrak{e}_\mu|\le|\mathfrak{e}_\mu|_*\ \text{on level-$j$ bonds},\qquad
|\mathfrak{e}^{rim}|\le|\mathfrak{e}^{rim}|_*\ \text{on the graded rim of } \mathfrak{r}_v .
\end{gathered}
\end{equation}

Let $S=\alpha_{3,j}/\sup_b|B^{ax}(b)|$ be the radius of the field itself. Since
$|B^{ax}|\le|B^{ax}|_*$, comparison with the definition of $S^{\star}_v$ and with
\eqref{5.5:eq-near-unit-classes-a} gives
\begin{equation}\label{5.5:eq-near-unit-rows-2}
S\ \ge\ S^{\star}_v\ \ge\ \bigl(\Theta C_M D_X t^2\rho_{n,j}\bigr)^{-1}.
\end{equation}

\smallskip\noindent\emph{(ii) The rows.}

\emph{Box-read short single ($S^{\star}_v>1$).} The proof of the short-single lemma reads
$\mathfrak{b}'_j$ through condition (c1), which holds by step (i). It uses the chart
\begin{equation*}
\varphi(\sigma'):=F\bigl(X,U_j(\mathfrak{r}_v,e^{i\sigma'B^{ax}}),\dots\bigr).
\end{equation*}
For $|\sigma'|<S^{\star}_v$ we have $|\sigma'B^{ax}(b)|<S^{\star}_v|B^{ax}|_*(b)\le\alpha_{3,j}$.
So the chart stays in the domain given by condition (c2) and \cite[Lemma~4]{B-CMP109}, and $\varphi$
is holomorphic and bounded by $\mathfrak{n}$ on the disc $|\sigma'|<S^{\star}_v$. This disc contains
$1$ since $S^{\star}_v>1$. Moreover $\varphi'(0)=0$. The Schwarz lemma, in the form of
Lemma~\ref{5.2:lem-disc-bounds}, then gives the entry $2\mathfrak{n}_vS^{\star-2}_v$.

\emph{Box-read core, taken whole.} We use the steps of the proof of the core lemma rather than its
statement.
Each of its steps is a polynomial of degree at most $3$ in the data constant:
\begin{itemize}
\item the cubic Schwarz remainder on the chart;
\item the bilinear term $\varphi_X''(0)=D^2F(X;1,0)[\cdot,\cdot]$, through the bound
\begin{equation*}
|D^2F(X;1,0)[B_1,B_2]|\le 4\mathfrak{n}\,e^{-\kappa d_j(X)}\,|B_1|_\infty|B_2|_\infty\,
\alpha_{3,j}^{-2};
\end{equation*}
\item the main term of condition (c3);
\item the counterterm $A(h_y,\cdot)$, read on the same box pair $\mathfrak{b}'_j$, as the third class
files it.
\end{itemize}
Step (i) supplies the inputs with $\mathfrak{a}_n$ replaced by $\Theta\mathfrak{a}_n$. The
core lemma's bound therefore holds with $\rho_{n,j}$ replaced by $z$. Membership of the
arguments is given by condition (c2) on the chart. With the rim contribution of step (iii)
included, the constant is $C_I^{\sharp}\le C_I'$, and the entry is
$C_I'\mathfrak{n}\nu^3z^2(1+z)t^{4+\hat{\alpha}}$.

\emph{Own-read units.} By the own-read membership hypothesis of Lemma~\ref{5.5:lem-weight},
$|F(\mathcal{W}_T)|\le\mathfrak{n}$ for $|\tau|\le\rho_A(v)$. This gives the following entries.
\begin{itemize}
\item Tails, long singles and constituents with $\nu\le 2$: the entry $2\mathfrak{n}_v$.
\item The near constituents of a straddling core, at every $\nu$: such a core has
$y\in\tilde{\square}^2$ and $\mathfrak{r}_v\not\subset\tilde{\square}^2$. Its near constituents are
bounded by $2\mathfrak{n}_ve^{-\kappa d_j(X)}$ each, at the prefactor
$24K''\vartheta(\square)\eta_p$ with $\eta_p\le t^5$ by the own-read membership hypothesis, whose
two-machine clause gives the same row with $2\mathsf{S}$ in place of $2\mathfrak{n}_v$. This row
carries its own line in
\eqref{5.5:eq-weight-d}, together with its count per unit cell.
\item A read short single with $S^{\star}_v\le 1$: the entry
$2\mathfrak{n}_v=2\mathfrak{n}_v\min\{1,S^{\star-2}_v\}$, since $S^{\star-2}_v\ge 1$.
\item A read core with $S^{\star}_v\le 1$: treated in step (iv).
\end{itemize}

\emph{Third class.} The Wilson pieces $f_{\square}$ are entire. By the Wilson-piece bound, clause
(b), they are quadratic near the identity configuration. Each is supported within one level-$j$
unit of $y$, or in a block whose centre serves as $y$. Display \eqref{5.5:eq-weight-a}, applied
pointwise on $\mathfrak{b}'_j$, gives the entry $\Theta^2\mathfrak{N}_W(v)$.

For the counterterm piece of a core, the counterterm projection bound gives
$|\beta[F]|\le C\mathfrak{n}\alpha_{3,j}^{-2}$. Combined with the Wilson-piece bound, clause (b),
and \eqref{5.5:eq-weight-a}, this gives the entry $C'\mathfrak{n}z^2t^4$.

\smallskip\noindent\emph{(iii) The rim.}
The cover analysis has a step in which the insertion of condition (c3) into the core term costs
at most $C\mathfrak{n}e^{-\kappa d_j(X)}D^3\rho_{n,j}^2t^{4+\hat{\alpha}}$. That step uses the
H\"older member of (c3). In our setting, display \eqref{5.5:eq-weight-c} supplies the H\"older
member on level-$j$ bonds only, so we split $\mathfrak{e}=\mathfrak{e}^{in}+\mathfrak{e}^{rim}$.

The second derivative of the chart is
\begin{equation*}
\varphi_X''(0)=D^2F(X;1,0)\bigl[\mathsf{h}[B^{ax}],\mathsf{h}[B^{ax}]\bigr],
\qquad \mathsf{h}[B]:=\sum_b\mathsf{h}_bB(b).
\end{equation*}
Here, by \cite[(4.18)]{B-CMP109}, the family $\mathsf{h}_b$ decays exponentially, with the
constants $B_3$ and $\delta_0$ of \cite[(4.18)]{B-CMP109}:
\begin{equation*}
\max\bigl(|\mathsf{h}_b|,|\nabla\mathsf{h}_b|,\dots\bigr)\le
B_3e^{-\delta_0\operatorname{dist}_j(b,X)}=:\|\mathsf{h}_b\|_* .
\end{equation*}
For $\mathfrak{e}^{in}$, which lives on level-$j$ bonds, the insertion estimate of the cover
analysis applies unchanged.

By \eqref{5.5:eq-near-unit-rows-1} and the definition of $|\mathfrak{e}^{rim}|_*$, the remainder
$\mathfrak{e}^{rim}$ is bounded by $4dD\Theta\mathfrak{a}_nt^2$. It is supported on the outer
layer of $\mathfrak{r}_v$. Since $X\ni y$, that layer is at $\operatorname{dist}_j$ at least
$M(\nu-1-d_j(X))_+$ from $X$. Its insertion therefore costs at most
\begin{equation*}
C\mathfrak{n}D^{d+1}z^2t^4e^{-\kappa d_j(X)-\delta_0M(\nu-1-d_j(X))_+}
\ \le\ C''\mathfrak{n}\,e^{-\frac12\kappa d_j(X)}z^2t^{4+\hat{\alpha}} .
\end{equation*}

To justify the last inequality, put $\mu_0:=\min\{\tfrac12\kappa,\delta_0M\}$. Since
$d_j(X)+(\nu-1-d_j(X))_+\ge\nu-1$,
\begin{align*}
\kappa d_j(X)+\delta_0M(\nu-1-d_j(X))_+
 &\ge \tfrac12\kappa d_j(X)+\mu_0\bigl(d_j(X)+(\nu-1-d_j(X))_+\bigr)\\
 &\ge \tfrac12\kappa d_j(X)+\mu_0(\nu-1).
\end{align*}
The floor $\mu_0\ge 5\log L$ gives $e^{-\mu_0(\nu-1)}\le L^{-5(\nu-1)}$. We also have
$D=M(2\nu+3)\le 5M\nu$ and $t^{-\hat{\alpha}}=L^{\hat{\alpha}(\nu-1)}$. Hence
\begin{equation*}
D^{d+1}t^4e^{-\mu_0(\nu-1)}\ \le\ t^{4+\hat{\alpha}}\,(5M\nu)^{d+1}L^{(\hat{\alpha}-5)(\nu-1)} .
\end{equation*}
The last factor is bounded in $\nu$ because $\hat{\alpha}\le 1$. The constant $C''$ is one of the
contributions to $C_I^{\sharp}$ in Definition~\ref{5.5:def-weight-constants}.

\smallskip\noindent\emph{(iv) Near levels and the regime $S^{\star}_v\le 1$.}
Suppose $C_MDt^2z>\frac12$. Every read core with $S^{\star}_v\le 1$ is in this regime: for a core
$D_X=D$, so \eqref{5.5:eq-near-unit-rows-2} gives
\begin{equation*}
(C_MDt^2z)^{-1}\le S^{\star}_v\le 1<2 .
\end{equation*}

In this regime the core term $\mathfrak{i}_y$, read constituent by constituent together with its
counterterm companion, is trivially bounded by $2C(\kappa)\mathfrak{n}+C'\mathfrak{n}z^2t^4$. The
values are bounded as follows:
\begin{itemize}
\item at box-read units, by condition (c2) on the chart;
\item at own-read units, by the own-read membership hypothesis, constituent by constituent;
\item for the counterterm piece, by the counterterm projection bound, the Wilson-piece bound,
clause (b), and \eqref{5.5:eq-weight-a}.
\end{itemize}

Since $D\le 5M\nu$, the hypothesis $C_MDt^2z>\frac12$ gives $t^2>(10C_MM\nu z)^{-1}$. Hence
\begin{align*}
\nu^3z^2(1+z)t^{4+\hat{\alpha}}
 &\ge (10C_MM)^{-2-\hat{\alpha}/2}\,\nu^{1-\hat{\alpha}/2}\,z^{-\hat{\alpha}/2}(1+z)\\
 &\ge (10C_MM)^{-5/2}.
\end{align*}
In the second line we used $\nu\ge 1$ and $\hat{\alpha}\le 1$. We also used
$z^{-\hat{\alpha}/2}(1+z)\ge 1$: for $z\le 1$ the first factor is at least $1$, and for $z\ge 1$
the product is at least $z^{1-\hat{\alpha}/2}\ge 1$. By the member
$C_I'\ge 8C(\kappa)(10C_MM)^{5/2}$ of \eqref{5.5:eq-weight-constants-c},
\begin{equation*}
\tfrac12C_I'\mathfrak{n}\nu^3z^2(1+z)t^{4+\hat{\alpha}}\ \ge\ 4C(\kappa)\mathfrak{n}.
\end{equation*}
In the same way,
\begin{equation*}
\nu^3(1+z)t^{\hat{\alpha}}\ \ge\ (10C_MMz)^{-\hat{\alpha}/2}(1+z)\ \ge\ (10C_MM)^{-1/2}.
\end{equation*}
So by the member $C_I'\ge 4C'(10C_MM)^{1/2}$, the other half satisfies
\begin{equation*}
\tfrac12C_I'\mathfrak{n}z^2t^4\cdot\nu^3(1+z)t^{\hat{\alpha}}\ \ge\ 2C'\mathfrak{n}z^2t^4 .
\end{equation*}
Together, $C_I'\mathfrak{n}\nu^3z^2(1+z)t^{4+\hat{\alpha}}$ dominates the trivial bound. The
constant $C_I'$ does not depend on $\Theta$.

In the complementary regime $C_MDt^2z\le\frac12$, \eqref{5.5:eq-near-unit-rows-2} gives
$S^{\star}_v\ge 2>1$, so a read core is box-read there and its entry is that of step (ii), with
the rim of step (iii). The two regimes leave no gap.

The per-cell sums over own-read units do not depend on the field, by the field-free column bound.
They are therefore contained in the constant $\kappa_R$ of
Definition~\ref{5.5:def-weight-constants}.

\smallskip\noindent\emph{(v) Monotonicity in $\Theta$.}
Every row is non-decreasing in $\Theta$ and, since $\Theta\ge 1$, is at most $\Theta^a$ times its
value at $\Theta=1$, with $a\le 3$:
\begin{itemize}
\item Core: since $z=\Theta\rho_{n,j}$,
\begin{equation*}
z^2(1+z)=\Theta^2\rho_{n,j}^2(1+\Theta\rho_{n,j})\le\Theta^3\rho_{n,j}^2(1+\rho_{n,j}).
\end{equation*}
\item Short single: put
\begin{equation*}
x_v:=\Bigl(\sup_{b\subset\mathfrak{r}_v}2d(1+|b-y|)\mathfrak{a}_nt^2/\alpha_{3,j}\Bigr)^2 .
\end{equation*}
This is free of $\Theta$, and by \eqref{5.5:eq-windowed-source-b} we have
$S^{\star-2}_v=\Theta^2x_v$. Hence
\begin{equation*}
2\mathfrak{n}_v\min\{1,S^{\star-2}_v\}=2\mathfrak{n}_v\min\{1,\Theta^2x_v\}
\le\Theta^2\cdot2\mathfrak{n}_v\min\{1,x_v\}.
\end{equation*}
\item Wilson pieces: degree $2$.
\item Own-read units and remainders: degree $0$.
\end{itemize}
Comparing each row, under the filing that its own $\Theta$ prescribes, with its value at
$\Theta=1$ gives the degree bound of \eqref{5.5:eq-weight-d}. In particular,
\begin{equation*}
\mathfrak{N}^P(v;c_Ww)\le w^3\,\mathfrak{N}^P(v;c_W)\qquad (w\ge 1).
\end{equation*}
The Cauchy-integral bound on the filed discs is linear in $\mathfrak{N}(v)$, and its prefactors do
not depend on $\Theta$. The near terms at a block are grouped into the total by the grouping rule
of the sourced stage for the total at a block. By the own-read membership hypothesis, the own-read
pieces remain summands of the one near element.

\smallskip\noindent\emph{The other pieces.}
The far pieces are bounded by the far-piece clause of the sourced-stage estimate, with the far
terms of the second kind read on the configuration prescribed by that clause.

The remainders of clause (b$'$) of Lemma~\ref{5.5:lem-weight} are those named in
Definition~\ref{5.5:def-windowed-source}. For
them, membership, size and sum follow from two hypotheses of Lemma~\ref{5.5:lem-weight}: the
remainder hypothesis for box-read units, at the units of the rows $\flat$, and the remainder
hypothesis for the third class, at the third-class pieces. There are no remainders at own-read
units.

Finally, the pieces at blocks meeting the collar $R_{\mathsf{n}}$ read no cell of
$\mathcal{W}$, by clause (c) of Lemma~\ref{5.5:lem-weight}.
```

**W5-C1 (correction: degree language and reference).** The short-single row contains \(\min\{1,(S_v^\star)^{-2}\}\). The proof's word “polynomials” is therefore a degree majorization, not a polynomial identity. For \(a\ge1,u\ge0\), \(\min(1,a^2u^2)\le a^2\min(1,u^2)\): check \(u\ge1\), \(u<1,au\le1\), and \(u<1<au\) separately. This preserves the cubic weight majorization. The reference to “(b′)” in the row-three discussion means the remainder rows of (b), not an additional stated clause. No constant or row changes.

**W5-F2 (filled: straddling sum).** With \(q=L^{-(2-\hat\alpha)}<1\),
\[
\sum_{\nu\ge1}(\nu+2)q^{\nu-1}=\frac3{1-q}+\frac{q}{(1-q)^2}.
\]
This follows by differentiating finite geometric sums and taking their convergent limits. Rim polynomial factors are absorbed only in the exponential slack allocated in the source, preserving its decay rate.

### (c): weighted cells

CA-II:36037–36249. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of \eqref{5.5:eq-weight-e} in Lemma~\ref{5.5:lem-weight}: weighted cells within
reach of a block]\label{5.5:prf-weighted-cells}
We work in the setting of Definition~\ref{5.5:def-windowed-source}, with the levels and weights of
Notation~\ref{5.5:not-weight-notation}. Thus $\ell(x)$ is the current level of a point or cell $x$ and
$w$ is the actual weight. The set $\mathcal{W}$ consists of the inherited raised cells of the live
arrests of earlier steps. The block $\square$ lies in zone $n_0$, its own cell $\Delta_0$ has level
$n_0$, and for $y\in\tilde{\square}^2$ we put $n:=\min\{\ell(y),n_0\}$. Finally, $\mathfrak{R}(\square)$
is the set of cells within one own unit of $\tilde{\square}^2$, each of which meets
$\tilde{\square}^3$.

For a level $m$, $\operatorname{dist}_m$ denotes distance measured in units of $\ell_m=L^m\eta$. It
does not increase when $m$ increases.

An arrest or preparation $\mathfrak{c}$ comes with the following data: its region $X_{\mathfrak{c}}$,
its steps $h_{\mathfrak{c}}$ and $k_{\mathfrak{c}}$, and its level $k_0(\mathfrak{c})$. Recall from
\eqref{5.5:eq-weight-e} in Lemma~\ref{5.5:lem-weight} that $t_{\mathfrak{c}}=k_{\mathfrak{c}}$ if
$\mathfrak{c}$ is an arrest and $t_{\mathfrak{c}}=k$ if $\mathfrak{c}$ is the running or a sibling
preparation of the present operation $\mathbf{R}_k$, and that $t(\Delta)=t_{\mathfrak{c}}$ for a
weighted cell $\Delta$, where $\mathfrak{c}$ is the arrest or preparation whose weight $\Delta$
carries. In particular $t(\Delta)=k_{\mathfrak{a}}$ if $\Delta$ is one
of the cells $W_{\mathfrak{a}}$ of a live arrest $\mathfrak{a}$, on which $w=w_{\mathfrak{a}}$.
We write $\check{R}_m$ for Ba{\l}aban's separation radius at level $m$, and $\check{R}$ for the
separation radius between disjoint regions; it satisfies $\check{R}\ge 38$.

\emph{Step one: the separation claim.} We first prove, for every point $y$,
\begin{equation}\label{5.5:eq-weighted-cells-a}
\mathfrak{a}\ \text{a live arrest},\quad m:=\ell(y)>k_{\mathfrak{a}}
\quad\Longrightarrow\quad \operatorname{dist}_m(y,X_{\mathfrak{a}})\ge 3 .
\end{equation}
The point $y$ lies in the current small-field region $\Omega_m$. The region of $\mathfrak{a}$ satisfies
$X_{\mathfrak{a}}\subset Z_{k_{\mathfrak{a}}}$, and $Z_{k_{\mathfrak{a}}}\subset Z_{m-1}$ by the
monotonicity of the large-field regions in the level, part of the level-and-zone statement of the
scaffold, since $k_{\mathfrak{a}}\le m-1$. We distinguish two cases according to how $\Omega_m$ near
$y$ was made.

If the operation $\mathbf{T}_m$ made $\Omega_m$ near $y$, then by Ba{\l}aban's construction of
$\mathbf{T}_m$ in \cite{B-CMP119} the point $y$ lies at level-$m$ distance at least $8\check{R}_m$ from
$Z_{m-1}\supset X_{\mathfrak{a}}$. In particular this distance is at least $3$.

Otherwise, by the statement on arrests of attempts, exactly one attempt $\mathfrak{c}$ re-made
$\Omega_m$ near $y$. Its steps satisfy
$h_{\mathfrak{c}}<m\le k_{\mathfrak{c}}$, and $y\in X_{\mathfrak{c}}$. We compare $X_{\mathfrak{a}}$ with
$X_{\mathfrak{c}}$ in three cases.
\begin{itemize}
\item Suppose $X_{\mathfrak{c}}\subsetneq X_{\mathfrak{a}}$. By the ordering statement for nested
regions, the region strictly inside the other belongs to the earlier step, so
$k_{\mathfrak{c}}<k_{\mathfrak{a}}$. Hence
$m\le k_{\mathfrak{c}}<k_{\mathfrak{a}}$, which contradicts $k_{\mathfrak{a}}<m$.
\item Suppose $X_{\mathfrak{a}}$ and $X_{\mathfrak{c}}$ are disjoint. By the separation statement for
disjoint regions, they lie at distance at
least $\check{R}$ from each other. Since $y\in X_{\mathfrak{c}}$, the distance from $y$ to
$X_{\mathfrak{a}}$ is at least $\check{R}\ge 3$.
\item Suppose $X_{\mathfrak{a}}\subset X_{\mathfrak{c}}$. By the ordering statement for nested regions,
the inner region was made no later than the outer one began, and the beginning step of a preparation
precedes its level $k_0$, by the definition of $N_0$ in \cite{B-CMP122a}. Therefore
\begin{equation*}
k_{\mathfrak{a}}\le h_{\mathfrak{c}}<k_0(\mathfrak{c}),
\end{equation*}
and $X_{\mathfrak{a}}\subset Z'_{k_0(\mathfrak{c})}$. The level-$m$ distance from $y$ to
$Z'_{k_0(\mathfrak{c})}$ is bounded below in three sub-cases:
\begin{itemize}
\item it is at least $3\check{R}_m$ if $m\le k_0(\mathfrak{c})$;
\item it is at least $L^{k_{\mathfrak{c}}-m}\ge L$ if $k_0(\mathfrak{c})<m<k_{\mathfrak{c}}$;
\item it is at least $3$ if $m=k_{\mathfrak{c}}$.
\end{itemize}
In the last sub-case the bound holds because $Z''_{k_{\mathfrak{c}}}$ is the enlargement
$Z'^{\sim 3}_{k_0(\mathfrak{c})}$ of $Z'_{k_0(\mathfrak{c})}$ by three layers \cite{B-CMP122a}. Since
$\check{R}_m\ge 1$ and $L>3$, the distance is at least $3$ in each sub-case.
\end{itemize}
This proves \eqref{5.5:eq-weighted-cells-a}.

We draw the first consequence. Let $\Delta\in\mathcal{W}$, $y\in\tilde{\square}^2$ and
$\operatorname{dist}_n(\Delta,y)<1$. Then $\Delta$ is one of the cells $W_{\mathfrak{a}}$ of a live
arrest $\mathfrak{a}$, and these lie in $X_{\mathfrak{a}}$. Since $n\le\ell(y)$, the bound
$\operatorname{dist}_n(\Delta,y)<1$ gives $\operatorname{dist}_{\ell(y)}(\Delta,y)<1$, hence
$\operatorname{dist}_{\ell(y)}(y,X_{\mathfrak{a}})<3$. By \eqref{5.5:eq-weighted-cells-a} this forces
$\ell(y)\le k_{\mathfrak{a}}$, that is,
\begin{equation}\label{5.5:eq-weighted-cells-1}
t(\Delta)=k_{\mathfrak{a}}\ge\ell(y).
\end{equation}
If $\ell(y)\ge n_0-1$, then \eqref{5.5:eq-weighted-cells-1} gives $t(\Delta)\ge n_0-1$. It remains to
treat blocks whose set $\tilde{\square}^2$ holds a point of level at most $n_0-2$.

\emph{Step two: the thin stratum.} Let $\tilde{\square}^2$ hold a point of level at most $n_0-2$. This
point lies within $3$ level-$n_0$ units of the own cell $\Delta_0$, which has level $n_0$. By the
level-and-zone statement of the scaffold, levels change
by at most one between neighbouring cells, so zone $n_0-1$ is crossed within $3$ such units.

By the level-and-zone statement, the zones of a preparation have widths, in level-$n_0$ units, at
least $8\check{R}_{n_0}$, at least $3\check{R}_{n_0}$, at least $L$ (a $k_0$-zone) and at least $1$
(a thin stratum), according to the kind of zone.
Of these, only a thin stratum can have width at most $3$. Hence the piece crossed is a thin stratum of
a preparation $\mathfrak{c}$, for which
\begin{equation*}
k_0(\mathfrak{c})\le n_0-2,\qquad t_{\mathfrak{c}}\ge n_0,\qquad
\Delta_0\subset X_{\mathfrak{c}}\setminus Z''^{(\mathfrak{c})}_{n_0}.
\end{equation*}
Moreover $\tilde{\square}^2\subset X_{\mathfrak{c}}$. Indeed, by the collar statement for
preparations, the strata lie behind the collar of
$X_{\mathfrak{c}}$ of width $2\check{R}_{t_{\mathfrak{c}}}$, while $\tilde{\square}^2$ reaches only $3$
units from $\Delta_0$, and $3<\check{R}$.

\emph{Step three: uniqueness.} Suppose two preparations have thin strata inside $\tilde{\square}^2$. By
step two, each of their regions contains $\Delta_0$, so the regions are nested. Let the inner one have
step $t_{\mathrm{inner}}$, and the outer one steps $h_{\mathrm{outer}}$ and $k_0(\mathrm{outer})$. Step
two gives $t_{\mathrm{inner}}\ge n_0$ and $k_0(\mathrm{outer})\le n_0-2$. By the ordering statement for
nested regions, the inner region was made no
later than the outer one began, and $h_{\mathrm{outer}}<k_0(\mathrm{outer})$ by the definition of $N_0$
in \cite{B-CMP122a}.
Together these give
\begin{equation*}
n_0-1<t_{\mathrm{inner}}\le h_{\mathrm{outer}}<k_0(\mathrm{outer})<n_0-1,
\end{equation*}
which is absurd. Hence $\mathfrak{c}$ is unique.

\emph{Step four: reach and the level window.} We measure from $\Delta_0$ in level-$n_0$ units.
\begin{itemize}
\item If $n_0<t_{\mathfrak{c}}$, the set $Z'_{k_0(\mathfrak{c})}$ lies
$L^{t_{\mathfrak{c}}-n_0}\ge L>3$ units away.
\item If $n_0=t_{\mathfrak{c}}$, it lies exactly $3$ units away, by the enlargement identity of
\cite{B-CMP122a} recalled in step one.
\end{itemize}
Hence $\tilde{\square}^2$ meets $Z'_{k_0(\mathfrak{c})}$ at most along its boundary. Cells of
$X_{\mathfrak{c}}$ off the interior of $Z'_{k_0(\mathfrak{c})}$ have level at least $k_0(\mathfrak{c})$
\cite[(1.11)]{B-CMP122a}. With the upper bound $n_0+1$ from the facts stated with
Definition~\ref{5.5:def-data-factor}, every cell inside $\tilde{\square}^2$ has level in
$[k_0(\mathfrak{c}),n_0+1]$.

Let $y\in\tilde{\square}^2$. Then $\ell(y)\ge k_0(\mathfrak{c})\ge h_{\mathfrak{c}}+1$. Let
$\mathfrak{a}$ be a live arrest with a cell within one unit of $y$. Then
\eqref{5.5:eq-weighted-cells-a}, applied as in the derivation of \eqref{5.5:eq-weighted-cells-1},
gives
\begin{equation}\label{5.5:eq-weighted-cells-2}
k_{\mathfrak{a}}\ge\ell(y)\ge h_{\mathfrak{c}}+1.
\end{equation}

\emph{Step five: a live arrest against the preparation.} Let $\mathfrak{a}$ be as at the end of step
four. The comparison below uses the following inputs:
\begin{itemize}
\item the comparison of a live arrest with another live arrest, if $\mathfrak{c}$ is a live arrest;
\item the separation statement for disjoint regions;
\item the geometry statements of the comparison lemma's region, if $\mathfrak{c}$ is the running or a
sibling preparation of the comparison lemma's region.
\end{itemize}
We consider three cases.
\begin{itemize}
\item Suppose $X_{\mathfrak{a}}$ and $X_{\mathfrak{c}}$ are disjoint. They then lie at least
$\check{R}\ge 38$ apart. But $\tilde{\square}^2\subset X_{\mathfrak{c}}$ has diameter at most $6$,
and $\mathfrak{a}$ has a cell within one unit of it. This is impossible.
\item Suppose $X_{\mathfrak{a}}\subsetneq X_{\mathfrak{c}}$. By the ordering statement for nested
regions, the inner region was made no later than
the outer one began, so $k_{\mathfrak{a}}\le h_{\mathfrak{c}}$. This contradicts
\eqref{5.5:eq-weighted-cells-2}.
\item Suppose $X_{\mathfrak{c}}\subsetneq X_{\mathfrak{a}}$. Then
$k_{\mathfrak{c}}\le h_{\mathfrak{a}}$. By the layer statement for raised cells, the raised cells of
$\mathfrak{a}$ lie at least three layers
of cubes of side $LM\check{R}_{h_{\mathfrak{a}}+1}$ away from
$Z_{h_{\mathfrak{a}}}\supset X_{\mathfrak{c}}$. If $\mathfrak{c}$ is the running or a sibling
preparation of the comparison lemma's region, we argue instead from the treated component $C$ of that
region. Let $\mathsf{C}_C$ be its core, $h$ the step at which the preparation treating $C$ began, and
$Y^{\sharp}$ the set fixed in the geometry statements of that region. By those statements the core
$\mathsf{C}_C$ contains $Y^{\sharp}$, and every collar $R_\nu$ of $C$ satisfies
\begin{equation*}
\operatorname{dist}_{h+1}(Y^{\sharp},R_\nu)\ge\tfrac52\check{R}_{h+1}.
\end{equation*}
In either case no raised cell of $\mathfrak{a}$ lies at distance less than $1$ from
$\tilde{\square}^2\subset X_{\mathfrak{c}}$, which is a contradiction.
\end{itemize}
Hence $\mathfrak{a}=\mathfrak{c}$. For $\Delta\in\mathcal{W}$ within one own unit of
$y\in\tilde{\square}^2$ this gives
\begin{equation}\label{5.5:eq-weighted-cells-3}
t(\Delta)=t_{\mathfrak{c}}\ge n_0 .
\end{equation}

The same conclusion holds for every weighted cell within one own unit of $\tilde{\square}^2$. By the
layer statement for raised cells, the cells raised during the present run of $\mathbf{R}_k$ belong to
the preparation of this run, and by the anchor statement at the current step this preparation is again
$\mathfrak{c}$, with $t_{\mathfrak{c}}=k$. A completed preparation's cells carry weight $1$
(Notation~\ref{5.5:not-weight-notation}; after a completed operation the block partition on $Z$ is that
of \cite[(1.33)]{B-CMP122b}), and so are not weighted.

Steps two to five give the second assertion of \eqref{5.5:eq-weight-e}. Together with
\eqref{5.5:eq-weighted-cells-1} and \eqref{5.5:eq-weighted-cells-3}, they give
$t(\Delta)\ge\ell(y)$ and $t(\Delta)\ge n_0-1$ for every $\Delta\in\mathcal{W}$ and
$y\in\tilde{\square}^2$ with $\operatorname{dist}_n(\Delta,y)<1$.

\emph{Step six: old and exceptional blocks.} Let $\Delta\in\mathcal{W}\cap\mathfrak{R}(\square)$. Then
$\Delta$ meets $\tilde{\square}^3\subset\tilde{\square}^5$. By the facts stated with
Definition~\ref{5.5:def-data-factor}, either $\square\in\mathfrak{O}^+$ or $\square$ is exceptional.

In the second case the own cell of $\square$ lies off
\begin{equation*}
Z''_k=Z\cap Z'^{\sim 3}_{k_0}.
\end{equation*}
Consequently every $y\in\tilde{\square}^2$ satisfies
\begin{equation*}
\ell(y)\ge k_0(k)>h\ge k_{\mathfrak{a}}
\end{equation*}
for every live arrest $\mathfrak{a}$ inside the component $C''$. Here $C''$ is the component treated
by the present preparation of $\mathbf{R}_k$, which began at step $h$ and has level $k_0(k)$. The last
inequality holds by the ordering statement for nested regions, since the region of $\mathfrak{a}$ lies
inside that of this preparation. Live arrests
in other components lie at least $\check{R}_k$ away. So \eqref{5.5:eq-weighted-cells-a} forbids any
contact within one unit between $\tilde{\square}^2$ and a cell of $\mathcal{W}$. Hence an exceptional
block reads no cell of $\mathcal{W}$ through $\mathfrak{R}(\square)$.

Finally, a residual cell in the sense of the facts stated with Definition~\ref{5.5:def-data-factor} has
$t\le n_0-3$, which contradicts $t(\Delta)\ge n_0-1$, proved above. Hence no window block, the
exceptional ones included, reads a cell
of $\mathcal{W}$ through $\mathfrak{R}(\square)$. A cell of $\mathcal{W}$ within one own unit of
$\tilde{\square}^2$ can therefore occur only at a block $\square\in\mathfrak{O}^+$. This completes the
proof of \eqref{5.5:eq-weight-e}.
\end{proof}
```

### (c′) and (d): count times weight and data factor

CA-II:36251–36484. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of the count-times-weight bound and of the data-factor bound]
\label{5.5:prf-count-weight}
We prove the two parts of the count-times-weight bound \eqref{5.5:eq-weight-f} of
Lemma~\ref{5.5:lem-weight}, and then clause~(d) of that lemma, \eqref{5.5:eq-weight-g}. We
write $\mathsf{L}_0=L_{\circ}$ for the weight base of
Notation~\ref{5.5:not-weight-notation}. Recall from Definition~\ref{5.5:def-weight-constants}
that
\begin{equation*}
\mathfrak{K}(\square)=\sum\bigl\{w^{\vee}(\Delta')^3:\ \Delta'\text{ a unit $n$-cell inside }
\tilde{\square}^2\bigr\}
\end{equation*}
at every block $\square$, where $w^{\vee}(\Delta')$ is the largest weight of a cell within one
own unit of $\Delta'$. A cell $\Delta$ of raise $\mathsf{r}$ has weight
$w(\Delta)\le\mathsf{L}_0^{2\mathsf{r}}$,
and $\mathsf{L}_0^6\le L^3/27$ by \eqref{5.5:eq-weight-notation-a}; in particular
$\mathsf{L}_0^2\le L$. In the proof of the two parts of \eqref{5.5:eq-weight-f} the block
$\square$ is such that $\tilde{\square}^5$ meets $\mathcal{W}$; then $\square\in\mathfrak{O}^+$ or
$\square$ is exceptional, and $\varrho=\varrho(\square)\ge\check{R}_k-4$. The constant of the
target bound \eqref{5.5:eq-data-factor-a} of Definition~\ref{5.5:def-data-factor}, and the second
member of its defining maximum in \eqref{5.5:eq-weight-constants-b}, the constant introduced in
Definition~\ref{5.5:def-data-factor}, are written $C^{\mathrm{dat}}$ and $C^{\mathrm{dat}}_{pr}$
respectively; in particular $C^{\mathrm{dat}}\ge C^{\mathrm{dat}}_{pr}$.

\emph{Part~(i).} Suppose that $\tilde{\square}^2$ holds no point of level $\le n_0-2$. The unit
$n$-cells inside $\tilde{\square}^2$, which has side $6$, are then of three kinds: cells of level
$n_0-1$, of which there are at most $(6L)^d$; cells of level $n_0$, at most $6^d$; and level-$n_0$
sub-cubes of cells of level $n_0+1$, at most $6^d$. Their number is therefore at most
\begin{equation}\label{5.5:eq-count-weight-1}
(6L)^d+6^d+6^d\le 2(7L)^d .
\end{equation}
For each such $\Delta'$, the quantity $w^{\vee}(\Delta')$ is a maximum over cells within one own
unit of $\Delta'$, and two kinds of weighted cells can occur there.

A cell raised during the present operation $\mathbf{R}_k$ and lying within one own unit of
$\Delta'$ meets $\tilde{\square}^5$, so its raise $\mathsf{r}$ is at most $s(\square)$, which is,
by Definition~\ref{5.5:def-data-factor}, the largest raise of this $\mathbf{R}_k$ over cells
meeting $\tilde{\square}^5$; hence such a cell $\Delta$ has
$w(\Delta)^3\le\mathsf{L}_0^{6\mathsf{r}}\le L_{\circ}^{6s(\square)}$.

The other weighted cells there are inherited: let $\Delta\in\mathcal{W}$ lie within one own unit
of $\Delta'$. By the geometry clause \eqref{5.5:eq-weight-e} of
Lemma~\ref{5.5:lem-weight}, the step $t:=t(\Delta)$ satisfies $t\ge n_0-1$; by the bound on the
raises of inherited cells, $\mathsf{r}(\Delta)\le N_0(t)$. Hence
$w(\Delta)\le\mathsf{L}_0^{2N_0(t)}$ and,
as $\mathsf{L}_0^2\le L$, $w(\Delta)^3\le L^{3N_0(t)}$. The depth bound for the data factor gives
$L^{3N_0(t)}\le L^{12}(\check{\mathsf{T}}_k+3+c_{k-t})^{6r_{pr}}$. Since $\tilde{\square}^5$ meets
$\mathcal{W}$, the level estimate $k-n_0+1\le N_*+\varrho$ of
Definition~\ref{5.5:def-data-factor} holds, and the depth bound $N_*+\varrho\le\mathsf{n}(\varrho)$
together with the bound $\check{\mathsf{T}}_k\le\varrho+4$ on the depth parameter at old and
exceptional blocks give the two level estimates
\begin{equation*}
k-n_0+1\le N_*+\varrho\le\mathsf{n}(\varrho),\qquad \check{\mathsf{T}}_k\le\varrho+4 ;
\end{equation*}
and $t\ge n_0-1$ gives $k-t\le k-n_0+1\le\mathsf{n}(\varrho)$. Since
$c_j=\log(1+3\lambda j+2c_2)$ is increasing in $j$, $c_{k-t}\le c_{\mathsf{n}(\varrho)}$.
Therefore
\begin{equation}\label{5.5:eq-count-weight-2}
\begin{aligned}
w(\Delta)^3&\le L^{3N_0(t)}\le L^{12}\bigl(\check{\mathsf{T}}_k+3+c_{k-t}\bigr)^{6r_{pr}}
\le L^{12}\bigl(\varrho+7+c_{\mathsf{n}(\varrho)}\bigr)^{6r_{pr}}\\
&\le C^{\mathrm{dat}}_{pr}\,e^{\varrho-2},
\end{aligned}
\end{equation}
the last inequality by the definition
\begin{equation*}
C^{\mathrm{dat}}_{pr}=\sup_{\varrho'\ge1}L^{12}\bigl(\varrho'+7+c_{\mathsf{n}(\varrho')}\bigr)^{6r_{pr}}
e^{2-\varrho'}
\end{equation*}
of Definition~\ref{5.5:def-data-factor}, since $\varrho\ge1$. Consequently
\begin{equation*}
w^{\vee}(\Delta')^3\le\max\bigl\{L_{\circ}^{6s(\square)},\,C^{\mathrm{dat}}_{pr}e^{\varrho-2}\bigr\}
\end{equation*}
for every unit $n$-cell $\Delta'$ inside $\tilde{\square}^2$, and summing over the at most
$2(7L)^d$ such cells counted in \eqref{5.5:eq-count-weight-1} gives part~(i) of
\eqref{5.5:eq-weight-f}.

\emph{Part~(ii).} Suppose that $\tilde{\square}^2$ holds a point of level $\le n_0-2$, and let
$\mathfrak{c}$ be the one preparation given by the geometry clause \eqref{5.5:eq-weight-e}, of step
$t:=t_{\mathfrak{c}}\ge n_0$ ($t=k$ at an exceptional block). By that clause the cells inside
$\tilde{\square}^2$ have levels $m\in[k_0,n_0+1]$, where $k_0:=k_0(\mathfrak{c})=t-N_0(t)$ is the
lowest level of the preparation, $N_0(t)$ being its depth at step $t$ as in \cite{B-CMP122a}, and
every weighted cell within one own
unit of $\tilde{\square}^2$ is a cell of $\mathfrak{c}$. By the bound on the raises of the cells of
a preparation, such a cell $\Delta$ at level $i$ has raise at most $\max\{1,i-k_0\}$, and raise at
most $N_0(t)$, so that
\begin{equation*}
w(\Delta)\le\mathsf{L}_0^{2\max\{1,i-k_0\}}\le\mathsf{L}_0^{2N_0(t)} .
\end{equation*}
Cells within one level-$m$ unit of a level-$m$ cell have level at most $m+1$, by the level property
of the sequence of block partitions. Hence a unit cell $\Delta'$ of level $m\in[k_0,n_0]$ has
$w^{\vee}(\Delta')^3\le\mathsf{L}_0^{6(m+1-k_0)}$, and there are at most $(7L^{n_0-m})^d$ of them;
for the at most $7^d$ unit $n_0$-cells inside cells of level $n_0+1$,
$w^{\vee}\le\mathsf{L}_0^{2N_0(t)}$. Since $t\ge n_0$, we have $n_0-k_0=n_0-t+N_0(t)\le N_0(t)$.
Writing $m=k_0+q$ in the first sum, we obtain
\begin{equation}\label{5.5:eq-count-weight-a}
\begin{aligned}
\mathfrak{K}(\square)
&\le\sum_{m=k_0}^{n_0}7^dL^{d(n_0-m)}\mathsf{L}_0^{6(m+1-k_0)}+7^d\mathsf{L}_0^{6N_0(t)}\\
&\le 7^d\mathsf{L}_0^6L^{d(n_0-k_0)}\sum_{q\ge0}\bigl(\mathsf{L}_0^6L^{-d}\bigr)^q
+7^d\mathsf{L}_0^6\,\mathsf{L}_0^{6(N_0(t)-1)}\\
&\le 7^d\mathsf{L}_0^6L^{dN_0(t)}\Bigl[\bigl(1-(27L)^{-1}\bigr)^{-1}+1\Bigr]
\le 3\cdot7^d\mathsf{L}_0^6L^{dN_0(t)} .
\end{aligned}
\end{equation}
In the third line we used $n_0-k_0\le N_0(t)$; the inequality
$\mathsf{L}_0^6L^{-d}\le(27L)^{-1}$, which is \eqref{5.5:eq-weight-notation-a} with $d=4$,
so that the geometric series is at most $(1-(27L)^{-1})^{-1}$; and
\begin{equation*}
\mathsf{L}_0^{6(N_0(t)-1)}\le\bigl(L^3/27\bigr)^{N_0(t)-1}\le L^{dN_0(t)} .
\end{equation*}
In the last step, $(1-(27L)^{-1})^{-1}\le 27/26\le2$; the factor $3$ does not depend on $L$.

It remains to bound the factor $L^{dN_0(t)}$ by a constant times $e^{\varrho-1}$. Put
$y:=\check{R}_{k_0(t)+1}=L^{N_0(t)-1}$, so that $L^{dN_0(t)}=L^dy^d$. By
\cite[(2.5)]{B-CMP119}, $R(x)$ is the least power of $L$ which is $\ge(\log x)^{r_{pr}}$; hence
\begin{equation*}
y<L\max\bigl\{1,\check{\mathsf{T}}_{k_0(t)+1}^{\,r_{pr}}\bigr\}.
\end{equation*}
Since $k-k_0(t)-1=(k-t)+(N_0(t)-1)=(k-t)+\log_Ly$ and the sequence $c$ is sub-additive, the
comparison of the depth parameters at two levels gives
$\check{\mathsf{T}}_{k_0(t)+1}\le\check{\mathsf{T}}_k+1+c_{k-t}+c_{\log_Ly}$. With
$\mathsf{b}_t:=\check{\mathsf{T}}_k+1+c_{k-t}$ this reads $y<L(\mathsf{b}_t+c_{\log_Ly})^{r_{pr}}$. If
$c_{\log_Ly}\le\mathsf{b}_t$, then $y<L(2\mathsf{b}_t)^{r_{pr}}$. Otherwise
$y<L(2c_{\log_Ly})^{r_{pr}}$, and then
$y\le y_*$ by the definition $y_*=\sup\{y\ge1:\ y\le L(2c_{\log_Ly})^{r_{pr}}\}$ of
Definition~\ref{5.5:def-weight-constants}. In both cases
\begin{equation}\label{5.5:eq-count-weight-3}
y^d\le y_*^d+L^d2^{dr_{pr}}\mathsf{b}_t^{dr_{pr}} .
\end{equation}
At an old block, $t\ge n_0$ and the first level estimate give $k-t\le k-n_0+1\le\mathsf{n}(\varrho)$;
at an exceptional block $t=k$. In both cases $\check{\mathsf{T}}_k\le\varrho+4$ and
$c_{k-t}\le c_{\mathsf{n}(\varrho)}$, so that $\mathsf{b}_t\le\varrho+5+c_{\mathsf{n}(\varrho)}$.
Since $\varrho\ge1$, we have $y_*^d\le y_*^de^{\varrho-1}$ and
\begin{equation*}
\mathsf{b}_t^{dr_{pr}}\le\sup_{\varrho'\ge1}\bigl(\varrho'+5+c_{\mathsf{n}(\varrho')}\bigr)^{dr_{pr}}
e^{1-\varrho'}\cdot e^{\varrho-1}.
\end{equation*}
By \eqref{5.5:eq-count-weight-3} and the definition of $C^{tile}$ in
\eqref{5.5:eq-weight-constants-b}, therefore,
\begin{equation}\label{5.5:eq-count-weight-4}
\begin{aligned}
3\cdot7^d\mathsf{L}_0^6L^{dN_0(t)}&=3\cdot7^d\mathsf{L}_0^6L^dy^d
\le3\cdot7^d\mathsf{L}_0^6L^d\bigl[y_*^d+L^d2^{dr_{pr}}\mathsf{b}_t^{dr_{pr}}\bigr]\\
&\le C^{tile}e^{\varrho-1}.
\end{aligned}
\end{equation}
Together with \eqref{5.5:eq-count-weight-a} this is part~(ii) of \eqref{5.5:eq-weight-f}.

\emph{Clause~(d).} Let $\square$ be any block. The total at $\square$ which enters the definition
of $\mathfrak{d}(\square)$ in Definition~\ref{5.5:def-data-factor} is the resummation, by the
linear resummation lemma for the near-unit table, of the table of near-unit sizes. This
resummation is linear, its scaffold coefficients are non-negative, and the prefactors of the discs
\eqref{5.5:eq-near-unit-classes-b} are proportional to $\vartheta(\square)$. We group the near units
$v$ according to the unit $n$-cell $\Delta'$ which contains the anchor $y_v$. By the degree bound
of the table \eqref{5.5:eq-weight-d},
\begin{equation*}
\mathfrak{N}^P\bigl(v;c_Ww^{\vee}(y_v)\bigr)\le c_W^3\,w^{\vee}(\Delta')^3\,\mathfrak{N}^P(v;1).
\end{equation*}
By the definition of $\kappa_R^{act}$ in Definition~\ref{5.5:def-weight-constants} and
$\kappa_R\ge\kappa_R^{act}$, \eqref{5.5:eq-weight-constants-a}, the group of $\Delta'$, formed with
the table $\mathfrak{N}^P(\cdot\,;1)$, contributes at most $\kappa_R\mathfrak{N}_0(\square)$. By
linearity and non-negativity of the coefficients, the group of $\Delta'$ formed with the actual
sizes contributes at most $c_W^3w^{\vee}(\Delta')^3\kappa_R\mathfrak{N}_0(\square)$. Summing over
the unit $n$-cells $\Delta'$ inside $\tilde{\square}^2$, and using the definition
$\mathsf{l}^2(\square)=\max\{L_{\circ}^{6s(\square)},\kappa_Rc_W^3\mathfrak{K}(\square)\}$ of
\eqref{5.5:eq-weight-constants-b}, we obtain that at every block the total at $\square$ is at most
the left member of
\begin{equation}\label{5.5:eq-count-weight-5}
\kappa_Rc_W^3\,\mathfrak{K}(\square)\,\mathfrak{N}_0(\square)
\le\mathsf{l}^2(\square)\,\mathfrak{N}_0(\square).
\end{equation}

Now let $\tilde{\square}^5$ meet $\mathcal{W}$. By Definition~\ref{5.5:def-data-factor},
$\mathfrak{d}(\square)$ is the larger of $1$ and the quotient of the total at $\square$ by
$L_{\circ}^{6s(\square)}\mathfrak{N}_0(\square)$. Both are at most
$\mathsf{l}^2(\square)/L_{\circ}^{6s(\square)}$, the first because
$\mathsf{l}^2(\square)\ge L_{\circ}^{6s(\square)}$ and the second by \eqref{5.5:eq-count-weight-5};
that is, $L_{\circ}^{6s(\square)}\mathfrak{d}(\square)\le\mathsf{l}^2(\square)$. Next,
$\mathsf{l}^2(\square)\le\kappa_Rc_W^3\mathfrak{K}^{\sharp}(\square)
=L_{\circ}^{6s(\square)}\mathfrak{d}^{\sharp}(\square)$, which we check member by member. First,
$\mathfrak{K}\le\mathfrak{K}^{\sharp}$ by \eqref{5.5:eq-weight-f}. Second,
$L_{\circ}^{6s(\square)}\le\mathfrak{K}^{\sharp}(\square)\le\kappa_Rc_W^3\mathfrak{K}^{\sharp}(\square)$,
the second inequality because $\kappa_R\ge\kappa_R^{act}\ge1$ and $c_W\ge1$. The first holds in
case~(i) because
\begin{equation*}
\mathfrak{K}^{\sharp}(\square)=2(7L)^d\max\bigl\{L_{\circ}^{6s(\square)},\,
C^{\mathrm{dat}}_{pr}e^{\varrho-2}\bigr\}.
\end{equation*}
In case~(ii), $s(\square)=0$ when $\square\in\mathfrak{O}^+$ (Definition~\ref{5.5:def-data-factor}),
so that $L_{\circ}^{6s(\square)}=1\le\mathfrak{K}^{\sharp}(\square)$; at an exceptional block
$s(\square)\le N_0(k)$ and $t=k$, so that
\begin{equation*}
L_{\circ}^{6s(\square)}\le\mathsf{L}_0^6\,\mathsf{L}_0^{6(N_0(k)-1)}\le\mathsf{L}_0^6L^{dN_0(k)}
\le\mathfrak{K}^{\sharp}(\square).
\end{equation*}
Consequently $\mathfrak{d}^{\sharp}(\square)\ge1$ and
$\mathfrak{d}(\square)\le\mathfrak{d}^{\sharp}(\square)$.

By \eqref{5.5:eq-weight-f}, and since $L_{\circ}^{6s(\square)}\ge1$: in case~(i),
\begin{equation*}
\mathfrak{d}^{\sharp}(\square)\le2(7L)^d\kappa_Rc_W^3\max\bigl\{1,\,C^{\mathrm{dat}}_{pr}e^{\varrho-2}\bigr\};
\end{equation*}
in case~(ii), $\mathfrak{d}^{\sharp}(\square)\le\kappa_Rc_W^3C^{tile}e^{\varrho-1}$. By the floor
$\tfrac18\delta_Pw\ge2$ on the width $w$ which enters
$\varrho=1+d^{\wedge}(\square,R_{\mathsf{n}})/w$ in Definition~\ref{5.5:def-data-factor}, a floor
listed with the constants of Definition~\ref{5.5:def-weight-constants},
\begin{equation*}
e^{\varrho-2}\le e^{\varrho-1}=e^{d^{\wedge}(\square,R_{\mathsf{n}})/w}
\le e^{\frac18\delta_Pd^{\wedge}(\square,R_{\mathsf{n}})} .
\end{equation*}
Put $u:=\tfrac18\delta_Pd^{\wedge}(\square,R_{\mathsf{n}})\ge0$. Using $\max\{1,\xi\}\le1+\xi$, in
both cases $\mathfrak{d}^{\sharp}(\square)\le a+be^u$ with $a:=2(7L)^d\kappa_Rc_W^3\ge1$ and
$b:=\kappa_Rc_W^3[2(7L)^dC^{\mathrm{dat}}_{pr}+C^{tile}]$. Since $a\le ae^u$, we have
$a+be^u\le1+(a+b)e^u$ for $a\ge1$, $u\ge0$, and hence
\begin{equation}\label{5.5:eq-count-weight-6}
\begin{aligned}
\mathfrak{d}(\square)\le\mathfrak{d}^{\sharp}(\square)
&\le1+\kappa_Rc_W^3\bigl[2(7L)^d(1+C^{\mathrm{dat}}_{pr})+C^{tile}\bigr]
e^{\frac18\delta_Pd^{\wedge}(\square,R_{\mathsf{n}})}\\
&\le1+C^{\mathrm{dat}}e^{\frac18\delta_Pd^{\wedge}(\square,R_{\mathsf{n}})},
\end{aligned}
\end{equation}
the last inequality because $C^{\mathrm{dat}}$ is at least the third member of its defining maximum,
\eqref{5.5:eq-weight-constants-b}. Where $\tilde{\square}^5$ meets no cell of $\mathcal{W}$,
$\mathfrak{d}(\square)=1$ by Definition~\ref{5.5:def-data-factor}, and the same bound holds
trivially; this gives the target bound \eqref{5.5:eq-data-factor-a} at every block, with
$C^{\mathrm{dat}}\ge C^{\mathrm{dat}}_{pr}$.

All constants used in this proof are fixed before $\gamma$, and the bound on $\mathfrak{d}(\square)$
is of degree zero. The decay rate
$\tfrac18\delta_P$ spent here on $\mathfrak{d}$ and the rate $\tfrac38\delta_P$ spent in the other
decay estimate of Lemma~\ref{5.5:lem-weight} add up to $\tfrac12\delta_P$, the rate of
$\vartheta(\square)$, and the rate $\tfrac18\delta_P$ is spent only once.
\end{proof}
```

**W5-F3 (filled: exceptional depth and finite constants).** In the exceptional case \(k_0\le n_0-2\), hence \(N_0(t)\ge2\); the exponent \(N_0(t)-1\) is nonnegative. Since \(\mathsf L_0^2\le L/3\), \(\mathsf L_0^6L^{-4}\le(27L)^{-1}\), and the geometric series is bounded by \(27/26\le2\). For fixed \(p,c>0\), \(x^p e^{-cx}\to0\), by choosing an integer \(q>p\) and using \(e^{cx/2}\ge(cx/2)^q/q!\). This proves finiteness of all polynomial-exponential suprema used here. With \(x=\log y\) it also proves \((\log(1+C\log y))^{r_{\rm pr}}/y\to0\). Thus the defining set for \(y_*\) is bounded; if it is empty take the supremum in \([0,\infty]\), giving \(y_*=0\). The branch invoking membership of that set then never occurs, so no contribution is lost. The count spends \(\delta_P/8\), the other expenditure \(3\delta_P/8\), precisely the printed \(\delta_P/2\).

**W5-C2 (correction: constant aliases).** Identify \(C^{\mathrm{data}}_0,C^{\mathrm{data}}_{pr},C^{\mathrm{dat}}_{pr},C^{\mathtt a}_{pr}\) by the defining auxiliary supremum, and \(C^{\mathrm{data}},C^{\mathrm{dat}},C^{\mathtt a}\) by the final maximum, at II:34549–35005 and 36251–36484. These are notation variants, not four independent choices or a reduction of any maximum.

### (e): two machines on one scaffold

CA-II:36486–36797. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of clause~(e) of Lemma~\ref{5.5:lem-weight}]\label{5.5:prf-machine-differences}
Let $\mathsf{A}$ and $\mathsf{B}$ be the two machines on one scaffold of clause~(e) of the weight lemma
(Lemma~\ref{5.5:lem-weight}). Let $\mathcal{K}=\mathcal{K}^{rd}$ be their pair system, with the four
closure properties assumed in that clause and the closure of $\mathcal{K}$ under the move
$\mathsf{M}8$, which holds by construction of $\mathcal{K}^{rd}$. As there, for a function $f$ read in
both machines and $p\in\mathcal{K}$ we write
\begin{equation*}
\delta f(p) := f^{\mathsf{B}}(P^{\mathsf{B}})-f^{\mathsf{A}}(P^{\mathsf{A}}),
\end{equation*}
$\mathsf{S}:=\mathsf{S}^{rd}$ for the $\delta$-size and $\mathsf{a}:=\mathsf{S}^{rd}[\hat{A}]$ for the
$\delta$-size of the Wilson and counterterm functional $\hat{A}$. The index $\mathsf{m}$ runs over
$\{\mathsf{A},\mathsf{B}\}$. Throughout we use the notation fixed in the proof of the rows of the
near-unit table, within the proof of Lemma~\ref{5.5:lem-weight}: the data constants $\rho$ and $z$ of
those rows, the quantity $D$ (with $D\le 5M\nu$), and the constants $C(\kappa)$, $C$ and $C'$; the
letters $E_0$, $\mathfrak{N}_0(\square)$ and the base data $\mathfrak{n}_0$ are those of clauses~(d)
and~(e) of Lemma~\ref{5.5:lem-weight}, and $c_{\alpha}$, $C_R$, $C_2$ are the constants entering the
definition of $\kappa_R^{\times}$ in Definition~\ref{5.5:def-weight-constants}. We prove
\eqref{5.5:eq-weight-h} in the steps below. Step~4$'$ treats
the cores with $\nu\le 2$ and is inserted between Step~4 and Step~5.

\emph{Step 1: one scaffold.} The scaffold is one and the same for both machines. Hence the following
objects coincide in $\mathsf{A}$ and in $\mathsf{B}$:
\begin{itemize}
\item the level function $\ell$, the weight $w$, the family $\mathcal{W}$, the largest weight $w^{\vee}$
and $\Theta$;
\item the scaffold radius $S^{\star}_v$ of \eqref{5.5:eq-near-unit-classes-a}, the assignment of near
units to their classes, and the discs of \eqref{5.5:eq-near-unit-classes-b};
\item the boxes $Q_v$ and $\mathfrak{r}_v$, and the weighted scaffold majorants of
\eqref{5.5:eq-windowed-source-b};
\item the count $\mathfrak{K}(\square)$, the constants $\kappa_R$ of \eqref{5.5:eq-weight-constants-a}
and $c_W$, and the data factors $\mathsf{l}^2(\square)$ and $\mathfrak{d}^{\sharp}(\square)$ of
\eqref{5.5:eq-weight-constants-b}.
\end{itemize}

\emph{Step 2: clause~(a) in each machine.} Clauses (a1)--(a4) of Lemma~\ref{5.5:lem-weight} hold for the
box pair $\mathfrak{b}^{\mathsf{m}}$ of each machine $\mathsf{m}$ with the same constants. So do the
statements of part~(i) of the proof of the rows of the near-unit table, within the proof of
Lemma~\ref{5.5:lem-weight}. This is the hypothesis on the paired data made in the closure theorem
for the pair system. The membership input and the remainder input of
Definition~\ref{5.5:def-weight-inputs} likewise hold in each machine separately. Consequently the two
requirements which the two-machine comparison at the rim places on the paired reads are met at the
common weighted majorants of Step~1. The closure of $\mathcal{K}$ under the paired charts follows from
the closure of $\mathcal{K}$ under the move $\mathsf{M}5$.

\emph{Step 3: the difference principle.} Let $\mu\in\mathfrak{M}^{rd}$ be a move and let
$p\in\mathcal{K}^{rd}$. On the parameter domain $\mathfrak{P}_{\mu}$ of $\mu$ put
\begin{equation}\label{5.5:eq-machine-differences-1}
\delta(\pi) := f^{\mathsf{B}}\bigl(\mu^{\mathsf{B}}(\pi;P^{\mathsf{B}})\bigr)
-f^{\mathsf{A}}\bigl(\mu^{\mathsf{A}}(\pi;P^{\mathsf{A}})\bigr),\qquad \pi\in\mathfrak{P}_{\mu}.
\end{equation}
By clause~(iii) of the closure theorem for the pair system, $\delta$ is holomorphic on
$\mathfrak{P}_{\mu}$. Moreover
\begin{equation*}
|\delta|\le\sup_{\mathcal{K}}|f^{\mathsf{B}}-f^{\mathsf{A}}|,
\end{equation*}
and the right-hand side is the $\delta$-size. At the slot $\circ$ of the Wilson and counterterm pieces,
$\delta$ is entire and $\mathsf{a}\le 2\mathfrak{n}_{\hat{A}}$.

Three tools are used in the one-machine proofs: the Cauchy estimates, the three Schwarz-lemma bounds
(a)--(c), and, for a function $g$ read in one machine, the vanishing $\partial^i g(\pi_0)=0$ of
prescribed derivatives at the base point $\pi_0$ of the parameter domain. All three pass to $\delta$.
The first two apply to every bounded holomorphic function, and $\delta$ is one. The identities hold in
each machine, hence hold for the difference $\delta$ by subtraction.

\emph{Step 4: the places at which $\mathcal{K}$ is read.} The pair system is read at six places; the
seventh place listed in clause~(v)(c) of the closure theorem for the pair system, the closure under the
move $\mathsf{M}8$, is read here inside the fourth of them, the place of the $\circ$-class. We take the
places in turn.

\begin{enumerate}
\item The Cauchy integrals of the Cauchy-integral lemma for near units are taken on the discs of
\eqref{5.5:eq-near-unit-classes-b}. The prefactor of the paired Cauchy row of the two-machine comparison
at the rim is read as the prefactors fixed with those discs. The difference is controlled in two cases:
\begin{itemize}
\item at box pairs, by the closure of $\mathcal{K}$ under $\mathsf{M}2$;
\item at own-read units, by the closure under $\mathsf{M}3$.
\end{itemize}
The values at near levels are treated in the same way.

\item The short-single lemma uses the disc in $\sigma'$. Its chart satisfies
$(\varphi^{\mathsf{m}})'(0)=0$ for each machine $\mathsf{m}$. The difference is controlled by the
closure under $\mathsf{M}5$ with its first splitting.

\item The core lemma has several items, among them the rim item and the families generated from
$\mathbb{1}$. Inside each machine the marginal part cancels at $y$. These items are controlled by the
closure under $\mathsf{M}5$.

\item The $\circ$-class.
\begin{itemize}
\item The $\delta$-size $\mathsf{a}$ is reached through $\mathsf{M}2^{\circ}$.
\item At read cores, that is at cores with $\nu\ge 3$ and at every value of $S^{\star}_v$, the chart of
$\hat{A}$ has radius of order one. This chart is the paired chart of item~(a) of the move $\mathsf{M}5$
at radius $\alpha_3(\circ)$, taken through $\mathsf{M}2^{\circ}$ on the common majorants of part~(i) of
the proof of the rows of the near-unit table. Part~(i) supplies these majorants in each machine. This is
the hypothesis on the $\circ$-slot paired data of the closure theorem.
\item Off that chart two groups of items remain: the block pieces of row~5 at every $\nu$, and the
remainder rows of the counterterm companions at every $\nu$. Both follow from the third-class off-chart
input of Lemma~\ref{5.5:lem-weight} together with the closure of $\mathcal{K}$ under $\mathsf{M}8$.
\item The item of the companions at $\nu\le 2$ whose size is $\mathfrak{n}\mathsf{a}$ is treated in
Step~4$'$.
\end{itemize}

\item The remainders follow from the closure under $\mathsf{M}4$ and under $\mathsf{M}5$ with its fourth
splitting. This is the remainder input of Definition~\ref{5.5:def-weight-inputs}.

The remainders of the third class follow from the third-class remainder input. Its first member holds
as stated there. Its second member follows from the third-class off-chart input together with the
closure under $\mathsf{M}8$. Concretely, the second member is the pair of bounds (d)--(e) of that input
with $\mathsf{s}_v\mathsf{v}_v$ replaced by $C^{\perp}\mathsf{S}^{\perp}_v$.

\item The far pieces are controlled through three moves: $\mathsf{M}3$ at the far pairs, $\mathsf{M}4$
at the remainders, and $\mathsf{M}1^{M}$ combined with $\mathsf{M}6$.
\end{enumerate}

Hence the paired rows of the two-machine comparison at the rim, from the Cauchy row to the Wilson row,
hold as stated there with $\rho$ replaced by $\Theta\rho$. In particular the core term satisfies
\begin{equation}\label{5.5:eq-machine-differences-2}
|\delta\mathfrak{i}_y|\le C_I''(\mathsf{S}+\mathfrak{n}\mathsf{a})\,\nu^3(\Theta\rho)^2(1+\Theta\rho)\,
t^{4+\hat{\alpha}}.
\end{equation}
The short singles satisfy
\begin{equation}\label{5.5:eq-machine-differences-3}
|\delta f_v|\le 2\mathsf{S}\,e^{-\kappa d_j(X)}\min\bigl\{1,(S^{\star}_v)^{-2}\bigr\}.
\end{equation}
The own-read units satisfy
\begin{equation}\label{5.5:eq-machine-differences-4}
|\delta f_v|\le 2\mathsf{S}\,e^{-\kappa d_j(X)},
\end{equation}
by the membership input of Definition~\ref{5.5:def-weight-inputs}.

The Wilson pieces are bounded by $\Theta^2$ times their $\delta$-size. Off the chart this bound is
reached through the third-class off-chart input together with the closure under $\mathsf{M}8$. One
exception is left: the factor of the companions' item at $\nu\le 2$ treated in Step~4$'$.

Each of these bounds is a polynomial of degree at most three in $\Theta=c_Ww^{\vee}(y)\ge 1$. The
fraction $\tfrac18$ of the decay rate is spent once. Hence the degree bound of
\eqref{5.5:eq-weight-d} gives the factor $w^{\vee}(y)^3\,\mathfrak{N}^P(v;c_W)$ of
\eqref{5.5:eq-weight-h}, and these are the per-unit bounds of \eqref{5.5:eq-weight-h}, with the
substitutions $\mathfrak{n}\mapsto\mathsf{S}+\mathfrak{n}\mathsf{a}$, $C_I'\mapsto C_I''$ and
$\mathsf{s}_v\mathsf{v}_v\mapsto C^{\perp}\mathsf{S}^{\perp}_v$ stated there, apart from the item
treated in Step~4$'$.

\emph{Step 4$'$: cores with $\nu\le 2$.} At $\nu\le 2$ a core is own-read, by the class assignment of
Definition~\ref{5.5:def-near-unit-classes}, at every value of $S^{\star}_v$. Part~(i) of the proof of the
rows is stated for $\nu\ge 3$ and $L\ge 8$. This proof therefore provides at $\nu\le 2$ none of the
following on $\mathfrak{r}_v$: the identity, the comb rows, or a chart. None of them is used.

For one machine the core consists of two parts.
\begin{itemize}
\item Its constituents are units on $\mathcal{W}_T$, each bounded by $2\mathfrak{n}_v$.
\item Its counterterm companion $\beta[F]\hat{A}$ is a unit of the third class on $\mathfrak{b}'_j$. It
is bounded by $C'\mathfrak{n}z^2t^4$, by three statements: the counterterm-coefficient bound, the bound
for Wilson pieces, and \eqref{5.5:eq-weight-a}. This is part~(ii) of the proof of the rows of the
near-unit table and the clause of (b) on counterterm companions.
\end{itemize}

For two machines the constituents follow from the closure under $\mathsf{M}3$. By the membership input of
Definition~\ref{5.5:def-weight-inputs} their differences are bounded by
$2\mathsf{S}e^{-\kappa d_j(X)}$.

For the companion, the functional $\beta[\cdot]$ is linear. Hence
\begin{align}
\delta\bigl(\beta[F]\hat{A}\bigr)
&=\beta[F^{\mathsf{B}}]\hat{A}^{\mathsf{B}}-\beta[F^{\mathsf{A}}]\hat{A}^{\mathsf{A}}\notag\\
&=\beta[\delta F]\cdot\hat{A}^{\mathsf{B}}+\beta[F^{\mathsf{A}}]\cdot\delta\hat{A}.
\label{5.5:eq-machine-differences-5}
\end{align}
This is the two-machine identity for counterterm companions. The three factors are bounded as follows.
\begin{itemize}
\item $|\beta[\delta F]|$ is at most $\mathsf{S}$ times the constant and the squared inverse radius of
the paired counterterm-coefficient row of the two-machine comparison at the rim; this is the content
of that row.
\item $|\hat{A}^{\mathsf{m}}|\le\mathfrak{n}_{\hat{A}}$ in each machine, by the bound for Wilson pieces
together with \eqref{5.5:eq-weight-a}.
\item $\delta\hat{A}$ is controlled by the closure under $\mathsf{M}2^{\circ}$. Apply Step~3 at the
$\circ$-slot, which is entire, to
\begin{equation*}
\delta(\pi):=\hat{A}\bigl(\mathfrak{b}'^{\mathsf{B}}_j(\pi)\bigr)
-\hat{A}\bigl(\mathfrak{b}'^{\mathsf{A}}_j(\pi)\bigr).
\end{equation*}
This function is holomorphic on the parameter domain
$\mathfrak{P}=(b,\sigma)\times[0,1]\times\mathbb{D}_{\square}$ of $\mathsf{M}2$, whose first factor is
the range of the bond and $\sigma$ variables of the box read, and
$|\delta\hat{A}|\le\mathsf{a}$. This is a bound on the value; no chart enters.
\end{itemize}

Consider first the item $|\beta[\delta F]|\,|\hat{A}^{\mathsf{B}}|$. Because $\beta[\cdot]$ is linear,
it is the item of the table with $\mathfrak{n}$ replaced by $\mathsf{S}$.

Consider next the item
\begin{equation*}
|\beta[F^{\mathsf{A}}]|\,|\delta\hat{A}|\le C\mathfrak{n}\alpha_{3,j}^{-2}\mathsf{a}.
\end{equation*}
The two-machine statement for counterterm companions, which accompanies this identity, asserts
\begin{equation*}
|\delta\hat{A}|\le 2\mathsf{a}\,(CD\Theta\mathfrak{a}_nt^2)^2 ,
\end{equation*}
on the ground that $\hat{A}$ is entire at radius of order one: by the second Schwarz-lemma bound where
the radius of the chart of $\hat{A}$ exceeds one, and trivially otherwise. In the factor
$CD\Theta\mathfrak{a}_nt^2$, here and below, $C$ denotes a constant of that statement, containing the
factor $2d/\alpha_3(\circ)$; it is not the constant $C$ of the item just displayed. At $\nu\le 2$ we
examine the two halves of this assertion separately. The radius in question is that of the chart of
$\hat{A}$ on $\mathfrak{r}_v$,
\begin{equation*}
\alpha_3(\circ)\Big/\sup_{b\subset\mathfrak{r}_v}|B^{ax}|_*(b).
\end{equation*}

\begin{itemize}
\item Suppose this radius would be at most one, that is, $CD\Theta\mathfrak{a}_nt^2\ge 1$. Then the
value already carries the factor:
\begin{equation*}
|\delta\hat{A}|\le\mathsf{a}\le 2\mathsf{a}\,(CD\Theta\mathfrak{a}_nt^2)^2 .
\end{equation*}
The item is therefore at most $C'\mathfrak{n}\mathsf{a}z^2t^4$. This is the item of the table with
$\mathfrak{n}$ replaced by $\mathfrak{n}\mathsf{a}$. In total the two-machine statement for counterterm
companions gives the bound
\begin{equation*}
2C(\kappa)\mathsf{S}+C'(\mathsf{S}+\mathfrak{n}\mathsf{a})z^2t^4 .
\end{equation*}
Here $D\le 5M\nu\le 10M$ at $\nu\le 2$, and the resulting factor depending on $D$ is absorbed into
$C_I''$.

\item Suppose this radius would exceed one. Then the factor $(CD\Theta\mathfrak{a}_nt^2)^2$ is the one
given by the second Schwarz-lemma bound on a chart, and this proof does not construct that chart at
$\nu\le 2$. The table's form of the item there is carried by the off-chart clause of the paired Wilson
row of the two-machine comparison at the rim. That clause bounds the difference
\begin{equation*}
A^{\mathsf{B}}(c^{\mathsf{B}},P^{\mathsf{B}})-A^{\mathsf{A}}(c^{\mathsf{B}},P^{\mathsf{A}}),
\end{equation*}
in its own notation, through the bound for Wilson pieces. At the pair points of $\mathsf{M}2^{\circ}$,
this factor is the content of the low-order variation bound at the second cube size.

That bound is not among the hypotheses of clause~(e), and clause~(e) does not assert the table's form
of this item at these points; as clause~(e) states, that form rests on the low-order
variation bound at the second cube size, a statement on which the uniqueness theorem depends.

The third-class off-chart input, together with the closure under $\mathsf{M}8$, covers the second member
of the companion's third-class remainder at every $\nu$. Apart from the factor just named, what holds at
these points from the value alone is the bound $C\mathfrak{n}\alpha_{3,j}^{-2}\mathsf{a}$, which is
linear in $\mathsf{a}$.
\end{itemize}

At read cores ($\nu\ge 3$, every value of $S^{\star}_v$) the situation is different. The identity, the
comb rows and the four pointwise rows of part~(i) of the proof of the rows hold in each machine on
$\mathfrak{r}_v$. This is the hypothesis on the $\circ$-slot paired data of the closure theorem. The chart
of $\hat{A}$ in the two-machine identity for counterterm companions has radius of order one. It is the
paired chart of item~(a) of the move $\mathsf{M}5$ at radius $\alpha_3(\circ)$, taken through
$\mathsf{M}2^{\circ}$ at the common majorants. This chart carries $\delta\hat{A}$, with
\begin{equation*}
|\delta\hat{A}|\le 2\mathsf{a}\,(CD\Theta\mathfrak{a}_nt^2)^2 .
\end{equation*}
This is the form of the table. It is the form of the remainder line of the paired core row of the
two-machine comparison at the rim, which bounds the paired remainder of $\hat{A}$ by $C_I\mathsf{a}$ times
the weight at radius of order one, $C_I$ being the constant of that line.

No new constant, floor or ceiling enters Step~4$'$. The regimes are those of part~(iv) of the proof of
the rows and of the two-machine statement for counterterm companions.

\emph{Step 5: the block.} Three ingredients are field-free: clause~(c), the block-count lemma, and the
grouping by unit $n$-cells used in the proof of clause~(d) of Lemma~\ref{5.5:lem-weight}. Hence the same
$\mathsf{l}^2(\square)$ multiplies $\mathfrak{n}_0|_{E_0+1\mapsto\mathsf{l}^J}$. The ratio
$C_I''/C_I'$ is absorbed into $\mathfrak{n}_0|_1$, because the resummed total is linear in the sizes.

The passage from unit sizes to the $\delta$-sizes is paid by $\kappa_R^{\times}$. Consider the
$\delta$-sizes of the group of near units anchored in one unit $n$-cell $\Delta'$. Their per-cell row
sums in the near-unit table satisfy, row by row,
\begin{equation}\label{5.5:eq-machine-differences-6}
\sum_{v\in\text{row }r,\ y_v\in\Delta'}(\text{the per-unit bound of }v)
\le K_r\,\mathsf{l}^J\times(\text{the common cell factors of row }r).
\end{equation}
This is the per-cell row bound for the two-machine data functional. It holds for rows~1--3 and
$\partial$, and also for row~5, the remainder rows and the tail row of the closure theorem for the pair
system; for each of them $K_r$ is the single constant of Definition~\ref{5.5:def-weight-constants}.
\begin{itemize}
\item For the extended rows, $K_r$ is the per-cell number of the row at unit size, in the form in which
it is transported; the two-run constants are included in it.
\item For the third-class remainder row, the bound is the per-cube line of that row in its per-cube
$\delta$-size $\mathfrak{s}^{\perp}_{\alpha}$, with the constant $C^{\perp}K^W$, where $K^W$ is the
constant of the third-class remainder row.
\end{itemize}
The bound \eqref{5.5:eq-machine-differences-6} is read in the normalisation of the definition of
$\mathsf{l}^J$. The condition that the per-cell row-$r$ sums be at most $K_r$, in the definition of
$\kappa_R^{\times}$ (Definition~\ref{5.5:def-weight-constants}), uses the same constants $K_r$.

The resummation of the Cauchy-integral lemma for near units, with its scaffold coefficients, is linear in
the size vector; see the proof of clause~(d) of Lemma~\ref{5.5:lem-weight}. Hence the $\Delta'$-group at
the $\delta$-sizes equals $\mathsf{l}^J$ times the $\Delta'$-group at the $\delta$-sizes divided by
$\mathsf{l}^J$. By \eqref{5.5:eq-machine-differences-6}, the divided sizes have per-cell row-$r$ sums at
most $K_r$. So they lie in the set of sizes over which $\kappa_R^{\times}$ is defined. By that definition,
and since $\kappa_R\ge\kappa_R^{\times}$, the $\Delta'$-group is bounded by
\begin{align*}
\mathsf{l}^J\,\kappa_R^{\times}c_{\alpha}C_Re^{C_2\kappa_1}\vartheta(\square)
&\le\kappa_R\,c_{\alpha}C_Re^{C_2\kappa_1}\vartheta(\square)\,\mathsf{l}^J\\
&=\frac{\mathfrak{N}_0(\square)}{E_0}\,\kappa_R\,\mathsf{l}^J .
\end{align*}
This is the display \eqref{5.5:eq-weight-g} of (d) with $E_0$ replaced by $\mathsf{l}^J$. The linearity
in the sizes is used row by row, and no operator bound is needed.

The per-cell sums of rows~1 and~3 are summed over $j$ at the $\delta$-sizes; for row~3, whose cell number
is summable only through the sizes, this $j$-sum is the second member of $\mathsf{l}^J$.

The far pieces and the remainders are linear in the function. The items of the third class are treated as
in Steps~4 and~4$'$. Off the chart they follow from the third-class off-chart input together with the
closure under $\mathsf{M}8$. The factor of Step~4$'$ at $\nu\le 2$ is the low-order variation bound at
the second cube size, which is named there and is not an input of clause~(e). This proves the bound on
the differences at the one-block argument $\{\square\}$ asserted in clause~(e).

Clause~(e) is used in three ways. In the bound \eqref{5.5:eq-data-factor-a} on the data factor, read at
unit normalisation, the factor $(1+C^{\mathtt{a}})$ is kept on differences. The data functional
$\mathsf{l}_{\mathsf{n}+1}$ of the next stage contains $\mathsf{l}^J$ in sum form. The difference
statement for the count sums is taken over the same pair system $\mathcal{K}$.
\end{proof}
```

**W5-F4 (filled: zero normalization).** Divide the nonnegative size vector by \(\mathsf l^J\) only when \(\mathsf l^J>0\). If \(\mathsf l^J=0\), every nonnegative normalized row total is zero. The admitted per-unit bounds vanish and positive linear resummation is zero. This fills the zero case of II:36749–36756.

**W5-C3 (correction: scope of the total).** Carry the explicit exception in (e) into its final block-total sentence. At \(\nu\le2\),
\[
\delta(\beta[F]\hat A)=\beta[\delta F]\hat A^{\mathsf B}+\beta[F^{\mathsf A}]\delta\hat A.
\]
The first term has the admitted estimate. The second has the raw bound \(C\mathfrak n\alpha_{3,j}^{-2}\mathsf a\). If \(CD\Theta\mathfrak a_nt^2\ge1\), the raw bound supplies the factor. If it is less than one, W5-low is needed, as II:36706–36721 and 36785–36790 explicitly say. Thus the full consequent is conditional on W5-low; otherwise it applies to admitted pieces with the raw contribution retained. Third-class off-chart remainders do not supply it.

### Reconciliation of the two weight lemmas (chain-ca §7.1 item 3)

5.5:lem-weight controls windowed minimisers, fields, near-unit sizes, weighted counts and differences on **three filed discs**. It retains scaffold geometry, own-level and box membership, paired moves, third-class remainders and data-factor inputs. It does not assert analyticity in every decoupling variable.

5.6:lem-weight starts with **another input**, W6-H on \(P_{\mathcal V}(e^{\kappa_1})\), and the three chain properties. It extracts \(r(\kappa_1)\), counts link assignments and transfers decay already available on the exempt set. Application to actual localised terms still needs B1. At a consumer using both lemmas, first take the §5.5 size/data bound on its admitted domain, then retain B1 and chain geometry for that same term and datum before applying §5.6. Neither lemma proves the other's hypotheses. Plain-length transfer cannot replace relative length. The all-domain estimate spends a root-set prefactor; the fixed-domain application uses (b)/(c) without that expenditure. Both original Cauchy routes and constants are preserved.

## B4a: driven flow, before applying it to B3

The inputs are exactly the displayed radii, holomorphic functions, adaptive driver bound and summability hypothesis of 5.3:lem-driven-flow. This is an elementary conditional lemma; it does not provide the adaptive drivers. Its two analytic inputs are 5.2:lem-disc-bounds (a), II:2974–3021, and 5.2:lem-polydisc-gradient, II:3023–3087, both unqualified CA statements with proofs. Their needed arguments are filled below.

### Full proof of 5.3:lem-driven-flow

CA-II:26233–26324. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}
Write $\tfrac12\mathfrak{P}_k$ for the closed polydisc
$\{\xi=(\xi_j)_{j\le k}\in\mathbb{C}^{k+1}:|\xi_j|\le\tfrac12\mathfrak{d}_j\ \text{for all}\ j\le k\}$,
which is contained in $\mathfrak{P}_k$. For every $k<K$ the numbers $\omega_k$ and $v_k$ are
non-negative. Indeed, $|f_{k+1}|\le\omega_k$ holds on the non-empty set $\mathfrak{P}_k$. Further, the
family in which each of $\zeta_0,\dots,\zeta_k$ is the identity map $\zeta\mapsto\zeta$ consists of
holomorphic functions on $D(0,\varrho)$ with $|\zeta_j(\zeta)-\zeta|=0\le\tfrac13|\zeta|$, so the
hypothesis supplies for this family a function $\mathsf{q}_{k+1}$ with $|\mathsf{q}_{k+1}|\le v_k$ on the
non-empty disc $D(0,\varrho)$. Hence, by \eqref{5.3:eq-driven-flow-2}, $d_k\ge0$ for every $k<K$.

We prove by induction on $k\in\{0,\dots,K\}$ the following assertion $P(k)$: the functions
$\zeta_1,\dots,\zeta_k$ are defined by \eqref{5.3:eq-driven-flow-1} (with $\zeta_0(\zeta)=\zeta$), the
functions $\zeta_0,\dots,\zeta_k$ are holomorphic on $D(0,\varrho)$, and
for $\zeta\in D(0,\varrho)$ one has $|\zeta_{i+1}(\zeta)-\zeta_i(\zeta)|\le d_i|\zeta|$ for all $i<k$ and
$|\zeta_j(\zeta)-\zeta|\le\tfrac13|\zeta|$ for all $j\le k$. The assertion $P(0)$ holds, since
$\zeta_0(\zeta)=\zeta$ is holomorphic, there is no increment to bound, and $|\zeta_0-\zeta|=0$.
Assertion $P(K)$ contains all claims of the lemma.

Let $k<K$ and assume $P(k)$. By $P(k)$ the functions $\zeta_0,\dots,\zeta_k$ satisfy the hypothesis
under which $\mathsf{q}_{k+1}$ is given, so $\mathsf{q}_{k+1}$ is holomorphic on $D(0,\varrho)$ with
$|\mathsf{q}_{k+1}|\le v_k$.

\emph{The point $(\zeta_j(\zeta))_{j\le k}$ lies in the half polydisc.} Fix $\zeta\in D(0,\varrho)$ and set
$\xi:=(\zeta_j(\zeta))_{j\le k}$. For $j\le k$, $P(k)$ gives
\begin{equation}\label{5.3:eq-driven-flow-4}
|\xi_j|\le|\zeta|+|\zeta_j(\zeta)-\zeta|\le\tfrac43|\zeta|<\tfrac43\varrho
\le\tfrac12\mathfrak{d}_*(K-1)\le\tfrac12\mathfrak{d}_j ,
\end{equation}
where the penultimate inequality is the hypothesis $\tfrac83\varrho\le\mathfrak{d}_*(K-1)$, and the last
holds because $j\le k\le K-1$, so that $\mathfrak{d}_j$ is one of the numbers whose minimum is
$\mathfrak{d}_*(K-1)$. Hence $\xi\in\tfrac12\mathfrak{P}_k\subset\mathfrak{P}_k$. The map
$\zeta\mapsto(\zeta_j(\zeta))_{j\le k}$ is holomorphic from $D(0,\varrho)$ into $\mathfrak{P}_k$, and
$f_{k+1}$ is holomorphic on $\mathfrak{P}_k$. So the composite
$\zeta\mapsto f_{k+1}(\zeta_0(\zeta),\dots,\zeta_k(\zeta))$ is holomorphic on $D(0,\varrho)$, and
$\zeta_{k+1}$ of \eqref{5.3:eq-driven-flow-1} is defined and holomorphic on $D(0,\varrho)$.

\emph{The $f$-increment.} The set $\tfrac12\mathfrak{P}_k$ is convex, being a product of closed discs, and
it contains $0$ and $\xi$. Hence the segment $\{t\xi:0\le t\le1\}$ lies in
$\tfrac12\mathfrak{P}_k\subset\mathfrak{P}_k$, where $f_{k+1}$ is holomorphic. By the chain rule,
\begin{equation*}
f_{k+1}(\xi)-f_{k+1}(0)=\int_0^1\sum_{j\le k}\xi_j\,\partial_jf_{k+1}(t\xi)\,dt .
\end{equation*}
Therefore
\begin{equation}\label{5.3:eq-driven-flow-5}
|f_{k+1}(\xi)-f_{k+1}(0)|\le\max_{j\le k}|\xi_j|\cdot
\sup_{\eta\in\frac12\mathfrak{P}_k}\sum_{j\le k}|\partial_jf_{k+1}(\eta)| .
\end{equation}
Let $\eta\in\tfrac12\mathfrak{P}_k$. Since $\mathfrak{d}_j\ge\mathfrak{d}_*(k)$ for $j\le k$, the
$\ell^1$ gradient bound on a polydisc (Lemma~\ref{5.2:lem-polydisc-gradient}), applied to $f_{k+1}$ on
$\mathfrak{P}_k$ with sup bound $\omega_k$, gives
\begin{equation*}
\sum_{j\le k}|\partial_jf_{k+1}(\eta)|
\le\frac{1}{\mathfrak{d}_*(k)}\sum_{j\le k}\mathfrak{d}_j|\partial_jf_{k+1}(\eta)|
\le\frac43\,\frac{\omega_k}{\mathfrak{d}_*(k)} .
\end{equation*}
By \eqref{5.3:eq-driven-flow-4}, $\max_{j\le k}|\xi_j|\le\tfrac43|\zeta|$. Inserting both bounds into
\eqref{5.3:eq-driven-flow-5} yields
\begin{equation}\label{5.3:eq-driven-flow-6}
|f_{k+1}(\zeta_0(\zeta),\dots,\zeta_k(\zeta))-f_{k+1}(0)|
\le\frac43|\zeta|\cdot\frac43\,\frac{\omega_k}{\mathfrak{d}_*(k)}
=\frac{16}{9}\,\frac{\omega_k}{\mathfrak{d}_*(k)}\,|\zeta| .
\end{equation}

\emph{The driving increment.} The function $\mathsf{q}_{k+1}$ is holomorphic on $D(0,\varrho)$ and
bounded there by $v_k$. Part (a) of the bounds for a bounded analytic function on a disc
(Lemma~\ref{5.2:lem-disc-bounds}, \eqref{5.2:eq-disc-bounds-a}), applied with centre $0$ and radius
$\varrho$, gives
\begin{equation}\label{5.3:eq-driven-flow-7}
|\mathsf{q}_{k+1}(\zeta)-\mathsf{q}_{k+1}(0)|\le\frac{2v_k}{\varrho}\,|\zeta|
\qquad(\zeta\in D(0,\varrho)).
\end{equation}
The disc is the same $D(0,\varrho)$ at every step $k$, so the radius entering
\eqref{5.3:eq-driven-flow-7} is $\varrho$ for all $k<K$.

\emph{Summation.} By \eqref{5.3:eq-driven-flow-1}, \eqref{5.3:eq-driven-flow-6},
\eqref{5.3:eq-driven-flow-7} and the definition \eqref{5.3:eq-driven-flow-2},
\begin{equation*}
|\zeta_{k+1}(\zeta)-\zeta_k(\zeta)|
\le\Bigl(\frac{16}{9}\,\frac{\omega_k}{\mathfrak{d}_*(k)}+\frac{2v_k}{\varrho}\Bigr)|\zeta|
=d_k|\zeta| .
\end{equation*}
Combining this with the increment bounds for $i<k$ contained in $P(k)$, and using $d_i\ge0$,
\begin{equation*}
|\zeta_{k+1}(\zeta)-\zeta|
\le\sum_{i\le k}|\zeta_{i+1}(\zeta)-\zeta_i(\zeta)|
\le\Bigl(\sum_{i\le k}d_i\Bigr)|\zeta|
\le\Bigl(\sum_{i<K}d_i\Bigr)|\zeta|
\le\tfrac13|\zeta| .
\end{equation*}
Together with $P(k)$ this is $P(k+1)$. The induction is complete, and $P(K)$ gives
\eqref{5.3:eq-driven-flow-3} for every $k<K$.
\end{proof}
```

**D-F1 (filled: dimension-free gradient input).** Normalize \(f\) by its bound \(\omega>0\) and by its coordinate radii, obtaining \(g\) bounded by one on the unit polydisc. At \(a\), \(|a_j|\le1/2\), compose with \(\phi_{a_j}(t)=(t+a_j)/(1+\bar a_jt)\). For \(G=g\circ(\phi_{a_j})\), choose unit phases \(\lambda_j\) so that \(\lambda_j\partial_jG(0)\) have one argument. The one-variable function \(h(t)=G(\lambda_1t,\ldots,\lambda_nt)\) is bounded by one. Cauchy at radii tending to one gives
\[
\sum_j(1-|a_j|^2)|\partial_jg(a)|=|h'(0)|\le1.
\]
Thus \(\sum_jd_j|\partial_jf|\le4\omega/3\). If \(\omega=0\), \(f=0\) and the conclusion is immediate. This reproduces the account's polydisc-gradient route; summing separate coordinate estimates would incorrectly introduce a dimension factor.

**D-F2 (filled: driving quotient and induction).** The quotient \([q(\zeta)-q(0)]/\zeta\) has a removable singularity. On every circle of radius \(r'<\varrho\) its modulus is at most \(2v/r'\). Apply the maximum principle, then let \(r'\uparrow\varrho\), to get \(2v/\varrho\). The identity history is admissible, so the adaptive hypothesis supplies a driver even before induction; it also forces \(v_k\ge0\). At each constructed history the hypothesis supplies the next driver on the entire same disc. The half-polydisc inclusion is strict because \(|\zeta|<\varrho\), even when \(8\varrho/3=d_*(K-1)\). Segment integration and the preceding gradient estimate give \((4/3)(4/3)=16/9\), exactly the printed coefficient. Nonnegative \(d_k\) bound every prefix sum by the full sum. No driver is inferred from a value at zero.

## B3: conditional correlation assembly

### Named inputs and their standing

| Name | Account label/locus | Standing carried |
|---|---|---|
| C-admitted | 5.1:def-admitted-inputs, II:2083–2790 | All displayed source-free identities, configuration, own-box supplementary clause, operators, geometry, budgets, order of choice, floors and ceilings assumed exactly there. Published inputs remain named hypotheses in the register below. |
| C-boundary | 5.4:thm-finer-zone-sum, II:30857 onward; theorem invocation II:2808–2812 | Summation of boundary terms at finer zones assumed. This port does not prove its suppliers. |
| C-preparation | II:2386 onward and 2810–2812 | Source-free preparatory resummation geometry assumed; preparatory block window-data statement explicitly **proof outstanding**. W5 does not prove these antecedents. |
| C-B1 | 5.6:prop-polydisc-holomorphy, II:46131–46167 | **Outstanding**. Owner's ph lane is not yet done. Required for actual-term W6-H. |
| C-slots | Pure-step invocations II:25301–25326; 5.2:prop-complex-factor-step, II:3799 onward | Complex-slot bounds, admissible slot combinations, membership of histories and their holomorphic dependence assumed with their original domains. |
| C-frozen | II:25328–25343, 5.2:def-three-families | Frozen-integral proposition and valuation/remnant suppliers assumed, including the **whole-disc** bound on \(Q_\zeta\). |
| C-sites | 5.2:prf-induction-order, II:25480–25685 | Its eight inductive-step hypotheses retained. The proposition orders them; it does not prove those hypotheses. |
| C-reference | 5.1:def-reference-recursion, II:2029–2081; 5.3:prf-flow-reference, II:26531–26680 | Reference recursion and flow-constant definitions; the elementary implication is ported below. |
| C-one-loop | 4.2:lem-one-loop, CA-I:3901–3930 | **Cited input**, Balaban CMP 109 (1.22), Theorem 3; CMP 116 (2.41). Finite-part bound \(c_2\), not merely a formal coefficient. |
| C-Mfree | 5.10:prop-m-freeness, II:59574–59616; also 2.4:prop-m-freeness, CA-I:2239 | Explicitly **incomplete at (*)** for the companion random-walk kernel on local data. Preserve this even where the structural index says PROVED. |
| C-sixth | 5.11:lem-sixth-family, II:59618–59620 | Statement and proof **not written out**; retains W5-sixth's complex-extension use. |
| C-last | Nine hypotheses of 5.12:prf-torus-bound-proof, II:59645–59680, reproduced below | Sourced induction format; sourced real/complex CMP 119 (2.43)–(2.48) budget; complex weights (c); per-zone-cell bound and volume ceiling; flat modification (c); live gas and its two ceilings; complement count; unsourced floor; history labels and half payments. Each is assumed here with its original constants. |
| C-compact | 5.12:prop-subsequential-limits, II:59926–59978, assumption (2) | Equicontinuous multilinear compactness **and distributional extension** assumed as stated; proof below explains the subsequence use, not a new kernel theorem. |
| C-positive | 5.12:lem-limit-positivity, II:60089–60119 | Osterwalder–Seiler lattice reflection positivity and reflection invariance assumed. Conclusion is the stated polynomial in cumulants, off diagonals. |
| C-rank | 5.13:prop-sun-correlation, II:60180–60215 | **Proof outstanding** for \(N\ge3\). Required for the general-rank use, not needed for the \(N=2\) argument. |
| C-uniform-last | Theorem II:2960–2966 versus torus proof II:59770–59779, 59820–59821 | Uniformity in \(m\) of last-lattice constants is not supplied by the displayed proof. Retain as an additional hypothesis only for that literal uniformity claim; fixed-\(m\) limits do not require it. |

[P1](p1-base.md), [P3](p3-free.md), [P4](p4-operator.md) are **checked** inputs at the owner's stated scopes. [P5](p5-induction.md) is **ported**, supplying its A5/A6/A12/A13 implications, not all eight C-sites hypotheses. [port-pi](../port-pi.md) supplies the already-ported pointed irrelevance on its admitted E-family domain. [mu](../mu.md), [lrb](../lrb.md), [oc](../oc.md) are **proved and refereed** for 4.13, 4.4 and own-constant; [ui](../ui.md) is **checked** for 4.5. Their own assumptions and domain limitations remain attached. In particular P3's free analysis is not a proof of C-one-loop, and P4's checked conditional operator work does not close C-Mfree.

The account spreads the proof over the joint induction and the last-lattice argument. The following complete passages preserve that organization. A statement of assumed inductive steps is not an independent proof that all steps are available.

### Joint hypothesis, pure/frozen step, frozen averaging and large-field step

CA-II:25243–25478. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{definition}[The hypothesis of the joint induction]\label{5.2:def-joint-hypothesis}
Let $1\le k\le K$. All objects below live on the tori of
Definition~\ref{5.2:def-auxiliary-torus}, the physical torus and the auxiliary torus
$\mathbb{T}_{\mathrm{aux}}$. Here $r>0$ is the radius fixed earlier in this chapter. Write
$D(0,2r)$ for the disc of radius $2r$ about the origin in
the plane of the constant shift $\zeta$. We say that \emph{the hypothesis of the joint
induction holds at level $k$} if the following four clauses hold.
\begin{enumerate}
\item[(a)] The reference statement holds for every pair to which it applies whose two
entries are both at most $k$.
\item[(b)] For every $j\le k$, the running shift $\zeta_j$ and the marginal coefficient
$b_j(\zeta)=\beta[E^{(j)}_{\zeta}]$ of Definition~\ref{5.2:def-induction-format} are
analytic functions of $\zeta$ on $D(0,2r)$ and are real for real $\zeta$. For every
$\zeta\in D(0,2r)$ they satisfy
\begin{equation*}
|b_j(\zeta)-b_j(0)|\le d_{j-1}(2r)\,|\zeta|,
\qquad
|\zeta_j-\zeta|\le \tfrac13\,|\zeta| .
\end{equation*}
Here $d_{j-1}(2r)$ is the flow function $d_i(\varrho)$ of the reference recursion taken at the
index $i=j-1$ and at $\varrho=2r$; it is not the size $d_j(X)$ of a localisation domain.
\item[(c)] For every $j\le k$, the family $\mathsf{P}^{(j)}_{\xi}$ belongs to the ball fixed
for these families and is holomorphic on $\mathfrak{P}_{j-1}$. Moreover, with
$Q^{(j)}_{\zeta}=E^{(j)}_{\zeta}-P^{\flat(j)}_{\zeta}$,
\begin{equation*}
\|E^{(j)}_{\zeta}\|^{\flat}\le E_0,
\qquad
\|P^{\flat(j)}_{\zeta}\|^{\flat}\le E_0,
\qquad
\|Q^{(j)}_{\zeta}\|^{\flat}\le \mathfrak{m}_{j-1},
\end{equation*}
where $E_0$ is the bound fixed earlier in this chapter for these families.
\item[(d)] For all $\zeta$ with $|\zeta|<2r$, the induction hypothesis of the frozen
whole-lattice run at constant shift $\zeta$ holds at level $k$. In particular, for every
$j\le k$,
\begin{equation*}
\|R^{(j)}_{\zeta}\|^{\flat}\le g_j^{\kappa_0},
\end{equation*}
where $\kappa_0$ is the exponent fixed in that induction hypothesis.
If in addition $k\le K'$, then for every $w\in\mathcal{W}_k$ the induction hypothesis with
sources of Definition~\ref{5.2:def-induction-format} holds at level $k$ on the physical
torus, with
\begin{equation*}
|\zeta_j(p)|\le \tfrac43\,\sup|w|
\end{equation*}
for all $j\le k$ and all plaquettes $p$.
\end{enumerate}
At level $k=0$ the hypothesis of the joint induction is that the density is the sourced
density $\rho_0^w$ and that the running shift is $\zeta_0=w$; nothing else is required.
\end{definition}

\begin{proof}[Joint induction: the pure step and the frozen integral]
The passage from $(\mathrm{J}_k)$ to $(\mathrm{J}_{k+1})$, the hypothesis of the joint induction
of Definition~\ref{5.2:def-joint-hypothesis}, is carried out in several steps; the first two are
the pure step and the frozen whole-lattice integral. Throughout, $k<K$,
so that $g_j<g$ for every $j\le k$. For a complex number $c$ and a radius $a>0$ we write $D(c,a)$
for the open disc of radius $a$ about $c$.

\emph{The pure step.} Let $\xi=(\xi_j)\in\mathfrak{P}_k$. Then every slot combination $s_j$
lies in the disc $D(1,\sigma_0)$. For each $j\le k$ the complex-slot proposition bounds the family
$\mathsf{P}^{(j)}_{\xi}$ a priori,
\begin{equation*}
\|\mathsf{P}^{(j)}_{\xi}\|\le \tfrac12 E_0+E^{*}\le E_0 ,
\end{equation*}
and this bound does not depend on the inputs: the bound furnished by that proposition involves
no property of the families of the earlier levels. Consequently the tuple
$\mathsf{P}^{(\le k)}_{\xi}=(\mathsf{P}^{(j)}_{\xi})_{j\le k}$ lies in the ball $\mathbb{B}_k$ of
complex histories. Since $\mathsf{P}^{(\le k)}_{\xi}\in\mathbb{B}_k$, the family
$\mathsf{P}^{(k+1)}_{\xi}$ is defined. Each of its terms is holomorphic in each variable $\xi_j$
separately, the others being held fixed, and is locally bounded on $\mathfrak{P}_k$. By Osgood's
lemma (a locally bounded function of finitely many complex variables on an open set that is
holomorphic in each variable separately is holomorphic), each term of $\mathsf{P}^{(k+1)}_{\xi}$
is jointly holomorphic in $\xi$ on $\mathfrak{P}_k$.

The marginal coefficient $f_{k+1}=\beta[\Phi_{k+1}]$ of the one-step family $\Phi_{k+1}$ is
therefore holomorphic on $\mathfrak{P}_k$, and clause~(c) of the complex-slot proposition gives
\begin{equation}\label{5.2:eq-pure-step-a}
|f_{k+1}|\le C_\beta\,\mathrm{e}_k .
\end{equation}
Finally, by the slot lemma, the family $\mathsf{P}^{(k+1)}_{\xi}$ so obtained belongs to the ball;
this is the membership statement required in clause~(c) of $(\mathrm{J}_{k+1})$.

\emph{The frozen whole-lattice integral (the bridge).} The construction of the frozen integral at
level $k+1$ uses only data of levels at most $k$, namely: the cut $T_k$; the families
$(E^{(j)}_{\zeta})_{j\le k}$; the remainders $(R^{(j)}_{\zeta})_{j\le k_1(k)}$, where $k_1(k)<k$;
and the bound $|\zeta_k|\le\frac83 r$ on the running shift. All of these are contained in
$(\mathrm{J}_k)$; for the last three the relevant clauses are as follows: the families
$E^{(j)}_{\zeta}$, $j\le k$, and their bounds are those of clause~(c) of
Definition~\ref{5.2:def-joint-hypothesis}; the remainders $R^{(j)}_{\zeta}$ with $j\le k_1(k)$ are
among those of clause~(d), since $k_1(k)<k$; and clause~(b) gives $|\zeta_k-\zeta|\le\frac13|\zeta|$
for $\zeta\in D(0,2r)$, whence
\begin{equation*}
|\zeta_k|\le|\zeta|+|\zeta_k-\zeta|\le\tfrac43|\zeta|\le\tfrac83\,r .
\end{equation*}
With these data the frozen-integral proposition produces the family $E^{(k+1)}_{\zeta}$ on the
radii $\hat\alpha_k$. The valuation statement is then applied with
\begin{equation*}
\mathsf{q}_{k+1}:=\beta\bigl[Q^{(k+1)}_{\zeta}\bigr],
\end{equation*}
which satisfies $|\mathsf{q}_{k+1}|\le v_k$ on $D(0,2r)$.

The remaining clauses of $(\mathrm{J}_{k+1})$ are established in the steps that follow.
\end{proof}

\medskip
\noindent\textit{Joint induction: the frozen averaging step.}
We continue the passage from level $k$ to level $k+1$, $k<K$, of the joint induction
(see the part on the pure step and the frozen integral above), and now
treat the operation $\mathbf{T}$ of this step together
with its domains, and the renormalisation that follows it.

The operation $\mathbf{T}$ is applied in Ba{\l}aban's form, through the decompositions
\cite[(3.2), (3.3), (3.16)]{B-CMP119}, none of which involves the sources $z$. These
decompositions are followed by the exact refinement of the averaging step, and the step is then
taken with its parameter $a_k$.

At the sites of the operation $\mathbf{T}$ four lemmas, used together with the budget inequality
for the constant $C_{\sharp}$ of this chapter, give the three output families at level $k+1$. The
four lemmas are:
\begin{itemize}
\item the amplitude lemma;
\item the complex-parameter lemma;
\item the summation lemma;
\item the flat summation lemma.
\end{itemize}
The three families are $E^{(k+1)}$, $R''^{(k+1)}$ and $\mathbf{B}^{(k+1)}$. The last is kept
as a family of stored terms
\begin{equation}\label{5.2:eq-frozen-averaging-1}
  \sum_{\mathcal{S}} \mathbf{B}^{(k+1)}(X,\mathcal{S}),
\end{equation}
which carry the datum $A^{\flat}$ and satisfy the weighted bound of the flat boundary-term
corollary. All three families are defined on Ba{\l}aban's enlarged
spaces $\tilde{U}$, and they decay at the rate $\mathsf{r}(\delta)\kappa$, where
\begin{equation}\label{5.2:eq-frozen-averaging-2}
  \mathsf{r}(\delta)\kappa \;\ge\; (1+4\beta_s)\kappa \;=\; 2\kappa .
\end{equation}

The rate in \eqref{5.2:eq-frozen-averaging-2} is supplied by the threshold lemma for the decay
fraction $\delta$. That lemma reads \cite[(2.41)]{B-CMP116} at $\delta\le\delta_J(L)$. The
inequality in \eqref{5.2:eq-frozen-averaging-2} holds for every
$\delta\in\,]0,\delta_J(L)]$. Indeed,
$\delta\le\delta_J(L)=(1-4/L)/10$ gives $1-10\delta\ge 4/L$. Hence
\begin{equation*}
  \mathsf{r}(\delta)=\frac{(1-10\delta)L}{2}\ge 2 .
\end{equation*}
Moreover $\beta_s=1/4$, so that $(1+4\beta_s)\kappa=2\kappa$. The members of the one-loop
family $L^{(k+1)}$ enter with the decay rate $\delta_0 M$, and $\delta_0 M\ge 2\kappa$.

Let $\Lambda_{k+1}$ be the region so denoted at level $k+1$ in the decompositions
\cite[(3.2), (3.3), (3.16)]{B-CMP119}. The terms localised in domains $X\subset\Lambda_{k+1}$
``do not depend on
$\Lambda_{k+1}$, and coincide with the corresponding terms arising from the expressions
defined on the whole lattice'' \cite{B-CMP119}. These terms are therefore the whole-lattice
terms already constructed in the frozen-integral part of the induction step
above.

The vacuum values of the output families are collected into the constant $e^{(k+1)}$. The
marginal part is then removed as in \cite{B-CMP119}, ``subtracting
$\beta_{k+1}(g_k)A(\varphi_{k+1},U_{k+1})$'', with $\beta_{k+1}(g_k)$ replaced by the complex
coupling increment $b_{k+1}(\zeta)$ of the flow step
(the part on the coupling increment and the reference coupling, below).
Here $A(\varphi_{k+1},U_{k+1})$ is the action of
the level-$(k+1)$ configuration in Ba{\l}aban's notation.
After the subtraction, the weight multiplying the action is
\begin{equation}\label{5.2:eq-frozen-averaging-3}
  x_{k+1}(\cdot)-\zeta_{k+1},
\end{equation}
with $x_{k+1}$ and the running shift $\zeta_{k+1}$ as in the flow step.

\begin{remark}[Joint induction: the large-field step]\label{5.2:prf-large-field-step}
We apply the $\mathbf{R}$-operation at level $k+1$, in both its frozen and its local readings,
to the density obtained from the averaging step. Specifically, we apply at level $k+1$:

\begin{itemize}
\item the proposition describing the $\mathbf{R}$-operation at complex sources, of which clauses
(a) and (e) are used below;
\item the lemma that accompanies that proposition.
\end{itemize}

The averaging step in question is either the frozen averaging step or the local averaging step under sources
(\ref{5.3:prf-local-averaging}).

Clause (e) of that proposition divides the terms produced by the $\mathbf{R}$-operation into two
groups: the first group consists of the $\mathbf{R}$-born boundary terms $\mathbf{B}'^{(k+1)}$,
and the second group of the remaining terms produced by the $\mathbf{R}$-operation.

\emph{The first group.}
Clause (e) returns the first group, the terms $\mathbf{B}'^{(k+1)}$, into $\mathbf{B}^w$. Their
bound is the relative form of clause $(\mathrm{d})'(\alpha)$ of the induction format
(Definition~\ref{5.2:def-induction-format}), that is, \eqref{5.2:eq-induction-format-b}.
This is exactly the bound that clause (e) displays. This relative bound is supplied
by the relative complex bound for the large-field operations at level $k+1$; the propagation
lemma of the present induction derives it, through the five propositions on which that lemma
rests, from that bound at level $k$ and the joint induction
statement at level $k$. Hence the format is reproduced at level $k+1$ exactly as written, in
its relative form, that is, with the length in \cite[(2.42)]{B-CMP119} read as the relative size
of \cite[(1.67)]{B-CMP122b}, and not with the plain length of \cite[(2.42)]{B-CMP119}. Wherever
Ba{\l}aban's bounds are invoked in this step, they are his printed bounds, with the single change
that in \cite[(2.42)]{B-CMP119} the length is measured by the relative size of
\cite[(1.67)]{B-CMP122b}.

\emph{The second group.}
Clause (e) returns the second group into $\mathbf{R}^w$, bounded in the form of
\cite[(2.30)--(2.32)]{B-CMP119}.

\emph{Orbit data.}
Every new term of $\mathbf{B}$-type is filed together with its orbit datum, as clause
$(\mathrm{d})'(\gamma)$ of the format requires. In the two averaging steps this datum was supplied by
clause (d) of the corollary on boundary terms at complex sources. In the present step it is
supplied as follows:
\begin{itemize}
\item at the preparatory stages, by the corresponding corollary for the preparatory boundary
terms at complex sources;
\item at the localisation site, by clause (b) of the proposition on the bracket terms and its
corollary at complex sources.
\end{itemize}

\emph{Arrests.}
Clause (a) of the proposition on the $\mathbf{R}$-operation, together with clause
$(\mathrm{d})'(\beta)$ of the format, carries the arrested left-overs of every live arrest unchanged
from level $k$ to level $k+1$. An arrest $\mathfrak{a}$ may also be made at the present step,
because a chain is finished early or is excluded. Its frozen terms $\mathfrak{F}(\mathfrak{a})$
are then filed into clause $(\mathrm{d})'(\beta)$ of the format. This filing is made by the filing rule
for arrests, read under the standing domain convention.

\emph{Conclusion.}
All terms produced by the $\mathbf{R}$-operation at level $k+1$ have now been placed:
\begin{itemize}
\item the second group in $\mathbf{R}^w$, with the bound of \cite[(2.30)--(2.32)]{B-CMP119};
\item the first group in $\mathbf{B}^w$, with the relative bound
\eqref{5.2:eq-induction-format-b} and with its orbit datum;
\item the arrested left-overs, old and new, in clause $(\mathrm{d})'(\beta)$.
\end{itemize}
The format of Definition~\ref{5.2:def-induction-format} therefore holds at level $k+1$. With it
the joint induction statement holds at level $k+1$, which completes the induction step.
\end{remark}
```

### Order of the joint induction and its conclusion

CA-II:25480–25685. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proposition}[Order of the joint induction and its conclusion]
\label{5.2:prf-induction-order}
Let $(J_k)$, $0\le k\le K$, be the joint hypothesis of
Definition~\ref{5.2:def-joint-hypothesis}. Consider the following statements:
\begin{enumerate}
\item the correlation theorem, whose inductive step is the passage from $(J_k)$ to $(J_{k+1})$
carried out in the pure step and the frozen integral, the coupling
increment and the reference coupling (\ref{5.3:prf-flow-reference}), the frozen averaging step, the local averaging step under sources
(\ref{5.3:prf-local-averaging}) and the large-field step (\ref{5.2:prf-large-field-step}) of the
joint induction;
\item the collar-payment statement of the large-field step;
\item the relative bound for the chain terms $\mathbb{C}^{(n)}_k$;
\item the closing lemma at the localisation site, together with its version in the shift
variable $\zeta$;
\item the tube statement, in its form part (the tube-form proposition) and in its value part, the
two-point bound supplied by its base theorem;
\item the group bound at the preparatory site;
\item the lemma on plain units inside the large-field region;
\item Lemma~\ref{5.2:lem-exterior-pieces}, on the pieces of units whose label leaves the large-field
region.
\end{enumerate}
Assume, as hypotheses, the inductive steps of these statements: for each of them, at each step $k$
and each site of that step, the statement at that site is derived from the inputs named
where that statement is proved; these inputs are recalled, position by position, in the proof below.
We write $(g)_{k-1}$ and $(g)_k$ for the positions at which step $k$ opens and closes,
$(\mathrm{T})$ for the site of the averaging steps, $\mathcal{I}^{\mathbb{C}}_k$ for the position
of the complex inductive bound at scale $k$, that is, of the inductive hypothesis of the relative
bound for the chain terms at step $k$, $(\mathrm{P})$ and
$(\mathrm{L})$ for the preparatory and the localisation site of the large-field step, and $(c)$ for
the position, after $(\mathrm{P})$, that closes the part of step $k$ read by the closing lemma.
Then these statements hold together, by one induction on pairs $(\text{step},\text{site})$, in which
step $k$ runs through the positions in the order
\begin{equation}\label{5.2:eq-induction-order-a}
(g)_{k-1}\;\to\;(\mathrm{T})\;\to\;\mathcal{I}^{\mathbb{C}}_k\;\to\;(\mathrm{P})\;\to\;(c)
\;\to\;(\mathrm{L})\;\to\;(g)_k .
\end{equation}
Each item uses only items preceding it in \eqref{5.2:eq-induction-order-a} at the same step and
items of earlier steps. In particular the induction contains no circle. The induction ends with
$(J_K)$, and $(J_K)$ implies the reference-coupling clause, the running-shift statement and the
clause on $N_K$ of the correlation theorem.
\end{proposition}

\begin{proof}
The positions in \eqref{5.2:eq-induction-order-a} are those named in the statement. The site
$(\mathrm{T})$ is the site of the averaging steps, frozen (the frozen averaging step) and local (the local averaging step under sources,
\ref{5.3:prf-local-averaging}). The sites $(\mathrm{P})$ and $(\mathrm{L})$ are the two sites of the
large-field step (\ref{5.2:prf-large-field-step}). We list, position by position, what each item
uses, and check that nothing is used before it is established.

\emph{The flow and the remainders.} The running-shift statement at levels $\le j$ is used at the
large-field step of level $j$ to produce $R^{(j)}_\zeta$. The remainder $R^{(j)}_\zeta$ enters the
running-shift statement at level $k+1$ only for $k_1(k)\ge j$, through the frozen integral of the
pure step. Thus the flow at level $k+1$ uses remainders of levels already
completed, and there is no circle.

\emph{Internal orders.} The order \eqref{5.2:eq-induction-order-a} is the order in which the
collar-payment statement lists its items, and the ordering lemma of that statement shows that this
list contains no forward pointer. The items of the relative bound for the chain terms are used in
that bound's own ordered list; the first of them includes the tube statement at the site where the
large-field component is created.

\emph{The site $(\mathrm{P})$.} At $(\mathrm{P})$ the part of the correlation theorem attached to
this site uses the following inputs:
\begin{itemize}
\item the field-free scaffold and counting lemmas of the relative bound for the chain terms, namely
the flat lemma, the resummation lemma of the preparatory stage with its five clauses, the localised
star lemma, a further counting lemma, the window lemma and the anchoring lemma for all preparatory
terms;
\item the preparatory-site corollary of the collar-payment statement, with its accompanying bound;
\item the group bound at the preparatory site, for the groups it concerns.
\end{itemize}
The scaffold and counting lemmas are used in one direction only: no statement of the correlation
theorem is an input of theirs. In the other direction, the relative bound for the chain terms uses,
among the parts of the correlation theorem, only those lettered (C) and the small-field parts. It
does not use the conclusion reached at $(\mathrm{P})$.

\emph{The site $(\mathrm{L})$.} The closing lemma uses the items established up to position $(c)$ of
\eqref{5.2:eq-induction-order-a}. At $(\mathrm{L})$ of step $k$ its inputs are:
\begin{itemize}
\item clause (a) of $(J_k)$, i.e.\ the reference-coupling clause for pairs $\le k$;
\item the sourced inductive hypothesis for the chain terms at level $k$;
\item the containment statement;
\item the constant $\sigma_0$ of the relative bound for the chain terms;
\item clause (g) of the geometry, which follows from the statement on nested regions;
\item the two statements on the sources $w$;
\item two further lemmas established before position $(c)$ of \eqref{5.2:eq-induction-order-a}.
\end{itemize}
It uses no length, label or sum of step $k$, no value bound of the tube statement, no
$\mathbf{R}'^{(k)}$ and no $\alpha^{\sharp}(k)$. The off-diagonal rider and the half-power statement
use the same inputs, together with the supplementary statement on clause (a).

\emph{The plain-unit lemma.} The lemma on plain units inside the large-field region uses the closing
lemma and field-free counting, and returns its member of the pre-filing family.

\emph{The exterior lemma: inputs.} Lemma~\ref{5.2:lem-exterior-pieces} uses:
\begin{itemize}
\item the two statements on the sources;
\item clause (f) of the geometry;
\item the sum, which carries no field;
\item the sizes, and only the sizes, supplied by the filing step;
\item the stored bound of the amplitude lemma;
\item through one of the displayed bounds of the lemma on plain units, the containment statement
read at the auxiliary consumer term $\mathfrak{E}^{\oplus}_v=\mathbb{C}^{(N)}_k(Y(\mathrm{lab}_1))$
inside $Y_4$;
\item the inheritance statement, its corollary and its claim, in clause ($\beta$);
\item the arrest statements (0)--(2) and (5) on foreign live pieces;
\item the bounds of the off-diagonal rider in the case $b=0$ of its index $b\ge 0$, for the compact
pointed pieces only;
\item clause (ii)($\alpha$) of the collar-payment statement at the site $(\mathrm{L})$;
\item the bound \eqref{5.2:eq-plain-fine-units-a} on plain units finer than a cell;
\item the third of the auxiliary bounds of this chapter;
\item the recursion lemma for the correlation theorem.
\end{itemize}
The long pointed pieces, in the two domain classes of the correlation theorem where they occur, use
no item of the rider. For them the long-piece bound at $\mathsf{t}=0$ and
the two inequalities for $\theta'$ are used instead.

\emph{The exterior lemma: the recursion lemma and the output.} The recursion lemma uses:
\begin{itemize}
\item the layer objects $\mathbb{H}_s$ and $\mathcal{J}^{\sharp}_s[\chi]$, with the input bounds of
each layer $s$ and their localisation under sources, all of which lie upstream of every
part of the correlation theorem;
\item the supplementary statement on clause (a), read at clause (a) of $(J_k)$;
\item the arrest geometry;
\item the geometry and the cell structure, which carry no field.
\end{itemize}
It does not use the base theorem of the two-point bound. That theorem rests, through its part (D),
on the exterior carrier bound, so its use here would be a circle. Neither
Lemma~\ref{5.2:lem-exterior-pieces} nor the recursion lemma uses any length, value bound,
$\mathbf{R}'^{(k)}$ or $\alpha^{\sharp}(k)$ of step $k$. Lemma~\ref{5.2:lem-exterior-pieces} returns
$\varepsilon^{\mathrm{ext}}$.

\emph{The operations $\mathbf{R}$ and $\mathbf{B}$.} Clauses (c)--(e) of the proposition on the
operation $\mathbf{R}$ use the pre-filing family with its six members. The proposition on the terms
$\mathbf{B}$ returns the newly born terms of the relative bound for the chain terms at step $k+1$.

\emph{The tube statement: its two parts.} Its form part is the tube-form proposition, whose input is
a theorem that is not among the statements listed in the proposition. Its value part is the
two-point bound supplied by its base theorem. The
base theorem has its own position within the site $(\mathrm{L})$ of step $k$, after the
lists compiled at that site. It uses:
\begin{itemize}
\item the splitting, rim and totalisation statements and the carrier-pair statement;
\item the pointed version in $\zeta$ of the closing lemma;
\item the Wilson-density rider;
\item the nesting statement, which is obtained from its ingredients (A)--(H), with the statement on
the terms $\mathbf{C}_k$ entering at its line (i).
\end{itemize}

\emph{The tube statement: where it is used and paid.} Both parts are used at the localisation site
where the component is created, and at every later site $(\mathrm{T})$, $(\mathrm{P})$,
$(\mathrm{L})$ of the component's life. At every later site the value is paid in cells, measured in
$d^{\wedge}$, through the collar belonging to the region $(Y,m)$ that carries it, by the
collar-payment statement.

\emph{Conclusion of the first part.} In every case above, an item of step $k$ uses only items
preceding it in \eqref{5.2:eq-induction-order-a} and items of steps $<k$. The pairs
$(\text{step},\text{site})$ ordered lexicographically, with the sites of a step ordered by
\eqref{5.2:eq-induction-order-a}, are well ordered. The inductive step of the correlation theorem,
the passage from $(J_k)$ to $(J_{k+1})$ carried out in the statements listed in the first item of
the proposition, is placed
in the same order as follows: the averaging steps occupy $(\mathrm{T})$ and the large-field step
occupies $(\mathrm{P})$ and $(\mathrm{L})$, while the pure step, the frozen integral and the coupling
increment use only remainders of levels already completed, as shown in the paragraph on the flow.
Therefore the induction
closes, every statement of the list holds at every step $k\le K$, and the induction ends with
$(J_K)$. From $(J_K)$ we now deduce the three clauses of the correlation theorem.

\emph{The reference-coupling clause.} Clause (a) of $(J_k)$, valid at every step $k$ reached by the
induction, makes the first passage $K$ finite. The inequality
$x_{K+1}\le X$ gives $x_K\le X+b_+$. For $\varrho\in[r,2r]$ the sum $\sum_{k<K}d_k(\varrho)$ is
estimated by the summability condition on the flow constants $d_k(\varrho)$, applied with the lower
bound
\begin{equation}\label{5.2:eq-induction-order-1}
x_k\;\ge\;x_K+\lambda(K-k)-2c_2,\qquad 0\le k<K .
\end{equation}
These facts, together with clause (a) of $(J_K)$, give the reference-coupling clause.

\emph{The running-shift statement and the clause on $N_K$: the Cauchy estimate.} For $0\le k<K$ put
$h_k:=b_{k+1}-b_{k+1}(0)$. By clause (b) of $(J_K)$, applied with $j=k+1\le K$, the function $h_k$ is
analytic on $D(0,2r)$, real on reals, and $h_k(0)=0$. On $D(0,2r)$ it satisfies
\begin{equation*}
|h_k(\zeta)|\;\le\;d_k(2r)\,|\zeta|\;\le\;2r\,d_k(2r).
\end{equation*}
Let $\zeta\in\bar D(0,r)$ and $0<r'<r$. The circle of radius $r'$ about $\zeta$ lies in $D(0,2r)$, so
Cauchy's estimate gives $|h_k'(\zeta)|\le 2r\,d_k(2r)/r'$. Letting $r'\to r$ yields
\begin{equation}\label{5.2:eq-induction-order-2}
|h_k'(\zeta)|\;\le\;2\,d_k(2r),\qquad \zeta\in\bar D(0,r).
\end{equation}
Clause (b) of $(J_K)$ together with \eqref{5.2:eq-induction-order-2} gives the running-shift
statement.

\emph{The running-shift statement and the clause on $N_K$: the Schwarz lemma.} Since $h_k(0)=0$ and
$|h_k|\le 2r\,d_k(2r)$ on $D(0,2r)$, the Schwarz lemma gives $|h_k'(0)|\le d_k(2r)$. The quantity
$N_K$ of the correlation theorem satisfies
\begin{equation}\label{5.2:eq-induction-order-3}
N_K-1\;=\;\sum_{0\le k<K}h_k'(0).
\end{equation}
Each $h_k$ is real on reals, so each $h_k'(0)$ is real. Hence $N_K$ is real, and by the triangle
inequality
\begin{equation*}
|N_K-1|\;\le\;\sum_{0\le k<K}|h_k'(0)|\;\le\;\sum_{0\le k<K}d_k(2r).
\end{equation*}
The last sum is the sum estimated above at $\varrho=2r$. The reality of $N_K$ and the last display
give the clause on $N_K$.
\end{proof}
```

**C-F1 (filled: logical order and frozen data).** The order is
\[
(g)_{k-1}\to T\to\mathcal I_k^{\mathbb C}\to P\to c\to L\to(g)_k.
\]
Lexicographic induction on step and this finite ordered list is well-founded: each premise must either have smaller step or an earlier position at the same step, as the quoted proposition specifies. The eight C-sites hypotheses are indispensable. No simultaneous assertion of their conclusions replaces them. The pure history bound \(E_0/2+E^*\le E_0\) gives admission before evaluating the next pure step. The frozen step reads \(E_j\) only for \(j\le k\), \(R_j\) only for \(j\le k_1(k)<k\), and \(|\zeta_k|\le(4/3)2r\), all from the old joint hypothesis. This is precisely why the coupling increment can be extracted before defining the next radii.

The preparatory and localisation consumers retain W5, W6/B1, collar and relative-chain inputs at their respective sites. A decay bound on a plain length is not a bound on a relative chain length. Frozen arrested pieces stay at their own scales. These are admission requirements of C-sites, not extra conclusions of its ordering proof.

### Coupling increment and reference coupling

CA-II:26531–26680. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Joint induction: the coupling increment and the reference coupling]
\label{5.3:prf-flow-reference}
We continue the passage from the hypothesis of the joint induction at level $k$
(Definition~\ref{5.2:def-joint-hypothesis}) to the same hypothesis at level $k+1$. This passage
begins with the pure step and the frozen integral, treated above. As there, $k<K$, so that
$g_j<g$ for $j\le k$, that is, $x_j>X=g^{-2}$.

\emph{The increment as a function of the shift.} The coefficient $b_{k+1}$ of the induction
format (Definition~\ref{5.2:def-induction-format}) is decomposed as
\begin{equation}\label{5.3:eq-flow-reference-1}
b_{k+1}=\beta^0_{k+1}+f_{k+1}(\zeta_0,\dots,\zeta_k)+\mathsf{q}_{k+1}.
\end{equation}
We apply the flow lemma, which bounds the dependence on the shift of an increment of the form
\eqref{5.3:eq-flow-reference-1}, to $b_{k+1}$, with the
following data:
\begin{itemize}
\item the polydisc radii $\mathfrak{d}_j=\sigma_0 x_j$; the quantity $\mathfrak{d}_*(k)$ that the
flow lemma forms from them satisfies $\mathfrak{d}_*(k)\ge\sigma_0 y_k$, where
$\sigma_0$ is the radius of the discs $D(1,\sigma_0)$ of the pure step and $y_k$ is the constant of
Definition~\ref{5.1:def-reference-recursion};
\item the sup bound furnished by the pure-step bound \eqref{5.2:eq-pure-step-a},
\begin{equation*}
\omega_k=C_\beta\mathrm{e}_k\le C_\beta\,\mathrm{e}\bigl(y_k^{-1/2}\bigr),
\end{equation*}
in which $\mathrm{e}(\cdot)$ is the function of the coupling of
Definition~\ref{5.1:not-coupling-functions};
\item the driving term $\mathsf{q}_{k+1}=\beta[Q^{(k+1)}_\zeta]$, with $Q^{(k+1)}_\zeta$ the family of
Definition~\ref{5.2:def-three-families}, whose modulus at $\zeta=0$ is bounded by the remainder
constant $v_k$ of Definition~\ref{5.1:def-reference-recursion};
\item an arbitrary $\varrho\in[r,2r]$.
\end{itemize}
The flow lemma requires $\tfrac{8}{3}\cdot 2r\le\sigma_0 g^{-2}$. This inequality is one of the
conditions on $g$ collected in the definition of $\gamma_J$; it holds for $g\le\gamma_J$. With
these data the flow lemma gives
\begin{equation}\label{5.3:eq-flow-reference-2}
|b_{k+1}(\zeta)-b_{k+1}(0)|\le d_k(\varrho)\,|\zeta|,\qquad \zeta\in D(0,\varrho).
\end{equation}

\emph{The running shift.} Clause (a) of the hypothesis of the joint induction controls the
reference couplings for pairs of levels at most $k$. From this clause and the summability
condition on the Lipschitz constants $d_j(\varrho)$ (the constants of
Definition~\ref{5.1:def-reference-recursion}), applied with the inequality $x_k>X$, we obtain
$\sum_{j\le k}d_j(\varrho)\le\tfrac13$.

In the recursion of the flow lemma the shift advances by the increment,
$\zeta_l-\zeta_{l-1}=b_l(\zeta)-b_l(0)$ for $1\le l\le k+1$, and $\zeta_0=\zeta$ by the
hypothesis of the joint induction at level zero. Summing these relations,
\begin{equation*}
\zeta_{k+1}-\zeta=\sum_{l=1}^{k+1}\bigl(b_l(\zeta)-b_l(0)\bigr).
\end{equation*}
Each summand obeys $|b_l(\zeta)-b_l(0)|\le d_{l-1}(\varrho)|\zeta|$: for $l=k+1$ this is
\eqref{5.3:eq-flow-reference-2}, and for $l\le k$ it is the same bound obtained at the earlier
steps. Hence
\begin{equation}\label{5.3:eq-flow-reference-3}
|\zeta_{k+1}-\zeta|\le\sum_{j\le k}d_j(\varrho)\,|\zeta|\le\tfrac13|\zeta|,
\qquad \zeta\in D(0,\varrho).
\end{equation}

\emph{The increment at zero shift and the reference recursion.} Set $\zeta=0$ in
\eqref{5.3:eq-flow-reference-1}. The term $f_{k+1}$ is bounded by $C_\beta\mathrm{e}_k$, by the
pure-step bound. The remaining term $\mathsf{q}_{k+1}$ is bounded in modulus by $v_k$, as
recorded among the data of the flow lemma above. Therefore
\begin{equation}\label{5.3:eq-flow-reference-4}
|b_{k+1}(0)-\beta^0_{k+1}|\le C_\beta\mathrm{e}_k+v_k\le\lambda,
\end{equation}
where $\lambda=c_0/2$ is the step constant of Definition~\ref{5.1:def-reference-recursion} (not to
be confused with $\underline{\lambda}=c_0/4$), and the last inequality is again one of the
conditions on $g$ collected in the definition of $\gamma_J$, and holds for $g\le\gamma_J$. We define
\begin{equation*}
x_{k+1}:=x_k-b_{k+1}(0).
\end{equation*}
Unwinding this recursion gives, for $i\le k$,
\begin{equation*}
x_i-x_{k+1}=\sum_{l=i+1}^{k+1}b_l(0).
\end{equation*}
We now use the statement on the sums of the one-loop coefficients, in the form
\begin{equation*}
\sum_{l=i+1}^{k+1}\beta^0_l=(k+1-i)c_0+s_i-s_{k+1},\qquad |s_i-s_{k+1}|\le 2c_2,
\end{equation*}
where $s_i$ denotes the remainder of that statement at level $i$. The $k+1-i$ differences
$b_l(0)-\beta^0_l$ are each at most $\lambda$ in modulus: for $l=k+1$ this is
\eqref{5.3:eq-flow-reference-4}, and for $l\le k$ it is the same bound obtained at the earlier
steps. Since $c_0=2\lambda$, the sum of $(k+1-i)c_0$ and of these differences lies in
$[\lambda(k+1-i),3\lambda(k+1-i)]$, and adding $s_i-s_{k+1}$ widens this interval by at most
$2c_2$ on each side. The result is
\begin{equation}\label{5.3:eq-flow-reference-a}
\begin{split}
x_i-x_{k+1}&=(k+1-i)c_0+s_i-s_{k+1}+\sum_{l=i+1}^{k+1}\bigl(b_l(0)-\beta^0_l\bigr)\\
&\in\bigl[\lambda(k+1-i)-2c_2,\ 3\lambda(k+1-i)+2c_2\bigr].
\end{split}
\end{equation}
Together with clause (a) at level $k$, \eqref{5.3:eq-flow-reference-a} gives the reference
comparisons for all pairs of levels at most $k+1$, which is clause (a) of the hypothesis of the
joint induction at level $k+1$.

\emph{The radii at level $k+1$.} With $x_{k+1}$ in hand, the quantities $g_{k+1}$,
$\check{R}_{k+1}$, $\varepsilon_{k+1}$ and $\alpha_{\cdot,k+1}$ are defined; here
$\check{R}_{k+1}=R(\min_{i\le k+1}x_i)$, where $R(x)$ is the least power of $L$ not below
$(\log x)^{r_{\mathrm{pr}}}$, $\varepsilon_{k+1}$ is the radius of the orbit data carried by the
induction format at level $k+1$, and $\alpha_{\cdot,k+1}=\alpha_\cdot(g_{k+1})$ are the
coupling-dependent radii at level $k+1$ of Definition~\ref{5.1:def-analyticity-spaces}. The
case $i=k$ of
\eqref{5.3:eq-flow-reference-a} gives $x_k-x_{k+1}\le 3\lambda+2c_2=b_+$, that is,
$x_{k+1}\ge x_k-b_+$. This gives
\begin{equation*}
\alpha_\cdot(g_{k+1})\le\bigl(1+b_+g^2\bigr)^{1/2}\bigl(1+o(1)\bigr)\,\alpha_\cdot(g_k),
\end{equation*}
where $o(1)$ denotes a quantity tending to zero as $g\to0$, uniformly in $k$,
and hence, for $g\le\gamma_J$,
\begin{equation}\label{5.3:eq-flow-reference-5}
(1+\beta_{\mathrm{pr}})\,\alpha_{\cdot,k+1}\le(1+\beta_s)\,\alpha_{\cdot,k+1}
\le(1+2\beta_s)\,\alpha_\cdot(g_k)=\hat\alpha_k .
\end{equation}
In \eqref{5.3:eq-flow-reference-5}:
\begin{itemize}
\item the first inequality holds because Ba{\l}aban's enlargement of the spaces is by the fraction
$\beta_{\mathrm{pr}}=1/5$, and $\beta_{\mathrm{pr}}\le\beta_s=1/4$, as in part~(ii) of
Lemma~\ref{5.2:lem-enlargement-fractions} (enlargement by one quarter against Ba{\l}aban's one
fifth);
\item the second inequality holds because
\begin{equation*}
(1+\beta_s)\bigl(1+b_+g^2\bigr)^{1/2}\bigl(1+o(1)\bigr)\le 1+2\beta_s
\end{equation*}
once $g$ is below the ceiling $\gamma_J$.
\end{itemize}
Consequently the families bounded on the spaces of radii $\hat\alpha_k$ are bounded, by
restriction, on Ba{\l}aban's enlarged spaces after the operation $\mathbf{T}$ at level $k+1$
\cite[\S2]{B-CMP119}; the later steps of the induction read them there.

The definition of $g_{k+1}$ involves no circularity: $b_{k+1}(0)$ is the value of the functional
$\beta[\cdot]$ on the family $E^{(k+1)}_0$ of the induction format
(Definition~\ref{5.2:def-induction-format}), and $\beta[\cdot]$ is a derivative at the trivial
configuration; so $b_{k+1}(0)$ is determined independently of the radii $\alpha_{\cdot,k+1}$,
which are defined from $x_{k+1}$ only afterwards.

\emph{The background hypothesis at level $k+1$.} The items of the background hypothesis at level
$k+1$ that concern the admissible backgrounds and their comb-gauge data involve the couplings
through two kinds of input only. The
first is $g_j\le\gamma$. The second is the comparisons \cite[(2.6)--(2.9)]{B-CMP119}, whose
constants, printed there $\beta_0$ and $\beta'$, we write $\beta_{\mathrm{cp}}$ and
$\beta'_{\mathrm{cp}}$ so as not to confuse them with the one-loop coefficients $\beta^0_l$:
for $m<n$,
\begin{equation*}
g_m\le(1+\beta_{\mathrm{cp}})\,g_n,\qquad
g_n\le\bigl(1+g_n^2\beta'_{\mathrm{cp}}(n-m)\bigr)^{1/2}g_m .
\end{equation*}
These are exactly the reference comparisons of clause (a) of the hypothesis of the joint
induction, for pairs of levels at most $k+1$. Thus these items use no bound on the couplings of
the asymptotic-freedom kind derived in \cite{B-CMP109} beyond the two inputs just listed.
\end{proof}
```

**C-C1 (correction: whole-disc driver).** The driver bullet at II:26557–26559 mentions only its modulus at \(\zeta=0\). That alone does not satisfy the driven-flow lemma. Replace it by the whole-disc bound \(|\beta[Q^{(k+1)}_\zeta]|\le v_k\) on \(D(0,2r)\), already supplied by the frozen/valuation passage at II:25340–25343. Keep that supplier as C-frozen. This is a correction of the invocation, not a new remnant theorem.

**C-C2 (correction: radius and flow-constant notation).** The theorem and reference definition use \(\sigma_{\rm rad}x_j\) and \(\mathcal D_k(\varrho)\); the proof calls them \(\sigma_0x_j\) and \(d_k(\varrho)\). Use the theorem's \(\sigma_{\rm rad}x_j\) and \(d_k=\mathcal D_k\) throughout the application. C-slots must assert that these radii put every slot combination in \(D(1,\sigma_0)\), as the pure-step passage requires. Do not silently identify the slot-disc width \(\sigma_0\) with the shift-polydisc radius constant: if the identification is intended, it is part of that admission. This keeps the defined constants rather than replacing a radius by a larger one.

**C-F2 (filled: summability condition used by the flow proof).** On a prefix ending at \(k\), \(x_k>X\) and the already established pair bounds give
\[
y_j=\min_{i\le j}x_i-2c_2>X-4c_2+\lambda(k-j)
 \ge X/2+\lambda(k-j),\qquad j\le k,
\]
since \(X\ge8c_2+4\). The source functions and ceilings give, for large \(y\),
\(\psi(y^{-1/2})=y^{-1}e(y^{-1/2})\le C y^{-3/2}(\log y)^{p_0}\), and \(v_j=2C_\beta C_t C_{\mathfrak m}y_j^{-(\kappa_0-4)/2}\). The admitted positive integer degree \(p_0\) (CA-I:1863–1865) has \(2p_0>1\), making the exponential term of \(e\) obey this bound. Choose the unspecified final ceiling also so \(X/2\ge e^{2p_0}\); then the scalar formula is monotone throughout the interval through \(y_j^{-1/2}\), even if that auxiliary argument exceeds the physical run coupling. This is a sufficient explicit reading of “sufficiently small” in the source, not a larger physical domain. Explicitly its ratio to \(y^{-1/2}(\log y)^{p_0}\) has logarithm
\(-(\gamma_2A_1^2/4)(\log y)^{2p_0}+\frac12\log y-p_0\log\log y+O(1)\); under those conditions it tends to \(-\infty\). This is the same majorant summation invoked in the source.

For completeness the summation loses no cutoff factor. For sufficiently large \(A=X/2\), \(h(t)=t^{-3/2}(\log t)^{p_0}\) is decreasing, and
\[
\sum_{u\ge0}h(A+\lambda u)\le h(A)+\lambda^{-1}\int_A^\infty h(t)\,dt
 \le C\lambda^{-1}A^{-1/2}(\log A)^{p_0}.
\]
For the last inequality set \(t=Ae^v\); the integral becomes
\(A^{-1/2}\int_0^\infty e^{-v/2}(\log A+v)^{p_0}dv\).
Bound \((\log A+v)^{p_0}\le C(\log A)^{p_0}(1+v^{p_0})\) for \(\log A\ge1\), and use exponential domination to integrate. Absorb the initial term into the source's unspecified constant, with \(\lambda\) fixed before the ceiling. For \(a=(\kappa_0-4)/2>1\), the same integral comparison gives \(\sum_{u\ge0}(A+\lambda u)^{-a}\le C\lambda^{-1}A^{1-a}\). Consequently
\[
\sum_{j\le k}d_j(\varrho)\le C_{\mathfrak D}
 [\lambda^{-1}g(\log g^{-2})^{p_0}+g^{\kappa_0-6}/(\lambda\varrho)].
\]
The source chooses \(\gamma_J\) so the right side is at most \(1/3\) for \(\varrho\ge r\). This uses only earlier pair bounds on the prefix, so it does not assume the next coupling comparison.

**C-F3 (filled: endpoint, radii and derivatives).** Telescoping the Gaussian finite-part bound and defects gives exactly \(\lambda(j-i)-2c_2\le x_i-x_j\le3\lambda(j-i)+2c_2\). Infinite survival above \(X\) would contradict its lower bound with \(i=0,j\to\infty\). At the first failure, \(x_{K+1}\le X<x_K\) and \(x_K-x_{K+1}\le b_+\), whence \(X<x_K\le X+b_+\). This is the correlation convention for \(K\).

For active consecutive levels, \(x_k/x_{k+1}\le1+b_+/x_{k+1}\le1+b_+g^2\); fixed logarithmic powers in the radius schedules have ratios \(1+o(1)\) uniformly for \(x\ge X\), since their arguments differ by a fixed bounded amount. This gives the source's radius comparison, with the same enlargement fractions \(1/5,1/4\). Restrict to levels whose positive radii have been defined; no radius at a nonpositive inverse coupling is used.

For \(h_k=b_{k+1}-b_{k+1}(0)\), \(h_k(0)=0\) and \(|h_k(\zeta)|\le d_k(2r)|\zeta|\), so \(|h'_k(0)|\le d_k(2r)\). Reality on the real slice makes their sum real, giving \(N_K\in[2/3,4/3]\). On \(\bar D(0,r)\), Cauchy on radius tending to \(r\) about each point, inside \(D(0,2r)\), gives \(|b'_{k+1}|\le2d_k(2r)\). Integrating over line segments gives the stated total Lipschitz bound \(2/3\).

### Local averaging with sources

CA-II:26682–26777. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Joint induction: the local averaging step under sources]
\label{5.3:prf-local-averaging}
We treat the local averaging step from level $k$ to level $k+1$ with $k+1\le K'$, where
$K'=K-m$ is the last step of the local run (Definition~\ref{5.2:def-auxiliary-torus}), on the
physical torus, for a complex source $w\in\mathcal{W}_{k+1}\subset\mathcal{W}_k$.

\emph{The operations.} The step performs the same operations as the frozen averaging step
of the joint induction. This includes the exact refinement of the rim cut-offs
(Definition~\ref{5.2:def-rim-refinement}): its rule, its thresholds and its labels do not
depend on the source coefficients $z_i$ of $w=\sum_i z_i f_i$, so they are the same at every
source. The summation lemma for the refined rim cut-offs, which the frozen averaging step
uses, holds for $w\in\mathcal{W}_k$; there $w$ enters only as a
parameter of the potentials $V$, and the majorants are independent of $w$. At level $k$ the
running shift obeys $|\zeta_k|\le\tfrac83 r$. For $k=0$ the sum in
\eqref{5.2:eq-induction-format-a} is empty, so $\zeta_0=w$ and $|w|<2r$. For $k\ge1$ this is
the bound \eqref{5.3:eq-local-averaging-2} below at level $k$, read with $\sup|w|<2r$ on
$\mathcal{W}_k$, since $\tfrac43\cdot 2r=\tfrac83 r$.
The vertex $\mathfrak{S}_k$ of the step (Definition~\ref{5.2:def-three-families}) is a
function of $g_kC\mathsf{A}$, where $\mathsf{A}$ is the scaled fluctuation field and $C$ the
operator for which the constrained fluctuation form is
$\langle\mathsf{A},C^{*}\Delta^{(k)}C\mathsf{A}\rangle$; it vanishes at $0$ and contains no
factor $g_k^{-2}$. Hence the passage of \cite{B-CMP119} that treats vertex functions of this
kind applies to it.

\emph{Properties of the outputs.} Here $X'$ denotes a localisation domain, and $X'^{+}$ its
enlargement that enters the class $\mathcal{W}_{k+1}(X')$ of
Definition~\ref{5.1:def-weight-classes}. The outputs of the step have three properties.
\begin{itemize}
\item An output term with localisation domain $X'$ is analytic in $w$ on
$\mathcal{W}_{k+1}(X')$.
\item They are local: a potential in $Y\subset X'$ reads $\zeta_k|_Y$ and the old terms in $Y$.
It therefore reads only $w|_{X'^{+}}$.
\item They are frozen at constants: if $w\equiv\hat w$ on $X'^{+}$, every potential in $X'$ is
the frozen one.
\end{itemize}

\emph{The counterterm and the running shift.} Since $|w(p_y)|<2r$, the number
$b_{k+1}(w(p_y))$ is defined. We subtract the sum
\begin{equation*}
\sum_{y} b_{k+1}(w(p_y))\,A\bigl(h^{(k+1)}_y\varphi_{k+1},U_{k+1}\bigr)
\end{equation*}
from the effective action produced by the step, and move it, together with
$+A(\zeta_k,U_{k+1})$, into the weight. The total is unchanged: what is subtracted from the
effective action is added back through the weight. Because $A(c,U)$ is linear in the weight $c$ and
$\sum_y h^{(k+1)}_y=1$, the sum splits into two parts. The first is
$b_{k+1}(0)A(\varphi_{k+1},U_{k+1})$, which does not depend on $w$; it is the part taken up
by the reference recursion $x_{k+1}=x_k-b_{k+1}(0)$ of the flow step. The second is $A$
applied to the weight
\begin{equation*}
\varphi_{k+1}\sum_y h^{(k+1)}_y\bigl[b_{k+1}(w(p_y))-b_{k+1}(0)\bigr],
\end{equation*}
and it joins $A(\zeta_k,U_{k+1})$.
The result is the definition \eqref{5.2:eq-induction-format-a} of the induction format
(Definition~\ref{5.2:def-induction-format}) at level $k+1$. Comparing that definition at
levels $k+1$ and $k$, this reads
\begin{equation}\label{5.3:eq-local-averaging-1}
\zeta_{k+1}(p)=\zeta_k(p)
+\varphi_{k+1}(p)\sum_{y\in T^{(k+1)}}h^{(k+1)}_y(p)\bigl[b_{k+1}(w(p_y))-b_{k+1}(0)\bigr].
\end{equation}

\emph{The bound on the running shift.} This is the one place in the local run where the
increment bound of the flow step is used, at the levels $j\le k+1$. In the flow step of the
joint induction, on the coupling increment and the reference coupling, the increments satisfy
$|b_j(\zeta)-b_j(0)|\le d_{j-1}(\varrho)|\zeta|$ on $D(0,\varrho)$ for every
$\varrho\in[r,2r]$. We take $\varrho=2r$; this is admissible since $|w(p_y)|<2r$.
Inserting these bounds into the definition \eqref{5.2:eq-induction-format-a} at level $k+1$
gives the first inequality in
\begin{equation}\label{5.3:eq-local-averaging-2}
\begin{split}
|\zeta_{k+1}(p)|
&\le |w(p)|+\sum_{j\le k+1}\varphi_j(p)\sum_{y}h^{(j)}_y(p)\,d_{j-1}(2r)\,|w(p_y)|\\
&\le \tfrac43\sup|w| .
\end{split}
\end{equation}
The first inequality uses $\varphi_j\ge0$ and $h^{(j)}_y\ge0$. The second uses
$0\le\varphi_j\le1$ for the cut-off functions $\varphi_j$ of the induction format,
$\sum_y h^{(j)}_y=1$, and
\begin{equation*}
\sum_{j\le k+1}d_{j-1}(2r)\le\tfrac13 ,
\end{equation*}
which is the bound on $\sum_{j\le k}d_j(\varrho)$ proved in that same flow step, read at
$\varrho=2r$.

\emph{The bound on the coupling increments.} The bound $|b_j|\le b_++\tfrac23 r$ is taken
from the flow step of the joint induction, once that step has been carried
out. In particular no Cauchy estimate at the radii of
\cite[(2.28)]{B-CMP119} is involved.

\emph{The difference term.} Set $D^{(k+1)}$ equal to the local potential minus the frozen
one, as in the induction format (Definition~\ref{5.2:def-induction-format}). At each later
level, the freezing lemma, which bounds a local potential minus the frozen one, gives the
bound on $D^{(k+1)}$ directly from the a priori bound $E_0$ that the induction format
(Definition~\ref{5.2:def-induction-format}) carries for the potentials. This bound is not
derived from the bound at the preceding level, so nothing compounds
from level to level.
\end{proof}
```

**C-F4 (filled: local recurrence and mass).** The local action is linear in each local shift, so frozen subtraction leaves the same difference \(b_{k+1}(w(p_y))-b_{k+1}(0)\) multiplied by the printed partition \(h_y[k+1](p)\). These coefficients are nonnegative with sum one and the cutoff is at most one. Each increment is bounded by \(d_k\sup|w|\); sum the increments and include the initial \(w\) to get \(4\sup|w|/3\). Mass preservation is the exact normalized \(T^w,R^\flat\) identity retained from C-admitted and P1, iterated finitely; an analytic size bound is not a substitute for that identity.

### Full torus-bound implication, including its nine hypotheses

CA-II:59645–59924. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of the torus bound]\label{5.12:prf-torus-bound-proof}
The torus bound of the correlation theorem (Theorem~\ref{5.1:thm-correlation-theorem}) is derived
here as an implication. The statements
entering as hypotheses are the following.
\begin{enumerate}
\item The induction format with sources, Definition~\ref{5.2:def-induction-format}, at every
level $k\le K'$ of the local run (the renormalisation steps $k\le K'$, performed on the
physical torus), in particular its clauses (c), (d) and (f). We also use the
reference bound on the running inverse coupling, from the reference recursion of
Definition~\ref{5.1:def-reference-recursion},
$x_{K'}\le g^{-2}+b_++3\lambda m+2c_2$.
\item The sourced versions, on real and on complex backgrounds, of the bounds
\cite[(2.43)--(2.46)]{B-CMP119}, given by the last column of the budget at each site
(Definition~\ref{5.2:def-comparison-constant}), whose constant is $C_\sharp$, and the sup-norm
bounds \cite[(2.47)--(2.48)]{B-CMP119}.
\item Clause (c) of the lemma on complex plaquette weights in the expansions
(Lemma~\ref{5.2:lem-complex-weights}), with its constant
$\theta_W$, the ratio of complex to real weight.
\item The per-zone-cell value bound, with its constant $\mathsf{K}_{\mathrm{cell}}(k,n)$, and
the volume ceiling on $\gamma$ that bounds this constant.
\item Clause (c) of the modification bound for arbitrary regions on the flat domain
class (the class of localisation domains attached to the flat, coupling-dependent radii), that
is, the modification bound with the additional term
$-\kappa_{\mathfrak{d}}d_k(X)$.
\item The bound for the gas of live large-field components on the flat domain class, together
with the polymer bound $\Xi\le\exp(e^{-p_0(g_k)}|\mathbb{L}_k|)$, valid under the two ceilings
on $\gamma$. Here $\Xi$ is the partition function of that gas at level $k$, $\mathbb{L}_k$ is
the set of level-$k$ cubes over which the live components range, and $p_0(\cdot)$ is the degree
function.
\item The counting lemma, which controls the number $\#\bigl((\Lambda^{*})^{c}\bigr)$ of elements
of the complement of the set $\Lambda^{*}$ entering the indexing of the histories by the labels
$I^*$.
\item The floor for the unsourced integral at the level $K'$.
\item Clause (c) of the lemma indexing the histories, and the payment per $I$-cube with its
half factors.
\end{enumerate}

The local run is stopped at the level $K'=K-m$ of Definition~\ref{5.2:def-auxiliary-torus}, on
the physical torus. Its lattice $T^{(K')}$
has $N_{\mathrm{side}}$ sites per side; the letter $N$ is reserved for the group
$\mathrm{SU}(N)$. Throughout, $w=\sum_i z_if_i$ with $z$ in the ball
$\mathbb{D}$ of
admissible sources; $\mathbb{D}$, the number $r$ and the constant $\mathsf{Q}$ are those of the
torus bound in Theorem~\ref{5.1:thm-correlation-theorem}.

We begin by separating off the following terms. For $j\le K'$ and a localisation
domain $X$ at level $j$, put
\begin{equation}\label{5.12:eq-torus-bound-proof-1}
e^{(j)}(X;w):=\sum_{y\in X}E^{(j)}(X,1,y;w)+R^{(j)}(X,1;w),
\end{equation}
to which, when $X$ is the cube of a point $y$ at level $j$, the further term
$\log[\mathfrak{z}(a_j(y))/\mathfrak{z}(x_j)]$ is added.
The first two members are built from the $E$- and $R$-terms of the induction format at source $w$
(Definition~\ref{5.2:def-induction-format}); the further term on the cube of $y$ comes from the
one-bond Haar integrals
$\mathfrak{z}$ of the gauge-fixing move; here $a_j(y)$ is the argument at which the one-bond
integral $\mathfrak{z}$ is evaluated on the cube of $y$ at level $j$, and $x_j$ is the running
inverse coupling of level $j$, with which it is compared. Define
\begin{equation}\label{5.12:eq-torus-bound-proof-2}
e_j(X;z):=e^{(j)}(X;w)-e^{(j)}(X;0).
\end{equation}
By definition $e_j(X;0)=0$. Clauses (c), (d) and (f) of the induction format with sources
(Definition~\ref{5.2:def-induction-format}) give three further properties:
\begin{itemize}
\item $e_j(X;\cdot)$ is analytic on $\mathbb{D}$;
\item $e_j(X;\cdot)$ does not depend on $z_i$ unless $X^+\cap\operatorname{supp}f_i\neq\emptyset$,
where $X^+$ is the enlargement of $X$;
\item $e_j(X;\cdot)$ obeys, with the constant $C_e$ of the bounds of the induction format with
sources (Definition~\ref{5.2:def-induction-format}), the bound
\begin{equation}\label{5.12:eq-torus-bound-proof-3}
|e_j(X;z)|\le C_e\,e^{-(1-\delta)\kappa d_j(X)},\qquad z\in\mathbb{D}.
\end{equation}
\end{itemize}
Put $\mathcal{E}(z):=\sum_{j\le K'}\sum_Xe_j(X;z)$; the sum is finite on the torus. Define
$\tilde Z$ by $Z=e^{\mathcal{E}}\tilde Z$.

We next represent $\tilde Z$. By the induction format with sources at $k=K'$, $Z$ is the
integral over the variables $V_{K'}$ of $\rho^w_{K'}$. Here $\rho^w_{K'}$ is the sum over
histories $\{\Omega_j,\Lambda_j,I_j\}$ of $\chi_{K'}\mathbf{T}^w_{K'}\exp A^w_{K'}$. Hence
\begin{equation}\label{5.12:eq-torus-bound-proof-4}
\tilde Z(z)=\int dV_{K'}\sum\chi_{K'}\mathbf{T}^w_{K'}\exp\bigl[A^w_{K'}-\mathcal{E}\bigr].
\end{equation}
In a given history, the constant term of Ba{\l}aban's expansion appears together with
$-\sum_j\sum_{X\not\subset\Lambda_j}e_j(X;z)$, and this additional sum has modulus at most
$O(1)\sum_j|Z_j|$, where $Z_j$ are the large-field regions of the history.

The histories are indexed, at each step, by a pair consisting of a region and a label $I^*$;
this is clause (c) of the lemma indexing the histories. The additional
sum over the labels $I^*$ at step $j$ is paid for by the half factors reserved in the payment
made per $I$-cube.
These half factors lie inside the factor $\exp O(1)(MR_j)^{-d}|Z_j|$ of
\cite{B-CMP122b}, where $R_j$ denotes Ba{\l}aban's parameter $R$ at step $j$. The count
$\#\bigl((\Lambda^{*})^{c}\bigr)$ is controlled by the counting lemma. Together,
these two payments change the constants $E_+^{\sharp}$ and $C_{\mathrm{low}}$ below only by
numbers depending on $d$ and $L$.

We now bound the exponent. The sourced versions of \cite[(2.43)--(2.46)]{B-CMP119} on real and
complex backgrounds, in the last column of the budget at each site
(Definition~\ref{5.2:def-comparison-constant}), the sup-norm bounds
\cite[(2.47)--(2.48)]{B-CMP119} and clause (c) of
Lemma~\ref{5.2:lem-complex-weights} together give
\begin{equation}\label{5.12:eq-torus-bound-proof-a}
\begin{split}
\operatorname{Re}A^w_{K'}\le{}&-(1-\theta_W)\,A(x_{K'}(\cdot),U_{K'})
+(\text{logarithmic terms})\\
&+\sum_j\mathsf{K}_{\mathrm{cell}}(K',j)\,|\Gamma_j|
+\sum_{\mathfrak{a}\ \text{live at}\ K'}\mathsf{P}(\mathfrak{a}).
\end{split}
\end{equation}
Here $\mathsf{K}_{\mathrm{cell}}(K',j)$ is the per-zone-cell constant of the per-zone-cell value
bound, and the $\Gamma_j$ are the regions of \cite[(2.49)]{B-CMP119}, the zones. The constant
$\mathsf{K}_{\mathrm{cell}}(K',j)$ covers the
classes of terms listed in the per-zone-cell value bound under its first, second, third and
fifth items, its item of boundary-type terms and its item of the boundary terms $\mathbf{B}$,
together with the chain terms of the last step. By the volume ceiling on $\gamma$,
\begin{equation}\label{5.12:eq-torus-bound-proof-5}
\mathsf{K}_{\mathrm{cell}}(K',j)\le 2^{-d}\bigl(C_{\sharp}O(1)+1\bigr)\log g_j^{-2}
\qquad\text{per cell.}
\end{equation}
This is one more logarithmic term.

For the zones $j<K'$, which carry large-field factors, this term is controlled together with
the other logarithmic terms. In \cite[(2.49)]{B-CMP119} the corresponding member is
$O(1)\sum_j|\Gamma_j|$, and the first term of that bound also controls the logarithmic terms
there. The constants $E_\pm$ of \cite[Corollary~3]{B-CMP119} depend on $g_k$, and so do the
corresponding constants in \cite{B-CMP122b}.

The zone $j=K'$ has $|\Gamma_{K'}|$ of order $N_{\mathrm{side}}^4$ and no large-field factor.
There the term
joins $E_+^{\sharp}$ as the member $2^{-d}(C_\sharp O(1)+1)\mathsf{T}_{K'}$. This member reads
$(g,m)$ through
\begin{equation}\label{5.12:eq-torus-bound-proof-6}
\mathsf{T}_{K'}=\log g_{K'}^{-2}\le\log(g^{-2}+b_++3\lambda m+2c_2).
\end{equation}
This inequality is the reference bound on $x_{K'}=g_{K'}^{-2}$, read through the logarithm,
exactly as for $C_{\mathrm{low}}$ below.

In the last sum of \eqref{5.12:eq-torus-bound-proof-a}, $\mathfrak{a}$ runs over the arrests,
that is, the arrested chains of the large-field expansion, that are still live at the level
$K'$, that is, still carry their large-field factor at that level; for such an arrest
$\mathfrak{a}$, $\mathsf{P}(\mathfrak{a})$ denotes its frozen pile, the contribution of the
frozen left-over terms of $\mathfrak{a}$. Clause $(\beta')$ of the per-zone-cell value
bound describes it. It is extensive, each of its terms being counted at that term's own scale.
It is absorbed in the large-field volume charge $O(1)M^dR_j^{d+1}d'_j(Z_j)$ of the gas of live
components, where $d'_j(Z_j)$ is the size of $Z_j$ measured in cubes of side $MR_j$, with the
constant $2c_{\mathsf{P}}M^{-d}$; here $c_{\mathsf{P}}$ is the constant of the frozen pile in the
per-zone-cell value bound, and $2c_{\mathsf{P}}M^{-d}$ is a number once $M$ is fixed.
Accordingly, the charge of the bound for the gas of live large-field components contains it, by
the charge clause of that bound. A
live arrest lies in a large-field region of the history contained in $\Lambda^c_{K'}$, never in
the top zone. Therefore the upper bound
on $|\tilde Z|$ below holds with $E_+^{\sharp}$ changed only by the one member reading $(g,m)$
named above.

We turn to the upper bound. We use clause (c) of the modification bound for arbitrary regions
on the flat domain class, that is, the modification bound with the additional term
$-\kappa_{\mathfrak{d}}d_k(X)$; here $\kappa_{\mathfrak{d}}$ is the coefficient of the additional
term of \cite{B-CMP122b}, denoted there $\kappa_1$.

Ba{\l}aban proves the upper member of \cite[(2.50)]{B-CMP119} by bounding the moduli of the
terms. We follow that proof, with the moduli integrated over the variables $V_{K'}$ by the device
for integrating bounds on moduli over these variables. On the
flat domain class the gas of live components is controlled by the bound for the gas of live
large-field components, together with the polymer bound for $\Xi$, which holds under
the two ceilings on $\gamma$. Combining this with \eqref{5.12:eq-torus-bound-proof-4},
\eqref{5.12:eq-torus-bound-proof-a} and the history bound above gives
\begin{equation}\label{5.12:eq-torus-bound-proof-7}
|\tilde Z(z)|\le e^{E_+^{\sharp}N_{\mathrm{side}}^4},\qquad z\in\mathbb{D}.
\end{equation}

For the floor, note that $\mathcal{E}(0)=0$, since every $e_j(X;0)$ vanishes. The floor for the
unsourced integral then gives
\begin{equation}\label{5.12:eq-torus-bound-proof-8}
\tilde Z(0)=\int dV_{K'}\,\rho^0_{K'}\ge e^{-C_{\mathrm{low}}N_{\mathrm{side}}^4}.
\end{equation}
The constant $C_{\mathrm{low}}$ reads the coupling through the reference bound
$x_{K'}\le g^{-2}+b_++3\lambda m+2c_2$.

We now estimate the derivatives. Put $\mathsf{h}:=\tilde Z/\tilde Z(0)$. Dividing
\eqref{5.12:eq-torus-bound-proof-7} by \eqref{5.12:eq-torus-bound-proof-8} gives
\begin{equation*}
|\mathsf{h}|\le e^{(E_+^{\sharp}+C_{\mathrm{low}})N_{\mathrm{side}}^4}\le\mathsf{Q}
\qquad\text{on }\mathbb{D},
\end{equation*}
the constant $\mathsf{Q}$ of the torus bound in Theorem~\ref{5.1:thm-correlation-theorem}
dominating $e^{(E_+^{\sharp}+C_{\mathrm{low}})N_{\mathrm{side}}^4}$.

Since $Z=e^{\mathcal{E}}\tilde Z(0)\,\mathsf{h}$, wherever $\operatorname{Log}\mathsf{h}$ is
defined the logarithm of $Z$ equals $\mathcal{E}+\log\tilde Z(0)+\operatorname{Log}\mathsf{h}$.
Its mixed derivative $\partial_{z_1}\cdots\partial_{z_n}$ at $z=0$ is therefore the sum of the
corresponding derivatives of $\operatorname{Log}\mathsf{h}$ and of $\mathcal{E}$. We estimate
them in turn.

($\alpha$) The derivatives of $\operatorname{Log}\mathsf{h}$. The function $\mathsf{h}-1$
vanishes at $0$ and is bounded by $\mathsf{Q}+1$ on $\mathbb{D}$. Fix $z\in\mathbb{D}$. Since
$\mathbb{D}$ is a ball about $0$, the map $\varsigma\mapsto\mathsf{h}(\varsigma z)-1$ is analytic
for complex $\varsigma$ of modulus less than one, vanishes at $\varsigma=0$ and is bounded by
$\mathsf{Q}+1$. The Schwarz lemma on
this complex line gives $|\mathsf{h}(\varsigma z)-1|\le(\mathsf{Q}+1)|\varsigma|$. Hence
\begin{equation}\label{5.12:eq-torus-bound-proof-9}
|\mathsf{h}-1|\le\tfrac12\quad\text{on }(2\mathsf{Q}+2)^{-1}\mathbb{D}.
\end{equation}
There $\operatorname{Log}\mathsf{h}$, the principal branch, is analytic. Its power series in
$\mathsf{h}-1$ gives
\begin{equation}\label{5.12:eq-torus-bound-proof-10}
|\operatorname{Log}\mathsf{h}|
\le\sum_{\ell\ge1}\frac{|\mathsf{h}-1|^\ell}{\ell}
\le\sum_{\ell\ge1}\frac{2^{-\ell}}{\ell}
=\log2 .
\end{equation}

We apply the Cauchy estimate on the circles
$|z_i|=(1-\upsilon)r/((2\mathsf{Q}+2)n\|f_i\|_\sharp)$, $i=1,\dots,n$, with $0<\upsilon<1$. For
$\upsilon>0$ these circles lie in $(2\mathsf{Q}+2)^{-1}\mathbb{D}$; at $\upsilon=0$ the polyradii
lie on its boundary. The estimate gives
\begin{equation}\label{5.12:eq-torus-bound-proof-11}
\bigl|\partial_{z_1}\cdots\partial_{z_n}\operatorname{Log}\mathsf{h}(0)\bigr|
\le\log2\,\prod_{i=1}^n\frac{(2\mathsf{Q}+2)\,n\,\|f_i\|_\sharp}{(1-\upsilon)\,r}.
\end{equation}
Letting $\upsilon\downarrow0$ removes the factors $(1-\upsilon)^{-1}$. Alternatively, the
closure of $(2\mathsf{Q}+2)^{-1}\mathbb{D}$ lies in $\mathbb{D}$, and the set where
$|\mathsf{h}-1|\le\frac12$ is closed. So \eqref{5.12:eq-torus-bound-proof-9} holds on that
closure, and one may take $\upsilon=0$ directly. The constant is the same either way.

($\beta$) The derivatives of $\mathcal{E}$. Since $e_j(X;\cdot)$ does not depend on $z_i$
unless $X^+$ meets $\operatorname{supp}f_i$, the derivative
$\partial_{z_1}\cdots\partial_{z_n}e_j(X;0)$ vanishes unless $X^+$ meets every
$\operatorname{supp}f_i$. In that case
$4M\mathsf{t}_j(d_j(X)+3)\ge\mathsf{d}$, where $\mathsf{t}_j:=L^j\varepsilon$ and $\varepsilon$
is the lattice spacing. Since $d_j(X)\ge0$, this means
$d_j(X)\ge[\mathsf{d}/(4M\mathsf{t}_j)-3]_+$.

For each such $X$ we apply the Cauchy estimate to $e_j(X;\cdot)$ on the circles
$|z_i|=(1-\upsilon)r/(n\|f_i\|_\sharp)$, using the bound \eqref{5.12:eq-torus-bound-proof-3},
and let $\upsilon\downarrow0$. This gives
\begin{equation}\label{5.12:eq-torus-bound-proof-12}
\bigl|\partial_{z_1}\cdots\partial_{z_n}e_j(X;0)\bigr|
\le C_e\,e^{-(1-\delta)\kappa d_j(X)}\prod_{i=1}^n\frac{n\|f_i\|_\sharp}{r}.
\end{equation}
We anchor each contributing $X$ at one of the at most $1+(M\mathsf{t}_j)^{-4}$ cubes of level
$j$ that meet $(\operatorname{supp}f_1)^+$. We then sum over $X$ with
\cite[(1.26)]{B-CMP116}, under the constraint
$d_j(X)\ge[\mathsf{d}/(4M\mathsf{t}_j)-3]_+$. After summation over $j\le K'$ this gives
\begin{equation}\label{5.12:eq-torus-bound-proof-13}
\bigl|\partial_{z_1}\cdots\partial_{z_n}\mathcal{E}(0)\bigr|
\le C_{\mathrm{UV}}(\mathsf{d})\prod_{i=1}^n\frac{n\|f_i\|_\sharp}{r},
\end{equation}
where
\begin{equation}\label{5.12:eq-torus-bound-proof-14}
C_{\mathrm{UV}}(\mathsf{d}):=C_e\,O(1)\sum_{j\le K'}\bigl(1+(M\mathsf{t}_j)^{-4}\bigr)
e^{-\frac14\kappa[\mathsf{d}/(4M\mathsf{t}_j)-3]_+}.
\end{equation}

It remains to bound $C_{\mathrm{UV}}(\mathsf{d})$ independently of $K$. The numbers
$\mathsf{t}_j$ form a
geometric sequence of ratio $L$. The summands of \eqref{5.12:eq-torus-bound-proof-14} with
$M\mathsf{t}_j\le\mathsf{d}/24$, prefactor $C_e\,O(1)$ included, sum to at most
$C\mathsf{d}^{-4}$, with a constant $C$ that does
not depend on $K$. Write
$\log_L^+x:=\max\{\log_Lx,0\}$. The remaining terms, those with $M\mathsf{t}_j>\mathsf{d}/24$,
number at most $1+\log_L^+(24M/(\mathsf{d}N_{\mathrm{side}}))$. Each of them is at most
$C_e\,O(1)(1+(24/\mathsf{d})^4)$, since for them $(M\mathsf{t}_j)^{-4}<(24/\mathsf{d})^4$ and
the exponential factor is at most one. Hence
\begin{equation}\label{5.12:eq-torus-bound-proof-15}
C_{\mathrm{UV}}(\mathsf{d})\le C\mathsf{d}^{-4}
+C_e\,O(1)\bigl(1+(24/\mathsf{d})^{4}\bigr)\bigl(1+\log_L^+(24M/(\mathsf{d}N_{\mathrm{side}}))\bigr),
\end{equation}
and the right-hand side does not depend on $K$.

Finally, the derivative of the constant $\log\tilde Z(0)$ vanishes, so by the decomposition of
the logarithm of $Z$ above, \eqref{5.12:eq-torus-bound-proof-11} with $\upsilon\downarrow0$ and
\eqref{5.12:eq-torus-bound-proof-13} give
\begin{equation}\label{5.12:eq-torus-bound-proof-16}
\bigl|\partial_{z_1}\cdots\partial_{z_n}\log Z(0)\bigr|
\le\Bigl[(2\mathsf{Q}+2)^n\log2+C_{\mathrm{UV}}(\mathsf{d})\Bigr]
\prod_{i=1}^n\frac{n\|f_i\|_\sharp}{r},
\end{equation}
with $C_{\mathrm{UV}}(\mathsf{d})$ bounded independently of $K$ by
\eqref{5.12:eq-torus-bound-proof-15}.
\end{proof}
```

**C-F5 (filled: Cauchy zero case and ultraviolet sum).** If any test function has zero norm, it is zero and multilinearity makes the mixed derivative zero; omit division by that norm. Otherwise the printed radii are positive, and the factor \(1-\upsilon\) puts their entire product inside the source ball.

For the ultraviolet estimate write \(a_j=M\mathsf t_j\). If \(a_j\le\mathsf d/24\), then
\[
[\mathsf d/(4a_j)-3]_+\ge\mathsf d/(8a_j),\qquad
e^{-\kappa\mathsf d/(32a_j)}\le C(a_j/\mathsf d)^5.
\]
The last inequality follows from \(e^x\ge x^5/5!\), with the same fixed \(\kappa\). Hence the fine-scale sum is bounded by
\[
C\sum_{a_j\le\mathsf d/24}
 [(a_j/\mathsf d)^5+\mathsf d^{-4}(a_j/\mathsf d)]
 \le C(1+\mathsf d^{-4}),
\]
because \(a_j\) is geometric. For nonzero pairwise separated tests on the fixed physical unit torus, \(\mathsf d\) is bounded by its diameter, so this is at most \(C\mathsf d^{-4}\), with a fixed geometric constant. The remaining scales number at most \(1+\log_L^+(24M/(\mathsf d N_{\rm side}))\), as in the source, and each contributes at most \(C(1+(24/\mathsf d)^4)\). With \(N_{\rm side}\ge1\) and \(M,L\) fixed, this is
\(C\mathsf d^{-4}(1+\log^+\mathsf d^{-1})\).
This fills the omitted geometric-sum estimate; the anchor count and rooted-domain summation CMP 116 (1.26) remain the exact named geometric inputs of the original route.

The normalized \(\mathsf h\) obeys \(\mathsf h(0)=1\) because the retained unsourced floor is positive. Schwarz on each complex radial line gives \(|\mathsf h-1|\le1/2\) in the stated smaller ball, and the convergent logarithm series is bounded by \(\log2\). Thus no global zero-free assertion about the original source ball is needed or claimed.

**C-C3 (correction: dependence of last-lattice constants).** The theorem's last sentence says no constants depend on \(m\). Its proof at II:59770–59779 explicitly puts
\[
2^{-d}(C_\sharp O(1)+1)\log(g^{-2}+b_++3\lambda m+2c_2)
\]
into \(E_+^\sharp\), and II:59820–59821 lets \(C_{\rm low}\) read the same bound. The displayed argument therefore proves the torus estimate uniformly in \(K\) at **fixed \(g,m,N_T\)**, not the blanket \(m\)-independence of these two constants. The smallest correction is to allow this displayed \((g,m)\)-dependence for the last-lattice constants. To retain the literal independence sentence, add C-uniform-last as a named, unproved input. The ultraviolet constant and the volume-free flow argument are separate. No missing last-scale uniformity is inferred from W5, W6, or the one-loop law.

### Subsequential off-diagonal limits: exact auxiliary statement and proof

CA-II:59926–60087. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proposition}[Subsequential continuum limits of the Schwinger functions]
\label{5.12:prop-subsequential-limits}
Fix $(g,m,N_T)$, where $N_T$ is the positive
integer for which $N_{\mathrm{side}}:=N_TL^m$ is the number of sites per side of the unit lattice
$T^{(K')}$ after $K'=K-m$ renormalisation steps (the letter $N$ being reserved for
$\mathrm{SU}(N)$); $N_T$ is not to be
confused with the torus floor function
$N_{\mathbb{T}}(g,m)$ of Definition~\ref{5.1:def-torus-floor}. In this proposition the index $m$ of
$S^T_{n;K,m}$ and of its limit $S^T_{n;m}$ is this number of renormalisation steps withheld, the run
being stopped at level $K'$.
For test functions $f_1,\dots,f_n$ of class $C^1$ on the physical torus $\mathbb{T}^4$ of
Definition~\ref{5.2:def-auxiliary-torus} and the complex source
$w=\sum_i z_i f_i$, with
$Z(z)$ the sourced partition function and
$\mathcal{O}(f)=\sum_p f(x(p))\,[1-\operatorname{Re}\operatorname{tr}U(\partial p)]$, set
\begin{equation}\label{5.12:eq-subsequential-limits-1}
S^T_{n;K,m}(f_1,\dots,f_n)
:=\partial_{z_1}\cdots\partial_{z_n}\log Z(z)\big|_{z=0}
=\langle \mathcal{O}(f_1);\dots;\mathcal{O}(f_n)\rangle^{\mathrm{conn}}_K .
\end{equation}
At fixed $N_T$, the left side of \eqref{5.12:eq-subsequential-limits-1} does not depend on $m$.
Let $(g_0^{(i)})_{i\ge 1}$ be a
sequence of bare couplings, let $K_i:=K(g_0^{(i)},g)$ be the first-passage levels of
Definition~\ref{5.1:def-reference-recursion}, with $x_0^{(i)}=(g_0^{(i)})^{-2}$, and assume:
\begin{enumerate}
\item the torus bound of the correlation theorem (Theorem~\ref{5.1:thm-correlation-theorem}), which
bounds $S^T_{n;K,m}$ uniformly in $K$ at pairwise separated supports;
\item the compactness lemma for equicontinuous multilinear functionals, in the following form. Let
$n\ge2$, let $B_1,\dots,B_n\subset\mathbb{T}^4$ be closed sets pairwise at positive distance, and
let $C^1_{B_j}$ be the linear space of test functions supported in $B_j$. Let $(S_i)_{i\ge1}$ be a
sequence of multilinear functionals on $C^1_{B_1}\times\dots\times C^1_{B_n}$, equicontinuous on
$\|\cdot\|_\sharp$-bounded subsets and convergent on a countable $\|\cdot\|_\sharp$-dense subset.
Then $(S_i)$ converges at every tuple of $C^1_{B_1}\times\dots\times C^1_{B_n}$ to a multilinear
limit. If, moreover, $(S_i)$ is defined on all tuples of test functions with pairwise disjoint
supports and these hypotheses hold on every such product, then the limits so obtained on all these
products are the restrictions of one distribution of finite order on the open set
\begin{equation}\label{5.12:eq-subsequential-limits-2}
\{(x_1,\dots,x_n)\in(\mathbb{T}^4)^n : x_i\ne x_j \text{ for } i\ne j\};
\end{equation}
\item $K_i\to\infty$ as $i\to\infty$;
\item the torus-compatibility condition of Definition~\ref{5.1:def-torus-floor} on $(g,m,N_T)$, with
the constant $C_{\mathbb{T}}=L^{11}M$.
\end{enumerate}
Then there is a subsequence $(K_{i_l})_{l\ge1}$ such that, for every $n\ge 2$ and every tuple
$f_1,\dots,f_n$ of test functions with pairwise disjoint supports,
$S^T_{n;K_{i_l},m}(f_1,\dots,f_n)$
converges; the limit, denoted $S^T_{n;m}(f_1,\dots,f_n)$ and depending on the subsequence, is
multilinear, and $S^T_{n;m}$ is the restriction of one distribution of finite order on the open set
\eqref{5.12:eq-subsequential-limits-2}. Each $S^T_{n;m}$ is symmetric in its $n$
arguments and is
covariant under the lattice symmetries common to all members of the subsequence. Nothing is asserted for
$n=1$ or at coinciding points.
\end{proposition}

\begin{proof}
The first equality in \eqref{5.12:eq-subsequential-limits-1} is the definition. The second is the
definition of the connected correlation (joint cumulant) as the mixed derivative at the origin of the
logarithm of the generating function. Indeed, $Z(z)$ is the integral of the density sourced by
$w=\sum_i z_if_i$, and $w$ enters the weight through
$\sum_i z_i\,\mathcal{O}(f_i)$. Neither side refers to $m$ at fixed $N_T$: the observable
$\mathcal{O}(f)$ and the bare sourced density $\rho_0^w$ live on the finest lattice of the physical
torus of Definition~\ref{5.2:def-auxiliary-torus}, whose number of sites per side,
$N_{\mathrm{side}}L^{K'}=N_TL^mL^{K-m}=N_TL^K$, is fixed by $K$ and $N_T$ alone, and they make no
reference to $m$.

Fix $(g,m,N_T)$ obeying the torus-compatibility condition, under which the torus bound of
assumption (1) is in force, and let $K_i\to\infty$. Since
$N_{\mathrm{side}}$ is fixed, the torus bound, in the form \eqref{5.12:eq-torus-bound-proof-a} of
its proof, applies, with the same value of $N_{\mathrm{side}}$, to
every member of the sequence with $K_i$ sufficiently large (in particular $K_i\ge m$, so that
$K'=K_i-m\ge0$); by the third assumption this excludes only finitely many members, and discarding them
we assume that it applies to every member of the sequence.
It bounds $S^T_{n;K_i,m}(f_1,\dots,f_n)$ uniformly in $i$ in terms of the
norms $\|f_j\|_\sharp$ and the separation of the supports.

Fix $n\ge2$ and closed sets $B_1,\dots,B_n\subset\mathbb{T}^4$ pairwise at distance at least
$\mathsf{d}>0$, with $C^1_{B_j}$ as in assumption (2).
For tuples $f=(f_1,\dots,f_n)$ and $f'=(f'_1,\dots,f'_n)$ in
$C^1_{B_1}\times\dots\times C^1_{B_n}$, multilinearity gives the telescoping identity
\begin{equation*}
S^T_{n;K_i,m}(f)-S^T_{n;K_i,m}(f')
=\sum_{j=1}^n S^T_{n;K_i,m}(f'_1,\dots,f'_{j-1},f_j-f'_j,f_{j+1},\dots,f_n).
\end{equation*}
Each tuple on the right again lies in $C^1_{B_1}\times\dots\times C^1_{B_n}$, because each
$C^1_{B_j}$ is a linear space; hence its supports are pairwise at distance at least $\mathsf{d}$, and
the torus bound estimates each term by a constant, independent of $i$, depending on $n$, $\mathsf{d}$
and the fixed data $(g,m,N_T)$, times the product of the $\|\cdot\|_\sharp$-norms of its entries.
Calling this constant $C_n(\mathsf{d})$, we obtain
\begin{equation*}
\bigl|S^T_{n;K_i,m}(f)-S^T_{n;K_i,m}(f')\bigr|
\le C_n(\mathsf{d})\sum_{j=1}^n\|f_j-f'_j\|_\sharp\prod_{r\ne j}\max\{\|f_r\|_\sharp,\|f'_r\|_\sharp\}
\end{equation*}
uniformly in $i$. Thus $\{S^T_{n;K_i,m}\}_{i\ge1}$ is equicontinuous on $\|\cdot\|_\sharp$-bounded
subsets of $C^1_{B_1}\times\dots\times C^1_{B_n}$.

Every tuple of test functions with pairwise disjoint supports lies in such a product for a choice in
which each $B_j$ is a finite union of closed balls with rational centres and rational radii. Indeed,
the supports are compact and pairwise disjoint, hence pairwise at distance at least $3\mathsf{d}$ for
some $\mathsf{d}>0$. Each point of $\operatorname{supp}f_j$ lies in a closed ball with rational centre
within $\mathsf{d}/4$ of it and rational radius strictly between $\mathsf{d}/4$ and $\mathsf{d}/2$.
By compactness
finitely many of these balls cover $\operatorname{supp}f_j$; let $B_j$ be their union. Every point of
$B_j$ lies within $\mathsf{d}$ of $\operatorname{supp}f_j$, so the sets $B_j$ are pairwise at distance
at least $\mathsf{d}$. There are countably many such choices of $(B_1,\dots,B_n)$.

On $C^1$ functions on the compact torus the norm $\|\cdot\|_\sharp$ is dominated by a multiple of the
$C^1$ norm, and the space of $C^1$ functions is separable for the $C^1$ norm; hence each
$C^1_{B_1}\times\dots\times C^1_{B_n}$ contains a countable $\|\cdot\|_\sharp$-dense subset. Let
$\mathcal{D}$ be the union of these subsets over all $n\ge2$ and all countably many choices of
$(B_1,\dots,B_n)$ above; $\mathcal{D}$ is countable. For each tuple in $\mathcal{D}$, the numbers
$S^T_{n;K_i,m}(f_1,\dots,f_n)$ form a bounded sequence, bounded by the same estimate, so it has a
convergent subsequence. Enumerate $\mathcal{D}$ and extract successively nested subsequences, one for
each of its elements. The diagonal sequence $(K_{i_l})$ then gives convergence of
$S^T_{n;K_{i_l},m}$ on the whole of $\mathcal{D}$, for every $n\ge 2$.

Equicontinuity on each of the products of the countable family above and convergence on a dense
subset of it are exactly the hypotheses of assumption (2). Its first conclusion gives, on each of
these products, convergence of $S^T_{n;K_{i_l},m}$ at every tuple to a multilinear limit. Since every
tuple with pairwise disjoint supports lies in one of these products, and at a tuple lying in several
of them the limit is the limit of one sequence of numbers, hence the same, this defines, for each
$n\ge 2$, a multilinear limit $S^T_{n;m}$ of $S^T_{n;K_{i_l},m}$ on all tuples with pairwise disjoint
supports. The hypotheses of assumption (2) now hold on every product
$C^1_{B_1}\times\dots\times C^1_{B_n}$ with closed sets $B_j$ pairwise at positive distance:
equicontinuity was shown above for every such product, and convergence holds at every tuple of it,
in particular on the countable $\|\cdot\|_\sharp$-dense subset that it contains by the separability
argument above, which applies to every such product. The second conclusion of assumption (2)
therefore shows that the limits on all these products are the restrictions of one distribution of
finite order on the open set \eqref{5.12:eq-subsequential-limits-2}. This open set is covered by the
sets $\operatorname{int}B_1\times\dots\times\operatorname{int}B_n$ of the countable family: if the
coordinates of $(x_1,\dots,x_n)$ are pairwise at distance at least $3\mathsf{d}$ for some
$\mathsf{d}>0$, a closed ball $B_j$ with rational centre within $\mathsf{d}/4$ of $x_j$ and rational
radius strictly between $\mathsf{d}/4$ and $\mathsf{d}/2$ contains $x_j$ in its interior, and these
balls are pairwise at distance at least $\mathsf{d}$.

For symmetry, note that $S^T_{n;K,m}$ is, by \eqref{5.12:eq-subsequential-limits-1}, a mixed partial
derivative of the function $z\mapsto\log Z(z)$. The lattice is finite and the integrand defining
$Z(z)$ is the exponential of a function affine in $z$, so $Z$ is holomorphic in $z$; at $z=0$ the
integrand is positive, so $Z(0)>0$. Hence $\log Z$ is holomorphic near $z=0$ and its mixed partial
derivatives commute, so the value of $S^T_{n;K,m}(f_1,\dots,f_n)$ is unchanged under every
permutation of its arguments. This identity holds for every member of the subsequence and therefore
for the limit.

For covariance, let $\iota$ be an isometry of $\mathbb{T}^4$ that maps the finest lattice at cutoff
$K_{i_l}$ onto itself for every $l$, and for a configuration $U$ let $\iota_*U$ be the
configuration with $(\iota_*U)(\iota b)=U(b)$ on every oriented bond $b$. The product of the Haar
measures over the bonds and the Wilson action are invariant under $U\mapsto\iota_*U$. Relabelling the
plaquettes by $p'=\iota p$, using $x(\iota p)=\iota\, x(p)$, and using that
$(\iota_*U)(\partial(\iota p))$ equals $U(\partial p)$ up to inversion and conjugation, neither of
which changes $\operatorname{Re}\operatorname{tr}$, one has
\begin{equation*}
\mathcal{O}(f)(\iota_*U)
=\sum_{p}f(\iota\, x(p))\,[1-\operatorname{Re}\operatorname{tr}U(\partial p)]
=\mathcal{O}(f\circ\iota)(U).
\end{equation*}
Since $w$ enters the weight only through $\sum_i z_i\,\mathcal{O}(f_i)$, the change of variables
$U\mapsto\iota_*U$ in the integral defining $Z(z)$ shows that $Z(z)$ is unchanged when every $f_i$ is
replaced by $f_i\circ\iota$. By \eqref{5.12:eq-subsequential-limits-1},
\begin{equation*}
S^T_{n;K_{i_l},m}(f_1\circ\iota,\dots,f_n\circ\iota)=S^T_{n;K_{i_l},m}(f_1,\dots,f_n)
\end{equation*}
for every $l$, and letting $l\to\infty$ gives the same identity for $S^T_{n;m}$.
\end{proof}
```

**C-F6 (filled: extension from the dense set).** On a fixed product of separated support spaces, approximate a tuple \(f\) by a dense tuple \(f^{(q)}\), with uniformly bounded norms. The displayed telescoping estimate makes \(|S_i(f)-S_i(f^{(q)})|\) uniformly small in \(i\). For \(i,j\) large, split
\[
S_i(f)-S_j(f)=[S_i(f)-S_i(f^{(q)})]+
 [S_i(f^{(q)})-S_j(f^{(q)})]+
 [S_j(f^{(q)})-S_j(f)].
\]
Choose \(q\) first and then \(i,j\). This proves convergence at \(f\); the same finite-sum argument preserves multilinearity. On overlaps there is just one limit of one numerical sequence. The countable support-family diagonal extraction therefore works for every \(n\). The assertion that these forms extend to a distribution is still the explicitly assumed **second part of C-compact**, not a consequence asserted solely from boundedness. No value on a diagonal and no one-point function has been obtained.

**C-C4 (correction: torus-bound cross-reference).** The compactness proof calls 5.12:eq-torus-bound-proof-a the correlation estimate. That equation bounds the exponent. Its required mixed-derivative estimate is 5.12:eq-torus-bound-proof-16 (II:59917–59923), with -15 controlling \(C_{\rm UV}\). Replace that reference only; the fixed-\((g,m,N_T)\) conclusion is unchanged.

### Exact positivity statement and full proof

CA-II:60089–60178. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{lemma}[Reflection positivity of the limits at disjoint supports]
\label{5.12:lem-limit-positivity}
Assume the lemma on reflection positivity of the lattice measure \cite{OSe78}. For a point $x$
of the torus write
$x^{0}$ for its time coordinate, and let $\theta$ denote the time reflection $x^{0}\mapsto -x^{0}$ for
which that lemma holds; assume further that the expectation
$\langle\cdot\rangle_K$ is invariant under $\theta$. The reflection $\theta$ acts on test functions by
$(\theta f)(x):=f(\theta x)$, on bond variables by $(\theta U)(b):=U(\theta b)$ for an oriented
bond $b$, and on functions of the bond variables by $(\theta F)(U):=F(\theta U)$. Let
$(K_{i_l})_{l\ge 1}$ be the subsequence of the sequence $(K_i)$ along which
Proposition~\ref{5.12:prop-subsequential-limits} provides the limits $S^T_{n;m}$, $n\ge 2$, of the
connected Schwinger functions $S^T_{n;K,m}$. In this lemma $g$ and $m$ are fixed as in
Proposition~\ref{5.12:prop-subsequential-limits}, and we abbreviate $S^K_n:=S^T_{n;K,m}$ and
$S_n:=S^T_{n;m}$.

Let $(f_i)_{i\in I}$, with $I$ a finite index set, be test functions whose supports are pairwise
disjoint and contained in $\{0<x^{0}<\tfrac12\}$. For subsets $\alpha\subset I$ let $c_\alpha$ be
complex numbers, and put
\begin{equation*}
F:=\sum_{\alpha}c_\alpha\prod_{i\in\alpha}\bigl(\mathcal{O}(f_i)-\langle\mathcal{O}(f_i)\rangle_K\bigr).
\end{equation*}
Then $\langle\overline{\theta(F)}\,F\rangle_K\ge 0$ for every $K$. This quantity is a
polynomial $P_K(F)$ in the connected functions $S^K_n$, $n\ge 2$, evaluated at test functions with
pairwise disjoint supports; it depends only on the $c_\alpha$ and the $f_i$, not on the centring
constants. As $l\to\infty$, $P_{K_{i_l}}(F)$ converges to the same polynomial $P(F)$ in the
limits $S_n$, and
\begin{equation}\label{5.12:eq-limit-positivity-1}
P(F)=\lim_{l\to\infty}\bigl\langle\overline{\theta(F)}\,F\bigr\rangle_{K_{i_l}}\ \ge\ 0 .
\end{equation}
Nothing is asserted for the one-point functions ($n=1$) or at coinciding points.
\end{lemma}

\begin{proof}
For each $K$, $F$ is a function of the bond variables of the plaquettes whose
barycentres lie in the union of the supports of the $f_i$. This union is contained in
$\{0<x^{0}<\tfrac12\}$. Reflection positivity of the lattice measure, applied to $F$, therefore gives
$\langle\overline{\theta(F)}F\rangle_K\ge 0$ (cf.\ \cite{OSe78}).

We next write the left side in terms of connected functions. The reflection maps plaquettes to
plaquettes and barycentres to reflected barycentres, and $1-\operatorname{Re}\operatorname{tr}U(\partial p)$ is
unchanged under reversal of orientation. Hence $\theta(\mathcal{O}(f))=\mathcal{O}(\theta f)$. By the
hypothesis that the expectation is invariant under $\theta$,
$\langle\mathcal{O}(\theta f)\rangle_K=\langle\mathcal{O}(f)\rangle_K$. Since $\mathcal{O}(f)$ is linear in
$f$ with real plaquette weights, $\overline{\mathcal{O}(f)}=\mathcal{O}(\bar f)$. Together these give
\begin{equation*}
\overline{\theta(F)}=\sum_{\alpha}\bar c_\alpha\prod_{i\in\alpha}
\bigl(\mathcal{O}(\theta\bar f_i)-\langle\mathcal{O}(\theta\bar f_i)\rangle_K\bigr).
\end{equation*}
For a pair $(\alpha,\beta)$ let $\alpha'=\{i':i\in\alpha\}$ be a disjoint copy of $\alpha$. Put
$h_{i'}:=\theta\bar f_i$ for $i\in\alpha$ and $h_j:=f_j$ for $j\in\beta$. Then
$\langle\overline{\theta(F)}F\rangle_K$ is the sum over $(\alpha,\beta)$ of $\bar c_\alpha c_\beta$ times
the moment of the centred variables $\mathcal{O}(h_j)-\langle\mathcal{O}(h_j)\rangle_K$,
$j\in\alpha'\sqcup\beta$.

By the moment--cumulant formula, a moment is the sum over partitions $\pi$ of the index set of the
products over blocks $B\in\pi$ of joint cumulants. Cumulants of order one of centred variables vanish.
Cumulants of order at least two do not change when constants are added to the variables. By the
definition in Proposition~\ref{5.12:prop-subsequential-limits}, the joint cumulant of
$\mathcal{O}(h_j)$, $j\in B$, is
\begin{equation*}
S^K_{|B|}\bigl((h_j)_{j\in B}\bigr)
=\langle\mathcal{O}(h_{j_1});\dots;\mathcal{O}(h_{j_{|B|}})\rangle^{\mathrm{conn}}_K,
\end{equation*}
where $j_1,\dots,j_{|B|}$ enumerate $B$; the order is immaterial, since this function is symmetric
in its arguments. Write $\Pi_{\ge 2}(J)$ for the set of partitions of a finite set
$J$ into blocks of size at least two; for $J=\emptyset$ it consists of the empty partition, with empty
product $1$. Then $\langle\overline{\theta(F)}F\rangle_K=P_K(F)$, where
\begin{equation}\label{5.12:eq-limit-positivity-2}
P_K(F):=\sum_{\alpha,\beta}\bar c_\alpha c_\beta
\sum_{\pi\in\Pi_{\ge2}(\alpha'\sqcup\beta)}\ \prod_{B\in\pi}S^K_{|B|}\bigl((h_j)_{j\in B}\bigr).
\end{equation}
Let $P(F)$ be the same expression with $S^K_{|B|}$ replaced by $S_{|B|}$. Both $P_K(F)$ and $P(F)$
depend only on the coefficients $c_\alpha$ and the test functions $f_i$, not on the centring
constants.

In each term of \eqref{5.12:eq-limit-positivity-2}, every $f_i$ and every $\theta\bar f_i$ occurs at
most once. The supports of the $h_j$, $j\in\beta$, are pairwise disjoint by hypothesis. Those of the
$h_{i'}$, $i\in\alpha$, are pairwise disjoint because $\theta$ is a bijection and conjugation preserves
supports. The two families are disjoint from each other because they lie in
$\{0<x^{0}<\tfrac12\}$ and $\{-\tfrac12<x^{0}<0\}$ respectively. Hence each tensor product
$\bigotimes_{j\in B}h_j$ is supported in $\{x_i\ne x_j\}$. On that set the limits of
Proposition~\ref{5.12:prop-subsequential-limits} are defined and attained along $(K_{i_l})$, so
$S^{K_{i_l}}_{|B|}((h_j)_{j\in B})\to S_{|B|}((h_j)_{j\in B})$ as $l\to\infty$.

The sum \eqref{5.12:eq-limit-positivity-2} is finite and each term is a finite product. Therefore
$P_{K_{i_l}}(F)\to P(F)$. Since every $P_{K_{i_l}}(F)=\langle\overline{\theta(F)}F\rangle_{K_{i_l}}$ is
non-negative, so is the limit, which is \eqref{5.12:eq-limit-positivity-1}. Only cumulants of order at
least two, at pairwise disjoint supports, entered. This is why nothing is asserted for the one-point
functions ($n=1$) or at coinciding points.
\end{proof}
```

**C-F7 (filled: meaning of positivity).** The finite polynomial uses partitions into blocks of size at least two, since centered first cumulants vanish and higher cumulants are invariant under constant shifts. The empty index set contributes one. Every \(f_i\) occurs at most once in each positive-half monomial, and every reflected conjugate occurs at most once in the negative half. Compact disjoint supports are positively separated, so every block evaluation lies off the diagonals. Passage to the limit is through a finite sum of finite products. This proves precisely \(P(F)\ge0\) in 5.12:lem-limit-positivity. It does not prove a separate positivity condition on each connected cumulant, or full Osterwalder–Schrader reconstruction. Symmetry and common-lattice covariance are the identities proved in the preceding passage, not full continuum rotation invariance.

## B4b: exact one-loop implication

Named inputs: **O-flow** is the flow part of B3 with C-admitted, C-sites, C-B1 and all its own antecedents, restricted to the indicated reference run; at \(N\ge3\) it additionally requires C-rank, whose proof is outstanding. **O-Gaussian** is C-one-loop, 4.2:lem-one-loop (CA-I:3901–3930), explicitly used by statement from Balaban CMP 109 (1.22), Theorem 3, and CMP 116 (2.41). **O-identification** is 5.14:not-flow-notation (a)–(d), II:26779–26859: \(\beta_{k+1}=b_{k+1}(0)\) is the coefficient of the **complete regular part, including large-field remainders**, not only its Gaussian normalizer. **O-passage** is the first-passage property of clause (0), invoked in that notation. These are the precise hypotheses of the one-loop implication, not new results established here.

Here \(K=\min\{k:x_k\le X+B^\sharp\}\), whereas the correlation theorem's \(K_J\) is the last index all of whose earlier \(x_j\) exceed \(X\). The identity of the runs and O-passage give \(K\le K_J\), so the flow bounds apply on the entire interval needed. Keep the same \(c_0=11N^2\log L/(12\pi^2)\), \(\lambda=c_0/2\), \(c_2\), and \(C_{\mathfrak m}=5/2+5/[\lambda(\kappa_0-4)]\). No change of coupling normalization is made.

The source's scalar function is
\[
e(g')=\frac{4E^*A_1}{\varepsilon_1}g'(\log g'^{-2})^{p_0}
 +E^*\exp[-\gamma_2A_1^2(\log g'^{-2})^{2p_0}/4],
\]
and \(v_k=2C_\beta C_tC_{\mathfrak m}y_k^{-(\kappa_0-4)/2}\),
\(y_k=\min_{i\le k}x_i-2c_2\). This is exactly 5.14:eq-flow-notation-c. The majorants and their proof follow, before the full theorem proof.

### Exact majorant definitions and their full proof

CA-II:26967–27040. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{definition}[Cutoff-free majorants of the per-step defects]\label{5.14:def-defect-majorants}
Let $c_0$, $c_2$ be the constants of the one-loop lemma, and let $\lambda=c_0/2$, $C_{\beta}$,
$C_t$, $C_{\mathfrak{m}}$, $\kappa_0$ and the function $e(g')$ be as in
Notation~\ref{5.14:not-flow-notation}, display~\eqref{5.14:eq-flow-notation-c}. We put
\begin{equation}\label{5.14:eq-defect-majorants-a}
\begin{aligned}
\bar{h}_u &:= (6c_2+4+\lambda u)^{-1/2} && (u\ge 1),\\
\mathfrak{e}_u &:= \sup\{\,e(g') : 0<g'\le \bar{h}_u\,\} && (u\ge 1),\\
\mathfrak{v}_u &:= 2C_{\beta}C_tC_{\mathfrak{m}}\,(4+\lambda u)^{-(\kappa_0-4)/2}
  && (u\ge 1),\\
C_v &:= \sum_{u=1}^{\infty}\mathfrak{v}_u, &&\\
\delta_e(s) &:= \frac{1}{s}\sum_{u=1}^{s}\mathfrak{e}_u && (s\ge 1),\\
\Delta(s) &:= 2c_2 + C_v + C_{\beta}\, s\,\delta_e(s) && (s\ge 1),\\
\Delta(0) &:= 2c_2 + C_v. &&
\end{aligned}
\end{equation}
Thus $\Delta(s)=2c_2+C_v+C_{\beta}\sum_{u=1}^{s}\mathfrak{e}_u$ for every $s\ge 0$, the sum
being empty for $s=0$.
Each of these quantities depends on $(L,N,\mathfrak{p})$ only, through $c_2$, $\lambda$,
$C_{\beta}$, $C_t$, $C_{\mathfrak{m}}$, $\kappa_0$ and the parameters $A_1$,
$\varepsilon_1$, $E^{*}$, $\gamma_2$, $p_0$ that enter $e(\cdot)$. None of them depends on
$K$, $g$, $g_0$, $m$, $s(\mathsf{d})$ or a position on the lattice; they are defined
quantities, not hypotheses, and no numerical value is assigned to any of them. The sequence
$\bar{h}_u$ is strictly decreasing with $\bar{h}_u\le\tfrac12$ and $\bar{h}_u\to 0$; each
$\mathfrak{e}_u$ is finite and $u\mapsto\mathfrak{e}_u$ is non-increasing; and $C_v<\infty$.
The quantity $\delta_e(s)$ is the Ces\`aro mean of $(\mathfrak{e}_u)_{u\ge1}$. That
$\mathfrak{e}_u\to 0$ as $u\to\infty$ and $\delta_e(s)\to 0$ as $s\to\infty$, and hence
$\Delta(s)/s\to 0$, is proved in the proof of the statement on exact one-loop running below.
\end{definition}

\begin{proof}
Since $c_0>0$ we have $\lambda>0$, so $u\mapsto 6c_2+4+\lambda u$ is strictly increasing and
tends to $+\infty$; therefore $\bar{h}_u$ is strictly decreasing and $\bar{h}_u\to 0$. As
$c_2\ge 0$ and $\lambda u>0$, we have $6c_2+4+\lambda u\ge 4$, whence
$\bar{h}_u\le 4^{-1/2}=\tfrac12<1$.

By display~\eqref{5.14:eq-flow-notation-c},
\begin{equation*}
e(g') = \frac{4E^{*}A_1}{\varepsilon_1}\,g'\,(\log g'^{-2})^{p_0}
 + E^{*}\exp\!\Bigl(-\tfrac14\gamma_2A_1^{2}(\log g'^{-2})^{2p_0}\Bigr).
\end{equation*}
For $0<g'<1$ one has $\log g'^{-2}>0$, so both terms are continuous on $]0,1[$. As
$g'\downarrow 0$, $\log g'^{-2}\to+\infty$; the first term tends to $0$ because $g'$ times a
fixed power of $\log g'^{-2}$ tends to $0$, and the second tends to $0$ because its exponent
tends to $-\infty$. Hence $e$ extends to a continuous function on $[0,\bar{h}_u]$, which is a
compact subset of $[0,1[$ because $\bar{h}_u\le\tfrac12$; it is therefore bounded there, and
$\mathfrak{e}_u<\infty$. Since $\bar{h}_{u+1}<\bar{h}_u$, the interval
$]0,\bar{h}_{u+1}]$ is contained in $]0,\bar{h}_u]$, and a supremum over a smaller set is not
larger; thus $\mathfrak{e}_{u+1}\le\mathfrak{e}_u$.

For $C_v$: since $\kappa_0\ge 7$, the exponent satisfies $(\kappa_0-4)/2\ge 3/2>1$. Because
$4+\lambda u\ge 1$, raising it to the larger negative power gives a smaller number, so
\begin{equation*}
\mathfrak{v}_u\le 2C_{\beta}C_tC_{\mathfrak{m}}\,(4+\lambda u)^{-3/2}\qquad(u\ge 1).
\end{equation*}
The function $t\mapsto(4+\lambda t)^{-3/2}$ is decreasing on $[0,\infty[$, so
$(4+\lambda u)^{-3/2}\le\int_{u-1}^{u}(4+\lambda t)^{-3/2}\,dt$ for every $u\ge1$. Summing
over $u\ge1$,
\begin{equation*}
C_v \le 2C_{\beta}C_tC_{\mathfrak{m}}\sum_{u\ge 1}(4+\lambda u)^{-3/2}
 \le 2C_{\beta}C_tC_{\mathfrak{m}}\int_{0}^{\infty}(4+\lambda t)^{-3/2}\,dt
 = \frac{2C_{\beta}C_tC_{\mathfrak{m}}}{\lambda},
\end{equation*}
where the integral equals
$\bigl[-\tfrac{2}{\lambda}(4+\lambda t)^{-1/2}\bigr]_{0}^{\infty}=\tfrac{2}{\lambda}\cdot
\tfrac12=\tfrac1\lambda$. Thus $C_v<\infty$.

Finally, dividing the definition of $\Delta(s)$ by $s$ gives
\begin{equation*}
\frac{\Delta(s)}{s} = \frac{2c_2+C_v}{s} + C_{\beta}\,\delta_e(s),
\end{equation*}
so $\Delta(s)/s\to 0$ as soon as $\delta_e(s)\to 0$, the first term tending to $0$ because
$2c_2+C_v$ is finite.
\end{proof}
```

**O-F1 (filled: domain of the scalar majorant).** The notation initially defines \(e\) for \(g'\le\gamma_J\), while \(\bar h_u\) need not be at most \(\gamma_J\). Read the displayed algebraic formula as its extension to \(0<g'<1\), as the majorant proof itself does; set \(e(0)=0\). This defines the supremum without asserting any physical estimate above \(\gamma_J\). The latter estimates are used only on the admitted run. For the first term, put \(t=\log g'^{-2}\), so it is a constant times \(e^{-t/2}t^{p_0}\); the elementary exponential-versus-power estimate in W5-F3 proves its limit zero. The second term tends to zero since \(p_0,\gamma_2,A_1>0\). Continuity on \([0,\bar h_u]\) proves finiteness; shrinking intervals give monotonicity. For \(C_v\), the source's decreasing-integral comparison gives exactly
\(\int_0^\infty(4+\lambda t)^{-3/2}dt=1/\lambda\), with no numerical integration.

### Full proof of 5.14:thm-one-loop-law

CA-II:27120–27305. Complete original passage (Sussman–Alpoge, with Claude and Codex).

```latex
\begin{proof}[Proof of Theorem~\ref{5.14:thm-one-loop-law}]
\emph{Step 0: one sequence, and the range of the flow statement.} Under the identification, recorded
in Notation~\ref{5.14:not-flow-notation}, of the correlation theorem's coupling increment with that of
the flow \eqref{5.14:eq-flow-notation-a}, both being Ba{\l}aban's coefficient of the complete regular
part, for every $k\le K$ the number $x_k$ of
\eqref{5.14:eq-flow-notation-a} is the reference value of the correlation theorem; the increment
function of the correlation theorem at zero shift satisfies $b_{k+1}(0)=\beta_{k+1}$; the coefficients
$\beta^{0}_{l}$ of the correlation theorem are the coefficients $\beta^{0}_{l}$ of the Gaussian
normalisers of the steps to which the one-loop lemma applies, and the one-loop bound used in the
correlation theorem is the one-loop lemma \eqref{5.14:eq-flow-notation-b}. Moreover $K\le K_J$, where
$K_J$ is the stopping index of the correlation theorem, that is, the largest $k$ with $x_{k'}>g^{-2}$
for all $k'\le k$: indeed $x_k>g^{-2}$ for every $k\le K$ by the first-passage lemma of clause~(0) of
Theorem~0. The hypotheses under which the correlation theorem
asserts the bounds \eqref{5.14:eq-flow-notation-d} are met: $g\le\gamma_J$ by (H7); and
$x_0=g_0^{-2}\ge g^{-2}+B^{\sharp}>g^{-2}$ by the choice $g_0\le g_{-}(g)$ (hypothesis (H6) of
Theorem~0), so the initial value exceeds the reference value $g^{-2}$, as
\eqref{5.14:eq-flow-notation-d} requires. Moreover no constant
in \eqref{5.14:eq-flow-notation-d} depends on $K$, $k$, $m$, the torus or the position; hence
hypothesis (H5) of Theorem~0 on the torus plays no role here, and $m$ enters nothing below. Since
$K\le K_J$, the
two-sided linear flow window in \eqref{5.14:eq-flow-notation-d} holds for all pairs $0\le i<j\le K$,
and the closeness bound in \eqref{5.14:eq-flow-notation-d},
\begin{equation}\label{5.14:eq-one-loop-law-2}
\bigl|b_{k+1}(0)-\beta^{0}_{k+1}\bigr|\le C_\beta\,e(g_k)+v_k,
\end{equation}
holds for all $0\le k\le K-1$.

\emph{Step 1: telescoping.} Fix $0\le i<j\le K$. By \eqref{5.14:eq-flow-notation-a} and Step~0,
$x_{l-1}-x_l=\beta_l=b_l(0)$ for $1\le l\le K$. Summing over $l=i+1,\dots,j$ and adding and
subtracting $\beta^{0}_{l}$ in each term,
\begin{align}
x_i-x_j&=\sum_{l=i+1}^{j}\bigl(x_{l-1}-x_l\bigr)=\sum_{l=i+1}^{j}b_l(0)\notag\\
&=\sum_{l=i+1}^{j}\beta^{0}_{l}+\sum_{l=i+1}^{j}\bigl(b_l(0)-\beta^{0}_{l}\bigr).
\label{5.14:eq-one-loop-law-3}
\end{align}

\emph{Step 2: the one-loop lemma, used at both ends.} The one-loop lemma
\eqref{5.14:eq-flow-notation-b}, applied at $k=j$ and at $k=i$, bounds each of
$\bigl|\sum_{l=1}^{j}\beta^{0}_{l}-j\,c_0\bigr|$ and $\bigl|\sum_{l=1}^{i}\beta^{0}_{l}-i\,c_0\bigr|$
by $c_2$. Writing the partial sum from $i+1$ to $j$ as the difference of the partial sums from $1$ to
$j$ and from $1$ to $i$, and using the triangle inequality,
\begin{align}
\Bigl|\sum_{l=i+1}^{j}\beta^{0}_{l}-(j-i)\,c_0\Bigr|
&=\Bigl|\Bigl(\sum_{l=1}^{j}\beta^{0}_{l}-j\,c_0\Bigr)
-\Bigl(\sum_{l=1}^{i}\beta^{0}_{l}-i\,c_0\Bigr)\Bigr|\notag\\
&\le c_2+c_2=2c_2.
\label{5.14:eq-one-loop-law-4}
\end{align}

\emph{Step 3: the closeness bound, summed.} For each $l$ with $i+1\le l\le j$ put $k:=l-1$; then
$k\in\{i,\dots,j-1\}\subset\{0,\dots,K-1\}$, so \eqref{5.14:eq-one-loop-law-2} applies at this $k$ by
Step~0 and gives
\begin{equation*}
\bigl|b_l(0)-\beta^{0}_{l}\bigr|\le C_\beta\,e(g_{l-1})+v_{l-1}.
\end{equation*}
Subtract $(j-i)c_0$ from both sides of \eqref{5.14:eq-one-loop-law-3}, apply the triangle inequality,
bound the first sum by \eqref{5.14:eq-one-loop-law-4} and each term of the second sum by the last
display, and re-index the second sum by $k=l-1$:
\begin{align}
\bigl|x_i-x_j-(j-i)\,c_0\bigr|
&\le 2c_2+\sum_{l=i+1}^{j}\bigl|b_l(0)-\beta^{0}_{l}\bigr|\notag\\
&\le 2c_2+\sum_{k=i}^{j-1}\bigl[C_\beta\,e(g_k)+v_k\bigr].
\label{5.14:eq-one-loop-law-5}
\end{align}
This is \eqref{5.14:eq-one-loop-law-a}.

Now let $1\le s\le K$ and take $i=K-s$, $j=K$ in \eqref{5.14:eq-one-loop-law-a}, and substitute
$u:=K-k$, so that $k=K-u$ and $k$ runs over $K-s,\dots,K-1$ exactly when $u$ runs over $1,\dots,s$.
The defects summed are those of the $s$ steps from level $K-s$ to level $K$. This gives the first
inequality of \eqref{5.14:eq-one-loop-law-b}. For $s=0$ the left side of
\eqref{5.14:eq-one-loop-law-b} vanishes, the sum on the right is empty, and the first inequality reads
$0\le 2c_2$, which holds because $c_2$ bounds an absolute value in \eqref{5.14:eq-flow-notation-b}.

It remains to prove the second inequality in \eqref{5.14:eq-one-loop-law-b}, the limit
$\Delta(s)/s\to 0$ with its uniformity, and the consequence \eqref{5.14:eq-one-loop-law-c}. For $s=0$
the three members of \eqref{5.14:eq-one-loop-law-b} read $0\le 2c_2\le 2c_2+C_v$, since the sums are
empty and $C_v\ge 0$ as a sum of majorants of the non-negative numbers $v_k$. Throughout what follows,
$g\le\gamma_J$, $g_0\in\left]0,g_{-}(g)\right]$, $K=K(g_0,g)$, and $1\le s\le K$.

We use the lower member of the two-sided linear flow window in \eqref{5.14:eq-flow-notation-d}. It reads
\begin{equation}\label{5.14:eq-one-loop-law-6}
x_i-x_j\ge\lambda\,(j-i)-2c_2,\qquad \lambda=\frac{c_0}{2},
\end{equation}
and by Step~0 it holds for all $0\le i<j\le K$. Since $L>1$, \eqref{5.14:eq-one-loop-law-1} gives
$c_0>0$, hence $\lambda>0$. We also use two facts from clause~(0) of Theorem~0 and one from the
correlation theorem. First, $K$ is the first index $k\ge 0$ with $x_k\le g^{-2}+B^{\sharp}$, so
$x_K\le g^{-2}+B^{\sharp}$. Second, $x_K>g^{-2}$ by the first-passage lemma of clause~(0), as in Step~0.
Third, the coupling ceiling of the correlation theorem satisfies $\gamma_J\le(8c_2+4)^{-1/2}$, so
$g\le\gamma_J$ gives
\begin{equation}\label{5.14:eq-one-loop-law-7}
g^{-2}\ge 8c_2+4.
\end{equation}

\emph{Step 4: the couplings along the last $s$ steps.} Let $1\le u\le s$ and $0\le i\le K-u$. Then
$i<K$, and \eqref{5.14:eq-one-loop-law-6} applies to the pair $(i,K)$. Since $K-i\ge u$ and
$\lambda>0$, we obtain $x_i-x_K\ge\lambda(K-i)-2c_2\ge\lambda u-2c_2$. Together with $x_K>g^{-2}$ and
\eqref{5.14:eq-one-loop-law-7},
\begin{equation}\label{5.14:eq-one-loop-law-8}
x_i>g^{-2}+\lambda u-2c_2\ge 6c_2+4+\lambda u\qquad(0\le i\le K-u).
\end{equation}
For $i=K-u$, \eqref{5.14:eq-one-loop-law-8} says
$g_{K-u}^{-2}>6c_2+4+\lambda u=\bar{h}_u^{-2}$. Hence $0<g_{K-u}<\bar{h}_u$, where $\bar{h}_u$ is as in
Definition~\ref{5.14:def-defect-majorants}. Since $\mathfrak{e}_u$ is the supremum of $e(g')$ over
$0<g'\le\bar{h}_u$ (Definition~\ref{5.14:def-defect-majorants}, \eqref{5.14:eq-defect-majorants-a}),
\begin{equation}\label{5.14:eq-one-loop-law-9}
e(g_{K-u})\le\mathfrak{e}_u\qquad(1\le u\le s).
\end{equation}

\emph{Step 5: the remnant bounds.} The remnant bound of the correlation theorem is
$v_k=2C_\beta C_tC_{\mathfrak{m}}\,y_k^{-(\kappa_0-4)/2}$, where
$y_k=\min_{i\le k}x_i-2c_2$ and $C_{\mathfrak{m}}=5/2+5/(\lambda(\kappa_0-4))$. Take $k=K-u$ with
$1\le u\le s$. Taking the minimum over $0\le i\le K-u$ in \eqref{5.14:eq-one-loop-law-8} gives
\begin{equation*}
y_{K-u}>6c_2+4+\lambda u-2c_2=4c_2+4+\lambda u>0 .
\end{equation*}
The exponent satisfies $(\kappa_0-4)/2\ge 3/2>0$ because $\kappa_0\ge 7$, so
\begin{equation}\label{5.14:eq-one-loop-law-10}
v_{K-u}\le 2C_\beta C_tC_{\mathfrak{m}}\,\bigl(4c_2+4+\lambda u\bigr)^{-(\kappa_0-4)/2}
\qquad(1\le u\le s).
\end{equation}
The right side of \eqref{5.14:eq-one-loop-law-10} is built from $(L,N,\mathfrak{p})$ only. Because the
exponent is at least $3/2>1$, its sum over $u\ge 1$ converges. By
Definition~\ref{5.14:def-defect-majorants}, $\mathfrak{v}_u$ is the majorant of $v_{K-u}$ obtained
through this lower bound on $y_{K-u}$; hence $v_{K-u}\le\mathfrak{v}_u$ for $1\le u\le s$, and
$C_v=\sum_{u\ge 1}\mathfrak{v}_u$. Therefore
\begin{equation}\label{5.14:eq-one-loop-law-11}
\sum_{u=1}^{s}v_{K-u}\le\sum_{u\ge 1}\mathfrak{v}_u=C_v .
\end{equation}

\emph{Step 6: the second inequality in \eqref{5.14:eq-one-loop-law-b}.} Multiply
\eqref{5.14:eq-one-loop-law-9} by $C_\beta\ge 0$ and sum over $u=1,\dots,s$. Add
\eqref{5.14:eq-one-loop-law-11}. This gives
\begin{equation*}
2c_2+\sum_{u=1}^{s}\bigl[C_\beta\,e(g_{K-u})+v_{K-u}\bigr]
\le 2c_2+C_v+C_\beta\sum_{u=1}^{s}\mathfrak{e}_u=\Delta(s),
\end{equation*}
which is the second inequality in \eqref{5.14:eq-one-loop-law-b}.

\emph{Step 7: $\Delta(s)/s\to 0$, uniformly.} By Definition~\ref{5.14:def-defect-majorants},
$\bar{h}_u\downarrow 0$ as $u\to\infty$; and $e(g')\to 0$ as $g'\downarrow 0$, a property of the
correlation theorem's function $e$ (hypothesis~(a)). Let $\varepsilon>0$.
Choose $\eta>0$ with $e(g')\le\varepsilon$ for $0<g'\le\eta$, and then $u_0$ with
$\bar{h}_u\le\eta$ for $u\ge u_0$. For $u\ge u_0$ the supremum defining $\mathfrak{e}_u$ is taken over
a subset of $\left]0,\eta\right]$, so $0\le\mathfrak{e}_u\le\varepsilon$. Thus $\mathfrak{e}_u\to 0$.
For $s\ge u_0$,
\begin{equation*}
\frac1s\sum_{u=1}^{s}\mathfrak{e}_u\le\frac1s\sum_{u=1}^{u_0-1}\mathfrak{e}_u+\varepsilon ,
\end{equation*}
and the first term on the right tends to $0$ as $s\to\infty$, so
\begin{equation*}
\limsup_{s\to\infty}\frac1s\sum_{u=1}^{s}\mathfrak{e}_u\le\varepsilon .
\end{equation*}
Since $\varepsilon>0$ was arbitrary, the Ces\`aro means of $(\mathfrak{e}_u)$ tend to $0$. Therefore
\begin{equation*}
\frac{\Delta(s)}{s}=\frac{2c_2+C_v}{s}+C_\beta\cdot\frac1s\sum_{u=1}^{s}\mathfrak{e}_u\longrightarrow 0
\qquad(s\to\infty).
\end{equation*}
Every quantity in $\Delta(s)$, namely $c_2$, $C_v$, $C_\beta$ and the numbers $\mathfrak{e}_u$, depends
on $(L,N,\mathfrak{p})$ only. So $\Delta(s)$, and with it the convergence $\Delta(s)/s\to 0$, is the
same for every $K\ge s$, every $g\le\gamma_J$, every $g_0$, every $m$ and every position.

\emph{Step 8: the consequences.} Let $K\ge s$. Dividing \eqref{5.14:eq-one-loop-law-b} by $s\ge 1$ gives
\begin{equation*}
\Bigl|\frac{x_{K-s}-x_K}{s}-c_0\Bigr|\le\frac{\Delta(s)}{s}.
\end{equation*}
By Step~7 the right side tends to $0$ independently of $K$. Hence $(x_{K-s}-x_K)/s\to c_0$ as
$s\to\infty$, uniformly in $K\ge s$.

Now let $g_0^{(i)}\downarrow 0$ with $K_i:=K(g_0^{(i)},g)\ge s$ and $g_{K_i-s}\to g_{\infty,s}$ along a
subsequence of the corollary to clause~(0). Apply \eqref{5.14:eq-one-loop-law-b} at $g_0=g_0^{(i)}$
and combine it with $g^{-2}<x_{K_i}\le g^{-2}+B^{\sharp}$. This gives
\begin{equation*}
g^{-2}+s\,c_0-\Delta(s)\le x_{K_i-s}=g_{K_i-s}^{-2}\le g^{-2}+B^{\sharp}+s\,c_0+\Delta(s).
\end{equation*}
The upper bound keeps $g_{K_i-s}$ above a positive number independent of $i$, so $g_{\infty,s}>0$ and
$g_{K_i-s}^{-2}\to g_{\infty,s}^{-2}$. The closed interval above does not depend on $i$, so it contains
the limit. This is \eqref{5.14:eq-one-loop-law-c}. Dividing \eqref{5.14:eq-one-loop-law-c} by
$s\,c_0>0$, the endpoints are
\begin{equation*}
1+\frac{g^{-2}}{s\,c_0}-\frac{\Delta(s)}{s\,c_0}
\qquad\text{and}\qquad
1+\frac{g^{-2}+B^{\sharp}}{s\,c_0}+\frac{\Delta(s)}{s\,c_0};
\end{equation*}
since $g$ and $B^{\sharp}$ do not depend on $s$, both tend to $1$ by Step~7. Hence
$g_{\infty,s}^{-2}/(s\,c_0)\to 1$ as $s\to\infty$.
\end{proof}
```

**O-F2 (filled: indexing and the two lower bases).** In telescoping \(x_i-x_j\), increments have indices \(l=i+1,\ldots,j\), while defects \(e_k,v_k\) have \(k=l-1\). At \(i=K-s,j=K\), set \(u=K-k\); \(k=K-s,\ldots,K-1\) becomes \(u=s,\ldots,1\), so reordering gives exactly \(u=1,\ldots,s\), with no endpoint \(u=0\). For every \(i\le K-u\),
\[
x_i\ge x_K+\lambda(K-i)-2c_2
 >X+\lambda u-2c_2\ge6c_2+4+\lambda u.
\]
Hence \(g_{K-u}<\bar h_u\) and
\[
y_{K-u}>X+\lambda u-4c_2
 \ge4c_2+4+\lambda u\ge4+\lambda u.
\]
The last comparison bridges the tighter base in the proof to the weaker base in the **definition** of \(\mathfrak v_u\). Since the exponent is negative, it gives \(v_{K-u}\le\mathfrak v_u\). Neither constant changes. For \(s=0\), the left side is zero and the sum is empty; the declared \(\Delta(0)=2c_2+C_v\) bounds it.

**O-F3 (filled: uniform Cesàro conclusion and its limits).** Given \(\epsilon>0\), choose \(u_0\) so \(\mathfrak e_u<\epsilon\) for \(u\ge u_0\). Then
\[
s^{-1}\sum_{u=1}^s\mathfrak e_u
 \le s^{-1}\sum_{u<u_0}\mathfrak e_u+\epsilon.
\]
The finite head vanishes as \(s\to\infty\); \(u_0\) depends only on the fixed majorant data. Thus \(\Delta(s)/s\to0\) uniformly over the admitted \(K\ge s,g,g_0,m\), since none enters the majorant. The interval for a fixed-depth limit follows by adding \(X<x_K\le X+B^\sharp\) and using continuity of the inverse square: the reference upper bound \(x_{K-s}\le X+B^\sharp+3\lambda s+2c_2\) keeps the limiting coupling positive at fixed \(g,s\). Divide that interval by \(s c_0\) to get the stated ratio at fixed \(g\). This ratio limit is not uniform as \(g\downarrow0\), because \(X/(s c_0)\) would then be uncontrolled; the **increment-slope** and \(\Delta(s)/s\) assertions have the printed uniformity. The theorem neither constructs a unique subsequence nor asserts a sign for individual increments or any Schwinger-function conclusion.

## Named published and inherited hypotheses

Every entry in the following citation register is a **named hypothesis, cited at the displayed locus, not re-proved or independently checked against the original Balaban paper by this port**. Distinct theorem/formula numbers in a row retain their individual hypotheses. The register includes all Balaban citations in the five exact statements and the reproduced proof passages, plus the account's explicit chapter input list at CA-II:60235–60282. A bare paper citation retains only the invocation at its displayed CA locus; it is not a claim that the whole paper has been proved here.

The printed sentences have the stronger warning recorded separately below. Cited published theorems and sentences printed without proof are not assigned the same standing.

| Name | Balaban reference and exact cited locus | CA-II invocation lines |
|---|---|---|

| B001 | B-CMP102b: (7), (9)--(10), (170)--(171), (174), (178), (181), (190) | 60250 |
| B002 | B-CMP102b: Proposition~9 | 35633, 35669, 35706, 60249 |
| B003 | B-CMP102b: Sect.~F | 60252 |
| B004 | B-CMP102b: Sect.~G | 60253 |
| B005 | B-CMP102b: Theorem~1 | 35582, 35633, 35647, 35705, 60248 |
| B006 | B-CMP109: (2.1)--(2.12) | 60254 |
| B007 | B-CMP109: (3.26) | 34692, 35664 |
| B008 | B-CMP109: (3.27) | 35683 |
| B009 | B-CMP109: (3.30)--(3.32) | 35633, 35693 |
| B010 | B-CMP109: (3.32) | 35720 |
| B011 | B-CMP109: (3.38) | 35714 |
| B012 | B-CMP109: (3.39) | 35580 |
| B013 | B-CMP109: (3.40) | 35569 |
| B014 | B-CMP109: (4.16)--(4.18) | 35720 |
| B015 | B-CMP109: (4.18) | 35909, 35910 |
| B016 | B-CMP109: (paper cited without a numbered locus) | 26679, 35637 |
| B017 | B-CMP109: Lemma~4 | 35848 |
| B018 | B-CMP109: Lemma~4, pp.~276--277 | 60255 |
| B019 | B-CMP109: Sect.~2 | 60254 |
| B020 | B-CMP109: Sects.~3--5, (3.2)--(3.54), (4.1)--(4.36), (5.10) | 60256 |
| B021 | B-CMP109: \S3 | 35761 |
| B022 | B-CMP109: p.~278 | 35570 |
| B023 | B-CMP116: (1.26) | 59886 |
| B024 | B-CMP116: (1.32) | 2819 |
| B025 | B-CMP116: (1.42)--(1.43), (2.1)--(2.42) | 60262 |
| B026 | B-CMP116: (2.1)--(2.13), (2.27)--(2.41) | 2804 |
| B027 | B-CMP116: (2.41) | 25381 |
| B028 | B-CMP116: (paper cited without a numbered locus) | 2834 |
| B029 | B-CMP116: Lemma~1, p.~9 | 60257 |
| B030 | B-CMP116: Lemma~2, p.~11 | 60258 |
| B031 | B-CMP116: Lemma~3 | 60259 |
| B032 | B-CMP116: \S1, (1.9)--(1.29) | 60260 |
| B033 | B-CMP119: (2.28) | 26768 |
| B034 | B-CMP119: (2.30)--(2.32) | 25446, 25471 |
| B035 | B-CMP119: (2.42) | 25438, 25439, 25441 |
| B036 | B-CMP119: (2.43)--(2.46) | 59657, 59741 |
| B037 | B-CMP119: (2.47)--(2.48) | 59659, 59744 |
| B038 | B-CMP119: (2.49) | 59755, 59767 |
| B039 | B-CMP119: (2.5) | 36365 |
| B040 | B-CMP119: (2.50) | 59804 |
| B041 | B-CMP119: (2.6)--(2.9) | 26669 |
| B042 | B-CMP119: (3.2), (3.3), (3.16) | 25355, 25392 |
| B043 | B-CMP119: (paper cited without a numbered locus) | 2824, 25395, 25400, 26703, 36073 |
| B044 | B-CMP119: Corollary~3 | 59769 |
| B045 | B-CMP119: Sect.~3, (3.2)--(3.68) | 60265 |
| B046 | B-CMP119: Theorem~1, Lemma~4, Corollary~3, (2.19)--(2.22), (2.27), (2.30)--(2.50) | 60263 |
| B047 | B-CMP119: \S2 | 26658 |
| B048 | B-CMP119: p.~276 | 35761 |
| B049 | B-CMP122a: (1.11) | 36161 |
| B050 | B-CMP122a: (1.24) | 2814 |
| B051 | B-CMP122a: (1.60)--(1.63), (1.65)--(1.70), (1.84), pp.~188--189 | 60268 |
| B052 | B-CMP122a: (paper cited without a numbered locus) | 36091, 36103, 36145, 36157, 36331 |
| B053 | B-CMP122a: p.~190, (1.64) | 60266 |
| B054 | B-CMP122b: (1.11), (1.23)--(1.48) | 60279 |
| B055 | B-CMP122b: (1.33) | 36216 |
| B056 | B-CMP122b: (1.49)--(1.65) | 60270 |
| B057 | B-CMP122b: (1.61)--(1.63) | 45202 |
| B058 | B-CMP122b: (1.66) | 45208, 45639 |
| B059 | B-CMP122b: (1.66)--(1.72), (1.74)--(1.99), (1.103)--(1.104), (2.21) | 60272 |
| B060 | B-CMP122b: (1.67) | 25439, 25442, 45640 |
| B061 | B-CMP122b: (paper cited without a numbered locus) | 59736, 59770, 59802 |
| B062 | B-CMP122b: Theorem~1 | 2795, 60274 |
| B063 | B-CMP122b: p.~368, after (1.46)--(1.48) | 60277 |
| B064 | B-CMP122b: p.~375 | 60276 |
| B065 | B-CMP122b: text following (1.66) | 45199, 45267 |
| B066 | B-CMP98: (11), (97), (148) | 60240 |
| B067 | B-CMP98: Proposition~2 | 34694, 35633, 35657, 35705, 35729, 60239 |
| B068 | B-CMP99a: (1.3)--(1.6) | 60242 |
| B069 | B-CMP99b: (3.19), (3.35)--(3.36), (3.108), (3.113)--(3.114), (3.128)--(3.129), (3.138), (3.154)--(3.156), (3.158), (3.161), (3.168)--(3.169), (3.185), (3.187) | 60245 |
| B070 | B-CMP99b: Theorems~3.1--3.11 | 60243 |
| B071 | B-CMP99b: Theorem~3.15 | 60244 |

**B-ONELOOP**, in addition to those rows: CMP 109 (1.22), Theorem 3; CMP 116 (2.41), at CA-I:3901–3930, and its telescoping/determinant comparison at 3930–4030. The declaration cites these results by statement; CA-I:56361–56368 later calls its proof incomplete at one step. This **source-status discrepancy is unresolved**, as P5-H-loop already records. O-Gaussian/C-one-loop remains a cited/open named premise; this port does not infer the finite-part theorem from the formal coefficient or P3.

**B-COVER-PRINTED:** CMP 119 p.276 transfers CMP 109 §3 and Lemmas 5–6 to the cover; CA-II:35065–35069, 35761–35777. **Printed without proof**, W5-cover. Its complex averaging use additionally needs W5-sixth.

**B-OLD-PRINTED:** CMP 122b p.375, bounds for old terms beside a new region; CA-II:60274–60276. **Printed without proof**, retained in C-admitted/C-Mfree's applications.

**B-REM-PRINTED:** CMP 122b p.368 after (1.46)–(1.48), smallness of the sum of localized remainders from localization/exponentiation (1.11), (1.23)–(1.48); CA-II:60277–60280. **Printed without proof**. This is distinct from merely bounding one piece.

**B-ENLARGED-PRINTED:** CMP 122b p.379, bound on the enlarged island with a different constant; CA-I:21394–21398, P5-B-enlarged-interaction. **Printed without proof** and distinct from interaction locality.

The following inherited printed-sentence and cited-theorem registers are carried from [P5](p5-induction.md), §§“Printed-sentence frontier” and “Cited theorem frontier.” Names retain P5's prefix so no source is silently renamed. These are inherited through representation/operator inputs, not a claim that each is a direct premise of every scalar calculation above.

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

### Inherited open representation inputs

The following table is carried from P5's named frontier at this checkout. The **only standing change in this copied table** is the owner's explicit update of oc to proved and refereed. The other already supplied results keep the owner's standings stated at the top of this note. “Unresolved” means no completion is used in this port, not a fresh audit of all downstream work. The source loci and the descriptive-name inputs below are recovery pointers; their long proofs are not re-ported here.

| Name | CA label | CA locus | Source standing recorded in chain-ca | Standing carried here |
|---|---|---|---|---|
| F01 | `2.4:prop-m-freeness` | I:2239 | incomplete, I:2239 | Carried unresolved input; no completion invoked here. |
| F02 | `4.2:lem-unmarked` | I:4031 | incomplete, I:4031 | Carried unresolved input; no completion invoked here. |
| F03 | `4.4:prop-local-real-base` | I:8110 | outstanding, I:8110 | lrb: proved and refereed, with its inherited inputs. |
| F04 | `4.5:lem-uniform-increment` | I:16019 | incomplete, I:16019 | ui: completed and checked, with its inherited inputs. |
| F05 | `4.12:prop-reblocking-inside` | I:44127 | incomplete, I:44128 | Carried unresolved input; no completion invoked here. |
| F06 | `4.12:prop-reblocking-outside` | I:45085 | outstanding, I:45085 | Carried unresolved input; no completion invoked here. |
| F07 | `4.13:lem-minimizer-unique` | I:45162 | outstanding, I:45163 | mu: proved and refereed, at its stated/use scope. |
| F08 | `4.13:lem-own-constant` | I:45203 | outstanding, I:45204 | oc: proved and refereed (owner update); inherited gauge inputs retained. |
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

### P4's additional explicitly printed suppliers

The checked standing of P4 does not remove these named hypotheses:

| Name | Exact published locus | CA-I locus and standing |
|---|---|---|
| 4.5:rem-covariance-inverse-walks | CMP 99b §3 before (3.132), inverse constrained covariance \(\mathsf q_0\) bounds and intrinsic walks | 13142–13173; printed without proof. |
| 4.5:rem-averaging-analyticity | CMP 98 §E p.43 after (164), complex analytic extension of averaging derivative bounds (156)–(157) | 13175–13197; printed without proof. |
| 4.5:rem-block-curvature-complex | CMP 109 p.263 and (3.26), p.275; extension p.277 | 13198–13249; printed without proof, only where the literal-frame variant is used. |

P4 also retains the explicitly named \(C_H\) corollary and auxiliary derivative/Landau-to-axial bounds (I:19376–19420, 19588–19590), glued-window regularity (I:17015–17055, 19591), level-\(j\) window identity (I:19592–19593), and frame BCH remainder hypothesis (I:19594–19596). They remain assumed at those loci. The original P4 table's older “not yet checked” wording for ui is superseded by the owner's **checked** standing in this task.

### External cross-reference ledger

For completeness, every label referenced by a quoted passage but not defined in another quoted passage is listed below. “Adopted” means the original definition/display, including its hypotheses, is used; it does not grant proof status. “Named hypothesis” means its full proof is not ported here. The main input tables give the stronger known standings and the repository replacements. Equation references remain equations, not invented theorems.

| Source label | CA-II declaration line | Use/standing in this port |
|---|---|---|

| 5.13:prop-sun-correlation | 60181 | Proof outstanding at II:60191; required only for general-rank application. |
| 5.14:eq-flow-notation-a | 26786 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.14:eq-flow-notation-b | 26806 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.14:eq-flow-notation-c | 26829 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.14:eq-flow-notation-d | 26847 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.14:not-flow-notation | 26779 | Adopted definition with all attached hypotheses. |
| 5.1:def-admitted-inputs | 2084 | Adopted definition with all attached hypotheses. |
| 5.1:def-analyticity-spaces | 1754 | Adopted definition with all attached hypotheses. |
| 5.1:def-reference-recursion | 2030 | Adopted definition with all attached hypotheses. |
| 5.1:def-torus-floor | 679 | Adopted definition with all attached hypotheses. |
| 5.1:def-weight-classes | 2722 | Adopted definition with all attached hypotheses. |
| 5.1:eq-admitted-inputs-a | 2259 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-admitted-inputs-b | 2414 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-admitted-inputs-c | 2653 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-analyticity-spaces-a | 1776 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-analyticity-spaces-c | 1883 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-torus-floor-a | 711 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:eq-torus-floor-b | 736 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.1:not-coupling-functions | 1944 | Adopted definition with all attached hypotheses. |
| 5.2:def-auxiliary-torus | 24924 | Adopted definition with all attached hypotheses. |
| 5.2:def-comparison-constant | 7993 | Adopted definition with all attached hypotheses. |
| 5.2:def-induction-format | 25012 | Adopted definition with all attached hypotheses. |
| 5.2:def-rim-refinement | 11310 | Adopted definition with all attached hypotheses. |
| 5.2:def-three-families | 14139 | Adopted definition with all attached hypotheses. |
| 5.2:eq-disc-bounds-a | 2980 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.2:eq-induction-format-a | 25048 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.2:eq-induction-format-b | 25134 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.2:eq-plain-fine-units-a | 23328 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.2:lem-complex-weights | 5043 | Named hypothesis; full supplier proof not re-ported. |
| 5.2:lem-disc-bounds | 2974 | CA elementary proved implication; needed argument included in D-F1/D-F2. |
| 5.2:lem-enlargement-fractions | 25945 | Named hypothesis; full supplier proof not re-ported. |
| 5.2:lem-exterior-pieces | 24029 | Named hypothesis; full supplier proof not re-ported. |
| 5.2:lem-polydisc-gradient | 3023 | CA elementary proved implication; needed argument included in D-F1/D-F2. |
| 5.5:def-data-factor | 34549 | Adopted definition with all attached hypotheses. |
| 5.5:def-near-unit-classes | 34389 | Adopted definition with all attached hypotheses. |
| 5.5:def-weight-constants | 34664 | Adopted definition with all attached hypotheses. |
| 5.5:def-weight-inputs | 35007 | Adopted definition with all attached hypotheses. |
| 5.5:def-windowed-source | 34159 | Adopted definition with all attached hypotheses. |
| 5.5:eq-data-factor-a | 34630 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-near-unit-classes-a | 34407 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-near-unit-classes-b | 34472 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-weight-constants-a | 34779 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-weight-constants-b | 34813 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-weight-constants-c | 34712 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-weight-constants-d | 34846 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-weight-notation-a | 34138 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:eq-windowed-source-b | 34319 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.5:not-weight-notation | 34020 | Adopted definition with all attached hypotheses. |
| 5.6:def-decoupling-variables | 44708 | Adopted definition with all attached hypotheses. |
| 5.6:def-pieces | 44792 | Adopted definition with all attached hypotheses. |
| 5.6:eq-cauchy-estimates-a | 45013 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.6:eq-linear-sizes-a | 44670 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.6:eq-pieces-b | 44830 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.6:eq-pieces-c | 44863 | Adopted displayed relation on its stated domain; named premise unless derived above. |
| 5.6:lem-cauchy-estimates | 45009 | CA elementary proved implication; needed Cauchy route included in W6-F1 and source proof (a). |
| 5.6:lem-cauchy-factor | 44942 | CA elementary proved implication; needed Cauchy route included in W6-F1 and source proof (a). |
| 5.6:lem-rooted-sets | 45645 | Named hypothesis; full supplier proof not re-ported. |
| 5.6:lem-tree-cells | 45703 | Named hypothesis; full supplier proof not re-ported. |
| 5.6:lem-tree-length-adjunction | 45479 | Named hypothesis; full supplier proof not re-ported. |

### Non-Balaban inputs

Osgood's finite-dimensional separate-holomorphy theorem is used in the pure step with local boundedness explicitly supplied (II:25311–25316); finite-dimensional Cauchy, Schwarz, maximum principle, identity theorem and compactness of bounded scalar sequences are used on the domains specified above. C-compact retains the account's stated multilinear/distributional compactness lemma. C-positive retains Osterwalder–Seiler (OSe78), lattice reflection positivity and reflection invariance, exactly at II:60091–60096. These are mathematical input theorems, not numerical checks. The inherited covariance-root use of Combes–Thomas keeps the hypotheses recorded in P4 and C-admitted; no spectral gap or coercivity is inferred from a compressed form alone.

## Source navigation and current recovery checkpoint

The repository remains at e5d4b95fe9b7e5eede4d9535fedacd6a15a05353. The requested GOAL method, FINISH sections, chain-ca §7.2 and ca-full README governed this port. The prescribed docs/ai_methodology/SCIENCE_WORKFLOW.md is absent from this checkout; no replacement workflow was fabricated. No audit, PR, status update or external communication was undertaken.

Navigation used library/sa-index/README.md, relevant chunk rows and obligations, and ca-full/index.tsv and leaves.tsv, with neighbouring rows. The bounded outline context was the correlation/source discussion at SA:22502–22560 and 22861–22890 and the first-passage context at 19936–19996. The proofs here use the **complete account**, not an alternative outline derivation. Full account proof ranges are recorded immediately above each excerpt. Relevant declarations were checked at their source lines: in particular B1, C-Mfree, C-sixth and C-rank override misleading or absent structural-index statuses.

The [upstream README at the pinned revision](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/README.md), under “Collaboration”, permits use of all repository documents for any purpose. The complete source passages are reproduced under that permission, credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban receives the attribution at each published input; this port does not claim those inputs as new work.

The following SHA-256 identities are bookkeeping, not scientific verification:

| Source | SHA-256 |
|---|---|

| SA outline | d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f |
| CA-I | 4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93 |
| CA-II | 6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f |
| chain-ca | 5c3653be968613911d0afe5c40dfec070f39a205e5257acd38805d39a6642f79 |
| pointed irrelevance | e53e8f210c92cde4b4eb1bf5733a5378f88177183bd8eeab3d6abc00eb249b1e |
| P1 | 55230153fd7047d0c3e4e5bbc1fdd4339ae4f822bc4f2f08fb4d2fb90e877ac5 |
| P3 | fdcf9691f06dcabf973d3f25de934fd6ea7e75c74bcfbfa2ecc5049eb5233e53 |
| P4 | 4bd5bd700a453a1a1d87ad18e161ea1f629840b21fdf3a10b2ea9cd7f50d5fb2 |
| P5 | f181f10a7e018282d632217c7880812e844aa1123ecc4a4c03fd9fc25fc94d4b |
| mu | 2f3643c41fa8655a01ae8a6f7afa16c45f459bf41512c585acbeae63504a323b |
| lrb | 23b7d710a2dff388ac1adbededa2177a0a0bf02f97d12523ca9f9fb35552969d |
| oc | 914c4ab01ecda3dadb4f1f18d3c4b2f6684b3834cf08a1dd763e953a26044238 |
| ui | 68ab86d412b8587fe7729a44373f17b6097e6efea35d771053ded604583d9957 |

The current checkpoint is this completed conditional port. Recovery should start with its named-input tables and the source identities above, then revisit only changed suppliers or a disputed passage. Failed/unsupported shortcuts preserved here: replacing B1 by window holomorphy; inferring chain geometry from Cauchy; using only the driver value at zero; taking the eight induction steps as proved by their ordering; dropping the low-order variation exception; reading the fixed-\(m\) torus argument as \(m\)-uniform; and identifying P3's free calculation with the finite-part one-loop input. None was used.

Next mathematical decisions belong to the named-input work: B1/ph; window-data and stage admission; the local-data companion kernel; the sixth-family complex extension; low-order variation if the unrestricted difference total is needed; last-lattice uniformity if the theorem's blanket independence is retained; and the general-rank input if \(N\ge3\) is requested. The inherited P5 frontier and the cited/printed Balaban hypotheses remain attached. No completion is asserted for them.

Text verification: all 26 quoted passages match the pinned CA-II source exactly; all five requested statement labels are present, and the numbered fill/correction markers and text encoding were checked. The bookkeeping record is /tmp/p6-port/text-verification.json. These checks establish transcription and file consistency only, not mathematical correctness.

## Result

**Statements ported, on their own routes:** 5.6:lem-weight (all six clauses); 5.5:lem-weight (a1–a4, b, c, c′, d and the precise scope of e); 5.3:lem-driven-flow; 5.1:thm-correlation-theorem as its explicit conditional joint-induction and fixed-\((g,m,N_T)\) torus implication, with its stated off-diagonal subsequence/positivity consequences; and 5.14:thm-one-loop-law, conditional on the flow and cited finite-part bound. The exact source statements precede the complete proof passages. The two weight lemmas' different hypotheses and roles are reconciled above.

**Every added filled step:**

- W6-F1: Cauchy-radius limits, empty derivatives, datum-only constants and the scalar factor.
- W6-F2: component rooting, composition count, tree encoding and scale cancellation.
- W6-F3: the finite coordinate-product telescoping identity and empty subsets.
- W5-F1: identity-theorem continuation on the admitted common chart and the level restriction.
- W5-F2: the explicit straddling geometric series.
- W5-F3: exceptional-depth lower bound, geometric factor, finite suprema and empty-set convention.
- W5-F4: zero normalization in positive linear resummation.
- D-F1: the dimension-free polydisc-gradient argument, including zero sup bound.
- D-F2: the driving quotient, strict domain inclusion and adaptive induction.
- C-F1: the lexicographic induction and earlier-level frozen-data admission.
- C-F2: the source's prefix summability estimate, including the scalar-domain ceiling and integral comparisons.
- C-F3: stopping, adjacent radii, derivative and Lipschitz endpoints.
- C-F4: local shift recurrence and the exact mass identity.
- C-F5: zero tests, the ultraviolet geometric sum and the local logarithm domain.
- C-F6: dense-set extension while retaining the distributional compactness hypothesis.
- C-F7: the precise centered-cumulant positivity polynomial.
- O-F1: the scalar majorant's algebraic extension and convergence.
- O-F2: defect index shift, the two lower bases and depth zero.
- O-F3: uniform Cesàro convergence and the fixed-\(g\) subsequential ratio.

**Every correction:** W6-C1 repairs zero decay at infinite length; W5-C1 repairs degree language and the nonexistent (b′) reference; W5-C2 identifies data-constant aliases by formula; W5-C3 retains the low-order exception in the total; C-C1 supplies the already-stated whole-disc driver at the invocation; C-C2 reconciles flow/radius notation while retaining slot admission; C-C3 limits the demonstrated last-lattice uniformity to what the proof actually supplies; C-C4 repairs the compactness proof's torus-bound cross-reference. Constants and the original routes are otherwise retained. The one-loop supplier's inconsistent source status is recorded as unresolved, not repaired by declaration.

**Named hypotheses carried:** every W6 and W5 input row; C-admitted, C-boundary, C-preparation, C-B1, C-slots, C-frozen, C-sites, C-reference, C-one-loop, C-Mfree, C-sixth, C-last, C-compact, C-positive, C-rank and C-uniform-last on their indicated scopes; O-flow, O-Gaussian, O-identification and O-passage; all 71 published citation/locus entries, the separately named printed sentences, P5's inherited theorem and printed-sentence registers, F01–F35 with the owner-updated closed inputs, P5's descriptive open inputs, P4's additional suppliers, and the 59-label external-reference ledger. None is discharged by indexing, source copying or an analytic argument on an unadmitted domain.

Only library/port/p6-correlation.md changed. No editable prompt file or platform instruction changed. Source-transcription comparisons and file inventories are bookkeeping only; every mathematical argument here is textual and by hand. No run discharges a proof obligation. This is research text, not an audit; it grants no status and does not establish full T0.

**This text is not yet checked by another model.**
