# Last-scale constants in the Sussman–Alpoge complete account

Provenance: Codex, 2026-11-05, checkout `204610ca1ab6f259118a2655d87f44ef8f8ad92d`. Research proof lane; not an audit and grants no status. No computer-assisted proof steps.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the constructions and estimates the account uses.

Target: `6.3:lem-last-scale-constants`, the open last-scale input of Chapter 6, and hence of clauses (iii-b) and (ii-ℝ⁴). This note preserves the account's route and order of constants.

## 1. What must be proved

CA-I, II and III denote the three `theorem_0_complete_account_raw_*.tex` files at the credited revision. SA denotes `YM4_sketch_500.tex`. All source references below use their original line numbers.

The label at II:63365–63367 is a remark, not a written lemma statement. Parts (b)–(e) follow at II:63369–63833. There is no marked `(∗)` in this passage. Part (a), and the labels (I1)–(I3) mentioned at II:63701, are absent. III:110895–110899 calls the last-scale input incomplete; II:64603 says there are no incomplete chapter inputs. We keep the former declaration as the task's starting point. We do not invent a source sentence for the missing statement or marker.

The consumers specify its meaning:

- II:63531–63565 needs bounded per-site constants at a fixed omitted-step exponent.
- II:63907–63925 needs this bound uniformly in the physical torus exponent, followed by the finite maximum over changes of units.
- II:64255–64285 needs this bound only after the chessboard estimate has replaced total volume by cell volume.
- II:64436–64478 discusses the small-cutoff alternative and requires a local plaquette count.
- II:68357–68367 lists this input in the limit argument. No clause of (ii) supplies it.

Here is the reconstructed statement. Its hypotheses are the existing CA inputs, not new Yang–Mills assumptions. They retain their standing in the account.

**Lemma LSC (reconstruction of `6.3:lem-last-scale-constants`).** Fix the account's dimension four, group SU(2), normalized trace, odd $L$, auxiliary tuple $\mathfrak p$, coupling window $\gamma$, terminal ceiling $\gamma_H<1$, and source radius $\varrho>0$, in their prescribed order. Retain clause (0), the identification $b_{k+1}(0)=\beta_{k+1}$, and the correlation theorem's construction and estimates. In particular, retain its source-free density, real-background, and sourced majorant inputs, specified in §3 below. Do not assume LSC or volume-free correlations.

Write
\[
X=g^{-2},\quad x_0=g_0^{-2},\quad
\lambda=c_0/2,\quad c_5=2c_2,\quad b_+=3\lambda+2c_2,
\quad g_-(g)=(X+B^\sharp)^{-1/2}.
\]
The common numerical flow has
\[
K=\min\{k:x_k\le X+B^\sharp\},\qquad
K_J=\max\{k:x_j>X\text{ for all }j\le k\}.
\]
Clause (0) gives $X<x_K\le X+B^\sharp$, $K\to\infty$ as $g_0\downarrow0$, and the flow up to $K$. The correlation theorem gives
\[
\lambda(j-i)-2c_2\le x_i-x_j\le3\lambda(j-i)+2c_2,
\qquad X<x_{K_J}\le X+b_+ .                         \tag{1}
\]
The numerical flow and its coefficients are independent of the torus.

Let $R_J(x)$ be the least integer power of $L$ at least $(\log x)^r$, with the radius exponent of the common admitted parameter tuple. Define
\[
N_{\mathbb T}(g,m)=L^{11}M\sup_{u\ge0,\ u\in\mathbb Z}
 L^{-u}R_J\bigl(X+b_++4c_2+3\lambda(m+u)\bigr),
\quad m_J=m^J_{\mathbb T}(g)=\min\{m\ge0:L^m\ge N_{\mathbb T}(g,m)\}.
                                                               \tag{2}
\]
The radius exponent $r$ here is $r_{\rm pr}$ in Chapter 5; that chapter's source-disc radius $r$ is our $\varrho$. Chapter 5 restricts its radius powers to nonnegative exponents (II:688–699). The conventions agree on the admitted range: $\gamma_J\le(8c_2+4)^{-1/2}\le1/2$ (II:2865–2868), so every argument of $R_J$ used here is at least $X\ge4$.

Distinguish this $m_J$ from the physical torus floor

\[
m_{\mathbb T}(g_-)=11+m'+\log_LR(g_-),\qquad M=L^{m'}.
\]

Put
\[
\mathcal A=\{0\}\cup\{a\in\mathbb Z_{\ge1}:\lambda a<B^\sharp+c_5\},
\qquad a^\natural=\max\mathcal A .                         \tag{3}
\]
Choose $0<g\le\min\{\gamma_H,\gamma_J,\gamma_D\}$, where $\gamma_D$ ensures
\[
m_{\mathbb T}(g_-),m_J\ge a^\natural.
\]
Take any integer $m_1\ge m_{\mathbb T}(g_-)$, any $0<g_0\le g_-(g)$, and the bare lattice of spacing $L^{-K}$ in the torus of side $2L^{m_1}$. For real Lipschitz sources, let $S^T_n$ be the joint cumulant of
\[
\mathcal O(f)=\sum_p f(x(p))[1-\operatorname{Re}\operatorname{tr}U(\partial p)],
\qquad \|f\|_\sharp=\max\{\|f\|_\infty,40M\operatorname{Lip}f\}.
\]

**(a) Bounded offset.** $K\le K_J$ and $a=K_J-K\in\mathcal A$.

**(b) Last-scale constants.** If $K_J\ge m_J$, set
\[
K'=K_J-m_J=K-b,\quad b=m_J-a,\quad
N_T=2L^{m_1-a},\quad N=N_TL^{m_J}=2L^{m_1+b}.                \tag{4}
\]
These are admissible correlation-theorem data. Dilation to its side-one torus identifies the bare measures and source cumulants. Its source norm is no larger than $\|f\|_\sharp$. Moreover
\[
X<x_{K'}\le x^*(g):=X+b_++3\lambda m_J+2c_2,
\quad E_+^\sharp+C_{\rm low}\le E_*(L,\mathfrak p,g,\varrho)<\infty. \tag{5}
\]
The bound is uniform in $K,g_0,m_1,a,N_T,N$ and source positions. Here $E_+^\sharp,C_{\rm low}$ are chosen valid per-site bounds for the account's sourced remainder and its zero-source floor, in the same source-independent vacuum normalization. Their sum is unchanged by a common change of that normalization.

**(c) Change of units.** Let $n\ge2$, $R,d>0$, and let $\ell(n,R)$ be the least power of $L$ at least $8n(R+1)$. Also require $L^{m_1}\ge L^{m_J}\ell(n,R)$. For the class $\mathfrak S(n,R,d)$ of II:63098–63118, in Case A, $K_J\ge m_J$,
\[
|S^T_n(\vec f)|\le C^*_n(d;R)\prod_i\|f_i\|_\sharp,\qquad
C^*_n(d;R)=\max_{b\in\mathcal B(g)}\Phi_{n,dL^b,RL^b}(E_*),       \tag{6}
\]
where $\mathcal B(g)=\{m_J-a:a\in\mathcal A\}\subset[0,m_J]$ and
\[
\Phi_{n,d',R'}(t)=\left[2C_{\rm UV}(d';R')+
(\log2)\mathfrak r^n
\left(2e^{n[t\ell(n,R')^4+2C_{\rm face}(R')]}+2\right)^n\right]
\left(\frac n\varrho\right)^n .                              \tag{7}
\]
The coefficients are exactly those of II:63633–63640 and `6.4:eq-per-ball-bound-b`. $C^*_n$ depends only on the fixed data and $n,d,R$, and is non-increasing in $d$.

**(d) Remaining cutoffs.** In Case B, $K_J<m_J$, for $n\ge1$ and $\vec f\in\mathfrak S(n,R)$,
\[
|S^T_n(\vec f)|\le C^B_n(R)\prod_i\|f_i\|_\infty,
\quad C^B_n(R)=c_n[12(2R+3)^4]^nL^{4nm_J},
\quad c_n=\sum_{\pi\in\operatorname{Part}(n)}(|\pi|-1)!.        \tag{8}
\]
Thus, under part (c)'s torus floor, the maximum of (6) and (8) applies at every bare coupling, uniformly in the physical torus. Section 6.4 also proves the bound under the original floor of (iii-b).

**(e) Limits.** At fixed $g,m_1$, every sequence $g_0\downarrow0$ eventually lies in Case A. It has a subsequence with fixed $a,N_T,m_J,b$, along which the correlation theorem's fixed-data limit clauses apply. The estimates hold in their respective cases along the full sequence; their combined bound needs no extraction.

The declaration of dependence on $L,\mathfrak p,g,\varrho$ follows CA's convention that $\gamma$ and its choices are already fixed. It does not assert uniformity while varying that earlier window.

## 2. Comparison before proof

The outline index was searched first, including neighbouring rows and `obligations.md`. The relevant source passages are SA:22504–22550, 23165–23196, 23481–23539, and 23767–23866. The outline's positive-label floor is conditional on its background action and test estimates. Its explicit SU(2) Haar calculation is useful below. It does not prove the CA offset and unit-matching lemma.

- `sr1.md`, lines 38–65, imports uniform upper stability and the floor as UV1/D1. Its later transfer argument cannot supply those imports.
- `cl1.md`, lines 57–74, imports first passage and SR1's bounds. It does not supply last-scale uniformity.
- Frozen `o4-two-point.md`, lines 31–46, uses CA (iii-b) at $n=2$, at CA standing. It is a consumer of LSC.
- `port/p1-base.md`, §2, already ports first passage and two-sided flow arithmetic. We use it for $K\to\infty$ and the terminal interval. It does not compare $K$ and $K_J$.
- `port/p4-operator.md` ports operator, local independence and regularity implications, with their named hypotheses. These do not state a partition-function floor or the comparison in (4). Its §A9-F9 is a related constant-choice argument, not LSC.

A further CA comparison is useful: `8.8:lem-stability-exponent`, II:109859–110014, already proves the small-field integral floor from the lower density and the minimizing-background estimate. Its lower-half proof is II:109918–109975. Its full conclusion concerns a reserve-weight exponent, assumes $x_{K'}\le2X$, and assumes logarithmic upper bounds after splitting off its flat and linear reserves. Those are not the sourced exponent required here. Section 5 ports its lower-half calculation with a smaller, explicit radius valid on the whole interval $(X,x^*]$, including the background theorem's $a_1$ threshold. We do not import its reserve hypotheses.

The new work needed here is the missing offset argument, explicit bounded-window aggregation of the last-scale constants, and a non-circular assembly of the printed parts. Proved CA material is used on its own route. Its upstream open inputs stay open.

## 3. Inputs used at the last lattice

These inputs are from the account, not conclusions inferred from compactness of the coupling interval.

**Flow.** `4.2:lem-first-passage` (I:3636–3721; ported in P1 §2.2), clause (0), and `5.1:thm-correlation-theorem` (II:2791–2966) give the common flow and (1). The coefficient identification is the standing hypothesis at II:63072–63081. It is retained, not proved by comparing two numerical lists.

**Lower density and real background.** We use the lower member of `4.33:thm-stability`, I:157028–157130:
\[
\rho_k^{\rm sf}\,dV\ \ge\ \chi_k\exp[-x_kA(U_k(V))-E_-\mathsf V_k]\,dV,
\quad E_-=C_E+C_{\mathfrak r},\quad
C_E=E_1^\sharp(1-L^{-\beta_T})^{-1}+1 .                    \tag{9}
\]
Here $\rho_k^{\rm sf}$ is the source-free Chapter 4 density, and $\mathsf V_k$ denotes the number of last-lattice sites, not a field coordinate. The constants in (9) are independent of $x_k,k,K$ and the torus. The density theorem retains its positivity, representation, irrelevance and vacuum-energy hypotheses. This note does not prove those hypotheses.

The real-background input is Balaban CMP 102b, Theorem 1, (7)–(8), in the CA form `4.31:eq-standing-inputs-e`, I:154052–154058. In level-$k$ units, $\eta=L^{-k}$. If

\[
\sup_p\|V(\partial p)-1\|<w\le a_1,
\]

then its real minimizing background obeys

\[
\sup_p\|U_k(V,\partial p)-1\|<B_3w\eta^2.                 \tag{10}
\]

The same estimate on each determining box gives the characteristic-function implication of `4.31:lem-window-characteristic`, I:155039–155096:

\[
\sup_p\|V(\partial p)-1\|<w\le a_1,\quad B_3w\le\varepsilon(x_k)
\quad\Longrightarrow\quad\chi_k(V)=1,
\qquad \varepsilon(x)=A_0x^{-1/2}(\log x)^{p_0}.            \tag{11}
\]

Its proof applies (10) to each factor of the actual $\chi_k$, whose threshold is $\varepsilon(x_k)\eta^2$. The determining box contains the tested plaquettes. This is why the estimate concerns the minimizing background and its tests, not just the coarse Wilson action. Both $a_1$ and $B_3\ge1$ are fixed before $g$, independently of the torus. CA uses the operator norm here (I:153575–153583). At $k=0$, use $U_0=V$; the same inequalities hold with $B_3\ge1$.

**Sourced upper majorant.** We port the accounting in `5.12:prf-torus-bound-proof`, II:59645–59821. Its nine hypotheses are the sourced induction format; the sourced and sup-norm versions of Balaban 119 (2.43)–(2.48); complex plaquette-weight control; the per-zone-cell value estimate; the modification estimate on the flat domain class; the live-component gas and polymer bounds; the count of complementary cells; the zero-source floor; and history indexing with its reserved half factors. We replace only the floor hypothesis by the proof in §5. The other eight retain their CA standing.

The upper argument uses no floor. In its notation:

1. Subtract $\mathcal E(z)=\sum_{j,X}[e^{(j)}(X;w)-e^{(j)}(X;0)]$. The missing shares cost $O(1)\sum_j|Z_j|$, paid by the existing history charges (II:59718–59739).
2. The real part of the Wilson term is nonpositive. The extra zone-cell term is at most $2^{-4}(C_\sharp O(1)+1)\log x_j$ per zone cell (II:59741–59764).
3. Below $k=K'$, this joins the already paid logarithmic charges. A live arrested pile is paid in its own large-field region, never the top zone (II:59766–59799).
4. Only the top-zone contribution must remain extensive at the last lattice. The modulus integration and live-component gas sum give the upper bound (II:59801–59813).

To expose all dependence, the source-free part can be read from I:157046–157105 and I:157133–157181. Its summation is

\[
\sum_{\mathcal S}\mathfrak M_k(\mathcal S)e^{q_k(\mathcal S)}
 \le e^{c_M\mathsf V_k},\qquad |\Gamma_k|\le\mathsf V_k,
\]
\[
C_\Gamma(x)=\frac92(\log x+B_\sharp\gamma^2)+C_{\mathfrak r},
\qquad E_+(x)=C_\Gamma(x)+C_{\rm maj}+c_M.                  \tag{12}
\]

The coefficient $9/2$ is the SU(2) value of $\frac32\dim SU(N)$. The letter $B_\sharp$ in (12) is the vacuum-energy constant used in I:157049, distinct from the first-passage constant $B^\sharp$.

The comparison constant introduces no hidden last-scale dependence: II:7992–8073 defines $C_\sharp$ uniformly over the admitted reference sequences and bounds it by the fixed number $\bar C_\sharp$ before the coupling ceiling is chosen. The per-cell calculation II:14644–14772 bounds the current chain's contribution by $C_\sharp[\mathsf K_{\rm cell}^0+3(\mathsf N_0(\log x_j)+3)C_0^\sharp]$. Its admitted volume ceiling gives the logarithmic bound used in item 2 above. Its live arrested terms are expressly excluded from that top-cell charge and are paid separately, as in item 3.

Here is the corresponding sourced summation, with the payments exposed. After subtracting $\mathcal E$, apply the eight retained upper-bound hypotheses to each history $h$ at level $k=K'$. Write $\mathfrak M^J_k(h)$ for its paid modulus majorant, including the non-top logarithmic charges and the live arrested piles. The sourced versions of the bounds used in (12) replace its fixed coefficients by fixed coefficients $a_\Gamma,b_\Gamma\ge0$. The additional top coefficient is $c_{\rm top}=2^{-4}(C_\sharp C_{\rm zone}+1)$, with the fixed geometric counting factor included in $C_{\rm zone}$ if necessary. Thus the modulus integration and gas sum of II:59801–59813 have the form

\[
\begin{split}
\left|\int\tau^J_h(z)\right|
&\le \mathfrak M^J_k(h)
 \exp\{[a_\Gamma+(b_\Gamma+c_{\rm top})\log x]\mathsf V_k\},\\
\sum_h\mathfrak M^J_k(h)&\le \exp(c_{\rm gas}\mathsf V_k).
\end{split}                                                   \tag{12a}
\]

Here $\tau^J_h$ is the history term after the subtraction. The first inequality is the same separation into top and non-top terms as (12): $|\Gamma_k|\le\mathsf V_k$, while every lower-zone charge is included in the paid majorant. The second inequality is exactly where the retained live-gas and history-count hypotheses are used. In particular, the gas term $e^{-p_0(g_k)}|\mathbb L_k|$ is at most $\mathsf V_k$; the history-label payments change its coefficient by fixed $(d,L)$-numbers. The missing shares and live piles have already been paid before this summation. There is no sum of unpaid charges over levels.

Consequently, with $A_J=a_\Gamma+c_{\rm gas}$ and $B_J=b_\Gamma+c_{\rm top}$, a valid sourced exponent satisfies

\[
E_+^\sharp(x)\le A_J+B_J\log x\quad\text{at admitted last-scale couplings}.                \tag{13}
\]

The constants $a_\Gamma,b_\Gamma,c_{\rm gas}$ are the fixed source-budget replacements and history payments just described; they depend on the admitted construction and source radius. They contain neither $N_T$ nor the number of levels. Equation (12a) ports the upper accounting of the cited proof; it does not assume its final last-scale-uniformity clause. No supremum over an unspecified function of $x$ is being assumed.

This also clarifies II:63531–63565. The single *additional* member is the top-zone logarithm; the original Balaban constants already contain a logarithm, as II:59766–59769 states. All logarithmic members can be collected into one dominating term of the displayed $2^{-4}(C_\sharp O(1)+1)\log x$ form by enlarging its fixed constant. The consumers need the resulting upper bound, not a unique decomposition of the exponent.

**Normalization.** Equations (9), (12), (13) use the common vacuum normalization of the construction. If $\widetilde Z$ is multiplied by $e^{-h}$, replace $E_+^\sharp$ by $E_+^\sharp-h/\mathsf V_k$ and $C_{\rm low}$ by $C_{\rm low}+h/\mathsf V_k$. Their sum and every normalized source bound are unchanged. Thus the additive bare constant $E$ of II:730–739 is harmless. One must not combine an upper bound in one normalization with a lower bound in another.

Choose that $E$ to be the vacuum constant of the source-free run. By (15) below the two bare integrals agree at zero source. Since $K'\le K$, equality of source-free integrals, I:157110, with its stated hypotheses, identifies this bare integral with $\int\rho_{K'}^{\rm sf}\,dV$. This suffices to use (9). We do not need to identify the sourced flat-history density with the Chapter 4 density pointwise.

## 4. The offset, floors and lattice identification

**Existence of the floor in (2).** This ports II:62887–62983. Set $D_g=X+b_++4c_2+3\lambda+e$. For $m,u\ge0$,

\[
X+b_++4c_2+3\lambda(m+u)\le D_g(1+m)(1+u).
\]

Also $R_J(x)\le L\max\{1,(\log x)^r\}$. Taking logarithms in the preceding inequality bounds the logarithm of its left side by a fixed multiple, depending on $g$, of $\log(2+m)\log(2+u)$. Indeed, each of $\log D_g,\log(1+m),\log(1+u)$ is at most

\[
(\log2)^{-2}\log D_g\log(2+m)\log(2+u).
\]

Therefore

\[
N_{\mathbb T}(g,m)\le C(g)(\log(2+m))^r
 \sup_{u\ge0}L^{-u}(\log(2+u))^r<\infty.                 \tag{14}
\]

The ratio of consecutive terms in the last supremum tends to $L^{-1}<1$. Choose any fixed number strictly between $L^{-1}$ and one. Beyond a finite index it bounds the ratio, so a geometric sequence bounds the tail. This proves finiteness and decay without evaluation. The same ratio argument shows that $L^m/(\log(2+m))^r\to\infty$. Hence (2) has an admissible integer $m$, and a least one.

The terms in its defining supremum have the form $L^v$, $v\in\mathbb Z$, and tend to zero. Only finitely many are at least the positive $u=0$ term. Their maximum attains the supremum. Keeping that term gives

\[
L^{m_J}\ge L^{11}M R_J(X),
\]

since $b_+,c_2,\lambda\ge0$. Thus $m_J\to\infty$ as $g\downarrow0$. The physical floor also diverges, since $g_-\downarrow0$. The finite set $\mathcal A$ is fixed before $g$. The definition of a limit therefore supplies $\gamma_D>0$ making both floors at least $a^\natural$ for *every* $g\le\gamma_D$. Monotonicity of $m_J(g)$ is not needed.

**Part (a).** Clause (0) and equality of the two recursions give $x_j>X$ for every $j\le K$. The definition of $K_J$ implies $K\le K_J$. If $a=0$, (3) applies. If $a>0$, apply (1) at $i=K,j=K_J$:

\[
\lambda a-c_5\le x_K-x_{K_J}<(X+B^\sharp)-X=B^\sharp.
\]

Hence $\lambda a<B^\sharp+c_5$, which proves (a), including its strict inequality. No sign for individual increments was used.

**Part (b), identification.** The floors give $m_1\ge a$ and $m_J\ge a$. Thus $N_T=2L^{m_1-a}$ is a positive integer and $b=m_J-a\ge0$. In Case A, $K'=K_J-m_J\ge0$. Moreover

\[
L^{K_J}N_T=2L^{m_1+K},\qquad
2L^{m_1}\frac{L^{j-K_J}}{N_T}=L^{j-K}.                    \tag{15}
\]

The first equality matches the bare lattice. The second matches every later spacing. At $j=K'$ it gives $L^{-b}$. The correlation floor is satisfied by (2); all its other numerical hypotheses have been retained.

For $\widetilde f(y)=f(2L^{m_1}y)$,

\[
\|\widetilde f\|^J_\sharp
=\max\{\|f\|_\infty,40ML^{-b}\operatorname{Lip}f\}
\le\|f\|_\sharp .                                       \tag{16}
\]

Dilation preserves the finite bond-indexed Haar product and plaquette products. It also preserves each source value at the corresponding barycentre. Thus

\[
A(x_0-\textstyle\sum_i z_i\widetilde f_i,U)
=x_0A(U)-\sum_i z_i\mathcal O(f_i).
\]

The two partition functions differ only by the source-independent factor $e^{-E}$. Near zero their logarithms differ by a constant, so all positive-order cumulants agree. There is no field rescaling or Jacobian factor in this relabelling of bond variables.

Finally, $x_{K'}>X$. If $m_J>0$, (1) gives

\[
x_{K'}\le x_{K_J}+3\lambda m_J+2c_2\le x^*(g).
\]

For $m_J=0$, use $x_{K'}=x_{K_J}\le X+b_+\le x^*(g)$. This proves the coupling part of (5).

## 5. Explicit uniform last-scale exponents

Set $\mathsf V=N^4$, $x=x_{K'}\in(X,x^*]$, and $\eta=L^{-K'}$. We port the lower-half argument of II:109918–109975, using one radius for the whole bounded interval. At fixed $g$, define

\[
\varepsilon_*(g)=A_0(x^*)^{-1/2}(\log X)^{p_0}>0,
\quad
s_*(g)=\min\left\{\frac12,\frac{a_1}{8},
 \frac{\varepsilon_*}{8B_3},\frac{1}{8B_3\sqrt{x^*}}\right\}>0. \tag{17}
\]

All logarithms are positive since $X>1$. Since $p_0\ge0$, $\varepsilon(x)\ge\varepsilon_*$ throughout the interval. These definitions are made after $g$; they impose no new condition on an earlier construction constant.

Restrict the last block field to $\mathcal B=\{V:\|V_b-1\|<s_*\text{ for every independent bond }b\}$. A product of four unitary matrices satisfies

\[
\|V_1V_2V_3V_4-1\|\le\sum_{j=1}^4\|V_j-1\|<4s_*.
\]

This follows by telescoping the product and using that multiplication by a unitary preserves the operator norm. An inverse bond has the same distance from one. Consequently (10) and (11), with $w=4s_*$, imply

\[
\chi_{K'}=1\text{ on }\mathcal B,\qquad
\|U_{K'}(\partial p)-1\|<4B_3s_*\eta^2.                  \tag{18}
\]

The thresholds have a factor-two margin: $4s_*\le a_1/2$ and $4B_3s_*\le\varepsilon_*/2$. This uses the account's actual small-field test, not an assumption that its history tests are empty.

For $W\in SU(2)$, its eigenvalues are $e^{\pm i\theta}$. Thus

\[
1-\operatorname{Re}\operatorname{tr}W
=1-\cos\theta=\tfrac12\|W-1\|^2.
\]

There are exactly $6\mathsf V\eta^{-4}$ fine plaquettes. Combining this count with (18) gives

\[
A(U_{K'}(V))\le48B_3^2s_*^2\mathsf V,
\qquad xA(U_{K'}(V))\le\tfrac34\mathsf V.                       \tag{19}
\]

The powers $\eta^4$ and $\eta^{-4}$ cancel. This is the dimensional step in the floor argument. It is the curvature estimate for the minimizing background in (10) that permits it.

For normalized SU(2) Haar measure and $0<s\le1$,

\[
\operatorname{Haar}\{W:\|W-1\|<s\}\ge c_Hs^3,
\qquad c_H=\frac{8}{3\pi^3}.                             \tag{20}
\]

Here is the hand calculation, following SA:23504–23513. Parametrize $W=\cos\theta\,1+i\sin\theta\,n\cdot\sigma$, $n\in S^2$. Haar measure is normalized spherical volume on $S^3$, with density $(2\pi^2)^{-1}\sin^2\theta\,d\theta\,d\Omega$. Left multiplication is an orthogonal transformation of unit quaternions, so this probability is Haar. The interval $0<\theta<s$ lies in the operator ball, since $2\sin(\theta/2)\le\theta$. Concavity of sine on $[0,\pi/2]$ gives $\sin\theta\ge2\theta/\pi$ for $0\le\theta\le1$. Integrating and using $|S^2|=4\pi$ yields (20). Endpoints have measure zero.

There are $4\mathsf V$ independent last-lattice bonds. Integrate (9) over $\mathcal B$, use (19), and multiply their independent Haar masses:

\[
\begin{split}
\widetilde Z(0)=Z(0)=\int\rho_{K'}^{\rm sf}\,dV
&\ge e^{-(E_-+3/4)\mathsf V}(c_Hs_*^3)^{4\mathsf V}\\
&=e^{-C_{\rm low}^*(g)\mathsf V},\\
C_{\rm low}^*(g)&=E_-+\frac34+4\log(c_H^{-1})+12\log(s_*^{-1}).
\end{split}                                                \tag{21}
\]

The first equality uses $\mathcal E(0)=0$. The second is the common bare integral and source-free integral identity explained in §3; the sourced integral identity is also the correlation theorem's clause (iii). For $K'=0$, use $U_0=V$ in (9); this is the direct Wilson estimate with the same vacuum factor. Every constant in (21) is independent of $K,g_0,m_1,N_T,a$.

The account's more specific dependence on the single last-scale coupling can also be retained. For any admitted $x$, use

\[
s(x)=\min\left\{\frac12,\frac{a_1}{8},
\frac{\varepsilon(x)}{8B_3},\frac{1}{8B_3\sqrt x}\right\},\qquad
C_{\rm low}(x)=E_-+\frac34+4\log(c_H^{-1})+12\log(s(x)^{-1}).
\]

The preceding integral proof works with $s(x)$ at that coupling. Moreover $s(x)\ge s_*$ for $X<x\le x^*$, by the componentwise bounds used in (17). Hence $C_{\rm low}(x)\le C_{\rm low}^*$. This produces an actual single-coupling floor function and proves its boundedness on the required interval.

For the upper bound, insert $x\le x^*$ into (13):

\[
|\widetilde Z(z)|\le e^{C_+^*(g,\varrho)\mathsf V},\qquad
C_+^*(g,\varrho)=A_J+B_J\log x^* .                        \tag{22}
\]

The source radius and norm are those already admitted by the correlation theorem. The same estimate applies to the transported and periodized source lists used by Chapter 6; their admissibility is its periodized-weight lemma, not a new analytic continuation here.

We may therefore choose the common dominating exponent

\[
\boxed{E_*=A_J+B_J\log x^*+E_-+\frac34+
4\log(c_H^{-1})+12\log(s_*^{-1}).}                        \tag{23}
\]

This proves the second assertion of (5). Constants in upper bounds can be enlarged to (21)–(22). Thus this proves existence of the constants that the consumers require, rather than bounding arbitrary unnecessarily large choices of them. The proof did not assume that an arbitrary function of a bounded coupling is bounded. Its only coupling functions are displayed in (17), (21), (22).

## 6. The printed conclusions and their consumers

### 6.1 The per-ball deduction with a symbolic exponent

There is an apparent circle if part (c) cites the *uniformity conclusion* of the per-ball theorem. The actual proof has no circle. First retain
$t=E_+^\sharp+C_{\rm low}$ as a numerical parameter throughout the proof of 6.4. Only its final paragraph invokes LSC.

Here are the exact ingredients of that proof. They are ported from II:63964–64285, with their retained antecedents:

- The placement lemma, II:61417–61432, places each ball a distance at least $R+2$ from cell faces using a lattice translation.
- The periodized-weight lemma, II:61517–61565, supplies the admissible copied source lists and the chessboard identity. Choose the account's reading $\mathfrak r=2$ for the literal finite-source polydisc; $\mathfrak r=1$ is also available under its class reading.
- Locality, analyticity and the term bound are II:60715–60731. They are independent of last-scale normalization.
- The ultraviolet and face estimates, II:62127–62157 and 62293–62314, hold for arbitrary relevant subfamilies. Their constants are

\[
\begin{split}
C_{\rm UV}(d;R)&=C_eC_{(1.26)}
\sum_{i\ge0}\mathfrak a(R,i)e^{-c_\kappa[dL^i/(4M)-4]_+},\\
C_{\rm face}(R)&=C_eC_{(1.26)}
\sum_{i\ge0}\mathfrak a(R,i)e^{-c_\kappa[RL^i/(4M)-3]_+},\\
\mathfrak a(R,i)&=\left(2(R+2)L^i/M+6\right)^4 .
\end{split}                                                    \tag{24}
\]

The tree estimate underlying (24) is Balaban 116 (1.26), in the form of II:62030–62067. It is a retained input here. Each series is finite: beyond a fixed index, its terms are bounded by $C L^{4i}e^{-cL^i}$ for positive fixed $C,c$. The ratio of this majorant at $i+1$ and $i$ is $L^4e^{-c(L-1)L^i}$, eventually at most $1/2$. This is an existence estimate, not a computation. The first series is non-increasing in $d$.

Let $\mathcal C$ be the cells and $q\le n$ the occupied-cell count. Use the account's counterterm $\mathcal E''$: the average of each occupied cell's transported bulk energies, with outer conjugation on odd reflections, plus the original face energy. For holomorphic $\Phi$, the function $z\mapsto\overline{\Phi(\bar z)}$ is holomorphic. Locality and $\mathcal E(0)=0$ give $\mathcal E''(0)=0$.

If at least two cells are occupied, every bulk summand omits one of the $n$ variables. Its full mixed derivative vanishes. If one cell is occupied, its transported bulk terms have the original support radii and separations. Apply the ultraviolet estimate to each, then take their average. Apply it once more to the face subfamily. Hence

\[
|\partial_1\cdots\partial_n\mathcal E''(0)|
\le2C_{\rm UV}(d;R)(n/\varrho)^n\prod_i\|f_i\|_\sharp.       \tag{25}
\]

The original bare integral makes $Z(z)$ entire, by compactness of the finite product of bond groups and linearity of the source exponent. Thus $h''=e^{-\mathcal E''}Z/Z(0)$ is holomorphic on the admitted ball. The chessboard estimate at a copied source, followed by the upper bound and floor, gives a cost $tN^4/|\mathcal C|=t\ell^4$ per occupied cell. In the real part of $\mathcal E''$, the bulk terms are exactly those copied bulk terms. They cancel, term by term. The two face contributions cost at most $2nC_{\rm face}(R)$ by (24). Thus

\[
|h''|\le\exp\{n[t\ell^4+2C_{\rm face}(R)]\}=Q,\qquad h''(0)=1. \tag{26}
\]

Here $t\ge0$, since the upper and lower bounds hold at zero, so $Q\ge1$. All of (25)–(26) holds before any assertion that $t$ is uniform.

For completeness, the account's final analytic step is elementary. On the source ball
$\rho(z)=\varrho^{-1}\sum_i|z_i|\|f_i\|_\sharp<1/\mathfrak r$, apply Schwarz's lemma on the complex line through $z$ to $(h''-1)/(Q+1)$. It gives
$|h''(z)-1|\le(Q+1)\mathfrak r\rho(z)$. On the smaller ball
$\rho<1/[2\mathfrak r(Q+1)]$, the logarithm has modulus at most
$\sum_{j\ge1}2^{-j}/j=\log2$. Cauchy's formula on coordinate circles approaching radii
$\varrho/[2n\mathfrak r(Q+1)\|f_i\|_\sharp]$ gives

\[
|\partial_1\cdots\partial_n\log h''(0)|
\le(\log2)(2Q+2)^n\mathfrak r^n(n/\varrho)^n\prod_i\|f_i\|_\sharp .
\]

If a source norm is zero, that source is zero and the mixed cumulant vanishes; no division is then needed. Adding (25) proves (7), with $t$ still symbolic. This reproduces the CA route. It assumes neither a zero-free original source ball nor an independent cell-covariance assertion.

### 6.2 Part (c): transport and maximum

In Case A, the last-lattice radius is $RL^b$ and its separation is $dL^b$. Equation (16) controls its source norms. Since $L^b\ge1$,

\[
8n(RL^b+1)\le L^b\,8n(R+1)\le L^b\ell(n,R).
\]

The last quantity is a power of $L$. By minimality,

\[
\ell(n,RL^b)\le L^b\ell(n,R)\le L^{m_J}\ell(n,R)\le L^{m_1}. \tag{27}
\]

Thus the printed floor suffices for every possible $b$. The raw deduction above gives
$\Phi_{n,dL^b,RL^b}(t)$. The map $t\mapsto\Phi_{n,d',R'}(t)$ is non-decreasing, since every coefficient is nonnegative. Replace $t$ by (23), then maximize over the finite set $\mathcal B(g)$. This proves (6). Only $C_{\rm UV}$ depends on $d$, and it is non-increasing. A finite maximum preserves that property.

### 6.3 Parts (d) and (e)

In Case B, part (a) gives $0\le K\le K_J<m_J$. Let $\epsilon=L^{-K}\le1$. A plaquette whose barycentre lies in a radius-$R$ ball has its base site within sup-distance $R+\epsilon$ of the ball's centre. On each coordinate circle there are at most $2R/\epsilon+3$ such sites. This remains an upper bound when the interval covers the circle: then count all sites, which is no larger. There are six direction pairs. Hence

\[
\#\{p:x(p)\in\operatorname{supp}f_i\}
\le6(2R+3)^4L^{4K}\le6(2R+3)^4L^{4m_J}=:P_R.
\]

Since $0\le a_p\le2$, $|\mathcal O(f_i)|\le2P_R\|f_i\|_\infty$.
For bounded random variables $Y_i$, expanding $\log\langle e^{\sum z_iY_i}\rangle$ at zero gives

\[
\kappa(Y_1,\ldots,Y_n)=
\sum_{\pi\in\operatorname{Part}(n)}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}\left\langle\prod_{i\in B}Y_i\right\rangle .
\]

Indeed, the term with $j$ factors of the nonconstant part of the moment generating function orders the $j$ nonempty blocks in $j!$ ways. Its logarithmic coefficient is $(-1)^{j-1}/j$, leaving $(-1)^{j-1}(j-1)!$. This finite coefficient identity is not a computer enumeration. Each moment product is at most $\prod_i\|Y_i\|_\infty$. The displayed local count therefore proves (8). No total-torus plaquette count occurs.

For part (e), the first-passage bound from P1 gives

\[
K(g_0,g)\ge\frac{g_0^{-2}-X}{B^\sharp}-1\longrightarrow\infty .
\]

Part (a) implies $K_J\ge K$, so Case A eventually holds. An infinite sequence taking values in a finite set has an infinite constant subsequence: otherwise it is a finite union of finite sets. Apply this to $a\in\mathcal A$. At fixed $g,m_1$, (4) then fixes $N_T,m_J,N,b$, while $K_J\to\infty$. These are precisely the fixed-data hypotheses of the correlation theorem's subsequential-limit clause. Its conclusions apply. The bounds need no such extraction, since all possible $a$ were already covered.

### 6.4 The original torus floor of (iii-b)

Part (c) follows the stronger printed floor at II:63275–63280. The principal statement (I:2610–2620) asks only

\[
m_1\ge m_{\mathbb T}(g_-),\qquad L^{m_1}\ge\ell(n,R).
\]

We must not silently replace this by the stronger floor. The remaining physical torus exponents form a finite set depending only on the fixed data, $n,R$. They are covered by the original torus bound.

Set

\[
J=\max\{m_{\mathbb T}(g_-),\,m_J+\log_L\ell(n,R)\},\qquad
N_{\max}=2L^{J+m_J},\qquad \Delta=d/(2L^J).
\]

For $m_1\ge J$, parts (c) and (d) apply. For $m_1<J$ in Case A, (4) gives $N\le N_{\max}$. On the side-one torus the source separation is at least $d/(2L^{m_1})\ge\Delta$. The norm is bounded by (16). Clause (iv) of the correlation theorem, II:2937–2959, therefore yields

\[
|S^T_n(\vec f)|\le C^{\rm bd}_n(d;R)\prod_i\|f_i\|_\sharp,
\]
\[
C^{\rm bd}_n(d;R)=
\left[
C\,\Delta^{-4}(1+\log^+\Delta^{-1})
+(\log2)\left(2e^{E_*N_{\max}^4}+2\right)^n
\right](n/\varrho)^n .                                    \tag{28}
\]

Here $C$ is that theorem's ultraviolet constant, already fixed independently of cutoff and torus. We used its displayed decreasing majorant, so (28) is non-increasing in $d$. If a nonzero separated tuple cannot fit on a small torus, there is simply no such tuple; the estimate still applies to every tuple that does fit. Case B is covered by (8). Consequently

\[
C^\infty_n(d;R)=
\max\{C^*_n(d;R),\,C^B_n(R),\,C^{\rm bd}_n(d;R)\}             \tag{29}
\]

proves the consumer's bound with its original floor. This finite-torus completion uses the already established (5) and the torus theorem, not (iii-b) itself. The simpler constant $\max(C^*_n,C^B_n)$ suffices under part (c)'s printed floor.

## 7. Constant order, scope and source checks

The account's early order is unchanged: its Stage-0 exponents; $L$ and the ensuing operator/geometry constants; decay rates and widths; $M_1,M$; the remaining activity, radius and extraction constants; then the coupling ceilings. See I:1331–1685 and II:2412–2438. In the correlation construction the source radius is fixed before its final coupling ceiling (II:2858–2867). None of our choices changes an earlier ceiling.

After those choices, fix the target $g$. Equations (2), (3) then determine $m_J,\mathcal A$; the set $\mathcal A$ itself was fixed before $g$. Equation (5) determines $x^*$; (17) determines a radius used only to restrict an integral; (21)–(23) determine the exponents. After choosing $n,R,d$, choose the cell length and the physical torus floor, then vary $m_1,g_0$ and the source positions. No estimate selects $L,M,\kappa,\gamma$ from $m_1,K,g_0$ or from the integration radius.

Three distinctions matter.

1. Uniformity is in the physical torus exponent $m_1$. The omitted-step exponent is fixed as $m_J(g)$. No assertion of boundedness as an independently varying omitted-step exponent tends to infinity is needed.
2. Bounds (9)–(13) retain their construction hypotheses. The proof adds no proof of positivity dichotomy, the sourced induction, polydisc holomorphy, or Balaban's real-background theorem. Those are upstream inputs of the same account.
3. The result gives the per-order bound (29). It does not give the factorial growth, clustering, or higher-point rotational conclusions required elsewhere for T0.

The source was fetched at the specified revision and read in bounded excerpts. All occurrences of the LSC label in CA-I/II/III were searched. Its actual references are in CA-II; the assembly in CA-III names it in prose. The pre-statement definitions, all printed proof parts, the corollary, the constants remarks, the small-cutoff remarks, and the named limit consumer were read. The source supplies no statement or marked step to quote beyond the unwritten-statement remark. This note reconstructs the obligation from those consumers.

Additional source reconciliation:

- II:64268–64273 uses an unqualified statement about independence of the torus index. Equations (4)–(5) give the precise reading with two distinct exponents.
- II:64468–64471 describes part (d) as counting the entire torus. This is stale relative to II:63713–63796, which explicitly counts only the support ball. We port the actual local proof.
- The stronger floor in the printed unit-rescaling proof is handled explicitly by §6.4. It is not an unmentioned weakening of (iii-b).

Only this note is changed. Shell and text-processing tools were used to retrieve, locate, read and write text. No run, numerical value, enumeration or formal-verification output is a proof step. Author check only; not yet checked by another model.

## Result

**Proof**

Lemma LSC (a)–(e) holds as an implication from the unchanged CA flow, density, real-background and sourced-construction inputs specified above. In particular, at the fixed omitted-step exponent $m_J(g)$, (23) bounds $E_+^\sharp+C_{\rm low}$ uniformly in $K,g_0,m_1,a,N_T$ and positions. The constant (29) gives the per-ball bound with the original torus floor of CA clause (iii-b).

This completes the missing LSC implication on the account's route. The proof supplies the absent offset argument, a uniform small-field integral floor, the last-scale constant aggregation, and the finite-torus completion. It ports the printed unit-rescaling, plaquette-count and subsequence arguments with their hypotheses intact. It is a proof of a step left incomplete, not an audit or a proof of the upstream RG construction or of T0.
